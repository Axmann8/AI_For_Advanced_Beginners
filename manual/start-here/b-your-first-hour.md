# ⚡ Your First Hour: 60 Minutes to AI Superpowers

> ⏱️ 60 min hands-on · 🎯 Beginner-friendly · 🧰 Needs: a computer, a free Claude account (ChatGPT works too)

**This is the fastest route from "I use AI to answer questions" to "my AI reads my files, browses the web, remembers me,
and runs a little automation."** Six mini-missions, ten minutes each. Grab a drink, put on a good playlist, and let's go. 🎧

<details class="eli5" open>
<summary>🧸 ELI5: This hour in 30 seconds</summary>

In one hour you'll give your AI friend **eyes** (it reads your stuff), **hands** (it does things), a **memory** (it
remembers you), and a **little robot helper** that works while you're away. Each mission is a small step, and every step
ends with a "wow" moment.

</details>

<!-- in-this-chapter -->

## 🗺️ The plan

<details class="eli5">
<summary>🧸 ELI5</summary>

Six small missions. Do them in order and you'll feel like a wizard by the end.

</details>

| Time | Mission | Superpower |
|---|---|---|
| 0–10 min | 1. Connect your own data | 👀 Eyes |
| 10–20 min | 2. Install your first MCP servers | 🖐️ Hands |
| 20–30 min | 3. Give your AI a memory | 🧠 Memory |
| 30–40 min | 4. Build a mini app in chat | 🛠️ Creation |
| 40–50 min | 5. Create a reusable assistant | 🎭 Personality |
| 50–60 min | 6. Your first automation | 🤖 Autopilot |

## 1️⃣ Connect your own data (0–10 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

We'll let the AI peek at *your* files (with your permission) so it can answer questions about your real life instead of
the whole internet.

</details>

1. Open **Claude** (claude.ai or the desktop app) → **Settings → Connectors**.
2. Connect **one** thing you actually use: Google Drive, Gmail, Google Calendar, Notion, or GitHub.
3. Start a new chat and ask:
   > *"Based on my recent files, what are the 3 things I've been working on most this month? Anything I seem to have forgotten?"*
4. Then try:
   > *"What's on my calendar this week, and what should I prepare for each meeting?"*

**The wow:** the first time AI answers from *your* data, something clicks. You'll never look at chatbots the same way. 💡

> [!NOTE]
> **📌 Using ChatGPT or Gemini instead?**
> Same idea: ChatGPT has connectors and plugins in its settings, and Gemini connects to Gmail, Drive and Calendar
> natively. See [Built-in Connectors](../part-4-mcp-and-connectors/41-built-in-connectors.md).

## 2️⃣ Install your first MCP servers (10–20 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

Now we give the AI "hands": a little program that lets it create files in a safe play folder, and another that lets it
read any web page.

</details>

1. Install **Claude Desktop** (claude.ai/download) and **Node.js** (nodejs.org, LTS version).
2. Create a folder named `ai-playground` in your home folder.
3. In Claude Desktop: **Settings → Developer → Edit Config**. Paste this, replacing `YOU` with your username:

    ```json
    {
      "mcpServers": {
        "playground": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-filesystem", "/Users/YOU/ai-playground"]
        },
        "memory": {
          "command": "npx",
          "args": ["-y", "@modelcontextprotocol/server-memory"]
        }
      }
    }
    ```

    (On Windows, the path looks like `C:\\Users\\YOU\\ai-playground`, with doubled backslashes.)

4. **Fully quit** Claude Desktop and reopen it. You should see the tools icon with new tools listed.
5. Ask:
   > *"Create a file called `bucket-list.md` in my playground with 10 fun things to do this year, organized by season."*

**The wow:** open the folder, and *the AI made a real file on your computer*. 🤯

## 3️⃣ Give your AI a memory (20–30 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

Normally AI forgets you after every chat. The memory server is like a notebook it can write in and read later.

</details>

The config above already added the **Memory** server. Now try:

1. > *"Please remember: my name is ___, I'm learning about AI agents, I love ___, and I prefer short, cheerful answers."*
2. Start a **brand-new chat** and ask:
   > *"What do you know about me? Use your memory."*
3. Bonus: Claude also has built-in memory and **Projects** (a place for standing instructions and files). Create a
   Project called "My AI Journey" and add a short note about your goals.

**The wow:** a new conversation that already knows you. 🧠

## 4️⃣ Build a mini app in chat (30–40 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

