# Multi-Topic Research Agent Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the single-topic awesome-list repository into a multi-topic research agent system with per-topic folders, GitHub Project boards, Claude-powered curation, and a smart CLI for adding topics.

**Architecture:** Central `topics.yml` registry drives a single GitHub Actions workflow that iterates all topics. Each topic has its own folder (`topics/<id>/`) with a curated README, and its own GitHub Project board. Standalone Python scripts handle scouting (Grok, arXiv) and curation (Anthropic Claude). A bash CLI scaffolds new topics with Claude-powered deduplication.

**Tech Stack:** Python 3.10+ (anthropic SDK, pyyaml), Bash, GitHub Actions, GitHub Projects v2 API via `gh` CLI, xAI Grok API, arXiv RSS feeds.

**Spec:** `docs/superpowers/specs/2026-03-22-multi-topic-research-agent-design.md`

---

## File Map

| File | Action | Responsibility |
|------|--------|---------------|
| `scripts/topic_config.py` | Create | Shared module: load `topics.yml`, find topic by ID, slug generation |
| `scripts/grok_scout.py` | Create | Grok social signal collector, topic-aware (extracted from workflow) |
| `scripts/arxiv_scout.py` | Create | arXiv RSS collector, topic-aware (extracted from workflow) |
| `scripts/claude_curate.py` | Create | Anthropic Claude curation pass (replaces Codex action) |
| `scripts/create_project_board.sh` | Create | GitHub Project board creation + column setup |
| `scripts/run_all_topics.py` | Create | Workflow orchestrator: iterates topics, manages git branches |
| `scripts/templates/topic-readme.md` | Create | Starter README template for new topics |
| `add-topic.sh` | Create | Smart topic CLI with Claude deduplication |
| `topics.yml` | Create | Central topic registry (seeded with agentic-ml) |
| `requirements.txt` | Create | Python dependencies |
| `topics/agentic-ml/README.md` | Move | Migrated from root `README.md` |
| `README.md` | Rewrite | Lightweight index of all topics |
| `.github/workflows/weekly-resource-research.yml` | Rewrite | Multi-topic iteration workflow |

**Note on naming:** The spec uses hyphenated filenames (`grok-scout.py`) but this plan uses underscores (`grok_scout.py`) because Python cannot import modules with hyphens. The spec's `create-project-board.sh` becomes `create_project_board.sh` for consistency. The plan also introduces `scripts/topic_config.py` (shared config module), `scripts/add_topic_impl.py` (CLI implementation), and `scripts/run_all_topics.py` (workflow orchestrator) which are not in the spec but are necessary for clean implementation.

---

### Task 1: Create shared topic config module

**Files:**
- Create: `scripts/__init__.py`
- Create: `scripts/topic_config.py`
- Create: `topics.yml`
- Create: `requirements.txt`

- [ ] **Step 1: Create `requirements.txt`**

```
anthropic>=0.40.0
pyyaml>=6.0
```

- [ ] **Step 2: Create `scripts/__init__.py`**

Empty file to make `scripts/` a Python package.

- [ ] **Step 3: Create `topics.yml` with the agentic-ml seed entry**

```yaml
topics:
  - id: agentic-ml
    name: "Awesome Agentic ML"
    description: "Autonomous AI systems that plan, execute, and iterate on machine learning workflows with minimal human intervention"
    grok_keywords: >-
      agentic ML, AutoML agents, autonomous machine learning,
      LLM ML engineering, ML workflow automation
    arxiv_feeds:
      - { name: "cs.AI", url: "https://rss.arxiv.org/rss/cs.AI" }
      - { name: "cs.LG", url: "https://rss.arxiv.org/rss/cs.LG" }
      - { name: "stat.ML", url: "https://rss.arxiv.org/rss/stat.ML" }
    inclusion_criteria:
      min_match: 3
      checklist:
        - "Goal-directed ML planning (selects or revises strategy for an ML objective)"
        - "Tool-using execution across ML lifecycle stages (data prep, feature engineering, model training, evaluation, experimentation)"
        - "Iterative feedback loop (uses metrics/errors/results to revise actions)"
        - "Empirical ML outcome (benchmark, competition result, ablation, or measurable improvement)"
    exclude:
      - "Generic web/desktop/coding agents without meaningful ML workflow contribution"
      - "Social-only announcements without a primary technical source (paper/repo/blog)"
      - "Stale resources unless there is a substantive new release/update in the recent window"
    github_project: null
```

- [ ] **Step 4: Create `scripts/topic_config.py`**

```python
"""Shared utilities for loading topic configuration from topics.yml."""

import os
import re
import sys

import yaml

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOPICS_FILE = os.path.join(REPO_ROOT, "topics.yml")


def load_topics():
    """Load and return the list of topics from topics.yml."""
    with open(TOPICS_FILE, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data.get("topics", [])


def find_topic(topic_id):
    """Find a topic by ID. Exits with error if not found."""
    for topic in load_topics():
        if topic["id"] == topic_id:
            return topic
    print(f"Error: topic '{topic_id}' not found in {TOPICS_FILE}", file=sys.stderr)
    sys.exit(1)


def slugify(name):
    """Convert a topic name to a URL-friendly slug."""
    slug = name.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def topic_dir(topic_id):
    """Return the absolute path to a topic's directory."""
    return os.path.join(REPO_ROOT, "topics", topic_id)


def topic_readme(topic_id):
    """Return the absolute path to a topic's README."""
    return os.path.join(topic_dir(topic_id), "README.md")


def suggestions_dir(topic_id):
    """Return the absolute path to a topic's suggestion log directory."""
    return os.path.join(REPO_ROOT, ".github", "research-suggestions", topic_id)


def save_topics(topics_list):
    """Write the topics list back to topics.yml."""
    with open(TOPICS_FILE, "w", encoding="utf-8") as f:
        yaml.dump({"topics": topics_list}, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
```

