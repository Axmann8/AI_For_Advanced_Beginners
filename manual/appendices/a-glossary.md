# 📖 Glossary

Quick, plain-English definitions for the jargon in this guide.

| Term | Meaning |
|---|---|
| **Agent** | An AI system that works in a loop (think → use a tool → look at the result → repeat) until a goal is done. |
| **Agent loop** | That think/act/observe cycle. See [Ch. 1](../part-1-foundations/01-the-mental-model.md). |
| **AGENTS.md / CLAUDE.md** | A Markdown file in a project that agents read automatically as standing instructions. |
| **API** | A way for programs to talk to each other. AI APIs charge per token. |
| **Artifact** | A generated, often interactive, piece of content (an app, doc, or chart) displayed alongside a Claude chat. |
| **Chunking** | Splitting documents into passages before embedding them for RAG. |
| **Computer use** | AI controlling a mouse, keyboard, and screen (or a browser) like a human would. |
| **Connector** | A ready-made integration in an AI app (often MCP under the hood) that links it to a service like Gmail. |
| **Context window** | How much text (in tokens) a model can consider at once. It's the model's working memory. |
| **Elicitation** | An MCP feature where a server asks *you* a question mid-task. |
| **Embedding** | A list of numbers that represents the meaning of text. Similar meanings get similar numbers. |
| **Fine-tuning** | Further training a model on your examples. Usually *not* needed. Try RAG and prompting first. |
| **Function calling / tool use** | The model outputting a structured request to run a tool, which your software executes. |
| **Hallucination** | The model confidently stating something false. Grounding and verification reduce it. |
| **Hook** | An automatic script that runs on agent events (e.g. "after each file edit, run the formatter"). |
| **Host / client / server (MCP)** | Host = the AI app. Client = its connection manager. Server = the program exposing tools and data. |
| **Human-in-the-loop** | A step where a person approves or edits before the AI's output is used. |
| **Inference** | Running a model to get output (as opposed to training it). |
| **MCP (Model Context Protocol)** | The open standard for connecting AI apps to tools and data. See [Ch. 4](../part-2-mcp-and-connectors/04-mcp-explained.md). |
| **MCP Apps** | An MCP extension that lets servers show interactive UI inside the chat. |
| **Multimodal** | Handling more than text: images, audio, video. |
| **Node (n8n/Make)** | One step in a visual workflow. |
| **OAuth** | The "Log in with…" flow that grants an app limited access without sharing your password. |
| **Open-weight model** | A model whose weights you can download and run yourself (Llama, Qwen, Gemma, and others). |
| **Plugin** | A bundle of connectors/MCP servers, skills, and commands you can install at once. |
| **Prompt caching** | Reusing processed prompt prefixes to make repeated calls cheaper and faster. |
| **Prompt injection** | Malicious instructions hidden in content the AI reads. See [Ch. 37](../part-10-mastery/37-safety-costs-and-gotchas.md). |
| **Quantization** | Compressing a model (e.g. to 4-bit) so it fits on smaller hardware. |
| **RAG** | Retrieval-Augmented Generation: fetch relevant snippets, then have the model answer using them. |
| **Reranking** | A second pass that re-orders retrieved results by relevance. |
| **Resource (MCP)** | Data a server exposes for the app or user to attach as context. |
| **Skill** | A folder of instructions (and optional scripts) an agent loads on demand for a specific task. |
| **stdio / Streamable HTTP** | The two MCP transports: local (the app launches the server) and remote (connect over a URL). |
| **Subagent** | A helper agent with its own context, which a main agent delegates tasks to. |
| **Temperature** | A randomness setting. Lower is more predictable, higher is more creative. |
| **Token** | A chunk of text (about ¾ of a word) that models read, write, and bill by. |
| **Trigger** | The event that starts an automation (a schedule, webhook, or new email). |
| **Vector database** | A database built to find embeddings that are "near" each other, i.e. similar in meaning. |
| **Vibe coding** | Building software by describing what you want and letting AI write the code. |
| **Webhook** | A URL that runs something when data is POSTed to it. It's how apps poke automations. |

---

**Next:** [Appendix F · 30 Project Ideas to Level Up →](f-project-ideas.md)
