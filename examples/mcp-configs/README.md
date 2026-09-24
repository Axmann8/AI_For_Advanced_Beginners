# 🔌 Copy-Paste MCP Configs

Ready-made configs for the most popular AI apps. Pick your app, copy the file into the
right place, delete the servers you don't want, and add your keys.

| File | App | Where it goes |
|---|---|---|
| [`claude_desktop_config.json`](claude_desktop_config.json) | Claude Desktop | macOS: `~/Library/Application Support/Claude/`<br>Windows: `%APPDATA%\Claude\`<br>(or **Settings → Developer → Edit Config**) |
| [`claude-code.mcp.json`](claude-code.mcp.json) | Claude Code | Rename to `.mcp.json` at your project root (shared with your team), or use `claude mcp add` |
| [`cursor.mcp.json`](cursor.mcp.json) | Cursor | `.cursor/mcp.json` in a project, or `~/.cursor/mcp.json` globally |
| [`vscode.mcp.json`](vscode.mcp.json) | VS Code (Copilot agent mode) | `.vscode/mcp.json` in your workspace |

## The two shapes of MCP server

```jsonc
// 1) LOCAL (stdio): the app launches a program on your machine
"memory": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-memory"] }

// 2) REMOTE (HTTP): the app connects to a URL, and you usually log in with OAuth
"linear": { "url": "https://mcp.linear.app/mcp" }
```

Remote servers are the easy mode: no installs, and login happens in your browser. Local servers
can touch your files and apps directly, which makes them powerful and worth a little care.

## Handy Claude Code commands

```bash
claude mcp add --transport http notion https://mcp.notion.com/mcp   # add a remote server
claude mcp add memory -- npx -y @modelcontextprotocol/server-memory  # add a local server
claude mcp list                                                     # see what's connected
claude mcp remove memory                                            # remove one
# inside a session: /mcp   → check status and log in to OAuth servers
```

## Prereqs for local servers
- `npx` comes with [Node.js](https://nodejs.org) (LTS is fine).
- `uvx` comes with [uv](https://docs.astral.sh/uv/), a fast Python tool runner.

## 🔐 Key hygiene
- **Never commit real API keys.** Claude Code's `.mcp.json` supports `${ENV_VAR}` expansion, and VS Code
  supports `${input:...}` prompts. Use them!
- Point the filesystem server at a **specific playground folder**, not your whole home directory.
- Remote server URLs change sometimes. If one fails, check the vendor's docs for the current endpoint.
