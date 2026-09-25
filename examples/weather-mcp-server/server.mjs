#!/usr/bin/env node
/**
 * ☔ Weather Buddy: a publishable MCP server with real data (free Open-Meteo API, no key needed).
 *
 * Tools:
 *   get_current_weather   right-now conditions for any city
 *   get_forecast          a 1–7 day forecast with highs, lows and rain chance
 *   packing_advice        what to wear or pack, based on the forecast
 *
 * Runs two ways:
 *   node server.mjs                 local (stdio): for Claude Desktop, Claude Code, Cursor…
 *   node server.mjs --http          remote (Streamable HTTP on PORT, default 3000): for hosting
 *
 * Environment (optional):
 *   PORT                       HTTP port for --http mode
 *   MCP_AUTH_TOKEN             if set, --http mode requires "Authorization: Bearer <token>"
 *   OPEN_METEO_GEOCODING_URL   override the geocoding API (used by the tests)
 *   OPEN_METEO_FORECAST_URL    override the forecast API (used by the tests)
 */
import { createServer } from "node:http";
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { z } from "zod";

const GEOCODING_URL = process.env.OPEN_METEO_GEOCODING_URL ?? "https://geocoding-api.open-meteo.com/v1/search";
const FORECAST_URL = process.env.OPEN_METEO_FORECAST_URL ?? "https://api.open-meteo.com/v1/forecast";

// WMO weather codes → friendly words and emoji (https://open-meteo.com/en/docs)
const WEATHER_CODES = {
  0: ["clear sky", "☀️"], 1: ["mainly clear", "🌤️"], 2: ["partly cloudy", "⛅"], 3: ["overcast", "☁️"],
  45: ["fog", "🌫️"], 48: ["freezing fog", "🌫️"],
  51: ["light drizzle", "🌦️"], 53: ["drizzle", "🌦️"], 55: ["heavy drizzle", "🌧️"],
  61: ["light rain", "🌦️"], 63: ["rain", "🌧️"], 65: ["heavy rain", "🌧️"],
  66: ["freezing rain", "🌧️"], 67: ["heavy freezing rain", "🌧️"],
  71: ["light snow", "🌨️"], 73: ["snow", "🌨️"], 75: ["heavy snow", "❄️"], 77: ["snow grains", "🌨️"],
  80: ["rain showers", "🌦️"], 81: ["heavy showers", "🌧️"], 82: ["violent showers", "⛈️"],
  85: ["snow showers", "🌨️"], 86: ["heavy snow showers", "❄️"],
  95: ["thunderstorm", "⛈️"], 96: ["thunderstorm with hail", "⛈️"], 99: ["thunderstorm with heavy hail", "⛈️"],
};
const describe = (code) => WEATHER_CODES[code] ?? ["unknown conditions", "🌈"];
const text = (t) => ({ content: [{ type: "text", text: t }] });

async function getJson(url) {
  const res = await fetch(url, { headers: { "User-Agent": "weather-buddy-mcp/1.0" } });
  if (!res.ok) throw new Error(`Weather service returned HTTP ${res.status}`);
  return res.json();
}

/** Find a place by name. Returns null if nothing matches. */
async function geocode(city) {
  const url = `${GEOCODING_URL}?${new URLSearchParams({ name: city, count: "1", language: "en", format: "json" })}`;
  const data = await getJson(url);
  const place = data.results?.[0];
  if (!place) return null;
  const where = [place.name, place.admin1, place.country].filter(Boolean).join(", ");
  return { name: where, latitude: place.latitude, longitude: place.longitude };
}

async function forecast(place, days) {
  const params = new URLSearchParams({
    latitude: String(place.latitude),
    longitude: String(place.longitude),
    current: "temperature_2m,apparent_temperature,weather_code,wind_speed_10m",
    daily: "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max",
    timezone: "auto",
    forecast_days: String(days),
  });
  return getJson(`${FORECAST_URL}?${params}`);
}

/** Shared lookup with friendly errors, so tools never crash the conversation. */
async function lookup(city, days = 1) {
  const place = await geocode(city);
  if (!place) return { error: `I couldn't find a place called "${city}". Try adding the country, e.g. "Paris, France".` };
  return { place, data: await forecast(place, days) };
}

function formatDays(daily) {
  return daily.time.map((date, i) => {
    const [words, emoji] = describe(daily.weather_code[i]);
    const hi = Math.round(daily.temperature_2m_max[i]);
    const lo = Math.round(daily.temperature_2m_min[i]);
    const rain = daily.precipitation_probability_max?.[i];
    return `${date}  ${emoji} ${words}, ${lo}–${hi}°C${rain == null ? "" : `, ${rain}% chance of rain`}`;
  });
}

