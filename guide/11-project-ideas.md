# 11 · 30 Project Ideas to Level Up 🚀

Reading is great, but building is where it sticks. The projects go from 🟢 weekend-afternoon to 🔴 ambitious.
Every one of them teaches something real.

> **How to pick:** Choose something that fixes an *actual annoyance in your life*. You'll finish it.

---

## 🟢 Starter (an afternoon, no code)
| # | Project | Stack | What you'll learn |
|---|---|---|---|
| 1 | **Chat with your Drive**: ask questions across your docs | Claude + Google Drive connector | Connectors, grounded answers |
| 2 | **Study podcast**: turn notes into an audio overview | NotebookLM | RAG, multimodal output |
| 3 | **AI filesystem cleanup**: sort a messy folder | Claude Desktop + Filesystem MCP | Local MCP, permissions |
| 4 | **Custom assistant**: a Project with your writing style guide | Claude Projects / Custom GPT / Gem | Persistent instructions |
| 5 | **Meeting → Notion**: paste a transcript, get an action-item page | Claude + Notion connector | Cross-app actions |
| 6 | **Mini-app in chat**: budget calculator, quiz, or game | Claude Artifacts | Vibe-coding basics |
| 7 | **Personal brand kit**: logo, palette, and banner | Ideogram / Canva AI / Midjourney | Image-gen prompting |
| 8 | **Voice memo journal**: dictate, AI cleans it up and tags it | Wispr Flow / ChatGPT voice + Notes | Voice workflows |

## 🟡 Intermediate (a weekend, light config)
| # | Project | Stack | What you'll learn |
|---|---|---|---|
| 9 | **Morning digest** delivered to Slack or email | n8n ([importable](../examples/n8n-workflows/morning-ai-digest.json)) | Triggers, AI steps |
| 10 | **Idea inbox**: phone → Notion, auto-categorized | n8n + iOS Shortcut ([importable](../examples/n8n-workflows/idea-inbox-to-notion.json)) | Webhooks, structured output |
| 11 | **Inbox triage bot**: labels and drafts replies | Zapier or n8n + Gmail | Classification, human-in-the-loop |
| 12 | **Receipt → spreadsheet** expense tracker | n8n + vision model + Google Sheets | Extraction from images |
| 13 | **Multi-tool research agent** | Claude + Brave Search + Fetch + Notion MCP | Chaining MCP tools |
| 14 | **Job-hunt copilot**: score postings against your résumé | RSS + n8n + Claude + Airtable | Scoring and ranking |
| 15 | **Smart-home butler** | Home Assistant MCP + Claude | Real-world actions via MCP |
| 16 | **Weekly review skill** | Claude Code + a skill ([example](../examples/prompts-for-agents/skills/weekly-review/SKILL.md)) | Skills, agent memory |
| 17 | **Local private journal analyst** | Ollama + a Python script | Local models, privacy |
| 18 | **Content repurposer**: 1 blog post → 5 formats | Make/Zapier + Claude + Buffer | Multi-output pipelines |

## 🟠 Advanced (a few weekends, some code with AI help)
| # | Project | Stack | What you'll learn |
|---|---|---|---|
| 19 | **Your own MCP server** for a hobby API (Spotify, Strava, Pokémon, anything) | Python/TS SDK ([starter](../examples/my-first-mcp-server/)) | Tool design |
| 20 | **Expose n8n workflows as MCP tools** | n8n MCP Server Trigger + Claude | Automation ↔ agent bridge |
| 21 | **RAG chatbot over your notes** in Slack/Discord | LlamaIndex or n8n + Chroma/pgvector | Embeddings, retrieval |
| 22 | **Price tracker** with AI "is this a good deal?" analysis | Playwright/Apify + Supabase + cron | Scraping, scheduling |
| 23 | **Full web app from a prompt**: e.g., a book club tracker with logins | Lovable / Bolt + Supabase | Full-stack via AI |
| 24 | **Personal finance analyst** | CSV exports + Claude Code + Python + charts | Data analysis with agents |
| 25 | **Discord/Telegram bot** with personality and memory | Claude API + a bot library + Memory MCP | APIs, state |

## 🔴 Ambitious (stretch goals!)
| # | Project | Stack | What you'll learn |
|---|---|---|---|
| 26 | **Phone-call voice agent** that books appointments | Vapi/Retell + Claude + Calendar | Real-time voice agents |
| 27 | **Multi-agent content studio**: researcher → writer → editor → designer | Claude Agent SDK / CrewAI / LangGraph | Orchestration |
| 28 | **"Second brain" OS**: Obsidian + Memory MCP + daily automations + RAG | Everything in this guide 😄 | Systems thinking |
| 29 | **AI dungeon master** with dice (!), maps, NPC voices, and saved campaigns | Custom MCP + ElevenLabs + image gen | Creative multi-tool design |
| 30 | **Publish an MCP server** to the official registry | Your #19 project + `mcp-publisher` | Sharing with the world 🌍 |

---

## A 30-day "go deeper" plan 🗓️
| Week | Focus | Projects |
|---|---|---|
| 1 | Connectors & MCP basics | #1, #3, #5, #13 |
| 2 | Automations | #9, #10, #11 |
| 3 | Build with agents | #16, #19, #23 |
| 4 | Knowledge & capstone | #21 + pick one from 🔴 |

Share what you build! Post in communities like r/ClaudeAI, r/n8n, r/LocalLLaMA, the MCP Discord, or
X/Bluesky. People love seeing real projects, and you'll learn tons from the replies.

**Next:** [12 · Safety, Costs & Gotchas →](12-safety-costs-and-gotchas.md)
