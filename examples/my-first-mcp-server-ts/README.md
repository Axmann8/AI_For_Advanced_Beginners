# 🟨 Pocket Toolkit: TypeScript/JavaScript Edition

The same friendly MCP server as the [Python version](../my-first-mcp-server/), built with the official
**MCP TypeScript SDK**. If you live in the JavaScript world (or want to publish to npm so anyone can
`npx` your server), start here.

| Kind | Name | What it does |
|---|---|---|
| 🔧 Tool | `roll_dice` | Rolls dice in tabletop notation (`2d6+3`) |
| 🔧 Tool | `random_fortune` | Gives you a fortune-cookie pep talk |
| 🔧 Tool | `save_note` / `list_notes` | A tiny local notes store (`notes.json`) |
| 📄 Resource | `notes://all` | All notes as JSON |
| 💬 Prompt | `daily_standup` | Turns your notes into a standup update |

## Run it

```bash
cd examples/my-first-mcp-server-ts
npm install
npm test            # smoke test: lists tools and rolls some dice 🎲
npm run inspect     # opens the MCP Inspector web UI
```

## Plug it into your AI

**Claude Code:**
```bash
claude mcp add pocket-toolkit-ts -- node /full/path/to/server.mjs
```

**Claude Desktop / Cursor** (`claude_desktop_config.json` or `.cursor/mcp.json`):
```json
{
  "mcpServers": {
    "pocket-toolkit-ts": { "command": "node", "args": ["/full/path/to/server.mjs"] }
  }
}
```

## How it's built (the 30-second tour)

```js
const server = new McpServer({ name: "pocket-toolkit-ts", version: "1.0.0" });

server.registerTool(
  "roll_dice",
  {
    description: "Roll dice using tabletop notation…",  // ← the AI reads this!
    inputSchema: { notation: z.string().default("1d20") }, // ← zod schema = parameters
  },
  async ({ notation }) => ({ content: [{ type: "text", text: "🎲 …" }] }),
);

await server.connect(new StdioServerTransport());
```

- **`zod`** schemas define the parameters. The SDK turns them into JSON Schema for the model.
- **Descriptions matter.** They're the model's only guide to when and how to use a tool.
- **Never `console.log` in a stdio server!** stdout *is* the protocol channel. Log with `console.error`.

## Make it yours

- Publish to npm and let people run it with `npx your-server-name`.
- Swap stdio for **Streamable HTTP** (see `StreamableHTTPServerTransport` in the SDK) to host it remotely.
- Wrap any API you love: Spotify, Strava, the Pokémon API, your company's internal tools.

Full walkthrough: [The manual: Building MCP Servers](../../manual/part-4-mcp-and-connectors/42-building-mcp-servers.md).
