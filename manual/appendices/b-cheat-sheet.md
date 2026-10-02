# Appendix B · The Cheat Sheet 📋

> ⏱️ 10 min read · 🎯 Everyone · 🧰 Needs: a printer or a screenshot button 😄

**The whole manual, squeezed onto (a very long) one page.** Every section here is a reminder of a full chapter, so when a line
makes you think *"wait, how does that work?"*, follow the link. Print it, pin it, screenshot it. 📌

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

This cheat sheet condenses the manual's most important ideas, commands and checklists into quick-reference sections. Each section links to the chapter with full details.

- **Use it as a refresher** after reading the relevant chapters.
- **Print it** and keep it nearby while you work.

</details>

<!-- in-this-chapter -->

## 🧠 The core ideas

- **Agent = model + tools + loop + stopping rule.** ([Build Your Own Agent](../part-7-building-with-ai/68-build-your-own-agent.md))
- **Context is king.** Most AI failures are "it couldn't see what I see." Fix with connectors, MCP, documents and memory.
- **Deterministic where you can, AI where you must.** Plain automation moves data, and AI does the fuzzy steps.
- **Verify** anything that matters. Give AI a way to check its own work.
- **Approve before acting** on anything that sends, deletes, pays or publishes.
- **Try > read.** Ten minutes hands-on beats an hour of hot takes.

## 🤖 Assistant quick reference

| Want… | 💬 ChatGPT | ✨ Gemini | 🧡 Claude | 🪟 Copilot | 🔎 Perplexity |
|---|---|---|---|---|---|
| Tell it about you | Settings → Personalization | Settings → Personal context | Settings → Profile | Settings → Memory | Settings → Personalization |
| A reusable helper | Projects (skills) | Gems | Projects | Microsoft 365 agents | Spaces |
| Private one-off chat | Temporary chat | Temporary chat | Incognito 👻 | Settings → Privacy | Incognito |
| Talk out loud | Voice (waveform icon) | Live | Voice icon | Microphone | Voice mode |
| Deep research | Tools → Deep research | Tools → Deep Research | Research | Researcher (365 Premium) | Research mode |
| Images | Just ask / Images | Just ask (Nano Banana) | ➖ (diagrams only) | Just ask | Pro: just ask |
| Stop training on my chats | Data controls | Gemini Apps Activity | Privacy | Privacy | Preferences |

Full guides: [Part II · The AI Assistants Field Guide](../part-2-ai-assistants-field-guide/index.md).

## 🪜 The knowledge ladder

**Paste it → Projects → Gemini Notebook → Connectors/MCP → Memory → Build your own RAG**
([RAG, Memory & Knowledge](../part-8-knowledge-and-memory/72-rag-memory-and-knowledge.md))

A few documents? **Paste them.** A study pile? **Gemini Notebook.** Live work data? **Connectors.** A huge private collection
in your own app? **RAG.**

## 🔌 MCP quick reference

```bash
# Claude Code
claude mcp add --transport http <name> <url>        # remote server
claude mcp add <name> -- <command> <args...>          # local server
claude mcp list        # see servers
claude mcp remove <name>
/mcp                   # in-session: status & OAuth login

# Test any server by hand
npx @modelcontextprotocol/inspector <command> <args>
```

| App | Config location |
|---|---|
| Claude Desktop | Settings → Connectors (remote), or Settings → Developer → Edit Config (`claude_desktop_config.json`) |
| Claude Code | `.mcp.json` (project) or `claude mcp add` |
| Cursor | `.cursor/mcp.json` or `~/.cursor/mcp.json` |
| VS Code | `.vscode/mcp.json` (`"servers"` key) |

**Starter servers:** Filesystem · Fetch · Memory · GitHub · Playwright · a docs server · a search server · Notion
([MCP Server Catalog](../part-4-mcp-and-connectors/40-mcp-server-catalog.md))

## ⚙️ The automation pattern

```
⚡ Trigger → 📥 Gather → 🤖 AI step → 🔀 Route → 📤 Act   (+ 🧑 human approval for anything outbound)
```

| Want | Use |
|---|---|
| Fastest, most apps | Zapier |
| Visual power, good value | Make |
| Self-host, code, AI agents, local models | n8n (`npx n8n` or Docker) |
| Phone and desktop | Shortcuts, Tasker, Power Automate |

## 🧑‍💻 Claude Code essentials

