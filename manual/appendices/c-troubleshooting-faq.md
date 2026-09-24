# Appendix C · Troubleshooting FAQ 🔧

Stuck? You're not alone. These are the most common problems and how to fix them. When in doubt, paste the
exact error message into your AI assistant. It's usually the fastest fix of all.

---

## 🔌 MCP & connectors

### My MCP server doesn't show up in Claude Desktop / Cursor.

1. **Fully quit** the app (not just close the window) and reopen it.
2. **Validate your JSON:** a missing comma or trailing comma breaks the whole file. Paste it into a JSON validator or ask AI to fix it.
3. Use **absolute paths** for commands and files.
4. Check the **logs** (Claude Desktop: Settings → Developer → Open Logs Folder).

### Error: `spawn npx ENOENT` / `command not found`.

GUI apps often don't see your terminal's PATH. Use the **full path**: run `which npx` (or `where npx` on Windows)
and put that path in `"command"`. Same for `uvx`, `python`, and `node`.

### The server connects but has no tools, or disconnects immediately.

- For stdio servers, something is **printing to stdout** (a stray `print()`/`console.log`). Log to stderr instead.
- Test it standalone: `npx @modelcontextprotocol/inspector <command> <args>`.
- Missing environment variables (API keys) often cause silent startup crashes.

### OAuth login for a remote server fails or loops.

Try removing and re-adding the connector, make sure pop-ups aren't blocked, and check that your account (or workspace admin)
allows that integration. In Claude Code, use `/mcp` to re-authenticate.

### The AI ignores my MCP tools or uses the wrong one.

- Mention the tool explicitly: *"Use the Notion tool to…"*
- Disable unrelated servers. Too many tools confuse models.
- If it's your own server, improve the **tool descriptions** ([Ch. 7](../part-2-mcp-and-connectors/07-building-mcp-servers.md)).

## ⚙️ Automations

### My n8n/Zapier/Make workflow works in testing but not when active.

- **Webhook URLs differ:** n8n's `/webhook-test/` only works while testing, and production uses `/webhook/`.
- Is the workflow actually **toggled Active / published**?
- Local n8n can't receive webhooks from the internet. Use n8n Cloud, a VPS, or a tunnel.
- Check the **execution log** for the failing run.

### The AI step returns text when I need JSON.

Ask for *"ONLY a JSON object, no prose"*, show the exact shape, use a **structured output parser** if available, and
strip ```` ``` ```` fences before parsing ([Ch. 12](../part-3-automation/12-webhooks-apis-json.md)).

### Error 429 (rate limit) in bulk workflows.

Process in **batches** with **Wait** nodes between them, enable retries with backoff, and check your API tier's limits.

### Expressions like `{{ $json.field }}` return nothing.

Open the previous node's output and check the **exact field path** (case-sensitive, nested objects). In n8n, drag the field
from the input panel to insert the correct expression.

## 🤖 AI behavior

### It confidently makes things up.

Give it **ground truth**: web search, documents, or connectors. Ask for **citations**, and explicitly allow *"say you don't know."*
For facts that matter, verify at the source. ([Ch. 2](../part-1-foundations/02-how-models-really-work.md))

### It forgot what we discussed earlier.

The context got long, was compacted, or you're in a new chat. Restate key facts, use Projects/memory/`CLAUDE.md`, or start
fresh with a summary.

### The answers are generic and bland.

Add **specifics**: audience, examples, constraints, your own opinions and stories. Ask it to avoid clichés. Give it samples of
the style you want.

### It keeps 'fixing' code and breaking other things.

Commit working states, ask it to **write tests first**, make one change at a time, and when looping, ask it to *step back and list
possible causes before changing code*. Or `/clear` and restart with a crisp description.

## 🔑 API & costs

### 401 / authentication error.

Check the key is set in the environment the code actually runs in (`echo $ANTHROPIC_API_KEY`), has no extra spaces, and
hasn't been revoked. Restart your terminal after setting it.

### My bill is higher than expected.

Check the usage dashboard per key. Common culprits: agent loops, huge tool results, max effort everywhere, no caching, and
processing items repeatedly. See [Ch. 39](../part-10-mastery/39-cost-optimization.md), and set spend limits now.

### Responses get cut off mid-sentence.

You hit `max_tokens`. Raise it (and use streaming for long outputs), or ask for a more concise format.

## 🏠 Local models & home lab

### Local models are painfully slow.

Use a smaller or more quantized model (e.g. a 4-bit quantization), close other heavy apps, make sure the GPU is actually being used, and
on Apple Silicon run Ollama **natively** rather than in Docker.

### Open WebUI can't see my Ollama models.

Inside Docker Compose use `http://ollama:11434`. For native Ollama on the host use `http://host.docker.internal:11434`. Then pull a model:
`docker compose exec ollama ollama pull gemma3`.

### Docker says a port is already in use.

Something else is running on that port. Change the left side of the mapping in `docker-compose.yml` (e.g. `"3001:8080"`).

## 🌐 This manual's website

### How do I publish the website version of this manual?

In the GitHub repo: **Settings → Pages → Source: GitHub Actions**. Then merge to `main`, and the `Manual website`
workflow builds and deploys it automatically.

### How do I build it locally?

`pip install -r requirements-docs.txt && mkdocs serve`, then open http://127.0.0.1:8000.

---

**Next:** [Appendix D · 100 Prompts That Use Tools →](d-100-prompts.md)
