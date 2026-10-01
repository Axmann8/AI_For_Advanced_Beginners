# 104 · Privacy & Your Data: Use AI Without Oversharing 🔒🧠

> ⏱️ 8 min read · 🎯 Everyone (especially anyone using AI with work, family or health data) · 🧰 Needs: 20 minutes to check your AI app settings

**AI gets more useful the more it knows about you, which is exactly why privacy matters.** The good news: you don't need to be
paranoid, just intentional. This chapter explains what happens to what you type, the settings worth checking in every AI app,
a simple traffic-light system for deciding what to share, how to handle work data, connectors and kids' data, when to go fully
local, and how to build privacy-respecting AI tools yourself. 🛡️

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Anything you type into a cloud AI service is sent to the provider's servers, where it may be stored and, depending on your settings, used for training. Most everyday use is fine, but some information should never be shared, and some belongs only with local models.

1. **Understand what happens** to your data with each provider.
2. **Review the privacy settings** in every AI app you use.
3. **Apply the traffic-light system** to decide what to share.
4. **Use local AI** for your most sensitive information.

</details>

<!-- in-this-chapter -->

## 📮 What happens to what you type?

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Your messages go to the provider's servers so the model can respond. Depending on the product and your settings, they may be retained for a period and used to improve future models. The table summarizes the general picture; check each product's current policy.

</details>

