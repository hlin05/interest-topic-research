# CLAUDE.md

## Project Overview

**Awesome Agentic ML** — a curated resource list documenting autonomous AI systems for ML workflows. This is a documentation-only repo; there is no application source code to build or run.

## How This Repo Works

- `README.md` is the main deliverable — a curated index of frameworks, agents, papers, datasets, and benchmarks.
- `.github/workflows/weekly-resource-research.yml` runs every Monday at 14:00 UTC, using Grok (xAI) for social signals and arXiv RSS for academic papers, then Claude/Codex for curation decisions.
- High-signal weeks: workflow updates README.md and opens a draft PR.
- Low-signal weeks: workflow opens an issue with scout outputs.

## Inclusion Criteria

A resource must satisfy **at least 3 of 4**:
1. Goal-directed ML planning
2. Tool-using execution across ML lifecycle (data prep, training, evaluation)
3. Iterative feedback loop (metrics/errors/results)
4. Empirical ML outcome (benchmark, competition result, ablation)

Exclude: generic coding agents without ML contribution, social-only announcements, stale resources.

## Required Secrets & Variables

- `XAI_API_KEY` — GitHub repository secret
- `XAI_BASE_URL` — repository variable (default: https://api.x.ai)
- `GROK_MODEL` — repository variable (default: grok-4-1-fast-reasoning)

## Editing Guidelines

- Keep README.md sections in order: Frameworks, AutoML Agents, Research Papers, Datasets/Benchmarks, MLE-bench Leaderboard, Contributing.
- Each entry needs: name, link, and 1-line description.
- Do not add entries that fail the inclusion criteria above.
