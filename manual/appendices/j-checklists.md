# Appendix J · Printable Checklists ✅🖨️

> ⏱️ 8 min read · 🎯 Everyone · 🧰 Needs: a printer, a pen, or a checklist app

**The manual's most useful checklists, gathered in one printable place.** Stick them on the fridge, pin them above your desk, or
paste them into Notion. Each one links back to the chapter that explains the *why*. Tick boxes, feel great. ✅

<details class="eli5" open>
<summary>🧸 ELI5: This page in 30 seconds</summary>

Checklists are like packing lists for a trip: you tick each thing so you don't forget anything important. These ones help you
set up AI safely, launch projects, and build good habits. 📝✔️

</details>

<!-- in-this-chapter -->

## 🚀 Your first week with AI

<details class="eli5">
<summary>🧸 ELI5</summary>

Seven small steps for your first week, one a day.

</details>

- [ ] Pick **one main assistant** and set custom instructions about you ([Your First Hour](../start-here/b-your-first-hour.md))
- [ ] Try **voice mode** on a walk
- [ ] Show it a **photo** and ask about it
- [ ] Connect **one app** (email, calendar or Drive) ([Built-in Connectors](../part-4-mcp-and-connectors/41-built-in-connectors.md))
- [ ] Make a **Gemini Notebook** from 5 sources and generate an Audio Overview
- [ ] Do the **overwhelm reset** prompt ([Life Admin](../part-11-ai-for-life-and-work/95-life-admin-and-productivity.md#-the-overwhelm-reset))
- [ ] Teach **one person** something you learned 💛

## 🛡️ Safety pre-flight (before anything runs unattended)

<details class="eli5">
<summary>🧸 ELI5</summary>

Check these before letting a robot run by itself.

</details>

- [ ] **Spend limit** and alerts set in every API console
- [ ] **Tested on a small batch** first
- [ ] **Destructive or outbound actions** (send, delete, pay, post) gated behind approval
- [ ] **Secrets** in env vars, not in code, workflows or repos
- [ ] **Failure notification** set up
- [ ] No **private data + untrusted content + outbound actions** without a human gate

([Safety, Costs & Gotchas](../part-12-mastery/103-safety-costs-and-gotchas.md))

## 🔒 Privacy settings tune-up

<details class="eli5">
<summary>🧸 ELI5</summary>

Switches to check in every AI app, so your information goes only where you want.

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

<details class="eli5">
<summary>🧸 ELI5</summary>

Before adding a plug-in, make sure it comes from someone you trust and only gets the access it needs.

</details>

- [ ] From an **official** vendor, the MCP Registry, or a source I trust
- [ ] I've read what tools it has and what they can **do**
- [ ] **Version pinned** for anything important
- [ ] **Least access** (e.g. filesystem scoped to one folder, read-only tokens)
- [ ] Untrusted servers run in **Docker** or a sandbox
- [ ] Approvals **on** for destructive tools

([MCP Security & Trust](../part-4-mcp-and-connectors/43-mcp-security-and-trust.md))

## 🧑‍💻 Before asking a coding agent for a big change

<details class="eli5">
<summary>🧸 ELI5</summary>

Get ready before your AI helper makes big changes, so you can always undo.

</details>

- [ ] Working state **committed** (save point!)
- [ ] **Plan mode** first, and I've read the plan
- [ ] "**Done** means…" written down (tests pass, page loads, works on mobile)
- [ ] The agent has a way to **verify** (tests, Playwright, a command)
- [ ] `CLAUDE.md` / `AGENTS.md` is up to date
- [ ] Dangerous commands still on **ask**

([Claude Code Masterclass](../part-7-building-with-ai/62-claude-code-masterclass.md))

## 🌍 Launching a web app

<details class="eli5">
<summary>🧸 ELI5</summary>

Check all the locks before inviting people to your app.

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

<details class="eli5">
<summary>🧸 ELI5</summary>

Steps before sharing your plug-in with the world.

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

<details class="eli5">
<summary>🧸 ELI5</summary>

Check these before a talking robot answers real phone calls.

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

<details class="eli5">
<summary>🧸 ELI5</summary>

Questions to make sure what you built is fair, honest and kind.

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

<details class="eli5">
<summary>🧸 ELI5</summary>

Little things to do every week so you keep learning and stay organized.

</details>

- [ ] Triage my notes inbox ([Second Brain](../part-13-build-alongs/114-build-along-second-brain.md))
- [ ] Friday weekly review
- [ ] Try **one** new AI thing (30 minutes)
- [ ] Skim one newsletter or my digest ([Staying Current](../part-12-mastery/110-staying-current.md))
- [ ] Add one line to my **learning log**
- [ ] Check automation executions for failures
- [ ] Glance at API usage dashboards 💸

## 🗓️ Monthly & quarterly maintenance

<details class="eli5">
<summary>🧸 ELI5</summary>

Bigger check-ups every month and every few months.

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
