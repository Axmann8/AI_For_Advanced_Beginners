# 39 · MCP Under the Hood: The Protocol, Demystified 🔬🔌

> ⏱️ 9 min read · 🎯 Intermediate (no coding required to follow) · 🧰 Needs: optional, Node.js for the MCP Inspector

**What actually travels between Claude and an MCP server?** This chapter opens the hood: the messages, the conversation
flow, how tools/resources/prompts are described, how data moves locally and over the internet, how login works, and what
changed in the big 2026 spec. You'll finish able to *read* MCP traffic and debug servers like a pro.

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

This chapter explains how MCP works at the protocol level: the messages exchanged, how they travel, and how authorization works. Understanding it makes building and debugging servers much easier.

- **Two layers:** the data layer (JSON-RPC messages) and the transport layer (stdio or Streamable HTTP).
- **A typical session:** initialize, list tools, then call tools as the model requests them.
- **Remote servers** use OAuth 2.1 so the AI app never sees your password.
- **Hands-on:** use the MCP Inspector to watch the messages yourself.

</details>

<!-- in-this-chapter -->

## 🧱 Two layers: the letters and the mail truck

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

MCP has two layers. The **data layer** defines the messages (what you can ask and what comes back). The **transport layer** defines how those messages are delivered: stdio for local servers, Streamable HTTP for remote ones.

</details>

| Layer | What it defines | Options |
|---|---|---|
| ✉️ **Data layer** | The messages: what you can ask, what comes back | JSON-RPC 2.0 messages: `tools/list`, `tools/call`, `resources/read`… |
| 🚚 **Transport layer** | How messages physically travel | **stdio** (local process) or **Streamable HTTP** (network) |

Because these are separate, the same server logic can run locally *or* remotely just by switching transports, which is
exactly what the Pocket Toolkit examples do ([Building MCP Servers](42-building-mcp-servers.md)).

## ✉️ JSON-RPC in 60 seconds

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

MCP messages use JSON-RPC 2.0, a simple format with three message types: a **request** (with an ID, a method and parameters), a **response** (matching that ID) and a **notification** (no reply expected).

</details>

MCP messages use **JSON-RPC 2.0**, a tiny, decades-old convention with three message types:

**1. Request** (expects an answer):

```json
{
  "jsonrpc": "2.0",
  "id": 7,
  "method": "tools/call",
  "params": { "name": "roll_dice", "arguments": { "notation": "2d6" } }
}
```

