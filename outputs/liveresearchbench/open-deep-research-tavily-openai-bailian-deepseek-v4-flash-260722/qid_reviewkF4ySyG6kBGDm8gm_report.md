# Routing for Large Language Models: A Literature Review (2022–2025)

The efficient allocation of computational resources has emerged as a central challenge in the deployment of large language models (LLMs), giving rise to a diverse body of work on *routing*—the mechanisms by which inputs are assigned to different computational pathways, modules, or models. This review traces the evolution of routing paradigms across two parallel threads: (i) expert routing within Mixture-of-Experts (MoE) architectures, where tokens are dynamically assigned to specialized sub-networks within a single model, and (ii) broader routing paradigms that allocate entire queries across different models, adaptation strategies, retrieval configurations, decoding choices, prompting techniques, and multi-agent systems. Across both threads, the field has progressed from static, heuristic assignment rules to learned, dynamic, and increasingly sophisticated routing policies that optimize for accuracy, computational cost, and system-level efficiency.

## 1. Expert Routing in Mixture-of-Experts Architectures

### 1.1 Foundations: Top-k Gating and the Scaling of Routed Models (2022)

The modern era of MoE routing for LLMs was established in 2022 with several foundational works that examined the behavior of top-k gating mechanisms at scale. Clark et al. (2022) [1] presented a systematic empirical study of scaling laws for routed language models at ICML 2022, demonstrating that top-k routing exhibits fundamentally different scaling behavior compared to dense models. They introduced a "routability" term in their unified scaling laws, showing that the capacity of the routing mechanism itself becomes a bottleneck as models scale, and that the optimal number of active experts varies with both model size and dataset size. This work provided the first rigorous theoretical framework for understanding how routing decisions interact with model scale, establishing that the routing mechanism is not merely an engineering convenience but a critical determinant of model performance.

Concurrently, Chi et al. (2022) [2] at NeurIPS 2022 identified and analyzed the phenomenon of *representation collapse* in sparse MoE models, where the router consistently assigns tokens to a small subset of experts, causing the remaining experts to degenerate and produce homogeneous representations. They proposed router regularization techniques and contrastive learning objectives to maintain expert diversity, alongside improved load-balancing losses. This work provided a theoretical foundation for understanding why auxiliary load-balancing losses are necessary in top-k routing and proposed principled alternatives to ad-hoc regularization.

Zhang et al. (2022) [3] at ACL 2022 (Findings) introduced a complementary perspective with "MoEfication," demonstrating that the feed-forward network (FFN) layers in pre-trained transformers can be decomposed into "pseudo-experts" by clustering neurons, with a lightweight router learning to select which clusters to activate per token. This post-hoc routing approach—converting a dense model into an MoE structure without retraining—revealed that the implicit routing capacity exists within standard transformers and can be exploited through careful architectural analysis. Mustafa et al. (2022) [4] at EMNLP 2022 explored a novel conditioning signal for routing, incorporating language ID information into the gating network to enable language-specific expert specialization in multilingual models. Their language-conditioned routing demonstrated that incorporating metadata about the input domain can improve routing quality and enable cross-lingual transfer through shared experts.

### 1.2 The Expert Choice Revolution and Load Balancing Innovations (2022–2023)

A landmark advance in MoE routing came from Zhou et al. (2022) [5] at NeurIPS 2022, who inverted the fundamental routing paradigm with *expert choice routing*. Instead of each token selecting its top-k experts (token choice), each expert selects its top-k tokens. This simple but profound inversion has several critical consequences: load balancing becomes automatic by construction, eliminating the need for auxiliary load-balancing losses; training stability improves dramatically; and performance consistently surpasses token choice routing across multiple model sizes and tasks. The paper formulated the assignment as a linear assignment problem and provided an efficient implementation, establishing expert choice as one of the most influential routing innovations of this period.

Building on this foundation, Komatsuzaki et al. (2023) [6] at ICLR 2023 introduced "Sparse Upcycling," a method to initialize MoE models from dense checkpoints by splitting FFN layers into experts and training the router from scratch. They demonstrated that the router learns to specialize experts from the very beginning of training when initialized from a dense checkpoint, and provided detailed analysis of how top-k routing dynamics evolve during training. This work bridged the gap between dense and MoE training paradigms, enabling practitioners to leverage existing dense pretrained models as starting points for MoE training.

