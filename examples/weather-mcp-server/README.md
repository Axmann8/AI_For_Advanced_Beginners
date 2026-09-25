# ☔ Weather Buddy: a publishable MCP server

A small, real, **publishable** MCP server that gives any AI assistant live weather superpowers, using the free
[Open-Meteo](https://open-meteo.com) API (no API key needed).

| Tool | What it does |
|---|---|
| `get_current_weather` | Right-now conditions for any city |
| `get_forecast` | A 1–7 day forecast: conditions, highs and lows, chance of rain |
| `packing_advice` | What to wear or pack, based on the forecast |

It runs **two ways**:

- **Local (stdio):** `node server.mjs`, for Claude Desktop, Claude Code, Cursor and friends.
- **Remote (Streamable HTTP):** `node server.mjs --http`, for hosting on the internet, with an optional bearer token.

This is the companion kit for **[Build-Along: Publish Your Own MCP Server](../../manual/part-11-build-alongs/82-build-along-publish-an-mcp-server.md)**.

## Quick start 🚀

```bash
cd examples/weather-mcp-server
npm install
npm test            # offline smoke test (fake weather API, both stdio and HTTP modes)
npm run inspect     # poke at it in the MCP Inspector
```

## Use it in Claude Code or Claude Desktop

```bash
claude mcp add weather-buddy -- node /full/path/to/examples/weather-mcp-server/server.mjs
```

```json
{
  "mcpServers": {
    "weather-buddy": { "command": "node", "args": ["/full/path/to/examples/weather-mcp-server/server.mjs"] }
  }
}
```

Then ask: *"Should I pack an umbrella for Lisbon this weekend?"* ☂️

## Run it as a remote server 🌍

```bash
MCP_AUTH_TOKEN=pick-a-long-random-secret PORT=3000 npm run http
# MCP endpoint: http://localhost:3000/mcp    health check: http://localhost:3000/health
```

It's **stateless** (a fresh server per request), so it's happy on serverless-style hosts and behind load balancers. Deploy
the included `Dockerfile` to Render, Railway, Fly.io or Google Cloud Run, set `MCP_AUTH_TOKEN`, and connect with:

```bash
claude mcp add --transport http weather-buddy https://your-host.example.com/mcp \
  --header "Authorization: Bearer pick-a-long-random-secret"
```

> 🔐 A shared bearer token is fine for personal use. For a public, multi-user server, use proper OAuth (see
> [Building MCP Servers](../../manual/part-2-mcp-and-connectors/11-building-mcp-servers.md)).

## Publish it 📦

1. Replace `your-github-username` in `package.json` and `server.json` with your GitHub username.
2. `npm publish --access public`
3. Install `mcp-publisher` (e.g. `brew install mcp-publisher`), then `mcp-publisher login github` and `mcp-publisher publish`.

The full walkthrough, including testing, versioning and a listing people will love, is in the build-along.

## Make it yours 🎨

- Add a `get_air_quality` tool (Open-Meteo has a free air-quality API).
- Add °F support with a `units` parameter.
- Add a resource with your favorite cities, or a prompt template for "plan my week around the weather."
