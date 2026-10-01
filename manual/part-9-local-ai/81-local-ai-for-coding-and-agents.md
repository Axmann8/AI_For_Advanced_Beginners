# 81 · Local AI for Coding & Agents: Private Pair Programming 🔒💻

> ⏱️ 7 min read · 🎯 Intermediate · 🧰 Needs: Ollama or LM Studio, a code editor, and ideally 32 GB+ of memory ([Hardware](79-hardware-for-local-ai.md))

**Can you get AI coding help without sending a single line of code to the cloud? Yes, and it's getting better fast.**
Local models now power autocomplete, chat, and even agent tools like Cline, Aider, and Claude Code itself (via Ollama's
Anthropic-compatible API). This chapter shows you the setups, which models work best, how to size context, and, just as
importantly, where local agents still struggle so you can mix local and cloud wisely. 🧠⚖️

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Local models can power coding assistants and agents so your code and data never leave your computer. This is valuable for confidential projects, offline work and avoiding per-request costs. Local models are less capable than the strongest cloud models on large, complex tasks, so many developers combine the two.

- **Local excels** at autocomplete, quick questions and small, well-defined tasks.
- **Three setups:** editor autocomplete and chat, local coding agents, and Claude Code with local models.
- **Get better results** with smaller tasks, clear instructions and tests.

</details>

<!-- in-this-chapter -->

## ⚖️ Local vs. cloud for coding: the honest picture

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Local models handle autocomplete, code explanations and small edits well. For large, multi-step tasks, frontier cloud models are still noticeably stronger. The table compares them task by task.

</details>

| Task | Local models today | Frontier cloud models |
|---|---|---|
| ⌨️ Autocomplete | ✅ Excellent (small, fast models) | ✅ Excellent |
| 💬 "Explain this code" chat | ✅ Very good with mid-size models | ✅ Excellent |
| ✏️ Small edits and refactors | ✅ Good with 14B+ models | ✅ Excellent |
| 🤖 Multi-step agent tasks (edit, run, fix, repeat) | 🟡 Good with large models (30B+ MoE), weaker below | ✅ Best |
| 🏗️ Big features across many files | 🟡 Possible on big hardware, less reliable | ✅ Best |
| 🔒 Privacy, offline, no per-use cost | ✅ Total | ❌ Your code goes to a provider |

> [!TIP]
> **💡 The hybrid habit**
> Local for **autocomplete, explanations, private code and bulk chores**. Cloud frontier models for **hard, multi-step agent
> work**. Many tools let you switch per task with one setting.

## 🧠 Choosing coding models

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Choose a model trained for code, and pick the largest one that fits your memory, because coding agents need both capability and a long context. The table suggests models by available memory.

</details>

| Your memory | Try | Good for |
|---|---|---|
| 8–16 GB | Small Qwen-Coder or Gemma models | Autocomplete, quick questions |
| 24–32 GB | `gemma4:26b`, `qwen3.6:27b`, `gpt-oss:20b` | Solid chat and edits, light agent work |
| 48–64 GB | `qwen3.6:35b` and Qwen3-Coder MoE models | Real agent sessions on small projects |
| 128 GB+ | `gpt-oss:120b`, the largest Qwen-Coder and DeepSeek models | The closest thing to frontier agents at home |

**What makes a good local coding model:** trained for code, supports **tool calling** (essential for agents), and handles a
**long context** (agents read lots of files). Check the model page in the Ollama library for the "tools" capability.

> [!NOTE]
> **📌 Context length matters for agents**
> Coding agents need big context windows (Ollama's Claude Code guide recommends **64k tokens or more**). Longer context uses
> more memory, so a model that fits at 8k might not fit at 64k. Set Ollama's context length (for example with the
> `OLLAMA_CONTEXT_LENGTH` environment variable or in the app settings), and leave memory headroom.

## 🧩 Setup 1: autocomplete + chat in your editor

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Extensions like Continue add local autocomplete and chat to VS Code and JetBrains.

1. Install the extension in your editor.
2. Add Ollama or LM Studio as the provider.
3. Choose a small, fast model for autocomplete and a larger one for chat.

</details>

| Tool | Editor | Setup |
|---|---|---|
| **Continue** | VS Code, JetBrains | Add Ollama or LM Studio as a provider, and pick a small model for autocomplete and a bigger one for chat |
| **Zed** | Zed | Settings → AI → Ollama or LM Studio |
| **JetBrains AI** | IntelliJ family | Supports local models via Ollama/LM Studio in settings |
| **Cursor / VS Code Copilot** | Their editors | Mostly cloud-first; local support is limited or via custom endpoints |

**The winning combo:** a tiny, fast model for **autocomplete** (it runs on every keystroke) + your biggest comfortable model
for **chat**.

## 🤖 Setup 2: local coding agents

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Several coding agents, including Cline, Roo Code, Aider, OpenCode and Goose, can use local models. Point them at Ollama or LM Studio as the provider. The table shows how to connect each.

</details>

| Agent | Where it runs | Connect to local |
|---|---|---|
| **Cline / Roo Code / Kilo Code** | VS Code | API provider → **Ollama** or **LM Studio**, pick the model |
| **Aider** | Terminal, Git-native | `aider --model ollama_chat/qwen3.6:27b` (with `OLLAMA_API_BASE=http://127.0.0.1:11434`) |
| **OpenCode, Goose** | Terminal / desktop | Configure an Ollama or OpenAI-compatible provider |
| **Claude Code** | Terminal | Via **Ollama's Anthropic-compatible API** (next section) |
| **Open WebUI + tools** | Browser | Code interpreter and tools with local models ([Home Lab](80-home-lab.md)) |

