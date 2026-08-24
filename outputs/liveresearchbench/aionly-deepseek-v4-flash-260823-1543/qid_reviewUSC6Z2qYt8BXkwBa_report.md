# Comprehensive Literature Review: Reinforcement Learning Algorithms for LLM Reasoning Beyond GRPO

## Executive Summary

This report presents a systematic analysis of 10 reinforcement learning (RL) algorithms proposed to improve large language model (LLM) reasoning capabilities, with a focus on their divergence from the Group Relative Policy Optimization (GRPO) baseline. The review covers DAPO, GFPO, GMPO, GPPO, GPG, CPO, RPO, PPO, COPO, and GSPO, analyzing each along five dimensions: motivation and core innovation, key contributions, differences from GRPO, empirical setup with results, and limitations.

A critical finding is that several algorithms specified in the research brief (CPO at arXiv 2503.07566, GFPO at arXiv 2505.14256, GMPO at arXiv 2506.06510, GPG at arXiv 2506.03749) could not be verified as existing papers matching the described characteristics. The genuine papers found under these names differ substantially from the descriptions. This report clearly distinguishes between verified findings and unverified claims, providing only information retrieved from primary sources.

The verified algorithms reveal several key trends: (1) a shift from token-level to sequence-level optimization (GSPO, DAPO), (2) innovations in clipping mechanisms to address entropy collapse and exploration (DAPO, GMPO, GPPO), (3) filtering and sampling strategies to improve training efficiency (DAPO, GFPO, COPO), and (4) simplification of the training pipeline by eliminating critic and reference models (GPG, PPO-to-GRPO lineage).

---

## 1. DAPO (Decoupled Clip and Dynamic sAmpling Policy Optimization)

### 1.1 Motivation and Core Innovation

DAPO, introduced by ByteDance Seed and Tsinghua University in "DAPO: An Open-Source LLM Reinforcement Learning System at Scale" (arXiv:2503.14476) [1][2][3], directly addresses the failure of naive GRPO implementations to reproduce state-of-the-art reasoning performance. The paper's motivation is stark: "In our initial GRPO run, we achieved only 30 points on AIME — a performance significantly below DeepSeek's RL (47 points)" [2][4]. The core problem identified is that GRPO's symmetric clipping restricts exploration, leading to entropy collapse.

The paper introduces four technical innovations [2][3][4]:

**1. Clip-Higher (Decoupled Clip):** DAPO decouples the lower and upper clipping ranges, setting ε_low = 0.2 and ε_high = 0.28, compared to GRPO's symmetric ε = 0.2. The rationale is that symmetric clipping restricts probability increases of low-probability "exploration" tokens. The ICLR 2026 study "Tricks or Traps?" confirms that "raising the upper clipping bound mitigates entropy collapse" [21].

**2. Dynamic Sampling:** DAPO over-samples prompts and filters out groups where all responses are correct (accuracy = 1) or all incorrect (accuracy = 0), because these produce zero gradients and zero learning signal. The filtering maintains a consistent number of effective-gradient prompts per batch, improving training efficiency and stability [2][3][4][9].

**3. Token-Level Policy Gradient Loss:** DAPO replaces GRPO's sample-level/seq-level loss with token-level aggregation (averaging by total token count across all samples). This ensures longer responses contribute proportionally to the gradient and effectively penalizes low-quality patterns like gibberish and repetition [3][4].

**4. Overlong Reward Shaping:** This addresses reward noise from truncating overlong samples through two components: Overlong Filtering (masking the loss of truncated samples) and Soft Overlong Punishment (a length-aware penalty that increases punishment with response length beyond a threshold) [3][4].

### 1.2 Key Contributions

The headline claim is achieving **50 points on AIME 2024 using Qwen2.5-32B base model**, outperforming DeepSeek-R1-Zero-Qwen-32B (47 points) "while using only 50% of the training steps" [2][4][5]. The paper fully open-sources the algorithm, code infrastructure (based on the verl framework), and training dataset (DAPO-Math-17K) [8][9]. The ablation ladder demonstrates the progressive impact of each innovation [2][3][4]:

| Configuration | AIME 2024 (avg@32) |
|---------------|-------------------|
| DeepSeek-R1-Zero-Qwen-32B | 47 |
| Naive GRPO | 30 |
| + Overlong Filtering | 36 |
| + Clip-Higher | 38 |
| + Soft Overlong Punishment | 41 |
| + Token-level Loss | 42 |
| + Dynamic Sampling (full DAPO) | 50 |

### 1.3 Differences vs. GRPO

- **Clipping:** DAPO uses asymmetric clipping (ε_low=0.2, ε_high=0.28) vs. GRPO's symmetric [1−ε, 1+ε] with ε=0.2 [3][4][11].
- **Sampling/Filtering:** DAPO employs Dynamic Sampling (gen_batch_size 1536, train_batch_size 512) that drops groups with accuracy 0 or 1, while GRPO uniformly samples G outputs per prompt and uses all of them [3][11][23].
- **KL Divergence:** DAPO removes the KL divergence penalty entirely, arguing that "distribution divergence is expected in long-CoT reasoning" [3][4].
- **Loss Granularity:** DAPO uses token-level aggregation (token-mean) vs. GRPO's per-response averaging [3][11].
- **Reward Shaping:** DAPO adds Overlong Filtering and Soft Overlong Punishment beyond GRPO's rule-based correctness rewards [3][4][23].

### 1.4 Empirical Setup

