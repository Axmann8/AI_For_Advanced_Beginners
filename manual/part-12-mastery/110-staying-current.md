# 110 · Staying Current Without Drowning 🌊📰

> ⏱️ 6 min read · 🎯 Everyone who wants to keep up without burning out · 🧰 Needs: a newsletter or two, a calendar, optionally the Morning AI Digest workflow

**AI moves at a ridiculous pace. New models, tools and features launch every week, and some tools vanish just as fast.** You
don't need to follow everything (nobody can!). You need a **light, reliable system** that surfaces what matters and keeps you
learning. This chapter gives you a sustainable "AI diet," the best newsletters, podcasts, courses and communities, a
self-running news digest, a hype filter, and a learning log that compounds. Stay curious, stay calm. 😌

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

AI news is like a firehose: way too much water to drink! Instead of trying to drink it all, you use a little cup: a few minutes
a day of news, one new thing to try each week, and a bigger learning session each month. That way you keep growing without
getting overwhelmed. 🥤🌱

</details>

<!-- in-this-chapter -->

## 🥗 The sustainable AI diet

<details class="eli5">
<summary>🧸 ELI5</summary>

A little bit every day, a bit more every week, and a big session every month. Small and steady wins the race.

</details>

| Frequency | Time | What |
|---|---|---|
| **Daily** | 5 min | Skim one AI newsletter or your automated digest |
| **Weekly** | 30–60 min | Try **one** new thing hands-on (a tool, feature or MCP server) |
| **Monthly** | 1–2 hours | A deeper learning session: a course module, a long read or a project |
| **Quarterly** | 1 hour | Re-evaluate your stack ([Choosing Your AI Stack](../part-3-foundations/37-choosing-your-ai-stack.md)) and re-run your personal eval ([Evaluating AI](105-evaluating-ai.md)) |

> [!TIP]
> **💡 Try > read**
> Ten minutes using a new feature teaches more than an hour of hot takes.

## 📬 Newsletters & blogs

<details class="eli5">
<summary>🧸 ELI5</summary>

A few trusted email newsletters and websites that explain AI news clearly. Pick one or two, not all of them.

</details>

| Source | Why |
|---|---|
| **Simon Willison's Weblog** | Thoughtful, hands-on, honest. A treasure for builders |
| **Import AI** (Jack Clark) | Research trends and big-picture thinking |
| **The Batch** (DeepLearning.AI) | Weekly news with context |
| **Latent Space** | AI engineering deep dives (plus a podcast) |
| **Ben's Bites / TLDR AI / The Rundown** | Quick daily digests |
| **Official blogs**: Anthropic, OpenAI, Google DeepMind, Hugging Face, the MCP blog | Primary sources for launches |
| **Changelogs** of the tools you use | Features you're already paying for! |

## 🎧 Podcasts & YouTube

<details class="eli5">
<summary>🧸 ELI5</summary>

Shows you can listen to on a walk or watch on the couch to learn about AI.

</details>

| Show / channel | Vibe |
|---|---|
| **Latent Space** | Builders and researchers, technical |
| **Hard Fork** | Tech news, entertaining |
| **Dwarkesh Podcast** | Long, deep interviews with leading thinkers |
| **The Cognitive Revolution** | In-depth conversations on AI capabilities |
| **AI Explained** (YouTube) | Clear breakdowns of new models and papers |
| **Andrej Karpathy** (YouTube) | How LLMs actually work, from scratch |
| **3Blue1Brown** (neural networks series) | Beautiful visual intuition |
| **Two Minute Papers** | Fun research highlights |

**Hack:** turn long episodes or papers into a Gemini Notebook and listen to a custom Audio Overview instead
([Gemini Notebook Masterclass](../part-8-knowledge-and-memory/76-notebooklm-masterclass.md)). 🎧

## 🎓 Courses & learning paths

<details class="eli5">
<summary>🧸 ELI5</summary>

Free online classes that teach AI skills step by step, from building with Claude to automation tools.

</details>

| Resource | Good for |
|---|---|
| **Anthropic's courses & docs** (prompting, tool use, MCP, Claude Code) | Building with Claude |
| **DeepLearning.AI short courses** | Free 1–2 hour courses on agents, RAG, MCP, evals… |
| **Hugging Face courses** (LLMs, agents, MCP) | The open-source ecosystem, hands-on |
| **fast.ai** | Deep learning from a practical, top-down angle |
| **n8n / Zapier / Make academies** | Automation skills |
| **modelcontextprotocol.io** | The official MCP docs and tutorials |
| **This manual's Build-Alongs** | Hands-on projects ([Part XIII](../part-13-build-alongs/index.md)) |

