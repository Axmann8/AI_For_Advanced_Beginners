# 05 · The Big MCP Server Catalog 📚

There are **thousands** of MCP servers. This is a curated tour of the best-known, most useful, and
most *fun* ones, grouped by what you'd use them for. Each entry has a "try this" prompt so you can go
straight from reading to doing.

> 🏷️ **Legend:** ☁️ = official remote server (paste a URL, log in) · 🏠 = runs locally ·
> ✅ = made or maintained by the vendor itself · 🧪 = community-built (check the repo's activity before trusting it)
>
> Endpoints and package names change. When in doubt, click through to the vendor's docs.

---

## 🧱 The Starter Pack (the official reference servers)
From the [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) repo. These are
free, need no accounts, and are perfect for learning.

| Server | What it does | 🎮 Try this |
|---|---|---|
| **Filesystem** 🏠 | Read, write, and search files in folders you allow | "Organize my `Downloads/screenshots` folder into subfolders by month." |
| **Fetch** 🏠 | Grabs a web page and converts it to clean markdown | "Fetch these 3 articles and tell me where they disagree." |
| **Memory** 🏠 | A persistent knowledge graph of facts about you and your projects | "Remember that my cat is named Pixel and I'm allergic to cilantro." |
| **Git** 🏠 | Read and search git history, diffs, and branches | "What changed in this repo last week, in plain English?" |
| **Time** 🏠 | Time and timezone conversions | "It's 3pm my time. What time is it for my teammates in Tokyo and Berlin?" |
| **Sequential Thinking** 🏠 | A "scratchpad" tool for step-by-step reasoning | "Plan a 3-city Japan trip, revising the plan as you go." |
| **Everything** 🏠 | A demo server exercising every MCP feature | Great for testing clients or learning the protocol. |

---

## 💻 Developer & Coding

| Server | What it does | 🎮 Try this |
|---|---|---|
| [**GitHub**](https://github.com/github/github-mcp-server) ☁️✅ | Repos, issues, PRs, Actions, code search | "Summarize open issues labeled `bug` and draft a triage plan." |
| [**Playwright**](https://github.com/microsoft/playwright-mcp) 🏠✅ | Drives a real browser: click, type, screenshot | "Go to my website, fill out the contact form, and tell me if anything breaks." |
| [**Chrome DevTools**](https://github.com/ChromeDevTools/chrome-devtools-mcp) 🏠✅ | Lets the AI inspect performance, console, and network in Chrome | "Why is this page slow to load? Record a trace and explain." |
| [**Context7**](https://github.com/upstash/context7) 🏠☁️✅ | Pulls *up-to-date* library docs into context | "Use context7 to show me the current way to do auth in Next.js." |
| [**Sentry**](https://github.com/getsentry/sentry-mcp) ☁️✅ | Errors, stack traces, issues | "What's the most common error this week, and where's the bug?" |
| [**Vercel**](https://vercel.com/docs/mcp) ☁️✅ | Deployments, logs, projects | "Why did my last deploy fail?" |
| [**Cloudflare**](https://github.com/cloudflare/mcp-server-cloudflare) ☁️✅ | Workers, DNS, analytics, docs, and more | "Show me traffic to my site over the last 7 days." |
| [**Docker MCP Toolkit**](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) 🏠✅ | A catalog of containerized MCP servers with one-click install | Run sketchy servers safely inside containers. |
| [**Terraform**](https://github.com/hashicorp/terraform-mcp-server) 🏠✅ | Terraform registry, providers, and modules | "Write Terraform for a static site on S3 using current provider docs." |
| [**AWS**](https://github.com/awslabs/mcp) 🏠✅ | A whole family of AWS servers (docs, CDK, cost, and more) | "What's costing me the most on AWS this month?" |
| [**Azure**](https://github.com/microsoft/mcp) 🏠✅ | Microsoft's collection of Azure and related servers | "List my Azure resources and flag anything idle." |
| [**Grafana**](https://github.com/grafana/mcp-grafana) 🏠✅ | Dashboards, queries, incidents | "Pull up yesterday's latency spike and explain it." |
| [**Desktop Commander**](https://github.com/wonderwhy-er/DesktopCommanderMCP) 🏠🧪 | Terminal commands and file editing from Claude Desktop | Turns Claude Desktop into a mini coding agent. ⚠️ Powerful, so scope carefully. |

---

## 📋 Productivity, Notes & Project Management

| Server | What it does | 🎮 Try this |
|---|---|---|
| [**Notion**](https://developers.notion.com/docs/mcp) ☁️✅ | Search, read, create, and update pages and databases | "Turn this meeting transcript into a Notion page with action items in my Tasks DB." |
| [**Linear**](https://linear.app/docs/mcp) ☁️✅ | Issues, projects, cycles | "Create issues for each bug in this list, with priorities." |
| [**Atlassian (Jira + Confluence)**](https://www.atlassian.com/platform/remote-mcp-server) ☁️✅ | Tickets, pages, search | "Write a Confluence release-notes page from the tickets closed this sprint." |
| [**Asana**](https://developers.asana.com/docs/using-asanas-mcp-server) ☁️✅ | Tasks, projects, portfolios | "What's overdue across my projects? Draft nudges to the owners." |
| **Slack** ☁️✅ | Search messages, read channels, send messages | "Catch me up on #product from this week in 5 bullets." |
| **Gmail / Google Calendar / Drive** ☁️ | Mail, events, docs (built-in connectors in Claude and others) | "Find a 30-min slot next week that works around my calendar and draft the invite email." |
| [**Todoist**](https://github.com/Doist/todoist-ai) ☁️✅ | Tasks and projects | "Break 'plan my sister's birthday party' into Todoist tasks with due dates." |
| [**HubSpot**](https://developers.hubspot.com/mcp) ☁️✅ | CRM contacts, deals, companies | "Which deals haven't been touched in 2 weeks?" |
| **Microsoft 365** ☁️ | Outlook, Teams, SharePoint, OneDrive (via Copilot and connectors) | "Summarize the Teams thread I missed." |
| [**Obsidian**](https://github.com/MarkusPfundstein/mcp-obsidian) 🏠🧪 | Your local vault, via the Local REST API plugin | "Find notes I wrote about 'habits' and build a MOC page linking them." |
| [**Basic Memory**](https://github.com/basicmachines-co/basic-memory) 🏠🧪 | AI memory stored as plain Markdown files you own | Build a second brain that both you and the AI can edit. |

---

## 🔎 Web Search, Research & Scraping

| Server | What it does | 🎮 Try this |
|---|---|---|
| [**Brave Search**](https://github.com/brave/brave-search-mcp-server) 🏠✅ | Web, news, and image search (free tier available) | "What launched in AI this week? Cite sources." |
| [**Exa**](https://github.com/exa-labs/exa-mcp-server) ☁️✅ | "Semantic" search built for AI, good at finding similar pages and papers | "Find 10 indie blogs that write about home automation." |
| [**Tavily**](https://github.com/tavily-ai/tavily-mcp) ☁️✅ | Search plus extraction tuned for agents | "Research the top 5 note-taking apps and build a comparison table." |
| [**Perplexity**](https://github.com/perplexityai/modelcontextprotocol) 🏠✅ | Perplexity's answer engine as a tool | "Ask Perplexity for the latest on X, then critique its sources." |
| [**Firecrawl**](https://github.com/firecrawl/firecrawl-mcp-server) 🏠☁️✅ | Crawl whole sites and extract structured data | "Crawl this docs site and make me a study guide." |
| [**Apify**](https://github.com/apify/actors-mcp-server) ☁️✅ | Thousands of ready-made scrapers ("Actors") for Maps, Instagram, and more | "Find the top-rated coffee shops near me from Google Maps into a table." |
| [**Browserbase**](https://github.com/browserbase/mcp-server-browserbase) ☁️✅ | Cloud browsers for agents | Browser automation without running Chrome yourself. |
| **arXiv / PubMed / Semantic Scholar** 🧪 & ✅ | Academic paper search | "Find 5 recent papers on sleep and memory and explain them simply." |
| **YouTube transcripts** 🧪 | Pulls a video's transcript | "Summarize this 2-hour podcast into the 10 best insights." |

---

## 🗄️ Data & Databases

| Server | What it does | 🎮 Try this |
|---|---|---|
| [**Supabase**](https://supabase.com/docs/guides/getting-started/mcp) ☁️✅ | Tables, SQL, migrations, edge functions | "Design a schema for a habit tracker and create it." |
| [**Neon**](https://github.com/neondatabase/mcp-server-neon) ☁️✅ | Serverless Postgres with branching | "Branch my DB, try this migration, and show me the diff." |
| [**Postgres MCP Pro**](https://github.com/crystaldba/postgres-mcp) 🏠🧪 | Postgres querying plus index and health tuning | "Why is this query slow? Suggest indexes." |
| [**MongoDB**](https://github.com/mongodb-js/mongodb-mcp-server) 🏠✅ | Query and manage MongoDB and Atlas | "What's the shape of the documents in `orders`?" |
| [**MCP Toolbox for Databases**](https://github.com/googleapis/genai-toolbox) 🏠✅ | Google's multi-database server (BigQuery, AlloyDB, Cloud SQL, Postgres, MySQL…) | Define safe, pre-written queries as tools. |
| [**Snowflake**](https://github.com/Snowflake-Labs/mcp) 🏠✅ | Cortex search/analyst and SQL | "Which region's revenue grew fastest last quarter?" |
| **Airtable / Google Sheets / Excel** 🧪 & ✅ | Spreadsheet-style data | "Clean up the duplicates in my contacts sheet." |

> 💡 **Pro move:** Connect databases with a **read-only** user first. Let the AI explore and explain
> before you ever give it write access.

---

## 🎨 Creative & Design

| Server | What it does | 🎮 Try this |
|---|---|---|
| **Figma** (Dev Mode MCP) 🏠☁️✅ | Gives coding agents your designs: layout, tokens, components | "Build this Figma frame as a React component matching our tokens." |
| **Canva** ☁️✅ | Create, search, and edit designs | "Make 3 Instagram post options announcing my bake sale." |
| [**Blender MCP**](https://github.com/ahujasid/blender-mcp) 🏠🧪 | Claude controls Blender: modeling, materials, scenes | "Build a low-poly island with a lighthouse at sunset." 🤯 |
| [**Ableton MCP**](https://github.com/ahujasid/ableton-mcp) 🏠🧪 | Claude creates tracks, clips, and MIDI in Ableton Live | "Make a lo-fi beat at 80 BPM with a jazzy chord progression." |
| [**ElevenLabs**](https://github.com/elevenlabs/elevenlabs-mcp) 🏠✅ | Text-to-speech, voices, sound effects | "Narrate my blog post in a warm British voice." |
| **Image generation** (various) 🧪 & ✅ | Replicate, fal, Stability, and others via MCP | "Generate 4 logo concepts for 'Pixel's Plant Shop.'" |
| [**Hugging Face**](https://huggingface.co/mcp) ☁️✅ | Search models, datasets, papers, and Spaces, and even call Spaces as tools | "Find a good open-source model for transcribing Spanish audio." |

---

## 💸 Commerce, Payments & Business

| Server | What it does | 🎮 Try this |
|---|---|---|
| [**Stripe**](https://docs.stripe.com/mcp) ☁️✅ | Customers, payments, invoices, docs | "Create a payment link for my $25 workshop." |
| [**Shopify**](https://shopify.dev/docs/apps/build/devmcp) 🏠✅ | Dev docs and API help (plus storefront MCP for shops) | "Help me build a Shopify app that tags VIP customers." |
| **PayPal / Square** ☁️✅ | Payments, invoices, catalogs | "Send an invoice to this client for last month's work." |
| **QuickBooks / Xero** ☁️ | Accounting data | "Which clients are late on payments?" |

---

## 🏠 Life, Home & Just-for-Fun

| Server | What it does | 🎮 Try this |
|---|---|---|
| [**Home Assistant**](https://www.home-assistant.io/integrations/mcp_server/) 🏠✅ | Built-in MCP server: your smart home as tools | "Movie mode: dim the living room to 20% and turn off the kitchen lights." |
| **Spotify** 🧪 | Search, play, and build playlists | "Make a 90-minute focus playlist with no lyrics." |
| **Weather / maps** 🧪 & ✅ | Forecasts, directions, places | "Should I bike to work tomorrow?" |
| **Strava / fitness** 🧪 | Your workouts | "How has my running pace trended this year?" |
| **Your own server!** 🏠 | Anything you can script | See [the Pocket Toolkit example](../../examples/my-first-mcp-server). 🎲 |

---

## 🔀 Meta-Servers: One Connection, Thousands of Apps

These are cheat codes. Each one gives your AI access to **huge** app catalogs through a single server.

| Server | What it is |
|---|---|
| [**Zapier MCP**](https://zapier.com/mcp) ☁️ | Exposes actions from Zapier's 8,000+ app catalog as tools. Pick which actions the AI may use. |
| [**Pipedream MCP**](https://mcp.pipedream.com) ☁️ | Thousands of APIs with managed auth. Great for developers building their own agents. |
| [**Composio**](https://composio.dev) ☁️ | Hundreds of toolkits with auth handled, popular with agent builders. |
| **n8n (MCP Server Trigger)** ☁️🏠 | Turn *any n8n workflow* into an MCP tool. Your custom automations become AI superpowers. See [Ch. 9](../part-3-automation/14-automation-platforms.md). |
| **Make (MCP server)** ☁️ | Expose Make scenarios as tools. |

---

## 🗺️ Where to Find More Servers

| Directory | Why it's good |
|---|---|
| [**Official MCP Registry**](https://registry.modelcontextprotocol.io) | The canonical, community-owned registry (still labeled preview). Other directories pull from it. |
| **Claude's Directory** (Settings → Connectors) | Reviewed connectors, skills, and plugins you can install in one click. |
| [**GitHub MCP Registry**](https://github.com/mcp) | Browse and one-click install into VS Code and others. |
| [**Docker MCP Catalog**](https://hub.docker.com/mcp) | Containerized, signed servers. |
| [**awesome-mcp-servers**](https://github.com/punkpeye/awesome-mcp-servers) | A massive community-curated list. |
| [**Glama**](https://glama.ai/mcp/servers), [**Smithery**](https://smithery.ai), [**PulseMCP**](https://www.pulsemcp.com), [**mcp.so**](https://mcp.so) | Searchable directories with ratings, usage stats, and hosted options. |

### How to judge a random server in 30 seconds
1. **Who made it?** Vendor-official beats a random account.
2. **Is it alive?** Recent commits, open issues answered, reasonable star count.
3. **What does it ask for?** A "weather" server that wants your full Google account scope is a 🚩.
4. **Can you run it sandboxed?** Docker, or a remote official version.

---

### 🚀 Try this next
Pick **one server from three different categories** above (say GitHub + Brave Search + Notion) and
give your AI a task that needs all three:
> *"Find the 5 most-starred new MCP servers on GitHub this month, research what each does, and
> create a Notion page ranking them for a beginner."*

That's a genuinely useful multi-tool agent run, and you set it up with config files. 🎉

**Next:** [06 · Built-in Connectors & Plugins →](10-built-in-connectors.md)
