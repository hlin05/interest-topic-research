# Awesome Agentic Workflow Design [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Agentic workflow design and practices covers architectural patterns, design principles, and engineering practices for building reliable, production-grade agentic systems—from single-agent pipelines to multi-agent orchestration.

🤖 *This resource list is maintained with the help of [Claude](https://www.anthropic.com/claude) by Anthropic.*

---

## Scope: What Counts as Agentic Workflow Design?

A resource belongs in this list when it addresses the design, architecture, or engineering practices for agentic systems in a substantive, principled way.

**Inclusion checklist (meet at least 3 of 4):**

- Architectural guidance for goal-directed agent systems (patterns, orchestration, state management)
- Tool-use and execution design across agent lifecycle stages (planning, execution, feedback, recovery)
- Iterative refinement practices (evaluation loops, human-in-the-loop, observability)
- Empirical or practical grounding (case studies, benchmarks, production deployment evidence)

**Exclude or deprioritize:**

- Generic LLM tutorials without agentic design focus
- Social-only announcements without a primary technical source (paper/repo/blog)
- Stale resources unless there is a substantive new release/update in the recent window

---

## Research Assistant Agent

This repository runs a weekly **Research Assistant Agent** via GitHub Actions to scout and triage potential additions.

- Workflow: `.github/workflows/weekly-resource-research.yml`
- Primary curation model: `gpt-5.3-codex` with `xhigh` effort
- Default Grok scout model: `grok-4-1-fast-reasoning` (override with `GROK_MODEL` repository variable)
- Signal sources: xAI Grok social scout + arXiv RSS scout + Codex curation pass

---

## Contents

- [Guides & References](#guides--references)
- [Research Papers](#research-papers)
- [Contributing](#contributing)

---

## Guides & References

*Canonical guides and reference material for agentic workflow design and practices.*

| Resource | Description |
|----------|-------------|
| [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents) | Anthropic's authoritative guide covering workflow patterns (prompt chaining, routing, parallelization, orchestrator-subagent, evaluator-optimizer), agent design principles, and production safety practices. |
| [A Practical Guide for Designing, Developing, and Deploying Production-Grade Agentic AI Workflows](https://arxiv.org/abs/2512.08769) | Comprehensive arXiv paper covering tool-first design, single-responsibility agents, externalized prompt management, integration testing, and human-in-the-loop patterns for production agentic systems. |

---

## Research Papers

*Coming soon — populated by the weekly Research Assistant Agent.*


- [HyEvo: Self-Evolving Hybrid Agentic Workflows for Efficient Reasoning](https://arxiv.org/abs/2603.19639) — Proposes a self-evolving hybrid agentic workflow architecture that dynamically adapts workflow structure for efficient reasoning, with empirical evaluation across benchmarks.

- [Utility-Guided Agent Orchestration for Efficient LLM Tool Use](https://arxiv.org/abs/2603.19896) — Introduces a utility-guided orchestration framework for selecting and sequencing LLM tool use efficiently, with empirical benchmarking across agentic task settings.
---

## Contributing

See the root [README](../../README.md) for how to add a topic. For individual entries, open a PR with the resource and a note on which inclusion criteria it meets.
