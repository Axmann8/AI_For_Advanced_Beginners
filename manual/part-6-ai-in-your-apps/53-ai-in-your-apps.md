# 53 · AI Inside the Apps You Already Use 🏡✨

> ⏱️ 6 min read · 🎯 Everyone · 🧰 Needs: the apps you already use

**You don't always need a new tool.** The apps you already live in (notes, docs, email, spreadsheets, chat, design tools,
even your phone's operating system) now have serious AI built in, and many are **MCP-connected**, so your AI can reach in
and your apps can reach out. This chapter is a guided tour of where the AI is hiding and the best tricks in each.

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Your favorite apps got secret AI helpers! Your notes app can organize itself, your email can summarize itself, your
spreadsheet can fill itself in, and your phone can read your screen. This chapter is a treasure map showing where each
helper lives and one great trick for each.

</details>

<!-- in-this-chapter -->

## 🧭 Why built-in AI is underrated

<details class="eli5">
<summary>🧸 ELI5</summary>

The AI inside your apps already knows what you're looking at, so you don't have to copy and paste. That makes small jobs
super fast.

</details>

| Built-in AI | Standalone chat AI |
|---|---|
| ✅ Already sees your document, sheet or inbox | ❌ You copy and paste context in |
| ✅ Results land right where you need them | ❌ You copy results back out |
| ✅ Uses the app's permissions and data rules | ⚠️ Depends on your connectors |
| ❌ Usually one app at a time | ✅ Can combine many apps (with connectors/MCP) |

**The sweet spot:** built-in AI for *in-app* jobs (rewrite this doc, summarize this thread), and your main assistant with
connectors for *cross-app* jobs (read my email + calendar + notes and plan my week).

## 📒 Notes & docs

<details class="eli5">
<summary>🧸 ELI5</summary>

Notes apps now have helpers that can write, tidy up, answer questions about all your notes, and even run little jobs on a
schedule.

</details>

| App | AI highlights | Deep dive |
|---|---|---|
| **Notion** | Notion Agent, Custom Agents on schedules, AI meeting notes, database autofill, MCP both ways | [Notion AI Deep Dive](54-notion-ai-deep-dive.md) |
| **Obsidian** | Community AI plugins, local models, MCP and Claude Code access to your Markdown vault | [Obsidian + AI](56-obsidian-and-ai.md) |
| **Google Docs** | Gemini drafting, rewriting, summarizing, "help me create" from your files | [Google & Microsoft AI](55-google-and-microsoft-ai.md) |
| **Microsoft Word** | Copilot drafting from files, rewriting, Q&A on long docs | [Google & Microsoft AI](55-google-and-microsoft-ai.md) |
| **Coda, Craft, Mem, Reflect, Capacities** | AI columns, AI-native note organization, chat with notes | [Personal Knowledge Management](../part-8-knowledge-and-memory/77-personal-knowledge-management.md) |

🎮 **Try:** in any doc, select a messy paragraph → *"Rewrite for clarity and half the length, keep my voice."*

## 📊 Spreadsheets

<details class="eli5">
<summary>🧸 ELI5</summary>

Spreadsheets can now have AI in the cells: you can ask each row "is this customer happy or sad?" and it fills in the answers
for hundreds of rows.

</details>

- **Google Sheets + Gemini:** generate formulas, tables and analysis, plus the `=AI()` function for per-cell prompts.
- **Excel + Copilot:** formulas, pivots, charts, Python in Excel, and a `COPILOT()` function in recent versions.
- **Airtable AI:** AI fields that summarize, categorize and extract per row.

🎮 **Try:** paste 200 survey responses into a sheet and add AI columns for *sentiment*, *theme* and *one-line summary*.
Everything else in [Spreadsheet Superpowers](58-spreadsheet-superpowers.md).

## ✉️ Email & calendar

<details class="eli5">
<summary>🧸 ELI5</summary>

Email apps can now summarize long threads, write replies that sound like you, and find the right time for meetings.

</details>

- **Gmail + Gemini** and **Outlook + Copilot:** summaries, drafting, smart search.
- **AI-first email clients:** Superhuman, Shortwave, Spark, with auto-triage, AI search and "write like me."
- **AI calendars:** Reclaim, Motion and similar tools that auto-schedule tasks and defend focus time.

Full playbook: [Email & Calendar Superpowers](57-email-and-calendar.md).

## 🗂️ Project & team tools

<details class="eli5">
<summary>🧸 ELI5</summary>

Team apps have helpers that write status updates, find duplicate tasks, summarize long discussions and answer "what did we
decide?"

</details>

| App | AI highlights |
|---|---|
| **Linear** | AI triage, duplicate detection, agents you can assign issues to, official MCP |
| **Asana** | AI teammates, status summaries, smart workflows, MCP server |
| **ClickUp / monday.com** | Workspace Q&A, auto-updates, AI fields, official MCP servers |
| **Slack** | Channel recaps, thread summaries, enterprise search, agents, an official MCP server |
| **Jira / Confluence** | AI summaries, Rovo search and agents, remote MCP server |
| **Miro / FigJam** | Cluster sticky notes, generate diagrams, summarize boards |

## 🎨 Design & creative apps

<details class="eli5">
<summary>🧸 ELI5</summary>

