# 58 · Spreadsheet Superpowers 📊✨

> ⏱️ 6 min read · 🎯 Everyone who's ever fought a VLOOKUP · 🧰 Needs: Google Sheets, Excel or Airtable

**Spreadsheets are where AI quietly delivers some of its biggest everyday wins.** It writes and explains formulas, cleans
messy data, classifies hundreds of rows with a single function, builds charts, and finds the story in your numbers. This
chapter turns you into the spreadsheet wizard of your group, no formula memorization required. 🧙

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Spreadsheets are grids of boxes. Now AI can fill boxes for you: "is this review happy or sad?", "what country is this
address in?", "write a summary of this row." It can also write the tricky math formulas, clean up messy lists, and draw
charts that explain what your numbers mean.

</details>

<!-- in-this-chapter -->

## 💞 Why spreadsheets + AI is a perfect match

<details class="eli5">
<summary>🧸 ELI5</summary>

Spreadsheets have lots of rows that each need the same little job done. AI is great at doing the same little job over and
over, so they're best friends.

</details>

Spreadsheets are **structured** (rows and columns), **repetitive** (the same job for every row), and **full of fuzzy text**
(comments, descriptions, addresses). That's the exact shape of work AI excels at, and the grid shows every result, so it's
easy to spot-check.

## 🧮 Formula help: write, explain, fix

<details class="eli5">
<summary>🧸 ELI5</summary>

Instead of memorizing tricky formulas, just describe what you want in plain words, and the AI writes the formula and
explains how it works.

</details>

| You say… | AI gives you… |
|---|---|
| *"Sum column C where column A is 'Paid' and the date in B is this month."* | `=SUMIFS(C:C, A:A, "Paid", B:B, ">="&EOMONTH(TODAY(),-1)+1, B:B, "<="&EOMONTH(TODAY(),0))` |
| *"Look up each email in Sheet2 and return the plan name."* | An `XLOOKUP` (or `INDEX/MATCH`) with error handling |
| *"Explain this formula like I'm five."* | A step-by-step breakdown of a scary nested formula |
| *"Why does this return #N/A?"* | The likely cause (extra spaces, text vs. number, missing value) + a fix |
| *"Extract the domain from these emails."* | `REGEXEXTRACT` or `TEXTAFTER` formulas |

**Where to ask:** Gemini in Sheets, Copilot in Excel, or any assistant (paste a few sample rows and your column letters).

## 🤖 AI functions in cells

<details class="eli5">
<summary>🧸 ELI5</summary>

Some spreadsheets now have an "ask AI" formula. Put it in a column and it answers your question for every single row.

</details>

| Tool | Function | Example |
|---|---|---|
| **Google Sheets** | `=AI(prompt, [range])` | `=AI("Classify this review as positive, neutral or negative", B2)` |
| **Excel** (Microsoft 365 Copilot) | `COPILOT(...)` | `=COPILOT("Summarize this feedback in 5 words", B2)` |
| **Airtable** | AI fields | An AI field "Category" that auto-tags each new record |

**The magic trick:** 500 survey responses → add AI columns for **sentiment**, **theme** and **one-line summary** → pivot by
theme. Qualitative mush becomes a clear chart in 10 minutes. 🪄

> [!WARNING]
> **⚠️ AI cells aren't ordinary formulas**
> They can give slightly different answers on recalculation, have usage limits, and send cell contents to the AI service.
> **Freeze results** (copy → paste values) once you're happy, and don't feed them sensitive data unless your plan allows it.

## 🧹 Cleaning messy data

<details class="eli5">
<summary>🧸 ELI5</summary>

Real lists are messy: the same company spelled five ways, dates in different formats, names squished together. AI can tidy
all of that up.

</details>

| Mess | Prompt |
|---|---|
| Inconsistent names ("Acme Inc", "ACME", "acme corp.") | *"Standardize company names in column A, and show me a mapping table first."* |
| Mixed date formats | *"Convert column C to ISO dates (YYYY-MM-DD). Flag anything ambiguous like 03/04."* |
| Full names in one cell | *"Split into first and last name. Handle middle names and 'van der' style surnames."* |
| Duplicates with small differences | *"Find likely duplicate contacts (same person, different spellings) and propose merges."* |
| Free-text categories | *"Map these 300 free-text job titles into 8 standard categories."* |

**Pro tip:** ask for a **mapping table** or **proposed changes** before applying them, and keep the original column. Undo is
your friend.

## 📈 Analysis & charts

<details class="eli5">
<summary>🧸 ELI5</summary>

Ask your spreadsheet questions in normal words, like "which month was best?", and the AI works out the answer and draws a chart.

</details>

