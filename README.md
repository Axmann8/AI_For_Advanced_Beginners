# 🚀 AI for Advanced Beginners

### *You know what an LLM is. You know how to prompt. Now what?*

This is a hands-on field guide to the **fun part** of AI: connecting it to your apps, letting it take
actions, automating your life, running models on your own machine, and building your own tools.
There's no "what is a large language model" and no "10 rules for better prompts." You've got that.
This is what comes next. 🎉

> 📅 Current as of **September 2026**. The AI world moves fast, so product names and features shift
> monthly. The concepts here will last much longer than the specifics.

---

## 📚 The Guide

| # | Chapter | You'll learn |
|---|---|---|
| 01 | [The Mental Model](guide/01-the-mental-model.md) | Chatbot → agent: tools, context, memory, loops, and how it all fits |
| 02 | [MCP Explained](guide/02-mcp-explained.md) | The "USB-C for AI" standard, and how to install servers in every major app |
| 03 | [**The Big MCP Server Catalog**](guide/03-mcp-server-catalog.md) | 65+ servers by category, each with a "try this" prompt, plus where to find more |
| 04 | [Built-in Connectors & Plugins](guide/04-built-in-connectors.md) | Claude, ChatGPT, Gemini, and Copilot integrations, no config needed |
| 05 | [Automation Platforms](guide/05-automation-platforms.md) | n8n, Zapier, Make, Pipedream, Activepieces: AI that works while you sleep |
| 06 | [AI Inside Your Apps](guide/06-ai-in-your-apps.md) | Notion AI, Obsidian, Sheets, email, calendar, and desktop AI |
| 07 | [Agents & AI Coding Tools](guide/07-agents-and-coding-tools.md) | Claude Code, Cursor, Lovable, skills, hooks, subagents, agent SDKs |
| 08 | [Local & Open Models](guide/08-local-and-open-models.md) | Ollama, LM Studio, and private AI on your laptop |
| 09 | [RAG, Memory & Knowledge](guide/09-rag-memory-and-knowledge.md) | Make AI know *your* stuff: NotebookLM, vector DBs, memory |
| 10 | [The Multimodal Playground](guide/10-multimodal-playground.md) | Images, video, voice, music, and computer-use agents |
| 11 | [30 Project Ideas](guide/11-project-ideas.md) | Weekend builds from 🟢 easy to 🔴 ambitious, plus a 30-day plan |
| 12 | [Safety, Costs & Gotchas](guide/12-safety-costs-and-gotchas.md) | Prompt injection, keys, and avoiding surprise bills |
| 📖 | [Glossary](guide/glossary.md) | Every buzzword, in plain English |

## 🧪 Hands-On Starter Kits

| Kit | What's inside |
|---|---|
| [🧰 My First MCP Server](examples/my-first-mcp-server/) | A working ~100-line Python MCP server (dice 🎲, fortunes 🥠, notes 📝) with a smoke test. Plug it into Claude in 5 minutes. |
| [🔌 Copy-Paste MCP Configs](examples/mcp-configs/) | Ready configs for Claude Desktop, Claude Code, Cursor, and VS Code |
| [⚡ n8n Workflows](examples/n8n-workflows/) | Two importable automations: a ☕ Morning AI Digest and a 💡 Idea Inbox → Notion |
| [🧠 Agent Memory & Skills](examples/prompts-for-agents/) | A sample `CLAUDE.md` and a `weekly-review` skill |

---

## 🧭 Pick Your Adventure

**"I want results in the next 10 minutes."**
→ [Ch. 4: Connectors](guide/04-built-in-connectors.md). Turn on Google Drive or Notion in Claude or ChatGPT and ask about your own stuff.

**"I want to understand the MCP hype."**
→ [Ch. 2](guide/02-mcp-explained.md) → [Ch. 3](guide/03-mcp-server-catalog.md) → build [your own server](examples/my-first-mcp-server/).

**"I want to automate boring stuff."**
→ [Ch. 5: Automation](guide/05-automation-platforms.md) → import the [n8n workflows](examples/n8n-workflows/).

**"I want to build apps without being a 'real' programmer."**
→ [Ch. 7: Agents & Coding Tools](guide/07-agents-and-coding-tools.md) → [Project ideas](guide/11-project-ideas.md).

**"I want privacy and to tinker under the hood."**
→ [Ch. 8: Local Models](guide/08-local-and-open-models.md) → [Ch. 9: RAG](guide/09-rag-memory-and-knowledge.md).

**"I just want to make cool stuff."**
→ [Ch. 10: Multimodal Playground](guide/10-multimodal-playground.md). Go make a song, a movie trailer, or a 3D scene. 🎨

---

## ⚡ Quick Start: Your First Superpower in 5 Minutes

```bash
git clone <this-repo> && cd claude_cloud_trial_credits/examples/my-first-mcp-server
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python smoke_test.py            # 🎲 🥠 it works!
claude mcp add pocket-toolkit -- "$(pwd)/.venv/bin/python" "$(pwd)/server.py"
claude                          # then: "roll 4d6 and give me a fortune"
```

---

*Built with [Claude Code](https://claude.ai/code) using trial credits, which is itself a pretty good example of
what this guide is about. Now go build something fun.* ✨
