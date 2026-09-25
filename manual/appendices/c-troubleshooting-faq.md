# Appendix C · Troubleshooting FAQ 🔧

> ⏱️ 15 min read · 🎯 Anyone who's stuck (it happens to everyone!) · 🧰 Needs: the exact error message

**Stuck? You're not alone.** These are the most common problems across the whole manual, grouped by topic, with fixes. And
the #1 universal trick: **paste the exact error message into your AI assistant**, along with what you did and what you
expected. It's usually the fastest fix of all. 🪄

<details class="eli5" open>
<summary>🧸 ELI5: This page in 30 seconds</summary>

When something breaks, don't panic! Find your problem in this list (they're grouped like drawers: plug-ins, robots, coding,
money…), and follow the fix. If it's not here, copy the error message and ask your AI helper. 🔧🙂

</details>

<!-- in-this-chapter -->

## 🧭 The universal debugging recipe

<details class="eli5">
<summary>🧸 ELI5</summary>

For any problem: write down what you did, what you expected, and what happened, then check one thing at a time.

</details>

1. **Reproduce it:** can you make it happen again?
2. **Read the error** (really read it). The answer is often right there.
3. **Isolate:** test one piece at a time (the tool alone, the workflow step alone).
4. **Ask AI with context:** *"I did [X], expected [Y], got [Z]. Here's the error: [paste]. Before fixing, list 3 likely causes."*
5. **Change one thing**, test again. Commit or save when it works.

## 🐣 Beginner questions & everyday assistant hiccups

<details class="eli5">
<summary>🧸 ELI5</summary>

The most common little problems people hit in ChatGPT, Gemini, Claude and friends, like limits, logins and answers that
stop halfway, and how to fix each one.

</details>

### "You've reached your limit" / "Try again later."

Free (and even paid) plans have usage limits that reset after a few hours or a day. Wait until the time shown, switch to
a smaller or faster model in the model picker, or carry on in another assistant for now
([Using Several Assistants](../part-2-ai-assistants-field-guide/31-using-several-assistants.md)).

### The answer stopped in the middle.

Type **"continue"** or press **Regenerate**. For very long outputs, ask for them in parts (*"part 1 of 3"*).

### "Something went wrong" / network error.

Wait a few seconds and retry; refresh the page; check your internet connection; check the company's status page (for
example status.openai.com, status.anthropic.com, or search "[assistant] status"). Long chats sometimes fail: start a new
chat with a short summary.

### I can't log in, or I'm not getting the login email.

Check spam, make sure you're using the same sign-in method as before ("Continue with Google" vs. email), and try the app
*and* the website. Never enter your password on a page you reached from an unexpected email.

### It answers in the wrong language or uses American spelling.

Tell it (*"Reply in Spanish"*, *"Use British spelling"*) and put the preference in your **custom instructions**
([Getting Set Up](../part-1-ai-from-zero/05-getting-set-up.md)).

### I can't find a feature someone mentioned (memory, voice, projects…).

Features vary by **plan, country, device and account type** (personal vs. work), and apps move buttons often. Ask the
assistant itself: *"Where do I find [feature] in this app?"*, or check its [Field Guide
chapter](../part-2-ai-assistants-field-guide/index.md).

### I shared something private by mistake.

Delete the chat, remove any memory it created (Settings → Memory), and revoke any shared link. If you shared a password
or card number, **change the password or call your bank** right away ([Staying Safe](../part-1-ai-from-zero/11-staying-safe-with-ai.md)).

### Which assistant should I actually use?

Any of the big ones is fine to start. Use the [30-second answer](../part-1-ai-from-zero/04-choosing-your-first-assistant.md)
or do the 15-minute taste test.

## 🔌 MCP & connectors

<details class="eli5">
<summary>🧸 ELI5</summary>

Problems with plug-ins: they don't show up, they crash, or the AI ignores them.

</details>

### My MCP server doesn't show up in Claude Desktop or Cursor.

1. **Fully quit** the app (not just close the window) and reopen it.
2. **Validate your JSON:** a missing or trailing comma breaks the whole file. Paste it into a validator or ask AI to fix it.
3. Use **absolute paths** for commands and files.
4. Check the **logs** (Claude Desktop: Settings → Developer → Open Logs Folder).

### Error: `spawn npx ENOENT` / `command not found`.

GUI apps often don't see your terminal's PATH. Use the **full path**: run `which npx` (or `where npx` on Windows) and put that
in `"command"`. Same for `uvx`, `python` and `node`.

### The server connects but has no tools, or disconnects immediately.

- For stdio servers, something is **printing to stdout** (a stray `print()` or `console.log`). Log to stderr instead.
- Test it standalone: `npx @modelcontextprotocol/inspector <command> <args>`.
- Missing environment variables (API keys) often cause silent startup crashes.

