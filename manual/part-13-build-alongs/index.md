# 🧱 Part XIII · Build-Alongs

Eight long, friendly, step-by-step projects. Each one combines skills from across the manual into something real you'll
actually use, and each is doable in a weekend.

<details class="eli5" open>
<summary>🧸 ELI5: This part in 30 seconds</summary>

These are like LEGO instruction booklets. Each one has numbered steps, pictures of what you're building, and checkpoints
so you know it's working. At the end, you have a real, working thing: a pocket assistant, your own MCP server, a web app,
a research robot, and more.

</details>

## 🧭 Pick a build

| Build | Difficulty | You'll use | Time |
|---|---|---|---|
| [Your Pocket AI Assistant on Telegram](112-build-along-pocket-ai-assistant.md) | 🟢🟡 | n8n, Claude, Google Calendar, memory | ~3 hours |
| [Publish Your Own MCP Server](113-build-along-publish-an-mcp-server.md) | 🟡 | Node.js, MCP SDK, npm, the MCP Registry | ~3 hours |
| [The Second Brain](114-build-along-second-brain.md) | 🟢 | Obsidian, Claude Code, skills, automations | ~2 hours |
| [A Web App with Logins & AI](115-build-along-web-app-with-ai.md) | 🟡🔴 | Claude Code, Supabase, Vercel, Claude API | a weekend |
| [A Research Agent That Writes Reports](116-build-along-research-agent.md) | 🟡 | Python, Claude API, web search | ~3 hours |
| [The Private Home Assistant](117-build-along-private-home-assistant.md) | 🟡 | Docker, Ollama, Open WebUI, RAG | ~3 hours |
| [The Automated Newsletter](118-build-along-automated-newsletter.md) | 🟢🟡 | RSS, n8n or Python, Claude, email | ~2 hours |
| [An AI Voice Receptionist](119-build-along-voice-receptionist.md) | 🟡🔴 | Voice platform, n8n, Google Calendar | a weekend |

> [!TIP]
> **💡 How to use a build-along**
> Every build has ✅ **checkpoints**. Don't move on until the checkpoint works, because it makes debugging 10× easier. Stuck?
> Paste the step, what you expected, and what happened into your AI assistant. That's a real pro move, not cheating!

## 🧰 The starter kits

Every build has tested, ready-to-run pieces in the repo's `examples/` folder:

| Kit | Used in | Tested by |
|---|---|---|
| [`n8n-workflows/telegram-pocket-assistant.json`](../../examples/n8n-workflows/telegram-pocket-assistant.json) | Pocket AI Assistant | JSON + connection checks in CI |
| [`weather-mcp-server/`](../../examples/weather-mcp-server/) | Publish an MCP Server | Offline smoke test (stdio + HTTP) |
| [`second-brain-vault/`](../../examples/second-brain-vault/) | The Second Brain | Open it in Obsidian! |
| [`research-agent/`](../../examples/research-agent/) | Research Agent | Offline agent-loop tests |
| [`homelab/`](../../examples/homelab/) | Private Home Assistant | YAML validated in CI |
| [`newsletter-pipeline/`](../../examples/newsletter-pipeline/) | Automated Newsletter | Offline parsing, dedupe and rendering tests |
| [`n8n-workflows/voice-receptionist-tools.json`](../../examples/n8n-workflows/voice-receptionist-tools.json) | Voice Receptionist | Slot-finder logic tested |

## 📚 All build-alongs

<!-- chapters:start -->
<div class="grid cards clickable" markdown>

-   **[112 · Build-Along: Your Pocket AI Assistant on Telegram 📱🤖](112-build-along-pocket-ai-assistant.md)**

    ---

    <span class="card-meta">⏱️ ~3 hours to build · 🎯 Beginner → intermediate (no code)</span>

    By the end of this build-along, you'll have your own AI assistant living in Telegram. It's called Pip (rename it!), it remembers your conversation, checks your Google Calendar, adds events after you confirm, does math, and politely ignores everyone except you.

-   **[113 · Build-Along: Publish Your Own MCP Server ☔📦](113-build-along-publish-an-mcp-server.md)**

    ---

    <span class="card-meta">⏱️ ~3 hours to build · 🎯 Intermediate (copy-paste friendly)</span>

    In this build-along you'll take a real MCP server from "works on my machine" to "anyone in the world can install it." You'll run and test Weather Buddy (live weather, forecasts and packing advice from the free Open-Meteo API), make it yours with a new tool, connect it to Claude, publish it to npm, list it in the official MCP Registry, and optionally host it as a remote server.

-   **[114 · Build-Along: The Second Brain 🧠🗃️](114-build-along-second-brain.md)**

    ---

    <span class="card-meta">⏱️ ~2 hours to build · 🎯 Beginner-friendly</span>

    By the end of this build-along, you'll have a second brain that organizes itself. Ideas land in an inbox from your phone, AI triages them into the right folders with tags and links, a weekly review writes itself, and you can ask your notes questions like "what have I learned about sleep?" Everything is plain Markdown files you own, so it works with any AI, today and in ten years.

-   **[115 · Build-Along: A Web App with Logins & AI 🍲💻](115-build-along-web-app-with-ai.md)**

    ---

    <span class="card-meta">⏱️ A weekend · 🎯 Intermediate (no prior coding needed if you use Claude Code)</span>

    This weekend you'll ship a real web app to the internet: Recipe Box. People sign in, save their own recipes (private to them), and tap ✨ Remix to have Claude invent a new dish from whatever's in their fridge.

-   **[116 · Build-Along: A Research Agent That Writes Reports 🔎📄](116-build-along-research-agent.md)**

    ---

    <span class="card-meta">⏱️ ~3 hours to build · 🎯 Intermediate (copy-paste friendly Python)</span>

    In this build-along you'll run, understand and customize your own research agent. Give it a question; it plans, searches the live web, reads primary sources, cross-checks claims and saves a cited Markdown report.

-   **[117 · Build-Along: The Private Home Assistant 🏡🔒](117-build-along-private-home-assistant.md)**

    ---

    <span class="card-meta">⏱️ ~3 hours to build · 🎯 Intermediate (copy-paste friendly)</span>

    In this build-along you'll create an AI assistant for your whole household that never sends a word to the cloud.

-   **[118 · Build-Along: The Automated Newsletter 📰💌](118-build-along-automated-newsletter.md)**

    ---

    <span class="card-meta">⏱️ ~2 hours to build · 🎯 Beginner → intermediate</span>

    By the end of this build-along, a beautiful newsletter will write itself every week. It reads your favorite feeds, Claude picks the best items and explains why each matters, and a lovely email lands in your inbox (or your subscribers').

-   **[119 · Build-Along: An AI Voice Receptionist 📞🤖](119-build-along-voice-receptionist.md)**

    ---

    <span class="card-meta">⏱️ A weekend · 🎯 Intermediate → advanced</span>

    This is the grand finale: a friendly AI receptionist that answers a real phone number, answers questions, checks your calendar, books appointments, and sends you a summary of every call.

</div>
<!-- chapters:end -->