- **In-app:** Gemini in Sheets and Copilot in Excel answer questions, build pivots and suggest charts.
- **Upload to an assistant with code execution** (Claude, ChatGPT, Gemini): *"Clean this, find the top 3 insights, and make a
  chart for each."* Behind the scenes, it writes and runs Python ([Data Analysis for Everyone](../part-11-ai-for-life-and-work/102-data-analysis.md)).
- **Always ask:** *"Show me the calculation"* and *"What assumptions did you make?"* That's how you catch mistakes.

## 🐍 Python in Excel & friendly scripts

<details class="eli5">
<summary>🧸 ELI5</summary>

For really big or tricky jobs, the spreadsheet can run little Python programs, and AI can write those programs for you.

</details>

- **Python in Excel:** run pandas and charts inside cells, and Copilot can write the Python for you.
- **Google Apps Script:** automate Sheets (and call AI APIs) on schedules ([Google & Microsoft AI](55-google-and-microsoft-ai.md#-apps-script--gemini-a-tiny-robot-optional)).
- **Office Scripts / VBA:** AI is excellent at writing and explaining macros: *"Write an Office Script that formats this table
  and highlights overdue rows."*

## 🔌 Spreadsheets as AI databases

<details class="eli5">
<summary>🧸 ELI5</summary>

Spreadsheets are also great "memory boxes" for robot recipes: a place to log what happened, store lists, and keep settings
that automations read.

</details>

- **Logs:** every automation run appends a row, making debugging and stats easy.
- **Config:** a "settings" sheet (keywords, targets, recipients) that non-technical teammates can edit.
- **Memory:** a simple table of facts or preferences an agent reads and updates.
- **Mini CRM:** contacts + AI columns for "next best action."

Google Sheets, Excel Online and Airtable all have great nodes in n8n, Zapier and Make ([Part V](../part-5-automation/index.md)).

## 🧪 10 spreadsheet projects to try

<details class="eli5">
<summary>🧸 ELI5</summary>

Ten fun spreadsheet jobs where AI saves you hours.

</details>

| # | Project | AI does |
|---|---|---|
| 1 | 🗣️ Survey analyzer | Sentiment, themes and summaries per response |
| 2 | 💸 Expense categorizer | Categories from bank descriptions |
| 3 | 🧾 Receipt log | Extracts vendor, amount and date from photos (via automation) |
| 4 | 🧲 Lead scorer | Fit score + reason from company info |
| 5 | 🌍 Translation table | Product descriptions in 5 languages |
| 6 | 📚 Reading list | Summary + "worth reading?" score from URLs |
| 7 | 🏷️ Inventory tagger | Categories and attributes from product names |
| 8 | 📅 Content calendar | Post ideas and captions per row |
| 9 | 🧑‍🏫 Gradebook helper | Draft comments from scores and notes (teacher reviews each!) |
| 10 | 🏠 Home maintenance tracker | Due dates and plain-English instructions per task |

## ⚠️ Pitfalls to avoid

<details class="eli5">
<summary>🧸 ELI5</summary>

AI can occasionally make up numbers or mislabel rows, so check a few by hand, save final answers as plain values, and keep
private information private.

</details>

| Pitfall | Fix |
|---|---|
| Trusting AI math blindly | Verify one number by hand or with a pivot, and prefer real formulas for arithmetic |
| Results change on recalculation | Copy → paste values once final |
| Hitting usage limits on AI functions | Process in batches, and only rows that need it |
| Sensitive data in AI cells | Check your plan's data policy, and anonymize first |
| Overwriting originals | Always write AI output to a **new column** |

## 🎯 Key takeaways

- AI **writes, explains and fixes formulas** from plain English.
- **AI functions** (`=AI()`, `COPILOT()`, Airtable AI fields) classify and extract across hundreds of rows.
- AI is a superb **data cleaner**. Ask for proposed changes first and keep originals.
- For analysis, **ask for the calculation and assumptions**, and verify a number yourself.
- Spreadsheets double as **logs, config and memory** for automations.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Your AI-classified column changed when you reopened the sheet. Why, and what's the fix?</summary>

AI functions can **recalculate** with slightly different results. **Copy → paste values** once you're happy.

</details>

<details class="quiz">
<summary>❓ 2. Safest way to let AI standardize 1,000 company names?</summary>

Ask for a **mapping table** first, review it, and write results to a **new column**, keeping the original.

</details>

> [!TIP]
> **🎮 Try this**
> Export any list you have (reviews, expenses, contacts, even your Spotify playlist), add one AI column with a fun question
> (*"what mood is this song?"*), and make a chart of the results. Spreadsheets have never been this fun. 📊🎉

---

**Next:** [59 · Chat Apps & Bots →](59-chat-apps-and-bots.md)
