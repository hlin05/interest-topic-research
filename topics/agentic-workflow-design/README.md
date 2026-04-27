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

### 2026-04-27

- [Memanto: Typed Semantic Memory with Information-Theoretic Retrieval for Long-Horizon Agents](https://arxiv.org/abs/2604.22085) — Proposes a typed semantic memory system with information-theoretic retrieval designed for long-horizon agentic tasks, addressing state management, execution-time memory access, and iterative refinement across extended agent trajectories.
- [From Skills to Talent: Organising Heterogeneous Agents as a Real-World Company](https://arxiv.org/abs/2604.22446) — Presents an organizational framework for structuring heterogeneous multi-agent systems using real-world company hierarchies, with architectural patterns for role specialization, agent orchestration, and collaborative task execution.


### 2026-04-20

- [Experience Compression Spectrum: Unifying Memory, Skills, and Rules in LLM Agents](https://arxiv.org/abs/2604.15877) — Proposes a unified framework spanning memory, skills, and rules as complementary experience compression mechanisms in LLM agents, with architectural implications for state management, tool-use design, and iterative refinement across the agent lifecycle.
- [Weak-Link Optimization for Multi-Agent Reasoning and Collaboration](https://arxiv.org/abs/2604.15972) — Introduces a weak-link optimization principle for identifying and strengthening bottleneck agents in multi-agent reasoning pipelines, with empirical evaluation on collaborative task performance.


### 2026-04-13

- [Artifacts as Memory Beyond the Agent Boundary](https://arxiv.org/abs/2604.08756) — Examines how artifacts serve as persistent memory structures that extend state management beyond individual agent boundaries, with implications for multi-agent orchestration and long-horizon workflow design.
- [SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment](https://arxiv.org/abs/2604.08988) — Proposes a benchmark framework for evaluating self-evolving agents across multi-episode trajectories, providing empirical grounding for evaluation loop design and iterative refinement practices in agentic systems.


### 2026-04-06

- [Holos: A Web-Scale LLM-Based Multi-Agent System for the Agentic Web](https://arxiv.org/abs/2604.02334) — Presents architectural design and orchestration patterns for a web-scale multi-agent system, addressing agent coordination, tool use, and production deployment at scale.
- [Improving Role Consistency in Multi-Agent Collaboration via Quantitative Role Clarity](https://arxiv.org/abs/2604.02770) — Proposes a quantitative framework for enforcing role clarity in multi-agent collaboration, improving orchestration reliability and agent coordination consistency with empirical evaluation.


### 2026-03-30

- [AIRA_2: Overcoming Bottlenecks in AI Research Agents](https://arxiv.org/abs/2603.26499) — Identifies and addresses architectural bottlenecks in AI research agent pipelines, with implications for orchestration design, execution reliability, and iterative refinement.
- [Consistency Amplifies: How Behavioral Variance Shapes Agent Accuracy](https://arxiv.org/abs/2603.25764) — Empirical study on how behavioral variance across agent runs affects accuracy, providing grounding for evaluation loop design and reliability practices in agentic workflows.


### 2026-03-24

- [HyEvo: Self-Evolving Hybrid Agentic Workflows for Efficient Reasoning](https://arxiv.org/abs/2603.19639) — Proposes a self-evolving hybrid agentic workflow architecture that dynamically adapts workflow structure and agent composition for efficient multi-step reasoning tasks.
- [Utility-Guided Agent Orchestration for Efficient LLM Tool Use](https://arxiv.org/abs/2603.19896) — Presents a utility-guided orchestration framework for selecting and sequencing LLM tool calls efficiently, with empirical evaluation across multi-step agentic tasks.


---

## Contributing

See the root [README](../../README.md) for how to add a topic. For individual entries, open a PR with the resource and a note on which inclusion criteria it meets.
