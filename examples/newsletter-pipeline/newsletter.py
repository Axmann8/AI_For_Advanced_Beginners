"""
📰 Newsletter Pipeline: RSS feeds → Claude picks the best → a beautiful email (or an HTML file).

    feeds.txt → fetch & parse → last N days → skip already-sent → Claude curates → HTML + Markdown → send or save

Run it:
    pip install -r requirements.txt
    python newsletter.py --dry-run                # no API key: just fetch, filter and render the latest items
    export ANTHROPIC_API_KEY=sk-ant-...
    python newsletter.py                          # curated issue saved to out/
    python newsletter.py --send                   # also email it (set the SMTP_* variables below)

Email settings (environment variables, only needed for --send):
    SMTP_HOST, SMTP_PORT (default 587), SMTP_USER, SMTP_PASSWORD, NEWSLETTER_TO, NEWSLETTER_FROM (default SMTP_USER)
"""

from __future__ import annotations

import argparse
import html
import json
import os
import smtplib
import urllib.request
import xml.etree.ElementTree as ET
from datetime import date, datetime, timedelta, timezone
from email.message import EmailMessage
from email.utils import parsedate_to_datetime
from pathlib import Path

from pydantic import BaseModel, Field

HERE = Path(__file__).parent
MODEL = "claude-opus-5"
SEEN_FILE = HERE / "seen.json"
OUT_DIR = HERE / "out"
ATOM = "{http://www.w3.org/2005/Atom}"


# ------------------------------------------------------------------ 1. fetch & parse ---
def parse_date(value: str | None) -> datetime | None:
    if not value:
        return None
    value = value.strip()
    try:
        parsed = parsedate_to_datetime(value)  # RSS style: "Tue, 23 Sep 2026 08:00:00 GMT"
    except (TypeError, ValueError):
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))  # Atom style: ISO 8601
        except ValueError:
            return None
    return parsed if parsed.tzinfo else parsed.replace(tzinfo=timezone.utc)


def parse_feed(xml_text: str, source: str = "") -> list[dict]:
    """Parse RSS 2.0 or Atom into simple dicts: title, url, summary, published, source."""
    root = ET.fromstring(xml_text)
    items = []
    if root.tag == f"{ATOM}feed":
        feed_title = root.findtext(f"{ATOM}title", default=source)
        for entry in root.findall(f"{ATOM}entry"):
            link = entry.find(f"{ATOM}link[@rel='alternate']")
            if link is None:  # (Elements without children are falsy, so compare with None, never use `or`.)
                link = entry.find(f"{ATOM}link")
            items.append({
                "title": (entry.findtext(f"{ATOM}title") or "").strip(),
                "url": link.get("href") if link is not None else "",
                "summary": (entry.findtext(f"{ATOM}summary") or entry.findtext(f"{ATOM}content") or "").strip(),
                "published": parse_date(entry.findtext(f"{ATOM}published") or entry.findtext(f"{ATOM}updated")),
                "source": feed_title,
            })
    else:
        channel = root.find("channel")
        feed_title = channel.findtext("title", default=source) if channel is not None else source
        for item in root.iter("item"):
            items.append({
                "title": (item.findtext("title") or "").strip(),
                "url": (item.findtext("link") or "").strip(),
                "summary": (item.findtext("description") or "").strip(),
                "published": parse_date(item.findtext("pubDate")),
                "source": feed_title,
            })
    return [i for i in items if i["title"] and i["url"]]


def fetch(url: str) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "newsletter-pipeline/1.0 (+https://github.com)"})
    with urllib.request.urlopen(request, timeout=20) as response:
        return response.read().decode("utf-8", errors="replace")


def gather(feed_urls: list[str], days: int, seen: set[str], fetcher=fetch) -> list[dict]:
    """Fetch every feed, keep recent unseen items, newest first. One broken feed never stops the issue."""
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    items, urls = [], set()
    for url in feed_urls:
        try:
            for item in parse_feed(fetcher(url), source=url):
                fresh = item["published"] is None or item["published"] >= cutoff
                if fresh and item["url"] not in seen and item["url"] not in urls:
                    items.append(item)
                    urls.add(item["url"])
        except Exception as err:  # noqa: BLE001: report and keep going
            print(f"  ⚠️ Skipping {url}: {err}")
    return sorted(items, key=lambda i: i["published"] or datetime.min.replace(tzinfo=timezone.utc), reverse=True)


# ---------------------------------------------------------------- 2. curate with AI ---
class Pick(BaseModel):
    title: str
    url: str
    why_it_matters: str = Field(description="1–2 friendly sentences on why a reader should care")
    tag: str = Field(description="One short topic tag, e.g. 'tools', 'research', 'how-to'")


class Issue(BaseModel):
    subject: str = Field(description="An inviting email subject line, under 60 characters")
    intro: str = Field(description="2–3 warm sentences opening the issue")
    picks: list[Pick]
    try_this: str = Field(description="One concrete thing readers can try this week")


def curate(items: list[dict], audience: str, count: int, client=None) -> Issue:
    import anthropic

    client = client or anthropic.Anthropic()
    listing = "\n".join(
        f"[{n}] {i['title']}\n    {i['url']}\n    {html.unescape(i['summary'])[:300]}" for n, i in enumerate(items[:60], 1)
    )
    response = client.messages.parse(
        model=MODEL,
        max_tokens=8000,
        system=(
            f"You edit a friendly newsletter for {audience}. Pick the {count} most useful, interesting and varied items. "
            "Only use items from the list, with their exact URLs. Be warm, specific and never hypey."
        ),
        messages=[{"role": "user", "content": f"This week's candidate items:\n\n{listing}"}],
        output_format=Issue,
    )
    return response.parsed_output


