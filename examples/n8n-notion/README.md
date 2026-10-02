# 🔗 n8n + Notion Starter Kit: Your AI Command Center

Five importable [n8n](https://n8n.io) workflows that turn [Notion](https://www.notion.com) into an AI-powered command
center. They're used in the manual's build-along,
[Your AI Command Center](../../manual/part-14-n8n-and-notion/127-build-along-ai-command-center.md), which walks through
every step with screenshots and checkpoints.

| File | What it does |
|---|---|
| [`1-capture-to-inbox.json`](1-capture-to-inbox.json) | `POST` any text (from a phone shortcut, form or app) → AI triage → a tidy Notion **Inbox** row |
| [`2-process-with-ai-button.json`](2-process-with-ai-button.json) | Click **Process with AI** on an Inbox row → AI summary, next step and up to 5 subtasks in **Tasks** |
| [`3-daily-briefing.json`](3-daily-briefing.json) | Every morning at 7 → open tasks due soon → AI briefing → a **Daily Briefings** page and a Telegram message |
| [`4-error-logger.json`](4-error-logger.json) | Any workflow fails → a row in the **Automation Log** with the error and a link to the execution |
| [`5-notion-tools-mcp-server.json`](5-notion-tools-mcp-server.json) | Serves `find_tasks`, `create_task` and `complete_task` to Claude, ChatGPT or Cursor over MCP |

All five are checked by CI ([`scripts/check_n8n_workflows.py`](../../scripts/check_n8n_workflows.py)) so their nodes and
connections stay consistent.

---

## 1 · Create the Notion databases

Create four databases (full-page databases are easiest) with these **exact** property names and types. Option names
matter: the workflows write these values.

### 📥 Inbox
| Property | Type | Options |
|---|---|---|
| Name | Title | |
| Status | Status | `New`, `Processing`, `Processed`, `Error` |
| Type | Select | `Task`, `Idea`, `Note`, `Link` |
| Priority | Select | `High`, `Medium`, `Low` |
| Source | Select | `Phone`, `Email`, `Web`, `Telegram`, `Slack`, `Other` |
| Summary | Text | |
| Next step | Text | |
| AI processed | Checkbox | |
| Process with AI | Button | *Send webhook* → workflow 2's Production URL (paid Notion plans) |

### ✅ Tasks
| Property | Type | Options |
|---|---|---|
| Name | Title | |
| Status | Status | `To do`, `In progress`, `Done` |
| Priority | Select | `High`, `Medium`, `Low` |
| Due | Date | |
| Source | Select | `Me`, `AI`, `Email`, `Phone` |

### ☀️ Daily Briefings
| Property | Type |
|---|---|
| Name | Title |
| Date | Date |

### 🚨 Automation Log
| Property | Type | Options |
|---|---|---|
| Name | Title | |
| Status | Select | `Error`, `Info` |
| Error | Text | |
| Execution link | URL | |
| Time | Date (include time) | |

> 💡 Faster: ask Notion AI (or Claude with the Notion connector) to *"create these four databases with exactly these
> properties"* and paste the tables above.

## 2 · Connect n8n to Notion

1. Create an internal integration at **notion.so/profile/integrations** → **New integration** (type *Internal*) and copy
   its **Internal Integration Secret**.
2. Give it access: open the page that holds your four databases → **••• → Connections** → add your integration.
3. The first time you open a Notion node in n8n, click **Connect to Notion** and paste the secret. Every other Notion
   node can reuse that credential.

## 3 · Import and configure each workflow

Tested by importing into **n8n 2.41**. Start with workflow 4 (the error logger), so later problems get logged.

1. In n8n, create a workflow → **⋯ → Import → From URL** and paste the file's raw link, for example
   `https://raw.githubusercontent.com/Axmann8/The_Massive_AI_Manual/main/examples/n8n-notion/4-error-logger.json`
   (or download the file and use **Import → From file**).
2. Open every node with a ⚠️ and pick its credential (Notion API, Anthropic, Telegram, Header Auth, Bearer Auth).
3. In each Notion node with a **Database** box, replace the `PASTE-YOUR-…-DATABASE-URL` placeholder with your database's
   link (in Notion: open the database → **••• → Copy link**). n8n refuses to run while a placeholder is still there
   (*"Not a valid Notion Database URL"*).
4. **Webhook security:** workflows 1 and 2 use **Header Auth**. Create a *Header Auth* credential with name
   `X-Webhook-Secret` and a long random value, and send the same header from your phone shortcut or Notion button.
5. Workflow 3: replace `PASTE-YOUR-TELEGRAM-CHAT-ID` with your chat ID (or delete the Telegram node, or swap in Gmail or
   Slack).
6. Workflow 5: on the MCP Server Trigger, click **Connect to Bearer Auth** and enter a long random token.
7. **Publish** workflow 4 first. Then, in every other workflow, open **⋯ → Settings → Error Workflow**, choose the error
   logger, save, and **Publish**. (Until the error logger is published, n8n shows a ⚠️ next to it: *Not published*.)

The manual's [build-along](../../manual/part-14-n8n-and-notion/127-build-along-ai-command-center.md) shows each of these
screens.

## 4 · Test

```bash
# Workflow 1: capture. Use the Test URL (/webhook-test/...) right after clicking Execute workflow,
# or the Production URL (/webhook/...) once the workflow is published.
curl -X POST "https://YOUR-N8N/webhook/capture" \
  -H "Content-Type: application/json" \
  -H "X-Webhook-Secret: YOUR-SECRET" \
  -d '{"text": "Plan a birthday dinner for Sam next Friday, 8 people, somewhere with vegetarian options", "source": "Web"}'
```

Expected: a JSON reply with the new page's URL, and an Inbox row titled something like *Plan Sam's birthday dinner*.

- **Workflow 2:** click **Process with AI** on that row. Within seconds, Status becomes *Processed*, Summary and Next step
  fill in, and new tasks appear in Tasks.
- **Workflow 3:** click **Execute workflow** to get today's briefing immediately.
- **Workflow 5:** connect an MCP client to the trigger's Production URL with your bearer token, for example
  `claude mcp add --transport http notion-tasks https://YOUR-N8N/mcp/notion-tools --header "Authorization: Bearer YOUR-TOKEN"`,
  then ask *"What's on my Notion task list this week?"*

## Notes

- **Models:** capture uses a fast, inexpensive model (`claude-haiku-4-5`); planning and briefings use
  `claude-sonnet-5-5`. Swap in any chat model n8n supports, including Ollama for fully local AI.
- **No paid Notion plan?** Replace workflow 2's Webhook with a **Notion Trigger** (*Page Updated in Database*) plus an
  **IF** node that checks a *Run AI* checkbox.
- **Webhook payloads:** workflow 2 looks for the page ID at `body.data.id` (Notion's Send webhook format). If Notion
  changes the shape, update the *Get page ID* node.
- **Rate limits:** Notion allows about three requests per second per integration. The Notion nodes retry automatically.
- **Node versions:** the Notion nodes use version 2.2, which imports and runs on n8n 2.x. New Notion nodes you add
  yourself will be version 3, which adds data-source and Markdown operations; both work side by side.
