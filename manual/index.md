# 🚀 AI for Advanced Beginners: The Massive Manual

### *You know what an LLM is. You know how to prompt. Welcome to the fun part.*

This manual picks up where "intro to AI" leaves off. It's **40+ chapters** on connecting AI to your
apps, letting it take actions, automating your life, building your own tools and agents, running models
on your own machine, making art and music, and using all of it in real work and real life.

There's no "what is a large language model," and no "10 rules for better prompts." You've got that. This is what comes next. 🎉

> [!TIP]
> **How to read this manual**
> You don't have to go in order. Skim the parts below, jump to whatever excites you, and **do the
> 🎮 "Try this" boxes**. Ten minutes of doing beats an hour of reading. Every chapter ends with a
> link to the next one if you'd rather go straight through.

> 📅 Current as of **September 2026**. AI moves fast, so product names and features shift monthly,
> but the concepts and patterns here will last much longer than the specifics.

---

## 🗺️ The Ten Parts

| Part | What it's about | Start here |
|---|---|---|
| **I · Foundations** | The mental model, how models really work, picking your stack | [The Mental Model](part-1-foundations/01-the-mental-model.md) |
| **II · MCP & Connectors** | The "USB-C for AI" standard, 65+ servers, building your own, recipes | [MCP Explained](part-2-mcp-and-connectors/04-mcp-explained.md) |
| **III · Automation** | n8n, Zapier, Make, webhooks and APIs: AI that works while you sleep | [Automation Platforms](part-3-automation/09-automation-platforms.md) |
| **IV · AI in Your Apps** | Notion, Google Workspace, Microsoft 365, Obsidian | [AI Inside Your Apps](part-4-ai-in-your-apps/13-ai-in-your-apps.md) |
| **V · Building with AI** | Claude Code, vibe coding, APIs, your own agents, multi-agent systems | [Agents & Coding Tools](part-5-building-with-ai/17-agents-and-coding-tools.md) |
| **VI · Knowledge & Memory** | RAG, building a RAG system, second brains | [RAG, Memory & Knowledge](part-6-knowledge-and-memory/23-rag-memory-and-knowledge.md) |
| **VII · Local AI** | Ollama, LM Studio, and a home lab in Docker | [Local & Open Models](part-7-local-ai/26-local-and-open-models.md) |
| **VIII · Creative AI** | Images, video, audio, music, voice agents | [Multimodal Playground](part-8-creative-ai/28-multimodal-playground.md) |
| **IX · AI for Life & Work** | Research, writing, small business, life admin, data analysis | [Research & Learning](part-9-ai-for-life-and-work/32-research-and-learning.md) |
| **X · Mastery** | Safety, evals, cost optimization, staying current, the future | [Safety, Costs & Gotchas](part-10-mastery/37-safety-costs-and-gotchas.md) |
| **Appendices** | Glossary, cheat sheet, troubleshooting, 100 prompts, resources, 30 projects | [Cheat Sheet](appendices/b-cheat-sheet.md) |

---

## 🧭 Pick Your Path

**⚡ Results in 10 minutes**

1. [Built-in Connectors](part-2-mcp-and-connectors/06-built-in-connectors.md): turn on Drive or Notion in Claude or ChatGPT.
2. Ask about **your own** stuff.
3. Grab a prompt from [100 Prompts That Use Tools](appendices/d-100-prompts.md).

**🔌 Understand MCP**

1. [MCP Explained](part-2-mcp-and-connectors/04-mcp-explained.md)
2. [The Big Server Catalog](part-2-mcp-and-connectors/05-mcp-server-catalog.md)
3. [Building MCP Servers](part-2-mcp-and-connectors/07-building-mcp-servers.md)
4. [MCP Recipe Book](part-2-mcp-and-connectors/08-mcp-recipe-book.md)

**⚙️ Automate boring stuff**

1. [Automation Platforms](part-3-automation/09-automation-platforms.md)
2. [n8n Masterclass](part-3-automation/10-n8n-masterclass.md)
3. [Webhooks, APIs & JSON](part-3-automation/12-webhooks-apis-json.md)

**🛠️ Build apps & agents**

1. [Agents & Coding Tools](part-5-building-with-ai/17-agents-and-coding-tools.md)
2. [Claude Code Masterclass](part-5-building-with-ai/18-claude-code-masterclass.md)
3. [Vibe Coding Your First App](part-5-building-with-ai/19-vibe-coding-your-first-app.md)
4. [Build Your Own Agent](part-5-building-with-ai/21-build-your-own-agent.md)

**🔒 Private & tinkery**

1. [Local & Open Models](part-7-local-ai/26-local-and-open-models.md)
2. [Home Lab](part-7-local-ai/27-home-lab.md)
3. [Build a RAG System](part-6-knowledge-and-memory/24-build-a-rag-system.md)

**🎨 Make cool stuff**

1. [Multimodal Playground](part-8-creative-ai/28-multimodal-playground.md)
2. [Image Generation Deep Dive](part-8-creative-ai/29-image-generation-deep-dive.md)
3. [Video & Audio Production](part-8-creative-ai/30-video-and-audio-production.md)

---

## 🧪 Hands-On Starter Kits

The manual comes with working code and configs you can use right away:

| Kit | What's inside |
|---|---|
| [🧰 My First MCP Server (Python)](../examples/my-first-mcp-server/) | Dice 🎲, fortunes 🥠, notes 📝. Plug it into Claude in 5 minutes |
| [🟨 My First MCP Server (TypeScript)](../examples/my-first-mcp-server-ts/) | The same server in JavaScript/TypeScript land |
| [🤖 Build Your Own Agent](../examples/build-your-own-agent/) | The agent loop in ~100 lines of Python on the Claude API |
| [📚 RAG from Scratch](../examples/rag-from-scratch/) | Chat with a folder of notes, and see every step |
| [🏠 Home Lab](../examples/homelab/) | Ollama + Open WebUI + n8n in one `docker compose up` |
| [🔌 MCP Configs](../examples/mcp-configs/) | Copy-paste configs for Claude, Cursor, and VS Code |
| [⚡ n8n Workflows](../examples/n8n-workflows/) | A Morning AI Digest and an Idea Inbox → Notion |
| [🧠 Agent Memory & Skills](../examples/prompts-for-agents/) | A sample `CLAUDE.md` and a skill |

> [!TIP]
> **Prefer one giant file?**
> The whole manual is also published as a single **`MANUAL.md`**, which is perfect for printing, offline
> reading, or handing to an AI as context. It's built automatically alongside this site.

**Ready?** → [Start with The Mental Model](part-1-foundations/01-the-mental-model.md) 🚀
