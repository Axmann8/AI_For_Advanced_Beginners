# 50 · Phone & Desktop Automation: Shortcuts, Tasker, Raycast & Friends 📱💻

> ⏱️ 8 min read · 🎯 Beginner-friendly · 🧰 Needs: an iPhone, Android phone, Mac or Windows PC (whatever you have!)

**The most personal automations live on the devices in your pocket and on your desk.** With one tap, a voice command, a
location or a keyboard shortcut, you can send AI your thoughts, photos, clipboard or screen and get something useful back
instantly. This chapter covers Apple Shortcuts (with iOS 26's built-in AI models), Android, Mac, Windows and Linux.

<details class="eli5" open>
<summary>🧸 ELI5: This chapter in 30 seconds</summary>

Your phone and computer can have **magic buttons**. Press one, or say a phrase, and a little robot recipe runs: it listens to
your idea, asks an AI to tidy it up, and puts it in your notes. Or it reads a receipt photo and logs it. Or it turns whatever
you copied into a summary. This chapter shows you how to make those buttons.

</details>

<!-- in-this-chapter -->

## 📱 Why device automation is a superpower

<details class="eli5">
<summary>🧸 ELI5</summary>

Your phone is always with you, has a camera and a microphone, and knows where you are. That makes it the perfect place for
quick AI buttons.

</details>

| Your device knows… | Which enables… |
|---|---|
| 🎙️ Your voice | Dictate ideas, notes and tasks hands-free |
| 📸 What the camera sees | Receipts, whiteboards, plants, menus, documents |
| 📍 Where you are | "When I arrive at the office…" / "When I leave home…" |
| ⏰ The time and your focus mode | Morning briefings, evening wind-downs |
| 📋 What you copied | Instant summarize, translate, rewrite |
| 🔌 When you plug in, connect CarPlay, or tap an NFC tag | Context-aware routines |

Combine these triggers with AI and you get the fastest capture-and-process loop there is. ⚡

## 🍎 Apple Shortcuts + AI

<details class="eli5">
<summary>🧸 ELI5</summary>

The Shortcuts app on iPhone and Mac lets you chain actions like LEGO. Since iOS 26, it has a "Use Model" block that can ask
Apple's own AI (on your phone or in Apple's private cloud) or ChatGPT to do the thinking.

</details>

**The key action: Use Model** (iOS, iPadOS and macOS 26). It sends a prompt (plus any Shortcuts variables, like dictated text,
clipboard or a photo) to:

| Model option | What it is | Best for |
|---|---|---|
| **On-Device** | Apple's Foundation Model, running on your device | Private, fast, offline-friendly, simple tasks |
| **Private Cloud Compute** | Apple's larger model on Apple's privacy-focused servers | Harder requests, still privacy-first |
| **ChatGPT** (extension) | OpenAI's model via Apple's integration | The most capable general model option |

The action can also return **structured output** (e.g. a dictionary with fixed keys), which makes the AI's answer easy to
feed into the next actions deterministically. 🎯

Other ways to use AI from Shortcuts:

- Many AI apps (ChatGPT, Claude, Perplexity and others) ship their own **Shortcuts actions**.
- **Get Contents of URL** can call any API or your n8n/Zapier/Make **webhook** ([Webhooks, APIs & JSON](46-webhooks-apis-json.md)).
- Apple Intelligence **Writing Tools** and **summaries** actions for quick text jobs.

## 🧪 Five Shortcuts recipes to build today

<details class="eli5">
<summary>🧸 ELI5</summary>

Here are five magic buttons you can build in about ten minutes each: a brain-dump sorter, a receipt logger, a clipboard
summarizer, a morning pep talk and a meeting-notes helper.

</details>

### 1. 🧠 Brain Dump → Organized Note
**Dictate Text** → **Use Model** (*"Turn this rambling into a tidy note: title, 3–5 bullets, and any tasks as a checklist."*)
→ **Create Note** (or Append to Note) → **Show Notification** "Saved ✅".

### 2. 🧾 Receipt Snap → Expense Log
**Take Photo** → **Use Model** with the photo (*"Extract merchant, date, total and category as a dictionary"*) →
**Add to spreadsheet** (Numbers or a Google Sheets webhook) → notification.

