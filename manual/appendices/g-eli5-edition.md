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

### [14 · Automation Platforms: AI That Works While You Sleep ⚙️🌙](../part-3-automation/14-automation-platforms.md)

An automation is a robot recipe: **"When this happens, do that."** When an email arrives, summarize it and put it in my
notes. Every morning, send me the news. Automation platforms (Zapier, Make, n8n…) are kitchens where you build these
recipes by connecting blocks, and adding an AI block lets the robot *think*: sort, summarize, write and decide.

### [15 · Webhooks, APIs & JSON for Non-Programmers 🌐📦](../part-3-automation/15-webhooks-apis-json.md)

**JSON** is a neat way of writing information with labels, like a form: `name: Pixel, species: cat`. An **API** is an app's
front desk, where you ask it for something in a polite, exact way and it answers with JSON. A **webhook** is a doorbell: when
something happens in one app, it rings your doorbell (a special web address) so your robot can spring into action.

### [16 · The n8n Masterclass 🟣⚙️](../part-3-automation/16-n8n-masterclass.md)

n8n is a big LEGO board for robot recipes. Each LEGO brick (a "node") does one thing: check email, ask Claude, post to
Slack. You snap them together left to right, and information flows through them like water through pipes. You can run the
whole board on your own computer for free.

### [17 · n8n AI Agents Deep Dive 🤖🟣](../part-3-automation/17-n8n-ai-agents.md)

A normal n8n recipe follows fixed steps. An **AI Agent brick** is a little brain inside the recipe that decides for itself
which tools to use, like a helper you can text: "What's on tomorrow, and add 'buy a birthday card' before my 3pm meeting."
It checks your calendar, adds the task and texts you back. You give it a brain (model), a memory and a toolbox.

### [18 · Zapier & Make Walkthroughs 🟠🟦](../part-3-automation/18-zapier-and-make-walkthroughs.md)

Zapier and Make are robot-recipe kitchens you use in your web browser. **Zapier** is like a simple recipe card: step 1, step
2, step 3. **Make** is like drawing a map with bubbles and arrows, so recipes can split and loop. Both can add AI to any
step, and Zapier can even hand your AI chat a remote control for thousands of apps.

### [19 · Phone & Desktop Automation: Shortcuts, Tasker, Raycast & Friends 📱💻](../part-3-automation/19-phone-and-desktop-automation.md)

Your phone and computer can have **magic buttons**. Press one, or say a phrase, and a little robot recipe runs: it listens to
your idea, asks an AI to tidy it up, and puts it in your notes. Or it reads a receipt photo and logs it. Or it turns whatever
you copied into a summary. This chapter shows you how to make those buttons.

### [20 · Web Scraping & Monitoring with AI 🕸️👀](../part-3-automation/20-web-scraping-and-monitoring.md)

Scraping means having a robot visit web pages and copy the important bits for you, like a friend who checks the toy store
website every morning and texts you when your favorite toy goes on sale. AI makes this easy because it can *read* a messy
page like a person and pull out exactly what you asked for.

### [21 · The Automation Recipe Book: 50 Workflows to Steal 🍳⚙️](../part-3-automation/21-automation-recipe-book.md)

A cookbook with fifty robot recipes. Each one says what starts it (like "a new email arrives"), what the robot does (like
"ask AI to summarize it"), and what you get (like "a tidy note in your to-do app"). Find the recipe for the chore you hate
most and build that one first!

## 🏡 Part IV · AI in Your Apps

### [22 · AI Inside the Apps You Already Use 🏡✨](../part-4-ai-in-your-apps/22-ai-in-your-apps.md)

Your favorite apps got secret AI helpers! Your notes app can organize itself, your email can summarize itself, your
spreadsheet can fill itself in, and your phone can read your screen. This chapter is a treasure map showing where each
helper lives and one great trick for each.

### [23 · Notion AI Deep Dive: Build an AI-Powered Second Brain 📒✨](../part-4-ai-in-your-apps/23-notion-ai-deep-dive.md)

