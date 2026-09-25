# 05 · Context Engineering: Prompting's Big Sibling 🧩📐

> ⏱️ 8 min read · 🎯 Intermediate · 🧰 Needs: any AI assistant

**You already know the basics of good prompts. Context engineering is the next level: designing *everything* the model
sees** (standing instructions, examples, documents, tool descriptions, memory and conversation history) so it succeeds
reliably, not just once. It's the single biggest skill difference between casual users and people who get jaw-dropping
results.

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Imagine asking a new babysitter to look after your kids. A good note says who the kids are, the rules, where the snacks
are, what to do if something goes wrong, and an example of a perfect bedtime routine. **Context engineering is writing that
perfect note for your AI**, and keeping its desk tidy so the important stuff doesn't get buried.

</details>

<!-- in-this-chapter -->

## 🔭 From prompting to context engineering

<details class="eli5">
<summary>🧸 ELI5</summary>

A prompt is one sentence you say. Context is *everything* on the AI's desk: rules, examples, files, tools and past chat.
Getting the whole desk right matters more than the one sentence.

</details>

A **prompt** is the message you type. **Context** is the entire package the model receives. In modern AI setups, your
typed message is often the *smallest* part:

| Layer | Who writes it | How much it matters |
|---|---|---|
| App's system prompt | The app maker | You can't change it, but you can add to it |
| **Your standing instructions** (Projects, custom instructions, `CLAUDE.md`) | **You** | 🔥 Huge, applied every time |
| **Tool descriptions** (MCP servers, connectors) | Server authors, or **you** | 🔥 Huge for agents |
| **Retrieved or attached documents** | **You**, or RAG | 🔥 Huge for accuracy |
| **Examples** | **You** | 🔥 Shapes style and format |
| Conversation history | You + the model | Grows, and can get messy |
| Your latest message | **You** | Important, but not everything |

**Context engineering** = deliberately designing each layer. Anthropic and others started using the term in 2025 because,
for agents especially, the prompt is only a sliver of what determines success.

## 📜 Standing instructions that actually work

<details class="eli5">
<summary>🧸 ELI5</summary>

Standing instructions are the note you leave once that the AI reads every single time, like the rules on the fridge. Write
them clearly and you'll never have to repeat yourself.

</details>

Standing instructions live in **Projects** (Claude, ChatGPT), **Gems** (Gemini), **custom instructions**, or agent memory
files like **`CLAUDE.md` / `AGENTS.md`**. A great one covers:

| Part | Example |
|---|---|
| 🎯 **Goal & audience** | "You help me write a weekly newsletter for beginner gardeners." |
| 🧑 **Context about me/us** | "I'm a nurse, not a gardener by trade. Readers are busy parents in cool climates." |
| 📏 **Constraints** | "Max 600 words. No Latin plant names without a plain name. UK spelling." |
| 🧾 **Output format** | "Sections: Hook, This Week's Task, Plant Spotlight, Quick Wins (3 bullets)." |
| 🗂️ **Reference material** | "Use the attached 'past issues' file for tone. Never repeat a spotlight plant." |
| 🚦 **Judgment calls** | "If a claim is uncertain, say so. Ask me before recommending pesticides." |

**Tips from people who do this all day:**

- **Explain *why*, not just *what*.** "Keep it short *because readers skim on phones*" generalizes far better than "keep it short."
- **Don't over-prescribe.** Modern models are smart. A wall of ALL-CAPS rules makes them rigid and anxious. State priorities calmly.
- **Positive instructions beat negative ones.** "Write in plain, warm language" works better than a list of banned words
  (although a short "avoid these clichés" list can help).
- **Keep it living.** When the AI makes a mistake twice, add one line to the instructions. When a line stops mattering, delete it.

## 🧪 Examples beat adjectives

<details class="eli5">
<summary>🧸 ELI5</summary>

Saying "make it fun and punchy" is fuzzy. Showing one example of what you mean is crystal clear. AI copies examples
really well.

</details>

"Make it punchy" means different things to different people. **One good example communicates more than ten adjectives.**

```text
Write product descriptions in this style.

<example>
Product: Bamboo cutting board
Description: Tough on knives' enemies, gentle on the knives. 🎋 Naturally antibacterial, dishwasher-shy, and
pretty enough to serve cheese on. Pairs well with Friday nights.
</example>

Now write one for: Cast-iron skillet
```