- [ ] **Step 5: Verify module loads**

Run: `cd C:/Users/taoga/projects/interest-topic-research && python -c "from scripts.topic_config import load_topics; print(load_topics()[0]['id'])"`
Expected: `agentic-ml`

- [ ] **Step 6: Commit**

```bash
git add requirements.txt scripts/__init__.py scripts/topic_config.py topics.yml
git commit -m "feat: add topic config module and seed topics.yml with agentic-ml"
```

---

### Task 2: Extract Grok scout into standalone script

**Files:**
- Create: `scripts/grok_scout.py`

The current inline Grok scout (workflow lines 50-219) is extracted into a standalone script that accepts `--topic-id` and reads config from `topics.yml`.

- [ ] **Step 1: Create `scripts/grok_scout.py`**

```python
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
```

- [ ] **Step 2: Verify script loads and parses args**

Run: `cd C:/Users/taoga/projects/interest-topic-research && python scripts/grok_scout.py --help`
Expected: Shows usage with `--topic-id` argument

- [ ] **Step 3: Commit**

```bash
git add scripts/grok_scout.py
git commit -m "feat: extract Grok scout into standalone topic-aware script"
```

---

### Task 3: Extract arXiv scout into standalone script

**Files:**
- Create: `scripts/arxiv_scout.py`

- [ ] **Step 1: Create `scripts/arxiv_scout.py`**

```python
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
        feed_name = feed_entry["name"]
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
```

- [ ] **Step 2: Verify script loads and parses args**

Run: `cd C:/Users/taoga/projects/interest-topic-research && python scripts/arxiv_scout.py --help`
Expected: Shows usage with `--topic-id` argument

- [ ] **Step 3: Commit**

```bash
git add scripts/arxiv_scout.py
git commit -m "feat: extract arXiv scout into standalone topic-aware script"
```

---

### Task 4: Create Claude curation script

**Files:**
- Create: `scripts/claude_curate.py`

- [ ] **Step 1: Create `scripts/claude_curate.py`**

