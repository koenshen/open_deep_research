# Comprehensive Literature Review of Data Synthesis Methods for Tool-Augmented LLM Agent Training (2025)

This review covers eight data synthesis and training algorithms published in 2025 for tool-augmented (primarily web search) LLM agent training. Each algorithm is analyzed in depth, covering motivation, core innovation, key contributions, empirical setup with headline results, and reported limitations.

---

## TaskCraft (Shi et al., 2025)

**Paper:** [TaskCraft: Automated Generation of Agentic Tasks](https://arxiv.org/abs/2506.10055) | **Venue:** ICLR 2026 | **Code:** [github.com/OPPO-PersonalAI/TaskCraft](https://github.com/OPPO-PersonalAI/TaskCraft)

### Motivation and Core Innovation

TaskCraft addresses two critical bottlenecks: (1) existing instruction datasets lack essential information on tool usage and environment interaction, and (2) human-annotated benchmarks like GAIA and BrowseComp are limited in scale. The core innovation is a **bottom-up task construction** approach that generates tasks from unlabeled corpora (webpages ~75%, images ~15%, PDFs ~10%) through three stages:

1. **Atomic Task Generation:** Simple tasks solvable with a single tool invocation, validated via rejection sampling (agent-with-tools > LLM-only, non-zero answer).
2. **Depth-Based Extension:** Recursive multi-step dependencies creating sequential multi-hop reasoning tasks.
3. **Width-Based Extension:** Parallel sub-problems requiring orchestration of multiple tool calls.

Verification is performed via rejection sampling for atomic tasks and LLM-based linguistic analysis for extension tasks to prevent information leakage.

### Key Contributions

- First automated workflow for generating difficulty-scalable, multi-tool, and verifiable agentic tasks with execution trajectories.
- The resulting dataset comprises ~36,000–41,000 tool-intensive tasks across varied difficulty levels, including ~12,600 tool-interaction trajectories and ~5,000 multi-hop decompositions.
- SFT with synthetic data yields average improvements of +14.0% on Qwen2.5-3B-Base and +6.0% on Qwen2.5-3B-Instruct over base workflows.
- State-of-the-art results on GAIA, WebWalker, BrowseComp, and HLE when combined with RL training.

### Empirical Setup

**Baselines:** MHQA (Multi-Hop QA) data, base workflow (direct LLM prompting), Search-R1, various TIR (Tool-Integrated Reasoning) models.

**Models:** Qwen2.5-3B-Base, Qwen2.5-3B-Instruct for SFT; Qwen-2.5, DeepSeek, QwQ-32B for broader evaluation.

**Training Configurations:** SFT data sizes tested: 1k, 2.5k, 5k, 7.5k, and 8k tasks. RL data: 8k tasks. Scaling trend: increasing training data from 1k to 5k tasks yields progressive improvements (17.5% → 39.8% on GAIA).

**Headline Results:**

| Benchmark | Configuration | Result |
|-----------|--------------|--------|
| GAIA | MHQA baseline | 20.4%–38.8% |
| GAIA | + 2.5k TaskCraft SFT | 60.2% |
| GAIA | + 8k TaskCraft SFT + RL | **60.8%** (SOTA among TIR models) |
| HotpotQA | Search-R1 alone | 0.284 |
| HotpotQA | Search-R1 + TaskCraft SFT | **0.344** |
| SFT avg. gain | Qwen2.5-3B-Base | +14.0% |
| SFT avg. gain | Qwen2.5-3B-Instruct | +6.0% |

**Human Evaluation:** 91.7% linguistic fluency, 95.0% accuracy for atomic tasks; 82.3% validity for extended tasks.

### Limitations and Failure Modes

- **Limited tool scope:** Currently focuses on only three tools (web browsing, PDF reading, image analysis). Future work will enable user-defined custom tools.
- **Verification challenges:** Extension tasks rely on LLM-based linguistic analysis rather than full execution-based validation.
- **Generation agent ceiling:** Task quality is bounded by the capabilities of the LLM used as the generation agent, though tasks can exceed the agent's own capabilities.
- **Pseudo-supersets:** Risk of creating extension tasks that don't genuinely require all subtasks.
- **Information leakage:** One subtask's answer may inadvertently reveal another's, undermining multi-hop reasoning requirements.

---

## Beyond Ten Turns / ASearcher (Gao et al., 2025)

**Paper:** [Beyond Ten Turns: Unlocking Long-Horizon Agentic Search with Large-Scale Asynchronous RL](https://arxiv.org/abs/2508.07976) | **Venue:** ICLR 2026 (Poster), NeurIPS 2025 Workshop (Spotlight) | **Code:** [github.com/inclusionAI/ASearcher](https://github.com/inclusionAI/ASearcher)

### Motivation and Core Innovation

Existing online RL methods impose small turn limits (≤10) to keep GPU utilization high, restricting complex strategy learning. The paper identifies two key limitations: insufficient search turns and lack of large-scale, high-quality QA pairs.

The **ASearcher framework** introduces three pillars:

1. **Fully Asynchronous RL Training (AReaL):** Decouples trajectory execution from model updates, supporting turn limits up to 128 per trajectory with near-100% GPU utilization. This eliminates the bottleneck where long trajectories block training.

2. **Data Synthesis Agent:** An autonomous prompt-based LLM agent generates challenging QA pairs via two-stage process:
   - **Injection:** Starting from seed questions, injects related external facts to increase complexity.
   - **Fuzzing:** Deliberately blurs/obscures details to increase uncertainty.
   - Output: **25.6k high-quality samples** from 14k seed questions, plus 16,000 filtered challenging samples from open-source datasets.

3. **Agent Design:** Minimal two-tool design (search + browse) with no external LLMs or commercial APIs. Trained end-to-end via GRPO with sparse rewards.

### Key Contributions

- Scalable fully asynchronous RL training enabling long-horizon search (up to 128 turns) while maintaining high training efficiency.
- Autonomous data synthesis agent producing 25.6k challenging QA pairs.
- State-of-the-art results: Through RL training, the QwQ-32B agent achieves substantial improvements (+22.4 Avg@4 on xBench-DeepSearch, +15.0 on GAIA, +14.6 on Frames).
- Emergent expert-level search behaviors: uncertainty-aware reasoning, precise extraction, cross-document inference, rigorous confirmation.
- Generalization from local knowledge bases to web search.

### Empirical Setup

**Baselines:** Search-R1-32B, R1-Searcher-32B, WebExplorer-7B/14B, Search-o1-32B, WebThinker-32B, WebDancer-32B, GPT-4o + Search, OpenAI DeepResearch, Kimi-Researcher.

**Models:** Qwen2.5-7B, Qwen2.5-14B, QwQ-32B.

**Training Configurations:** GRPO algorithm, turn limit up to 128, sparse reward (Format + F1 for base LLMs; LLM-as-Judge for LRMs). Compute budget: ~16k H800 GPU hours for ASearcher-Web-QwQ.

**Headline Results:**

| Benchmark | Base QwQ-32B | ASearcher-Web-QwQ (RL) | Improvement |
|-----------|-------------|------------------------|-------------|
| GAIA | ~43.7 | **58.7** | **+15.0** |
| xBench-DeepSearch | ~28.7 | **51.1** | **+22.4** |
| Frames | ~59.9 | **74.5** | **+14.6** |

**With zero-shot enhancements (DeepSeek-V3 summary + 16 parallel rollouts):** GAIA 71.8, xBench 75.0, Frames 83.4, outperforming OpenAI DeepResearch and Kimi-Researcher.

**Local Knowledge Base Setting:** ASearcher-Local-14B (Avg F1=60.0) surpasses Search-R1-32B (F1=58.7) despite being less than half the size.

### Limitations and Failure Modes

- **Compute cost:** Training requires ~16k H800 GPU hours for the 32B model.
- **Dependence on base model quality:** Effectiveness correlates with base model reasoning capabilities; QwQ-32B shows much larger gains than Qwen2.5 base models.
- **Data synthesis quality:** Relies on the synthesis agent's ability to generate challenging, grounded questions.
- **Generalization gap:** Training on static local KBs may not fully capture real web stochasticity.
- **Context window saturation:** For LRMs, history truncated to 25k characters; thinking discarded to keep inputs within ~10k tokens.
- **Reported failure modes in baselines:** Failure to decompose complex queries, hallucination, missing key information, failure to verify conclusions, local optimum traps.

---

## DeepDive (Lu et al., 2025)

**Paper:** [DeepDive: Advancing Deep Search Agents with Knowledge Graphs and Multi-Turn RL](https://arxiv.org/abs/2509.10446) | **Code:** [github.com/THUDM/DeepDive](https://github.com/THUDM/DeepDive)

### Motivation and Core Innovation

Open-source LLMs struggle with long-horizon reasoning and browsing due to (1) lack of sufficiently difficult training data and (2) absence of effective multi-turn RL training for integrating reasoning with web search.

**Core Methodology (Two-Stage Pipeline):**

**Stage 1 — Automated Data Synthesis from Knowledge Graphs:**
- Performs random walks on open KGs (KILT and AMiner) to generate multi-hop reasoning paths.
- Applies entity attribute obfuscation (generalizing dates to ranges, masking entities) to create ambiguity.
- Uses a difficulty filter: only questions that frontier models fail to solve are retained.
- Produces **3,090 high-quality deep search QAs** (1,016 for SFT, 2,234 for RL).

**Stage 2 — End-to-End Multi-Turn RL:**
- Uses GRPO with a strict binary reward function (format correctness + exact match).
- Incorporates a redundancy penalty based on Jaccard similarity between search queries to discourage repeated queries.
- Implements early-termination mechanism for robust tool use.

### Key Contributions

- Automated synthesis of complex, hard-to-find QA pairs from open KGs — scalable without human annotation.
- End-to-end multi-turn RL framework for deep search agents.
- DeepDive-32B achieves new open-source SOTA on BrowseComp (14.8%–15.3%), outperforming WebSailor, DeepSeek-R1-Browse, and Search-o1.
- Demonstration of test-time scaling: performance improves with more allocated tool calls (8% at 8 calls → 15% at 128 calls).
- Parallel sampling with fewest-tool-call selection raises accuracy from 12.0% to 24.8% on a subset.

### Empirical Setup

**Baselines:** WebSailor, DeepSeek-R1-Browse, Search-o1, GPT-4o with browsing, Claude-3.7-Sonnet.

**Models:** GLM-Z1-9B-0414, QwQ-32B. Trained models: DeepDive-9B, DeepDive-32B.

**Training Configurations:** GRPO with binary reward + redundancy penalty. Data split: 1,016 SFT + 2,234 RL. Built on Slime RL framework with Serper and Jina APIs.

**Headline Results:**

| Benchmark | DeepDive-32B | Context |
|-----------|-------------|---------|
| BrowseComp | **14.8%–15.3%** | Open-source SOTA |
| BrowseComp (+ i.i.d. data) | **22.2%** | With semi-automated data |
| BrowseComp-ZH | **25.6%** | Chinese variant |
| Xbench-DeepSearch | **50.5%** | Deep search benchmark |
| SEAL-0 | **29.3%** | Search and evaluation |

**Test-time scaling:** RL training increased average tool calls during inference from ~35 to ~45. Adding redundancy penalty reduced tool call counts during training.

### Limitations and Failure Modes

- **Difficulty ceiling:** Synthetic data from KGs has a difficulty ceiling below expert-level benchmarks.
- **"Over-search" phenomenon:** Model trained on high-difficulty data tends to over-search — continues browsing excessively even when enough information is available.
- **Gap with frontier proprietary models:** DeepDive-32B still significantly lags behind OpenAI Deep Research (51.5% on BrowseComp) and o3.
- **Shortcut exploitation:** Binary outcome rewards can lead to shortcut exploitation rather than thorough reasoning.
- **Reward hacking risk:** Strict binary reward creates sparse signal that can be slow to converge.

---

## WebThinker (Li et al., 2025)

**Paper:** [WebThinker: Empowering Large Reasoning Models with Deep Research Capability](https://arxiv.org/abs/2504.21776) | **Venue:** NeurIPS 2025 | **Code:** [github.com/RUC-NLPIR/WebThinker](https://github.com/RUC-NLPIR/WebThinker)

### Motivation and Core Innovation

Large reasoning models (LRMs) like OpenAI-o1 and DeepSeek-R1 demonstrate impressive reasoning capabilities but rely on static internal knowledge, limiting performance on knowledge-intensive tasks and report generation.

**WebThinker** empowers LRMs to autonomously search the web, navigate pages, and draft reports during reasoning through three key innovations:

1. **Deep Web Explorer Module:** Enables LRMs to dynamically search, navigate, and extract information from the web when encountering knowledge gaps. Unlike standard RAG, it allows iterative deep web navigation integrated into reasoning.

2. **Autonomous Think-Search-and-Draft Strategy:** Allows the model to seamlessly interleave reasoning, information gathering, and report writing in real time. In Report Generation Mode, it uses three tools: draft, check, and edit.

3. **RL-based Training via Iterative Online DPO:** Preference pairs are constructed based on correctness, tool efficiency, and thinking conciseness. The RL-trained version (WebThinker-32B-RL) substantially improves over the Base version.

### Key Contributions

- First deep research agent that empowers LRMs to autonomously search, navigate, and draft reports during reasoning.
- Deep Web Explorer module enabling dynamic web navigation integrated into reasoning.
- Autonomous Think-Search-and-Draft strategy for real-time report generation.
- State-of-the-art results among 32B models on all evaluated benchmarks.
- Surpasses Search-o1 by 21.9% on GAIA and 36.2% on HLE.
- Outperforms Grok3 DeeperSearch and Gemini2.0 Deep Research on report generation.

### Empirical Setup

**Baselines:** Direct reasoning, standard RAG, Search-o1, Grok3 DeeperSearch, Gemini2.0 Deep Research, GPT-4o, DeepSeek-R1-671B.

**Models:** QwQ-32B, DeepSeek-R1 (7B, 14B, 32B). Trained variants: WebThinker-QwQ-32B, WebThinker-R1-7B/14B/32B.

**Training Configurations:** Iterative online DPO with preference pairs based on correctness, tool efficiency, and thinking conciseness. Uses Bing Web Search API and Crawl4AI.

**Headline Results:**

| Benchmark | WebThinker-32B-RL | Improvement over Base |
|-----------|-------------------|-----------------------|
| GPQA | **70.7%** | — |
| GAIA | **48.5%** | +8.5% |
| WebWalkerQA | **46.5%** | — |
| HLE | **15.8%** | +21.5% |

**Report Generation (Glaive dataset):** Average score 8.1/10, outperforming Gemini2.0 Deep Research (7.9) and Grok3 DeeperSearch.

**Gains over direct generation:** Relative gains of 174.4% on GAIA and 422.6% on WebWalkerQA compared to direct generation.

### Limitations and Failure Modes

- **Lack of multimodal processing:** Cannot process images, videos, or other multimodal information.
- **Limited tool set:** Currently supports only web search, navigation, and drafting tools.
- **No GUI-based web exploration:** Needs extension to clicking buttons, interacting with dynamic web elements beyond simple links.
- **Future work directions:** Multimodal reasoning, advanced tool learning, GUI-based exploration, broader applicability in finance, science, and engineering.

---

## WebShaper (Tao et al., 2025)

**Paper:** [WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization](https://arxiv.org/abs/2507.15061) | **Venue:** ICLR 2026 | **Code:** [Alibaba-NLP/WebAgent](https://github.com/Alibaba-NLP/WebAgent) | **Models:** [HuggingFace](https://huggingface.co/Alibaba-NLP/WebShaper-32B)

### Motivation and Core Innovation

Existing data synthesis approaches adopt an **information-driven paradigm** — first collect web data, then generate questions. This leads to inconsistency between information structure and reasoning structure.

WebShaper proposes a **formalization-driven paradigm** that systematically formalizes information-seeking tasks using **set-theoretic constructs (Knowledge Projections)** before any information is collected.

**Knowledge Projections (KP):** Central to the formalization, KP enables precise control over reasoning structure through operations like R-Union and Intersection. This ensures structural consistency between information structure, reasoning structure, and QA pairs.

**Data Synthesis Pipeline:**
1. **Seed Question Construction:** 18,000 seed questions via guided random walks on Wikipedia.
2. **Agentic Expansion:** An autonomous Expander agent uses a layer-wise expansion strategy to avoid redundancy and reasoning shortcuts. The Expander autonomously interprets KP representations, retrieves online knowledge, constructs sub-questions, and validates them.
3. **Trajectory Construction:** 5,000 trajectories in ReAct format for SFT and RL (GRPO).

### Key Contributions

- First formalization-driven data synthesis method for information-seeking agents.
- Introduction of Knowledge Projections (KP) for precise reasoning structure control.
- Layer-wise expansion strategy minimizing redundancy while preventing reasoning shortcuts.
- State-of-the-art performance among open-source IS agents on GAIA (60.19%) and WebWalkerQA (52.50%).
- WebShaper-72B is the only open-source method scoring >60 points on GAIA, close to OpenAI Deep Research.

### Empirical Setup

**Baselines:** WebDancer, WebThinker, WebSailor, Search-o1, other open-source IS agents.

**Models:** Qwen-2.5-72B, Qwen-2.5-32B.

**Training Configurations:** SFT for cold start, then GRPO RL. Context length up to 128K. Tools: search, visit, summarization, validation in ReAct framework.

**Headline Results:**

| Benchmark | WebShaper-72B | Context |
|-----------|--------------|---------|
| GAIA | **60.19%** | Best open-source IS agent |
| WebWalkerQA | **52.50%** | Best open-source IS agent |

**Ablation Findings:**
- Formalization-driven approach significantly outperforms natural language and sequential expansion baselines.
- Layer-wise expansion outperforms sequential expansion.
- RL training (GRPO) improves scores by +7.7 to +14.5 points over SFT alone.
- Tool call analysis reveals longer, more complex reasoning chains.

### Limitations and Failure Modes

- **Computational cost:** Synthesis process is computationally expensive due to the Expander agent's autonomous retrieval and validation.
- **Non-stationary web environment:** Web pages change over time, causing potential inconsistencies between training and deployment.
- **Data scale:** Released dataset contains only 500 QA pairs (though 5,000 trajectories used for training).
- **Dependence on Wikipedia:** Seed questions from Wikipedia random walks may introduce biases.
- **Limited to text-based information seeking:** Not explicitly addressing multimodal needs.
- **Failure modes without formalization:** Natural language instead of KP leads to worse performance. Without layer-wise expansion, redundancy and reasoning shortcuts reduce data quality.

---

## WebWalkerQA (Wu et al., 2025)

**Paper:** [WebWalker: Benchmarking LLMs in Web Traversal](https://arxiv.org/abs/2501.07572) | **Venue:** ACL 2025 (Long Paper) | **Benchmark:** [HuggingFace Dataset](https://huggingface.co/datasets/callanwu/WebWalkerQA) | **Leaderboard:** [HuggingFace Space](https://huggingface.co/spaces/callanwu/WebWalkerQALeaderboard)

### Motivation and Core Innovation

Traditional search engines retrieve shallow content, limiting LLMs' ability to handle complex, multi-layered information spread across multiple webpage layers. The paper characterizes small ReAct models as "impatient" — they often stop after only a few actions whether or not they have found relevant evidence.

**WebWalker Multi-Agent Framework:**
- **Explorer Agent:** Navigates web pages via a Thought-Action-Observation cycle, selecting links to visit using HTML clickable links.
- **Critic Agent:** Evaluates whether gathered information is sufficient, manages memory, accumulates relevant information, and decides when enough evidence has been gathered.

**WebWalkerQA Benchmark:**
- 680 human-verified QA pairs spanning 1,373 webpages across four domains (conference, organization, education, game) in two languages (English and Chinese).
- Questions categorized as single-source (depth 2–4) and multi-source (depth 2–8), with three difficulty levels each.
- Explicitly requires vertical exploration through clickable links, unlike prior benchmarks focusing on horizontal retrieval.

### Key Contributions

- Introduction of WebWalkerQA benchmark for assessing LLMs' ability to perform web traversal.
- WebWalker multi-agent framework mimicking human-like web navigation through an explore-critic paradigm.
- Demonstration that even the best-performing model (GPT-4o + WebWalker) achieves only ~37.5% accuracy, highlighting the challenge.
- RAG + vertical exploration integration improves performance across all difficulty levels.
- Inference-time scaling: increasing allowed actions (from 5 to 25) yields further improvements.

### Empirical Setup

**Baselines:** ReAct, Reflexion, closed-book models, commercial RAG systems.

**Models:** GPT-4o, Qwen-Plus (closed-source); Qwen2.5 series (7B, 14B, 32B, 72B) (open-source).

**Note:** WebWalker is a framework applied at inference time, not a fine-tuning approach. However, WebWalkerQA has been used as a training/evaluation benchmark for other works.

**Headline Results:**

| Configuration | Accuracy |
|--------------|----------|
| GPT-4o + WebWalker | ~37.5% |
| Commercial RAG (best) | 40.73% |
| Closed-book models | <10% |
| Hard multi-source (best) | 16.67% (GPT-4o Reflexion) |

**Subsequent Leaderboard Results (from other models):**
- WebShaper: 52.50% on WebWalkerQA
- WebDancer: 62.0% (Pass@3)
- Mango with GPT-5-mini: 52.5% success rate
- DeepReason: 55.2% average accuracy

### Limitations and Failure Modes

- **Small dataset size:** Only 680 items, relatively small compared to other benchmarks.
- **HTML-only environment:** Operates only on textual HTML, not visual/multimodal content.
- **No training on navigation:** Framework applied at inference time without fine-tuning for navigation.
- **Residual reasoning errors:** Even after reaching correct pages, models may still make extraction errors.
- **Dependence on root URLs:** Requires predefined root URLs.
- **Failure modes observed:** Premature stopping ("impatient" behavior), performance degradation with depth, hard multi-source questions remain extremely challenging, refusal errors, wrong page failures, reasoning errors after reaching correct page.

---

## Search-R1 (Li et al., 2025)

**Note:** The first author is Bowen Jin (Jin et al.), though the brief references "Li et al., 2025." The paper is cited as Jin et al., 2025.

**Paper:** [Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning](https://arxiv.org/abs/2503.09516) | **Venue:** COLM 2025 | **Code:** [github.com/PeterGriffinJin/Search-R1](https://github.com/PeterGriffinJin/Search-R1) | **Citations:** ~1,265

### Motivation and Core Innovation

LLMs struggle with static knowledge cutoffs, multi-step reasoning requiring external facts, and hallucinations. Existing approaches (RAG, prompting for tool use, SFT) have significant limitations: RAG is one-shot, prompting is unreliable, SFT suffers from poor generalization.

**Search-R1** extends DeepSeek-R1 by having the LLM learn — solely through RL — to autonomously generate search queries during step-by-step reasoning with real-time retrieval.

**Key Innovations:**
1. **Search engine as part of the RL environment:** The LLM generates search queries and interleaves retrieved text with its own reasoning.
2. **Multi-turn interleaved reasoning and search:** Uses special tokens (`<search>`, `<information>`, `<answer>`) to structure multi-turn interactions.
3. **Retrieved token masking:** Critical technical contribution — policy gradients are computed only over LLM-generated tokens, excluding retrieved passages. Prevents search engine text from skewing RL updates.
4. **Simple outcome-based reward:** Exact match (binary) of final answer. No format rewards. Complex multi-turn behaviors emerge from simple binary feedback.
5. **Fully RL-based training without human-labeled trajectories.**

### Key Contributions

- Identification of challenges in applying RL to LLM reasoning with search engine calling.
- Novel RL framework (Search-R1) supporting LLM rollout and optimization with a search engine.
- Retrieved token masking to stabilize RL training.
- 26%, 21%, and 10% average relative improvement with three LLMs (Qwen2.5-7B, Qwen2.5-3B, LLaMA3.2-3B) over strong baselines.
- Empirical insights into PPO vs. GRPO, base vs. instruction-tuned models, and response length dynamics.
- Emergent behaviors: autonomous search query generation, self-verification through iterative retrieval.

### Empirical Setup

**Baselines:** CoT, RAG, IRCoT, R1 (DeepSeek-R1-style RL without search), SFT, Rejection Sampling, Search-o1.

**Models:** Qwen2.5-7B (Base/Instruct), Qwen2.5-3B (Base/Instruct), LLaMA3.2-3B (Base/Instruct).

**Training Configurations:** RL methods (PPO, GRPO, Reinforce++). Knowledge source: 2018 Wikipedia dump with e5 retriever, top-3 passages. Retrieved token loss masking applied. Training data: NQ and HotpotQA.

**Headline Results:**

| Model | Relative Improvement | Absolute Performance (Avg EM) |
|-------|---------------------|-------------------------------|
| Qwen2.5-7B | 26% (41% over RAG) | 0.431 (Search-R1) vs 0.348 (RAG) |
| Qwen2.5-3B | 21% (20% over RAG) | — |
| LLaMA3.2-3B | 10% | — |

**Ablation Findings:**
- Retrieved token loss masking is crucial: without masking, performance drops significantly (Avg. 0.343 vs 0.431 for 7B Base).
- PPO vs. GRPO: GRPO converges faster but PPO is more stable; comparable final performance.
- Base vs. Instruct: Instruct models start better but base models catch up after RL.
- Top-3 retrieved passages is optimal.

### Limitations and Failure Modes

- **Focus on textual QA with single search tool:** Limited to question-answering; future work may extend to multiple tools and multimodal tasks.
- **Sensitivity to top-k retrieval:** Optimal at top-3.
- **Simple reward function:** Outcome-based reward may not capture full complexity of search behavior.
- **Computational cost:** RL training can be computationally expensive.
- **Over-reliance on search:** Model may perform unnecessary searches when it already has the answer.
- **No format reward:** May lead to less structured outputs.
- **Derivative work critiques:** Outcome-supervised methods cannot distinguish between pivotal and redundant search rounds (credit assignment problem). GRPO's uniform advantage estimation across turns leads to training instability and collapse in multi-turn settings.
- **"Search Wisely" extension (β-GRPO):** Formally defines over-search and under-search, proposing to reward only confident, correct search decisions.

---

## AutoCoA (Zhang et al., 2025)

**Paper:** [Agent models: Internalizing Chain-of-Action Generation into Reasoning models](https://arxiv.org/abs/2503.06580) | **Code:** [github.com/ADaM-BJTU/AutoCoA](https://github.com/ADaM-BJTU/AutoCoA) | **Citations:** 17

### Motivation and Core Innovation

Traditional agentic workflows rely on external prompts to manage interactions with tools and the environment. The authors argue this is a fundamental limitation, proposing **Large Agent Models (LAMs)** that internalize the generation of Chain-of-Action (CoA), enabling autonomous tool-use decisions.

**AutoCoA Framework** combines SFT and RL with the following stages:

**SFT Phases (Three Substages):**
1. **Step-level action triggering (CoT+A):** Contrastive learning approach to help the model distinguish between reasoning steps and action steps.
2. **Trajectory-level CoA optimization (CoT+CoA with observation masking):** Prevents the model from simply copying tool outputs; trains it to reason with tool feedback.
3. **Internal world model learning:** Model learns to simulate expected tool responses internally, enabling prediction without actual tool calls.

**RL Phases (Two Stages):**
1. **Simulated environment (5/6 of RL budget):** GRPO training using the internal world model to generate tool responses, reducing real-environment interaction costs.
2. **Real environment (1/6 of RL budget):** Small portion of real-world interaction to improve adaptation to dynamic environments.

### Key Contributions

- Introduction of Large Agent Models (LAMs) that internalize CoA generation.
- AutoCoA framework combining SFT and RL for training reasoning models to seamlessly interleave CoT and CoA.
- Step-level action triggering via contrastive learning.
- Trajectory-level CoA optimization with observation masking.
- Internal world model for simulated environment interaction.
- AutoCoA-trained agent models significantly outperform ReAct-based workflows, especially in tasks requiring long-term reasoning and multi-step actions.
- Demonstration that acceptable results can be achieved with only 1/6 real interactions.

### Empirical Setup

**Baselines:** ReAct-based workflows on the same base model.

**Models:** DeepSeek-R1-Distill-Qwen-7B (7.62B parameters).

**Training Configurations:** SFT (three substages) + RL (GRPO, simulated then real environment). Built on verl and FlashRAG.

**Headline Results:**

| Configuration | Avg EM (%) | Avg LLM Accuracy (%) |
|--------------|-----------|----------------------|
| ReAct on R1-Distill-Qwen-7B (baseline) | **15.2** | **18.5** |
| SFT-stage1&2 only | **32.0** | **38.5** |
| SFT1&2&3 + RL1&2 (complete AutoCoA) | **34.2** | **40.8** |

**Key observations:** All AutoCoA variants substantially outperform the ReAct baseline. The trained model exhibits longer reasoning processes, incorporates its own knowledge more frequently, and calls tools only when necessary.

### Limitations and Failure Modes

- **Scope of evaluation:** Limited to open-domain QA tasks (single-hop and multi-hop). Future work should extend to open-ended problems.
- **Internal world model fidelity:** The simulated environment's world model is acknowledged as imperfect; improving fidelity is a future direction.
- **Real-environment adaptation:** While two-stage RL training helps, the model still requires some real-environment interaction.
- **Generalization to other domains:** Primarily focused on open-domain QA; other domains and task types not extensively explored.
- **Future work directions:** Open-ended problems, improving internal world simulation fidelity.

---

## Comparative Analysis

### Data Synthesis Paradigms

| Algorithm | Paradigm | Data Source | Scale |
|-----------|----------|-------------|-------|
| TaskCraft | Bottom-up corpus-driven | Webpages, PDFs, images | ~36k–41k tasks |
| Beyond Ten Turns | Prompt-based synthesis agent | Seed questions + external facts | 25.6k + 16k filtered |
| DeepDive | Knowledge graph random walks | KILT, AMiner | 3,090 QAs |
| WebThinker | RL-based self-improvement | Iterative online DPO | Not separately released |
| WebShaper | Formalization-driven (KP) | Wikipedia random walks | 18k seeds → 5k trajectories |
| WebWalkerQA | Human-verified benchmark | 1,373 webpages | 680 QA pairs |
| Search-R1 | RL with outcome rewards | NQ, HotpotQA | Not separately released |
| AutoCoA | SFT + RL with world model | Open-domain QA datasets | Not separately released |

### Training Approaches

| Algorithm | RL Method | Key Technical Innovation |
|-----------|-----------|--------------------------|
| TaskCraft | Combined with Search-R1 RL | Bottom-up task construction; rejection sampling |
| Beyond Ten Turns | GRPO (asynchronous) | AReaL fully asynchronous RL; 128-turn support |
| DeepDive | GRPO | Binary reward + redundancy penalty; KG-based synthesis |
| WebThinker | Iterative online DPO | Three-criteria preference construction |
| WebShaper | GRPO | Knowledge Projections formalization; layer-wise expansion |
| WebWalkerQA | Inference-time framework | Explore-critic paradigm; no training |
| Search-R1 | PPO/GRPO | Retrieved token masking; simple outcome reward |
| AutoCoA | GRPO | Internal world model; contrastive step-level triggering |

### Benchmark Performance Summary

| Benchmark | Best Open-Source | Score | Algorithm |
|-----------|-----------------|-------|-----------|
| GAIA | WebShaper-72B | **60.19%** | WebShaper |
| GAIA | TaskCraft (with RL) | **60.8%** | TaskCraft |
| GAIA | ASearcher-Web-QwQ | **58.7%** | Beyond Ten Turns |
| WebWalkerQA | WebShaper-72B | **52.50%** | WebShaper |
| BrowseComp | DeepDive-32B | **15.3%** | DeepDive |
| xBench-DeepSearch | ASearcher-Web-QwQ | **51.1%** | Beyond Ten Turns |
| HLE | WebThinker-32B-RL | **15.8%** | WebThinker |

### Common Failure Modes Across Algorithms

1. **Over-reliance on search:** Multiple works (DeepDive, Search-R1, WebShaper) report "over-search" behavior where models continue searching excessively.
2. **Credit assignment in multi-turn RL:** Outcome-based rewards cannot distinguish between pivotal and redundant search rounds (Search-R1, DeepDive).
3. **Difficulty ceiling:** Synthetic data often has a difficulty ceiling below expert-level benchmarks (DeepDive, TaskCraft).
4. **Tool scope limitations:** Most works focus on 2–3 tool types, limiting generalization (TaskCraft, WebThinker, ASearcher).
5. **Generalization gaps:** Models trained on specific environments (local KBs, Wikipedia) may not fully generalize to real web stochasticity (Beyond Ten Turns, WebShaper).
6. **Computational cost:** RL training with web search requires significant compute resources (16k+ GPU hours for 32B models).

---

## Emerging Trends and Future Directions

1. **Scaling turn budgets:** From ≤10 turns to 128+ turns, enabled by asynchronous RL and efficient training frameworks.
2. **Formalization-driven synthesis:** Moving from information-driven to formalization-driven data synthesis for better reasoning structure alignment.
3. **Internal world models:** Reducing real-environment interaction costs by simulating tool responses.
4. **Test-time scaling:** Performance improves with more tool calls and parallel sampling, suggesting a direction for inference-time compute scaling.
5. **Multi-modal extension:** Several works (WebThinker, TaskCraft) identify multimodal processing as a key future direction.
6. **GUI-based exploration:** Moving beyond HTML-only to full GUI-based web interaction.
7. **Custom tool support:** Enabling user-defined tools and atomic tasks for new tool types.

---

### Sources

[1] TaskCraft: Automated Generation of Agentic Tasks: https://arxiv.org/abs/2506.10055

[2] TaskCraft ICLR 2026 Proceedings: https://proceedings.iclr.cc/paper_files/paper/2026/file/48644509339cb3076f7b0407c7588af6-Paper-Conference.pdf

[3] TaskCraft GitHub: https://github.com/OPPO-PersonalAI/TaskCraft

[4] Beyond Ten Turns: Unlocking Long-Horizon Agentic Search with Large-Scale Asynchronous RL: https://arxiv.org/abs/2508.07976

[5] ASearcher GitHub: https://github.com/inclusionAI/ASearcher

[6] Beyond Ten Turns OpenReview PDF: https://openreview.net/pdf/d8435685e907b0499cf0ebaf26f2f7d01a04d8e7.pdf

[7] DeepDive: Advancing Deep Search Agents with Knowledge Graphs and Multi-Turn RL: https://arxiv.org/abs/2509.10446

[8] DeepDive GitHub: https://github.com/THUDM/DeepDive

[9] WebThinker: Empowering Large Reasoning Models with Deep Research Capability: https://arxiv.org/abs/2504.21776

[10] WebThinker GitHub: https://github.com/RUC-NLPIR/WebThinker

[11] WebThinker NeurIPS 2025 Proceedings: https://proceedings.neurips.cc/paper_files/paper/2025/file/ae03bdef276132fae089692445725635-Paper-Conference.pdf

[12] WebShaper: Agentically Data Synthesizing via Information-Seeking Formalization: https://arxiv.org/abs/2507.15061

[13] WebShaper ICLR 2026 Proceedings: https://proceedings.iclr.cc/paper_files/paper/2026/file/a6ffd1854c6191b1f33b7ad9509d46f9-Paper-Conference.pdf

[14] WebShaper on HuggingFace: https://huggingface.co/Alibaba-NLP/WebShaper-32B

[15] WebWalker: Benchmarking LLMs in Web Traversal: https://arxiv.org/abs/2501.07572

[16] WebWalker ACL 2025 Proceedings: https://aclanthology.org/2025.acl-long.508.pdf

[17] WebWalkerQA Dataset: https://huggingface.co/datasets/callanwu/WebWalkerQA

[18] Search-R1: Training LLMs to Reason and Leverage Search Engines with Reinforcement Learning: https://arxiv.org/abs/2503.09516

[19] Search-R1 GitHub: https://github.com/PeterGriffinJin/Search-R1

[20] AutoCoA: Agent models: Internalizing Chain-of-Action Generation into Reasoning models: https://arxiv.org/abs/2503.06580

[21] AutoCoA GitHub: https://github.com/ADaM-BJTU/AutoCoA
