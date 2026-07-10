# Design: LLM Alignment & Feedback Infrastructure Topic

**Date:** 2026-07-10
**Status:** Approved

---

## Summary

Add a new research topic, `llm-alignment-feedback-infra`, to the weekly automated research pipeline. The topic tracks the infrastructure for specifying desired LLM behavior (contracts, rubrics, model specs), evaluating against those specifications (LLM-as-judge, rubric scoring), and training toward them (RLAIF, Constitutional AI, scalable oversight).

---

## Scope & Differentiation

This topic is broader than the existing `rlhf-agentic` topic:

| | `rlhf-agentic` | `llm-alignment-feedback-infra` |
|---|---|---|
| Focus | RLHF applied in agentic (multi-step, tool-using) settings | General LLM training infra: spec → eval → feedback loop |
| RLAIF coverage | Only when used in agentic deployments | RLAIF as a base training mechanism |
| Rubrics | Only rubric-based reward shaping for agents | Rubrics as evaluation and training signal infrastructure |
| Contracts/model specs | Not covered | Core coverage: how desired behavior is formally specified |

---

## Topic Configuration

**ID:** `llm-alignment-feedback-infra`
**Name:** LLM Alignment & Feedback Infrastructure
**Description:** Infrastructure for specifying desired LLM behavior (contracts, rubrics, model specs), evaluating against those specifications (LLM-as-judge, rubric scoring), and training toward them (RLAIF, Constitutional AI, scalable oversight)

### Grok Keywords
```
RLAIF, LLM-as-judge, rubric-based training, model spec, Constitutional AI,
scalable oversight, AI feedback loop, preference data generation,
LLM alignment infrastructure, reward specification
```

### arXiv Feeds
- `cs.CL` — Computation and Language
- `cs.LG` — Machine Learning
- `cs.AI` — Artificial Intelligence

### Inclusion Criteria (meet at least 3 of 4)
1. Defines or implements a specification layer for desired LLM behavior (rubric, contract, model spec, constitution, system prompt as policy)
2. Uses AI-generated feedback signals for LLM training or evaluation (RLAIF, LLM-as-judge, AI critique/revision)
3. Iterative loop where specification + feedback jointly improve model outputs (not a one-shot annotation pass)
4. Empirical outcome (benchmark, eval score, alignment improvement, or measurable quality gain)

### Exclusions
- RLHF applied only in agentic/multi-step task settings (covered by `rlhf-agentic`)
- Human-only feedback pipelines without an AI-in-the-loop component
- Social-only announcements without a primary technical source (paper/repo/blog)
- Stale resources without a substantive new release or update

### Max entries per week: 3

---

## Implementation

Two files need to be created or modified:

1. **`topics.yml`** — append the new topic entry under the existing `topics` list
2. **`topics/llm-alignment-feedback-infra/README.md`** — create from the template at `scripts/templates/topic-readme.md`, populated with the topic's scope, inclusion criteria, and initial sections

No changes to the GitHub Actions workflow are required; the weekly research pipeline reads `topics.yml` dynamically via `scripts/topic_config.py`.

### README Initial Sections
- Specification Frameworks (contracts, model specs, constitutions)
- Rubric-Based Evaluation & Training
- RLAIF & AI Feedback Pipelines
- Scalable Oversight Methods
- Research Papers
- Datasets & Benchmarks
- Contributing
