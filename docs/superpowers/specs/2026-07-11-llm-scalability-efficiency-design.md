# Design: LLM Scalability & Efficiency Topic

**Date:** 2026-07-11
**Status:** Approved

---

## Summary

Add a new research topic, `llm-scalability-efficiency`, to the weekly automated research pipeline. The topic tracks techniques and systems for making large language models faster, cheaper, and more accessible — spanning parameter-efficient fine-tuning, compute-efficient architectures, distributed training, quantization, and high-throughput serving infrastructure.

---

## Differentiation from Existing Topics

| Existing Topic | Focus | Overlap with new topic |
|---|---|---|
| `agentic-ml` | Autonomous ML workflow agents | None — agentic-ml is about goal-directed planning, not model performance |
| `agentic-workflow-design` | Agent architecture patterns | None — design patterns, not compute efficiency |
| `top-claude-tips` | Practical Claude usage tips | None |
| `harness-engineering` | Agent execution scaffolding | None — harness layer, not model internals |
| `rlhf-agentic` | RLHF in agentic systems | None — alignment training, not efficiency |
| `transformers-beyond-nlp` | Transformers in non-NLP domains | Minimal — domain application, not efficiency techniques |
| `llm-alignment-feedback-infra` | Rubrics, contracts, RLAIF | None — specification/training signal, not compute performance |

The new topic is the only one focused on compute, memory, latency, and throughput of LLMs.

---

## Topic Configuration

**ID:** `llm-scalability-efficiency`
**Name:** LLM Scalability & Efficiency
**Description:** Techniques and systems for making large language models faster, cheaper, and more accessible — spanning parameter-efficient fine-tuning, compute-efficient architectures, distributed training, quantization, and high-throughput serving infrastructure

### Grok Keywords
```
LLM quantization, GPTQ, AWQ, LoRA, QLoRA, PEFT, Flash Attention, vLLM,
speculative decoding, PagedAttention, FSDP, tensor parallelism,
mixture of experts, LLM inference optimization, LLM serving throughput
```

### arXiv Feeds
- `cs.LG` — Machine Learning (primary venue for efficiency papers)
- `cs.AR` — Hardware Architecture (hardware-aware methods)
- `cs.DC` — Distributed Computing (distributed training and serving)

### Inclusion Criteria (meet at least 3 of 4)
1. Reduces compute, memory, or latency cost of LLM training or inference through algorithmic or systems-level innovation
2. Applies or evaluates a scalability technique across model sizes, hardware configurations, or deployment scenarios
3. Demonstrates measurable efficiency gain (throughput, memory footprint, FLOPs, latency, or cost) with empirical evidence
4. Novel contribution to parameter efficiency (PEFT/LoRA), compute efficiency (attention variants, MoE), quantization, distributed training, or serving infrastructure

### Exclusions
- Generic neural network compression without LLM-specific application or validation
- Hardware design papers without an LLM software-level efficiency contribution
- RLHF, alignment, or agentic applications (covered by other topics)
- Social-only announcements without a primary technical source (paper/repo/blog)
- Stale resources unless there is a substantive new release/update in the recent window

### Max entries per week: 4

---

## Implementation

Two files need to be created or modified:

1. **`topics.yml`** — append the new topic entry under the existing `topics` list
2. **`topics/llm-scalability-efficiency/README.md`** — create with the topic's scope, inclusion criteria, and initial seeded resources

No changes to the GitHub Actions workflow are required.

### README Initial Sections
- Parameter-Efficient Fine-Tuning (LoRA, QLoRA, PEFT methods)
- Compute-Efficient Architectures (Flash Attention, MoE, Mixture of Depths)
- Quantization & Compression (GPTQ, AWQ, bitsandbytes)
- Distributed Training (FSDP, tensor/pipeline parallelism)
- Serving & Inference Infrastructure (vLLM, speculative decoding, batching)
- Research Papers
- Datasets & Benchmarks
