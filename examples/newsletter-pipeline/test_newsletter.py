"""Offline tests (no API key, no internet):   python test_newsletter.py"""

from datetime import datetime, timedelta, timezone
from types import SimpleNamespace as NS

from newsletter import Issue, Pick, curate, gather, parse_feed, to_html, to_markdown

NOW = datetime.now(timezone.utc)
RECENT = (NOW - timedelta(days=1)).strftime("%a, %d %b %Y %H:%M:%S GMT")
OLD = (NOW - timedelta(days=30)).strftime("%a, %d %b %Y %H:%M:%S GMT")

RSS = f"""<?xml version="1.0"?><rss version="2.0"><channel><title>Tiny Blog</title>
<item><title>Fresh post</title><link>https://tiny.blog/fresh</link><description>New &amp; shiny</description><pubDate>{RECENT}</pubDate></item>
<item><title>Old post</title><link>https://tiny.blog/old</link><description>Dusty</description><pubDate>{OLD}</pubDate></item>
<item><title>Seen post</title><link>https://tiny.blog/seen</link><pubDate>{RECENT}</pubDate></item>
</channel></rss>"""

ATOM = f"""<?xml version="1.0" encoding="utf-8"?><feed xmlns="http://www.w3.org/2005/Atom"><title>Atom Place</title>
<entry><title>Atom entry</title><link rel="alternate" href="https://atom.place/1"/><summary>Hello</summary>
<updated>{(NOW - timedelta(hours=5)).isoformat()}</updated></entry>
<entry><title>Duplicate of fresh</title><link href="https://tiny.blog/fresh"/><updated>{NOW.isoformat()}</updated></entry>
</feed>"""


def test_parse_both_formats():
    rss = parse_feed(RSS)
    assert [i["title"] for i in rss] == ["Fresh post", "Old post", "Seen post"]
    assert rss[0]["source"] == "Tiny Blog" and rss[0]["published"].tzinfo
    atom = parse_feed(ATOM)
    assert atom[0]["url"] == "https://atom.place/1" and atom[0]["source"] == "Atom Place"


def test_gather_filters_dedupes_and_survives_broken_feeds():
    feeds = {"rss": RSS, "atom": ATOM}

    def fetcher(url):
        if url == "broken":
            raise OSError("feed is down")
        return feeds[url]

    items = gather(["rss", "broken", "atom"], days=7, seen={"https://tiny.blog/seen"}, fetcher=fetcher)
    urls = [i["url"] for i in items]
    assert "https://tiny.blog/old" not in urls, "old items are filtered out"
    assert "https://tiny.blog/seen" not in urls, "already-sent items are skipped"
    assert urls.count("https://tiny.blog/fresh") == 1, "duplicates across feeds are removed"
    assert urls[0] == "https://atom.place/1", "newest first"


def test_render_escapes_html():
    issue = Issue(subject="Hello <world>", intro="Hi & welcome",
                  picks=[Pick(title="<script>x</script>", url="https://a.b/?q=1&r=2", why_it_matters="Because", tag="tools")],
                  try_this="Build something")
    page = to_html(issue)
    assert "<script>x</script>" not in page and "&lt;script&gt;" in page
    assert "https://a.b/?q=1&amp;r=2" in page
    assert to_markdown(issue).startswith("# Hello <world>")


def test_curate_uses_structured_output():
    expected = Issue(subject="This week in AI", intro="Hi!", picks=[], try_this="Try it")

    class FakeMessages:
        def parse(self, **kwargs):
            assert kwargs["output_format"] is Issue
            assert "[1] Fresh post" in kwargs["messages"][0]["content"]
            return NS(parsed_output=expected)

    items = [{"title": "Fresh post", "url": "https://tiny.blog/fresh", "summary": "x", "source": "Tiny Blog"}]
    assert curate(items, "testers", 3, client=NS(messages=FakeMessages())) is expected


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print(f"✅ {name}")
    print("🎉 All newsletter tests passed.")
