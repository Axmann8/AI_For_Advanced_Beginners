# 44 · The MCP Recipe Book: 44 Multi-Tool Combos 🍳🔌

> ⏱️ 10 min read (or pick one recipe!) · 🎯 Everyone · 🧰 Needs: a few connectors or MCP servers

**Single MCP servers are useful. Combinations are where the magic happens.** Each recipe lists the **ingredients**
(servers or connectors), the **prompt** to run, and **why it works**. Copy, paste, adapt, enjoy. Most recipes work with
built-in connectors *or* the equivalent server from [the catalog](40-mcp-server-catalog.md).

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Like a cookbook, but for AI. Each recipe says which "doors" (apps) to connect and exactly what to say. Mixing two or three
doors lets your AI do jobs that would take you an hour, like reading your emails, checking your calendar and writing
replies all at once.

</details>

<!-- in-this-chapter -->

## 🧑‍💻 For builders

<details class="eli5">
<summary>🧸 ELI5</summary>

Recipes for people who make software: finding bugs, testing websites, keeping docs fresh and turning designs into code.

</details>

### 1. The Bug Detective 🕵️
**Ingredients:** Sentry + GitHub + your coding agent
> *"Find the most frequent unresolved error in Sentry this week. Locate the code responsible, explain the root cause, write
> a fix with a test, and open a draft PR that links the Sentry issue."*

**Why it works:** errors (Sentry) + code (repo) + workflow (GitHub) = a full triage-to-fix loop.

### 2. The Visual QA Robot 🤖
**Ingredients:** Playwright (or Chrome DevTools)
> *"Open http://localhost:3000, click through signup → dashboard → settings, screenshot each page at mobile and desktop
> sizes, and list anything broken, misaligned or slow."*

### 3. Docs-Accurate Coding 📚
**Ingredients:** Context7 + your coding agent
> *"Use context7 to pull the latest docs for [library], then refactor `auth.ts` to the current recommended API. Cite which
> doc sections you used."*

**Why it works:** it kills the "outdated API from training data" problem.

### 4. Design-to-Code 🎨
**Ingredients:** Figma (Dev Mode MCP) + coding agent
> *"Implement the selected Figma frame as a React component using our existing design tokens and components. Match spacing
> exactly, and flag anything that isn't in our component library."*

### 5. The Database Whisperer 🗄️
**Ingredients:** Supabase or Postgres (read-only user!) + a chart-capable client
> *"Explore the schema, then answer: which signup source produced users with the highest 30-day retention? Show the SQL and
> make a chart."*

### 6. The Incident Commander 🚒
**Ingredients:** Datadog or Grafana + GitHub + Slack
> *"Summarize what changed in the hour before the latency spike: deploys, config changes, error trends. Draft an incident
> summary for #incidents, but don't post until I approve."*

### 7. The Onboarding Guide 🧭
**Ingredients:** DeepWiki (or your repo) + Notion
> *"Explain this codebase's architecture for a new teammate: main modules, data flow, how to run tests. Save it as a Notion
> onboarding page with a diagram."*

### 8. The Dependency Gardener 🌱
**Ingredients:** GitHub + Context7 + your coding agent
> *"List outdated dependencies, check each one's changelog for breaking changes, and upgrade the safe ones on a branch with
> tests passing. Summarize the risky ones for me."*

## 📋 For productivity

<details class="eli5">
<summary>🧸 ELI5</summary>

Recipes for everyday work: morning briefings, meeting follow-ups, a tidy inbox and a calendar that makes sense.

</details>

### 9. Monday Morning Briefing ☕
**Ingredients:** Gmail + Google Calendar + Slack + Linear or Asana
> *"Give me a Monday briefing: this week's meetings (with prep notes for each), unanswered emails older than 2 days, Slack
> threads where I'm mentioned, and my overdue tasks. End with my top 3 priorities."*

### 10. Meeting → Action Machine 🎬
**Ingredients:** meeting notes or transcript + Notion + Linear + Gmail (drafts)
> *"From this transcript: create a Notion meeting page, file action items as Linear issues assigned to the right people, and
> draft a follow-up email to attendees. Show me the drafts before sending anything."*

### 11. Inbox Zero Sprint 📭
**Ingredients:** Gmail + Calendar + Todoist
> *"Go through my last 50 unread emails. Suggest newsletters to unsubscribe from, turn requests into Todoist tasks with due
> dates, draft replies for quick ones, and give me a short list of what needs my brain."*

### 12. The Scheduling Negotiator 📅
**Ingredients:** Google Calendar + Gmail + Time
> *"Find three 45-minute slots next week that work for me and fit Tokyo business hours, avoiding my focus blocks. Draft an
> email proposing them to Kenji."*

### 13. Project Status Autopilot 📊
**Ingredients:** GitHub + Linear + Slack + Notion
> *"Compile this week's status for Project Phoenix: merged PRs, closed issues, blockers mentioned in Slack. Write it in Notion
> under Weekly Updates and post a 5-line summary to #phoenix."*

### 14. The Document Detective 🔍
**Ingredients:** Google Drive or Box + Notion
> *"Find every document that mentions 'Q4 pricing' across Drive, tell me which is the latest version, and list where they
> contradict each other."*

