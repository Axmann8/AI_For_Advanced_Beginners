# 82 · Build-Along: Publish Your Own MCP Server ☔📦

> ⏱️ ~3 hours to build · 🎯 Intermediate (copy-paste friendly) · 🧰 Needs: Node.js 18+, a GitHub account, an npm account, Claude Code or Claude Desktop

**In this build-along you'll take a real MCP server from "works on my machine" to "anyone in the world can install it."**
You'll run and test Weather Buddy (live weather, forecasts and packing advice from the free Open-Meteo API), make it yours
with a new tool, connect it to Claude, publish it to **npm**, list it in the **official MCP Registry**, and optionally host it
as a **remote server**. By the end, you're an MCP author. 🎉

<details class="eli5" open>
<summary>🧸 ELI5: This build in 30 seconds</summary>

An MCP server is a plug-in that gives AI a new skill. We'll take a weather plug-in, test it, add your own twist, and then put
it in the world's "plug-in shop" (npm and the MCP Registry) so anyone can install it with one line. It's like writing a
little app and putting it in an app store. ☔🛍️

</details>

<!-- in-this-chapter -->

## 🗺️ What you'll build

<details class="eli5">
<summary>🧸 ELI5</summary>

You'll test the plug-in on your computer, connect it to Claude, then share it on npm and the MCP Registry, and maybe put it on
the internet too.

</details>

```mermaid
flowchart LR
    K[📁 weather-mcp-server kit] --> T[🧪 Test<br/>npm test + Inspector]
    T --> Y[🎨 Make it yours<br/>new tool]
    Y --> C[🤖 Connect to Claude]
    C --> N[📦 npm publish]
    N --> R[🗂️ MCP Registry<br/>mcp-publisher]
    Y -.optional.-> H[🌍 Remote hosting<br/>Docker + HTTP]
```

**The kit:** [`examples/weather-mcp-server`](../../examples/weather-mcp-server/) has three tools, a stdio mode, a stateless
Streamable HTTP mode with optional bearer-token auth, an offline smoke test, a `server.json` for the registry, and a
`Dockerfile`. Background reading: [Building MCP Servers](../part-2-mcp-and-connectors/11-building-mcp-servers.md).

## ✅ Before you start

<details class="eli5">
<summary>🧸 ELI5</summary>

Make sure you have Node.js installed and accounts on GitHub and npm (both free).

</details>

- [ ] **Node.js 18+** (`node --version`)
- [ ] A **GitHub** account (your registry namespace will be `io.github.your-username`)
- [ ] An **npm** account (`npm adduser` to log in)
- [ ] **Claude Code** or **Claude Desktop** to try your server
- [ ] Optional: **Docker** and a host (Render, Railway, Fly.io, Cloud Run) for remote hosting

## 1️⃣ Step 1: Run and test the kit (15 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

Download the parts, then run the automatic test that checks everything works, without even needing the internet.

</details>

```bash
cd examples/weather-mcp-server
npm install
npm test
```

You should see:

```text
✅ stdio: 3 tools, ⛅ Lisbon, Lisbon, Portugal: partly cloudy, 21°C (feels like 21°C), wind 14 km/h.
✅ http: 3 tools, ⛅ Lisbon, Lisbon, Portugal: partly cloudy, 21°C (feels like 21°C), wind 14 km/h.
🎉 All weather-buddy checks passed.
```

The test starts a **fake weather API**, then talks to your server in **both** modes (stdio and HTTP), checks every tool, and
checks that the HTTP mode rejects requests without the right token. Tests that need no internet are tests you'll actually run.

> ✅ **Checkpoint:** `npm test` passes.

## 2️⃣ Step 2: Explore it in the MCP Inspector (15 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

The Inspector is a test window where you can press your plug-in's buttons yourself and see exactly what the AI would see.

</details>

```bash
npm run inspect
```

1. The **MCP Inspector** opens in your browser. Click **Connect**.
2. Open **Tools** → `get_forecast` → enter `{"city": "Reykjavik", "days": 4}` → **Run**. You get a real forecast. 🌦️
3. Try `packing_advice` for somewhere hot, then somewhere snowy.
4. Try a nonsense city. The server answers with a friendly message instead of crashing.

Look at how each tool has a **title**, **description**, **input schema** and **annotations** (`readOnlyHint`): that's the
"instruction manual" the AI reads to decide when to use it.

> ✅ **Checkpoint:** all three tools return real weather in the Inspector.

## 3️⃣ Step 3: Make it yours (45 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

Add your own new button to the plug-in, like "is it a good day for a picnic?" Your AI coding helper can write most of it.

