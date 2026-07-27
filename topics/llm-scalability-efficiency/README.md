# LLM Scalability & Efficiency [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Techniques and systems for making large language models faster, cheaper, and more accessible — spanning parameter-efficient fine-tuning, compute-efficient architectures, distributed training, quantization, and high-throughput serving infrastructure.

🤖 *This resource list is maintained with the help of [Claude](https://www.anthropic.com/claude) by Anthropic.*

---

## Scope: What Counts as LLM Scalability & Efficiency?

A resource belongs here when it reduces the compute, memory, or latency cost of working with large language models — whether during training, fine-tuning, or inference. The unifying theme is achieving more with less: less memory, less compute, less latency, lower cost.

**Inclusion checklist (meet at least 3 of 4):**

- Reduces compute, memory, or latency cost of LLM training or inference through algorithmic or systems-level innovation
- Applies or evaluates a scalability technique across model sizes, hardware configurations, or deployment scenarios
- Demonstrates measurable efficiency gain (throughput, memory footprint, FLOPs, latency, or cost) with empirical evidence
- Novel contribution to parameter efficiency (PEFT/LoRA), compute efficiency (attention variants, MoE), quantization, distributed training, or serving infrastructure

**Exclude or deprioritize:**

- Generic neural network compression without LLM-specific application or validation
- Hardware design papers without an LLM software-level efficiency contribution
- RLHF, alignment, or agentic applications (covered by other topics)
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
- The agent applies the inclusion checklist above and avoids resources focused on alignment or agentic applications rather than efficiency gains.

---

## Contents

- [Research Assistant Agent](#research-assistant-agent)
- [Parameter-Efficient Fine-Tuning](#parameter-efficient-fine-tuning)
- [Compute-Efficient Architectures](#compute-efficient-architectures)
- [Quantization & Compression](#quantization--compression)
- [Distributed Training](#distributed-training)
- [Serving & Inference Infrastructure](#serving--inference-infrastructure)
- [Research Papers](#research-papers)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Contributing](#contributing)

---

## Parameter-Efficient Fine-Tuning

*Methods that adapt large models with a fraction of the trainable parameters.*

| Project | Description | Stars |
|---------|-------------|-------|
| [PEFT](https://github.com/huggingface/peft) | HuggingFace library unifying LoRA, QLoRA, prefix tuning, prompt tuning, and IA³ under one API. | ![GitHub stars](https://img.shields.io/github/stars/huggingface/peft?style=flat-square) |
| [LoRA](https://github.com/microsoft/LoRA) | Microsoft's original low-rank adaptation implementation — fine-tunes only injected rank-decomposition matrices, reducing trainable params by 10,000×. | ![GitHub stars](https://img.shields.io/github/stars/microsoft/LoRA?style=flat-square) |
| [Unsloth](https://github.com/unslothai/unsloth) | 2× faster LoRA/QLoRA fine-tuning with 70% less memory via hand-written Triton kernels, no custom CUDA required. | ![GitHub stars](https://img.shields.io/github/stars/unslothai/unsloth?style=flat-square) |

---

## Compute-Efficient Architectures

*Attention variants, sparse architectures, and training algorithms that cut FLOPs.*

| Project | Description | Stars |
|---------|-------------|-------|
| [FlashAttention](https://github.com/Dao-AILab/flash-attention) | IO-aware exact attention that is 2–4× faster and uses 5–20× less memory than standard attention via tiling and kernel fusion. | ![GitHub stars](https://img.shields.io/github/stars/Dao-AILab/flash-attention?style=flat-square) |
| [Mixtral (MoE)](https://github.com/mistralai/mistral-inference) | Mistral's mixture-of-experts implementation — 8 experts per token, only 2 active, delivering 7B-param inference cost at 45B-param quality. | ![GitHub stars](https://img.shields.io/github/stars/mistralai/mistral-inference?style=flat-square) |
| [xFormers](https://github.com/facebookresearch/xformers) | Meta's modular transformer library with memory-efficient attention, sparse attention, and optimized building blocks for custom architectures. | ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/xformers?style=flat-square) |

---

## Quantization & Compression

*Reducing model precision and size without proportional quality loss.*

| Project | Description | Stars |
|---------|-------------|-------|
| [bitsandbytes](https://github.com/TimDettmers/bitsandbytes) | 8-bit and 4-bit quantization via LLM.int8() and QLoRA; integrates directly into HuggingFace Transformers. | ![GitHub stars](https://img.shields.io/github/stars/TimDettmers/bitsandbytes?style=flat-square) |
| [AutoGPTQ](https://github.com/AutoGPTQ/AutoGPTQ) | GPTQ-based post-training quantization to 4-bit with optional act-order; supports most HuggingFace causal LMs. | ![GitHub stars](https://img.shields.io/github/stars/AutoGPTQ/AutoGPTQ?style=flat-square) |
| [llm-awq](https://github.com/mit-han-lab/llm-awq) | MIT's Activation-aware Weight Quantization — 4-bit quantization that protects salient weights identified by activation magnitude, outperforming GPTQ on instruction-following tasks. | ![GitHub stars](https://img.shields.io/github/stars/mit-han-lab/llm-awq?style=flat-square) |

---

## Distributed Training

*Frameworks for training LLMs across multiple GPUs and nodes.*

| Project | Description | Stars |
|---------|-------------|-------|
| [DeepSpeed](https://github.com/microsoft/DeepSpeed) | Microsoft's training optimization library implementing ZeRO (Zero Redundancy Optimizer) stages 1–3, offloading, and pipeline parallelism. | ![GitHub stars](https://img.shields.io/github/stars/microsoft/DeepSpeed?style=flat-square) |
| [Megatron-LM](https://github.com/NVIDIA/Megatron-LM) | NVIDIA's framework for tensor, pipeline, and sequence parallelism; used to train GPT-3, LLaMA-scale models on thousands of GPUs. | ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/Megatron-LM?style=flat-square) |
| [torchtitan](https://github.com/pytorch/torchtitan) | PyTorch-native LLM training framework built on FSDP2, tensor parallelism, and async checkpointing — reference implementation for distributed training best practices. | ![GitHub stars](https://img.shields.io/github/stars/pytorch/torchtitan?style=flat-square) |

---

## Serving & Inference Infrastructure

*Systems for high-throughput, low-latency LLM deployment.*

| Project | Description | Stars |
|---------|-------------|-------|
| [vLLM](https://github.com/vllm-project/vllm) | PagedAttention-based inference engine achieving 24× higher throughput than HuggingFace Transformers by eliminating KV cache memory fragmentation. | ![GitHub stars](https://img.shields.io/github/stars/vllm-project/vllm?style=flat-square) |
| [llama.cpp](https://github.com/ggerganov/llama.cpp) | Pure C/C++ inference for LLaMA-family models with 2–6 bit quantization (GGUF format); runs 70B models on consumer hardware. | ![GitHub stars](https://img.shields.io/github/stars/ggerganov/llama.cpp?style=flat-square) |
| [TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) | NVIDIA's optimized inference library with in-flight batching, speculative decoding, and INT4/INT8 quantization for production GPU serving. | ![GitHub stars](https://img.shields.io/github/stars/NVIDIA/TensorRT-LLM?style=flat-square) |

### 2026-07-27

- [Medusa](https://github.com/FasterDecoding/Medusa) — Tree-based speculative decoding using multiple fine-tuned draft heads on the same model — achieves 2–3× inference speedup without a separate draft model.


---

## Research Papers

### Parameter-Efficient Fine-Tuning

- **LoRA: Low-Rank Adaptation of Large Language Models** (ICLR 2022) — [Paper](https://arxiv.org/abs/2106.09685)
  Introduces trainable rank-decomposition matrices injected into frozen weights, reducing GPU memory 3× and training time by a factor without quality loss.

- **QLoRA: Efficient Finetuning of Quantized LLMs** (NeurIPS 2023) — [Paper](https://arxiv.org/abs/2305.14314)
  Combines 4-bit NormalFloat quantization with LoRA adapters and paged optimizers to fine-tune 65B models on a single 48 GB GPU.

- **LongLoRA: Efficient Fine-tuning of Long-Context Large Language Models** (ICLR 2024) — [Paper](https://arxiv.org/abs/2309.12307)
  Extends LLaMA-2 context to 100K tokens using sparse attention during fine-tuning with standard dense attention at inference — only trains 1.7% of parameters.

### Compute-Efficient Architectures

- **FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness** (NeurIPS 2022) — [Paper](https://arxiv.org/abs/2205.14135)
  Reformulates attention as a tiled algorithm that avoids materializing the full attention matrix, achieving 2–4× end-to-end speedup on GPT-2 training.

- **FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning** (ICLR 2024) — [Paper](https://arxiv.org/abs/2307.08691)
  Achieves 50–73% of theoretical peak GPU FLOPs by improving thread block partitioning and reducing non-matmul operations.

- **Mixtral of Experts** (2024) — [Paper](https://arxiv.org/abs/2401.04088)
  Sparse MoE with 8 experts and top-2 routing delivers GPT-3.5-level performance at 6× faster inference than a dense 45B model.

### Quantization & Compression

- **GPTQ: Accurate Post-Training Quantization for Generative Pre-trained Transformers** (ICLR 2023) — [Paper](https://arxiv.org/abs/2210.17323)
  Layer-wise quantization using approximate second-order information; quantizes OPT-175B and BLOOM-176B to 3–4 bits in under 4 hours.

- **AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration** (MLSys 2024) — [Paper](https://arxiv.org/abs/2306.00978)
  Identifies 1% of weights critical to output quality via activation magnitude and protects them during quantization, outperforming GPTQ by 3 perplexity points at 4-bit.

- **LLM.int8(): 8-bit Matrix Multiplication for Transformers at Scale** (NeurIPS 2022) — [Paper](https://arxiv.org/abs/2208.07339)
  Mixed-precision decomposition that handles emergent outlier features in 8-bit, enabling inference of 175B models on consumer GPUs without quality degradation.

### Distributed Training

- **ZeRO: Memory Optimizations Toward Training Trillion Parameter Models** (SC 2020) — [Paper](https://arxiv.org/abs/1910.02054)
  Partitions optimizer states, gradients, and parameters across data-parallel workers, reducing per-GPU memory by 64× vs. standard data parallelism.

- **Megatron-LM: Training Multi-Billion Parameter Language Models Using Model Parallelism** (2019) — [Paper](https://arxiv.org/abs/1909.08053)
  Introduces intra-layer tensor parallelism for transformer blocks, enabling 8.3B parameter GPT-2 training on 512 GPUs with 76% scaling efficiency.

- **Efficient Large-Scale Language Model Training on GPU Clusters Using Megatron-LM** (SC 2021) — [Paper](https://arxiv.org/abs/2104.04473)
  Combines tensor, pipeline, and data parallelism (3D parallelism) to train 1T parameter models on 3072 GPUs at 502 petaFLOP/s.

### Serving & Inference Infrastructure

- **Efficient Memory Management for Large Language Model Serving with PagedAttention** (SOSP 2023) — [Paper](https://arxiv.org/abs/2309.06180)
  Introduces virtual memory paging for KV caches, reducing memory waste from 60–80% to under 4% and enabling 24× throughput gains vs. FasterTransformer.

- **Fast Inference from Transformers via Speculative Decoding** (ICML 2023) — [Paper](https://arxiv.org/abs/2211.17192)
  Uses a small draft model to propose tokens verified in parallel by the large model, achieving 2–3× latency reduction with identical outputs.

- **Continuous Batching: Orca** (OSDI 2022) — [Paper](https://www.usenix.org/conference/osdi22/presentation/yu)
  Iteration-level scheduling replaces request-level batching, increasing GPU utilization 23× on production LLM serving workloads.

---

## Datasets & Benchmarks

| Benchmark | Description | Link |
|-----------|-------------|------|
| MLPerf Inference | Industry-standard benchmark measuring throughput and latency of LLM inference across hardware; includes LLaMA-2 70B and Mixtral 8x7B tasks. | [Site](https://mlcommons.org/benchmarks/inference-datacenter/) |
| Open LLM Perf Leaderboard | Community benchmark ranking models by tokens/second, memory usage, and quality trade-offs across quantization levels on consumer hardware. | [HuggingFace](https://huggingface.co/spaces/optimum/llm-perf-leaderboard) |
| LM-Eval Harness | EleutherAI's evaluation suite — used to measure quality degradation from quantization, pruning, and PEFT across 60+ tasks. | [GitHub](https://github.com/EleutherAI/lm-evaluation-harness) |
| EfficientML Benchmark | Tracks model compression ratios, inference speedups, and quality-efficiency Pareto fronts across pruning and distillation methods. | [Paper](https://arxiv.org/abs/2312.03863) |

---

## Contributing

Contributions are welcome! To add a project or paper, simply [open an issue](../../issues) or submit a PR.

When proposing additions, include a short note on which inclusion criteria the item satisfies and link the strongest supporting evidence (paper/repo/benchmark/blog).

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related rights to this work.