Notion is like a magic binder where every page can hold notes, lists and tables. Now the binder has a **helper who lives
inside it**: you can ask it to write pages, tidy your lists, summarize meetings, and even do chores on a schedule while
you sleep. We'll build a "second brain" binder that organizes itself.

### [24 · Google Workspace & Microsoft 365 AI 🔵🟣](../part-4-ai-in-your-apps/24-google-and-microsoft-ai.md)

Google and Microsoft put AI helpers inside email, documents, spreadsheets, slides and video calls. **Gemini** is Google's
helper, and **Copilot** is Microsoft's. They can summarize, write, make slides from documents, take meeting notes and more.
This chapter shows you the best trick in each app, plus how to make little robots that do the boring stuff automatically.

### [25 · Obsidian + AI: Your Local-First Thinking Machine 🟪🧠](../part-4-ai-in-your-apps/25-obsidian-and-ai.md)

Obsidian keeps your notes as simple text files in a folder, like pages in a real notebook you own. Because they're just
files, any AI helper can read them: an AI inside Obsidian, Claude through a connector, or a coding agent that tidies your
whole notebook. You can even use an AI that lives only on your computer, so your diary never leaves home.

### [26 · Email & Calendar Superpowers 📬📅](../part-4-ai-in-your-apps/26-email-and-calendar.md)

