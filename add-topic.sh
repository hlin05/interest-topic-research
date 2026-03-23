#!/usr/bin/env bash
# Smart topic CLI — scaffolds a new research topic with Claude-powered deduplication.
# Usage: ./add-topic.sh "Topic Name"

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ $# -lt 1 ]; then
    echo "Usage: $0 \"Topic Name\" [--max-entries N]"
    echo "Example: $0 \"Autonomous Robotics\" --max-entries 3"
    exit 1
fi

TOPIC_NAME="$1"
shift

MAX_ENTRIES_ARG=""
while [[ $# -gt 0 ]]; do
    case "$1" in
        --max-entries)
            MAX_ENTRIES_ARG="--max-entries $2"
            shift 2
            ;;
        *)
            echo "Unknown argument: $1" >&2
            exit 1
            ;;
    esac
done

# Check dependencies
command -v python3 >/dev/null 2>&1 || { echo "Error: python3 required" >&2; exit 1; }
command -v gh >/dev/null 2>&1 || { echo "Error: gh CLI required" >&2; exit 1; }

if [ -z "${ANTHROPIC_API_KEY:-}" ]; then
    echo "Error: ANTHROPIC_API_KEY environment variable not set" >&2
    exit 1
fi

# Run the Python scaffolding logic
python3 "${SCRIPT_DIR}/scripts/add_topic_impl.py" "$TOPIC_NAME" $MAX_ENTRIES_ARG
