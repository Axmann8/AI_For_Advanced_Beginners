# Appendix A · Glossary 📖

> ⏱️ 25 min read · 🎯 Everyone (keep it open in a tab!) · 🧰 Needs: nothing

**Every piece of AI jargon in this manual, in plain English, with a real-world example for each one.** Jump to a letter
with the sidebar or the cards below. Tip: on the website, **acronyms anywhere in the manual show their definition when you
hover over them** (or tap them on a phone). That feature is powered by this page. ✨

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

This glossary defines more than 200 AI terms used in this manual. Each entry gives a clear definition and a practical example of where you'll encounter the term or how it's used.

- **Search** with your browser's find function (Ctrl/Cmd+F) or the site search.
- **Follow the links** to the chapter that covers each term in depth.
- **On the website,** hovering over common acronyms anywhere in the manual shows their definitions.

</details>

<!-- in-this-chapter -->

## 🅰️ A

| Term | Meaning | In practice |
|---|---|---|
| **A2A (Agent2Agent)** | An open protocol for AI agents built by different companies or frameworks to talk to and delegate to each other. | A travel-booking agent hands the hotel search to a separate hotel company's agent and gets the results back. |
| **AAC** | Augmentative and alternative communication: tools that help people who can't rely on speech to communicate, increasingly with AI voices. | A speech-generating app that turns typed or tapped phrases into a natural voice. |
| **Adaptive thinking / effort** | Settings that let a model decide how much to "think" before answering, or let you dial reasoning depth up or down. | Choosing "low effort" for a quick rewrite and "high effort" for a tricky planning problem. |
| **Agent** | An AI system that works in a loop (think → use a tool → look at the result → repeat) until a goal is done. | Claude Code fixing a bug: it reads the files, edits code, runs the tests and repeats until they pass. |
| **Agent loop** | The think/act/observe cycle an agent repeats until it finishes or hits a limit. | Search the web → read a page → decide it needs another source → search again → write the answer. |
| **Agent SDK (Claude Agent SDK)** | A library that gives your own apps the same agent harness that powers Claude Code. | Building your own research or support agent in Python or TypeScript with file, tool and MCP support built in. |
| **Agentic RAG** | RAG where an agent decides what to search, searches several times and checks results. | An assistant that searches your docs, notices a gap, rephrases the query and searches again before answering. |
| **AGENTS.md / CLAUDE.md** | Markdown files in a project that coding agents read automatically as standing instructions. | A file listing your project's test command, coding style and "never edit these files" rules. |
| **AGI** | Artificial general intelligence: a hypothetical AI as capable as humans across most tasks. Definitions vary and are debated. | The term you'll see in headlines and lab mission statements; there's no agreed test for when it's reached. |
| **Alexa+** | Amazon's rebuilt, generative-AI Alexa: conversational, remembers preferences, and can book, order and control your smart home. Included with Prime in the US. | "Alexa, order what we usually get for taco night and remind me to defrost the chicken." |
| **Alt text** | A short text description of an image for people using screen readers. | `alt="Bar chart showing sales doubled between March and June"` on a website image. |
| **ANN** | Approximate nearest neighbor search: fast, nearly-exact search for similar vectors. | How a vector database searches millions of embeddings in milliseconds instead of comparing every one. |
| **Answer engine** | A search tool that writes an answer with numbered sources instead of a list of links. Perplexity is the best-known. | Asking Perplexity "best budget e-reader?" and getting a written comparison with clickable citations. |
| **API** | A way for programs to talk to each other. AI APIs let your code send prompts and get answers, usually billed per token. | A script that sends 500 product descriptions to a model and saves the rewritten versions to a spreadsheet. |
| **API key** | A secret string that identifies you (and your bill) when calling an API. | Stored in a `.env` file as `ANTHROPIC_API_KEY=...`, never pasted into code you share. |
| **Apple Intelligence** | Apple's AI features on iPhone, iPad and Mac, including the rebuilt Siri, Writing Tools and Visual Intelligence. | Highlighting an email on iPhone and choosing **Writing Tools → Proofread**. |
| **Artifact** | A generated, often interactive piece of content (an app, doc or chart) shown alongside a Claude chat. | Asking Claude for a habit tracker and getting a working, clickable app in a panel beside the chat. |
| **ASR** | Automatic speech recognition, also called speech-to-text. | The engine behind dictation, live captions and meeting transcripts. |
| **ATS** | Applicant tracking system: software employers use to collect and filter job applications. | Why résumés should use standard headings and include the job ad's key skills in plain text. |
| **Audio Overview** | A Gemini Notebook (NotebookLM) feature that turns your sources into a two-host podcast. | Turning a stack of lecture PDFs into a 15-minute discussion to listen to on your commute. |
| **Autonomy levels** | How much an AI does on its own: from suggestions, to drafts, to acting with approval, to fully automatic. | An email agent that drafts replies for approval (level 3) versus one that sends on its own (level 5). |