**2. Response** (answers request #7):

```json
{
  "jsonrpc": "2.0",
  "id": 7,
  "result": {
    "content": [{ "type": "text", "text": "🎲 2d6: [3, 5] = **8**" }],
    "isError": false
  }
}
```

**3. Notification** (no answer expected, just FYI):

```json
{ "jsonrpc": "2.0", "method": "notifications/tools/list_changed" }
```

That's it. Every MCP feature is built from these three shapes. 🎉

## 🔄 The conversation, step by step

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

A session follows a predictable sequence: the client initializes the connection, asks the server what it offers, and then calls tools as the model requests them. The core methods are listed below.

</details>

```mermaid
sequenceDiagram
    autonumber
    participant H as Host + client (Claude Desktop)
    participant S as MCP server (Pocket Toolkit)
    H->>S: tools/list
    S-->>H: [roll_dice, random_fortune, save_note, list_notes] + schemas
    Note over H: The model sees these tools<br/>alongside your message
    H->>S: tools/call roll_dice {"notation": "4d6"}
    S-->>H: content: "🎲 4d6: [6, 2, 5, 4] = 17"
    H->>S: resources/read notes://all
    S-->>H: contents: [ {...json...} ]
    S--)H: notifications/tools/list_changed
    H->>S: tools/list (refresh)
```

**The core methods you'll see most:**

| Method | Direction | Purpose |
|---|---|---|
| `tools/list` | app → server | "What tools do you have?" |
| `tools/call` | app → server | "Run this tool with these arguments." |
| `resources/list`, `resources/read` | app → server | Browse and read data the server exposes |
| `resources/templates/list` | app → server | Discover parameterized resources like `recipes://{id}` |
| `prompts/list`, `prompts/get` | app → server | Discover and fill in prompt templates |
| `notifications/…/list_changed` | server → app | "My list of tools, resources or prompts changed" |

Older protocol versions started every connection with an `initialize` handshake to agree on a version and capabilities.
The **2026-07-28** spec removed that in favor of **stateless, self-describing requests**. The SDKs handle version details for
you, so you rarely think about it.

## 🔧 Tools up close

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Each tool definition includes a name, a description, an input schema describing the required arguments, and optional annotations such as whether the tool is read-only or destructive. The table explains why each field matters.

</details>

A tool definition from `tools/list` looks like this:

```json
{
  "name": "save_note",
  "title": "Save note",
  "description": "Save a short note to the local notes file, with an optional tag.",
  "inputSchema": {
    "type": "object",
    "properties": {
      "text": { "type": "string" },
      "tag": { "type": "string", "default": "general" }
    },
    "required": ["text"]
  },
  "annotations": { "readOnlyHint": false, "destructiveHint": false }
}
```

| Field | Why it matters |
|---|---|
| `name` | What the model calls. Keep it clear: `search_orders`, not `do_stuff` |
| `description` | **The model's only manual.** It explains when to use the tool and what it returns |
| `inputSchema` | JSON Schema for the arguments: types, required fields, enums, defaults |
| `outputSchema` (optional) | Lets tools return **structured content** that machines can rely on |
| `annotations` | Hints like read-only, destructive, idempotent, open-world, so apps can decide when to ask you |

**Errors are results too.** A tool that fails returns `"isError": true` with a helpful message, so the model can adapt
("file not found → let me list the folder first") instead of the whole conversation crashing.

## 📄 Resources & prompts up close

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

**Resources** are data identified by URIs, similar to web addresses, that the app can read. **Prompts** are reusable templates with arguments that users choose from a menu.

</details>

**Resources** are identified by **URIs** (like web addresses):

| Example URI | Means |
|---|---|
| `file:///Users/you/notes/todo.md` | A file |
| `notes://all` | Everything in the Pocket Toolkit's notes |
| `recipes://{id}` | A **template**: `recipes://42` gets recipe 42 |
| `postgres://db/schema` | A database's schema |

Apps usually let **you** attach resources to a conversation (for example with an `@` menu), and clients can **subscribe**
to changes on a resource.

**Prompts** are named templates with arguments (`daily_standup(focus)`), and many apps show them as **slash commands**.
`prompts/get` returns ready-to-send messages with your arguments filled in.

## 🚚 Transports: local and remote

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

With **stdio**, the app launches the server as a local process and exchanges messages through standard input and output. With **Streamable HTTP**, the app sends HTTP requests to a URL and can receive streamed responses. The messages are identical either way.

</details>

| | 🏠 **stdio** | ☁️ **Streamable HTTP** |
|---|---|---|
| How | The app launches the server as a child process and writes JSON lines to its stdin, reading replies from stdout | The app sends HTTP POST requests to one endpoint (e.g. `https://…/mcp`), and the server can stream results |
| Best for | Local tools, files, dev machines | SaaS integrations, shared team servers |
| Auth | Inherits your local permissions (plus env vars for API keys) | **OAuth 2.1** or tokens in headers |
| Gotcha | **Never print to stdout**, because it corrupts the protocol! Log to stderr | Needs HTTPS, auth, and rate limiting |

**What the 2026 spec changed for HTTP (you'll see these in logs):**

- **Stateless:** no session IDs, and every request carries what it needs, so servers scale behind ordinary load balancers.
- **Routing headers:** the method and tool name travel in `Mcp-Method` and `Mcp-Name` HTTP headers, so gateways can route
  and authorize without parsing JSON bodies.
- **Cacheable lists:** `tools/list` and friends can include cache hints (`ttlMs`, `cacheScope`).
- **Multi round-trip requests** replace server-initiated calls: when a tool needs your input mid-call, the server returns a
  request for more information, and the client calls back with the answer.
- **Legacy HTTP+SSE transport** (from the early days) is officially deprecated.

## 🔐 Authorization in one page

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Remote MCP servers use OAuth 2.1. You sign in with the actual service, which issues the app a token limited to specific permissions (scopes). The AI app never sees your password, and you can revoke access at any time.

</details>

Remote MCP servers use **OAuth 2.1**, the same family of standards behind every "Sign in with Google" button:

```mermaid
sequenceDiagram
    participant You
    participant App as MCP client (Claude)
    participant S as MCP server
    participant AS as Login server (e.g. Notion)
    App->>S: Request without a token
    S-->>App: 401 + "here's where to log in" (protected resource metadata)
    App->>You: Opens a browser login
    You->>AS: Log in and approve scopes
    AS-->>App: Access token (limited scopes, expires)
    App->>S: Requests with Bearer token
```

Key ideas:

- **Scopes** limit what the token can do (read-only vs. write, specific workspaces).
- Tokens **expire** and can be **revoked** from the service's settings.
- The spec now prefers **Client ID Metadata Documents** over dynamic client registration, and requires stricter issuer
  validation. For users this all happens behind one "Connect" button.
- **Local** servers usually use **API keys in environment variables** instead. Keep them out of shared files!

## 🧩 Extensions & advanced features

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Optional extensions add advanced capabilities: long-running **Tasks**, **MCP Apps** that display interactive interfaces in the chat, and **elicitation**, which lets a server ask you for input. The table shows each one's status.

</details>

| Feature | What it enables | Status (2026) |
|---|---|---|
| **Tasks** | Start a long job, poll `tasks/get`, update with `tasks/update` | Official extension |
| **MCP Apps** | Tools return interactive UI (forms, charts, pickers) rendered in the chat | Official extension, powers app/plugin UIs in major clients |
| **Asking the user** (elicitation → multi round-trip requests) | "Which calendar?" or "Confirm delete?" mid-call | Core feature, redesigned for stateless |
| **Enterprise Managed Authorization** | Companies control which servers and scopes employees may use | Official extension |
| **Sampling, Roots, Logging** | Older server-initiated features | **Deprecated** (still working during a transition window) |

## 🕰️ A tiny spec timeline

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

MCP versions are named by release date. The table summarizes each version's major changes, from the original 2024 release to today.

</details>

| Version | Highlights |
|---|---|
| **2024-11-05** | The original public release: tools, resources, prompts, stdio and HTTP+SSE |
| **2025-03-26** | **Streamable HTTP** transport, OAuth-based authorization, tool annotations |
| **2025-06-18** | **Elicitation** (asking the user), **structured tool output**, auth hardening |
| **2025-11-25** | Experimental **Tasks**, Client ID Metadata Documents, more auth improvements (first-anniversary release) |
| **2026-07-28** | **Stateless core**, routing headers, cacheable lists, multi round-trip requests, formal extensions (Tasks, MCP Apps) |

Specs are published at [modelcontextprotocol.io](https://modelcontextprotocol.io). Clients and servers negotiate versions,
and SDKs usually support several at once.

## 🔍 Watch the wire yourself (hands-on)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

The MCP Inspector is a free web tool for exploring any server directly.

1. Launch it with the command below, pointing it at a server.
2. Click **List Tools** to see the exact definitions the model receives.
3. Choose a tool, enter arguments and click **Run** to see the raw response.

</details>

The **MCP Inspector** is a web UI for any server:

```bash
# Inspect the official Memory server
npx @modelcontextprotocol/inspector npx -y @modelcontextprotocol/server-memory

# Inspect this manual's Pocket Toolkit (from its folder, with its venv active)
npx @modelcontextprotocol/inspector python server.py
```

In the Inspector:

1. Click **List Tools**. You'll see the exact JSON the model sees.
2. Pick a tool, fill in arguments, click **Run**, and read the raw result.
3. Open the **history** panel to see every request and response.
4. Try breaking things (wrong argument types) and see how errors come back.

Ten minutes of this and MCP will never feel like magic again, in the best way.

## 🎯 Key takeaways

- MCP = **JSON-RPC messages** (data layer) over **stdio or Streamable HTTP** (transport layer).
- The core loop is **`tools/list` → `tools/call`**, plus resources and prompts.
- Tool **descriptions and schemas** are what the model actually reads, and **errors are results** too.
- Remote servers use **OAuth 2.1** with scopes, and local servers use env-var API keys.
- The **2026-07-28 spec** made MCP stateless, cache-friendly and gateway-friendly, and formalized Tasks and MCP Apps.
- The **MCP Inspector** lets you see and poke everything.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. What are the three JSON-RPC message types?</summary>

**Request** (has an `id`, expects a response), **response** (same `id`, has `result` or `error`), and **notification**
(no `id`, no response).

</details>

<details class="quiz">
<summary>❓ 2. Why must a stdio server never print debug text to stdout?</summary>

Because **stdout is the protocol channel**. Extra text corrupts the JSON stream and the client disconnects. Log to stderr.

</details>

<details class="quiz">
<summary>❓ 3. A tool fails because a file is missing. Should the server crash or return something?</summary>

Return a **tool result with `isError: true`** and a helpful message, so the model can recover.

</details>

<details class="quiz">
<summary>❓ 4. What's the big architectural change in the 2026-07-28 spec?</summary>

A **stateless core**: no handshake or session IDs, and self-describing requests, so remote servers scale like normal web APIs.

</details>

> [!TIP]
> **🎮 Try this**
> Run the MCP Inspector against the [Pocket Toolkit](../../examples/my-first-mcp-server/) and call `roll_dice` with
> `"banana"` as the notation. Look at how the error comes back as a friendly result instead of a crash. Then peek at the
> raw `tools/list` JSON and find the description the model reads. 🔍

---

**Next:** [40 · The Big MCP Server Catalog →](40-mcp-server-catalog.md)
