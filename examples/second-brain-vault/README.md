# 🧠 Second Brain Vault: a starter kit

A ready-to-open **Obsidian-compatible vault** that's designed for AI from day one: PARA folders, templates, a `CLAUDE.md` with
house rules, and Claude Code **skills** for inbox triage and weekly reviews.

Companion kit for **[Build-Along: The Second Brain](../../manual/part-13-build-alongs/114-build-along-second-brain.md)**.

```
second-brain-vault/
├── CLAUDE.md                  ← rules for any AI working in the vault (never delete, plan before moving…)
├── 00-Inbox/                  ← everything lands here first
├── 01-Projects/               ← goals with a finish line
├── 02-Areas/                  ← ongoing responsibilities
├── 03-Resources/              ← reference and interests
├── 04-Archive/                ← finished or paused (never deleted)
├── Journal/                   ← daily notes (YYYY-MM-DD.md)
├── Reviews/                   ← weekly reviews
├── Templates/                 ← Daily Note, Resource, Weekly Review
└── .claude/
    ├── skills/inbox-triage/   ← "triage my inbox"
    ├── skills/weekly-review/  ← "do my weekly review"
    └── commands/capture.md    ← /capture your quick note
```

## Quick start 🚀

1. **Copy** this folder somewhere you keep your notes (e.g. `~/Documents/SecondBrain`).
2. **Open it in Obsidian:** *Open folder as vault*. Point the Templates core plugin at `Templates/`.
3. **Open it in Claude Code:**

    ```bash
    cd ~/Documents/SecondBrain
    claude
    ```

    Then try: *"Triage my inbox"*, *"Do my weekly review"*, or `/capture Buy seeds for the balcony garden`.

4. **Or connect Claude Desktop** with the filesystem MCP server, scoped to just this folder:

    ```json
    {
      "mcpServers": {
        "vault": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/you/Documents/SecondBrain"]
        }
      }
    }
    ```

## Make it yours 🎨

- Replace the sample notes with your own (or keep them until the triage clicks).
- Add a **voice capture** pipeline that drops notes into `00-Inbox/` ([Phone & Desktop Automation](../../manual/part-5-automation/50-phone-and-desktop-automation.md)).
- Put the vault in **Git** for version history ([Git & GitHub](../../manual/part-7-building-with-ai/61-git-and-github.md)), and keep it **private**.
- Want it fully private? Use a local model ([Local & Open Models](../../manual/part-9-local-ai/78-local-and-open-models.md)).