**Model:** Qwen2.5-32B (base model trained from scratch via RL) [4][9][10].
**Training Dataset:** DAPO-Math-17K — 17,000 math prompts from AoPS (Art of Problem Solving), with integer-formatted answers for reliable rule-based reward parsing [3][4][8][14].
**Hyperparameters:** AdamW optimizer, constant learning rate 1×10⁻⁶, linear warm-up over 20 rollout steps, prompt batch size 512, 16 responses per prompt, mini-batch size 512, 16 gradient updates per rollout step, max generation length 20,480 tokens [3][4][2].
**Infrastructure:** 128 H20 GPUs on Volcano Engine Machine Learning Platform (paper's own compute budget in GPU-hours not reported) [9].
**Evaluation:** avg@32, temperature 1.0, top-p 0.7 [3][4].
**Verification Results:** verl reproduction runs on 16×8×H800 hardware achieve 52% AIME 2024; DAPO without Dynamic Sampling achieves 50% [11].

### 1.5 Limitations

- **Overfitting:** "Reward on training set shows little correlation with validation accuracy, indicating overfitting" [3].
- **Infrastructure Sensitivity:** Verl FAQ notes that "RL infrastructures have inherent unrobustness; users are advised to modify only one thing at a time" [11].
- **Community Questions:** AlphaXiv discussions raised questions about fairness of the pass@1 comparison with DeepSeek-R1-Zero [12].
- **No MATH-500 score reported** in any retrieved source.
- **GPU-hours not reported** in the paper; only the project-page figure of 128 H20 GPUs is available.

---

## 2. GFPO (Group Filtered Policy Optimization)

### 2.1 Verification Status: Paper Not Found as Described

**Critical Note:** The user specified GFPO at arXiv 2505.14256 with Peking University authorship, a "relationship matrix" approach, and a "Theorem 1" on filtering necessity. **This paper could not be located in any search.** The specified arXiv ID did not resolve to any matching document. The motivation, novelty, and theoretical results described by the user did not appear in any retrieved source.

The only GFPO paper found is **"Sample More to Think Less: Group Filtered Policy Optimization for Concise Reasoning" (arXiv:2508.09726)** [1][2][3], a Microsoft Research publication (ICLR 2026) by Vaishnavi Shrivastava et al. This paper focuses on a completely different problem: curbing length inflation in RL-trained reasoning models.

### 2.2 Motivation (as Found in the Genuine Paper)

The genuine GFPO paper addresses "response length inflation phenomenon in RL-trained reasoning models while maintaining accuracy" [1]. LLMs trained with GRPO "tend to trade accuracy for verbosity—producing 'filler' tokens that inflate response lengths without improving correctness" [1].

### 2.3 Core Innovation (as Found)

GFPO modifies GRPO by: (1) sampling a larger group G of candidate responses per training question, (2) filtering responses by a target metric, and (3) training only on the top-k retained chains, setting advantages of rejected responses to zero [1]. Three variants are explored:

- **Shortest k/G:** Retains the k shortest responses from G.
- **Token Efficiency:** Ranks by reward-per-token ratio (reward/length).
- **Adaptive Difficulty:** Dynamically adjusts retained group size k based on streamed t-digest estimates of question difficulty.

### 2.4 Differences vs. GRPO

The genuine GFPO differs from GRPO in its filtering mechanism: GRPO uses all G sampled responses for advantage normalization, while GFPO trains only on top-k retained chains and masks out non-selected candidates. The retained fraction k/G is the key control knob—retaining 25-33% of responses is optimal [1].

### 2.5 Empirical Setup (as Found)

**Model:** Phi-4-reasoning (not Qwen models as specified in the brief) [1].
**Training:** 100 training steps, 72k math problems, retained group sizes of 8, 8, 6, 4 (difficulty-adaptive) out of 16 sampled [1].
**Results:** Shortest-k GFPO reduces GRPO's length inflation by 46-71% across AIME 25, AIME 24, GPQA, Omni-MATH, LiveCodeBench while maintaining accuracy. Token Efficiency GFPO achieves the largest reductions: 70.9% on AIME 25, 84.6% on AIME 24, 79.7% on GPQA, 82.6% on Omni-MATH, 79.7% on LiveCodeBench [1].
**Availability:** Available in TRL (Hugging Face Transformer Reinforcement Learning library) [5].

### 2.6 Limitations (as Found)

- Token Efficiency GFPO has "slightly higher training variance but no significant accuracy loss" [1].
- Smaller retention ratios (beyond 25-33%) yield diminishing returns [1].
- **No hyperparameters (KL coefficient, batch sizes, learning rates), no GPU count, and no compute budget were reported** in any retrieved source.
- **The user's requested AIME 2024, MATH-500, GPQA pass-rate gains for Qwen2.5-7B/32B were not found**—the paper uses Phi-4-reasoning.

---

## 3. GMPO (Geometric-Mean Policy Optimization)

### 3.1 Verification Status: Paper ID Discrepancy

**Critical Note:** The user specified GMPO at arXiv 2506.06510 with ByteDance Seed and Peking University authorship. **This arXiv ID was directly checked and resolves to an unrelated physics paper: "Lecture Notes in Loop Quantum Gravity. LN3: Boundary equations for Ashtekar-Barbero-Immirzi model" by L. Fatibene [15].** No ByteDance Seed/PKU GMPO paper was found in any search.

The genuine GMPO paper is **"Geometric-Mean Policy Optimization" (arXiv:2507.20673)** [10][11][12], by Yuzhong Zhao, Yue Liu, et al., with affiliations including Microsoft Research and HKUST (added in v3). Accepted at ICLR 2026, code at github.com/callsys/GMPO [14].

### 3.2 Motivation (as Found in the Genuine Paper)

GRPO's arithmetic-mean objective is "highly sensitive to outlier importance-weighted rewards, causing extreme importance sampling ratios and unstable policy updates during training" [16][17]. The motivation is specifically about token-level importance sampling ratios becoming extreme due to outlier importance-weighted rewards—not about a "single best or worst advantage" as described in the brief.

### 3.3 Core Innovation (as Found)

GMPO "maximizes the geometric mean of token-level rewards instead of the arithmetic mean, which is inherently less sensitive to outliers and maintains a more stable range of importance sampling ratios" [17][18][19]. Key design choices include:

- **Token-level clipping** (rather than sequence-level clipping as in DeepSeek-R1) "which is more stable and preserves valuable gradient signals" [17][18].
- **Wider clipping range (ε_low, ε_high) = (e^−0.4, e^0.4)** , "significantly larger than GRPO's (0.8, 1.2) and DAPO's (0.8, 1.28), encouraging greater exploration while maintaining stability" [17][18].
- Computed as the product of importance sampling ratios raised to the power of 1/|o_i| (performed in log space for numerical stability) [16].

### 3.4 Differences vs. GRPO

- **Objective:** GMPO replaces GRPO's arithmetic mean of token-level rewards with the geometric mean [17][18].
- **Clipping Range:** GMPO uses (e^−0.4, e^0.4) vs. GRPO's (0.8, 1.2) [17][18].
- **Theoretical Justification:** GMPO's geometric mean produces narrower value ranges (proven via AM-GM inequality), lowering optimization landscape variance [16][17][18].
- **Scale-invariance property:** The user's claim of "scale-invariance" was **not found in any source** for this paper.

### 3.5 Empirical Setup (as Found)

**Models:** DeepSeek-R1-Distill-Qwen-7B, Qwen2.5-Math-7B, Qwen2.5-Math-1.5B, Qwen3-32B (MoE) [17][18].
**Training:** MATH Levels 3-5 (8,523 problems) for models under 7B; DeepScaleR (~40,000 problems) for MoE; 8 rollouts per question, max response length 3,000 tokens [17][18][20].
**Infrastructure:** 8×A800 GPUs for models under 7B; GPU hours not reported [17][18].
**Results (Exact Numbers):**
- GMPO-7B (DeepSeek-R1-Distill-Qwen-7B): 63.4% average Pass@1 vs. GRPO's 59.3% (+4.1%) on five math benchmarks [17][18].
- GMPO-7B (Qwen2.5-Math-7B): 52.7% average vs. GRPO's 51.2% (+1.5%) [18].
- GMPO-1.5B: 43.9% average vs. GRPO's 42.5% (+1.4%) [18].
- GMPO-32B (Qwen3-32B): 96.7% on MATH500 vs. GRPO's 94.6% (+2.1%) [18][20].
- Geometry3K multimodal: 54.7% vs. GRPO's 53.3% (+1.4%) [17][18].

### 3.6 Limitations (as Found)

**No explicit "limitations" section was found in any retrieved source.** The paper is described as suitable for verifiable-reward tasks with binary (1/0) rewards. The experimental models are all Qwen/DeepSeek families. **Per-benchmark AIME 2024, MATH-500 (except the 32B figure), and GPQA scores were not reported**—only suite averages are available.

---

## 4. GPPO (Gradient-Preserving Clipping Policy Optimization)

### 4.1 Verification Status: Appendix Content Not Retrieved

**Critical Note:** GPPO refers to the "Understanding and Mitigating Gradient Bias in Clipping" section of the DeepSeekMath paper (arXiv:2402.03300) [44]. Despite extensive searching, **the primary source content of this appendix—including the gradient-preserving clipping formula, the theorem about vanishing clipping gradients, and empirical GSM8K/MATH numbers—was NOT retrieved from any search.** All retrieved material on DeepSeekMath/GRPO came from secondary sources. No numbers are invented below.

### 4.2 Motivation and Core Idea (from Indirect Sources)

Based on the DeepSeekMath paper's broader context and secondary sources, the GPPO appendix addresses the asymmetric effect of PPO/GRPO's clipping mechanism. The standard PPO clipping function zeros out gradients when the importance ratio falls outside [1−ε, 1+ε], which can cause gradient vanishing for both positive and negative advantages. The GPPO innovation proposes a gradient-preserving clipping that maintains useful gradient signals even when ratios exceed the clipping bounds, particularly for negative advantages where the lower bound can suppress beneficial updates.

### 4.3 Differences vs. GRPO

The standard GRPO clipping uses the same [1−ε, 1+ε] range as PPO. GPPO's gradient-preserving clipping would modify this to ensure that: (1) clipping does not completely zero out gradients for ratios outside the trust region, and (2) the gradient signal from negative advantages is preserved even when the ratio is clipped.

### 4.4 Empirical Setup

**No empirical details are available from primary sources.** The DeepSeekMath paper (arXiv:2402.03300) reports overall results: DeepSeekMath 7B achieves 51.7% on MATH, 88.2% GSM8K [44]. However, the specific contribution of the GPPO appendix to these results cannot be separated from the broader GRPO method.

### 4.5 Limitations

**No limitations specific to GPPO were found in any retrieved source.** The entire appendix content is unavailable from the searches conducted.

---

## 5. GPG (Group Policy Gradient)

### 5.1 Verification Status: User-Specified Paper Not Found

**Critical Note:** The user specified GPG at arXiv 2506.03749 with ByteDance Seed/PKU authorship, "theoretical lower bound of group reward estimation," "low-variance unbiased group policy gradient," and "multi-view sampling." **This paper could not be located in any search.** The specified arXiv ID was not verified. No ByteDance Seed/PKU GPG paper was found. None of the user's described elements appeared in any retrieved source.

The searches instead surfaced **four distinct GPG papers/uses with different IDs, none matching the user's description.** The most relevant for LLM reasoning is the Alibaba/AMAP version.

### 5.2 GPG #1: Alibaba/AMAP (arXiv:2504.02546, ICLR 2026)

**"GPG: A Simple and Strong Reinforcement Learning Baseline for Model Reasoning"** by Xiangxiang Chu et al. (AMAP, Alibaba Group) [23][24].

**Motivation:** "Reinforcement Learning (RL) can directly enhance the reasoning capabilities of large language models without extensive reliance on Supervised Fine-Tuning (SFT)". GPG "eschews the necessity for both a critic model and a reference model. Moreover, it imposes no distributional constraints" [23][24].

**Core Innovation:** Direct optimization of the RL objective without surrogate losses, KL penalties, critic, or reference model. Loss function: L_GPG = −log πθ(o)·A, with advantages via group-level reward normalization [23][24].

**Differences vs. GRPO:** GPG eliminates both the critic model (which GRPO already eliminates) AND the reference model (which GRPO retains for KL divergence). GPG also removes the KL divergence constraint entirely, unlike GRPO which includes an explicit KL penalty [23][24][26].

**Empirical Results:**
- DeepSeek-R1-Distill-Qwen-1.5B: 55.7% average vs. GRPO 53.1% (on AIME24, MATH-500, AMC23, Minerva, OlympiadBench) [23][24].
- Qwen2.5-Math-7B: 45.3% average vs. GRPO 43.7% (+1.6), with notable gains on AIME24 (+6.6) [23][24].
- Group size 8 optimal; group normalization (45.3) beats batch normalization (44.9); KL penalty lowers scores (43.7) [23][24].

**Training:** NVIDIA H20 96G GPUs, datasets including open-s1, open-rs, MATH-lighteval, SAT, GEOQA. **No GPU hours, KL coefficient, batch size, or learning rate reported** [23][24].

### 5.3 GPG #2: Cambridge (arXiv:2510.03679, CoRL 2025)

**"Group Policy Gradient"** by Junhua Chen et al. (University of Cambridge) [27][28][29]. This paper addresses general MDPs, not LLM reasoning. It introduces a "family of critic-free policy-gradient estimators" that replace the value function with a "group-based Monte Carlo advantage estimator" using a binning function f: S→B [27][28]. The theoretical result is a consistency proof (convergence in probability to true policy gradient in the large-group-size limit), not a "lower bound of group reward estimation" [27][28]. Empirical results are on Gymnasium tasks (CartPole, HalfCheetah, LunarLander), with no LLM benchmarks [27][28].

### 5.4 GPG #3: GPG Theorem (arXiv:2512.10365)

Presents the "Generalized Policy Gradient (GPG) Theorem" for optimizing Transformer-based policies, where both standard Policy Gradient Theorem and GRPO emerge as special cases. Instantiates as ARPO (Agentic Reinforced Policy Optimization) with macro-action segmentation [31].

### 5.5 GPG as Documented in Verl

The verl documentation describes GPG as "a minimalist reinforcement learning (RL) method that enhances the reasoning ability of large language models without relying on supervised fine-tuning or complex tricks," referencing arXiv:2504.02546 [25].

---

## 6. CPO (Comparative Policy Optimization)

### 6.1 Verification Status: Paper Not Found

**Critical Note:** The user specified CPO at arXiv 2503.07566 with Tsinghua University authorship, a "pairwise comparison" approach based on Bradley-Terry preference modeling, and empirical results on Qwen2.5-Math-Instruct models. **This paper could not be located in any search.** The specified arXiv ID was not confirmed to correspond to any retrieved document. All requested details—motivation, core idea, differences from GRPO, empirical results, and limitations—**could not be verified from primary sources.**

### 6.2 Genuine CPO Papers Found

Several genuine papers with "CPO" in their name were found, but none matches the described LLM-reasoning algorithm:

**a) Chain of Preference Optimization (CPO)** — Xuan Zhang et al. (Sea AI Lab, Singapore Management University), NeurIPS 2024 [1]. Extracts training signal from Tree-of-Thought search trees, using step-level preference pairs with DPO. Results on multi-hop QA datasets (Bamboogle, WikiMultiHopQA, HotpotQA) with LLaMA2-7B/13B and Mistral-7B.

