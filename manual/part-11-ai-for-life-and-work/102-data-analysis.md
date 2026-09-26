# 102 · Data Analysis for Everyone: From CSV to Dashboard 📊🐍

> ⏱️ 7 min read · 🎯 Everyone with a spreadsheet (no stats or Python needed) · 🧰 Needs: an assistant with code execution, optionally Claude Code, Jupyter/Colab or a database

**You don't need to know statistics or Python to get real answers from data anymore.** AI can load your spreadsheet, clean it,
analyze it, chart it and explain what it means, in plain English. This chapter climbs five levels, from "chat with a CSV" to
AI inside spreadsheets, notebooks, talking to databases with MCP, and building live dashboards, plus the thinking skills that
keep you from fooling yourself with numbers. Let's find the story in your data. 📈✨

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Data is just a big table of numbers and words, like a list of everything you bought last year. AI can read the whole table in
seconds and answer questions like "what did I spend the most on?" or "which month was the busiest?", then draw a chart to show
you. It's like having a detective for numbers. 🕵️📊

</details>

<!-- in-this-chapter -->

## 🪜 The five levels

<details class="eli5">
<summary>🧸 ELI5</summary>

There are five levels: chatting about a spreadsheet, AI inside your spreadsheet, fancy notebooks, asking questions of big
databases, and building live dashboards.

</details>

| Level | What you do | Effort |
|---|---|---|
| 1️⃣ **Chat with a spreadsheet** | Upload a file, ask questions | 🟢 Minutes |
| 2️⃣ **AI inside your spreadsheet** | Formulas, AI columns, pivots | 🟢 Minutes |
| 3️⃣ **Analysis notebooks** | Repeatable analysis with Python | 🟡 An hour |
| 4️⃣ **Talk to databases with MCP** | Ask questions in English, AI writes SQL | 🟡 Setup once |
| 5️⃣ **Dashboards & data apps** | Live, shareable dashboards | 🟡 An afternoon |

## 1️⃣ Chat with a spreadsheet

<details class="eli5">
<summary>🧸 ELI5</summary>

Upload your spreadsheet to an AI assistant and ask it questions. Behind the scenes, it writes a little program to find the
answers.

</details>

Upload a CSV or Excel file to an assistant with **code execution** (Claude, ChatGPT and Gemini all do this). Behind the scenes,
it writes and runs Python for you.

| Goal | Starter prompt |
|---|---|
| **Get oriented** | *"Describe this dataset: columns, row count, data-quality issues, and 5 interesting questions we could answer."* |
| **Clean** | *"Clean it: fix dates, remove duplicates, standardize categories. Show me what you changed and the row counts before and after."* |
| **Insights** | *"What are the top 3 insights? Include a chart for each."* |
| **Compare** | *"Is the difference between group A and B meaningful, or could it be noise? Explain simply."* |
| **Export** | *"Give me the cleaned file as a download."* |

> [!TIP]
> **💡 Always ask two questions**
> *"Show me the code you ran"* and *"What assumptions did you make?"* That's how you catch mistakes, and how you learn.

## 2️⃣ AI inside your spreadsheet

<details class="eli5">
<summary>🧸 ELI5</summary>

Spreadsheet apps now have AI built in: it writes tricky formulas, and special AI columns can read every row and add a label,
like "happy" or "sad" for reviews.

</details>

| Tool | What you can do |
|---|---|
| **Google Sheets + Gemini** | Generate formulas and tables, and `=AI()` per-cell prompts for classifying and summarizing rows |
| **Excel + Copilot** | Formulas, pivots, charts, insights, **Python in Excel** |
| **Airtable AI** | AI fields that enrich every row automatically |

**The classic magic trick:** 500 customer comments in column A → add AI columns for **sentiment**, **theme** and **urgency** →
pivot by theme. Qualitative data becomes quantitative in minutes. 🪄 Full details in [Spreadsheet Superpowers](../part-6-ai-in-your-apps/58-spreadsheet-superpowers.md).

## 3️⃣ Analysis notebooks with AI

<details class="eli5">
<summary>🧸 ELI5</summary>

A notebook is a document mixing notes, code and charts. AI can write the whole thing, and you can re-run it any time new data
arrives.

</details>

For repeatable, bigger analysis:

1. Open **Claude Code** or **Cursor** in a folder with your data, or use **Jupyter / Google Colab** with AI assistance.
2. *"Create a Jupyter notebook that loads sales.csv, cleans it, and analyzes monthly trends by region with charts. Explain each
   step in markdown cells."*
3. Run, read and iterate: *"Add a forecast for the next 3 months with a simple model and confidence intervals."*

| Library | Job |
|---|---|
| **pandas** / **polars** | Tables: filter, group, join |
| **DuckDB** | SQL directly on CSV and Parquet files (fast, and AI loves it) |
| **matplotlib** / **seaborn** / **plotly** | Charts (plotly for interactive ones) |
| **scikit-learn** | Simple machine learning (clustering, prediction) |
| **statsmodels** | Statistics and forecasting |

**DuckDB is a cheat code:**

```python
import duckdb
duckdb.sql("""
    SELECT region, date_trunc('month', order_date) AS month, sum(total) AS revenue
    FROM 'sales.csv'
    GROUP BY ALL
    ORDER BY month
""").show()
```

Ask your agent to write queries like this for you, then read them to learn SQL along the way. 🦆

## 4️⃣ Talk to databases with MCP

<details class="eli5">
<summary>🧸 ELI5</summary>

Big companies keep data in databases. With a special plug-in, you can ask the database questions in normal English, and AI
writes the database code for you.

