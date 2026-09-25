# 📰 Newsletter Pipeline: feeds in, a lovely email out

A small, readable Python pipeline that turns any RSS or Atom feeds into a **curated newsletter**: Claude picks the best items,
writes a warm "why it matters" for each, and you get a beautiful HTML email (plus a Markdown copy).

```
feeds.txt → fetch & parse → last 7 days → skip already-sent → 🤖 Claude curates → 💌 HTML + Markdown → 📬 send (optional)
```

Companion kit for **[Build-Along: The Automated Newsletter](../../manual/part-13-build-alongs/118-build-along-automated-newsletter.md)**.

## Quick start 🚀

```bash
cd examples/newsletter-pipeline
pip install -r requirements.txt
python test_newsletter.py                # offline tests: no key, no internet
python newsletter.py --dry-run           # real feeds, no AI: check fetching and the email design (see out/)

export ANTHROPIC_API_KEY=sk-ant-...
python newsletter.py                     # a Claude-curated issue in out/
python newsletter.py --audience "busy parents who love cooking" --count 7
```

Open `out/newsletter-YYYY-MM-DD.html` in your browser to see the email. 🎨

## Send it by email 📬

Set these environment variables (most email providers offer "app passwords" for SMTP), then add `--send`:

```bash
export SMTP_HOST=smtp.gmail.com SMTP_PORT=587 SMTP_USER=you@example.com SMTP_PASSWORD=your-app-password
export NEWSLETTER_TO=you@example.com
python newsletter.py --send
```

> For a real list of subscribers, send through a newsletter platform (Beehiiv, Buttondown, Kit, Substack) instead:
> they handle unsubscribes, deliverability and privacy laws for you.

## Put it on autopilot ⏰

- **cron:** `0 7 * * MON cd /path/to/newsletter-pipeline && python newsletter.py --send`
- **GitHub Actions:** a `schedule` workflow with your API key and SMTP password as repository secrets.
- **n8n:** the same idea visually: see [Morning AI Digest](../n8n-workflows/morning-ai-digest.json).

## How it works 🧩

| Piece | What it teaches |
|---|---|
| `parse_feed()` | Parsing RSS 2.0 *and* Atom with only the standard library |
| `gather()` | Freshness filtering, de-duplication across feeds, and surviving broken feeds |
| `curate()` | **Structured output**: Claude fills an `Issue` Pydantic model, so there's no fragile JSON parsing |
| `to_html()` | An email-safe design with inline styles, and HTML escaping so feed content can't break your layout |
| `seen.json` | Memory between runs: nothing is sent twice |

## Make it yours 🎨

- Edit `feeds.txt`: blogs, subreddits (`https://www.reddit.com/r/LocalLLaMA/top/.rss?t=week`), YouTube channels, news.
- Change `--audience` to write for a different crowd.
- Add a section: "one tool of the week," "a question from a reader," or a joke. 😄
- Post the Markdown to Slack, Discord or your blog.
