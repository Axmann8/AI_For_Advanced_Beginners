# ⚡ Your First Hour: 60 Minutes to AI Superpowers

> ⏱️ 60 min hands-on · 🎯 Beginner-friendly · 🧰 Needs: a computer and a free ChatGPT, Gemini or Claude account (most missions work in all three)

**This is the fastest route from "I use AI to answer questions" to "my AI reads my files, browses the web, remembers me,
and runs a little automation."** Six mini-missions, ten minutes each. Grab a drink, put on a good playlist, and let's go. 🎧

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

This hour-long session takes you through six short missions that show what modern AI assistants can really do beyond simple chat.

- **You'll connect your own data,** add tools through MCP, and give your assistant a memory.
- **You'll build a working mini app** and a reusable custom assistant just by describing them.
- **You'll set up a first automation** that runs on a schedule without you.
- **What you need:** a free account with ChatGPT, Gemini or Claude; Claude Desktop for mission 2.

</details>

<!-- in-this-chapter -->

## 🗺️ The plan

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Each mission takes about ten minutes and builds on the one before, so it works best in order. The table shows the timing and the capability each mission adds.

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

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Connecting an app lets the AI answer questions using your real email, files or calendar instead of only its general knowledge. You choose exactly what it can access, and you can disconnect at any time.

1. Pick **one** app you use daily (Gmail, Drive, Calendar, Outlook, Notion or GitHub).
2. Open your assistant's connector settings (steps for each assistant are below) and sign in.
3. Ask a question only your data can answer, such as *"What's on my calendar this week?"*

</details>

Connect **one** thing you actually use (Gmail, Google Drive, Google Calendar, Outlook, Notion or GitHub):

=== "💬 ChatGPT"

    Profile → **Settings → Connectors** (or **Plugins**) → pick Gmail, Google Drive, Outlook or another app → sign in and allow
    access.

=== "✨ Gemini"

    **Settings → Apps** (or turn on **Personal Intelligence**) → switch on Gmail, Calendar and Drive. They're already
    part of your Google account.

=== "🧡 Claude"

    **Settings → Connectors** → browse the directory → connect Google Drive, Gmail, Calendar, Notion or GitHub.

=== "🪟 Copilot"

    Sign in with your Microsoft account; with Microsoft 365, Copilot can work with your Outlook email and OneDrive
    files.

Then start a new chat and ask:
   > *"Based on my recent files, what are the 3 things I've been working on most this month? Anything I seem to have forgotten?"*
4. Then try:
   > *"What's on my calendar this week, and what should I prepare for each meeting?"*

**The wow:** the first time AI answers from *your* data, something clicks. You'll never look at chatbots the same way. 💡

> [!NOTE]
> **📌 More assistants, more connections**
> Perplexity, Le Chat and others have connectors too. The full tour, app by app, is in
> [Built-in Connectors](../part-4-mcp-and-connectors/41-built-in-connectors.md).

## 2️⃣ Install your first MCP servers (10–20 min)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

MCP servers are small programs that give your AI new abilities. Here you'll add two: one that reads web pages and one that can create files, limited to a single folder you choose.

1. Install **Claude Desktop** and create a folder for the AI to work in.
2. Paste the configuration below into the settings file and restart the app.
3. Test it by asking the AI to read a web page and save a summary into that folder.

</details>

