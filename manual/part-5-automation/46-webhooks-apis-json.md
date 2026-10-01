# 46 · Webhooks, APIs & JSON for Non-Programmers 🌐📦

> ⏱️ 8 min read · 🎯 Beginner-friendly, no coding required · 🧰 Needs: a terminal (optional) and curiosity

**Three concepts unlock *everything* in automation and AI integrations: JSON (how data looks), APIs (how apps talk), and
webhooks (how apps poke each other).** Learn them once and every tool in this manual gets easier, from n8n to MCP to
building your own apps. No coding degree required! 🎓

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Three concepts underpin almost every automation and integration, and you don't need to be a programmer to understand them.

- **JSON** is a format for structured, labeled data, such as `"name": "Pixel"`.
- **An API** is how one program requests data or actions from another, usually exchanging JSON.
- **A webhook** is a URL that receives a message the moment something happens in another app, so your automation can respond immediately.

</details>

<!-- in-this-chapter -->

## 📦 JSON: the universal data format

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

JSON stores data as labeled values in a strict, readable format. It uses objects (labeled fields in curly braces), arrays (lists in square brackets), strings, numbers, booleans and null, and these can be nested inside each other.

</details>

JSON is just **labeled data** in a strict, readable format:

```json
{
  "name": "Pixel",
  "species": "cat",
  "age": 4,
  "indoor": true,
  "favorite_toys": ["laser", "crinkle ball"],
  "vet": { "name": "Dr. Lee", "phone": "555-0199" },
  "middle_name": null
}
```

| Piece | Looks like | Example |
|---|---|---|
| **Object** | `{ "key": value }` | the whole thing above |
| **String** | `"text in quotes"` | `"Pixel"` |
| **Number** | `4`, `3.14` | `"age": 4` |
| **Boolean** | `true` / `false` | `"indoor": true` |
| **Array** (list) | `[ ... ]` | `["laser", "crinkle ball"]` |
| **Nested object** | an object inside an object | `"vet": {...}` |
| **Nothing** | `null` | `"middle_name": null` |

**Paths** point into JSON: `vet.name` → `"Dr. Lee"`, and `favorite_toys[0]` → `"laser"`. In n8n that's
`{{ $json.vet.name }}`, while in Zapier and Make you click the field in a picker.

## 🐛 Common JSON mistakes (and what the error means)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

JSON has strict syntax rules, and a single error makes the whole document invalid. The most common mistakes are trailing commas, single quotes and unquoted keys; the table shows each one corrected.

</details>

| Mistake | Broken | Fixed |
|---|---|---|
| Trailing comma | `{"a": 1,}` | `{"a": 1}` |
| Single quotes | `{'a': 1}` | `{"a": 1}` |
| Unquoted keys | `{a: 1}` | `{"a": 1}` |
| Comments | `{"a": 1 // note}` | Remove comments (strict JSON has none) |
| Smart quotes from a word processor | `{“a”: 1}` | Use plain `"` quotes |

💡 Paste broken JSON into your AI assistant with *"fix this JSON and explain what was wrong."* It's instant and educational.

## 🤖→📦 Getting JSON out of AI reliably

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

To get reliable JSON from an AI for use in automations:

1. Ask for JSON only, and show the exact structure you expect.
2. Use the platform's structured output or JSON mode if available.
3. Validate the result before the next step uses it.

</details>

When an automation needs AI output as data:

1. **Ask explicitly and show the shape:** *"Reply with ONLY a JSON object like {"title": string, "priority": "High" | "Low"}."*
2. **Use structured-output features** where available: structured output parsers in n8n, JSON schemas in APIs
   ([Calling AI APIs](../part-7-building-with-ai/67-calling-ai-apis.md)).
