# 107 · AI Ethics for Builders: Build Things You're Proud Of 🌍🤝

> ⏱️ 7 min read · 🎯 Everyone who builds, automates or publishes with AI · 🧰 Needs: a project you care about, and 15 minutes of honest reflection

**The moment you build something with AI (a bot, an automation, an app, a video) you're making choices that affect other people.**
Ethics isn't a lecture or a list of "don'ts"; it's the craft of building things people can trust. This chapter turns big ideas
into practical habits: honesty and disclosure, consent, fairness and bias testing, privacy, human oversight, respecting creators,
environmental footprint, the rules taking shape around AI, and a one-page checklist you can run before you ship. Build boldly,
and build kindly. 💛

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Anyone who builds with AI affects real people, even with a small project. This chapter covers the ethical practices that keep your work safe, fair, honest and respectful.

- **Be honest** about AI involvement, and get consent before using anyone's likeness, voice, data or work.
- **Test for bias,** and keep humans responsible for consequential decisions.
- **Respect creators,** and minimize your environmental footprint.
- **Run the ethics checklist** before you ship.

</details>

<!-- in-this-chapter -->

## 🧭 Why builders need ethics (not just big companies)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Individual builders can now ship tools that once required whole teams, such as customer-service bots, hiring tools and voice agents. A little care at the design stage prevents real harm later.

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

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Tell people when they're interacting with AI or viewing AI-generated content, and offer a way to reach a person. The table describes honest practice for chatbots, content, voice agents and more.

</details>

| Situation | Honest practice |
|---|---|
| **Chatbots & voice agents** | Say it's AI at the start, and offer a human path ([Voice Agents](../part-10-creative-ai/87-voice-agents.md)) |
| **Realistic images, video, audio** | Label AI-generated media where people could be misled |
| **Content & journalism** | Follow platform and publisher disclosure rules |
| **Capabilities** | Don't oversell what your AI can do. Say what it can't |
| **Provenance** | Prefer tools that add content credentials (C2PA) |

## ✋ Consent: faces, voices, data & work

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Use real people's faces, voices, personal data or creative work only with explicit permission, and never to deceive or humiliate.

</details>

- **Voices and faces:** only clone or generate real people **with explicit permission**, and never to deceive or humiliate.
- **Personal data:** use people's data only in ways they'd reasonably expect, and let them opt out
  ([Privacy & Your Data](104-privacy-and-your-data.md#-privacy-for-builders)).
- **Private messages:** don't feed friends' or customers' private messages into AI without consent.
- **Training data:** only fine-tune on data you have rights to ([Fine-Tuning](../part-9-local-ai/82-fine-tuning-for-normal-people.md)).
- **Kids:** take extra care with children's images and data.

## ⚖️ Fairness & bias

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

AI models can reflect biases in their training data. This matters most when AI influences decisions about people, such as hiring, lending or access to services. Test outputs across different groups, and keep humans involved in consequential decisions.

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

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

For decisions involving money, health, legal matters, employment or safety, a person should review AI outputs and be accountable for the result. Log decisions and provide a way to appeal. The table describes each principle.

</details>

| Principle | In practice |
|---|---|
| **Humans for consequential decisions** | Money, health, legal, jobs, safety → a person approves |
| **Explainability** | Log why decisions were made (inputs, prompts, outputs) |
| **An appeal path** | People can ask a human to review |
| **Clear ownership** | Someone is responsible for how the system behaves |
| **Monitor after launch** | Review samples, complaints and failures regularly |

## 🎨 Respecting creators

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Avoid imitating living artists' distinctive styles to compete with them, credit sources and collaborators, and use tools trained on licensed data where possible.

</details>

- **Don't imitate living artists' signature styles** to compete with them; describe eras, media and moods instead
  ([Image Generation](../part-10-creative-ai/84-image-generation-deep-dive.md)).
- **Don't reproduce copyrighted work** (lyrics, articles, characters) for commercial use without rights.
- **Check commercial-use terms** of each tool ([Music Making](../part-10-creative-ai/86-music-making-with-ai.md#-rights-copyright--being-fair)).
- **Credit and pay** human collaborators, and hire artists for work that deserves a human touch.
- **Respect opt-outs** (robots.txt, "no AI training" requests) when scraping or collecting data ([Web Scraping](../part-5-automation/51-web-scraping-and-monitoring.md)).

## 🌱 Environmental footprint

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

AI uses significant energy and water. The habits that save money also reduce environmental impact: use appropriately sized models, avoid unnecessary runs and cache repeated work.

</details>

AI uses real energy and water, mostly in data centers. The same habits that save money also save energy:

- **Right-size models:** small models for simple tasks ([Cost Optimization](106-cost-optimization.md)).
- **Don't generate waste:** avoid giant batch runs "just because," and cache repeated work.
- **Be thoughtful with video and images:** generation is compute-heavy.
- **Local isn't automatically greener**, but idle cloud loops definitely aren't.

## 📜 The rules taking shape

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

AI regulation is developing worldwide. Common themes include risk-based rules (such as the EU AI Act), transparency requirements, data protection and specific rules for deepfakes and automated decisions. The table gives examples.

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

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Before shipping, work through this checklist: honesty, consent, fairness, human oversight, privacy, safety and respect for creators.

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