```python
#!/usr/bin/env python3
"""Claude curation — evaluates scout signals and proposes README additions using Anthropic API."""

import argparse
import json
import os
import re
import sys

import anthropic

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.topic_config import find_topic, topic_dir, topic_readme


def read_file_or_empty(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return ""


def extract_json_from_response(text):
    """Extract JSON from a code fence in Claude's response."""
    pattern = r"```(?:json)?\s*\n(.*?)\n```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    # Try parsing the whole response as JSON
    return json.loads(text)


def insert_suggestion_into_readme(readme_content, suggestion):
    """Insert a suggestion into the correct section of the README.

    Finds the section by heading match and appends the entry as a table row
    or list item depending on section format.
    """
    section = suggestion["section"]
    title = suggestion["title"]
    url = suggestion["url"]
    description = suggestion["description"]

    # Look for a markdown table in the target section
    # Find the section heading
    section_pattern = re.compile(
        rf"^##\s+.*{re.escape(section)}.*$",
        re.MULTILINE | re.IGNORECASE,
    )
    match = section_pattern.search(readme_content)
    if not match:
        # Section not found — append before Contributing section
        contrib_match = re.search(r"^## Contributing", readme_content, re.MULTILINE)
        if contrib_match:
            new_section = (
                f"\n---\n\n## {section}\n\n"
                f"| Project | Description | Stars |\n"
                f"|---------|-------------|-------|\n"
                f"| [{title}]({url}) | {description} | - |\n"
            )
            pos = contrib_match.start()
            return readme_content[:pos] + new_section + "\n" + readme_content[pos:]
        # Fallback: append at end
        return readme_content + f"\n\n## {section}\n\n- [{title}]({url}) — {description}\n"

    # Find the end of the section (next ## heading or end of file)
    section_start = match.end()
    next_heading = re.search(r"^---$|^## ", readme_content[section_start:], re.MULTILINE)
    section_end = section_start + next_heading.start() if next_heading else len(readme_content)
    section_text = readme_content[section_start:section_end]

    # Check if section uses a table format
    if "|------" in section_text:
        # Find the last table row and insert after it
        table_rows = list(re.finditer(r"^\|.*\|$", section_text, re.MULTILINE))
        if table_rows:
            last_row_end = section_start + table_rows[-1].end()
            new_row = f"\n| [{title}]({url}) | {description} | - |"
            return readme_content[:last_row_end] + new_row + readme_content[last_row_end:]

    # List format — insert before section end
    new_entry = f"\n- [{title}]({url}) — {description}\n"
    return readme_content[:section_end] + new_entry + readme_content[section_end:]


def main():
    parser = argparse.ArgumentParser(description="Claude curation pass")
    parser.add_argument("--topic-id", required=True, help="Topic ID from topics.yml")
    args = parser.parse_args()

    topic = find_topic(args.topic_id)
    t_dir = topic_dir(args.topic_id)

    readme_path = topic_readme(args.topic_id)
    readme_content = read_file_or_empty(readme_path)
    grok_signals = read_file_or_empty(os.path.join(t_dir, "grok-signals.md"))
    arxiv_signals = read_file_or_empty(os.path.join(t_dir, "arxiv-signals.md"))

    if not readme_content:
        print(f"Error: no README found at {readme_path}", file=sys.stderr)
        sys.exit(1)

    # Build criteria text
    criteria = topic.get("inclusion_criteria", {})
    checklist = criteria.get("checklist", [])
    min_match = criteria.get("min_match", 3)
    excludes = topic.get("exclude", [])

    checklist_text = "\n".join(f"  - {c}" for c in checklist)
    exclude_text = "\n".join(f"  - {e}" for e in excludes)

    system_prompt = (
        f"You are curating an awesome list for {topic['name']}.\n"
        f"Topic description: {topic['description']}\n\n"
        f"Inclusion checklist (resource must satisfy at least {min_match} of {len(checklist)}):\n"
        f"{checklist_text}\n\n"
        f"Exclude or deprioritize:\n"
        f"{exclude_text}\n\n"
        "Return your response as JSON inside a code fence with this exact schema:\n"
        '```json\n'
        '{\n'
        '  "result": "FOUND" or "NONE",\n'
        '  "summary": "Brief scan summary",\n'
        '  "suggestions": [\n'
        '    {\n'
        '      "title": "Project Name",\n'
        '      "url": "https://...",\n'
        '      "section": "Section Name in README",\n'
        '      "description": "One-line description",\n'
        '      "criteria_met": ["criterion 1", "criterion 3"]\n'
        '    }\n'
        '  ]\n'
        '}\n'
        '```\n'
        "If no additions are warranted, return NONE with an empty suggestions array.\n"
        "Do NOT force suggestions when quality is low or novelty is weak.\n"
        "Only propose items NOT already present in the README."
    )

    user_message = (
        f"## Current README\n\n{readme_content}\n\n"
        f"## Grok Social Scout Signals\n\n{grok_signals or 'No Grok signals available.'}\n\n"
        f"## arXiv RSS Scout Signals\n\n{arxiv_signals or 'No arXiv signals available.'}\n\n"
        "Evaluate these signals against the inclusion criteria. "
        "Propose only high-confidence additions that are not already in the README."
    )

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("Error: ANTHROPIC_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=4096,
        temperature=0.2,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )

    response_text = response.content[0].text

    # Parse the structured response
    try:
        result = extract_json_from_response(response_text)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"Error: failed to parse Claude response as JSON: {e}", file=sys.stderr)
        print(f"Raw response:\n{response_text}", file=sys.stderr)
        sys.exit(1)

    decision = result.get("result", "NONE")
    summary = result.get("summary", "")
    suggestions = result.get("suggestions", [])

    # Write suggestions file
    suggestions_path = os.path.join(t_dir, "weekly-suggestions.md")
    with open(suggestions_path, "w", encoding="utf-8") as f:
        f.write(f"RESULT: {decision}\n")
        if summary:
            f.write(f"\n{summary}\n")
        if suggestions:
            f.write("\n## Suggestions\n\n")
            for s in suggestions:
                criteria_str = ", ".join(s.get("criteria_met", []))
                f.write(f"- [{s['title']}]({s['url']}) — {s['description']}\n")
                f.write(f"  Section: {s['section']} | Criteria: {criteria_str}\n\n")

    # If FOUND, update the README
    if decision == "FOUND" and suggestions:
        updated_readme = readme_content
        for s in suggestions:
            # Check the item isn't already in the README
            if s["url"] in updated_readme or s["title"] in updated_readme:
                print(f"Skipping duplicate: {s['title']}")
                continue
            updated_readme = insert_suggestion_into_readme(updated_readme, s)

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_readme)
        print(f"README updated at {readme_path}")

    # Output the result line for the workflow to parse
    print(f"RESULT: {decision}")
    if summary:
        print(summary)


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Verify script loads and parses args**

Run: `cd C:/Users/taoga/projects/interest-topic-research && python scripts/claude_curate.py --help`
Expected: Shows usage with `--topic-id` argument

- [ ] **Step 3: Commit**

```bash
git add scripts/claude_curate.py
git commit -m "feat: add Claude curation script using Anthropic API"
```

---

### Task 5: Migrate agentic-ml content to topics folder

**Files:**
- Move: `README.md` → `topics/agentic-ml/README.md`
- Create: `README.md` (new root index)

- [ ] **Step 1: Create topics directory and move README**

```bash
cd C:/Users/taoga/projects/interest-topic-research
mkdir -p topics/agentic-ml
git mv README.md topics/agentic-ml/README.md
```

- [ ] **Step 2: Create new root `README.md`**