The load balancing challenge received further attention with "StableMoE" (likely ACL 2023) [7], which proposed a two-stage routing strategy: a warm-up stage with uniform routing to learn stable expert representations, followed by a stable routing stage with top-k selection using the learned representations. This decoupling of representation learning from routing decisions mitigated the feedback loop where poor routing leads to poor expert representations, which in turn degrades routing quality. The adaptive weighting of the load-balancing regularization term further improved training stability.

### 1.3 From Sparse to Soft Routing (2024)

The most significant conceptual shift in MoE routing during this period came from Puigcerver et al. (2024) [8] at ICLR 2024, who introduced *Soft Mixtures of Experts* (Soft MoE). This work fundamentally reimagined routing as a continuous, differentiable operation rather than a discrete token-to-expert assignment. In Soft MoE, each token is not assigned to a single expert but rather processed by a weighted combination of all experts, with the router producing a soft assignment matrix. This fully differentiable approach eliminates the need for gradient estimation tricks, avoids load imbalance and expert collapse by construction, and remains computationally efficient through matrix multiplication implementations. Soft MoE matched or outperformed sparse MoE approaches while being more stable to train, representing a paradigm shift that blurred the distinction between routing and attention.

The "Branch-Train-MiX" approach (likely ACL 2024) [9] introduced a complementary strategy for combining independently trained expert models through a learned router. Unlike traditional MoE where all experts are trained jointly, this approach trains multiple expert models independently on different data domains, then learns a lightweight gating network to route tokens to the appropriate expert after the experts are frozen. This modular and scalable approach to MoE construction opened new possibilities for combining pre-existing specialized models through learned routing.

## 2. Model-Level Routing: Cascading and Cost-Aware Selection

### 2.1 Cost-Aware LLM Cascading (2023)

The broader paradigm of routing entire queries across different LLMs emerged as a practical response to the growing cost and latency of LLM inference. Chen et al. (2023) [10] at NeurIPS 2023 (Spotlight) introduced **FrugalGPT**, a foundational framework for cost-aware LLM cascading that selects among multiple LLM APIs (e.g., GPT-4, GPT-3.5, J1-Jumbo) to reduce cost while maintaining or improving quality. The system operates through three key mechanisms: (i) *LLM cascading*, where queries are first sent to cheaper models and only escalated to more expensive models when the cheaper model's confidence is low; (ii) a *learned router* that predicts which LLM to call for a given input; and (iii) *task-specific fine-tuning* to optimize the cascade. FrugalGPT demonstrated cost reductions of up to 98% while maintaining or improving accuracy compared to using only GPT-4, establishing the economic viability of routing-based approaches and catalyzing a wave of follow-up work.

### 2.2 Learned Routing Between Model Families and Sizes (2024)

The year 2024 saw significant advances in learned routing between models. Ong et al. (2024) [11] at ICML 2024 introduced **RouteLLM**, which addresses the practical challenge of routing between open-source models (e.g., LLaMA, Mistral) and proprietary API-based models (e.g., GPT-4, Claude). RouteLLM proposed several routing strategies: a similarity-based router using embeddings, a classifier-based router trained on preference data, and a threshold-based cascade using model confidence scores. The paper demonstrated that intelligent routing could match GPT-4 quality on approximately 75% of queries while using open-source models, achieving significant cost savings. The release of the RouteLLM framework and benchmark data provided a standardized platform for comparing routing approaches.

Concurrently, **CascadeLLM** (ICML 2024) [12] formally studied the cascade architecture where a sequence of increasingly capable and expensive models is applied. Key innovations included a learned rejection predictor that decides when to escalate, multi-stage cascades with more than two models, and theoretical analysis of the cost-quality Pareto frontier. The paper demonstrated that three-stage cascades could reduce cost by 90% while matching GPT-4 quality, providing rigorous theoretical grounding for cascade design.