| Question | The general picture (check each product's current policy) |
|---|---|
| **Where does it go?** | To the provider's servers (unless you run a local model) |
| **Is it stored?** | Usually yes, as chat history, for a retention period that varies by product and setting |
| **Is it used for training?** | Consumer apps often let you **choose**. Business, team and API plans typically **don't train on your data by default** |
| **Can humans see it?** | Some providers may review flagged content for safety. Policies explain when |
| **What about connectors?** | The AI reads connected data (email, Drive) to answer you, within the permissions you grant |
| **Memory?** | Some facts may be saved across chats, and you can view and delete them ([Memory for Agents](../part-8-knowledge-and-memory/75-memory-for-agents.md)) |

> [!NOTE]
> **📌 Policies change**
> Privacy terms and defaults change over time. Re-check your settings every few months, and whenever a product announces new
> features.

## ⚙️ Settings to check in every AI app

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Spend twenty minutes reviewing these settings in each AI app: training, chat history, memory, connected apps, temporary chats and data export or deletion.

</details>

- [ ] **Model training / "help improve" toggle:** decide whether your chats can be used to train models.
- [ ] **Chat history & retention:** how long chats are kept, and how to delete them.
- [ ] **Memory:** what's remembered about you. Review and delete anything you don't want.
- [ ] **Temporary / incognito chats:** know how to start one for sensitive topics.
- [ ] **Connectors & integrations:** which apps are connected, and with what permissions.
- [ ] **Shared links:** any conversations you've shared publicly? Revoke old ones.
- [ ] **Data export & deletion:** how to download or delete everything.
- [ ] **Account security:** strong password, two-factor authentication. 🔑

> [!TIP]
> **🎮 Try this now**
> Ask your assistant: *"Walk me through every privacy setting in this app, one at a time."* Then open settings and do it
> together. Twenty minutes, and you'll know exactly where your data goes.

## 🚦 The traffic-light system: what to share

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

The traffic-light system sorts information by sensitivity: 🟢 general questions are fine to share, 🟡 personal details need care, and 🔴 passwords, ID numbers and confidential data should never be shared, or should only go to local models. The table gives examples.

</details>

| 🟢 Green: share freely | 🟡 Yellow: share with care | 🔴 Red: don't share (or go local) |
|---|---|---|
| General questions and learning | Your own work documents (follow company policy) | Passwords, PINs, 2FA codes |
| Public information | Health questions without identifying details | Full card, bank or ID numbers |
| Your own creative writing | Finances with account numbers redacted | Other people's private information without consent |
| Anonymous or made-up examples | Family details (first names, general situations) | Confidential client or employer data on unapproved tools |
| Code without secrets | Personal journals (consider local models) | Detailed medical records with identifiers |

**Redaction tricks:** replace names with roles ("my manager," "Client A"), mask numbers (`****1234`), crop screenshots, and
remove metadata from photos (location data!). Ask AI to help: *"Here's a doc. List everything I should redact before
sharing it with an AI tool."* (Do this on a local model if the doc is sensitive!)

## 💼 Work data & company policies

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

At work, use only your company's approved AI tools and plans, follow its policies on confidential data, and never paste sensitive work information into personal accounts. The table lists do's and don'ts.

</details>

| Do ✅ | Don't ❌ |
|---|---|
| Use your company's **approved** AI tools and plans | Paste confidential data into personal accounts |
| Read your organization's **AI policy** | Upload customer data without permission |
| Ask IT or legal when unsure | Connect work email to unapproved AI apps |
| Use business plans with admin controls | Assume "it's just a quick question" is harmless |

Business and enterprise plans typically offer **no training on your data**, admin controls, audit logs, data retention settings
and compliance certifications. If your company doesn't have an approved tool, that's worth raising: people use AI anyway, and
safe options beat shadow IT.

## 🔌 Connectors, MCP & permissions

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Connectors give AI access to your email, files and other accounts. Connect only what's needed, prefer read-only access, and remove connections you no longer use. The table explains each principle.

</details>

| Principle | In practice |
|---|---|
| **Least access** | Connect only the folders, calendars or repos needed |
| **Read-only first** | Especially for email and databases |
| **Review regularly** | Remove connectors you don't use |
| **Know who sees it** | Team connectors may expose data to colleagues' AI chats, following existing permissions |
| **Beware prompt injection** | Connected data can contain hostile instructions ([Safety, Costs & Gotchas](103-safety-costs-and-gotchas.md#-prompt-injection-the-1-thing-to-understand)) |

## 🏠 Going local for maximum privacy

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Local models run entirely on your device, so nothing leaves your computer. They're the right choice for journals, health records, financial documents and confidential client data.

</details>

Local models run entirely on your device: **nothing leaves your machine** ([Local & Open Models](../part-9-local-ai/78-local-and-open-models.md)).

| Great for local | Setup |
|---|---|
| 📓 Journals and diaries | Ollama + Obsidian plugins |
| 🩺 Health records and symptom logs | LM Studio or Open WebUI |
| 💰 Detailed financial documents | Local model + local spreadsheet analysis |
| 🧾 Redacting documents before cloud use | A small local model that finds names and numbers |
| 🎙️ Private voice memos | Local Whisper transcription |

**The hybrid pattern:** local model to **redact or summarize** sensitive data → cloud model for **hard reasoning** on the
cleaned version. 🔒➡️☁️

## 👨‍👩‍👧 Kids, family & other people's data

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Take extra care with information about children and other people, who haven't consented to sharing. Avoid uploading identifiable photos of children to unfamiliar tools, and remove other people's personal details from documents.

</details>

- **Kids' photos:** avoid uploading identifiable photos of children to tools you're unsure about.
- **Other people's messages:** get consent before feeding a friend's private messages or voice into AI.
- **Family group chats:** tell people if an AI bot is in the chat ([Chat Apps & Bots](../part-6-ai-in-your-apps/59-chat-apps-and-bots.md#-safety-privacy--etiquette)).
- **Age rules:** many AI apps have minimum ages. Check before setting kids up ([Parents, Teachers & Students](../part-11-ai-for-life-and-work/98-parents-teachers-and-students.md)).
- **Voice and face cloning:** only with explicit consent ([AI Ethics for Builders](107-ai-ethics-for-builders.md)).

## ⚖️ Your rights

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Depending on where you live, privacy laws such as the GDPR and CCPA may give you the right to access, correct and delete your data and to opt out of certain uses. Most providers offer forms or settings for these requests.

</details>

Depending on where you live, privacy laws (such as the GDPR in Europe and state laws like the CCPA in California) may give you
rights to **access**, **correct**, **delete** and **export** your data, and to object to certain uses. Most AI providers offer
data export and deletion in settings or through a privacy request form. *"Help me write a data access request to [company]"*
is a great AI task. ✉️

## 🛠️ Privacy for builders

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

If you build AI applications, collect only the data you need, protect it, explain clearly how it's used and let users delete it. The table describes each principle in practice.

</details>

| Principle | In practice |
|---|---|
| **Collect less** | Only the data you need, for as short a time as possible |
| **Tell people** | A plain-language note on what's sent to AI providers and why |
| **Choose providers carefully** | API and business terms that don't train on your users' data |
| **Protect secrets & data** | Encryption, access controls, env vars, row-level security ([Vibe Coding](../part-7-building-with-ai/65-vibe-coding-your-first-app.md#-step-6-dont-skip-the-safety-basics)) |
| **Scope per user** | Memory and RAG results never leak between users ([Memory for Agents](../part-8-knowledge-and-memory/75-memory-for-agents.md)) |
| **Let users delete** | A clear "delete my data" path |
| **Redact logs** | Don't log full prompts with personal data forever |

## 🎯 Key takeaways

- What you type usually goes to the provider's servers. **Know your settings**: training, history, memory, connectors.
- Use the **traffic-light system**: green freely, yellow with care, red never (or locally).
- **Work data** belongs in **approved** tools only.
- **Least access** for connectors, and review them regularly.
- **Local models** keep the most sensitive data at home, and builders should **collect less and explain more**.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Is it OK to paste a client contract into your personal AI account to summarize it?</summary>

Usually **not** unless your employer and client allow it. Use your organization's **approved** tools and follow its AI policy.

</details>

<details class="quiz">
<summary>❓ 2. Name three "red" items you should never share with a cloud AI.</summary>

Any three of: **passwords/PINs/2FA codes**, **full card/bank/ID numbers**, **others' private information without consent**,
**confidential employer or client data** on unapproved tools, **identifiable medical records**.

</details>

<details class="quiz">
<summary>❓ 3. How can you use a powerful cloud model on sensitive documents more safely?</summary>

**Redact or summarize locally first** (a local model or by hand), then send the cleaned version to the cloud model.

</details>

> [!TIP]
> **🎮 Try this**
> Do the **settings checklist** above in your main AI app today, and turn on a temporary/incognito chat the next time you ask
> something personal. Then ask: *"What do you remember about me?"* and tidy up. Privacy, sorted. 🔒✨

---

**Next:** [105 · Evaluating & Comparing AI →](105-evaluating-ai.md)
