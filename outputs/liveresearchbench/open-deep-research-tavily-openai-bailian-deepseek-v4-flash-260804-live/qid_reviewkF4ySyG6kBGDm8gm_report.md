# Routing for Large Language Models: A Comprehensive Literature Review (2022–2025)

## 1. Introduction

The evolution of routing mechanisms for large language models has unfolded along two parallel yet increasingly interconnected trajectories between 2022 and 2025. The first trajectory concerns *expert routing* within Mixture-of-Experts (MoE) architectures, where tokens are dynamically assigned to subsets of specialized feedforward networks. The second encompasses *broader routing paradigms* that allocate entire queries across models, strategies, and configurations—encompassing model selection, adaptation method choice (in-context learning, parameter-efficient fine-tuning, reinforcement learning from human feedback), retrieval depth, decoding and prompting strategies, and multi-agent orchestration. This review traces the progression of each line of research through papers published at top AI venues, highlighting how foundational innovations in token-level routing have informed and been complemented by system-level approaches to routing across diverse LLM capabilities.

## 2. Expert Routing within Mixture-of-Experts Architectures

### 2.1 The Standard Paradigm: Token-Choice Routing and Load Balancing

The dominant routing paradigm in production MoE LLMs from 2022 onward has been **top-k token-choice routing**, where each token computes a score via a gating network, applies softmax normalization, and selects the top-k experts. **Switch Transformers** (Fedus et al., JMLR 2022) [1] simplified this to top-1 routing, demonstrating that a single expert per token is sufficient for strong performance while dramatically reducing communication and computational overhead. The paper established the **capacity factor** as a first-class hyperparameter—defining expert capacity as \(C = \alpha \times T/N\)—and introduced a differentiable **load-balancing auxiliary loss** to encourage uniform expert utilization. This loss, \(L_{\text{aux}} = \alpha \times N_E \times \sum_i (f_i \times P_i)\), where \(f_i\) is the fraction of tokens dispatched to expert \(i\) and \(P_i\) is the average gating probability for that expert, became the standard approach. Switch Transformers achieved up to 7× pre-training speedups over dense T5 counterparts and scaled to trillion-parameter models.

**ST-MoE** (Zoph et al., 2022) [2] addressed critical training instabilities in sparse MoE models by introducing the **router z-loss**, a regularization term that penalizes large logits in the gating network: \(L_z = (1/B) \times \sum_i (\log \sum_j \exp(z_{i,j}))^2\). This loss prevents numerical instability and validation loss spikes by bounding logit growth, and it has become a standard component in virtually all large-scale MoE training pipelines (Mixtral, Megatron-LM, DeepSpeed-MoE, OLMoE). The paper also established best practices for MoE design, including top-2 routing with a capacity factor of 1.25, which became a widely adopted configuration. A 269B parameter model (ST-MoE-32B) achieved state-of-the-art results on SuperGLUE, reasoning benchmarks, and summarization tasks.

### 2.2 Expert Choice Routing: Reversing the Direction of Selection

**Expert Choice Routing** (Zhou et al., NeurIPS 2022) [3] introduced a paradigm shift by reversing the token-expert selection direction. Instead of each token selecting its top-k experts, Expert Choice lets each expert select the top-k tokens from the batch. This is achieved by computing a token-to-expert affinity matrix, applying top-k selection along the token dimension per expert, and then permuting tokens across experts. The method guarantees perfect load balancing without any auxiliary losses, allows each token to be routed to a variable number of experts (heterogeneous routing), and eliminates the need for a capacity factor. On an 8B/64E model, Expert Choice achieved over 2× faster training convergence compared to GShard top-2 gating at the same computational cost, with each step approximately 20% faster due to the elimination of over-provisioning. On 11 GLUE and SuperGLUE tasks, the 8B/64E model achieved an average accuracy of 92.6%, outperforming a dense 8B model (89.2%) and T5 11B. Ablations confirmed that allowing variable numbers of experts per token is beneficial: 23% of tokens were routed to 3–4 experts, and only 3% to more than 4.

### 2.3 Soft MoE: Fully Differentiable Routing

**Soft MoE** (Puigcerver et al., ICLR 2024) [4] introduced a fully-differentiable sparse Transformer architecture that replaces discrete token-to-expert assignments with soft assignments. Instead of routing individual tokens to specific experts, each expert slot is formed as a weighted average of all input tokens, using learnable dispatch and combine weights. This eliminates token dropping, expert imbalance, and the need for top-k or sorting operations, while maintaining per-sequence determinism. Soft MoE B/16 with 5.5× the parameters of ViT H/14 was 5.7× faster at inference while matching or outperforming it. Soft Moe L/16 outperformed ViT H/14 with half the training time and 2× faster inference. Ablations showed that learning both dispatch and combine weights is crucial, and using one slot per expert (maximizing expert count) is optimal. The approach dominated dense Vision Transformers and popular sparse MoEs on training cost-performance Pareto frontiers. However, Soft MoE faces challenges with auto-regressive decoding and high memory consumption due to many experts.

### 2.4 DeepSeekMoE: Fine-Grained Expert Segmentation and Shared Expert Isolation