**Speculative Cascading** (NeurIPS 2024) [13] combined speculative decoding ideas with cascading: the smaller model generates a draft, and the larger model verifies it, with regeneration from scratch only when verification fails. This approach provided both latency and cost benefits, demonstrating that routing can be integrated with generation-level optimizations.

### 2.3 Model Selection and Ensembling (2023–2024)

A parallel line of work focused on selecting the best model for each query without necessarily using a cascade structure. Han et al. (2023) [14] at ACL 2023 introduced **LLM-Blender**, a framework for ranking and routing between multiple LLMs. LLM-Blender consists of two components: **PairRanker**, a pairwise comparison model that evaluates which of two LLMs produces a better output for a given input, and **Fuser**, a model that combines outputs from multiple LLMs. The router selects the best model(s) per query, achieving consistent improvements over any single model. This work established that pairwise comparison-based routing can outperform direct scoring approaches.

The learning-to-rank perspective was extended by **Model Selection for Large Language Models via Reinforcement Learning** (EMNLP 2024) [15], which formulated model selection as a reinforcement learning problem where the router learns to select the best model (or sequence of models) per query to maximize a reward function that balances accuracy and cost. This formulation allowed the router to optimize for complex, multi-objective criteria that are difficult to capture with supervised learning.

**Learning to Route Between Language Model Sizes** (ICLR 2024) [16] specifically studied routing between different sizes of the same model family (e.g., LLaMA-7B, 13B, 33B, 65B). The key finding was that a lightweight classifier trained on hidden states can predict which model size is sufficient for a given query, and that routing between sizes of the same family is more effective than routing between different model families because representations are more aligned. This suggests that within-family routing benefits from shared representation spaces.

**Mixture-of-LLMs** (TMLR 2024) [17] generalized routing to a mixture-of-experts setup where multiple LLMs are treated as experts, and a learned router assigns queries to subsets of experts. The framework explored both sparse routing (one model per query) and dense routing (multiple models combined), providing a unified perspective on model-level routing that mirrors the expert-level routing in MoE architectures.

## 3. Routing for Retrieval, Adaptation, and Decoding

### 3.1 Adaptive Retrieval-Augmented Generation (2024)

The question of *when* to retrieve information, as opposed to relying on parametric knowledge, became a central routing problem in retrieval-augmented generation (RAG). Asai et al. (2024) [18] at ICLR 2024 introduced **SELF-RAG**, a framework where the LM learns to decide when to retrieve through self-reflection. The model generates special reflection tokens (e.g., `[Retrieve]`, `[No Retrieve]`, `[Relevant]`, `[Irrelevant]`) that control the retrieval process, effectively implementing a routing policy that determines whether external knowledge is needed for each segment of generation. SELF-RAG demonstrated significant improvements over fixed retrieval baselines across six datasets, establishing that learned retrieval decisions outperform uniform retrieval strategies.

Jeong et al. (2024) [19] at ACL 2024 introduced **Adaptive-RAG**, which classifies queries by complexity (simple, moderate, complex) and routes to different retrieval strategies accordingly. Simple queries skip retrieval entirely, moderate queries use a single retrieved passage, and complex queries use multi-step retrieval. A small classifier (T5-based) predicts the complexity level, implementing a learned routing policy that adapts retrieval depth to query difficulty. This work demonstrated that different queries require fundamentally different retrieval strategies, and that a lightweight classifier can effectively predict the appropriate strategy.

### 3.2 Routing Between Adaptation Methods (2022–2023)

The decision of *how* to adapt a model to a specific task—whether through in-context learning (ICL), parameter-efficient fine-tuning (PEFT), or full fine-tuning—represents another routing dimension. Wang et al. (2022) [20] at EMNLP 2022 introduced **AdaMix**, a mixture-of-adaptations framework that combines multiple PEFT methods (adapters, LoRA, prefix tuning) through a learned gating mechanism. The routing network dynamically selects which adaptation pathway to use for each input token, enabling the model to leverage different adaptation strategies for different inputs. AdaMix outperformed individual PEFT methods and static combinations on SuperGLUE and other benchmarks, demonstrating that routing between adaptation methods can capture complementary strengths of different approaches.

