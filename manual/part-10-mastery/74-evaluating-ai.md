# 38 · Evaluating & Comparing AI (Evals for Normal People) 🧪⚖️

"Which model is best?" The honest answer is **"best at *what*, for *you*?"** Leaderboards are a starting
point, but the only benchmark that truly matters is **your tasks**. This chapter teaches the skill that separates AI power users
from everyone else: **testing things properly.** It's easier than it sounds and genuinely fun.

---

## Why evaluate?
- Pick the **right model or tool** for a job (and save money by not over-buying).
- Know if a **prompt change actually helped** or just *felt* better.
- Catch **regressions** when a model or tool updates.
- Build **trust** before automating something important.

## The 15-minute personal eval 🏃

1. **Collect 10–20 real tasks** you actually do: emails to draft, questions about your docs, data to extract, code to fix.
2. **Write down what "good" looks like** for each (a correct answer, or 3–5 criteria).
3. **Run each task** through the options you're comparing (models, prompts, tools).
4. **Score them blind** if you can: hide which output came from where. (Ask a friend to shuffle, or use a tool.)
5. **Tally the results**, and note the cost and speed too.

| Task | Criteria | Model A | Model B | Model C |
|---|---|---|---|---|
| Reply to angry customer email | Empathetic, concise, offers a fix, no over-promising | 4/5 | 5/5 | 3/5 |
| Extract invoice fields | All 6 fields correct | ✅ | ✅ | ❌ (missed due date) |
| Summarize meeting | Captures all decisions + owners | 3/4 | 4/4 | 4/4 |

Put it in a spreadsheet. Congratulations, you've built an **eval set**. 🎉

## Scoring methods

| Method | Use for | Notes |
|---|---|---|
| **Exact match / checks** | Extraction, classification, math, code (tests!) | Objective and automatable, the gold standard |
| **Rubric scoring (you)** | Writing, advice, creativity | Use 3–5 specific criteria, not vibes |
| **Pairwise comparison** | "Which is better, A or B?" | Humans are better at comparing than rating |
| **LLM-as-judge** | Scaling rubric scoring | A strong model grades outputs against your rubric. Spot-check it against your own judgment! |

## Arenas & leaderboards (useful hints) 🏟️
| Resource | What it measures |
|---|---|
| **LMArena** (formerly Chatbot Arena) | Human preference votes in blind head-to-heads |
| **Artificial Analysis** | Quality indices, speed, and price comparisons |
| **SWE-bench & coding leaderboards** | Real-world coding tasks |
| **Vendor model cards** | Benchmarks the labs report (read the fine print) |

Leaderboards tell you **who's in the top tier**. Your own eval tells you **who's best for you**.

## Evaluating your own AI systems 🛠️

Building RAG bots, agents, or automations? Treat quality like code:
- **Keep a test set** (inputs + expected outputs) in a file. The RAG kit's [`test_rag.py`](../../examples/rag-from-scratch/test_rag.py) is a tiny example.
- **Re-run after every change** (prompt, model, chunk size, tool description).
- **Track metrics over time:** accuracy, "I don't know" correctness, cost per task, latency.
- **Include edge cases:** empty input, trick questions, prompt-injection attempts, questions with no answer in the docs.
- **Tools that help:** n8n evaluations, promptfoo, Braintrust, LangSmith, Langfuse, and the providers' own eval tooling.

## Comparing *tools* (not just models) 🧰

When choosing between, say, three meeting-note apps or two automation platforms:
1. Run each on the **same 3 real scenarios**.
2. Score: output quality, time to set up, integrations, privacy, cost, and "did I enjoy using it?"
3. Pick one and commit for 30 days before re-evaluating.

## Mindset tips 🧠
- **Beware the first impression.** One amazing (or awful) answer isn't a trend. Test 10+.
- **Variance is real.** Run important tests 2–3 times.
- **Cheaper often wins.** You'll frequently find a smaller model scores the same on simple tasks at a fraction of the cost.
- **Re-test when models update.** The landscape shifts every few months.

---

### 🎮 Try this
**Model tasting night:** write 10 prompts that matter to you, run them through 3 assistants (free tiers are fine), and score
them blind. Share your results with a friend. You'll learn more about AI in one evening than from a month of reading hot takes. 🍷

---

**Next:** [39 · Cost Optimization Deep Dive →](75-cost-optimization.md)