### OAuth login for a remote server fails or loops.

Remove and re-add the connector, make sure pop-ups aren't blocked, and check your account (or workspace admin) allows that
integration. In Claude Code, use `/mcp` to re-authenticate.

### The AI ignores my MCP tools or uses the wrong one.

- Mention the tool explicitly: *"Use the Notion tool to…"*
- Disable unrelated servers. Too many tools confuse models and eat context.
- If it's your own server, improve the **tool descriptions** ([Building MCP Servers](../part-4-mcp-and-connectors/42-building-mcp-servers.md)).

## ⚙️ Automations

<details class="eli5">
<summary>🧸 ELI5</summary>

Problems with robot recipes in n8n, Zapier or Make: they work in testing but not for real, or they give messy answers.

</details>

### My workflow works in testing but not when active.

- **Webhook URLs differ:** n8n's `/webhook-test/` only works while testing; production uses `/webhook/`.
- Is the workflow actually **Active / published**?
- Local n8n can't receive webhooks from the internet. Use n8n Cloud, a VPS or a tunnel.
- Check the **execution log** for the failing run.

### The AI step returns text when I need JSON.

Ask for *"ONLY a JSON object, no prose,"* show the exact shape, use a **structured output parser** if available, and strip
code fences before parsing ([Webhooks, APIs & JSON](../part-5-automation/46-webhooks-apis-json.md)).

### Error 429 (rate limit) in bulk workflows.

Process in **batches** with **Wait** nodes between them, enable retries with backoff, and check your API tier's limits.

### Expressions like `{{ $json.field }}` return nothing.

Open the previous node's output and check the **exact field path** (case-sensitive, nested). In n8n, drag the field from the
input panel to insert the right expression.

### My Telegram bot doesn't reply.

