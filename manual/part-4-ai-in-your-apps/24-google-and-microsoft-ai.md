# 24 · Google Workspace & Microsoft 365 AI 🔵🟣

> ⏱️ 7 min read · 🎯 Everyone · 🧰 Needs: a Google or Microsoft account (AI features vary by plan)

**Most of the world's work lives in Google Workspace or Microsoft 365, and both now have AI woven through every app.**
This chapter is your practical tour: the best feature in each app, power workflows that save real hours, how to automate
with Apps Script and Power Automate, and how to bring outside AI (Claude, ChatGPT) into the mix.

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Google and Microsoft put AI helpers inside email, documents, spreadsheets, slides and video calls. **Gemini** is Google's
helper, and **Copilot** is Microsoft's. They can summarize, write, make slides from documents, take meeting notes and more.
This chapter shows you the best trick in each app, plus how to make little robots that do the boring stuff automatically.

</details>

<!-- in-this-chapter -->

> [!NOTE]
> **📌 Features depend on your plan**
> Look for the ✨ Gemini or Copilot icons in your apps. Business, education and personal plans include different features,
> and admins can turn things on or off.

## 🔵 Google Workspace + Gemini, app by app

<details class="eli5">
<summary>🧸 ELI5</summary>

Every Google app has a Gemini button. Here's what it's best at in each one, with a prompt you can copy.

</details>

| App | What Gemini does | 🎮 Try |
|---|---|---|
| **Gmail** | Summarize threads, draft and refine replies, smart search | *"Summarize this thread and draft a reply that politely declines."* |
| **Docs** | Draft, rewrite, summarize, generate from your files | *"Draft a project brief using @Q3-notes and @budget-sheet."* |
| **Sheets** | Build formulas and tables, analyze, `=AI()` per-cell prompts | `=AI("Classify the sentiment of", A2)` down a column |
| **Slides** | Generate slides and images from prompts or docs | *"Make a 6-slide deck from this doc."* |
| **Meet** | "Take notes for me," recaps, action items, translated captions | Turn on auto notes for recurring meetings |
| **Drive** | Summarize folders and files, answer questions across docs | *"What's the status of the Aurora project across these files?"* |
| **Calendar** | Scheduling help, Gemini in the side panel | *"Find time with Priya next week for 30 minutes."* |
| **Vids** | AI-assisted video creation from docs and prompts | *"Turn this onboarding doc into a 2-minute training video."* |

## 💎 The Gemini app, Gems & Deep Research

<details class="eli5">
<summary>🧸 ELI5</summary>

Outside the individual apps, the Gemini app is a big chat helper. **Gems** are custom helpers you set up once, and **Deep
Research** reads dozens of websites and writes you a report.

</details>

- **Gems:** custom assistants with standing instructions, like a "Meeting prep Gem," an "Email tone checker Gem" or a
  "Recipe scaler Gem" ([Context Engineering](../part-1-foundations/05-context-engineering.md)).
- **Deep Research:** multi-step research across the web (and optionally your files) that produces a long, cited report you
  can export to Docs.
- **Canvas:** a live document or code editor alongside the chat.
- **Connected apps:** Gemini can pull from Gmail, Drive, Calendar, Maps and YouTube inside the chat.
- **NotebookLM:** grounded research on your chosen sources with audio overviews ([NotebookLM Masterclass](../part-6-knowledge-and-memory/45-notebooklm-masterclass.md)).
- **Google AI Studio:** a free playground and API keys for building with Gemini models.

## 🟣 Microsoft 365 + Copilot, app by app

<details class="eli5">
<summary>🧸 ELI5</summary>

Every Microsoft app has a Copilot button. It can read your work emails, files and meetings to help you write, analyze and
catch up.

</details>

| App | What Copilot does | 🎮 Try |
|---|---|---|
| **Outlook** | Summaries, drafting, tone coaching, scheduling | *"Summarize my unread emails from leadership."* |
| **Word** | Drafting from files, rewriting, summarizing, Q&A on long docs | *"Draft a proposal based on /Proposal-2025.docx and this email."* |
| **Excel** | Formulas, analysis, charts, **Python in Excel**, insights | *"Which region's sales dropped most? Chart it."* |
| **PowerPoint** | Decks from prompts or Word docs, redesign, speaker notes | *"Turn this Word report into a 10-slide deck."* |
| **Teams** | Meeting recaps, "what did I miss," action items, chat summaries | Ask during a meeting: *"What decisions have we made so far?"* |
| **Copilot Chat** | Work-grounded chat across your emails, files and meetings | *"Prep me for my 2pm with Contoso."* |

## 🤖 Copilot agents, Copilot Studio & Power Automate

<details class="eli5">
<summary>🧸 ELI5</summary>

Microsoft lets companies build their own Copilot helpers that know their documents and can use their tools, and Power
Automate is Microsoft's robot-recipe kitchen.

</details>

- **Built-in agents:** Microsoft 365 Copilot includes specialized agents (for example for deep research and data analysis)
  that go beyond quick chat answers.
- **Copilot Studio:** build custom agents with your knowledge sources, connectors, actions and **MCP tools**. A classic
  first agent is an HR policy Q&A bot grounded in SharePoint.
- **SharePoint agents:** agents grounded in a specific site or document library.
- **Power Automate:** cloud and desktop flows with 1,000+ connectors, AI Builder, and Copilot-assisted flow building
  (*"When a file lands in this SharePoint folder, summarize it and post to Teams"*).

## ⚡ Power workflows (Google)

<details class="eli5">
<summary>🧸 ELI5</summary>

Four clever combos that save hours in Google-land: research into docs, spreadsheets as AI factories, little scripts that run
every morning, and custom Gems for repeat jobs.

</details>

