# 🧰 Pocket Toolkit: Your First MCP Server

About 100 lines of Python that give your AI assistant **new abilities**. It's the
fastest way to go from "I've heard of MCP" to "I built an MCP server."

| Kind | Name | What it does |
|---|---|---|
| 🔧 Tool | `roll_dice` | Rolls dice in tabletop notation (`2d6+3`) |
| 🔧 Tool | `random_fortune` | Gives you a fortune-cookie pep talk |
| 🔧 Tool | `save_note` | Saves a tagged note to `notes.json` |
| 🔧 Tool | `list_notes` | Reads your notes back, optionally filtered by tag |
| 📄 Resource | `notes://all` | All your notes as JSON, attachable as context |
| 💬 Prompt | `daily_standup` | A reusable template that turns your notes into a standup update |

That's all three MCP building blocks (**tools, resources, prompts**) in one file.

---

## 1. Set it up (2 minutes)

```bash
cd examples/my-first-mcp-server
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 2. Prove it works

```bash
python smoke_test.py
```

You should see something like:

```
Tools: roll_dice, random_fortune, save_note, list_notes
roll_dice -> 🎲 3d6+2: [3, 1, 5] + 2 = **11**
random_fortune -> 🥠 You are one config file away from something awesome.
```

Want a visual playground instead? The **MCP Inspector** gives you a web UI to poke at every tool:

```bash
npx @modelcontextprotocol/inspector python server.py
```

## 3. Plug it into your AI

You need **absolute paths** here. Use the Python inside your venv so the `mcp` package is found.

### Claude Code

```bash
claude mcp add pocket-toolkit -- /full/path/to/.venv/bin/python /full/path/to/server.py
```

Then start `claude` and try: *"Roll me 4d6 for a D&D stat, then save a note saying I rolled it."*

### Claude Desktop

Open **Settings → Developer → Edit Config** and add the following to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "pocket-toolkit": {
      "command": "/full/path/to/.venv/bin/python",
      "args": ["/full/path/to/server.py"]
    }
  }
}
```

Fully quit and reopen Claude Desktop. Your tools will show up in the tools menu. 🎉

### Cursor / VS Code / others

Same shape of config. See [`../mcp-configs/`](../mcp-configs/) for copy-paste examples.

---

## 4. Make it yours

This is the fun part. Ideas, from easy to spicy:

- 🌤️ **Weather tool**: call a free weather API with `httpx`.
- 🍳 **Recipe box**: swap notes for recipes, and add a "what can I cook with X?" tool.
- 🎮 **Game master**: add `draw_card`, `random_npc_name`, and `random_encounter` tools.
- 🗂️ **Real storage**: replace `notes.json` with SQLite.
- 🏠 **Home automation**: wrap your Home Assistant REST API. "Hey Claude, dim the lights."
- 🌐 **Go remote**: run with `mcp.run(transport="streamable-http")` and connect over a URL.
  (Add auth before exposing it to the internet!)

> **Tip:** The docstring on each tool *is* the instruction manual the AI reads. Clear
> docstrings plus good parameter names get you a much smarter assistant.

## A note on SDK versions

This targets the **MCP Python SDK v2**, where the class is `MCPServer`. On the older
v1 SDK, change the import to:

```python
from mcp.server.fastmcp import FastMCP as MCPServer
```

and everything else works as-is.