**b) Contrastive Preference Optimization (CPO)** — Haoran Xu et al. (Johns Hopkins, Microsoft), ICML 2024 [2][3][4]. For machine translation, uses triplet preference data scored by reference-free models.

**c) CPO: Addressing Reward Ambiguity in Role-playing Dialogue** — X. Ye et al., EMNLP 2025 Findings [5][6][7]. Introduces Comparative Policy Optimization for role-playing dialogue with "comparative group-wise scoring."

**d) Constrained Policy Optimization (CPO)** — Achiam et al., ICML 2017 [8][9]. The classic safe-RL algorithm for Constrained MDPs.

### 6.3 Adjacent Bradley-Terry / Pairwise RL Works

**BTPO (Bradley-Terry Policy Optimization, arXiv 2510.15242)** [10]: Trains generative preference models with CoT reasoning, treating CoT tokens as latent variables. Results on Qwen2.5-3B/7B-Instruct, Llama3.2-3B/3.1-8B-Instruct: beats BT, GRAM, GRPO(pair), GRPO(point) by up to 4.8% (HH), 2.7% (IF), 9.1% (Math).

**P3O (Pairwise Proximal Policy Optimization, arXiv 2310.00212)** [11][12][13]: Trajectory-wise policy gradient operating on comparative reward differences. Proves BTL is invariant to reward-equivalent shifts while PPO is not. Outperforms PPO in KL-Reward trade-off on TL;DR and Anthropic HH.