**Pro tips:**

- Use **2–3 varied examples** if you want range, because one example can make outputs too similar.
- Wrap examples in tags like `<example>` so the model knows they're examples, not instructions.
- For automations, **show the exact output format** (e.g., a JSON sample). Consistency skyrockets.

## 📎 Feeding documents the right way

<details class="eli5">
<summary>🧸 ELI5</summary>

When you give the AI a big stack of papers, put the papers first and your question at the end, label each paper clearly,
and ask it to find the exact quotes before answering.

</details>

| Technique | Why it works |
|---|---|
| **Long documents first, question last** | Models answer best when the question comes after the material |
| **Label each document** (`<doc title="Q3 report">…</doc>`) | Helps the model keep sources straight and cite them |
| **"Quote first, then answer"** | Ask it to pull relevant quotes, then reason from them, which cuts hallucinations sharply |
| **Only what's relevant** | 20 focused pages beat 500 loosely related ones |
| **Metadata matters** | Dates, authors and versions help it judge what's current |
| **Say what to do when it's missing** | "If the documents don't say, reply 'not in the sources'." |

For big, changing collections, you'll want **RAG** (fetching only the relevant chunks automatically). See
[RAG, Memory & Knowledge](../part-6-knowledge-and-memory/41-rag-memory-and-knowledge.md).

## 🔧 Tool descriptions are prompts too

<details class="eli5">
<summary>🧸 ELI5</summary>

Each tool has a little label telling the AI what it does. If the label is confusing, the AI will use the tool wrong, just
like you would with a mislabeled button.

</details>

For agents, **tool names and descriptions are some of the most important context there is.** Compare:

| ❌ Vague | ✅ Clear |
|---|---|
| `search(q)`: "Searches." | `search_customer_orders(email, since_date)`: "Find a customer's orders by email. Use when the user asks about order status, refunds or history. Returns up to 20 orders, newest first." |
| `update(id, data)` | `mark_invoice_paid(invoice_id)`: "Marks an invoice as paid. Only use after the user confirms payment was received." |

Good tool descriptions say **what it does, when to use it, what it returns, and any cautions**. You'll write these yourself
in [Building MCP Servers](../part-2-mcp-and-connectors/11-building-mcp-servers.md).

**Also:** fewer tools is better context. Every enabled tool's description takes up space and adds a choice. Turn off what
the task doesn't need.

## 📦 Structured outputs: context for machines

<details class="eli5">
<summary>🧸 ELI5</summary>

When a robot (not a person) will read the AI's answer, ask the AI to fill in a form with fixed boxes. Robots love forms.

</details>

When AI output feeds another step (an automation, a spreadsheet, a database), ask for **structured output**:

```text
Classify this support email. Reply with ONLY this JSON:
{"category": "billing" | "bug" | "feature" | "other", "urgency": 1-5, "summary": "one sentence"}
```

Many APIs and tools can **enforce** a schema so the output is always valid JSON (structured outputs, output parsers). See
[Calling AI APIs Directly](../part-5-building-with-ai/36-calling-ai-apis.md) and [Webhooks, APIs & JSON](../part-3-automation/15-webhooks-apis-json.md).

## 🗜️ Managing long sessions (context rot)

<details class="eli5">
<summary>🧸 ELI5</summary>

After a long, messy conversation, the AI's desk gets cluttered with old ideas and mistakes, and it starts getting
confused. Sometimes the best fix is a clean desk: a new chat with a short summary of what matters.

</details>

Long conversations accumulate **stale ideas, abandoned attempts and contradictions**. Researchers and practitioners call
this **context rot**: quality slowly drops even when there's room left.

**Hygiene habits:**

1. **One task per session.** New topic? New chat (or `/clear` in Claude Code).
2. **Handoff notes.** Before starting fresh, ask: *"Summarize what we decided, what's done, and what's next in 10 bullets."*
   Paste that into the new session.
3. **Correct early.** If the AI heads the wrong way, interrupt and redirect. Don't let a wrong assumption pile up for 20 turns.
4. **Prune pasted junk.** Giant logs and files you no longer need eat attention.
5. **Let tools compact.** Agents like Claude Code summarize automatically, but a manual summary at a milestone is even better.

