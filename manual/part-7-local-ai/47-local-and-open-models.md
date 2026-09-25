# 47 · Local & Open Models: AI on Your Own Machine 🏠💻

> ⏱️ 8 min read · 🎯 Everyone (one command to start) · 🧰 Needs: a laptop or desktop with 8 GB+ RAM, and Ollama or LM Studio

**Yes, you can run surprisingly capable AI entirely on your laptop: offline, private, and free per use.** Open-weight models
have improved at a startling pace, and a mid-range computer now runs assistants that would have seemed like frontier
magic a couple of years ago. This chapter explains why you'd go local, the tools, the model families, what your computer can
handle, the jargon (quantization, MoE, GGUF), and a pile of fun projects. It's one of the most *fun* rabbit holes in AI. 🐇

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Most AI lives in giant computers far away, and you "call" it over the internet. But smaller AI brains can now live **right
on your own computer**, like having a pet robot at home instead of phoning one. It works with the Wi-Fi off, nobody else sees
what you ask it, and it's free to use as much as you like. It's not quite as clever as the giant ones, but it's clever
enough for loads of everyday jobs.

</details>

<!-- in-this-chapter -->

## 🤔 Why go local?

<details class="eli5">
<summary>🧸 ELI5</summary>

Local AI is great for secrets, for places without internet, and for doing the same job thousands of times for free. For the
very hardest problems, the big online AIs are still smarter.

</details>

| 👍 Great for | 👎 Not great for |
|---|---|
| 🔐 **Privacy** (journals, medical, client data) | The hardest reasoning and big coding tasks |
| ✈️ **Offline** use (flights, cabins, bad Wi-Fi) | Very long documents on small machines |
| ♾️ **Unlimited experimentation** at no per-use cost | Speed on older hardware |
| 🏭 **Batch jobs** (tag 10,000 photos) | "It just works" convenience |
| 🎓 **Learning** how LLMs actually work | Web search and tools out of the box (needs setup) |
| 🎛️ **Control** (pick the model, no surprise changes) | |

> [!TIP]
> **💡 The sweet spot: hybrid**
> Use frontier models (Claude and friends) for hard thinking. Use local models for private, repetitive or high-volume grunt
> work. Many tools (Open WebUI, n8n, Cline) let you mix both in one place.

## 🚀 Your first local model in 5 minutes

<details class="eli5">
<summary>🧸 ELI5</summary>

Install one free app, type one command, and you're chatting with an AI that lives on your computer.

</details>

=== "🦙 Ollama (terminal)"

    ```bash
    # install from ollama.com (Mac, Windows, Linux), then:
    ollama run gemma4          # downloads once, then chats in your terminal
    ```

    Useful commands:

    ```bash
    ollama list                # installed models
    ollama pull qwen3.6:27b    # download another model
    ollama ps                  # what's loaded right now
    ollama rm <model>          # free up disk space
    ```

=== "🖥️ LM Studio (app)"

    1. Download **LM Studio** from lmstudio.ai.
    2. Open the **Discover** tab and search for a model (e.g. "Gemma" or "Qwen"). It shows which sizes fit your machine.
    3. Click **Download**, then chat in the **Chat** tab.
    4. Optional: start the **local server** so other apps can use it.

Ask it something, then **turn off your Wi-Fi and ask again**. It still works. 🤯

## 🧰 The toolkit

<details class="eli5">
<summary>🧸 ELI5</summary>

There are free apps for running local AI: some are for the terminal, some are pretty desktop apps, and some make your own
private ChatGPT-style website.

</details>

