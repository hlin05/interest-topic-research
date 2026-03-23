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