> [!NOTE]
> **📌 Why Claude Desktop for this mission?**
> MCP servers work in lots of apps now (ChatGPT's developer mode, Le Chat's custom connectors, VS Code, Cursor, Gemini
> CLI and more), but **Claude Desktop** is still the simplest place to run *local* servers on your own computer, and the
> free plan works. Using another app? The same servers plug in almost identically: see
> [MCP Explained](../part-4-mcp-and-connectors/38-mcp-explained.md#-installing-servers-app-by-app).

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

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

By default, an assistant starts every chat from scratch. A memory feature (or the Memory MCP server you just installed) lets it store facts about you and use them in later conversations.

1. Tell the assistant a few facts and preferences, and ask it to remember them.
2. Open a brand-new chat and ask what it knows about you.
3. Review what's stored from time to time, and delete anything you don't want kept.

</details>

The config above already added the **Memory** server. Now try:

1. > *"Please remember: my name is ___, I'm learning about AI agents, I love ___, and I prefer short, cheerful answers."*
2. Start a **brand-new chat** and ask:
   > *"What do you know about me? Use your memory."*
3. Bonus: every major assistant now has **built-in memory** too (ChatGPT memory, Gemini's saved info and Personal
   Intelligence, Claude memory, Le Chat memories) plus **Projects** or **Gems** for standing instructions and files.
   Create a Project (or Gem) called "My AI Journey" and add a short note about your goals.

**The wow:** a new conversation that already knows you. 🧠

## 4️⃣ Build a mini app in chat (30–40 min)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

Features like Claude Artifacts, ChatGPT Canvas and Gemini Canvas can build small interactive apps from a plain-language description and run them right in the chat.

1. Describe the app you want, including what it should do and how it should look.
2. Try the result immediately.
3. Ask for one change at a time until it works the way you want.

</details>

In **Claude** (Artifacts), **ChatGPT** (Canvas) or **Gemini** (Canvas, from the Tools menu), ask:

> *"Build me an interactive habit tracker as an app I can use right here: 5 habits I can edit, a checkbox grid for this week, a streak
> counter, and confetti when I complete a whole day. Make it cheerful and colorful."*

Then iterate, one change at a time:

- *"Add a dark mode toggle."*
- *"Make the confetti rain emojis instead."*
- *"Add a motivational quote that changes every day."*

**The wow:** you just "programmed" an app without writing code. That's **vibe coding**
([Vibe Coding Your First Real App](../part-7-building-with-ai/65-vibe-coding-your-first-app.md) takes it much further).

## 5️⃣ Create a reusable assistant (40–50 min)

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

A Project (Claude or ChatGPT) or a Gem (Gemini) stores instructions for a recurring task, so you don't have to repeat them every time.

1. Choose a task you do often, such as meal planning or writing emails.
2. Create a Project or Gem and paste in instructions like the example below.
3. Start each new conversation inside it with a short request, like *"plan my week."*

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

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

An automation runs a task for you whenever something happens, such as a set time each day or a new email arriving. You'll set up a simple daily briefing.

1. Choose the easiest option below (your assistant's scheduled tasks, Zapier, or a phone shortcut).
2. Set the schedule and write the instruction the AI should follow.
3. Run it once manually to check the result, then let it run on its own.

</details>

Pick the easiest option for you:

- **Right inside your assistant (easiest):** *"Every morning at 7am, give me one fun AI fact and one tiny challenge for
  the day."* ChatGPT (scheduled tasks), Gemini (scheduled actions) and Claude (Cowork's scheduled tasks, on paid plans)
  will run it for you and send a notification.
- **Zapier (no install):** create a Zap with **Schedule by Zapier** (every day at 7am) → **AI by Zapier** ("Give me one
  fun AI fact and one tiny challenge for today") → **Email by Zapier** to yourself. Turn it on.
- **n8n (free, local):** run `npx n8n`, open http://localhost:5678, and import our
  [Morning AI Digest workflow](../../examples/n8n-workflows/morning-ai-digest.json)
  ([how-to](../part-5-automation/47-n8n-masterclass.md)).
- **Your phone:** in the iOS **Shortcuts** app, create a daily *Personal Automation* that asks an AI model for a
  motivational message and shows it as a notification ([Phone & Desktop Automation](../part-5-automation/50-phone-and-desktop-automation.md)).

**The wow:** tomorrow morning, something useful arrives that *you built*, and it runs while you sleep. 😴🤖

## 🏁 You did it! What's next?

<details class="keypoints" open>
<summary>✅ Key Points & Steps</summary>

In one hour you've connected data, added tools, set up memory, built an app, created a custom assistant and automated a task. Choose the mission you enjoyed most and use the table below to find the chapters that go deeper.

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
- **Artifacts and Canvas** turn descriptions into working mini apps, and **Projects/Gems** turn repeated instructions
  into assistants.
- **Automations** make AI work for you on a schedule or trigger.
- You did all of that in an hour. Imagine the next ten! 🚀

> [!TIP]
> **🎮 Try this**
> Screenshot your habit tracker and your bucket list and send them to a friend with *"I built these with AI in an hour."*
> Teaching someone else is the fastest way to lock in what you learned (and it's fun to show off a little 😄).

---

**Next:** [🗺️ The Big Map of AI (One-Page Overview) →](c-the-big-map.md)
