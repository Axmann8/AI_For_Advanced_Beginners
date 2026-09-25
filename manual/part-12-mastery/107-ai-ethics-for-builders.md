# 107 · AI Ethics for Builders: Build Things You're Proud Of 🌍🤝

> ⏱️ 7 min read · 🎯 Everyone who builds, automates or publishes with AI · 🧰 Needs: a project you care about, and 15 minutes of honest reflection

**The moment you build something with AI (a bot, an automation, an app, a video) you're making choices that affect other people.**
Ethics isn't a lecture or a list of "don'ts"; it's the craft of building things people can trust. This chapter turns big ideas
into practical habits: honesty and disclosure, consent, fairness and bias testing, privacy, human oversight, respecting creators,
environmental footprint, the rules taking shape around AI, and a one-page checklist you can run before you ship. Build boldly,
and build kindly. 💛

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

When you build something with AI, it's like inviting people to play in a treehouse you made. You want it to be **safe** (no
broken boards), **fair** (everyone can climb up), **honest** (no hidden tricks), and **kind** (it doesn't take things that
aren't yours). This chapter is a checklist for building a treehouse everyone's happy to play in. 🌳🏠

</details>

<!-- in-this-chapter -->

## 🧭 Why builders need ethics (not just big companies)

<details class="eli5">
<summary>🧸 ELI5</summary>

Even small projects affect real people. A little care at the start prevents big problems later.

</details>

Small builders now ship things that used to need whole teams: customer-service bots, hiring tools, voice agents, content
pipelines. That means **small choices reach real people**:

| A small choice… | …that affects people |
|---|---|
| Not telling callers they're talking to AI | Deceives customers, and may break the law |
| A résumé screener trained on past hires | Can quietly repeat past bias |
| A chatbot with no "talk to a human" option | Traps people with urgent problems |
| Cloning a voice "for fun" | Can harm the real person |
| Scraping artists' work for a style generator | Takes value from creators without consent |

Good ethics is also **good business**: trust is the hardest thing to rebuild once lost.

## 🗣️ Honesty & disclosure

<details class="eli5">
<summary>🧸 ELI5</summary>

Be honest when AI made something or when someone's talking to a robot. People deserve to know.

</details>

| Situation | Honest practice |
|---|---|
| **Chatbots & voice agents** | Say it's AI at the start, and offer a human path ([Voice Agents](../part-10-creative-ai/87-voice-agents.md)) |
| **Realistic images, video, audio** | Label AI-generated media where people could be misled |
| **Content & journalism** | Follow platform and publisher disclosure rules |
| **Capabilities** | Don't oversell what your AI can do. Say what it can't |
| **Provenance** | Prefer tools that add content credentials (C2PA) |

## ✋ Consent: faces, voices, data & work

<details class="eli5">
<summary>🧸 ELI5</summary>

Always ask before using someone's face, voice, words or art. If they say no, that's the answer.

</details>

- **Voices and faces:** only clone or generate real people **with explicit permission**, and never to deceive or humiliate.
- **Personal data:** use people's data only in ways they'd reasonably expect, and let them opt out
  ([Privacy & Your Data](104-privacy-and-your-data.md#-privacy-for-builders)).
- **Private messages:** don't feed friends' or customers' private messages into AI without consent.
- **Training data:** only fine-tune on data you have rights to ([Fine-Tuning](../part-9-local-ai/82-fine-tuning-for-normal-people.md)).
- **Kids:** take extra care with children's images and data.

## ⚖️ Fairness & bias

<details class="eli5">
<summary>🧸 ELI5</summary>

AI learned from the internet, which has unfair ideas in it. So AI can sometimes treat people unfairly. Test for it, and keep
humans in charge of big decisions about people.

</details>

AI models learn from human data, including its biases. That matters most when AI **affects decisions about people**: hiring,
lending, housing, education, healthcare, policing.

**A simple bias test you can run today:**

1. Take a realistic input (a résumé, a loan application, a support request).
2. Create **variants that change only one attribute** (name, gender, age, accent, neighborhood).
3. Run them all and **compare the outputs**. Any differences that shouldn't exist?
4. Fix the prompt, the data or the design, and **re-test** ([Evaluating AI](105-evaluating-ai.md)).

| Higher-risk uses | Safer designs |
|---|---|
| AI decides who gets hired | AI summarizes; humans decide with clear criteria |
| AI scores tenants or borrowers | Don't, or use audited, regulated systems |
| AI grades students alone | AI drafts feedback; teachers decide |
| AI moderates with no appeal | Human review and an appeal path |

## 👩‍⚖️ Human oversight & accountability

<details class="eli5">
<summary>🧸 ELI5</summary>

For important choices, a real person should always check the AI's work and be responsible for the final decision.

</details>

| Principle | In practice |
|---|---|
| **Humans for consequential decisions** | Money, health, legal, jobs, safety → a person approves |
| **Explainability** | Log why decisions were made (inputs, prompts, outputs) |
| **An appeal path** | People can ask a human to review |
| **Clear ownership** | Someone is responsible for how the system behaves |
| **Monitor after launch** | Review samples, complaints and failures regularly |

## 🎨 Respecting creators

<details class="eli5">
<summary>🧸 ELI5</summary>

Artists, writers and musicians work hard on their creations. Don't copy their work or style to compete with them, and give
credit where it's due.

</details>

- **Don't imitate living artists' signature styles** to compete with them; describe eras, media and moods instead
  ([Image Generation](../part-10-creative-ai/84-image-generation-deep-dive.md)).
- **Don't reproduce copyrighted work** (lyrics, articles, characters) for commercial use without rights.
- **Check commercial-use terms** of each tool ([Music Making](../part-10-creative-ai/86-music-making-with-ai.md#-rights-copyright--being-fair)).
- **Credit and pay** human collaborators, and hire artists for work that deserves a human touch.
- **Respect opt-outs** (robots.txt, "no AI training" requests) when scraping or collecting data ([Web Scraping](../part-5-automation/51-web-scraping-and-monitoring.md)).

## 🌱 Environmental footprint

<details class="eli5">
<summary>🧸 ELI5</summary>

AI computers use electricity and water. You can help by using smaller AIs for small jobs and not wasting runs.

</details>

AI uses real energy and water, mostly in data centers. The same habits that save money also save energy:

- **Right-size models:** small models for simple tasks ([Cost Optimization](106-cost-optimization.md)).
- **Don't generate waste:** avoid giant batch runs "just because," and cache repeated work.
- **Be thoughtful with video and images:** generation is compute-heavy.
- **Local isn't automatically greener**, but idle cloud loops definitely aren't.

## 📜 The rules taking shape

<details class="eli5">
<summary>🧸 ELI5</summary>

Countries are making new laws about AI. Most say: be honest, be careful with risky uses, and protect people's information.

</details>

AI regulation is evolving worldwide. Common themes:

| Theme | Examples |
|---|---|
| **Risk-based rules** | The EU AI Act sorts uses by risk, with strict duties for "high-risk" uses (hiring, credit, education) and bans on some practices |
| **Transparency** | Telling people when they interact with AI, and labeling synthetic media |
| **Privacy** | Existing data-protection laws (like the GDPR) apply to AI too |
| **Sector rules** | Health, finance, employment and telemarketing have their own requirements |
| **Consumer protection** | No deceptive claims about what AI can do |

**Not legal advice:** if you're building something in a regulated area or at scale, get proper legal guidance.

## ✅ The builder's ethics checklist

<details class="eli5">
<summary>🧸 ELI5</summary>

Before you share what you built, go through these questions. If any answer worries you, fix it first.

</details>

Before you ship, ask:

- [ ] **Honest?** Do people know when they're dealing with AI, and what it can't do?
- [ ] **Consent?** Do we have permission for every face, voice, dataset and creative work used?
- [ ] **Fair?** Did we test with varied inputs for unfair differences?
- [ ] **Private?** Do we collect only what we need, protect it, and let people delete it?
- [ ] **Safe?** Are harmful or irreversible actions gated behind human approval? ([Safety, Costs & Gotchas](103-safety-costs-and-gotchas.md))
- [ ] **Accountable?** Is there a human owner, a log, and an appeal path?
- [ ] **Accessible?** Can people with disabilities use it? ([Accessibility & AI](../part-11-ai-for-life-and-work/101-accessibility-and-ai.md))
- [ ] **Would I be comfortable** if this project appeared on the front page, explained in full? 📰

## 🎯 Key takeaways

- Small builders make choices that reach real people, so **ethics is part of the craft**.
- **Disclose AI**, get **consent** for faces, voices, data and creative work, and **respect creators**.
- **Test for bias** with one-attribute variants, and keep **humans in charge** of consequential decisions.
- Right-size models for **cost and energy**, and follow the **rules taking shape** (risk, transparency, privacy).
- Run the **checklist** before you ship.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. How can you test a résumé-screening prompt for bias?</summary>

Create **variants that change only one attribute** (name, gender, age), run them all, and **compare the outputs** for differences
that shouldn't exist.

</details>

<details class="quiz">
<summary>❓ 2. Your voice agent sounds very human. What must it do at the start of calls?</summary>

**Disclose that it's an AI** (and offer a way to reach a human).

</details>

<details class="quiz">
<summary>❓ 3. Is it OK to train an image LoRA on a living illustrator's portfolio to sell prints in their style?</summary>

**No**, not without their **consent**. It uses their work to compete with them.

</details>

> [!TIP]
> **🎮 Try this**
> Pick one thing you've built with AI (or plan to build) and run the **builder's ethics checklist**. Fix one thing it reveals, even
> a small one, like adding "I'm an AI assistant" to a bot's greeting. That's how trustworthy AI gets built: one small choice at a
> time. 🌱

---

**Next:** [108 · Teaching Others About AI →](108-teaching-others.md)
