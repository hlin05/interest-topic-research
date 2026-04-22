# Transformers Beyond NLP [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Applications of the transformer architecture outside of natural language processing and language modeling — spanning biology, chemistry, computer vision, physics, genomics, materials science, time-series forecasting, and more.

🤖 *This resource list is maintained with the help of [Claude](https://www.anthropic.com/claude) by Anthropic.*

---

## Scope: What Counts as Transformers Beyond NLP?

A resource belongs in this list when it applies the transformer architecture (self-attention, positional encoding, encoder/decoder design) to a domain other than natural language processing or language modeling.

**Inclusion checklist (meet at least 3 of 4):**

- Applies transformer architecture to a non-NLP domain (biology, chemistry, vision, physics, time-series, etc.)
- Addresses a domain-specific task with measurable performance (structure prediction, property forecasting, classification, generation)
- Iterative modeling or training loop grounded in domain data (sequences, graphs, spectra, images, signals)
- Empirical outcome demonstrating advantage of transformer approach (benchmark result, ablation, competition result, or downstream application)

**Exclude or deprioritize:**

- Pure NLP or language model applications (even if the model is novel)
- Vision-language or multimodal models where the primary contribution is NLP/captioning, not a non-language domain task
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
- The agent applies the inclusion checklist in this README and excludes NLP-primary resources.

---

## Contents

- [Research Assistant Agent](#research-assistant-agent)
- [Biology & Genomics](#biology--genomics)
- [Protein & Molecular Structure](#protein--molecular-structure)
- [Chemistry & Materials Science](#chemistry--materials-science)
- [Computer Vision](#computer-vision)
- [Time-Series & Signals](#time-series--signals)
- [Physics & Scientific Computing](#physics--scientific-computing)
- [Research Papers](#research-papers)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [Contributing](#contributing)

---

## Biology & Genomics

*Transformers applied to DNA, RNA, and genomic sequences.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Nucleotide Transformer](https://github.com/instadeepai/nucleotide-transformer) | InstaDeep/Google DeepMind foundation model for DNA sequences, trained on 3,000+ genomes. | ![GitHub stars](https://img.shields.io/github/stars/instadeepai/nucleotide-transformer?style=flat-square) |
| [DNABERT-2](https://github.com/Zhihan1996/DNABERT-2) | Multi-species DNA foundation model using BPE tokenization and ALiBi attention. | ![GitHub stars](https://img.shields.io/github/stars/Zhihan1996/DNABERT-2?style=flat-square) |
| [Enformer](https://github.com/google-deepmind/deepmind-research/tree/master/enformer) | DeepMind transformer for predicting gene expression from DNA sequence at long range. | ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/deepmind-research?style=flat-square) |

---

## Protein & Molecular Structure

*Transformers for protein folding, structure prediction, and molecular design.*

| Project | Description | Stars |
|---------|-------------|-------|
| [ESM-2 / ESMFold](https://github.com/facebookresearch/esm) | Meta's protein language models; ESMFold predicts 3D structure from sequence using a single transformer. | ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/esm?style=flat-square) |
| [OpenFold](https://github.com/aqlaboratory/openfold) | Open-source reimplementation of AlphaFold2's Evoformer transformer for structure prediction. | ![GitHub stars](https://img.shields.io/github/stars/aqlaboratory/openfold?style=flat-square) |
| [Uni-Mol](https://github.com/deepmodeling/Uni-Mol) | DPTECH universal molecular transformer pretrained on 3D conformations for property prediction and docking. | ![GitHub stars](https://img.shields.io/github/stars/deepmodeling/Uni-Mol?style=flat-square) |

---

## Chemistry & Materials Science

*Transformers for molecular property prediction, synthesis planning, and materials discovery.*

| Project | Description | Stars |
|---------|-------------|-------|
| [ChemBERTa](https://github.com/seyonechithrananda/bert-loves-chemistry) | RoBERTa pretrained on SMILES strings for molecular property prediction. | ![GitHub stars](https://img.shields.io/github/stars/seyonechithrananda/bert-loves-chemistry?style=flat-square) |
| [MolBERT](https://github.com/BenevolentAI/MolBERT) | BenevolentAI BERT model for learning molecular representations from SMILES. | ![GitHub stars](https://img.shields.io/github/stars/BenevolentAI/MolBERT?style=flat-square) |
| [Graphormer](https://github.com/microsoft/Graphormer) | Microsoft Research transformer for molecular graph property prediction; winner of OGB-LSC. | ![GitHub stars](https://img.shields.io/github/stars/microsoft/Graphormer?style=flat-square) |

---

## Computer Vision

*Pure vision transformers and transformer-based vision architectures.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Vision Transformer (ViT)](https://github.com/google-research/vision_transformer) | Google's original image-patch transformer achieving strong ImageNet performance without convolutions. | ![GitHub stars](https://img.shields.io/github/stars/google-research/vision_transformer?style=flat-square) |
| [Segment Anything (SAM)](https://github.com/facebookresearch/segment-anything) | Meta's promptable image segmentation model using a transformer-based mask decoder. | ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/segment-anything?style=flat-square) |
| [DINO / DINOv2](https://github.com/facebookresearch/dinov2) | Meta self-supervised vision transformer with strong spatial features for segmentation and retrieval. | ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/dinov2?style=flat-square) |

---

## Time-Series & Signals

*Transformers applied to temporal signals, forecasting, and sensor data.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Time-Series Library (TSLib)](https://github.com/thuml/Time-Series-Library) | Tsinghua benchmark suite covering transformer-based time-series forecasting models (PatchTST, iTransformer, etc.). | ![GitHub stars](https://img.shields.io/github/stars/thuml/Time-Series-Library?style=flat-square) |
| [PatchTST](https://github.com/yuqinie98/PatchTST) | Patch-based ViT-style transformer for long-horizon time-series forecasting with channel independence. | ![GitHub stars](https://img.shields.io/github/stars/yuqinie98/PatchTST?style=flat-square) |
| [Moirai](https://github.com/SalesforceAIResearch/uni2ts) | Salesforce universal time-series transformer pretrained on LOTSA data for zero-shot forecasting. | ![GitHub stars](https://img.shields.io/github/stars/SalesforceAIResearch/uni2ts?style=flat-square) |

---

## Physics & Scientific Computing

*Transformers for physical simulation, weather forecasting, and scientific PDEs.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Pangu-Weather](https://github.com/198808xc/Pangu-Weather) | Huawei 3D Earth transformer for deterministic global weather forecasting at 1-hour resolution. | ![GitHub stars](https://img.shields.io/github/stars/198808xc/Pangu-Weather?style=flat-square) |
| [Aurora](https://github.com/microsoft/aurora) | Microsoft Research foundation model for atmospheric forecasting trained on heterogeneous weather datasets. | ![GitHub stars](https://img.shields.io/github/stars/microsoft/aurora?style=flat-square) |
| [Perceiver IO](https://github.com/deepmind/deepmind-research/tree/master/perceiver) | DeepMind general-purpose transformer for arbitrary input/output modalities including point clouds and optical flow. | ![GitHub stars](https://img.shields.io/github/stars/google-deepmind/deepmind-research?style=flat-square) |

---

## Research Papers

### Foundational Cross-Domain Transformers

- **An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale (ViT)** (ICLR 2021) - [Paper](https://arxiv.org/abs/2010.11929)
  Demonstrates that pure transformer applied to image patches can match or exceed CNNs on ImageNet when pretrained at scale.

- **Highly accurate protein structure prediction with AlphaFold** (Nature 2021) - [Paper](https://www.nature.com/articles/s41586-021-03819-2)
  DeepMind's landmark Evoformer-based system predicting protein 3D structure from sequence at near-experimental accuracy.

- **Perceiver: General Perception with Iterative Attention** (ICML 2021) - [Paper](https://arxiv.org/abs/2103.03206)
  DeepMind architecture handling arbitrary input modalities (images, audio, point clouds) via cross-attention to a learned latent array.

### Biology & Genomics

- **Biological structure and function emerge from scaling unsupervised learning to 250 million protein sequences (ESM-1b)** (PNAS 2021) - [Paper](https://www.pnas.org/doi/10.1073/pnas.2016239118)
  Shows that protein language models learn structural and functional properties from sequence alone, without structure supervision.

- **Hyena DNA: Long-Range Genomic Sequence Modeling at Single Nucleotide Resolution** (ICML 2023) - [Paper](https://arxiv.org/abs/2306.15794)
  Subquadratic attention-free alternative to transformers for million-token genomic sequences with better length generalization.

- **Evo: DNA foundation model for long-context genomic sequence generation** (Science 2024) - [Paper](https://www.science.org/doi/10.1126/science.ado9336)
  Arc Institute model trained on prokaryotic genomes enabling single-nucleotide-resolution generation and fitness prediction.

### Chemistry & Materials

- **Uni-Mol: A Universal 3D Molecular Representation Learning Framework** (ICLR 2023) - [Paper](https://openreview.net/forum?id=6K2RM6wVqKu)
  Pretrains on 3D molecular conformations for property prediction, binding pose, and drug-target interaction tasks.

- **A generalist neural algorithmic learner (Graphormer)** (NeurIPS 2022) - [Paper](https://arxiv.org/abs/2205.09494)
  Microsoft's graph transformer incorporating degree, spatial, and edge encoding for molecular graph tasks.

### Time-Series & Forecasting

- **Are Transformers Effective for Time Series Forecasting?** (AAAI 2023) - [Paper](https://arxiv.org/abs/2205.13504)
  Critical analysis showing linear models can match transformers on many forecasting benchmarks; spurred better transformer designs.

- **iTransformer: Inverted Transformers Are Effective for Time Series Forecasting** (ICLR 2024) - [Paper](https://arxiv.org/abs/2310.06625)
  Applies attention across variates rather than time steps, achieving state-of-the-art on multivariate forecasting.

- **A decoder-only foundation model for time-series forecasting (TimesFM)** (ICML 2024) - [Paper](https://arxiv.org/abs/2310.10688)
  Google decoder-only transformer pretrained on 100B time-series points enabling zero-shot forecasting.

### Physics & Weather

- **Accurate medium-range global weather forecasting with 3D neural networks (Pangu-Weather)** (Nature 2023) - [Paper](https://www.nature.com/articles/s41586-023-06185-3)
  Huawei 3D Earth transformer outperforming ECMWF's operational model on deterministic medium-range forecasts.

- **Neural General Circulation Models for Weather and Climate** (Nature 2024) - [Paper](https://www.nature.com/articles/s41586-024-07744-y)
  Google DeepMind end-to-end differentiable atmosphere model combining transformers with physical constraints.

---

## Datasets & Benchmarks

*Domain-specific benchmarks for evaluating cross-domain transformers.*

| Benchmark | Description | Link |
|-----------|-------------|------|
| CASP (Critical Assessment of Protein Structure Prediction) | Gold-standard biennial benchmark for protein structure prediction evaluated against experimental data. | [Website](https://predictioncenter.org/) |
| MoleculeNet | Large-scale molecular property prediction benchmark spanning quantum mechanics, biophysics, and physiology. | [Paper](https://arxiv.org/abs/1703.00564) \| [GitHub](https://github.com/deepchem/deepchem) |
| OGB-LSC (Open Graph Benchmark Large Scale Challenge) | Graph-level property prediction at scale; includes PCQM4Mv2 for quantum chemistry. | [Website](https://ogb.stanford.edu/docs/lsc/) |
| Long-Range Arena (LRA) | Benchmark for evaluating efficient transformers on long sequences across modalities (text, images, math). | [Paper](https://arxiv.org/abs/2011.04006) \| [GitHub](https://github.com/google-research/long-range-arena) |
| LOTSA (Large-Scale Open Time Series Archive) | 27B observations across 9 domains used to pretrain universal time-series forecasting transformers. | [Paper](https://arxiv.org/abs/2402.02592) |
| WeatherBench 2 | Comprehensive benchmark for global weather and climate prediction models. | [Paper](https://arxiv.org/abs/2308.15560) \| [GitHub](https://github.com/google-research/weatherbench2) |

---

## Contributing

Contributions are welcome! To add a project or paper, simply [open an issue](../../issues) or submit a PR.

When proposing additions, include a short note on which inclusion criteria the item satisfies and link the strongest supporting evidence (paper/repo/benchmark/blog).

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related rights to this work.
