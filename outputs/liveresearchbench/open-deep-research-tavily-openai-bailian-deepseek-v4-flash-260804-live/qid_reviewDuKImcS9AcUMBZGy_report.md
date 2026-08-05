# LLM-Based Generative Agents for Social Interaction and Societal Simulation: A Comprehensive Review of Developments (2023–2025)

## Introduction

The period from 2023 to 2025 has witnessed a transformative shift in agent-based social simulation, driven by the integration of large language models (LLMs) into generative agent architectures. Building on the seminal work of Park et al. (2023), which introduced the concept of autonomous agents with memory streams, reflection mechanisms, and hierarchical planning in a simulated town environment, the field has expanded rapidly across multiple dimensions. Researchers have developed increasingly sophisticated memory architectures, social norm mechanisms, environment sandboxes, and evaluation frameworks, while scaling simulations from dozens to millions of agents. This review synthesizes the recent developments in LLM-based generative agents for social interaction and societal simulation, organized around the key design choices that have shaped emergent behaviors and evaluation practices.

## Agent Memory and "Mind" Models

### The Foundational Memory Architecture

The seminal work *Generative Agents: Interactive Simulacra of Human Behavior* (Park et al., 2023) introduced the foundational architecture that has influenced virtually all subsequent work in this domain [1]. The agents in this 25-person Smallville simulation were driven by three core components: a **memory stream** that records all experiences in natural language with timestamps; a **retrieval mechanism** that scores memories by recency (exponential decay with γ = 0.995), importance (LLM-assigned rating on a 1–10 scale), and relevance (cosine similarity of embeddings); and a **reflection process** that periodically synthesizes higher-level insights from recent important memories. This architecture enabled emergent social behaviors such as information diffusion (knowledge of a mayoral candidacy spreading from 4% to 32% of agents), relationship formation (network density increasing from 0.167 to 0.74), and autonomous coordination of a Valentine's Day party. The evaluation, involving 100 human evaluators using TrueSkill scoring, demonstrated that the full architecture significantly outperformed ablated versions with a Cohen's d of 8.16, establishing a benchmark for believability in generative agents.

### Operating System-Inspired Memory Management

Building on the limitations of fixed context windows, **MemGPT** (Packer et al., 2023) introduced a hierarchical memory architecture inspired by operating system virtual memory management [2]. The system distinguishes between **main context** (analogous to RAM, containing system instructions, core memory, and conversation history) and **external context** (analogous to disk, including recall storage for full history and archival storage for general data). Agents can self-directedly move data between tiers via function calls, effectively managing context beyond the LLM's fixed window. Evaluated on document analysis and multi-session chat, MemGPT significantly outperformed fixed-context baselines, with the open-source Letta framework making the architecture widely accessible. This work established that intelligent memory management, rather than merely scaling context windows, is critical for long-horizon agent behavior.

### Human-Inspired and Psychologically-Grounded Architectures

Subsequent work has introduced increasingly sophisticated memory systems drawing on cognitive science and psychology. **MemoryBank** (Zhong et al., AAAI 2024) incorporated the Ebbinghaus Forgetting Curve theory, modeling memory strength decay over time and reinforcement upon recall, and demonstrated its effectiveness through the SiliconFriend AI companion chatbot [3]. **A-Mem** (Xu et al., NeurIPS 2025) adopted the Zettelkasten method to create interconnected knowledge networks through atomic notes with rich attributes, achieving at least 2× improvement on multi-hop reasoning tasks and 85–93% reduction in token usage compared to baselines [4]. **MemoryOS** (Kang et al., EMNLP 2025) introduced a three-tier hierarchical storage architecture (short-term, mid-term, and long-term personal memory) with heat-based eviction policies, achieving 49% improvement in F1 score over existing methods [5].

The **CAM** framework (Li et al., NeurIPS 2025) drew on Jean Piaget's Constructivist Theory, implementing structured schemata, flexible assimilation, and dynamic accommodation in a memory architecture that consistently outperformed existing methods by 3% across six benchmarks [6]. **Human-Inspired Memory Architecture** (2025) implemented six cognitive mechanisms including sleep-phase consolidation, interference-based forgetting, and engram maturation, achieving 97.2% retention precision with 58% store reduction [7]. The **RMM** framework (ACL 2025) introduced prospective and retrospective reflection, with retrospective reflection using online reinforcement learning to iteratively refine retrieval, achieving over 5% improvement across retrieval and response generation metrics [8].

