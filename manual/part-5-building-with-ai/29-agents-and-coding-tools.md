# 17 · Agents & AI Coding Tools: Become a Builder 🛠️

Here's the secret: **you don't need to be a programmer to build software anymore.** Coding agents
write, run, test, and fix code for you. Even if you never plan to "code," these tools are the
fastest way to build your own automations, MCP servers, and little apps.

---

## The spectrum

```
Chat-to-app builders ──── AI editors ──── Terminal/cloud agents ──── Agent frameworks
(describe it, get an app)  (you + AI in code)  (AI does whole tasks)      (build your own agents)
   Lovable, Bolt, v0        Cursor, VS Code     Claude Code, Codex        Claude Agent SDK, LangGraph
```

## 🪄 Chat-to-app builders (no code needed)
| Tool | Sweet spot |
|---|---|
| **Claude Artifacts** | Interactive mini-apps, dashboards, and games, right in chat, shareable by link |
| **Lovable** | Full web apps with auth and a database (Supabase), from a description |
| **Bolt.new** | Full-stack apps in the browser, deploy in a click |
| **v0 (Vercel)** | Gorgeous React/Next.js UIs and apps |
| **Replit Agent** | Build, host, and deploy in one place, with a mobile app too |
| **Google AI Studio / Firebase Studio** | Prototype Gemini-powered apps fast |

**🎮 Try:** *"Build me a habit tracker with streaks, confetti when I complete all habits, and a dark mode."*

## ✍️ AI code editors
| Tool | Notes |
|---|---|
| **Cursor** | The most popular AI-first editor (a VS Code fork), with agent mode, background agents, and MCP |
| **VS Code + GitHub Copilot** | Agent mode, MCP gallery, coding agent that opens PRs from issues |
| **Windsurf** | An agentic IDE with its "Cascade" agent |
| **Zed** | A fast editor with built-in agents and MCP |
| **JetBrains AI / Junie** | For IntelliJ/PyCharm fans |

## 🤖 Autonomous coding agents (terminal and cloud)
| Tool | Notes |
|---|---|
| **Claude Code** | Anthropic's agent for your terminal, IDE, desktop, web, and phone. It reads your whole project, runs commands, and ships features. (This repo was built by it! 👋) |
| **OpenAI Codex** | CLI plus cloud agent, integrated with ChatGPT |
| **Gemini CLI** | Google's open-source terminal agent |
| **GitHub Copilot coding agent** | Assign an issue, get a PR |
| **Aider** | Open-source, git-native pair programmer, works with any model |
| **Cline / Roo Code / Kilo Code** | Open-source agents inside VS Code, bring-your-own-model |
| **Goose** | Open-source, MCP-centric local agent |
| **Devin, Jules** | Cloud "AI software engineers" for async tasks |

## 🧩 Customizing agents: the power-user layer
This is where agents go from "helpful" to "*my* helpful." Using Claude Code terms (most tools have equivalents):

| Feature | What it does | Example |
|---|---|---|
| **`CLAUDE.md` / `AGENTS.md`** | Always-on project memory | "Run tests with `pytest`. Never touch `/legacy`." ([example](../../examples/prompts-for-agents/CLAUDE.md)) |
| **Skills** | On-demand playbooks plus scripts | A `weekly-review` skill ([example](../../examples/prompts-for-agents/skills/weekly-review/SKILL.md)) |
| **Slash commands** | Saved prompts you trigger with `/name` | `/changelog`, `/fix-issue 123` |
| **Subagents** | Specialist helpers with their own context and tools | A "code reviewer" or "test writer" subagent |
| **Hooks** | Shell commands that run automatically on events | Auto-format after every edit, block edits to `.env` |
| **MCP servers** | External tools | GitHub, Playwright, your DB |
| **Plugins** | Bundles of all of the above | Install a team's whole setup in one command |
| **Headless / SDK mode** | Run the agent from scripts, cron, or CI | `claude -p "summarize today's errors" --output-format json` |

## 🏗️ Agent frameworks: build your own
When you want an agent inside *your* app or script:
- **Claude Agent SDK** (Python/TS): the same harness that powers Claude Code, with tools, MCP,
  subagents, and context management built in.
- **OpenAI Agents SDK**: lightweight multi-agent orchestration with handoffs.
- **LangGraph**: graph-based, stateful agents with fine control.
- **CrewAI**: role-based "crews" of agents.
- **Pydantic AI, Mastra (TS), Google ADK, Microsoft Agent Framework, smolagents (Hugging Face)**: more solid options.
- **Vercel AI SDK**: the go-to for AI features in web apps.

> 💡 **Build-vs-configure tip:** Try configuring an existing agent (Claude Code + skills + MCP) *before*
> writing a framework-based agent. You'll get 80% of the way there with 5% of the effort.

## 🎯 How to work with coding agents like a pro
1. **Plan first.** Ask for a plan (Claude Code has a plan mode), review it, *then* let it build.
2. **Give it a way to check its work**: tests, a linter, a screenshot via Playwright. Agents that can
   verify their output are dramatically better.
3. **Small steps, frequent commits.** Git is your undo button.
4. **Let it explain.** "Walk me through what you changed and why" is how you level up fast.
5. **Run things in parallel.** Cloud agents can work on 3 tasks while you have lunch. 🥪

---

### 🚀 Try this next
Install Claude Code (or open Cursor), `cd` into this repo, and ask:
> *"Add a `weather` tool to the Pocket Toolkit MCP server using the free Open-Meteo API, then test it."*

Congrats, you just extended an MCP server with an AI pair programmer.

**Next:** [18 · The Claude Code Masterclass →](31-claude-code-masterclass.md)