## 👥 Communities

<details class="eli5">
<summary>🧸 ELI5</summary>

Places online and in real life where people who love AI help each other and share what they've made.

</details>

| Community | Topic |
|---|---|
| **r/LocalLLaMA** | Local and open models (hugely knowledgeable) |
| **r/ClaudeAI, r/ChatGPT, r/OpenAI** | Assistant tips and news |
| **r/n8n, the n8n community forum** | Automation help and templates |
| **MCP Discord & GitHub discussions** | Building MCP servers |
| **Hugging Face** | Models, Spaces, datasets, discussions |
| **Local meetups & hackathons** | The fastest way to make AI friends 🤝 |

## 🤖 Automate your own AI news feed

<details class="eli5">
<summary>🧸 ELI5</summary>

Build a little robot that reads AI news for you every morning and sends you just the five best bits.

</details>

You've already got the tools! Import the [Morning AI Digest](../../examples/n8n-workflows/morning-ai-digest.json) and point it at:

- The blogs above (most have RSS feeds)
- `https://hnrss.org/newest?q=MCP+OR+Claude+OR+n8n&points=50` (filtered Hacker News)
- `https://www.reddit.com/r/LocalLLaMA/top/.rss?t=day`

Have Claude pick the top 5 **for your interests**, with a "try this today" suggestion. Your personal AI news editor. ☕ (Full
build: [Build-Along: Automated Newsletter](../part-13-build-alongs/118-build-along-automated-newsletter.md).)

## 🧭 Filtering the hype

<details class="eli5">
<summary>🧸 ELI5</summary>

Lots of AI news is exciting but not useful for you. Ask a few questions before getting excited or spending money.

</details>

Ask of any announcement:

1. **Can I try it today?** (Demos and waitlists aren't products.)
2. **Does it solve a problem I actually have?**
3. **What do hands-on users say after a week?** (Not launch-day reactions.)
4. **Is it better on *my* tasks?** (Run your eval.)
5. **Will it still be here next year?** (Tools do shut down, so keep your own copies of your work.)

> [!NOTE]
> **📌 It's OK to miss things**
> Anything truly important will still be important next month, with better docs and fewer bugs. 😌

## 🌱 Keep a learning log

<details class="eli5">
<summary>🧸 ELI5</summary>

Write down what you tried each week and whether you liked it. After a few months, you'll see how much you've grown!

</details>

A simple note or spreadsheet:

| Date | What I tried | What I learned | Keep / drop |
|---|---|---|---|
| 2026-09-02 | Claude Code plan mode | Plans save me from rework | ✅ Keep |
| 2026-09-09 | A new image model | Great text in images, slow | 🤔 For posters only |
| 2026-09-16 | Local model for journaling | Good enough, fully private | ✅ Keep |

After a few months it becomes a gold mine, and great material to share ([Teaching Others](108-teaching-others.md)).

## 🎯 Key takeaways

- Follow a **sustainable AI diet**: 5 minutes daily, one hands-on try weekly, a deeper session monthly, a stack review quarterly.
- Pick **one or two** newsletters and podcasts, not twenty.
- **Automate** your AI news with a digest workflow.
- **Filter hype** with five questions, and remember it's OK to miss things.
- Keep a **learning log** that compounds.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. What's the single most effective way to stay current?</summary>

**Try things hands-on** regularly (one new thing a week). Try > read.

</details>

<details class="quiz">
<summary>❓ 2. A flashy launch video promises a revolutionary tool, but there's only a waitlist. How do you treat it?</summary>

As **not yet real** for you. Wait until you can try it, and check what hands-on users say after a week.

</details>

<details class="quiz">
<summary>❓ 3. Why keep your own copies of work made in AI tools?</summary>

Tools can **change or shut down** (it happens!), and you don't want to lose your creations.

</details>

> [!TIP]
> **🎮 Try this**
> Set up your **sustainable AI diet** today: subscribe to **one** newsletter, pick **one** podcast, and put a recurring 30-minute
> "try one new AI thing" block on your calendar every week. Future you will be amazed how far you've come. 🚀

---

**Next:** [111 · Where This Is All Heading →](111-where-this-is-heading.md)
