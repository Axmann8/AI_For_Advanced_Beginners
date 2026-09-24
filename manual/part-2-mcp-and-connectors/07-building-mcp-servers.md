# 07 · Building MCP Servers: The Deep Dive 🏗️

Using MCP servers is fun. **Building** them is a superpower. Any API, script, database, or gadget
you can talk to with code can become a tool that *every* AI app can use. This chapter takes you from
"hello world" to a remote, authenticated server published to the official registry.

!!! success "You don't have to be a strong programmer"
    Everything in this chapter can be built *with* an AI coding agent. Open Claude Code or Cursor, point it
    at this chapter, and say *"help me build this."* That's the whole point of Part V. 😄

---

## Step 0: Decide what your server should do

A great MCP server is **small, focused, and well-described**. Ask:

1. **What's the noun?** (Spotify, my recipes, Home Assistant, our company wiki)
2. **What are the verbs?** (search, get, create, update)
3. **Who's the user?** (Just you → local stdio. Your team or the public → remote HTTP.)

!!! tip "Design tools for the model, not for the API"
    Don't mirror a REST API 1:1 with 60 endpoints. Design **5–15 task-shaped tools** with clear names
    (`search_recipes`, `add_to_shopping_list`) that return **concise, readable** results. The model reads
    every tool description on every request, so bloated servers make agents dumber.

## Step 1: Your first server in 5 minutes

Two complete, tested examples ship with this manual:

| | Python | TypeScript/JavaScript |
|---|---|---|
| Kit | [`examples/my-first-mcp-server`](../../examples/my-first-mcp-server/) | [`examples/my-first-mcp-server-ts`](../../examples/my-first-mcp-server-ts/) |
| SDK | `mcp` (v2: `MCPServer`) | `@modelcontextprotocol/sdk` (`McpServer`) |
| Tool syntax | `@mcp.tool()` decorator + type hints | `server.registerTool(name, {inputSchema: zod}, fn)` |
| Test | `python smoke_test.py` | `npm test` |

### Python anatomy

```python
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("recipe-box", instructions="Helps the user manage their recipes.")

@mcp.tool()
def search_recipes(ingredient: str, max_results: int = 5) -> str:
    """Find recipes that use an ingredient. Returns titles and cook times."""
    ...

@mcp.resource("recipes://favorites")
def favorites() -> str:
    """The user's favorite recipes as Markdown."""
    ...

@mcp.prompt()
def weekly_meal_plan(diet: str = "anything") -> str:
    """Plan a week of dinners."""
    return f"Use search_recipes to plan 7 dinners for a {diet} diet, then list the groceries."

if __name__ == "__main__":
    mcp.run(transport="stdio")
```

The SDK reads your **function name, type hints, and docstring** and turns them into the tool's name,
JSON Schema, and description. The docstring is your prompt engineering for the tool.

## Step 2: Writing tools the AI will use well ✍️

| Do ✅ | Don't ❌ |
|---|---|
| `search_recipes(ingredient, max_results=5)` | `api_call(endpoint, params_json)` |
| Docstring says *when* to use it and what it returns | Empty or one-word descriptions |
| Return short, human-readable text or compact JSON | Dump a 5,000-line raw API response |
| Helpful errors: "No recipes with 'kale'. Try a broader ingredient." | Stack traces |
| Paginate or limit big results | Return everything |
| Use enums and defaults for constrained params | Free-text params that must match magic values |
| Mark read-only vs. destructive tools (tool **annotations**) | Surprise side effects |

**Tool annotations** let you hint to clients how risky a tool is (e.g. `readOnlyHint`,
`destructiveHint`, `idempotentHint`, `openWorldHint`). Good clients use these to decide when to ask the user for
confirmation.

### Structured output
Tools can return **structured content** (typed JSON matching an output schema) alongside text. That's
handy when the result feeds another tool or an automation. The SDKs generate this for you when your function has a
typed return value (e.g. a Pydantic model or TypedDict in Python).

## Step 3: Test like a pro 🧪

1. **MCP Inspector:** `npx @modelcontextprotocol/inspector python server.py` gives you a web UI
   to list and call every tool, read resources, and view raw protocol messages.
2. **Smoke tests:** script a client that calls your tools ([Python example](../../examples/my-first-mcp-server/smoke_test.py)).
   Put it in CI (this repo does, in `.github/workflows/examples.yml`).
3. **Real-model test:** connect it to Claude and try 5 natural requests. If the model picks the
   wrong tool or passes bad arguments, **fix the descriptions**, not the model.

!!! warning "The #1 stdio bug"
    In a stdio server, **stdout is the protocol channel.** A stray `print()` or `console.log()` corrupts
    it and the client disconnects mysteriously. Log to **stderr** instead.