## 🦙 Setup 3: Claude Code on local models

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Ollama (version 0.14 and later) supports Anthropic's Messages API, so Claude Code's full workflow, including file editing, commands, skills and hooks, can run on a local model.

1. Install or update Ollama and download a capable coding model.
2. Set the environment variables shown below to point Claude Code at Ollama.
3. Launch Claude Code with the local model name.

</details>

Ollama (v0.14+) speaks **Anthropic's Messages API**, so Claude Code's harness (file editing, commands, skills, hooks,
subagents) can drive an open model:

```bash
# the one-liner: sets everything up and launches Claude Code
ollama launch claude

# or configure it yourself
export ANTHROPIC_BASE_URL=http://localhost:11434
export ANTHROPIC_AUTH_TOKEN=ollama
export ANTHROPIC_API_KEY=""
claude --model qwen3.6:35b
```

**What to expect:** the same workflow you learned in the [Claude Code Masterclass](../part-7-building-with-ai/62-claude-code-masterclass.md),
with quality depending on the model you pick. Bigger local models handle real tasks; small ones get lost in long agent loops.
Ollama also offers `:cloud` models through the same setup if you want a bigger open model without the hardware.

> [!WARNING]
> **⚠️ Check what "local" means**
> Models with a `:cloud` tag run on Ollama's servers, not your machine. For truly private work, stick to models you've
> downloaded, and double-check with `ollama ps`.

## 🧪 Making local agents work better

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Local models benefit from tighter direction: break work into smaller, well-defined tasks, provide a thorough `AGENTS.md`, include tests the agent can run, and keep the context focused. The table explains why each tip helps.

</details>

| Tip | Why |
|---|---|
| **Smaller, well-defined tasks** | "Add input validation to `signup.py`" beats "build auth" |
| **A great `AGENTS.md` / `CLAUDE.md`** | Clear commands and conventions matter even more for smaller models |
| **Tests as the finish line** | *"Make `pytest tests/test_signup.py` pass"* keeps agents on track |
| **Plan with a big model, execute locally** | A frontier model writes the plan; the local agent does the steps |
| **Fewer MCP tools** | Every tool definition eats context |
| **Enough context** | 32k–64k+ tokens for agent work |
| **Commit often** | Rewinding is your friend ([Git & GitHub](../part-7-building-with-ai/61-git-and-github.md)) |
| **Measure** | Run the same 5 tasks on a few models and keep a scorecard ([Evaluating AI](../part-12-mastery/105-evaluating-ai.md)) |

## 🛠️ Local agents beyond coding

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Local agents can also handle non-coding work on private data, such as organizing files, processing documents and running automations. The table suggests setups for each.

</details>

| Agent job | Local setup |
|---|---|
| 🗂️ File organizing and renaming | Claude Code or Goose + a local model |
| 📧 Email triage on private mail | n8n AI Agent + Ollama ([n8n AI Agents](../part-5-automation/48-n8n-ai-agents.md)) |
| 📄 Document Q&A | Open WebUI Knowledge, or local RAG ([Build a RAG System](../part-8-knowledge-and-memory/74-build-a-rag-system.md)) |
| 🏡 Smart home control | Home Assistant's local LLM integration ([Private Home Assistant](../part-13-build-alongs/117-build-along-private-home-assistant.md)) |
| 🧾 Receipt and invoice extraction | A vision model + structured output via the OpenAI-compatible API |

Your homemade agent from [Build Your Own Agent](../part-7-building-with-ai/68-build-your-own-agent.md) can run locally too: point the
OpenAI or Anthropic SDK at Ollama's local URL and pick a tool-capable model.

## 🎯 Key takeaways

- Local models are **excellent for autocomplete and chat**, and **increasingly capable as agents** on big hardware.
- Pick **code-trained, tool-calling, long-context** models, as big as your memory allows.
- **Continue / Zed** for editor help, **Cline / Aider / OpenCode** for agents, and **Claude Code via Ollama** for Claude Code's
  workflow on open models.
- Give local agents **small tasks, clear rules and tests**, and plan with a big model when needed.
- `:cloud` models aren't local. **Check before trusting privacy.**

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Why use a tiny model for autocomplete but a bigger one for chat?</summary>

Autocomplete runs on **every keystroke**, so it must be **fast**. Chat benefits from a **smarter**, larger model.

</details>

<details class="quiz">
<summary>❓ 2. How does Claude Code talk to a local model?</summary>

Through **Ollama's Anthropic-compatible Messages API**: `ollama launch claude`, or set `ANTHROPIC_BASE_URL` to Ollama's local
URL and pick a model.

</details>

<details class="quiz">
<summary>❓ 3. Your local agent keeps losing track in long tasks. Name two fixes.</summary>

Any two of: **smaller tasks**, **a bigger model**, **more context length**, **tests as the finish line**, **fewer tools**,
**a clearer AGENTS.md**, or **planning with a frontier model** first.

</details>

> [!TIP]
> **🎮 Try this**
> Install Continue or Cline, point it at Ollama, and ask the local model to *"explain what `scripts/sync_manual.py` does in this
> repo, then add a docstring to every function."* Turn off your Wi-Fi halfway through. Private pair programming, achieved. 🔒✨

---

**Next:** [82 · Fine-Tuning for Normal People →](82-fine-tuning-for-normal-people.md)
