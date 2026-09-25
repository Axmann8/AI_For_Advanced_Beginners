# 79 · Hardware for Local AI: What to Buy (and What Not To) 🖥️⚡

> ⏱️ 8 min read · 🎯 Anyone thinking about running AI at home · 🧰 Needs: nothing (this is a buying and understanding guide)

**The single most important number for local AI isn't your processor speed. It's memory.** How *much* memory decides which
models fit, and how *fast* that memory is decides how quickly they talk. Once you understand those two ideas, the whole
hardware world snaps into focus: why Macs are surprisingly good, why gamers' graphics cards are coveted, and why a used GPU can
beat a brand-new laptop. This chapter explains it all, then gives you budget tiers, a buying checklist and upgrade paths. 🛒

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

An AI model is like a giant book the computer must hold open on its desk while it thinks. **Memory** is the size of the desk:
if the book doesn't fit, it can't be read. **Memory speed** is how fast the computer can flip through the pages: faster
flipping means faster answers. So for local AI, you want a **big desk** and **fast page-flipping**. Everything else matters
much less.

</details>

<!-- in-this-chapter -->

## 🧠 The two numbers that matter

<details class="eli5">
<summary>🧸 ELI5</summary>

How much memory decides which AI brains fit. How fast the memory is decides how fast they answer. That's 90% of what you need
to know.

</details>

| Number | Decides | Rule of thumb |
|---|---|---|
| 📦 **Memory capacity** (VRAM on a GPU, unified memory on a Mac) | **Which models fit** | ~0.6 GB per billion parameters at 4-bit, plus a few GB for context |
| 🚀 **Memory bandwidth** (GB/s) | **How fast it generates** | Tokens per second ≈ bandwidth ÷ model size in GB (roughly) |

**Worked example:** a 14B model at 4-bit is ~9 GB. On memory with ~400 GB/s bandwidth, that's roughly 400 ÷ 9 ≈ **40
tokens/second** at best: comfortably faster than you read. On a laptop with ~100 GB/s, it's closer to **10 tokens/second**:
usable, but you'll wait.

