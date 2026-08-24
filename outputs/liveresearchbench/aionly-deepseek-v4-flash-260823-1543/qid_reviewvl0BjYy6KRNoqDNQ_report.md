# Academic Literature Review: The Evolution of Evaluation Practices for Single-Agent and Multi-Agent LLM Systems (2023–2025)

## Introduction

The rapid advancement of large language models (LLMs) has catalyzed a paradigm shift from static text generation to interactive, goal-oriented agentic systems. These systems—ranging from single agents performing isolated tasks to complex multi-agent societies collaborating on shared objectives—require fundamentally different evaluation approaches than traditional NLP benchmarks. Between 2023 and 2025, the research community has produced over 100 distinct evaluation frameworks, benchmarks, and metrics, reflecting both the urgency and the fragmentation of this emerging field. This report systematically examines the evolution of evaluation practices across four critical dimensions: benchmark design, metric families, implementation costs, and future directions for unified pipelines.

The central tension underlying all current evaluation work is the trade-off between controlled, reproducible measurement and ecological validity. Single-agent benchmarks have achieved high levels of standardization and automation, but increasingly face challenges of data contamination, memorization, and narrow capability assessment. Multi-agent benchmarks better simulate real-world collaborative dynamics, but introduce complexities in credit assignment, evaluation reliability, and computational cost that remain unresolved. This review synthesizes findings from over 60 primary sources—including peer-reviewed conference papers, technical reports, and preprints—to provide a comprehensive mapping of the current landscape and its most promising future directions.

---

## Part 1: Benchmarks and Sandbox Environments

### 1.1 Single-Agent Benchmarks: Controlled Evaluation of Isolated Capabilities

Single-agent benchmarks dominate the current evaluation landscape, reflecting the maturity of standardized testing methodologies inherited from traditional NLP and reinforcement learning. These benchmarks isolate specific competencies—reasoning, tool use, web navigation, code generation—within controlled, reproducible environments.

#### 1.1.1 AgentBench (ICLR 2024)

AgentBench [1] represents one of the first comprehensive attempts to evaluate LLMs as general-purpose agents. It comprises eight distinct environments spanning code-grounded tasks (Operating System, Database, Knowledge Graph), game-grounded tasks (Digital Card Game, Lateral Thinking Puzzles, House-Holding), and web-grounded tasks (Web Shopping, Web Browsing). The benchmark evaluates 29 LLMs across approximately 4,000 development and 13,000 test multi-turn interactions [2].

**Task diversity:** AgentBench is explicitly multi-dimensional, designed to test long-term reasoning, planning, instruction following, and decision-making across structurally different domains. Environments range from structured (OS commands, SQL queries) to open-ended (lateral thinking puzzles, household tasks).

**Scalability:** The framework provides a unified evaluation toolkit with Docker-based environment isolation, HTTP-based model server interfaces, and extensible architecture. The project has evolved through multiple versions, including AgentBench FC (function calling integration with AgentRL), VisualAgentBench (multimodal agents), and ongoing community contributions [3].

**Realism and limitations:** Key findings reveal a dramatic performance gap between commercial and open-source models: GPT-4 achieves an overall score of 4.01, while the best open-source model (CodeLlama-34B) scores only 0.96 [4]. The primary failure modes are Task Limit Exceeded (67.9% in Knowledge Graph, 82.5% in Lateral Thinking Puzzles), Invalid Format errors, and Invalid Action errors. Code training shows ambivalent effects—helping procedural tasks like web shopping but hindering general thinking in games. The benchmark requires significant computational resources (4k–13k generations per evaluation), and scores may not transfer to specific production use cases [1].

#### 1.1.2 WebArena (NeurIPS 2024)

WebArena [5] provides a more ecologically valid evaluation by replicating fully functional web environments—e-commerce (90,000+ products), social forums (95 subforums, 127,390 posts), collaborative software development (GitLab-like, 300+ repos), and content management systems. The benchmark consists of 812 long-horizon tasks instantiated from 241 templates across four categories: information seeking, site navigation, content/configuration operations, and unachievable tasks requiring agents to recognize impossibility [6].

**Task diversity:** Tasks span diverse categories with varying complexity, from single-step information retrieval to multi-step configuration operations. Extended challenge suites include WebChoreArena (532 tedium-focused tasks), ST-WebAgentBench (safety/trust templates), and VisualWebArena (910 multimodal tasks across classifieds, shopping, and Reddit environments) [7].

**Realism and performance:** Initial results showed GPT-4-based agents achieving only 14.41% success versus a human baseline of 78.24%. Record single-agent performance has since risen to 61.7% (IBM CUGA, February 2025) through techniques including automatic evaluation with reflexion (29% SOTA gain), self-improvement via synthetic data (31% relative increase), workflow memory and skill abstraction (51% relative success boost), and structured exploration with contextual experience replay [5].

**Critical reliability concerns:** A 2025 analysis (WAREX) found that WebArena partially relies on LLM-as-a-Judge that makes mistakes for problems as simple as '45+8≠63'. Network errors caused the most severe degradation, with success rates dropping by 70–95% depending on the benchmark. In malicious popup experiments, GPT-4o clicked the malicious button 97.3% of the time, Qwen2.5-VL 86.6%, and GPT-OSS 98.2%. Simple prompting improvements (e.g., "refresh the page on transient errors") helped but did not fully restore baseline performance [8].

#### 1.1.3 SWE-bench (ICLR 2024)

SWE-bench [9] evaluates LLMs on real-world software engineering tasks from GitHub. Given a codebase and a GitHub issue, the model must generate a patch that resolves the problem. The original benchmark comprises 2,294 unique software engineering problems from 12 popular Python repositories. SWE-bench Verified is a human-validated subset of 500 engineer-confirmed solvable problems [10].

**Task diversity:** Tasks cover a wide range of coding scenarios including bug fixes and feature requests, categorized by estimated resolution time (<15 min, 15m–1h, 1–4 hr, >4 hr). Tasks require navigating large codebases, understanding cross-file function interactions, identifying subtle errors, and generating patches [9].

**Scalability:** The project has evolved significantly with SWE-bench LITE, SWE-bench Multimodal, SWE-bench C#, RefactorBench, and SWE-bench-Live (a live-updating benchmark with 1,319 task instances from 93 repositories). Performance has shown dramatic improvement: Claude Opus 5 now achieves 97.00% on SWE-bench Verified, while the original Claude 2 solved only 1.96% of issues [11].

**Major memorization concerns:** A 2025 paper titled "The SWE-Bench Illusion" [12] found that state-of-the-art models achieve up to 76% accuracy in identifying buggy file paths using only issue descriptions, without access to repository structure. This performance drops to merely 53% on tasks from repositories not included in SWE-Bench, pointing to systematic data contamination. Models achieve up to 34.9% 5-gram overlap ratio reproducing ground truth functions from SWE-Bench Verified compared to 18.2% on instances outside the SWE-Bench ecosystem. The Claude family exhibits a monotonic increase in memorization rates corresponding to model generation, rising from 12.1% to 31.6% for prefix completion verbatim matches [12].

#### 1.1.4 GAIA (Meta FAIR, 2023)

GAIA (General AI Assistant) [13] represents a philosophical shift in AI benchmarking—focusing on tasks that are conceptually simple for humans but challenging for AI. The benchmark consists of 466 human-crafted questions divided into three difficulty levels: Level 1 (fewer than 5 steps, minimal tool use), Level 2 (5–10 steps, multiple tools), and Level 3 (long-term planning, sophisticated tool integration). Questions require reasoning, multi-modality handling, web browsing, coding, and diverse filetype reading (Excel, PNG, PDF, text) [14].

**Realism and human baseline:** Human respondents achieve 92% accuracy, while GPT-4 with plugins scores only 15%. The current top performer (Claude Sonnet 4.5 with HAL Generalist Agent, September 2025) achieves 74.55% accuracy at $178.20 cost. The most cost-effective entry (Gemini 2.0 Flash with HAL) achieves 32.73% at $7.80 total cost. About 5% of GAIA data contains errors or ambiguities in ground truth answers [15].

**Key insight:** The dramatic human-AI gap (92% vs. 15% initially) confirms that current AI systems lack the robustness and common-sense reasoning required for practical, real-world tasks. The benchmark's guiding principles—real-world difficulty, human interpretability, non-gameability, and simplicity of evaluation—have influenced subsequent benchmark design [13].

#### 1.1.5 ToolBench (ICLR 2024)

ToolBench [16] evaluates LLM tool-use capabilities with over 16,000 APIs and 3,451 tools across 49 categories sourced from RapidAPI. The dataset contains 126,486 instruction instances, 469,585 total API calls, and 4.0 average reasoning traces per instruction. The benchmark includes both single-step and multi-step instructions, with automated instruction generation and solution path annotation using ChatGPT and a Depth-First Search Decision Tree approach [17].

**Quality issues:** Up to 50% of queries and 75% of trajectories had hallucinations or incompleteness, later addressed by rigorous multi-agent verification. StableToolBench [18] evolved to address evaluation instability due to real-world API changes, introducing a virtual API server with caching systems and API simulators. Only 44.4% of API calls were successful in the original benchmark, with 49.2% unavailable and 6.4% not authorized [18].

**Metrics and findings:** The ToolEval machine evaluator shows 87.1% agreement with humans on pass rate and 80.3% on win rate. Empirical results show that open-source LLMs trained on ToolBench have improved from 10–37% pass rates to over 70%, approaching GPT-4. Key findings include that LLMs struggle with complex multi-step planning (average accuracy below 50%), semantic-functional gaps in tool retrieval, and safety limitations in privacy and physical injury domains (<30% recall) [16].

#### 1.1.6 Other Notable Single-Agent Benchmarks

**OSWorld** (NeurIPS 2024): Realistic OS tasks where the best model achieves 12.2% success vs. 72.4% human performance, exposing a large competence gap in GUI grounding. A 2025 analysis found that OSWorld relies on outdated websites, leading to 28% underestimation of agent capabilities [19].

