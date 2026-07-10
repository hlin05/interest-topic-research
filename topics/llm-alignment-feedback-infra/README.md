# LLM Alignment & Feedback Infrastructure [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Infrastructure for specifying desired LLM behavior (contracts, rubrics, model specs), evaluating against those specifications (LLM-as-judge, rubric scoring), and training toward them (RLAIF, Constitutional AI, scalable oversight).

🤖 *This resource list is maintained with the help of [Claude](https://www.anthropic.com/claude) by Anthropic.*

---

## Scope: What Counts as LLM Alignment & Feedback Infrastructure?

A resource belongs here when it addresses the pipeline from behavior specification through AI-generated evaluation to training signal — in base LLM training contexts, not just agentic deployment (see [rlhf-agentic](../rlhf-agentic/README.md) for that).

**Inclusion checklist (meet at least 3 of 4):**

- Defines or implements a specification layer for desired LLM behavior (rubric, contract, model spec, constitution, system prompt as policy)
- Uses AI-generated feedback signals for LLM training or evaluation (RLAIF, LLM-as-judge, AI critique/revision)
- Iterative loop where specification + feedback jointly improve model outputs (not a one-shot annotation pass)
- Empirical outcome (benchmark, eval score, alignment improvement, or measurable quality gain)

**Exclude or deprioritize:**

- RLHF applied only in agentic/multi-step task settings (covered by `rlhf-agentic`)
- Human-only feedback pipelines without an AI-in-the-loop component
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
- The agent applies the inclusion checklist above and avoids resources without an AI-in-the-loop feedback component.

---

## Contents

- [Research Assistant Agent](#research-assistant-agent)
- [Specification Frameworks](#specification-frameworks)
- [Rubric-Based Evaluation & Training](#rubric-based-evaluation--training)
- [RLAIF & AI Feedback Pipelines](#rlaif--ai-feedback-pipelines)
- [Scalable Oversight Methods](#scalable-oversight-methods)
- [Research Papers](#research-papers)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Contributing](#contributing)

---

## Specification Frameworks

*Contracts, model specs, and constitutions that formally define desired LLM behavior.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Anthropic Model Spec](https://github.com/anthropics/model-spec) | Anthropic's public specification of Claude's values, priorities, and behavioral constraints — a worked example of a behavior contract. | ![GitHub stars](https://img.shields.io/github/stars/anthropics/model-spec?style=flat-square) |
| [Constitutional AI](https://github.com/anthropics/constitutional-ai) | Anthropic's approach to alignment using a written constitution to guide AI self-critique and revision. | ![GitHub stars](https://img.shields.io/github/stars/anthropics/constitutional-ai?style=flat-square) |

---

## Rubric-Based Evaluation & Training

*Structured scoring frameworks used as evaluation criteria or reward signal proxies.*

| Project | Description | Stars |
|---------|-------------|-------|
| [MT-Bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) | Multi-turn benchmark using GPT-4 as a judge with structured rubrics to score LLM responses on reasoning and instruction following. | ![GitHub stars](https://img.shields.io/github/stars/lm-sys/FastChat?style=flat-square) |
| [Prometheus](https://github.com/kaistAI/Prometheus) | Open-source LLM fine-tuned as a rubric-following evaluator, designed to match GPT-4 judge quality using reference answers and scoring rubrics. | ![GitHub stars](https://img.shields.io/github/stars/kaistAI/Prometheus?style=flat-square) |

---

## RLAIF & AI Feedback Pipelines

*Systems that use AI-generated feedback as the training signal.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Self-Rewarding Language Models](https://github.com/facebookresearch/llm-self-rewarding) | Meta's approach where the same model generates preference data and trains on it iteratively via LLM-as-judge. | ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/llm-self-rewarding?style=flat-square) |
| [OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | High-performance RLHF/RLAIF training framework supporting PPO, DPO, GRPO, and reward modeling at scale. | ![GitHub stars](https://img.shields.io/github/stars/OpenRLHF/OpenRLHF?style=flat-square) |

---

## Scalable Oversight Methods

*Techniques for supervising AI outputs beyond what direct human annotation can cover.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Debate (OpenAI)](https://github.com/openai/debate) | AI safety technique where two agents argue opposing positions; a human judge determines which is correct, scaling oversight to complex tasks. | ![GitHub stars](https://img.shields.io/github/stars/openai/debate?style=flat-square) |

---

## Research Papers

### Specification & Contracts

- **Constitutional AI: Harmlessness from AI Feedback** (2022) — [Paper](https://arxiv.org/abs/2212.08073)
  Anthropic introduces using a written constitution to guide AI self-critique and revision (RLAIF), enabling alignment without per-output human labels.

- **Model Spec** (2024) — [Blog](https://www.anthropic.com/news/claude-s-constitution)
  Anthropic's public model specification: a detailed contract defining Claude's values, priority ordering, and behavioral constraints.

### Rubric-Based Evaluation

- **Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena** (NeurIPS 2023) — [Paper](https://arxiv.org/abs/2306.05685)
  Establishes LLM-as-judge as a scalable eval methodology using structured rubrics; finds strong correlation with human preference.

- **Prometheus: Inducing Fine-Grained Evaluation Capability in Language Models** (ICLR 2024) — [Paper](https://arxiv.org/abs/2310.08491)
  Trains an open LLM to follow reference rubrics as a judge, matching GPT-4 correlation with human scores on absolute and relative grading tasks.

- **Stabilizing Rubric Integration Training via Decoupled Advantage Normalization** (2026) — [Paper](https://arxiv.org/abs/2603.26535)
  Introduces decoupled advantage normalization to stabilize RL policy training when reward signals are derived from human-defined rubrics.

### RLAIF & AI Feedback

- **RLAIF: Scaling Reinforcement Learning from Human Feedback with AI Feedback** (2023) — [Paper](https://arxiv.org/abs/2309.00267)
  Google DeepMind shows RLAIF (AI-generated preference labels) matches RLHF quality on summarization while scaling annotation cost to near-zero.

- **Self-Rewarding Language Models** (2024) — [Paper](https://arxiv.org/abs/2401.10020)
  Meta demonstrates iterative self-improvement where the model acts as its own judge, generating preference data and improving through DPO.

- **Direct Preference Optimization (DPO)** (NeurIPS 2023) — [Paper](https://arxiv.org/abs/2305.18290)
  Eliminates the explicit reward model by re-parameterizing RLHF as a supervised objective on preference pairs — widely used downstream of RLAIF pipelines.

### Scalable Oversight

- **Scalable Oversight via AI Debate** (2018) — [Paper](https://arxiv.org/abs/1805.00899)
  OpenAI's foundational paper on debate as a scalable oversight mechanism for tasks too complex for direct human evaluation.

- **Weak-to-Strong Generalization** (2023) — [Paper](https://arxiv.org/abs/2312.09390)
  OpenAI studies whether strong models can be aligned using only weak supervisor labels — a core challenge for scalable oversight.

---

## Datasets & Benchmarks

| Benchmark | Description | Link |
|-----------|-------------|------|
| UltraFeedback | 64K instruction dataset with GPT-4 rubric scores across four dimensions; widely used for RLAIF and DPO training. | [Dataset](https://huggingface.co/datasets/openbmb/UltraFeedback) |
| Prometheus-Eval | Evaluation benchmark for rubric-following judge models; tests absolute and relative grading against human annotations. | [Paper](https://arxiv.org/abs/2405.01535) \| [GitHub](https://github.com/prometheus-eval/prometheus-eval) |
| MT-Bench | 80 multi-turn questions with GPT-4-judged rubric scoring across reasoning, coding, math, and writing. | [GitHub](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) |
| AlpacaEval | LLM-as-judge leaderboard using win-rate against GPT-4-Turbo as the reference. | [GitHub](https://github.com/tatsu-lab/alpaca_eval) |

---

## Contributing

Contributions are welcome! To add a project or paper, simply [open an issue](../../issues) or submit a PR.

When proposing additions, include a short note on which inclusion criteria the item satisfies and link the strongest supporting evidence (paper/repo/benchmark/blog).

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related rights to this work.