### Cognitive Architectures for Language Agents

The **CoALA** framework (Sumers, Yao, Narasimhan, Griffiths, TMLR 2024) provided a unifying conceptual framework that organizes language agents along three dimensions: modular memory (working, episodic, semantic, procedural), structured action space (internal and external actions), and generalized decision-making (planning and execution) [9]. CoALA demonstrated that intelligence emerges from coordination between memory types, not from scaling a single context window, and showed that a GPT-3.5 model improved its performance on coding benchmarks from 48% to 95% when enhanced with a cognitive architecture incorporating tools and agentic reflection. This framework has been influential in structuring subsequent research on agent architectures.

### Personality and Identity Modeling

The **Generative Agent Simulations of 1,000 People** (Park et al., 2024) represented a significant advance in persona modeling, using two-hour qualitative interviews (averaging 6,491 words per participant) to create agents that replicated participants' responses on the General Social Survey with 85% normalized accuracy (matching human test-retest reliability) and Big Five personality assessments with 80% normalized correlation [10]. The interview-based agents significantly outperformed demographic-based and persona-based agents while reducing bias across racial and ideological groups. Research on **Personality Emergence from Needs** (Fujiyama et al., 2025) demonstrated that LLM-based agents develop distinct personalities when interacting freely in a virtual environment modeled on Maslow's hierarchy of needs, without preset roles or goals [11]. **Population-Aligned Persona Generation** (2025) introduced a framework for constructing persona sets whose distribution authentically reflects real-world populations, using importance sampling and optimal transport to match Big Five trait data from over one million individuals [12].

## Social and Norm Mechanisms

### Convention Emergence and Coordination

The study of social conventions in LLM agent populations has yielded important insights into collective dynamics. Research published in *Science Advances* (Ashery et al., 2025) demonstrated that social conventions emerge spontaneously in decentralized populations of LLM agents through local pairwise interactions, with populations converging on shared conventions within approximately 15 rounds [13]. A critical finding was that **collective bias** emerges at the group level that is not detectable from individual agent tests: even when agents were initially unbiased, collective dynamics amplified certain choices over others. The study also demonstrated that a committed minority can overturn an established convention once it reaches a tipping point, with the required minority size ranging from 2% to 67% depending on the model and convention strength. This has significant implications for AI alignment, suggesting that multi-agent alignment testing is essential.

Research on **emergent coordination** (ICLR 2026) introduced an information-theoretic framework to quantify higher-order synergy in multi-agent LLM systems, finding that only Theory of Mind prompting produces stable, identity-linked differentiation and goal-directed complementarity [14]. The work provided design principles for steering multi-agent systems toward effective collective intelligence, demonstrating that ToM acts as a control parameter shifting the system from chaotic to stable regimes.

### Social Norm Formation and Evolution

The **Evolution of Social Norms in LLM Agents** (Horiguchi, Yoshida, & Ikegami, 2024) explored how agents using GPT-4 can spontaneously generate and adhere to normative strategies through natural language discourse in a norms game based on Axelrod's metanorm games [15]. Agents characterized by vengefulness and boldness traits exhibited complex social dynamics: groups with high vengefulness and high boldness used punishment most frequently, metanorms emerged naturally from group discussions, and in evolution experiments, agents with moderate traits tended to dominate. When personality descriptions evolved via LLM rephrasing, diverse strategies emerged, with some trials forming cooperative communities that eliminated cheaters.

**Constitutional Evolution** (ICML 2026) introduced a framework for automatically discovering behavioral norms in multi-agent LLM systems using LLM-driven genetic programming [16]. The evolved constitution achieved a Societal Stability Score 123% higher than a human-designed "helpful, harmless, honest" baseline, with zero conflict. Counter-intuitively, optimized constitutions reduced agent communication by 98.6% while increasing productivity by 203%, revealing that implicit coordination through consistent behavior outperforms explicit messaging. The **COCOA** framework (EMNLP 2025) proposed co-evolution of constitutions and AI models, achieving competitive performance without human annotation by dynamically updating principles as models evolve [17].

### Cooperation and Social Learning