Is the workflow **Active**, and is n8n reachable over **HTTPS**? Does the "Only me?" check contain *your* numeric user ID?
([Pocket AI Assistant](../part-13-build-alongs/112-build-along-pocket-ai-assistant.md#-troubleshooting))

## 🤖 AI behavior

<details class="eli5">
<summary>🧸 ELI5</summary>

Problems with how the AI answers: making things up, forgetting, or sounding boring.

</details>

### It confidently makes things up.

Give it **ground truth**: web search, documents or connectors. Ask for **citations**, and explicitly allow *"say you don't know."*
For facts that matter, verify at the source ([How Models Really Work](../part-3-foundations/33-how-models-really-work.md)).

### It forgot what we discussed earlier.

The context got long, was compacted, or you're in a new chat. Restate key facts, use Projects, memory or `CLAUDE.md`, or start
fresh with a summary ([Context Engineering](../part-3-foundations/36-context-engineering.md)).

### The answers are generic and bland.

Add **specifics**: audience, examples, constraints, your own opinions and stories. Ask it to avoid clichés, and give it samples of
the style you want ([Writing & Content](../part-11-ai-for-life-and-work/92-writing-and-content.md)).

### It refuses something harmless.

Explain the context and purpose plainly (*"I'm a nurse preparing patient education materials about…"*). If it's a genuine
misunderstanding, rephrasing usually works.

## 🧑‍💻 Coding agents & Git

<details class="eli5">
<summary>🧸 ELI5</summary>

Problems when an AI coding helper breaks things, goes in circles, or Git gets confusing.

</details>

### It keeps "fixing" code and breaking other things.

Commit working states, ask it to **write tests first**, make one change at a time, and when looping, ask it to *step back and
list possible causes before changing code*. Or `/clear` and restart with a crisp description.

### The agent broke everything and I didn't commit.

`git restore .` discards uncommitted changes (it's permanent, so be sure!). In Claude Code, `Esc Esc` or `/rewind` also returns
to checkpoints ([Git & GitHub](../part-7-building-with-ai/61-git-and-github.md#-oh-no-rescue-guide)).

### Claude Code doesn't follow my project rules.

Put them in `CLAUDE.md` (short and specific), and after a mistake say *"add a note to CLAUDE.md so this doesn't happen again."* For
rules that must *always* happen, use a **hook** ([Claude Code Power-Ups](../part-7-building-with-ai/63-claude-code-power-ups.md)).

### I leaked an API key in a commit.

**Rotate it immediately** (make a new key, revoke the old one). Deleting the commit isn't enough.

## 🔑 API & costs

<details class="eli5">
<summary>🧸 ELI5</summary>

Problems with AI keys and bills: login errors, surprise costs, or answers that stop halfway.

</details>

### 401 / authentication error.

Check the key is set in the environment the code actually runs in (`echo $ANTHROPIC_API_KEY`), has no extra spaces, and hasn't
been revoked. Restart your terminal after setting it.

### My bill is higher than expected.

Check the usage dashboard per key. Common culprits: agent loops, huge tool results, max effort everywhere, no caching, and
processing items repeatedly ([Cost Optimization](../part-12-mastery/106-cost-optimization.md)). **Set spend limits now.**

### Responses get cut off mid-sentence.

You hit `max_tokens`. Raise it (and use streaming for long outputs), or ask for a more concise format.

### The API rejects a server tool type (like web search).

Server tool type names are **versioned** (e.g. `web_search_20260318`). Check the docs for the current names, and update your SDK.

## 🌍 Deploying & hosting

<details class="eli5">
<summary>🧸 ELI5</summary>

Problems putting your app on the internet: it works at home but not online, or logins go to the wrong place.

</details>

### It works locally but not on Vercel or Netlify.

Missing **environment variables** on the host is the #1 cause. Add them in the dashboard, then **redeploy**. Then read the build
logs ([Deploying & Hosting](../part-7-building-with-ai/66-deploying-and-hosting.md)).

### Login links redirect to localhost.

Update the **Site URL** and **redirect URLs** in your auth provider (e.g. Supabase → Authentication → URL Configuration).

### Users can see each other's data.

Enable **row-level security** on every table and write per-user policies. Test with a second account
([Vibe Coding](../part-7-building-with-ai/65-vibe-coding-your-first-app.md#-step-6-dont-skip-the-safety-basics)).

## 🗣️ Voice agents

<details class="eli5">
<summary>🧸 ELI5</summary>

Problems with talking robots: they're slow, talk too much, or mishear names.

</details>

| Problem | Fix |
|---|---|
| Long awkward pauses | Faster models, shorter tool responses, a filler phrase ("One moment…") |
| Talks too much | *"1–2 short sentences per turn"* in the prompt |
| Mishears names and numbers | Ask it to spell back, and pick a better speech-to-text model |
| Tools never called | Clearer tool descriptions, and tell it *when* to call each |

More: [Voice Receptionist troubleshooting](../part-13-build-alongs/119-build-along-voice-receptionist.md#-troubleshooting).

## 🏠 Local models & home lab

<details class="eli5">
<summary>🧸 ELI5</summary>

Problems with AI on your own computer: too slow, can't find the model, or programs fighting over the same door number.

</details>

### Local models are painfully slow.

Use a smaller or more quantized model, close other heavy apps, make sure the GPU is actually being used, and on Apple Silicon run
Ollama **natively** rather than in Docker ([Hardware for Local AI](../part-9-local-ai/79-hardware-for-local-ai.md)).

### Open WebUI can't see my Ollama models.

Inside Docker Compose use `http://ollama:11434`. For native Ollama on the host use `http://host.docker.internal:11434`. Then pull
a model: `docker compose exec ollama ollama pull gemma4`.

### Docker says a port is already in use.

Something else uses that port. Change the left side of the mapping in `docker-compose.yml` (e.g. `"3001:8080"`).

### My local model can't use tools or loses track in agent tasks.

Pick a model with **tool calling**, give it a longer context (32k–64k+), and give it smaller tasks
([Local AI for Coding & Agents](../part-9-local-ai/81-local-ai-for-coding-and-agents.md)).

## 🧰 This repo's starter kits

<details class="eli5">
<summary>🧸 ELI5</summary>

Problems running the example projects that come with this manual.

</details>

| Kit | If it fails… |
|---|---|
| `my-first-mcp-server` | `pip install -r requirements.txt` (MCP SDK v2), then `python smoke_test.py` |
| `weather-mcp-server` | `npm install`, then `npm test` (works offline). Live "fetch failed" = no internet or a blocked network |
| `research-agent` | Run `python test_research_agent.py` first. API errors about tool types: check current server tool names |
| `newsletter-pipeline` | `--dry-run` first. A feed skipped = not a valid feed URL |
| `rag-from-scratch` | `python test_rag.py`, and `--search` works without a key |
| n8n workflows | Re-select credentials after import, and re-add a node if its version looks off |

## 🌐 This manual's website

<details class="eli5">
<summary>🧸 ELI5</summary>

How to publish or preview the website version of this manual.

</details>

### How do I publish the website version of this manual?

In the GitHub repo: **Settings → Pages → Source: GitHub Actions**. Then merge to `main`, and the site workflow builds and deploys it
automatically.

### How do I build it locally?

`pip install -r requirements-docs.txt && mkdocs serve`, then open `http://127.0.0.1:8000`.

---

**Next:** [Appendix D · The Prompt Library →](d-prompt-library.md)
