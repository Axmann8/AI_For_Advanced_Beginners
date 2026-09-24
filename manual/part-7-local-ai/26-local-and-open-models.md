# 26 · Local & Open Models: AI on Your Own Machine 🏠💻

Yes, you can run surprisingly capable AI **entirely on your laptop**: offline, private, and free per use.
It's also one of the most *fun* rabbit holes in AI.

---

## Why go local?
| 👍 Great for | 👎 Not great for |
|---|---|
| Privacy (journals, medical, client data) | Frontier-level reasoning and hard coding tasks |
| Offline use (flights, cabins) | Very long documents on small machines |
| Unlimited cheap experimentation | Speed on older hardware |
| Batch jobs (tag 10,000 photos) | "It just works" convenience |
| Learning how LLMs actually work | |

**The sweet spot:** Use frontier models (Claude, and others) for hard thinking. Use local models for
private, repetitive, or high-volume grunt work.

## The toolkit
| Tool | What it is | Vibe |
|---|---|---|
| **[Ollama](https://ollama.com)** | Command-line model runner with an OpenAI-compatible API | `ollama run llama3.2` and you're chatting. The standard. |
| **[LM Studio](https://lmstudio.ai)** | Beautiful desktop app: browse, download, and chat, plus a local API server and MCP support | Easiest for non-terminal folks |
| **[Jan](https://jan.ai)** | Open-source ChatGPT-style desktop app, local-first | Privacy-focused and clean |
| **[Open WebUI](https://openwebui.com)** | Self-hosted ChatGPT-like web UI for Ollama and APIs, with RAG, tools, and multi-user support | Your own private ChatGPT |
| **[llama.cpp](https://github.com/ggml-org/llama.cpp)** | The engine under much of this, in C++ | For tinkerers who want max control |
| **MLX / mlx-lm** | Apple's framework, very fast on Apple Silicon | Mac power users |
| **vLLM / SGLang** | High-throughput serving on GPUs | When you're serving a team |
| **GPT4All, Msty, AnythingLLM** | More friendly desktop options (AnythingLLM does great doc chat) | Try a few! |

## Open model families to know
Names and versions move *fast*. Check the [Hugging Face](https://huggingface.co/models) trending page
and leaderboards for the current best. Families to watch: **Llama** (Meta), **Qwen** (Alibaba, very
strong at coding), **DeepSeek** (strong reasoning), **Gemma** (Google, great small models),
**Mistral**, **Phi** (Microsoft, tiny and capable), **gpt-oss** (OpenAI's open-weight models), **Kimi**,
and **GLM**.

## What can my computer run? (rough guide)
| Your machine | Comfortable model size | Feels like |
|---|---|---|
| 8 GB RAM laptop | 1–4B params | Quick helper, summaries, classification |
| 16 GB RAM / Apple M-series | 7–14B | Solid chat, decent coding help |
| 32–64 GB Mac or 24 GB GPU | 20–35B | Genuinely impressive |
| 128 GB+ / multi-GPU | 70B+ | Near-frontier on many tasks |

**Quantization** (Q4, Q5, Q8) shrinks models to fit. **Q4_K_M** is the usual sweet spot of quality versus size.

## 🔀 Access to lots of models through one API
- **[OpenRouter](https://openrouter.ai)**: one API key, hundreds of models (open and closed). Great for comparing models.
- **Groq, Together, Fireworks, Cerebras**: very fast hosted open models.
- **Hugging Face Inference Providers**: run models from the Hub without managing servers.

## Fun local projects 🎮
1. **Private journal analyst:** Ollama + a script that reads your journal and finds mood patterns. Nothing leaves your machine.
2. **Photo tagger:** a local vision model captions and tags your whole photo library.
3. **Local agent in n8n:** point n8n's AI Agent at Ollama for free, unlimited automations.
4. **Offline coding buddy:** hook Ollama or LM Studio into Cline, Continue, or Aider.
5. **Model battle:** run the same 10 prompts through 3 local models and a frontier model, then score them blind.

---

### 🚀 Try this next
```bash
# install from ollama.com, then:
ollama run gemma3        # or llama3.2, qwen3, phi4-mini: whatever's current and fits your RAM
```
Ask it something, then turn off your Wi-Fi and ask again. It still works. 🤯

**Next:** [27 · The AI Home Lab →](27-home-lab.md)
