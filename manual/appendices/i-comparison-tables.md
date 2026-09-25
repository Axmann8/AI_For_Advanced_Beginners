# Appendix I · Comparison Tables ⚖️📊

> ⏱️ 12 min read · 🎯 Anyone choosing a tool · 🧰 Needs: nothing

**"Which one should I use?" This page answers that question for every category in the manual, side by side.** The ratings are
friendly rules of thumb, not lab results. Tools change fast, so treat these as a starting shortlist and let
[your own eval](../part-12-mastery/105-evaluating-ai.md) pick the winner. ⚖️

> [!NOTE]
> **📌 A snapshot, not a scoreboard**
> These comparisons reflect the landscape as of September 2026. Leaders shift every few months, and sometimes tools disappear
> entirely. The *questions* in each table ("do I need self-hosting?", "do I care about privacy?") age much better than the
> answers.

<details class="eli5" open>
<summary>🧸 ELI5: This page in 30 seconds</summary>

When you're picking between toys at a shop, it helps to see them side by side. These tables put similar AI tools next to each
other, so you can quickly see which is best for what you want to do. 🛍️

</details>

<!-- in-this-chapter -->

## 🧠 AI assistants

<details class="eli5">
<summary>🧸 ELI5</summary>

The big chat apps, and what each is especially good at.

</details>

| | Claude | ChatGPT | Gemini | Microsoft Copilot | Perplexity |
|---|---|---|---|---|---|
| **Especially good at** | Writing, reasoning, coding, long documents | All-rounder, huge ecosystem, voice | Google apps, long video and documents | Microsoft 365 work | Fast answers with sources |
| **Coding** | ⭐⭐⭐ (Claude Code) | ⭐⭐⭐ (Codex) | ⭐⭐⭐ (Gemini CLI) | ⭐⭐ | ⭐ |
| **Connects to your apps** | Connectors + MCP | Plugins + connectors | Google Workspace | Microsoft 365 | Some connectors |
| **Research mode** | ✅ | ✅ | ✅ | ✅ | ✅ (its core) |
| **Standout extra** | Artifacts, Projects, skills | Image generation, agent mode | Gemini Notebook, video understanding | Deep Office integration | Citations everywhere |

More: [The AI Landscape](../part-3-foundations/35-the-ai-landscape.md), [Choosing Your AI Stack](../part-3-foundations/37-choosing-your-ai-stack.md).

## ⚙️ Automation platforms

<details class="eli5">
<summary>🧸 ELI5</summary>

The robot-recipe builders, compared on ease, power and price style.

</details>

| | Zapier | Make | n8n | Power Automate |
|---|---|---|---|---|
| **Ease for beginners** | ⭐⭐⭐ | ⭐⭐ | ⭐⭐ | ⭐⭐ |
| **Power & flexibility** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| **App integrations** | ⭐⭐⭐ (most) | ⭐⭐⭐ | ⭐⭐ (+ any HTTP API) | ⭐⭐ (Microsoft-first) |
| **AI agents** | ✅ | ✅ | ✅ (very strong) | ✅ (Copilot Studio) |
| **Self-hosting** | ❌ | ❌ | ✅ | ❌ |
| **Billing unit** | Tasks (per step) | Operations/credits | Executions (per run) | Per user/flow |
| **Pick it when** | You want it working in 10 minutes | You want visual power at good value | You want control, code and local models | You live in Microsoft 365 |

More: [Automation Platforms](../part-5-automation/45-automation-platforms.md).

## 🛠️ AI coding tools

<details class="eli5">
<summary>🧸 ELI5</summary>

Tools that build apps for you, from "describe it" websites to coding helpers in your terminal.

</details>

| Tool | Type | Best for | Coding needed |
|---|---|---|---|
| **Claude Artifacts** | Chat-to-app | Tiny apps and games in chat | None |
| **Lovable / Bolt / v0 / Replit** | Chat-to-app | Full apps in the browser, fast | None to little |
| **Cursor** | AI editor | Seeing and steering code, Tab predictions | Some |
| **VS Code + Copilot** | AI editor | The standard editor with AI everywhere | Some |
| **Claude Code** | Agent (terminal, IDE, desktop, web) | Big tasks, non-code chores, automation | None to start |
| **Codex / Gemini CLI** | Agent | Similar agentic workflows in other ecosystems | None to start |
| **Aider / Cline / OpenCode** | Open-source agents | Bring-your-own-model, local models | Some |

More: [Agents & AI Coding Tools](../part-7-building-with-ai/60-agents-and-coding-tools.md), [Cursor & AI IDEs](../part-7-building-with-ai/64-cursor-and-ai-ides.md).