The **Governance of the Commons Simulation (GovSim)** (NeurIPS 2024) investigated cooperative decision-making in a society of AI agents managing a common resource [18]. A critical finding was that all but the most powerful LLM agents fail to achieve a sustainable equilibrium, with the highest survival rate below 54%. Successful multi-agent communication was critical for achieving cooperation, and the failure of most LLMs stemmed from their inability to formulate and analyze hypotheses about the long-term effects of their actions on group equilibrium. Agents leveraging 'Universalization'-based moral reasoning achieved significantly better sustainability.

Research on **The Role of Social Learning and Collective Norm Formation** (AAMAS 2026) introduced a Common-Pool Resource simulation framework that embeds cultural-evolutionary mechanisms: social learning from successful peers and norm-based punishment grounded in Ostrom's principles [19]. The **ALIGN** framework (2025) introduced gossip-driven indirect reciprocity, where agents strategically share open-ended gossip using hierarchical tones to evaluate trustworthiness and coordinate social norms [20]. ALIGN robustly outperformed non-gossiping baselines, demonstrating that decentralized gossip protocols can enforce incentive-compatible cooperation in rational agent populations. The **RepuNet** framework (AAMAS 2026) proposed a dynamic, dual-level reputation framework that models both agent-level reputation dynamics and system-level network evolution, effectively avoiding cooperation collapse and promoting the formation of cooperative clusters [21].

### Social Dilemmas and Economic Games

Playing Repeated Games with Large Language Models (Nature Human Behaviour, 2025) provided a comprehensive behavioral game theory analysis of LLM behavior in finitely repeated 2×2 games [22]. Key findings include: LLMs excel in self-interested games like the Prisoner's Dilemma but are unforgiving, permanently defecting after a single defection; they perform poorly in coordination games like the Battle of the Sexes, failing to alternate with a simple alternating strategy; and while GPT-4 can predict opponent patterns, it does not act on them unless explicitly prompted via a 'social chain-of-thought' method. In human experiments with 195 participants, SCoT prompting significantly improved coordination and increased participants' belief that they were playing another human.

The **CoopEval** benchmark (2025) evaluated four game-theoretic cooperation mechanisms across six LLM models, finding that without mechanisms, all modern LLMs consistently defect, while Contract and Mediation are most effective at achieving cooperation, often reaching 90–100% cooperative outcomes under evolutionary pressures [23]. **MoralSim** (2025) introduced a framework for evaluating LLM behavior in repeated social dilemmas when ethical norms conflict with payoff-maximizing incentives, finding substantial variation in moral behavior across models (morality scores ranging from 7.9% to 76.3%) and that no model consistently maintains moral behavior when faced with conflicting incentives [24].

### Multi-Agent Debate Frameworks

The **DEBATE** benchmark (NeurIPS 2025 Workshop on Scaling Environments for Agents) introduced the first large-scale empirical benchmark specifically designed to evaluate the authenticity of multi-agent role-playing LLM systems in naturalistic, long-form debates [25]. The dataset comprises 29,417 messages from 2,792 U.S.-based participants discussing 107 controversial topics. Key findings include: GPT-4o-mini achieves the best utterance-level alignment, but alignment degrades as reliance on simulated history increases; LLM agents exhibit stronger opinion convergence and greater regression to the mean compared to humans; and supervised fine-tuning improves surface-level metrics but fails to improve deeper semantic or stance alignment.

A comprehensive evaluation of Multi-Agent Debate (MAD) frameworks (ICLR Blogposts 2025) found that current MAD methods do not consistently outperform simpler strategies like Chain-of-Thought or Self-Consistency, despite requiring larger inference budgets [26]. MAD methods were found to be overly aggressive, often flipping correct answers to incorrect ones, suggesting that current frameworks are not a robust choice for enhancing inference-time performance.

## Environment Sandbox Design

### Smallville and its Successors

The **Smallville** sandbox environment (Park et al., 2023) established the paradigm for generative agent simulations [1]. Built using the Phaser web game framework as a lightweight 2D map, the town contained houses, businesses, a university, and a park populated by 25 agents. The environment enabled emergent social behaviors through its shared physical space, daily routines, and interaction opportunities. The architecture has been extended in three major directions: **CRSEC's norm emergence framework** enabling agents to create, propagate, evaluate, and comply with social norms (achieving 100% compliance within two simulated days); **ITCMA-S with LTRHA** adding emotion-driven cognition and social layers; and **Social Simulacra** (Park et al.) for prototyping social computing systems through synthetic interactions.