1. **Deep Research → Doc:** research a topic → export to Docs → share with your team.
2. **Sheets as an AI pipeline:** a column of inputs → `=AI()` columns for classify, extract and summarize. It's a no-code
   batch processor. 🤯
3. **Apps Script + Gemini:** a tiny script that runs every morning, reads new form responses, and emails a summary (see below).
4. **Gems for repeatable tasks:** meeting prep, tone checking, recipe scaling, lesson planning.

## ⚡ Power workflows (Microsoft)

<details class="eli5">
<summary>🧸 ELI5</summary>

Four clever combos for Microsoft-land: meetings that turn into tasks, spreadsheets that analyze themselves, custom agents,
and SharePoint helpers that answer team questions.

</details>

1. **Meeting → minutes → tasks:** Teams recap → Planner or To Do tasks → follow-up email draft.
2. **Excel analyst:** Copilot + Python in Excel for real data analysis without leaving the spreadsheet.
3. **Copilot Studio agent + MCP:** connect an MCP server (e.g. Zapier MCP or your own) to give your agent new tools.
4. **SharePoint knowledge agent:** answers team questions from your policies and docs, with links to sources.

## 🧑‍💻 Apps Script + Gemini: a tiny robot (optional)

<details class="eli5">
<summary>🧸 ELI5</summary>

Apps Script is a free way to write little robot helpers that live inside Google Sheets and Gmail. Your AI assistant can
write the whole script for you, and you just paste it in.

</details>

**Apps Script** is free JavaScript that runs inside Google Workspace. A sketch of a daily "summarize new form responses"
robot (ask Claude or Gemini to adapt it to your sheet):

```javascript
// Extensions → Apps Script in your responses Sheet. Store your key in
// Project Settings → Script properties as GEMINI_API_KEY.
const MODEL = "YOUR_GEMINI_MODEL"; // pick a current model name from ai.google.dev

function dailySummary() {
  const rows = SpreadsheetApp.getActiveSheet().getDataRange().getValues().slice(1);
  const text = rows.slice(-20).map(r => r.join(" | ")).join("\n");
  const key = PropertiesService.getScriptProperties().getProperty("GEMINI_API_KEY");
  const url = `https://generativelanguage.googleapis.com/v1beta/models/${MODEL}:generateContent?key=${key}`;
  const res = UrlFetchApp.fetch(url, {
    method: "post",
    contentType: "application/json",
    payload: JSON.stringify({ contents: [{ parts: [{ text: "Summarize these form responses in 5 bullets:\n" + text }] }] }),
  });
  const summary = JSON.parse(res.getContentText()).candidates[0].content.parts[0].text;
  MailApp.sendEmail(Session.getActiveUser().getEmail(), "📋 Daily form summary", summary);
}
// Then: Triggers (clock icon) → add a time-driven trigger for dailySummary every morning.
```

## 🌉 Bringing outside AI into Google & Microsoft

<details class="eli5">
<summary>🧸 ELI5</summary>

You're not stuck with just Gemini or Copilot. You can let Claude or ChatGPT read your Google Drive or Microsoft files too,
and pick the best brain for each job.

</details>

- **Claude:** Google Drive, Gmail and Calendar connectors, plus Microsoft 365 options ([Built-in Connectors](../part-2-mcp-and-connectors/10-built-in-connectors.md)).
- **ChatGPT:** Drive, Gmail, Calendar and SharePoint connectors.
- **Automation:** every Workspace and 365 app has rich n8n, Zapier, Make and Power Automate nodes ([Part III](../part-3-automation/index.md)).
- **Mix and match:** nothing stops you from using Claude to write while Gemini handles your Google-native tasks.

## 💡 Cross-platform tips

<details class="eli5">
<summary>🧸 ELI5</summary>

Point the AI at the exact files you mean, keep your file sharing tidy, and check for important stuff before you send it.

</details>

- **Ground the AI in specific files** (`@file` in Gemini, `/` in Copilot) for dramatically better answers.
- **Permissions = visibility:** AI only sees what you (or the agent) can access, so tidy sharing settings help.
- **Name files clearly:** "2026-Q3 Budget (FINAL)" beats "budget v7 new new."
- **Check before sending:** AI-drafted emails and slides deserve a human read, especially for external audiences.
- **Work data policies:** follow your organization's rules on which AI tools may see which data.

## 🎯 Key takeaways

- **Gemini** (Google) and **Copilot** (Microsoft) are built into mail, docs, sheets, slides and meetings.
- **Gems, Deep Research, NotebookLM** (Google) and **Copilot agents, Copilot Studio** (Microsoft) go beyond quick chat.
- **Apps Script** and **Power Automate** let you build free or low-cost robots inside each ecosystem.
- Ground AI in **specific files**, keep **sharing tidy**, and **mix in outside AI** where it's stronger.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. How do you classify 500 rows of feedback without leaving Google Sheets?</summary>

Use the **`=AI()` function** in a new column (or Gemini in the side panel to generate it).

</details>

<details class="quiz">
<summary>❓ 2. Where would you build an HR-policy Q&A agent in Microsoft 365?</summary>

**Copilot Studio** (or a SharePoint agent) grounded in your policy documents.

</details>

<details class="quiz">
<summary>❓ 3. What's the free way to schedule a Gemini-powered summary inside Google Workspace?</summary>

**Apps Script** with a **time-driven trigger**.

</details>

> [!TIP]
> **🎮 Try this**
> Pick **one recurring task** you do in Gmail/Outlook or Docs/Word every week (a status email, meeting notes, a report).
> Do it with the built-in AI this week. If it saves 10+ minutes, automate it next week with [Part III](../part-3-automation/index.md). ⏱️

---

**Next:** [25 · Obsidian + AI →](25-obsidian-and-ai.md)
