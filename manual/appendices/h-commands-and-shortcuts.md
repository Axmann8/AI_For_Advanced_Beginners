# Appendix H · Commands & Shortcuts ⌨️⚡

> ⏱️ 10 min read · 🎯 Everyone who touches a terminal or an AI editor · 🧰 Needs: a terminal (Terminal, iTerm, PowerShell, WSL)

**Every command and keyboard shortcut from the manual, in one place.** Terminal basics for total beginners, then Claude
Code, Git, MCP, Ollama, Docker, Python and Node, n8n, and AI editors. Keep it open while you build. 🛠️

<details class="eli5" open>
<summary>🧸 ELI5: This page in 30 seconds</summary>

A terminal is a window where you type commands instead of clicking buttons. This page is a list of the most useful commands
and keyboard shortcuts, like a cheat card of magic words for your computer. 🪄⌨️

</details>

<!-- in-this-chapter -->

## 🐚 Terminal basics (start here!)

<details class="eli5">
<summary>🧸 ELI5</summary>

The first few commands everyone learns: where am I, what's here, go into a folder, make a folder.

</details>

| Command | Does | Example |
|---|---|---|
| `pwd` | Where am I? (print working directory) | `pwd` |
| `ls` (`dir` on Windows CMD) | What's in this folder? | `ls -la` (including hidden files) |
| `cd <folder>` | Go into a folder | `cd examples/weather-mcp-server` |
| `cd ..` | Go up one folder | `cd ..` |
| `mkdir <name>` | Make a folder | `mkdir my-project` |
| `cat <file>` | Show a file's contents | `cat README.md` |
| `cp` / `mv` | Copy / move (or rename) | `mv draft.md final.md` |
| `echo $VAR` | Show an environment variable | `echo $ANTHROPIC_API_KEY` |
| `export VAR=value` | Set one for this session | `export ANTHROPIC_API_KEY=sk-ant-...` |
| `which <cmd>` | Where does this program live? | `which npx` |
| `Tab` | Autocomplete names | type `cd exa` then `Tab` |
| `↑` | Previous command | |
| `Ctrl+C` | Stop the running program | |
| `clear` | Clean the screen | |

> [!TIP]
> **💡 Scared of the terminal?**
> Open Claude Code and say: *"Teach me the terminal. Give me one small task at a time, explain each command, and wait for me to
> try it."* You'll be comfortable in an afternoon. 🐚

## 🧑‍💻 Claude Code

<details class="eli5">
<summary>🧸 ELI5</summary>

The keys and commands for driving your AI coding helper.

</details>

**Keys**

| Key | Does |
|---|---|
| `Shift+Tab` | Cycle modes: normal → auto-accept edits → plan mode |
| `Esc` | Interrupt |
| `Esc` `Esc` | Rewind to an earlier point |
| `@path` | Reference a file or folder |
| `!command` | Run a shell command directly |
| `Shift+Enter` | New line without sending |

**Slash commands**

| Command | Does |
|---|---|
| `/init` | Create a starter `CLAUDE.md` |
| `/clear` | Fresh context |
| `/compact` | Summarize to free up context |
| `/context` | See what's using context |
| `/model` | Switch models |
| `/memory` | Edit memory files |
| `/permissions` | Allow or deny tools and commands |
| `/mcp` | MCP servers and OAuth logins |
| `/agents` · `/hooks` · `/plugin` | Subagents · hooks · plugins |
| `/rewind` | Return to a checkpoint |
| `/review` | Review code changes |
| `/statusline` | Customize the status bar |
| `/install-github-app` | Set up `@claude` in GitHub |
| `/doctor` · `/help` | Diagnose · everything else |

**CLI**

```bash
claude                                   # start a session
claude --continue                        # continue the last session
claude --resume                          # pick an older session
claude -p "prompt"                       # headless (print) mode
claude -p "prompt" --output-format json  # machine-readable output
claude -p "fix lint" --allowedTools "Edit,Bash(npm run lint)"
```

([Claude Code Masterclass](../part-5-building-with-ai/31-claude-code-masterclass.md), [Power-Ups](../part-5-building-with-ai/32-claude-code-power-ups.md))

## 🔌 MCP

<details class="eli5">
<summary>🧸 ELI5</summary>

Commands for adding, listing and testing AI plug-ins.

</details>

```bash
claude mcp add <name> -- <command> <args...>                 # local (stdio) server
claude mcp add --transport http <name> <url>                  # remote server
claude mcp add --scope project <name> ...                     # share via .mcp.json
claude mcp add --transport http <name> <url> --header "Authorization: Bearer <token>"
claude mcp list
claude mcp remove <name>

npx @modelcontextprotocol/inspector <command> <args>          # test any server by hand

mcp-publisher login github                                    # MCP Registry
mcp-publisher publish
```

## 🌳 Git & GitHub

<details class="eli5">
<summary>🧸 ELI5</summary>

Save-point commands for your projects, and GitHub's helper commands.

</details>

