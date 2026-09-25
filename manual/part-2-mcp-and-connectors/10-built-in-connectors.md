# 10 · Built-in Connectors & Plugins 🧩✨

> ⏱️ 8 min read · 🎯 Beginner-friendly · 🧰 Needs: an account with Claude, ChatGPT, Gemini or Copilot

**MCP is the engine. Connectors are the polished, click-to-install version inside the big AI apps.** If you want results
*today* with zero config files, start here. You'll learn what each major assistant offers, how connectors differ from
skills and plugins, the best combos, and how to keep permissions tidy.

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Connectors are like apps on your phone's app store, but for your AI. Tap "Connect Gmail," log in, and now your AI can
read and help with your email. No setup files, no code. This chapter shows you where the "app store" is in each AI app
and which connections give you the biggest wow.

</details>

<!-- in-this-chapter -->

## 🧩 Connectors vs. MCP vs. skills vs. plugins

<details class="eli5">
<summary>🧸 ELI5</summary>

A **connector** is a door to one app. A **skill** is a how-to guide the AI can pull off the shelf. A **plugin** is a gift
box with several doors and guides inside. **Raw MCP** is building the door yourself.

</details>

| | 🔌 Built-in connector | 🛠️ Raw MCP server | 🎓 Skill | 🎁 Plugin / bundle |
|---|---|---|---|---|
| What it is | A ready-made link to one service | Any MCP server you configure | Packaged instructions (+ optional scripts) for a task | A bundle of connectors, skills, commands |
| Setup | Click, then log in | Config file or URL | Upload or install | One install |
| Under the hood | Usually MCP! | MCP | Files the AI loads when relevant | Mix of the above |
| Best for | Everyday apps (Gmail, Drive, Notion, Slack) | Niche tools, local files, your own code | Repeatable workflows ("make a deck in our style") | A whole role or workflow at once |

**Rule of thumb:** use the connector if one exists. Drop to raw MCP when it doesn't, or when you want something local or
custom. Add skills when you keep explaining the same process.

## 🟠 Claude

<details class="eli5">
<summary>🧸 ELI5</summary>

Claude has a directory where you can add connectors, skills and plugins with a click, plus Projects for standing
instructions and Artifacts for building mini apps.

</details>

| Feature | What it does |
|---|---|
| **Connectors directory** (Settings → Connectors) | One-click connections: Google Workspace, Notion, Slack, GitHub, Linear, Asana, Atlassian, Canva, Figma, Stripe, DocuSign, and many more |
| **Custom connectors** | Paste any remote MCP server URL |
| **Desktop Extensions** (`.mcpb`) | One-click local servers for Claude Desktop |
| **Skills** | Packaged instructions and scripts Claude loads on demand ("make a deck in our brand," "fill this PDF form"), and you can write your own |
| **Plugins** | Bundles of connectors, skills and commands for a role or workflow |
| **Projects** | Standing instructions + files per project, plus memory across chats |
| **Artifacts** | Claude builds live mini apps, documents and dashboards you can share |
| **Research** | Multi-step research across the web and your connectors, with citations |
| **Claude in Chrome** | Claude can read and act on web pages in your browser ([Computer Use](../part-5-building-with-ai/40-computer-use-and-browser-agents.md)) |

## 🟢 ChatGPT

<details class="eli5">
<summary>🧸 ELI5</summary>

ChatGPT has plugins (little apps that can even show buttons and forms inside the chat), connectors to your files, an agent
that can browse for you, and a developer mode for adding any MCP server.

</details>

| Feature | What it does |
|---|---|
| **Plugins** (renamed from "apps" in mid-2026) | Third-party integrations that can show **interactive UI** in the chat, built on MCP |
| **Connectors** | Drive, Gmail, Calendar, SharePoint, GitHub and more, used by chat and deep research |
| **Developer Mode** | Add *any* remote MCP server with full read and write tools (plan- and workspace-dependent) |
| **Agent mode** | A browser + terminal agent for multi-step web tasks |
| **Custom GPTs & Projects** | Reusable assistants and project workspaces |
| **Memory** | Remembers preferences across chats (viewable and editable) |

