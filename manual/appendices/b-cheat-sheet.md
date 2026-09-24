# Appendix B · The Cheat Sheet 📋

The whole manual on one page. Print it, pin it, screenshot it. 📌

---

## 🧠 Core ideas
- **Agent = model + tools + loop + stopping rule.** ([Ch. 21](../part-5-building-with-ai/21-build-your-own-agent.md))
- **Context is king.** Most AI failures are "it couldn't see what I see." Fix with connectors, MCP, docs, and memory.
- **Deterministic where you can, AI where you must.** Plain automation for moving data, and AI for the fuzzy steps.
- **Verify** anything that matters. Give AI a way to check its own work.
- **Try > read.** Ten minutes hands-on beats an hour of hot takes.

## 🔌 MCP quick reference

```bash
# Claude Code
claude mcp add --transport http <name> <url>        # remote server
claude mcp add <name> -- <command> <args...>          # local server
claude mcp list | claude mcp remove <name>            # manage
/mcp                                                  # in-session: status & OAuth login

# Test any server
npx @modelcontextprotocol/inspector <command> <args>
```

```jsonc
// Local (stdio)
"name": { "command": "npx", "args": ["-y", "@modelcontextprotocol/server-memory"] }
// Remote (HTTP)
"name": { "url": "https://mcp.example.com/mcp" }        // Cursor style
"name": { "type": "http", "url": "https://..." }         // Claude Code .mcp.json style
```

| App | Config location |
|---|---|
| Claude Desktop | Settings → Developer → Edit Config (`claude_desktop_config.json`), or Settings → Connectors for remote |
| Claude Code | `.mcp.json` (project) or `claude mcp add` |
| Cursor | `.cursor/mcp.json` or `~/.cursor/mcp.json` |
| VS Code | `.vscode/mcp.json` (`"servers"` key) |

**Starter servers:** Filesystem · Fetch · Memory · GitHub · Playwright · Context7 · Brave Search · Notion

## ⚙️ The automation pattern
```
⚡ Trigger → 📥 Gather → 🤖 AI step → 🔀 Route → 📤 Act   (+ 🧑 human approval for anything outbound)
```
| Want | Use |
|---|---|
| Fastest, most apps | Zapier |
| Visual power, good value | Make |
| Self-host, code, AI agents, local models | n8n (`npx n8n` or Docker) |

## 🧑‍💻 Claude Code essentials
| | |
|---|---|
| `Shift+Tab` | Cycle modes (incl. **plan mode**) |
| `Esc` / `Esc Esc` | Interrupt / rewind |
| `@file` · `!cmd` | Reference a file · run a shell command |
| `/init` `/clear` `/compact` | Create CLAUDE.md · fresh context · summarize |
| `/agents` `/hooks` `/plugin` `/mcp` | Subagents · hooks · plugins · MCP |
| `claude -p "..."` | Headless / scripting |
| `CLAUDE.md` | Always-on project memory |
| `.claude/skills/<name>/SKILL.md` | On-demand skills |

**Workflow:** Explore → Plan → Code → **Verify** → Commit.

## 🏷️ Picking a model
1. Start with the **workhorse tier** (fast + smart).
2. Struggling? **Move up** a tier or raise the effort.
3. Running it thousands of times? **Move down** and test.
4. Private or offline? **Local model** (Ollama / LM Studio).

## 📚 RAG in 4 moves
**Chunk → Embed → Search → Answer ("use ONLY these sources, cite them, say if you don't know")**
Not enough? Hybrid search · reranking · better chunking · or just put the whole doc in context.

## 🌐 HTTP status codes
`200` ✅ · `400` bad request · `401/403` auth · `404` not found · `429` slow down · `5xx` their problem

## 💸 Cost savers (in order)
Caching → trim input → filter before AI → batch → lower effort → smaller model → local model. **Always set spend limits.**

## 🛡️ Safety pre-flight
- [ ] Spend limit set
- [ ] Tested on a small batch
- [ ] Outbound/destructive actions need approval
- [ ] Secrets in env vars, not code or repos
- [ ] Failure alerts on
- [ ] No combination of private data + untrusted content + outbound actions without a human gate

## 🎮 Ten prompts to try right now
1. *"What are the 3 things I've worked on most this month, based on my recent files?"* (Drive/Notion connector)
2. *"Summarize my unread email: action needed, FYI, junk."*
3. *"Plan my week from my calendar and this task list. Be kind about my capacity."*
4. *"Research [topic] with 10+ sources and write a brief with citations and open questions."*
5. *"Interview me with 8 questions to turn my app idea into a spec."*
6. *"Here's my bank CSV: find forgotten subscriptions."*
7. *"Quiz me on [topic] Socratically, one question at a time."*
8. *"Analyze my writing samples and write my personal style guide."*
9. *"I'm overwhelmed. Brain dump: [...]. Sort into now/later/never and give me ONE next step."*
10. *"Build me a single-page app that [does one fun thing]. Make it beautiful."*

---

**Next:** [Appendix C · Troubleshooting FAQ →](c-troubleshooting-faq.md)