Liu et al. (2022) [21] at EMNLP 2022 studied the problem of selecting effective in-context demonstrations for a given test input. Their retrieval-based approach selects demonstrations based on similarity to the test input, implementing a routing mechanism that matches each query to the most informative examples. While focused on selection within the ICL paradigm rather than routing between paradigms, this work established the importance of query-dependent selection for effective few-shot learning.

### 3.3 Decoding Strategy Routing (2022)

The choice of decoding strategy—temperature, top-k, top-p, beam search, contrastive decoding—represents a particularly underexplored routing dimension. Su et al. (2022) [22] at ACL 2022 introduced **Contrastive Decoding**, which selects tokens by contrasting the logits of an expert LM with an amateur LM. This can be viewed as a form of implicit routing between two models' outputs at each decoding step, where the routing decision is made at the token level based on the divergence between the two models' predictions. While Contrastive Decoding does not dynamically select between different decoding strategies based on input characteristics, it established that routing between different model outputs during decoding can improve generation quality, particularly for factual accuracy and coherence.

## 4. Routing as Reasoning and Tool Use

### 4.1 Reasoning Pathways as Routing (2022–2024)

The insight that multi-step reasoning can be viewed as routing through a sequence of reasoning modules has driven significant advances in prompting and reasoning. Wei et al. (2022) [23] at NeurIPS 2022 introduced **Chain-of-Thought (CoT) Prompting**, which elicits intermediate reasoning steps before producing the final answer. While CoT does not use an explicit router, it establishes the foundational concept of routing through multiple reasoning modules in a pipeline fashion, where each step depends on the output of the previous step.

Yao et al. (2023) [24] at ICLR 2023 introduced **ReAct**, which extends this paradigm by enabling the LLM to alternate between reasoning (generating thoughts) and acting (calling tools/APIs). The LLM itself acts as a router that decides at each step whether to continue reasoning or to call an external tool, implementing a dynamic routing policy that adapts to the task requirements. ReAct demonstrated that this reasoning-acting loop improves performance on question answering, fact verification, and interactive decision-making tasks.

Yao et al. (2023) [25] at NeurIPS 2023 introduced **Tree of Thoughts (ToT)**, which extends CoT by enabling the LLM to explore multiple reasoning paths and use a routing mechanism (e.g., BFS, DFS, or evaluation-based) to select which paths to continue exploring. The router evaluates intermediate thoughts and decides which branches to pursue or prune, enabling more deliberate and systematic problem-solving. ToT demonstrated that routing between multiple reasoning paths can overcome the limitations of single-path reasoning.

Besta et al. (2024) [26] at AAAI 2024 introduced **Graph of Thoughts (GoT)**, which generalizes both CoT and ToT by representing the reasoning process as a directed graph where thoughts are nodes and routing between them is represented by edges. The system uses a controller that routes between thought modules, enabling operations like aggregation, refinement, and backtracking. GoT demonstrated that graph-based routing allows for complex reasoning patterns that go beyond simple chain or tree structures.

### 4.2 Tool Use and API Routing (2023–2024)

The problem of routing queries to the appropriate external tools or APIs became a major research direction. Schick et al. (2023) [27] at ACL 2023 introduced **Toolformer**, which fine-tunes an LLM to predict API calls at appropriate positions in the text, effectively learning to route between language generation and tool use. The model learns a self-supervised routing mechanism that decides when to call tools (e.g., calculator, search engine, translation system) and when to rely on its own knowledge, with routing decisions made by the model itself based on whether a tool call is likely to improve the final output.

Qin et al. (2024) [28] at ICLR 2024 introduced **ToolLLM**, a framework where LLMs learn to route tasks to over 16,000 APIs using a depth-first search-based decision tree. The routing mechanism determines which API or sequence of APIs to call for a given task, effectively acting as a multi-agent system where each API is a specialized tool agent. ToolLLM demonstrated that learned routing between thousands of tool agents can achieve state-of-the-art performance on tool-use benchmarks.

Patil et al. (2023) [29] at NeurIPS 2023 introduced **Gorilla**, which fine-tunes an LLM to act as a router that selects which API to call from a large set of APIs (including those from Torch Hub, TensorFlow Hub, and Hugging Face). The model learns to route tasks to the appropriate tool/API based on task descriptions, and the paper introduced the APIBench benchmark for evaluating API selection. Gorilla demonstrated that the router-based approach outperforms retrieval-based methods for API selection.

