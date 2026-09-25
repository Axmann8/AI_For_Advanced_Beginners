/**
 * Smoke test (offline): a fake Open-Meteo API + the server in both stdio and HTTP modes.   npm test
 */
import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { createServer } from "node:http";
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";
import { StreamableHTTPClientTransport } from "@modelcontextprotocol/sdk/client/streamableHttp.js";

// 1) A tiny fake weather API so the test never needs the internet.
const fake = createServer((req, res) => {
  const url = new URL(req.url, "http://localhost");
  res.setHeader("Content-Type", "application/json");
  if (url.pathname === "/geo") {
    const results = url.searchParams.get("name") === "Nowhereville" ? [] : [
      { name: "Lisbon", admin1: "Lisbon", country: "Portugal", latitude: 38.72, longitude: -9.14 },
    ];
    return res.end(JSON.stringify({ results }));
  }
  const days = Number(url.searchParams.get("forecast_days") ?? 1);
  res.end(JSON.stringify({
    current: { temperature_2m: 21.4, apparent_temperature: 20.9, weather_code: 2, wind_speed_10m: 14.2 },
    daily: {
      time: Array.from({ length: days }, (_, i) => `2026-09-${String(25 + i).padStart(2, "0")}`),
      weather_code: Array.from({ length: days }, (_, i) => (i === 1 ? 63 : 1)),
      temperature_2m_max: Array.from({ length: days }, () => 26),
      temperature_2m_min: Array.from({ length: days }, () => 12),
      precipitation_probability_max: Array.from({ length: days }, (_, i) => (i === 1 ? 70 : 5)),
    },
  }));
});
await new Promise((resolve) => fake.listen(0, resolve));
const base = `http://127.0.0.1:${fake.address().port}`;
const env = { ...process.env, OPEN_METEO_GEOCODING_URL: `${base}/geo`, OPEN_METEO_FORECAST_URL: `${base}/forecast` };

async function exercise(client, label) {
  const { tools } = await client.listTools();
  assert.deepEqual(tools.map((t) => t.name).sort(), ["get_current_weather", "get_forecast", "packing_advice"]);

  const now = await client.callTool({ name: "get_current_weather", arguments: { city: "Lisbon" } });
  assert.match(now.content[0].text, /Lisbon, Lisbon, Portugal: partly cloudy, 21°C/);

  const fc = await client.callTool({ name: "get_forecast", arguments: { city: "Lisbon", days: 3 } });
  assert.match(fc.content[0].text, /3-day forecast/);
  assert.match(fc.content[0].text, /70% chance of rain/);

  const pack = await client.callTool({ name: "packing_advice", arguments: { city: "Lisbon", days: 3 } });
  assert.match(pack.content[0].text, /umbrella/);
  assert.match(pack.content[0].text, /sweater/);

  const missing = await client.callTool({ name: "get_current_weather", arguments: { city: "Nowhereville" } });
  assert.match(missing.content[0].text, /couldn't find/);

  console.log(`✅ ${label}: ${tools.length} tools, ${now.content[0].text}`);
}

// 2) stdio mode (how Claude Desktop, Claude Code and Cursor run it locally)
const stdio = new Client({ name: "smoke-test", version: "1.0.0" });
await stdio.connect(new StdioClientTransport({ command: process.execPath, args: ["server.mjs"], env }));
await exercise(stdio, "stdio");
await stdio.close();

// 3) HTTP mode (how you'd host it remotely), with a bearer token
const port = 3100 + Math.floor(Math.random() * 500);
const child = spawn(process.execPath, ["server.mjs", "--http"], {
  env: { ...env, PORT: String(port), MCP_AUTH_TOKEN: "test-token" },
  stdio: ["ignore", "ignore", "pipe"],
});
await new Promise((resolve) => child.stderr.on("data", (d) => d.toString().includes("listening") && resolve()));

const unauthorized = await fetch(`http://127.0.0.1:${port}/mcp`, { method: "POST", body: "{}" });
assert.equal(unauthorized.status, 401);

const http = new Client({ name: "smoke-test-http", version: "1.0.0" });
await http.connect(new StreamableHTTPClientTransport(new URL(`http://127.0.0.1:${port}/mcp`), {
  requestInit: { headers: { Authorization: "Bearer test-token" } },
}));
await exercise(http, "http");
await http.close();

child.kill();
fake.close();
console.log("🎉 All weather-buddy checks passed.");