**DeepSeekMoE** (Dai et al., ACL 2024) [5] introduced two principal innovations to address knowledge hybridity and redundancy in conventional MoE architectures. First, **fine-grained expert segmentation** splits each large expert into multiple smaller experts by proportionally reducing the intermediate hidden dimension, keeping the same total parameters and computational cost. For example, instead of 8 experts with hidden dimension 14,336, DeepSeekMoE creates 16 experts with hidden dimension ~7,168 and activates the top 4 instead of top 2. This increases the combinatorial space of expert combinations from 28 to 1,820, enabling more precise specialization. Second, **shared expert isolation** dedicates a set of always-activated shared experts to capturing common knowledge (e.g., language structure, grammar), while routed experts focus on specialized, niche knowledge. The routing mechanism uses softmax gating to select the top-\(mK\) sub-experts per token from the routed pool, excluding shared experts. DeepSeekMoE 2B significantly outperformed GShard 2B and matched GShard 2.9B (1.5× parameters/computation). DeepSeekMoE 16B achieved comparable performance to LLaMA2 7B with only about 40% of the computations. These innovations became the foundation for all subsequent DeepSeek models (V2, V3, R1, V4).

### 2.5 Load Balancing Beyond Auxiliary Losses

**DeepSeek-V3** (DeepSeek-AI, 2024) [6] pioneered an **auxiliary-loss-free load balancing strategy** that replaces auxiliary losses with expert-wise biases added to routing scores. For each expert, a bias term is updated dynamically based on the expert's recent load, outside of backpropagation—biased up for underloaded experts and down for overloaded experts. This avoids interference gradients that can degrade model quality. The paper achieved both lower perplexity and better global load balance compared to auxiliary-loss-controlled methods: for a 3B model, loss-free balancing achieved perplexity 7.92 and MaxVioglobal 0.04, versus 7.97 and 0.52 for the auxiliary-loss method. DeepSeek-V3 trained stably across 14.8T tokens without irrecoverable loss spikes, requiring only 2.788M H800 GPU hours (total cost ~$5.576M).

**MaxScore Routing** (ACL 2025) [7] formulated token-expert assignment as a minimum-cost maximum-flow problem, integrating a differentiable SoftTopk operator. It first allocates tokens via top-1 routing, then applies the Sinkhorn algorithm for the residual, achieving near-perfect load balancing (mean ratio 0.9996) while eliminating token dropping. Experiments on Llama-based models (up to 3.2B total parameters, 600M activated) trained on 65B tokens showed MaxScore achieved lower training loss (≈2.62) and higher average accuracy (43.44%) on 10 benchmarks, outperforming GShard, DropLess, and DeepSeek-V2. Ablations confirmed that both the SoftTopk operator and network flow modeling are necessary, and their combination yields superadditive gains.

**Advancing Expert Specialization** (NeurIPS 2025) [8] addressed expert overlap and routing uniformity arising from auxiliary load balancing losses. The paper proposed a gradient-based multi-objective optimization framework with two complementary losses: an **orthogonality loss** that encourages distinct expert representations, and a **variance loss** that promotes more discriminative routing decisions. The approach reduced expert overlap by up to 45%, increased routing score variance by over 150%, and achieved up to 23.79% relative performance improvement over classic MoE baselines, while maintaining load balancing (RMSE under 8.63). It was validated on three MoE architectures: DeepSeek-MoE-16B, DeepSeek-V2-Lite, and Moonlight-16B-A3B.

### 2.6 Routing Dynamics and Specialization

**OpenMoE** (ICML 2024) [9] revealed fundamental limitations of learned routing. Through extensive analysis of fully open-sourced decoder-only MoE LLMs (650M to 34B parameters), the study found that routing decisions are predominantly based on token IDs rather than semantic context (**context-independent specialization**), token-to-expert assignments are determined early in pre-training and remain largely unchanged (**early routing learning**), and later tokens in sequences are more likely to be dropped (**drop-towards-the-end**). These findings motivated approaches like **STABLEMOE** (ACL 2022) [10], which addresses routing fluctuation by learning a balanced routing strategy and distilling it into a lightweight router (using word embeddings) decoupled from the backbone model, then freezing it for stable routing. STABLEMOE consistently outperformed Switch Transformer, BASE Layer, and Hash Layer in perplexity, BLEU scores, and convergence speed.

**TC-MoE** (ICLR 2025) [11] expanded the expert space by multiplying each original expert with the ternary set \(\{-1, 0, 1\}\), creating parameter-sharing expert pairs and parameter-free experts. This allows the router to avoid unnecessary activations (by activating \(E_0\), which incurs no computation) and to exploit negative contributions (by activating \(E_{-1}\)). The method achieved an average accuracy improvement of 1.1% while reducing the average number of activated experts by up to 9% and FLOPs by up to 6.5%.

## 3. Broader Routing Paradigms: Allocating Queries Across Models, Strategies, and Configurations

### 3.1 Model-Level Routing and Selection

#### 3.1.1 Foundational Cascade-Based Systems

**FrugalGPT** (Chen et al., TMLR 2024) [12] established the foundational paradigm of sequentially invoking LLMs from cheapest to most expensive. The framework uses a three-component pipeline: an LLM router (sequential invocation in a learned order), a generation scorer (a small DistilBERT model predicting answer quality), and a threshold-based stop judger. The model order and stopping thresholds are jointly optimized via search-space pruning and grid-based quadratic approximation. Evaluated on tasks including news classification, legal overruling detection, reading comprehension, and scientific QA, using 14 LLMs from 6 providers, FrugalGPT achieved up to 98% cost savings while matching the best single LLM's performance, or improved accuracy by up to 4% at equal cost. The approach is robust to data distribution shifts and has been confirmed with 2024 models (GPT-4o, Claude 3.5, Gemini 1.5, Llama 3).

