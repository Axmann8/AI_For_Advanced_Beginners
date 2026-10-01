# 52 · The Automation Recipe Book: 50 Workflows to Steal 🍳⚙️

> ⏱️ 8 min read (or grab one recipe!) · 🎯 Everyone · 🧰 Needs: Zapier, Make, n8n, or phone Shortcuts

**Fifty ready-to-build AI automations**, each written as **trigger → steps → result**, grouped by life area, and rated by
difficulty. Every one works on Zapier, Make or n8n (and many on phone Shortcuts). Pick one that annoys you *today*, build it
this weekend, and enjoy the hours it gives back.

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

This chapter is a collection of 50 automation recipes, organized by area. Each describes the trigger, the steps and the result, with a difficulty rating.

1. **Find a recipe** for the task you'd most like to stop doing manually.
2. **Build it** on your preferred platform, following the method at the end of the chapter.
3. **Test it** with real data before relying on it.

</details>

<!-- in-this-chapter -->

> [!NOTE]
> **📌 How to read the recipes**
> **Trigger → steps → result.** Difficulty: 🟢 easy (under 30 min), 🟡 medium (about an hour), 🔴 spicy (an afternoon).
> "AI" means an AI step (Claude, GPT, Gemini, or a local model). Before anything *sends* or *deletes*, add a **human approval**
> step until you trust it.

## 🧠 Personal productivity

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These recipes support personal productivity: capturing ideas, daily planning, briefings and follow-up reminders.

</details>

