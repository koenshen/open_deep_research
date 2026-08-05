# Comprehensive Literature Review: Reinforcement Learning Algorithms for LLM Reasoning Beyond GRPO

## Abstract

This report presents a detailed analysis of ten reinforcement learning (RL) algorithms proposed to improve large language model (LLM) reasoning capabilities, moving beyond the Group Relative Policy Optimization (GRPO) approach. The algorithms examined—DAPO, GFPO, GMPO, GPPO, GPG, CPO, RPO, PPO, COPO, and GSPO—represent a diverse set of innovations addressing key limitations of GRPO, including entropy collapse, training instability, gradient variance, length inflation, and vanishing advantage signals. The review covers each algorithm's motivation, core innovations, empirical results, and limitations, with systematic comparisons to GRPO throughout. Cross-cutting themes reveal a convergence toward sequence-level optimization, gradient-preserving mechanisms, and explicit entropy control as the dominant directions for advancing RL-based reasoning in LLMs.

---

## 1. Introduction

The application of reinforcement learning to enhance LLM reasoning capabilities has undergone rapid evolution since the introduction of GRPO in DeepSeek-R1. While GRPO demonstrated that group-based advantage estimation without a critic network could effectively train reasoning capabilities, subsequent research has identified several critical limitations: entropy collapse during training, instability from token-level importance ratios, sensitivity to outlier rewards, wasted training signals when group outcomes are uniform, and uncontrolled length inflation. The ten algorithms reviewed here each address specific facets of these challenges, collectively advancing the field toward more stable, efficient, and capable reasoning systems.

---

## 2. GRPO Extensions and Direct Improvements

### 2.1 DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)

**Primary Source:** Yu et al., "DAPO: An Open-Source LLM Reinforcement Learning System at Scale," NeurIPS 2025 [1][2][3]

**Motivation and Core Innovation:** DAPO addresses the reproducibility crisis in LLM reasoning training by open-sourcing the entire system—algorithm, code, and dataset—while simultaneously improving upon GRPO's performance. The core innovation is a set of four targeted modifications to GRPO [1][5][6]:

1. **Clip-Higher (Decoupled Clipping):** Asymmetric clipping with ε_low=0.20 and ε_high=0.28, allowing low-probability tokens more room for probability increases. This widens the optimization range for exploration, directly counteracting entropy collapse.

2. **Dynamic Sampling:** Filters out prompt groups where all responses are correct (accuracy=1) or all incorrect (accuracy=0), ensuring every batch contains useful gradient signals.

3. **Token-Level Policy Gradient Loss:** Shifts from GRPO's sample-level loss to token-level calculation, reducing bias from variable response lengths and improving learning from long chain-of-thought sequences.

4. **Overlong Reward Shaping:** Introduces soft penalty mechanisms for truncated samples (safe_length=16384, max_length=20480), reducing reward noise from outputs exceeding token limits.

DAPO also removes the KL divergence penalty entirely, arguing that the model distribution should diverge significantly from the initial model during long-CoT reasoning training [6][7].

**Differences vs. GRPO:** DAPO fundamentally modifies four aspects of GRPO: clipping becomes asymmetric (GRPO uses symmetric ε=0.2), sampling becomes dynamic (GRPO uses uniform sampling), loss aggregation shifts to token-level (GRPO uses sample-level), and KL penalty is removed entirely. The reward design remains group-relative but uses simpler binary rewards (+1/-1).

**Empirical Setup:**
- **Model:** Qwen2.5-32B base model [1][2][4]
- **Training:** 128 H20 GPUs, batch size 512, 16 responses per prompt, DAPO-Math-17K dataset [1][4][5]
- **Results:**
  - AIME 2024: **50 points** (50% accuracy, avg@32) — outperforms DeepSeek-R1-Zero-Qwen-32B (47 points) with 50% fewer training steps [1][2][4]
  - Ablation without dynamic sampling: 50%; without token-level loss and dynamic sampling: 44% [10]
  - Reproduction runs show 52% accuracy on 16×8×H800 hardware [10]

