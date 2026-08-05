# The Evolution of Evaluation Practices for Single-Agent and Multi-Agent LLM Systems (2023–2025)

## Introduction

The landscape of evaluating large language model (LLM)-based systems has undergone a fundamental transformation between 2023 and 2025. Early benchmarks that defined progress in 2023—such as MMLU, HumanEval, and GSM8K—have become largely saturated, with frontier models now scoring 93–99% on many of them [41]. This saturation has catalyzed a shift toward harder, more dynamic, and more realistic evaluation paradigms. Simultaneously, the emergence of multi-agent systems—where multiple LLM-powered agents collaborate, compete, or communicate—has introduced entirely new evaluation challenges that go far beyond measuring individual model capability.

The Stanford HAI 2025 AI Index Report documents that AI performance on MMMU and GPQA improved by 18.8 and 48.9 percentage points respectively in 2024 alone, while on SWE-bench, AI systems solved just 4.4% of coding problems in 2023—a figure that jumped to 71.7% in 2024 [81][84]. A survey of 283 LLM benchmarks identifies three major issues facing current benchmarks: inflated scores caused by data contamination, unfair evaluation due to cultural and linguistic biases, and the lack of evaluation on "process credibility" and "dynamic environments" [43][85].

This report provides a comprehensive synthesis of evaluation practices across four critical dimensions: benchmarks and sandbox environments, evaluation metrics, implementation and cost considerations, and future directions for unified evaluation pipelines. The analysis covers both single-agent and multi-agent systems, drawing on high-quality published papers, technical reports, and preprints from 2023 through 2025.

---

## Section 1: Benchmarks and Sandbox Environments

### 1.1 Single-Agent Benchmarks: From Saturation to Specialization

The single-agent evaluation landscape has evolved through three distinct phases. In 2023, the dominant benchmarks were **MMLU** (Massive Multitask Language Understanding), **HumanEval** (code generation), **GSM8K** (grade-school math), and **BIG-Bench** (204 diverse tasks). These benchmarks defined the frontier but quickly became saturated as models improved.

**MMLU** tests knowledge across 57 subjects with 15,908 multiple-choice questions [15][26]. Frontier models now score 88–99% on MMLU [6][14][31], leading to saturation. The benchmark has documented limitations including a 6.49% error rate in questions, 4–5% prompt sensitivity, 13 percentage point reproducibility variance, and data contamination concerns [6]. MMLU-Pro (June 2024, NeurIPS 2024 Spotlight) was introduced to address saturation by expanding answer choices from 4 to 10, containing over 12,000 questions across 14 disciplines, and emphasizing reasoning over factual recall [1][3][4][9]. Model accuracy drops by 16–33% compared to MMLU (e.g., GPT-4 from 88.7% to 72.6%) [1][3][8]. By early 2026, top models approach 90% accuracy on MMLU-Pro, suggesting potential saturation of even this harder variant [1][9][10].

**HumanEval** consists of 164 hand-crafted Python programming problems evaluated by functional correctness (pass@k) [19][20][21][30]. Frontier models now score 96–98% pass@1, making it "useless for comparing leading models" [27][29]. Under tougher tests (HumanEval+ with 80× more test inputs), top models lost 19–29% of their apparent pass rate [29]. The benchmark has spawned numerous extensions: HumanEval+ (80× more tests), HumanEval-X (multilingual), mHumanEval (204 natural languages), and HumanEval-V (multimodal) [19][30][32].

**GSM8K** contains 8,500 grade-school math word problems requiring 2–8 steps of basic arithmetic [38][40][42][44]. Frontier models now exceed 95% accuracy [56]. GSM-Symbolic (2024) revealed that LLMs rely on pattern-matching rather than true symbolic reasoning—inserting a single irrelevant clause can collapse accuracy by up to 65 percentage points [39]. GSM1k (2024) was created to measure overfitting and data contamination, showing performance drops of up to 13% for some model families [41].

**BIG-Bench** is a collaborative effort involving 450+ authors from 132 institutions, featuring 204 diverse tasks [57][58][59][62][63][64]. BIG-Bench Hard (BBH) comprised 23 especially challenging tasks; using Chain-of-Thought prompting, PaLM (540B) surpassed average human score on 10 of 23 tasks [62]. BIG-Bench Extra Hard (BBEH, February 2025) replaces each BBH task with a harder counterpart, increasing context length sixfold and reasoning depth sevenfold, resulting in only ~9.8% harmonic mean accuracy for general-purpose LLMs and ~44.8% for reasoning-specialized models [67][68][72].

**HELM** (Holistic Evaluation of Language Models) from Stanford's CRFM evaluates models across 42 scenarios and 7 metrics (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency) [76][77][78][79][80][83][87][89]. The framework ran over 4,900 evaluations, costing $38K for commercial models and 20K GPU hours for open models [89]. The leaderboard now includes 19 leaderboards, 150+ datasets, and 350+ models [85]. HELM entered maintenance mode on June 1, 2026 [82].

**AlpacaEval** uses an LLM judge (typically GPT-4) to perform pairwise comparisons on 805 prompts, reporting a length-controlled win-rate [7][9][13][14]. By May 2026, frontier models all exceed 95% LC win-rate, rendering the benchmark saturated [3]. AlpacaEval is vulnerable to adversarial gaming—null models with meaningless outputs scored up to 86.5% LC win rate [9].

**MT-Bench** evaluates LLMs in multi-turn conversational settings with 80 questions across 8 categories, each with a predefined follow-up (160 turns total) [20][21][22][38]. The judge (GPT-4) achieves ~80–85% agreement with human annotators [20][22][38]. MT-Bench-101 (ACL 2024) expanded to 1,388 multi-turn dialogues with 4,208 turns across 13 tasks [24][28][29][30][31][36].

**Chatbot Arena (LMArena)** is a crowdsourced platform where users submit prompts and receive anonymous responses from two randomly selected models, then vote for the better one [39][40][41][47][48][53]. As of early 2025, over 2 million human votes have been collected across hundreds of models [40]. The platform uses the Bradley-Terry model for simultaneous maximum likelihood estimation with confidence intervals [40][41]. "Arena Elo has become one of the most influential AI evaluation methods because it captures something benchmarks can't: how a model actually feels to use" [43].

**SimpleQA** (OpenAI, October 2024) evaluates factuality with 4,326 short, fact-seeking questions with single, indisputable answers [57][58][59][60][72]. OpenAI's o1-preview scored 42.7% correct, GPT-4o 38.2%, Claude-3.5-sonnet 28.9% [58]. SimpleQA Verified (2025, by Google) refined the benchmark to 1,000 questions, addressing noisy labels and topical biases [59][67].

