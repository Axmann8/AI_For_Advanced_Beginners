# 39 · Cost Optimization Deep Dive 💸📉

AI can be almost free or surprisingly expensive, depending on how you use it. The good news: a few simple
habits usually cut costs by **50–90%** with no loss in quality. This chapter is your money-saving playbook for
subscriptions, APIs, and automations.

---

## Part A: Subscriptions 📦

| Tip | Why |
|---|---|
| **One main paid assistant**, and free tiers for the rest | Most people don't need three $20 plans |
| **Audit quarterly** | Cancel tools you haven't opened in 30 days |
| **Annual billing** for tools you're sure about | Usually cheaper |
| **Team/business plans** only when you need admin/privacy features | They cost more per seat |
| **Check what's bundled** | E.g. Claude paid plans include Claude Code, and Google/Microsoft bundles include Gemini/Copilot |
| **Hitting limits often?** | Compare the higher tier's cost to your API usage. Sometimes upgrading is cheaper than pay-per-token |

## Part B: API costs, understanding the bill 🧾

```
cost ≈ (input tokens × input price) + (output tokens × output price)
```

- **Output tokens cost several times more** than input tokens.
- **Thinking/reasoning tokens** are billed as output.
- **Agents multiply calls:** a 10-step agent might resend the growing conversation 10 times.
- **Tool results count as input**, and big web pages or file dumps add up fast.

**Always log `usage`** from API responses (input/output/cached tokens). You can't optimize what you can't see.

## Part C: The optimization levers (in order) 🎚️

### 1. Free wins first
| Lever | Savings | How |
|---|---|---|
| **Prompt caching** | Big on repeated prefixes | Keep stable content (system prompt, docs, tool list) at the start, and variable content at the end. Cached reads are much cheaper |
| **Trim the input** | Proportional | Send the relevant excerpt, not the whole file. Summarize old conversation turns |
| **Filter before AI** | Up to 100% per item | Use plain workflow logic to skip items that don't need AI |
| **Batch API** | ~50% | For non-urgent bulk jobs (overnight classification, bulk summaries) |
| **Deduplicate** | Varies | Don't reprocess the same email, doc, or row. Store what's done |

### 2. Then the tradeoffs
| Lever | How |
|---|---|
| **Lower effort / thinking** | Simple tasks don't need deep reasoning. Tune per task |
| **Smaller model for simple steps** | Classify, extract, and route with small/fast models, and keep big models for hard reasoning |
| **Cap output length** | Ask for concise formats (JSON, bullets), and set sensible `max_tokens` |
| **Fewer agent turns** | Better tool descriptions → fewer wasted calls. Set turn limits |
| **Local models for grunt work** | Ollama handles high-volume, low-stakes tasks for the cost of electricity ([Ch. 26](../part-7-local-ai/26-local-and-open-models.md)) |

> 💡 **Measure before downgrading.** Run your eval set ([Ch. 38](38-evaluating-ai.md)) on the cheaper option. Judge **cost per
> completed task**, not per request. A cheap model that needs retries isn't cheap.

## Part D: Automation-platform costs ⚙️

| Platform | Billing unit | Optimization |
|---|---|---|
| **Zapier** | Tasks (each action step) | Filters early, Formatter instead of AI for simple text, fewer steps |
| **Make** | Operations/credits (each module run) | Aggregate before processing, avoid unnecessary iterations |
| **n8n Cloud** | Executions (whole runs) | Complex workflows are "free" per step, and self-hosting removes limits |
| **All** | Plus AI API costs | Cache, batch, and right-size models inside the workflows |

## Part E: Guardrails against surprise bills 🛡️

- [ ] **Spend limits** in every API console (hard caps + email alerts at 50% and 80%)
- [ ] **Separate API keys per project** so you can see what's spending
- [ ] **Turn limits** on agents and **max items** on loops
- [ ] **Rate limits** on any public-facing app that calls AI (bots can drain your budget!)
- [ ] **Test on 5 items** before running on 5,000
- [ ] A **monthly review** of the usage dashboards

## Part F: Quick math examples 🧮

Rough illustration (real prices vary by model and change over time):
- Summarizing **100 emails/day** with a small model ≈ pocket change per month.
- The same with a frontier model at max effort, sending full threads ≈ many times more.
- Add **caching** for the shared instructions + **trimming** to the latest message + the **small model for triage** only,
  escalating to a big model for the 10% that need it, and you get a fraction of the naive cost with the same quality where it matters.

The pattern: **route easy work to cheap paths, and save expensive intelligence for where it earns its keep.**

---

### 🎮 Try this
Pick one automation or script you run and **log its token usage for a day**. Then apply just two levers (trimming + caching, or a smaller
model for one step) and compare. Watching the number drop is deeply satisfying. 📉😄

---

**Next:** [40 · Staying Current Without Drowning →](40-staying-current.md)