### 15. The Contract Chaser ✍️
**Ingredients:** DocuSign + Gmail
> *"Which agreements are still waiting on signatures? For each, draft a friendly reminder to the signer."*

### 16. Focus Time Defender 🛡️
**Ingredients:** Google Calendar + Slack
> *"Look at my next two weeks. Protect 3 two-hour focus blocks, suggest meetings that could be async, and draft polite
> decline messages I can review."*

## 🔎 For research & learning

<details class="eli5">
<summary>🧸 ELI5</summary>

Recipes for curious minds: deep research with real sources, understanding papers, and turning videos into study notes.

</details>

### 17. Deep-Dive Research Brief 🔬
**Ingredients:** Brave, Exa or Tavily + Fetch or Firecrawl + Notion
> *"Research [topic] using at least 10 sources across news, blogs and papers. Resolve contradictions, rate source quality,
> and write a 2-page brief in Notion with citations and a 'what's still uncertain' section."*

### 18. Paper Explainer 📄
**Ingredients:** arXiv or PubMed + Fetch + Memory
> *"Find the 5 most-cited recent papers on [topic]. Explain each like I'm a smart non-expert, connect their findings, and
> remember the key concepts for future chats."*

### 19. YouTube University 🎓
**Ingredients:** YouTube transcripts + Filesystem or Obsidian
> *"Pull the transcripts of these 3 lectures, create unified study notes with timestamps, then write 15 flashcards to my
> vault under /Flashcards."*

### 20. Competitive Scan 🏁
**Ingredients:** Firecrawl or Apify + Brave Search + Google Sheets
> *"Crawl the pricing pages of these 5 competitors, extract plans, prices and features into a Google Sheet, and highlight where
> we're cheaper or missing features."*

### 21. Fact-Checker on Demand ✅
**Ingredients:** web search + Fetch
> *"Here's a viral claim. Find the original source, check whether it's accurate, and explain what's missing or exaggerated."*

### 22. Learning Path Builder 🧗
**Ingredients:** web search + Notion + Calendar
> *"Build a 30-day plan to learn [skill] with free resources (verify every link works), save it in Notion, and put 30-minute
> sessions on my calendar."*

## 🏠 For life

<details class="eli5">
<summary>🧸 ELI5</summary>

Recipes for home: trips, smart lights, money check-ins, gifts, groceries and staying organized as a family.

</details>

### 23. The Trip Planner ✈️
**Ingredients:** web search + weather/maps + Calendar + Notion
> *"Plan a 4-day Lisbon trip for mid-October: weather-appropriate activities, a day-by-day plan with travel times, and
> restaurant picks by neighborhood. Block the dates in my calendar and create a Notion trip page."*

### 24. Smart Home Scenes 🏡
**Ingredients:** Home Assistant + Time + Weather
> *"Create a 'cozy evening' scene: if it's below 12°C outside, set the thermostat to 21°, dim living room lights to 30% warm
> white, and turn off the office. Run it now and tell me what changed."*

### 25. Personal Finance Check-in 💰
**Ingredients:** a CSV export + Filesystem + code execution
> *"Analyze my last 3 months of transactions: categorize spending, find subscriptions I forgot about, compare to last
> quarter, and suggest 3 painless savings. Make a chart."* (Use exports or **read-only** access for anything financial.)

### 26. The Gift Genius 🎁
**Ingredients:** Memory + web search + notes
> *"Remember: my sister loves bouldering, Studio Ghibli and fancy tea. Her birthday is Nov 3. Now find 5 gift ideas under $60
> from real stores, with links."*

### 27. Recipe → Groceries 🛒
**Ingredients:** Fetch + Todoist or Notion + Memory (dietary preferences)
> *"Fetch these 3 recipe URLs, scale each to 4 servings, merge them into one grocery list grouped by store aisle, remove things
> I already have (see my pantry note), and add it to Todoist."*

### 28. Family Command Center 👨‍👩‍👧
**Ingredients:** shared Google Calendar + Gmail + Notion
> *"Look at everyone's calendars and school emails for next week. List pickups, forms to sign, and events, and create a
> family checklist page in Notion."*

### 29. The Renter's Assistant 🏢
**Ingredients:** Google Drive (lease PDF) + Gmail + Calendar
> *"Read my lease: when's the notice deadline, what's the pet policy, who fixes appliances? Put the key dates on my calendar."*

## 🎨 For creators

<details class="eli5">
<summary>🧸 ELI5</summary>

Recipes for making things: turning one post into many, producing podcasts, building 3D scenes and designing graphics.

</details>

### 30. Content Multiplier 📣
**Ingredients:** Fetch + Canva + Notion or Buffer
> *"Turn my latest blog post into a 7-post thread, a LinkedIn post, a newsletter intro and 3 Canva quote graphics in my brand
> kit. Put all drafts on one Notion page."*

### 31. Podcast Producer 🎙️
**Ingredients:** transcript + ElevenLabs + Filesystem
> *"From this episode transcript: write show notes with timestamps, 5 clip ideas with exact quotes, and an intro read.
> Generate the intro audio with ElevenLabs."*