function buildServer() {
  const server = new McpServer(
    { name: "weather-buddy", version: "1.0.0" },
    { instructions: "Weather lookups for any city worldwide. Temperatures are in °C. Use get_forecast for plans beyond today." },
  );

  server.registerTool(
    "get_current_weather",
    {
      title: "Current weather",
      description: "Get the current weather for a city, e.g. 'Lisbon' or 'Springfield, Illinois'.",
      inputSchema: { city: z.string().min(1).describe("City name, optionally with region or country") },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async ({ city }) => {
      try {
        const result = await lookup(city);
        if (result.error) return text(result.error);
        const c = result.data.current;
        const [words, emoji] = describe(c.weather_code);
        return text(
          `${emoji} ${result.place.name}: ${words}, ${Math.round(c.temperature_2m)}°C ` +
            `(feels like ${Math.round(c.apparent_temperature)}°C), wind ${Math.round(c.wind_speed_10m)} km/h.`,
        );
      } catch (err) {
        return { ...text(`The weather service is having a moment: ${err.message}. Try again shortly.`), isError: true };
      }
    },
  );

  server.registerTool(
    "get_forecast",
    {
      title: "Forecast",
      description: "Get a daily forecast (1–7 days) for a city: conditions, high/low temperatures and chance of rain.",
      inputSchema: {
        city: z.string().min(1).describe("City name, optionally with region or country"),
        days: z.number().int().min(1).max(7).default(3).describe("Number of days, 1 to 7"),
      },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async ({ city, days }) => {
      try {
        const result = await lookup(city, days);
        if (result.error) return text(result.error);
        return text(`📅 ${days}-day forecast for ${result.place.name}:\n${formatDays(result.data.daily).join("\n")}`);
      } catch (err) {
        return { ...text(`The weather service is having a moment: ${err.message}. Try again shortly.`), isError: true };
      }
    },
  );

  server.registerTool(
    "packing_advice",
    {
      title: "Packing advice",
      description: "Suggest what to wear or pack for a trip, based on the forecast for the next few days.",
      inputSchema: {
        city: z.string().min(1),
        days: z.number().int().min(1).max(7).default(3),
      },
      annotations: { readOnlyHint: true, openWorldHint: true },
    },
    async ({ city, days }) => {
      try {
        const result = await lookup(city, days);
        if (result.error) return text(result.error);
        const d = result.data.daily;
        const low = Math.min(...d.temperature_2m_min);
        const high = Math.max(...d.temperature_2m_max);
        const rainy = (d.precipitation_probability_max ?? []).some((p) => p >= 40);
        const snowy = d.weather_code.some((code) => code >= 71 && code <= 86);
        const tips = [];
        if (low < 5) tips.push("🧥 a warm coat, hat and gloves");
        else if (low < 13) tips.push("🧶 a sweater or light jacket for the evenings");
        if (high >= 25) tips.push("🕶️ sunglasses, sunscreen and breathable clothes");
        if (rainy) tips.push("☂️ an umbrella or rain jacket");
        if (snowy) tips.push("🥾 waterproof boots");
        if (!tips.length) tips.push("👕 comfy layers: it looks mild");
        return text(`🧳 For ${result.place.name} (${Math.round(low)}–${Math.round(high)}°C over ${days} days), pack:\n- ${tips.join("\n- ")}`);
      } catch (err) {
        return { ...text(`The weather service is having a moment: ${err.message}. Try again shortly.`), isError: true };
      }
    },
  );

  return server;
}

async function startHttp() {
  const port = Number(process.env.PORT ?? 3000);
  const token = process.env.MCP_AUTH_TOKEN;

  const http = createServer(async (req, res) => {
    if (req.url === "/health") {
      res.writeHead(200, { "Content-Type": "application/json" }).end('{"ok":true}');
      return;
    }
    if (!req.url?.startsWith("/mcp")) {
      res.writeHead(404).end("Not found. The MCP endpoint is /mcp");
      return;
    }
    if (token && req.headers.authorization !== `Bearer ${token}`) {
      res.writeHead(401, { "Content-Type": "application/json" }).end('{"error":"unauthorized"}');
      return;
    }
    if (req.method !== "POST") {
      // Stateless servers don't offer a standalone SSE stream or sessions.
      res.writeHead(405, { Allow: "POST" }).end();
      return;
    }
    try {
      let body = "";
      for await (const chunk of req) body += chunk;
      // Stateless mode: a fresh server + transport per request. Simple, and it scales horizontally.
      const server = buildServer();
      const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined, enableJsonResponse: true });
      res.on("close", () => {
        transport.close();
        server.close();
      });
      await server.connect(transport);
      await transport.handleRequest(req, res, body ? JSON.parse(body) : undefined);
    } catch (err) {
      if (!res.headersSent) res.writeHead(400, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ jsonrpc: "2.0", error: { code: -32700, message: String(err.message ?? err) }, id: null }));
    }
  });

  http.listen(port, () => console.error(`☔ Weather Buddy MCP listening on http://localhost:${port}/mcp`));
}

if (process.argv.includes("--http")) {
  await startHttp();
} else {
  await buildServer().connect(new StdioServerTransport());
}