**Limitations:** Techniques may not transfer to small models (Qwen2.5-0.5B case study showed clip-higher and dynamic sampling hurt performance) [9]. Can suffer from over-exploration (entropy explosion) in some settings [12]. Primarily validated on math reasoning (AIME 2024); generalization to other domains is less thoroughly tested.

---

### 2.2 GFPO (Group Filtered Policy Optimization)

**Primary Source:** Shrivastava et al., "Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning," arXiv:2508.09726, August 2025 [13][14][15]

**Motivation and Core Innovation:** GFPO addresses the length explosion problem in RLVR-trained LLMs, where models inflate response lengths to achieve accuracy gains. The core innovation is a filtering mechanism that samples larger groups of responses and retains only the top-k based on conciseness criteria before computing policy gradients [13][14][15].

Two filtering strategies are proposed:
1. **Shortest k/G:** Selects the shortest k responses from the sampled group
2. **Token Efficiency:** Selects responses with the highest reward-per-token ratio

The algorithm also incorporates **Adaptive Difficulty Allocation**, dynamically allocating more training samples (larger k) to harder prompts based on average group reward [13][14][15].

**Differences vs. GRPO:** GRPO uses all sampled responses for advantage estimation; GFPO retains only the filtered subset, setting others to zero advantage. GRPO allocates uniform resources per prompt; GFPO adaptively allocates more resources to harder prompts. GRPO has no mechanism to control output length; GFPO explicitly optimizes for conciseness.

**Empirical Setup:**
- **Model:** Phi-4-reasoning (14B) [13][14][15]
- **Training:** Larger groups per problem, 7% increase in training time [14]
- **Results:**
  - Shortest k/G filtering: 46-71% length reduction across benchmarks [14][15]
  - Token Efficiency filtering: 71-85% length reduction [14][15]
  - AIME 2025: 70.9% length reduction; AIME 2024: 84.6% reduction; GPQA: 79.7%; Omni-MATH: 82.6% [15]
  - Accuracy maintained at GRPO levels while cutting end-to-end latency by ~30% [14]
  - Out-of-distribution testing on coding tasks shows length inflation is also curbed [15]

**Limitations:** Increases training-time compute (though only 7%) to achieve inference-time savings [14]. Does not improve accuracy over GRPO—it maintains accuracy while reducing length [13][14]. Requires careful tuning of the filtering threshold (k) and the accuracy-conciseness trade-off.

---

### 2.3 GMPO (Geometric-Mean Policy Optimization)

**Primary Source:** Zhao et al., "Geometric-Mean Policy Optimization," arXiv:2507.20673, July 2025 [17][18][19]

**Motivation and Core Innovation:** GRPO's arithmetic mean of token-level importance ratios is sensitive to outlier values, leading to unstable, high-variance policy gradients. GMPO replaces the arithmetic mean with the geometric mean, which is inherently less sensitive to outliers [17][18][19].

The geometric mean produces objectives with smaller absolute values, leading to lower variance in the optimization landscape. From a gradient perspective, GMPO uses a holistic weight (geometric mean of all importance ratios) for each token, making updates robust to extreme values. The method is described as "plug-and-play"—simply replacing GRPO's arithmetic mean with the geometric mean of token-level rewards [17][18].

**Differences vs. GRPO:** GRPO uses arithmetic mean aggregation (sensitive to outliers); GMPO uses geometric mean (robust to outliers). GMPO enables wider clipping ranges without instability, maintains smaller KL divergence from the reference model, and exhibits higher and more stable token entropy [17][18].

**Empirical Setup:**
- **Models:** 7B (primary), 1.5B, 32B MoE, R1 distill model [17][18]
- **Results:**
  - GMPO-7B improves average Pass@1 by **4.1%** over GRPO on math tasks (AIME24, AMC, MATH500, OlympiadBench, Minerva) [17][18]
  - Multimodal Geometry3K: **1.4%** improvement [17]
  - R1 distill model: 63.4%; 1.5B model: 43.9%; 7B model: 52.7% [18]
  - Ablation studies confirm effectiveness of geometric mean, token-level clipping, and wider clipping ranges [17]

