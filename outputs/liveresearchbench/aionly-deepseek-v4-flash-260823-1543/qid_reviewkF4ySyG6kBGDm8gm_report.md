# Related Work

## 1. Expert Routing in Mixture-of-Experts Architectures

The evolution of routing mechanisms within Mixture-of-Experts (MoE) large language models has progressed from static top-\(k\) gating to more dynamic, learned, and parameter-efficient strategies. While early MoE models such as the Switch Transformer (Fedus et al., 2021) established the foundation by routing each token to a single expert, the 2022–2025 period has seen a shift toward adaptive and composable expert selection. The *Efficient Large Language Models: A Survey* (Wan et al., 2024) provides a comprehensive overview of MoE architectures, including advances in sparse gating, expert balancing, and training stability, highlighting the critical role of routing in scaling model capacity without proportional compute increases [1].

A key development in this period is the integration of parameter-efficient fine-tuning (PEFT) with MoE routing. *PERFT: Parameter-Efficient Routed Fine-Tuning for Mixture-of-Expert Model* (Liu et al., 2025), published at ICLR 2025, introduces a unified framework that routes between PEFT modules (e.g., LoRA adapters) within an MoE architecture [2]. PERFT allows each expert to be fine-tuned with a small number of parameters while a learned router selects the appropriate expert composition for a given input, enabling efficient adaptation to diverse downstream tasks. This work demonstrates that routing can be applied not only at the token level but also at the module level, bridging the gap between model architecture and fine-tuning strategy.

Complementing this line, *L2R: Dynamic Adapter Routing in Continual Learning of Language Models* (ICML 2025) addresses the problem of catastrophic forgetting in continual learning by isolating the training of new PEFT modules and then learning to combine them via a router network [3]. L2R leverages a small memory of prior task examples to train the router, which dynamically selects which previously learned adapters to activate for a given input. This approach shows that routing can serve as a mechanism for composing specialized knowledge accumulated over time, offering a path toward lifelong learning in large language models.

These works collectively illustrate a trend from static, hand-designed routing in MoE to learned, dynamic routing that can adapt to task demands, resource constraints, and evolving knowledge. The combination of PEFT with MoE routing has opened new avenues for efficient fine-tuning and model composition, with PERFT and L2R representing two distinct but complementary approaches to expert routing beyond the traditional top-\(k\) gating paradigm.

## 2. Broader Routing Paradigms

Beyond expert routing within MoE architectures, a rich body of work has emerged on routing at the system level: allocating queries across different models, adaptation methods, retrieval depths, decoding strategies, and even multi-agent systems. This line of research is unified by the goal of optimizing the trade-off between performance and cost, where cost may refer to computational expense, latency, or monetary API fees.

### 2.1 Model Selection and Routing Across LLMs

The earliest systematic approach to cross-model routing was *FrugalGPT* (Chen et al., 2023), published in TMLR [4]. FrugalGPT proposes a cascade of LLMs where queries are first sent to a cheap model and only escalated to a more expensive model if the cheap model’s confidence is low. This simple yet effective strategy can match GPT-4 performance with up to 98% cost reduction. The paper also introduces prompt adaptation, caching, and fine-tuning of smaller models as complementary techniques for cost savings.

RouteLLM (Ong et al., 2025), presented at ICLR 2025, reframes LLM routing as a preference learning problem [5]. By training a router on human preference data from Chatbot Arena, RouteLLM learns to predict when a strong model (e.g., GPT-4) will outperform a weak model for a given query. The resulting router reduces costs by over 2× on MT Bench while maintaining 95% of GPT-4 performance. The paper shows that matrix factorization routers are particularly effective, requiring only 26% of GPT-4 calls to achieve near-optimal performance.

A unified theoretical treatment is provided by *A Unified Approach to Routing and Cascading for LLMs* (Dekoninck et al., 2025), published at ICML 2025 [6]. This work derives optimal strategies for both routing and cascading and introduces *cascade routing*, which iteratively selects the best model for each query rather than following a fixed sequence. Cascade routing consistently outperforms individual routing or cascading approaches by up to 14%, demonstrating the benefits of combining both paradigms.

Router-R1 (Zhang et al., 2025), a NeurIPS 2025 paper, extends routing to a multi-round, sequential decision process [7]. The router is itself an LLM that interleaves “think” actions (internal deliberation) with “route” actions (dynamic model invocation), trained via reinforcement learning with a reward balancing performance and cost. Router-R1 conditions on simple model descriptors (pricing, latency, example performance) and generalizes to unseen model selections, achieving strong results on seven QA benchmarks.

