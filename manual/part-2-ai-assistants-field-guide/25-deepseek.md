# 25 · DeepSeek: The Complete Guide 🐋

> ⏱️ 5 min read · 🎯 Curious beginners and budget-minded users · 🧰 Needs: a free DeepSeek account (chat.deepseek.com) or a local AI setup

**DeepSeek shook the AI world in January 2025, when a small Chinese lab released a free reasoning model that rivaled the
best in the West, and published it openly for anyone to download.** Today DeepSeek offers a capable, completely free
chat app with a "DeepThink" reasoning mode, plus open-weight models you can run yourself. It's also the assistant where
you most need to think about privacy. Here's how to use it wisely.

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

DeepSeek is a free AI from a company in China. It's really good at thinking through problems, and it shows you its
thinking. The company also shares its AI "brains" so anyone can use them. But the app stores your chats in China, so use
it for general questions, not your private information.

</details>

<!-- in-this-chapter -->

## 🐋 Quick facts

<details class="eli5">
<summary>🧸 ELI5</summary>

The basics: who makes DeepSeek, where you can use it and what it's best at.

</details>

| | |
|---|---|
| **Made by** | DeepSeek, an AI lab in Hangzhou, China |
| **Where** | chat.deepseek.com · iPhone/Android apps · open models on Hugging Face (run locally or through other providers) |
| **Free?** | Yes, the chat app is free |
| **Best at** | Step-by-step reasoning, math, coding, long documents; transparent "thinking" |
| **Brains** | The **DeepSeek-V4** family (V4 and V4-Pro, previewed in April 2026 and fully released in August 2026) |
| **Watch out for** | **Data stored in China**; restricted on government devices in several countries; avoids topics sensitive to the Chinese government |

## 🚪 Getting started

<details class="eli5">
<summary>🧸 ELI5</summary>

Go to the DeepSeek website or app, sign up, and switch on DeepThink when you have a hard question.

</details>