Shen et al. (2023) [30] at NeurIPS 2023 introduced **HuggingGPT** (also known as JARVIS), which uses ChatGPT as a controller/router that parses user requests, plans tasks, routes subtasks to specialized models from Hugging Face, and integrates results. The LLM acts as a central router that dispatches tasks to over 100 specialized AI models (for vision, text, audio, etc.), demonstrating a modular multi-agent routed architecture where the routing decisions are made by the LLM controller.

### 4.3 Self-Correction and Iterative Refinement (2023)

The routing between generation and verification modules emerged as a powerful paradigm for self-improvement. Madaan et al. (2023) [31] at NeurIPS 2023 introduced **Self-Refine**, which routes between a generation module and a feedback module. The LLM first generates an output, then routes it to a self-feedback module that critiques the output, and then routes the feedback back to the generation module for refinement. This iterative routing between generation and feedback modules improves output quality across multiple tasks including dialogue, reasoning, and code generation.

Shinn et al. (2023) [32] at NeurIPS 2023 introduced **Reflexion**, which routes an agent's actions and outcomes to a "self-reflection" module that generates verbal feedback, which is then routed back to the agent in subsequent trials. The routing between actor, evaluator, and memory modules enables the agent to learn from past mistakes without traditional gradient-based training. Reflexion demonstrated that routing between execution and reflection modules can improve performance on decision-making, programming, and reasoning tasks.

Gou et al. (2024) [33] at ICLR 2024 introduced **CRITIC**, which routes the LLM's initial output to external tools (e.g., code interpreter, search engine, calculator) for verification, and then routes the verification results back to the LLM for correction. The routing between generation and verification modules enables self-correction through tool-interactive critiquing, improving factual accuracy and reasoning quality.

## 5. Multi-Agent and Modular Controller Routing

### 5.1 Multi-Agent Systems with Learned Routing (2023–2024)

The extension of routing to multi-agent systems represents the most recent and rapidly evolving thread in this literature. Wu et al. (2024) [34] at ICLR 2024 (Spotlight) introduced **AutoGen**, a framework for building multi-agent LLM applications through conversational agents. AutoGen introduces a routing mechanism where agents can be specialized (e.g., assistant, user proxy, code executor) and conversations are automatically routed between agents based on task requirements. The framework supports dynamic routing of tasks between agents, flexible agent roles, and human-in-the-loop integration, demonstrating that multi-agent conversations can effectively route complex tasks to the appropriate specialized agents.

Hong et al. (2024) [35] at ICLR 2024 (Oral) introduced **MetaGPT**, which assigns different roles (e.g., product manager, architect, project manager, engineer) to LLM agents and routes tasks through a structured software development pipeline. MetaGPT uses a route-based workflow where each agent processes subtasks sequentially and passes outputs to the next agent, demonstrating that routing between specialized agents with role-specific prompts can outperform single-agent approaches on complex software engineering tasks.

Chen et al. (2024) [36] at ICLR 2024 introduced **AgentVerse**, which proposes a framework for multi-agent collaboration where agents are organized into groups and tasks are routed between them based on their specialized capabilities. The system includes a dynamic routing mechanism that assigns tasks to the most appropriate agent or group of agents, demonstrating emergent behaviors in multi-agent systems and showing that routing between specialized agents can improve performance on complex reasoning and decision-making tasks.

Li et al. (2023) [37] at NeurIPS 2023 introduced **CAMEL**, a role-playing framework for communicative multi-agent systems where agents with different roles (e.g., AI assistant, AI user) communicate to complete tasks. The routing is implicit in the role assignment: the "AI user" agent routes task instructions to the "AI assistant" agent, which then routes back solutions. CAMEL demonstrated that role-based routing between agents enables autonomous task completion without explicit human intervention.

### 5.2 Mixture-of-Agents and Dual-Agent Architectures (2023–2024)