## 🔵 Google Gemini

<details class="eli5">
<summary>🧸 ELI5</summary>

Gemini is best friends with Gmail, Docs, Drive, Calendar, Maps and YouTube, so it can help across all your Google stuff.
It also comes with NotebookLM, a magical study buddy.

</details>

- **Deep integration** with Gmail, Docs, Drive, Calendar, Maps and YouTube.
- **Gems:** custom assistants with standing instructions.
- **Deep Research** and **Canvas** for long reports and live documents.
- **NotebookLM:** grounded research on your sources with audio overviews ([NotebookLM Masterclass](../part-6-knowledge-and-memory/45-notebooklm-masterclass.md)).
- **Gemini CLI:** an open-source terminal agent that speaks MCP.
- More in [Google Workspace & Microsoft 365 AI](../part-4-ai-in-your-apps/24-google-and-microsoft-ai.md).

## 🟣 Microsoft Copilot

<details class="eli5">
<summary>🧸 ELI5</summary>

Copilot lives inside Outlook, Teams, Word and Excel, and companies can build their own Copilot helpers that connect to
their tools (including MCP servers).

</details>

- **Microsoft 365 Copilot** works across Outlook, Teams, Word, Excel, PowerPoint and SharePoint using your work data.
- **Copilot Studio** lets organizations build agents with connectors, actions and **MCP tools**.
- **Power Platform connectors** (1,000+) plug into Power Automate flows.
- **GitHub Copilot** brings agents and MCP to coding ([Cursor & AI IDEs](../part-5-building-with-ai/33-cursor-and-ai-ides.md)).

## ⚫ Others worth knowing

<details class="eli5">
<summary>🧸 ELI5</summary>

Lots of other apps have their own connector shelves too: your notes app, your chat app, your computer's launcher and your phone.

</details>

| App | Connector story |
|---|---|
| **Perplexity** | Search-first AI with connectors for files and apps |
| **Notion AI** | Its own agents plus MCP connections to other tools ([Notion AI Deep Dive](../part-4-ai-in-your-apps/23-notion-ai-deep-dive.md)) |
| **Slack** | AI features and agents inside Slack, plus an official MCP server |
| **Raycast** (Mac/Windows) | System-wide AI with extensions and MCP |
| **Apple Intelligence** | On-device features, ChatGPT integration, Shortcuts that call AI models ([Phone & Desktop Automation](../part-3-automation/19-phone-and-desktop-automation.md)) |

## ✨ Ten connector combos that feel like magic

<details class="eli5">
<summary>🧸 ELI5</summary>

Connecting two or three apps at once is where AI really shines: it can take something from one app, think about it, and
put the result in another.

</details>

| # | Combo | Prompt |
|---|---|---|
| 1 | 📧 Gmail + 📅 Calendar | *"Find emails where someone asked to meet and I haven't replied. Propose times that fit my calendar and draft replies."* |
| 2 | 📁 Drive + 📒 Notion | *"Read my last 5 meeting-notes docs and build a Notion project tracker from the action items."* |
| 3 | 💬 Slack + 📐 Linear | *"Scan #bugs this week and file Linear issues for anything not already tracked."* |
| 4 | 🐙 GitHub + 💬 Slack | *"Write a friendly weekly changelog from merged PRs and post it to #updates."* |
| 5 | 🎨 Canva + 📁 Drive | *"Take the stats from my Q3 doc and make an infographic in Canva."* |
| 6 | 📅 Calendar + 🔎 web search | *"For each external meeting this week, research the company and give me 3 talking points."* |
| 7 | 📧 Gmail + 📊 Sheets | *"Find every receipt email from last month and list vendor, date and amount in a sheet."* |
| 8 | 📒 Notion + 🔎 Research | *"Research the best beginner telescopes under $500 and save a comparison page to Notion."* |
| 9 | ✍️ DocuSign + 📧 Gmail | *"Which contracts are waiting on signatures? Draft polite nudges to each signer."* |
| 10 | 📁 Drive + 🎓 a skill | *"Using our brand-deck skill, turn this strategy doc into a 10-slide deck."* |

