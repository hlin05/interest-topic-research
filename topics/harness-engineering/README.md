# Harness Engineering [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Harness engineering covers the design and implementation of the scaffolding, execution environments, and control infrastructure that host AI agents—the layer between the model and the world that manages the agent loop, tool dispatch, context, state, safety constraints, and observability.

🤖 *This resource list is maintained with the help of [Claude](https://www.anthropic.com/claude) by Anthropic.*

---

## Scope: What Counts as Harness Engineering?

A resource belongs here when it substantively addresses the *infrastructure* layer of agent execution, not just the agent's reasoning or application logic.

**Inclusion checklist (meet at least 3 of 4):**

- Defines or implements the execution loop, scaffolding, or runtime environment that hosts an AI agent
- Manages tool dispatch, context handling, state management, or safety constraints at the harness layer
- Evaluates or benchmarks agent behavior through controlled harness-mediated interactions
- Empirical or production evidence of harness design improving reliability, safety, or performance

**Exclude or deprioritize:**

- Agent application logic unrelated to the hosting infrastructure (e.g., pure prompt engineering)
- Generic CI/CD or test frameworks not specific to AI agent execution
- Social-only announcements without a primary technical source (paper/repo/blog)
- Stale resources unless there is a substantive new release/update in the recent window

---

## Research Assistant Agent

This repository runs a weekly **Research Assistant Agent** via GitHub Actions to scout and triage potential additions.

- Workflow: `.github/workflows/weekly-resource-research.yml`
- Default Grok scout model: `grok-4-1-fast-reasoning` (override with `GROK_MODEL` repository variable)
- Signal sources: xAI Grok social scout + arXiv RSS scout + Claude curation pass

**Behavior:**

- If high-confidence additions are found, the agent updates `README.md` and opens a draft PR with a supporting suggestion log.
- If no high-confidence additions are found, the agent opens an issue log with the weekly scout outputs (instead of forcing changes).
- The agent applies the inclusion checklist above and avoids resources focused only on model capabilities without harness-layer contributions.

---

## Contents

- [Research Assistant Agent](#research-assistant-agent)
- [Agent Execution Frameworks](#agent-execution-frameworks)
- [Evaluation Harnesses](#evaluation-harnesses)
- [Tool & API Integration Layers](#tool--api-integration-layers)
- [Safety & Constraint Infrastructure](#safety--constraint-infrastructure)
- [Observability & Debugging](#observability--debugging)
- [Research Papers](#research-papers)
- [Contributing](#contributing)

---

## Agent Execution Frameworks

*Runtimes and scaffolds that manage the agent loop, tool dispatch, and context.*

| Project | Description | Stars |
|---------|-------------|-------|
| [LangGraph](https://github.com/langchain-ai/langgraph) | Graph-based agent runtime with explicit state machines, checkpointing, and human-in-the-loop interrupts. | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langgraph?style=flat-square) |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Agent harness with sandboxed execution, event stream architecture, and pluggable agent backends. | ![GitHub stars](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=flat-square) |
| [SWE-agent](https://github.com/SWE-agent/SWE-agent) | Agent-Computer Interface (ACI) harness for software engineering tasks with controlled file/shell access. | ![GitHub stars](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=flat-square) |
| [Agentless](https://github.com/OpenAgentX/agentless) | Minimalist harness for code repair: localize, repair, validate — no dynamic tool selection overhead. | ![GitHub stars](https://img.shields.io/github/stars/OpenAgentX/agentless?style=flat-square) |
| [inspect_ai](https://github.com/UKGovernmentBEIS/inspect_ai) | UK AISI's evaluation harness for LLM agents — tasks, solvers, scorers, and sandboxed tool execution. | ![GitHub stars](https://img.shields.io/github/stars/UKGovernmentBEIS/inspect_ai?style=flat-square) |
| [smolagents](https://github.com/huggingface/smolagents) | HuggingFace's minimal agent harness with code-as-actions execution and sandboxed Python interpreter. | ![GitHub stars](https://img.shields.io/github/stars/huggingface/smolagents?style=flat-square) |
| [Claude Code SDK](https://github.com/anthropics/claude-code) | Anthropic's CLI/SDK harness for Claude agents with hooks, permissions, and session management. | ![GitHub stars](https://img.shields.io/github/stars/anthropics/claude-code?style=flat-square) |

### 2026-03-30

- [AutoGen Studio](https://github.com/microsoft/autogen/tree/main/python/packages/autogen-studio) — Microsoft Research's visual IDE and runtime for designing, debugging, and executing multi-agent workflows — includes execution scaffolding, agent session management, and interactive harness-level debugging.


---

## Evaluation Harnesses

*Frameworks for running controlled agent evaluations with reproducible environments.*

| Project | Description | Stars |
|---------|-------------|-------|
| [EleutherAI lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) | Standard harness for LLM benchmark evaluation across hundreds of tasks with pluggable model backends. | ![GitHub stars](https://img.shields.io/github/stars/EleutherAI/lm-evaluation-harness?style=flat-square) |
| [HELM](https://github.com/stanford-crfm/helm) | Stanford's holistic evaluation harness covering accuracy, calibration, robustness, fairness, and efficiency. | ![GitHub stars](https://img.shields.io/github/stars/stanford-crfm/helm?style=flat-square) |
| [AgentBench](https://github.com/THUDM/AgentBench) | Multi-environment harness evaluating LLM agents across OS, DB, web, game, and code tasks. | ![GitHub stars](https://img.shields.io/github/stars/THUDM/AgentBench?style=flat-square) |
| [τ-bench](https://github.com/sierra-research/tau-bench) | Harness for evaluating agents in realistic customer-service task environments with dynamic user simulation. | ![GitHub stars](https://img.shields.io/github/stars/sierra-research/tau-bench?style=flat-square) |
| [MLE-bench](https://github.com/openai/mle-bench) | Harness running agents against 75 Kaggle competitions in isolated Docker environments with metric validation. | ![GitHub stars](https://img.shields.io/github/stars/openai/mle-bench?style=flat-square) |
| [WebArena](https://github.com/web-arena-x/webarena) | Self-hosted web environment harness with deterministic task replay for evaluating browser-using agents. | ![GitHub stars](https://img.shields.io/github/stars/web-arena-x/webarena?style=flat-square) |

---

## Tool & API Integration Layers

*Protocols and middleware for connecting agents to tools, APIs, and external systems.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Model Context Protocol (MCP)](https://github.com/modelcontextprotocol/specification) | Anthropic's open standard for connecting agents to tools, resources, and prompts via a unified server interface. | ![GitHub stars](https://img.shields.io/github/stars/modelcontextprotocol/specification?style=flat-square) |
| [LangChain Tools](https://github.com/langchain-ai/langchain) | Standardized tool abstraction layer with 200+ integrations for agent harnesses. | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langchain?style=flat-square) |
| [ToolBench](https://github.com/OpenBMB/ToolBench) | Benchmark and training framework for tool-augmented LLMs across 16,000+ real-world APIs. | ![GitHub stars](https://img.shields.io/github/stars/OpenBMB/ToolBench?style=flat-square) |

---

## Safety & Constraint Infrastructure

*Harness-layer mechanisms for sandboxing, permission gating, and safe execution.*

| Project | Description | Stars |
|---------|-------------|-------|
| [E2B](https://github.com/e2b-dev/e2b) | Sandboxed cloud execution environment for running agent-generated code safely with filesystem isolation. | ![GitHub stars](https://img.shields.io/github/stars/e2b-dev/e2b?style=flat-square) |
| [Daytona](https://github.com/daytonaio/daytona) | Secure, isolated development environments for agent code execution with snapshot/restore. | ![GitHub stars](https://img.shields.io/github/stars/daytonaio/daytona?style=flat-square) |
| [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) | NVIDIA's programmable guardrails layer for constraining LLM outputs and tool use in agent pipelines. | ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/NeMo-Guardrails?style=flat-square) |

---

## Observability & Debugging

*Tools for tracing, logging, and debugging agent execution at the harness level.*

| Project | Description | Stars |
|---------|-------------|-------|
| [LangSmith](https://github.com/langchain-ai/langsmith-sdk) | Tracing and debugging platform for LangChain and LangGraph agent runs with step-level inspection. | ![GitHub stars](https://img.shields.io/github/stars/langchain-ai/langsmith-sdk?style=flat-square) |
| [Arize Phoenix](https://github.com/Arize-ai/phoenix) | Open-source observability for LLM applications — traces, spans, evals, and prompt analysis. | ![GitHub stars](https://img.shields.io/github/stars/Arize-ai/phoenix?style=flat-square) |
| [AgentOps](https://github.com/AgentOps-AI/agentops) | Observability SDK for AI agents — session replay, cost tracking, and error analytics. | ![GitHub stars](https://img.shields.io/github/stars/AgentOps-AI/agentops?style=flat-square) |
| [Langfuse](https://github.com/langfuse/langfuse) | Open-source LLM engineering platform with traces, evals, and prompt management for agent debugging. | ![GitHub stars](https://img.shields.io/github/stars/langfuse/langfuse?style=flat-square) |

---

## Research Papers

### Agent-Computer Interfaces & Scaffolding Design

- **SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering** (NeurIPS 2024) - [Paper](https://arxiv.org/abs/2405.15793) | [Code](https://github.com/SWE-agent/SWE-agent)
  Introduces the ACI concept — purpose-built harness interfaces outperform raw shell access by constraining the action space for agent reliability.

- **OpenHands: An Open Platform for AI Software Agents** (2024) - [Paper](https://arxiv.org/abs/2407.16741) | [Code](https://github.com/All-Hands-AI/OpenHands)
  Event-stream architecture separating agent logic from harness concerns (sandbox, file access, browser control) for modular agent deployment.

- **ADAS: Automated Design of Agentic Systems** (2024) - [Paper](https://arxiv.org/abs/2408.08435)
  Meta-agent that searches the space of harness designs (prompts, tools, control flow) to automatically optimize scaffolding for new tasks.

### Evaluation Harness Design

- **AgentBench: Evaluating LLMs as Agents** (ICLR 2024) - [Paper](https://arxiv.org/abs/2308.03688) | [Code](https://github.com/THUDM/AgentBench)
  Systematic evaluation harness spanning 8 environments. Shows significant gaps between API model rankings on benchmarks vs. agentic task performance.

- **τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains** (2024) - [Paper](https://arxiv.org/abs/2406.12045) | [Code](https://github.com/sierra-research/tau-bench)
  Harness simulating dynamic user behavior during agent task execution — captures failures that static benchmarks miss.

- **Inspect: A Framework for Large Language Model Evaluations** (2024) - [Blog](https://ukgovernmentbeis.github.io/inspect_ai/) | [Code](https://github.com/UKGovernmentBEIS/inspect_ai)
  UK AISI's evaluation harness with composable solvers, scorers, and sandboxed tool execution for safety-critical agent evaluation.

### Sandboxing & Safe Execution

- **InterCode: Standardizing and Benchmarking Interactive Coding with Execution Feedback** (NeurIPS 2023) - [Paper](https://arxiv.org/abs/2306.14898) | [Code](https://github.com/princeton-nlp/intercode)
  Defines a harness standard for interactive code execution with sandboxed environments and reward signals from execution outcomes.

- **PACO: Plan-Assisted Code Generation via Agent Communication** (2025) - [Paper](https://arxiv.org/abs/2503.12542)
  Examines harness-level communication protocols between planning and execution agents with isolated execution environments.

### Harness Failure Modes & Reliability

- **Failures Pave the Way: Enhancing Large Language Models through Tuning with Trial and Error** (2024) - [Paper](https://arxiv.org/abs/2402.17747)
  Analyzes how harness-level error feedback (failed tool calls, execution errors) can be structured to improve agent policy via fine-tuning.

- **Large Language Models Cannot Self-Correct Reasoning Yet** (ICLR 2024) - [Paper](https://arxiv.org/abs/2310.01848)
  Shows that self-correction only helps when the harness provides ground-truth external feedback — harness signal quality determines correction quality.

- **AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses** (2024) - [Paper](https://arxiv.org/abs/2406.13352) | [Code](https://github.com/ethz-spylab/agentdojo)
  Harness for evaluating agent vulnerability to prompt injection through tool outputs — harness-layer filtering as a defense mechanism.

### Context & State Management

- **MemGPT: Towards LLMs as Operating Systems** (2024) - [Paper](https://arxiv.org/abs/2310.08560) | [Code](https://github.com/cpacker/MemGPT)
  Harness that manages tiered memory (in-context, external storage) and self-directed context paging for long-running agents.

- **A-MEM: Agentic Memory System for LLM Agents** (2025) - [Paper](https://arxiv.org/abs/2502.12110)
  Dynamic memory harness that structures, indexes, and retrieves agent experiences using Zettelkasten-inspired note linking.

---

## Contributing

Contributions are welcome! To add a project or paper, simply [open an issue](../../issues) or submit a PR.

When proposing additions, include a short note on which inclusion criteria the item satisfies and link the strongest supporting evidence (paper/repo/benchmark/blog).

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related rights to this work.