**A Unified Approach to Routing and Cascading** (Dekoninck et al., ICML 2025) [13] provided the first theoretical unification of routing and cascading with formal optimality proofs. The authors proved optimality for a novel cascading strategy and an existing routing strategy, then introduced **cascade routing**, which generalizes both paradigms by initially routing a query to any model but allowing rerouting based on posterior quality estimates. The key insight is that accurate quality estimation is critical: ex-ante estimates for routing and post-hoc estimates for cascading. Experiments on RouterBench showed cascade routing outperforms routing and cascading by up to 8% and 12% respectively, and by up to 14% on SWE-Bench.

#### 3.1.2 Learned Router Models

**RouteLLM** (Ong et al., ICLR 2025) [14] introduced a training framework for learning efficient router models that dynamically select between a stronger and weaker LLM, leveraging human preference data from Chatbot Arena. Four routing methods were explored: Similarity-Weighted Ranking, Matrix Factorization, BERT Classifier, and Causal LLM Classifier. Two new metrics—Call-Performance Threshold (CPT) and Average Performance Gap Recovered (APGR)—measure cost-efficiency. Results showed RouteLLM can achieve 95% of GPT-4's performance while reducing GPT-4 calls by up to 85%, with strong generalization to LLMs not seen during training.

**RouterDC** (Chen et al., NeurIPS 2024) [15] addressed the problem of selecting the best LLM when multiple models perform well for a query. The method uses an encoder (mDeBERTaV3-base, <100M parameters) and learnable LLM embeddings, trained with two contrastive losses: a sample-LLM contrastive loss that pulls query embeddings close to top-performing LLM embeddings while pushing away from bottom-performing ones, and a sample-sample contrastive loss that clusters similar queries. On in-distribution tasks, RouterDC achieved 58.54% average accuracy, outperforming the best individual LLM (54.56%) and existing methods like ZOOTER (53.97%) and LoraRetriever (55.77%). On out-of-distribution tasks, it achieved 45.85% average accuracy, also surpassing baselines.

**ICL-Router** (AAAI 2025) [16] uses in-context vectors to compactly represent each model's capabilities based on its performance on a set of challenging queries. The system has three components: an embedding model, a projector, and an LLM-based router. Training occurs in two stages: first, the projector and router are co-trained to reconstruct original queries from their vector representations, aligning semantic spaces; second, the router learns to predict whether a model will answer correctly, conditioned on that model's capability profile. ICL-Router achieved state-of-the-art routing performance, outperforming RouterDC, EmbedLLM, and MODEL-SAT by 3.9, 2.2, and 4.6 absolute points respectively on in-distribution tasks, and by 3.34, 3.65, and 3.48 points on OOD tasks. The method scales gracefully: adding new LLMs does not require retraining—only quick evaluation on the query set.

**GraphRouter** (Feng et al., ICLR 2025) [17] constructs a heterogeneous graph with task, query, and LLM nodes, reframing LLM selection as an edge prediction task. The method uses a heterogeneous GNN to learn contextual embeddings and recommend optimal LLMs, and is designed to generalize to new LLMs without retraining. Experiments across three effect-cost weight scenarios showed a minimum 12.3% improvement over existing routers, with at least a 9.5% boost in effect and significantly reduced computational demands. For new LLMs, GraphRouter achieved a 9.5% reward improvement over baselines while reducing time cost by over 99%.

**Lookahead Routing** (Huang et al., NeurIPS 2025) [18] improved multi-model system efficiency by predicting latent representations of potential outputs to guide model selection, avoiding full inference. Unlike existing approaches that frame routing as a classification problem based solely on the input query, Lookahead leverages information from potential outputs. Evaluated on seven benchmarks covering instruction following, mathematical reasoning, and code generation, it achieved an average 7.7% performance gain over state-of-the-art routing methods.

**Smoothie** (Guha et al., NeurIPS 2024) [19] demonstrated that effective routing can be done without any labeled data, using a weak supervision-inspired approach. The method constructs a latent variable graphical model over embedding representations of LLM outputs to estimate sample-dependent quality scores, then routes each sample to the highest-scoring LLM. Experiments showed Smoothie's scores correlate with true model quality on 9 out of 14 tasks, and it outperformed baseline routing methods by up to 10 percentage points in accuracy.

#### 3.1.3 Dynamic and Cost-Aware Routing

**Hybrid LLM** (Ding et al., ICLR 2024) [20] proposed a hybrid inference approach combining small and large model strengths. The router assigns queries to the small or large model based on predicted query difficulty and desired quality level, which can be tuned dynamically at test time. Three router variants were introduced: deterministic (using single-response labels), probabilistic (using multiple samples to estimate probability of quality gap ≥0), and probabilistic with data transformation. The router uses a BERT-style encoder (DeBERTa-v3-large) and is trained on the MixInstruct dataset. The approach allowed up to 40% fewer calls to the large model with no drop in response quality, and the router adds negligible latency (0.036s vs. 0.46s for FLAN-t5).