Imagine a friendly assistant who reads all your mail first, puts it into neat piles ("important," "can wait," "just
newsletters"), writes draft replies for you to check, and keeps your calendar tidy so you have quiet time to think. That's
what we're building, and you stay the boss who approves everything.

### [27 · Spreadsheet Superpowers 📊✨](../part-4-ai-in-your-apps/27-spreadsheet-superpowers.md)

Spreadsheets are grids of boxes. Now AI can fill boxes for you: "is this review happy or sad?", "what country is this
address in?", "write a summary of this row." It can also write the tricky math formulas, clean up messy lists, and draw
charts that explain what your numbers mean.

### [28 · Chat Apps & Bots: Slack, Discord, Telegram & WhatsApp 💬🤖](../part-4-ai-in-your-apps/28-chat-apps-and-bots.md)

A chat bot is a robot friend that lives in your group chat. You message it like a person ("what's the wifi password?" or
"summarize today's chat"), and it answers using AI. You can build one without coding using n8n, or with a little Python if
you're feeling adventurous.

## 🛠️ Part V · Building with AI

### [29 · Agents & AI Coding Tools: Become a Builder 🛠️🤖](../part-5-building-with-ai/29-agents-and-coding-tools.md)

Imagine a super-fast builder robot. You describe the treehouse you want ("two floors, a rope ladder, a secret door"), and
the robot builds it, tests that the ladder holds, and fixes anything wobbly while you watch. **Coding agents** are that
robot, but for apps and websites. Some live in your web browser, some in a code editor, and some in a terminal. This
chapter helps you pick one and be a great boss to it.

### [30 · Git & GitHub for AI Builders 🌳🐙](../part-5-building-with-ai/30-git-and-github.md)

Imagine a video game where you can **save your progress** any time. If you fall into lava, you just load your last save.
**Git** is that save system for your projects. **GitHub** is a cloud locker where your saves live, where friends (and AI
helpers) can suggest changes, and where little robots can check your work and even turn it into a website.

### [31 · The Claude Code Masterclass 🧑‍💻🤖](../part-5-building-with-ai/31-claude-code-masterclass.md)

Claude Code is like having a super-smart helper sitting at your computer. You type what you want in plain words ("make me a
website about my cat"), and it opens files, writes code, runs it, sees what's broken and fixes it, asking your permission
for anything risky. Your job is to be a good boss: explain the goal, check the plan, and say "yes, keep going."

### [32 · Claude Code Power-Ups: Skills, Subagents, Hooks, Plugins & More ⚡🧙](../part-5-building-with-ai/32-claude-code-power-ups.md)

Think of Claude Code as a robot with an empty backpack. **Skills** are instruction booklets it can pull out when needed.
**Subagents** are little helper robots it can send off on errands. **Hooks** are automatic rules ("always wipe your feet
when you come in"). **MCP** gives it new tools. **Plugins** are gift boxes containing all of the above. You can build every
one of them, or install ones other people made.

### [33 · Cursor & AI IDEs: Coding Side by Side with AI 🖱️✨](../part-5-building-with-ai/33-cursor-and-ai-ides.md)

An IDE is the program where people write code, like a word processor for programs. An **AI IDE** has a helper that
finishes your sentences, fixes lines you point at, answers questions about your project, and can even make big changes
across many files while you watch. It's like writing with a friend looking over your shoulder who happens to be a coding
genius.

### [34 · Vibe Coding Your First Real App 🎸💻](../part-5-building-with-ai/34-vibe-coding-your-first-app.md)

You tell the AI "I want an app where my family can share wish lists," and it builds it. You click around, say "make that
button bigger" or "it breaks when I do this," and it fixes things. Keep going until it's good, then put it on the internet
and send the link to your family. You're the director, the AI is the film crew. 🎬

### [35 · Deploying & Hosting: Put Your Creation on the Internet 🌍🚀](../part-5-building-with-ai/35-deploying-and-hosting.md)

Your app lives on your computer, and only you can see it. **Deploying** means copying it to a computer that's always on and
connected to the internet, so anyone with the link can use it. Some companies give you that computer for free for small
projects. You connect your GitHub, click "deploy," and get a link to share. 🔗

### [36 · Calling AI APIs Directly 🔑🐍](../part-5-building-with-ai/36-calling-ai-apis.md)

A chat app is like ordering at a restaurant counter. An **API** is the kitchen's back door: your own programs can send
orders directly ("summarize this," "read this receipt") and get answers back, thousands of times a day, without anyone
typing into a chat box. You get a secret key (like a membership card), send a message in a special format, and get the
AI's reply as data your program can use.

### [37 · Build Your Own Agent 🤖🔧](../part-5-building-with-ai/37-build-your-own-agent.md)

An agent is an AI that can **do things**, not just talk. You give it a goal and a toolbox (a calculator, a file reader, a web
search). It thinks "I need the calculator," uses it, looks at the answer, thinks again, uses another tool, and keeps going
until the job is done. That "think → use a tool → look → think again" circle is called **the loop**, and you'll write it
yourself in about 100 lines.

### [38 · Agent Frameworks Tour: Pick Your LEGO Set 🧱🤖](../part-5-building-with-ai/38-agent-frameworks-tour.md)

You *can* build a robot from loose parts, but LEGO sets come with the special pieces already made: wheels, arms, a remote
control. **Agent frameworks** are LEGO sets for AI helpers. Each set has a different style. Some are simple, some build
giant castles (big multi-robot teams), and some are made for websites. This chapter shows you the sets so you can pick one
you like.

### [39 · Multi-Agent Systems: Teams of AIs 👥🤖](../part-5-building-with-ai/39-multi-agent-systems.md)

Imagine building a huge sandcastle. One kid can do it, but it takes forever. With a team, one kid digs the moat, one builds
towers, one decorates, and a "boss kid" checks everyone's work and puts it all together. **Multi-agent systems** are teams
of AI helpers like that. They're great for big jobs, but teams also cost more and can get messy, so you only form a team
when one helper really isn't enough.

### [40 · Computer Use & Browser Agents: AI That Clicks for You 🖱️🌐](../part-5-building-with-ai/40-computer-use-and-browser-agents.md)

Most AI helpers can only read and write words. A **computer-use agent** can actually *use* a computer: it looks at the screen
(like taking a picture), decides where to click, clicks, types, and checks what happened. You can say "find me a table for four
at an Italian place near me on Friday at 7" and watch it browse websites to do it. It's slower than you and sometimes gets
confused, but it never gets bored of filling in forms!

## 📚 Part VI · Knowledge & Memory

## 🏠 Part VII · Local AI

## 🎨 Part VIII · Creative AI

## 🌱 Part IX · AI for Life & Work

## 🏆 Part X · Mastery

---

**You made it to the end! 🎉** [Back to the manual home ↩](../index.md)