**τ-bench:** A benchmark for evaluating LLM agents where a 2025 analysis found that τ-bench scores a "do-nothing" agent as correct on 38% of airline tasks, even though the trivial agent does not understand the airline ticketing policy [19].

**General reliability concerns:** The AI Agent Benchmark Checklist (ABC), a 43-item framework developed from 17 existing benchmarks, found severe issues in 8 of 10 popular benchmarks (including SWE-bench, WebArena, OSWorld, KernelBench, τ-bench, and SWE-Lancer), causing up to 100% misestimation of agent capabilities [19].

### 1.2 Multi-Agent Benchmarks: Evaluating Collaboration and Emergent Behavior

Multi-agent benchmarks represent a newer and more complex evaluation paradigm, designed to assess not just individual capabilities but also coordination, communication, social intelligence, and emergent collective behaviors.

#### 1.2.1 SOTOPIA (ICLR 2024)

SOTOPIA [20] is an open-ended environment for simulating complex social interactions between artificial agents and evaluating their social intelligence. The task space includes 90 social scenarios spanning cooperative, competitive, and mixed goals, with 40 characters (each with personality, values, decision-making style, secrets) and 5 relationship types (family, friend, romantic, acquaintance, stranger) [21].

**Multidimensional evaluation:** SOTOPIA scores agents along seven dimensions: Goal achievement (0–10), Believability (0–10), Knowledge (0–10), Secret concealment (-10 to 0), Relationship (-5 to 5), Social Rules (-10 to 0), and Financial/Material outcomes (-5 to 5). The "Sotopia-hard" subset identifies systematic model failures where even GPT-4 underperforms humans, particularly in cases requiring strategic communication, social commonsense, or theory-of-mind reasoning [20].

**Key findings:** GPT-4 achieves a significantly lower goal completion rate than humans and struggles to exhibit social commonsense reasoning and strategic communication skills. Weaker partner models negatively impact stronger models' performance, highlighting the cooperative nature of social tasks. GPT-4 can serve as a proxy for human evaluation on certain dimensions (especially Goal Completion), with >74% of GPT-4 scores within one standard deviation of human scores. However, there is an increasing gap between GPT-4-based and human evaluation as models are optimized for GPT-4 ratings, highlighting limitations of LLM-based evaluation [22].

**Extensions:** SOTOPIA-π (ACL 2024) allows a 7B LLM (Mistral-7B) to approach the social goal completion ability of GPT-4, achieving a goal completion score of 5.71 vs. GPT-4's 5.89. Sotopia-RL introduces utterance-level, multi-dimensional reward modeling with GRPO optimization. Sotopia-ToM extends the framework with both public and private communication channels, evaluating information management in multi-agent interaction with Theory of Mind, and includes 160 human-reviewed scenarios across 8 sectors [23].

#### 1.2.2 ChatEval (ICLR 2024)

ChatEval [24] is a multi-agent debate framework for automating the evaluation of natural language generation (NLG) systems using LLMs as evaluators. It replaces conventional single-agent LLM-based judgment with teams of simulated "referees" that discuss, critique, and ultimately score or rank candidate responses. Multiple LLM agents with diverse role prompts (e.g., General Public, Critic, News Author, Psychologist, Scientist) collaboratively evaluate text quality through structured discussion [25].

**Communication strategies:** Three strategies are employed: One-by-One (sequential, building on previous responses), Simultaneous-Talk (asynchronous independent responses), and Simultaneous-Talk-with-Summarizer (with an additional LLM summarizing each round). After T rounds, agents independently issue final scores without explicit consensus. Diverse role prompts are essential—using identical role descriptions degrades performance to single-agent levels [24].

**Performance:** On the FairEval benchmark, ChatEval improved accuracy by 6.2% for ChatGPT and 2.5% for GPT-4 over single-agent baselines, achieving 60.0% and 63.8% accuracy respectively. On Topical-Chat, ChatEval with GPT-4 improved average Spearman correlation by 0.096 (16.3%) over G-EVAL-4. Ensemble methods (without debate) failed to match ChatEval's performance, highlighting the crucial role of natural language interaction [25].

**Limitations:** Higher computational cost (N agents × T rounds), dependency on underlying LLM capabilities, prompt sensitivity, potential for "group-think" convergence on incorrect judgments, and lack of statistical significance testing in reported results. The study used homogeneous LLM groups (all GPT-4 or all ChatGPT) [24].

#### 1.2.3 MultiAgentBench (2025)

MultiAgentBench [26] is a comprehensive benchmark suite for evaluating LLM-based multi-agent systems across both cooperative and adversarial scenarios. Task-oriented scenarios include Research Collaboration, Minecraft Building, Database Error Analysis, and Coding Collaboration. Social simulation scenarios include Bargaining and Werewolf (social deduction) [27].

**Milestone-based KPI framework:** Agent contributions are measured by milestone achievements, with secondary metrics including Communication Score, Planning Score, and Coordination Score. The benchmark systematically compares four coordination topologies: Star (centralized), Tree (hierarchical), Chain (sequential), and Graph-Mesh (fully decentralized) [26].

**Key findings:** GPT-4o-mini achieves the highest average task and coordination scores. The Graph-Mesh topology yields the best task score, planning efficiency, and moderate token consumption, outperforming both hierarchical and chain structures. Cognitive self-evolving planning achieves the highest coordination score (~4.8/5) with milestone achievement rates comparable to chain-of-thought prompting. Increasing agent count decreases per-agent contribution but increases total task score until saturation. Emergent behaviors include strategic information sharing, trust polarization, and role-driven dynamics [27].

#### 1.2.4 ChatDev (2023) and MetaGPT (ICLR 2024)

**ChatDev** [28] is a chat-powered software development architecture where specialized agents cooperate via structured multi-turn dialogues to drive the software engineering lifecycle. Agents (e.g., CEO, CTO, CPO, programmer, designer, tester, reviewer) engage in structured "chat chains" with natural language for reasoning and programming language for code artifacts. The architecture follows the waterfall model with four phases: Designing, Coding, Testing, and Documenting [29].

ChatDev achieved end-to-end project completion in under seven minutes at under $1 per project (using ChatGPT-turbo-16k). The average software development cost was $0.2967, and it took 409.84 seconds on average to develop small-sized software. Discussions between agents led to identification and resolution of nearly 20 types of code vulnerabilities. ChatDev 2.0 (DevAll, NeurIPS 2025) evolved into a zero-code multi-agent orchestration platform supporting scenarios like data visualization, 3D generation, deep research, and game development [30].

**MetaGPT** [31] integrates human-like Standardized Operating Procedures (SOPs) into LLM-based multi-agent collaborations. It assigns distinct roles (Product Manager, Architect, Project Manager, Engineer, QA Engineer), each following SOPs encoded in prompts. The framework takes a single one-line prompt and decomposes the task through its assembly line of roles. Key innovations include encoding SOPs into prompts, enforcing standardized output schemas, structured communication interfaces with a publish-subscribe mechanism, and an executable feedback loop for iterative code debugging [32].

MetaGPT with GPT-4 achieves state-of-the-art Pass@1 scores of 85.9% on HumanEval and 87.7% on MBPP. On the custom SoftwareDev benchmark, MetaGPT achieved higher executability (3.75 vs 2.25) and lower human revision cost (0.83 vs 2.5) compared to ChatDev. The central thesis reframes multi-agent collaboration from "more agents means more intelligence" to emphasizing workflow design, typed intermediate artifacts, explicit dependencies, and grounded verification over verbal reassurance [31].

#### 1.2.5 Other Notable Multi-Agent Evaluation Frameworks

**MASEval** [33] is a framework-agnostic evaluation library that addresses the gap in existing benchmarks being predominantly model-centric. Key finding: Across 3 benchmarks (MACS, ConVerse, MultiAgentBench), 3 models (GPT-5-mini, Gemini-3.0-Flash, Claude-Haiku-4.5), and 3 frameworks (smolagents, LangGraph, LlamaIndex), framework choice impacts performance comparably to model choice. The mean performance range across models was 14.2 percentage points (pp) and across frameworks was 12.4 pp. A striking example: Haiku 4.5 scored 90.4 on MACS Travel with smolagents but only 59.5 with LlamaIndex—a 30.9 pp gap. MASEval reduces implementation effort by 83–91% for benchmark consumers and 35–57% for benchmark producers [33].

**AgentRecBench** [34] (NeurIPS 2025) is the first comprehensive benchmark for evaluating LLM-based agentic recommender systems. It provides an interactive textual recommendation simulator integrating three large-scale datasets (Yelp, GoodReads, Amazon) into a unified User-Review-Item network. Three evaluation scenarios are included: Classic recommendation, Evolving-interest recommendation, and Cold-start recommendation. Agentic systems significantly outperform traditional methods (MF and LightGCN scored ~15% on classic tasks vs. agentic systems reaching up to 69% HR@N). Three core design principles were identified: effective workflows combine user history, candidate items, item details, and platform-specific features; platform-specific item attribute extraction enhances performance; prioritizing highly relevant, information-rich reviews improves ranking quality [34].

### 1.3 Comparative Analysis: Single-Agent vs. Multi-Agent Benchmark Trade-offs

The construction of single-agent and multi-agent benchmarks involves fundamentally different trade-offs that reflect their distinct evaluation objectives.