3. **Parse defensively:** strip ```` ``` ```` fences and have a fallback. Our
   [idea-inbox workflow](../../examples/n8n-workflows/idea-inbox-to-notion.json) does exactly this.

## 🚪 APIs: apps' front doors

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

An API lets one program ask another to read or change data. Most web APIs use HTTP requests, each made up of a method (such as GET or POST), a URL, headers (often including authentication) and, for some requests, a JSON body.

</details>

An **API** lets programs ask another app to do something. Most web APIs are **REST over HTTP**:

```text
METHOD   URL                                     → what it does
GET      https://api.example.com/v1/cats/42      → read cat #42
POST     https://api.example.com/v1/cats         → create a cat (data in the body)
PATCH    https://api.example.com/v1/cats/42      → update some fields
DELETE   https://api.example.com/v1/cats/42      → remove it
```

Every request has:

| Part | What | Example |
|---|---|---|
| **Method** | The verb | `GET`, `POST` |
| **URL** | The address, plus **query params** after `?` | `...?limit=10&sort=new` |
| **Headers** | Metadata, especially **auth** | `Authorization: Bearer sk-...` |
| **Body** | Data you send (usually JSON) | `{"name": "Pixel"}` |

## 🚦 Status codes: what the server is telling you

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Every API response includes a status code: 200-level codes mean success, 400-level codes mean a problem with the request, and 500-level codes mean a problem on the server. The table explains the most common codes and what to do about each.

</details>

| Code | Meaning | Your move |
|---|---|---|
| **200 / 201** | ✅ Success | Party 🎉 |
| **400** | Bad request: your data's wrong | Check the body, required fields and JSON syntax |
| **401 / 403** | Not authorized | Check the API key, token and scopes |
| **404** | Not found | Check the URL and IDs |
| **429** | Too many requests | Slow down, and add waits or retries |
| **500+** | The server broke | Retry later. Not your fault! |

## 🧪 Try an API right now (no key needed!)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

You can call a real API right now without signing up.

1. Open a terminal and run the command below.
2. Read the JSON that comes back, which includes the current temperature in London.
3. Try one of the other free APIs in the table.

</details>

```bash
curl "https://api.open-meteo.com/v1/forecast?latitude=51.5&longitude=-0.12&current=temperature_2m"
```

You'll get JSON with the current temperature in London. 🌤️ That's it, you just used an API.

**Free, no-key APIs to play with:**

| API | Fun use |
|---|---|
| **Open-Meteo** | Weather forecasts anywhere |
| **PokéAPI** | Every Pokémon's stats 🐉 |
| **REST Countries** | Flags, capitals, populations |
| **Open Library** | Book info by ISBN |
| **The Cat API / Dog CEO** | Random cat and dog pictures (essential research 🐶) |
| **Hacker News (Firebase)** | Top tech stories |
| **NASA APOD** (free demo key) | Astronomy picture of the day |

## 🔑 Authentication types

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

APIs authenticate requests with an API key, a bearer token or OAuth (signing in with your account). Automation platforms handle most of the complexity; your main job is keeping keys secret.

</details>

- **API key:** a secret string in a header or parameter. Simple, so **keep it secret**.
- **Bearer token:** similar, sent as `Authorization: Bearer <token>`.
- **OAuth:** the "Log in with Google" flow. Automation platforms handle it for you, and that's a big part of their value!
- **Webhook signatures:** a secret used to prove a webhook really came from the service (see below).

## 📖 Reading API docs (the skill nobody teaches)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

API documentation follows a common structure. Look for the base URL, the authentication section, the endpoint you need, its required parameters and an example request. You can also ask an AI assistant to read the docs and explain the request you need.

</details>

Look for:

1. The **base URL**.
2. The **authentication** section.
3. The **endpoint** you need (e.g. "Create a task").
4. **Required parameters** and body fields.
5. An **example request and response**.
6. **Rate limits** and **pagination** (how to get page 2 of results).

Or paste the docs page into your AI: *"Show me the exact HTTP request to do X with this API, as an n8n HTTP Request node
config."* Many docs also publish an **OpenAPI** spec, a machine-readable menu that tools (and AI) can use directly.

## 🔌 The HTTP Request node: the universal adapter

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Every automation platform has a general-purpose HTTP request step, so you can use any service with an API even if there's no built-in integration for it.

</details>

Every platform has one: n8n **HTTP Request**, Zapier **Webhooks by Zapier / API Request**, Make **HTTP**. If a service has an
API, you can use it even with no official integration.

**Pro tip:** API docs often show **curl** examples, and n8n can **import a curl command** directly into an HTTP Request node.
Desktop tools like **Bruno**, **Postman** or **HTTPie** let you experiment with requests in a friendly UI.

## 📞 Webhooks: "call me when something happens"

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

With **polling**, your automation checks for new data on a schedule. With a **webhook**, the other app sends data to your URL the instant something happens. Webhooks are faster and more efficient whenever an app supports them.

</details>

**Polling** = *you* checking every 5 minutes for something new. 😴
**Webhook** = the app *calls your URL* the instant something happens. ⚡

```mermaid
sequenceDiagram
    participant S as Stripe (or any app)
    participant W as Your webhook URL (n8n/Zapier/Make)
    participant AI as Claude
    S->>W: POST {"type": "payment.succeeded", "amount": 4900, ...}
    W->>AI: "Write a thank-you note for this customer"
    AI-->>W: "Hi Sam! Thanks so much for..."
    W->>S: (sends email via another app)
