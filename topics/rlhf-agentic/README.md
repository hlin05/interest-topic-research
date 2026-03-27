# RLHF in Agentic Systems [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Reinforcement learning from human feedback (RLHF) and its application in building aligned, adaptive agentic AI systems—covering reward modeling, preference learning, Constitutional AI, and human-in-the-loop RL for autonomous agents.

🤖 *This resource list is maintained with the help of [Claude](https://www.anthropic.com/claude) by Anthropic.*

---

## Scope: What Counts as RLHF in Agentic Systems?

A resource belongs in this list when it demonstrates RLHF or related human-feedback techniques applied to agentic or autonomous AI behavior.

**Inclusion checklist (meet at least 3 of 4):**

- Applies RLHF, RLAIF, reward modeling, or preference learning in an agentic or autonomous setting
- Goal-directed agent behavior shaped by human feedback signals or learned reward models
- Iterative alignment loop (human ratings, preference comparisons, or AI-generated feedback refine agent policy)
- Empirical outcome (benchmark, task success rate, safety evaluation, or measurable alignment improvement)

**Exclude or deprioritize:**

- RLHF applied only to static language model fine-tuning without agentic deployment
- Social-only announcements without a primary technical source (paper/repo/blog)
- Generic RL tutorials without human feedback or agentic alignment focus
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
- The agent applies the inclusion checklist in this README and avoids RLHF resources without an agentic component.

---

## Contents

- [Research Assistant Agent](#research-assistant-agent)
- [Foundational Methods](#foundational-methods)
- [Reward Modeling & Preference Learning](#reward-modeling--preference-learning)
- [RLHF for LLM Agents](#rlhf-for-llm-agents)
- [Constitutional AI & RLAIF](#constitutional-ai--rlaif)
- [Human-in-the-Loop Agentic Systems](#human-in-the-loop-agentic-systems)
- [Research Papers](#research-papers)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Contributing](#contributing)

---

## Foundational Methods

*Seminal techniques establishing RLHF as a training paradigm.*

| Project | Description | Stars |
|---------|-------------|-------|
| [TRL (Transformer Reinforcement Learning)](https://github.com/huggingface/trl) | HuggingFace library for training LLMs with RL, supporting PPO, DPO, GRPO, and reward modeling. | ![GitHub stars](https://img.shields.io/github/stars/huggingface/trl?style=flat-square) |
| [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | High-performance RLHF training framework with Ray-based distributed support for 70B+ models. | ![GitHub stars](https://img.shields.io/github/stars/OpenRLHF/OpenRLHF?style=flat-square) |
| [DeepSpeed-Chat](https://github.com/microsoft/DeepSpeed) | Microsoft's end-to-end RLHF pipeline integrated into DeepSpeed for scalable training. | ![GitHub stars](https://img.shields.io/github/stars/microsoft/DeepSpeed?style=flat-square) |

---

## Reward Modeling & Preference Learning

*Systems that learn human preferences to guide agent behavior.*

| Project | Description | Stars |
|---------|-------------|-------|
| [RewardBench](https://github.com/allenai/reward-bench) | AllenAI benchmark for evaluating reward models used in RLHF pipelines. | ![GitHub stars](https://img.shields.io/github/stars/allenai/reward-bench?style=flat-square) |
| [Preference Transformer](https://github.com/cldoughty/preference-transformer) | Transformer-based reward model learning from human preference comparisons for offline RL. | ![GitHub stars](https://img.shields.io/github/stars/cldoughty/preference-transformer?style=flat-square) |

---

## RLHF for LLM Agents

*Applying RLHF to train LLMs as agents for tool use, planning, and task execution.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Agentless + RLHF](https://github.com/OpenAgentX/agentless-rlhf) | RLHF fine-tuning pipeline for software engineering agents using preference data from task outcomes. | ![GitHub stars](https://img.shields.io/github/stars/OpenAgentX/agentless-rlhf?style=flat-square) |
| [RLVR (RL via Verifiable Rewards)](https://github.com/RLVR-org/rlvr) | Trains agents on tasks with verifiable outcomes (math, code) as a scalable alternative to human labels. | ![GitHub stars](https://img.shields.io/github/stars/RLVR-org/rlvr?style=flat-square) |

---

## Constitutional AI & RLAIF

*AI-generated feedback as a scalable substitute for human annotation in agentic alignment.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Anthropic Constitutional AI](https://github.com/anthropics/constitutional-ai) | Anthropic's approach to alignment using AI self-critique and revision guided by a written constitution. | ![GitHub stars](https://img.shields.io/github/stars/anthropics/constitutional-ai?style=flat-square) |

---

## Human-in-the-Loop Agentic Systems

*Systems that integrate human feedback at runtime to guide or correct agent behavior.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Rlang](https://github.com/nicksyth/rlang) | Natural language reward specification framework allowing humans to define agent goals via language. | ![GitHub stars](https://img.shields.io/github/stars/nicksyth/rlang?style=flat-square) |
| [TAMER](https://github.com/wesleysmithcs/TAMER) | Training an Agent Manually via Evaluative Reinforcement — real-time human feedback shaping agent policy. | ![GitHub stars](https://img.shields.io/github/stars/wesleysmithcs/TAMER?style=flat-square) |

---

## Research Papers

### Foundational RLHF

- **Learning to summarize from human feedback** (NeurIPS 2020) - [Paper](https://arxiv.org/abs/2009.01325) | [Code](https://github.com/openai/summarize-from-feedback)
  OpenAI's landmark paper demonstrating RLHF for summarization. Reward model trained on human comparisons, then PPO fine-tunes the policy.

- **Training language models to follow instructions with human feedback (InstructGPT)** (NeurIPS 2022) - [Paper](https://arxiv.org/abs/2203.02155)
  Aligns GPT-3 to follow instructions using RLHF. Foundation for modern instruction-tuned LLMs.

- **Constitutional AI: Harmlessness from AI Feedback** (2022) - [Paper](https://arxiv.org/abs/2212.08073)
  Anthropic introduces RLAIF — AI-generated critique and revision guided by a written constitution, scaling alignment beyond human labeling.

### Preference Optimization

- **Direct Preference Optimization: Your Language Model is Secretly a Reward Model (DPO)** (NeurIPS 2023) - [Paper](https://arxiv.org/abs/2305.18290)
  Eliminates explicit reward model and RL loop by re-parameterizing RLHF as a supervised objective on preference pairs.

- **GRPO: Group Relative Policy Optimization** (2024) - [Paper](https://arxiv.org/abs/2402.03300)
  DeepSeek's RL method using group-relative rewards, central to DeepSeek-R1 training. More compute-efficient than PPO for reasoning tasks.

- **KTO: Model Alignment as Prospect Theoretic Optimization** (ICML 2024) - [Paper](https://arxiv.org/abs/2402.01306)
  Aligns models using only binary signal (desirable/undesirable) without requiring preference pairs, enabling alignment from unpaired feedback.

### RLHF for Agentic Systems

- **RLHF Workflow: From Reward Modeling to Online RLHF** (2024) - [Paper](https://arxiv.org/abs/2405.07863)
  Reproduces online RLHF training pipelines with iterative reward model updates. Documents practical challenges and solutions for agentic RLHF.

- **RLVR is Not RL: Reward Learning and Policy Optimization in the Absence of Verifiable Rewards** (2025) - [Paper](https://arxiv.org/abs/2501.09576)
  Distinguishes verifiable reward training (RLVR) from RLHF with learned reward models, clarifying when each approach is appropriate for agentic settings.

- **Agent-FLAN: Designing Data and Methods for Effective Agent Tuning** (NeurIPS 2024) - [Paper](https://arxiv.org/abs/2403.12881)
  Combines SFT and RL signal for training LLMs as tool-using agents, showing that preference-based fine-tuning improves agentic task completion.

- **ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering** (2025) - [Paper](https://arxiv.org/abs/2505.23723)
  Applies online RL to train LLM agents for ML engineering tasks with exploration-enriched fine-tuning and step-wise reward signals.

- **SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks** (2025) - [Paper](https://arxiv.org/abs/2503.15478)
  RL framework for multi-turn agentic tasks assigning step-level credit using a judge model trained on human comparisons.

- **Reinforcement Learning for Long-Horizon Interactive LLM Agents** (2025) - [Paper](https://arxiv.org/abs/2502.01600)
  Trains LLM agents on long-horizon tasks (web navigation, code execution) using sparse reward signals from task outcomes.

### Reward Modeling

- **Scaling Laws for Reward Model Overoptimization** (2022) - [Paper](https://arxiv.org/abs/2210.10760)
  Characterizes how optimizing too aggressively against a proxy reward leads to policy collapse — critical for agentic reward design.

- **Let's Verify Step by Step (Process Reward Models)** (2023) - [Paper](https://arxiv.org/abs/2305.20050)
  OpenAI introduces process reward models (PRMs) that score intermediate reasoning steps rather than final outcomes. Key for agentic multi-step tasks.

- **Math-Shepherd: Verify and Reinforce LLMs Step-by-Step Without Human Annotations** (ACL 2024) - [Paper](https://arxiv.org/abs/2312.08935)
  Automated process reward model construction using execution-verified step labels. Enables scalable PRM training for agentic reasoning.

### Safety & Alignment in Agents

- **RLHF is Not Yet Scalable for LLM-based Agents** (2024) - [Paper](https://arxiv.org/abs/2307.13981)
  Identifies challenges with applying standard RLHF to multi-step agents: reward sparsity, action space complexity, and annotation difficulty.

- **Reward Tampering Problems and Solutions in Reinforcement Learning** (2019) - [Paper](https://arxiv.org/abs/1908.04734)
  DeepMind's analysis of how sufficiently capable agents may manipulate their reward signal — foundational for agentic safety design.

---

## Datasets & Benchmarks

*Preference datasets and benchmarks for evaluating RLHF-trained agents.*

| Benchmark | Description | Link |
|-----------|-------------|------|
| Anthropic HH-RLHF | Human preference data (helpful/harmless) collected for Constitutional AI and RLHF alignment research. | [Dataset](https://huggingface.co/datasets/Anthropic/hh-rlhf) |
| OpenAI Summarization Comparisons | Human comparison data for summarization quality used in the landmark RLHF summarization paper. | [Dataset](https://huggingface.co/datasets/openai/summarize_from_feedback) |
| RewardBench | Structured benchmark for evaluating reward models across chat, safety, and reasoning domains. | [Paper](https://arxiv.org/abs/2403.13787) \| [GitHub](https://github.com/allenai/reward-bench) |
| UltraFeedback | Large-scale preference dataset (64K instructions, 256K responses) with GPT-4 scoring for DPO/RLHF training. | [Dataset](https://huggingface.co/datasets/openbmb/UltraFeedback) |
| WebArena | Realistic web-based agent benchmark where RLHF-trained agents are evaluated on long-horizon tasks. | [Paper](https://arxiv.org/abs/2307.13854) \| [GitHub](https://github.com/web-arena-x/webarena) |

---

## Contributing

Contributions are welcome! To add a project or paper, simply [open an issue](../../issues) or submit a PR.

When proposing additions, include a short note on which inclusion criteria the item satisfies and link the strongest supporting evidence (paper/repo/benchmark/blog).

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related rights to this work.
