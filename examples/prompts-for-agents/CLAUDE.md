# CLAUDE.md: Example project memory file

> Put a file like this at the root of any project. Claude Code reads it automatically at the
> start of every session, so it works like a permanent briefing for your AI teammate.
> (Cursor has `.cursor/rules`, Codex and many other agents read `AGENTS.md`. Same idea.)

## What this project is
A personal automation hub: small Python scripts + n8n workflows that glue my apps together
(Notion, Gmail, Google Calendar, Slack).

## How to run things
- Install: `pip install -r requirements.txt`
- Tests: `pytest -q`. Run these before saying something is done.
- Format: `ruff format . && ruff check --fix .`

## Conventions
- Python 3.11+, type hints everywhere, small functions.
- Secrets live in `.env` (never commit it). Read them with `os.environ`.
- Every script gets a `--dry-run` flag that prints what it *would* do.

## Things to be careful about
- Never send emails or Slack messages without `--dry-run` first unless I say "send it".
- Don't delete Notion pages. Archive them instead.

## My preferences
- Explain *why* when you pick between two approaches. I'm learning!
- Keep commit messages short and descriptive.