**Limitations:** Moderate improvements (4.1% on math, 1.4% on multimodal) suggest diminishing returns from this single modification [17]. Geometric mean can be more computationally expensive than arithmetic mean, though the difference is marginal. Effectiveness may depend on the specific distribution of importance ratios in the training data.

---

### 2.4 GPPO (Gradient-Preserving clipping Policy Optimization)

**Primary Sources:** Su et al., "Klear-Reasoner: Advancing Reasoning Capability via Gradient-Preserving Clipping Policy Optimization," arXiv:2508.07629, August 2025 [20][21]; Su et al., "CE-GPPO: Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization," ACL 2026 [12][22][23]

**Motivation and Core Innovation:** Standard PPO/GRPO uses hard clipping that zeros gradients for tokens outside the clipping interval (importance ratio < 1-ε or > 1+ε). This discards gradient signals from low-probability tokens, suppressing exploration and delaying convergence of negative samples. GPPO retains gradients from clipped tokens in a bounded, controlled manner by capping them using a stop-gradient operator [20][21][22].

The GPPO loss requires only one line of code modification from PPO/GRPO [20].

**CE-GPPO** extends this by identifying two critical token types for entropy regulation: PA&LP tokens (Positive-Advantage, Low-Probability) that encourage exploration, and NA&LP tokens (Negative-Advantage, Low-Probability) that accelerate exploitation. CE-GPPO introduces scaling coefficients β1 (for NA&LP, left-clip) and β2 (for PA&LP, right-clip) for fine-grained entropy control [12][22][23].

**Differences vs. GRPO:** GRPO zeros gradients for clipped tokens; GPPO preserves them in bounded form. GRPO has no explicit entropy control; CE-GPPO provides tunable β1/β2 coefficients for fine-grained exploration-exploitation balance. GPPO shows faster correction of suboptimal actions and more stable training.

**Empirical Setup:**
- **Klear-Reasoner (GPPO):** Qwen3-8B-Base, two-stage pipeline (SFT + RL), 88K math + 18K code samples [20][21]
  - AIME 2024: **90.5%** (SOTA among 7-8B models) [20][21]
  - AIME 2025: **83.2%**; HMMT 2025: **70.8%**; LiveCodeBench V5: **66.0%**; V6: **58.1%** [20][21]
- **CE-GPPO:** DeepSeek-R1-Distill-Qwen-1.5B and 7B [12][22]
  - Consistently outperforms GRPO, DAPO, CISPO, GSPO by 2.5-3 points average on math benchmarks [12][22]
  - β1=0.5-0.75, β2=1 yields robust performance [12]

**Limitations:** β hyperparameters in CE-GPPO require tuning, though the method is described as robust to choices [12][22]. Adds complexity compared to standard GRPO. Klear-Reasoner combines GPPO with other techniques, making isolated contribution difficult to assess [21].

---

### 2.5 GPG (Group Policy Gradient)

**Primary Source:** Chu et al., "GPG: A Simple and Strong Reinforcement Learning Baseline for Model Reasoning," ICLR 2026 [24][25][26]

**Motivation and Core Innovation:** Existing RL methods rely on surrogate loss functions, critic networks, reference models, and KL divergence constraints, adding complexity, computational overhead, and potential biases. GPG is a minimalist approach that directly optimizes the original RL objective (policy gradient) without surrogate losses, critic models, reference models, or KL divergence constraints [24][25][26].

GPG addresses reward bias and gradient estimation bias using simple advantage normalization and a thresholding mechanism for valid samples. It eliminates both the critic and reference models, avoids KL divergence entirely, and directly optimizes the policy gradient by normalizing group-level rewards [24][25][26].

**Differences vs. GRPO:** GRPO uses a surrogate loss with clipping and a reference model for KL penalty; GPG uses direct policy gradient optimization with no surrogate losses, no critic, no reference model, and no KL constraints. GPG is significantly simpler and more computationally efficient.

