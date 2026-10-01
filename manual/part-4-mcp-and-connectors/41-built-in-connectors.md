# 41 · Built-in Connectors & Plugins 🧩✨

> ⏱️ 9 min read · 🎯 Beginner-friendly · 🧰 Needs: an account with Claude, ChatGPT, Gemini or Copilot

**MCP is the engine. Connectors are the polished, click-to-install version inside the big AI apps.** If you want results
*today* with zero config files, start here. You'll learn what each major assistant offers, how connectors differ from
skills and plugins, the best combos, and how to keep permissions tidy.

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Built-in connectors are the simplest way to link an AI assistant to your other apps: choose an app from a directory, sign in, and the assistant can work with it. No configuration files or code are needed.

- **Know the terms:** connectors, raw MCP servers, skills and plugins each serve a different purpose.
- **Each assistant** (Claude, ChatGPT, Gemini, Copilot and others) has its own directory and features.
- **Combine connectors** for the most useful workflows, and set approvals for actions that send, delete or spend.

</details>

<!-- in-this-chapter -->

## 🧩 Connectors vs. MCP vs. skills vs. plugins

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

A **connector** is a ready-made link to one service. A **raw MCP server** is any server you configure yourself. A **skill** is a packaged set of instructions the AI loads when relevant. A **plugin** bundles several of these together. The table compares them.

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

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Claude offers a connectors directory in **Settings → Connectors**, plus skills, plugins, Projects for standing instructions and Artifacts for building interactive content. The table describes each feature.

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
| **Claude in Chrome** | Claude can read and act on web pages in your browser ([Computer Use](../part-7-building-with-ai/71-computer-use-and-browser-agents.md)) |

## 🟢 ChatGPT

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

ChatGPT offers plugins (third-party integrations that can show interactive elements in the chat), connectors to your files and accounts, agent mode for web tasks, and a developer mode for adding any MCP server.

</details>

| Feature | What it does |
|---|---|
| **Plugins** (renamed from "apps" in mid-2026) | Third-party integrations that can show **interactive UI** in the chat, built on MCP |
| **Connectors** | Drive, Gmail, Calendar, SharePoint, GitHub and more, used by chat and deep research |
| **Developer Mode** | Add *any* remote MCP server with full read and write tools (plan- and workspace-dependent) |
| **Agent mode** | A browser + terminal agent for multi-step web tasks |
| **Projects & skills** | Project workspaces with instructions and files; **skills** (inside plugins) replace custom GPTs, which retire on December 11, 2026 |
| **Scheduled tasks & ChatGPT Work** | Recurring jobs, and an agent that turns a goal into finished docs, sheets and slides |
| **Memory** | Remembers preferences across chats (viewable and editable) |

## 🔵 Google Gemini

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Gemini integrates deeply with Google's services: Personal Intelligence draws on Gmail, Calendar, Drive, Photos, YouTube and Maps, and Gemini Notebook (formerly NotebookLM) answers questions from sources you provide.

</details>

- **Personal Intelligence** (opt-in): Gemini uses your Gmail, Calendar, Drive, Photos, YouTube and Maps to answer
  questions about *your* life ([Gemini guide](../part-2-ai-assistants-field-guide/19-gemini.md)).
- **Deep integration** with Gmail, Docs, Drive, Calendar, Maps and YouTube.
- **Gems:** custom assistants with standing instructions.
- **Deep Research** and **Canvas** for long reports and live documents.
- **Gemini Notebook (NotebookLM):** grounded research on your sources with audio overviews ([Gemini Notebook (NotebookLM) Masterclass](../part-8-knowledge-and-memory/76-notebooklm-masterclass.md)).
- **Gemini CLI:** an open-source terminal agent that speaks MCP.
- More in [Google Workspace & Microsoft 365 AI](../part-6-ai-in-your-apps/55-google-and-microsoft-ai.md).

## 🟣 Microsoft Copilot

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Copilot connects to your Microsoft 365 email and files and works inside Outlook, Teams, Word and Excel. Organizations can build custom Copilot agents that connect to their own tools, including MCP servers.

</details>

