# 34 · A Short, Fun History of Modern AI 📜✨

> ⏱️ 8 min read · 🎯 Everyone · 🧰 Needs: a cozy chair

**AI didn't appear out of nowhere in 2022.** It's a 75-year story of big dreams, "AI winters," surprise breakthroughs, and
one very important research paper. Knowing the story makes today's tools less magical and more understandable, and it
helps you spot hype versus real progress.

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

AI research began in the 1950s and went through cycles of excitement and disappointment for decades. Three developments made modern AI possible: abundant data from the internet, fast GPU computing, and the Transformer architecture introduced in 2017.

- **1950s–1990s:** early ambitions, "AI winters" and rule-based expert systems.
- **2010s:** the deep learning boom, followed by the Transformer.
- **2018–2024:** scaling up models led to ChatGPT and a wave of competing and open models.
- **2025–2026:** the age of agents, where AI uses tools to complete real tasks.

</details>

<!-- in-this-chapter -->

## 🕰️ The whole story on one timeline

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

The timeline below summarizes 75 years of AI history, from Turing's question about thinking machines to today's agents.

</details>

```mermaid
timeline
    title 75 years of thinking machines
    1950s : Turing asks "Can machines think?" (1950)
          : The term "artificial intelligence" is coined at Dartmouth (1956)
          : The Perceptron, an early neural network (1958)
    1960s-80s : ELIZA, the first chatbot (1966)
              : Expert systems boom, then AI winters
              : Backpropagation popularized (1986)
    1990s-2000s : Deep Blue beats Kasparov at chess (1997)
                : The web creates oceans of data
    2010s : AlexNet kicks off the deep learning boom (2012)
          : AlphaGo beats Lee Sedol (2016)
          : "Attention Is All You Need" introduces the Transformer (2017)
          : GPT-1, BERT, GPT-2 (2018-2019)
    2020-2022 : GPT-3 shows few-shot magic (2020)
              : GitHub Copilot, AI pair programming (2021)
              : DALL-E 2, Midjourney, Stable Diffusion (2022)
              : ChatGPT launches (Nov 30, 2022)
    2023-2024 : GPT-4, Claude, Llama and the open-model boom (2023)
              : Multimodal models, reasoning models (2024)
              : Model Context Protocol (MCP) announced (Nov 2024)
    2025-2026 : Agents everywhere, coding agents go mainstream
              : Video with sound, AI music, AI browsers
              : MCP becomes the universal standard
```

## 🌱 The dreamers (1950s–1960s)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

In 1950, Alan Turing proposed the imitation game (later called the Turing test), and the term "artificial intelligence" was coined at a 1956 workshop at Dartmouth. Early researchers were optimistic that human-level AI was close.

</details>

- **1950:** Alan Turing publishes *"Computing Machinery and Intelligence,"* proposing the **imitation game**, later called
  the Turing test: if you can't tell a machine from a human in conversation, does it matter whether it "thinks"?
- **1956:** The **Dartmouth workshop** coins the term *artificial intelligence*. The proposal optimistically suggested that
  significant progress could be made in a single summer.
- **1958:** Frank Rosenblatt's **Perceptron**, a tiny "neural network" inspired by brain cells, learns to recognize simple
  patterns. Newspapers got very excited about machines that would soon walk, talk and be conscious.
- **1966:** Joseph Weizenbaum's **ELIZA** imitates a therapist using simple pattern-matching ("Tell me more about your mother").
  People got emotionally attached to it anyway.

> [!NOTE]
> **🤯 Fun fact: the "ELIZA effect"**
> Weizenbaum was startled that people confided in a program he knew was just shuffling their words back at them. The
> **ELIZA effect**, our tendency to see understanding where there's only pattern-matching, is still worth remembering today.

## ❄️ Winters and expert systems (1970s–1990s)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

When early AI failed to meet expectations, funding collapsed in "AI winters" in the 1970s and late 1980s. Expert systems, which encoded human knowledge as thousands of hand-written rules, had some success but proved brittle and expensive to maintain.

</details>