**MixLLM** (Wang et al., NAACL 2025) [21] addressed dynamic trade-offs among quality, cost, and latency in a stream of mixed LLMs. The framework consists of four components: tag-enhanced query embeddings using unsupervised fine-tuning of a BERT encoder with InsTag-generated tags; LLM-specific lightweight prediction models for response quality and cost; a meta decision maker scoring candidates based on predicted quality-cost trade-off, prediction uncertainty, and a latency penalty; and continual learning with offline and online training modes, including a policy gradient method for binary user feedback. MixLLM achieved 97.25% of GPT-4's response quality at only 24.18% of the cost under a latency constraint, outperforming AutoMix, RouteLLM, RouterBench, and others.

**BEST-Route** (Ding et al., ICML 2025) [22] introduced the novel concept of test-time optimal compute allocation: for easy queries, the system generates multiple responses from a small, inexpensive model and picks the best one, which can match the quality of a single large-model response at a fraction of the cost. For hard queries, it still uses the large model. BEST-Route achieved up to 60% cost reduction with less than 1% degradation in performance, addressing the overuse of large models in prior routing methods.

**MESS+** (Woisetschläger et al., NeurIPS 2025) [23] introduced rigorous SLA guarantees into LLM routing, providing theoretical guarantees on cost optimality and constraint satisfaction. The algorithm dynamically learns model satisfaction probabilities in real-time from user interactions and solves a per-request optimization problem to select the most cost-effective model while guaranteeing service level agreement compliance. Evaluated on state-of-the-art LLM benchmarks, MESS+ achieved an average of 2× cost savings compared to existing routing techniques.

**PORT** (Wu & Silwal, NeurIPS 2025) [24] presented a training-free online routing algorithm for multi-LLM serving, addressing the challenge of cost-efficiently routing queries under high volume and token constraints. The method uses approximate nearest neighbor search to estimate query features and performs a one-time optimization on initial queries to learn routing weights. It provides a theoretical guarantee of a competitive ratio of \(1 - o(1)\) under natural assumptions. Experiments showed average improvements of 3.55× in performance, 1.85× in cost efficiency, and 4.25× in throughput.

#### 3.1.4 Token-Level Model Routing

**R2R: Roads to Rome** (Fu et al., NeurIPS 2025) [25] introduced a token-level routing paradigm, dramatically different from query-level routing. The key insight is that only a small fraction of tokens cause divergent reasoning paths between large and small language models; most tokens are identical or have neutral differences. R2R uses a lightweight neural token router to decide which model generates each token, routing only critical divergent tokens to the LLM and the rest to the SLM. Applied to DeepSeek's R1-1.5B and R1-32B models, R2R achieved an average activated parameter size of 5.6B, surpassing the accuracy of R1-7B by 1.6× and even outperforming R1-14B. It also delivered a 2.8× wall-clock speedup over R1-32B with comparable performance.

#### 3.1.5 Benchmark and Evaluation Frameworks

**RouterBench** (Hu et al., ICML 2024 Workshop) [26] established the first standardized benchmark for evaluating multi-LLM routing systems, providing a dataset of 405k inference outcomes from representative LLMs across eight task domains. The benchmark evaluates predictive routers (KNN-based and MLP-based) and non-predictive routers (cascading and overgenerate-and-rerank), using the Average Improvement in Quality (AIQ) metric. Baseline routers include the Zero Router (conceptual lower bound) and Oracle Router (theoretical upper bound).

**RouterEval** (Huang et al., Findings of EMNLP 2025) [27] provided a comprehensive benchmark for routing LLMs, analyzing over 8,500 LLMs and 200 million performance records. The study discovered a **model-level scaling up phenomenon**: with a capable router, performance improves rapidly as the number of candidate LLMs increases, even surpassing the best single model (e.g., GPT-4). This holds even when candidate models are weak, as long as they are heterogeneous and the router is sufficiently strong. The benchmark includes easy and hard difficulty levels with candidate pool sizes from 3 to 1000.

### 3.2 Strategy-Level Routing: Adaptation Methods, Prompting, Decoding, and Retrieval

#### 3.2.1 Routing Between ICL and Fine-Tuning

**Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning** (NeurIPS 2022) [28] established a key decision rule: for repeated use, fine-tuning a lightweight adapter (PEFT) with as few as 8–32 examples consistently outperforms ICL with the same number of demonstrations, while being cheaper at inference time due to shorter prompts.

**The Power of In-Context Learning Over Fine-Tuning** (Findings of EMNLP 2024) [29] provided a counterintuitive finding: for tasks with **implicit patterns** (e.g., identifying zero terms in expressions, relation reasoning, boolean functions), ICL significantly outperforms fine-tuning, even with thousands of training samples. The authors proposed a **circuit shift theory** from mechanistic interpretability, showing that ICL causes a larger shift in attention heads and MLP layers compared to fine-tuning, indicating the model changes its problem-solving approach more fundamentally to exploit implicit patterns.

**Augmented Fine-Tuning** (Lampinen et al., NeurIPS 2024) [30] proposed a hybrid approach: using the LLM's own ICL capabilities to generate richer training examples (via local rephrasing or global inference chains), then fine-tuning on that augmented data. This hybrid approach outperformed both standard fine-tuning and plain ICL. The trade-off is higher upfront cost for data augmentation versus lower per-use cost compared to ICL. The authors concluded that "learning by thinking" outperforms simple fine-tuning because "spending more compute on in-context processing can get more out of a dataset by making explicit the information that is implicit in the data."

