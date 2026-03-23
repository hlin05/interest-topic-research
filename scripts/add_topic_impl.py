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
                "Return JSON in a code fence:\n"
                "```json\n"
                "{\"overlaps\": true/false, \"overlapping_topic\": \"name or null\", "
                "\"explanation\": \"brief reason\"}\n"
                "```"
            ),
        }],
    )

    text = response.content[0].text
    match = re.search(r"```(?:json)?\s*\n(.*?)\s*```", text, re.DOTALL)
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
        "\nReturn JSON in a code fence:\n"
        "```json\n"
        "{\n"
        "  \"description\": \"One-sentence description of the topic scope\",\n"
        "  \"grok_keywords\": \"comma-separated search keywords for social signal scouting\",\n"
        "  \"arxiv_feeds\": [{\"name\": \"cs.XX\", \"url\": \"https://rss.arxiv.org/rss/cs.XX\"}],\n"
        "  \"inclusion_criteria\": {\n"
        "    \"min_match\": 3,\n"
        "    \"checklist\": [\"criterion 1\", \"criterion 2\", \"criterion 3\", \"criterion 4\"]\n"
        "  },\n"
        "  \"exclude\": [\"exclusion rule 1\", \"exclusion rule 2\"]\n"
        "}\n"
        "```\n"
        "Use real arXiv category codes. Be specific with criteria."
    )

    response = client.messages.create(
        model="claude-opus-4-6",
        max_tokens=2048,
        temperature=0.2,
        messages=[{"role": "user", "content": prompt}],
    )

    text = response.content[0].text
    match = re.search(r"```(?:json)?\s*\n(.*?)\s*```", text, re.DOTALL)
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
    readme_content = readme_content.replace("{min_match}", str(config["inclusion_criteria"]["min_match"]))
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
            ["bash", board_script, slug, name],
            capture_output=True, text=True, check=True,
        )
        project_number_str = result.stdout.strip().splitlines()[-1]
        project_number = int(project_number_str)
        print(f"Created GitHub Project board #{project_number}")
    except (subprocess.CalledProcessError, ValueError, IndexError) as e:
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

    new_row = f"| [{name}](topics/{slug}/) | {config['description']} |"
    # Find the last table row in the Topics table and insert after it
    lines = root_content.split("\n")
    insert_idx = None
    for i, line in enumerate(lines):
        if line.startswith("## Adding"):
            insert_idx = i
            break
    if insert_idx:
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