```markdown
# Research Topics

Automated research agent system that scouts, curates, and maintains awesome lists across multiple topics using AI-powered signal collection and curation.

## How It Works

Each topic has its own curated awesome list maintained by a weekly Research Assistant Agent:

1. **Grok Scout** — collects recent social signals via xAI API
2. **arXiv Scout** — pulls recent papers from topic-specific RSS feeds
3. **Claude Curation** — evaluates candidates against topic-specific criteria using Anthropic Claude

## Topics

| Topic | Description |
|-------|-------------|
| [Agentic ML](topics/agentic-ml/) | Autonomous AI systems for ML workflows |

## Adding a Topic

```bash
./add-topic.sh "Your Topic Name"
```

The CLI will:
- Check for overlap with existing topics
- Generate topic-specific search keywords, RSS feeds, and inclusion criteria
- Create a GitHub Project board for tracking
- Scaffold the topic folder with a starter README

## Configuration

Topics are configured in [`topics.yml`](topics.yml). Each topic defines:
- Search keywords for social signal scouting
- arXiv RSS feed categories
- Inclusion/exclusion criteria for curation

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
```

- [ ] **Step 3: Move existing suggestion logs if present**

```bash
cd C:/Users/taoga/projects/interest-topic-research
if [ -d ".github/research-suggestions" ] && [ "$(ls -A .github/research-suggestions 2>/dev/null)" ]; then
  mkdir -p .github/research-suggestions/agentic-ml
  find .github/research-suggestions -maxdepth 1 -type f -exec git mv {} .github/research-suggestions/agentic-ml/ \;
fi
```

- [ ] **Step 4: Commit the migration**

```bash
git add README.md topics/agentic-ml/README.md .github/research-suggestions/
git commit -m "feat: migrate agentic-ml content to topics/ folder structure"
```

---

### Task 6: Create starter README template

**Files:**
- Create: `scripts/templates/topic-readme.md`

- [ ] **Step 1: Create the template**

```markdown
# {name} [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

{description}

---

## Scope

{scope}

**Inclusion checklist (meet at least {min_match} of {num_criteria}):**

{checklist}

**Exclude or deprioritize:**

{exclude}

---

## Research Assistant Agent

This topic is maintained by a weekly Research Assistant Agent. See the [main README](../../README.md) for details.

---

## Contents

- [Contributing](#contributing)

---

## Contributing

Contributions welcome! [Open an issue](../../../../issues) or submit a PR.

When proposing additions, include a short note on which inclusion criteria the item satisfies and link the strongest supporting evidence (paper/repo/benchmark/blog).

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
```

- [ ] **Step 2: Commit**

```bash
mkdir -p scripts/templates
git add scripts/templates/topic-readme.md
git commit -m "feat: add starter README template for new topics"
```

---

### Task 7: Create GitHub Project board script

**Files:**
- Create: `scripts/create_project_board.sh`

- [ ] **Step 1: Create `scripts/create_project_board.sh`**

```bash
#!/usr/bin/env bash
# Creates a GitHub Project (v2) board for a research topic.
# Usage: ./scripts/create_project_board.sh <topic-slug> "<topic-name>"
# Outputs: project number to stdout

set -euo pipefail

if [ $# -lt 2 ]; then
    echo "Usage: $0 <topic-slug> \"<topic-name>\"" >&2
    exit 1
fi

TOPIC_SLUG="$1"
TOPIC_NAME="$2"

# Detect repo owner
REPO_OWNER=$(gh repo view --json owner -q '.owner.login' 2>/dev/null)
if [ -z "$REPO_OWNER" ]; then
    echo "Error: could not determine repo owner. Is gh CLI authenticated?" >&2
    exit 1
fi

echo "Creating project board: Research: ${TOPIC_NAME}..." >&2

# Create the project
PROJECT_NUMBER=$(gh project create \
    --owner "$REPO_OWNER" \
    --title "Research: ${TOPIC_NAME}" \
    --format json | python3 -c "import sys,json; print(json.load(sys.stdin)['number'])")

echo "Created project #${PROJECT_NUMBER}" >&2

# The default Status field already exists. Add custom options to it.
# Get the Status field ID
FIELD_ID=$(gh project field-list "$PROJECT_NUMBER" \
    --owner "$REPO_OWNER" \
    --format json | python3 -c "
import sys, json
fields = json.load(sys.stdin).get('fields', [])
for f in fields:
    if f.get('name') == 'Status':
        print(f['id'])
        break
")

if [ -n "$FIELD_ID" ]; then
    echo "Configuring Status field options..." >&2
    # Delete default options and add custom ones via GraphQL
    for OPTION in "Scouted" "Under Review" "Accepted"; do
        gh api graphql -f query='
          mutation($projectId: ID!, $fieldId: ID!, $option: String!) {
            updateProjectV2Field(input: {
              projectId: $projectId
              fieldId: $fieldId
              singleSelectOptions: [{name: $option, color: GRAY}]
            }) {
              projectV2Field { ... on ProjectV2SingleSelectField { id } }
            }
          }
        ' -f projectId="$(gh project view "$PROJECT_NUMBER" --owner "$REPO_OWNER" --format json | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")" \
          -f fieldId="$FIELD_ID" \
          -f option="$OPTION" 2>/dev/null || echo "  Warning: could not add option '$OPTION' — configure manually" >&2
    done
    echo "Note: verify board columns at https://github.com/orgs/$REPO_OWNER/projects/$PROJECT_NUMBER" >&2
fi

# Output the project number
echo "$PROJECT_NUMBER"
```