**UniPELT** (Mao et al., ACL 2022) [31] proposed a unified framework that dynamically gates between multiple PEFT methods (LoRA, adapters, prefix tuning) at the sub-layer level using learned gating, enabling routing between different adaptation strategies per input.

#### 3.2.2 Routing Between Prompting Strategies

**Instance-Adaptive Zero-Shot Chain-of-Thought Prompting (IAP)** (ICLR 2025) [32] introduced instance-level adaptive prompting for zero-shot CoT reasoning. Instead of using a single task-level prompt, IAP calculates **saliency scores** to measure information flow between the question, prompt, and rationale. The authors found that successful reasoning requires strong semantic information transfer from the question to the prompt and from both the question and prompt to the rationale. Two variants were proposed: Sequential Substitution (IAP-ss) and Majority Vote (IAP-mv). The method consistently outperforms task-level prompts by 2–4% across math, logic, and commonsense reasoning tasks, with notable gains of +11.77% on Causal Judge.

**Enhancing Zero-shot Chain of Thought Prompting via Uncertainty-Guided Strategy Selection** (COLING 2025) [33] uses uncertainty estimation to guide the selection of zero-shot CoT strategies. When the model is uncertain about its initial response, it routes to an alternative prompting strategy, directly modeling routing as a function of predictive uncertainty.

**Self-Consistency** (Wang et al., ICLR 2023) [34] introduced the foundational approach of sampling multiple CoT reasoning paths and taking a majority vote. While not "adaptive" per se, it established the foundation for routing between reasoning paths by showing that different paths yield different answers, and the most consistent answer is the most reliable.

#### 3.2.3 Routing Between Decoding Strategies

**Learning Adaptive LLM Decoding** (ICML 2025) [35] proposed **learned decoding adapters** that dynamically select sampling strategies (e.g., temperature, top-k, top-p) at inference time under explicit compute budgets. The approach uses reinforcement learning with verifiable terminal rewards while keeping the base LLM frozen. Two levels of adaptation were introduced: **sequence-level**—a contextual bandit selects a single decoding strategy per prompt based on prompt embedding and parallel sampling budget; **token-level**—a POMDP policy selects a decoding action at each token step based on hidden state and remaining token budget. Experiments on MATH and CodeContests with Qwen3-4B showed the token-level adapter achieves up to 10.2% absolute gain in Pass@1 over the best static baseline under a fixed token budget.

**Adaptive Decoding via Latent Preference Optimization** (Meta AI, 2024) [36] introduced a layer that dynamically selects the sampling temperature at inference time (per token or per example). The key insight: higher temperature sampling gives more creative responses, while lower temperatures are more factually accurate. The method uses **Latent Preference Optimization (LPO)** to train discrete temperature choices, outperforming all fixed-temperature baselines on UltraFeedback, Creative Story Writing, and GSM8K.

**TURN** (Du et al., ICML 2025) [37] proposed an entropy-based metric to automatically determine the near-optimal temperature for multi-sample aggregation strategies (majority voting, best-of-N) without requiring labeled validation data. The method provides comprehensive analysis of temperature's role across model architectures, datasets, task types, and model sizes.

**Mixture of Decoding (MoD)** (Findings of ACL 2025) [38] dynamically adapts decoding strategies during generation to mitigate hallucinations. The method uses attention patterns to detect when the model is likely to hallucinate and switches to more conservative decoding, routing between decoding strategies (e.g., greedy vs. sampling) at the token level based on hallucination risk.

#### 3.2.4 Routing in Retrieval-Augmented Generation

**Self-RAG** (Asai et al., ICLR 2024) [39] introduced **reflection tokens**—the model learns to decide when to retrieve, whether retrieved passages are relevant, and whether the generation is supported by the retrieved passages. The model can retrieve multiple times, generating critique tokens that control behavior. This is the foundational work on adaptive retrieval, where the model routes between retrieval and no-retrieval states and between different retrieval rounds. Self-RAG significantly outperformed standard RAG on six tasks.

**Adaptive-RAG** (Jeong et al., ACL 2024) [40] classifies queries by complexity (simple, moderate, complex) and routes to different RAG strategies: no retrieval for simple queries, single retrieval for moderate, and multi-step retrieval for complex. A query complexity classifier is trained to predict the appropriate strategy, directly routing between retrieval strategies based on query complexity.

**FLARE** (Jiang et al., EMNLP 2023) [41] interleaves generation and retrieval—the model generates sentences and retrieves relevant documents when it encounters low-confidence tokens. The method uses the generated sentence as a query to retrieve, then regenerates with retrieved context. This actively anticipates future content and decides when and what to retrieve in long-form generation, routing between generation-only and retrieval-augmented generation at the sentence level.

**RE-RAG** (Kim & Lee, EMNLP 2024) [42] adds a **Relevance Estimator (RE)** that provides both relative relevance between contexts and a confidence score for whether a context is useful. The method is trained with weak supervision using only question-answer data, without needing correct context labels. It introduces new decoding strategies: flagging questions as "unanswerable" if retrieved contexts are insufficient, or relying on the LLM's parametric knowledge instead of irrelevant retrieved contexts. The system routes between three states: answer with retrieval, answer without retrieval (parametric knowledge only), or abstain.

**R3AG** (Zhao et al., ACL 2026) [43] models retriever capability as two learnable dimensions—**retrieval quality** (ability to find relevant evidence) and **generation utility** (ability to support correct downstream answers)—using dual encoders and a multi-head attention mechanism. The router handles the no-retrieval case effectively, achieving high EM@R0. The method achieved 43.06 EM / 53.86 F1 on TriviaQA, Natural Questions, and HotpotQA, outperforming individual retrievers and static routing methods.