def fallback_issue(items: list[dict], count: int) -> Issue:
    """--dry-run: no AI, just the newest items, so you can test everything else for free."""
    picks = [Pick(title=i["title"], url=i["url"], why_it_matters=f"From {i['source']}.", tag="new") for i in items[:count]]
    return Issue(subject=f"Your digest for {date.today():%B %d}", intro="Here's what's new this week (dry run, no AI).",
                 picks=picks, try_this="Run without --dry-run to let Claude curate the issue.")


# ------------------------------------------------------------------- 3. render & send ---
def to_markdown(issue: Issue) -> str:
    lines = [f"# {issue.subject}", "", issue.intro, ""]
    for n, pick in enumerate(issue.picks, 1):
        lines += [f"## {n}. [{pick.title}]({pick.url})", f"*{pick.tag}*: {pick.why_it_matters}", ""]
    lines += ["---", f"🎮 **Try this week:** {issue.try_this}", ""]
    return "\n".join(lines)


def to_html(issue: Issue) -> str:
    e = html.escape
    cards = "".join(
        f'<div style="border:1px solid #e9e3ff;border-radius:14px;padding:16px 18px;margin:14px 0;background:#fff">'
        f'<div style="font-size:12px;color:#7c3aed;text-transform:uppercase;letter-spacing:.06em">{e(p.tag)}</div>'
        f'<a href="{e(p.url, quote=True)}" style="font-size:18px;font-weight:700;color:#1f1147;text-decoration:none">{e(p.title)}</a>'
        f'<p style="margin:8px 0 0;color:#3f3a52;line-height:1.55">{e(p.why_it_matters)}</p></div>'
        for p in issue.picks
    )
    return f"""<!doctype html><html><body style="margin:0;background:#f6f3ff;font-family:Inter,Segoe UI,Arial,sans-serif">
<div style="max-width:620px;margin:0 auto;padding:28px 18px">
  <div style="background:linear-gradient(135deg,#6d28d9,#db2777);color:#fff;border-radius:18px;padding:24px 22px">
    <div style="font-size:13px;opacity:.85">{date.today():%A, %B %d, %Y}</div>
    <h1 style="margin:6px 0 0;font-size:26px">{e(issue.subject)}</h1>
  </div>
  <p style="color:#3f3a52;line-height:1.6;font-size:16px">{e(issue.intro)}</p>
  {cards}
  <div style="background:#fff7e6;border-radius:14px;padding:16px 18px;color:#5b3b00">🎮 <b>Try this week:</b> {e(issue.try_this)}</div>
  <p style="color:#8a84a3;font-size:12px;margin-top:24px">Curated with a little help from Claude. Reply to say hi!</p>
</div></body></html>"""


def send_email(issue: Issue, html_body: str, text_body: str) -> None:
    host, user, password, to = (os.environ.get(k) for k in ("SMTP_HOST", "SMTP_USER", "SMTP_PASSWORD", "NEWSLETTER_TO"))
    if not all([host, user, password, to]):
        raise SystemExit("Set SMTP_HOST, SMTP_USER, SMTP_PASSWORD and NEWSLETTER_TO to use --send.")
    message = EmailMessage()
    message["Subject"], message["From"], message["To"] = issue.subject, os.environ.get("NEWSLETTER_FROM", user), to
    message.set_content(text_body)
    message.add_alternative(html_body, subtype="html")
    with smtplib.SMTP(host, int(os.environ.get("SMTP_PORT", 587))) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        smtp.send_message(message)


def main() -> None:
    parser = argparse.ArgumentParser(description="Turn RSS feeds into a curated newsletter.")
    parser.add_argument("--feeds", default=str(HERE / "feeds.txt"))
    parser.add_argument("--days", type=int, default=7)
    parser.add_argument("--count", type=int, default=5)
    parser.add_argument("--audience", default="curious people learning to build with AI")
    parser.add_argument("--dry-run", action="store_true", help="skip the AI step (no API key needed)")
    parser.add_argument("--send", action="store_true", help="email the issue via SMTP")
    args = parser.parse_args()

    feed_urls = [line.strip() for line in Path(args.feeds).read_text().splitlines()
                 if line.strip() and not line.startswith("#")]
    seen = set(json.loads(SEEN_FILE.read_text())) if SEEN_FILE.exists() else set()

    print(f"📥 Fetching {len(feed_urls)} feeds…")
    items = gather(feed_urls, args.days, seen)
    print(f"🧺 {len(items)} fresh items")
    if not items:
        print("Nothing new this time. 🌙")
        return

    issue = fallback_issue(items, args.count) if args.dry_run else curate(items, args.audience, args.count)
    OUT_DIR.mkdir(exist_ok=True)
    stem = OUT_DIR / f"newsletter-{date.today().isoformat()}"
    html_body, text_body = to_html(issue), to_markdown(issue)
    stem.with_suffix(".html").write_text(html_body, encoding="utf-8")
    stem.with_suffix(".md").write_text(text_body, encoding="utf-8")
    print(f"💌 Saved {stem}.html and .md")

    if args.send:
        send_email(issue, html_body, text_body)
        print("📬 Sent!")
    if not args.dry_run:
        SEEN_FILE.write_text(json.dumps(sorted(seen | {p.url for p in issue.picks}), indent=2))


if __name__ == "__main__":
    main()
