# 28 · Chat Apps & Bots: Slack, Discord, Telegram & WhatsApp 💬🤖

> ⏱️ 6 min read · 🎯 Beginner → intermediate · 🧰 Needs: a Slack workspace, Discord server or Telegram account (+ n8n or a little Python)

**Chat apps are where people already hang out, which makes them the perfect home for AI.** Build a bot that answers team
questions from your docs, a Discord game master for your friends, a Telegram assistant in your pocket, or a Slack helper
that summarizes channels. This chapter covers built-in AI in chat apps, then shows three ways to build your own bot, from
no-code to code.

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

A chat bot is a robot friend that lives in your group chat. You message it like a person ("what's the wifi password?" or
"summarize today's chat"), and it answers using AI. You can build one without coding using n8n, or with a little Python if
you're feeling adventurous.

</details>

<!-- in-this-chapter -->

## 🧭 Built-in AI in chat apps

<details class="eli5">
<summary>🧸 ELI5</summary>

Some chat apps already have AI helpers inside that can summarize conversations and answer questions. Try those before
building anything.

</details>

| App | Built-in AI | Also… |
|---|---|---|
| **Slack** | Channel recaps, thread summaries, AI search across conversations and connected apps, agents | Official MCP server for other AIs to use Slack ([Built-in Connectors](../part-2-mcp-and-connectors/10-built-in-connectors.md)) |
| **Microsoft Teams** | Copilot recaps, "what did I miss," meeting notes | Copilot Studio agents can live in Teams |
| **Discord** | Varies by server, mostly via bots and apps | Huge bot ecosystem |
| **Telegram** | Bots are first-class citizens (created via @BotFather) | Perfect for personal assistants |
| **WhatsApp** | Meta AI built in, and business bots via the WhatsApp Business Platform | Official APIs for business use |

## 🏗️ Three ways to build your own bot

<details class="eli5">
<summary>🧸 ELI5</summary>

You can build a bot by connecting blocks (no code), by writing a small program, or by letting an AI coding helper write the
program for you. Pick whatever feels comfy.

</details>

| Way | Tools | Best for |
|---|---|---|
| 🟢 **No-code** | n8n (Telegram/Slack/Discord triggers + AI Agent node), Zapier, Make | Personal assistants, team helpers, quick prototypes |
| 🟡 **Low-code** | Bot frameworks (discord.py, Slack Bolt, python-telegram-bot, grammY) + the Claude API | Custom behavior, games, community bots |
| 🔵 **AI-built** | Claude Code or Cursor writes the bot for you | Anything, fast, and you learn by reading the code |

## 🟢 Build: a Telegram assistant with n8n (no code)

<details class="eli5">
<summary>🧸 ELI5</summary>

We'll make a robot you can text on Telegram. It uses AI to answer, remembers the conversation, and only talks to you, not
strangers.

</details>

1. On Telegram, message **@BotFather** → `/newbot` → pick a name → copy the **token**.
2. In n8n: **Telegram Trigger** (on message) with the token as a credential.
3. **If** node: continue only if `{{ $json.message.from.id }}` is *your* user ID (message @userinfobot to find it). 🔒
4. **AI Agent** (Anthropic model + Simple Memory keyed by `{{ $json.message.chat.id }}`) with a friendly system message.
5. **Telegram → Send Message** back to the same chat with `{{ $json.output }}`.
6. Activate. Text it: *"Give me a 10-minute workout I can do at my desk."* 💪