For real-world deployment, *SELECT-THEN-ROUTE* (EMNLP 2025 Industry Track) proposes a two-stage framework: first, a taxonomy-guided classifier selects a small, task-appropriate pool of candidate models; second, a confidence-based cascade routes each query within that pool [8]. This system achieves 94.3% accuracy (compared to 91.7% for the best single model, O3 Mini) while reducing inference cost by 4×, demonstrating the practical viability of routing in enterprise settings.

### 2.2 Adaptive Retrieval and RAG Routing

Routing is also critical in retrieval-augmented generation (RAG), where the depth and type of retrieval must be adapted to query complexity. *Adaptive-RAG* (Jeon et al., 2024), published at NAACL 2024, introduces a classifier that categorizes queries into three complexity levels: no retrieval, single-step retrieval, or multi-step retrieval [9]. The classifier is trained on automatically labeled data and dynamically selects the appropriate retrieval strategy, achieving a favorable balance between accuracy and efficiency. On open-domain QA datasets, Adaptive-RAG reduces the number of retrieval steps by over half compared to a fixed multi-step approach while maintaining comparable F1 scores.

RAGRouter (2025), presented at NeurIPS 2025, defines a new retrieval-augmented LLM routing problem that accounts for how retrieved documents dynamically affect answer quality [10]. RAGRouter uses document embeddings and RAG capability embeddings learned via contrastive learning to capture knowledge representation shifts, enabling informed routing decisions across multiple RAG systems. The framework outperforms the best individual LLM and existing routing methods on knowledge-intensive tasks, while a score-threshold mechanism allows low-latency deployment.

### 2.3 Routing Between Prompting and Decoding Strategies

The choice of prompting strategy—whether to use chain-of-thought (CoT), direct answer, or other structured prompts—can be routed based on query difficulty. *Pattern-CoT* (AAAI, 2024) enhances CoT by selecting demonstrations based on reasoning patterns rather than semantic similarity, improving performance on arithmetic reasoning tasks across multiple model families [11]. Although not a routing method per se, it illustrates that the composition of demonstrations can be optimized for different query types.

A more explicit routing approach is *RoutingGen* (AAAI, 2025), which dynamically routes queries to either direct few-shot prompting or a novel structured reasoning strategy called Intention Chain-of-Thought (ICoT) based on a difficulty classifier [12]. Inspired by dual-process theory, RoutingGen uses a lightweight classifier (Qwen3-8B) to estimate problem complexity. On simple tasks, direct prompting is used; on complex tasks, ICoT generates a two-stage reasoning process (Specification and Idea). RoutingGen achieves state-of-the-art Pass@1 on six code generation benchmarks while reducing token usage by 46.37% on average, demonstrating the cost-effectiveness of routing between prompting strategies.

DCoT (UKPLab, ACL 2025) introduces another approach: fine-tuning LLMs to generate a sequence of diverse chains of thought within a single inference step, enabling within-inference refinement without external feedback [13]. This method improves performance over standard CoT on tasks with large result state spaces, showing that routing can occur internally within a single model’s generation process.

Cross-lingual prompting (CLP) (EMNLP 2023) addresses routing across languages by using a two-stage prompting strategy: first, a cross-lingual alignment prompt to represent the task in English, then a task-specific solver prompt in the target language [14]. This can be seen as routing the reasoning process across language representations, improving zero-shot CoT performance on multilingual benchmarks.

### 2.4 Multi-Agent and Modular Controllers

Routing extends to multi-agent systems, where queries are decomposed and allocated to specialized agents. *AgentNet* (NeurIPS 2025) proposes a decentralized, RAG-based framework where agents autonomously evolve, specialize, and coordinate without a central orchestrator, using a directed acyclic graph (DAG) structure [15]. This paradigm enables fault tolerance and emergent collective intelligence, outperforming centralized systems in efficiency and scalability.

AgentMaster (NeurIPS 2025 Workshop) integrates both Anthropic’s Model Context Protocol (MCP) and Google’s Agent-to-Agent (A2A) protocol within a unified conversational interface, enabling dynamic coordination across agent-to-agent, agent-to-tool, and agent-to-resource channels [16]. The framework achieves high BERTScore and G-Eval scores, demonstrating robust inter-agent routing and query decomposition.