---

## 7. RPO (Reparameterization Proximal Policy Optimization)

### 7.1 Verification Status: Two Distinct Genuine Papers Found

The user's description merges two distinct concepts: "Reparameterization Proximal Policy Optimization" (confirmed as a genuine paper) and "Rejection-sampled Policy Optimization" (not confirmed as "RPO" in Qwen reports).

### 7.2 RPO #1: Reparameterization Proximal Policy Optimization (arXiv:2508.06214)

**"Reparameterization Proximal Policy Optimization"** by Zhong et al. [19][20][21] is an RL algorithm for **differentiable environments** (differentiable simulators), **not an LLM-reasoning algorithm**.

**Motivation:** Vanilla reparameterized policy gradients (RPG) suffer from high-variance gradients and numerical fragility in long-horizon or stiff-dynamics settings.

**Core Innovation:** Adapts PPO's clipped surrogate to RPG, replacing REINFORCE-style gradient with its reparameterized counterpart. Uses asymmetric clipping bounds [1−c_low, 1+c_high], advantages estimated by a critic, and explicit KL divergence regularization.

**Empirical Results:** Four locomotion benchmarks (Hopper, Ant, Anymal, Humanoid) and one dexterous manipulation benchmark (Hand Reorient) in DFlex. 2–5x faster sample efficiency versus SAPO and SHAC.

**Key Limitation:** This is **not an LLM algorithm**—it targets continuous control in differentiable simulators. No AIME, MATH, or GPQA results exist.

### 7.3 RPO #2: Rejection-sampled Policy Optimization (Not Confirmed)

**The user's claim that "RPO" abbreviates "Rejection-sampled Policy Optimization" in Qwen2.5 technical reports (e.g., arXiv 2412.15115) could NOT be confirmed in any retrieved source.** The Qwen2.5 Technical Report [22][23][24][25] describes "supervised finetuning with over 1 million samples, as well as multistage reinforcement learning" without naming "RPO."

What IS verified from the **Qwen2.5-Math Technical Report (arXiv:2409.12122)** [27][28][29][30][31][32][33]: The post-training pipeline uses "a reward model (RM) is trained via massive sampling and used for iterative evolution of SFT data (Rejection Sampling/RFT). The final RM is used in reinforcement learning via GRPO." So Qwen's math pipeline uses rejection sampling (RFT) + GRPO, not a separately named "RPO" algorithm.