| # | Recipe | Trigger → steps → result | Level |
|---|---|---|---|
| 1 | **Morning briefing** | 7:00 → calendar + weather + top news → AI writes a cheerful 100-word brief → phone notification | 🟢 |
| 2 | **Idea inbox** | Phone shortcut (voice) → webhook → AI titles, categorizes, prioritizes → Notion ([importable](../../examples/n8n-workflows/idea-inbox-to-notion.json)) | 🟢 |
| 3 | **Weekly review** | Friday 16:00 → calendar + completed tasks + notes → AI recap (wins, lessons, next week's top 3) → journal page | 🟡 |
| 4 | **Overdue task nudger** | Daily → tasks overdue 3+ days → AI suggests "do, delegate, defer or drop" for each → message | 🟢 |
| 5 | **Meeting prep pack** | 30 min before external meetings → attendee info + past emails + web research → AI 5-bullet brief | 🟡 |
| 6 | **Voice journal** | Voice memo saved → transcription → AI reflection (mood, themes, one kind note to self) → private journal | 🟡 |
| 7 | **Reading list digester** | Link saved to "Read later" → fetch → AI summary + "should I read it fully?" score → reading database | 🟢 |
| 8 | **Habit coach** | Evening → habit tracker data → AI writes an encouraging streak update + tomorrow's tiny goal | 🟢 |

## 📧 Email & communication

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These recipes manage email and communication: triage, summaries, reply drafts and alerts for important messages.

</details>

| # | Recipe | Trigger → steps → result | Level |
|---|---|---|---|
| 9 | **Inbox triage** | New email → AI classifies (urgent / needs reply / FYI / newsletter / receipt) → apply labels | 🟢 |
| 10 | **Draft-a-reply** | Email labeled "needs reply" → AI drafts in your style guide → saved as draft for review | 🟡 |
| 11 | **Newsletter digest** | Daily → all newsletters → AI picks the 5 best items with links → one digest email, then archive the rest | 🟡 |
| 12 | **VIP alert** | Email from key people → AI 2-line summary → phone push | 🟢 |
| 13 | **Follow-up reminder** | Sent email with a question, no reply in 3 days → AI drafts a gentle nudge → task + draft | 🟡 |
| 14 | **Slack catch-up** | Morning → messages mentioning you + key channels → AI summary with "needs your input" list | 🟢 |
| 15 | **Auto-translate** | Message in another language in a shared inbox → AI translation + suggested reply in the same language | 🟢 |

## 💼 Work & business

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These recipes support teams and small businesses: lead handling, customer feedback, meeting follow-ups, invoices and reports.

</details>

| # | Recipe | Trigger → steps → result | Level |
|---|---|---|---|
| 16 | **Lead responder** | Form submitted → AI personalized reply draft + lead score → CRM + draft email ([walkthrough](49-zapier-and-make-walkthroughs.md#-walkthrough-1-ai-lead-responder-15-min)) | 🟢 |
| 17 | **Lead enricher** | New CRM contact → web research → AI fills company size, industry, talking points | 🟡 |
| 18 | **Meeting → actions** | Transcript ready → AI extracts decisions and owners → tasks in PM tool + recap email draft | 🟡 |
| 19 | **Support sorter** | New ticket → AI classifies + drafts answer from the help center → human approves in Slack | 🟡 |
| 20 | **Review responder** | New Google or app store review → AI drafts a warm, specific reply → approval → post | 🟡 |
| 21 | **Invoice extractor** | Invoice email → AI reads PDF → Sheets row + due-date calendar event ([walkthrough](49-zapier-and-make-walkthroughs.md#-walkthrough-5-invoice-extractor)) | 🟡 |
| 22 | **Weekly KPI report** | Monday → pull metrics (Sheets, Stripe, analytics) → AI narrative "what changed and why it matters" → Slack | 🟡 |
| 23 | **Onboarding buddy** | New hire added → AI generates a personalized first-week plan from the handbook → email + tasks | 🔴 |

## 🎨 Content & creators

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These recipes help creators repurpose content across channels, plan posts and capture ideas.

</details>

| # | Recipe | Trigger → steps → result | Level |
|---|---|---|---|
| 24 | **Content repurposer** | New blog post → AI writes thread + LinkedIn post + newsletter blurb → drafts ([walkthrough](49-zapier-and-make-walkthroughs.md#-walkthrough-4-social-media-repurposer-30-min)) | 🟡 |
| 25 | **YouTube → blog** | New video → transcript → AI article with headings and quotes → CMS draft | 🟡 |
| 26 | **Podcast show notes** | New episode → transcript → AI show notes, timestamps, 5 clip ideas → Notion | 🟡 |
| 27 | **Idea bank** | Saved tweets, articles and notes tagged #idea → AI clusters weekly into 5 content themes | 🟡 |
| 28 | **Comment helper** | New comments on your posts → AI flags questions worth answering and drafts replies | 🟢 |
| 29 | **Thumbnail brainstorm** | New video title → AI suggests 5 thumbnail concepts + generates 2 with an image model | 🔴 |

## 🔬 Learning & research

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These recipes support learning and research: topic monitoring, study aids and research digests.

</details>

| # | Recipe | Trigger → steps → result | Level |
|---|---|---|---|
| 30 | **Topic radar** | Daily → RSS + Google News for your topics → AI filters and ranks → digest ([Web Scraping & Monitoring](51-web-scraping-and-monitoring.md)) | 🟢 |
| 31 | **Paper alerts** | New arXiv or PubMed papers on your keywords → AI plain-English summary + "why it matters" | 🟡 |
| 32 | **Flashcard factory** | New note in "Learning" folder → AI makes 5–10 Q&A flashcards → Anki or a spaced-repetition app | 🟡 |
| 33 | **Lecture digester** | New lecture recording → transcription → AI study notes + quiz → notes app | 🟡 |
| 34 | **Word of the day** | Daily → AI picks a word in the language you're learning, with examples at your level → notification | 🟢 |
| 35 | **Deep-dive Friday** | Friday → AI research agent writes a cited 1-page brief on a question from your list | 🔴 |

## 💰 Money & admin

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These recipes handle financial and administrative tasks: receipts, bills, subscriptions and paperwork.

</details>

| # | Recipe | Trigger → steps → result | Level |
|---|---|---|---|
| 36 | **Receipt tracker** | Receipt photo (phone) or email → AI extracts merchant, amount, category → spreadsheet | 🟢 |
| 37 | **Subscription spotter** | Monthly → bank CSV export → AI finds recurring charges and price increases → summary | 🟡 |
| 38 | **Bill reminder** | Bill email → AI extracts amount and due date → calendar reminder 3 days before | 🟢 |
| 39 | **Paperwork explainer** | Letter photo → AI plain-English summary + deadline + action → task with due date | 🟢 |
| 40 | **Budget check-in** | Weekly → spending by category vs. budget → AI friendly coach note with one suggestion | 🟡 |

## 🏡 Home & family

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These recipes help at home: meal planning, school communications, chores, plant care and family scheduling.

</details>

| # | Recipe | Trigger → steps → result | Level |
|---|---|---|---|
| 41 | **Meal planner** | Sunday → your preferences + pantry note → AI plans 5 dinners + grocery list by aisle → shared list | 🟢 |
| 42 | **School email decoder** | Email from school → AI extracts dates, forms and things to bring → family calendar + checklist | 🟡 |
| 43 | **Chore rotation** | Monday → AI assigns chores fairly from last week's history → family chat message | 🟢 |
| 44 | **Plant care buddy** | Daily → weather + your plant list → AI "water today?" advice → notification 🌱 | 🟢 |
| 45 | **Birthday concierge** | 7 days before a birthday → AI gift ideas from your notes about the person + a card message draft | 🟢 |

## 🛠️ Developer & tech

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These recipes help developers and technical teams: pull request summaries, error alerts, changelogs and uptime checks.

</details>

| # | Recipe | Trigger → steps → result | Level |
|---|---|---|---|
| 46 | **PR summarizer** | New pull request → AI summary + risk notes → comment or Slack | 🟡 |
| 47 | **Error explainer** | New error in Sentry/logs → AI explains likely cause + first debugging step → ticket | 🟡 |
| 48 | **Changelog writer** | Weekly → merged PRs → AI friendly release notes → Slack + docs draft | 🟢 |
| 49 | **Uptime storyteller** | Monitor alert → AI incident summary from recent deploys and metrics → #incidents draft | 🔴 |
| 50 | **Dependency watch** | Weekly → outdated packages → AI flags breaking changes from changelogs → issue | 🟡 |

## 🧑‍🍳 How to build any recipe (the method)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Build any recipe using the same method:

1. Write it as one sentence: *"When [trigger], get [data], ask AI to [task], then [action]."*
2. Build the trigger and capture a real sample.
3. Add the AI step and check its output on the sample.
4. Add the final action, with an approval step for anything important.
5. Turn it on and review the first few runs.

</details>

1. **Write it down first:** *"When [trigger], get [data], ask AI to [job], then [action]."*
2. **Build the trigger** and capture a real sample (pin it in n8n or Make).
3. **Add the AI step** with a clear prompt, and **ask for JSON** if the next step needs fields.
4. **Test on 3–5 real samples.** Tweak the prompt until it's right every time.
5. **Add the action**, with an **approval step** if it sends, posts or deletes.
6. **Add error alerts** and a log (a sheet of every run).
7. **Turn it on**, and check the log daily for the first week.

## 📝 Design your own recipe

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Use this template to design your own automation. If you can complete each line, you have everything you need to build it.

</details>

```markdown
### Recipe: ________________
- ⚡ Trigger: ________________ (schedule / new email / form / webhook / phone button)
- 📥 Gather: ________________ (what data does it need?)
- 🤖 AI job: ________________ (summarize / classify / extract / draft / decide)
- 🔀 Route: ________________ (any if/else?)
- 📤 Action: ________________ (where does the result go?)
- 🧑‍⚖️ Approval needed? yes / no
- ⏱️ Time saved per week: ____ min
```

## 🎯 Key takeaways

- Every recipe is **trigger → steps → result**. Once you see it, you can invent your own.
- Start with a **🟢 easy** recipe that fixes a *real* annoyance.
- **Test on real samples**, ask for **JSON**, and add **approvals** before anything outbound.
- Log every run for the first week, then relax and enjoy the time you got back. 😌

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Which recipe step should you add before an automation sends email to customers?</summary>

A **human approval** step (a draft or send-and-wait) until it's proven reliable.

</details>

<details class="quiz">
<summary>❓ 2. What's the first thing to do when building any recipe?</summary>

**Write the one-sentence recipe** (when/get/ask/then), then build the trigger and capture a real sample.

</details>

> [!TIP]
> **🎮 Try this**
> Pick the recipe that fixes your **biggest weekly annoyance**, fill in the **design form**, and build it this weekend. Then
> calculate the time saved per year (minutes per week × 52), and prepare to feel very smug. 😎

---

**Next:** [53 · AI Inside the Apps You Already Use →](../part-6-ai-in-your-apps/53-ai-in-your-apps.md)
