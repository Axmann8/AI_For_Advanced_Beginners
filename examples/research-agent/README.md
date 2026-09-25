# 🔎 Research Agent: questions in, cited reports out

A ~150-line agent that researches any question on the live web and saves a **cited Markdown report**. It uses Claude's
**server-side** `web_search` and `web_fetch` tools (no search API key needed) plus one local tool, `save_report`.

Companion kit for **[Build-Along: A Research Agent That Writes Reports](../../manual/part-11-build-alongs/85-build-along-research-agent.md)**.

## Quick start 🚀

```bash
cd examples/research-agent
pip install -r requirements.txt
python test_research_agent.py            # offline tests: no key, no internet

export ANTHROPIC_API_KEY=sk-ant-...
python research_agent.py "Which heat pumps work best in cold climates, and what do they cost to run?"
python research_agent.py --depth quick "What's new in the Model Context Protocol this year?"
python research_agent.py --depth deep  "What does the research say about 4-day work weeks?"
```

You'll watch it think and search, then find your report in `reports/`. 📄

| Depth | Searches | Report length |
|---|---|---|
| `quick` | up to 4 | 400–600 words |
| `standard` | up to 8 | 800–1,200 words |
| `deep` | up to 15 | 1,500–2,500 words |

## What's inside 🧩

| Piece | What it teaches |
|---|---|
| `SYSTEM` prompt | A research process: sub-questions, primary sources, cross-checking, honest uncertainty |
| `TOOLS` | Mixing **server tools** (Anthropic runs them) with a **client tool** (your code runs it) |
| `research()` loop | The agent loop, including `pause_turn` (continuing a long server-side turn) and a max-turns safety valve |
| `save_report()` | A sandboxed tool that can only write inside `reports/` |
| `test_research_agent.py` | Testing an agent loop offline with a scripted fake client |

## Make it yours 🎨

- **Send it somewhere:** email the report, post it to Slack, or save it to Notion via MCP.
- **Schedule it:** a weekly "what changed in my field?" report with cron or GitHub Actions.
- **Add your own sources:** combine with the [RAG kit](../rag-from-scratch/) to research your own notes *and* the web.
- **Allowed domains:** restrict searches to trusted sites with `allowed_domains` on the web search tool.

> 💸 Research agents make many calls. Set a **spend limit** in the Anthropic console, and start with `--depth quick`.
