# 34 · AI for Small Business & Side Hustles 🏪🚀

For a small business, AI is like hiring a marketing assistant, a bookkeeper's helper, a receptionist, and an
analyst for less than the cost of lunch each month. This chapter maps AI to every part of running a business, with
concrete setups you can deploy this week.

---

## Where AI pays off fastest 💰

| Area | High-impact uses | Start with |
|---|---|---|
| 📣 **Marketing** | Content, social posts, ad variants, email campaigns, SEO | Claude/ChatGPT + Canva AI + a scheduler |
| 💬 **Customer service** | FAQ chatbot, email drafts, review responses | A chatbot on your website + email drafting |
| 📞 **Front desk** | Answering calls, booking, after-hours messages | A voice agent ([Ch. 31](../part-8-creative-ai/56-voice-agents.md)) |
| 💼 **Sales** | Lead research, personalized outreach, proposal drafts | CRM with AI + Zapier/Make |
| 🧾 **Admin & finance** | Invoice extraction, expense categorizing, reminders | Automation + accounting software AI |
| 📊 **Insights** | Sales analysis, customer feedback themes, forecasting | Spreadsheet AI / code-execution chat ([Ch. 36](71-data-analysis.md)) |
| 📋 **Operations** | SOPs, checklists, training docs, scheduling | Notion/Docs + AI |

## Setup 1: The marketing engine 📣 (an afternoon)

1. **Brand brief:** *"Interview me about my business, then write a brand voice guide, 3 customer personas, and
   10 content pillars."* Save it in a Project so every future chat knows your business.
2. **Monthly content calendar:** *"Create a 4-week social calendar using my pillars: 3 posts per week, with captions,
   hashtags, and image ideas."*
3. **Visuals:** Canva AI with your brand kit.
4. **Schedule:** Buffer/Later/Meta Business Suite.
5. **Automate:** new blog post or product → AI drafts → posts queue for your approval ([Ch. 11](../part-3-automation/18-zapier-and-make-walkthroughs.md)).

## Setup 2: The customer-service copilot 💬

1. **Write your knowledge base:** hours, pricing, policies, FAQs, and troubleshooting in one doc. (Have AI draft it from your emails!)
2. **Website chatbot:** many website builders and help desks (Intercom, Zendesk, HubSpot, Tidio, Shopify apps) offer AI
   bots trained on your docs. Or build one with n8n + RAG ([Ch. 24](../part-6-knowledge-and-memory/43-build-a-rag-system.md)).
3. **Email drafts:** a Zapier/n8n flow classifies incoming support emails and **drafts** replies using your knowledge base. You approve and send.
4. **Reviews:** *"Draft warm, specific replies to these 10 Google reviews. For negative ones, apologize, address the issue, and offer to make it right."*

**Golden rule:** AI drafts, and **humans approve** anything involving refunds, complaints, or promises.

## Setup 3: Admin autopilot 🧾

| Flow | Tools |
|---|---|
| Invoice emails → extract → accounting | Make/Zapier + AI extraction ([Ch. 11 walkthrough 5](../part-3-automation/18-zapier-and-make-walkthroughs.md)) |
| Receipt photos → expense sheet | Phone → n8n → vision model → Sheets |
| Late payment reminders | Accounting software automations + AI-written friendly nudges |
| Meeting notes → CRM | AI notetaker → CRM updates via Zapier |
| Contracts | AI summarizes key terms and dates → calendar reminders (a lawyer still reviews important contracts!) |

## Setup 4: Business insights 📊

Export your sales, customers, or reviews as CSV → upload to an AI with code execution:
- *"Which products are growing fastest? Which customers haven't ordered in 90 days?"*
- *"Cluster these 300 reviews into themes, with counts and representative quotes."*
- *"Forecast next quarter's revenue with a simple model and explain the assumptions."*

## Side-hustle ideas powered by AI 💡

| Idea | AI's role |
|---|---|
| Niche newsletter | Research, drafting, repurposing |
| Local business AI consultant | Set up chatbots, automations, and content systems for other businesses (you're learning exactly these skills!) |
| Automation builder (n8n/Make/Zapier freelancer) | Build workflows for clients |
| Print-on-demand designs | Image generation + mockups (check licensing!) |
| Faceless YouTube / podcast | The production pipelines in [Ch. 30](../part-8-creative-ai/54-video-and-audio-production.md) |
| Micro-SaaS / simple web apps | Vibe-coded tools solving one niche problem ([Ch. 19](../part-5-building-with-ai/34-vibe-coding-your-first-app.md)) |
| Custom GPTs, skills, or MCP servers for a niche | Package expertise as AI tools |

## Guardrails for businesses ⚖️
- **Privacy:** check data policies before uploading customer data. Use business/team plans with appropriate settings.
- **Accuracy:** AI can make up policies or prices, so ground chatbots in your docs and test them hard.
- **Disclosure:** let customers know when they're talking to AI, and always offer a human path.
- **Regulated stuff** (legal, medical, financial advice): AI assists professionals, and it doesn't replace them.
- **Keep your voice:** customers buy from *you*. Let AI handle the busywork so you can be more human, not less.

---

### 🎮 Try this
Do **Setup 1, step 1** right now: have AI interview you and write your brand brief. Even if you don't have a business yet,
do it for a dream one. It's fun, and it's the foundation for everything else. 🏪

---

**Next:** [35 · Life Admin & Personal Productivity →](64-life-admin-and-productivity.md)