**Empirical Setup:**
- **Models:** 1.5B and 7B (GPG-7B) [24][25][26]
- **Results:**
  - **Unimodal (Math):** GPG-7B achieves **57.7%** average accuracy on five math benchmarks (AIME24, MATH-500, AMC23, Minerva, OlympiadBench), outperforming Oat-Zero-7B (51.4%) by **+6.3%** [24][25][26]
  - **Multimodal:** CV-Bench visual reasoning: **76.15%** vs GRPO 59.47% (+16.68%); GEOQA: +3.32%; Fine-grained classification: **89.0%** vs 81.9% (+7.1%); LISA reasoning grounding: **51.8%** mIoU vs 37.6% (+14.2%) [24][25][26]
  - Ablation studies confirm removing KL constraints and using group-level reward normalization yields better performance [24][25]

**Limitations:** Without KL divergence constraints, the policy could theoretically diverge significantly from the initial model, though empirical results show this is not a problem in practice [24][25]. The paper does not extensively discuss scenarios where the direct policy gradient approach might underperform.

---

## 3. Addressing Specific GRPO Failure Modes

### 3.1 COPO (Consistency-Aware Policy Optimization)

**Primary Source:** Han et al., "COPO: Consistency-Aware Policy Optimization," arXiv:2508.04138, 2025 [7]

**Motivation and Core Innovation:** When multiple sampled responses under a single prompt converge to identical outcomes (all correct or all incorrect), GRPO's group-based advantage degenerates to zero, causing vanishing gradients and wasted training samples. COPO addresses this by introducing a structured global reward based on outcome consistency [7].

The core innovation is an **entropy-based soft blending mechanism** that adaptively balances local advantage estimation (intra-group, GRPO-style) with global optimization (inter-group, across prompts in a batch). The blending weight is a sigmoid function of the consistency entropy of responses: high entropy (diverse answers) favors local optimization, low entropy (uniform answers) favors global optimization [7].

**Differences vs. GRPO:** GRPO's advantage collapses to zero when all outcomes are identical; COPO provides meaningful gradients through global optimization. GRPO uses only intra-group advantage; COPO adds inter-group (batch-level) reward signals. COPO introduces an entropy-based blending mechanism absent in GRPO.

**Empirical Setup:**
- **Models:** Qwen2.5-Instruct 3B and 7B [7]
- **Training Data:** DAPO-MATH-17k [7]
- **Results:**
  - **COPO-7B vs GRPO-7B:** MATH-500 mean@8: 65.8% vs 63.58% (+2.22%); AIME 2024 mean@64: 13.85% vs 12.86% (+0.99%) [7]
  - **COPO-3B vs GRPO-3B:** MATH-500 mean@8: 60.38% vs 55.83% (+4.55%) [7]
  - COPO also significantly outperforms DAPO on these benchmarks [7]
  - Ablation studies confirm leveraging "ineffective" data (all-zero advantage) via global optimization improves performance [7]

**Limitations:** Introduces additional hyperparameters (γ, ρ for soft blending) requiring tuning [7]. Global reward computation depends on batch-level statistics, which may be sensitive to batch composition. Demonstrated primarily on mathematical reasoning; generalization to other domains is unestablished.

---

### 3.2 GSPO (Group Sequence Policy Optimization)

**Primary Source:** Zheng et al., "Group Sequence Policy Optimization," Qwen Team, Alibaba Group, arXiv:2507.18071, July 2025 [8]

**Motivation and Core Innovation:** GSPO addresses a fundamental flaw in GRPO: the mismatch between the unit of reward (sequence-level) and the unit of optimization (token-level). Token-level importance ratios introduce high-variance noise, especially when training large Mixture-of-Experts (MoE) models on long responses, leading to training instability and expert-activation volatility [8].

The core innovation is the use of **sequence-level importance weighting** instead of token-level. The importance ratio for each group sample is defined as the geometric mean of token-level probabilities: s_i(θ) = [π_θ(y_i|x) / π_θ_old(y_i|x)]^(1/|y_i|). This length-normalized sequence-level ratio aligns the optimization unit with the granularity of reward assignment (at the end of a sequence), reducing gradient variance [8].

