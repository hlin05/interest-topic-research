# Multi-Topic Research Agent System — Design Spec

**Date:** 2026-03-22
**Status:** Approved

## Overview

Redesign the single-topic "Awesome Agentic ML" repository into a flexible, multi-topic research agent system. Each topic gets its own folder, curated README, GitHub Project board, and scout configuration. A CLI scaffolds new topics with smart deduplication. The OpenAI Codex curation model is replaced by Anthropic Claude Opus 4.6.

## Repository Structure

```
topics.yml                          # Central registry of all topics
add-topic.sh                        # CLI to scaffold a new topic
requirements.txt                    # Python dependencies (anthropic SDK)
scripts/
  grok-scout.py                     # Grok social signal collector (topic-aware)
  arxiv-scout.py                    # arXiv RSS collector (per-topic feeds)
  claude-curate.py                  # Anthropic Claude curation pass
  create-project-board.sh           # Creates GitHub Project board for a topic
  templates/
    topic-readme.md                 # Starter README template for new topics
topics/
  agentic-ml/                       # Migrated from current root README
    README.md                       # The curated awesome list
  <future-topic>/
    README.md
.github/
  workflows/
    weekly-resource-research.yml    # Single workflow, iterates all topics
  research-suggestions/
    agentic-ml/                     # Per-topic suggestion logs
      <date>.md
```

The root `README.md` becomes a lightweight index pointing to each topic folder. The `add-topic.sh` script updates the root index automatically when a new topic is created.

## `topics.yml` Schema

```yaml
topics:
  - id: agentic-ml                  # Auto-generated slug from name
    name: "Awesome Agentic ML"
    description: "Autonomous AI systems for ML workflows"
    grok_keywords: >-
      agentic ML, AutoML agents, autonomous machine learning,
      LLM ML engineering
    arxiv_feeds:
      - { name: "cs.AI", url: "https://rss.arxiv.org/rss/cs.AI" }
      - { name: "cs.LG", url: "https://rss.arxiv.org/rss/cs.LG" }
      - { name: "stat.ML", url: "https://rss.arxiv.org/rss/stat.ML" }
    inclusion_criteria:
      min_match: 3
      checklist:
        - "Goal-directed ML planning"
        - "Tool-using ML lifecycle execution"
        - "Iterative feedback loop from metrics/errors/results"
        - "Empirical ML outcome (benchmark/ablation/competition)"
    exclude:
      - "Generic web/desktop/coding agents without ML workflow contribution"
      - "Social-only announcements lacking a primary technical source"
      - "Stale resources unless substantive recent release/update"
    github_project: null            # Populated by add-topic.sh after board creation
```

## `add-topic.sh` — Smart Topic CLI

Takes only a natural language topic name:

```bash
./add-topic.sh "Autonomous Robotics"
```

### Flow

1. **Auto-generates a slug** from the name (e.g., `autonomous-robotics`). The user never sees or manages IDs.
2. **Compares against existing topics** in `topics.yml` using Claude (Anthropic API). Sends the new topic name + all existing topic descriptions and asks whether there is substantial overlap.
3. **If overlap detected**, presents an interactive prompt:
   ```
   This looks related to "Awesome Agentic ML".

   What would you like to do?
     1) Modify the existing topic to also cover this area
     2) Create a new topic for ONLY the parts not covered by existing topics
     3) Create a new standalone topic covering everything relevant
     4) Cancel
   ```
   - **Option 1:** Updates existing topic's keywords, feeds, and criteria in `topics.yml`.
   - **Option 2:** Claude generates scoped description and exclusion rules that carve out what the existing topic already covers.
   - **Option 3:** Creates topic with full scope, accepting some overlap.