</details>

Pick one idea (or invent your own) and add a fourth tool:

| Idea | Tool |
|---|---|
| 🧺 Picnic checker | `picnic_score(city, date)`: 0–10 score based on rain, wind and temperature |
| 🌫️ Air quality | `get_air_quality(city)` using Open-Meteo's free air-quality API |
| 🏃 Run planner | `best_time_to_run(city)`: the coolest dry hour tomorrow |
| 🌡️ Fahrenheit | Add a `units` parameter to every tool |

**Let Claude Code pair with you:**

> *"In examples/weather-mcp-server, add a `picnic_score` tool: 0–10 based on the forecast for a given date, with a one-line
> reason. Follow the style of the existing tools (title, description, zod schema, readOnlyHint, friendly errors). Extend
> smoke-test.mjs to cover it, including the fake API. Run npm test until it passes."*

Then **update the version** in `package.json` and `server.json` (e.g. `1.1.0`: new features bump the middle number).

> ✅ **Checkpoint:** your new tool works in the Inspector, and `npm test` still passes.

## 4️⃣ Step 4: Connect it to Claude (10 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

Plug your new skill into Claude and ask it about the weather. Claude will use your plug-in to answer.

</details>

=== "💻 Claude Code"

    ```bash
    claude mcp add weather-buddy -- node /full/path/to/examples/weather-mcp-server/server.mjs
    claude
    ```

=== "🖥️ Claude Desktop"

    Add this to your config (Settings → Developer → Edit Config), then restart Claude Desktop:

    ```json
    {
      "mcpServers": {
        "weather-buddy": { "command": "node", "args": ["/full/path/to/examples/weather-mcp-server/server.mjs"] }
      }
    }
    ```

Ask: *"I'm going to Edinburgh for 4 days next week. What should I pack, and which day is best for a long walk?"* Watch Claude
call your tools. 🤩

> ✅ **Checkpoint:** Claude answers using **your** server's tools (you'll see the tool calls).

## 5️⃣ Step 5: Prepare for publishing (20 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

Before putting your plug-in in the shop, give it your name, a good description and a clear instruction page.

</details>

1. **Create a GitHub repo** for your server (e.g. `weather-buddy-mcp`) and copy the kit's files into it (`server.mjs`,
   `package.json`, `server.json`, `README.md`, `Dockerfile`, `smoke-test.mjs`).
2. **Replace `your-github-username`** everywhere in `package.json` and `server.json`. Three fields must line up:

    | File | Field | Example |
    |---|---|---|
    | `package.json` | `name` | `@alexrivera/weather-buddy-mcp` |
    | `package.json` | `mcpName` | `io.github.alexrivera/weather-buddy` |
    | `server.json` | `name` (must equal `mcpName`) and `packages[0].identifier` (must equal the npm name) | as above |

3. **Polish the README:** what it does, a one-line install, example questions, and the tools table.
4. **Add a license** (MIT is a friendly default) and push to GitHub.

> [!TIP]
> **💡 A listing people love**
> Great MCP READMEs show **example prompts**, a **copy-paste config**, and a **screenshot or GIF** of Claude using the tools.
> Ask Claude: *"Review my README like a first-time user. What's confusing or missing?"*

## 6️⃣ Step 6: Publish to npm (10 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

npm is the giant shop for JavaScript packages. Publishing puts your plug-in there so anyone can download it with one command.

</details>

```bash
npm login
npm test                       # never publish without a green test!
npm publish --access public    # scoped packages (@you/...) need --access public the first time
```

Now anyone can run your server with **no download or install step**:

```json
{
  "mcpServers": {
    "weather-buddy": { "command": "npx", "args": ["-y", "@alexrivera/weather-buddy-mcp"] }
  }
}
```

> ✅ **Checkpoint:** your package page appears on npmjs.com, and the `npx` config above works in Claude.

## 7️⃣ Step 7: List it in the MCP Registry (15 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

The MCP Registry is the official list of plug-ins that AI apps can search. Adding yours helps people find it.

</details>

The **official MCP Registry** is where clients and catalogs discover servers. It points to your npm package, and verifies you
own it via the `mcpName` field.

```bash
# install the publisher CLI (or download a release binary from the registry's GitHub repo)
brew install mcp-publisher

mcp-publisher login github     # proves you own io.github.your-username
mcp-publisher publish          # reads server.json and publishes the listing
```

> [!NOTE]
> **📌 Check the current docs**
> The registry and its `server.json` schema are evolving. If `publish` complains, compare your file with the latest schema
> linked in `$schema`, and check the registry's quickstart on GitHub.

