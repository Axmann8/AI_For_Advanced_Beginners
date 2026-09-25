# 42 · Building MCP Servers: The Deep Dive 🏗️🔌

> ⏱️ 9 min read · 🎯 Intermediate (AI can write the code with you) · 🧰 Needs: Python 3.10+ or Node.js 20+

**Using MCP servers is fun. Building them is a superpower.** Any API, script, database or gadget you can talk to with
code can become a tool that *every* AI app can use. This chapter takes you from "hello world" to a remote, authenticated
server published to the official registry, with tested starter kits in both Python and TypeScript.

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Building an MCP server is like building a new button panel for your AI. You write a few little functions ("roll dice,"
"save a note," "check the weather"), give each a clear label, and the MCP kit turns them into buttons any AI can press. Start
with our ready-made example, change it, and you've made your first AI superpower. 🦸

</details>

<!-- in-this-chapter -->

> [!TIP]
> **💡 You don't have to be a strong programmer**
> Everything here can be built *with* an AI coding agent. Open Claude Code or Cursor, point it at this chapter, and say
> *"help me build this."* That's the whole point of [Part VII](../part-7-building-with-ai/index.md). 😄

## 🎯 Step 0: Decide what your server should do

<details class="eli5">
<summary>🧸 ELI5</summary>

Before building, decide what your panel is for (the "noun," like recipes or weather) and what buttons it needs (the
"verbs," like search, add, delete). Fewer, clearer buttons are better.

</details>

A great server is **small, focused and well-described**. Answer three questions:

1. **What's the noun?** Spotify, my recipes, Home Assistant, our company wiki.
2. **What are the verbs?** search, get, create, update, summarize.
3. **Who's the user?** Just you → local stdio. Your team or the public → remote HTTP with auth.

> [!NOTE]
> **📌 Design tools for the model, not for the API**
> Don't mirror a REST API 1:1 with 60 endpoints. Design **5–15 task-shaped tools** with clear names (`search_recipes`,
> `add_to_shopping_list`) that return **concise, readable** results. Every tool description is read on every request, so
> bloated servers make agents slower and dumber.

## 🚀 Step 1: Your first server in 5 minutes

<details class="eli5">
<summary>🧸 ELI5</summary>

Copy our ready-made example, run one command to check it works, and plug it into your AI. Then start changing it.

</details>

Two complete, tested kits ship with this manual, and CI runs their smoke tests on every change:

| | 🐍 Python | 🟨 TypeScript / JavaScript |
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

### TypeScript anatomy

```js
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const server = new McpServer({ name: "recipe-box", version: "1.0.0" });

server.registerTool(
  "search_recipes",
  {
    description: "Find recipes that use an ingredient. Returns titles and cook times.",
    inputSchema: { ingredient: z.string(), max_results: z.number().int().default(5) },
  },
  async ({ ingredient, max_results }) => ({ content: [{ type: "text", text: "…" }] }),
);

await server.connect(new StdioServerTransport());
```

