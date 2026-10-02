# 126 · The n8n + Notion Recipe Book: 40 Workflows 🍳

> ⏱️ 5 min read · 🎯 Anyone with n8n and Notion connected · 🧰 Needs: n8n, Notion, and the apps each recipe names

**Forty proven workflows that combine n8n and Notion, organized by area of life and work.** Each recipe lists the
trigger, the steps and what you end up with in Notion, plus a difficulty rating. Find the one that would save you the most
time this week and build it first.

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

This chapter collects 40 workflows that combine n8n and Notion. Each lists its trigger, steps, Notion result and difficulty, and links to the chapter that explains the techniques it uses.

1. **Find a recipe** in the section that matches your goal.
2. **Prepare the Notion database** it writes to, with the properties listed.
3. **Build it** using the method at the end of this chapter, testing with real data before publishing.

</details>

> [!NOTE]
> **📌 How to read the recipes**
> **Trigger → steps → Notion result.** Difficulty: 🟢 easy (under 30 minutes), 🟡 medium (about an hour), 🔴 advanced (an
> afternoon). "AI" means any model node: Claude, GPT, Gemini or a local model through Ollama. Recipes marked 💳 need a paid
> Notion plan for button or automation webhooks; each one can also use a checkbox plus the Notion Trigger instead.

<!-- in-this-chapter -->

## 📥 Capture

| # | Recipe | Trigger → steps → Notion result | Level |
|---|---|---|---|
| 1 | **Voice capture** | Phone shortcut webhook → AI title, type and priority → Inbox row | 🟢 |
| 2 | **Email to task** | Gmail label *To Notion* → AI summary and due date → Tasks row with email link | 🟢 |
| 3 | **Web page saver** | Bookmarklet or Raycast webhook → fetch page → AI summary and tags → Resources row | 🟡 |
| 4 | **Slack saver** | Slack reaction 📌 → message text and link → Inbox row; reply in thread with the Notion link | 🟡 |
| 5 | **Telegram capture bot** | Message to your bot → AI classification → Inbox row; bot replies "Saved ✅" | 🟢 |
| 6 | **Receipt scanner** | Photo shortcut → vision model extracts vendor, amount, category → Expenses row | 🟡 |
| 7 | **Book highlights** | Readwise export or Kindle file → one Notion page per book with highlights and AI key ideas | 🟡 |

## 🗂️ Organize and enrich

| # | Recipe | Trigger → steps → Notion result | Level |
|---|---|---|---|
| 8 | **Inbox triage** | Schedule (every morning) → Inbox rows not yet processed → AI picks project and type → updates rows | 🟡 |
| 9 | **Auto-tag resources** | Notion Trigger (page added) → read page as Markdown → AI topics → multi-select tags | 🟢 |
| 10 | **Process with AI button** 💳 | Button webhook → read page → AI plan and subtasks → page body and related tasks | 🟡 |
| 11 | **Duplicate finder** | Weekly schedule → Get Many → AI groups near-duplicate titles → report page | 🟡 |
| 12 | **Stale project alert** | Weekly schedule → projects not edited in 14 days → Status *Stalled* and a Slack nudge | 🟢 |
| 13 | **Meeting note processor** | Status *Final* 💳 → AI extracts decisions and action items → tasks with owners | 🟡 |
| 14 | **Translate page** 💳 | Button → page Markdown → AI translation → appended section or new linked page | 🟢 |

## 📅 Plan and review

| # | Recipe | Trigger → steps → Notion result | Level |
|---|---|---|---|
| 15 | **Daily briefing** | 7:00 schedule → tasks due, calendar, weather → AI briefing → Daily page and Telegram message | 🟡 |
| 16 | **Time blocking** | Evening schedule → tomorrow's tasks with estimates → AI proposes a schedule → calendar events | 🔴 |
| 17 | **Weekly review** | Friday schedule → completed tasks, journal, metrics → AI review → Weekly Review page | 🟡 |
| 18 | **Monthly goals check-in** | First of the month → Goals and linked projects → AI progress report → Goals page comment | 🟡 |
| 19 | **Meeting prep** | Morning schedule → today's events → AI research on attendees and notes → Meeting pages | 🟡 |
| 20 | **Habit tracker summary** | Sunday schedule → Habits database → streaks and trends → dashboard page | 🟢 |

## 💼 Work and business

