# 08 · The MCP Recipe Book 🍳

Single MCP servers are useful. **Combinations** are where the magic happens. Each recipe below lists
the **ingredients** (servers/connectors), the **prompt** to run, and **why it works**. Copy, paste,
adapt, enjoy.

> Use whichever servers you have. Most recipes work with built-in connectors *or* the equivalent MCP
> server from [the catalog](09-mcp-server-catalog.md).

---

## 🧑‍💻 For Builders

### 1. The Bug Detective 🕵️
**Ingredients:** Sentry + GitHub + (your codebase via Claude Code)
> *"Find the most frequent unresolved error in Sentry this week. Locate the code responsible, explain the root
> cause, write a fix with a test, and open a draft PR that links the Sentry issue."*

**Why it works:** Errors (Sentry) + code (repo) + workflow (GitHub) = a full triage-to-fix loop.

### 2. The Visual QA Robot 🤖
**Ingredients:** Playwright (or Chrome DevTools)
> *"Open http://localhost:3000, click through signup → dashboard → settings, screenshot each page at mobile
> and desktop sizes, and list anything broken, misaligned, or slow."*

### 3. Docs-Accurate Coding 📚
**Ingredients:** Context7 + your coding agent
> *"Use context7 to pull the latest docs for [library], then refactor `auth.ts` to the current recommended
> API. Cite which doc sections you used."*

**Why it works:** It kills the "outdated API from training data" problem.

### 4. Design-to-Code 🎨
**Ingredients:** Figma (Dev Mode MCP) + coding agent
> *"Implement the selected Figma frame as a React component using our existing design tokens and components.
> Match spacing exactly, and flag anything that isn't in our component library."*

### 5. The Database Whisperer 🗄️
**Ingredients:** Supabase/Postgres (read-only user!) + a chart-capable client (Claude Artifacts)
> *"Explore the schema, then answer: which signup source produced users with the highest 30-day retention?
> Show the SQL and make a chart."*

---

## 📋 For Productivity

### 6. Monday Morning Briefing ☕
**Ingredients:** Gmail + Google Calendar + Slack + Linear/Asana
> *"Give me a Monday briefing: this week's meetings (with prep notes for each), unanswered emails older than
> 2 days, Slack threads where I'm mentioned, and my overdue tasks. End with my top 3 priorities."*

### 7. Meeting → Action Machine 🎬
**Ingredients:** Meeting notes (Granola/Notion AI/transcript) + Notion + Linear + Gmail (drafts)
> *"From this transcript: create a Notion meeting page, file action items as Linear issues assigned to the
> right people, and draft a follow-up email to attendees. Show me the drafts before sending anything."*

### 8. Inbox Zero Sprint 📭
**Ingredients:** Gmail + Calendar + Todoist
> *"Go through my last 50 unread emails. Archive newsletters I never open, turn requests into Todoist tasks
> with due dates, draft replies for anything needing a quick answer, and give me a list of what needs my brain."*

### 9. The Scheduling Negotiator 📅
**Ingredients:** Google Calendar + Gmail + Time
> *"Find three 45-minute slots next week that work for me and fit Tokyo business hours, avoiding my focus
> blocks. Draft an email proposing them to Kenji."*

### 10. Project Status Autopilot 📊
**Ingredients:** GitHub + Linear + Slack + Notion
> *"Compile this week's status for Project Phoenix: merged PRs, closed issues, blockers mentioned in Slack.
> Write it in Notion under Weekly Updates and post a 5-line summary to #phoenix."*

---

## 🔎 For Research & Learning

### 11. Deep-Dive Research Brief 🔬
**Ingredients:** Brave/Exa/Tavily + Fetch/Firecrawl + Notion
> *"Research [topic] using at least 10 sources across news, blogs, and papers. Resolve contradictions, rate
> source quality, and write a 2-page brief in Notion with citations and a 'what's still uncertain' section."*

### 12. Paper Explainer 📄
**Ingredients:** arXiv/PubMed + Fetch + Memory
> *"Find the 5 most-cited recent papers on [topic]. Explain each like I'm a smart non-expert, connect their
> findings, and remember the key concepts for future chats."*

### 13. YouTube University 🎓
**Ingredients:** YouTube transcript server + Filesystem/Obsidian
> *"Pull the transcripts of these 3 lectures, create unified study notes with timestamps, then write 15
> flashcards to my Obsidian vault under /Flashcards."*

