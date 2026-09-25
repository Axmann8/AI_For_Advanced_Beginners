# 15 · Google Workspace & Microsoft 365 AI 🔵🟣

Most of the world's work lives in Google Workspace or Microsoft 365. Both have AI woven through every app,
and both connect to outside AI (Claude, ChatGPT) and automation platforms. Here's how to squeeze the
most out of whichever one you live in.

> Feature names and plan requirements shift often. Look for the Gemini ✨ or Copilot icons in your apps
> and check your plan's details.

---

## 🔵 Google Workspace + Gemini

| App | What Gemini does | 🎮 Try |
|---|---|---|
| **Gmail** | Summarize threads, draft and refine replies, smart search, "help me write" | *"Summarize this thread and draft a reply that politely declines."* |
| **Docs** | Draft, rewrite, summarize, generate from your files | *"Draft a project brief using @Q3-notes and @budget-sheet."* |
| **Sheets** | Build formulas and tables, analyze, `=AI()` function per cell | `=AI("Classify sentiment of", A2)` down a column |
| **Slides** | Generate slides and images from prompts or docs | *"Make a 6-slide deck from this doc."* |
| **Meet** | "Take notes for me," recaps, action items, translated captions | Turn on auto notes for recurring meetings |
| **Drive** | Summarize folders and files, answer questions across docs | *"What's the status of the Aurora project across these files?"* |
| **Calendar** | Scheduling help, and Gemini in the side panel | *"Find time with Priya next week for 30 minutes."* |
| **Gemini app** | Gems (custom assistants), Deep Research, Canvas, connected Google apps | Build a Gem for your writing style |
| **NotebookLM** | Grounded research and audio overviews from your sources | See [Ch. 23](../part-6-knowledge-and-memory/41-rag-memory-and-knowledge.md) |
| **Google AI Studio / Apps Script** | Build custom tools and automations with Gemini | Automate Sheets with a small script |

### Power workflows
1. **Deep Research → Doc:** Gemini Deep Research on a topic → export to Docs → share with your team.
2. **Sheets as an AI pipeline:** a column of inputs → `=AI()` columns for classify, extract, and summarize. It's a no-code
   batch processor. 🤯
3. **Apps Script + Gemini API:** a tiny script that runs every morning, reads new form responses, and emails a summary.
   (Ask Claude or Gemini to write it for you!)
4. **Gems** for repeatable tasks: "Meeting prep Gem," "Email tone checker Gem," "Recipe scaler Gem."

### Bringing Workspace into other AIs
- **Claude:** Google Drive, Gmail, and Calendar connectors ([Ch. 6](../part-2-mcp-and-connectors/10-built-in-connectors.md)).
- **ChatGPT:** Drive, Gmail, and Calendar connectors.
- **Automation:** every Workspace app has rich n8n, Zapier, and Make nodes.

---

## 🟣 Microsoft 365 + Copilot

| App | What Copilot does | 🎮 Try |
|---|---|---|
| **Outlook** | Summaries, drafting, coaching on tone, scheduling | *"Summarize my unread emails from leadership."* |
| **Word** | Drafting from files, rewriting, summarizing, Q&A on long docs | *"Draft a proposal based on /Proposal-2025.docx and this email."* |
| **Excel** | Formulas, analysis, charts, **Python in Excel**, insights | *"Which region's sales dropped most? Chart it."* |
| **PowerPoint** | Decks from prompts or Word docs, redesign, speaker notes | *"Turn this Word report into a 10-slide deck."* |
| **Teams** | Meeting recaps, "what did I miss," action items, chat summaries | Ask in a meeting: *"What decisions have we made so far?"* |
| **Copilot Chat** | Work-grounded chat across your M365 data (emails, files, meetings) | *"Prep me for my 2pm with Contoso."* |
| **Copilot Studio** | Build custom agents with connectors, actions, and **MCP** | An HR policy Q&A agent for your team |
| **Power Automate** | Automation with AI Builder and Copilot-assisted flow building | *"When a file lands in SharePoint, summarize it to Teams."* |

### Power workflows
1. **Meeting → minutes → tasks:** Teams recap → Planner/To Do tasks → follow-up email draft.
2. **Excel analyst:** Copilot + Python in Excel for real data analysis without leaving the spreadsheet.
3. **Copilot Studio agent + MCP:** connect an MCP server (e.g. Zapier MCP or your own) to give your agent new tools.
4. **SharePoint knowledge agent:** an agent grounded on a SharePoint site answers team questions.

---

## Cross-platform tips 🌉

- **Ground the AI in files.** Both suites work much better when you reference specific files (`@file` in Gemini, `/` in Copilot).
- **Permissions = visibility.** AI only sees what you (or the agent) have access to, so tidy sharing matters.
- **Mix and match.** Nothing stops you from using Claude with Google Drive connectors or ChatGPT with SharePoint. Pick the best brain for the job.
- **Automate the handoffs:** Zapier, Make, n8n, and Power Automate all bridge Google ↔ Microsoft ↔ everything else.

---

### 🎮 Try this
Pick **one recurring task** you do in Gmail/Outlook or Docs/Word every week (a status email, meeting notes, a report).
Do it once with the built-in AI this week. If it saves 10+ minutes, automate it next week using [Part III](../part-3-automation/14-automation-platforms.md).

---

**Next:** [16 · Obsidian + AI →](25-obsidian-and-ai.md)
