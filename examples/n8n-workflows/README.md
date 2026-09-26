# ⚡ Importable n8n Workflows

Starter automations you can import into [n8n](https://n8n.io) in about 30 seconds and then
remix. They all use Claude as the "brain", and you can swap in any model n8n supports.

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

## 📱 3. Pocket AI Assistant on Telegram: [`telegram-pocket-assistant.json`](telegram-pocket-assistant.json)

```
📱 Telegram message → 🔒 only you? → 🤖 Pip (AI Agent + memory + calendar + calculator) → 📱 reply
```

Your own AI assistant in your pocket: it remembers the conversation, checks your Google Calendar, adds events after you
confirm, and does math. Strangers get ignored.

**Setup:** create a bot with **@BotFather**, add the token as a Telegram credential, paste **your** Telegram user ID (ask
@userinfobot) into the **Only me? 🔒** node, and connect Anthropic and Google Calendar credentials. The full walkthrough is
[Build-Along: Your Pocket AI Assistant](../../manual/part-13-build-alongs/112-build-along-pocket-ai-assistant.md).

## 📞 4. Voice Receptionist Tools: [`voice-receptionist-tools.json`](voice-receptionist-tools.json)

```
🌐 POST /receptionist/check-availability {date}      → 📅 that day's events → 🧮 free 30-min slots → 💬 spoken-style reply
🌐 POST /receptionist/book-appointment {name, phone, start, notes} → 📅 create event → ✅ confirmation
```

Two webhook "tools" a voice agent (Vapi, Retell, ElevenLabs Agents…) can call mid-conversation. Set your business hours and
timezone at the top of the **Find free slots** node.

```bash
curl -X POST "http://localhost:5678/webhook-test/receptionist/check-availability" \
  -H "Content-Type: application/json" -d '{"date": "2026-10-01"}'
```

Full walkthrough: [Build-Along: An AI Voice Receptionist](../../manual/part-13-build-alongs/119-build-along-voice-receptionist.md).

---

### Notes
- The model is set to `claude-opus-5`. For high-volume or simple steps you can pick a smaller, cheaper
  model like `claude-haiku-4-5` in the **Claude** node, or swap that node for OpenAI, Gemini, Ollama (local!), or OpenRouter.
- n8n node versions evolve. If a node looks off after import, delete it and re-add the same node
  type. The settings are simple to redo.
