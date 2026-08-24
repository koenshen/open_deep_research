# Comprehensive Literature Review: Data Synthesis Methods for Tool-Augmented LLM Agent Training (2025)

## Introduction

The year 2025 has witnessed a surge of research on data synthesis methods for training tool-augmented large language model (LLM) agents, particularly those capable of web search and multi-step reasoning. This review covers eight key works published in 2025, analyzing their motivations, core innovations, empirical setups, and limitations. The papers span a range of approaches—from automated task generation and reinforcement learning frameworks to formalization-driven synthesis and benchmark construction—collectively advancing the frontier of how agents learn to use tools autonomously.

---

## 1. TaskCraft (Shi et al., 2025)

**arXiv:** [2506.10055](https://arxiv.org/abs/2506.10055) | **Venue:** ICLR 2026 | **Code:** [github.com/OPPO-PersonalAI/TaskCraft](https://github.com/OPPO-PersonalAI/TaskCraft)

### 1.1 Motivation and Core Idea

**Motivation:** Existing instruction datasets lack tool interaction, and current agentic benchmarks like GAIA, BrowseComp, and HLE rely on costly human annotation, limiting scalability. There is no scalable way to generate training data for agentic tasks requiring multi-step problem solving, tool use, and adaptive reasoning.

**Core Innovation:** TaskCraft is the first automated workflow for generating scalable, multi-tool, difficulty-scalable, and verifiable agentic tasks with execution trajectories. The approach begins by generating "atomic tasks" solvable with single-tool invocations, then progressively increases complexity through two types of extensions:
- **Depth-based extensions:** Creates sequential, multi-hop dependencies where each step depends on previous outputs.
- **Width-based extensions:** Combines multiple independent sub-problems into compound problems.

Verification uses a two-phase system: (1) rejection sampling for atomic tasks, ensuring tasks genuinely necessitate tool usage, and (2) linguistic analysis with LLMs for extensions to validate superset integrity and prevent information leakage. The workflow uses **bootstrap few-shot learning** to optimize four key prompts, iteratively improving generation pass rates and reducing generation time. The seed corpus consists of 75% web data, 15% image data, and 10% PDF data across multiple domains.

### 1.2 Key Takeaways and Claimed Contributions

- TaskCraft is the first automated workflow for generating scalable, multitool, and verifiable agentic tasks of varying difficulty.
- The generated dataset comprises 41k tool-intensive tasks across varied difficulty levels, including 12.6k tool-interaction trajectories and 5k multi-hop decompositions.
- The workflow supports adaptive difficulty, multi-tool integration, and generation of tasks beyond the capabilities of the task-generation agent.
- Controlled generation ensures inherent access to ground-truth execution trajectories, enabling precise interpretability, reproducibility, and verifiability.
- TaskCraft data substantially improves multi-hop reasoning and agentic capabilities when used for SFT and RL training across multiple LLMs.
- Human evaluation showed 91.7% linguistic fluency and 95.0% accuracy for atomic tasks, and 82.3% extended validity for depth-based extensions.

### 1.3 Empirical Setup

**Prompt Optimization Results:**
- Bootstrap few-shot prompt optimization improved atomic task pass rate from 54.9% to 68.1%.
- Depth-wise extension pass rate improved from 41.0% to 51.2%.
- Generation time reduced by 19.2%.
- Compared to direct LLM prompting, TaskCraft achieved a 24.5% higher pass rate (43.0% vs. 18.5%) while reducing generation time by 28 seconds (86.7s vs. 119.7s).

**Supervised Fine-Tuning (SFT) Results:**
- **Models used:** Qwen2.5-3B-Base and Qwen2.5-3B-Instruct
- **Benchmarks:** HotpotQA, Musique, Bamboogle
- Qwen2.5-3B-Base: +14.0% average improvement over the base workflow.
- Qwen2.5-3B-Instruct: +6.0% average improvement over the base workflow.
- Up to +19.2% on Bamboogle when SFT combined with Search-R1 reinforcement learning.

**GAIA Benchmark Results (with RL training):**
- Baseline (MHQA data): 38.8%
- With 2.5k TaskCraft tasks + RL: 60.2% (+21.4)
- With 8k TaskCraft tasks + RL: 60.8% (+22.0), achieving state-of-the-art among TIR models.

**WebWalker Results:**
- Qwen-2.5-7B-Instruct trained with TaskCraft exceeded the previous best, including the much larger QWQ-32B.

**No explicit compute budget or training hyperparameters reported.**

### 1.4 Limitations and Failure Modes

No specific limitations or failure modes were explicitly reported in the available sources. The paper focuses on methodology and demonstrated effectiveness. The workflow's ability to generate tasks exceeding the generation agent's capabilities is noted as a feature rather than a limitation.

---

## 2. Beyond Ten Turns / ASearcher (Gao et al., 2025)

**arXiv:** [2508.07976](https://arxiv.org/abs/2508.07976) | **Venue:** NeurIPS 2025 | **Code:** [github.com/inclusionAI/ASearcher](https://github.com/inclusionAI/ASearcher)

### 2.1 Motivation and Core Idea

**Motivation:** The paper introduces **ASearcher**, an open-source project for large-scale reinforcement learning training of search agents. Two key obstacles are identified: (1) insufficient search turn limits (≤10 turns) in existing online RL methods, which restrict complex strategy learning, and (2) a lack of large-scale, high-quality QA pairs for training.

**Core Innovation 1 – Scalable Fully Asynchronous RL Training:**
- Uses a fully asynchronous training paradigm (built on AReaL) that decouples trajectory execution from model updates, allowing relaxed turn limits (up to 128 turns per trajectory) without sacrificing training efficiency.
- This eliminates waiting bottlenecks and achieves near-full GPU utilization.
- Enables extreme long-horizon search: tool calls exceeding 40 turns and output tokens exceeding 150k during training (later versions report exceeding 100 tool calls and 400k output tokens).

**Core Innovation 2 – Prompt-based QA Synthesis Agent:**
- An LLM-based agent autonomously generates challenging QA pairs by iteratively modifying seed questions through two operations: **"Injection"** (adding related facts to increase complexity) and **"Fuzzing"** (blurring/obscuring key details to make questions harder).
- Multi-stage validation ensures quality.
- From 14,000 seed QAs, the system generates 134,000 high-quality samples, with 25,600 requiring external tools.

**Agent Design:** Simple two-tool setup (search engine + web browser) with webpage summarization. Two instantiations: base LLMs (Qwen2.5-7B/14B) and advanced LRMs (QwQ-32B). Training uses GRPO with sparse rewards and dynamic filtering, with a two-stage curriculum training where the second stage requires at least 5 tool calls to activate long-horizon capabilities.

### 2.2 Key Takeaways and Claimed Contributions

- ASearcher is a large-scale open-source online agentic RL pipeline for LRM-based and LLM-based search agents.
- The fully asynchronous system avoids long trajectories from blocking training by decoupling trajectory execution from model updates.
- The agent exhibits emergent expert-level search behaviors: uncertainty-aware reasoning, precise key information extraction, cross-document inference, and grounded verification.
- The 14B model surpasses larger 32B baselines.
- Zero-shot transfer from local to web-based search is demonstrated.
- With test-time scaling (K=16 trials) and external summarization tools (DeepSeek-V3), ASearcher approaches commercial systems like Kimi-Researcher, OpenAI DeepResearch, and OpenAI o3.

### 2.3 Empirical Setup

**Results for ASearcher-Local (base LLMs):**
- ASearcher-Local-14B achieves Avg F1 of 60.0 and LasJ of 65.6, surpassing even larger 32B models.

**ASearcher-Web-QwQ Results:**

| Metric | Value |
|--------|-------|
| GAIA Avg@4 | 52.8 (v1), 58.7 (v2/v4) |
| GAIA Pass@4 | 70.1 (v1), 74.7 (v2) |
| xBench-DeepSearch Avg@4 | 42.1 (v1), 51.1 (v2/v4) |
| xBench-DeepSearch Pass@4 | 68.0 (v1), 75.0 (v2) |
| Frames Avg@4 | 74.5 |
| Frames Pass@4 | 85.5 |

**RL Training Improvements (over pre-RL baselines):**
- xBench-DeepSearch: +46.7% (v1), +78.0% (v4)
- GAIA: +20.8% (v1), +34.3% (v4)
- Frames: +14.6 Avg@4

**Baselines compared against:** Existing open-source 32B agents (specific names not enumerated in available sources). **Training data:** 35k curated samples from filtered open-source datasets (HotpotQA, 2WikiMultiHopQA, WebWalkerQA) plus synthetic QA pairs. **No specific compute budget reported.**

### 2.4 Limitations and Failure Modes

No specific limitations or failure modes for ASearcher were explicitly reported in the available sources. The paper is focused on introducing the methodology and demonstrating its effectiveness. The open-source nature of the project is highlighted as enabling further research.

---

## 3. DeepDive (Lu et al., 2025)

**arXiv:** [2509.10446](https://arxiv.org/abs/2509.10446) | **Code:** [github.com/THUDM/DeepDive](https://github.com/THUDM/DeepDive)

### 3.1 Motivation and Core Idea

**Motivation:** DeepDive addresses the gap between open-source LLMs and proprietary models like OpenAI DeepResearch in deep search tasks. Two key challenges are identified: (1) the lack of sufficiently difficult training data for deep search, and (2) the absence of effective multi-turn RL training for long-horizon reasoning with web browsing.

**Core Innovation 1 – Automated Data Synthesis from Knowledge Graphs:**
- Generates complex, multi-hop QA pairs by performing random walks (5-9 steps, k > 5) on open knowledge graphs (KILT, AMiner).
- Starting from node v₀, the agent navigates k steps to form paths, then deliberately obscures entity attributes (dates, names, locations) to create "blurry entities" requiring deep search/disambiguation.
- Uses a difficulty filter: a frontier model (GPT-4o) attempts each question 4 times; only questions that fail in all 4 attempts are retained.
- Produced 3,250 deep search QA pairs total (1,016 for SFT, 2,234 for RL).

**Core Innovation 2 – End-to-End Multi-Turn Reinforcement Learning:**
- Uses Multi-Turn GRPO with normalized advantages.
- The agent iteratively reasons, executes search/click/open actions, and observes web content.
- **Strict binary reward:** +1 only if format is correct AND answer matches ground truth exactly.
- **Early exit mechanism:** Terminates trajectories on format errors with 0 reward.
- **Cold-start phase:** Uses Claude-4-Sonnet-Thinking as teacher model to generate initial SFT trajectories (858 search traces via reject sampling).
- v2 of the paper adds a **redundancy penalty** (Jaccard similarity) to discourage repeated similar queries.

**Training Details:** Backbone models: GLM-Z1-9B-0414 and QwQ-32B. Teacher model: Claude-4-Sonnet-Thinking. Tools: Serper API (search), Jina API (click/open). RL rollout size: 8. Max context length: 50k. Temperature: 1.0. KL penalty: β=0. RL framework: Slime (based on GRPO).

### 3.2 Key Takeaways and Claimed Contributions

- DeepDive presents an automated approach for training deep search agents that can navigate complex, multi-step information-seeking tasks.
- An automated method to synthesize complex, difficult, and hard-to-find questions from open knowledge graphs.
- Multi-turn RL training improves deep search ability and significantly contributes to performance improvements across multiple benchmarks.
- DeepDive-32B achieves a new open-source competitive result on BrowseComp, outperforming WebSailor, DeepSeek-R1-Browse, and Search-o1.
- DeepDive enables test-time scaling of tool calls and parallel sampling, increasing efficiency.
- Skills learned in solving complex problems transfer to simpler scenarios (HotpotQA, Frames, WebWalker).

### 3.3 Empirical Setup

**Main Results:**

| Benchmark | DeepDive-9B | DeepDive-32B | Previous Best Open | DeepResearch (Proprietary) |
|-----------|-------------|-------------|-------------------|---------------------------|
| BrowseComp | 6.3% | 14.8% (v1), 15.3% (v2) | 10.5% (WebSailor-32B) | 51.5% |
| BrowseComp-ZH | 15.1% | 25.6% | 25.5% (WebSailor-32B) | 42.9% |
| Xbench-DeepSearch | 38.0% | 50.5% | 53.3% (WebSailor-32B) | - |
| SEAL-0 | 12.2% | 29.3% | - | - |

**Additional Results:**
- DeepDive-32B achieves >60 points on WebWalker, surpassing WebShaper-72B (52.2).
- Outperforms all open-source competitors on BrowseComp.

**Semi-Automated i.i.d. Data Results:**
- A human-in-the-loop framework produces 2,997 English + 275 Chinese QA pairs.
- With this data, DeepDive-32B reaches 22.2% on BrowseComp (a 40% improvement over KG-only 14.8%).
- Contamination analysis shows <3.4% contamination rate.

**Test-Time Scaling:**
- Tool Call Scaling: Accuracy rises from 8% at 8 tool calls to 15% at 128 tool calls on BrowseComp.
- Parallel Sampling: Selecting the answer with the fewest tool calls among 8 samples raises accuracy from 12.0% to 24.8% on BrowseComp-266.
- RL training increases average tool calls by ~30% (from 35 to 45 during evaluation).

### 3.4 Limitations and Failure Modes

- **Generated data difficulty gap:** The difficulty of synthetic data remains lower than real benchmarks like BrowseComp, leading to performance below advanced models like o3.
- **"Over-search" behavior:** The high-difficulty training focus can cause the model to search too much even when unnecessary.
- **Optimal training steps:** Determining the optimal training steps and designing a more appropriate reward mechanism for the RL stage is identified as an important future direction.
- **Performance ceiling:** The model still lags significantly behind proprietary models like OpenAI DeepResearch (51.5% vs. 14.8% on BrowseComp).

---

## 4. WebThinker (Li et al., 2025)

**arXiv:** [2504.21776](https://arxiv.org/abs/2504.21776) | **Venue:** NeurIPS 2025 | **Code:** [github.com/RUC-NLPIR/WebThinker](https://github.com/RUC-NLPIR/WebThinker)

### 4.1 Motivation and Core Idea

**Motivation:** Large Reasoning Models (LRMs) like OpenAI-o1 and DeepSeek-R1 excel at complex reasoning tasks but are limited by their reliance on static, pre-trained internal knowledge. They struggle with knowledge-intensive tasks requiring up-to-date, comprehensive external information. Existing RAG approaches use predefined workflows that result in "shallow search," preventing deep web exploration and multi-step reasoning.

**Core Innovation:** WebThinker is a deep research agent that empowers LRMs to autonomously search the web, navigate web pages, and draft research reports during the reasoning process. The system operates on a continuous belief-updating loop grounded in Bayesian principles (Posterior and Likelihood). It employs a structured **"Think-Search-and-Draft"** strategy where a main LRM orchestrates high-level reasoning while an assistant LLM executes detailed writing tasks.

**Key Components:**
1. **Deep Web Explorer Module:** Enables LRMs to dynamically search, navigate, and extract information from the web when encountering knowledge gaps, including clicking links and diving deeper into pages.
2. **Autonomous Think-Search-and-Draft Strategy:** Enables seamless interleaving of reasoning, information gathering, and report writing in real time, managed by an assistant LLM with specialized tools (`write_section`, `check_article`, `edit_article`).
3. **RL-based Training via Iterative Online Direct Preference Optimization (DPO):** Enhances tool utilization by sampling multiple reasoning trajectories, determining preferences based on correctness and information coverage, and iteratively refining the model.

**Two Operating Modes:** Problem-Solving Mode (LRM invokes Deep Web Explorer via search tool calls) and Report Generation Mode (integrates report writing tools for composing comprehensive research reports).

### 4.2 Key Takeaways and Claimed Contributions

- WebThinker bridges the gap between advanced reasoning and real-world information access.
- Open-source deep research capabilities.
- Introduces autonomous tool orchestration (dynamic vs. predefined), hierarchical information processing, real-time integration of gathering/reasoning/writing, and preference-based optimization for tool use.
- WebThinker-32B-RL achieves new state-of-the-art results among 32B models, outperforming both retrieval-augmented and proprietary systems like GPT-4o and DeepSeek-R1-671B.
- Surpasses Search-o1 by 21.9% on GAIA and 36.2% on HLE.
- Outperforms Grok3 and Gemini2.0 on report generation tasks.
- Ablation studies confirm the critical role of link clicking, the Think-Search-and-Draft strategy, and RL training.

### 4.3 Empirical Setup

**Backbone Models:** QwQ-32B and DeepSeek-R1 series (7B, 14B, 32B). Uses Bing Web Search API, Crawl4AI for web crawling, and an assistant LLM (Qwen2.5-Instruct) for tool execution.

**Evaluation Benchmarks:** GPQA, GAIA, WebWalkerQA, HLE (complex reasoning); Glaive dataset (scientific report generation).

**Baselines:** Search-o1, RAG baselines, GPT-4o, DeepSeek-R1-671B, o3-mini (High), Grok3 DeeperSearch, Gemini2.0 Deep Research.

**Reported Metrics:**

**Complex Problem-Solving:**
- WebThinker-32B-RL: 70.7% on GPQA, 15.8% on HLE (gains up to +21.5% over baselines).
- On HLE, surpasses o3-mini (High).
- WebThinker-32B-Base outperforms Search-o1 with 22.9% improvement on WebWalkerQA and 20.4% on HLE.
- RL-trained version improves over Base: +8.5% on GAIA, +21.5% on HLE.
- WebThinker surpasses Search-o1 by 21.9% on GAIA and 36.2% on HLE.

**Smaller Backbone Results:**
- With DeepSeek-R1-7B: relative gains of 174.4% on GAIA and 422.6% on WebWalkerQA compared to direct generation.
- 82.9% on GAIA and 161.3% on WebWalkerQA over standard RAG.

**Scientific Report Generation:**
- WebThinker achieves highest overall score of 8.0, surpassing Gemini-Deep Research (7.9).
- On Glaive dataset, outperforms Gemini2.0 Deep Research and Grok3 DeeperSearch, scoring 8.1 in average quality metrics.

**Training Configuration:** RL-based training via iterative online Direct Preference Optimization (DPO). **Specific compute budget not reported.**

### 4.4 Limitations and Failure Modes

- Multimodal capabilities not yet supported.
- Limited to DeepSeek-R1 architecture (and QwQ-32B).
- Reliance on strong base models (requires capable LRMs as backbone).
- Cost of iterative training (RL-based DPO requires multiple reasoning trajectory samples).
- Challenges with complex web pages (navigation may fail on dynamically rendered or complex sites).
- Potential for error propagation from web search results.
- Risks of misinformation, bias amplification, and need for verification mechanisms.
- Limited tool scalability (constrained to current set of search, navigation, and drafting tools).

---

## 5. WebShaper (Tao et al., 2025)

**arXiv:** [2507.15061](https://arxiv.org/abs/2507.15061) | **Venue:** ICLR 2026 | **Dataset:** [huggingface.co/datasets/Alibaba-NLP/WebShaper](https://huggingface.co/datasets/Alibaba-NLP/WebShaper)

### 5.1 Motivation and Core Idea

**Motivation:** Current LLM-powered information-seeking (IS) agents rely on task-specific trajectories for SFT and RL training. Manual construction is complex and unscalable. Existing automated "information-driven" approaches suffer from: (1) inconsistency between information structure and reasoning structure, (2) redundancy and limited diversity due to disordered information retrieval.

**Core Innovation:** WebShaper introduces a **formalization-driven** paradigm shift for synthesizing training data. Unlike existing "information-driven" methods that first collect web data and then generate questions, WebShaper formalizes IS tasks using set-theoretic constructs and systematically guides data generation from formalization.

**Formalization Core:** Set-theoretic constructs with three concepts:
1. **Entities and Relations** (universal set E, relation subspace R)
2. **Knowledge Projection (KP):** The fundamental unit representing entities related to a set via a relation
3. **KP Operations:** Compositions (R-Union and Intersection) enabling precise control over reasoning structure

**Data Synthesis Pipeline (3 stages):**
1. **Seed Question Construction:** Offline Wikipedia with hyperlinks; 18,000 seed questions generated and filtered for correctness.
2. **Agentic Expansion:** Iterative layer-wise expansion using an Expander Agent with ReAct framework and three tools: `Search`, `Summarize`, `Validate`. The layer-wise strategy treats formalized questions as graphs, systematically adding complexity at leaf constants (avoiding redundancy and reasoning shortcuts).
3. **Trajectory Construction & Filtering:** QwQ-based agent framework; yields 5,000 high-quality trajectories after correctness validation and quality checks.

**Computational Cost:** ~20 LLM completions, 6 searches, 7 minutes per example—justified by quality gains.

### 5.2 Key Takeaways and Claimed Contributions

- WebShaper achieves state-of-the-art performance among all open-source IS agents on GAIA and WebWalkerQA benchmarks.
- Currently the only open-source method with a score of more than 60 points on GAIA, approaching OpenAI Deep Research (67.4%).
- Establishes a mathematical (set-theoretic) foundation for information-seeking task generation.
- Enables scalable, controllable data generation for complex reasoning tasks.
- The formalization-driven paradigm shifts the focus from reactive information organization to proactive task specification.

### 5.3 Empirical Setup

**Backbone Models:** Qwen-2.5-32B, Qwen-2.5-72B, QwQ-32B. WebShaper-72B (Qwen-2.5-72B backbone). QwQ-based agent framework for trajectory construction.

**Training Configuration:** 5,000 high-quality trajectories for SFT and RL training. RL training uses GRPO. RL yields significant improvements: +7.8 for 32B, +13.5 for 72B on GAIA (some sources cite +8.8 to +14.5 points). **Specific compute budget not reported.**

**Evaluation Benchmarks:** GAIA (main), WebWalkerQA.

**Baselines:** WebDancer, WebThinker, Search-o1, WebSailor (overall IS agent comparison). SFT data baselines: WebWalkerQA, E2HQA, MHQA (data quality comparison).

**Reported Metrics:**

**GAIA Benchmark:**
- WebShaper-72B: 60.1% Pass@1 (some sources cite 60.19), state-of-the-art among open-source IS agents.
- WebShaper-72B (Qwen-2.5-72B): 52.4% (pre-RL), 60.1% (after RL).
- WebShaper-32B: 47.9% (pre-RL), 55.7% (after RL).

**WebWalkerQA:**
- WebShaper achieves 52.2% (some sources cite 52.50), highest among open-sourced methods.

**Ablation Results:**
- Formalization-language (FL) based synthesis consistently outperforms natural language (NL) based synthesis across all backbone models.
- Layer-wise expansion outperforms sequential and random structures.
- Generated tasks require significantly more search and visit operations vs. baselines.

**Dataset Characteristics:** Balanced domain coverage: Sports 21%, Academic 17%, Politics 15%, Entertainment 13%, Literature 12%, Culture 8%. 500 question-answer pairs released.

### 5.4 Limitations and Failure Modes

- Computationally intensive (~20 LLM completions, 6 searches, 7 minutes per example), though justified by quality gains.
- Additional limitations not explicitly detailed in the available sources.

---

## 6. WebWalkerQA (Wu et al., 2025)

**arXiv:** [2501.07572](https://arxiv.org/abs/2501.07572) | **Venue:** ACL 2025 | **Code:** [github.com/Alibaba-NLP/WebAgent](https://github.com/Alibaba-NLP/WebAgent)

**Important Note:** WebWalkerQA is primarily a benchmark, not a data synthesis method per se. However, the dataset and framework are used by other works (e.g., WebShaper, WebDancer) as training data sources and evaluation benchmarks.

### 6.1 Motivation and Core Idea

**Motivation:** Traditional search engines and RAG systems retrieve surface-level content ("horizontal search") but struggle with tasks requiring deep, multi-step navigation within websites to extract information buried in subpages ("vertical exploration"). Existing benchmarks do not adequately evaluate LLMs' ability to systematically traverse websites.

**Core Innovation:** The paper introduces WebWalkerQA, a benchmark designed to assess the ability of LLMs to perform web traversal—systematically navigating a website's subpages to extract high-quality data. The dataset spans 1,373 webpages across four domains (conference, organization, education, game) and two languages (Chinese 60.5%, English 39.5%). It includes both single-source and multi-source questions at three difficulty levels (easy, medium, hard).

The authors also propose **WebWalker**, a multi-agent framework that mimics human-like web navigation through an explore-critic paradigm:
- **Explorer Agent:** Navigates subpages via a Thought-Action-Observation loop (ReAct-style)
- **Critic Agent:** Manages memory and assesses information relevance, generating responses

### 6.2 Key Takeaways and Claimed Contributions

- WebWalkerQA is a challenging benchmark for evaluating LLMs' web traversal capabilities.
- Even the best-performing system (GPT-4o + WebWalker) achieves under 40% accuracy.
- Combining RAG (horizontal search) with WebWalker (vertical exploration) improves performance across all difficulty levels.
- Scaling the number of exploration actions (K up to 25) improves performance, suggesting vertical exploration is a promising direction for scaling inference-time computation.
- WebWalker can be a module in agentic RAG systems, enabling vertical exploration.

### 6.3 Empirical Setup

**Models Tested:** Closed-source: GPT-4o, Qwen-Plus. Open-source: Qwen2.5 series (7B–72B). Commercial RAG systems: Tongyi (best at 40.73%).

**Evaluation:** WebWalkerQA itself (680 query-answer pairs). Comparisons against ReAct and Reflexion baselines.

**Reported Metrics:**
- Even with GPT-4o, WebWalker achieves only 37.50% overall accuracy.
- Best commercial RAG system (Tongyi): 40.73%.
- Naive RAG: 20.73%.
- Closed-book LLMs: Gemini-1.5-Pro at 8.08%.
- WebWalker consistently outperforms ReAct and Reflexion.

**As a training data source for other methods:**
- WebWalkerQA is used as a training data benchmark by WebShaper, WebDancer, WebExplorer.
- WebShaper achieves 52.2% on WebWalkerQA (highest among open-sourced methods).
- WebExplorer-8B achieves 62.7% on WebWalkerQA.

### 6.4 Limitations and Failure Modes

- RAG systems struggle with tasks requiring deep web traversal.
- Even the largest models tested show suboptimal performance on the benchmark.
- The benchmark is limited to four domains and two languages.
- The paper focuses on benchmarking, and the framework is primarily an evaluation methodology rather than a full training data synthesis pipeline.

---

## 7. Search-R1 (Jin et al., 2025)

**arXiv:** [2503.09516](https://arxiv.org/abs/2503.09516) | **Venue:** COLM 2025 | **Code:** [github.com/PeterGriffinJin/Search-R1](https://github.com/PeterGriffinJin/Search-R1)

**Note on Authorship:** The available paper lists Bowen Jin et al. as authors, not Li et al. as cited in the research brief. This may reflect a different Search-R1 paper or a citation error in the brief.

### 7.1 Motivation and Core Idea

**Motivation:** LLMs are constrained by static, pre-trained knowledge and cannot adapt to real-time information. Traditional RAG approaches rely on single-shot retrieval, insufficient for multi-hop reasoning. Tool-augmented LLMs are rigid, require costly supervised data, and fail to generalize. Prompting advanced LLMs with reasoning capabilities to use search engines during inference is often suboptimal.

**Core Innovation:** Search-R1 is a reinforcement learning framework that extends DeepSeek-R1 to enable LLMs to autonomously generate search queries during step-by-step reasoning with real-time retrieval. The core innovation is treating search as an intrinsic part of the reasoning process via a continuous loop (Reason → Search → Retrieve & Analyze → Iterate → Answer → Learn). The search engine is modeled as part of the environment, supporting interleaved multi-turn reasoning and retrieval using special tokens (<search>, </search>, <information>, </information>). The model learns entirely through RL without requiring large-scale supervised training data.

**Key Technical Innovations:**
1. **RL with Search Engine:** Models the search engine as part of the environment, using retrieved token masking to stabilize RL training. Compatible with PPO and GRPO.
2. **Multi-Turn Interleaved Reasoning & Search:** LLMs alternate between reasoning and search calls, with results enclosed in <information> tokens.
3. **Retrieved Token Masking (Loss Masking):** Ensures stable RL training by excluding retrieved content from policy gradient optimization—policy gradients only computed over LLM-generated tokens.
4. **Simple Outcome-Based Reward Function:** Uses exact match (EM) as reward based solely on whether the final answer is correct, avoiding complex process-based rewards.
5. **Formalization:** Search-as-Reasoning Loop formalized as πθ(· | x; R) = πθ(· | x) ⊗ R.

### 7.2 Key Takeaways and Claimed Contributions

- First RL framework that enables LLMs to search, reason, and answer autonomously without relying on labeled datasets or pre-designed templates.
- Demonstrates that complex multi-turn reasoning and search behaviors can emerge from simple binary feedback signals.
- Provides empirical insights into RL optimization methods, LLM choices, and response length dynamics.
- Open-source code, model checkpoints, and data available.
- Works on both base and instruct variants of Qwen and LLaMA, showing general applicability.

### 7.3 Empirical Setup

**Models Used:** Qwen2.5-7B, Qwen2.5-3B, LLaMA3.2-3B (both base and instruction-tuned variants).

**Training Configurations:** RL Algorithms: PPO and GRPO. PPO offers greater training stability; GRPO converges faster but can lead to reward collapse. Retrieval: 2018 Wikipedia dump, 3 retrieved passages per query. Response length dynamics: initial reduction (eliminating filler words), then increased search usage and reward improvement, stabilization at ~500 tokens. Loss masking is essential: without it, average EM drops from 0.305 to 0.147. **Specific compute budget not reported.**

**Baselines:** Various RAG baselines (ReAct, IRCoT, Search-o1, SFT-based methods, R1—RL without search).

**Evaluation Benchmarks:** NQ, TriviaQA, PopQA, HotpotQA, 2WikiMultiHopQA, Musique, Bamboogle.

**Reported Metrics:**
- **26% average relative improvement** over SOTA baselines with Qwen2.5-7B.
- **21% average relative improvement** with Qwen2.5-3B.
- **10% average relative improvement** with LLaMA3.2-3B.
- Search-R1-base (Qwen2.5-7B): 0.373 avg. EM.
- Search-R1-instruct (Qwen2.5-7B): 0.384 avg. EM.
- With loss masking: 0.431 avg. EM for Qwen2.5-7B-base.
- Without masking: 0.343 (or 0.147 in different ablation) avg. EM.
- **Per-dataset breakdowns not explicitly reported in gathered sources.**

### 7.4 Limitations and Failure Modes

- Current focus on textual QA with a single search tool.
- GRPO can lead to reward collapse after training for many steps (e.g., on LLaMA3.2-3B-Instruct).
- The exact match (EM) reward function captures only 15.8% of human judgment (noted by a subsequent paper).
- Requires RL training which is computationally intensive; no specific compute budget reported.
- Only tested on Wikipedia-based retrieval (2018 dump), not on live web search in the original paper.
- The model's search behavior is limited to a single search engine/tool.

---

## 8. AutoCoA (Zhang et al., 2025)

**arXiv:** [2503.06580](https://arxiv.org/abs/2503.06580) | **Code:** [github.com/ADaM-BJTU/AutoCoA](https://github.com/ADaM-BJTU/AutoCoA)

### 8.1 Motivation and Core Idea

**Motivation:** The paper argues that just as reasoning models internalized Chain-of-Thought (CoT) generation, agent models should internalize Chain-of-Action (CoA) generation to autonomously decide when and how to use external tools. Traditional agentic workflows rely on external prompts or scripts, limiting autonomy. Two core challenges: (1) balancing reasoning and action (preventing reasoning capability forgetting), and (2) managing costly, dynamic real-environment interactions.

**Core Innovation:** The paper introduces the concept of **Large Agent Models (LAMs)** and the **AutoCoA (Automatic Chain-of-Action) framework** for internalizing CoA generation into reasoning models. An Agent Model is defined as a generative model built upon a reasoning model, enhanced through end-to-end task-oriented tool-augmented training, producing sequences of interleaved reasoning (CoT) and action (CoA) steps. The switching between thought and action is based on the model's inherent behaviors, where the model "actively" decides when and how to take action.

**AutoCoA Framework consists of two phases with sub-stages:**

1. **Supervised Fine-Tuning (SFT) Phase:**
   - **SFT Stage 1 (CoT+A):** Step-level action triggering via contrastive learning to teach *when* to act.
   - **SFT Stage 2 (CoT+CoA w/ observation mask):** Trajectory-level learning of *how* to act (excluding environment feedback from loss).
   - **SFT Stage 3 (CoT+CoA w/o observation mask):** Includes environment response prediction, effectively learning an internal world model.

2. **Reinforcement Learning (RL) Phase:**
   - **RL Stage 1 (simulated environment):** Uses the internal world model for extensive low-cost exploration, reducing real-environment interaction costs.
   - **RL Stage 2 (real environment):** Interacts with actual tools (e.g., web search) to adapt to real-world dynamics.

**Key Technical Innovations:** Separating *when-to-act* and *how-to-act* training stages; step-level action triggering via contrastive learning; trajectory-level CoA optimization; internal world model to reduce real-environment interaction costs; uses GRPO with rewards based on exact output matching and format coherence.

### 8.2 Key Takeaways and Claimed Contributions

- Defines the concept of Large Agent Models (LAMs) that internalize CoA generation.
- Proposes the AutoCoA framework combining SFT and RL for training agent models.
- Demonstrates that internalizing CoA generation substantially improves task completion rates compared to agentic workflows.
- Shows that simulated environment training with limited real interactions (1/6 of total training) achieves competitive results while reducing costs.
- Provides an agent roadmap covering short-term and mid-term applications.
- AutoCoA trained from reasoning LLMs exhibits longer reasoning processes, more frequent incorporation of own knowledge, and appropriate tool usage.
- Agent models maintain high accuracy even with 5+ action steps, unlike workflow-based models which show declining success rates.

### 8.3 Empirical Setup

**Models Used:** R1-Distill-Qwen-7B as the base reasoning model.

**Training Configurations:** SFT includes CoT+A substage (contrastive loss) and CoT+CoA stages (with/without observation masks). RL uses GRPO with rewards based on exact output matching and format coherence. Simulated environment (RL-stage1) uses internal world model. Real environment (RL-stage2) interacts with actual tools. **Specific compute budget not reported.**

**Baselines:** ReAct-based agentic workflows using the same base model (R1-Distill-Qwen-7B with ReAct prompting). Various AutoCoA variants compared against each other.

**Evaluation Benchmarks:** NQ, TriviaQA, HotpotQA, 2WikiMultihopQA, MuSiQue, Bamboogle.

**Reported Metrics:**

| Configuration | EM | LLM Average Accuracy |
|---------------|-----|----------------------|
| Initial policy with ReAct workflow | 15.2% | 18.5% |
| **Best AutoCoA (SFT-stage1&2 + RL-stage2)** | **33.9%** | **38.5%** |

- All AutoCoA variants substantially outperform the initial policy model with the ReAct workflow.
- Agent models maintain relatively high accuracy even at 5+ action steps, while ReAct-based workflows show declining success rates.
- Separating when-to-act and how-to-act training stages improves performance.
- Simulated environment training with limited real interactions (1/6 of total training) achieves competitive results.
- **Per-dataset breakdowns not reported in gathered sources.**

### 8.4 Limitations and Failure Modes

- Methodologically, this report represents an initial exploration into learning CoA.
- The approach focuses on open-domain QA tasks with a single tool (web search).
- The gap between AutoCoA performance (33.9% EM) and potential human-level performance is still large.
- The paper does not evaluate on more complex agentic benchmarks beyond QA (e.g., web browsing, API calling, code execution).
- No comparison with other agent frameworks beyond ReAct-based workflows.
- The internal world model may have fidelity limitations as it's an LLM-based simulation.
- Scaling to larger models (beyond 7B parameters) not explored.
- Per-dataset breakdowns of results not provided.

---

## Summary and Comparative Analysis

The eight papers reviewed represent a diverse set of approaches to data synthesis for tool-augmented LLM agent training, with several common themes and notable differences.

### Common Themes

**Reinforcement Learning Dominance:** Virtually all papers employ RL as a key component of their training pipeline. GRPO is the most widely used algorithm (employed by Beyond Ten Turns, DeepDive, WebShaper, Search-R1, and AutoCoA), with DPO used by WebThinker and PPO by Search-R1 as an alternative.

**Automated Data Generation:** All papers propose some form of automated or semi-automated data synthesis to reduce reliance on human annotation. Approaches range from knowledge graph walks (DeepDive) and formalization-driven synthesis (WebShaper) to prompt-based QA synthesis (Beyond Ten Turns) and bootstrapped task generation (TaskCraft).

**Focus on Multi-Hop and Long-Horizon Tasks:** The papers consistently target complex, multi-step reasoning tasks requiring deep web exploration, moving beyond simple single-hop QA. Benchmarks like GAIA, BrowseComp, WebWalkerQA, and HLE are used to evaluate this capability.

### Key Differentiators

| Dimension | TaskCraft | Beyond Ten Turns | DeepDive | WebThinker | WebShaper | WebWalkerQA | Search-R1 | AutoCoA |
|-----------|-----------|------------------|----------|------------|-----------|-------------|-----------|---------|
| Primary Method | Automated task generation | Asynchronous RL + QA synthesis | KG-based data synthesis | RL + DPO for tool use | Formalization-driven synthesis | Benchmark + multi-agent framework | RL with search-as-reasoning | SFT+RL for CoA internalization |
| RL Algorithm | Not specified | GRPO | Multi-Turn GRPO | Iterative DPO | GRPO | N/A | PPO/GRPO | GRPO |
| Key Innovation | Depth/width extensions | Asynchronous training | KG random walks | Think-Search-Draft | Set-theoretic formalization | Web traversal benchmark | Loss masking | Internal world model |
| Best Model | Qwen2.5-7B | QwQ-32B | QwQ-32B | QwQ-32B | Qwen2.5-72B | GPT-4o | Qwen2.5-7B | R1-Distill-Qwen-7B |
| Top GAIA Score | 60.8% | 58.7% | ~50% (Xbench) | 70.7% (GPQA) | 60.1% | N/A | N/A | N/A |
| Open Source | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

### Open Challenges

Despite significant progress, several challenges remain across the field:

1. **Compute Budget Transparency:** Most papers do not report specific compute budgets, GPU hours, or training costs, making reproducibility and fair comparison difficult.
2. **Generalization Gap:** Performance on benchmarks like BrowseComp still lags significantly behind proprietary systems (e.g., DeepDive-32B at 14.8% vs. OpenAI DeepResearch at 51.5%).
3. **Tool Diversity:** Most methods focus on a single tool (web search), with limited exploration of multi-tool environments (code execution, API calling, multimodal tools).
4. **Reward Design:** Simple exact match rewards capture only a fraction of human judgment, and more sophisticated reward mechanisms are needed.
5. **Over-Search and Efficiency:** Several papers note that RL training can lead to excessive search behavior, and balancing thoroughness with efficiency remains an open problem.

---

### Sources

[1] TaskCraft arXiv: https://arxiv.org/abs/2506.10055
[2] TaskCraft ICLR 2026 Proceedings: https://proceedings.iclr.cc/paper_files/paper/2026/file/48644509339cb3076f7b0407c7588af6-Paper-Conference.pdf
[3] TaskCraft GitHub: https://github.com/OPPO-PersonalAI/TaskCraft
[4] Beyond Ten Turns arXiv: https://arxiv.org/abs/2508.07976
[5] Beyond Ten Turns NeurIPS 2025: https://neurips.cc/virtual/2025/128035
[6] ASearcher GitHub: https://github.com/inclusionAI/ASearcher
[7] DeepDive arXiv: https://arxiv.org/abs/2509.10446
[8] DeepDive GitHub: https://github.com/THUDM/DeepDive
[9] WebThinker arXiv: https://arxiv.org/abs/2504.21776
[10] WebThinker NeurIPS 2025 Proceedings: https://proceedings.neurips.cc/paper_files/paper/2025/file/ae03bdef276132fae089692445725635-Paper-Conference.pdf
[11] WebThinker GitHub: https://github.com/RUC-NLPIR/WebThinker
[12] WebShaper arXiv: https://arxiv.org/abs/2507.15061
[13] WebShaper ICLR 2026 Proceedings: https://proceedings.iclr.cc/paper_files/paper/2026/file/a6ffd1854c6191b1f33b7ad9509d46f9-Paper-Conference.pdf
[14] WebShaper HuggingFace Dataset: https://huggingface.co/datasets/Alibaba-NLP/WebShaper
[15] WebWalker arXiv: https://arxiv.org/abs/2501.07572
[16] WebWalker ACL 2025 Proceedings: https://aclanthology.org/2025.acl-long.508.pdf
[17] WebAgent GitHub: https://github.com/Alibaba-NLP/WebAgent
[18] Search-R1 arXiv: https://arxiv.org/abs/2503.09516
[19] Search-R1 GitHub: https://github.com/PeterGriffinJin/Search-R1
[20] AutoCoA arXiv: https://arxiv.org/abs/2503.06580
[21] AutoCoA GitHub: https://github.com/ADaM-BJTU/AutoCoA
