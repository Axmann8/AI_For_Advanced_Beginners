# 20 · Calling AI APIs Directly 🔑🐍

Chat apps are wonderful, but the **API** is where AI becomes a programmable ingredient. It's how you
put AI in scripts, spreadsheets, bots, apps, and automations. This chapter gets you making real API calls
in minutes, then covers the patterns that matter: streaming, tool use, structured output, vision, and cost control.

Examples use Python and the Claude API (`anthropic` SDK). The same ideas apply to every provider.

---

## Step 0: Setup (5 minutes)

1. Create an account at **console.anthropic.com**, add a little credit, and **set a monthly spend limit**. 💸🛡️
2. Create an API key. Treat it like a password.
3. Install and configure:
   ```bash
   pip install anthropic
   export ANTHROPIC_API_KEY="sk-ant-..."     # macOS/Linux (Windows: setx ANTHROPIC_API_KEY "...")
   ```

## Step 1: Your first call

```python
import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

response = client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    messages=[{"role": "user", "content": "Give me 3 fun facts about octopuses 🐙"}],
)
print(response.content[0].text)
print(response.usage)  # input/output tokens: what you're billed for
```

### The anatomy of a request
| Field | Meaning |
|---|---|
| `model` | Which model (see the provider's model list; tiers trade capability for speed and cost) |
| `max_tokens` | The ceiling on the reply length. Don't set it too low, or answers get cut off |
| `system` | Standing instructions (persona, rules, format) |
| `messages` | The conversation: alternating `user` / `assistant` turns |
| `tools` | Functions the model may call (below) |

**APIs are stateless:** send the *whole* conversation each time. That's how "memory" works in chat apps.

```python
messages = [
    {"role": "user", "content": "My name is Sam."},
    {"role": "assistant", "content": "Nice to meet you, Sam!"},
    {"role": "user", "content": "What's my name?"},
]
```

## Step 2: Streaming (so it feels alive) 🌊

```python
with client.messages.stream(
    model="claude-opus-5",
    max_tokens=64000,
    messages=[{"role": "user", "content": "Write a short bedtime story about a brave toaster."}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)
```

Use streaming for anything long. Text appears as it's generated, and you avoid timeouts.

## Step 3: Structured output, getting data instead of prose 📦

Perfect for automations: extract fields into a validated Python object.

```python
from pydantic import BaseModel

class Event(BaseModel):
    title: str
    date: str
    location: str
    attendees: list[str]

response = client.messages.parse(
    model="claude-opus-5",
    max_tokens=16000,
    messages=[{"role": "user", "content":
        "Extract the event: 'Team picnic at Riverside Park on June 14, Priya, Sam and Lee are coming.'"}],
    output_format=Event,
)
event = response.parsed_output
print(event.title, event.date, event.attendees)
```

## Step 4: Tool use, letting the model call your functions 🔧

The SDK's **tool runner** handles the whole agent loop for you:

```python
from anthropic import beta_tool

@beta_tool
def get_weather(city: str) -> str:
    """Get the current weather for a city.

    Args:
        city: City name, e.g. "Lisbon".
    """
    return f"22°C and sunny in {city}"  # call a real weather API here

runner = client.beta.messages.tool_runner(
    model="claude-opus-5",
    max_tokens=16000,
    tools=[get_weather],
    messages=[{"role": "user", "content": "Should I pack a jacket for Lisbon today?"}],
)
for message in runner:          # each step of the loop
    print(message.content)
```

Want to see the loop *without* the helper? That's exactly what [Ch. 21](21-build-your-own-agent.md) and the
[build-your-own-agent kit](../../examples/build-your-own-agent/) show.

## Step 5: Vision & documents 👁️📄

```python
import base64, pathlib

image_b64 = base64.standard_b64encode(pathlib.Path("receipt.jpg").read_bytes()).decode()
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    messages=[{"role": "user", "content": [
        {"type": "image", "source": {"type": "base64", "media_type": "image/jpeg", "data": image_b64}},
        {"type": "text", "text": "List every item and price on this receipt, then the total."},
    ]}],
)
```

PDFs work similarly with `{"type": "document", ...}` blocks. Scanned forms, charts, and screenshots all become data.

## Step 6: Server-side tools (the provider runs them) 🌐

Some tools run on Anthropic's side, so you don't write any code for them: **web search**, **web fetch**, and **code execution**
(a sandbox where Claude runs Python). You just declare them in `tools`. Great for research bots and data analysis. Check the
current docs for tool type names, since they're versioned.

## Step 7: Make it cheap and fast 💸⚡

| Lever | What it does |
|---|---|
| **Right-size the model** | Smaller tiers for classification/extraction, and the big models for hard reasoning |
| **Effort / thinking controls** | Lower effort for simple tasks, higher for hard ones |
| **Prompt caching** | Reusing the same long prefix (instructions, documents) is much cheaper and faster on repeat calls |
| **Batch API** | Non-urgent bulk jobs at a big discount |
| **Trim context** | Send only what's needed |
| **Spend limits + usage logging** | Log `response.usage` to see where tokens go |

More in [Ch. 39: Cost Optimization](../part-10-mastery/39-cost-optimization.md).

## Step 8: Handle errors gracefully

```python
try:
    response = client.messages.create(...)
except anthropic.RateLimitError:
    print("Slow down: wait and retry")          # the SDK already retries a few times for you
except anthropic.APIStatusError as e:
    print("API error:", e.status_code, e.message)
except anthropic.APIConnectionError:
    print("Network problem")
```

Also check `response.stop_reason`: `"end_turn"` (done), `"max_tokens"` (cut off, so raise the limit), `"tool_use"` (wants a tool),
`"refusal"` (declined).

## Other providers & gateways 🌍
- **OpenAI, Google Gemini, Mistral, and others** all have similar SDKs: messages in, text or tool calls out.
- **OpenRouter** gives one key for hundreds of models, which is great for comparing them.
- **Local models** (Ollama, LM Studio) expose HTTP APIs on your machine ([Ch. 26](../part-7-local-ai/26-local-and-open-models.md)).
- **Cloud platforms** (AWS Bedrock, Google Vertex AI, Microsoft Foundry) offer Claude and others inside enterprise clouds.

## 🎮 Five weekend API projects
1. **Receipt → CSV** scanner for a folder of photos (vision + structured output)
2. **Email draft assistant** CLI: pipe in an email, get three reply options
3. **Journal prompt bot** that texts you a reflective question daily (Twilio or Telegram)
4. **Spreadsheet enricher:** add AI columns to a CSV (classify, summarize, translate)
5. **Research bot** with web search: *"Brief me on X with sources"* → Markdown file

---

### 🎮 Try this
Run the octopus example, then change one thing at a time: add a `system` prompt (*"You are a pirate"*), stream it,
and log `response.usage`. You'll understand API costs better than most people. 🏴‍☠️

---

**Next:** [21 · Build Your Own Agent →](21-build-your-own-agent.md)
