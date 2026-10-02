# 🔗 Part XIV · n8n & Notion: The Power Stack

Two tools show up in almost every chapter of this manual: **n8n**, the automation engine, and **Notion**, the workspace
where your information lives. Together they form one of the most capable personal and small-team AI stacks you can
build. This part goes deep on both, and shows exactly how they connect to each other and to everything else: your AI
assistants, email, calendar, chat apps, phone, code, business tools and local models.

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Notion is where people see and edit information; n8n is the engine that moves that information, calls AI and connects to other apps. This part teaches both in depth and shows how to combine them into one system.

- **Understand the architecture** and the five ways n8n and Notion connect, then master Notion's data model and API.
- **Build two-way workflows:** Notion buttons and status changes that trigger n8n, and n8n workflows that write results back.
- **Add AI and connect everything else:** agents, RAG, MCP, email, chat, phone and business tools, then run it reliably.

</details>

> [!NOTE]
> **📌 Current as of October 2026**
> Both tools ship updates every few weeks. This part reflects n8n 2.x and the Notion API's data-source model (API version
> 2025-09-03 and later). If a menu has moved, look for the same idea nearby. The concepts last much longer than the labels.

## 🧭 Suggested path

| If you… | Read |
|---|---|
| Want the big picture first | [The Power Stack](120-the-power-stack.md) |
| Already use Notion and want to automate it | [Connecting n8n to Notion](122-connecting-n8n-to-notion.md) → [Notion as Your Command Center](123-notion-as-your-command-center.md) |
| Want to understand Notion properly before automating | [Notion for Builders](121-notion-for-builders.md) |
| Want AI agents that work across both | [AI Agents Across n8n + Notion](124-ai-agents-across-n8n-and-notion.md) |
| Want to connect Gmail, Slack, Claude, your phone and more | [Connecting Everything](125-connecting-everything.md) |
| Just want ready-made workflows | [The n8n + Notion Recipe Book](126-n8n-notion-recipe-book.md) |
| Learn best by building (with screenshots of every n8n screen) | [Build-Along: Your AI Command Center](127-build-along-ai-command-center.md) |
| Rely on this for real work | [Running n8n + Notion in Production](128-running-in-production.md) |

New to either tool? Start with the [n8n Masterclass](../part-5-automation/47-n8n-masterclass.md) (your first AI workflow, click by click) and the
[Notion AI Deep Dive](../part-6-ai-in-your-apps/54-notion-ai-deep-dive.md), then come back here.

## 📚 Chapters in this part

<!-- chapters:start -->
<div class="grid cards clickable" markdown>

-   **[120 · The Power Stack: Why n8n + Notion Can Run Everything 🔗](120-the-power-stack.md)**

    ---

    <span class="card-meta">⏱️ 8 min read · 🎯 Anyone automating their work or life</span>

    Most people's digital life is scattered across a dozen apps that don't talk to each other.

-   **[121 · Notion for Builders: Databases, Data Sources & the API 🧱](121-notion-for-builders.md)**

    ---

    <span class="card-meta">⏱️ 9 min read · 🎯 Notion users ready to automate</span>

    To automate Notion well, you need to see it the way software does. On screen, Notion is pages, tables and boards.

-   **[122 · Connecting n8n to Notion: The Complete Integration Guide 🔌](122-connecting-n8n-to-notion.md)**

    ---

    <span class="card-meta">⏱️ 10 min read · 🎯 Intermediate</span>

    This is the reference chapter you'll keep open while building. It covers connecting n8n to Notion securely, every operation the Notion node offers, the four ways to trigger workflows from Notion, mapping each property type correctly, filtering, falling back to raw API calls, and the patterns (upserts, batching, deduplication) that separate fragile workflows from dependable ones.

-   **[123 · Notion as Your Command Center: Buttons, Pipelines & Two-Way Workflows 🎛️](123-notion-as-your-command-center.md)**

    ---

    <span class="card-meta">⏱️ 5 min read · 🎯 Intermediate</span>

    The most powerful way to combine these tools is to make Notion the control panel for everything n8n does.

-   **[124 · AI Agents Across n8n + Notion 🤖](124-ai-agents-across-n8n-and-notion.md)**

    ---

    <span class="card-meta">⏱️ 8 min read · 🎯 Intermediate → advanced</span>

    AI can live in three places in this stack: inside Notion, inside n8n, and in the assistants you chat with.

-   **[125 · Connecting Everything: n8n + Notion + Your Whole Stack 🌐](125-connecting-everything.md)**

    ---

    <span class="card-meta">⏱️ 9 min read · 🎯 Intermediate</span>

    This chapter is the map of how your n8n + Notion system connects to the rest of your digital life.

-   **[126 · The n8n + Notion Recipe Book: 40 Workflows 🍳](126-n8n-notion-recipe-book.md)**

    ---

    <span class="card-meta">⏱️ 5 min read · 🎯 Anyone with n8n and Notion connected</span>

    Forty proven workflows that combine n8n and Notion, organized by area of life and work. Each recipe lists the trigger, the steps and what you end up with in Notion, plus a difficulty rating.

-   **[127 · Build-Along: Your AI Command Center in Notion + n8n 🏗️](127-build-along-ai-command-center.md)**

    ---

    <span class="card-meta">⏱️ ~3 hours to build · 🎯 Intermediate (no coding required)</span>

    You'll build a working AI command center, one click at a time. Anything you capture (spoken on your phone, sent from any app) lands in a Notion Inbox, already titled, typed and prioritized by AI.

-   **[128 · Running n8n + Notion in Production 🏭](128-running-in-production.md)**

    ---

    <span class="card-meta">⏱️ 7 min read · 🎯 Anyone relying on their automations for real work</span>

    Building a workflow is the fun part; keeping dozens of them running reliably for months is the real skill.

</div>
<!-- chapters:end -->

## 🧰 The starter kit

Everything in this part's build-along is in the repo, ready to import:

| File | What it does |
|---|---|
| [`n8n-notion/README.md`](../../examples/n8n-notion/README.md) | Setup guide and the exact Notion database layouts |
| [`1-capture-to-inbox.json`](../../examples/n8n-notion/1-capture-to-inbox.json) | Any app or phone shortcut → AI triage → Notion Inbox |
| [`2-process-with-ai-button.json`](../../examples/n8n-notion/2-process-with-ai-button.json) | A Notion button → AI plan and subtasks → written back to Notion |
| [`3-daily-briefing.json`](../../examples/n8n-notion/3-daily-briefing.json) | Every morning: tasks due → AI briefing → Notion page + Telegram |
| [`4-error-logger.json`](../../examples/n8n-notion/4-error-logger.json) | Any failed workflow → a row in a Notion "Automation Log" |
| [`5-notion-tools-mcp-server.json`](../../examples/n8n-notion/5-notion-tools-mcp-server.json) | Your Notion task tools, served to Claude or ChatGPT over MCP |