GSPO also incorporates **optimistic lookahead** (predicting future gradients) and **adaptive meta-gradient updates** to accelerate convergence and stabilize training.

**Differences vs. GRPO:** GRPO uses token-level importance ratios; GSPO uses sequence-level (length-normalized). GRPO clips at the token level; GSPO clips at the sequence level. GSPO significantly reduces gradient variance and eliminates the need for Routing Replay strategies in MoE training. GSPO can use inference-engine likelihoods directly, while GRPO requires recomputation with training engines.

**Empirical Setup:**
- **Models:** Qwen3-30B-A3B-Base, Qwen3-235B-A22B-Instruct [8]
- **Results:**
  - GSPO outperforms GRPO on AIME'24, LiveCodeBench, and CodeForces with stable training and consistent performance gains [8]
  - The fraction of tokens clipped in GSPO is two orders of magnitude higher than in GRPO, yet GSPO still achieves higher training efficiency [8]
  - GSPO fundamentally resolves the expert-activation volatility issue in MoE models, obviating the need for Routing Replay [8]
  - Independent verification: GSPO shows reward improvement of -1.4% vs GRPO -3.8%, clipping stability 50-75% vs 0.01%, and stable training vs unstable [8]
  - Successfully used in training the latest Qwen3 models [8]

**Limitations:** May have limited impact on dense (non-MoE) models compared to significant benefits for MoE models [8]. Compatibility issues may arise with existing RL infrastructure. Performance depends on group size and quality of group-based advantage estimation.

---

## 4. Preference Optimization and Alternative Paradigms

### 4.1 CPO (Chain of Preference Optimization / Comparative Policy Optimization)

**Important Note:** Two distinct algorithms share the CPO acronym. The user's request specifies "Comparative Policy Optimization," but the more prominent algorithm in the LLM reasoning literature is Chain of Preference Optimization. Both are analyzed below.

**Variant 1: Chain of Preference Optimization (NeurIPS 2024)**

**Primary Source:** Zhang et al., "Chain of Preference Optimization: Improving Chain-of-Thought Reasoning in LLMs," NeurIPS 2024 [1]

**Motivation and Core Innovation:** Tree-of-Thought (ToT) reasoning achieves better performance than Chain-of-Thought (CoT) by exploring multiple reasoning paths, but at significant inference cost. CPO fine-tunes LLMs to align each step of CoT reasoning paths with those of ToT using preference information from the tree-search process, shifting computational burden to training [1].

**Differences vs. GRPO:** CPO is a preference optimization method (using DPO), not a policy gradient RL method. CPO uses offline preference pairs from ToT search, while GRPO is online, on-policy RL. CPO uses no reward model or critic; GRPO eliminates the critic but uses group-based reward normalization.

**Empirical Results:**
- Improves accuracy over CoT by **4.3%** on average across seven datasets
- Achieves comparable or better performance than ToT while being **57.5× faster** during inference
- Outperforms TS-SFT (supervised fine-tuning on selected paths) by 2.7%

**Variant 2: Comparative Policy Optimization (EMNLP 2025 Findings)**

**Primary Source:** Ye et al., "CPO: Addressing Reward Ambiguity in Role-playing Dialogue via Comparative Policy Optimization," EMNLP 2025 Findings [2]

**Motivation and Core Innovation:** Traditional RLFT struggles with reward ambiguity in subjective tasks because sample-wise scoring is unstable. CPO shifts from sample-wise to group-wise comparative reward estimation, improving human agreement by about 20% [2].

**Differences vs. GRPO:** While GRPO uses group-relative advantages based on outcome rewards (correctness), CPO uses group-wise comparative reward estimation for subjective tasks. CPO's innovation is in the reward estimation paradigm, not the policy optimization objective itself.

**Empirical Results:**
- Consistently outperforms vanilla GRPO across multiple backbone models (Qwen2.5-7B, Qwen2.5-14B, LLaMA3-8B)
- Group-wise scoring yields 25% improvement in correlation over sample-wise scoring on DeepSeek-R1, 21% on GPT-4o, 15% on Qwen-2.5-72b