> ✅ **Checkpoint:** searching the registry for your server's name shows your listing. 🎉 You're a published MCP author!

## 🌍 Step 8 (optional): Host it as a remote server

<details class="eli5">
<summary>🧸 ELI5</summary>

You can also run your plug-in on a computer on the internet, so it works from phones and web apps without anyone installing
anything.

</details>

Remote servers work from Claude on the web and mobile, and from other people's apps, with nothing to install
([Deploying & Hosting](../part-5-building-with-ai/35-deploying-and-hosting.md#-hosting-a-remote-mcp-server)).

1. **Try it locally:** `MCP_AUTH_TOKEN=a-long-random-secret npm run http` → the endpoint is `http://localhost:3000/mcp`.
2. **Deploy the Dockerfile** to Render, Railway, Fly.io or Google Cloud Run. Set `MCP_AUTH_TOKEN` as a secret.
3. **Connect:**

    ```bash
    claude mcp add --transport http weather-buddy https://your-host.example.com/mcp \
      --header "Authorization: Bearer a-long-random-secret"
    ```

4. **Check health:** `https://your-host.example.com/health` should return `{"ok":true}`.

> [!WARNING]
> **🔐 Auth matters**
> A shared bearer token is fine for **personal** use. For a public, multi-user server, use proper **OAuth**, add rate limits,
> and log carefully ([MCP Security & Trust](../part-2-mcp-and-connectors/12-mcp-security-and-trust.md)). Weather is harmless,
> but the habits matter for the next server you build.

## 🔁 Maintaining your server

<details class="eli5">
<summary>🧸 ELI5</summary>

After you share it, keep your plug-in healthy: fix bugs, add features, and give each new version a new number.

</details>

| Habit | How |
|---|---|
| **Semantic versioning** | Fixes → `1.0.1`, new features → `1.1.0`, breaking changes → `2.0.0` |
| **Test before every publish** | `npm test`, and add a test for every bug you fix |
| **CI** | A GitHub Action that runs `npm test` on every push ([Git & GitHub](../part-5-building-with-ai/30-git-and-github.md#-github-actions-robots-that-work-for-you)) |
| **Update both files** | Bump `version` in `package.json` *and* `server.json`, then publish to npm and the registry |
| **Listen to users** | GitHub issues are gold: they tell you what to build next |

## 🩺 Troubleshooting

<details class="eli5">
<summary>🧸 ELI5</summary>

If something doesn't work, here are the usual suspects and how to fix them.

</details>

| Problem | Fix |
|---|---|
| Claude doesn't see the tools | Use the **full path** to `server.mjs`, restart Claude, check `claude mcp list` or Desktop's MCP logs |
| `npm publish` 403 / 402 | Scoped package? Add `--access public`. Name taken? Pick another |
| Registry rejects the listing | `server.json` `name` must equal `mcpName`, and `identifier`/`version` must match what's on npm |
| "fetch failed" in tools | No internet or a blocked network. The smoke test still passes because it uses a fake API |
| HTTP mode returns 401 | Send `Authorization: Bearer <token>` exactly |
| Works locally, not remotely | Check the host's logs, `PORT`, and that the path is `/mcp` |

## 🎯 Key takeaways

- A **publishable** MCP server = good tools + tests + a README + matching `package.json`/`server.json`.
- **Test offline** with a fake API, and explore interactively with the **MCP Inspector**.
- **npm** makes installation a one-liner (`npx`), and the **MCP Registry** makes you discoverable.
- **Remote hosting** (Streamable HTTP) works everywhere, and needs real auth for public use.
- Maintain with **semantic versions, CI and user feedback**.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Which three names must line up for the registry?</summary>

`package.json` **`mcpName`** = `server.json` **`name`**, and `server.json` **`packages[0].identifier`** = the **npm package name**.

</details>

<details class="quiz">
<summary>❓ 2. Why does the smoke test use a fake weather API?</summary>

So tests run **offline, fast and reliably** (in CI too), without depending on someone else's service.

</details>

<details class="quiz">
<summary>❓ 3. You added a new tool. What version number should you publish?</summary>

A **minor** bump, e.g. `1.0.0` → **`1.1.0`** (new feature, nothing broken).

</details>

> [!TIP]
> **🎮 Try this**
> Once it's published, share your server's one-line `npx` config with a friend and ask them to plan a weekend trip with Claude
> using it. Watching someone else use a tool *you* made is the best feeling in software. ☔🎉

---

**Next:** [83 · The Second Brain →](83-build-along-second-brain.md)