## 🧱 Agent frameworks

<details class="eli5">
<summary>🧸 ELI5</summary>

LEGO sets for building your own AI helpers, and what each one is best at.

</details>

| Framework | Language | Superpower | Pick it when |
|---|---|---|---|
| **Claude Agent SDK** | Python, TS | Claude Code's harness (files, bash, subagents, MCP) | You want a Claude Code-grade agent in your app |
| **OpenAI Agents SDK** | Python, TS | Simple agents + handoffs + tracing | You like minimal and friendly |
| **LangGraph** | Python, JS | Graphs with state, checkpoints, human-in-the-loop | You need control and resumable flows |
| **CrewAI** | Python | Role-based crews | Teams of specialists |
| **Pydantic AI** | Python | Type-safe, validated outputs | Clean Python apps |
| **Vercel AI SDK / Mastra** | TypeScript | Web-native streaming, workflows | Building web apps |
| **n8n AI Agent** | Visual | No-code agents in workflows | Business automations |

More: [Agent Frameworks Tour](../part-7-building-with-ai/69-agent-frameworks-tour.md).

## 🏠 Local AI runners

<details class="eli5">
<summary>🧸 ELI5</summary>

Apps for running AI on your own computer, from simple to super-powerful.

</details>

| Tool | Interface | Best for |
|---|---|---|
| **Ollama** | Terminal + API | The standard; scripts, n8n, Claude Code via `ollama launch` |
| **LM Studio** | Desktop app | Browsing and trying models visually |
| **Jan** | Desktop app | A private ChatGPT-style app |
| **Open WebUI** | Web app | A private ChatGPT for your household or team |
| **llama.cpp** | Engine | Maximum control |
| **MLX** | Apple framework | Speed on Apple Silicon |
| **vLLM / SGLang** | Server | Serving many users on GPUs |

More: [Local & Open Models](../part-9-local-ai/78-local-and-open-models.md).

## 💻 Hardware for local AI

<details class="eli5">
<summary>🧸 ELI5</summary>

Which kinds of computers are best for running AI at home.

</details>

| | Apple Silicon Mac | PC + NVIDIA GPU | Unified-memory mini PC | Raspberry Pi |
|---|---|---|---|---|
| **Biggest models that fit** | ⭐⭐⭐ (lots of unified memory) | ⭐⭐ (VRAM-limited) | ⭐⭐⭐ (up to ~128 GB) | ⭐ |
| **Speed** | ⭐⭐ (⭐⭐⭐ on Max/Ultra chips) | ⭐⭐⭐ | ⭐⭐ | ⭐ |
| **Image & video generation** | ⭐⭐ | ⭐⭐⭐ | ⭐⭐ | ❌ |
| **Quiet & efficient** | ⭐⭐⭐ | ⭐ | ⭐⭐ | ⭐⭐⭐ |
| **Upgradeable** | ❌ | ✅ | ❌ | ❌ |

More: [Hardware for Local AI](../part-9-local-ai/79-hardware-for-local-ai.md).

## 🗄️ Vector databases

<details class="eli5">
<summary>🧸 ELI5</summary>

Databases that find things by meaning, from tiny ones for learning to giant ones for big apps.

</details>

| Tool | Style | Best for |
|---|---|---|
| **Chroma** | Embedded (Python) | Learning and prototypes |
| **LanceDB / sqlite-vec** | Embedded, file-based | Local and portable projects |
| **pgvector** (Supabase, Neon) | Postgres extension | Vectors next to your normal data |
| **Qdrant / Weaviate / Milvus** | Open-source servers | Scale, filtering, hybrid search |
| **Pinecone / Turbopuffer** | Managed | Zero ops at huge scale |
| **Elasticsearch / OpenSearch** | Search engine | Great keyword + vector hybrid |

More: [Embeddings & Vector Databases](../part-8-knowledge-and-memory/73-embeddings-and-vector-databases.md).

## 📚 Note apps for a second brain

<details class="eli5">
<summary>🧸 ELI5</summary>

Notebook apps compared, so you can pick where to keep your notes.

</details>

| | Obsidian | Notion | Google Docs | Apple Notes |
|---|---|---|---|---|
| **You own the files** | ✅ (Markdown) | Export | Export | Export |
| **Databases** | Plugins | ⭐⭐⭐ | ❌ | ❌ |
| **Built-in AI** | Plugins | ⭐⭐⭐ (agents) | Gemini | Apple Intelligence |
| **AI access from outside** | Filesystem MCP, Claude Code | Official MCP | Connectors | Limited |
| **Privacy / local AI** | ⭐⭐⭐ | ⭐ | ⭐ | ⭐⭐ |
| **Teams** | ⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐ |

More: [Personal Knowledge Management](../part-8-knowledge-and-memory/77-personal-knowledge-management.md).

## 🎨 Creative tools

<details class="eli5">
<summary>🧸 ELI5</summary>

The best tools for pictures, videos, voices and music, side by side.

</details>

| Need | Great picks |
|---|---|
| **Instruction-following images & editing** | ChatGPT (GPT Image), Gemini (Nano Banana) |
| **Artistic images** | Midjourney |
| **Photoreal & open models** | FLUX |
| **Text in images** | Ideogram |
| **Vectors & icons** | Recraft |
| **Cinematic video with sound** | Veo, Kling, Seedance |
| **Pro video editing & control** | Runway |
| **Voices & dubbing** | ElevenLabs |
| **Songs with vocals** | Suno |
| **Edit by transcript** | Descript |

More: [The Multimodal Playground](../part-10-creative-ai/83-multimodal-playground.md).

## 🗣️ Voice-agent platforms

<details class="eli5">
<summary>🧸 ELI5</summary>

Websites for building phone robots, compared.

</details>

| | Vapi | Retell | ElevenLabs Agents | LiveKit / Pipecat |
|---|---|---|---|---|
| **Setup** | No-code + API | No-code + API | No-code + API | Code (open source) |
| **Phone numbers** | ✅ | ✅ | ✅ | Via telephony providers |
| **Bring your own LLM** | ✅ | ✅ | ✅ | ✅ |
| **Voices** | Many providers | Many providers | ⭐⭐⭐ | Any |
| **Pick it when** | Flexible dev-friendly agents | Business phone calls | The best voices | Full control, self-hosting |

More: [Voice Agents](../part-10-creative-ai/87-voice-agents.md).

## 🌍 Hosting

<details class="eli5">
<summary>🧸 ELI5</summary>

Places to put your apps on the internet, and which kind of app each one suits.

</details>

| Host | Static sites | Web apps | Always-on bots | Free tier |
|---|---|---|---|---|
| **GitHub Pages** | ✅ | ❌ | ❌ | ✅ |
| **Netlify / Cloudflare Pages** | ✅ | ✅ (functions) | ❌ | ✅ |
| **Vercel** | ✅ | ✅ (Next.js ⭐) | ❌ | ✅ |
| **Render / Railway / Fly.io** | ✅ | ✅ | ✅ | Some |
| **A VPS or home server** | ✅ | ✅ | ✅ | Your hardware |

More: [Deploying & Hosting](../part-7-building-with-ai/66-deploying-and-hosting.md).

## 💳 Subscription vs. API vs. local

<details class="eli5">
<summary>🧸 ELI5</summary>

Three ways to pay for AI: a monthly plan, pay-per-use, or run it at home for free.

</details>

| | Subscription (Pro, Plus…) | API (pay per token) | Local model |
|---|---|---|---|
| **Cost style** | Fixed monthly, with usage limits | Pay per use | Hardware + electricity |
| **Best for** | Daily chatting, coding with Claude Code | Apps, automations, bots | Privacy, bulk work, offline |
| **Privacy** | Settings-dependent | Business terms (usually no training) | ✅ Stays home |
| **Quality** | Frontier | Frontier | Good and improving |
| **Watch out for** | Hitting limits | Surprise bills (set spend limits!) | Slower on small machines |

More: [Cost Optimization](../part-12-mastery/106-cost-optimization.md).

## 🔌 MCP: local vs. remote servers

<details class="eli5">
<summary>🧸 ELI5</summary>

AI plug-ins can live on your computer or on the internet. Each way has pros and cons.

</details>

| | Local (stdio) | Remote (Streamable HTTP) |
|---|---|---|
| **Runs** | On your machine, launched by the app | On a server, reached by URL |
| **Works from phone / web** | ❌ | ✅ |
| **Access to local files** | ✅ | ❌ (unless you build it) |
| **Auth** | Your machine's permissions | OAuth or tokens |
| **Install for others** | `npx` / `uvx` one-liner | Paste a URL |
| **Best for** | Filesystem, local apps, dev tools | SaaS integrations, sharing, mobile |

More: [MCP Under the Hood](../part-4-mcp-and-connectors/39-mcp-under-the-hood.md), [Building MCP Servers](../part-4-mcp-and-connectors/42-building-mcp-servers.md).

---

**Next:** [Appendix J · Printable Checklists →](j-checklists.md)
