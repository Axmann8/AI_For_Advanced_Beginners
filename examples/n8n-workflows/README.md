# ⚡ Importable n8n Workflows

Two starter automations you can import into [n8n](https://n8n.io) in about 30 seconds and then
remix. Both use Claude as the "brain", and you can swap in any model n8n supports.

## How to import
1. In n8n, create a new workflow.
2. Click the **⋯ menu → Import from File** (or just copy the JSON and **paste it onto the canvas**).
3. Open each node with a ⚠️ and pick or create its credential (Anthropic, Slack, Notion).
4. Hit **Test workflow**. Once it works, toggle it **Active**.

> Don't have n8n yet? The fastest local option is `npx n8n` (needs Node.js), which opens
> at http://localhost:5678. Or use Docker, or n8n Cloud.

---

## ☕ 1. Morning AI Digest: [`morning-ai-digest.json`](morning-ai-digest.json)

```
⏰ Schedule (7am) → 📰 RSS (Hacker News, AI filter) → ✂️ Top 15 → 🧩 Build list → 🤖 Claude summary → 💬 Slack
```

Every morning, Claude reads the newest well-upvoted AI stories and sends you the 5 best, each with a
"why it matters" line and a "try this today" idea.

**Remix ideas:**
- Swap the RSS URL for your favorite blogs, subreddits (`reddit.com/r/LocalLLaMA/.rss`), or YouTube channels.
- Replace Slack with **Gmail**, **Discord**, or **Telegram**. It's the same pattern with a different final node.
- Merge several RSS nodes to build a personal newspaper.

## 💡 2. Idea Inbox → Notion: [`idea-inbox-to-notion.json`](idea-inbox-to-notion.json)

```
🌐 Webhook (POST) → 🤖 Claude classifies → 🧩 Parse JSON → 📒 New Notion database page
```

Send any messy idea to a URL and it shows up in Notion titled, categorized, prioritized, and
summarized, with a suggested first step.

**Set up the Notion database** with these properties:

| Property | Type | Options |
|---|---|---|
| Name | Title | – |
| Category | Select | Project, Content, Business, Learning, Life |
| Priority | Select | High, Medium, Low |
| Summary | Text | – |

Then share the database with your n8n Notion integration and paste its URL into the Notion node.

**Test it:**

```bash
curl -X POST "http://localhost:5678/webhook-test/idea-inbox" \
  -H "Content-Type: application/json" \
  -d '{"text": "what if my plants could text me when they need water, arduino + moisture sensor maybe"}'
```

(`webhook-test` works while you click "Test workflow". Once the workflow is active, use `/webhook/idea-inbox`.)

**Remix ideas:**
- Trigger it from an **iOS Shortcut** or **Android Tasker**, and dictate ideas by voice straight into Notion. 🤯
- Add an **If** node so "High" priority ideas also ping you on Slack.
- Swap Notion for **Airtable**, **Google Sheets**, or **Todoist**.

---

### Notes
- The model is set to `claude-sonnet-5`. Change it in the **Claude** node to anything your Anthropic
  key can access, or swap that node for OpenAI, Gemini, Ollama (local!), or OpenRouter.
- n8n node versions evolve. If a node looks off after import, delete it and re-add the same node
  type. The settings are simple to redo.
