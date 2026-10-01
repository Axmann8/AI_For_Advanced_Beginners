# Appendix J · Printable Checklists ✅🖨️

> ⏱️ 8 min read · 🎯 Everyone · 🧰 Needs: a printer, a pen, or a checklist app

**The manual's most useful checklists, gathered in one printable place.** Stick them on the fridge, pin them above your desk, or
paste them into Notion. Each one links back to the chapter that explains the *why*. Tick boxes, feel great. ✅

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These checklists cover the moments where a quick review prevents problems: getting started, protecting your privacy, installing tools, launching projects and maintaining good habits. Print them or copy them into your notes.

- **Getting started:** beginner setup, scam protection and your first week.
- **Before you launch:** safety pre-flight, MCP installation, coding changes, web apps, MCP publishing and voice agents.
- **Ongoing:** ethics review, weekly habits and monthly and quarterly maintenance.

</details>

<!-- in-this-chapter -->

## 🐣 Absolute beginner's starter checklist

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Use this checklist if you've never used an AI assistant: choose one, secure your account, adjust key settings and have your first conversations.

</details>

- [ ] Choose **one** assistant ([Choosing Your First AI Assistant](../part-1-ai-from-zero/04-choosing-your-first-assistant.md))
- [ ] Install the **official app** (check the developer name) and sign in
- [ ] Turn on **two-step verification**
- [ ] Fill in **custom instructions** about you ([Getting Set Up](../part-1-ai-from-zero/05-getting-set-up.md))
- [ ] Have your **first three conversations** ([Your First AI Conversation](../part-1-ai-from-zero/03-your-first-ai-conversation.md))
- [ ] Use the **five-ingredient** prompt recipe once ([Prompting 101](../part-1-ai-from-zero/06-prompting-101.md))
- [ ] **Fact-check** one answer by clicking its sources ([When AI Gets It Wrong](../part-1-ai-from-zero/10-when-ai-gets-it-wrong.md))
- [ ] Learn where **memory**, **training** and **temporary chat** settings live
- [ ] Start the [30-Day Plan](../part-1-ai-from-zero/16-your-30-day-plan.md) 🎉

## 🛡️ Scam-proof your family

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These steps protect your family from AI-powered scams such as cloned voices and deepfakes.

</details>

- [ ] Agree a **family safe word** for emergency calls
- [ ] Tell older relatives and teens about **voice-cloning** scams
- [ ] Rule: **hang up and call back** on a known number before sending money
- [ ] Never **invest** from a video ad, however famous the face
- [ ] Only install **official** AI apps and trusted browser extensions
- [ ] Know how to **report** fraud and who to call at your bank

([Staying Safe: Privacy, Scams & Deepfakes](../part-1-ai-from-zero/11-staying-safe-with-ai.md))

## 🚀 Your first week with AI

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These seven steps, one per day, establish your first AI habits.

</details>

