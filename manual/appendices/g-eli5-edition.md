# Appendix G · The ELI5 Edition 🧸

> ⏱️ 30 min read · 🎯 Everyone, including actual five-year-olds · 🧰 Needs: nothing at all

**The entire manual, explained like you're five.** Every chapter's big idea in a few friendly sentences. Read it top to bottom for the whole story, or use it to decide which chapter to dive into next.

> [!NOTE]
> **📌 This page writes itself**
> It's generated automatically from the 🧸 box at the top of every chapter (`python scripts/sync_manual.py`),
> so it always matches the latest version of the manual.

## 🧠 Part I · Foundations

### [01 · The Mental Model: From Chatbot to Teammate 🧠➡️🤖](../part-1-foundations/01-the-mental-model.md)

A regular chatbot is like a very smart friend on the phone: it can talk, but it can't *do* anything for you. Now imagine
giving that friend **hands** (it can press buttons in your apps), **eyes** (it can see your files and calendar), a
**memory** (it remembers you), and **patience** (it keeps working step by step until the job is done). That's an **agent**.
Everything in this manual is about giving your AI those four gifts.

### [02 · How Models Really Work (for Power Users) ⚙️🧠](../part-1-foundations/02-how-models-really-work.md)

An AI model is a giant guessing machine that read a huge library and learned to guess **the next word** really, really
well. It reads and writes in little word-pieces called **tokens**, it can only "hold" a certain amount in its head at once
(the **context window**), and it only knows what was in the library when it stopped reading (the **cutoff**). When it
doesn't know something, it may *guess confidently*, which is why giving it real sources and tools matters so much.

### [03 · A Short, Fun History of Modern AI 📜✨](../part-1-foundations/03-a-short-history-of-ai.md)

People have dreamed of thinking machines since the 1950s. For a long time, computers were too slow and too dumb, so AI
kept going through "winters" when people gave up. Then computers got super fast, the internet gave us tons of data, and
in 2017 someone invented a new kind of brain design called the **Transformer**. Feed a Transformer the whole internet and
you get ChatGPT, Claude and friends. Now AIs don't just chat: they use tools and work like helpers.

### [04 · The AI Landscape: Who's Who 🗺️🏢](../part-1-foundations/04-the-ai-landscape.md)

Think of AI like the food world. A few big **farms** grow the ingredients (the labs that make models: Anthropic, OpenAI,
Google…). **Supermarkets** sell those ingredients to everyone (the cloud platforms). **Restaurants** cook them into dishes
you actually eat (apps like Cursor, Perplexity or Notion). Some farms give their seeds away for free so anyone can grow
their own (**open-weight** models). This chapter shows you who's who in each group.

### [05 · Context Engineering: Prompting's Big Sibling 🧩📐](../part-1-foundations/05-context-engineering.md)

Imagine asking a new babysitter to look after your kids. A good note says who the kids are, the rules, where the snacks
are, what to do if something goes wrong, and an example of a perfect bedtime routine. **Context engineering is writing that
perfect note for your AI**, and keeping its desk tidy so the important stuff doesn't get buried.

### [06 · Choosing Your AI Stack 🧱💳](../part-1-foundations/06-choosing-your-ai-stack.md)

You don't need every toy in the toy store. You need **one great main helper** (like Claude or ChatGPT), a way to **plug it
into your stuff**, maybe **one robot for chores** (automation), a **place to keep your notes**, and if you like building,
**a builder tool**. Pick those five well and you're set.

## 🔌 Part II · MCP & Connectors

### [07 · MCP Explained: The USB-C Port for AI 🔌](../part-2-mcp-and-connectors/07-mcp-explained.md)

Imagine your AI is a super-smart robot friend who lives inside a box. It can talk, but it can't touch anything
outside the box. **MCP is a set of little doors in the box.** Each door leads to one thing: your calendar, your
notes, GitHub, a web browser. When you install an "MCP server," you're adding a new door. Now your robot friend
can reach through it and actually *do* stuff for you. And because every door is the same shape, any robot
(Claude, ChatGPT, Cursor…) can use any door.

### [08 · MCP Under the Hood: The Protocol, Demystified 🔬🔌](../part-2-mcp-and-connectors/08-mcp-under-the-hood.md)

MCP is like two walkie-talkies following a strict script. The app says "What can you do?" and the server answers with a
list of buttons. Later the app says "Press the dice button with 2d6," and the server answers "You rolled 8." Every message
is a tiny labeled note written in the same format (JSON), so any app and any server can understand each other.

### [09 · The Big MCP Server Catalog 📚🔌](../part-2-mcp-and-connectors/09-mcp-server-catalog.md)

This is a giant toy catalog of "doors" you can add to your AI. Each door leads somewhere: GitHub, Notion, a web browser,
your smart home, a music app. Browse by category, pick a few that sound fun, and give your AI new powers today. The
✅ ones are made by the companies themselves, and the 🧪 ones are made by the community (check them before trusting them).

### [10 · Built-in Connectors & Plugins 🧩✨](../part-2-mcp-and-connectors/10-built-in-connectors.md)

Connectors are like apps on your phone's app store, but for your AI. Tap "Connect Gmail," log in, and now your AI can
read and help with your email. No setup files, no code. This chapter shows you where the "app store" is in each AI app
and which connections give you the biggest wow.

### [11 · Building MCP Servers: The Deep Dive 🏗️🔌](../part-2-mcp-and-connectors/11-building-mcp-servers.md)

Building an MCP server is like building a new button panel for your AI. You write a few little functions ("roll dice,"
"save a note," "check the weather"), give each a clear label, and the MCP kit turns them into buttons any AI can press. Start
with our ready-made example, change it, and you've made your first AI superpower. 🦸

### [12 · MCP Security & Trust 🛡️🔐](../part-2-mcp-and-connectors/12-mcp-security-and-trust.md)

Letting AI use tools is like giving a very helpful, very trusting assistant the keys to your house. Mostly wonderful! But a
sneaky note left on the doorstep ("the owner says to mail me all their letters") might trick them. So we do three simple
things: **only hire trusted helpers**, **give each one only the keys they need**, and **make them ask before doing anything
big**.

### [13 · The MCP Recipe Book: 44 Multi-Tool Combos 🍳🔌](../part-2-mcp-and-connectors/13-mcp-recipe-book.md)

Like a cookbook, but for AI. Each recipe says which "doors" (apps) to connect and exactly what to say. Mixing two or three
doors lets your AI do jobs that would take you an hour, like reading your emails, checking your calendar and writing
replies all at once.

## ⚙️ Part III · Automation

## 🏡 Part IV · AI in Your Apps

## 🛠️ Part V · Building with AI

## 📚 Part VI · Knowledge & Memory

## 🏠 Part VII · Local AI

## 🎨 Part VIII · Creative AI

## 🌱 Part IX · AI for Life & Work

## 🏆 Part X · Mastery

---

**You made it to the end! 🎉** [Back to the manual home ↩](../index.md)