- **AI winters:** overpromising led to funding cuts in the 1970s and again in the late 1980s.
- **Expert systems** tried to capture human expertise as thousands of hand-written *if-then* rules. They worked in narrow
  areas (like configuring computers or diagnosing infections), but were brittle and expensive to maintain.
- Quietly, the ideas that would win later kept developing: **backpropagation** (how neural networks learn, popularized in
  1986), **LSTMs** (1997, for sequences), and statistical machine learning.
- **1997:** IBM's **Deep Blue** beats world chess champion Garry Kasparov, though mostly through brute-force search rather
  than learning.

**The lesson:** hand-writing intelligence doesn't scale. *Learning* it from data does.

## 🔥 The deep learning boom (2010s)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

In the 2010s, large datasets, GPUs originally built for video games, and better neural network techniques combined to produce dramatic gains in image and speech recognition, starting with AlexNet in 2012.

</details>

The recipe that changed everything: **big data** (the internet) + **big compute** (GPUs built for video games) + **better
neural networks**.

- **2012:** **AlexNet** crushes the ImageNet image-recognition competition using deep neural networks on GPUs. The deep
  learning era begins.
- **2013–2014:** **word2vec** turns words into meaningful vectors (the ancestor of embeddings, see
  [Embeddings & Vector Databases](../part-8-knowledge-and-memory/73-embeddings-and-vector-databases.md)), and **GANs** start generating images.
- **2016:** DeepMind's **AlphaGo** beats Go champion Lee Sedol. Its famous **"move 37"** looked like a mistake to experts
  and turned out to be brilliant: a machine showing something like creativity.
- Speech recognition, translation and photo search quietly get dramatically better in everyday apps.

## ⚡ The Transformer changes everything (2017)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

The Transformer, introduced in the 2017 paper "Attention Is All You Need," uses a mechanism called attention to relate every word in a passage to every other word at once. It trains efficiently on enormous amounts of text and became the foundation of nearly all modern AI models.

</details>

In June 2017, a Google research paper with the delightfully confident title **"Attention Is All You Need"** introduced the
**Transformer**.

Why it mattered:

- **Attention:** every word can "look at" every other word to understand context ("bank" near "river" vs. near "money").
- **Parallelism:** unlike older sequence models, Transformers train efficiently on GPUs at enormous scale.
- **Generality:** the same architecture turned out to work for text, code, images, audio, video, even protein structures.

Nearly every model in this manual, including Claude, GPT, Gemini, Llama and Qwen, is a descendant of that paper.

## 📈 Scale is (almost) all you need (2018–2022)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Researchers found that making Transformers larger and training them on more data steadily improved their abilities, sometimes producing skills no one trained directly. This led from GPT-1 and BERT in 2018 to ChatGPT in late 2022.

</details>

