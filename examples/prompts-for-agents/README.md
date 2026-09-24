# 🧠 Teaching Your Agent: Memory Files & Skills

Two small files that make an AI coding agent feel like it *knows you*.

| File | What it is | Where it goes |
|---|---|---|
| [`CLAUDE.md`](CLAUDE.md) | **Project memory**: a standing briefing loaded every session | Project root (or `~/.claude/CLAUDE.md` for global prefs) |
| [`skills/weekly-review/SKILL.md`](skills/weekly-review/SKILL.md) | **A skill**: a packaged, on-demand playbook the agent loads only when relevant | `.claude/skills/weekly-review/SKILL.md` (project) or `~/.claude/skills/...` (personal) |

## Memory vs. skills: the mental model
- **Memory (`CLAUDE.md` / `AGENTS.md`)** is always on. Keep it short: facts, commands, and rules.
- **Skills** load on demand. The agent only reads the `description` until it decides the skill is
  relevant, then pulls in the full instructions (and any scripts or templates in that folder). That means you can
  have *dozens* of skills without bloating every conversation.

## Try it
```bash
mkdir -p .claude/skills
cp -r examples/prompts-for-agents/skills/weekly-review .claude/skills/
claude
> recap my week
```

Skills are an open format, so the same `SKILL.md` folder structure works in a growing number of tools.
Once you've written a few, look into **plugins**, which bundle skills, MCP servers, slash commands,
and hooks into one installable package you can share.