4. **If no overlap**, proceeds directly to scaffold:
   - Creates `topics/<slug>/README.md` from `scripts/templates/topic-readme.md`
   - Appends entry to `topics.yml` — Claude generates `grok_keywords`, `arxiv_feeds`, `inclusion_criteria`, and `exclude` fields based on the topic name and description
   - Calls `scripts/create-project-board.sh <slug> <name>` to create the GitHub Project board
   - Creates `.github/research-suggestions/<slug>/` directory
   - Updates root `README.md` index with a link to the new topic

### Claude-Generated Topic Config

When scaffolding, Claude generates the following fields:
- `grok_keywords`: Search terms tailored to the topic
- `arxiv_feeds`: Relevant arXiv category RSS feeds (from the known set of arXiv categories)
- `inclusion_criteria.checklist`: 3-5 domain-specific criteria
- `inclusion_criteria.min_match`: Defaults to 3 unless Claude recommends otherwise
- `exclude`: Domain-specific exclusion rules

The user can review and edit `topics.yml` after scaffolding.

### Requirements

- `gh` CLI authenticated
- `ANTHROPIC_API_KEY` environment variable set
- Python 3.10+ with `anthropic` package installed

## `scripts/create-project-board.sh`

Creates and configures a GitHub Project (v2) board for a topic.

**Interface:**
```bash
./scripts/create-project-board.sh <topic-slug> "<topic-name>"
# Outputs the project number to stdout
```

**Steps:**
1. Creates board via `gh project create --owner <repo-owner> --title "Research: <topic-name>"`
2. Adds three status columns: **Scouted**, **Under Review**, **Accepted** via `gh project field-create` and option configuration
3. Prints the project number to stdout (captured by `add-topic.sh` to write into `topics.yml`)

## Script Interface Contract

All scripts accept `--topic-id <id>` as their primary argument and read `topics.yml` directly to extract their own configuration.

### `scripts/grok-scout.py`

```bash
python3 scripts/grok-scout.py --topic-id agentic-ml
```
- Reads `grok_keywords` and `description` from `topics.yml` for the given topic
- Writes output to `topics/<id>/grok-signals.md` (temporary, not committed)
- Requires `XAI_API_KEY` environment variable

### `scripts/arxiv-scout.py`

```bash
python3 scripts/arxiv-scout.py --topic-id agentic-ml
```
- Reads `arxiv_feeds` from `topics.yml` for the given topic
- Writes output to `topics/<id>/arxiv-signals.md` (temporary, not committed)
- Uses only Python stdlib (no external dependencies)

### `scripts/claude-curate.py`

```bash
python3 scripts/claude-curate.py --topic-id agentic-ml
```
- Reads from `topics.yml`: `inclusion_criteria`, `exclude`, `name`, `description`
- Reads: `topics/<id>/README.md`, `topics/<id>/grok-signals.md`, `topics/<id>/arxiv-signals.md`
- Calls Anthropic Messages API with `claude-opus-4-6`, temperature 0.2
- Requires `ANTHROPIC_API_KEY` environment variable
- Outputs `RESULT: FOUND` or `RESULT: NONE` as first line of stdout
- Writes `topics/<id>/weekly-suggestions.md`
- If FOUND, updates `topics/<id>/README.md` directly

### Claude Curation Output Format

Claude is instructed to return JSON within a code fence:

```json
{
  "result": "FOUND",
  "summary": "Brief scan summary",
  "suggestions": [
    {
      "title": "Project Name",
      "url": "https://...",
      "section": "Frameworks & Platforms",
      "description": "One-line description",
      "criteria_met": ["criterion 1", "criterion 3", "criterion 4"]
    }
  ]
}
```

The script parses this JSON, validates each suggestion (URL accessible, not already in README), and inserts entries into the correct sections of the topic's `README.md`.

## Workflow Design

Single workflow: `.github/workflows/weekly-resource-research.yml`

**Trigger:** Weekly cron (Monday 14:00 UTC) + `workflow_dispatch` for manual runs.

### Loop Mechanism