- [ ] Pick **one main assistant** and set custom instructions about you ([Your First Hour](../start-here/b-your-first-hour.md))
- [ ] Try **voice mode** on a walk
- [ ] Show it a **photo** and ask about it
- [ ] Connect **one app** (email, calendar or Drive) ([Built-in Connectors](../part-4-mcp-and-connectors/41-built-in-connectors.md))
- [ ] Make a **Gemini Notebook** from 5 sources and generate an Audio Overview
- [ ] Do the **overwhelm reset** prompt ([Life Admin](../part-11-ai-for-life-and-work/95-life-admin-and-productivity.md#-the-overwhelm-reset))
- [ ] Teach **one person** something you learned 💛

## 🛡️ Safety pre-flight (before anything runs unattended)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Confirm each item before letting any automation or agent run unattended.

</details>

- [ ] **Spend limit** and alerts set in every API console
- [ ] **Tested on a small batch** first
- [ ] **Destructive or outbound actions** (send, delete, pay, post) gated behind approval
- [ ] **Secrets** in env vars, not in code, workflows or repos
- [ ] **Failure notification** set up
- [ ] No **private data + untrusted content + outbound actions** without a human gate

([Safety, Costs & Gotchas](../part-12-mastery/103-safety-costs-and-gotchas.md))

## 🔒 Privacy settings tune-up

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Review these settings in every AI app you use so your information is handled the way you choose.

</details>

- [ ] Model training / "help improve" setting chosen deliberately
- [ ] Chat history and retention understood
- [ ] Memory reviewed, and wrong or unwanted items deleted
- [ ] Know how to start a **temporary/incognito** chat
- [ ] Connectors reviewed (least access, remove unused)
- [ ] Old shared links revoked
- [ ] Two-factor authentication on 🔑

([Privacy & Your Data](../part-12-mastery/104-privacy-and-your-data.md))

## 🔌 Installing an MCP server safely

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Before installing an MCP server, confirm it comes from a trusted source and requests only the access it needs.

</details>

- [ ] From an **official** vendor, the MCP Registry, or a source I trust
- [ ] I've read what tools it has and what they can **do**
- [ ] **Version pinned** for anything important
- [ ] **Least access** (e.g. filesystem scoped to one folder, read-only tokens)
- [ ] Untrusted servers run in **Docker** or a sandbox
- [ ] Approvals **on** for destructive tools

([MCP Security & Trust](../part-4-mcp-and-connectors/43-mcp-security-and-trust.md))

## 🧑‍💻 Before asking a coding agent for a big change

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Complete these steps before asking a coding agent to make a large change, so you can always roll back.

</details>

- [ ] Working state **committed** (save point!)
- [ ] **Plan mode** first, and I've read the plan
- [ ] "**Done** means…" written down (tests pass, page loads, works on mobile)
- [ ] The agent has a way to **verify** (tests, Playwright, a command)
- [ ] `CLAUDE.md` / `AGENTS.md` is up to date
- [ ] Dangerous commands still on **ask**

([Claude Code Masterclass](../part-7-building-with-ai/62-claude-code-masterclass.md))

## 🌍 Launching a web app

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Confirm each item before inviting users to a web app you've built.

</details>

- [ ] **Row-level security** on every table, tested with a second account
- [ ] **No secret keys** in browser code or `NEXT_PUBLIC_`/`VITE_` variables
- [ ] **AI calls** behind login, with rate limits
- [ ] **Spend limits** on AI keys
- [ ] `.env` in `.gitignore`, no secrets ever committed
- [ ] Works on a **phone**
- [ ] Accessibility pass: contrast, labels, keyboard
- [ ] One real friend has used it 🎉

([Vibe Coding](../part-7-building-with-ai/65-vibe-coding-your-first-app.md), [Deploying & Hosting](../part-7-building-with-ai/66-deploying-and-hosting.md))

## 📦 Publishing an MCP server

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Complete these steps before publishing an MCP server for others to use.

</details>

- [ ] `npm test` passes
- [ ] Tool names, descriptions and annotations are clear
- [ ] README with install config and example prompts
- [ ] `mcpName` = `server.json` `name`, and identifiers and versions match
- [ ] License added, repo public
- [ ] `npm publish --access public`, then `mcp-publisher publish`
- [ ] Remote version (if any) has **real auth**

([Build-Along: Publish Your Own MCP Server](../part-13-build-alongs/113-build-along-publish-an-mcp-server.md))

## 🗣️ Voice agent go-live

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Confirm each item before a voice agent handles real phone calls.

</details>

- [ ] Says it's an **AI assistant** at the start
- [ ] **Recording consent** handled per local law
- [ ] **Inbound only** (outbound AI calls have strict rules)
- [ ] **Human path** (transfer or message) always available
- [ ] **Spend limits** and usage alerts
- [ ] Transcripts stored securely, deleted on a schedule
- [ ] 10+ test calls listened to end to end

([Build-Along: An AI Voice Receptionist](../part-13-build-alongs/119-build-along-voice-receptionist.md))

## ⚖️ The builder's ethics check

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Review these questions before releasing anything you've built, to confirm it's honest, consensual, fair and safe.

</details>

- [ ] **Honest:** people know when it's AI, and what it can't do
- [ ] **Consent:** for every face, voice, dataset and creative work
- [ ] **Fair:** tested with one-attribute variants
- [ ] **Private:** collect less, protect it, let people delete
- [ ] **Safe:** risky actions need human approval
- [ ] **Accountable:** an owner, a log, an appeal path
- [ ] **Accessible:** people with disabilities can use it
- [ ] Comfortable seeing it on the **front page**, explained in full 📰

([AI Ethics for Builders](../part-12-mastery/107-ai-ethics-for-builders.md))

## 🔁 Weekly AI habits

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These short weekly habits keep your notes organized and your skills growing.

</details>

- [ ] Triage my notes inbox ([Second Brain](../part-13-build-alongs/114-build-along-second-brain.md))
- [ ] Friday weekly review
- [ ] Try **one** new AI thing (30 minutes)
- [ ] Skim one newsletter or my digest ([Staying Current](../part-12-mastery/110-staying-current.md))
- [ ] Add one line to my **learning log**
- [ ] Check automation executions for failures
- [ ] Glance at API usage dashboards 💸

## 🗓️ Monthly & quarterly maintenance

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

These periodic reviews keep your subscriptions, data, security and tools in good shape.

</details>

**Monthly**

- [ ] Review subscriptions and cancel unused tools
- [ ] Review AI memory and delete stale facts
- [ ] Update the home lab (`docker compose pull && docker compose up -d`)
- [ ] Back up workflows, vault and databases

**Quarterly**

- [ ] Re-run my personal eval on current models ([Evaluating AI](../part-12-mastery/105-evaluating-ai.md))
- [ ] Re-evaluate my stack ([Choosing Your AI Stack](../part-3-foundations/37-choosing-your-ai-stack.md))
- [ ] Rotate API keys and remove unused connectors
- [ ] Pick next quarter's build from the [Project Ideas](f-project-ideas.md) 🚀

---

**You made it to the end! 🎉** [Back to the manual home ↩](../index.md)
