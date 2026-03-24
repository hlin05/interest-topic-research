#!/usr/bin/env python3
"""Claude curation — evaluates scout signals and proposes README additions using Anthropic API."""

import argparse
import datetime as dt
import json
import os
import re
import sys
from collections import defaultdict

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
    pattern = r"```(?:json)?\s*\n(.*?)\s*```"
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    # Try parsing the whole response as JSON
    return json.loads(text)


def insert_dated_block_into_section(readme_content, section, date_str, suggestions):
    """Insert a dated block of suggestions at the top of a section (most recent first).

    Builds a ### YYYY-MM-DD sub-heading with list entries and inserts it before
    any previous dated blocks, so the newest week always appears first.
    """
    block_lines = [f"### {date_str}", ""]
    for s in suggestions:
        block_lines.append(f"- [{s['title']}]({s['url']}) — {s['description']}")
    block_lines.append("")
    block = "\n".join(block_lines) + "\n"

    # Find the section heading
    section_pattern = re.compile(
        rf"^#{{2,3}}\s+.*{re.escape(section)}.*$",
        re.MULTILINE | re.IGNORECASE,
    )
    match = section_pattern.search(readme_content)
    if not match:
        # Section not found — create it before Contributing
        contrib_match = re.search(r"^## Contributing", readme_content, re.MULTILINE)
        if contrib_match:
            new_section = f"\n---\n\n## {section}\n\n{block}"
            pos = contrib_match.start()
            return readme_content[:pos] + new_section + "\n" + readme_content[pos:]
        return readme_content + f"\n\n## {section}\n\n{block}"

    section_start = match.end()
    next_section = re.search(r"^---$|^## ", readme_content[section_start:], re.MULTILINE)
    section_end = section_start + next_section.start() if next_section else len(readme_content)
    section_text = readme_content[section_start:section_end]

    # Insert before the first existing dated sub-heading, or at the end of the section
    prev_dated = re.search(r"^### \d{4}-\d{2}-\d{2}", section_text, re.MULTILINE)
    if prev_dated:
        insert_at = section_start + prev_dated.start()
    else:
        insert_at = section_end

    return readme_content[:insert_at] + block + "\n" + readme_content[insert_at:]


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
    max_entries = topic.get("max_entries_per_week", 5)

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
        f"Propose at most {max_entries} suggestion(s) per run — rank by signal strength and stop there.\n"
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
        model="claude-sonnet-4-6",
        max_tokens=4096,
        temperature=0.2,
        system=system_prompt,
        messages=[{"role": "user", "content": user_message}],
    )

    if not response.content:
        print("Error: Anthropic API returned empty content", file=sys.stderr)
        sys.exit(1)
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

    # Output the result line for the workflow to parse (MUST be first stdout line)
    print(f"RESULT: {decision}")
    if summary:
        print(summary)

    # If FOUND, update the README (cap at max_entries as a hard guard)
    suggestions = suggestions[:max_entries]
    if decision == "FOUND" and suggestions:
        date_str = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
        updated_readme = readme_content

        # Group suggestions by section, filtering duplicates
        by_section = defaultdict(list)
        for s in suggestions:
            if s.get("url", "") in updated_readme or f"[{s.get('title', '')}]" in updated_readme:
                print(f"Skipping duplicate: {s.get('title', '?')}")
                continue
            if not all(k in s for k in ("title", "url", "section", "description")):
                print(f"Warning: skipping malformed suggestion (missing required fields): {s!r}", file=sys.stderr)
                continue
            by_section[s["section"]].append(s)

        for section_name, section_suggestions in by_section.items():
            try:
                updated_readme = insert_dated_block_into_section(
                    updated_readme, section_name, date_str, section_suggestions
                )
            except Exception as exc:
                print(f"Warning: could not insert suggestions for '{section_name}': {exc}", file=sys.stderr)

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_readme)
        print(f"README updated at {readme_path}")


if __name__ == "__main__":
    main()