The SDKs read your **names, types and descriptions** and turn them into the tool's JSON Schema, which is exactly what the
model sees ([MCP Under the Hood](39-mcp-under-the-hood.md#-tools-up-close)).

> [!NOTE]
> **📌 SDK versions**
> The Python SDK v2 renamed `FastMCP` to `MCPServer` (`from mcp.server.mcpserver import MCPServer`). On v1, use
> `from mcp.server.fastmcp import FastMCP`. The API is otherwise nearly identical.

## ✍️ Step 2: Write tools the AI will use well

<details class="eli5">
<summary>🧸 ELI5</summary>

Good buttons have clear labels, ask for simple information, give short helpful answers, and explain kindly what went
wrong when something fails.

</details>

| Do ✅ | Don't ❌ |
|---|---|
| `search_recipes(ingredient, max_results=5)` | `api_call(endpoint, params_json)` |
| Docstring says *when* to use it and *what it returns* | Empty or one-word descriptions |
| Return short, readable text or compact JSON | Dump a 5,000-line raw API response |
| Helpful errors: "No recipes with 'kale'. Try a broader ingredient." | Stack traces |
| Paginate or limit big results | Return everything |
| Enums and defaults for constrained params | Free-text params that must match magic values |
| Mark read-only vs. destructive tools (**annotations**) | Surprise side effects |
| One tool per clear task | One mega-tool with a `mode` parameter |

**Tool annotations** (`readOnlyHint`, `destructiveHint`, `idempotentHint`, `openWorldHint`) let apps decide when to ask
the user for confirmation, so set them honestly.

## 📦 Step 3: Structured output & errors

<details class="eli5">
<summary>🧸 ELI5</summary>

Sometimes a robot, not a person, reads the answer, so you can also return a neat form with labeled boxes. And when
something breaks, say so politely instead of crashing.

</details>

- **Structured content:** tools can return typed JSON (matching an output schema) alongside text, which is great when results
  feed other tools or automations. In Python, a typed return value (a Pydantic model or TypedDict) generates this for you.
- **Errors as results:** return a tool result flagged as an error with a clear message ("File not found: try `list_notes`
  first") rather than raising unhandled exceptions. The model can then recover.
- **Validate inputs** at the boundary (dates, IDs, sizes) and explain what's wrong.

## 📄 Step 4: Resources and prompts

<details class="eli5">
<summary>🧸 ELI5</summary>

Besides buttons, your panel can offer folders to read (resources) and recipe cards to pick (prompts). These are great for
"attach my project status" or "run my weekly review."

</details>

- **Resources** expose readable data at URIs: `notes://all`, `recipes://{id}` (templates). Apps let users attach them as context.
- **Prompts** are reusable templates with arguments, often surfaced as **slash commands**: `/weekly_meal_plan diet=vegan`.
- Rule of thumb: **tools** for actions the model chooses, **resources** for data the user attaches, **prompts** for workflows the user triggers.

## 🧪 Step 5: Test like a pro

<details class="eli5">
<summary>🧸 ELI5</summary>

Press every button yourself before handing the panel to the AI. There's a free tool for that, and you can write a little
robot that tests it automatically every time you change something.

</details>

1. **MCP Inspector:** `npx @modelcontextprotocol/inspector python server.py` lets you list and call every tool by hand.
2. **Smoke tests:** a tiny client script that calls your tools ([Python example](../../examples/my-first-mcp-server/smoke_test.py)).
   Put it in CI like this repo does (`.github/workflows/examples.yml`).
3. **Real-model test:** connect it to Claude and try 5 natural requests. If the model picks the wrong tool or passes bad
   arguments, **fix the descriptions**, not the model.

> [!WARNING]
> **⚠️ The #1 stdio bug**
> In a stdio server, **stdout is the protocol channel.** A stray `print()` or `console.log()` corrupts it and the client
> disconnects mysteriously. Log to **stderr** instead.

## ☁️ Step 6: Go remote with Streamable HTTP

<details class="eli5">
<summary>🧸 ELI5</summary>

A local panel only works on your computer. To share it with your phone, your team or the world, put it on the internet
with a web address. Same buttons, longer wire.

</details>

```python
# Python (SDK v2): serves at http://127.0.0.1:8000/mcp
mcp.run(transport="streamable-http", host="0.0.0.0", port=8000, stateless_http=True)
```

```js
// TypeScript: use StreamableHTTPServerTransport with Express, Hono, etc.
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
```

- **Stateless mode** is the modern default. Each request stands alone, so you can scale behind a load balancer.
- **Where to host:** Cloudflare Workers (MCP templates available), Vercel, Fly.io, Railway, Render, Google Cloud Run, AWS
  Lambda, or a small VPS ([Deploying & Hosting](../part-7-building-with-ai/66-deploying-and-hosting.md)).
- **Connect:** Claude's *Add custom connector*, `claude mcp add --transport http name URL`, or any client's remote config.

## 🔐 Step 7: Authentication

<details class="eli5">
<summary>🧸 ELI5</summary>

If your panel can touch private stuff, it needs a lock. Simple locks (a secret password in the request) are fine for you
and friends, and proper "Sign in with…" locks (OAuth) are for the public.

</details>

**Never expose a server that touches private data without auth.** Options, from simple to proper:

| Option | Good for | Notes |
|---|---|---|
| **Private network only** | Home lab | Tailscale or a VPN, so nothing is exposed publicly |
| **API key / bearer header** | Personal and team servers | Clients send `Authorization: Bearer …`. Simple, but manual |
| **OAuth 2.1** (the MCP spec's standard) | Public and multi-user servers | Users click "Connect" and log in, with discovery and client registration defined by the spec |
| **Managed auth platforms** | Skipping the hard parts | Cloudflare, Stytch, WorkOS, Auth0 and others ship MCP-ready OAuth |

The auth story evolved a lot in 2025–26: **Client ID Metadata Documents** replaced dynamic client registration as the
recommended approach, and issuer validation got stricter. The SDKs' auth helpers track the spec, so use them rather than
rolling your own.

## 🌍 Step 8: Publish it

<details class="eli5">
<summary>🧸 ELI5</summary>

Share your panel with the world: put the code in a package store so anyone can install it with one command, then add it
to the official directory so people can find it.

</details>

### To npm or PyPI
Package it so people can run it with one command: `npx your-server` or `uvx your-server`.

### To the Official MCP Registry
The [official registry](https://registry.modelcontextprotocol.io) stores **metadata** pointing at your package or remote
URL, and other directories pull from it:

```bash
# install the publisher CLI (see the registry repo for current install options), then:
mcp-publisher init          # creates server.json describing your server
mcp-publisher login github  # proves you own io.github.<you>/* names
mcp-publisher publish
```

Namespaces are verified: `io.github.yourname/...` via GitHub login, or your own domain via DNS. For npm packages you also
add an `mcpName` field to `package.json` so the registry can verify ownership. Full walkthrough in
[Build-Along: Publish Your Own MCP Server](../part-13-build-alongs/113-build-along-publish-an-mcp-server.md).

### As a Claude Desktop Extension (`.mcpb`)
Bundle a local server with its runtime into a **one-click installable** file, so non-technical friends can use it.

### As part of a plugin
Bundle your server with skills and slash commands as a Claude Code plugin, so a whole workflow installs in one step
([Claude Code Power-Ups](../part-7-building-with-ai/63-claude-code-power-ups.md)).

## 🚀 Step 9: Level up

<details class="eli5">
<summary>🧸 ELI5</summary>

Once the basics work, you can add fancy extras: progress bars for slow jobs, questions for the user, and even little
interactive screens inside the chat.

</details>

- **Resource templates:** `recipes://{id}` gives browsable, attachable data.
- **Prompts** show up as slash commands in many clients, so they're great for "packaged workflows."
- **Progress notifications** for long-running tools, and **Tasks** for really long jobs.
- **Asking the user mid-call** (multi round-trip requests): confirm or choose before acting.
- **MCP Apps:** return **interactive UI** that renders inside the chat (forms, charts, pickers).
- **Caching hints:** list results can tell clients how long they're valid.

## 🚧 Common mistakes (and fixes)

<details class="eli5">
<summary>🧸 ELI5</summary>

Here are the oopsies almost everyone makes on their first server, so you can skip them.

</details>

| Mistake | Symptom | Fix |
|---|---|---|
| `print()` in a stdio server | Client disconnects, "invalid JSON" | Log to stderr |
| Giant raw API responses | Slow, expensive, confused model | Summarize, trim, paginate |
| Vague descriptions | Wrong tool chosen, bad arguments | Say what, when, returns, cautions |
| Too many tools | Model dithers, context bloat | Merge or remove, aim for 5–15 |
| Secrets in code | Leaked keys on GitHub | Env vars + `.gitignore` |
| No auth on a remote server | Anyone can use your tools | Bearer token or OAuth, or a private network |
| Relative paths in configs | Works in terminal, fails in app | Absolute paths everywhere |

## 💡 20 MCP server ideas to build

<details class="eli5">
<summary>🧸 ELI5</summary>

Need inspiration? Here are twenty panels you could build, from super easy to spicy.

</details>

| Easy 🟢 | Medium 🟡 | Spicy 🔴 |
|---|---|---|
| Recipe box | Spotify DJ | Home Assistant controller with safety rails |
| Workout logger | Strava coach | Personal finance (read-only!) |
| Book and movie log | Pokémon / D&D 5e API | Company wiki + ticketing combo |
| Local weather (Open-Meteo, free) | RSS reader with summaries | Multi-user remote server with OAuth |
| Random generators (names, ideas) | Your Obsidian vault with backlinks | MCP App with interactive charts |
| Plant watering tracker | SQLite notes with search | 3D printer / OctoPrint control |
| Quote of the day | GitHub stats dashboard | Voice-note transcriber (Whisper) |

## 🎯 Key takeaways

- Start from the **tested kits** (Python or TypeScript) and change one thing at a time.
- Design **5–15 task-shaped tools** with great descriptions, honest annotations and friendly errors.
- **Test** with the Inspector, smoke tests and real prompts, and fix descriptions first.
- Go **remote** with Streamable HTTP (stateless) and add **auth** before exposing anything private.
- **Publish** to npm/PyPI and the **official registry**, or ship as a `.mcpb` or plugin.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. The model keeps calling the wrong tool. What do you change first?</summary>

The **tool names and descriptions** (what, when, returns, cautions), and consider removing overlapping tools.

</details>

<details class="quiz">
<summary>❓ 2. Your server works in the terminal but not in Claude Desktop. Likely culprits?</summary>

**Relative paths** or **PATH issues** (GUI apps don't see your shell's PATH), or a missing env var. Use absolute paths.

</details>

<details class="quiz">
<summary>❓ 3. Tool, resource or prompt: "attach the current project status to this chat"?</summary>

A **resource**: data the user chooses to attach.

</details>

> [!TIP]
> **🎮 Try this**
> Open Claude Code in this repo and say: *"Add a `weather` tool to examples/my-first-mcp-server using the free Open-Meteo
> API (no key needed). Include a good docstring, handle errors kindly, and update the smoke test."* Then connect it to
> Claude Desktop and ask *"Should I bring an umbrella tomorrow?"* You just shipped a real integration. ☔

---

**Next:** [43 · MCP Security & Trust →](43-mcp-security-and-trust.md)