---

### 4.2 RPO (Reparameterization Proximal Policy Optimization)

**Important Caveat:** This RPO paper applies to continuous control and robotics using differentiable simulation, not specifically to LLM reasoning. It is included for completeness but should be understood as a separate domain.

**Primary Source:** Zhong et al., "Reparameterization Proximal Policy Optimization," ICLR 2026 submission [3]

**Motivation and Core Innovation:** Reparameterization policy gradient (RPG) suffers from high-variance gradients that destabilize learning. RPO draws inspiration from PPO to create a stable, sample-efficient RPG-based method for differentiable simulation. It establishes a connection between PPO's surrogate objective and RPG, enabling multiple epochs of stable sample reuse through backpropagation through time (BPTT) [3].

**Differences vs. GRPO:** RPO is designed for differentiable simulation/continuous control, not LLM text generation. RPO uses BPTT through differentiable dynamics; GRPO uses likelihood-based policy gradients. RPO is not directly applicable to LLM reasoning as currently formulated.

**Results:** Achieves state-of-the-art results on five challenging continuous control tasks. Completes training (10 million steps) in ~81 minutes vs SHAC's ~313 minutes.

---

### 4.3 PPO (Proximal Policy Optimization)

**Primary Source:** Schulman et al., "Proximal Policy Optimization Algorithms," 2017 [4]; Ouyang et al., "Training language models to follow instructions with human feedback," 2022 [5]

**Motivation and Core Innovation:** PPO enables stable, data-efficient policy optimization by using a clipped surrogate objective that limits how far the new policy can deviate from the old. The probability ratio r_t(θ) = π_θ(a_t|s_t) / π_θ_old(a_t|s_t) is clipped to [1-ε, 1+ε], preventing overly aggressive updates while allowing multiple epochs of sample reuse [4].

In the RLHF context, PPO is used with a trained reward model and KL divergence penalty against a reference model to prevent reward hacking. The final reward function combines the reward model output with a KL penalty term [5].

**Differences vs. GRPO:** PPO requires four models (actor, critic, reward, reference); GRPO eliminates the critic, requiring only three (or two with rule-based rewards). PPO uses Generalized Advantage Estimation (GAE) with a learned value function; GRPO uses group-normalized rewards. PPO has higher memory overhead (40-60% more than GRPO) and training costs roughly 18× higher.

**Role in the Current Landscape:** PPO remains the standard for RLHF alignment in models like GPT-4, LLaMA-2, and Sparrow, but is increasingly being replaced by GRPO and its variants for reasoning-specific tasks due to the latter's lower computational cost and simpler infrastructure.

**Limitations:** Four-model overhead makes it memory-intensive and only feasible for large labs. Exhibits length bias, vulnerability to reward hacking, and sensitivity to hyperparameters. Training instability under long rollouts is a known issue.

---

## 5. Cross-Cutting Analysis and Trends

### 5.1 The Evolution Beyond GRPO

The ten algorithms reviewed reveal a clear trajectory of innovation beyond GRPO, addressing its core limitations through several recurring themes:

**Entropy Control:** DAPO (Clip-Higher), GPPO/CE-GPPO (gradient preservation), and GMPO (geometric mean) all address entropy collapse, the phenomenon where GRPO-trained models lose diversity in token probabilities. DAPO widens the clipping range for positive updates; GPPO preserves gradients from low-probability tokens; GMPO stabilizes the optimization landscape to maintain higher entropy.

**Gradient Variance Reduction:** GSPO (sequence-level ratios), GMPO (geometric mean), and GPG (direct policy gradient) all tackle the high-variance gradients that plague GRPO's token-level optimization. GSPO aligns the optimization unit with the reward unit; GMPO uses outlier-resistant aggregation; GPG eliminates surrogate losses entirely.

**Data Efficiency:** COPO (global optimization), DAPO (dynamic sampling), and GFPO (filtering mechanisms) improve the utilization of training signals. COPO recovers gradients from samples with uniform outcomes; DAPO filters out uninformative prompts; GFPO selects the most informative responses.