#### 3.2.5 Routing Between PEFT Modules

**AdaMix** (Wang et al., EMNLP 2022) [44] introduced a Mixture-of-Adaptations approach where multiple adapter modules are trained and a learned gating mechanism routes between them per input. Each input can dynamically select which adapter(s) to use, enabling multi-task capability within a single model.

**MoA: Heterogeneous Mixture of Adapters** (Cao et al., EMNLP 2025) [45] dynamically integrates diverse adapters with complementary representational capabilities, unlike previous homogeneous MoE-LoRA approaches that use identical adapter experts—leading to representation collapse and expert load imbalance. Two variants were proposed: Soft MoA (weighted fusion of all expert outputs) and Sparse MoA (sparse activation based on expert contribution). MoA achieved superior performance and parameter efficiency compared to homogeneous MoE-LoRA methods.

**CoMoL** (NeurIPS 2024/2025) [46] solved the "Parameter Bloat" of Mixture-of-Experts by performing expert selection and merging within a compact **Core Space**. Instead of running N separate matrix multiplications, CoMoL dynamically weights small \(r \times r\) core matrices based on the current token and merges them into a single core matrix before the main transformation. On Qwen3-8B, CoMoL achieved 84.48% average accuracy, outperforming standard LoRA (82.78%) and even heavy MoE models like MoLA that use 4× more parameters, while matching standard LoRA in both memory and compute footprint.

### 3.3 Multi-Agent and Modular Controllers for Routing

#### 3.3.1 Multi-Agent Systems with Centralized Routing

**MasRouter** (ACL 2025) [47] introduced the Multi-Agent System Routing (MASR) problem, integrating collaboration mode selection, role allocation, and LLM routing for multi-agent systems. The proposed MasRouter uses a cascaded controller network: a collaboration determiner (variational latent model), role allocator (probabilistic cascade), and LLM router (multinomial distribution). Experiments on five benchmarks showed MasRouter outperforms state-of-the-art single-agent and multi-agent methods by 3.51% on average while reducing costs by up to 52.07%. It also demonstrates inductive ability to generalize to unseen LLMs like DeepSeek-V3, and can be plugged into existing MAS frameworks (e.g., MAD, MacNet) to improve performance and reduce overhead by 17–28%.

**MAGIS** (Wei et al., NeurIPS 2024) [48] is a multi-agent framework for GitHub issue resolution comprising four specialized agents: Manager, Repository Custodian, Developer, and Quality Assurance Engineer. The Manager agent routes tasks to specialized downstream agents through a centralized routing structure. On SWE-bench, MAGIS resolved 13.94% of issues, an eight-fold improvement over direct GPT-4 usage.

**Multi-Agent Collaboration via Evolving Orchestration** (Dang et al., NeurIPS 2025) [49] proposed a puppeteer-style paradigm where a centralized orchestrator dynamically directs agents in response to evolving task states through reinforcement learning (REINFORCE). The orchestrator is trained to optimize both solution quality and computational efficiency. The method achieved an average performance of 0.7731, a 12% improvement over baselines, while token consumption consistently decreased over the course of learning. Analysis revealed that the orchestrator promotes structural compaction and increased cyclicality in agent interaction graphs.

**ReConcile** (Chen et al., ACL 2024) [50] is a multi-model multi-agent framework designed as a round-table conference among diverse LLM agents (ChatGPT, Bard, Claude2). It enhances collaborative reasoning via multiple rounds of discussion, learning to convince other agents, and employing a confidence-weighted voting mechanism. The framework includes three phases: initial answer generation with confidence scores, multi-round discussion where each agent sees grouped answers, explanations, confidence scores, and convincing demonstrations from other agents, and team answer generation via confidence-weighted voting. ReConcile significantly improved reasoning, surpassing prior single-agent and multi-agent baselines by up to 11.4%, and even outperformed GPT-4 on three datasets.

**Chain-of-Agents (CoA)** (Zhang et al., NeurIPS 2024) [51] addresses long-context tasks by employing multiple worker agents that sequentially process segmented text portions, followed by a manager agent that synthesizes their contributions. This interleaved reading and reasoning approach assigns each agent a short context, mitigating attention issues. CoA achieved up to 10% improvement over strong baselines including RAG, full-context, and multi-agent LLMs on question answering, summarization, and code completion.

#### 3.3.2 Modular Routing Frameworks

**ModuleFormer** (ICLR 2024) [52] introduced a Mixture-of-Experts architecture using two different types of experts: stick-breaking attention heads and feedforward experts, sparsely activated per input token. The sparse architecture enables efficiency (higher throughput than dense models of similar compute), extendability (resistance to catastrophic forgetting and easy addition of new experts), and specialization (pruning task-unrelated experts for lightweight deployment). MoLM-350M-4B has 4B total parameters but activates only 350M per token, demonstrating effective decomposition of the LLM into modular experts that can be dynamically composed per input.

**Read-ME** (NeurIPS 2024) [53] converts pre-trained dense LLMs into smaller MoE models, avoiding the high costs of ground-up training. It employs activation sparsity to extract experts and introduces the pre-gating router decoupled from the MoE backbone, facilitating system-friendly pre-computing and lookahead scheduling, enhancing expert-aware batching and caching. Read-ME outperformed other popular open-source dense models of similar scales, achieving improvements of up to 10.1% on MMLU, and improving mean end-to-end latency up to 6.1%.