> [!TIP]
> **💡 Why MoE models are a hardware hack**
> Mixture-of-experts models only use a few billion parameters per token. So a "35B-A3B" model needs memory for 35B, but runs
> about as **fast** as a ~3B model. If you have lots of memory but modest bandwidth, MoE models are your best friend
> ([Local & Open Models](78-local-and-open-models.md#-local-ai-jargon-decoded)).

## 🗺️ The hardware landscape

<details class="eli5">
<summary>🧸 ELI5</summary>

There are four main kinds of AI-capable computers: Macs with shared memory, PCs with gaming graphics cards, new mini PCs with
lots of shared memory, and tiny boards for small projects.

</details>

| Kind | Examples | Strengths | Trade-offs |
|---|---|---|---|
| 🍎 **Apple Silicon Macs** | MacBook Pro, Mac mini, Mac Studio (M-series) | **Unified memory** (the GPU can use most of the RAM), quiet, efficient, huge memory options | Slower than top GPUs per GB, memory can't be upgraded later |
| 🎮 **PCs with NVIDIA GPUs** | GeForce RTX cards (8–32 GB VRAM), workstation cards | **Fastest** tokens/second, best software support (CUDA), great for image and video models too | VRAM is limited and expensive, power and noise |
| 🧊 **Unified-memory mini PCs** | AMD Ryzen AI Max ("Strix Halo") boxes, NVIDIA DGX Spark | Up to ~128 GB shared memory in a small box | Middling bandwidth, newer software support |
| 🍓 **Tiny boards** | Raspberry Pi 5, NVIDIA Jetson | Low power, always on, cheap | Tiny models only |
| 💻 **Copilot+ / NPU laptops** | Laptops with neural processing units | Great battery life for built-in AI features | NPUs are rarely used by local LLM tools (yet) |

## 🍎 Macs: the surprise champions

<details class="eli5">
<summary>🧸 ELI5</summary>

Macs share one big pool of memory between everything, so they can hold much bigger AI brains than most computers of the same
price.

</details>

Apple Silicon Macs use **unified memory**: the CPU and GPU share one big, fast pool. That means a Mac with 64 GB can load models
that would need a very expensive GPU on a PC.

| Mac memory | What fits well |
|---|---|
| 16 GB | 7–12B models (plus your other apps) |
| 24–36 GB | 14–27B models |
| 48–64 GB | 30–35B models, including big MoE models, with room for long context |
| 96–128 GB | 70B-class and ~100B+ MoE models |
| 192 GB+ (Mac Studio) | The largest open models (heavily quantized) |

**Mac tips:** Pro/Max/Ultra chips have **much higher bandwidth** than base chips (faster generation). Use **MLX** builds of
models (LM Studio and Ollama support them) for extra speed. Buy more memory than you think you need, because you can't add it
later.

## 🎮 NVIDIA GPUs: the speed kings

<details class="eli5">
<summary>🧸 ELI5</summary>

Gaming graphics cards are super fast at AI math. The catch is their memory is small, so pick the card with the most memory you
can afford.

</details>

| VRAM | Typical cards | What fits |
|---|---|---|
| 8 GB | Entry gaming cards | 3–8B models, image generation (SDXL-class) |
| 12–16 GB | Mid-range RTX cards | 12–14B models fast, most image models |
| 24 GB | High-end cards (including popular **used** RTX 3090s) | ~30B models, big image and video models |
| 32 GB | Flagship consumer cards | 30B+ comfortably, long context |
| 48 GB+ | Two cards, or workstation cards | 70B-class models |

**GPU tips:**

- **VRAM beats speed.** A card with more VRAM that's a bit slower usually wins for LLMs.
- **Used 24 GB cards** are a classic value pick for local AI.
- **Two GPUs can split a model** (Ollama, llama.cpp and vLLM support this), but it's more complex.
- **Image and video generation** (Stable Diffusion, Flux, video models) are much happier on NVIDIA than elsewhere
  ([Image Generation](../part-10-creative-ai/84-image-generation-deep-dive.md)).
- Check your **power supply and case size** before buying a big card. 🔌

## 🧊 Unified-memory mini PCs

<details class="eli5">
<summary>🧸 ELI5</summary>

A newer kind of small computer has a huge shared memory pool like a Mac, so it can hold big AI brains in a box the size of a
lunchbox.

</details>

Mini PCs built on chips like **AMD's Ryzen AI Max** series and **NVIDIA's DGX Spark** offer up to ~128 GB of memory the GPU can
use, in a compact box.

- **Great for:** big MoE models, always-on home AI servers, experimenting with 70B-class models.
- **Less great for:** raw speed on dense models (bandwidth is lower than top GPUs).
- **Check:** software support for your favorite tools (it's improving quickly).

## 💰 Budget tiers

<details class="eli5">
<summary>🧸 ELI5</summary>

You don't need to spend a lot. Start with the computer you already have, and only buy something new when you know exactly
what you want it for.

</details>

| Tier | Setup | You get |
|---|---|---|
| 🆓 **$0** | Whatever you own + small models, or free cloud tiers | Learning, summaries, simple automations |
| 💵 **Budget** | A used office mini PC or Raspberry Pi 5 as an **always-on** box | n8n, databases, tiny models, calls cloud AI for the hard stuff |
| 💵💵 **Mid** | A 16–24 GB GPU in an existing PC, or a Mac with 32–48 GB | 14–30B models, image generation, private coding help |
| 💵💵💵 **Enthusiast** | A Mac with 64–128 GB, a 32 GB GPU, or a 128 GB mini PC | 30–120B models, long contexts, a serious home lab |
| 💵💵💵💵 **Wild** | Multi-GPU rigs or a maxed-out Mac Studio | The biggest open models at home 🦖 |

> [!NOTE]
> **📌 Cloud might be cheaper**
> For occasional big-model use, renting a cloud GPU by the hour or using hosted open models can cost far less than buying
> hardware. Buy when you'll use it **every day**, or when privacy truly requires it.

## ✅ The buying checklist

<details class="eli5">
<summary>🧸 ELI5</summary>

Before you buy, answer these questions so you get the right computer and don't waste money.

</details>

- [ ] **What will you run?** Chat, coding, images, video, or an always-on server?
- [ ] **Which model size do you want?** Use the ~0.6 GB per billion parameters rule, then add 20–30% headroom.
- [ ] **Memory first:** the most VRAM or unified memory you can afford.
- [ ] **Bandwidth second:** Pro/Max/Ultra Macs and higher-end GPUs are much faster.
- [ ] **Software support:** NVIDIA is the safest bet, and Apple is excellent for LLMs.
- [ ] **Noise, heat and power:** is it going in your bedroom? 😴
- [ ] **Always-on?** Low idle power matters for a 24/7 home server.
- [ ] **Upgrade path:** can you add a GPU or more storage later?
- [ ] **Try before you buy:** test the model size you want on a cloud GPU or hosted API first.

Or ask your assistant: *"My budget is X, I want to run Y for Z. Here are 3 machines I'm considering [links]. Which fits best,
and what am I missing?"*

## 🗄️ Storage, power & the boring-but-important bits

<details class="eli5">
<summary>🧸 ELI5</summary>

AI brains are big files, so you need lots of storage space. And computers that run all day use electricity, so efficient ones
save money.

</details>

| Thing | Guidance |
|---|---|
| **Storage** | Models are 2–80+ GB each. A fast 1–2 TB SSD fills up faster than you'd think |
| **System RAM (PC)** | 32 GB+ so the rest of your computer stays happy |
| **Power** | Big GPUs draw lots of power under load. Macs and mini PCs sip it |
| **Cooling & noise** | Sustained AI work runs hot. Good airflow = stable speeds |
| **Networking** | Wired Ethernet for a home server, and Tailscale for remote access ([Home Lab](80-home-lab.md)) |

## 🔭 Where hardware is heading

<details class="eli5">
<summary>🧸 ELI5</summary>

Computers are quickly getting better at AI, and AI brains are getting smaller and smarter, so the same computer can do more
every year.

</details>

- **Smarter small models:** each generation packs more capability into fewer parameters, so your existing machine gets
  "upgraded" for free every few months. 🎁
- **More unified memory everywhere:** big shared-memory designs are spreading beyond Apple.
- **NPUs growing up:** laptop neural processors are slowly gaining support in local AI tools.
- **Efficient formats:** new quantization formats keep squeezing models smaller with less quality loss.

## 🎯 Key takeaways

- **Memory capacity decides which models fit. Memory bandwidth decides how fast they run.**
- ~**0.6 GB per billion parameters** at 4-bit, plus headroom for context.
- **Macs** shine for big models thanks to unified memory. **NVIDIA GPUs** shine for speed and image/video.
- **MoE models** give big-model smarts at small-model speed if you have the memory.
- Start with **what you own**, try big models in the cloud, and buy for **daily** use.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. About how much memory does a 30B model need at 4-bit quantization?</summary>

Roughly **18 GB** (30 × 0.6), plus a few GB for context: so a **24 GB** GPU or a **32 GB+** Mac.

</details>

<details class="quiz">
<summary>❓ 2. Two machines have the same memory size, but one has 3× the bandwidth. What changes?</summary>

The higher-bandwidth machine generates text roughly **3× faster**. The same models fit on both.

</details>

<details class="quiz">
<summary>❓ 3. You want to generate lots of images and videos locally. Mac or NVIDIA GPU?</summary>

Usually an **NVIDIA GPU**: image and video tools have the best support and speed there.

</details>

> [!TIP]
> **🎮 Try this**
> Find your computer's memory (and GPU VRAM if you have one). Use the 0.6 GB rule to work out the biggest model you can run,
> then pull one just under that size in Ollama or LM Studio and time how many tokens per second you get. Now you *know* your
> machine's AI power level. ⚡

---

**Next:** [80 · The AI Home Lab →](80-home-lab.md)