- [ ] **Step 2: Make it executable**

```bash
chmod +x scripts/create_project_board.sh
```

- [ ] **Step 3: Commit**

```bash
git add scripts/create_project_board.sh
git commit -m "feat: add GitHub Project board creation script"
```

---

### Task 8: Create `add-topic.sh` CLI

**Files:**
- Create: `add-topic.sh`

- [ ] **Step 1: Create `add-topic.sh`**

```bash
#!/usr/bin/env bash
# Smart topic CLI — scaffolds a new research topic with Claude-powered deduplication.
# Usage: ./add-topic.sh "Topic Name"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ $# -lt 1 ]; then
    echo "Usage: $0 \"Topic Name\""
    echo "Example: $0 \"Autonomous Robotics\""
    exit 1
fi

TOPIC_NAME="$1"

# Check dependencies
command -v python3 >/dev/null 2>&1 || { echo "Error: python3 required" >&2; exit 1; }
command -v gh >/dev/null 2>&1 || { echo "Error: gh CLI required" >&2; exit 1; }

if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
    echo "Error: ANTHROPIC_API_KEY environment variable not set" >&2
    exit 1
fi

# Run the Python scaffolding logic
python3 "${SCRIPT_DIR}/scripts/add_topic_impl.py" "$TOPIC_NAME"
```

- [ ] **Step 2: Create `scripts/add_topic_impl.py`**