More in [The MCP Recipe Book](13-mcp-recipe-book.md).

## 🔐 Permissions & approvals

<details class="eli5">
<summary>🧸 ELI5</summary>

For each connector you choose what the AI may do: always allowed, ask me first, or never. Keep "ask me first" for anything
that sends, deletes or spends.

</details>

- **Per-tool settings:** most apps let you set each tool to **always allow**, **ask first** or **never**.
- **Ask first** for anything that **sends, deletes, buys, shares or posts publicly**.
- **Least privilege:** when a connector asks for scopes, prefer read-only if that's all you need.
- **Revoke anytime:** disconnect in the AI app *and* remove access in the service's security settings (e.g. your
  Google account's third-party access page).
- **Turn off unused connectors:** fewer tools = more focused AI + smaller risk.

## 🏢 Connectors at work

<details class="eli5">
<summary>🧸 ELI5</summary>

At work, the grown-ups in IT decide which doors are allowed. If a connector is missing, ask them nicely. They're trying
to keep company data safe.

</details>

- On **Team/Enterprise** plans, admins often choose which connectors are available and who can use them.
- Company data policies may restrict connecting personal accounts to work assistants (and vice versa).
- If a connector you need isn't available, ask IT, and explain the task and the data involved. That makes a "yes" more likely.
- Many enterprises route MCP through **gateways** that log and control access ([MCP Security & Trust](12-mcp-security-and-trust.md)).

## 🧭 Connector, MCP server, or automation?

<details class="eli5">
<summary>🧸 ELI5</summary>

Use a connector when you want to *ask* your AI about an app. Use an automation when you want something to *happen by
itself*. Build an MCP server when no connector exists.

</details>

| You want… | Use |
|---|---|
| To *ask* your AI about your email, docs or tasks, when you feel like it | 🔌 **Connector** |
| A tool no connector covers (local files, your database, a niche app) | 🛠️ **MCP server** |
| Something to happen *automatically* on a schedule or trigger | ⚙️ **Automation** ([Part III](../part-3-automation/index.md)) |
| A repeatable multi-step process done the same way every time | 🎓 **Skill** or automation |
| A whole team setup in one go | 🎁 **Plugin** |

## 🎯 Key takeaways

- **Connectors** = click-to-install MCP inside AI apps, and the fastest path to value.
- Claude, ChatGPT, Gemini and Copilot all have connector ecosystems, plus **skills**, **plugins** and **projects**.
- **Cross-app prompts** (2–3 connectors at once) create the biggest wins.
- Keep **ask-first** on for risky actions, grant **least privilege**, and **revoke** what you don't use.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. What's the difference between a connector and a skill?</summary>

A **connector** gives the AI access to an app or data source. A **skill** gives it packaged know-how (instructions, and
optionally scripts) for doing a task well.

</details>

<details class="quiz">
<summary>❓ 2. You want a weekly summary emailed every Friday automatically. Connector or automation?</summary>

**Automation**. Connectors are for when *you* ask. Schedules and triggers belong to automation platforms.

</details>

<details class="quiz">
<summary>❓ 3. Which tool permission setting should "send email" have?</summary>

**Ask first** (or never, until you trust the setup).

</details>

> [!TIP]
> **🎮 Try this**
> Connect **two** apps you use daily and run combo #1 or #2 from the table above. Cross-app tasks are where the time
> savings really show up, often 30+ minutes saved on the very first try. ⏱️

---

**Next:** [11 · Building MCP Servers →](11-building-mcp-servers.md)
