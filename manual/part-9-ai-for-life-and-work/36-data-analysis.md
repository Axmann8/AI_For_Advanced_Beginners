# 36 · Data Analysis for Everyone 📊🐍

You don't need to know statistics or Python to get real answers from data anymore. AI can load your
spreadsheet, clean it, analyze it, chart it, and explain what it means. This chapter goes from "chat with a CSV" to
building live dashboards.

---

## Level 1: Chat with a spreadsheet 💬

Upload a CSV or Excel file to an assistant with **code execution** (Claude, ChatGPT, and Gemini all do this). Behind the scenes, it
writes and runs Python for you.

**Starter prompts:**
- *"Describe this dataset: columns, row count, data quality issues, and 5 interesting questions we could answer."*
- *"Clean it: fix dates, remove duplicates, standardize categories. Show me what you changed."*
- *"What are the top 3 insights? Include a chart for each."*
- *"Is the difference between group A and B meaningful, or could it be noise? Explain simply."*
- *"Give me the cleaned file as a download."*

💡 **Always ask:** *"Show me the code you ran"* and *"What assumptions did you make?"* That's how you catch mistakes, and
how you learn.

## Level 2: AI inside your spreadsheet 📈

| Tool | What you can do |
|---|---|
| **Google Sheets + Gemini** | Generate formulas and tables, and `=AI()` per-cell prompts for classifying and summarizing rows |
| **Excel + Copilot** | Formulas, pivots, charts, insights, **Python in Excel** |
| **Airtable AI** | AI fields that enrich every row automatically |

**Classic magic trick:** 500 customer comments in column A → add columns with AI for **sentiment**, **theme**, and
**urgency** → pivot table by theme. Qualitative data becomes quantitative in minutes. 🪄

## Level 3: Analysis notebooks with AI 🐍

When you want repeatable, bigger analysis:
1. Open **Claude Code / Cursor** in a folder with your data, or use **Jupyter / Google Colab** with AI assistance.
2. *"Create a Jupyter notebook that loads sales.csv, cleans it, and analyzes monthly trends by region with charts. Explain each
   step in markdown cells."*
3. Run, read, and iterate: *"Add a forecast for the next 3 months with a simple model and confidence intervals."*

Handy libraries the AI will reach for: **pandas** or **polars** (tables), **matplotlib/seaborn/plotly** (charts), **DuckDB**
(SQL on files, which is great with AI), and **scikit-learn** (simple ML).

## Level 4: Talk to databases with MCP 🗄️

Connect a database MCP server ([Ch. 5](../part-2-mcp-and-connectors/05-mcp-server-catalog.md)) with a **read-only** user:
> *"Explore the schema. Which marketing channel brought customers with the highest lifetime value? Show the SQL."*

The AI writes SQL, runs it, checks the results, and explains. This is a game-changer for anyone who's ever waited on a data team.

## Level 5: Dashboards & data apps 🖥️

| Option | Effort | Notes |
|---|---|---|
| **Claude Artifacts** | Minutes | Interactive charts and dashboards right in chat, shareable |
| **Looker Studio / Power BI + AI** | Low | Classic BI with AI assistance |
| **Streamlit** (Python) | Medium | *"Build a Streamlit dashboard for this CSV with filters by region and date."* |
| **Evidence, Observable** | Medium | Code-based, beautiful data reports |
| **Vibe-coded web app** | Medium | A custom dashboard with Supabase data ([Ch. 19](../part-5-building-with-ai/19-vibe-coding-your-first-app.md)) |

## Fun datasets to practice with 🎮
| Dataset | Questions to ask |
|---|---|
| Your **bank/credit card export** | Where does my money go? Trends? Forgotten subscriptions? |
| Your **Spotify/YouTube/Netflix data export** | My taste over time, top artists by season, binge patterns 🎧 |
| Your **fitness app export** (Strava, Apple Health) | Am I improving? Best training days? |
| **Google Takeout: Location/Maps** | Places I visit most, travel stats |
| **Public data** (Kaggle, data.gov, Our World in Data) | Anything you're curious about! |

## Avoiding data mistakes ⚠️
- **Check the row counts** before and after cleaning.
- **Correlation ≠ causation.** Ask AI to list alternative explanations.
- **Watch for tiny samples.** *"Is the sample size big enough to conclude this?"*
- **Verify one number by hand** (or in a pivot table) to make sure the AI's pipeline is right.
- **Privacy:** strip names, emails, and account numbers before uploading sensitive data.

---

### 🎮 Try this
Request your **Spotify (or YouTube/Netflix) data export**, upload it, and ask: *"Tell me the story of my year in listening, with
charts, surprising stats, and a playful personality analysis."* Data analysis has never been this fun. 🎶📊

---

**Next:** [37 · Safety, Costs & Gotchas →](../part-10-mastery/37-safety-costs-and-gotchas.md)