The *Lessons Learned* framework (NeurIPS 2025) addresses the challenge of varying performance across code LLMs by having multiple agents share knowledge through a solicitation-banking-selection mechanism [17]. A key finding is that a team of small LLMs using this approach can outperform a much larger LLM, highlighting the power of routing and collaboration among specialized models.

### 2.5 Benchmarking and Evaluation

To systematically evaluate routing strategies, *RouterBench* (Hu et al., ICML 2024 Workshop) provides a benchmark with over 405k precomputed inference records from 11 LLMs across diverse domains [18]. It introduces metrics such as cost–quality analysis and the Average Improvement in Quality (AIQ) for comparing routing policies. The dataset reveals an oracle router achieving ~0.96 mean performance at ~$0.30 mean cost, compared to GPT-4’s ~0.83 performance at ~$4.09 cost, underscoring the potential of routing to dramatically improve cost–performance trade-offs.

## Conclusion

The 2022–2025 period has witnessed a remarkable evolution in routing for large language models. Within MoE architectures, routing has moved from static top-\(k\) gating to learned, dynamic expert selection, with PEFT-based routing enabling efficient adaptation and continual learning. At the system level, routing now encompasses model selection, adaptive retrieval, prompting strategy selection, and multi-agent coordination, all unified by the goal of optimizing the performance–cost frontier. The proliferation of specialized routers, theoretical frameworks, and benchmarks reflects the growing recognition that no single model or strategy is optimal for all queries, and that intelligent routing is a key enabler of efficient, scalable, and high-performing LLM systems.

### Sources

[1] Efficient Large Language Models: A Survey: https://github.com/AIoT-MLSys-Lab/Efficient-LLMs-Survey/blob/main/README.md  
[2] PERFT: Parameter-Efficient Routed Fine-Tuning for Mixture-of-Expert Model: https://openreview.net/forum?id=PPjpGTPG5K&noteId=dlI6oh4zSl  
[3] L2R: Dynamic Adapter Routing in Continual Learning of Language Models: https://icml.cc/virtual/2025/poster/46753  
[4] FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance: https://www.semanticscholar.org/paper/FrugalGPT%3A-How-to-Use-Large-Language-Models-While-Chen-Zaharia/585f8b9725f5f5e5495c3508d39f70d1c053e190  
[5] RouteLLM: Learning to Route LLMs with Preference Data: https://www.lmsys.org/blog/2024-07-01-routellm  
[6] A Unified Approach to Routing and Cascading for LLMs: https://icml.cc/virtual/2025/poster/46183  
[7] Router-R1: Teaching LLMs Multi-Round Routing and Aggregation via Reinforcement Learning: https://neurips.cc/virtual/2025/poster/119214  
[8] SELECT-THEN-ROUTE: Taxonomy guided Routing for LLMs: https://aclanthology.org/2025.emnlp-industry.28.pdf  
[9] Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity: https://aclanthology.org/2024.naacl-long.389.pdf  
[10] RAGRouter: Learning to Route Queries to Multiple Retrieval-Augmented Language Models: https://neurips.cc/virtual/2025/poster/119935  
[11] Pattern-CoT: Enhancing Chain of Thought Prompting in Large Language Models via Pattern-Based Demonstration Selection: https://ojs.aaai.org/index.php/AAAI/article/view/34793/36948  
[12] RoutingGen: Intention Chain-of-Thought Prompting with Dynamic Routing for Code Generation: https://ojs.aaai.org/index.php/AAAI/article/view/37030/40992  
[13] DCoT: Fine-Tuning on Diverse Reasoning Chains Drives Within-Inference CoT Refinement in LLMs: https://github.com/UKPLab/acl2025-diverse-cot  
[14] Cross-lingual Prompting for Zero-shot CoT: https://aclanthology.org/2023.emnlp-main.163.pdf  
[15] AgentNet: Decentralized Evolutionary Coordination for LLM-based Multi-Agent Systems: https://neurips.cc/virtual/2025/poster/115584  
[16] AgentMaster: A Modular Multi-Agent Framework with A2A and MCP Protocols: https://neurips.cc/virtual/2025/137154  
[17] Lessons Learned: A Multi-Agent Framework for Code LLMs to Learn and Improve: https://neurips.cc/virtual/2025/poster/115952  
[18] RouterBench: A Benchmark for Multi-LLM Routing System: https://icml.cc/virtual/2024/39041