```

**Making your own webhook:**

1. Add a **Webhook** trigger (n8n), **Catch Hook** (Zapier) or **Custom webhook** (Make). You get a URL.
2. Send it data from anywhere: an app's webhook settings, a form, an iOS Shortcut, or curl:
   ```bash
   curl -X POST "https://your-n8n/webhook/idea-inbox" \
     -H "Content-Type: application/json" \
     -d '{"text": "Build a plant-watering reminder bot"}'
   ```
3. Your workflow runs with that JSON as input. ✨

**Testing tip:** services like **webhook.site** give you a temporary URL that shows every request it receives, which is perfect
for seeing what an app actually sends before building your workflow.

## 📱 Phone superpower: Shortcuts → webhook

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

You can build a phone shortcut that sends dictated text to a webhook, so a spoken idea lands in your notes automatically.

1. Create a webhook in your automation platform and copy its URL.
2. In the iPhone Shortcuts app, add **Dictate Text** and **Get Contents of URL** (POST, with the dictated text in a JSON body).
3. Add the shortcut to your home screen or Action button.

</details>

On iPhone: **Shortcuts app** → new shortcut → **Dictate Text** → **Get Contents of URL** (method POST, JSON body
`{"text": Dictated Text}`, URL = your webhook). Add it to your home screen or Action Button. Now you can **speak ideas straight
into your AI workflows.** On Android, use Tasker or HTTP Shortcuts. More in [Phone & Desktop Automation](50-phone-and-desktop-automation.md).

## 🔒 Webhook security basics

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Treat webhook URLs like passwords and don't share them publicly. Add a secret header check, and use signature verification where the sending service supports it.

</details>

- Webhook URLs are like passwords, so **don't share them publicly**.
- Add a **secret header** check (`X-Secret: …`) or use the platform's auth options.
- For services like Stripe and GitHub, **verify signatures** (they document how).
- Local n8n isn't reachable from the internet, so use n8n Cloud, a VPS, or a tunnel (Cloudflare Tunnel, ngrok) for testing.

## 📏 Rate limits, pagination & retries

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

APIs limit how fast you can send requests (a 429 error means slow down) and return large lists in pages. Add waits between requests, follow pagination to collect every page, and retry failed requests with increasing delays.

</details>

- **Rate limits:** too many requests → `429`. Add **Wait** nodes, batch items, and respect `Retry-After` headers.
- **Pagination:** big lists come in pages (`?page=2`, cursors, or "next" links). Loop until there are no more.
- **Retries:** enable *retry on fail* with increasing waits for flaky APIs, but don't blindly retry `400` errors, because the
  request itself is wrong.
- **Idempotency:** for "create" actions, some APIs accept an idempotency key so a retry doesn't create duplicates.

## 🧩 Putting it all together

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Nearly every integration follows the same sequence: an event triggers a JSON message, the automation reshapes the data, AI processes it, and an API call takes action in another app. The same pattern appears in MCP and in AI agents.

</details>

```text
Something happens ─(webhook/trigger)─▶ JSON arrives ─▶ transform ─▶ AI step ─▶ JSON ─▶ API call to act
```

You'll see this pattern everywhere: in MCP (tool calls are JSON, and servers call APIs), in agents, and in every automation.
**You now speak the language of the internet's plumbing.** 🔧

## 🎯 Key takeaways

- **JSON** = labeled data with strict syntax. **APIs** = method + URL + headers + body. **Webhooks** = apps calling *you*.
- Status codes tell you **whose fault** an error is (4xx: yours, 5xx: theirs).
- Ask AI for **JSON with a shown shape** when machines read its output.
- The **HTTP Request node** lets you use any API, even without an official integration.
- Protect webhooks with **secrets and signature checks**, and handle **rate limits and pagination**.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. What's wrong with <code>{'name': 'Pixel',}</code>?</summary>

Two things: **single quotes** (JSON needs double quotes) and a **trailing comma**.

</details>

<details class="quiz">
<summary>❓ 2. Your request returns 401. What do you check?</summary>

Your **API key or token**: is it present, correct, and does it have the right scopes?

</details>

<details class="quiz">
<summary>❓ 3. Why is a webhook better than polling for "new payment" events?</summary>

It's **instant** and **efficient**: the app notifies you the moment it happens instead of you asking repeatedly.

</details>

> [!TIP]
> **🎮 Try this**
> 1. Create a webhook in your automation tool of choice. 2. Hit it with the `curl` command above (or the iOS Shortcut).
> 3. Add an AI step that turns the text into a structured JSON task and sends it to your task app.
> Congratulations: you've built an **AI-powered API** in 15 minutes. 🎉

---

**Next:** [47 · The n8n Masterclass →](47-n8n-masterclass.md)
