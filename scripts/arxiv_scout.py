#!/usr/bin/env python3
"""arXiv RSS scout — collects recent papers from topic-specific RSS feeds."""

import argparse
import datetime as dt
import html
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.topic_config import find_topic, topic_dir


def clean_text(value):
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    return " ".join(value.split())


def main():
    parser = argparse.ArgumentParser(description="arXiv RSS scout")
    parser.add_argument("--topic-id", required=True, help="Topic ID from topics.yml")
    args = parser.parse_args()

    topic = find_topic(args.topic_id)
    feeds = topic.get("arxiv_feeds", [])
    topic_name = topic.get("name", args.topic_id)

    if not feeds:
        print(f"Warning: no arxiv_feeds configured for topic '{args.topic_id}'", file=sys.stderr)

    cutoff = dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=14)
    collected = []
    max_items = 18

    for feed_entry in feeds:
        if not isinstance(feed_entry, dict) or "url" not in feed_entry:
            print(f"Warning: skipping malformed feed entry: {feed_entry!r}", file=sys.stderr)
            continue
        feed_name = feed_entry.get("name", feed_entry["url"])
        feed_url = feed_entry["url"]
        try:
            with urllib.request.urlopen(feed_url, timeout=30) as resp:
                xml_text = resp.read().decode("utf-8", errors="replace")
            root = ET.fromstring(xml_text)
        except Exception as exc:
            collected.append((feed_name, None, None, f"Feed fetch failed: {exc}"))
            continue

        channel = root.find("channel")
        if channel is None:
            collected.append((feed_name, None, None, "Missing RSS channel data"))
            continue

        for item in channel.findall("item"):
            title = clean_text(item.findtext("title", default=""))
            link = clean_text(item.findtext("link", default=""))
            pub_raw = clean_text(item.findtext("pubDate", default=""))
            if not title or not link:
                continue
            try:
                published = dt.datetime.strptime(pub_raw, "%a, %d %b %Y %H:%M:%S %z")
            except Exception:
                published = None
            if published is None or published < cutoff:
                continue
            collected.append((feed_name, title, link, published.isoformat()))
            if sum(1 for c in collected if c[1]) >= max_items:
                break
        if sum(1 for c in collected if c[1]) >= max_items:
            break

    lines = [
        f"# arXiv RSS Scout ({dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d')})",
        "",
        f"Topic: {topic_name}",
        "",
        "Recent papers from configured arXiv RSS feeds (last 14 days).",
        "",
    ]

    has_items = False
    for source, title, link, extra in collected:
        if title and link:
            has_items = True
            lines.append(f"- [{title}]({link}) ({source})")
        elif extra:
            lines.append(f"- {source}: {extra}")

    if not has_items:
        lines.append("- No recent arXiv items found from configured feeds.")

    out_dir = topic_dir(args.topic_id)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "arxiv-signals.md")

    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(lines).strip() + "\n")

    print(f"arXiv signals written to {out_path}")


if __name__ == "__main__":
    main()