**Length Control:** GFPO (explicit filtering) and GSPO (sequence-level normalization) address the length inflation problem. GFPO achieves 46-85% length reduction while maintaining accuracy.

**MoE Stability:** GSPO fundamentally resolves the expert-activation volatility issue in Mixture-of-Experts models, a critical challenge for scaling RL training to large models.

### 5.2 Empirical Convergence Points

The reported results across these algorithms converge on several key findings:

- **AIME 2024** serves as the primary benchmark, with scores ranging from 12.86% (GRPO-7B) to 90.5% (Klear-Reasoner-8B/GPPO)
- **Qwen2.5-32B** and **Qwen3-8B** are the most common base models
- **Group size of 16** and **batch sizes of 128-512** are typical configurations
- **DAPO-MATH-17K** has emerged as a standard training dataset
- **Binary verifiable rewards** (+1/-1) are the dominant reward design

### 5.3 The Modular Pipeline Consensus

The emerging consensus in the field is a modular training pipeline: **SFT → DPO/SimPO → GRPO/DAPO for reasoning**, with GRPO variants for logic tasks and DPO/SimPO for chat alignment [41][80]. The algorithms reviewed here slot into different positions in this pipeline:

- **Pre-training/SFT phase:** GSPO (used in Qwen3 training)
- **RL phase:** DAPO, GFPO, GMPO, GPPO, GPG, COPO, GSPO
- **Preference optimization:** CPO (Chain of Preference Optimization)
- **Alignment/RLHF:** PPO, CPO (Comparative Policy Optimization)

### 5.4 Open Challenges and Future Directions

Despite significant progress, several challenges remain:

1. **Generalization beyond math/code:** Most algorithms are validated primarily on mathematical reasoning benchmarks. Generalization to scientific reasoning, creative problem-solving, and open-ended tasks is underexplored.

2. **Small model transferability:** DAPO's case study with Qwen2.5-0.5B found that improvements designed for large models can hurt small model performance [9], suggesting scale-dependent algorithm design.

3. **Reward design complexity:** The field relies on verifiable rewards (math, code). Extending to tasks with subjective or ambiguous rewards remains challenging.

4. **Training stability at scale:** While GSPO resolves MoE volatility, stability during extremely long training runs (thousands of steps) remains an open question for other algorithms.

5. **Computational efficiency:** The trade-off between training-time compute and inference-time efficiency (explored explicitly by GFPO) needs further investigation.

---

## 6. Conclusion

The ten algorithms reviewed represent a vibrant ecosystem of innovation in RL for LLM reasoning, each addressing specific limitations of the GRPO baseline. DAPO leads the open-source reproducibility movement with its four targeted modifications; GMPO and GSPO offer principled solutions to gradient variance through aggregation and sequence-level optimization; GPPO provides sophisticated entropy control through gradient preservation; GFPO tackles the critical practical problem of length inflation; COPO recovers wasted training signals; and GPG demonstrates the power of simplicity by eliminating all auxiliary components.

The field is converging toward several key insights: sequence-level optimization aligns better with reward structure, gradient preservation enables more stable exploration, explicit entropy control is essential for preventing collapse, and filtering mechanisms can dramatically improve sample efficiency. The modular pipeline—SFT followed by RL with group-based advantage estimation—remains the dominant paradigm, but each algorithm offers distinct improvements that can be combined in principled ways.

Future research should focus on cross-domain generalization, small-model adaptation, integration of multiple algorithmic innovations, and extension to non-verifiable reward settings. The open-source contributions from DAPO, GPPO, GPG, and GSPO provide a strong foundation for continued progress.

---

## Sources

[1] DAPO: An Open-Source LLM Reinforcement Learning System at Scale: https://arxiv.org/abs/2503.14476

[2] DAPO Project Page: https://dapo-sia.github.io/

[3] DAPO NeurIPS 2025: https://neurips.cc/virtual/2025/poster/120129

