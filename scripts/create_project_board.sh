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
PROJECT_JSON=$(gh project create \
    --owner "$REPO_OWNER" \
    --title "Research: ${TOPIC_NAME}" \
    --format json)

PROJECT_NUMBER=$(echo "$PROJECT_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['number'])")
PROJECT_NODE_ID=$(echo "$PROJECT_JSON" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

echo "Created project #${PROJECT_NUMBER} (node ID: ${PROJECT_NODE_ID})" >&2

# Get the Status field ID via field-list
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
    echo "Configuring Status field options via GraphQL..." >&2
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
        ' -f projectId="$PROJECT_NODE_ID" \
          -f fieldId="$FIELD_ID" \
          -f option="$OPTION" 2>/dev/null \
          && echo "  Added option: $OPTION" >&2 \
          || echo "  Warning: could not add option '$OPTION' — configure manually at https://github.com/orgs/$REPO_OWNER/projects/$PROJECT_NUMBER" >&2
    done
else
    echo "Note: Status field not found — configure board columns manually at https://github.com/orgs/$REPO_OWNER/projects/$PROJECT_NUMBER" >&2
fi

# Output the project number (stdout only, for capture by caller)
echo "$PROJECT_NUMBER"