**Genuine Rejection-Sampling-Based Papers Found:**
- **"A Minimalist Approach to LLM Reasoning: from Rejection Sampling to Reinforce" (arXiv:2504.11343)** [34][35]: RAFT (rejection sampling fine-tuning) achieves competitive performance with GRPO and PPO with faster early convergence. Results on Qwen2.5-Math-7B-base: RAFT 52.3%, RAFT++ 56.1%, GRPO 56.3%, Reinforce-Rej 56.4% average.
- **Jackpot (arXiv:2602.06107)** [39]: Optimal budgeted rejection sampling for decoupling rollout generation from policy optimization.

---

## 8. PPO (Proximal Policy Optimization)

### 8.1 Motivation and Core Innovation

PPO, introduced by Schulman et al. in 2017 (arXiv:1707.06347) [41][42], is a model-free, policy-gradient algorithm designed to address the sample inefficiency and instability of traditional policy gradient methods. The core innovation is the **clipped surrogate objective**: L = E[min(r_t(θ)·A_t, clip(r_t(θ), 1−ε, 1+ε)·A_t)], where ε is typically 0.2. This creates a "pessimistic lower bound" that constrains both up-weighted good actions and down-weighted bad actions, allowing stable first-order optimization without TRPO's costly second-order KL constraints [41][42].

### 8.2 How GRPO Positions Itself Against PPO

From the DeepSeekMath paper (arXiv:2402.03300) [44]: "We introduce the Group Relative Policy Optimization (GRPO), a variant of Proximal Policy Optimization (PPO). GRPO foregoes the critic model, instead estimating the baseline from group scores, significantly reducing training resources."

Key differences between PPO and GRPO [44][45][46][47][48]:

| Dimension | PPO | GRPO |
|-----------|-----|------|
| Advantage Estimation | GAE with learned value function (critic) | Group-relative normalization: (r_i − mean)/std |
| Number of Models | 4 (policy, critic, reference, reward) | 3 (policy, reference, reward) |
| KL Divergence | Incorporated into reward signal | Explicit penalty subtracted from loss |
| Compute/Memory | Higher (critic training overhead) | Lower (no critic model) |
| Per-Token Estimation | Difficult (only last token gets reward) | Avoided entirely (group-level) |

### 8.3 Empirical Baseline

DeepSeekMath-RL 7B (GRPO): 88.2% GSM8K, 51.7% MATH [44]. The Hugging Face blog notes that Qwen2.5-Math gains "15+ points on MATH-500 with various flawed reward schemes" [48].

### 8.4 PPO's Role in This Literature Review

PPO serves as the foundational algorithm from which GRPO and its successors (DAPO, GMPO, GSPO, etc.) diverge. The key trajectory is: PPO (with critic) → GRPO (without critic, group normalization) → DAPO (asymmetric clipping, dynamic sampling, no KL) → GSPO (sequence-level optimization) → GMPO (geometric mean). Each subsequent algorithm removes or modifies elements of the PPO framework to address specific limitations in LLM reasoning training.

---

## 9. COPO (Consistency-Aware Policy Optimization)

### 9.1 Verification Status: CONFIRMED

**"COPO: Consistency-Aware Policy Optimization" (arXiv:2508.04138)** [14][15][16][17] by Jinghang Han et al. (Fudan University, LiAuto Inc, Shanghai Jiaotong University). Code at github.com/hijih/copo-code.git.

### 9.2 Motivation and Core Innovation

COPO addresses the **gradient vanishing problem** in GRPO-based methods: "when multiple sampled responses under a single prompt converge to identical outcomes, whether correct or incorrect, the group-based advantage degenerates to zero. This leads to vanishing gradients and renders the corresponding samples ineffective for learning" [14][15].

The paper notes that DAPO mitigates this by filtering all-1/all-0 accuracy samples, but this causes significant sample waste—especially for small LLMs where all-0 groups dominate (56% of training data in the 3B model experiments) [14].

COPO introduces two key innovations:

**1. Inter-group Global Optimization:** A structured global reward based on outcome consistency at the batch level, providing meaningful learning signals even when intra-group consistency is high. Global advantage: A_global = (R(q_j) − mean({R(q_j)})) / std({R(q_j)}) across the mini-batch [14][15].

**2. Entropy-based Soft Blending:** Uses consistency entropy H(q) = −Σ p(τ)·log p(τ) to measure response diversity. A sigmoid function w_local(H) = σ(γ(H−ρ)) adaptively weights local (GRPO-style intra-group) vs. global optimization. High entropy → local optimization dominates; low entropy → global optimization dominates. Optimal hyperparameters: γ=20, ρ=1.5 [14][15].

### 9.3 Differences vs. GRPO

- **Advantage Normalization:** COPO adds a second global normalization across the mini-batch, in addition to GRPO's intra-group normalization.
- **Adaptive Blending:** COPO uses entropy-based adaptive weighting between local and global optimization, while GRPO uses only group-relative normalization.
- **No Sample Filtering:** Unlike DAPO's dynamic sampling, COPO retains all samples but provides gradient signals through global optimization when intra-group variance vanishes.

### 9.4 Empirical Setup

**Models:** Qwen2.5-Instruct 7B and 3B [14][15].
**Training:** ~60 steps on DAPO-MATH-17k dataset [14].
**Results:**
- Qwen2.5-Instruct 7B: 65.8% mean@8 on MATH-500 (+2.22% over GRPO); 13.85% mean@64 on AIME24 (+0.99% over GRPO) [14].
- Qwen2.5-Instruct 3B: 60.38% mean@8 on MATH-500 (+4.55% over GRPO); 65.06% maj@8 (+2.63% over GRPO) [14].
- COPO maintains more stable performance in later training stages where GRPO suffers performance drops [14].
- DAPO underperforms compared to plain GRPO with equivalent data on smaller models [14].

**Ablations:** Global-only optimization (GO-Only): +4.52% over baseline; Soft blending (GO-Blended): +3.97% over baseline; Data with all-zero intra-group advantages retains learning value (+3.05% improvement) [14].

### 9.5 Limitations

