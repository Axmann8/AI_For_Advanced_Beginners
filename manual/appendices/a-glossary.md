# Appendix A · Glossary 📖

Quick, plain-English definitions for the jargon in this manual, in alphabetical order.

| Term | Meaning |
|---|---|
| **Adaptive thinking / effort** | Settings that let a model decide how much to "think" before answering, or let you dial reasoning depth up or down. |
| **Agent** | An AI system that works in a loop (think → use a tool → look at the result → repeat) until a goal is done. |
| **Agent loop** | That think/act/observe cycle. See [Ch. 1](../part-1-foundations/01-the-mental-model.md). |
| **AGENTS.md / CLAUDE.md** | A Markdown file in a project that agents read automatically as standing instructions. |
| **API** | A way for programs to talk to each other. AI APIs charge per token. |
| **Artifact** | A generated, often interactive, piece of content (an app, doc, or chart) displayed alongside a Claude chat. |
| **BM25** | A classic keyword-ranking algorithm, often combined with vector search in "hybrid search." |
| **Chunking** | Splitting documents into passages before embedding them for RAG. |
| **Computer use** | AI controlling a mouse, keyboard, and screen (or a browser) like a human would. |
| **Connector** | A ready-made integration in an AI app (often MCP under the hood) that links it to a service like Gmail. |
| **Context window** | How much text (in tokens) a model can consider at once. It's the model's working memory. |
| **Cosine similarity** | A measure of how closely two vectors point in the same direction. It's how RAG finds similar text. |
| **Custom connector** | A remote MCP server you add to an AI app by pasting its URL. |
| **Deep research** | An assistant mode that runs a multi-step, multi-source investigation and writes a cited report. |
| **Docker / container** | A packaged, isolated app that runs the same everywhere. It's how the home lab runs Ollama, Open WebUI, and n8n. |
| **Elicitation** | An MCP feature where a server asks *you* a question mid-task. |
| **Embedding** | A list of numbers that represents the meaning of text. Similar meanings get similar numbers. |
| **Eval (evaluation)** | A repeatable test set for measuring AI quality on your tasks. See [Ch. 38](../part-10-mastery/38-evaluating-ai.md). |
| **Fine-tuning** | Further training a model on your examples. Usually *not* needed. Try RAG and prompting first. |
| **Function calling / tool use** | The model outputting a structured request to run a tool, which your software executes. |
| **Hallucination** | The model confidently stating something false. Grounding and verification reduce it. |
| **Headless mode** | Running an agent (like Claude Code) from scripts or CI without an interactive chat. |
| **Hook** | An automatic script that runs on agent events (e.g. "after each file edit, run the formatter"). |
| **Host / client / server (MCP)** | Host = the AI app. Client = its connection manager. Server = the program exposing tools and data. |
| **Human-in-the-loop** | A step where a person approves or edits before the AI's output is used. |
| **Hybrid search** | Combining keyword and vector search for better retrieval. |
| **Inference** | Running a model to get output (as opposed to training it). |
| **JSON** | The universal text format for structured data (`{"key": "value"}`). See [Ch. 12](../part-3-automation/12-webhooks-apis-json.md). |
| **JSON Schema** | A description of what valid JSON looks like. Tools use it to define their parameters. |
| **Knowledge cutoff** | The date a model's training data ends. It doesn't know later events unless given tools or documents. |
| **LLM-as-judge** | Using a model to grade other models' outputs against a rubric. |
| **LoRA** | A small add-on trained to teach an image or language model a specific style, character, or skill. |
| **MCP (Model Context Protocol)** | The open standard for connecting AI apps to tools and data. See [Ch. 4](../part-2-mcp-and-connectors/04-mcp-explained.md). |
| **MCP Apps** | An MCP extension that lets servers show interactive UI inside the chat. |
| **MCP Inspector** | A web tool for testing MCP servers by hand: list tools, call them, read raw messages. |
| **Multimodal** | Handling more than text: images, audio, video. |
| **Node (n8n/Make)** | One step in a visual workflow. |
| **OAuth** | The "Log in with…" flow that grants an app limited access without sharing your password. |
| **Open-weight model** | A model whose weights you can download and run yourself (Llama, Qwen, Gemma, and others). |
| **Orchestrator** | In multi-agent systems, the lead agent that plans and delegates to worker agents. |
| **PARA** | A note-organizing method: Projects, Areas, Resources, Archive. |
| **Plugin** | A bundle of connectors/MCP servers, skills, and commands you can install at once. |
| **Prompt caching** | Reusing processed prompt prefixes to make repeated calls cheaper and faster. |
| **Prompt injection** | Malicious instructions hidden in content the AI reads. See [Ch. 37](../part-10-mastery/37-safety-costs-and-gotchas.md). |
| **Prompt template (MCP prompt)** | A reusable prompt a server offers, often shown as a slash command. |
| **Quantization** | Compressing a model (e.g. to 4-bit) so it fits on smaller hardware. |
| **RAG** | Retrieval-Augmented Generation: fetch relevant snippets, then have the model answer using them. |
| **Rate limit** | A cap on how many requests you can make in a time window (HTTP 429 when exceeded). |
| **Realtime / speech-to-speech model** | A model that listens and speaks directly, for low-latency voice agents. |
| **Reranking** | A second pass that re-orders retrieved results by relevance. |
| **Resource (MCP)** | Data a server exposes for the app or user to attach as context. |
| **REST API** | The common style of web API using HTTP methods (GET, POST…) on URLs. |
| **Sandbox** | An isolated environment where code or agents can run without touching the rest of your system. |
| **Skill** | A folder of instructions (and optional scripts) an agent loads on demand for a specific task. |
| **stdio / Streamable HTTP** | The two MCP transports: local (the app launches the server) and remote (connect over a URL). |
| **Structured output** | Forcing a model's reply to match a schema (e.g. valid JSON with specific fields). |
| **STT / TTS** | Speech-to-text (transcription) and text-to-speech (voice generation). |
| **Subagent** | A helper agent with its own context, which a main agent delegates tasks to. |
| **Temperature** | A randomness setting. Lower is more predictable, higher is more creative. |
| **TF-IDF** | A classic way to turn text into vectors by weighting rare, meaningful words. It's used in the RAG kit. |
| **Token** | A chunk of text (about ¾ of a word) that models read, write, and bill by. |
| **Tool annotations** | Hints in MCP tool definitions (read-only, destructive, etc.) that help clients decide when to ask for approval. |
| **Tool runner** | An SDK helper that runs the agent loop (call model → run tools → repeat) for you. |
| **Trigger** | The event that starts an automation (a schedule, webhook, or new email). |
| **Vector database** | A database built to find embeddings that are "near" each other, i.e. similar in meaning. |
| **Vibe coding** | Building software by describing what you want and letting AI write the code. |
| **Webhook** | A URL that runs something when data is POSTed to it. It's how apps poke automations. |


---

**Next:** [Appendix B · The Cheat Sheet →](b-cheat-sheet.md)
