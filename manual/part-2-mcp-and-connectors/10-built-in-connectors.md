# 06 · Built-in Connectors & Plugins 🧩

MCP is the engine, and **connectors** are the polished, click-to-install version inside the big AI apps.
If you want results *today* with zero config files, start here.

---

## Connectors vs. raw MCP vs. plugins

| | Built-in connector | Raw MCP server | Plugin / bundle |
|---|---|---|---|
| Setup | Click, then log in | Config file or URL | One install |
| Under the hood | Usually MCP! | MCP | Connectors/MCP + skills + commands |
| Best for | Everyday apps (Gmail, Drive, Notion, Slack) | Niche tools, local files, your own code | A whole workflow in one package |
| Control | Vendor-reviewed | You choose everything | Curated by the author |

**Rule of thumb:** Use the connector if one exists. Drop to raw MCP when it doesn't, or when you want
something local or custom.

## Where each AI app stands (as of Sept 2026)

### 🟠 Claude
- **Connectors directory** (Settings → Connectors): Google Workspace, Notion, Slack, GitHub,
  Linear, Asana, Atlassian, Canva, Figma, Stripe, and many more. You can also add **custom connectors** by URL.
- **Skills**: packaged instructions and scripts Claude loads on demand, like "make a slide deck in our
  brand" or "fill out this PDF". You can write your own ([example](../../examples/prompts-for-agents)).
- **Plugins**: bundles of connectors, skills, and commands, for example a role-specific pack for sales or finance.
- **Projects**: persistent knowledge and instructions per project. **Memory** across chats.
- **Artifacts**: Claude builds live mini-apps, dashboards, and docs you can share.
- **Research mode**: multi-step web + connector research with citations.

### 🟢 ChatGPT
- **Apps / plugins** (renamed from "apps" to **plugins** in mid-2026): third-party integrations
  that can show interactive UI inside the chat, built on MCP (the Apps SDK).
- **Connectors** for Drive, Gmail, SharePoint, GitHub, and more, used by chat and deep research.
- **Developer Mode**: connect *any* remote MCP server with full read and write tools (plan-dependent).
- **Agent mode**: a browser-driving agent for multi-step web tasks. **Custom GPTs** and **Projects** too.

### 🔵 Google Gemini
- Deep integration with **Gmail, Docs, Drive, Calendar, Maps, and YouTube**.
- **Gems** (custom assistants), **Deep Research**, and **NotebookLM** (see [Ch. 23](../part-6-knowledge-and-memory/41-rag-memory-and-knowledge.md)).
- **Gemini CLI** is open source and speaks MCP.

### 🟣 Microsoft Copilot
- **Microsoft 365 Copilot** works across Outlook, Teams, Word, Excel, and SharePoint.
- **Copilot Studio** lets you build agents with connectors and MCP tools, plus the Power Platform's
  1,000+ connectors.

### ⚫ Others worth knowing
- **Perplexity**: search-first AI with connectors for your files and apps.
- **Notion AI**: its own agents plus MCP connections to other tools (see [Ch. 13](../part-4-ai-in-your-apps/22-ai-in-your-apps.md)).
- **Raycast AI** (Mac/Windows): system-wide AI with extensions and MCP.

---

## Five connector combos that feel like magic ✨

1. **Gmail + Calendar** → *"Find every email where someone asked to meet and I haven't replied.
   Propose times that fit my calendar and draft the replies."*
2. **Drive + Notion** → *"Read my last 5 meeting notes docs and build a Notion project tracker from the
   action items."*
3. **Slack + Linear** → *"Scan #bugs this week and file Linear issues for anything not already tracked."*
4. **GitHub + Slack** → *"Write a friendly weekly changelog from merged PRs and post it to #updates."*
5. **Canva + Drive** → *"Take the stats from my Q3 doc and make an infographic in Canva."*

## Permissions tips
- Most apps let you set each tool to **always allow**, **ask first**, or **never**. Keep "ask first" for
  anything that sends, deletes, buys, or posts publicly.
- Turn off connectors you're not using. It keeps the AI focused and reduces risk.
- Workspace or enterprise plans may need an admin to enable connectors, so ask them nicely. 😄

---

### 🚀 Try this next
Connect **two** apps you use daily and give the AI a task that needs **both**. The cross-app
tasks are where the time savings really show up.

**Next:** [07 · Building MCP Servers →](11-building-mcp-servers.md)