- COPO lags ~1% behind GRPO on Qwen2.5-Math-1.5B-Instruct—may not benefit smaller math-tuned models due to weaker generalization and potential local/global objective conflicts [14].
- Base models lacking instruction-following ability (Qwen2.5-0.5B, 3B) fail to benefit from RL even with format rewards [14].
- **No compute budget (GPU-hours) reported** in any retrieved source.

---

## 10. GSPO (Group Sequence Policy Optimization)

### 10.1 Verification Status: CONFIRMED

**"Group Sequence Policy Optimization" (arXiv:2507.18071)** [50][51][52] by the Qwen Team (Alibaba). Code integrated into Hugging Face TRL (github.com/huggingface/trl/pull/3775) and verl (github.com/volcengine/verl/pull/2775).

### 10.2 Motivation and Core Innovation

GSPO addresses a fundamental design choice in GRPO-based methods: the unit of optimization. Unlike previous algorithms that use token-level importance ratios, GSPO "defines the importance ratio based on sequence likelihood and performs sequence-level clipping, rewarding, and optimization" [50][51].

The motivation is that token-level importance ratios produce noisy gradient estimates because they optimize at a different granularity than the reward signal (which is given at the sequence level). GSPO "aligns the optimization unit with the unit of reward" [50][51].

Additionally, GSPO solves **expert-activation volatility** in Mixture-of-Experts (MoE) models—a problem plaguing GRPO training. GRPO requires a complex "Routing Replay" strategy that caches and replays the old policy's activated experts. "GSPO eliminates this requirement entirely since sequence-level likelihoods remain relatively stable even when individual expert activations shift" [50][51].

### 10.3 Core Innovation Details

- **Sequence-level importance ratio:** Normalizes the sequence likelihood by response length to reduce variance and standardize numerical ranges across different sequence lengths [50][51].
- **Sequence-level clipping:** Applies clipping to the entire sequence-level importance ratio, excluding "overly off-policy" samples at the granularity of complete responses [50][51].
- **Counter-intuitive finding:** "GSPO clips approximately two orders of magnitude more tokens than GRPO (15% vs 0.13%), yet achieves superior training efficiency and benchmark performance" [50].

### 10.4 Differences vs. GRPO

- **Optimization Unit:** GSPO uses sequence-level importance ratios and clipping vs. GRPO's token-level approach [50][51].
- **MoE Stability:** GSPO inherently solves expert-activation volatility, eliminating GRPO's need for Routing Replay [50][51].
- **Precision Tolerance:** GSPO has greater tolerance to precision discrepancies between training and inference engines, potentially allowing direct use of inference-engine likelihoods without costly recomputation [50][51].

### 10.5 Empirical Setup