| Command | Does |
|---|---|
| `git init` | Start tracking a folder |
| `git status` · `git diff` | What changed? Show me exactly |
| `git add .` · `git commit -m "msg"` | Stage · save point |
| `git push` · `git pull` | Upload · download |
| `git log --oneline` | History |
| `git switch -c <branch>` | New branch |
| `git switch main` · `git merge <branch>` | Back to main · bring a branch in |
| `git restore .` | 🆘 Discard all uncommitted changes (permanent!) |
| `git reset --soft HEAD~1` | Undo the last commit, keep the changes |
| `git revert <sha>` | Undo a pushed commit safely |
| `git worktree add ../dir -b <branch>` | A parallel working folder (for parallel agents) |
| `git reflog` | Find "lost" commits |
| `gh auth login` · `gh repo create` | GitHub CLI: log in · create a repo |
| `gh issue view <n>` · `gh pr create` | View an issue · open a pull request |

([Git & GitHub](../part-5-building-with-ai/30-git-and-github.md))

## 🦙 Ollama & local AI

<details class="eli5">
<summary>🧸 ELI5</summary>

Commands for downloading and running AI brains on your own computer.

</details>

```bash
ollama run gemma4                    # chat
ollama pull qwen3.6:27b              # download
ollama list                          # installed models
ollama ps                            # running models
ollama rm <model>                    # delete
ollama launch claude                 # Claude Code on local models
curl http://localhost:11434/api/embed -d '{"model":"nomic-embed-text","input":"hello"}'
```

OpenAI-compatible endpoint: `http://localhost:11434/v1`. ([Local & Open Models](../part-7-local-ai/47-local-and-open-models.md))

## 🐳 Docker & the home lab

<details class="eli5">
<summary>🧸 ELI5</summary>

Commands for starting, stopping and updating the programs in your home lab.

</details>

```bash
docker compose up -d                          # start everything
docker compose ps                             # what's running
docker compose logs -f <service>              # watch logs
docker compose pull && docker compose up -d   # update
docker compose down                           # stop (data stays in volumes)
docker compose exec ollama ollama pull gemma4 # run a command inside a container
docker system df                              # disk usage
```

([The AI Home Lab](../part-7-local-ai/49-home-lab.md))

## 🐍 Python & 🟩 Node basics

<details class="eli5">
<summary>🧸 ELI5</summary>

Commands for installing and running Python and JavaScript projects, like the examples in this repo.

</details>

| Python | Node.js |
|---|---|
| `python -m venv .venv` → a private package folder | `npm install` → install dependencies |
| `source .venv/bin/activate` (Windows: `.venv\Scripts\activate`) | `npm test` / `npm start` → run scripts |
| `pip install -r requirements.txt` | `npx <tool>` → run a tool without installing |
| `python script.py` | `node file.mjs` |
| `python -m pytest` (if installed) | `npm publish --access public` |

## ⚙️ n8n

<details class="eli5">
<summary>🧸 ELI5</summary>

Commands for starting the automation tool on your computer, and its handy tricks.

</details>

```bash
npx n8n                           # quick local start → http://localhost:5678
docker run -it --rm -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
```

| Trick | How |
|---|---|
| Import a workflow | ⋯ menu → Import from File, or paste JSON onto the canvas |
| Test webhook URL | `/webhook-test/<path>` (while testing), then `/webhook/<path>` (active) |
| Insert a field | Drag it from the input panel into an expression |
| See what happened | **Executions** tab |

## ✍️ AI editors (Cursor & VS Code)

<details class="eli5">
<summary>🧸 ELI5</summary>

Keyboard shortcuts for code editors with AI helpers.

</details>

| Action | Cursor | VS Code + Copilot |
|---|---|---|
| Accept a suggestion | `Tab` | `Tab` |
| Inline edit | `Cmd/Ctrl+K` | `Cmd/Ctrl+I` |
| Open the AI chat / agent panel | `Cmd/Ctrl+L` (or `Cmd/Ctrl+I`) | `Ctrl+Cmd+I` (Mac) / `Ctrl+Alt+I` (Windows) |
| Command palette | `Cmd/Ctrl+Shift+P` | `Cmd/Ctrl+Shift+P` |
| Mention context | `@file`, `@docs`, `@web` | `#file` and `@`-participants |

Shortcuts change between versions. Check each editor's keyboard shortcuts screen if one doesn't work
([Cursor & AI IDEs](../part-5-building-with-ai/33-cursor-and-ai-ides.md)).

## 🏗️ This repo's kits

<details class="eli5">
<summary>🧸 ELI5</summary>

The exact commands to run every example project in this repository.

</details>

```bash
# Python MCP server
cd examples/my-first-mcp-server && pip install -r requirements.txt && python smoke_test.py
# Weather MCP server (JS, publishable)
cd examples/weather-mcp-server && npm install && npm test && npm run inspect
# Build-your-own agent
cd examples/build-your-own-agent && pip install -r requirements.txt && python agent.py "question"
# RAG from scratch
cd examples/rag-from-scratch && python rag.py --search "descale the coffee machine"
# Research agent
cd examples/research-agent && python test_research_agent.py && python research_agent.py --depth quick "question"
# Newsletter pipeline
cd examples/newsletter-pipeline && python test_newsletter.py && python newsletter.py --dry-run
# Home lab
cd examples/homelab && docker compose up -d
# This manual's website, locally
pip install -r requirements-docs.txt && mkdocs serve
```

---

**Next:** [Appendix I · Comparison Tables →](i-comparison-tables.md)