**GPQA** (Graduate-Level Google-Proof Q&A, November 2023) contains 448 difficult multiple-choice questions in physics, chemistry, and biology written by domain experts [31][69]. Experts with PhDs in corresponding domains reach 65% accuracy, while highly skilled non-expert validators only reach 34% despite unrestricted web access [69]. By 2024, AI performance on GPQA improved by 48.9 percentage points [81][84].

**HLE** (Humanity's Last Exam) contains 2,500 expert-level questions designed to be extremely difficult for AI models, with state-of-the-art models scoring below 50% accuracy [32][35][41].

**LiveCodeBench** is a continuously updated coding benchmark that uses LeetCode, AtCoder, and Codeforces problems released after a model's training cutoff, structurally preventing contamination [13][27][29][76][86].

### 1.2 Multi-Agent Benchmarks and Sandboxes: Evaluating Collaboration and Emergence

The evaluation of multi-agent systems presents fundamentally different challenges from single-agent evaluation. Rather than measuring individual capability, multi-agent benchmarks must assess coordination, communication, role assignment, and emergent behaviors. The survey by Mohammadi et al. (KDD 2025) uses the analogy: "Evaluating an LLM is like testing an engine, whereas evaluating an agent is like testing the entire car under various driving conditions."

**AgentBench** (Liu et al., 2023, ICLR 2024) is a multi-dimensional benchmark consisting of 8 distinct interactive environments: Operating System, Database (SQL), Knowledge Graph, Digital Card Game, Lateral Thinking Puzzles, House Holding (ALFWorld), Web Shopping (WebShop), and Web Browsing (Mind2Web) [2]. The benchmark includes 1,091 tasks across 8 environments. The original 2023 paper tested 29 LLMs, finding that top commercial LLMs (especially GPT-4) significantly outperformed OSS models (average overall score 2.32 vs. 0.51). The predominant failure reason is Task Limit Exceeded (weak reasoning/decision-making), followed by Invalid Format and Invalid Action. By 2026, the benchmark is considered "more historically important than practically used," with most teams comparing frontier agents using SWE-bench Verified, WebArena, OSWorld, GAIA, and Tau-Bench instead.

**ChatDev** (2023, NeurIPS 2025) is a chat-powered framework for multi-agent software development using LLMs, integrating specialized agents (CEO, CTO, Programmer, Tester, Designer) in a waterfall model with three phases: design, coding, and testing [2]. Evaluation on a custom dataset (SRDD) of 1,200 software requirements shows ChatDev outperforms baselines (GPT-Engineer, MetaGPT) across completeness, executability, consistency, and overall quality. ChatDev 2.0 (DevAll, January 2026) evolved into a comprehensive zero-code multi-agent orchestration platform. However, it is noted that "ChatDev and MetaGPT can report contradictory numbers on similar tasks. ChatDev's paper claims 88 percent executability. MetaGPT's paper claims 41 percent executability. Different benchmarks, different metrics, different evaluation criteria."

**WebArena** (2024, NeurIPS 2024 Oral) provides a standalone, self-hostable web environment for building autonomous agents, with five key domains: e-commerce (90,000+ products), social forums (95 subforums, 127,390 posts), collaborative software development (GitLab-like, 300+ repos), content management systems, and supplementary tools [2]. The benchmark includes 812 long-horizon tasks from 241 templates. The core metric is end-to-end functional correctness. Human annotation established a reference performance baseline of 78.24% human success. Initial LLM agents (GPT-4) achieved only 14.41% success. Subsequent advances have raised state-of-the-art to 61.7% (IBM CUGA). The WebArena ecosystem includes VisualWebArena (ACL 2024) for multimodal agents, TheAgentCompany (ICML 2025) for benchmarking in a simulated company, and WAREX for evaluating reliability under website failures.

**SWE-bench** (Jimenez et al., 2024, ICLR 2024) evaluates LLMs on real-world GitHub software issues, with models receiving a codebase and issue description and generating a patch [2]. The full benchmark comprises 2,294 problems from 12 popular Python repositories. SWE-bench Verified is a human-filtered subset of 500 instances. The ecosystem includes SWE-bench Multilingual (300 tasks across 9 languages), Multi-SWE-bench (1,632–2,132 instances across 7–8 languages), SWE-bench Pro (1,865 problems from 41 repositories), and SWE-MERA (automated pipeline for quarterly new tasks). A 2025 analysis found that 19.78% of cases labeled as "solved" on the leaderboard are semantically incorrect—they pass unit tests by coincidence or by reward-hacking [2]. As of early 2026, Claude Opus 4.5 leads at 76.80% resolved on SWE-bench Verified.

**MetaGPT** (2023, ICLR 2024 Oral) is a meta-programming framework for multi-agent collaboration using LLMs, incorporating Standard Operating Procedures (SOPs) from human workflows [2]. Agents with specialized roles (Product Manager, Architect, Project Manager, Engineer, QA Engineer) produce structured outputs rather than relying on unstructured dialogue. The framework achieves state-of-the-art results on HumanEval (85.9% Pass@1) and MBPP (87.7% Pass@1) with GPT-4. The core lesson from MetaGPT is that "reliable agent collaboration is not mainly a social problem. It is an interface, artifact, and verification problem."

**CAMEL** (Li et al., 2023, NeurIPS 2023) is an open-source multi-agent framework designed to study the scaling laws of agents, enabling large-scale simulations of up to 1M agents [2]. The CAMEL AI 'Domain Expert' dataset, comprising 25,000 conversations between two GPT-3.5 Turbo agents, was used as part of the training data for Teknium's OpenHermes model and the Microsoft Phi model. **CRAB** (2024) is a cross-environment agent benchmark for multimodal language model agents, enabling agents to operate multiple devices (e.g., Android and Ubuntu) simultaneously. Testing showed GPT-4o achieving the highest Completion Rate of 35.26% on cross-platform tasks.

**SOTOPIA** (Zhou et al., 2023, ICLR 2024) is an open-ended environment for simulating complex social interactions and evaluating social intelligence [2]. It covers negotiation, persuasion, collaboration, cooperation, competition, and exchange, contextualized in character backgrounds and relationships. The environment includes 90 social scenarios and 40 characters. The SOTOPIA-Eval framework scores episodes along seven dimensions: Goal Completion, Believability, Knowledge, Secret, Relationship, Social Rules, and Financial/Material. GPT-4 achieves a goal completion rate of 7.62/10, significantly lower than humans, and struggles to exhibit social commonsense reasoning and strategic communication skills. SOTOPIA-Ω, SOTOPIA-π, and Sotopia-RL extend the framework with dynamic strategy injection, interactive learning, and multi-dimensional reward modeling.

**AgentVerse** (Chen et al., 2023, ICLR 2024) structures problem-solving into four iterative stages: Expert Recruitment, Collaborative Decision-Making, Action Execution, and Evaluation [2]. Multi-agent groups consistently outperform single agents across all tested tasks. For GPT-4, pass@1 on HumanEval improves from 83.5 (CoT) to 89.0 (Group). The framework reveals emergent social behaviors: volunteer behaviors, conformity behaviors, and destructive behaviors.

**CrewAI** (December 2023) is an open-source Python framework for building AI agents and multi-agent systems, used by 65% of the Fortune 500 according to the company [2]. A 2025 benchmarking study found that framework choice produces performance variation comparable to model choice. CrewAI is best suited for complex use cases like automated research, content pipelines, and business intelligence.

**AutoGen** (Microsoft Research, 2023) won Best Paper at the LLM Agents Workshop ICLR'24 [2]. AutoGen Studio (2024) provides a no-code interface for prototyping and debugging multi-agent workflows. AutoGenBench (2024) is a benchmark runner for agent evaluation. A 2025 benchmarking study found that AutoGen scales best for complex multi-agent systems but requires stronger developer skills.

### 1.3 Comparative Analysis: Single-Agent vs. Multi-Agent Benchmarks

**Task Diversity:** Single-agent benchmarks offer broad coverage of knowledge domains (MMLU: 57 subjects; BIG-Bench: 204 tasks) but typically test isolated capabilities. Multi-agent benchmarks are more specialized—most focus on software development (ChatDev, MetaGPT, SWE-bench), social interaction (SOTOPIA), or web tasks (WebArena, AgentBench). The survey of Jurkovic (2025) examined 32 multi-agent evaluation papers and found that miscoordination is heavily represented (26 papers), while collusion is underrepresented (5 papers, all based on party games).

**Scalability:** Single-agent benchmarks are generally easier to scale—running MMLU on new models is straightforward via the EleutherAI lm-evaluation-harness [15]. Multi-agent evaluations are more complex and expensive, requiring multiple agents, orchestration frameworks, and sandbox environments. The CRAB benchmark, for example, requires a cross-platform infrastructure. AgentBench's Dev and Test splits require approximately 4,000 and 13,000 multi-turn interactions respectively.

**Realism:** Single-agent benchmarks often test artificial scenarios (multiple-choice questions, isolated function calls) that may not reflect real-world usage. As one practitioner notes, "HumanEval scores look great on pitch decks but miss what production coding agents need" [23]. Multi-agent benchmarks tend to be more realistic—WebArena simulates real web environments, SWE-bench uses actual GitHub issues, and SOTOPIA models social interactions. However, as Jurkovic's survey notes, current multi-agent evaluations "often lack realism, relying on games rather than real-world tasks."

**Design Trade-offs:** Single-agent benchmarks face trade-offs between breadth and depth. MMLU offers broad coverage but shallow evaluation (multiple-choice). BIG-Bench offers deep coverage but high computational cost. Multi-agent benchmarks face trade-offs between realism and reproducibility. WebArena's Dockerized setup ensures reproducibility but uses static snapshots of websites. SWE-bench uses real GitHub issues but faces contamination risks from public git history.

**Strengths and Limitations:** Single-agent benchmarks excel at standardized comparison and reproducibility but suffer from saturation and contamination. Multi-agent benchmarks capture emergent behaviors and real-world complexity but face challenges in standardization, cost, and evaluation reliability. The Yehudai et al. (2025) survey identifies critical gaps in multi-agent evaluation: lack of evaluation for cost-efficiency, safety, robustness, policy adherence, and fine-grained diagnostic metrics.

---

## Section 2: Evaluation Metrics

### 2.1 LLM-as-Judge Metrics

The LLM-as-a-Judge paradigm uses strong LLMs (e.g., GPT-4) as automated evaluators of other LLMs' outputs. The foundational paper, "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (Zheng et al., 2023, NeurIPS 2023), identifies key biases: position bias, verbosity bias, self-enhancement bias, and limited math/reasoning grading [20][21][22]. Mitigation strategies include positional randomization, few-shot prompting, chain-of-thought prompts, and reference-guided grading. GPT-4 achieves over 80% agreement with human experts, matching inter-human agreement.

**Specific Implementations:**

- **AlpacaEval:** Uses a judge model to compare outputs against a reference (usually GPT-4) on 805 prompts, reporting a length-controlled win-rate. By May 2026, it is saturated and length-biased; the community has shifted to Arena-Hard-Auto, WildBench, and LiveBench [7][9][13][14].

- **MT-Bench:** Uses GPT-4 to score answers on a 1–10 scale across 80 multi-turn questions. GPT-4 achieves ~80–85% agreement with human annotators [20][21][22][38].

- **G-Eval:** Uses chain-of-thought prompting to achieve high alignment with human judgments (up to ~80% agreement with GPT-4) [2].

**Biases and Mitigations:**
- **Position bias:** Favoring answers based on order. GPT-4 has over 65% consistency, improving to 77.5% with few-shot [2].
- **Verbosity bias:** Preferring longer responses. GPT-4 shows 8.7% failure rate vs. 91.3% for other models [2].
- **Self-enhancement bias:** Rating own outputs higher. GPT-4 shows a 10% higher win rate for its own responses [2].
- **Limited reasoning ability:** Reference-guided evaluation reduces mathematical failure rate from 70% to 15% [2].

**Domain-Specific Limitations:** The paper "Limitations of the LLM-as-a-Judge Approach for Evaluating LLM Outputs in Expert Knowledge Tasks" (IUI '25, March 2025) found that subject matter experts agreed with LLM judges only 68% of the time in dietetics and 64% in mental health. The study concludes that LLM-as-a-judge is insufficient for complex, domain-specific tasks [2].

**Cost Comparisons:** GPT-4o is the cheapest judge ($0.93 per eval) but inflates scores by about 12% relative to GPT-4 8K ($5.10 per eval). GPT-4 Turbo ($1.85) is closest to the baseline in scoring [2].

**The "Rubber-Stamp Effect":** Dietz et al. (2025) identified a phenomenon where humans passively agree with LLM assessments, making human judgment still essential as of 2026 [2].

**Rubric-Based Evaluation:** Rubric-based evaluation is emerging as the new gold standard over reference-based metrics. The core principle: "A weak judge on a great rubric outperforms a great judge on a weak rubric" [2]. Key milestones include OpenAI's HealthBench (48,562 physician-authored criteria) and Prometheus (open evaluator trained on customized rubrics).

**Current State (2026):** The default for large-volume labeling is LLM-as-judge with a 5–10% human verification rate. Production teams compute Cohen's kappa between judge and a labeled human sample before shipping any new rubric, and re-sample monthly to catch judge drift [2].

### 2.2 Agent-as-Judge Approaches

The **Agent-as-Judge** framework (Zhuge et al., ICML 2025, arXiv:2410.10934) uses agentic systems to evaluate other agentic systems, incorporating agentic features that enable intermediate feedback for the entire task-solving process [2]. Applied to code generation with the DevAI benchmark (55 realistic AI development tasks with 365 hierarchical requirements), Agent-as-Judge achieves approximately 90% agreement with human expert evaluations, compared to 70% for LLM-as-a-Judge, while reducing evaluation time and cost by about 97% (from 86 hours/$1,297 to 2 hours/$31) [2].

**Multi-Agent-as-Judge (MAJ-Eval)** formalizes the use of multiple LLM agents with diverse, automatically derived personas to simulate multidimensional human judgment, achieving Spearman's ρ=0.43–0.47 [2]. The **MAST Framework** organizes multi-agent errors into specification & system design, inter-agent misalignment, and task verification & termination [2].

### 2.3 Human Annotation and Human Evaluation

Human evaluation remains the gold standard but is not always feasible due to temporal or technical constraints. The prevailing approach is to lean heavily on automated evaluations, followed by a deeper dive with high-quality human evaluators. Pairwise comparison is preferred over rating scales [2].

**Inter-Annotator Agreement (IAA):** IAA must be a continuous quality signal, not a one-time pilot check. Disagreement is informative—it reveals task subjectivity, guideline ambiguity, or annotator drift. Key metrics include Cohen's kappa (two annotators, categorical), Fleiss kappa (multiple annotators, categorical), Krippendorff's alpha (handles missing data and ordinal scales), and correlation metrics (Kendall's tau for preference ranking). Recommended IAA targets depend on task subjectivity: 0.90+ for objective tasks, 0.70–0.85 for moderately subjective, and 0.60–0.75 for inherently subjective (e.g., RLHF preferences) [2].

**Crowdsourcing vs. Managed Services vs. In-House Teams:** Crowdsourcing platforms (e.g., MTurk, Toloka, Prolific) offer low cost and high speed but suffer from quality issues—spam, label inconsistency, lack of domain expertise, and cultural bias. Managed services (e.g., Scale AI, Humyn Labs, Turing) provide vetted experts and multi-layer QC. Verified experts outperform anonymous crowds for multimodal data, with error rates 3–5× lower on medical imaging and IAA scores above 0.75 vs. crowd scores below 0.5 [2].

**Human vs. LLM Annotation (2026):** Human annotation remains best for nuanced tasks (sarcasm, medical/legal review, safety-critical) but is costly (cents to dollars per label) and slow (days). LLM annotation costs fractions of a cent per label, runs in minutes, and offers high consistency but struggles with ambiguity and hallucination. The hybrid workflow—LLM-as-judge with 5–10% human verification—is the 2026 default for production teams [2].

**Assessing Crowdsourced Annotations with LLMs:** The paper "Assessing Crowdsourced Annotations with LLMs" (NLP4DH, May 2025) found that LLM and human evaluators agreed on 74.3% of annotations (Cohen's κ = 0.286, fair agreement). The authors conclude that LLMs can serve as an effective initial filter to flag low-certainty cases for expert review [2].

### 2.4 Exact/String Matching Metrics

**Reference-Based Metrics:**
- **N-gram based:** BLEU (precision-focused, for machine translation), ROUGE (recall-focused, for summarization), and JS divergence [2].
- **Text similarity:** Levenshtein similarity ratio and variants (partial ratio, token-sort ratio, token-set ratio) [2].
- **Semantic similarity:** BERTScore, MoverScore, and Sentence Mover Similarity, using contextualized embeddings and cosine similarity [2].

**Reference-Free Metrics:** Quality-based metrics (SUPERT, BLANC, ROUGE-C), entailment-based metrics (SummaC, FactCC, DAE), and factuality/QA metrics (SRLScore, QAFactEval, QuestEval) [2].

**Trade-offs:** Traditional metrics like BLEU and ROUGE are fast and cheap but fail for open-ended tasks requiring nuance. The guide from Confident AI advises against using traditional statistical scorers for complex LLM outputs and recommends LLM-as-a-judge as the most reliable method [2].

**Metrics for LLM-generated code:** Functional correctness executes test cases to check if code produces expected outputs. Rule-based metrics include syntax correctness, format check, language check, and keyword presence. Automatic test generation uses LLM to generate diverse test cases [2].

**Metrics for RAG:** Faithfulness (factual consistency of answer against retrieved context), Answer relevancy, Context relevancy, and Context recall [2].

### 2.5 Process-Based vs. Outcome-Based Metrics

**Process Reward Models (PRMs) vs. Outcome Reward Models (ORMs):** PRMs evaluate each intermediate reasoning step for correctness, while ORMs only evaluate the final answer [2]. ORMs are simple to train but unable to distinguish correct reasoning from lucky guessing. PRMs provide dense reward signals enabling better credit assignment, reward hacking resistance, and interpretable verification. Training PRMs requires step-level labels, which are 3–10× more expensive per example than outcome annotation [2].

**Technical Innovations:**
- **ThinkPRM** (arXiv:2504.16828): A generative PRM that verifies step-by-step reasoning by generating a verification chain-of-thought, outperforming discriminative PRMs trained on two orders of magnitude more data [2].
- **DG-PRM** (ACL 2025): Dynamic and Generalizable Process Reward Modeling constructs a reward tree via hierarchical clustering of multifaceted criteria, achieving 81.8% on PRMBENCH [2].
- **PAVs (Process Advantage Verifiers)** (ICLR 2025 Spotlight): Measure progress—a change in the likelihood of producing a correct response before and after each step, achieving >8% higher accuracy and 1.5–5× compute efficiency gains [2].

**Frontier Practice:** DeepSeek-R1 used a rule-based reward system consisting mainly of accuracy rewards and format rewards, and did not apply neural outcome or process reward models because those models can suffer reward hacking [2].

**GEMMAS: Graph-based Evaluation Metrics for Multi-Agent Systems (EMNLP 2025):** GEMMAS analyzes the internal collaboration process by modeling agent interactions as a directed acyclic graph [2]. It proposes two process-level metrics: Information Diversity Score (IDS)—measuring semantic variation in inter-agent messages, and Unnecessary Path Ratio (UPR)—quantifying redundant reasoning paths. On GSM8K, systems with only a 2.1% difference in accuracy differ by 12.8% in IDS and 80% in UPR, demonstrating that outcome-only metrics are insufficient for evaluating multi-agent performance.

### 2.6 Comprehensive Metric Categories

**15 Multi-Agent Metrics (Grouped into Four Categories):**
- **Task & Outcome:** Action Completion, Factual Groundedness, Context Adherence, Instruction Adherence, Completeness
- **Interaction & Coordination:** Agent Flow, Agentic Trajectories, Feedback Loop Efficiency, Dynamic Multi-turn State Transitions, Conversation Quality
- **Tool Selection & Efficiency:** Tool Selection Quality, Tool Error, Resource Utilization
- **Security & System Health:** Scalability & Throughput, Cross-agent Context Poisoning [2]

**14 Metrics for LLM Agents (Confident AI, 2026):** Three evaluation levels: end-to-end (did the task succeed?), trajectory-level (was the path efficient?), and component-level (which component broke?). Metrics include Task Completion, Step Efficiency, Tool Correctness, Argument Correctness, Plan Adherence, Plan Quality, G-Eval, reasoning metrics, RAG metrics, and safety metrics [2].

**Three-Layer Evaluation Framework:** Tool selection, trajectory (step-by-step decisions), and final output. Six failure types: wrong tool, wrong arguments, wrong order, fabricated tool execution, inconsistency at scale, and correct answer with wrong reasoning [2].

**Trajectory Evaluation:** Scores the entire execution path—including tool calls, intermediate reasoning, and conversation turns. The key insight: "Correct final answers can hide broken reasoning" [2].

---

## Section 3: Implementation and Cost

### 3.1 Infrastructure Requirements for Single-Agent Evaluation

**HELM Infrastructure Costs:** The HELM evaluation tested 30 models across 16 scenarios using 7 metrics, resulting in 17 million queries, 12 billion tokens, and $38k in API costs [76][77][78][79][80][83][87][89]. HELM evaluations are computationally expensive and time-consuming, making frequent re-evaluation challenging as models update rapidly.

**Standard Evaluation Frameworks:**
- **OpenAI Evals:** A framework for evaluating LLMs, supporting regression testing and custom evaluation pipelines [1][4][30].
- **EleutherAI LM Evaluation Harness:** A standardized, reproducible framework for running benchmarks, widely used by the open-source community [5][15][25].
- **LangSmith/LangChain:** Frameworks supporting stepwise, trajectory, and final-response assessment for agent evaluation [2][3][19].
- **DeepEval:** A framework for running benchmarks with few lines of code, supporting synthetic data generation for custom benchmarks [28][30].
- **MLflow:** The top pick in 2026 with 30M+ monthly downloads, broadest metric coverage, and trace-aware evaluation [2].

**LLM-in-Sandbox Paradigm** (arXiv:2601.16206): Grants LLMs access to a code sandbox (virtual computer) to elicit general agentic intelligence. The sandbox provides three meta-capabilities: external resource access, file management, and code execution. Strong LLMs spontaneously leverage these capabilities on non-code tasks, achieving significant performance gains (up to +24.2% on mathematics for Qwen3-Coder). The sandbox infrastructure overhead is minimal: 1.1 GB shared image, ~50 MB per container idle [2].

### 3.2 Infrastructure Requirements for Multi-Agent Evaluation

**AgentCompass: Unified Evaluation Infrastructure** (arXiv:2607.13705): An open-source, lightweight, and extensible evaluation infrastructure for LLM-based agents [2]. Its core design decouples evaluations into three independent components: Benchmark (task-specific logic and scoring), Harness (agent interaction loop and prompting), and Environment (isolated execution context). This modular architecture allows flexible configurations (benchmark × harness × environment) without reimplementing complex execution logic. It natively supports over 20 benchmarks across five capability dimensions: Tool Use, Web & Research, Scientific Reasoning, Agentic Coding, and Productivity. Key findings: agent performance is highly sensitive to the choice of harness, with models deviating substantially from their officially reported baselines; trajectory analysis reveals distinct behavioral failure patterns; reward-hacking is prevalent among high-scoring models on coding benchmarks.

**MASEval: Framework-Agnostic Evaluation** (ACL 2026): A framework-agnostic evaluation library for multi-agent systems that treats the complete agent system as the unit of analysis [2]. It provides a unified benchmark interface, multi-agent tracing, and a benchmark development toolkit. Experiments across 3 benchmarks, 3 frameworks (smolagents, LangGraph, LlamaIndex), and 3 models (GPT-5-mini, Gemini-3.0-Flash, Claude-Haiku-4.5) show that framework choice impacts performance comparably to model choice, with mean performance ranges of 14.2 percentage points across models and 12.4 pp across frameworks. The most dramatic case: Haiku 4.5 scored 90.4% on MACS Travel with smolagents but only 59.5% with LlamaIndex, a 30.9 pp gap. MASEval reduces implementation effort for benchmark consumers by 83–91% and for benchmark producers by 35–57% [2].

**EnterpriseBench** (EMNLP 2025): Comprises 500 tasks across HR, IT, SWE, Sales, and Business Operations domains, with a simulated sandbox featuring fragmented data sources, access control hierarchies, and cross-functional workflows. Even the most capable models achieve only 41.8% task completion. Human agents achieve 70% accuracy but take much longer [2].

### 3.3 Human Annotation Costs and Involvement

**Hybrid Evaluation Workflow (2026 Default):** The 2026 default for large-volume labeling is LLM-as-judge with a 5–10% human verification rate [2]. Production teams compute Cohen's kappa between judge and a labeled human sample before shipping any new rubric, and re-sample monthly to catch judge drift. The hybrid loop produces near-human-grade labels at a fraction of the cost and time, with a paper trail for every label.

**Cost Comparisons:**
- **LLM-as-judge:** GPT-4o costs $0.93 per eval; GPT-4 8K costs $5.10 per eval [2].
- **Agent-as-Judge:** Reduces evaluation time and cost by roughly 97%, from 86 hours/$1,297 to approximately 2 hours/$31 [2].
- **Active Evaluation Acquisition** (ICML 2025): A novel RL-based policy can cut evaluation costs by over 90% by selecting a small subset of test prompts for actual evaluation, then predicting outcomes for the rest using learned dependencies [2].

**Scoutbee Case Study:** Calibrated evaluation pipelines reduced labeling time by 20× and increased revenue by 2–3×. Netflix achieved 85% agreement with just 100–200 expert examples [2].

**Evaluation Platform Market:** The global LLM evaluation platform market was valued at $2.4 billion in 2025 and is projected to reach $18.7 billion by 2034 at a CAGR of 25.6%. Growth is driven by rapid enterprise LLM deployment, AI governance regulations (e.g., EU AI Act), safety concerns, and integration with LLMOps toolchains. North America dominated with 41.8% revenue share in 2025; Asia Pacific is fastest-growing at 29.1% CAGR [2].

### 3.4 Scalability and Reliability Considerations

**Production Evaluation Pipeline (2026):** The recommended pipeline consists of six stages: pick 3–5 product-specific metrics; build a fixture set of 100–300 labeled prompts covering head and tail distributions; mix deterministic heuristics (schema, regex) first, then LLM judges for subjective dimensions; gate CI with tight thresholds that block regressions; sample 5–20% of live production traffic for async scoring; and close the loop by turning failing traces into new fixtures [2].

**Reliability Gap:** 72% of organizations have deployed agents somewhere, yet only 11% have achieved true production-scale deployment, and just 6% fully trust agents to autonomously run core business processes. Elite teams (top 15%) achieve 2.2× better reliability than other teams. Agent performance drops from 60% → 25% success rate when measured for consistency across multiple runs. Gartner predicts 40% of agentic AI projects will be canceled by 2027. Teams with established evaluation frameworks deploy model upgrades in days versus weeks [2].

**Pass@k vs. Pass^k:** The core shift in 2026 is from pass@k (best-case: at least one of k attempts succeeds) to pass^k (all-runs consistency). For a 70% per-trial agent, pass@3 is ~97% but pass^3 is only ~34.3%—a 63-point gap that exposes overconfidence [2].

**Sandbox Testing:** The report "Sandboxes for AI: Tools for a new frontier" (Datasphere Initiative, 2025) examines 66 sandboxes related to data, AI, or technology worldwide. Of these, 59 are national sandboxes, with 31 specifically designed for AI innovation, spanning 23 countries actively planning or operating AI-specific sandboxes [2].

---

## Section 4: Future Directions for Unified Evaluation Pipelines

### 4.1 Unified Frameworks and Design Principles

**Unified Four-Stage Framework** (ACM Survey, 2025): Proposes task generation, interactive execution, automated evaluation, and safety compliance—decomposing agent assessment into modular, verifiable components [2]. Four persistent gaps are identified: (1) insufficient task and scenario coverage, (2) fragmented metrics and limited comparability, (3) reproducibility, safety, and alignment issues, and (4) lack of human value alignment. Five future directions are proposed: lightweight and standardized benchmark design, cross-domain and cross-modal evaluation, combined self-supervised and human-preference evaluation, dynamic task generation and continual learning, and open community governance.

**Perfecting AI Agent Frameworks through Unified Design** (ICAART 2026): Presents a unified architecture that reconciles research prototypes (emphasizing transparent reasoning and pedagogy) and production toolkits (emphasizing operational resilience) [2]. Four design principles: modularity, explainability, safety-by-default, and observability-first. The six-layer architecture comprises: Deliberation (policy prompts, planning), Orchestration (agent hierarchies, workflow controllers), Model Abstraction (normalized LLM endpoints), Tools & Services (unified tool registry, context propagation, artifact management, memory), Execution (local/remote sandboxes, streaming, resumable processes), and Monitoring & Governance (telemetry, guardrails, evaluation feedback).

### 4.2 Concrete Research Directions

**1. Dynamic and Living Benchmarks:** The shift from static to dynamic/living benchmarks is essential to prevent saturation and contamination. LiveCodeBench, Chatbot Arena, and SWE-MERA represent early examples. Research is needed on automated pipelines for continuous task generation, periodic benchmark updates, and contamination-resistant evaluation protocols [2][13][16].

**2. Unified Metrics and Standardization:** The fragmentation of metrics across benchmarks hinders comparability. The GEMMAS framework demonstrates that outcome-only metrics are insufficient for multi-agent systems, but process-level metrics add complexity. Research is needed on standardized metric taxonomies, harmonized evaluation protocols, and methods for combining multiple metrics into interpretable overall scores [2].

**3. Cross-Domain and Cross-Modal Evaluation:** Current benchmarks are largely domain-specific. Future research should develop cross-domain evaluation frameworks that assess agents across web, software engineering, scientific, conversational, and embodied tasks simultaneously. The AgentCompass modular architecture (benchmark × harness × environment) provides a template for this approach [2].

**4. Automated Evaluation with Human Verification:** The 2026 default of LLM-as-judge with 5–10% human verification is a pragmatic compromise, but research is needed on optimal sampling strategies, drift detection methods, and automated rubric generation. The "rubber-stamp effect" (humans passively agreeing with LLM assessments) requires mitigation strategies [2].

**5. Safety and Alignment Evaluation:** Safety evaluation is becoming a governance requirement (EU AI Act). The Jurkovic survey (2025) found that most threat models lack any multi-agent evaluations. Research is needed on multi-agent safety benchmarks covering collusion, miscoordination, and adversarial behaviors. The WAREX framework for simulating website failures provides a template for evaluating robustness under adverse conditions [2].

**6. Cost-Efficiency Metrics:** The Yehudai et al. (2025) survey identifies lack of evaluation for cost-efficiency as a critical gap. Future benchmarks should integrate cost, latency, and computational efficiency alongside accuracy and success rates. The Agent-as-Judge framework's 97% cost reduction demonstrates the potential for efficient evaluation methods [2].

**7. Process-Level Evaluation:** The shift from outcome-only to process-level evaluation (PRMs, GEMMAS, trajectory evaluation) is a key trend. Research is needed on scalable methods for collecting process-level annotations, automated process reward models, and metrics that capture collaboration quality in multi-agent systems [2].

**8. Scalable Human Annotation:** Hybrid human-LLM annotation workflows reduce costs but require careful validation. Research is needed on optimal annotation budgets, annotator selection methods, and statistical frameworks for validating annotation agreement between humans and LLMs (e.g., the Alt-Test) [2].

### 4.3 Design Principles for Unified Pipelines

**1. System as Unit of Analysis:** MASEval treats the entire agentic system—including framework, orchestration, and error handling—as the unit of analysis, rather than just the model. This principle is essential for evaluating multi-agent systems where framework choice can produce performance variation comparable to model choice [2].

**2. Modular Decoupling:** AgentCompass decouples evaluations into three independent components (Benchmark, Harness, Environment), enabling flexible configurations without reimplementing complex execution logic. This modularity supports rapid experimentation and cross-platform comparisons [2].

**3. Trace-First Evaluation:** MASEval uses trace-first evaluation, collecting detailed traces of agent interactions for post-hoc analysis. This enables process-level diagnostics, failure mode analysis, and interpretable evaluation beyond aggregate scores [2].

**4. Continuous Monitoring and Drift Detection:** Production teams should compute Cohen's kappa between automated judges and human samples before shipping any new rubric, and re-sample monthly to catch judge drift. This principle applies to both single-agent and multi-agent evaluations [2].

**5. Multi-Dimensional Safety and Alignment:** Evaluation pipelines should integrate safety, fairness, robustness, and policy compliance alongside task performance. The HELM framework's multi-metric approach (accuracy, calibration, robustness, fairness, bias, toxicity, efficiency) provides a template. For multi-agent systems, additional dimensions include coordination quality, information diversity, and unnecessary communication [2].

**6. Human-in-the-Loop Validation:** While automated evaluation is essential for scalability, human validation remains critical for nuanced tasks, safety-critical applications, and domain-specific expertise. The hybrid workflow—LLM-as-judge with 5–10% human verification—is the 2026 default, but optimal ratios and sampling strategies require further research [2].

**7. Open Governance and Community Standards:** The shift toward community-governed benchmarks (e.g., BIG-Bench's "living benchmark" accepting new tasks on a rolling basis) and open-source frameworks (e.g., EleutherAI LM Evaluation Harness, AgentCompass, MASEval) promotes transparency, reproducibility, and collective improvement. Future pipelines should adopt open governance models to ensure broad adoption and trust [2].

---

## Conclusion

The evaluation of LLM-based systems has evolved dramatically from 2023 to 2025, driven by the saturation of early benchmarks, the emergence of multi-agent systems, and the growing recognition that evaluation must be multi-dimensional, dynamic, and realistic. Single-agent benchmarks have shifted from static knowledge tests (MMLU, HumanEval, GSM8K) to harder, more specialized evaluations (GPQA, SWE-bench, LiveCodeBench, HLE), while multi-agent benchmarks have introduced entirely new evaluation challenges around coordination, communication, and emergent behaviors (AgentBench, WebArena, SOTOPIA, MetaGPT).

The metrics landscape has similarly expanded from simple exact-match and n-gram metrics to sophisticated LLM-as-judge, agent-as-judge, and process-based evaluation approaches. The recognition that outcome-only metrics are insufficient—particularly for multi-agent systems—has driven the development of process-level metrics (PRMs, GEMMAS, trajectory evaluation) that capture the quality of reasoning and collaboration.

Implementation and cost considerations have become central to evaluation practice, with the hybrid workflow (LLM-as-judge with 5–10% human verification) emerging as the 2026 default. The evaluation platform market, valued at $2.4 billion in 2025 and projected to reach $18.7 billion by 2034, reflects the growing importance of rigorous evaluation infrastructure.

Looking forward, the development of unified, generalizable evaluation pipelines will require progress on multiple fronts: dynamic and living benchmarks, unified metrics and standardization, cross-domain evaluation, automated evaluation with human verification, safety and alignment evaluation, cost-efficiency metrics, process-level evaluation, and scalable human annotation. Design principles such as system-as-unit-of-analysis, modular decoupling, trace-first evaluation, continuous monitoring, multi-dimensional safety, human-in-the-loop validation, and open governance provide a roadmap for building evaluation pipelines that can keep pace with the rapid evolution of LLM-based systems.

The fundamental challenge remains: evaluation must be both rigorous enough to provide meaningful comparisons and practical enough to be adopted across the field. The tension between standardization and flexibility, between automation and human judgment, and between breadth and depth will continue to shape the evolution of evaluation practices for years to come.

---

### Sources

[1] MMLU and MMLU-Pro: [https://arxiv.org/abs/2406.01574](https://arxiv.org/abs/2406.01574)

[2] Survey of Emerging Trends in LLM Agent Benchmarking (ACM 2025): [https://dl.acm.org/doi/10.1145/3711890](https://dl.acm.org/doi/10.1145/3711890)

[3] MMLU-Pro: [https://arxiv.org/abs/2406.01574](https://arxiv.org/abs/2406.01574)

[4] MMLU-Pro Discussion: [https://www.reddit.com/r/LocalLLaMA/comments/1duq5q7/mmlupro_a_more_robust_and_challenging_massive/](https://www.reddit.com/r/LocalLLaMA/comments/1duq5q7/mmlupro_a_more_robust_and_challenging_massive/)

[5] MMLU on EleutherAI: [https://blog.eleuther.ai/mmlu/](https://blog.eleuther.ai/mmlu/)

[6] MMLU Limitations: [https://arxiv.org/abs/2406.04127](https://arxiv.org/abs/2406.04127)

[7] AlpacaEval: [https://tatsu-lab.github.io/alpaca_eval/](https://tatsu-lab.github.io/alpaca_eval/)

[8] AlpacaEval GitHub: [https://github.com/tatsu-lab/alpaca_eval](https://github.com/tatsu-lab/alpaca_eval)

[9] AlpacaEval 2.0: [https://crfm.stanford.edu/2024/04/11/alpacaeval_2.0.html](https://crfm.stanford.edu/2024/04/11/alpacaeval_2.0.html)

[10] AlpacaEval 2.0 Length-Controlled: [https://arxiv.org/abs/2404.04475](https://arxiv.org/abs/2404.04475)

[13] AlpacaEval Instructions: [https://github.com/tatsu-lab/alpaca_eval?tab=readme-ov-file#instructions](https://github.com/tatsu-lab/alpaca_eval?tab=readme-ov-file#instructions)

[14] AlpacaEval 2.0 Paper: [https://arxiv.org/abs/2404.04475](https://arxiv.org/abs/2404.04475)

[15] MMLU Overview: [https://paperswithcode.com/dataset/mmlu](https://paperswithcode.com/dataset/mmlu)

[17] MMLU Construct Validity: [https://www.nytimes.com/2024/11/12/technology/ai-benchmark-mmlu.html](https://www.nytimes.com/2024/11/12/technology/ai-benchmark-mmlu.html)

[19] HumanEval: [https://github.com/openai/human-eval](https://github.com/openai/human-eval)

[20] HumanEval Paper: [https://arxiv.org/abs/2107.03374](https://arxiv.org/abs/2107.03374)

[21] HumanEval Overview: [https://paperswithcode.com/dataset/humaneval](https://paperswithcode.com/dataset/humaneval)

[22] HumanEval Evaluation: [https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/](https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/)

[23] HumanEval Limitations: [https://www.interconnects.ai/p/reflections-on-swe-bench](https://www.interconnects.ai/p/reflections-on-swe-bench)

[24] HumanEval Extensions: [https://arxiv.org/abs/2305.01210](https://arxiv.org/abs/2305.01210)

[25] HumanEval Contamination: [https://arxiv.org/abs/2402.15896](https://arxiv.org/abs/2402.15896)

[26] HumanEval Saturation: [https://www.semianalysis.com/p/ai-evaluation](https://www.semianalysis.com/p/ai-evaluation)

[27] LiveCodeBench: [https://livecodebench.github.io/](https://livecodebench.github.io/)

[28] HumanEval+ Paper: [https://arxiv.org/abs/2305.01210](https://arxiv.org/abs/2305.01210)

[29] HumanEval+ Analysis: [https://blog.allenai.org/humaneval-plus-124c3a5c9f8b](https://blog.allenai.org/humaneval-plus-124c3a5c9f8b)

[30] HumanEval GitHub: [https://github.com/openai/human-eval](https://github.com/openai/human-eval)

[31] GPQA: [https://arxiv.org/abs/2311.12022](https://arxiv.org/abs/2311.12022)

[32] HLE: [https://arxiv.org/abs/2412.10378](https://arxiv.org/abs/2412.10378)

[35] HLE Results: [https://lastexam.ai/](https://lastexam.ai/)

[38] GSM8K: [https://arxiv.org/abs/2110.14168](https://arxiv.org/abs/2110.14168)

[39] GSM-Symbolic: [https://arxiv.org/abs/2404.19274](https://arxiv.org/abs/2404.19274)

[40] GSM8K Overview: [https://paperswithcode.com/dataset/gsm8k](https://paperswithcode.com/dataset/gsm8k)

[41] GSM1k: [https://arxiv.org/abs/2402.17764](https://arxiv.org/abs/2402.17764)

[42] GSM8K OpenAI: [https://openai.com/index/grade-school-math/](https://openai.com/index/grade-school-math/)

[43] GSM8K Survey: [https://arxiv.org/abs/2402.17764](https://arxiv.org/abs/2402.17764)

[44] GSM8K Dataset: [https://github.com/openai/grade-school-math](https://github.com/openai/grade-school-math)

[47] Chatbot Arena Launch: [https://lmsys.org/blog/2023-05-03-arena/](https://lmsys.org/blog/2023-05-03-arena/)

[48] Chatbot Arena Blog: [https://lmsys.org/blog/2024-01-09-arena/](https://lmsys.org/blog/2024-01-09-arena/)

[50] LMArena: [https://lmarena.ai/](https://lmarena.ai/)

[53] Chatbot Arena Paper: [https://arxiv.org/abs/2403.04132](https://arxiv.org/abs/2403.04132)

[57] BIG-Bench: [https://arxiv.org/abs/2206.04615](https://arxiv.org/abs/2206.04615)

[58] BIG-Bench Limitations: [https://arxiv.org/abs/2206.04615](https://arxiv.org/abs/2206.04615)

[59] BIG-Bench Paper: [https://arxiv.org/abs/2206.04615](https://arxiv.org/abs/2206.04615)

[60] SimpleQA Paper: [https://cdn.openai.com/papers/simpleqa.pdf](https://cdn.openai.com/papers/simpleqa.pdf)

[62] BIG-Bench Overview: [https://github.com/google/BIG-bench](https://github.com/google/BIG-bench)

[63] BIG-Bench Analysis: [https://arxiv.org/abs/2206.04615](https://arxiv.org/abs/2206.04615)

[64] BIG-Bench GitHub: [https://github.com/google/BIG-bench](https://github.com/google/BIG-bench)

[65] BIG-Bench Saturation: [https://arxiv.org/abs/2206.04615](https://arxiv.org/abs/2206.04615)

[67] BBEH: [https://arxiv.org/abs/2502.03687](https://arxiv.org/abs/2502.03687)

[68] BBEH Results: [https://arxiv.org/abs/2502.03687](https://arxiv.org/abs/2502.03687)

[69] GPQA Results: [https://arxiv.org/abs/2311.12022](https://arxiv.org/abs/2311.12022)

[72] BBEH Paper: [https://arxiv.org/abs/2502.03687](https://arxiv.org/abs/2502.03687)

[76] HELM Paper: [https://arxiv.org/abs/2211.09110](https://arxiv.org/abs/2211.09110)

[77] HELM Overview: [https://crfm.stanford.edu/helm/latest/](https://crfm.stanford.edu/helm/latest/)

[78] HELM Blog: [https://crfm.stanford.edu/2023/03/27/helm.html](https://crfm.stanford.edu/2023/03/27/helm.html)

[79] HELM Methodology: [https://crfm.stanford.edu/helm/](https://crfm.stanford.edu/helm/)

[80] HELM Limitations: [https://crfm.stanford.edu/2023/03/27/helm.html](https://crfm.stanford.edu/2023/03/27/helm.html)

[81] Stanford HAI 2025 AI Index: [https://hai.stanford.edu/ai-index/2025](https://hai.stanford.edu/ai-index/2025)

[82] HELM Maintenance Mode: [https://github.com/stanford-crfm/helm](https://github.com/stanford-crfm/helm)

[83] HELM Results: [https://arxiv.org/abs/2211.09110](https://arxiv.org/abs/2211.09110)

[84] Stanford HAI 2025 Report: [https://hai.stanford.edu/ai-index/2025](https://hai.stanford.edu/ai-index/2025)

[85] HELM Leaderboard: [https://crfm.stanford.edu/helm/latest/](https://crfm.stanford.edu/helm/latest/)

[86] SWE-bench Verified: [https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/](https://openai.com/index/improving-mathematical-reasoning-with-process-supervision/)

[87] HELM Core Scenarios: [https://crfm.stanford.edu/helm/latest/](https://crfm.stanford.edu/helm/latest/)

[88] SWE-bench Results: [https://www.swebench.com/](https://www.swebench.com/)

[89] HELM Evaluation Details: [https://arxiv.org/abs/2211.09110](https://arxiv.org/abs/2211.09110)

[90] MedHELM: [https://crfm.stanford.edu/2024/07/08/medhelm.html](https://crfm.stanford.edu/2024/07/08/medhelm.html)

[91] VHELM: [https://crfm.stanford.edu/2024/07/08/vhelm.html](https://crfm.stanford.edu/2024/07/08/vhelm.html)