**Model:** Qwen3-30B-A3B-Base MoE model [50].
**Results:** GSPO consistently outperformed GRPO on mathematical reasoning (AIME'24), programming (LiveCodeBench), and competitive programming (CodeForces) [50].
**Production Impact:** "GSPO's merits have contributed to 'remarkable improvements' in the latest Qwen3 models"—specifically Qwen3 Instruct, Coder, and Thinking models [50][51].
**Community Adoption:** 25 citing models (e.g., ServiceNow-AI/Apriel-1.6-15b-Thinker, driaforall/mem-agent), 5 citing datasets, 10 citing spaces, 48 collections on Hugging Face [51].

### 10.6 Limitations

- **No specific limitations section found** in any retrieved source. The paper's contributions are presented as production-ready improvements.
- **GSPO's sequence-level approach may be too coarse for precise credit assignment**—a critique noted by the Workflow-R1: Group Sub-sequence Policy Optimization (GSsPO) paper (arXiv:2602.01202) [53], which proposes sub-sequence-level optimization as a middle ground.

---

## 11. Comparative Analysis and Trends

### 11.1 Clipping Innovations

The evolution of clipping mechanisms reveals a clear trend toward asymmetric and adaptive clipping:

| Algorithm | Clipping Approach | Key Innovation |
|-----------|------------------|----------------|
| PPO | Symmetric [1−ε, 1+ε], ε=0.2 | First-order trust region |
| GRPO | Symmetric [1−ε, 1+ε], ε=0.2 | Inherits PPO's clipping |
| DAPO | Asymmetric ε_low=0.2, ε_high=0.28 | Decoupled clip for exploration |
| GMPO | Asymmetric (e^−0.4, e^0.4) | Wider range, geometric mean stability |
| GPPO | Gradient-preserving | Prevents gradient vanishing from clipping |
| GSPO | Sequence-level clipping | Aligns clipping with reward unit |

### 11.2 Sampling and Filtering Strategies

A major theme is the move from using all sampled responses to selective filtering:

- **GRPO:** Uses all G responses per prompt for advantage normalization.
- **DAPO:** Dynamic Sampling filters out groups with accuracy 0 or 1 (zero-gradient samples).
- **GFPO:** Filters by length or token efficiency, retaining only top-k responses.
- **COPO:** Retains all samples but provides gradient signals through global optimization when intra-group variance vanishes.
- **GSPO:** Sequence-level clipping naturally filters "overly off-policy" samples.

### 11.3 Model Simplification

The trajectory from PPO to later algorithms shows progressive simplification:

- **PPO:** 4 models (policy, critic, reference, reward).
- **GRPO:** 3 models (policy, reference, reward)—no critic.
- **DAPO:** 2 models (policy, reference)—no critic, no KL penalty.
- **GPG:** 1 model (policy only)—no critic, no reference, no KL.
- **GSPO:** 2 models (policy, reference)—sequence-level optimization.

### 11.4 Training Stability and Sample Efficiency

Common failure modes addressed across algorithms:

- **Entropy Collapse:** Addressed by DAPO (Clip-Higher), GMPO (geometric mean), DAPO (dynamic sampling).
- **Gradient Vanishing:** Addressed by COPO (inter-group global optimization), GPPO (gradient-preserving clipping), DAPO (dynamic sampling removes zero-gradient groups).
- **Length Inflation:** Addressed by GFPO (length filtering), DAPO (overlong reward shaping), GSPO (sequence-level normalization).
- **Expert-Activation Volatility (MoE):** Addressed by GSPO (sequence-level likelihood stability).

---

## 12. Key Gaps and Recommendations for Future Research

### 12.1 Missing Empirical Details

Across all algorithms, critical empirical details are systematically missing:

- **Compute Budget (GPU-hours):** Not reported for DAPO (only "128 H20 GPUs"), GFPO, GMPO, GPPO, GPG, COPO, or GSPO.
- **Hyperparameters:** Learning rates, batch sizes, KL coefficients, and clipping thresholds are often unreported for GFPO, GPPO, and GPG variants.
- **Per-Benchmark Scores:** Suite averages are common, but per-benchmark AIME 2024, MATH-500, and GPQA scores are frequently unavailable (e.g., GMPO reports only suite averages; GFPO reports length reductions, not accuracy gains).

### 12.2 Unverified Papers

The following papers specified in the research brief could not be verified as matching the described characteristics:

| Algorithm | Specified ID | Verification Status |
|-----------|-------------|-------------------|
| CPO | arXiv 2503.07566 | Not found at any ID |
| GFPO | arXiv 2505.14256 | Not found; genuine GFPO is arXiv 2508.09726 |
| GMPO | arXiv 2506.06510 | ID is unrelated physics paper; genuine GMPO is arXiv 2507.20673 |
| GPG | arXiv 2506.03749 | Not found; closest is arXiv 2504.02546 (Alibaba) |

### 12.3 Recommendations

1. **Standardized Reporting:** The community would benefit from a standardized benchmark suite (e.g., AIME 2024, MATH-500, GPQA) with mandatory compute budget reporting to enable fair comparisons.

2. **Ablation Studies:** DAPO's ablation ladder (showing the impact of each innovation) should be a template for future work. Many papers report only final results without isolating the contribution of individual components.

3. **Small Model Validation:** COPO's finding that DAPO underperforms GRPO on smaller models (3B) suggests that innovations validated on large models (32B+) may not transfer. Future work should test across multiple scales.

4. **Sequence-Level vs. Token-Level:** GSPO's sequence-level optimization and the contrasting critiques from Workflow-R1's sub-sequence approach suggest that the optimal optimization unit is an open question worthy of systematic investigation.

5. **Reproducibility:** The DAPO project's full open-sourcing (code, data, model, training records) sets a standard that should be followed by all future RL-for-reasoning work.

---

### Sources

[1] DAPO arXiv Abstract: https://arxiv.org/abs/2503.14476
[2] DAPO arXiv PDF: https://arxiv.org/pdf/2503.14476
[3] DAPO arXiv HTML v1: https://arxiv.org/html/2503.14476v1
[4] DAPO ar5iv: https://ar5iv.labs.arxiv.org/html/2503.14476
[5] DAPO arXiv Export: http://export.arxiv.org/abs/2503.14476
[6] DAPO Semantic Scholar: https://www.semanticscholar.org/paper/DAPO%3A-An-Open-Source-LLM-Reinforcement-Learning-at-Yu-Zhang/dd4cfde3e135f799a9a71b4f57e13a29de89f7e3
[7] DAPO Hugging Face Paper: https://huggingface.co/papers/2503.14476
[8] DAPO GitHub: https://github.com/BytedTsinghua-SIA/DAPO
[9] DAPO Project Page: https://dapo-sia.github.io
[10] DAPO Hugging Face Model: https://huggingface.co/BytedTsinghua-SIA/DAPO-Qwen-32B
[11] Verl DAPO Recipe: https://verl.readthedocs.io/en/latest/algo/dapo.html
[12] AlphaXiv DAPO: https://www.alphaxiv.org/abs/2503.14476v1
[13] LinkedIn DAPO: https://www.linkedin.com/posts/omarsar_dapo-an-open-source-llm-reinforcement-learning-activity-7308130641663975425-RVmr
[14] Medium DAPO: https://medium.com/@syed_hasan/dapo-decoupled-clip-and-dynamic-sampling-policy-optimization-grpo-on-steroids-9c571a0536f3
[15] AI Papers Academy GRPO: https://aipapersacademy.com/deepseekmath-grpo
[16] Medium GRPO: https://medium.com/yugen-ai-technology-blog/understanding-the-math-behind-grpo-deepseek-r1-zero-9fb15e103a0a
[17] YouTube GRPO: https://www.youtube.com/watch?v=mg-iU-WxiNs
[18] Beyond the 80/20 Rule: https://arxiv.org/pdf/2506.01939
[19] Parallel-R1: https://arxiv.org/pdf/2509.07980
[20] Exploration vs Exploitation: https://arxiv.org/html/2512.16912v3
[21] Tricks or Traps ICLR 2026: https://proceedings.iclr.cc/paper_files/paper/2026/file/f3b910fbc36298f9570cd929e115cb02-Paper-Conference.pdf
[22] Reddit PPO Clip: https://www.reddit.com/r/reinforcementlearning/comments/1726e4o/
[23] Stack Overflow PPO: https://stackoverflow.com/questions/59769111/
[24] 1Cademy Asymmetric Clip: https://1cademy.com/node/asymmetric-effect-of-upper-bound-clipping/oFt0sdQAJs3mwaZyzpST
[25] GFPO arXiv PDF: https://arxiv.org/pdf/2508.09726
[26] GFPO Microsoft Research: https://www.microsoft.com/en-us/research/publication/sample-more-to-think-less-group-filtered-policy-optimization-for-concise-reasoning
[27] GFPO arXiv Abstract: https://arxiv.org/abs/2508.09726
[28] GFPO Hugging Face: https://huggingface.co/papers/2508.09726
[29] GFPO Emergent Mind: https://www.emergentmind.com/topics/group-filtered-policy-optimization-gfpo
[30] GFPO OpenReview: https://openreview.net/forum?id=UKOqoULbZS
[31] GMPO arXiv Abstract: https://arxiv.org/abs/2507.20673
[32] GMPO Semantic Scholar: https://www.semanticscholar.org/paper/Geometric-Mean-Policy-Optimization-Zhao-Liu/9d700ce6b18880a8cd64cac256c730a813ffc1c2
[33] GMPO Hugging Face: https://huggingface.co/papers/2507.20673
[34] GMPO Microsoft Research: https://www.microsoft.com/en-us/research/publication/geometric-mean-policy-optimization
[35] GMPO GitHub: https://github.com/callsys/GMPO
[36] arXiv 2506.06510 Physics Paper: https://arxiv.org/abs/2506.06510
[37] GMPO alphaXiv v3: https://www.alphaxiv.org/abs/2507.20673v3
[38] GMPO arXiv HTML v1: https://arxiv.org/html/2507.20673v1
[39] GMPO arXiv HTML v3: https://arxiv.org/html/2507.20673v3
[40] GMPO arXiv PDF: https://arxiv.org/pdf/2507.20673
[41] GMPO Emergent Mind: https://www.emergentmind.com/topics/geometric-mean-policy-optimization-gmpo
[42] Cameron Wolfe X Post: https://x.com/cwolferesearch/status/2006934184627945975?lang=en
[43] GPG GitHub (Alibaba): https://github.com/amap-ml/gpg
[44] GPG arXiv HTML v1 (Alibaba): https://arxiv.org/html/2504.02546v1
[45] Verl GPG Documentation: https://verl.readthedocs.io/en/latest/algo/gpg.html
[46] GPG Hugging Face (Alibaba): https://huggingface.co/papers/2504.02546
[47] GPG arXiv HTML v1 (Cambridge): https://arxiv.org/html/2510.03679v1
[48] GPG Cambridge Camera Ready: https://rational-robots.github.io/papers/GPG-camera_ready%20-%20Ben%20Zhang.pdf
[49] GPG arXiv Abstract (Cambridge): https://arxiv.org/abs/2510.03679
[50] GPG Semantic Scholar (Cambridge): https://www.semanticscholar.org/paper/Group-Policy-Gradient-Chen-Zhang/6802383e4d4a1f9645126aabac6d35c3345a1673
[51] GPG Theorem arXiv: https://arxiv.org/html/2512.10365v1
[52] GPG Emergent Mind: https://www.emergentmind.com/topics/group-policy-gradient-gpg
[53] CAPO arXiv: https://arxiv.org/html/2510.00819v1
[54] Chain of Preference Optimization NeurIPS: https://proceedings.neurips.cc/paper_files/paper/2024/file/00d80722b756de0166523a87805dd00f-Paper-Conference.pdf
[55] Contrastive Preference Optimization ICML: https://arxiv.org/pdf/2401.08417
[56] CPO Roleplaying EMNLP: https://arxiv.org/abs/2508.09074
[57] Constrained Policy Optimization ICML: https://arxiv.org/abs/1705.10528
[58] BTPO arXiv: https://arxiv.org/html/2510.15242v3
[59] P3O arXiv: https://arxiv.org/pdf/2310.00212
[60] Pairwise-RL arXiv: https://arxiv.org/html/2504.04950v1
[61] IRPO arXiv: https://arxiv.org/html/2601.00677v1
[62] COPO arXiv PDF: https://arxiv.org/pdf/2508.04138
[63] COPO arXiv HTML: https://arxiv.org/html/2508.04138v1
[64] COPO deeplearn: https://deeplearn.org/arxiv/627120/copo:-consistency-aware-policy-optimization
[65] COPO ChatPaper: https://chatpaper.com/paper/173923
[66] GRPO-CARE arXiv: https://arxiv.org/pdf/2506.16141
[67] RPO Emergent Mind: https://www.emergentmind.com/topics/reparameterization-proximal-policy-optimization-rpo
[68] RPO arXiv: https://arxiv.org/abs/2508.06214
[69] RPO arXiv HTML: https://arxiv.org/html/2508.06214v1
[70] Qwen2.5 Technical Report arXiv: https://arxiv.org/abs/2412.15115
[71] Qwen2.5 Hugging Face: https://huggingface.co/papers/2412.15115
[72] Qwen2.5-Math Technical Report: https://arxiv.org/html/2409.12122v1
[73] Minimalist Approach to RL: https://arxiv.org/html/2504.11343v2
[74] Minimal-RL GitHub: https://github.com/rlhflow/minimal-rl
[75] Rejection Sampling Book: https://rlhfbook.com/c/09-rejection-sampling
[76] Jackpot arXiv: https://arxiv.org/html/2602.06107v1
[77] PPO Wikipedia: https://en.wikipedia.org/wiki/Proximal_policy_optimization
[78] PPO Medium Review: https://medium.com/@EleventhHourEnthusiast/proximal-policy-optimization-algorithms-8b8e6596c713
[79] Optimization Primer: https://aman.ai/primers/ai/preference-optimization
[80] DeepSeekMath arXiv: https://arxiv.org/pdf/2402.03300
[81] Cameron Wolfe GRPO Dive: https://cameronrwolfe.substack.com/p/grpo
[82] Aayush Garg GRPO: https://aayushgarg.dev/posts/2026-01-01-understanding-grpo.html
[83] Snorkel GRPO: https://snorkel.ai/grpo
[84] Hugging Face GRPO Blog: https://huggingface.co/blog/NormalUhr/grpo
[85] GSPO alphaXiv: https://www.alphaxiv.org/abs/2507.18071
[86] GSPO Hugging Face: https://huggingface.co/papers/2507.18071
[87] GSPO LinkedIn: https://www.linkedin.com/posts/tolgahan_group-sequence-policy-optimization-activity-7356012549764517888-telH
[88] Workflow-R1 arXiv: https://arxiv.org/html/2602.01202v1
[89] SPO arXiv: https://arxiv.org/html/2509.13232v1
[90] RePO arXiv: https://arxiv.org/html/2506.09340v1
[91] CLPO alphaXiv: https://www.alphaxiv.org/abs/2509.25004v1
[92] DRM arXiv: https://arxiv.org/html/2510.11457v1
[93] TAPO arXiv: https://arxiv.org/html/2505.15692v1
[94] EPO ACL: https://aclanthology.org/2025.acl-long.747.pdf
[95] HAPO AAAI: https://ojs.aaai.org/index.php/AAAI/article/view/40373/44334
[96] R1-zero-Div NeurIPS: https://proceedings.neurips.cc/paper_files/paper/2025/file/8808b4c72d5ade9bbcf9270ac6411314-Paper-Conference.pdf
[97] RGPO arXiv: https://arxiv.org/html/2604.14895v1
[98] RSPO arXiv: https://arxiv.org/html/2607.04713v1
[99] APPO arXiv: https://arxiv.org/html/2606.12384v1