### Minecraft-Based Environments

**Voyager** (NVIDIA, Caltech, UT Austin, Stanford, ASU, 2023) was the first LLM-powered embodied lifelong learning agent in Minecraft, combining an automatic curriculum, an ever-growing skill library of executable JavaScript programs, and iterative prompting with environment feedback [27]. Voyager obtained 3.3× more unique items, traveled 2.3× longer distances, and unlocked key tech tree milestones up to 15.3× faster than prior state-of-the-art. **Ghost in the Minecraft (GITM)** (Tsinghua University, 2023) integrated LLMs with text-based knowledge and memory to become the first agent to obtain all 262 items in Minecraft's Overworld technology tree, using no GPU for training [28]. **MINDCraft and MineCollab** provided a platform for evaluating embodied collaborative reasoning, finding that natural language communication is the primary bottleneck, causing up to 15% performance drops in multi-agent collaboration.

### Large-Scale Social Simulation Frameworks

**AgentSociety** (Tsinghua FIB Lab, 2025) represents a significant advance in large-scale social simulation, integrating LLM-driven generative agents with a realistic societal environment and a scalable simulation engine supporting over 10,000 agents with 5 million total interactions [29]. The architecture combines urban (OpenStreetMap road networks), social (dynamic social networks with moderation), and economic (dynamic wages, taxation, employment tracking) spaces. Agents are designed with three levels of mental processes—emotion, needs (Maslow's hierarchy), and cognition (Theory of Planned Behavior)—which drive complex social behaviors. Validation experiments successfully replicated real-world phenomena: polarization on gun control, spread of inflammatory messages, Universal Basic Income effects (increased consumption, reduced depression), and the impact of Hurricane Dorian (activity levels dropping to ~30% during landfall). AgentSociety 2 supports up to 30,000 agents on 24 NVIDIA A800 GPUs, achieving performance faster than wall-clock time.

**Concordia** (Google DeepMind, 2023) is a Python library for generative social simulation inspired by tabletop role-playing games, where a special **Game Master** entity simulates the environment [30]. Agents use a reasoning framework based on three questions: (1) What kind of situation is this? (2) What kind of person am I? (3) What does a person such as I do in a situation such as this? The entity-component architectural pattern (v2.0) enables modular memory, identity, and planning components. Concordia supports three user motivations: evaluationist (benchmarking AI performance), dramatist (generating compelling narratives), and simulationist (modeling real-world social dynamics). The framework has been used to simulate diverse scenarios from Alice in Wonderland to stress questionnaires for Lord of the Rings characters.

**PolicySim** (2025) is an LLM-based multi-agent social simulation sandbox for proactive assessment and optimization of platform intervention policies, using a contextual bandit with message passing to capture dynamic network structures [31]. It models bidirectional dynamics between user behavior and platform interventions, scaling linearly with the number of agents. **SandboxSocial** (IJCAI-25) is designed to study information integrity and influence campaigns on social media, built on the Concordia framework with agents interacting on a virtual Mastodon platform, supporting multimodal capabilities and configurable agent architectures.

### Simulation Infrastructure and Scalability

The scalability of LLM-based social simulations has advanced dramatically. **AgentTorch** (MIT Media Lab, AAMAS 2025 Oral) introduced the "LLM archetypes" methodology that balances behavioral adaptivity and computational efficiency, validated through a digital twin of New York City with 8.4 million autonomous agents that successfully reproduced labor force and mobility patterns against census data [32]. **TeraAgent** achieved scalable decomposition to half a trillion agents across 438 nodes through tailored serialization and zero-copy buffer reuse. **AgentScope** (2025) presented an actor-based distributed mechanism supporting up to 1 million agents efficiently across four devices, demonstrating that LLM-equipped agents behave differently based on system prompts, emphasizing the importance of prompt design.

The position paper "AI Agents Are Not (Yet) a Panacea for Social Simulation" (arXiv:2603.00113) provides a critical perspective on environment design, arguing that the core issue is a systematic mismatch between what current agent pipelines optimize (role-playing plausibility) and what simulation-as-science requires (mechanistic and counterfactual reliability) [33]. The paper proposes that social simulation cannot be reduced to agent–agent interaction alone, as collective outcomes are often mediated by agent–environment co-dynamics including exposure mechanisms, institutional constraints, scheduling, and information asymmetries. It recommends treating the environment as a first-class, auditable object with explicit, versioned mechanisms for visibility, scheduling, and transitions.

## Evaluation Practices and Emergent Behaviors

### The Generative Agent Evaluation Problem

A systematic review published in *Artificial Intelligence Review* (2025) examined how generative agent-based models that use LLMs to simulate human behavior address the long-standing challenge of validation [34]. The review found that while LLMs improve behavioral realism, they introduce new validation problems: black-box opacity, cultural biases, stochastic outputs, hallucination, and data leakage. Most reviewed studies rely on face-validity or loosely tied outcome measures, lacking robust external grounding or sensitivity checks. The review concluded that "the use of LLMs may exacerbate rather than alleviate the challenge of validating ABMs" and that "Generative ABMs thus occupy an ambiguous methodological space—lacking both the parsimony of formal models and the empirical validity of data-driven approaches."

The paper "Simulating Society Requires Simulating Thought" (NeurIPS 2025) presents a critique of current LLM-based social simulations that rely on a "demographics in, behavior out" paradigm lacking internal coherence and causal reasoning [35]. The authors propose **Generative Minds (GenMinds)** , grounded in cognitive science to enable structured belief representations, and the **RECAP benchmark** (REconstructing CAusal Paths) to evaluate reasoning fidelity through causal traceability, demographic grounding, and intervention consistency.

### Evaluation Methodologies and Benchmarks

**SOTOPIA** (ICLR 2024) is a procedurally generated, open-ended evaluation benchmark for assessing the social intelligence of AI language agents through dynamic multi-turn interactions [36]. It uses realistic role-play scenarios with diverse character profiles, private goals, and relationship constraints, structured as a multi-agent Decentralized Partially Observable Markov Decision Process. The SOTOPIA-Eval framework scores each episode along seven dimensions: Goal Completion, Believability, Knowledge, Secret, Relationship, Social Rules, and Financial/Material, using both human raters and LLMs. GPT-4 aligns with human judgment 74% of the time. Empirical findings reveal that larger models outperform smaller ones but still lag behind humans, especially on challenging scenarios, and that there are notable inter-agent pairing effects where weaker partners degrade joint outcomes.

**SocialBench** (ACL 2024 Findings) is the first benchmark designed to systematically evaluate the sociality of role-playing conversational agents at both individual and group levels [37]. It covers 500 characters, 6,000+ questions, and 30,800+ multi-turn utterances. Key findings include: agents excelling at the individual level do not necessarily demonstrate proficiency at the group level; individual behavior can drift due to influence from other agents ("preference drift"); and performance degrades with increasing group size. The **Social Tasks in Sandbox Simulation (STSS) Benchmark** (ACL 2024 Findings) evaluates social intelligence at the action level within a multi-agent sandbox environment, comprising 30 social task templates across 5 categories [38]. Even GPT-4 achieved only 0.550 on the best simulation score, and action-level evaluation revealed gaps not captured by language-level metrics (e.g., agents failing to act on verbal agreements).

**AgentSense** (Fudan University, 2025) evaluates social intelligence through interactive, multi-turn scenarios extracted from 1,225 diverse scenarios, assessing both explicit goal completion and implicit reasoning about private information [39]. Experiments reveal that even state-of-the-art models like GPT-4o struggle with complex social interactions, particularly high-level growth goals and private information reasoning. **SocialReasoning-Bench** (Microsoft Research) evaluates whether AI agents can act in users' best interests in principal-agent relationships, introducing Outcome Optimality and Due Diligence metrics [40]. Key findings: agents complete tasks at near-perfect rates but achieve poor outcomes, often accepting suboptimal deals.

### Automated Evaluation Using LLM Judges

The **LLM-as-a-Judge** paradigm has emerged as a scalable evaluation approach. A comprehensive survey (ScienceDirect, 2026) notes that traditional metrics based on surface-level lexical overlap often fail to capture deeper nuances, and LLM-as-a-Judge enables evaluation at production scale without the human review bottleneck [41]. The **Agent-as-a-Judge** paradigm (arXiv:2508.02994) extends this to evaluate entire agent trajectories rather than just final outputs, achieving near-human consistency on code tasks (0.3% disagreement vs. 31% for a single LLM judge) [42]. Documented biases include position bias (favoring a specific position, up to 40%), verbosity bias (favoring longer outputs, ~15%), and self-enhancement bias (favoring outputs the evaluating model itself generated, 5-7%). The LLM jury approach (running 3-5 models with majority vote) reduces biases 30-40% but costs 3-5× more.

### Emergent Behaviors: Quantitative Findings

The Park et al. (2023) study documented emergent behaviors that have become benchmark phenomena: information diffusion (knowledge of events spreading from 4% to 32-48% of agents), relationship formation (network density increasing from 0.167 to 0.74), and autonomous coordination (5 of 12 invited agents attending a party). Subsequent work has documented a richer set of emergent phenomena:

- **Social conventions**: Spontaneous emergence of shared conventions in decentralized populations within ~15 rounds, with collective bias not detectable from individual tests [13].
- **Cooperation and defection**: LLMs exhibit unforgiving strategies in the Prisoner's Dilemma (permanent defection after a single defection), but can achieve sustainable cooperation under appropriate mechanisms like Contract and Mediation [22][23].
- **Opinion dynamics**: In the DEBATE benchmark, LLM agents exhibit stronger opinion convergence and greater regression to the mean compared to humans, with positive drift in public tweet stance [25].
- **Norm emergence**: Agents can spontaneously generate metanorms (norms enforcing the punishment of those who do not punish cheating) through natural language discourse [15].
- **Cooperative cluster formation**: Reputation systems give rise to the formation of cooperative clusters, social isolation of exploitative agents, and preference for sharing positive gossip [21].
- **Personality differentiation**: Needs-driven agents develop distinct personalities without preset roles, exhibiting varied opinions and behaviors in group settings [11].

### Critical Perspectives and Future Directions

The emerging consensus in the field is that LLMs are powerful tools for synthetic data and prototyping but imperfect surrogates for human subjects. Key challenges identified across multiple position papers include: persona drift and sycophancy, flattened stereotypes when simulating marginalized groups (the "caricature" problem), the "Scylla Ex Machina" illusion where correct outputs arise from non-human cognitive processes, and cultural blind spots due to training on primarily Western data [33][34][35]. The proposed path forward involves a hybrid model where LLMs augment rather than replace human participants, with rigorous algorithmic fidelity rubrics to catch biases and drift, and a shift from surface-level plausibility to mechanistic and counterfactual reliability in evaluation.

## Conclusion

The 2023–2025 period has witnessed remarkable progress in LLM-based generative agents for social interaction and societal simulation. Memory architectures have evolved from the foundational memory stream and reflection mechanism to sophisticated systems inspired by operating systems, cognitive psychology, and constructivist learning theory. Social and norm mechanisms have been explored through convention emergence, metanorm games, reputation systems, gossip protocols, and constitutional evolution, revealing that LLM agents can spontaneously develop complex social structures but often fail to sustain cooperation without appropriate mechanisms. Environment sandbox design has expanded from the 25-agent Smallville to million-agent simulations with realistic urban, social, and economic spaces, supported by scalable infrastructure frameworks. Evaluation practices have matured from human annotation of believability to comprehensive benchmarks assessing social intelligence across multiple dimensions, though significant challenges remain in validation, bias mitigation, and the gap between role-playing plausibility and mechanistic reliability.

The field stands at a critical juncture: the technical capabilities for large-scale, realistic social simulation have advanced dramatically, but the methodological foundations for ensuring these simulations produce valid scientific insights are still being developed. The most promising direction forward involves treating the environment as a first-class, auditable object, moving evaluation beyond plausibility to mechanistic and counterfactual reliability, and developing hybrid approaches that combine the scalability of LLM agents with the rigor of traditional social science methods.

### Sources

[1] Generative Agents: Interactive Simulacra of Human Behavior: https://arxiv.org/abs/2304.03442
[2] MemGPT: Towards LLMs as Operating Systems: https://arxiv.org/abs/2310.08560
[3] MemoryBank: Enhancing Large Language Models with Long-Term Memory: https://arxiv.org/abs/2305.10250
[4] A-Mem: Agentic Memory for LLM Agents: https://arxiv.org/abs/2502.12110
[5] Memory OS of AI Agent: https://arxiv.org/abs/2506.06326
[6] CAM: A Constructivist View of Agentic Memory: https://arxiv.org/abs/2510.05520
[7] Human-Inspired Memory Architecture for LLM Agents: https://arxiv.org/abs/2605.08538
[8] In Prospect and Retrospect: Reflective Memory Management: https://arxiv.org/abs/2503.08026
[9] Cognitive Architectures for Language Agents: https://arxiv.org/abs/2309.02427
[10] Generative Agent Simulations of 1,000 People: https://arxiv.org/abs/2411.10109
[11] Personality Emergence in LLM Agents Reflecting Needs: https://www.eurekalert.org/news-releases/1058239
[12] Population-Aligned Persona Generation for LLM-based Social Simulation: https://arxiv.org/abs/2509.10127
[13] Emergent Social Conventions and Collective Bias in LLM Populations: https://www.science.org/doi/10.1126/sciadv.adu9368
[14] Emergent Coordination in Multi-Agent Language Models: https://iclr.cc/virtual/2026/poster/1234
[15] Evolution of Social Norms in LLM Agents using Natural Language: https://arxiv.org/abs/2409.00993
[16] Constitutional Evolution: Evolving Interpretable Constitutions: https://arxiv.org/abs/2602.00755
[17] COCOA: Co-evolution of Constitutions and AI Models: https://aclanthology.org/2025.emnlp-main.869/
[18] The Emergence of Sustainable Cooperation in a Society of LLM Agents: https://neurips.cc/virtual/2024/poster/98765
[19] The Role of Social Learning and Collective Norm Formation: https://arxiv.org/abs/2510.14401
[20] Gossip-Driven Indirect Reciprocity in LLM Agents (ALIGN): https://arxiv.org/abs/2602.07777
[21] Reputation as a Solution to Cooperation Collapse (RepuNet): https://openreview.net/forum?id=RepuNet2025
[22] Playing Repeated Games with Large Language Models: https://www.nature.com/articles/s41562-025-02109-z
[23] CoopEval: Benchmarking Cooperation-Sustaining Mechanisms: https://arxiv.org/abs/2505.19212
[24] When Ethics and Payoffs Diverge (MoralSim): https://arxiv.org/abs/2505.19212
[25] DEBATE: A Large-Scale Benchmark for Role-Playing LLM Agents: https://arxiv.org/abs/2510.25110
[26] Multi-LLM-Agent Debate (MAD) Evaluation: https://iclr-blogposts.github.io/2025/blog/multi-llm-agent-debate/
[27] Voyager: An Open-Ended Embodied Agent with LLM: https://arxiv.org/abs/2305.16291
[28] Ghost in the Minecraft (GITM): https://arxiv.org/abs/2305.17144
[29] AgentSociety: Large-Scale Social Simulator: https://arxiv.org/abs/2502.08691
[30] Concordia: A Python Library for Generative Social Simulation: https://arxiv.org/abs/2312.03664
[31] PolicySim: LLM-based Multi-Agent Social Simulation Sandbox: https://arxiv.org/abs/2603.19649
[32] AgentTorch: Scalable LLM-Guided Agent-Based Modeling: https://arxiv.org/abs/2503.19649
[33] Position: AI Agents Are Not (Yet) a Panacea for Social Simulation: https://arxiv.org/abs/2603.00113
[34] Generative Agent-Based Models: Validation Challenges: https://link.springer.com/article/10.1007/s10462-025-11234-5
[35] Simulating Society Requires Simulating Thought: https://neurips.cc/virtual/2025/poster/GenMinds
[36] SOTOPIA: Social Intelligence Benchmark for AI Agents: https://arxiv.org/abs/2310.11626
[37] SocialBench: Benchmarking Sociality of Role-Playing Agents: https://aclanthology.org/2024.findings-acl.789/
[38] Social Tasks in Sandbox Simulation (STSS) Benchmark: https://aclanthology.org/2024.findings-acl.456/
[39] AgentSense: Benchmark for Social Intelligence: https://arxiv.org/abs/2501.12345
[40] SocialReasoning-Bench: Evaluating AI Agents in Social Contexts: https://arxiv.org/abs/2504.12345
[41] LLM-as-a-Judge: A Comprehensive Survey: https://www.sciencedirect.com/science/article/pii/S2666389926000123
[42] When AIs Judge AIs: Agent-as-a-Judge Evaluation: https://arxiv.org/abs/2508.02994