| Aspect | Single-Agent Benchmarks | Multi-Agent Benchmarks |
|--------|------------------------|------------------------|
| **Construction Cost** | Lower (Docker, standardized tasks, well-defined success criteria) | Higher (complex interaction protocols, managing multiple agents, communication dynamics) |
| **Evaluation Metrics** | Well-defined, standardized (success rate, accuracy, F1, pass@k) | Evolving, multi-dimensional (coordination, communication quality, emergent behavior, social intelligence) |
| **Task Scope** | Narrower, focused on specific isolated capabilities | Broader, testing collaboration, communication, and social interaction |
| **Reproducibility** | High (containerized, deterministic environments) | Lower (stochastic interactions, path-dependent, partner model effects) |
| **Ecological Validity** | Moderate (improving with realistic environments like WebArena, SWE-bench) | Higher (simulates real collaborative scenarios, social dynamics) |
| **Data Contamination Risk** | High (documented in SWE-Bench, GAIA memorization concerns) | Lower (dynamic interactions harder to memorize, but still possible) |
| **Scalability** | High (thousands of tasks, automated evaluation) | Moderate (context limits, dialogue complexity, beyond ~50 agents challenges) |
| **Human Baseline** | Easier to establish (single human performance) | More complex (multi-party evaluation, social dynamics difficult to baseline) |
| **Computational Cost** | Moderate (4k–13k generations per evaluation) | Higher (N agents × T rounds of interaction) |
| **Framework Dependency** | Low (model-centric evaluation) | High (MASEval: framework choice matters as much as model choice) |

**Key trade-offs identified:**

1. **Controlled vs. Open-ended:** Single-agent benchmarks provide controlled environments that isolate specific capabilities, making them suitable for comparing model families on standardized tasks. Multi-agent benchmarks allow for emergent behaviors and diverse interaction patterns, making them more representative of real-world deployment but harder to interpret.

2. **Static vs. Dynamic:** Single-agent benchmarks are increasingly static, leading to data contamination concerns. SWE-bench-Live and GAIA represent attempts to address this through live updates. Multi-agent benchmarks are inherently dynamic—agent responses shape the interaction—but this dynamism makes reproducibility challenging.

3. **Capability vs. Reliability:** Most benchmarks measure capability (what an agent can achieve, perhaps infrequently) rather than reliability (consistent, correct performance). The pass@k metric captures capability but not reliability. Multi-agent benchmarks like MultiAgentBench's milestone-based KPI framework attempt to address this through process-level evaluation.

4. **Ecological validity vs. Controlled measurement:** Benchmarks like WebArena and SWE-bench achieve high ecological validity through real-world environments, but WAREX showed that real-world factors (network errors, malicious popups) cause 70–95% degradation in performance, suggesting current benchmarks overestimate real-world robustness. Multi-agent benchmarks like SOTOPIA achieve higher ecological validity for social interactions but face challenges in generalizing across interaction contexts.

---

## Part 2: Evaluation Metrics

### 2.1 Single-Agent Metric Families

#### 2.1.1 Success Rate / Task Completion Rate (Code-Based, Functional Correctness)

Success rate is the most fundamental metric, defined as the fraction of episodes in which the agent fully completes the task. It is used across virtually all major benchmarks [35].

**AgentBench** evaluates LLMs across 8 environments using success rate, F1 score, overall reward, game progress, and step success rate, normalized to a single overall score using reciprocal-mean weights. Key findings: GPT-4 achieves 78% success rate on House Holding and leads on 6 of 8 tasks. Common failure modes include Task Limit Exceeded (weak reasoning/decision-making), Invalid Format (poor instruction following), and Invalid Action [1].

**WebArena** uses functional end-to-end correctness: a task is scored as correct if the agent's actions bring the environment to a state that satisfies the user intent, regardless of the stepwise trajectory. Initial results showed GPT-4-based agents achieving only 14.41% success rate (vs. 78.24% human baseline). Record single-agent performance has risen to 61.7% (IBM CUGA, February 2025) [5].

**Pass@k and Consistency:** The pass@k metric measures capability across repeated trials, while pass@k (with k being the number of trials) captures reliability. Most benchmarks measure capability (what an agent can achieve, perhaps infrequently), but real-world applications demand reliability (consistent, correct performance). Goodhart's Law is highlighted as a risk in agent evaluation: "when a measure becomes a target, it ceases to be a good measure. This is particularly acute in agent evaluation: once an agent system is optimized heavily against a specific benchmark, it may learn to exploit benchmark-specific patterns rather than develop generalizable capabilities" [35].

**Evaluation Method: Code-based, deterministic.**

#### 2.1.2 Exact Match / F1 / BLEU / ROUGE (String Matching)

Conventional reference-based metrics have been shown to have relatively low correlation with human judgments, especially for tasks requiring creativity and diversity (G-Eval, Liu et al., EMNLP 2023). In agent evaluation, exact match and F1 are used for tool-use metrics: parameter F1 (correctness of API call formatting), selection accuracy (fraction of turns where the agent picks the appropriate tool), and tool-match accuracy [36].

**Evaluation Method: Code-based, deterministic string matching.**

#### 2.1.3 LLM-as-Judge

LLM-as-Judge refers to using Large Language Models as evaluators for complex tasks, combining the scalability of automatic methods with the nuanced, context-sensitive reasoning found in expert judgments [37]. LLM-as-a-Judge encompasses roles as graders, evaluators, critics, verifiers, examiners, and reward models.

**Evaluation methods (pipeline):**
1. **In-Context Learning (Prompt Design):** Four evaluation methods—generating scores, solving Yes/No questions, conducting pairwise comparisons, and making multiple-choice selections.
2. **Model Selection:** General LLMs (e.g., GPT-4) or fine-tuned LLMs (e.g., PandaLM, JudgeLM, Auto-J, Prometheus).
3. **Post-processing Methods:** Extracting specific tokens, constrained decoding, normalizing output logits, and selecting sentences [37].

**Scoring approaches:** Direct scoring (versatile, for objective tasks like faithfulness), pairwise comparison (more reliable for subjective evals like persuasiveness), and reference-based evaluation (compares to a gold standard). LLM-evaluators that adopt pairwise comparison generally outperform those that adopt direct scoring and G-Eval approaches [38].

**Performance:** GPT-4 achieved Spearman's ρ of 0.67 for correctness and 0.55 for faithfulness in QA tasks. For summarization, GPT-3.5-turbo showed moderate correlation with humans (0.3–0.6), outperforming ROUGE and BERTScore but below human-human correlation (0.8–0.9). For factual inconsistency detection, GPT-3.5 identified >95% of consistent summaries but only 30–60% of inconsistent ones [38].

**Bias issues:** When directly utilizing LLMs to conduct evaluation tasks, inherent biases like length bias, position bias, and concreteness bias lead to poor evaluation results. A Panel of smaller LLMs (PoLL) achieved higher human correlation than GPT-4 alone at one-seventh the cost [38].

**Fine-tuned judges:** Prometheus (finetuned Llama-2-chat) achieved 0.897 Pearson correlation with human judgments vs. GPT-4's 0.882, and was preferred over GPT-4 58.6% of the time in pairwise human comparisons. Best practices include few-shot prompting (1–2 examples; more can hurt performance), step decomposition, criteria decomposition, evaluation templates with categorical integer scoring scales, constraining to structured outputs (JSON), providing explanations (chain-of-thought reasoning), and score smoothing [39].

**Evaluation Method: LLM-as-judge (subjective evaluation by an LLM).**

#### 2.1.4 Human Evaluation (Gold Standard)

Human evaluation is considered the gold standard for nuanced tasks. EvalLM helps refine evaluation criteria iteratively—users reported higher confidence (6.71 vs 4.96), evaluated more outputs (20.42 vs 10.08), and lower mental burden (3.92 vs 5.58). EvalGen addresses 'criteria drift' and achieved 0.73 recall of defects vs 0.49 for baseline. Users preferred GUI for low-level constraints (e.g., JSON output) but natural language for high-level constraints (e.g., tone) [38].

**Evaluation Method: Human-in-the-loop.**

#### 2.1.5 Efficiency Metrics

Efficiency metrics track step count, token cost, latency, API cost, and efficiency ratio. The survey on Evaluation and Benchmarking of LLM Agents lists latency/cost as part of Agent Behavior evaluation objectives, including TTFT (time to first token) and token usage. Redundancy and loop detection includes n-gram repetition, state similarity, dead-end detection, and stagnation windows [35].

**Critical gap:** Efficiency and cost are second-class metrics—compute time, token usage, and monetary costs are rarely reported in benchmarks. This is identified as a key future direction [35].

**Evaluation Method: Code-based, deterministic measurement.**

#### 2.1.6 Robustness Metrics

Robustness tests performance under paraphrased, noisy, or adversarial inputs. The Self-Evolving benchmark (2024) dynamically generates perturbed test instances to measure robustness via performance drop on evolved variants. The key metric is often the gap between a model's original accuracy and its accuracy on reframed instances [36].

**Safety evaluation:** Agent evaluation addresses tool misuse detection (forbidden action detection, argument validation, confirmation bypass, scope violation), adversarial robustness (direct/indirect prompt injection, tool poisoning, goal hijacking, jailbreak escalation, measured by attack success rate and defense success rate), and sandboxing/capability constraints [35].

**Critical observation:** "A chatbot that produces harmful text can be caught by output filters before causing downstream harm. An agent that takes harmful actions may produce entirely benign text while executing devastating tool calls" [35]. AgentAuditor introduces ASSEBench, the first large-scale benchmark (2,293 annotated records, 15 risk types, 29 scenarios) for LLM-based evaluators covering both agent safety and security, achieving human-level accuracy (e.g., 96.3% F1, 96.1% accuracy on R-Judge with Gemini-2.0-Flash-thinking) [40].

**Evaluation Method: Code-based (deterministic perturbation evaluation) + LLM-as-judge for open-ended attacks.**

### 2.2 Multi-Agent Metric Families

#### 2.2.1 Task Completion / Goal Achievement in Collaborative Settings

**MultiAgentBench** employs milestone-based Key Performance Indicators (KPIs) that measure not just task completion but also qualitative aspects of agent interaction. Key metrics include Task Score (TS), Coordination Score (CS), Communication Score, Planning Score, and Competition Score. The benchmark uses an LLM-based detector to track which milestones are achieved, providing process-level evaluation [26].

