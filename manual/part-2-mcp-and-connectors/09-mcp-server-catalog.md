# 09 · The Big MCP Server Catalog 📚🔌

> ⏱️ 16 min read (or 2 min skim) · 🎯 Everyone · 🧰 Needs: an MCP-capable app (Claude, ChatGPT, Cursor, VS Code…)

**There are thousands of MCP servers. This is a curated tour of more than 100 of the best-known, most useful and most
*fun* ones, grouped by what you'd use them for.** Every entry has a "try this" prompt so you can go straight from reading
to doing.

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

This is a giant toy catalog of "doors" you can add to your AI. Each door leads somewhere: GitHub, Notion, a web browser,
your smart home, a music app. Browse by category, pick a few that sound fun, and give your AI new powers today. The
✅ ones are made by the companies themselves, and the 🧪 ones are made by the community (check them before trusting them).

</details>

<!-- in-this-chapter -->

> [!NOTE]
> **📌 How to read this catalog**
> ✅ = official (made or maintained by the vendor) · 🧪 = community-built (check the repo's activity first) ·
> ☁️ = remote (paste a URL, log in) · 🏠 = local (runs on your machine).
> Endpoints and package names change, so when in doubt click through to the vendor's docs or search the
> [official registry](https://registry.modelcontextprotocol.io). New to installing servers? Start with
> [MCP Explained](07-mcp-explained.md#installing-servers-app-by-app).

## 🧱 The starter pack (official reference servers)

<details class="eli5">
<summary>🧸 ELI5</summary>

These are the "training wheels" servers made by the MCP team itself. They're free, need no accounts, and are perfect for
learning how everything works.

</details>

From the [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) repo:

| Server | Type | What it does | 🎮 Try this |
|---|---|---|---|
| **Filesystem** | ✅🏠 | Read, write and search files in folders you allow | "Organize my `Downloads/screenshots` folder into subfolders by month." |
| **Fetch** | ✅🏠 | Grabs a web page and converts it to clean Markdown | "Fetch these 3 articles and tell me where they disagree." |
| **Memory** | ✅🏠 | A persistent knowledge graph of facts about you and your projects | "Remember that my cat is Pixel and I'm allergic to cilantro." |
| **Git** | ✅🏠 | Read and search git history, diffs and branches | "What changed in this repo last week, in plain English?" |
| **Time** | ✅🏠 | Time and timezone conversions | "It's 3pm here. What time is it for my teammates in Tokyo and Berlin?" |
| **Sequential Thinking** | ✅🏠 | A scratchpad tool for step-by-step reasoning | "Plan a 3-city Japan trip, revising the plan as you go." |
| **Everything** | ✅🏠 | A demo server exercising every MCP feature | Great for testing clients or learning the protocol |

> [!NOTE]
> **🤯 Fun fact: some reference servers "graduated"**
> Early reference servers for Postgres, SQLite, Slack, Puppeteer and others were archived as official vendor servers and
> better community versions took over. It's a sign of a healthy ecosystem!

## 💻 Developer & DevOps

<details class="eli5">
<summary>🧸 ELI5</summary>

Doors for people who build software: your code repositories, bug trackers, web browsers for testing, cloud servers and
monitoring dashboards. Your AI becomes a teammate who can check on all of them.

</details>

| Server | Type | What it does | 🎮 Try this |
|---|---|---|---|
| [**GitHub**](https://github.com/github/github-mcp-server) | ✅☁️ | Repos, issues, PRs, Actions, code search | "Summarize open issues labeled `bug` and draft a triage plan." |
| [**GitLab**](https://registry.modelcontextprotocol.io/?q=gitlab) | ✅☁️ | Projects, merge requests, issues, pipelines | "Why did the last pipeline on `main` fail?" |
| [**Playwright**](https://github.com/microsoft/playwright-mcp) | ✅🏠 | Drives a real browser: click, type, screenshot | "Go to my website, fill out the contact form, and tell me if anything breaks." |
| [**Chrome DevTools**](https://github.com/ChromeDevTools/chrome-devtools-mcp) | ✅🏠 | Performance traces, console, network inspection | "Why is this page slow to load? Record a trace and explain." |
| [**Context7**](https://github.com/upstash/context7) | ✅🏠☁️ | Pulls *up-to-date* library docs into context | "Use context7 to show me the current way to do auth in Next.js." |
| [**DeepWiki**](https://registry.modelcontextprotocol.io/?q=deepwiki) | ✅☁️ | Ask questions about any public GitHub repo's architecture | "How does routing work in this open-source project?" |
| [**Sentry**](https://github.com/getsentry/sentry-mcp) | ✅☁️ | Errors, stack traces, issues | "What's the most common error this week, and where's the bug?" |
| [**Datadog**](https://github.com/datadog-labs/mcp-server) | ✅☁️ | Metrics, logs, monitors, incidents | "What changed right before yesterday's latency spike?" |
| [**Grafana**](https://github.com/grafana/mcp-grafana) | ✅🏠 | Dashboards, queries, incidents | "Pull up last night's error-rate panel and explain it." |
| [**PostHog**](https://github.com/PostHog/posthog/tree/master/services/mcp) | ✅☁️ | Product analytics, feature flags, experiments | "Which feature flag rollout correlates with the drop in signups?" |
| [**Vercel**](https://vercel.com/docs/mcp) | ✅☁️ | Deployments, logs, projects | "Why did my last deploy fail?" |
| [**Netlify**](https://registry.modelcontextprotocol.io/?q=netlify) | ✅☁️ | Sites, deploys, forms, environment config | "Deploy this folder as a new site and give me the URL." |
| [**Cloudflare**](https://github.com/cloudflare/mcp-server-cloudflare) | ✅☁️ | Workers, DNS, analytics, docs and more | "Show me traffic to my site over the last 7 days." |
| [**Docker MCP Toolkit**](https://docs.docker.com/ai/mcp-catalog-and-toolkit/) | ✅🏠 | A catalog of containerized MCP servers, one-click installs | Run untrusted servers safely inside containers |
| [**Terraform**](https://github.com/hashicorp/terraform-mcp-server) | ✅🏠 | Terraform registry, providers and modules | "Write Terraform for a static site on S3 using current provider docs." |
| [**AWS**](https://github.com/awslabs/mcp) | ✅🏠☁️ | A family of AWS servers: docs, CDK, cost, and more | "What's costing me the most on AWS this month?" |
| [**Azure**](https://github.com/microsoft/mcp) | ✅🏠 | Microsoft's collection of Azure and related servers | "List my Azure resources and flag anything idle." |
| [**Kubernetes**](https://registry.modelcontextprotocol.io/?q=kubernetes) | 🧪🏠 | Inspect pods, logs, deployments | "Which pods restarted most today, and why?" |
| [**Desktop Commander**](https://github.com/wonderwhy-er/DesktopCommanderMCP) | 🧪🏠 | Terminal commands and file editing from Claude Desktop | Turns Claude Desktop into a mini coding agent. ⚠️ Powerful, so scope carefully |

## 📋 Productivity, docs & project management

<details class="eli5">
<summary>🧸 ELI5</summary>

Doors to where your work lives: notes, tasks, docs, chats and files. Your AI can find things, tidy them up and create new
ones for you.

</details>

| Server | Type | What it does | 🎮 Try this |
|---|---|---|---|
| [**Notion**](https://developers.notion.com/docs/mcp) | ✅☁️ | Search, read, create and update pages and databases | "Turn this meeting transcript into a Notion page with action items in my Tasks DB." |
| [**Linear**](https://linear.app/docs/mcp) | ✅☁️ | Issues, projects, cycles | "Create issues for each bug in this list, with priorities." |
| [**Atlassian (Jira + Confluence)**](https://www.atlassian.com/platform/remote-mcp-server) | ✅☁️ | Tickets, pages, search | "Write a Confluence release-notes page from tickets closed this sprint." |
| [**Asana**](https://developers.asana.com/docs/using-asanas-mcp-server) | ✅☁️ | Tasks, projects, portfolios | "What's overdue across my projects? Draft nudges to the owners." |
| [**monday.com**](https://registry.modelcontextprotocol.io/?q=monday) | ✅☁️ | Boards, items, updates | "Build a board for my product launch with these 12 tasks." |
| [**ClickUp**](https://registry.modelcontextprotocol.io/?q=clickup) | ✅☁️ | Tasks, docs, spaces | "Summarize what my team finished this week." |
| [**Todoist**](https://github.com/Doist/todoist-ai) | ✅☁️ | Tasks and projects | "Break 'plan my sister's birthday party' into tasks with due dates." |
| [**Slack**](https://registry.modelcontextprotocol.io/?q=slack) | ✅☁️ | Search messages, read channels, send messages | "Catch me up on #product from this week in 5 bullets." |
| **Gmail · Google Calendar · Google Drive** | ✅☁️ | Mail, events, docs (built-in connectors in Claude and others) | "Find a 30-min slot next week and draft the invite email." |
| **Microsoft 365** | ✅☁️ | Outlook, Teams, SharePoint, OneDrive via Copilot and connectors | "Summarize the Teams thread I missed." |
| [**Box**](https://registry.modelcontextprotocol.io/?q=box) | ✅☁️ | Files, folders, metadata, AI search across content | "Find the latest signed version of the vendor contract." |
| [**Dropbox**](https://registry.modelcontextprotocol.io/?q=dropbox) | ✅☁️ | Files and folders | "Which files in 'Taxes 2025' are still missing receipts?" |
| [**Airtable**](https://registry.modelcontextprotocol.io/?q=airtable) | ✅☁️ | Bases, tables, records | "Add these 20 leads to my CRM base, deduplicated by email." |
| [**DocuSign**](https://registry.modelcontextprotocol.io/?q=docusign) | ✅☁️ | Envelopes, agreements, status | "Which contracts are still waiting on signatures?" |
| [**Obsidian**](https://github.com/MarkusPfundstein/mcp-obsidian) | 🧪🏠 | Your local vault via the Local REST API plugin | "Find notes about 'habits' and build a MOC page linking them." |
| [**Basic Memory**](https://github.com/basicmachines-co/basic-memory) | 🧪🏠 | AI memory stored as Markdown files you own | Build a second brain that both you and AI can edit |

## 💼 Business, sales, support & payments

<details class="eli5">
<summary>🧸 ELI5</summary>

Doors to the "business" side: customers, sales, support tickets and money. Your AI becomes a helpful office assistant who
can look things up and prepare actions for you to approve.

</details>

| Server | Type | What it does | 🎮 Try this |
|---|---|---|---|
| [**HubSpot**](https://developers.hubspot.com/mcp) | ✅☁️ | CRM contacts, deals, companies | "Which deals haven't been touched in 2 weeks?" |
| [**Salesforce**](https://registry.modelcontextprotocol.io/?q=salesforce) | ✅☁️ | Accounts, opportunities, records | "Prep me for my call with Acme: open opportunities and recent activity." |
| [**Intercom**](https://registry.modelcontextprotocol.io/?q=intercom) | ✅☁️ | Conversations, contacts, help center | "What are customers asking about most this week?" |
| [**Stripe**](https://docs.stripe.com/mcp) | ✅☁️ | Customers, payments, invoices, docs | "Create a payment link for my $25 workshop." |
| [**Square**](https://registry.modelcontextprotocol.io/?q=square) | ✅☁️ | Payments, catalog, orders | "What were my best-selling items last month?" |
| [**PayPal**](https://registry.modelcontextprotocol.io/?q=paypal) | ✅☁️ | Invoices, transactions, disputes | "Send an invoice to this client for last month's work." |
| [**Shopify**](https://shopify.dev/docs/apps/build/devmcp) | ✅🏠 | Dev docs and API help (plus storefront MCP for shops) | "Help me build a Shopify app that tags VIP customers." |
| [**Webflow**](https://registry.modelcontextprotocol.io/?q=webflow) | ✅☁️ | Sites, CMS collections, pages | "Add these 5 blog posts to my CMS as drafts." |

> [!WARNING]
> **⚠️ Money tools deserve Level 2 autonomy**
> Anything that moves money, sends invoices or refunds should **always ask before acting**. Use test/sandbox modes while
> experimenting. See [autonomy levels](../part-1-foundations/01-the-mental-model.md#autonomy-levels-from-autocomplete-to-autopilot).

## 🔎 Web search, research & scraping

<details class="eli5">
<summary>🧸 ELI5</summary>

Doors to the whole internet: search engines, web page readers and "scrapers" that collect information from websites. Your
AI can research anything with real sources instead of guessing.

</details>

| Server | Type | What it does | 🎮 Try this |
|---|---|---|---|
| [**Brave Search**](https://github.com/brave/brave-search-mcp-server) | ✅🏠 | Web, news and image search (free tier available) | "What launched in AI this week? Cite sources." |
| [**Exa**](https://github.com/exa-labs/exa-mcp-server) | ✅☁️ | Semantic search built for AI, great at finding similar pages | "Find 10 indie blogs that write about home automation." |
| [**Tavily**](https://github.com/tavily-ai/tavily-mcp) | ✅☁️ | Search + extraction tuned for agents | "Research the top 5 note-taking apps and build a comparison table." |
| [**Perplexity**](https://github.com/perplexityai/modelcontextprotocol) | ✅🏠 | Perplexity's answer engine as a tool | "Ask Perplexity for the latest on X, then critique its sources." |
| [**Firecrawl**](https://github.com/firecrawl/firecrawl-mcp-server) | ✅🏠☁️ | Crawl whole sites and extract structured data | "Crawl this docs site and make me a study guide." |
| [**Apify**](https://github.com/apify/actors-mcp-server) | ✅☁️ | Thousands of ready-made scrapers ("Actors") for Maps, social and more | "Find the top-rated coffee shops near me from Google Maps into a table." |
| [**Browserbase**](https://github.com/browserbase/mcp-server-browserbase) | ✅☁️ | Cloud browsers for agents | Browser automation without running Chrome yourself |
| [**Jina AI**](https://registry.modelcontextprotocol.io/?q=jina) | ✅☁️ | Read any URL as clean text, search, rerank | "Read these 10 URLs and extract every pricing plan." |
| [**Bright Data**](https://registry.modelcontextprotocol.io/?q=bright%20data) | ✅☁️ | Industrial-strength web data access | "Track competitor prices across these product pages." |
| **PubMed** | ✅☁️ | Biomedical literature search (a Claude connector) | "Find 5 recent studies on sleep and memory and explain them simply." |
| [**arXiv**](https://registry.modelcontextprotocol.io/?q=arxiv) | 🧪🏠 | Search and read preprints | "What are the newest papers on small language models?" |
| [**YouTube transcripts**](https://registry.modelcontextprotocol.io/?q=youtube%20transcript) | 🧪🏠 | Pulls a video's transcript | "Summarize this 2-hour podcast into the 10 best insights." |

More in [Web Scraping & Monitoring with AI](../part-3-automation/20-web-scraping-and-monitoring.md).

## 🗄️ Data & databases

<details class="eli5">
<summary>🧸 ELI5</summary>

Doors to the big filing cabinets where apps keep their data. Your AI can look inside, answer questions with real numbers,
and even help design new cabinets. Always start with read-only keys!

</details>

| Server | Type | What it does | 🎮 Try this |
|---|---|---|---|
| [**Supabase**](https://supabase.com/docs/guides/getting-started/mcp) | ✅☁️ | Tables, SQL, migrations, edge functions | "Design a schema for a habit tracker and create it." |
| [**Neon**](https://github.com/neondatabase/mcp-server-neon) | ✅☁️ | Serverless Postgres with branching | "Branch my DB, try this migration, and show me the diff." |
| [**Postgres MCP Pro**](https://github.com/crystaldba/postgres-mcp) | 🧪🏠 | Postgres querying plus index and health tuning | "Why is this query slow? Suggest indexes." |
| [**MongoDB**](https://github.com/mongodb-js/mongodb-mcp-server) | ✅🏠 | Query and manage MongoDB and Atlas | "What's the shape of the documents in `orders`?" |
| [**MCP Toolbox for Databases**](https://github.com/googleapis/genai-toolbox) | ✅🏠 | Google's multi-database server (BigQuery, AlloyDB, Cloud SQL, Postgres, MySQL…) | Define safe, pre-written queries as tools |
| [**Snowflake**](https://github.com/Snowflake-Labs/mcp) | ✅🏠☁️ | Cortex search, analyst and SQL | "Which region's revenue grew fastest last quarter?" |
| [**ClickHouse**](https://github.com/ClickHouse/mcp-clickhouse) | ✅🏠 | Fast analytics queries | "Top 10 pages by visitors this week, with a chart." |
| [**Redis**](https://github.com/redis/mcp-redis) | ✅🏠 | Keys, caches, streams, vector search | "What's filling up my Redis memory?" |
| [**Elasticsearch**](https://github.com/elastic/mcp-server-elasticsearch) | ✅🏠 | Search indices and logs | "Find all checkout errors from the last hour." |
| [**Qdrant**](https://github.com/qdrant/mcp-server-qdrant) | ✅🏠 | Vector search memory | "Remember this design doc and find it later by meaning." |
| [**Chroma**](https://github.com/chroma-core/chroma-mcp) | ✅🏠 | Embedded vector database | "Index my notes folder so you can search it by meaning." |
| [**MotherDuck / DuckDB**](https://github.com/motherduckdb/mcp-server-motherduck) | ✅🏠 | SQL on local files and the cloud | "Query these three CSVs together and chart the trend." |
| [**dbt**](https://github.com/dbt-labs/dbt-mcp) | ✅🏠 | Models, lineage, metrics | "Which dashboards break if I rename this column?" |

> [!TIP]
> **💡 Pro move: read-only first**
> Connect databases with a **read-only** user first. Let the AI explore and explain before you ever give it write access.
> More in [MCP Security & Trust](12-mcp-security-and-trust.md).

## 🎨 Creative, design & media

<details class="eli5">
<summary>🧸 ELI5</summary>

Doors to art studios: design tools, 3D programs, music software and voice generators. Your AI becomes a creative
assistant that can actually touch the canvas.

</details>

| Server | Type | What it does | 🎮 Try this |
|---|---|---|---|
| **Figma** (Dev Mode MCP) | ✅🏠☁️ | Gives coding agents your designs: layout, tokens, components | "Build this Figma frame as a React component matching our tokens." |
| **Canva** | ✅☁️ | Create, search and edit designs | "Make 3 Instagram post options announcing my bake sale." |
| [**Blender MCP**](https://github.com/ahujasid/blender-mcp) | 🧪🏠 | Claude controls Blender: modeling, materials, scenes | "Build a low-poly island with a lighthouse at sunset." 🤯 |
| [**Ableton MCP**](https://github.com/ahujasid/ableton-mcp) | 🧪🏠 | Create tracks, clips and MIDI in Ableton Live | "Make a lo-fi beat at 80 BPM with a jazzy chord progression." |
| [**ElevenLabs**](https://github.com/elevenlabs/elevenlabs-mcp) | ✅🏠 | Text-to-speech, voices, sound effects | "Narrate my blog post in a warm storyteller voice." |
| [**Hugging Face**](https://huggingface.co/mcp) | ✅☁️ | Search models, datasets, papers and Spaces, and call Spaces as tools | "Find a good open model for transcribing Spanish audio." |
| [**Replicate**](https://registry.modelcontextprotocol.io/?q=replicate) | ✅☁️ | Run thousands of open image, video and audio models | "Generate 4 logo concepts for 'Pixel's Plant Shop'." |
| [**fal**](https://registry.modelcontextprotocol.io/?q=fal) | ✅☁️ | Fast media generation models | "Turn this photo into a short looping animation." |
| [**Unity**](https://registry.modelcontextprotocol.io/?q=unity) | 🧪🏠 | Control the Unity editor | "Add a bouncing collectible coin to my scene." |

More creative fun in [Part VIII](../part-8-creative-ai/index.md).

## 🏠 Life, home, health & fun

<details class="eli5">
<summary>🧸 ELI5</summary>

Doors to everyday life: your smart home, music, maps, fitness and even medical reference databases. Some are official,
many are hobby projects made with love by the community.

</details>

| Server | Type | What it does | 🎮 Try this |
|---|---|---|---|
| [**Home Assistant**](https://www.home-assistant.io/integrations/mcp_server/) | ✅🏠 | Built-in MCP server: your smart home as tools | "Movie mode: dim the living room to 20% and turn off the kitchen lights." |
| [**Spotify**](https://registry.modelcontextprotocol.io/?q=spotify) | 🧪🏠 | Search, play and build playlists | "Make a 90-minute focus playlist with no lyrics." |
| [**Google Maps**](https://registry.modelcontextprotocol.io/?q=google%20maps) | 🧪🏠 | Places, directions, distances | "Plan a walking route between these 5 cafés." |
| [**Weather**](https://registry.modelcontextprotocol.io/?q=weather) | 🧪🏠 | Forecasts (many use free Open-Meteo) | "Should I bike to work tomorrow?" |
| [**Strava**](https://registry.modelcontextprotocol.io/?q=strava) | 🧪🏠 | Your workouts | "How has my running pace trended this year?" |
| [**Apple apps**](https://registry.modelcontextprotocol.io/?q=apple) | 🧪🏠 | Notes, Reminders, Calendar, Messages on a Mac | "Add everything from this email to my Reminders." |
| **Healthcare reference connectors** (ICD-10, NPI Registry, CMS Coverage) | ✅☁️ | Medical codes, provider lookup, Medicare coverage policy (Claude connectors) | "What does ICD-10 code E11.65 mean, in plain English?" |
| **Intuit Credit Karma** | ✅☁️ | Your credit factors and spending overview (Claude connector) | "What's affecting my credit score most, and what can I do?" |
| **Your own server!** | 🏠 | Anything you can script | See the [Pocket Toolkit](../../examples/my-first-mcp-server/) 🎲 |

> [!NOTE]
> **📌 Health and money tools inform, they don't decide**
> They're great for understanding and preparing questions, but big medical or financial decisions belong with qualified
> humans. See [Health, Fitness & Wellbeing](../part-9-ai-for-life-and-work/66-health-fitness-and-wellbeing.md) and
> [Money & Personal Finance](../part-9-ai-for-life-and-work/65-money-and-personal-finance.md).

## 🔀 Meta-servers: one connection, thousands of apps

<details class="eli5">
<summary>🧸 ELI5</summary>

These are master keys: one door that leads to a hallway with thousands more doors. Connect one of these and your AI can
reach most apps in the world.

</details>

| Server | What it is |
|---|---|
| [**Zapier MCP**](https://zapier.com/mcp) | Exposes actions from Zapier's 8,000+ app catalog as tools. You pick exactly which actions the AI may use |
| [**Pipedream MCP**](https://mcp.pipedream.com) | Thousands of APIs with managed auth, great for developers building their own agents |
| [**Composio**](https://composio.dev) | Hundreds of toolkits with auth handled, popular with agent builders |
| **n8n** (MCP Server Trigger + instance MCP) | Turn *any n8n workflow* into an MCP tool, or let AI build workflows ([n8n AI Agents](../part-3-automation/17-n8n-ai-agents.md)) |
| **Make** (MCP server) | Expose Make scenarios as tools |
| **Activepieces** | Open-source automation "pieces," many also available as MCP servers |

## 🗺️ Where to find more servers

<details class="eli5">
<summary>🧸 ELI5</summary>

Like app stores, there are websites that list thousands of MCP servers with search, ratings and install buttons.

</details>

| Directory | Why it's good |
|---|---|
| [**Official MCP Registry**](https://registry.modelcontextprotocol.io) | The canonical, community-owned registry that other directories pull from |
| **Claude's Directory** (Settings → Connectors) | Reviewed connectors, skills and plugins, installable in one click |
| [**GitHub MCP Registry**](https://github.com/mcp) | Browse and one-click install into VS Code and others |
| [**Docker MCP Catalog**](https://hub.docker.com/mcp) | Containerized, signed servers |
| [**awesome-mcp-servers**](https://github.com/punkpeye/awesome-mcp-servers) | A massive community-curated list |
| [**Glama**](https://glama.ai/mcp/servers), [**Smithery**](https://smithery.ai), [**PulseMCP**](https://www.pulsemcp.com), [**mcp.so**](https://mcp.so) | Searchable directories with usage stats and hosted options |

## 🔍 Judging a random server in 30 seconds

<details class="eli5">
<summary>🧸 ELI5</summary>

Before letting a stranger's helper into your house, check who made it, whether anyone's still looking after it, and
whether it's asking for more keys than it needs.

</details>

1. **Who made it?** Vendor-official beats a random account.
2. **Is it alive?** Recent commits, answered issues, a reasonable number of users.
3. **What does it ask for?** A "weather" server that wants your whole Google account is a 🚩.
4. **Can you sandbox it?** Docker, a read-only token, or the vendor's remote version.
5. **Pin the version** for anything important, so a malicious update can't sneak in.

Full checklist in [MCP Security & Trust](12-mcp-security-and-trust.md).

## 🎯 Key takeaways

- There's an MCP server for almost everything: code, docs, business apps, data, creative tools, home and life.
- Prefer **✅ official** servers, and treat **🧪 community** ones with a quick trust check.
- **Meta-servers** (Zapier, Pipedream, Composio, n8n) unlock thousands of apps at once.
- Use the **official registry** and trusted directories to discover more.
- Start **read-only**, keep **approvals on** for money and messages, and enable only what you need.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. You want AI to test your website's signup form. Which server?</summary>

**Playwright** (or Chrome DevTools): they drive a real browser.

</details>

<details class="quiz">
<summary>❓ 2. Your code agent keeps using outdated library APIs. Which server helps?</summary>

**Context7**: it pulls current, version-specific documentation into context.

</details>

<details class="quiz">
<summary>❓ 3. One server to reach thousands of SaaS apps with managed logins?</summary>

A **meta-server** like **Zapier MCP**, **Pipedream** or **Composio**.

</details>

> [!TIP]
> **🎮 Try this**
> Pick **one server from three different categories** above (say GitHub + Brave Search + Notion) and give your AI a task
> that needs all three: *"Find the 5 most-starred new MCP servers on GitHub this month, research what each does, and create
> a Notion page ranking them for a beginner."* That's a genuinely useful multi-tool agent run, and you set it up with config
> files. 🎉 More combos in [The MCP Recipe Book](13-mcp-recipe-book.md).

---

**Next:** [10 · Built-in Connectors & Plugins →](10-built-in-connectors.md)