## 🅱️ B

| Term | Meaning | In practice |
|---|---|---|
| **Background agent** | A coding agent that works in the cloud on its own branch while you do other things. | Assigning "add dark mode" to a cloud agent before lunch and reviewing its pull request afterward. |
| **Barge-in** | Interrupting a voice agent while it's talking. Good agents stop and listen. | Saying "actually, make it Thursday" while a voice agent is still reading out available times. |
| **Batch API** | Sending many non-urgent requests at once for a big discount, with results later. | Classifying 50,000 support tickets overnight at roughly half the normal price. |
| **Benchmark** | A standard test set used to compare models. | SWE-bench for coding, or a leaderboard comparing models on reasoning and math tests. |
| **Bias (AI)** | Unfair patterns a model learned from data, which can affect outputs about people. | A résumé screener that rates otherwise identical candidates differently based on their names. |
| **BM25** | A classic keyword-ranking algorithm, often combined with vector search in hybrid search. | Finding an exact part number or error code that pure meaning-based search would miss. |
| **Body doubling** | Working alongside someone (or a voice AI) to stay focused. | Keeping a voice assistant session open while you work through a task you've been avoiding. |

## ©️ C

| Term | Meaning | In practice |
|---|---|---|
| **C2PA / content credentials** | A standard for attaching tamper-evident "how this was made" info to images and videos. | The "CR" label on an image that shows which AI tool created or edited it. |
| **Caching (prompt caching)** | Reusing processed prompt prefixes to make repeated calls cheaper and faster. | A 50-page manual sent with every question costs a fraction of the price after the first request. |
| **Chain / workflow** | A fixed sequence of steps, some of which use AI. | Every new form submission → AI summarizes it → summary is posted to Slack. |
| **Chatbot / AI assistant** | An app you talk to in plain language, like ChatGPT, Gemini, Claude, Copilot or Grok. | Typing "plan a three-day trip to Lisbon" into ChatGPT, Gemini or Claude. |
| **ChatGPT (OpenAI)** | OpenAI's assistant and the world's most-used AI app, with voice, images, projects, agents and more. | Using voice mode on a walk, Canvas for writing, or agent mode to research hotels. |
| **Checkpoint** | A saved state you can roll back to (in Claude Code, or a build-along's "it works so far" point). | Pressing Esc twice in Claude Code to rewind to before a change went wrong. |
| **Chunking** | Splitting documents into passages before embedding them for RAG. | Splitting a 200-page manual into passages of a few hundred words so search can find the right section. |
| **Claude (Anthropic)** | Anthropic's assistant, known for natural writing, long documents, Artifacts and Claude Code. | Uploading a long contract to Claude and asking for unusual clauses, with quotes. |
| **CLI** | Command-line interface: a program you use by typing commands in a terminal. | Typing `claude` or `ollama run gemma4` in a terminal window. |
| **Code execution** | A sandbox where the AI writes and runs code (often Python) to analyze data or check work. | Uploading a spreadsheet and asking for a chart; the assistant writes and runs Python to make it. |
| **Coding agent** | An AI that reads, writes, runs and fixes code on its own (Claude Code, Codex, Copilot agent…). | "Add a login page and tests for it," then reviewing the changes the agent made. |
| **Comet** | Perplexity's free AI web browser, with an assistant that can read and act on the pages you visit. | Asking the sidebar assistant to compare the prices in your three open shopping tabs. |
| **Commit (Git)** | A saved snapshot of your project with a message. | `git commit -m "Add recipe search"` creates a save point you can return to. |
| **Compaction** | Summarizing older parts of a long conversation to free up context. | Running `/compact` in Claude Code to summarize a long session before starting the next task. |
| **Computer use** | AI controlling a mouse, keyboard and screen (or a browser) like a human would. | An agent opening a website, filling in a form and taking a screenshot to check its work. |
| **Connector** | A ready-made integration in an AI app (often MCP under the hood) that links it to a service like Gmail. | Settings → Connectors → Gmail → sign in, then asking "what did my landlord say last week?" |
| **Context engineering** | Deliberately choosing what goes into the model's context: instructions, examples, documents, tools. | Giving the AI your style guide, two example emails and the relevant thread before asking for a reply. |
| **Context window** | How much text (in tokens) a model can consider at once: its working memory. | Why a very long chat starts "forgetting" details from the beginning. |
| **Copilot (Microsoft)** | Microsoft's assistant in Windows, Edge and Microsoft 365 apps like Word, Excel and Outlook. | Asking Copilot in Excel to "add a column that flags overdue invoices." |
| **Cosine similarity** | A measure of how closely two vectors point in the same direction. It's how RAG finds similar text. | A score near 1.0 between "car won't start" and "engine fails to turn over." |
| **CRM** | Customer relationship management: software (or a spreadsheet) for tracking contacts and deals. | HubSpot, or a simple sheet tracking each client, their last contact date and next step. |
| **CRUD** | Create, read, update, delete: the four basic things apps do with data. | A recipe app's add, view, edit and delete buttons. |
| **Custom connector** | A remote MCP server you add to an AI app by pasting its URL. | Pasting `https://example.com/mcp` into Claude's **Add custom connector** dialog. |
| **Custom instructions** | Standing notes about you and how you like answers, which the assistant includes in every chat. | "I'm a nurse in Ohio. Keep answers short and use bullet points." |

## 🇩 D

| Term | Meaning | In practice |
|---|---|---|
| **Deep research** | An assistant mode that runs a multi-step, multi-source investigation and writes a cited report. | Asking for a cited comparison of heat pumps for cold climates and getting a report minutes later. |
| **Deepfake** | Realistic fake video, audio or images of real people made with AI. | A fake video of a celebrity endorsing an investment scheme. |
| **DeepSeek (assistant)** | A Chinese AI lab and its free assistant, known for strong open-weight reasoning models. App data is stored in China. | Turning on DeepThink to watch it reason through a math problem step by step. |
| **Diff** | The list of changes between two versions of files. | Green and red lines showing exactly what a coding agent added and removed. |
| **Distillation** | Training a smaller model on a bigger model's outputs. | How many small, fast models get much of a large model's quality. |
| **Docker / container** | A packaged, isolated app that runs the same everywhere. | Starting the home lab's Ollama, Open WebUI and n8n with one `docker compose up -d`. |
| **DuckDB** | A tiny, fast database that runs SQL directly on CSV and Parquet files. | Running `SELECT category, SUM(amount) FROM 'bank.csv' GROUP BY 1` without setting up a database. |

## 🇪 E

| Term | Meaning | In practice |
|---|---|---|
| **Edge function** | A small piece of server code that runs close to users, on demand. | The small server route that sends a user's ingredients to Claude without exposing your API key. |
| **Elicitation** | An MCP feature where a server asks *you* a question mid-task. | A booking server pausing to ask "which of these three times works for you?" |
| **Embedding** | A list of numbers that represents the meaning of text (or images). Similar meanings get similar numbers. | Turning each note into a vector so "dentist appointment" finds a note about "teeth cleaning." |
| **Endpointing** | Deciding when a speaker has finished their turn, in voice agents. | Why a good voice agent waits for you to finish a sentence instead of cutting in mid-pause. |
| **Environment variable** | A named setting (like an API key) given to a program when it runs, instead of being written in the code. | `export OPENAI_API_KEY=...` in your shell, or a secret setting in Vercel. |
| **Eval (evaluation)** | A repeatable test set for measuring AI quality on your tasks. | Twenty real support questions with known good answers, rerun after every prompt change. |

## 🇫 F

| Term | Meaning | In practice |
|---|---|---|
| **Few-shot prompting** | Including a few examples in the prompt to show the pattern you want. | Showing two sample product descriptions, then asking for ten more in the same style. |
| **Fine-tuning** | Further training a model on your examples. Great for style and format, not for facts. | Training a small model on 300 of your emails so it drafts in your voice. |
| **Frontier model** | The most capable models available at a given time. | The top tier of each lab's lineup, used for the hardest reasoning and coding tasks. |
| **Function calling / tool use** | The model outputting a structured request to run a tool, which your software executes. | The model returns `get_weather(city="Lisbon")`; your code runs it and sends back the forecast. |

## 🇬 G

| Term | Meaning | In practice |
|---|---|---|
| **GDPR** | The European Union's data-protection law, giving people rights over their personal data. | Requesting a copy of everything a company stores about you, or asking it to delete your data. |
| **Gem** | A custom version of Gemini with saved instructions (and optional files) for a specific job. | A "Meal Planner" Gem that already knows your household's diet and budget. |
| **Gemini (Google)** | Google's assistant and model family, built into Android, Chrome, Gmail and Docs. | Asking Gemini "when is my flight?" and getting the answer from your Gmail. |
| **Gemini Live** | Gemini's real-time voice conversation mode, with camera and screen sharing. | Pointing your phone camera at the back of a TV and asking which HDMI port to use. |
| **Gemini Notebook (formerly NotebookLM)** | Google's source-grounded research notebook with Audio and Video Overviews, renamed in July 2026. | Uploading a course's readings and getting cited answers, flashcards and quizzes. |
| **Generative AI** | AI that creates new text, images, audio, music or video instead of only sorting or predicting. | Writing a speech, creating a logo, or composing a song from a short description. |
| **GGUF** | A file format for quantized local models, used by llama.cpp, Ollama and LM Studio. | Downloading `model-Q4_K_M.gguf` from Hugging Face to run in LM Studio. |
| **Git** | A version-control system that saves the history of your project. | Undoing a broken change with `git restore .` and getting back to the last working version. |
| **GitHub Actions** | Automations that run on GitHub when things happen (a push, a schedule, a comment). | Automatically running tests on every push, or building and deploying a website. |
| **GPU** | Graphics processing unit: a chip that's excellent at the math AI needs. | An NVIDIA graphics card with 16 GB of VRAM running a mid-size local model quickly. |
| **GraphRAG** | RAG that builds a knowledge graph of entities and relationships to answer connection questions. | Answering "which suppliers are connected to the delayed projects?" across many documents. |
| **Grok Imagine** | Grok's image and short-video generator. | Turning "a fox running through snow at dusk" into a short video clip with sound. |
| **Grok (xAI)** | The assistant from xAI (part of SpaceX), built into X, known for real-time posts and Grok Imagine. | Tapping Grok on a viral X post and asking for the background and what's confirmed. |
| **Grounding** | Making a model answer from specific sources (documents, search results) and cite them. | Telling the model "answer only from these documents and cite the page." |
| **Guardrails** | Rules, checks and limits that keep AI systems safe and on-task. | An agent that may read files freely but must ask before deleting or sending anything. |

## 🇭 H

| Term | Meaning | In practice |
|---|---|---|
| **Hallucination** | The model confidently stating something false. Grounding and verification reduce it. | A chatbot citing a court case or research paper that doesn't exist. |
| **Handoff** | One agent passing a conversation or task to another (or to a human). | A support bot transferring a billing question to a human agent with the conversation summary. |
| **Headless mode** | Running an agent (like Claude Code) from scripts or CI without an interactive chat. | `claude -p "summarize today's errors" < log.txt` running from a nightly cron job. |
| **HNSW** | A graph-based index that makes vector search fast. | The index type you'll see in vector database settings; it trades a tiny bit of accuracy for speed. |
| **Hook** | An automatic script that runs on agent events (e.g. "after each file edit, run the formatter"). | A rule that runs the code formatter after every edit, or blocks reading `.env` files. |
| **Host / client / server (MCP)** | Host = the AI app. Client = its connection manager. Server = the program exposing tools and data. | Claude Desktop (host) connects to the GitHub MCP server (server) through its own client. |
| **Human-in-the-loop** | A step where a person approves or edits before the AI's output is used. | An automation drafts a refund email, and it waits in Slack for your approval before sending. |
| **Hybrid search** | Combining keyword and vector search for better retrieval. | Combining BM25 and embeddings so a search finds both "error E4" and "machine won't heat." |

## 🇮 I

| Term | Meaning | In practice |
|---|---|---|
| **IDE** | Integrated development environment: a code editor with extras (VS Code, Cursor, JetBrains). | Writing code in Cursor or VS Code with AI suggestions alongside. |
| **Image-to-video** | Animating a still image with a video model. | Turning a product photo into a slow, rotating video clip for social media. |
| **Inference** | Running a model to get output (as opposed to training it). | Every chat message you send triggers inference; API pricing is for inference, not training. |
| **Inpainting / outpainting** | Editing part of an image, or extending it beyond its edges. | Removing a stranger from a photo's background, or extending a portrait into a landscape. |

## 🇯 J

| Term | Meaning | In practice |
|---|---|---|
| **JSON** | The universal text format for structured data (`{"key": "value"}`). | `{"name": "Pixel", "species": "cat", "age": 4}` |
| **JSON Schema** | A description of what valid JSON looks like. Tools use it to define their parameters. | A tool definition stating that `city` is a required string and `days` is an optional number. |
| **Jupyter notebook** | A document mixing notes, code and charts, run step by step. | A step-by-step sales analysis you can rerun each month on new data. |

## 🇰 K

| Term | Meaning | In practice |
|---|---|---|
| **Knowledge base** | A collection of documents an AI can search to answer questions. | A folder of company policies that an HR chatbot searches before answering. |
| **Knowledge cutoff** | The date a model's training data ends. It doesn't know later events unless given tools or documents. | Why a model without web search can't tell you last night's game score. |

## 🇱 L

| Term | Meaning | In practice |
|---|---|---|
| **Latency** | The delay before a response arrives. Crucial for voice. | Why a voice agent that takes three seconds to reply feels awkward on a phone call. |
| **Le Chat (Mistral)** | The assistant from French lab Mistral AI: fast, with memories, connectors and European privacy rules. | Asking Le Chat to transcribe and clean up a scanned handwritten recipe. |
| **Lethal trifecta** | Private data + untrusted content + a way to send data out, in one AI setup: a recipe for prompt-injection harm. | An agent that reads your email, browses the web and can send messages: one malicious page could leak your inbox. |
| **LLM** | Large language model: an AI trained on huge amounts of text to predict and generate language. | The model behind ChatGPT, Gemini, Claude and most other chat assistants. |
| **LLM-as-judge** | Using a model to grade other models' outputs against a rubric. | Asking a model to score 100 chatbot replies against a five-point rubric, then spot-checking its grades. |
| **Local model** | A model running on your own device instead of the cloud. | Running `ollama run gemma4` and chatting with no internet connection. |
| **LoRA** | Low-rank adaptation: a small add-on trained to teach a model a style, character or skill. | Training an image model on 20 photos of your dog so you can generate it in new scenes. |

## Ⓜ️ M

| Term | Meaning | In practice |
|---|---|---|
| **MCP** | Model Context Protocol: the open standard for connecting AI apps to tools and data. | Installing the GitHub MCP server so Claude, Cursor and ChatGPT can all read your issues. |
| **MCP Apps** | An MCP extension that lets servers show interactive UI inside the chat. | A booking server showing an interactive calendar right inside the chat. |
| **MCP Inspector** | A web tool for testing MCP servers by hand: list tools, call them, read raw messages. | `npx @modelcontextprotocol/inspector python server.py`, then clicking **List Tools**. |
| **MCP Registry** | The official public list of MCP servers that clients and catalogs can discover. | Searching registry.modelcontextprotocol.io for an official Notion or Stripe server. |
| **Memory (AI)** | Facts and preferences an assistant keeps across conversations. | "Remember that I'm vegetarian," and the assistant keeps it in mind in future chats. |
| **Meta AI** | Meta's assistant inside WhatsApp, Instagram, Messenger, Facebook and Ray-Ban Meta glasses. | Typing "@Meta AI suggest a restaurant for eight" in a WhatsApp group chat. |
| **Mixture of experts** | A model design where only some "expert" sub-networks run per token: big-model smarts, small-model speed. Often written "MoE". | Why some large open models run surprisingly fast on a Mac with enough memory. |
| **MLX** | Apple's machine-learning framework, fast on Apple Silicon. | Fine-tuning or running a model on a MacBook with `mlx-lm`. |
| **Model routing** | Sending easy tasks to cheap models and hard ones to frontier models. | A small model triages support emails, and only complex ones go to the flagship model. |
| **Multimodal** | Handling more than text: images, audio, video. | Uploading a photo of a broken part and asking what it is and how to fix it. |

## 🇳 N

| Term | Meaning | In practice |
|---|---|---|
| **n8n** | An open-source, self-hostable visual automation platform with strong AI features. | A self-hosted workflow that emails you an AI summary of new RSS articles every morning. |
| **Nano Banana** | The nickname for Google's Gemini image generation and editing models. | Asking Gemini to put you and a friend on a beach while keeping both faces recognizable. |
| **Node (n8n / Make)** | One step in a visual workflow. | A "Gmail Trigger" node feeding an "AI Agent" node, then a "Slack" node. |
| **NPU** | Neural processing unit: a chip in newer laptops and phones for efficient AI tasks. | The chip that runs on-device features like live captions and photo search on newer laptops and phones. |

## 🇴 O

| Term | Meaning | In practice |
|---|---|---|
| **OAuth** | The "Log in with…" flow that grants an app limited access without sharing your password. | Clicking "Sign in with Google" when connecting an AI app to your Drive. |
| **OCR** | Optical character recognition: turning images of text into actual text. | Extracting the text from a photo of a receipt so it can be added to a spreadsheet. |
| **Ollama** | A popular tool for running open models locally with one command. | `ollama pull qwen3` downloads a model; `ollama run qwen3` starts a chat. |
| **Open-weight model** | A model whose weights you can download and run yourself (Gemma, Qwen, Llama, gpt-oss…). | Downloading Gemma or Qwen and running it privately on your own computer. |
| **OpenAI-compatible API** | An API that copies OpenAI's format, so tools built for one work with many (including local models). | Pointing a tool built for OpenAI at `http://localhost:11434/v1` to use your local model instead. |
| **Orchestrator** | In multi-agent systems, the lead agent that plans and delegates to worker agents. | A lead research agent that assigns three subtopics to worker agents and merges their findings. |

## 🇵 P

| Term | Meaning | In practice |
|---|---|---|
| **PARA** | A note-organizing method: Projects, Areas, Resources, Archive. | Folders named Projects, Areas, Resources and Archive in Obsidian or Notion. |
| **Parameters (model)** | The learned numbers inside a model. More usually means more capable (and hungrier). | A "7B" model has about seven billion parameters and needs roughly 4–5 GB of memory at 4-bit. |
| **pause_turn** | An API stop reason meaning a long server-side tool turn paused, and you should continue the conversation. | When an API response ends with this stop reason, send the conversation back to let the model continue. |
| **Perplexity** | An AI answer engine that shows numbered sources for every answer; also makes the Comet browser. | Asking "which cordless vacuum is best for pet hair?" and getting a sourced comparison table. |
| **Personal Intelligence** | Gemini's opt-in feature that uses your Gmail, Calendar, Photos and other Google apps to answer questions about your own life. | Asking Gemini "what time is my dentist appointment?" and getting the answer from your Calendar. |
| **Phishing** | Scam messages that trick you into clicking links or sharing passwords or codes, now often written flawlessly by AI. | A perfectly written "your account is locked" email with a link to a fake login page. |
| **Plan mode** | A Claude Code mode where it researches and proposes a plan without changing anything. | Pressing Shift+Tab in Claude Code and asking for a plan before any files change. |
| **Plugin** | A bundle of skills, commands, subagents, hooks and MCP servers you install at once. | Installing one package that adds a team's review commands, skills and MCP servers to Claude Code. |
| **Progressive disclosure** | Loading only a short summary (like a skill's description) until the full content is needed. | Claude sees a one-line skill description and loads the full instructions only when the task needs them. |
| **Project (AI assistant)** | A workspace that groups chats with shared instructions and files, in ChatGPT, Claude, Le Chat and others. | A "Kitchen renovation" project holding your floor plan, budget and contractor quotes. |
| **Prompt** | The instructions and content you give a model. | "Write a 100-word birthday message for my grandmother, who loves gardening. Warm, not cheesy." |
| **Prompt injection** | Malicious instructions hidden in content the AI reads. | Hidden text on a web page telling an AI agent to email the user's files to an attacker. |
| **Prompt template (MCP prompt)** | A reusable prompt a server offers, often shown as a slash command. | Typing `/weekly-review` to run a server's ready-made review prompt. |
| **Pull request (PR)** | A proposed set of changes on GitHub for review before merging. | Reviewing the diff a coding agent proposed before merging it into the main branch. |

## 🇶 Q

| Term | Meaning | In practice |
|---|---|---|
| **Quantization** | Compressing a model (e.g. to 4-bit) so it fits on smaller hardware. | Running a 4-bit version of a 30B model that fits in 24 GB instead of 60 GB. |

## 🇷 R

| Term | Meaning | In practice |
|---|---|---|
| **RAG** | Retrieval-augmented generation: fetch relevant snippets, then have the model answer using them. | A support bot that searches the help center and answers with links to the articles it used. |
| **Rate limit** | A cap on how many requests you can make in a time window (HTTP 429 when exceeded). | An automation failing with "429 Too Many Requests" until you add a wait between calls. |
| **Realtime / speech-to-speech model** | A model that listens and speaks directly, for low-latency voice agents. | A phone agent that responds in under a second and handles interruptions naturally. |
| **Reasoning model** | A model that "thinks" step by step before answering, improving hard problems. | Choosing "Thinking" mode for a tax calculation or a complex scheduling problem. |
| **Remote MCP server** | An MCP server reached over the internet (Streamable HTTP) instead of launched locally. | Connecting to Notion's hosted MCP server by URL, with nothing installed on your computer. |
| **Repository (repo)** | A project folder tracked by Git, often hosted on GitHub. | `github.com/your-name/recipe-box`, containing your code and its full history. |
| **Reranking** | A second pass that re-orders retrieved results by relevance. | Retrieving the top 50 passages, then using a reranker to keep the best five for the answer. |
| **Resource (MCP)** | Data a server exposes for the app or user to attach as context. | Attaching `notes://all` from a notes server so the AI can read your notes as context. |
| **REST API** | The common style of web API using HTTP methods (GET, POST…) on URLs. | `GET /v1/forecast?city=London` returns weather data as JSON. |
| **RLHF** | Reinforcement learning from human feedback: training models using people's ratings of outputs. | Part of why assistants follow instructions politely instead of just continuing your text. |
| **RLS** | Row-level security: database rules so each user only sees their own rows (e.g. in Supabase). | A Supabase policy that ensures users only ever see recipes they created. |
| **Rubric** | A list of specific criteria for scoring outputs. | "1 point each: answers the question, cites a source, under 100 words, friendly tone." |

## 🇸 S

| Term | Meaning | In practice |
|---|---|---|
| **Sandbox** | An isolated environment where code or agents run without touching the rest of your system. | Running an untrusted MCP server in a Docker container with no access to your files. |
| **SDK** | Software development kit: a library that makes an API easy to use from a programming language. | `pip install anthropic`, then calling `client.messages.create(...)` from Python. |
| **Semantic search** | Searching by meaning (with embeddings), not just exact words. | Searching your notes for "ways to sleep better" and finding a note titled "evening routine." |
| **Server tool** | A tool the AI provider runs for you (web search, web fetch, code execution). | Enabling web search in an API request without writing any search code yourself. |
| **Serverless function** | Code that runs on demand in the cloud, with no server to manage. | An API route on Vercel that runs only when your app calls it. |
| **Siri** | Apple's voice assistant, rebuilt in 2026 with Apple Intelligence, on-screen awareness and Gemini-based models. | "Siri, send the photos from last weekend to Mom" using on-screen awareness and app actions. |
| **Skill** | A folder of instructions (and optional scripts) an agent loads on demand for a specific task. | An "inbox-triage" folder with instructions and a script that Claude loads when you ask it to sort notes. |
| **Slash command** | A saved prompt you trigger by typing `/name`. | Typing `/standup` to send your saved daily-update prompt. |
| **SOP** | Standard operating procedure: step-by-step instructions for a recurring task. | A written step-by-step process for onboarding clients that an AI agent can follow. |
| **Space (Perplexity)** | A Perplexity research folder with its own instructions and files. | A "Buying our first home" Space with your budget, preferred areas and mortgage documents. |
| **Spend limit** | A hard cap on API spending, set in the provider's console. | Setting a $20 monthly cap in the API console so a runaway loop can't cost more. |
| **SSE** | Server-sent events: a way for servers to stream updates to clients. Older MCP remote transport. | You'll see it in older MCP server docs; newer servers use Streamable HTTP instead. |
| **STAR method** | Situation, task, action, result: a structure for interview stories. | "Our launch was delayed (S), I owned the fix (T), I rebuilt the pipeline (A), we shipped a week early (R)." |
| **stdio / Streamable HTTP** | The two MCP transports: local (the app launches the server) and remote (connect over a URL). | A filesystem server running on your laptop (stdio) versus a hosted Notion server at a URL (HTTP). |
| **Stop reason** | Why the model stopped: finished, hit max tokens, wants a tool, paused, refused. | `end_turn` means finished; `tool_use` means run the requested tool; `max_tokens` means it was cut off. |
| **Streaming** | Receiving the model's output word by word as it's generated. | Text appearing word by word in a chat app instead of all at once after a delay. |
| **Structured output** | Forcing a model's reply to match a schema (e.g. valid JSON with specific fields). | Getting back `{"title": "...", "date": "2026-10-01", "priority": "High"}` instead of a paragraph. |
| **STT / TTS** | Speech-to-text (transcription) and text-to-speech (voice generation). | Whisper transcribing a voice memo (STT); ElevenLabs reading a script aloud (TTS). |
| **Subagent** | A helper agent with its own context, which a main agent delegates tasks to. | The main agent sends a "code reviewer" subagent to check its work and receives only the summary. |
| **Sycophancy** | When an AI agrees with you or flatters you instead of being honest. | The AI calling a weak business plan "brilliant" until you ask it to be critical. |
| **System prompt** | Standing instructions that set the model's role, rules and style for a conversation. | "You are a patient math tutor. Give hints, not answers. Check understanding before moving on." |

## 🇹 T

| Term | Meaning | In practice |
|---|---|---|
| **Tailscale** | A private network (VPN) that connects your devices securely without opening ports. | Opening your home AI server on your phone from anywhere, without exposing it to the internet. |
| **Temperature** | A randomness setting. Lower is more predictable, higher is more creative. | Setting 0.2 for consistent data extraction, 0.9 for brainstorming names. |
| **Temporary chat / incognito chat** | A chat that isn't saved to history or memory, and usually isn't used for training. | Asking a sensitive health question without it being saved to your history or memory. |
| **TF-IDF** | A classic way to turn text into vectors by weighting rare, meaningful words. Used in the RAG kit. | The simple search method in this manual's rag-from-scratch kit, which needs no API key. |
| **Token** | A chunk of text (about ¾ of a word) that models read, write and bill by. | "Unbelievable" might be three tokens; a one-page email is roughly 400. |
| **Tool annotations** | Hints in MCP tool definitions (read-only, destructive, etc.) that help clients decide when to ask for approval. | Marking `delete_file` as destructive so the app always asks before running it. |
| **Tool poisoning** | Hiding malicious instructions in an MCP tool's description or output. | A "weather" server whose description secretly tells the AI to read and send your SSH keys. |
| **Tool runner** | An SDK helper that runs the agent loop (call model → run tools → repeat) for you. | Passing Python functions to the SDK and letting it handle the call-run-repeat loop. |
| **Tracing** | Recording every step an agent took (inputs, outputs, timing, cost) for debugging. | Opening a trace to see exactly which tool call returned bad data and how much each step cost. |
| **Trigger** | The event that starts an automation (a schedule, webhook or new email). | "Every weekday at 7 a.m.," "when a form is submitted," or "when an email arrives from my boss." |

## 🇺 U · 🇻 V

| Term | Meaning | In practice |
|---|---|---|
| **Unified memory** | A design (e.g. Apple Silicon) where CPU and GPU share one big memory pool, great for local AI. | A Mac with 64 GB of unified memory running models that would need several GPUs on a PC. |
| **VAD** | Voice activity detection: noticing when someone starts and stops speaking. | How a voice agent knows you've started talking so it can stop and listen. |
| **Vector** | A list of numbers, such as an embedding. | `[0.12, -0.48, 0.91, …]`, often with hundreds or thousands of numbers. |
| **Vector database** | A database built to find embeddings that are "near" each other, i.e. similar in meaning. | Chroma, pgvector or Pinecone storing the embeddings for a document search bot. |
| **Veo** | Google's video generation model, available in Gemini, which makes short clips with sound. | Asking Gemini for an eight-second clip of a lighthouse at sunrise, with wave sounds. |
| **Vibe coding** | Building software by describing what you want and letting AI write the code. | Describing a family chore-chart app to Lovable or Claude Code and refining it through chat. |
| **Vision model** | A model that understands images. | Uploading a chart screenshot and asking what trend it shows. |
| **Voice banking** | Recording your voice so AI can create a personal synthetic voice, e.g. before losing speech. | Recording a few hours of speech after an ALS diagnosis to preserve a personal synthetic voice. |
| **Voice cloning** | AI copying someone's voice from a short recording. Useful for accessibility and dubbing, and misused in phone scams. | Dubbing your own video into Spanish in your voice, with consent; or a scammer faking a relative's call. |
| **Voice mode** | Talking with an assistant out loud instead of typing, often with the ability to interrupt. | Brainstorming out loud with ChatGPT, Gemini Live or Claude while cooking or walking. |
| **VRAM** | Video RAM: the memory on a graphics card. It decides which models fit on a GPU. | A 12 GB graphics card comfortably runs models up to about 12–14B parameters at 4-bit. |

## 🇼 W · 🇽 X · 🇾 Y · 🇿 Z

| Term | Meaning | In practice |
|---|---|---|
| **WCAG** | Web Content Accessibility Guidelines: the standard for making websites usable by everyone. | Checking that text has at least a 4.5:1 contrast ratio against its background. |
| **Webhook** | A URL that runs something when data is POSTed to it. It's how apps poke automations. | An iPhone shortcut that POSTs dictated text to an n8n webhook URL, creating a note. |
| **Workflow** | A sequence of automated steps, often visual (n8n, Zapier, Make). | A Zapier Zap or n8n workflow that turns invoice emails into spreadsheet rows. |
| **Worktree (Git)** | An extra working folder of the same repo on its own branch, great for parallel agents. | Running two Claude Code sessions on two features at once, each in its own worktree folder. |
| **World model** | An AI that generates or simulates an interactive environment you can move through. | Google DeepMind's Genie research, generating an explorable scene from a single image. |
| **Zero-shot** | Asking a model to do a task without giving examples. | "Classify this review as positive, neutral or negative," with no examples given. |

---

**Next:** [Appendix B · The Cheat Sheet →](b-cheat-sheet.md)