| Key / command | Does |
|---|---|
| `Shift+Tab` | Cycle modes (incl. **plan mode**) |
| `Esc` / `Esc Esc` | Interrupt / rewind |
| `@file` · `!cmd` | Reference a file · run a shell command |
| `/init` · `/clear` · `/compact` · `/context` | Create CLAUDE.md · fresh context · summarize · see what's using context |
| `/agents` · `/hooks` · `/plugin` · `/mcp` | Subagents · hooks · plugins · MCP |
| `claude -p "..."` | Headless / scripting |
| `CLAUDE.md` | Always-on project memory |
| `.claude/skills/<name>/SKILL.md` | On-demand skills |
| `.claude/commands/<name>.md` | Your own slash commands |

**Workflow:** Explore → Plan → Code → **Verify** → Commit. ([Masterclass](../part-7-building-with-ai/62-claude-code-masterclass.md))

## 🌳 Git in 8 commands

```bash
git status          # what changed?
git diff            # show me exactly
git add . && git commit -m "message"   # save point
git push            # upload
git switch -c idea  # new branch for an experiment
git restore .       # 🆘 undo all uncommitted changes
git revert <sha>    # undo a pushed commit safely
git log --oneline   # history
```

([Git & GitHub](../part-7-building-with-ai/61-git-and-github.md))

## 🐍 API quick reference

```python
import anthropic
client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY
r = client.messages.create(model="claude-opus-5", max_tokens=16000,
                           messages=[{"role": "user", "content": "Hello!"}])
print(r.content[0].text, r.usage)
```

| Need | Use |
|---|---|
| Live typing effect | `client.messages.stream(...)` |
| Data, not prose | `client.messages.parse(..., output_format=MyModel)` |
| Your own tools | `@beta_tool` + `client.beta.messages.tool_runner(...)` |
| Web search | a server tool (`"type": "web_search_…"`, check the current version) |
| Cheaper repeats | `cache_control` on long, stable prompt parts |
| Bulk, not urgent | the Batch API |

([Calling AI APIs](../part-7-building-with-ai/67-calling-ai-apis.md))

## 🏷️ Picking a model

1. Start with the **workhorse tier** (fast + smart).
2. Struggling? **Move up** a tier or raise the effort.
3. Running it thousands of times? **Move down** and test with your eval.
4. Private or offline? **Local model** (Ollama / LM Studio).

## 🏠 Local AI in 5 commands

```bash
ollama run gemma4          # chat with a local model
ollama pull qwen3.6:27b    # get another model
ollama list                # installed models
ollama ps                  # what's running
ollama launch claude       # Claude Code on local models
```

**Memory rule:** ~0.6 GB per billion parameters at 4-bit, plus headroom. ([Hardware](../part-9-local-ai/79-hardware-for-local-ai.md))

## 📚 RAG in 4 moves

**Chunk → Embed → Search → Answer ("use ONLY these sources, cite them, say if you don't know")**

Not enough? Hybrid search · reranking · contextual chunks · agentic retrieval · or just put the whole doc in context.

## 🌐 HTTP status codes

`200` ✅ · `201` created · `400` bad request · `401/403` auth problem · `404` not found · `429` slow down · `5xx` their problem

## 💸 Cost savers (in order)

Caching → trim input → filter before AI → dedupe → batch → lower effort → smaller model (routing) → local model.
**Always set spend limits.** ([Cost Optimization](../part-12-mastery/106-cost-optimization.md))

## 🛡️ Safety pre-flight

- [ ] Spend limit set
- [ ] Tested on a small batch
- [ ] Outbound/destructive actions need approval
- [ ] Secrets in env vars, not code or repos
- [ ] Failure alerts on
- [ ] No **private data + untrusted content + outbound actions** without a human gate (the lethal trifecta)

## 🚦 Privacy traffic lights

| 🟢 Share freely | 🟡 Share with care | 🔴 Never (or go local) |
|---|---|---|
| General questions, public info, your creative writing | Work docs (approved tools), redacted finances, health questions without IDs | Passwords, card and ID numbers, others' private info, confidential client data |

([Privacy & Your Data](../part-12-mastery/104-privacy-and-your-data.md))

## 🧪 The 15-minute eval

10–20 real tasks → write what "good" means → run each option → **score blind** → tally quality, cost and speed.
([Evaluating AI](../part-12-mastery/105-evaluating-ai.md))

## 🎓 Learning with AI

Try first → ask for hints, not answers → explain it back (Feynman) → quiz yourself (active recall) → flashcards (spaced
repetition) → verify important facts. ([Research & Learning](../part-11-ai-for-life-and-work/91-research-and-learning.md))

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

Hundreds more in the [Prompt Library](d-prompt-library.md). 💬

---

**Next:** [Appendix C · Troubleshooting FAQ →](c-troubleshooting-faq.md)