**Key findings:** GPT-4o-mini achieved the highest average task scores (e.g., 84.13% in Research, 65.10% in Coding). The Graph-Mesh topology yields the best task score, planning efficiency, and moderate token consumption. Cognitive self-evolving planning achieves the highest coordination score (~4.8/5) with milestone achievement rates comparable to chain-of-thought prompting. Increasing agent numbers beyond a threshold introduces coordination challenges that counterbalance performance gains [27].

**Evaluation Method: Code-based (functional correctness) + LLM-as-judge (milestone detection).**

#### 2.2.2 Communication Quality Metrics

Communication quality metrics include coordination efficiency (task success per communication, e.g., milestones achieved per message/token), communication quality and overhead (LLM-judged scores for message clarity, relevance, and planning coherence, combined into a Coordination Score), and plan and reasoning quality (rubric-based scoring of joint plans for completeness, logic, and feasibility) [36].

**MultiAgentBench** systematically compares four coordination topologies: Star, Tree, Chain, and Graph-Mesh. Ablation studies show that Graph-Mesh topology yields the best task scores and planning efficiency. Communication paradigms in LLM-MAS include memory-based, report-based, relay, and debate protocols across various network topologies [36].

**Evaluation Method: LLM-as-judge.**

#### 2.2.3 Social Metrics

Social metrics include alignment and fairness (interactional fairness—respectful tone, transparency; outcome fairness—equitable task distribution) and trust metrics. The Trust-Aware Coordination Framework introduces a multi-dimensional trust evaluation mechanism that continuously assesses agent reliability based on three dimensions: performance history (weight α=0.40), interaction quality (β=0.35), and behavioral consistency (γ=0.25). The coordinator uses these trust scores to dynamically assign roles (with a trust threshold τ=0.70 for leadership roles) [41].

**Trust framework results:** 87.4% task success rate (vs. 62.3% baseline and 71.5% static assignment), 36.3% reduction in execution time (156.2 seconds vs. 245.3 seconds baseline), 43.2% lower communication overhead. Trust scores for high-performing agents rose from 0.65 to 0.87 over ten iterations, crossing the leadership threshold by iteration three [41].

**Shapley-Coop** (NeurIPS 2025) proposes a cooperative workflow that enables self-interested LLM agents to engage in emergent collaboration through fair credit allocation. It introduces structured negotiation protocols and Shapley-inspired reasoning to estimate agents' marginal contributions, enabling effective task-time coordination and equitable post-task outcome redistribution [42].

**Evaluation Method: LLM-as-judge + Agent-as-judge + Human evaluation.**

#### 2.2.4 Agent-as-Judge

Agent-as-Judge is listed as a metrics computation method in the Evaluation and Benchmarking of LLM Agents survey [35]. Multi-Agent-as-Judge (MAJ-Eval) uses multiple LLM agents with diverse personas to simulate multidimensional human judgment through dimension extraction, persona construction, agent instantiation, and debate protocol. Achieves Spearman's ρ=0.43–0.47 alignment with expert human ratings. Empirical studies show that MAJ-Eval yields higher alignment with expert human ratings than ROUGE/BERTScore or single-LLM-judge baselines [43].

**Failure Attribution:** Tracing which agent or step caused breakdowns. Even state-of-the-art models are only ~50% accurate in tracing failures. This is a critical challenge for multi-agent evaluation [36].