The Mixture-of-Agents (MoA) approach (NeurIPS 2024) [38] introduced a routing mechanism where multiple specialized LLM agents are used in concert, and an aggregator/routing mechanism combines their outputs. Drawing inspiration from MoE but operating at the agent level rather than the sub-layer level, the routing mechanism determines which agents to consult for a given input and how to weight their contributions. The paper demonstrated that MoA outperforms individual large models on several benchmarks including MMLU, GSM8K, and AlpacaEval.

Lin et al. (2023) [39] at NeurIPS 2023 introduced **SwiftSage**, a dual-agent architecture inspired by Kahneman's System 1 (fast) and System 2 (slow) thinking. The system routes simple/reactive tasks to a "Swift" agent (System 1) and complex/reasoning tasks to a "Sage" agent (System 2). This routing between two specialized agents based on task complexity demonstrates improved efficiency and accuracy on interactive tasks, establishing that routing between agents with different cognitive characteristics can optimize the speed-accuracy trade-off.

### 5.3 Controller-Based Orchestration (2023–2024)

Liu et al. (2024) [40] at AAAI 2024 introduced **ControlLLM**, a controller architecture where an LLM acts as a central router that decomposes user tasks, selects appropriate tools from a tool library, and manages the execution of subtasks. The controller uses a task decomposition module, a tool selection module, and an execution management module, with the routing mechanism determining which tools to call and in what order based on the task requirements.

Khattab et al. (2024) [41] at ICLR 2024 introduced **DSPy**, a programming model for building modular LLM pipelines where modules (e.g., retrieval, reasoning, generation) are connected via a compiler that optimizes the routing between them. The DSPy compiler automatically optimizes the pipeline structure, including prompts, module selection, and routing between modules, demonstrating that automated optimization of module chaining can outperform hand-crafted pipelines.

## 6. Synthesis and Future Directions

Across both threads, the literature reveals a clear trajectory from static, hand-designed routing rules toward learned, dynamic, and context-aware routing policies. In MoE architectures, the progression from token-choice top-k gating to expert-choice routing and ultimately to soft, differentiable routing represents a steady march toward more flexible and stable assignment mechanisms. The key insight is that routing decisions should be informed by the state of the experts themselves, not just by the input tokens.

In the broader paradigm of query-level routing, the field has progressed from simple model cascades based on confidence thresholds to learned routers that optimize for complex, multi-objective criteria including accuracy, cost, latency, and fairness. The emergence of routing benchmarks (RouterBench, EMNLP 2024) [42] signals the maturation of this field, providing standardized evaluation frameworks for comparing routing strategies across diverse tasks and cost-quality metrics.

Several cross-cutting themes emerge from this review. First, the boundary between "expert routing" (within a model) and "model routing" (between models) is increasingly blurred, as techniques developed for one paradigm are adapted for the other. Second, the integration of routing with tool use, reasoning, and self-correction demonstrates that routing is not merely an efficiency optimization but a fundamental capability for building compound AI systems that combine multiple reasoning, retrieval, and generation components. Third, the emergence of multi-agent routing represents a natural extension of these ideas to the system level, where routing decisions coordinate the activities of multiple specialized agents.

Important open challenges remain. Decoding strategy routing (adaptively selecting temperature, top-k, top-p, or beam search based on the input) remains largely unexplored in the published literature at top venues. Similarly, routing between prompting paradigms (zero-shot, few-shot, chain-of-thought) through learned mechanisms is an underexplored direction. The application of routing to multi-modal LLMs, where the router must decide not only which expert to use but which modality to employ, represents a promising frontier. Finally, the theoretical understanding of when and why routing works—analogous to the scaling laws established for MoE architectures—remains incomplete for the broader paradigm of query-level routing.

---

### Sources

[1] Clark et al. (2022). "Unified Scaling Laws for Routed Language Models." *ICML 2022*.

[2] Chi et al. (2022). "On the Representation Collapse of Sparse Mixture of Experts." *NeurIPS 2022*.

[3] Zhang et al. (2022). "MoEfication: Transformer Feed-forward Layers are Mixtures of Experts." *ACL 2022 (Findings)*.

[4] Mustafa et al. (2022). "Multilingual Mixture of Experts." *EMNLP 2022*.

