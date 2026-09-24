---
name: weekly-review
description: Run my Friday weekly review — gather what I did this week from git, notes, and calendar, then write an encouraging recap with wins, lessons, and next week's top 3. Use when I say "weekly review", "recap my week", or "what did I do this week".
---

# Weekly Review

You're helping me close out the week on a high note. Be warm, specific, and brief.

## Steps
1. **Gather evidence** (use whatever is available, skip what isn't):
   - `git log --since="7 days ago" --oneline --all` in the current repo
   - Notes: any files in `notes/` modified this week
   - Calendar: if a calendar MCP/connector is connected, list this week's events
   - Tasks: if Notion/Linear/Todoist is connected, list items completed this week
2. **Find the wins.** Look for anything shipped, learned, fixed, or started. Small wins count.
3. **Spot one lesson.** Pick a pattern, e.g. "the stuff you started in the morning got finished."
4. **Propose next week's Top 3** based on unfinished threads.

## Output format
```
## 🏆 Wins this week
- ...

## 💡 Lesson
...

## 🎯 Next week's Top 3
1. ...
2. ...
3. ...

## 🔋 One-line pep talk
...
```

## Rules
- Never invent accomplishments. If evidence is thin, say so and ask me what I'd add.
- Save the recap to `notes/weekly/YYYY-MM-DD.md` only if I say "save it".