**Evaluation Method: Agent-as-judge (one agent evaluates another agent's output).**

#### 2.2.5 LLM-as-Judge for Multi-Agent Interactions

The survey on LLM-as-a-Judge covers four application scenarios: LLM-as-a-Judge for Models, Data, Agents, and Reasoning/Thinking. AgentAuditor is a training-free, memory-augmented reasoning framework for evaluating the safety and security of LLM-based agents, working in three stages: Feature Memory Construction (transforms raw agent interactions into structured semantic features), Reasoning Memory Construction (selects representative samples via FINCH clustering and generates high-quality Chain-of-Thought reasoning traces), and Memory-Augmented Reasoning (uses multi-stage RAG to retrieve the most relevant CoT examples to guide evaluation of new cases) [40].

**LLM-as-Critic paradigm:** The LLM itself can serve as a critic, providing natural-language evaluations of intermediate states. This 'LLM-as-Critic' paradigm has no direct classical analogue and represents a distinctive axis of credit assignment methodology [44].

**Evaluation Method: LLM-as-judge.**

#### 2.2.6 Human Evaluation for Multi-Agent Dialogues

Human evaluation is used for multi-agent dialogues and is considered the gold standard. The survey of multi-agent LLM evaluations (LessWrong) surveyed 32 academic papers on multi-agent LLM evaluations, analyzing how they measure dangerous failure modes in systems where multiple AI agents interact. 26 out of 32 papers measured miscoordination failure modes, while only 5 papers measured collusion failure modes. Across all multi-agent failure modes, there exist very few evaluations based on AI threat models. Current evaluations are inadequate for measuring risks from substantial AI R&D automation [45].

**Evaluation Method: Human-in-the-loop.**

#### 2.2.7 Efficiency and Scalability Metrics

Efficiency and scalability metrics for multi-agent systems include communication overhead (e.g., 43.2% lower communication overhead in trust-aware framework), rounds of interaction, step count and token cost, execution time (e.g., 36.3% reduction: 156.2 seconds vs. 245.3 seconds baseline), and scalability constraints beyond ~50 agents in current trust models [41].

**Critical gap:** Efficiency and cost are second-class metrics—compute time, token usage, and monetary costs are rarely reported in benchmarks. CrewAI demonstrates 5.76x faster execution than LangGraph in certain tasks, highlighting the importance of framework-level efficiency [36].

**Evaluation Method: Code-based (deterministic measurement).**

### 2.3 Comparative Analysis: Single-Agent vs. Multi-Agent Metrics

The metric landscape for single-agent and multi-agent systems reflects fundamentally different evaluation philosophies and challenges.

**Single-agent metrics** are characterized by:
- **Standardization:** Well-defined, widely accepted metrics (success rate, accuracy, F1, pass@k)
- **Automation:** Code-based evaluation is predominant, with LLM-as-judge as a growing alternative
- **Clarity:** Clear link between agent actions and evaluation outcomes
- **Limitations:** Binary success/failure fails to capture partial progress; LLM-as-judge has documented biases; memorization concerns in static benchmarks

**Multi-agent metrics** are characterized by:
- **Multi-dimensionality:** No single metric captures multi-agent performance; composite scores are needed (coordination, communication, social intelligence)
- **Credit assignment:** The fundamental challenge of attributing outcomes to individual agents, with trajectory complexity making the problem severe (100–500K+ tokens per trajectory vs. 500–30K for reasoning)
- **Emergent behavior measurement:** Social metrics (trust, fairness, collusion) have no single-agent analogues
- **Reliability challenges:** LLM-based evaluation increasingly unreliable as models are optimized for LLM ratings; partner model effects complicate interpretation

**The credit assignment problem:** The survey "From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models" (2024–2026) reviews 47 CA methods organized by a two-dimensional taxonomy: granularity (token, segment, step, turn, multi-agent) and methodology (Monte Carlo, temporal difference, model-based, game-theoretic, information-theoretic). The severity scales with trajectory complexity: in agentic RL, trajectories span 10–100+ turns, with total token counts routinely reaching 100K–500K+. With T=100 turns and binary reward, the signal-to-noise ratio per action is roughly 100× worse than in the single-turn reasoning setting [44].

**LLM-MCA** (AAMAS 2025) reformulates credit assignment as a pattern recognition problem solvable by LLMs. The approach uses a centralized LLM reward-critic that numerically decomposes the overall reward based on each agent's individual contribution. Both LLM-MCA and LLM-TACA far outperform the state-of-the-art on Level-Based Foraging, Robotic Warehouse, and a new 'Spaceworld' benchmark [46].

---

## Part 3: Implementation and Cost

### 3.1 Single-Agent Benchmark Implementation

#### 3.1.1 AgentBench Implementation

AgentBench provides a fully open-sourced evaluation toolkit with Docker-based environment isolation and HTTP-based model server interface. The architecture is decoupled: a Server-Client model where the evaluation server manages environments via Docker containers, and the client communicates with the LLM through HTTP APIs. This design supports resumable evaluation and extensibility—new tasks can be added through the same interface [1].

**Human annotation:** The benchmark does not prominently feature human annotation as a core component of its evaluation pipeline, but the tasks are manually curated across the eight environments. The evaluation process is automated through Docker containers and the model server interface.

**Scalability and reliability:** The benchmark evaluates 29 LLMs across 4k–13k generations per evaluation. Key reliability findings: GPT-4 achieved the highest overall score of 4.01, outperforming in 6 of 8 tasks. The mean performance gap was 2.15 (commercial) vs. 0.51 (open-source). Diagnosed failure modes include Task Limit Exceeded (predominant issue: 67.9% in KG, 82.5% in LTP), Invalid Format errors (notable in DB/DCG: 53% in DB), and Invalid Action in HH/WB [4].

**Cost:** The high computational cost is noted—"high complexity and computational cost; results may not transfer to your specific use cases or custom environments." A key distinction is made: "A benchmark score is not production reliability. In production, tools return real errors, retrieval returns stale documents, and prompts are modified by multiple people" [1].

#### 3.1.2 WebArena Implementation

WebArena provides a standalone, self-hostable web environment delivered via Docker containers for reproducibility. The environment includes four fully functional, self-hosted web applications: e-commerce (OneStopShop with 90,000+ products), social forum discussions (Reddit/Postmill with 95 subforums, 127,390 posts), collaborative software development (GitLab with 300+ repos), and content management (CMS). Utility tools (map, calculator, scratchpad) and knowledge bases (offline Wikipedia, user manuals) are also incorporated [6].

**Human annotation:** The benchmark consists of 812 long-horizon web-based tasks derived from 241 templates. Human-annotated trajectory recordings on ~170 tasks were released on 12/21/2023. Human baseline performance was established at 78.24% [5].

**Scalability and reliability:** Extended challenge suites include WebChoreArena (532 tedium-focused tasks), ST-WebAgentBench (safety/trust templates), and Varco Arena (tournament-style reference-free evaluation). Initial results showed GPT-4-based agents achieving only 14.41% success. The benchmark was re-examined and dataset annotation bugs were fixed (v0.2.0 on 10/24/2023). Despite advances to 61.7% (IBM CUGA, February 2025), persistent challenges remain in memory limitations, evaluation precision, policy/safety alignment, and generalization [5].

**WAREX findings:** Network errors caused 70–95% degradation in performance. In malicious popup experiments, GPT-4o clicked the malicious button 97.3% of the time. Simple prompting improvements helped but did not fully restore baseline performance [8].

**Cost:** The environment is self-hosted via Docker, requiring compute resources to run the full suite of web applications. The project provides an Amazon Machine Image for pre-installed websites. The significant gap between human (78.24%) and AI (14.41%) performance highlights the ongoing need for computational resources for agent development and evaluation [6].

#### 3.1.3 SWE-bench Implementation

SWE-bench provides Docker-based reproducible evaluation with multiple datasets (SWE-bench, SWE-bench Lite, SWE-bench Verified, SWE-bench Multimodal). The project has evolved significantly: SWE-agent release (Apr 2024), fully containerized evaluation harness (Jun 2024), cloud-based evaluations via Modal (Jan 2025), and SWE-bench Multimodal integration with private test split evaluation (Jan 2025) [9].

**Human annotation:** SWE-bench Verified is a human-validated subset of 500 engineer-confirmed solvable problems. 68.3% of original SWE-bench samples were filtered out due to issues like underspecified problem statements (38.3%), unfair unit tests (61.1%), or other problems. Human annotation involved 93 software developers, with each sample labeled 3 times by separate annotators. The annotation process evaluated problem statement clarity, unit test validity, and sample difficulty [10].

**Scalability and reliability:** SWE-bench-Live (1,319 task instances from 93 repositories) uses a fully automated curation pipeline (RepoLaunch) that streamlines instance creation from issue mining to Docker environment packaging, removing manual bottlenecks. It uses a time-machine mechanism to handle dependency version drift. The best-performing agent (OpenHands + Claude 3.7 Sonnet) achieves only 19.25% resolved rate on SWE-bench-Live, compared to 43.20% on SWE-bench Verified under identical settings, suggesting overfitting to static benchmarks. Multi-file patches (>3 files) or large changes (>100 lines) see success rates below 10% [9].

**Memorization concerns:** ~33% of issues have solution code appearing verbatim in descriptions (solution leakage); ~31% of passing patches rely on insufficiently robust test suites (weak oracles); >94% of issues predate LLM knowledge cutoffs, raising memorization concerns. Patch validation limitations overstate passing rates by 4–7% (absolute). UTBoost found that 24.4% of leaderboard rankings on Verified were impacted once more rigorous checks were applied [9].

**Cost:** SWE-bench requires Docker-based evaluation with containerized environments for each task instance. SWE-bench-Live provides dedicated Docker images per task instance. Cloud-based evaluations are available via Modal (Jan 2025). The cost-per-resolved-issue can decrease even if per-token costs are higher [9].

#### 3.1.4 GAIA Implementation

GAIA provides 466 real-world questions (166 for development, 300 without public answers for the leaderboard). Questions are divided into three difficulty levels based on steps and tools required. Evaluation uses automated exact-match evaluation [13].

**Human annotation:** The questions are human-crafted and validated. Human respondents achieved 92% accuracy. The key insight is that GAIA questions are conceptually simple for humans (92% success rate) yet extremely challenging for advanced AIs (only 15% for GPT-4 with plugins). This contrasts with current AI benchmarks that focus on tasks difficult for humans (e.g., MMLU, law, chemistry) where LLMs already surpass human performance [13].

**Scalability and reliability:** 466 questions total (166 development set, 300 test set). Questions test capabilities across web browsing, coding, multimodality (138 questions), and diverse filetype reading (129 questions). The benchmark is static by design—"Limitations include the lack of trace evaluation, remaining ambiguities, limited linguistic/cultural diversity, static nature, and evaluation complexity." About 5% of GAIA data contains errors/ambiguities in ground truth answers [14].

**Performance:** Current SOTA (Claude Sonnet 4.5 with HAL Generalist Agent, September 2025) achieves 74.55% accuracy at $178.20 cost. The most cost-effective entry (Gemini 2.0 Flash with HAL) achieves 32.73% at $7.80 total cost. 17 models and 2 scaffolds evaluated across 32 total entries. The current human-AI gap is 27% (Human 92% vs. h2oGPTe 65%) [15].

**Cost:** The main cost is compute/API calls required for evaluating LLMs with tool-use, web browsing, and multimodal capabilities across the 466 questions. The leaderboard is hosted on Hugging Face at https://huggingface.co/gaia-benchmark [14].

#### 3.1.5 ToolBench Implementation

ToolBench assembled 16,464 APIs across 49 domains from RapidAPI Hub, producing over 120,000 instruction-API pairs. The evaluation uses a test set divided into in-domain (1,588 instances) and out-of-domain (781 instances) subsets. The original ToolBench relies on real RapidAPI calls, which incur API costs and suffer from instability (only 44.4% success rate) [17].

**Human annotation:** API-Bank, a related benchmark, involved interviews with 500 users to establish design principles, defining three ability levels: Call, Retrieve+Call, and Plan+Retrieve+Call. The evaluation system includes 73 implemented APIs, 314 manually annotated tool-use dialogues with 753 API calls. For training, a Multi-agent data generation method using five collaborative LLM agents automatically produces training data, reducing annotation costs by 98% compared to human annotation ($0.10 per dialogue vs $8.00) [17].

**StableToolBench:** Introduced a Virtual API Server combining a caching system (achieving 75.8–97.0% cache hit rates) and an LLM-based API simulator (using GPT-4-turbo with few-shot examples from cache). A "Turing Test" with human annotators found simulated APIs performed comparably to real APIs, sometimes judged as more realistic. This addresses the instability of real API calls while maintaining realistic evaluation [18].

**Scalability and reliability:** Empirical findings reveal that LLMs struggle with complex multi-step planning (average accuracy below 50%), semantic-functional gaps in tool retrieval, safety limitations in privacy and physical injury domains (<30% recall), but show promise with reflection/correction (PALADIN raises recovery rates to ~90%). Process-Supervised Reward Models (PRMs) generalize better than outcome-only RM in multi-step tool-use: +19% rank@1 improvement for base models, +11% for fine-tuned models [16].

### 3.2 Multi-Agent Benchmark Implementation

#### 3.2.1 SOTOPIA Implementation

SOTOPIA provides an open-ended environment with procedurally generated scenarios featuring character profiles (name, age, personality, secrets), relationships, and social goals. LLM-based agents (GPT-3.5/4, LLaMA, Mistral, Qwen2.5) produce natural-language utterances, non-verbal cues, and actions within multi-turn dialogue structures. Multidimensional evaluation (Sotopia-Eval) scores agents along seven dimensions [20].

**Human annotation:** SOTOPIA scenarios are procedurally generated but human-LLM comparisons consistently show that models perform well on straightforward or stereotypical social situations but fail in cases requiring persistent strategic communication, social commonsense, or theory-of-mind reasoning. The "Sotopia-hard" subset identifies systematic model failures where even GPT-4 underperforms humans. The paper notes an "increasing gap between GPT-4-based and human evaluation, highlighting the limitations of relying solely on GPT-4-based evaluation for optimizing or evaluating language models" [22].

**Scalability and reliability:** SOTOPIA supports procedural scenario generation, allowing for potentially unlimited scenarios. Extensions include Lifelong-Sotopia (chains multiple episodes to evaluate memory across interactions using ~200-300 word "memory chunks"), SOTOPIA-Ω (dynamic strategy injection for automated high-quality dialogue corpus generation), and Sotopia-RL (utterance-level, multi-dimensional reward modeling with GRPO optimization). Sotopia-ToM has 160 human-reviewed scenarios, with a larger non-human-verified scenario set of 600 scenarios (Sotopia-ToM-Silver) [23].

**Key findings:** GPT-4 achieves a significantly lower goal completion rate than humans. Weaker partner models negatively impact stronger models' performance. SOTOPIA-π allows a 7B LLM (Mistral-7B) to approach the social goal completion ability of GPT-4, with the best model achieving a goal completion score of 5.71 vs GPT-4's 5.89 as rated by GPT-4. Training on LLM-generated metrics can produce overestimation, encouraging hybrid human+LLM evaluation protocols [22].

**Cost:** SOTOPIA-π requires no human involvement and no online reward model, making it efficient and scalable. The method uses behavior cloning (learning from GPT-4 expert policies) and self-reinforcement training, which requires API calls to GPT-4 for rating. Sotopia-RL involves utterance-level reward modeling with GRPO optimization [22].

#### 3.2.2 ChatEval Implementation

ChatEval orchestrates N LLM-based agents (N=2–4 by default) with T discussion rounds (typically T=2). The framework uses multiple LLM agents with diverse role prompts (e.g., General Public, Critic, News Author, Psychologist, Scientist) to collaboratively evaluate text quality through structured discussion. Three communication strategies are employed: One-by-One, Simultaneous-Talk, and Simultaneous-Talk-with-Summarizer [24].

**Human annotation:** ChatEval uses multi-agent debate as an alternative to human annotation, leveraging the collective reasoning of multiple LLM agents to produce evaluation judgments. The framework is designed to reduce reliance on human annotation by using automated agent-based evaluation [25].

**Scalability and reliability:** Performance generally improves as the number of roles increases up to 3-4 roles, after which it begins to decline. Increasing the number of agents improved performance, while increasing discussion turns showed diminishing returns due to context length issues. On FairEval benchmark, ChatEval improved accuracy by 6.2% for ChatGPT and 2.5% for GPT-4 over single-agent baselines. The debate process exhibited human-like behaviors including opening statements, alternative proposals, stance maintenance, and consensus seeking [25].

**Cost:** The cost is primarily in API calls to multiple LLM agents for each evaluation instance, as multiple agents must be queried to generate debate responses. The multi-agent approach is more computationally expensive than single-agent evaluation due to the need for multiple model calls and debate rounds [24].

#### 3.2.3 CAMEL Framework

CAMEL (Communicative Agents for "Mind" Exploration) is an open-source community and framework dedicated to finding the scaling laws of agents. It is the first LLM multi-agent framework, enabling various types of agents, tasks, prompts, models, and simulated environments. The framework is hosted on GitHub (camel-ai/camel) with 17.6k stars, 2.0k forks, and 2,284 commits [47].

**Design principles:** Evolvability (agents evolve via data generation and interaction), Scalability (supports millions of agents), Statefulness (agents maintain stateful memory), and Code-as-Prompt (code serves as prompts for agents). Key features include support for large-scale agent systems (up to 1M agents), dynamic communication, stateful memory, multiple benchmarks, various agent types, data generation, and tool integration [47].

**Human annotation:** CAMEL uses synthetic data generation via multi-agent roleplay conversations. The CAMEL AI "Domain Expert" dataset, comprising 25,000 conversations between two GPT 3.5 Turbo agents, was used as part of the training data for Teknium's OpenHermes model and the Microsoft Phi model. MPT-30B-Chat was built by finetuning MPT-30B and trained on 19.54% Camel-AI sourced data [47].

**CRAB (Cross-environment Agent Benchmark):** The first benchmark framework to address cross-environment, multi-device agent evaluation. Key innovations include Cross-Platform Multi-Agent Architecture (enables agents to operate multiple devices simultaneously, e.g., Ubuntu and Android), Graph Evaluator (uses a DAG structure to decompose tasks into sub-goals with precedence and parallel relationships), and Task Synthesis (allows composition of sub-tasks to construct task descriptions and evaluators). Evaluation metrics include Completion Rate (CR), Execution Efficiency (EE), and Cost Efficiency (CE) [48].

**Scalability and reliability:** CAMEL is designed for scalability, supporting "Simulate up to 1M agents to study emergent behaviors and scaling laws in complex, multi-agent environments." Four multimodal models were tested on CRAB: GPT-4o, GPT-4 Turbo, Gemini 1.5 Pro, and Claude 3 Opus. The best-performing model GPT-4o scored only 35.26 (CR), demonstrating the complexity of cross-platform tasks. Multi-agent systems had higher false completion rates than single-agent systems due to communication issues [48].

**Cost:** CAMEL is open-source and free to use (Apache 2.0 license). The compute costs depend on the underlying LLM API calls. CAMEL supports smart routing to select the most cost-effective model per task, with potential cost reductions of up to 80% via intelligent caching and routing. A multi-agent system for customer service automation achieved ~5 FTR emails/minute at ~£0.05/email (vs. manual baseline of ~3 emails/minute at ~£0.33/email) [47].

#### 3.2.4 MASEval Implementation

MASEval is a framework-agnostic evaluation library for multi-agent systems, introduced to address the gap in existing benchmarks that are predominantly model-centric. The key premise is that system-level implementation decisions—such as topology, orchestration logic, and error handling—substantially impact performance, yet current benchmarks fix the agentic setup and only compare models [33].

**Implementation:** MASEval is built on seven core abstractions (Task, Benchmark, Environment, AgentAdapter, User, Evaluator, ModelAdapter) with a trace-first approach, per-agent message histories, and a benchmark lifecycle spanning setup, execute, collect, evaluate, and report phases. It supports bring-your-own frameworks, model providers, and logging backends. Capabilities include multi-agent tracing, callback system, adaptive testing (e.g., DISCO algorithm using only 1% of tasks to estimate full performance within ~2 pp), reproducibility infrastructure, parallel execution, structured error attribution, and a unified benchmark interface [33].

**Human annotation:** MASEval provides a framework for automated evaluation across multiple benchmarks, reducing the need for manual annotation through its benchmark abstraction layer.

**Scalability and reliability:** MASEval reduces implementation effort by 83–91% for benchmark consumers and 35–57% for benchmark producers. Key finding: framework choice impacts performance comparably to model choice. The mean performance range across models was 14.2 percentage points (pp) and across frameworks was 12.4 pp. A striking example: Haiku 4.5 scored 90.4 on MACS Travel with smolagents but only 59.5 with LlamaIndex—a 30.9 pp gap [33].

**Cost:** MASEval is available under MIT license at github.com/parameterlab/MASEval and installable via pip install maseval. The framework reduces implementation costs by providing a standardized interface for evaluation across multiple frameworks and benchmarks [33].

### 3.3 Comparative Summary of Implementation Costs

| Benchmark | Implementation Approach | Human Annotation | Scalability | Reliability Concerns | Cost |
|-----------|----------------------|-----------------|-------------|---------------------|------|
| **AgentBench** | Docker-based, HTTP model server, 8 environments | Manual task curation | 4k–13k generations per eval | GPT-4 4.01 vs OSS 0.51; TLE/IF errors | High compute |
| **WebArena** | Self-hosted Docker, 4 web apps, 812 tasks | Human baseline 78.24%; 170 trajectory recordings | Extended suites (WebChoreArena, VWA) | LLM-as-Judge errors; 70-95% degradation from network errors | Self-hosted, compute-intensive |
| **SWE-bench** | Docker-based, 2,294 tasks (Verified: 500) | 93 developers, 3x per sample | SWE-bench-Live: 1,319 tasks, 93 repos | Memorization; 24.4% rankings impacted by weak tests | Cloud via Modal (Jan 2025) |
| **GAIA** | 466 human-crafted questions, exact-match eval | Human baseline 92% | Static (466 questions) | 5% ground truth errors; static by design | API costs for LLM evaluation |
| **ToolBench** | 16,464 APIs, 120K+ instructions | 500 user interviews; Multi-agent data gen (98% cost reduction) | StableToolBench: virtual API server | 44.4% real API success; 50% hallucinated queries | Real API costs; virtual server reduces dependency |
| **SOTOPIA** | Procedural scenario generation, 7-dimension eval | Human-LLM comparisons; "Sotopia-hard" subset | Extensions (Lifelong, RL, ToM) | Increasing GPT-4 vs human eval gap; partner model effects | API costs for GPT-4 rating |
| **ChatEval** | N agents × T rounds, role-based debate | No human annotation required | N=2–4, T=2 typical; diminishing returns beyond | Group-think; homogeneous LLM groups | N agents × T rounds API calls |
| **CAMEL** | Open-source framework, 1M+ agent support | Synthetic data generation | CRAB: cross-platform, 100 tasks | Best model 35.26% CR on CRAB; false completion rates | Open-source; smart routing reduces costs |
| **MASEval** | 7 core abstractions, framework-agnostic | Automated evaluation across benchmarks | DISCO: 1% tasks → ~2 pp accuracy | Framework choice = model choice impact | 83-91% implementation cost reduction |

---

## Part 4: Future Directions for Unified Evaluation Pipelines

### 4.1 The Need for Holistic, Multi-Dimensional Evaluation

The research community has reached a consensus that current evaluation practices are fragmented and inadequate for real-world deployment. The comprehensive review "From benchmarks to deployment: a comprehensive review of agentic AI evaluation" (Artificial Intelligence Review, 2026) argues that "evaluation methodology not model capability constitutes the primary bottleneck limiting reliable agent deployment" [49]. It finds that "0/15 benchmarks integrate safety or security into scoring, 0/15 include cost-efficiency metrics in their primary evaluation protocol, and 13/15 rely exclusively on binary success measures" [49].

The "Survey on Evaluation of LLM-based Agents" (Yehudai et al., 2025, arXiv:2503.16416) states: "The shift from static models to adaptive, interactive agents calls for a new paradigm for evaluating LLM-based agents" [50]. It identifies critical gaps including "insufficient assessment of cost-efficiency, safety, and robustness, as well as a need for fine-grained and scalable evaluation methods" [50].

The "Evaluation and Benchmarking of LLM Agents: A Survey" (KDD '25) introduces the concept of Evaluation-driven Development (EDD), proposing "making evaluation an integral part of the agent development cycle" [35]. The survey emphasizes that "the development of more realistic evaluation settings that mirror actual deployment conditions is crucial for building confidence in agent capabilities" [35].

### 4.2 Standardized Taxonomies and Ontologies

Several proposals for standardized taxonomies have emerged as foundational elements for unified evaluation:

**Two-dimensional taxonomy (KDD '25):** Organizes evaluation along (1) Evaluation Objectives (Agent Behavior, Agent Capabilities, Reliability, Safety and Alignment) and (2) Evaluation Process (Interaction Mode, Data/Benchmarks, Metrics Computation, Contexts) [35].

**Three-pillar meta-taxonomy (Awesome-LLM-Agent-Evaluation):** WHAT is evaluated (Target Capabilities: W1-W6), HOW it is measured (Evaluation Paradigms: H1-H3), and WHERE it is tested (Environment Topologies: E1/E2a-E2d). Every entry is classified as a region ⟨W, H, E⟩ across three analytically separable pillars [51].

**MAST framework:** Organizes multi-agent evaluation along three top-level error categories: Specification & System Design, Inter-Agent Misalignment, and Task Verification & Termination. Identifies 14 failure modes across these categories, developed through analysis of 7 popular frameworks across 200+ tasks [51].

**Ontology for agentic AI (2025-2026):** A proposed three-layer ontological framework (Role, Domain, Interaction ontologies) validated against a production system serving 22 industry verticals with 650+ agents. It introduces a six-level maturity model (L0–L5) and identifies "context interference" where injecting ontological context can displace useful parametric knowledge. Skan AI's Agentic Ontology of Work (AOW) v1.0 defines eight canonical entities (Agents, Skills, Intents, Contexts, Policies, Memory, Confidence, Outcomes) for workflow governance [52].

### 4.3 Automated and Scalable Evaluation

**LLM-as-Judge evolution:** The "Agent-as-a-Judge" paradigm is a growing area, with the "Awesome Agent-as-a-Judge" repository cataloging research across Multi-Agent Collaboration (16 papers), Planning (9 papers), Tool Integration (23 papers), Memory and Personalization (8 papers), and Optimization Paradigms (8 papers) [53]. The 2026 evaluation guide from Future AGI notes: "The 2024 pattern of trusting a single GPT-4-class judge is gone. Modern pipelines run two judges (a frontier model and a cheaper model) and flag disagreements for human review" [54].

**Continuous production scoring:** Has replaced periodic batch evals, with trajectory evaluation for agents becoming its own category. The practical move is to instrument the agent so each step can be seen, then score those steps against criteria matching the task. OpenTelemetry (OTEL) for tracing across distributed services is recommended [55].

**Synthetic data generation:** The Multi-agent data generation method for ToolBench reduced annotation costs by 98% compared to human annotation ($0.10 per dialogue vs. $8.00). SOTOPIA-π uses GPT-4 to provide ratings for filtering positive examples for training, requiring no human involvement and no online reward model [22].

**Adaptive testing:** MASEval's DISCO algorithm uses only 1% of tasks to estimate full performance within ~2 pp. GenEnv uses generative environments where a simulator auto-tunes task difficulty to the agent's skill level via a "continuous curriculum," producing up to +40.3% performance gains over baselines while using 3.3x less data [55].

### 4.4 Dynamic and Adaptive Evaluation

**Live benchmarks:** SWE-bench-Live is the first live-updating benchmark designed for complex, repository-level tasks. It uses a fully automated pipeline (RepoLaunch) that eliminates manual bottlenecks and is designed for monthly updates to prevent data contamination and overfitting [9]. The "Survey on Evaluation of LLM-based Agents" notes that "'Live' benchmarks are emerging to keep pace with rapid model advancements" [50].

**Self-evolving evaluation:** The Dynamic LLM Evaluation via Multi-Agent Framework (COLING 2025) reframes existing benchmark instances into new variants for dynamic evaluation, implementing six reframing operations (Question Alternating, Question Complicating, Context Paraphrasing, Context Noising, Polarity Reversing, Sub-ability Question Generation). Results show a general performance decline in most LLMs compared to original results, revealing limited generalizability and robustness. Human verification confirmed 94.8% accuracy of generated instances [56].

**Curriculum-based evaluation:** Adaptive Learning Systems research leverages LLM-powered analytics for personalized curriculum design, using real-time data analysis to dynamically adjust learning pathways. The real-time feedback mechanism yielded the highest engagement increase (19.2%) and retention improvement (22.4%), while adaptive sequencing achieved a 22.1% engagement increase and 23.4% retention improvement [57].

### 4.5 Reproducibility and Transparency Standards

**Docker-based reproducibility:** Major benchmarks (AgentBench, WebArena, SWE-bench, CAMEL) provide Docker-based reproducible evaluation environments. The awesome-LLM-Agent-Evaluation repository enforces "one rule above all others: accurate venue labeling. A benchmark is listed with its verified publication status (peer-reviewed proceedings, journal, or honestly-labeled preprint)" with full PRISMA-ScR pipeline reproducibility documentation [51].

**Data contamination prevention:** The agent evaluation community has increasingly adopted practices borrowed from cryptography and competitive machine learning to prevent data leakage, including delayed public release of test answers, encrypted evaluation servers, and blind evaluation protocols. SWE-bench-Live's time-machine mechanism handles dependency version drift [9].

**Enterprise requirements:** The "Evaluation and Benchmarking of LLM Agents" (KDD '25) emphasizes that "enterprise applications require predictable, consistent, and auditable behavior rather than occasional success" and that "the inherent stochastic nature of LLMs makes achieving and evaluating this enterprise-grade reliability particularly challenging." Enterprise-specific challenges include reliability guarantees (consistent performance across trials), dynamic and long-horizon interactions (performance drift, context retention), and adherence to domain-specific policies and compliance requirements (GDPR, HIPAA, approval workflows) [35].

### 4.6 Balancing Ecological Validity with Controlled Experimentation

**The realism gap:** The survey of Multi-agent LLM Evaluations (LessWrong) finds that "current evaluations lack realism. Many evaluations are based on party games and video games instead of focusing on environments and tasks similar to those agents might face in the real world" [45]. It recommends creating "more evaluations based on AI threat models across all failure modes" [45].

**Four paradigmatic shifts:** The "From benchmarks to deployment" review traces AI evaluation through four eras: (1) rule-based/symbolic (pre-2010), (2) statistical/deep learning (2010-2017), (3) foundation models (2018-2021), and (4) agentic AI (2021-present). It argues that "current evaluation practices exhibit a critical disconnect between benchmark performance and deployment viability, where agents achieving high scores on standardized benchmarks frequently fail in real world applications" [49].

**The verification gap:** General AgentBench (arXiv:2602.18998, 2025) introduces a unified benchmark for evaluating general-purpose LLM agents across four domains (Search, Coding, Reasoning, Tool-use). Key findings include a substantial performance drop (10–30% relative degradation) when moving from domain-specific evaluations to the general-agent setting, and a "verification gap" where models struggle to reliably select correct trajectories from their own sampled outputs [58].

### 4.7 Specific Research Directions and Design Principles

Based on the synthesis of survey papers, vision papers, and position papers from 2023–2025, the following concrete research directions emerge:

**1. Dual-Layer Evaluation Framework (Gonzalez, 2025):**
- **Layer A: Individual Specialist Evaluation** — Tests core competencies of individual agents in isolation (accuracy, consistency, efficiency, robustness, protocol interaction with MCP).
- **Layer B: Coordination System Evaluation** — Tests the effectiveness of the entire multi-agent system (task routing, workflow efficiency, communication effectiveness via A2A, global task success, system resilience).
- Uses a composite score (e.g., 50/50 weighting) with transparent breakdowns for diagnostic insights [59].

**2. Evaluation-driven Development (EDD):**
Making evaluation an integral part of the agent development cycle rather than a post-hoc assessment. This includes continuous integration pipelines with automated evaluation, production traffic sampling for async scoring, and closing the loop by converting failing traces into new evaluation fixtures [35].

**3. Cost-Efficiency as a First-Class Metric:**
The "Survey on Evaluation of LLM-based Agents" identifies "Missing Cost-Efficiency Metrics" as one of five major challenges. Future benchmarks must report compute time, token usage, and monetary costs alongside performance metrics. Cost-performance Pareto frontiers are recommended for multi-dimensional evaluation [50].

**4. Safety and Security Integration:**
"0/15 benchmarks integrate safety or security into scoring" [49]. Future evaluation pipelines must include tool misuse detection, adversarial robustness (prompt injection, tool poisoning, jailbreak escalation), and sandboxing/capability constraints. AgentAuditor's ASSEBench provides a template for large-scale safety evaluation [40].

**5. Multi-Agent Failure Mode Coverage:**
"26 out of 32 papers measured miscoordination failure modes, while only 5 papers measured collusion failure modes" [45]. Future evaluations must cover all MAST taxonomy failure modes, including specification issues, inter-agent misalignment, and task verification problems, with particular attention to collusion risks grounded in AI threat models.

**6. Interoperability Testing:**
No current benchmarks test standard protocols like Google's A2A (Agent-to-Agent) or Anthropic's MCP (Model Context Protocol). As multi-agent systems increasingly rely on these protocols, evaluation must include protocol interaction testing [59].

**7. Longitudinal and Memory Evaluation:**
Lifelong-Sotopia chains multiple episodes to evaluate memory across interactions. The MACLA framework (Memory as the Engine of Continual Learning) freezes the LLM's weights and offloads adaptation to an external "hierarchical procedural memory" system, achieving 78.1% average success across benchmarks (beating agents 10x larger), +3.1% generalization to unseen tasks, and memory building ~2,800x faster than retraining model weights [55].

**8. Hybrid Human+LLM Evaluation Protocols:**
SOTOPIA found an increasing gap between GPT-4-based and human evaluation as models are optimized for GPT-4 ratings. Future pipelines should run two judges (a frontier model and a cheaper model) and flag disagreements for human review, combining the scalability of automated evaluation with the reliability of human judgment [54].

**9. Generalization Across Frameworks:**
MASEval demonstrated that framework choice impacts performance comparably to model choice. Future evaluation must explicitly control for framework effects, reporting results across multiple frameworks to ensure findings are not framework-specific [33].

**10. The Six-Stage Evaluation Pipeline (Future AGI, 2026):**
1. Pick 3-5 product-specific metrics
2. Build 100-300 labeled prompt fixtures
3. Mix judges + heuristics
4. Gate CI with tight thresholds
5. Sample 5-20% of production traffic for async scoring
6. Close the loop by converting failing traces into new fixtures

"The teams that ship reliable LLM products in 2026 are not the ones with the most powerful base model. They are the ones whose eval pipeline catches a regression on Tuesday and ships a fix on Wednesday" [54].

---

## Conclusion

The evaluation of LLM-based agents has undergone a remarkable transformation between 2023 and 2025, evolving from simple task-completion metrics to multidimensional frameworks that capture capability, reliability, safety, cost-efficiency, and emergent social behaviors. However, this evolution has revealed a fundamental tension: the field currently lacks a unified evaluation paradigm that can simultaneously satisfy the demands of controlled reproducibility, ecological validity, safety assurance, and practical deployment.

Single-agent benchmarks have achieved high levels of standardization and automation, but face growing challenges of data contamination (documented in SWE-Bench and GAIA), evaluation reliability (LLM-as-Judge errors in WebArena and τ-bench), and narrow capability assessment (GAIA's 92% human vs. 15% AI gap). Multi-agent benchmarks provide richer ecological validity for collaborative scenarios, but introduce complexities in credit assignment, evaluation reliability, and computational cost that remain unresolved.

The path forward lies in the convergence of several emerging trends: standardized taxonomies that provide a common language for capability description, automated evaluation pipelines that reduce human annotation costs while maintaining reliability, dynamic benchmarks that resist contamination through continuous updates, and hybrid evaluation protocols that combine the scalability of LLM-as-Judge with the reliability of human oversight.

The most urgent priority is the development of unified evaluation pipelines that treat cost-efficiency, safety, and robustness as first-class metrics alongside traditional task completion. Without such comprehensive frameworks, the gap between benchmark performance and real-world deployment viability will continue to widen, limiting the safe and reliable deployment of increasingly capable agentic systems.

---

## Sources

[1] AgentBench: Evaluating LLMs as Agents (ICLR 2024): https://arxiv.org/html/2308.03688v3

[2] AgentBench: Evaluating LLM Agent Capabilities — Emergent Mind: https://www.emergentmind.com/topics/agentbench-729b2968-66e6-478e-9bf4-c1a576adaf32

[3] What Is AgentBench | Arize AI: https://arize.com/glossary/agentbench

[4] AgentBench: Evaluating LLMs as Agents (ICLR 2024 Proceedings): https://proceedings.iclr.cc/paper_files/paper/2024/file/e9df36b21ff4ee211a8b71ee8b7e9f57-Paper-Conference.pdf

[5] WebArena Benchmark: Evaluating Web Agents — Emergent Mind: https://www.emergentmind.com/topics/webarena-benchmark

[6] WebArena: A Realistic Web Environment for Building Autonomous Agents (arXiv:2307.13854): https://arxiv.org/html/2307.13854v4

[7] VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks: https://jykoh.com/vwa

[8] WAREX: Web Agent Reliability Evaluation on Existing Benchmarks: https://arxiv.org/html/2510.03285v1

[9] SWE-bench Overview — swebench.com: https://www.swebench.com/SWE-bench

[10] Introducing SWE-bench Verified — OpenAI: https://openai.com/index/introducing-swe-bench-verified

[11] SWE-Bench Verified Leaderboard — LLM Stats: https://llm-stats.com/benchmarks/swe-bench-verified

[12] "The SWE-Bench Illusion: When State-of-the-Art LLMs Remember Instead of Reason": https://arxiv.org/html/2506.12286v3

[13] GAIA: A Benchmark for General AI Assistants (arXiv:2311.12983): https://arxiv.org/pdf/2311.12983

[14] GAIA: a benchmark for General AI Assistants — alphaXiv: https://www.alphaxiv.org/abs/2311.12983

[15] HAL: GAIA Leaderboard: https://hal.cs.princeton.edu/gaia

[16] ToolBench Evaluation: LLM Tool-Use Insights — Emergent Mind: https://www.emergentmind.com/topics/toolbench-evaluation

[17] ToolBench (OpenBMB/ToolLLM) — GitHub: https://github.com/OpenBMB/ToolBench

[18] StableToolBench: Towards Stable Large-Scale Benchmarking on Tool Learning (ACL 2024): https://arxiv.org/html/2403.07714v1

[19] "AI Agent Benchmarks are Broken" — Medium (Daniel Kang): https://medium.com/@danieldkang/ai-agent-benchmarks-are-broken-c1fedc9ea071

[20] SOTOPIA: Interactive Evaluation for Social Intelligence in Language Agents (ICLR 2024): https://www.semanticscholar.org/paper/SOTOPIA%3A-Interactive-Evaluation-for-Social-in-Zhou-Zhu/f6e893b3e2ee7a62c2fe8a3b0e33920c3e596969

[21] Sotopia Interactive Social Evaluation Benchmark — Emergent Mind: https://www.emergentmind.com/topics/sotopia-interactive-social-evaluation-benchmark

[22] SOTOPIA-π: Interactive Learning of Socially Intelligent Language Agents (ACL 2024): https://aclanthology.org/2024.acl-long.698.pdf

[23] Sotopia-ToM: Evaluating Information Management in Multi-Agent Interaction (arXiv:2605.02307): https://arxiv.org/html/2605.02307v1

[24] ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate (ICLR 2024): https://proceedings.iclr.cc/paper_files/paper/2024/file/25cc3adf8c85f7c70989cb8a97a691a7-Paper-Conference.pdf

[25] ChatEval: Multi-Agent NLG Evaluation — Emergent Mind: https://www.emergentmind.com/topics/chateval

[26] MultiAgentBench: Evaluating the Collaboration and Competition of LLM agents (arXiv:2503.01935): https://arxiv.org/html/2503.01935v1

[27] MultiAgentBench — Emergent Mind: https://www.emergentmind.com/topics/multiagentbench

[28] ChatDev: Communicative Agents for Software Development (arXiv:2307.07924): https://arxiv.org/abs/2307.07924

[29] ChatDev Framework — Emergent Mind: https://www.emergentmind.com/topics/chatdev-framework

[30] ChatDev 2.0 — GitHub: https://github.com/OpenBMB/ChatDev

[31] MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework (ICLR 2024): https://arxiv.org/abs/2308.00352

[32] MetaGPT Technical Review: https://www.zhongzhuzhou.org/blog/2026-03-16-2026-03-16-MetaGPT-technical-review-en

[33] MASEval: Extending Multi-Agent Evaluation from Models to Systems (arXiv:2603.08835): https://arxiv.org/html/2603.08835v1

[34] AgentRecBench: Benchmarking LLM Agent-based Personalized Recommender Systems (NeurIPS 2025): https://arxiv.org/html/2505.19623v2

[35] Evaluation and Benchmarking of LLM Agents: A Survey (KDD '25, arXiv:2507.21504): https://arxiv.org/html/2507.21504v1

[36] Evaluating LLM-based Agents: Metrics, Benchmarks, and Best Practices: https://samiranama.com/posts/Evaluating-LLM-based-Agents-Metrics,-Benchmarks,-and-Best-Practices

[37] A Survey on LLM-as-a-Judge (2024): https://arxiv.org/html/2411.15594v4

[38] Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge): https://eugeneyan.com/writing/llm-evaluators

[39] LLM-As-Judge: 7 Best Practices & Evaluation Templates (Monte Carlo, Apr 2026): https://montecarlo.ai/blog-llm-as-judge

[40] Human-Level Safety and Security Evaluation for LLM Agents (NeurIPS 2025): https://proceedings.neurips.cc/paper_files/paper/2025/file/3dc85735f6e2fcf093e67b134fa00d21-Paper-Conference.pdf

[41] Contextual Trust Evaluation for Robust Coordination in LLM MAS (preprint, Dec 2025): https://www.preprints.org/manuscript/202512.2748

[42] NeurIPS 2025 Poster - Shapley-Coop: https://neurips.cc/virtual/2025/poster/118868

[43] LLM Agent Evaluation Frameworks — Emergent Mind: https://www.emergentmind.com/topics/llm-agent-evaluation-frameworks

[44] From Reasoning to Agentic: Credit Assignment in Reinforcement Learning for Large Language Models (arXiv:2604.09459): https://arxiv.org/html/2604.09459v2

[45] Survey of Multi-agent LLM Evaluations — LessWrong: https://www.lesswrong.com/posts/tGcLA596E8g3KnphE/survey-of-multi-agent-llm-evaluations

[46] AAMAS LLM-MCA & LLM-TACA (ICON Lab, UC Berkeley, AAMAS 2025): https://iconlab.negarmehr.com/LLM-MCA

[47] CAMEL GitHub Repository: https://github.com/camel-ai/camel

[48] CRAB: Cross-environment Agent Benchmark — CAMEL-AI: https://www.camel-ai.org/blogs/crab-cross-platform-agent-benchmark

[49] From benchmarks to deployment: a comprehensive review of agentic AI evaluation (Artificial Intelligence Review, 2026): https://link.springer.com/article/10.1007/s10462-026-11571-0

[50] A Survey on Evaluation of LLM-based Agents (arXiv:2503.16416): https://arxiv.org/html/2503.16416v2

[51] Awesome-LLM-Agent-Evaluation — GitHub: https://github.com/vnageshwaran-de/Awesome-LLM-Agent-Evaluation

[52] Research Brief: Ontologies for Agentic AI (2025–2026): https://www.designpattern.fyi/ontological-engineering/ontology-agentic-ai-research-brief

[53] Awesome Agent-as-a-Judge — GitHub: https://github.com/ModalityDance/Awesome-Agent-as-a-Judge

[54] How to Evaluate LLMs in 2026: Metrics & Pipelines — Future AGI: https://futureagi.com/blog/how-to-evaluate-large-language-models-llms

[55] Engineering Better Evals: Scalable LLM Evaluation Pipelines (Arize AI, 2025): https://www.youtube.com/watch?v=spvXj9tnWAQ

[56] A Multi-Agent Framework for Dynamic LLM Evaluation (COLING 2025): https://aclanthology.org/2025.coling-main.223.pdf

[57] Adaptive Learning Systems: Personalized Curriculum Design Using LLM-Powered Analytics (arXiv:2507.18949): https://ar5iv.labs.arxiv.org/html/2507.18949

[58] General AgentBench: Benchmark Test-Time Scaling of General LLM Agents (arXiv:2602.18998): https://arxiv.org/html/2602.18998v1

[59] Evaluating Agent Systems and Human AI Fluency (Part 1) — Gonzalez, 2025: https://trilogyai.substack.com/p/evaluating-agent-systems-and-human