- **2018:** OpenAI's **GPT-1** and Google's **BERT** show that pre-training on lots of text, then adapting, works wonders.
- **2019:** **GPT-2** writes surprisingly coherent paragraphs, and its full release was initially staged over misuse concerns.
- **2020:** **GPT-3** (175 billion parameters) can do new tasks from just a few examples in the prompt ("few-shot
  learning"). **Scaling laws** research shows performance improves predictably with more data, parameters and compute.
- **2021:** **GitHub Copilot** brings AI pair programming to millions of developers, and **DALL-E** generates images from text.
- **2022:** Image generation explodes with **DALL-E 2**, **Midjourney** and the open-source **Stable Diffusion**. Then, on
  **November 30, 2022**, **ChatGPT** launches and becomes one of the fastest-growing consumer apps in history.

> [!NOTE]
> **🤯 Fun fact: the chat interface was the breakthrough**
> The model behind the first ChatGPT wasn't dramatically different from what researchers already had. What changed
> everything was **instruction tuning + human feedback + a friendly chat box**. Sometimes the interface *is* the innovation.

## 🌍 The Cambrian explosion (2023–2024)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

After ChatGPT's release, many companies launched competing models, open-weight models made capable AI freely available, and models gained the ability to process images and audio and to reason step by step.

</details>

- **2023:** **GPT-4** (March) raises the bar. Anthropic launches **Claude**. Meta's **Llama** models kick off an
  **open-weight** boom, and soon anyone can run capable models locally ([Local & Open Models](../part-9-local-ai/78-local-and-open-models.md)).
  Tool use and "plugins" appear. Context windows grow from a few thousand tokens to hundreds of thousands.
- **2024:** **Multimodal** becomes normal (models that see, hear and speak in real time). Claude gets **Artifacts** for
  building interactive things in chat. **Reasoning models** that "think before answering" arrive (OpenAI's o1 in September).
  And in **November 2024**, Anthropic open-sources the **Model Context Protocol**: the USB-C port for AI.

## 🤖 The age of agents (2025–2026)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Since 2025, AI has moved from conversation to action: coding agents that work for hours, browser agents, computer use, video with sound, and thousands of integrations through MCP.

</details>

- **Open reasoning models** (DeepSeek-R1 in January 2025) show frontier-level reasoning can be open-weight and efficient.
- **Coding agents go mainstream:** Claude Code (early 2025), then agents in Cursor, VS Code, Codex and more. Developers
  delegate whole features, and non-developers start **vibe coding** their own apps.
- **New frontier generations** from every major lab: Claude 4 and later, GPT-5, Gemini 3, and rapid-fire updates after.
- **Creative AI levels up:** video models generate **sound and dialogue** together, image models get great at editing and
  text, and AI music becomes genuinely catchy.
- **Agents browse and click:** AI browsers and computer-use agents operate websites for you
  ([Computer Use & Browser Agents](../part-7-building-with-ai/71-computer-use-and-browser-agents.md)).
- **MCP becomes the universal standard:** adopted across ChatGPT, Gemini, Copilot, IDEs and automation tools, with an
  official registry and, in **July 2026**, a stateless spec built for web scale.

## 🧭 What history teaches us

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

History offers three lessons: short-term hype usually overpromises, long-term change is usually underestimated, and progress comes from data, computing power and better methods rather than sudden breakthroughs from nowhere.

</details>

1. **Hype cycles are real.** Every era overpromised in the short term. Be excited, and be skeptical of "next month
   everything changes" claims.
2. **Learning beats hand-coding.** From expert systems to deep learning, the systems that *learn from data* won.
3. **Compute + data + algorithms compound.** Progress came from all three improving together.
4. **Interfaces unlock adoption.** Chat boxes, then tools, then agents: each new interface made the same underlying tech
   far more useful.
5. **The long run is bigger than we expect.** The 1956 dream took ~70 years, and it arrived faster at the end than anyone
   predicted. You're living in the payoff era. 🚀

## 🎯 Key takeaways

- AI is a **75-year story**: early dreams, winters, a deep learning boom, the **Transformer** (2017), scale, and now agents.
- **ChatGPT (2022)** made AI mainstream mostly through a better *interface* (chat + instruction tuning).
- **2024–2026** brought multimodal models, reasoning models, open-weight models, coding agents, and **MCP**.
- History says: stay curious, discount short-term hype, and bet on long-term change.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. What 2017 invention sits inside almost every modern AI model?</summary>

The **Transformer** (from the paper "Attention Is All You Need").

</details>

<details class="quiz">
<summary>❓ 2. Why did expert systems eventually lose out?</summary>

Hand-writing thousands of rules was **brittle and didn't scale**. Systems that *learn* from data generalized far better.

</details>

<details class="quiz">
<summary>❓ 3. What three ingredients fueled the deep learning boom?</summary>

**Big data** (the internet), **big compute** (GPUs), and **better neural network methods**.

</details>

<details class="quiz">
<summary>❓ 4. When was MCP introduced, and why does it matter?</summary>

**November 2024.** It's the open standard that lets any AI app plug into any tool or data source, the foundation for agents
that act.

</details>

> [!TIP]
> **🎮 Try this**
> Ask your AI to role-play ELIZA: *"Pretend to be the 1966 ELIZA program. Only use its simple reflection tricks."* Chat
> for two minutes, then switch: *"Now answer as yourself."* Feeling the 60-year leap firsthand is surprisingly moving. 🤖💜

---

**Next:** [35 · The AI Landscape →](35-the-ai-landscape.md)