You describe a tiny app in normal words, and the AI builds a working one right there on the screen that you can click and play with.

</details>

In Claude, ask:

> *"Build me an interactive habit tracker as an artifact: 5 habits I can edit, a checkbox grid for this week, a streak
> counter, and confetti when I complete a whole day. Make it cheerful and colorful."*

Then iterate, one change at a time:

- *"Add a dark mode toggle."*
- *"Make the confetti rain emojis instead."*
- *"Add a motivational quote that changes every day."*

**The wow:** you just "programmed" an app without writing code. That's **vibe coding**
([Vibe Coding Your First Real App](../part-7-building-with-ai/65-vibe-coding-your-first-app.md) takes it much further).

## 5️⃣ Create a reusable assistant (40–50 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

Instead of explaining what you want every time, you write it down once, and the AI remembers it for that job forever.

</details>

Pick one recurring job, like writing emails, meal planning, or studying. Create a **Project** (Claude or ChatGPT) or a
**Gem** (Gemini) with instructions like:

```text
You are my friendly meal-planning assistant. I'm vegetarian, cook for 2, have 30 minutes on weeknights,
and hate mushrooms. When I say "plan my week", give 5 dinners with a combined grocery list grouped by aisle.
Keep it upbeat and practical.
```

Now just say *"plan my week"* whenever you want. ✨

## 6️⃣ Your first automation (50–60 min)

<details class="eli5">
<summary>🧸 ELI5</summary>

An automation is a little robot that does a job by itself when something happens, like "every morning at 7" or "when an
email arrives." We'll make one that sends you a daily AI summary.

</details>

Pick the easiest option for you:

- **Zapier (no install):** create a Zap with **Schedule by Zapier** (every day at 7am) → **AI by Zapier** ("Give me one
  fun AI fact and one tiny challenge for today") → **Email by Zapier** to yourself. Turn it on.
- **n8n (free, local):** run `npx n8n`, open http://localhost:5678, and import our
  [Morning AI Digest workflow](../../examples/n8n-workflows/morning-ai-digest.json)
  ([how-to](../part-5-automation/47-n8n-masterclass.md)).
- **Your phone:** in the iOS **Shortcuts** app, create a daily *Personal Automation* that asks an AI model for a
  motivational message and shows it as a notification ([Phone & Desktop Automation](../part-5-automation/50-phone-and-desktop-automation.md)).

**The wow:** tomorrow morning, something useful arrives that *you built*, and it runs while you sleep. 😴🤖

## 🏁 You did it! What's next?

<details class="eli5">
<summary>🧸 ELI5</summary>

You now have an AI that sees, does, remembers, builds and works on autopilot. Pick whichever part felt the most fun and
go deeper there.

</details>

| Loved… | Go deeper |
|---|---|
| Connecting your data | [The Big MCP Server Catalog](../part-4-mcp-and-connectors/40-mcp-server-catalog.md), [The MCP Recipe Book](../part-4-mcp-and-connectors/44-mcp-recipe-book.md) |
| The files-and-hands magic | [MCP Explained](../part-4-mcp-and-connectors/38-mcp-explained.md), [Building MCP Servers](../part-4-mcp-and-connectors/42-building-mcp-servers.md) |
| The mini app | [Claude Code Masterclass](../part-7-building-with-ai/62-claude-code-masterclass.md), [Vibe Coding](../part-7-building-with-ai/65-vibe-coding-your-first-app.md) |
| The automation | [The n8n Masterclass](../part-5-automation/47-n8n-masterclass.md), [The Automation Recipe Book](../part-5-automation/52-automation-recipe-book.md) |
| All of it 😄 | [Build-Along: Your Pocket AI Assistant](../part-13-build-alongs/112-build-along-pocket-ai-assistant.md) |

## 🎯 Key takeaways

- **Connectors** give AI your context. **MCP servers** give it tools. **Memory** gives it continuity.
- **Artifacts** turn descriptions into working mini apps, and **Projects/Gems** turn repeated instructions into assistants.
- **Automations** make AI work for you on a schedule or trigger.
- You did all of that in an hour. Imagine the next ten! 🚀

> [!TIP]
> **🎮 Try this**
> Screenshot your habit tracker and your bucket list and send them to a friend with *"I built these with AI in an hour."*
> Teaching someone else is the fastest way to lock in what you learned (and it's fun to show off a little 😄).

---

**Next:** [🗺️ The Big Map of AI (One-Page Overview) →](c-the-big-map.md)