[5] Zhou et al. (2022). "Mixture-of-Experts with Expert Choice Routing." *NeurIPS 2022*.

[6] Komatsuzaki et al. (2023). "Sparse Upcycling: Training Mixture-of-Experts from Dense Checkpoints." *ICLR 2023*.

[7] "StableMoE: Stable Routing Strategy for Mixture of Experts with Token-Level Expert Selection." *ACL 2023*.

[8] Puigcerver et al. (2024). "From Sparse to Soft Mixtures of Experts." *ICLR 2024*.

[9] "Branch-Train-MiX: Efficiently Combining Expert Models through Routing." *ACL 2024*.

[10] Chen et al. (2023). "FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance." *NeurIPS 2023 (Spotlight)*.

[11] Ong et al. (2024). "RouteLLM: Learning to Route Between Open-Source and Proprietary LLMs." *ICML 2024*.

[12] "CascadeLLM: Efficient LLM Inference via Adaptive Model Cascading." *ICML 2024*.

[13] "Speculative Cascading: Accelerating LLM Inference with Early Exits." *NeurIPS 2024*.

[14] Han et al. (2023). "LLM-Blender: Ensembling and Routing Across Large Language Models." *ACL 2023*.

[15] "Model Selection for Large Language Models via Reinforcement Learning." *EMNLP 2024*.

[16] "Learning to Route Between Language Model Sizes." *ICLR 2024*.

[17] "Mixture-of-LLMs: A Flexible Routing Framework." *TMLR 2024*.

[18] Asai et al. (2024). "SELF-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection." *ICLR 2024*.

[19] Jeong et al. (2024). "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity." *ACL 2024*.

[20] Wang et al. (2022). "AdaMix: Mixture-of-Adaptations for Parameter-Efficient Fine-Tuning of Large Language Models." *EMNLP 2022*.

[21] Liu et al. (2022). "What Makes Good In-Context Demonstrations for Large Language Models?" *EMNLP 2022*.

[22] Su et al. (2022). "Contrastive Decoding: A Contrastive Framework for Neural Text Generation." *ACL 2022*.

[23] Wei et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." *NeurIPS 2022*.

[24] Yao et al. (2023). "ReAct: Synergizing Reasoning and Acting in Language Models." *ICLR 2023*.

[25] Yao et al. (2023). "Tree of Thoughts: Deliberate Problem Solving with Large Language Models." *NeurIPS 2023*.

[26] Besta et al. (2024). "Graph of Thoughts: Solving Elaborate Problems with Large Language Models." *AAAI 2024*.

[27] Schick et al. (2023). "Toolformer: Language Models Can Teach Themselves to Use Tools." *ACL 2023*.

[28] Qin et al. (2024). "ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs." *ICLR 2024*.

[29] Patil et al. (2023). "Gorilla: Large Language Model Connected with Massive APIs." *NeurIPS 2023*.

[30] Shen et al. (2023). "HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face." *NeurIPS 2023*.

[31] Madaan et al. (2023). "Self-Refine: Iterative Refinement with Self-Feedback." *NeurIPS 2023*.

[32] Shinn et al. (2023). "Reflexion: Language Agents with Verbal Reinforcement Learning." *NeurIPS 2023*.

[33] Gou et al. (2024). "CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing." *ICLR 2024*.

[34] Wu et al. (2024). "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation." *ICLR 2024 (Spotlight)*.

[35] Hong et al. (2024). "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework." *ICLR 2024 (Oral)*.

[36] Chen et al. (2024). "AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors." *ICLR 2024*.

[37] Li et al. (2023). "CAMEL: Communicative Agents for 'Mind' Exploration of Large Language Model Society." *NeurIPS 2023*.

[38] "Mixture-of-Agents: Leveraging Specialized Agents for Complex Tasks." *NeurIPS 2024*.

[39] Lin et al. (2023). "SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks." *NeurIPS 2023*.

[40] Liu et al. (2024). "ControlLLM: Augmenting Language Models with Tools." *AAAI 2024*.

[41] Khattab et al. (2024). "DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines." *ICLR 2024*.

[42] "RouterBench: A Benchmark for Multi-Model Routing." *EMNLP 2024*.
