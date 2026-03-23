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
    pattern = r"```(?:json)?\s*\n(.*?)\s*```"
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

    # Look for the section heading
    section_pattern = re.compile(
        rf"^#{{2,3}}\s+.*{re.escape(section)}.*$",
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

    # Find the end of the section (next --- or ## heading)
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
        model="claude-opus-4-6",
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
        updated_readme = readme_content
        for s in suggestions:
            try:
                # Skip if already present — use anchored title check to avoid false positives
                if s.get("url", "") in updated_readme or f"[{s.get('title', '')}]" in updated_readme:
                    print(f"Skipping duplicate: {s.get('title', '?')}")
                    continue
                if not all(k in s for k in ("title", "url", "section", "description")):
                    print(f"Warning: skipping malformed suggestion (missing required fields): {s!r}", file=sys.stderr)
                    continue
                updated_readme = insert_suggestion_into_readme(updated_readme, s)
            except Exception as exc:
                print(f"Warning: could not insert suggestion '{s.get('title', '?')}': {exc}", file=sys.stderr)
                continue

        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(updated_readme)
        print(f"README updated at {readme_path}")


if __name__ == "__main__":
    main()