1. Go to **chat.deepseek.com** or install **DeepSeek** (check the developer is DeepSeek).
2. Sign up with email (or a supported sign-in option).
3. Use the toggles under the message box:
   - 🧠 **DeepThink:** turns on reasoning mode for harder problems (you'll see its thinking).
   - 🌐 **Search:** lets it search the web for current information.
4. Upload files (PDFs, documents, images with text) with the 📎 button.

## 🧠 DeepThink: watch it reason

<details class="eli5">
<summary>🧸 ELI5</summary>

When DeepThink is on, DeepSeek thinks out loud before answering, so you can see how it worked the problem out.

</details>

DeepSeek's reasoning mode shows its **chain of thought**: you can expand the "thinking" and read how it approached the
problem. That's genuinely educational:

- 🧮 *"A train leaves at 3:40 and arrives at 7:15 with a 25-minute stop. How long is it actually moving?"*
- 🧩 *"Help me plan a seating chart for 24 wedding guests with these constraints: [list]."*
- 💻 *"Why does this spreadsheet formula return an error? Walk through it."*

Reading the reasoning helps you **spot where it went wrong** if the answer seems off.

## 🔓 Open weights: DeepSeek beyond the app

<details class="eli5">
<summary>🧸 ELI5</summary>

DeepSeek lets anyone download its AI brains. That means other companies can run them, and you can even run smaller
versions on your own computer, where nothing leaves your home.

</details>

DeepSeek publishes its models openly (under a permissive license). That has big benefits:

- **Other providers host them:** you can use DeepSeek models through services in your own country (and hub apps like
  [Poe or HuggingChat](29-hubs-and-specialty-chatbots.md)), so your data isn't sent to DeepSeek's servers.
- **Run it yourself:** smaller "distilled" versions run on a good laptop or home PC with tools like **Ollama** or **LM
  Studio**. Fully private. See [Local & Open Models](../part-9-local-ai/78-local-and-open-models.md).
- **Developers:** DeepSeek's own API is very cheap, and the models are popular for building apps and agents.

## 🔐 Privacy: the important bit

<details class="eli5">
<summary>🧸 ELI5</summary>

The DeepSeek app keeps your chats on computers in China, where the government can ask for data. So don't put private or
work information into it.

</details>

DeepSeek's app and website store data on servers in the **People's Republic of China**, where companies can be required
to share data with authorities. Several governments have restricted DeepSeek on official devices, and some regulators
have investigated its data practices.

**Sensible rules:**

- ✅ Fine for: general knowledge, math, coding practice, learning, brainstorming.
- 🚫 Avoid: personal documents, health or financial details, work secrets, anything about other people.
- 🏠 Want DeepSeek's brains *with* privacy? Use the **open model locally** or through a trusted provider in your
  country.
- Check your **employer's or school's policy** before using it for work or study.

## 🧭 Content limits to know about

<details class="eli5">
<summary>🧸 ELI5</summary>

DeepSeek won't talk about some topics the Chinese government considers sensitive, so for those questions, use a
different AI.

</details>

Because it operates under Chinese regulations, DeepSeek's app **avoids or deflects questions on topics sensitive to the
Chinese government** (certain historical events, political figures, territorial questions). For history, politics or
current affairs involving China, use another assistant and multiple sources. (Open models run elsewhere can behave
somewhat differently, but still reflect their training.)

## 🍳 Step-by-step recipes

<details class="eli5">
<summary>🧸 ELI5</summary>

Three good jobs for DeepSeek today.

</details>

**Recipe 1: Learn math the transparent way**

1. DeepThink **on** → *"Explain how compound interest works, then calculate what $5,000 becomes after 10 years at 4%
   compounded monthly."*
2. Expand the thinking and follow each step.

**Recipe 2: Coding help for beginners**

1. *"I'm learning Python. Explain what this code does line by line and suggest one improvement: [paste code]."*

**Recipe 3: Compare it privately**

1. Install **Ollama**, run a small DeepSeek-based model, and ask it the same reasoning question offline. Compare with the
   app. (Guide: [Local & Open Models](../part-9-local-ai/78-local-and-open-models.md).)

## 💡 Pro tips and limitations

<details class="eli5">
<summary>🧸 ELI5</summary>

Clever tricks DeepSeek fans know, and the things to watch out for.

</details>

**Pro tips**

- 🧠 **DeepThink for logic, off for chat:** reasoning mode is slower; you don't need it for simple questions.
- 🌐 **Turn on Search** for anything recent.
- 📄 **Long documents:** the newest models handle very long inputs well.

**Limitations**

- **Privacy and jurisdiction** concerns (above).
- **Fewer features** than the big Western assistants: limited voice, no image generation, no memory, fewer integrations.
- **Busy periods** can bring "server busy" errors.

## 🎯 Key takeaways

- DeepSeek offers a **free, capable** assistant with a transparent **DeepThink** reasoning mode.
- Its **open-weight models** can run **locally** or via other providers, which is the private way to use them.
- The app stores data **in China**: keep personal and work information out.
- It **avoids topics sensitive to the Chinese government**; use other sources for those.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. What's the most private way to use DeepSeek's models?</summary>

Run an **open DeepSeek model locally** (for example with Ollama) or through a trusted provider in your own country.

</details>

<details class="quiz">
<summary>❓ 2. Is DeepSeek's app a good place to paste your medical test results?</summary>

No. Its data is stored in **China**. Use it for general questions and keep sensitive information out.

</details>

<details class="quiz">
<summary>❓ 3. What does DeepThink do?</summary>

Turns on **reasoning mode**: DeepSeek works through the problem step by step and shows its thinking before answering.

</details>

> [!TIP]
> **🎮 Try this**
> Give DeepSeek (DeepThink on) and one other assistant the same logic puzzle: *"Three friends split a $96 bill. One paid
> $40, one paid $36 and one paid $20. Who owes whom, and how much?"* Read DeepSeek's thinking. Did both get it right? 🧮

---

**Next:** [26 · Mistral Le Chat →](26-mistral-le-chat.md)