</details>

Connect a database MCP server ([MCP Server Catalog](../part-4-mcp-and-connectors/40-mcp-server-catalog.md)) with a **read-only**
user:

> *"Explore the schema. Which marketing channel brought customers with the highest lifetime value? Show the SQL."*

The AI writes SQL, runs it, checks the results and explains. This is a game-changer for anyone who's ever waited on a data team.

> [!WARNING]
> **⚠️ Read-only, always**
> Give AI **read-only** database credentials for analysis. An agent with write access can accidentally change or delete data
> ([MCP Security & Trust](../part-4-mcp-and-connectors/43-mcp-security-and-trust.md)).

## 5️⃣ Dashboards & data apps

<details class="eli5">
<summary>🧸 ELI5</summary>

A dashboard is a page with charts that update by themselves. AI can build one for you in minutes, so you and your team can see
the numbers any time.

</details>

| Option | Effort | Notes |
|---|---|---|
| **Claude Artifacts** | Minutes | Interactive charts and dashboards right in chat, shareable |
| **Looker Studio / Power BI + AI** | Low | Classic BI with AI assistance |
| **Streamlit** (Python) | Medium | *"Build a Streamlit dashboard for this CSV with filters by region and date."* |
| **Evidence, Observable** | Medium | Code-based, beautiful data reports |
| **Vibe-coded web app** | Medium | A custom dashboard with Supabase data ([Vibe Coding](../part-7-building-with-ai/65-vibe-coding-your-first-app.md)) |

**Automate the refresh:** a scheduled job (GitHub Actions, n8n) pulls fresh data nightly and rebuilds the dashboard
([n8n Masterclass](../part-5-automation/47-n8n-masterclass.md)).

## 🧠 Thinking clearly about data

<details class="eli5">
<summary>🧸 ELI5</summary>

Numbers can trick you. Two things happening together doesn't mean one caused the other, and a few examples don't prove a rule.
AI can help you check.

</details>

| Trap | Ask AI |
|---|---|
| **Correlation ≠ causation** | *"List 5 alternative explanations for this pattern."* |
| **Tiny samples** | *"Is the sample big enough to conclude this? What's the uncertainty?"* |
| **Cherry-picking** | *"What would the chart look like over a longer period?"* |
| **Averages hide things** | *"Show the distribution, not just the average. Any outliers?"* |
| **Misleading charts** | *"Is this chart honest? Check the axes and scale."* |
| **Missing data** | *"How much data is missing, and could it bias the result?"* |

**Verify one number by hand** (or in a pivot table) to make sure the AI's pipeline is right. If it matches, trust grows. If not,
you found a bug. 🐛

## 🎮 Fun datasets to practice with

<details class="eli5">
<summary>🧸 ELI5</summary>

Practice with data about your own life, like your music, your steps or your spending. It's way more fun when it's about you!

</details>

| Dataset | Questions to ask |
|---|---|
| Your **bank/credit card export** | Where does my money go? Trends? Forgotten subscriptions? ([Money](96-money-and-personal-finance.md)) |
| Your **Spotify / YouTube / Netflix data export** | My taste over time, top artists by season, binge patterns 🎧 |
| Your **fitness app export** (Strava, Apple Health, Garmin) | Am I improving? Best training days? ([Health](97-health-fitness-and-wellbeing.md)) |
| **Google Takeout** (location, search) | Places I visit most, travel stats, what I searched at 2am 😅 |
| **Your email or calendar** | How many hours in meetings? Who emails me most? |
| **Public data** (Kaggle, data.gov, Our World in Data) | Anything you're curious about! |

## 🔒 Privacy with data

<details class="eli5">
<summary>🧸 ELI5</summary>

Before sharing data with AI, remove people's names, emails and account numbers, especially if the data is about other people.

</details>

- **Strip identifiers** (names, emails, account numbers) before uploading sensitive data.
- **Aggregate** when possible: monthly totals instead of individual transactions.
- **Check your plan's data policy**, especially for work data ([Privacy & Your Data](../part-12-mastery/104-privacy-and-your-data.md)).
- **Go local** for very sensitive data: Claude Code or a local model on your own machine.

## 🎯 Key takeaways

- **Chat with a spreadsheet** using code execution, and always ask for the **code and assumptions**.
- **AI columns** turn text into numbers, and **notebooks** make analysis repeatable.
- **DuckDB** and **database MCP servers** (read-only!) let you ask SQL questions in English.
- **Dashboards** take minutes with Artifacts or Streamlit.
- Think clearly: **causation, sample size, distributions, honest charts**, and verify one number by hand.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. What two things should you always ask when AI analyzes your data?</summary>

**"Show me the code you ran"** and **"What assumptions did you make?"**

</details>

<details class="quiz">
<summary>❓ 2. Why give a database MCP server read-only credentials?</summary>

So the agent **can't accidentally change or delete** data while analyzing it.

</details>

<details class="quiz">
<summary>❓ 3. Ice cream sales and sunburns rise together. Does ice cream cause sunburn?</summary>

**No.** It's **correlation, not causation**: both are caused by sunny, hot weather.

</details>

> [!TIP]
> **🎮 Try this**
> Request your **Spotify (or YouTube/Netflix) data export**, upload it, and ask: *"Tell me the story of my year in listening, with
> charts, surprising stats and a playful personality analysis."* Data analysis has never been this fun. 🎶📊

---

**Next:** [103 · Safety, Costs & Gotchas →](../part-12-mastery/103-safety-costs-and-gotchas.md)
