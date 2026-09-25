# Appendix B · The Cheat Sheet 📋

> ⏱️ 10 min read · 🎯 Everyone · 🧰 Needs: a printer or a screenshot button 😄

**The whole manual, squeezed onto (a very long) one page.** Every section here is a reminder of a full chapter, so when a line
makes you think *"wait, how does that work?"*, follow the link. Print it, pin it, screenshot it. 📌

<details class="eli5" open>
<summary>🧸 ELI5: This page in 30 seconds</summary>

This is the "tiny notes" version of the whole book, like the notes you'd bring into a test if the teacher allowed it. Each
little box reminds you of a big idea. 📝

</details>

<!-- in-this-chapter -->

## 🧠 The core ideas

<details class="eli5">
<summary>🧸 ELI5</summary>

The biggest lessons of the whole manual, in six lines.

</details>

- **Agent = model + tools + loop + stopping rule.** ([Build Your Own Agent](../part-5-building-with-ai/37-build-your-own-agent.md))
- **Context is king.** Most AI failures are "it couldn't see what I see." Fix with connectors, MCP, documents and memory.
- **Deterministic where you can, AI where you must.** Plain automation moves data, and AI does the fuzzy steps.
- **Verify** anything that matters. Give AI a way to check its own work.
- **Approve before acting** on anything that sends, deletes, pays or publishes.
- **Try > read.** Ten minutes hands-on beats an hour of hot takes.

## 🪜 The knowledge ladder

<details class="eli5">
<summary>🧸 ELI5</summary>

Six ways to teach AI your stuff, from easiest to hardest.

</details>

**Paste it → Projects → Gemini Notebook → Connectors/MCP → Memory → Build your own RAG**
([RAG, Memory & Knowledge](../part-6-knowledge-and-memory/41-rag-memory-and-knowledge.md))

A few documents? **Paste them.** A study pile? **Gemini Notebook.** Live work data? **Connectors.** A huge private collection
in your own app? **RAG.**

## 🔌 MCP quick reference

<details class="eli5">
<summary>🧸 ELI5</summary>

The commands and settings for plugging new tools into your AI apps.

</details>

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
([MCP Server Catalog](../part-2-mcp-and-connectors/09-mcp-server-catalog.md))

## ⚙️ The automation pattern

<details class="eli5">
<summary>🧸 ELI5</summary>

Every robot recipe looks the same: something happens, gather info, let AI think, decide where it goes, then do something.

</details>

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

<details class="eli5">
<summary>🧸 ELI5</summary>

The most useful keys and commands for your AI coding helper.

</details>

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

**Workflow:** Explore → Plan → Code → **Verify** → Commit. ([Masterclass](../part-5-building-with-ai/31-claude-code-masterclass.md))

## 🌳 Git in 8 commands

<details class="eli5">
<summary>🧸 ELI5</summary>

The save-point commands you'll use every day.

</details>

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

([Git & GitHub](../part-5-building-with-ai/30-git-and-github.md))

## 🐍 API quick reference

<details class="eli5">
<summary>🧸 ELI5</summary>

The smallest program that talks to Claude, plus the key settings.

</details>

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

([Calling AI APIs](../part-5-building-with-ai/36-calling-ai-apis.md))

## 🏷️ Picking a model

<details class="eli5">
<summary>🧸 ELI5</summary>

Start with a good all-rounder, go bigger for hard jobs, smaller for simple repeated jobs, and home AI for secrets.

</details>

1. Start with the **workhorse tier** (fast + smart).
2. Struggling? **Move up** a tier or raise the effort.
3. Running it thousands of times? **Move down** and test with your eval.
4. Private or offline? **Local model** (Ollama / LM Studio).

## 🏠 Local AI in 5 commands

<details class="eli5">
<summary>🧸 ELI5</summary>

The commands for running AI on your own computer.

</details>

```bash
ollama run gemma4          # chat with a local model
ollama pull qwen3.6:27b    # get another model
ollama list                # installed models
ollama ps                  # what's running
ollama launch claude       # Claude Code on local models
```

**Memory rule:** ~0.6 GB per billion parameters at 4-bit, plus headroom. ([Hardware](../part-7-local-ai/48-hardware-for-local-ai.md))

## 📚 RAG in 4 moves

<details class="eli5">
<summary>🧸 ELI5</summary>

Cut into cards, give each card a meaning-address, find the best cards, answer only from them.

</details>

**Chunk → Embed → Search → Answer ("use ONLY these sources, cite them, say if you don't know")**

Not enough? Hybrid search · reranking · contextual chunks · agentic retrieval · or just put the whole doc in context.

## 🌐 HTTP status codes

<details class="eli5">
<summary>🧸 ELI5</summary>

The number codes websites send back: 200 means "yay," 400s mean "you made a mistake," 500s mean "they made a mistake."

</details>

`200` ✅ · `201` created · `400` bad request · `401/403` auth problem · `404` not found · `429` slow down · `5xx` their problem

## 💸 Cost savers (in order)

<details class="eli5">
<summary>🧸 ELI5</summary>

Ways to spend less on AI, starting with the ones that don't make anything worse.

</details>

Caching → trim input → filter before AI → dedupe → batch → lower effort → smaller model (routing) → local model.
**Always set spend limits.** ([Cost Optimization](../part-10-mastery/75-cost-optimization.md))

## 🛡️ Safety pre-flight

<details class="eli5">
<summary>🧸 ELI5</summary>

Check these before letting a robot run by itself.

</details>

- [ ] Spend limit set
- [ ] Tested on a small batch
- [ ] Outbound/destructive actions need approval
- [ ] Secrets in env vars, not code or repos
- [ ] Failure alerts on
- [ ] No **private data + untrusted content + outbound actions** without a human gate (the lethal trifecta)

## 🚦 Privacy traffic lights

<details class="eli5">
<summary>🧸 ELI5</summary>

Green is fine to share, yellow needs care, red never (or only with home AI).

</details>

| 🟢 Share freely | 🟡 Share with care | 🔴 Never (or go local) |
|---|---|---|
| General questions, public info, your creative writing | Work docs (approved tools), redacted finances, health questions without IDs | Passwords, card and ID numbers, others' private info, confidential client data |

([Privacy & Your Data](../part-10-mastery/73-privacy-and-your-data.md))

## 🧪 The 15-minute eval

<details class="eli5">
<summary>🧸 ELI5</summary>

Test AIs fairly: same questions, clear scoring, no peeking.

</details>

10–20 real tasks → write what "good" means → run each option → **score blind** → tally quality, cost and speed.
([Evaluating AI](../part-10-mastery/74-evaluating-ai.md))

## 🎓 Learning with AI

<details class="eli5">
<summary>🧸 ELI5</summary>

Use AI as a coach that asks questions, not a machine that does your homework.

</details>

Try first → ask for hints, not answers → explain it back (Feynman) → quiz yourself (active recall) → flashcards (spaced
repetition) → verify important facts. ([Research & Learning](../part-9-ai-for-life-and-work/60-research-and-learning.md))

## 🎮 Ten prompts to try right now

<details class="eli5">
<summary>🧸 ELI5</summary>

Ten ready-to-copy questions that show off what AI can do.

</details>

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