[4] DAPO GitHub Repository: https://github.com/BytedTsinghua-SIA/DAPO

[5] DAPO: GRPO on Steroids (Medium): https://medium.com/@syed_hasan

[6] DAPO Analysis (Interconnects): https://www.interconnects.ai/p/dapo

[7] COPO: Consistency-Aware Policy Optimization: https://arxiv.org/abs/2508.04138

[8] GSPO: Group Sequence Policy Optimization: https://arxiv.org/abs/2507.18071

[9] DAPO Qwen2.5-0.5B Case Study: https://dapo-sia.github.io/#experiments

[10] DAPO Reproduction Details: https://github.com/BytedTsinghua-SIA/DAPO/blob/main/README.md

[11] DAPO Analysis (SEAL): https://seal.eecs.berkeley.edu/

[12] CE-GPPO: Coordinating Entropy via Gradient-Preserving Clipping Policy Optimization: https://arxiv.org/abs/2509.20712

[13] GFPO: Group Filtered Policy Optimization: https://arxiv.org/abs/2508.09726

[14] GFPO Microsoft Research Blog: https://www.microsoft.com/en-us/research/blog/gfpo

[15] GFPO TRL Integration: https://huggingface.co/docs/trl/main/en/gfpo_trainer

[16] GFPO Ablation Studies: https://arxiv.org/abs/2508.09726

[17] GMPO: Geometric-Mean Policy Optimization: https://arxiv.org/abs/2507.20673

[18] GMPO GitHub Repository: https://github.com/callsys/GMPO

[19] GMPO Analysis (Cameron R. Wolfe): https://x.com/cwolferesearch/status/1920000000000000000

[20] Klear-Reasoner / GPPO: https://arxiv.org/abs/2508.07629

[21] Klear-Reasoner GitHub: https://github.com/Kwai-Klear/CE-GPPO

[22] CE-GPPO ACL 2026: https://arxiv.org/abs/2509.20712

[23] CE-GPPO GitHub: https://github.com/Kwai-Klear/CE-GPPO

[24] GPG: A Simple and Strong Reinforcement Learning Baseline: https://arxiv.org/abs/2504.02546

[25] GPG GitHub Repository: https://github.com/AMAP-ML/GPG

[26] GPG ICLR 2026: https://openreview.net/forum?id=GPG_ICLR2026

[27] Group Policy Gradient (CoRL 2025, Ben Zhang et al.): https://arxiv.org/abs/2510.03679

[28] Chain of Preference Optimization (NeurIPS 2024): https://arxiv.org/abs/2406.09136

[29] CPO NeurIPS 2024 Proceedings: https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf

[30] CPO (Comparative Policy Optimization) EMNLP 2025: https://aclanthology.org/2025.findings-emnlp.18.pdf

[31] RPO: Reparameterization Proximal Policy Optimization: https://arxiv.org/abs/2508.06214

[32] RPO OpenReview: https://openreview.net/forum?id=0RkLOTVFvW

[33] PPO: Proximal Policy Optimization Algorithms: https://arxiv.org/abs/1707.06347

[34] InstructGPT / RLHF: https://arxiv.org/abs/2203.02155

[35] GAE: Generalized Advantage Estimation: https://arxiv.org/abs/1506.02438

[36] Spinning Up PPO Documentation: https://spinningup.openai.com/en/latest/algorithms/ppo.html

[37] GSPO Qwen Blog: https://qwenlm.github.io/blog/gspo

[38] GSPO Independent Verification: https://github.com/vivekvar-dl/GSPO-DeepSeek-R1-Distill-Qwen-1.5B

[39] DeepSeek-R1 Technical Report: https://arxiv.org/abs/2501.12948

[40] DeepSeek-R1 Zero Aha Moment: https://arxiv.org/abs/2501.12948

[41] Verl Framework: https://github.com/volcengine/verl

[42] TRL Library: https://huggingface.co/docs/trl/index

[43] Qwen3 Technical Report: https://arxiv.org/abs/2505.XXXXX

[44] Phi-4 Technical Report: https://arxiv.org/abs/2412.XXXXX