| # | Recipe | Trigger → steps → Notion result | Level |
|---|---|---|---|
| 21 | **Lead intake and scoring** | Form webhook → AI fit score and research → Leads row → drafted reply | 🟡 |
| 22 | **Won deal onboarding** | Status *Won* 💳 → create client project from template, tasks, welcome email | 🟡 |
| 23 | **Stripe payments log** | Stripe Trigger → Payments row linked to the customer → monthly totals | 🟢 |
| 24 | **Overdue invoice nudges** | Daily schedule → invoices past due → AI drafts polite reminders → Gmail drafts | 🟡 |
| 25 | **Booking to client page** | Calendly or Cal.com webhook → Client and Meeting rows → prep notes | 🟢 |
| 26 | **Support inbox** | Support email → AI category and urgency → Requests row → Slack alert for urgent ones | 🟡 |
| 27 | **Proposal generator** 💳 | Button on a lead → AI drafts a proposal from your template and notes → Google Doc link on the page | 🔴 |
| 28 | **Team standup collector** | 9:00 Slack prompt → replies → AI summary → Standups page | 🟡 |

## 🎨 Content and learning

| # | Recipe | Trigger → steps → Notion result | Level |
|---|---|---|---|
| 29 | **Content pipeline** | Status *Drafting* 💳 → research and outline → page body; *Scheduled* → social posts | 🔴 |
| 30 | **Repurpose a post** 💳 | Button → AI writes thread, LinkedIn post and newsletter blurb → child pages | 🟢 |
| 31 | **Topic radar** | Daily schedule → RSS and news → AI ranks relevance → Resources rows with summaries | 🟡 |
| 32 | **YouTube study notes** | New video in a playlist → transcript → AI notes and quiz → Learning page | 🟡 |
| 33 | **Flashcards from notes** 💳 | Button on a study page → AI question-and-answer pairs → Flashcards database | 🟢 |
| 34 | **Publish to blog** | Status *Ready* 💳 → page Markdown → blog platform API → URL saved to the page | 🔴 |

## 🛠️ Builders and system maintenance

| # | Recipe | Trigger → steps → Notion result | Level |
|---|---|---|---|
| 35 | **GitHub issues sync** | GitHub Trigger → upsert by issue number → Roadmap rows | 🟡 |
| 36 | **Release notes** | New GitHub release → AI summary of merged PRs → Changelog page | 🟡 |
| 37 | **Error logger** | Error Trigger (all workflows) → Automation Log row with execution link | 🟢 |
| 38 | **Workflow inventory** | Weekly schedule → n8n API lists workflows → Automations database with status and last run | 🟡 |
| 39 | **Notion backup** | Weekly schedule → export key databases → CSV and Markdown in cloud storage | 🟡 |
| 40 | **RAG sync** | Notion Trigger (page updated) → Markdown → chunks and embeddings → vector store | 🔴 |

## 🧑‍🍳 How to build any recipe

```text
Recipe card
-----------
Name:          ______________________________
Trigger:       ______________________________   (schedule / webhook / Notion Trigger / app trigger)
Reads:         ______________________________   (Notion databases and other apps)
AI step:       ______________________________   (model + exact output fields)
Writes:        ______________________________   (database + properties)
Status flow:   ______________________________   (e.g. Ready → Processing → Done / Error)
Approval?      ______________________________   (who approves before anything is sent)
Error path:    Automation Log
```

## 🎯 Key takeaways

- Forty recipes cover **capture, organization, planning, business, content and system maintenance**.
- Every recipe follows **trigger → steps → Notion result**, with status and errors written back.
- Recipes that need **paid Notion webhooks** (💳) can also run with a **checkbox and the Notion Trigger**.
- Build one recipe at a time with the **six-step method**, testing on real data.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Which recipe should every n8n + Notion setup include first, and why?</summary>

The **error logger** (recipe 37), so every failure in every other workflow becomes visible in Notion instead of going
unnoticed.

</details>

<details class="quiz">
<summary>❓ 2. Recipe 22 needs a paid Notion plan for its status webhook. How could you build it on the free plan?</summary>

Use a **Notion Trigger** (Page Updated) or a scheduled **Get Many** that finds deals with Status *Won* that haven't been
processed yet, and mark them processed afterward.

</details>

<details class="quiz">
<summary>❓ 3. What's the first step in building any recipe?</summary>

**Prepare the Notion database**, with the right properties, and share it with your integration.

</details>

> [!TIP]
> **🎮 Try this**
> Build recipe **37 (error logger)** and recipe **1 (voice capture)** today using the starter kit from the next chapter.
> Together they take under an hour and give you a capture system you can trust.

---

**Next:** [127 · Your AI Command Center in Notion + n8n →](127-build-along-ai-command-center.md)
