# Awesome Agentic ML [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

Agentic ML refers to autonomous AI systems that can plan, execute, and iterate on machine learning workflows with minimal human intervention—from data preprocessing to model training, evaluation, and deployment.

🤖 *This resource list is maintained with the help of [Claude](https://www.anthropic.com/claude) by Anthropic.*

---

## Contents

- [Frameworks & Platforms](#frameworks--platforms)
- [AutoML Agents](#automl-agents)
- [Research Papers](#research-papers)
  - [Benchmarks & Evaluation](#benchmarks--evaluation)
  - [Autonomous Data Science Agents](#autonomous-data-science-agents)
  - [Multi-Agent Systems](#multi-agent-systems)
  - [Search & Planning Methods](#search--planning-methods)
  - [Domain-Specific Agentic ML](#domain-specific-agentic-ml)
  - [LLM-Based ML Optimization](#llm-based-ml-optimization)
  - [Surveys](#surveys)
  - [Foundation Models for ML](#foundation-models-for-ml)
- [Datasets & Benchmarks](#datasets--benchmarks)
- [MLE-bench Leaderboard](#mle-bench-leaderboard)
- [Related Resources](#related-resources)
- [Contributing](#contributing)

---

## Frameworks & Platforms

*End-to-end platforms and frameworks for building agentic ML systems.*

| Project | Description | Stars |
|---------|-------------|-------|
| [AlphaEvolve](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/) | Google DeepMind's evolutionary coding agent for scientific and algorithmic discovery using Gemini. | - |
| [AutoGluon](https://github.com/autogluon/autogluon) | Open-source AutoML toolkit by Amazon with foundational models and LLM agents. | ![GitHub stars](https://img.shields.io/github/stars/autogluon/autogluon?style=flat-square) |
| [EvoAgentX](https://github.com/EvoAgentX/EvoAgentX) | Open-source framework for building, evaluating, and evolving LLM-based agentic workflows. EMNLP 2025. | ![GitHub stars](https://img.shields.io/github/stars/EvoAgentX/EvoAgentX?style=flat-square) |
| [Karpathy](https://github.com/K-Dense-AI/karpathy) | Agentic ML Engineer using Claude Code SDK and Google ADK. By K-Dense. | ![GitHub stars](https://img.shields.io/github/stars/K-Dense-AI/karpathy?style=flat-square) |
| [K-Dense Web](https://k-dense.ai/) | Autonomous AI Scientist platform with dual-loop multi-agent system for research, coding, and ML. | - |
| [OpenEvolve](https://github.com/codelion/openevolve) | Open-source implementation of Google DeepMind's AlphaEvolve for evolutionary code optimization. | ![GitHub stars](https://img.shields.io/github/stars/codelion/openevolve?style=flat-square) |

---

## AutoML Agents

*LLM-powered agents for automated machine learning pipelines.*

| Project | Description | Stars |
|---------|-------------|-------|
| [Agent Laboratory](https://github.com/SamuelSchmidgall/AgentLaboratory) | Autonomous research framework with specialized agents for literature review, experimentation, and report writing. | ![GitHub stars](https://img.shields.io/github/stars/SamuelSchmidgall/AgentLaboratory?style=flat-square) |
| [AIDE](https://github.com/WecoAI/aideml) | AI-powered data science agent using tree search for solution exploration. | ![GitHub stars](https://img.shields.io/github/stars/WecoAI/aideml?style=flat-square) |
| [AIRA-dojo](https://github.com/facebookresearch/aira-dojo) | Meta's AI research agents using search policies (Greedy, MCTS, Evolutionary). | ![GitHub stars](https://img.shields.io/github/stars/facebookresearch/aira-dojo?style=flat-square) |
| [AutoGluon Assistant](https://github.com/autogluon/autogluon-assistant) | Multi-agent system for end-to-end multimodal ML automation. Also known as MLZero. | ![GitHub stars](https://img.shields.io/github/stars/autogluon/autogluon-assistant?style=flat-square) |
| [AutoMind](https://github.com/zjunlp/AutoMind) | Adaptive agent with expert knowledge base from 455 Kaggle competitions and tree search. By ZJU NLP. | ![GitHub stars](https://img.shields.io/github/stars/zjunlp/AutoMind?style=flat-square) |
| [AutoML-Agent](https://github.com/DeepAuto-AI/automl-agent) | Multi-Agent LLM Framework for Full-Pipeline AutoML. | ![GitHub stars](https://img.shields.io/github/stars/DeepAuto-AI/automl-agent?style=flat-square) |
| [Data Interpreter](https://github.com/geekan/MetaGPT) | LLM agent for data science using hierarchical graph modeling and programmable node generation. Part of MetaGPT. ICLR 2025. | ![GitHub stars](https://img.shields.io/github/stars/geekan/MetaGPT?style=flat-square) |
| [DS-Agent](https://github.com/guosyjlu/DS-Agent) | Automated data science agent using case-based reasoning from Kaggle. ICML 2024. | ![GitHub stars](https://img.shields.io/github/stars/guosyjlu/DS-Agent?style=flat-square) |
| [FM Agent](https://github.com/baidubce/FM-Agent) | Baidu's foundation model agent for ML engineering tasks. | ![GitHub stars](https://img.shields.io/github/stars/baidubce/FM-Agent?style=flat-square) |
| [InternAgent](https://github.com/Alpha-Innovator/InternAgent) | ML engineering agent with DeepSeek-R1 integration. | ![GitHub stars](https://img.shields.io/github/stars/Alpha-Innovator/InternAgent?style=flat-square) |
| [LADS (LightAutoDS)](https://github.com/sb-ai-lab/LADS) | Multi-AutoML agentic system combining LLM code generation with AutoGluon, LightAutoML, and FEDOT. | ![GitHub stars](https://img.shields.io/github/stars/sb-ai-lab/LADS?style=flat-square) |
| [MLE-STAR](https://research.google/blog/mle-star-a-state-of-the-art-machine-learning-engineering-agents/) | Google's ML engineering agent using web search and targeted code block refinement. Built with ADK. | - |
| [ML-Master](https://github.com/sjtu-sai-agents/ML-Master) | AI-for-AI agent integrating exploration and reasoning with adaptive memory. By SJTU SAI. | ![GitHub stars](https://img.shields.io/github/stars/sjtu-sai-agents/ML-Master?style=flat-square) |
| [OpenHands](https://github.com/All-Hands-AI/OpenHands) | Open-source AI software development agent adaptable to ML tasks. | ![GitHub stars](https://img.shields.io/github/stars/All-Hands-AI/OpenHands?style=flat-square) |
| [R&D-Agent](https://github.com/microsoft/RD-Agent) | Microsoft's research & development agent for ML tasks. | ![GitHub stars](https://img.shields.io/github/stars/microsoft/RD-Agent?style=flat-square) |
| [SELA](https://github.com/geekan/MetaGPT/tree/main/metagpt/ext/sela) | Tree-Search Enhanced LLM Agents for AutoML using MCTS. Part of MetaGPT. | ![GitHub stars](https://img.shields.io/github/stars/geekan/MetaGPT?style=flat-square) |

---

## Research Papers

*Academic papers on agentic ML, autonomous ML systems, and LLM-based ML agents.*

### Benchmarks & Evaluation

*Papers introducing benchmarks and evaluation methodologies for agentic ML systems.*

- **MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering** (2024) - [Paper](https://arxiv.org/abs/2410.07095) | [Code](https://github.com/openai/mle-bench)  
  Benchmark by OpenAI with 75 Kaggle competitions for evaluating ML engineering agents.

- **MLE-Smith: Scaling MLE Tasks with Automated Multi-Agent Pipeline** (2025) - [Paper](https://arxiv.org/abs/2510.07307)  
  Automated pipeline transforming raw datasets into competition-style MLE challenges.

- **MLAgentBench: Evaluating Language Agents on Machine Learning Experimentation** (ICML 2024) - [Paper](https://openreview.net/forum?id=1Fs1LvjYQW)  
  Benchmark for evaluating LLM agents on ML research tasks including model training and debugging.

- **MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research** (2025) - [Paper](https://arxiv.org/abs/2505.19955)  
  Benchmark with 201 research tasks from NeurIPS, ICLR, and ICML. Includes MLR-Judge for automated evaluation.

- **DataSciBench: An LLM Agent Benchmark for Data Science** (2025) - [Paper](https://arxiv.org/abs/2502.13897) | [Code](https://github.com/THUDM/DataSciBench)
  Comprehensive benchmark with Task-Function-Code (TFC) framework for rigorous evaluation of LLMs on data science tasks.

- **LMR-BENCH: Can LLM Agents Reproduce NLP Research?** (EMNLP 2025) - [Paper](https://aclanthology.org/2025.emnlp-main.314/)
  Tasks LLM agents with reproducing functions from NLP research papers. Tests understanding of scientific methods and implementation.

- **DS-1000: A Natural and Reliable Benchmark for Data Science Code Generation** (2022) - [Paper](https://arxiv.org/abs/2211.11501)
  1,000 data science problems from StackOverflow covering NumPy, Pandas, SciPy, Scikit-learn, Matplotlib, PyTorch, and TensorFlow.

- **MLE-Dojo: Interactive RL Environment for Machine Learning Engineering** (2025) - [Paper](https://arxiv.org/abs/2505.07782)
  Transforms MLE-bench into a Gym-style RL environment with 200+ Kaggle competitions, enabling agent training via supervised fine-tuning and reinforcement learning.

### Autonomous Data Science Agents

*LLM agents for end-to-end data science automation with case-based reasoning and knowledge retrieval.*

- **DS-Agent: Automated Data Science by Empowering LLMs with Case-Based Reasoning** (ICML 2024) - [Paper](https://arxiv.org/abs/2402.17453) | [Code](https://github.com/guosyjlu/DS-Agent)
  Two-stage framework (development + deployment) using case-based reasoning from Kaggle. GPT-4 achieves 100% success rate in development stage.

- **Agent Laboratory: Using LLM Agents as Research Assistants** (2025) - [Paper](https://arxiv.org/abs/2501.04227) | [Code](https://github.com/SamuelSchmidgall/AgentLaboratory)
  End-to-end autonomous research framework with specialized agents (PhD, Postdoc, ML Engineer, Professor) for literature review, experimentation, and report writing. 84% cost reduction vs. prior methods.

### Multi-Agent Systems

*Frameworks using multiple specialized agents for end-to-end ML pipelines.*

- **AutoML-Agent: A Multi-Agent LLM Framework for Full-Pipeline AutoML** (ICML 2025) - [Paper](https://openreview.net/forum?id=p1UBWkOvZm) | [Code](https://github.com/DeepAuto-AI/automl-agent)  
  Multi-agent system with data, model, and operation agents for full-pipeline automation.

- **LightAutoDS-Tab: Multi-AutoML Agentic System for Tabular Data** (2025) - [Paper](https://arxiv.org/abs/2507.13413) | [Code](https://github.com/sb-ai-lab/LADS)  
  Combines LLM-based code generation with multiple AutoML tools (AutoGluon, LightAutoML, FEDOT).

- **MLZero: A Multi-Agent System for End-to-end Machine Learning Automation** (NeurIPS 2025) - [Paper](https://arxiv.org/abs/2505.13941) | [Code](https://github.com/autogluon/autogluon-assistant)  
  Transforms raw multimodal data into ML solutions with zero human intervention.

- **SmartDS-Solver: Agentic AI for Vertical Domain Problem Solving in Data Science** (ICLR 2026 Submission) - [Paper](https://openreview.net/forum?id=r7gmePFADZ)
  Reasoning-centric system with SARTE algorithm for data science problem solving.

- **AutoKaggle: A Multi-Agent Framework for Autonomous Data Science Competitions** (2024) - [Paper](https://arxiv.org/abs/2410.20424)
  Multi-agent framework for autonomous Kaggle competitions with 85% valid submission rate. Iterative development with code execution, debugging, and unit testing.

- **The AI Data Scientist** (2025) - [Paper](https://arxiv.org/abs/2508.18113)
  Multi-subagent architecture with six specialized subagents (Data Cleaning, Hypothesis, Preprocessing, Feature Engineering, Model Training, Call-to-Action) for end-to-end workflows.

- **Data Interpreter: An LLM Agent for Data Science** (ICLR 2025) - [Paper](https://arxiv.org/abs/2402.18679) | [Code](https://github.com/geekan/MetaGPT)
  Hierarchical graph modeling with programmable node generation. Outperforms AutoGen on ML benchmarks.

- **MetaAgent: Automatically Constructing Multi-Agent Systems Based on Finite State Machines** (ICML 2025) - [Paper](https://arxiv.org/abs/2507.22606)
  FSM-based framework that auto-generates multi-agent systems with state traceback for self-correction. Matches or exceeds human-designed systems.

### Search & Planning Methods

*Papers using tree search, MCTS, or structured planning for ML workflow optimization.*

- **AI Research Agents for Machine Learning** (2025) - [Paper](https://arxiv.org/abs/2507.02554) | [Code](https://github.com/facebookresearch/aira-dojo)  
  Formalizes AI research agents as search policies with operators. Compares Greedy, MCTS, and Evolutionary strategies.

- **AutoMind: Adaptive Knowledgeable Agent for Automated Data Science** (2025) - [Paper](https://arxiv.org/abs/2506.10974) | [Code](https://github.com/zjunlp/AutoMind)  
  Features curated expert knowledge base from 455 Kaggle competitions, agentic knowledgeable tree search, and self-adaptive coding strategy.

- **I-MCTS: Enhancing Agentic AutoML via Introspective Monte Carlo Tree Search** (2025) - [Paper](https://arxiv.org/abs/2502.14693) | [Code](https://github.com/jokieleung/I-MCTS)  
  Introspective node expansion with hybrid LLM-estimated and actual performance rewards.

- **MLE-STAR: Machine Learning Engineering Agent via Search and Targeted Refinement** (2025) - [Paper](https://arxiv.org/abs/2506.15692) | [Blog](https://research.google/blog/mle-star-a-state-of-the-art-machine-learning-engineering-agents/)  
  Uses web search to retrieve models and targeted code block refinement via ablation studies.

- **ML-Master: Towards AI-for-AI via Integration of Exploration and Reasoning** (2025) - [Paper](https://arxiv.org/abs/2506.16499) | [Code](https://github.com/sjtu-sai-agents/ML-Master)
  Integrates exploration and reasoning with adaptive memory mechanism.

- **ML-Master 2.0: Toward Ultra-Long-Horizon Agentic Science** (2026) - [Paper](https://arxiv.org/abs/2601.10402) | [Code](https://github.com/sjtu-sai-agents/ML-Master)
  Hierarchical Cognitive Caching (HCC) for ultra-long-horizon ML engineering. Achieves 56.44% on MLE-bench via cognitive accumulation across 24-hour runs.

- **PiML: Automated Machine Learning Workflow Optimization using LLM Agents** (AutoML 2025) - [Paper](https://openreview.net/forum?id=Nw1qBpsjZz)
  Persistent iterative framework with adaptive memory and systematic debugging.

- **SELA: Tree-Search Enhanced LLM Agents for Automated Machine Learning** (2024) - [Paper](https://arxiv.org/abs/2410.17238) | [Code](https://github.com/geekan/MetaGPT/tree/main/metagpt/ext/sela)  
  Leverages MCTS to expand the search space with insight pools.

### Domain-Specific Agentic ML

*Agentic systems tailored for specific ML domains.*

- **AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery** (2025) - [Paper](https://arxiv.org/abs/2506.13131) | [Blog](https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/)
  Google DeepMind's evolutionary coding agent pairing Gemini LLMs with automated evaluators. Discovered novel matrix multiplication algorithms and optimizes data center operations.

- **AgenticSciML: Collaborative Multi-Agent Systems for Emergent Discovery in Scientific ML** (2025) - [Paper](https://arxiv.org/abs/2511.07262)
  Specialized agents propose, critique, and refine SciML solutions.

- **AI-Driven Automation Can Become the Foundation of Next-Era Science of Science Research** (NeurIPS 2025 Position) - [Paper](https://openreview.net/forum?id=u0FB996GIH)  
  Position paper on AI automation for scientific discovery with multi-agent systems to simulate research societies.

- **ClimateAgent: Multi-Agent Orchestration for Complex Climate Data Science Workflows** (TMLR) - [Paper](https://openreview.net/forum?id=XLWvXNumGa)  
  Multi-agent framework for end-to-end climate data analytics with dynamic API awareness and self-correction.

- **The AI Cosmologist: Agentic System for Automated Data Analysis** (2025) - [Paper](https://arxiv.org/abs/2504.03424)  
  Automates cosmological data analysis from idea generation to research dissemination.

- **TS-Agent: Structured Agentic Workflows for Financial Time-Series Modeling** (2025) - [Paper](https://arxiv.org/abs/2508.13915)  
  Modular framework for financial forecasting with structured knowledge banks.

### LLM-Based ML Optimization

*Using LLMs for specific ML optimization tasks.*

- **Using Large Language Models for Hyperparameter Optimization** (2023) - [Paper](https://arxiv.org/abs/2312.04528)
  Iterative HPO via LLM prompting. Matches or outperforms Bayesian optimization in limited-budget settings.

- **ML-Agent: Reinforcing LLM Agents for Autonomous Machine Learning Engineering** (2025) - [Paper](https://arxiv.org/abs/2505.23723)
  Applies online reinforcement learning to train LLM agents for ML tasks with exploration-enriched fine-tuning and step-wise RL.

- **CAAFE: Context-Aware Automated Feature Engineering** (NeurIPS 2024) - [Paper](https://arxiv.org/abs/2305.03403)
  LLM-driven automated feature engineering pipeline that generates and executes code for new features using dataset context.

- **LLM-FE: Automated Feature Engineering for Tabular Data with LLMs as Evolutionary Optimizers** (2025) - [Paper](https://arxiv.org/abs/2503.14434) | [Code](https://github.com/nikhilsab/LLMFE)
  Combines evolutionary search with LLM reasoning to discover effective feature transformations. Outperforms CAAFE and other baselines on classification and regression benchmarks.

- **A Human-Centered Automated Machine Learning Agent with LLMs** (2025) - [Paper](https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2025.1680845/full)
  LLM-driven agent enabling natural language interaction throughout the entire ML workflow with adaptive hyperparameter optimization.

### Surveys

*Survey papers covering the agentic ML landscape.*

- **Large Language Models for Constructing and Optimizing Machine Learning Workflows: A Survey** (ACM TOSEM, 2025) - [Paper](https://dl.acm.org/doi/10.1145/3773084)
  First SE-oriented, stage-wise review of LLM-based ML workflow automation covering data/feature engineering, model selection, HPO, and evaluation.

- **Large Language Model-based Data Science Agent: A Survey** (2025) - [Paper](https://arxiv.org/abs/2508.02744)
  Comprehensive survey examining how LLM-agent systems automate end-to-end data science pipelines.

- **A Survey on Large Language Model-based Agents for Statistics and Data Science** (The American Statistician, 2025) - [Paper](https://www.tandfonline.com/doi/full/10.1080/00031305.2025.2561140)
  Overview of evolution, capabilities, and applications of LLM-based data agents for simplifying complex data tasks.

- **Agentic AI for Scientific Discovery: A Survey of Progress, Challenges, and Future Directions** (2025) - [Paper](https://arxiv.org/abs/2503.08979)
  Categorizes agentic systems for scientific discovery into autonomous and collaborative frameworks across chemistry, biology, and materials science.

- **From AI for Science to Agentic Science: A Survey on Autonomous Scientific Discovery** (2025) - [Paper](https://arxiv.org/abs/2508.14111)
  Domain-oriented review unifying process-oriented, autonomy-oriented, and mechanism-oriented perspectives on autonomous scientific discovery.

- **From Automation to Autonomy: A Survey on Large Language Models in Scientific Discovery** (2025) - [Paper](https://arxiv.org/abs/2505.13259)
  Analyzes LLM progression from discrete task-oriented functions to sophisticated multi-stage agentic workflows across six stages of the scientific method.

- **A Comprehensive Survey of Self-Evolving AI Agents** (2025) - [Paper](https://arxiv.org/abs/2508.07407) | [Code](https://github.com/EvoAgentX/Awesome-Self-Evolving-Agents)
  Survey on agent evolution techniques that automatically enhance agent systems, bridging foundation models with continuous adaptability.

### Foundation Models for ML

*Pre-trained models that enable rapid ML development.*

- **TabPFN: A Transformer That Solves Small Tabular Classification Problems in a Second** (ICLR 2023) - [Paper](https://arxiv.org/abs/2207.01848) | [Code](https://github.com/automl/TabPFN)  
  Prior-Data Fitted Network using in-context learning for instant tabular classification.

- **Unlocking the Full Potential of Data Science Requires Tabular Foundation Models, Agents, and Humans** (NeurIPS 2025 Position) - [Paper](https://openreview.net/forum?id=aXMPvmBAm5)  
  Position paper on collaborative systems integrating agents, tabular foundation models, and human experts for data science.

---

## Datasets & Benchmarks

*Benchmarks and datasets for evaluating agentic ML systems.*

| Benchmark | Description | Link |
|-----------|-------------|------|
| AutoML-Agent Benchmark | 18 diverse datasets across tabular, CV, NLP, time-series, and graph tasks. | [Paper](https://openreview.net/forum?id=p1UBWkOvZm) |
| DataSciBench | Comprehensive data science benchmark with TFC framework for LLM evaluation. | [Paper](https://arxiv.org/abs/2502.13897) \| [GitHub](https://github.com/THUDM/DataSciBench) |
| DS-1000 | 1,000 data science code generation problems from StackOverflow across 7 libraries. | [Paper](https://arxiv.org/abs/2211.11501) |
| GAIA | General AI Assistants benchmark testing real-world reasoning and tool use. | [Paper](https://arxiv.org/abs/2311.12983) |
| LMR-BENCH | Benchmark tasking agents with reproducing functions from NLP research papers. | [Paper](https://aclanthology.org/2025.emnlp-main.314/) |
| MLE-bench | Kaggle-based benchmark for ML engineering agents by OpenAI. 75 competitions. | [Paper](https://arxiv.org/abs/2410.07095) \| [GitHub](https://github.com/openai/mle-bench) |
| MLE-Dojo | Gym-style RL environment built on MLE-bench with 200+ Kaggle competitions for agent training. | [Paper](https://arxiv.org/abs/2505.07782) |
| MLE-Smith | Automated pipeline for generating competition-style MLE challenges from raw datasets. | [Paper](https://arxiv.org/abs/2510.07307) |
| MLAgentBench | Benchmark for LLM agents on ML experimentation tasks. | [Paper](https://openreview.net/forum?id=1Fs1LvjYQW) |
| MLR-Bench | Open-ended ML research benchmark with 201 tasks from major ML conferences. | [Paper](https://arxiv.org/abs/2505.19955) |

---

## MLE-bench Leaderboard

*Top-performing agents on [MLE-bench](https://github.com/openai/mle-bench) (75 Kaggle competitions, ICLR 2025 Oral). Scored by "Any Medal %" — percentage of competitions earning at least a bronze medal. Agents run on 36 vCPUs, 440GB RAM, and one 24GB A10 GPU.*

| Rank | Agent | LLM | All (%) | Hours | Date |
|------|-------|-----|---------|-------|------|
| 1 | PiEvolve (Fractal AI) | Gemini-3-Pro-Preview | 61.33 | 24 | Jan 2026 |
| 2 | Famou-Agent 2.0 (Baidu) | Gemini-2.5-Pro | 59.56 | 24 | Dec 2025 |
| 3 | ML-Master 2.0 (SJTU) | DeepSeek-V3.2 | 56.44 | 24 | Dec 2025 |
| 4 | PiEvolve Fast (Fractal AI) | Gemini-3-Pro-Preview | 52.00 | 12 | Jan 2026 |
| 5 | Leeroo | Gemini-3-Pro-Preview | 50.67 | 24 | Dec 2025 |
| 6 | Thesis | gpt-5-codex | 48.44 | 24 | Nov 2025 |
| 7 | CAIR MLE-STAR-Pro-1.5 | Gemini-2.5-Pro | 44.00 | 24 | Nov 2025 |
| 8 | Famou-Agent (Baidu) | Gemini-2.5-Pro | 43.56 | 24 | Oct 2025 |
| 9 | Operand ensemble | gpt-5 + multi-model | 39.56 | 24 | Oct 2025 |
| 10 | CAIR MLE-STAR-Pro-1.0 | Gemini-2.5-Pro | 38.67 | 12 | Nov 2025 |
| 11 | InternAgent | DeepSeek-R1 | 36.44 | 12 | Sep 2025 |
| 12 | R&D-Agent | gpt-5 | 35.11 | 12 | Sep 2025 |
| 13 | Neo multi-agent | Undisclosed | 34.22 | 36 | Jul 2025 |
| 14 | AIRA-dojo (Meta) | o3 | 31.60 | 24 | May 2025 |
| 15 | R&D-Agent | o3 + GPT-4.1 | 30.22 | 24 | Aug 2025 |
| 16 | ML-Master (SJTU) | DeepSeek-R1 | 29.33 | 12 | Jun 2025 |
| 17 | R&D-Agent | o1-preview | 22.40 | 24 | May 2025 |
| 18 | AIDE | o1-preview | 17.12 | 24 | Oct 2024 |
| 19 | AIDE | gpt-4o | 8.63 | 24 | Oct 2024 |
| 20 | OpenHands | gpt-4o | 4.89 | 24 | Oct 2024 |

*Top score improved from 16.9% (Oct 2024) to 61.3% (Jan 2026) — a ~3.6x improvement in 15 months. See [MLE-bench README](https://github.com/openai/mle-bench) for the full leaderboard with per-difficulty breakdowns.*

---

## Related Resources

*Curated reading lists and paper collections on agentic ML.*

| Resource | Description | Stars |
|----------|-------------|-------|
| [LLM4AutoML](https://github.com/t-harden/LLM4AutoML) | Curated list of papers on using LLMs for AutoML. | ![GitHub stars](https://img.shields.io/github/stars/t-harden/LLM4AutoML?style=flat-square) |
| [LLM-Based Data Science Agent Reading List](https://github.com/Stephen-SMJ/Reading-List-of-Large-Language-Model-Based-Data-Science-Agent) | Reading list of papers on LLM-based data science agents. | ![GitHub stars](https://img.shields.io/github/stars/Stephen-SMJ/Reading-List-of-Large-Language-Model-Based-Data-Science-Agent?style=flat-square) |
| [ai-agent-papers](https://github.com/masamasa59/ai-agent-papers) | Biweekly-updated collection of AI agent research papers. | ![GitHub stars](https://img.shields.io/github/stars/masamasa59/ai-agent-papers?style=flat-square) |
| [Awesome-Self-Evolving-Agents](https://github.com/EvoAgentX/Awesome-Self-Evolving-Agents) | Survey and paper list on self-evolving AI agents bridging foundation models and lifelong systems. | ![GitHub stars](https://img.shields.io/github/stars/EvoAgentX/Awesome-Self-Evolving-Agents?style=flat-square) |
| [Awesome-Agent-Papers](https://github.com/luo-junyu/Awesome-Agent-Papers) | Up-to-date survey on LLM agent methodology, applications, and challenges. | ![GitHub stars](https://img.shields.io/github/stars/luo-junyu/Awesome-Agent-Papers?style=flat-square) |

---

## Contributing

Contributions are welcome! To add a project or paper, simply [open an issue](../../issues) or submit a PR.

---

## License

[![CC0](https://licensebuttons.net/p/zero/1.0/88x31.png)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the authors have waived all copyright and related rights to this work.