### 14. Competitive Scan 🏁
**Ingredients:** Firecrawl/Apify + Brave Search + Google Sheets
> *"Crawl the pricing pages of these 5 competitors, extract plans/prices/features into a Google Sheet, and
> highlight where we're cheaper or missing features."*

---

## 🏠 For Life

### 15. The Trip Planner ✈️
**Ingredients:** Search + Maps/weather + Calendar + Notion
> *"Plan a 4-day Lisbon trip for mid-October: weather-appropriate activities, a day-by-day plan with travel
> times, restaurant picks by neighborhood. Block the dates in my calendar and create a Notion trip page."*

### 16. Smart Home Scenes 🏡
**Ingredients:** Home Assistant MCP + Time + Weather
> *"Create a 'cozy evening' scene: if it's below 12°C outside, set the thermostat to 21°, dim living room lights
> to 30% warm white, and turn off the office. Run it now and tell me what changed."*

### 17. Personal Finance Check-in 💰
**Ingredients:** Spreadsheet or CSV export + Filesystem + code execution
> *"Analyze my last 3 months of transactions: categorize spending, find subscriptions I forgot about, compare
> to last quarter, and suggest 3 painless savings. Make a chart."*

(Use exported files or **read-only** access for anything financial.)

### 18. The Gift Genius 🎁
**Ingredients:** Memory + Search + Notes
> *"Remember: my sister loves bouldering, Studio Ghibli, and fancy tea. Her birthday is Nov 3. Now find 5 gift
> ideas under $60 from real stores, with links."*

### 19. Recipe → Groceries 🛒
**Ingredients:** Fetch + Todoist/Notion + Memory (dietary prefs)
> *"Fetch these 3 recipe URLs, scale each to 4 servings, merge them into one grocery list grouped by store
> aisle, remove things I already have (see my pantry note), and add it to Todoist."*

---

## 🎨 For Creators

### 20. Content Multiplier 📣
**Ingredients:** Fetch + Canva + Notion/Buffer
> *"Turn my latest blog post into: a 7-post X thread, a LinkedIn post, a newsletter intro, and 3 Canva quote
> graphics in my brand kit. Put all drafts on one Notion page."*

### 21. Podcast Producer 🎙️
**Ingredients:** Transcript + ElevenLabs + Filesystem
> *"From this episode transcript: write show notes with timestamps, 5 clip ideas with exact quotes, and an intro
> read. Generate the intro audio with ElevenLabs in my usual voice."*

### 22. 3D Scene Builder 🧊
**Ingredients:** Blender MCP (+ image reference)
> *"Build a cozy low-poly cabin in the woods at dusk with warm window light and falling snow particles. Render a preview."*

---

## 🔀 Meta-Recipes (automation ↔ agent)

### 23. Chat-Triggered Automations
**Ingredients:** Zapier MCP or n8n (MCP Server Trigger)
> *"Run my 'new client onboarding' workflow for Acme Corp with contact jane@acme.com."*

**Why it works:** Your reliable, tested n8n/Zapier workflows become tools the AI can call.

### 24. Workflow Builder
**Ingredients:** n8n's instance MCP (or Zapier Copilot)
> *"Build an n8n workflow that watches my Gmail for invoices, extracts amount and due date, and adds them to my
> Bills sheet. Test it with the last invoice email."*

### 25. The Self-Improving Assistant 🧠
**Ingredients:** Memory (or Basic Memory) + any tools
> *"At the end of each task today, save one lesson about how I like things done. Tomorrow, read your lessons first."*

---

## 🧂 Seasoning tips (make any recipe better)

- **Name the tools** in your prompt when there's ambiguity ("use Brave Search, not fetch").
- **Ask for a plan first** on big multi-tool tasks: *"Plan the steps, wait for my OK, then execute."*
- **Put a human gate before outbound actions:** *"Show drafts before sending or posting anything."*
- **Save winning prompts** as MCP prompts, skills, or slash commands so you can rerun them with one click.

---

### 🎮 Try this
Pick **one recipe from each of three sections** and run them this week. Then invent your own. Tweak the
ingredients to match the apps *you* use, and share the recipe! 🧑‍🍳

---

**Next:** [09 · Automation Platforms →](../part-3-automation/14-automation-platforms.md)