### 3. 📋 Clipboard → Summary
**Get Clipboard** → **Use Model** (*"Summarize in 3 bullets and one 'so what'"*) → **Show Result** or **Copy to Clipboard**.
Great with the **Share Sheet** too: share any article to the shortcut.

### 4. ☀️ Morning Pep Talk (personal automation)
**Automation** → Time of Day 7:00 → **Get Upcoming Events** + **Get Current Weather** → **Use Model** (*"Write a cheerful
60-word briefing: weather, first meeting, one tiny challenge"*) → **Speak Text** or notification.

### 5. 🎙️ Meeting Memo → Action Items
**Record Audio** (or pick a voice memo) → transcribe → **Use Model** (*"List decisions, action items with owners, and open
questions"*) → **Create Reminder** for each action item.

> [!TIP]
> **💡 Put it on a button**
> Assign your favorite shortcut to the **Action Button** (iPhone 15 Pro and later), **Back Tap** (Settings → Accessibility →
> Touch → Back Tap), a Home Screen icon, a Lock Screen widget, or a **Siri phrase**. The best automation is the one that's
> one tap away.

## ⏰ Personal automations: triggers that fire on their own

<details class="eli5">
<summary>🧸 ELI5</summary>

Some magic buttons press themselves: at a certain time, when you arrive somewhere, when you open an app, or when you tap
your phone on a little sticker (an NFC tag).

</details>

Shortcuts → **Automation** tab lets shortcuts run on triggers:

| Trigger | Idea |
|---|---|
| Time of day | Morning briefing, evening journal prompt |
| Arrive / leave a location | "Arrived at gym" → start workout playlist + log visit |
| Open an app | Open banking app → show this month's spending summary |
| Focus mode on/off | Work focus → post "heads-down" status to Slack via webhook |
| Charger connected at night | Generate tomorrow's plan from your calendar |
| **NFC tag** tapped | Tap the fridge sticker → add groceries by voice |
| CarPlay connects | Read out your first meeting and the traffic |

## 🤖 Android: Gemini, Tasker & friends

<details class="eli5">
<summary>🧸 ELI5</summary>

Android phones have Gemini built in, and apps like Tasker let you build very powerful magic buttons. You can also call your
robot recipes on the internet with a single tap.

</details>

| Tool | What it's great at |
|---|---|
| **Gemini** (built in) | Voice assistant, screen questions ("what's on my screen?"), and app actions |
| **Google Home routines** | Smart home + phone routines ("Good night" → lights off, alarm set, tomorrow's weather) |
| **Tasker** | The ultimate Android automation power tool: triggers, conditions, HTTP requests, AI actions via APIs |
| **MacroDroid / Automate** | Friendlier Tasker-style automation |
| **HTTP Shortcuts** | Home-screen buttons that call webhooks and APIs (perfect for n8n/Zapier) |

**Recipe:** HTTP Shortcuts button → prompts for text (or voice) → POSTs to your n8n **idea inbox** webhook → Claude categorizes
it → Notion. ([Importable workflow](../../examples/n8n-workflows/idea-inbox-to-notion.json).)

## 💻 Mac: Shortcuts, Raycast & more

<details class="eli5">
<summary>🧸 ELI5</summary>

On a Mac, you can press a keyboard shortcut anywhere to ask AI about what's selected, rename files automatically, or run
little AI helpers from a search bar.

</details>

| Tool | AI superpowers |
|---|---|
| **Shortcuts for Mac** | Same **Use Model** action, and it can run from the menu bar or keyboard shortcuts |
| **Raycast** | A launcher with **Raycast AI** (many models), AI commands on selected text, extensions, and **MCP** support |
| **Alfred** | Workflows can call AI APIs and scripts |
| **Keyboard Maestro** | Deep macro automation, and AI can write the macros for you |
| **Hazel** | Folder rules ("PDF lands in Downloads → rename by content → file it") |
| **Claude Desktop / ChatGPT app** | Global shortcuts, screen or window sharing, local MCP servers |

**Favorite trick:** a Raycast AI command bound to a hotkey, "Rewrite selection: friendlier, shorter," works in every app.

## 🪟 Windows: Power Automate, AutoHotkey & Copilot

<details class="eli5">
<summary>🧸 ELI5</summary>

Windows has its own robot kitchen (Power Automate), a classic keyboard-magic tool (AutoHotkey), and Copilot built right in.
AI can even write the AutoHotkey scripts for you.

</details>

| Tool | AI superpowers |
|---|---|
| **Copilot** (and the Copilot key on newer keyboards) | Ask about your screen, files and settings |
| **Power Automate Desktop** | Free desktop automation and RPA ("click this, type that"), with AI actions and cloud flows |
| **AutoHotkey** | Hotkeys and text macros. Ask Claude: *"Write an AutoHotkey v2 script that…"* |
| **PowerToys** | Handy utilities, including AI-assisted paste features in recent versions |
| **Raycast for Windows** | The same launcher-with-AI idea |

## 🐧 Terminal lovers (Mac, Linux, Windows)

<details class="eli5">
<summary>🧸 ELI5</summary>

If you like typing commands, you can pipe any text into an AI from the terminal and get answers back, then schedule it to
run automatically.

</details>

- **`llm`** (Simon Willison's CLI tool) supports many models, plugins and logging: `cat notes.txt | llm "summarize"`.
- **`claude -p`** runs Claude Code headless in scripts: `git diff | claude -p "write a commit message"`
  ([Claude Code Masterclass](../part-7-building-with-ai/62-claude-code-masterclass.md)).
- **cron / launchd / Task Scheduler** run scripts on schedules.
- **espanso** (open source) gives you text-expander snippets that can run scripts, including AI calls.

## ⌨️ Text expanders + AI

<details class="eli5">
<summary>🧸 ELI5</summary>

Text expanders turn tiny codes into big text. Type ";reply" and a whole polite email appears. Add AI and the snippet can
write something fresh each time.

</details>

- **Static snippets:** your address, email templates, signatures (espanso, TextExpander, Raycast snippets).
- **Dynamic AI snippets:** `;fix` → sends the current selection to an AI and replaces it with a corrected version.
- **Prompt snippets:** keep your best prompts one shortcut away (`;eli5`, `;critique`, `;summarize`).

## 🔐 Privacy notes

<details class="eli5">
<summary>🧸 ELI5</summary>

Some magic buttons think on your phone (very private), and some send your stuff to the cloud. Choose on-device for secrets
like health or money notes.

</details>

- **On-device models** keep data on your phone, which is best for journals, health notes and personal stuff.
- **Private Cloud Compute** is designed so Apple can't access your data, a good middle ground.
- **Third-party AI** (ChatGPT, Claude via webhooks) follows that provider's policies ([Privacy & Your Data](../part-12-mastery/104-privacy-and-your-data.md)).
- Keep **webhook URLs and API keys** out of shared shortcuts. Anyone with the shortcut can use them.

## 🎯 Key takeaways

- Devices bring unique **triggers** (voice, camera, location, time, clipboard, NFC) that make AI capture effortless.
- iOS 26's **Use Model** action puts on-device, private cloud or ChatGPT models inside any shortcut.
- Android (Tasker, HTTP Shortcuts), Mac (Raycast, Shortcuts), Windows (Power Automate, AutoHotkey) and terminals all
  connect to AI and to your **webhooks**.
- Put your best automation **one tap away**: Action Button, Back Tap, widgets, hotkeys.

## 🧠 Check yourself

<details class="quiz">
<summary>❓ 1. Which Use Model option keeps a journaling shortcut fully on your phone?</summary>

**On-Device**.

</details>

<details class="quiz">
<summary>❓ 2. How can an Android home-screen button send an idea to your n8n workflow?</summary>

With **HTTP Shortcuts** (or Tasker) POSTing JSON to your n8n **webhook** URL.

</details>

<details class="quiz">
<summary>❓ 3. You want AI to rewrite selected text in any app on your Mac. What's a quick way?</summary>

A **Raycast AI command** (or a Mac Shortcut) bound to a **hotkey**.

</details>

> [!TIP]
> **🎮 Try this**
> Build recipe **#1 (Brain Dump → Organized Note)** and assign it to your Action Button, Back Tap or a hotkey. Use it for
> every stray thought for one week. You'll be amazed how much clearer your head feels. 🧠✨

---

**Next:** [51 · Web Scraping & Monitoring with AI →](51-web-scraping-and-monitoring.md)