The workflow uses a single bash step that iterates over topics via Python parsing of `topics.yml`. Each topic is processed sequentially within one step. Errors for a single topic are caught and logged but do not abort the run — the loop continues to the next topic.

```
for each topic in topics.yml:
    try:
        run grok-scout.py --topic-id <id>
        run arxiv-scout.py --topic-id <id>
        run claude-curate.py --topic-id <id>
        if FOUND: create draft PR, update project board
        if NONE: create issue, update project board
    catch:
        log error, continue to next topic
```

### PR and Issue Strategy

- **One draft PR per topic** that has findings. Branch name: `automation/weekly-<topic-id>-<run-id>`.
- **One issue per topic** with no findings. Title: `research assistant log (<topic-id>) (no PR) (<date>)`.
- PRs include changes to `topics/<id>/README.md` and the suggestion log at `.github/research-suggestions/<id>/<date>.md`.

### Secrets

- `ANTHROPIC_API_KEY` (replaces `OPENAI_API_KEY` for curation)
- `XAI_API_KEY` (kept for Grok scout)

### Python Dependencies

The workflow includes a pip install step:
```yaml
- name: Install Python dependencies
  run: pip install -r requirements.txt
```

`requirements.txt` contains:
```
anthropic>=0.40.0
pyyaml>=6.0
```

## GitHub Project Board Integration

Each topic gets a GitHub Project (v2) board, created by `scripts/create-project-board.sh`.

### Board Columns

| Column | Purpose |
|--------|---------|
| **Scouted** | Raw candidates from weekly runs (auto-added) |
| **Under Review** | Items promoted from Scouted for human evaluation |
| **Accepted** | Items that made it into the topic's README |

### Card Management

- After each weekly run, candidates are added to **Scouted** (regardless of confidence level).
- High-confidence items auto-added to README are placed directly in **Accepted** with a PR link.
- "No additions" weeks get a single summary card in **Scouted** noting the run happened.
- Cards managed via `gh project item-add` and `gh project item-edit`. Project number stored in `topics.yml` under `github_project`.

## Starter README Template

Located at `scripts/templates/topic-readme.md`. Contains:

```markdown
# {name} [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

{description}

---

## Scope

{Claude-generated scope description and inclusion checklist}

---

## Contents

- [Contributing](#contributing)

---

## Contributing

Contributions welcome! Open an issue or submit a PR.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)
```

Sections are populated as resources are added by the weekly curation.

## Migration Plan

All migration steps are performed in a single branch with a PR, so rollback is simply closing the PR.

1. **Extract inline scripts** — move the inline Grok scout Python (~170 lines) and arXiv scout Python (~70 lines) from the current workflow into `scripts/grok-scout.py` and `scripts/arxiv-scout.py`. Add `--topic-id` CLI argument parsing to each.
2. **Create `scripts/claude-curate.py`** — new script replacing the Codex action, using the Anthropic SDK.
3. **Create `scripts/create-project-board.sh`** — board creation and column setup script.
4. **Create `requirements.txt`** with `anthropic` and `pyyaml` dependencies.
5. **Move** `README.md` → `topics/agentic-ml/README.md` (via `git mv` to preserve history).
6. **Create root `README.md`** as a lightweight index linking to all topic folders.
7. **Move existing suggestion logs** from `.github/research-suggestions/` into `.github/research-suggestions/agentic-ml/` (skip if directory is absent or empty).
8. **Populate `topics.yml`** with the agentic-ml entry, extracting criteria from the current README's scope section.
9. **Create `add-topic.sh`** with the smart CLI flow.
10. **Create starter template** at `scripts/templates/topic-readme.md`.
11. **Rewrite workflow** `.github/workflows/weekly-resource-research.yml` to iterate `topics.yml` and call the standalone scripts.
12. **Create first GitHub Project board** for agentic-ml.
13. **Update secrets:** remove `OPENAI_API_KEY` dependency; document `ANTHROPIC_API_KEY` requirement.