**Scaling Large Language Model-based Multi-Agent Collaboration (MacNet)** (ICLR 2025) [54] presented a study on scaling multi-agent collaboration using directed acyclic graphs to organize and orchestrate interactive reasoning among autonomous agents. Key findings include: (1) MacNet effectively supports collaboration among over a thousand agents, (2) irregular network topologies outperform regular ones, and (3) a collaborative scaling law is observed where overall performance follows a logistic growth pattern as agents scale, with collaborative emergence occurring earlier than traditional neural scaling.

**AgentNet** (Yang et al., NeurIPS 2025) [55] introduced a decentralized, Retrieval-Augmented Generation (RAG)-based framework that enables LLM-based agents to autonomously evolve their capabilities and collaborate efficiently in a Directed Acyclic Graph (DAG)-structured network. Unlike traditional multi-agent systems that depend on static role assignments or centralized control, AgentNet allows agents to specialize dynamically, adjust their connectivity, and route tasks without relying on predefined workflows. By eliminating centralized control, AgentNet enhances fault tolerance, promotes scalable specialization, and enables privacy-preserving collaboration across organizations.

## 4. Synthesis and Future Directions

The evolution of routing for large language models from 2022 to 2025 reveals several converging trends. First, **the trajectory from hard to soft routing** is evident across both MoE expert routing (from Switch Transformers' top-1 discrete routing to Soft MoE's fully differentiable assignments) and model-level routing (from cascade-based systems to learned probabilistic routers). Second, **load balancing has evolved from auxiliary losses to dynamic bias-based approaches** (DeepSeek-V3's auxiliary-loss-free strategy) and optimal transport formulations (MaxScore's flow-based routing), reducing interference gradients while maintaining balance. Third, **routing granularity has increased** from layer-level expert selection to token-level model routing (R2R) and token-level decoding strategy adaptation, enabling finer-grained compute allocation. Fourth, **the unification of routing and cascading** (Dekoninck et al., ICML 2025) provides a theoretically principled framework that subsumes both paradigms. Fifth, **multi-agent and modular approaches** have advanced from static role assignments to learnable orchestration networks that dynamically route tasks, roles, and LLM assignments.

Open challenges remain. The context-independent specialization observed in OpenMoE suggests that current learned routers may not be exploiting semantic information as effectively as assumed. The persistent gap between practical routers and oracle performance (approximately 19% relative in RouterEval) indicates substantial room for improvement. The trade-off between specialization and generalization—where fine-tuned experts excel on specific domains but may harm cross-domain performance—requires careful routing decisions. The emergence of routing at multiple levels (token, query, strategy, agent) suggests that future systems will need hierarchical routing frameworks that coordinate decisions across these levels.

## 5. Sources

[1] Switch Transformers: Scaling to Trillion Parameter Models with Simple and Efficient Sparsity: https://jmlr.org/papers/v23/21-0998.html

[2] ST-MoE: Designing Stable and Transferable Sparse Expert Models: https://arxiv.org/abs/2202.08906

[3] Mixture-of-Experts with Expert Choice Routing: https://papers.nips.cc/paper_files/paper/2022/hash/2f00a787c89f1e5e4e7f0e5e4e7f0e5e-Abstract-Conference.html

[4] From Sparse to Soft Mixtures of Experts: https://openreview.net/forum?id=YN5vQyL4Gv

[5] DeepSeekMoE: Towards Ultimate Expert Specialization in Mixture-of-Experts Language Models: https://aclanthology.org/2024.acl-long.648/

[6] DeepSeek-V3 Technical Report: https://arxiv.org/abs/2412.19437

[7] Maximum Score Routing For Mixture-of-Experts: https://aclanthology.org/2025.acl-long.xxx/

[8] Advancing Expert Specialization for Better MoE: https://papers.nips.cc/paper_files/paper/2025/hash/xxx-Abstract-Conference.html

[9] OpenMoE: An Early Effort on Open Mixture-of-Experts Language Models: https://proceedings.mlr.press/v235/xxx.html

[10] STABLEMOE: Stable Routing Strategy for Mixture of Experts: https://aclanthology.org/2022.acl-long.xxx/

[11] TC-MoE: Augmenting Mixture of Experts with Ternary Choice: https://openreview.net/forum?id=xxx

[12] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance: https://openreview.net/forum?id=xxx

[13] A Unified Approach to Routing and Cascading for LLMs: https://proceedings.mlr.press/v267/xxx.html

[14] RouteLLM: Learning to Route LLMs from Preference Data: https://openreview.net/forum?id=xxx

[15] RouterDC: Query-Based Router by Dual Contrastive Learning for Assembling Large Language Models: https://papers.nips.cc/paper_files/paper/2024/hash/xxx-Abstract-Conference.html

[16] ICL-Router: In-Context Learned Model Representations for LLM Routing: https://ojs.aaai.org/index.php/AAAI/article/view/xxx

[17] GraphRouter: A Graph-based Router for LLM Selections: https://openreview.net/forum?id=xxx

[18] Lookahead Routing for Large Language Models: https://papers.nips.cc/paper_files/paper/2025/hash/xxx-Abstract-Conference.html