## 🧠 What to remember, and where

<details class="eli5">
<summary>🧸 ELI5</summary>

Some things the AI should always know (put them in the fridge note). Some things only matter for one project (put them in
that project's folder). Some things change every day (let it look them up fresh).

</details>

| Kind of info | Where it belongs | Example |
|---|---|---|
| Stable facts about you | Custom instructions or memory | "I'm vegetarian, based in Lisbon, prefer short answers" |
| Project knowledge | Project files, `CLAUDE.md`, Notion page | Style guide, codebase conventions, client brief |
| Big or changing reference | RAG, connectors, MCP | Company wiki, your email, product docs |
| Today's specifics | Your message | "The meeting moved to Thursday" |
| Secrets (API keys, passwords) | **Nowhere in prompts!** Use env vars and secure connectors | Never paste keys into chats |

Deep dive: [Memory for Agents](../part-6-knowledge-and-memory/44-memory-for-agents.md).

## 🧰 Build a reusable context kit

<details class="eli5">
<summary>🧸 ELI5</summary>

Keep a little folder of your best notes (who you are, how you write, your project rules) and reuse it everywhere. It's
like having your favorite recipe cards ready.

</details>

Create a folder (or a Notion page) with these files, then attach or reference them whenever you start important work:

```text
context-kit/
├── about-me.md          ← role, goals, preferences, what "good" looks like to me
├── style-guide.md       ← voice, formatting, words I love and hate, 2-3 examples
├── glossary.md          ← terms, acronyms, project names that AI would otherwise guess
├── project-brief.md     ← goal, audience, constraints, decisions made so far
└── examples/            ← gold-standard outputs to imitate
```

Many people turn their kit into **Claude Projects**, **Gems**, **Claude skills** (packaged instructions the AI loads when
relevant, see [Claude Code Power-Ups](../part-5-building-with-ai/32-claude-code-power-ups.md)), or a `CLAUDE.md` in their
repo or Obsidian vault.

## ✅ The context engineering checklist

<details class="eli5">
<summary>🧸 ELI5</summary>

Before a big AI task, run through this list like a pilot's pre-flight check.

</details>

- [ ] Does the AI know the **goal**, the **audience**, and **why**?
- [ ] Did I include the **relevant documents** (and only those), with labels?
- [ ] Did I show **an example** of great output?
- [ ] Is the **output format** explicit (especially if a machine reads it)?
- [ ] Are the right **tools** enabled, with clear descriptions, and unnecessary ones off?
- [ ] Did I say what to do when **information is missing or uncertain**?
- [ ] Is this a **fresh session**, or a clean handoff from a long one?

## 🎯 Key takeaways

- Your typed message is a small part of the context. **Standing instructions, documents, examples and tools** matter more.
- **Explain why**, prefer examples to adjectives, and don't over-prescribe.
- **Documents first, question last**, labeled, with "quote first, then answer."
- **Tool descriptions are prompts**: be specific about what, when, returns and cautions.
- Fight **context rot** with one task per session and handoff summaries.
- Build a **reusable context kit** and use it everywhere.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Your AI writes in the wrong tone even though you said "casual." What's the strongest fix?</summary>

Show **one or two examples** of the tone you want (wrapped in `<example>` tags). Examples beat adjectives.

</details>

<details class="quiz">
<summary>❓ 2. Where should the question go when you attach a 50-page document?</summary>

**After** the document, at the end of the message.

</details>

<details class="quiz">
<summary>❓ 3. An agent keeps choosing the wrong tool. What do you check first?</summary>

The **tool names and descriptions** (are they specific about when to use each?) and whether **too many tools** are enabled.

</details>

<details class="quiz">
<summary>❓ 4. After two hours of back-and-forth, answers are getting worse. Why, and what do you do?</summary>

**Context rot**: stale ideas and contradictions pile up. Ask for a handoff summary and start a **fresh session** with it.

</details>

> [!TIP]
> **🎮 Try this**
> Build your **`about-me.md`** and **`style-guide.md`** today (15 minutes). Paste them into a Claude Project or ChatGPT
> Project, then ask for something you write often, like an email, a post or a plan. Compare it with what you got before. The
> jump in quality is usually dramatic. ✨

---

**Next:** [06 · Choosing Your AI Stack →](06-choosing-your-ai-stack.md)