Add tools (calendar, tasks, weather) exactly as in [n8n AI Agents Deep Dive](../part-3-automation/17-n8n-ai-agents.md#-build-a-personal-assistant-on-telegram-30-min),
and see the full build in [Build-Along: Your Pocket AI Assistant](../part-11-build-alongs/81-build-along-pocket-ai-assistant.md).

## 💼 Build: a Slack "ask our docs" helper

<details class="eli5">
<summary>🧸 ELI5</summary>

A Slack bot that answers teammates' questions using your team's documents, like "how do I request time off?", and tells
them which document the answer came from.

</details>

**The idea:** someone mentions `@DocsBot how do we request time off?` → the bot searches your docs → answers with a link.

1. **Knowledge:** put your docs in a vector store with an n8n ingest workflow ([RAG inside n8n](../part-3-automation/17-n8n-ai-agents.md#-rag-inside-n8n)),
   or ground it in Notion or Drive via connectors.
2. **Slack app:** create one at api.slack.com (bot token, `app_mentions:read` and `chat:write` scopes), install it to your
   workspace, and point its event subscription at your n8n webhook, or use n8n's Slack Trigger.
3. **Agent:** AI Agent + Vector Store tool, with a system message like *"Answer only from the knowledge base, cite the source
   page, and say 'I don't know. Try #help' if it isn't there."*
4. **Reply in thread** to keep channels tidy.

**Level up:** a daily channel digest, an "unanswered questions" report, or a `/summarize` slash command.

## 🎲 Build: a Discord game-master bot (with code)

<details class="eli5">
<summary>🧸 ELI5</summary>

A Discord robot that runs a fantasy adventure game for your friends: it describes the scene, rolls dice, and reacts to what
everyone does.

</details>

A small Python sketch using `discord.py` and the Claude API (ask Claude Code to flesh it out, add dice commands, and save
campaign memory):

```python
import os, discord, anthropic

intents = discord.Intents.default()
intents.message_content = True            # enable this intent in the Discord developer portal too
bot = discord.Client(intents=intents)
ai = anthropic.Anthropic()
history: dict[int, list] = {}             # per-channel conversation memory

GM = ("You are a cheerful, fair fantasy game master for a Discord group. Keep replies under 120 words, "
      "describe scenes vividly, ask players what they do next, and never decide actions for them.")

@bot.event
async def on_message(msg: discord.Message):
    if msg.author.bot or not msg.content.startswith("!gm"):
        return
    turns = history.setdefault(msg.channel.id, [])
    turns.append({"role": "user", "content": f"{msg.author.display_name}: {msg.content[3:].strip()}"})
    reply = ai.messages.create(model="claude-opus-5", max_tokens=1000, system=GM, messages=turns[-20:])
    text = reply.content[0].text
    turns.append({"role": "assistant", "content": text})
    await msg.channel.send(text[:1900])   # Discord messages max out around 2,000 characters

bot.run(os.environ["DISCORD_BOT_TOKEN"])
```

Then type `!gm We enter the misty tavern.` and let the adventure begin. 🐉 More game ideas in
[Storytelling & Interactive Fiction](../part-8-creative-ai/58-storytelling-and-interactive-fiction.md).

## 🧠 Designing a bot people love

<details class="eli5">
<summary>🧸 ELI5</summary>

Good bots have a clear job, a friendly personality, short answers, and they admit when they don't know something.

</details>

| Principle | In practice |
|---|---|
| **One clear job** | "Answers HR questions" beats "does everything" |
| **Personality** | A name, a friendly voice, and emoji if it fits the community |
| **Short replies** | Chat is conversational. Long answers go in threads or files |
| **Honest limits** | "I don't know. Try #help" beats a confident wrong answer |
| **Discoverability** | A `/help` command and a pinned intro message |
| **Memory with care** | Per-channel or per-user memory, and don't remember sensitive info |
| **Feedback loop** | 👍/👎 reactions logged to a sheet to improve prompts |

## 🔐 Safety, privacy & etiquette

<details class="eli5">
<summary>🧸 ELI5</summary>

Keep your bot's secret token secret, only let it into rooms where people know it's there, and don't let strangers use your
expensive AI for free.

</details>

- **Lock it down:** allowlist user IDs or channels, because public bots can rack up API bills fast.
- **Secrets:** bot tokens and API keys go in environment variables or credentials, never in code you share.
- **Tell people:** members should know a bot reads messages in a channel, and follow the platform's rules and your
  community's norms.
- **Least privilege:** request only the scopes and intents you need.
- **Rate limits and spend limits:** cap messages per user per hour, and set API spend limits ([Cost Optimization](../part-10-mastery/75-cost-optimization.md)).
- **Prompt injection:** in shared channels, anyone can type instructions to your bot, so keep powerful tools behind approvals.

## 💡 20 bot ideas

<details class="eli5">
<summary>🧸 ELI5</summary>

Twenty robot friends you could build for your chats: for work, for friends, for family and for fun.

</details>

| For work 💼 | For friends & family 👨‍👩‍👧 | For fun 🎉 |
|---|---|---|
| Docs Q&A bot | Shared grocery list bot | D&D game master 🐉 |
| Daily standup collector | Family calendar reminders | Trivia host |
| Meeting notes → channel summary | Chore rotation announcer | Movie night picker |
| "Who's on vacation?" bot | Group trip planner | Daily riddle bot |
| Customer feedback digest | Recipe and meal ideas bot | Song-lyric guessing game |
| Onboarding buddy for new hires | Plant watering reminders 🌱 | AI-powered choose-your-own-adventure |
| Incident summary bot | Homework helper (learning mode!) | Pet photo caption contest 🐶 |

## 🎯 Key takeaways

- Try **built-in AI** in Slack and Teams first, and **build a bot** when you need a specific job done.
- **n8n** gets you a Telegram or Slack bot with memory and tools in under an hour, no code.
- For custom behavior (games, communities), a **small Python bot + the Claude API** goes a long way.
- Great bots have **one job, short replies, honest limits** and a **locked-down** setup.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Your personal Telegram bot starts getting messages from strangers. What should you have added?</summary>

An **allowlist check** (an If node or a code check on the sender's user ID) so it only responds to you.

</details>

<details class="quiz">
<summary>❓ 2. Why should a docs bot reply "I don't know" sometimes?</summary>

Confident wrong answers destroy trust. Grounded bots should **admit when the answer isn't in the knowledge base** and point
to a human.

</details>

> [!TIP]
> **🎮 Try this**
> Build the **Telegram assistant** above and give it one fun personality (a pirate, a cheerful coach, a wise owl 🦉). Use it
> for a week, then add one real tool. You'll never want to go back to plain chat apps.

---

**Next:** [17 · Agents & AI Coding Tools →](../part-5-building-with-ai/29-agents-and-coding-tools.md)