## Step 4: Go remote with Streamable HTTP ☁️

Local stdio servers only work on your machine. To share with your team, your phone, or the world, serve over
**Streamable HTTP**:

```python
# Python (SDK v2): serves at http://127.0.0.1:8000/mcp
mcp.run(transport="streamable-http", host="0.0.0.0", port=8000, stateless_http=True)
```

```js
// TypeScript: use StreamableHTTPServerTransport with Express/Hono/etc.
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
```

- **Stateless mode** is the modern default. Each request stands alone, so you can scale horizontally behind
  a load balancer. (The July 2026 spec made the core protocol stateless.)
- **Where to host:** Cloudflare Workers (they have MCP templates), Vercel, Fly.io, Railway, Render, Google
  Cloud Run, AWS Lambda, or a small VPS.
- **Connect:** paste the URL into Claude's *Add custom connector*, `claude mcp add --transport http name URL`,
  or any client's remote config.

## Step 5: Authentication 🔐

**Never expose a server that touches private data without auth.** Your options, from simple to proper:

| Option | Good for | Notes |
|---|---|---|
| **Private network only** | Home lab | Tailscale or a VPN, so nothing is exposed publicly |
| **API key / bearer header** | Personal and team servers | Clients send `Authorization: Bearer …`. Simple, but manual |
| **OAuth 2.1** (the MCP spec's standard) | Public and multi-user servers | Users click "Connect" and log in. The spec defines discovery and client registration |
| **Managed auth platforms** | Skipping the hard parts | Cloudflare, Stytch, WorkOS, Auth0, and others ship MCP-ready OAuth |

The spec's auth story evolved a lot in 2025–26: **Client ID Metadata Documents** replaced dynamic
client registration as the recommended approach, and issuer validation got stricter. The SDKs' auth
helpers track the spec, so use them rather than rolling your own.

## Step 6: Publish it 🌍

### To npm or PyPI
Package it so people can run it with one command: `npx your-server` or `uvx your-server`.

### To the Official MCP Registry
The [official registry](https://registry.modelcontextprotocol.io) stores **metadata** pointing at your
package or remote URL, and other directories pull from it:

```bash
# install the publisher CLI (see the registry repo for current install options), then:
mcp-publisher init          # creates server.json describing your server
mcp-publisher login github  # proves you own io.github.<you>/* names
mcp-publisher publish
```

Namespaces are verified: `io.github.yourname/...` via GitHub login, or your own domain via DNS. For npm packages you
also add an `mcpName` field to `package.json` so the registry can verify ownership.

### As a Claude Desktop Extension (`.mcpb`)
Bundle a local server with its runtime into a **one-click installable** file, so non-technical friends can use it.

### As part of a plugin
Bundle your server with skills and slash commands as a Claude Code plugin, so your whole workflow installs in one step.

## Step 7: Level up 🚀

- **Resources with templates:** `recipes://{id}` gives the user browsable, attachable data.
- **Prompts** show up as slash commands in many clients. They're great for "packaged workflows."
- **Progress notifications** for long-running tools. **Tasks** for really long jobs.
- **User input mid-call** (elicitation / multi-round-trip requests): ask the user to confirm or choose.
- **MCP Apps:** return **interactive UI** that renders inside the chat (forms, charts, pickers).
- **Caching hints:** list results can tell clients how long they're valid.

---

## 💡 20 MCP server ideas to build

| Easy 🟢 | Medium 🟡 | Spicy 🔴 |
|---|---|---|
| Recipe box | Spotify DJ | Home Assistant controller with safety rails |
| Workout logger | Strava coach | Personal finance (Plaid, read-only!) |
| Book/movie log | Pokémon / D&D 5e API | Company wiki + ticketing combo |
| Local weather (Open-Meteo, free) | RSS reader with summaries | Multi-user remote server with OAuth |
| Random generators (names, ideas) | Your Obsidian vault with backlinks | MCP App with interactive charts |
| Plant watering tracker | Local SQLite notes with search | 3D printer / OctoPrint control |
| Quote of the day | GitHub stats dashboard | Voice-note transcriber (Whisper) |

---

### 🎮 Try this
Open Claude Code in this repo and say:
> *"Add a `weather` tool to examples/my-first-mcp-server using the free Open-Meteo API (no key needed).
> Include a good docstring, handle errors kindly, and update the smoke test."*

Then connect it to Claude Desktop and ask *"Should I bring an umbrella tomorrow?"* You just shipped a real integration. ☔

---

**Next:** [08 · The MCP Recipe Book →](08-mcp-recipe-book.md)