| Tool | What it is | Vibe |
|---|---|---|
| **[Ollama](https://ollama.com)** | Command-line model runner with an OpenAI-compatible API | `ollama run gemma4` and you're chatting. The standard |
| **[LM Studio](https://lmstudio.ai)** | Beautiful desktop app: browse, download, chat, local API server, MCP support | Easiest for non-terminal folks |
| **[Jan](https://jan.ai)** | Open-source ChatGPT-style desktop app, local-first | Privacy-focused and clean |
| **[Open WebUI](https://openwebui.com)** | Self-hosted ChatGPT-like web UI with RAG, tools and multiple users | Your own private ChatGPT ([Home Lab](49-home-lab.md)) |
| **[llama.cpp](https://github.com/ggml-org/llama.cpp)** | The C++ engine under much of this | Max control for tinkerers |
| **MLX / mlx-lm** | Apple's framework, very fast on Apple Silicon | Mac power users |
| **vLLM / SGLang** | High-throughput serving on GPUs | Serving a team |
| **AnythingLLM, Msty, GPT4All** | Friendly desktop apps (AnythingLLM does great document chat) | Try a few! |

## 🌍 Open model families to know

<details class="eli5">
<summary>🧸 ELI5</summary>

Different companies share AI brains for anyone to download. Each family has different strengths, and new versions come out
all the time.

</details>

| Family | From | Known for |
|---|---|---|
| **Gemma** | Google | Excellent small and mid-size models, vision, many languages |
| **Qwen** | Alibaba | Strong all-rounders and coding models (Qwen-Coder), many sizes |
| **DeepSeek** | DeepSeek | Strong reasoning and big mixture-of-experts models |
| **Llama** | Meta | The family that kicked off the open-model boom |
| **gpt-oss** | OpenAI | Open-weight reasoning models under a permissive license |
| **Mistral** | Mistral AI | Efficient European models, strong small ones |
| **Phi** | Microsoft | Tiny models that punch above their weight |
| **Nemotron** | NVIDIA | Models tuned for reasoning and agents |
| **Kimi, GLM, MiniMax** | Moonshot, Zhipu, MiniMax | Big, capable models popular for agentic coding |

> [!NOTE]
> **📌 Names move fast**
> At the time of writing, popular local picks include **Gemma 4**, the **Qwen 3.5/3.6** generation, **gpt-oss**,
> **DeepSeek-V4** and **Qwen3-Coder** models. By the time you read this there may be newer ones. Check the
> [Ollama library](https://ollama.com/library), LM Studio's Discover tab, and Hugging Face trending pages.

## 💻 What can my computer run?

<details class="eli5">
<summary>🧸 ELI5</summary>

Bigger AI brains need more memory. A normal laptop runs small brains well. A computer with lots of memory or a gaming graphics
card runs bigger, smarter ones.

</details>

**The rule of thumb:** a model needs roughly **its size in GB of memory** (RAM on a Mac, VRAM on a GPU), plus a bit extra for
the conversation. Quantized to 4 bits, that's about **0.6 GB per billion parameters**.

| Your machine | Comfortable models | Feels like |
|---|---|---|
| 8 GB RAM laptop | 1–4B (e.g. small Gemma, Phi, Qwen) | Quick helper: summaries, rewriting, classification |
| 16 GB RAM / Apple M-series | 7–14B (e.g. `gemma4:12b`) | Solid chat, decent coding help |
| 32–64 GB Mac or 24 GB GPU | 20–35B, including MoE models (e.g. `gemma4:26b`, `qwen3.6:35b`) | Genuinely impressive |
| 128 GB+ Mac or multi-GPU | 70–120B+ (e.g. `gpt-oss:120b`) | Near-frontier on many tasks |

Buying guide in [Hardware for Local AI](48-hardware-for-local-ai.md).

## 📖 Local AI jargon, decoded

<details class="eli5">
<summary>🧸 ELI5</summary>

A few funny words you'll see everywhere: "quantized" means squished to fit, "MoE" means a team of mini-experts where only a few
work at a time, and "GGUF" is just the file type.

</details>

| Term | Plain English |
|---|---|
| **Parameters (7B, 70B)** | The number of "knobs" in the model. Bigger is usually smarter and hungrier |
| **Open-weight** | You can download and run the model. (Fully "open source" also shares training data and code, which is rarer) |
| **Quantization** (Q4, Q5, Q8) | Storing the knobs with fewer bits to shrink the model. **Q4_K_M** is the usual sweet spot |
| **GGUF** | The file format used by llama.cpp, Ollama and LM Studio |
| **MLX** | Apple's format and framework for fast Mac inference |
| **MoE** (mixture of experts, e.g. "35B-A3B") | A big model where only a few "experts" (here ~3B parameters) work per token: big-model smarts, small-model speed |
| **Context length** | How much text it can consider at once. Longer context uses more memory |
| **Tokens per second** | Speed. ~10+ feels comfortable for reading along |
| **License** | What you're allowed to do (Apache 2.0 and MIT are permissive, others have conditions). Check before commercial use |

## 🔌 Using local models from other apps

<details class="eli5">
<summary>🧸 ELI5</summary>

Your local AI can be plugged into other apps, like your note-taking app, your automations or your code editor, so they use
your home robot instead of an online one.

</details>

Ollama and LM Studio expose an **OpenAI-compatible API** on your machine, so most tools that speak "OpenAI" can use them:

```python
# pip install openai
from openai import OpenAI

local = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")   # key is ignored
reply = local.chat.completions.create(
    model="gemma4",
    messages=[{"role": "user", "content": "Give me 3 cozy dinner ideas with lentils."}],
)
print(reply.choices[0].message.content)
```

| Plug into… | How |
|---|---|
| **n8n** | Ollama Chat Model node → AI Agent (free, unlimited automations) |
| **Obsidian** | Copilot or Smart Connections plugin pointed at Ollama ([Obsidian & AI](../part-4-ai-in-your-apps/25-obsidian-and-ai.md)) |
| **Code editors** | Cline, Continue, Roo Code, Zed or Aider with a local model ([Local AI for Coding](50-local-ai-for-coding-and-agents.md)) |
| **Open WebUI** | Point it at Ollama for a private ChatGPT |
| **Your scripts** | The OpenAI SDK with `base_url` set, as above |
| **Embeddings** | `ollama pull nomic-embed-text` for local RAG ([Embeddings & Vector Databases](../part-6-knowledge-and-memory/42-embeddings-and-vector-databases.md)) |

## 🔀 Open models in the cloud

<details class="eli5">
<summary>🧸 ELI5</summary>

You can also use these open AI brains on fast online computers, which is handy if your own computer is too small.

</details>

- **[OpenRouter](https://openrouter.ai):** one API key, hundreds of models (open and closed), great for comparing.
- **Groq, Cerebras, Together, Fireworks:** very fast hosted open models.
- **Hugging Face Inference Providers:** run models from the Hub without managing servers.
- **Ollama's cloud models:** some models have `:cloud` tags that run on Ollama's servers with the same commands.

Handy for trying a big model before buying hardware for it. (Remember: cloud means your data leaves your machine.)

## 🎮 Fun local projects

<details class="eli5">
<summary>🧸 ELI5</summary>

Ten fun things to do with an AI that lives on your own computer.

</details>

| # | Project | Why local shines |
|---|---|---|
| 1 | 📓 **Private journal analyst:** find mood patterns in your journal | Nothing leaves your machine |
| 2 | 📸 **Photo tagger:** a vision model captions and tags your photo library | Thousands of images, zero cost |
| 3 | ⚙️ **Local agent in n8n** for free, unlimited automations | No per-call bills |
| 4 | 💻 **Offline coding buddy** in Cline, Continue or Aider | Works on a plane |
| 5 | 🥊 **Model battle:** the same 10 prompts through 3 local models and a frontier model, scored blind | Builds real intuition |
| 6 | 🎙️ **Voice notes → summaries** with Whisper + a local model | Private meetings and memos |
| 7 | 🧾 **Receipt extractor** from scanned PDFs | Sensitive finances stay home |
| 8 | 🗂️ **File renamer:** "rename these 500 PDFs by their content" | Bulk work for free |
| 9 | 🌍 **Offline translator** for travel | No roaming data needed |
| 10 | 🧒 **Kid-safe story generator** on a family computer | You control the model and settings |

## 🎯 Key takeaways

- Local AI is **private, offline and free per use**, and good enough for loads of everyday jobs.
- **Ollama** (terminal) and **LM Studio** (app) get you running in minutes.
- Pick models by **memory first, task second**. Q4 quantization and **MoE** models stretch your hardware.
- Local models speak the **OpenAI-compatible API**, so n8n, Obsidian, editors and scripts can use them.
- Go **hybrid**: local for private and bulk work, frontier models for the hardest thinking.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. You have a 16 GB laptop. Roughly what size model runs comfortably?</summary>

Around **7–14B parameters** (quantized to ~4 bits).

</details>

<details class="quiz">
<summary>❓ 2. What does "35B-A3B" mean for a mixture-of-experts model?</summary>

It has **35B total parameters**, but only about **3B are active** for each token, so it runs much faster than a dense 35B model
(though it still needs memory for all 35B).

</details>

<details class="quiz">
<summary>❓ 3. How can n8n or a Python script use your local model?</summary>

Through Ollama's or LM Studio's **OpenAI-compatible API** (e.g. `http://localhost:11434/v1`), or n8n's Ollama nodes.

</details>

> [!TIP]
> **🎮 Try this**
> Install Ollama, run `ollama run gemma4`, and ask it to *"write a haiku about my Wi-Fi being off."* Then turn your Wi-Fi off
> and ask again. 📴 Next, try a model battle: the same three questions to `gemma4` and Claude. Where's the gap? Where isn't there
> one? That's your local-AI intuition forming.

---

**Next:** [48 · Hardware for Local AI →](48-hardware-for-local-ai.md)
