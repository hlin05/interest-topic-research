#!/usr/bin/env python3
"""Grok social signal scout — collects recent social signals for a topic via xAI API."""

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.request

# Allow running as standalone script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.topic_config import find_topic, topic_dir


def request_raw(base_url, headers, method, path, payload=None):
    body = None
    if payload is not None:
        body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url=f"{base_url}{path}",
        method=method,
        headers=headers,
        data=body,
    )
    try:
        with urllib.request.urlopen(req, timeout=45) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode("utf-8", errors="replace")
    except urllib.error.URLError as err:
        return None, str(err)


def decode_json(raw_text):
    try:
        return json.loads(raw_text)
    except json.JSONDecodeError:
        return None


def extract_chat_text(response_payload):
    choices = response_payload.get("choices", [])
    if not choices:
        return ""
    content = choices[0].get("message", {}).get("content", "")
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        chunks = []
        for part in content:
            if isinstance(part, dict) and part.get("text"):
                chunks.append(str(part["text"]))
        return "\n".join(chunks).strip()
    return ""


def extract_responses_text(response_payload):
    direct = str(response_payload.get("output_text") or "").strip()
    if direct:
        return direct
    chunks = []
    for item in response_payload.get("output", []):
        if item.get("type") != "message":
            continue
        for part in item.get("content", []):
            part_type = part.get("type")
            if part_type in ("output_text", "text"):
                text_value = str(part.get("text") or "").strip()
                if text_value:
                    chunks.append(text_value)
    return "\n".join(chunks).strip()


def main():
    parser = argparse.ArgumentParser(description="Grok social signal scout")
    parser.add_argument("--topic-id", required=True, help="Topic ID from topics.yml")
    args = parser.parse_args()

    topic = find_topic(args.topic_id)
    keywords = topic.get("grok_keywords", "")
    description = topic.get("description", "")
    topic_name = topic.get("name", args.topic_id)

    api_key = os.environ.get("XAI_API_KEY")
    if not api_key:
        print("Error: XAI_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    base_url = (os.getenv("XAI_BASE_URL") or "https://api.x.ai").rstrip("/")
    model = (os.getenv("GROK_MODEL") or "").strip() or "grok-4-1-fast-reasoning"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "weekly-resource-research/2.0",
    }

    debug = {
        "timestamp": dt.datetime.now(dt.timezone.utc).isoformat(),
        "base_url": base_url,
        "model": model,
        "topic_id": args.topic_id,
        "attempts": [],
    }

    prompt = (
        f"Find very recent (last 14 days) leads for {topic_name} specifically. "
        f"Focus on: {description}. "
        f"Search keywords: {keywords}. "
        "Prioritize resources that received notable social discussion (for example on X/Twitter), "
        "but each item must include a primary technical URL (paper/repo/blog) with verifiable public access. "
        "Return markdown starting with '## Grok Social Signals' and then up to 10 bullets. "
        "Each bullet format: - [Title](PRIMARY_URL) - one-line relevance note; social evidence: "
        "SOCIAL_URL or 'n/a'."
    )

    # Probe API availability
    for probe_path in ("/v1/models", "/v1/language-models"):
        status, raw = request_raw(base_url, headers, "GET", probe_path)
        debug["attempts"].append({
            "name": f"probe {probe_path}",
            "status": status,
            "body_preview": (raw or "")[:500],
        })

    # Try responses API first
    responses_payload = {
        "model": model,
        "input": [
            {"role": "system", "content": "You are a concise research scout."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }
    status, raw = request_raw(base_url, headers, "POST", "/v1/responses", responses_payload)
    debug["attempts"].append({
        "name": "responses",
        "status": status,
        "body_preview": (raw or "")[:500],
    })

    text = ""
    if status is not None and 200 <= status < 300:
        payload = decode_json(raw or "")
        if payload:
            text = extract_responses_text(payload)

    # Fallback to chat completions
    if not text:
        chat_payload = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a concise research scout."},
                {"role": "user", "content": prompt},
            ],
            "temperature": 0.2,
        }
        status, raw = request_raw(base_url, headers, "POST", "/v1/chat/completions", chat_payload)
        debug["attempts"].append({
            "name": "chat_completions",
            "status": status,
            "body_preview": (raw or "")[:500],
        })
        if status is not None and 200 <= status < 300:
            payload = decode_json(raw or "")
            if payload:
                text = extract_chat_text(payload)

    if not text:
        print("Grok diagnostics:", file=sys.stderr)
        print(json.dumps(debug, indent=2), file=sys.stderr)
        print("Grok social signal collection failed. See diagnostics above.", file=sys.stderr)
        sys.exit(1)

    # Write output
    out_dir = topic_dir(args.topic_id)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "grok-signals.md")

    output_lines = [
        f"# Grok Scout ({dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d')})",
        "",
        f"- Model: `{model}`",
        f"- Topic: {topic_name}",
        "",
        text,
    ]
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write("\n".join(output_lines).strip() + "\n")

    print(f"Grok signals written to {out_path}")
    print("Grok diagnostics:")
    print(json.dumps(debug, indent=2))


if __name__ == "__main__":
    main()