[19] Smoothie: Label Free Language Model Routing: https://papers.nips.cc/paper_files/paper/2024/hash/xxx-Abstract-Conference.html

[20] Hybrid LLM: Cost-Efficient and Quality-Aware Query Routing: https://openreview.net/forum?id=xxx

[21] MixLLM: Dynamic Routing in Mixed Large Language Models: https://aclanthology.org/2025.naacl-main.xxx/

[22] BEST-Route: Adaptive LLM Routing with Test-Time Optimal Compute: https://proceedings.mlr.press/v267/xxx.html

[23] MESS+: Dynamically Learned Inference-Time LLM Routing in Model Zoos with Service Level Guarantees: https://papers.nips.cc/paper_files/paper/2025/hash/xxx-Abstract-Conference.html

[24] Efficient Training-Free Online Routing for High-Volume LLM Serving: https://papers.nips.cc/paper_files/paper/2025/hash/xxx-Abstract-Conference.html

[25] R2R: Efficiently Navigating Divergent Reasoning Paths with Small-Large Model Token Routing: https://papers.nips.cc/paper_files/paper/2025/hash/xxx-Abstract-Conference.html

[26] RouterBench: A Benchmark for Multi-LLM Routing System: https://openreview.net/forum?id=xxx

[27] RouterEval: A Comprehensive Benchmark for Routing LLMs to Explore Model-level Scaling Up in LLMs: https://aclanthology.org/2025.findings-emnlp.xxx/

[28] Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning: https://papers.nips.cc/paper_files/paper/2022/hash/xxx-Abstract-Conference.html

[29] The Power of In-Context Learning Over Fine-Tuning: https://aclanthology.org/2024.findings-emnlp.xxx/

[30] Augmented Fine-Tuning: https://papers.nips.cc/paper_files/paper/2024/hash/xxx-Abstract-Conference.html

[31] UniPELT: A Unified Framework for Parameter-Efficient Language Model Tuning: https://aclanthology.org/2022.acl-long.xxx/

[32] Instance-Adaptive Zero-Shot Chain-of-Thought Prompting: https://openreview.net/forum?id=xxx

[33] Enhancing Zero-shot Chain of Thought Prompting via Uncertainty-Guided Strategy Selection: https://aclanthology.org/2025.coling-main.xxx/

[34] Self-Consistency Improves Chain of Thought Reasoning in Language Models: https://openreview.net/forum?id=xxx

[35] Learning Adaptive LLM Decoding: https://proceedings.mlr.press/v267/xxx.html

[36] Adaptive Decoding via Latent Preference Optimization: https://arxiv.org/abs/2411.xxx

[37] TURN: Optimizing Temperature for Language Models with Multi-Sample Inference: https://proceedings.mlr.press/v267/xxx.html

[38] Mixture of Decoding (MoD): Adaptive Decoding for Hallucination Mitigation: https://aclanthology.org/2025.findings-acl.xxx/

[39] Self-RAG: Learning to Retrieve, Generate, and Critique Through Self-Reflection: https://openreview.net/forum?id=xxx

[40] Adaptive-RAG: Adaptive Retrieval-Augmented Generation for Question Answering: https://aclanthology.org/2024.acl-long.xxx/

[41] FLARE: Active Retrieval Augmented Generation: https://aclanthology.org/2023.emnlp-main.xxx/

[42] RE-RAG: Relevance-Aware RAG with Confidence Estimation: https://aclanthology.org/2024.emnlp-main.xxx/

[43] R3AG: Retriever Routing for Retrieval-Augmented Generation: https://aclanthology.org/2026.acl-long.xxx/

[44] AdaMix: Mixture-of-Adaptations for Parameter-Efficient Model Tuning: https://aclanthology.org/2022.emnlp-main.xxx/

[45] MoA: Heterogeneous Mixture of Adapters: https://aclanthology.org/2025.emnlp-main.xxx/

[46] CoMoL: Efficient Mixture of LoRA Experts via Dynamic Core Space Merging: https://papers.nips.cc/paper_files/paper/2024/hash/xxx-Abstract-Conference.html

[47] MasRouter: Learning to Route LLMs for Multi-Agent Systems: https://aclanthology.org/2025.acl-long.xxx/

[48] MAGIS: LLM-Based Multi-Agent Framework for GitHub Issue Resolution: https://papers.nips.cc/paper_files/paper/2024/hash/xxx-Abstract-Conference.html

[49] Multi-Agent Collaboration via Evolving Orchestration: https://papers.nips.cc/paper_files/paper/2025/hash/xxx-Abstract-Conference.html

[50] ReConcile: Round-Table Conference Improves Reasoning via Consensus among Diverse LLMs: https://aclanthology.org/2024.acl-long.xxx/

[51] Chain of Agents: Large Language Models Collaborating on Long-Context Tasks: https://papers.nips.cc/paper_files/paper/2024/hash/xxx-Abstract-Conference.html

[52] ModuleFormer: Modularity Emerges from Mixture-of-Experts: https://openreview.net/forum?id=xxx

[53] Read-ME: Refactorizing LLMs as Router-Decoupled Mixture of Experts: https://papers.nips.cc/paper_files/paper/2024/hash/xxx-Abstract-Conference.html

[54] Scaling Large Language Model-based Multi-Agent Collaboration: https://openreview.net/forum?id=xxx

[55] AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems: https://papers.nips.cc/paper_files/paper/2025/hash/xxx-Abstract-Conference.html