```python
#!/usr/bin/env python3
"""Implementation of the add-topic CLI — Claude-powered topic scaffolding with deduplication."""

import json
import os
import re
import subprocess
import sys

import anthropic
import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.topic_config import (
    REPO_ROOT,
    TOPICS_FILE,
    load_topics,
    save_topics,
    slugify,
    suggestions_dir,
    topic_dir,
)


def check_overlap(topic_name, existing_topics):
    """Use Claude to check if the new topic overlaps with existing topics."""
    if not existing_topics:
        return None

    existing_descriptions = "\n".join(
        f"- {t['name']}: {t['description']}" for t in existing_topics
    )

    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=1024,
        temperature=0.1,
        messages=[{
            "role": "user",
            "content": (
                f"I want to create a new research topic called \"{topic_name}\".\n\n"
                f"Existing topics:\n{existing_descriptions}\n\n"
                "Is this new topic substantially overlapping with any existing topic? "
                "Return JSON:\n"
                '```json\n'
                '{"overlaps": true/false, "overlapping_topic": "name or null", '
                '"explanation": "brief reason"}\n'
                '```'
            ),
        }],
    )

    text = response.content[0].text
    match = re.search(r"```(?:json)?\s*\n(.*?)\n```", text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    return json.loads(text)


def generate_topic_config(topic_name, scoping_instruction=""):
    """Use Claude to generate topic configuration fields."""
    client = anthropic.Anthropic()
    prompt = (
        f"Generate configuration for a research curation topic called \"{topic_name}\".\n"
    )
    if scoping_instruction:
        prompt += f"\nScoping instruction: {scoping_instruction}\n"
    prompt += (
        "\nReturn JSON with these fields:\n"
        '```json\n'
        '{\n'
        '  "description": "One-sentence description of the topic scope",\n'
        '  "grok_keywords": "comma-separated search keywords for social signal scouting",\n'
        '  "arxiv_feeds": [{"name": "cs.XX", "url": "https://rss.arxiv.org/rss/cs.XX"}],\n'
        '  "inclusion_criteria": {\n'
        '    "min_match": 3,\n'
        '    "checklist": ["criterion 1", "criterion 2", "criterion 3", "criterion 4"]\n'
        '  },\n'
        '  "exclude": ["exclusion rule 1", "exclusion rule 2"]\n'
        '}\n'
        '```\n'
        "Use real arXiv category codes. Be specific with criteria."
    )

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text
    match = re.search(r"```(?:json)?\s*\n(.*?)\n```", text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    return json.loads(text)


def scaffold_topic(slug, name, config):
    """Create the topic folder, README, config entry, project board, and suggestion dir."""
    # Create topic directory
    t_dir = topic_dir(slug)
    os.makedirs(t_dir, exist_ok=True)

    # Load and fill the README template
    template_path = os.path.join(REPO_ROOT, "scripts", "templates", "topic-readme.md")
    with open(template_path, encoding="utf-8") as f:
        template = f.read()

    checklist_text = "\n".join(f"- {c}" for c in config["inclusion_criteria"]["checklist"])
    exclude_text = "\n".join(f"- {e}" for e in config["exclude"])

    readme_content = template.replace("{name}", name)
    readme_content = readme_content.replace("{description}", config["description"])
    readme_content = readme_content.replace("{scope}", config["description"])
    readme_content = readme_content.replace("{min_match}", str(config["inclusion_criteria"]["min_match"]))
    readme_content = readme_content.replace("{num_criteria}", str(len(config["inclusion_criteria"]["checklist"])))
    readme_content = readme_content.replace("{checklist}", checklist_text)
    readme_content = readme_content.replace("{exclude}", exclude_text)

    readme_path = os.path.join(t_dir, "README.md")
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(readme_content)
    print(f"Created {readme_path}")

    # Create suggestion log directory
    s_dir = suggestions_dir(slug)
    os.makedirs(s_dir, exist_ok=True)
    print(f"Created {s_dir}")

    # Create GitHub Project board
    project_number = None
    try:
        board_script = os.path.join(REPO_ROOT, "scripts", "create_project_board.sh")
        result = subprocess.run(
            [board_script, slug, name],
            capture_output=True, text=True, check=True,
        )
        project_number = int(result.stdout.strip())
        print(f"Created GitHub Project board #{project_number}")
    except (subprocess.CalledProcessError, ValueError) as e:
        print(f"Warning: could not create project board: {e}", file=sys.stderr)
        print("You can create it manually later.", file=sys.stderr)

    # Add entry to topics.yml
    topics = load_topics()
    new_entry = {
        "id": slug,
        "name": name,
        "description": config["description"],
        "grok_keywords": config["grok_keywords"],
        "arxiv_feeds": config["arxiv_feeds"],
        "inclusion_criteria": config["inclusion_criteria"],
        "exclude": config["exclude"],
        "github_project": project_number,
    }
    topics.append(new_entry)
    save_topics(topics)
    print(f"Added '{name}' to topics.yml")

    # Update root README index
    root_readme_path = os.path.join(REPO_ROOT, "README.md")
    with open(root_readme_path, encoding="utf-8") as f:
        root_content = f.read()

    # Insert new row before the table ends (before ## Adding a Topic)
    new_row = f"| [{name}](topics/{slug}/) | {config['description']} |"
    # Find the last table row before "## Adding"
    lines = root_content.split("\n")
    insert_idx = None
    for i, line in enumerate(lines):
        if line.startswith("## Adding"):
            insert_idx = i
            break
    if insert_idx:
        # Find last table row before this heading
        for j in range(insert_idx - 1, -1, -1):
            if lines[j].startswith("|") and "---" not in lines[j]:
                lines.insert(j + 1, new_row)
                break
        with open(root_readme_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print("Updated root README.md index")


def main():
    topic_name = sys.argv[1]
    slug = slugify(topic_name)
    existing = load_topics()

    # Check if slug already exists
    for t in existing:
        if t["id"] == slug:
            print(f"Error: topic '{slug}' already exists in topics.yml")
            sys.exit(1)

    # Check for overlap with existing topics
    if existing:
        print(f"Checking for overlap with {len(existing)} existing topic(s)...")
        overlap = check_overlap(topic_name, existing)

        if overlap and overlap.get("overlaps"):
            overlapping = overlap.get("overlapping_topic", "an existing topic")
            explanation = overlap.get("explanation", "")
            print(f"\nThis looks related to \"{overlapping}\".")
            if explanation:
                print(f"Reason: {explanation}")
            print()
            print("What would you like to do?")
            print("  1) Modify the existing topic to also cover this area")
            print("  2) Create a new topic for ONLY the parts not covered by existing topics")
            print("  3) Create a new standalone topic covering everything relevant")
            print("  4) Cancel")
            print()

            choice = input("Choice [1-4]: ").strip()

            if choice == "1":
                # Update existing topic — regenerate config with expanded scope
                print("Updating existing topic config...")
                config = generate_topic_config(
                    f"{overlapping} expanded to include {topic_name}",
                )
                for t in existing:
                    if t["name"] == overlapping:
                        t["grok_keywords"] = config["grok_keywords"]
                        t["arxiv_feeds"] = config["arxiv_feeds"]
                        t["inclusion_criteria"] = config["inclusion_criteria"]
                        t["exclude"] = config["exclude"]
                        t["description"] = config["description"]
                        break
                save_topics(existing)
                print(f"Updated '{overlapping}' in topics.yml")
                return
            elif choice == "2":
                scoping = f"ONLY cover aspects of {topic_name} that are NOT covered by: {overlapping} ({explanation})"
                print("Generating scoped topic config...")
                config = generate_topic_config(topic_name, scoping_instruction=scoping)
                scaffold_topic(slug, topic_name, config)
                return
            elif choice == "3":
                print("Generating standalone topic config...")
                config = generate_topic_config(topic_name)
                scaffold_topic(slug, topic_name, config)
                return
            else:
                print("Cancelled.")
                return

    # No overlap — proceed directly
    print("No overlap detected. Generating topic config...")
    config = generate_topic_config(topic_name)
    scaffold_topic(slug, topic_name, config)
    print(f"\nDone! Topic '{topic_name}' scaffolded at topics/{slug}/")
    print("Review and edit topics.yml if needed.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Make `add-topic.sh` executable**

```bash
chmod +x add-topic.sh
```

- [ ] **Step 4: Verify CLI parses args**

Run: `cd C:/Users/taoga/projects/interest-topic-research && bash add-topic.sh`
Expected: Shows usage message

- [ ] **Step 5: Commit**

```bash
git add add-topic.sh scripts/add_topic_impl.py
git commit -m "feat: add smart topic CLI with Claude deduplication"
```

---

### Task 9: Create workflow orchestrator and rewrite GitHub Actions workflow

**Files:**
- Create: `scripts/run_all_topics.py`
- Rewrite: `.github/workflows/weekly-resource-research.yml`

- [ ] **Step 1: Create `scripts/run_all_topics.py`**

```python
#!/usr/bin/env python3
"""Workflow orchestrator — iterates all topics, runs scouts + curation, creates PRs/issues."""

import datetime as dt
import os
import shutil
import subprocess
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from scripts.topic_config import REPO_ROOT


def run_cmd(args, check=True, capture=False):
    """Run a subprocess command with logging."""
    print(f"  $ {' '.join(args)}")
    if capture:
        return subprocess.run(args, capture_output=True, text=True, check=check, cwd=REPO_ROOT)
    return subprocess.run(args, check=check, cwd=REPO_ROOT)


def clean_topic_temp_files(topic_id):
    """Remove temporary scout signal files for a topic."""
    t_dir = os.path.join(REPO_ROOT, "topics", topic_id)
    for fname in ("grok-signals.md", "arxiv-signals.md", "weekly-suggestions.md"):
        path = os.path.join(t_dir, fname)
        if os.path.exists(path):
            os.remove(path)


def reset_to_main():
    """Ensure we're on main with a clean working tree."""
    subprocess.run(["git", "checkout", "main"], check=False, cwd=REPO_ROOT)
    subprocess.run(["git", "checkout", "--", "."], check=False, cwd=REPO_ROOT)
    subprocess.run(["git", "clean", "-fd", "topics/"], check=False, cwd=REPO_ROOT)


def process_topic(topic, run_id, date_str):
    """Process a single topic: scout, curate, create PR or issue."""
    topic_id = topic["id"]
    topic_name = topic["name"]
    topic_dir = os.path.join("topics", topic_id)
    suggestions_dir = os.path.join(".github", "research-suggestions", topic_id)

    # Step 1: Grok scout
    print(f"[{topic_id}] Running Grok scout...")
    run_cmd(["python3", "scripts/grok_scout.py", "--topic-id", topic_id])

    # Step 2: arXiv scout
    print(f"[{topic_id}] Running arXiv scout...")
    run_cmd(["python3", "scripts/arxiv_scout.py", "--topic-id", topic_id])

    # Step 3: Claude curation
    print(f"[{topic_id}] Running Claude curation...")
    result = run_cmd(
        ["python3", "scripts/claude_curate.py", "--topic-id", topic_id],
        capture=True,
    )
    print(result.stdout)

    # Parse decision
    decision = "NONE"
    for line in result.stdout.splitlines():
        if line.startswith("RESULT:"):
            decision = line.split(":", 1)[1].strip()
            break

    os.makedirs(os.path.join(REPO_ROOT, suggestions_dir), exist_ok=True)

    if decision == "FOUND":
        # Copy suggestion log before creating branch
        suggestions_src = os.path.join(REPO_ROOT, topic_dir, "weekly-suggestions.md")
        suggestions_dst = os.path.join(REPO_ROOT, suggestions_dir, f"{date_str}.md")
        if os.path.exists(suggestions_src):
            with open(suggestions_src) as sf:
                content = sf.read()
            log_content = "\n".join(content.splitlines()[1:])
            with open(suggestions_dst, "w") as df:
                df.write(log_content)

        # Create branch from main, add only the needed files
        branch = f"automation/weekly-{topic_id}-{run_id}"
        run_cmd(["git", "checkout", "-b", branch])
        run_cmd(["git", "add", f"{topic_dir}/README.md", suggestions_dst])
        run_cmd([
            "git", "commit", "-m",
            f"chore: weekly resource suggestions for {topic_id} ({date_str})",
        ])
        run_cmd(["git", "push", "-u", "origin", branch])

        run_cmd([
            "gh", "pr", "create",
            "--title", f"chore: weekly resource suggestions for {topic_id} ({date_str})",
            "--body", (
                f"This draft PR was generated by the Research Assistant Agent for **{topic_name}**.\n\n"
                f"Review the suggestion log at `.github/research-suggestions/{topic_id}/{date_str}.md`."
            ),
            "--draft",
            "--label", "automation,research",
        ])

        # Return to main and reset working tree for next topic
        reset_to_main()

    else:
        # Create issue with scout outputs
        grok_path = os.path.join(REPO_ROOT, topic_dir, "grok-signals.md")
        arxiv_path = os.path.join(REPO_ROOT, topic_dir, "arxiv-signals.md")
        suggestions_path = os.path.join(REPO_ROOT, topic_dir, "weekly-suggestions.md")

        body_parts = [f"# Weekly research log ({topic_name}) — {date_str}\n"]
        body_parts.append("No high-confidence additions this week.\n")

        for label, path in [
            ("Claude decision", suggestions_path),
            ("Grok scout output", grok_path),
            ("arXiv scout output", arxiv_path),
        ]:
            body_parts.append(f"\n## {label}\n")
            if os.path.exists(path):
                with open(path) as pf:
                    body_parts.append(pf.read())
            else:
                body_parts.append("(not available)")

        issue_body = "\n".join(body_parts)
        run_cmd([
            "gh", "issue", "create",
            "--title", f"research assistant log ({topic_id}) (no PR) ({date_str})",
            "--body", issue_body,
            "--label", "automation,research,no-pr",
        ])

    # Clean up temp files
    clean_topic_temp_files(topic_id)

    return decision


def main():
    with open(os.path.join(REPO_ROOT, "topics.yml"), encoding="utf-8") as f:
        topics = yaml.safe_load(f).get("topics", [])

    if not topics:
        print("No topics configured in topics.yml")
        sys.exit(0)

    run_id = os.environ.get("GITHUB_RUN_ID", "local")
    date_str = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    errors = []

    for topic in topics:
        topic_id = topic["id"]
        topic_name = topic["name"]
        print(f"\n{'='*60}")
        print(f"Processing topic: {topic_name} ({topic_id})")
        print(f"{'='*60}\n")

        try:
            decision = process_topic(topic, run_id, date_str)
            print(f"[{topic_id}] Done: RESULT: {decision}")
        except Exception as exc:
            errors.append((topic_id, str(exc)))
            print(f"[{topic_id}] ERROR: {exc}", file=sys.stderr)
            reset_to_main()
            clean_topic_temp_files(topic_id)
            continue

    # Summary
    print(f"\n{'='*60}")
    print(f"Processed {len(topics)} topic(s)")
    if errors:
        print(f"Errors in {len(errors)} topic(s):")
        for tid, err in errors:
            print(f"  - {tid}: {err}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Verify orchestrator loads**

Run: `cd C:/Users/taoga/projects/interest-topic-research && python scripts/run_all_topics.py --help 2>&1 || true`
Expected: Runs without import errors (may print "No topics configured" if topics.yml path differs)

- [ ] **Step 3: Rewrite the workflow YAML**

```yaml
name: Research Assistant Agent

on:
  workflow_dispatch:
  schedule:
    - cron: "0 14 * * 1"

permissions:
  contents: write
  pull-requests: write
  issues: write
  projects: write

jobs:
  scout:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install Python dependencies
        run: pip install -r requirements.txt

      - name: Configure git identity
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"

      - name: Verify API keys
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          XAI_API_KEY: ${{ secrets.XAI_API_KEY }}
        run: |
          if [ -z "$ANTHROPIC_API_KEY" ]; then
            echo "Missing repository secret: ANTHROPIC_API_KEY"
            exit 1
          fi
          if [ -z "$XAI_API_KEY" ]; then
            echo "Missing repository secret: XAI_API_KEY"
            exit 1
          fi

      - name: Run research agent for all topics
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          XAI_API_KEY: ${{ secrets.XAI_API_KEY }}
          XAI_BASE_URL: ${{ vars.XAI_BASE_URL }}
          GROK_MODEL: ${{ vars.GROK_MODEL }}
          GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: python3 scripts/run_all_topics.py
```

- [ ] **Step 4: Verify YAML is valid**

Run: `cd C:/Users/taoga/projects/interest-topic-research && python -c "import yaml; yaml.safe_load(open('.github/workflows/weekly-resource-research.yml'))"`
Expected: No errors

- [ ] **Step 5: Commit**

```bash
git add scripts/run_all_topics.py .github/workflows/weekly-resource-research.yml
git commit -m "feat: rewrite workflow with standalone orchestrator for multi-topic iteration"
```

---

### Task 10: Add .gitignore for temp signal files

**Files:**
- Create: `topics/.gitignore`

- [ ] **Step 1: Create `.gitignore` for temp files**

Create `topics/.gitignore`:
```
# Temporary scout signal files (not committed)
*/grok-signals.md
*/arxiv-signals.md
*/weekly-suggestions.md
```

- [ ] **Step 2: Commit**

```bash
git add topics/.gitignore
git commit -m "chore: gitignore temporary scout signal files"
```

---

### Task 11: Final integration verification

- [ ] **Step 1: Verify full repo structure**

```bash
cd C:/Users/taoga/projects/interest-topic-research && find . -not -path './.git/*' -type f | sort
```

Expected to see:
```
./add-topic.sh
./.github/workflows/weekly-resource-research.yml
./README.md
./requirements.txt
./scripts/__init__.py
./scripts/add_topic_impl.py
./scripts/arxiv_scout.py
./scripts/claude_curate.py
./scripts/create_project_board.sh
./scripts/grok_scout.py
./scripts/templates/topic-readme.md
./scripts/topic_config.py
./topics/agentic-ml/README.md
./topics/.gitignore
./topics.yml
```

- [ ] **Step 2: Verify all Python scripts import cleanly**

```bash
cd C:/Users/taoga/projects/interest-topic-research
python -c "from scripts.topic_config import load_topics, slugify; assert slugify('Autonomous Robotics') == 'autonomous-robotics'; print('OK')"
python scripts/grok_scout.py --help
python scripts/arxiv_scout.py --help
python scripts/claude_curate.py --help
```

- [ ] **Step 3: Verify topics.yml loads the agentic-ml entry**

```bash
cd C:/Users/taoga/projects/interest-topic-research
python -c "from scripts.topic_config import find_topic; t = find_topic('agentic-ml'); print(f'{t[\"name\"]}: {len(t[\"arxiv_feeds\"])} feeds, {len(t[\"inclusion_criteria\"][\"checklist\"])} criteria')"
```
Expected: `Awesome Agentic ML: 3 feeds, 4 criteria`

- [ ] **Step 4: Verify add-topic.sh shows usage**

```bash
cd C:/Users/taoga/projects/interest-topic-research && bash add-topic.sh
```
Expected: Shows usage message with example

- [ ] **Step 5: Final commit with any fixes**

If any fixes were needed, commit them. Otherwise skip.