- **The Microsoft Copilot app** (consumer and work apps merged in 2026) connects to your Microsoft 365 files and email.
- **Microsoft 365 Copilot** works across Outlook, Teams, Word, Excel, PowerPoint and SharePoint using your work data.
- **Copilot Studio** lets organizations build agents with connectors, actions and **MCP tools**.
- **Power Platform connectors** (1,000+) plug into Power Automate flows.
- **GitHub Copilot** brings agents and MCP to coding ([Cursor & AI IDEs](../part-7-building-with-ai/64-cursor-and-ai-ides.md)).

## ⚫ Others worth knowing

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Many other AI tools, including Perplexity, Le Chat, Notion, Slack, Raycast and phone assistants, have their own connector options. The table summarizes each.

</details>

| App | Connector story |
|---|---|
| **Perplexity** | Search-first AI with connectors for Gmail, Calendar, Notion, GitHub and more, plus local MCP in its desktop app |
| **Mistral Le Chat** | 20+ MCP connectors and custom MCP connectors on every plan ([Le Chat guide](../part-2-ai-assistants-field-guide/26-mistral-le-chat.md)) |
| **Grok** | Web and X search built in; fewer third-party connections so far |
| **Meta AI** | Lives inside WhatsApp, Instagram and Facebook; limited outside connections |
| **Alexa+** | Connects to smart home devices and services like groceries, rides and reservations |
| **Notion AI** | Its own agents plus MCP connections to other tools ([Notion AI Deep Dive](../part-6-ai-in-your-apps/54-notion-ai-deep-dive.md)) |
| **Slack** | AI features and agents inside Slack, plus an official MCP server |
| **Raycast** (Mac/Windows) | System-wide AI with extensions and MCP |
| **Apple Intelligence** | The rebuilt Siri with personal context and app actions, ChatGPT integration, Shortcuts that call AI models ([Built-In Assistants](../part-2-ai-assistants-field-guide/28-built-in-assistants.md), [Phone & Desktop Automation](../part-5-automation/50-phone-and-desktop-automation.md)) |

## ✨ Ten connector combos that feel like magic

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Connecting two or three apps lets AI move information between them, such as reading email, checking your calendar and drafting replies in one request. The table lists ten combinations with ready-to-use prompts.

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

More in [The MCP Recipe Book](44-mcp-recipe-book.md).

## 🔐 Permissions & approvals

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Most apps let you set each connector tool to **always allow**, **ask first** or **never**.

1. Allow read-only tools (search, list, read) freely.
2. Set anything that sends, deletes, buys, shares or posts to **ask first**.
3. Review your settings periodically and remove connectors you no longer use.

</details>

- **Per-tool settings:** most apps let you set each tool to **always allow**, **ask first** or **never**.
- **Ask first** for anything that **sends, deletes, buys, shares or posts publicly**.
- **Least privilege:** when a connector asks for scopes, prefer read-only if that's all you need.
- **Revoke anytime:** disconnect in the AI app *and* remove access in the service's security settings (e.g. your
  Google account's third-party access page).
- **Turn off unused connectors:** fewer tools = more focused AI + smaller risk.

## 🏢 Connectors at work

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

On Team and Enterprise plans, administrators usually decide which connectors are available. If one you need is missing, ask your IT team; they're balancing usefulness with data protection.

</details>

- On **Team/Enterprise** plans, admins often choose which connectors are available and who can use them.
- Company data policies may restrict connecting personal accounts to work assistants (and vice versa).
- If a connector you need isn't available, ask IT, and explain the task and the data involved. That makes a "yes" more likely.
- Many enterprises route MCP through **gateways** that log and control access ([MCP Security & Trust](43-mcp-security-and-trust.md)).

## 🧭 Connector, MCP server, or automation?

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Use a **connector** when you want to ask your AI about an app on demand. Use an **automation** when something should happen automatically. Build or install an **MCP server** when no connector exists for what you need.

</details>

| You want… | Use |
|---|---|
| To *ask* your AI about your email, docs or tasks, when you feel like it | 🔌 **Connector** |
| A tool no connector covers (local files, your database, a niche app) | 🛠️ **MCP server** |
| Something to happen *automatically* on a schedule or trigger | ⚙️ **Automation** ([Part V](../part-5-automation/index.md)) |
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

**Next:** [42 · Building MCP Servers →](42-building-mcp-servers.md)