Design apps can now make images, remove backgrounds, resize designs for every social network, and turn sketches into
real layouts.

</details>

| App | AI highlights | Deep dive |
|---|---|---|
| **Canva** | Magic design, image generation, brand kits, resize for every platform, MCP connector | [Design & UI with AI](../part-10-creative-ai/90-design-and-ui.md) |
| **Figma** | AI design features, Dev Mode MCP for coding agents | [Design & UI with AI](../part-10-creative-ai/90-design-and-ui.md) |
| **Adobe (Photoshop, Firefly, Express)** | Generative fill, expand, commercially safe generation | [Image Generation](../part-10-creative-ai/84-image-generation-deep-dive.md) |
| **CapCut / Descript** | Edit video by editing text, auto-captions, voice cleanup | [Video & Audio](../part-10-creative-ai/85-video-and-audio-production.md) |

## 🎙️ Meetings & voice

<details class="eli5">
<summary>🧸 ELI5</summary>

Meeting helpers listen to your calls and write the notes for you: who said what, what was decided and who does what next.

</details>

- **AI meeting notes:** Granola (no bot joins your call), Otter, Fireflies, plus built-ins in Zoom, Google Meet, Teams and Notion.
- **Dictation:** Wispr Flow, Superwhisper, and built-in OS dictation turn rambling into polished text.
- **Tip:** always tell people when you're recording or transcribing, both because it's polite and because it's often legally required.

## 📱 Your phone's operating system

<details class="eli5">
<summary>🧸 ELI5</summary>

Phones now have AI built into the whole system: it can summarize notifications, rewrite texts, describe photos, and run
magic-button shortcuts.

</details>

| Platform | AI highlights |
|---|---|
| **iPhone / Mac (Apple Intelligence)** | Writing Tools, notification summaries, Visual Intelligence, ChatGPT integration, Shortcuts **Use Model** action |
| **Android (Gemini)** | Gemini assistant, "ask about this screen," Circle to Search, app actions |
| **Samsung Galaxy AI** | Live translate for calls, note summaries, photo editing |
| **Windows (Copilot)** | Copilot app and key, AI features in Paint, Photos and more |

Build your own magic buttons in [Phone & Desktop Automation](../part-5-automation/50-phone-and-desktop-automation.md).

## 📚 Reading & learning apps

<details class="eli5">
<summary>🧸 ELI5</summary>

Reading apps can explain hard paragraphs, make flashcards, and even turn your notes into a podcast you can listen to on a walk.

</details>

- **NotebookLM:** grounded chat with your sources, audio and video overviews, quizzes ([NotebookLM Masterclass](../part-8-knowledge-and-memory/76-notebooklm-masterclass.md)).
- **Readwise Reader:** AI "Ghostreader" for summaries and definitions, plus highlight syncing to your notes.
- **Kindle / Apple Books / browser readers:** built-in summaries and "explain this" features keep improving.
- **Perplexity Spaces** and **Claude/ChatGPT Projects:** research workspaces with your files.

## 🕸️ The "hub" strategy

<details class="eli5">
<summary>🧸 ELI5</summary>

Pick one main home for all your stuff, send everything there automatically, and let your AI read from that one home. One
tidy home beats ten messy ones.

</details>

Pick **one home base** for your knowledge (Notion *or* Obsidian *or* Google Drive), then:

1. **Pipe things into it** with automations ([Part V](../part-5-automation/index.md)).
2. **Let AI read and write it** via connectors or MCP ([Part IV](../part-4-mcp-and-connectors/index.md)).
3. **Ask questions across it** with RAG or built-in search ([Part VIII](../part-8-knowledge-and-memory/index.md)).

A single well-fed hub beats ten half-used apps. 🏡

## 🔍 Audit your apps (10-minute exercise)

<details class="eli5">
<summary>🧸 ELI5</summary>

Make a list of the five apps you use most and go find the AI button in each one. You'll probably discover helpers you
didn't know you had!

</details>

| App I use daily | Its AI feature | One task I'll try this week |
|---|---|---|
| 1. | | |
| 2. | | |
| 3. | | |
| 4. | | |
| 5. | | |

Most people discover **2–3 features they're already paying for** but never used. 🎁

## 🎯 Key takeaways

- Built-in AI shines for **in-app** jobs, and your main assistant + connectors shine **across** apps.
- Notes, docs, sheets, email, team tools, design apps, meetings and even your **phone OS** now have strong AI.
- Pick **one knowledge hub**, feed it automatically, and let AI read it.
- **Audit** your daily apps, since you're probably sitting on unused AI features.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. When is a standalone assistant (with connectors) better than an app's built-in AI?</summary>

For **cross-app** tasks, such as combining email, calendar and notes into one plan.

</details>

<details class="quiz">
<summary>❓ 2. What's the "hub strategy"?</summary>

Choose **one home base** for knowledge, **pipe** things into it automatically, and let AI **read and write** it.

</details>

> [!TIP]
> **🎮 Try this**
> Do the **10-minute app audit** above, then use one newly discovered AI feature for a real task today. Small wins stack up
> into big habits. 🌱

---

**Next:** [54 · Notion AI Deep Dive →](54-notion-ai-deep-dive.md)