### 32. 3D Scene Builder 🧊
**Ingredients:** Blender MCP (+ a reference image)
> *"Build a cozy low-poly cabin in the woods at dusk with warm window light and falling snow particles. Render a preview."*

### 33. Thumbnail Lab 🖼️
**Ingredients:** Canva or an image-generation server + YouTube transcripts
> *"Read this video's transcript, propose 5 thumbnail concepts with 3–4 word titles, and generate the top 2."*

### 34. Beat Sketchpad 🎹
**Ingredients:** Ableton MCP
> *"Start a 90 BPM track: a warm Rhodes chord progression in D minor, a simple drum groove, and a bassline. Name the clips clearly."*

### 35. Audiobook Maker 📖
**Ingredients:** Filesystem + ElevenLabs
> *"Take chapters 1–3 of my story in /drafts, clean up typos, and narrate each as an MP3 with different voices for the two main characters."*

## 💼 For business

<details class="eli5">
<summary>🧸 ELI5</summary>

Recipes for running a business: prepping for sales calls, understanding customers, keeping the books and supporting people.

</details>

### 36. Sales Call Prep 🤝
**Ingredients:** HubSpot or Salesforce + web search + Calendar
> *"For each sales call this week, pull the CRM history, research the company's recent news, and give me 3 tailored talking
> points."*

### 37. Voice of the Customer 🗣️
**Ingredients:** Intercom or Zendesk + Notion
> *"Cluster this month's support conversations into themes with counts and representative quotes, and draft a product
> feedback page."*

### 38. Invoice Wrangler 🧾
**Ingredients:** Gmail + Stripe or PayPal + Sheets
> *"Match last month's invoices to payments received. List unpaid ones with due dates and draft friendly reminders."*

### 39. Store Pulse 🛍️
**Ingredients:** Square or Shopify + Sheets
> *"What were my top 10 products last month, which ones are slowing down, and what should I reorder?"*

### 40. Lead Enricher 🧲
**Ingredients:** Airtable + web search
> *"For each new lead in my Airtable, find their company size, industry and a recent news item, and fill in the fields."*

## 🔀 Meta-recipes (automation ↔ agent)

<details class="eli5">
<summary>🧸 ELI5</summary>

Recipes where your AI chat and your automation robots team up: the chat can start robot jobs, and robots can use AI inside them.

</details>

### 41. Chat-Triggered Automations ⚡
**Ingredients:** Zapier MCP or n8n (MCP Server Trigger)
> *"Run my 'new client onboarding' workflow for Acme Corp with contact jane@acme.com."*

**Why it works:** your reliable, tested workflows become tools the AI can call.

### 42. Workflow Builder 🏗️
**Ingredients:** n8n's instance MCP (or Zapier Copilot)
> *"Build an n8n workflow that watches my Gmail for invoices, extracts amount and due date, and adds them to my Bills sheet.
> Test it with the last invoice email."*

### 43. The Self-Improving Assistant 🧠
**Ingredients:** Memory (or Basic Memory) + any tools
> *"At the end of each task today, save one lesson about how I like things done. Tomorrow, read your lessons first."*

### 44. The Weekly Review Ritual 🔁
**Ingredients:** Calendar + tasks app + GitHub or Notion + a skill
> *"Run my weekly review: wins, open loops, lessons, and next week's top 3, using my weekly-review skill format."*
> ([Example skill](../../examples/prompts-for-agents/skills/weekly-review/SKILL.md))

## 🧂 Seasoning tips (make any recipe better)

<details class="eli5">
<summary>🧸 ELI5</summary>

A few extra tricks make every recipe taste better: name the tools, plan first, and always check before anything is sent.

</details>

- **Name the tools** when there's ambiguity: "use Brave Search, not fetch."
- **Plan first** on big multi-tool tasks: *"Plan the steps, wait for my OK, then execute."*
- **Human gate before outbound actions:** *"Show drafts before sending or posting anything."*
- **Save winning prompts** as MCP prompts, skills or slash commands, so they rerun with one click.
- **Start read-only**, then add write access once the recipe works.

## 🎯 Key takeaways

- Combos of **2–4 tools** turn hour-long chores into one prompt.
- Every recipe follows **gather → think → act (with approval)**.
- **Meta-recipes** connect chat agents with automation platforms for the best of both worlds.
- Save your favorites as **prompts or skills** so they're one click away.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Which recipe ingredient prevents "outdated API" mistakes in coding tasks?</summary>

**Context7**: it fetches current library documentation.

</details>

<details class="quiz">
<summary>❓ 2. Why do most recipes say "show me drafts before sending"?</summary>

Outbound actions are **hard to undo**. Human approval keeps you at a safe autonomy level while the recipe proves itself.

</details>

> [!TIP]
> **🎮 Try this**
> Pick **one recipe from each of three sections** and run them this week. Then invent your own: swap the ingredients for the
> apps *you* use and write it down. Share your best recipe with a friend, because good recipes are meant to be shared. 🧑‍🍳

---

**Next:** [45 · Automation Platforms →](../part-5-automation/45-automation-platforms.md)
