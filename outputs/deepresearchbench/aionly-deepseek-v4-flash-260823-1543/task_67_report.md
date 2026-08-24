# Reinforcement Learning Exploration for Sparse Rewards and Constraints: A Comprehensive Review with Implications for Trajectory Planning

## 1. Introduction

Reinforcement learning (RL) has achieved remarkable successes in domains ranging from game playing to robotic control, yet two fundamental challenges persist: exploring efficiently under sparse reward signals, and doing so while respecting safety, resource, or environmental constraints. These challenges are particularly acute in trajectory planning problems—such as robotic manipulation, autonomous driving, and legged locomotion—where the cost of failure is high and reward signals are often binary or delayed.

This report synthesizes the latest research progress up to August 2026 across three interconnected areas: (1) methods for efficient exploration under sparse rewards, (2) methods for constrained exploration, and (3) the implications of these advances for trajectory planning. The review covers key algorithmic innovations, theoretical contributions, and practical applications, drawing connections between RL exploration strategies and their applicability to motion planning domains.

---

## 2. Exploration Under Sparse Rewards

### 2.1 The Sparse Reward Problem

In sparse reward environments, the agent receives a non-zero reward only upon achieving a specific goal state, with all other transitions yielding zero reward. Consider a peg-in-hole insertion task on a 7-DoF arm: the reward is 1 if the peg is fully seated, 0 otherwise, and the action space is continuous joint velocities. A uniform-random policy has a success probability on the order of 1e-4 to 1e-5 per episode, which at 200 episodes per hour translates to 50–500 hours before the first random success [1]. This highlights why naive exploration is fundamentally insufficient for real-world applications.

### 2.2 Intrinsic Motivation and Curiosity-Driven Methods

#### 2.2.1 Intrinsic Curiosity Module (ICM)

The Intrinsic Curiosity Module (ICM), introduced by Pathak et al. (ICML 2017), uses a three-component architecture: an encoder that maps states to features, an inverse model that predicts actions from consecutive state features, and a forward model that predicts next-state features from current features and actions [2]. The prediction error of the forward model serves as an intrinsic reward signal. Crucially, the inverse model filters out uncontrollable visual distractors, enabling the agent to focus on aspects of the environment it can influence. However, ICM does not escape the "noisy TV" problem—stochastic dynamics can keep forward-model error high indefinitely, causing the agent to become stuck.

#### 2.2.2 Random Network Distillation (RND)

Random Network Distillation (RND), introduced by Burda et al. (ICLR 2019), addresses the stochasticity problem by decoupling the intrinsic reward computation from environment dynamics entirely [3]. RND uses two networks: a frozen, randomly initialized "target" network and a trainable "predictor" network. The intrinsic reward is the mean squared error between the predictor and target outputs for a given state. As the predictor becomes better at predicting the target's output for frequently visited states, the error decreases, naturally directing exploration toward novel states.

RND was the first method to achieve better-than-average human performance on Montezuma's Revenge without demonstrations or access to the underlying game state [3]. In practice, RND has become the default curiosity method for robotics applications because it is computationally efficient and avoids the stochastic dynamics trap that plagues ICM [1]. A 2025 experiment at MIT showed that a TurtleBot4 equipped with an RND-augmented Nav2 stack mapped a 500m² office building 40% faster than a frontier-based exploration approach [1].

#### 2.2.3 Distributional RND (DRND)

"Exploration and Anti-Exploration with Distributional Random Network Distillation" (ICML 2024) identified a "bonus inconsistency" issue within RND [4]. DRND addresses this by distilling a distribution of random networks rather than a single one, implicitly incorporating pseudo-counts to improve the precision of bonus allocation. The method excels in challenging online exploration scenarios and serves as an effective anti-exploration mechanism in offline tasks, all without introducing significant computational overhead.

#### 2.2.4 BYOL-Explore

BYOL-Explore (Bootstrap Your Own Latent), introduced by Google DeepMind (2022), represents a significant advance in curiosity-driven exploration [5]. The core innovation is learning a world representation by predicting its own future representation, then using the prediction error at the representation level as an intrinsic reward. The agent simultaneously learns world representation, dynamics, and an exploration policy by optimizing prediction error.

On the DM-HARD-8 suite (challenging 3D, visually complex tasks), BYOL-Explore outperformed RND and ICM in mean capped human-normalised score, achieving this performance using only a single network across all tasks—whereas prior work required demonstrations for meaningful progress [5]. BYOL-Explore also achieves super-human performance in the ten hardest exploration Atari games while having a simpler design than Agent57 and Go-Explore.

However, BYOL-Explore relies on deterministic dynamics. A follow-up method, BLaDE (Bootstrap Latent Diffusion Explorer), makes it robust to stochastic dynamics by using diffusion models for probabilistic world modeling.

#### 2.2.5 Empirical Study of Diversity Levels in Intrinsic Rewards

A systematic study by Kayal, Pignatelli, and Toni (Neural Computing and Applications, 2025) categorizes intrinsic rewards into four diversity levels: State level (count-based), State + Dynamics level (ICM), Policy level (Maximum Entropy), and Skill level (DIAYN) [6]. Key findings include:

- State-level count-based methods lead to the best exploration in low-dimensional observation spaces but degrade significantly with RGB observations due to representation learning challenges.
- Maximum Entropy methods are less impacted by observation type, offering more robust exploration despite not always being optimal.
- ICM shows consistent stability but slower convergence due to added computational complexity.
- Learning diverse skills with DIAYN does not promote exploration in MiniGrid environments because learning the skill space itself is challenging, and exploration within the skill space prioritizes differentiating behaviors over uniform state visitation.

This is the first systematic evaluation of diversity levels in intrinsic rewards within a unified framework, offering novel insights into their influence on exploration and performance.

### 2.3 Go-Explore and Its Variants

#### 2.3.1 The Original Go-Explore Algorithm

Go-Explore, introduced by Ecoffet et al. (Nature 2021), represents a paradigm shift in hard exploration [7]. The algorithm operates on three core principles: (1) remembering previously visited states, (2) returning to a promising state before exploring from it, and (3) solving simulated environments through any available means (including determinism), then robustifying via imitation learning.

The algorithm has two phases. Phase 1 builds an archive of interesting states and the trajectories leading to them, exploiting determinism to reliably return to archived states. Remarkably, this phase achieves its exploration success using entirely random actions—no neural network is needed. The key insight is that the primary bottleneck in hard exploration is not sophisticated action selection but rather the ability to systematically build upon previous discoveries. Phase 2 creates robust policies through imitation learning (the Backward Algorithm with PPO), introducing stochasticity for real-world conditions.

Go-Explore identified two fundamental issues with intrinsic motivation approaches: *Detachment* (agents drift away from promising areas after exhausting intrinsic rewards) and *Derailment* (stochasticity prevents reliable return to complex states). Key results include a mean score of over 43,000 points on Montezuma's Revenge without domain knowledge (almost 4× previous state of the art), and with domain knowledge, a maximum performance of nearly 18 million points—surpassing the human world record of 1,219,200 by over an order of magnitude [7]. On Pitfall, Go-Explore was the first algorithm to score above zero, achieving a mean score of ~60,000 points that exceeds expert human performance.

#### 2.3.2 Intelligent Go-Explore (IGE)

"Intelligent Go-Explore" by Lu, Hu, and Clune (ICLR 2025) greatly extends the scope of the original Go-Explore by replacing handcrafted heuristics with the intelligence and internalized human notions of interestingness captured by giant pretrained foundation models (FMs) [8]. IGE offers the exciting opportunity to recognize and capitalize on serendipitous discoveries—states encountered during exploration that are valuable yet where what makes them interesting was not anticipated by the human user.

Evaluated on diverse language and vision-based tasks requiring search and exploration, IGE strongly exceeds classic RL and graph search baselines, and succeeds where prior state-of-the-art FM agents like Reflexion completely fail. This opens up a new frontier of research into creating more generally capable agents with impressive exploration capabilities.

#### 2.3.3 Limitations and Extensions

Go-Explore's limitations include the requirement for simulator resets to arbitrary states, challenges in cell representation design, and scalability concerns in high-dimensional domains. Extensions include Policy-based Go-Explore (for when deterministic resets are impossible), Cell-Free Latent Go-Explore (LGE) using VQ-VAE, and I-Go-Explore combining ICM with the Go-Explore framework to alleviate the detachment problem in multi-agent settings [9][10].

Applications span robotics (pick-and-place tasks), automated game testing, safety verification (adaptive stress testing of autonomous vehicles), residential energy management (up to 19.84% cost savings), and language/reasoning tasks [9].

### 2.4 Hindsight Experience Replay (HER) and Its Successors

#### 2.4.1 The Original HER

Hindsight Experience Replay (HER), introduced by Andrychowicz et al. (NeurIPS 2017), is a goal-relabeled experience replay technique that converts failed episodes into synthetic successes [11]. The fundamental insight is deceptively simple yet powerful: even when an agent fails to reach its intended goal, it inevitably reaches some state at the end of the episode. This achieved state can be retrospectively treated as a valid goal.

HER acts as a form of implicit curriculum, enabling learning from failure. On robotic manipulation tasks (pushing, sliding, pick-and-place) with a simulated 7-DOF Fetch Robotics arm using DDPG: DDPG without HER achieved near-zero success rates, while DDPG+HER achieved success rates above 80–90%. The "future" strategy for selecting hindsight goals performed best, with k=4 to k=8 additional hindsight goals per transition. A policy trained entirely in simulation using HER successfully transferred to a physical Fetch robot, achieving 5/5 successes after retraining with added Gaussian noise [11].

#### 2.4.2 Key Variants

Key extensions include USHER (uses importance sampling to correct hindsight bias in stochastic environments), ARCHER (counters overoptimism through reward rescaling), model-based approaches (MHER, I-HER, MRHER that use forward models to imagine virtual goals), and diversity-driven replay using determinantal point processes [12].

A central theoretical trade-off in HER arises from the mismatch between the likelihood of trajectories under the original and relabeled goals. DHER (ICLR 2019) addresses the challenge of dynamic goals (e.g., grasping a moving object), automatically assembling successful experiences from two relevant failures [13].

#### 2.4.3 MOC-HER and 2HER

MOC-HER integrates HER into the Multi-updates Option Critic (MOC) framework for hierarchical RL in multi-goal environments with sparse rewards [14]. Results in FetchReach show that MOC-HER achieved up to 96.57% relative improvement with 2 options, while standard MOC failed to solve the environment.

Dual Objectives HER (2HER), accepted at AAMAS 2026, creates two sets of virtual goals: one based on the object's final state (standard HER) and one from the agent's effector positions [15]. This rewards the agent for both interacting with the object and completing the task. Experiments show MOC-2HER achieves success rates of up to 90% in object manipulation tasks, compared to less than 11% for both MOC and MOC-HER.

### 2.5 Hierarchical RL for Exploration in Sparse Reward Settings

#### 2.5.1 Unlimited Option Scheduling (UOS)

"Hierarchical reinforcement learning with unlimited option scheduling for sparse rewards in continuous spaces" (Expert Systems with Applications, 2024) introduces a distinction between "limited options" (sampled from discrete distributions) and "unlimited options" (extended to continuous distributions capable of representing infinite knowledge) [16]. UOS introduces a composite scheduling mode that generates arbitrary-length trajectories with intrinsic characteristics, providing both flexibility and concentration for unlimited options. Experimental results demonstrate notable success on sparse reward tasks compared to conventional option-based HRL algorithms.

#### 2.5.2 GEAPS: Goal Exploration via Pre-trained Skills

"Goal exploration augmentation via pre-trained skills for sparse-reward long-horizon goal-conditioned reinforcement learning" (Machine Learning, 2024) proposes GEAPS, a maximum entropy goal exploration method using pre-trained skills [17]. The method learns behavior patterns (goal-transition patterns) from pre-training environments in the form of skills. Skills are pre-trained via a novel entropy-based objective that maximizes both mutual information between skills and goals AND the entropy of goals, ensuring wider goal coverage. Theoretical analyses show that pre-trained skills can compose optimal exploration policies, and incorporating GEAPS into state-of-the-art GCRL methods (e.g., Goal GAN, Skew-Fit, OMEGA) boosts their exploration efficiency.

#### 2.5.3 HIDIO and Hierarchical World Models

HIDIO (Hierarchical RL by Discovering Intrinsic Options, ICLR 2021) learns task-agnostic options in a self-supervised manner while jointly learning to use them to solve sparse-reward tasks [18]. Options are learned through an intrinsic entropy minimization objective conditioned on option sub-trajectories, resulting in diverse and task-agnostic options. In sparse-reward robotic manipulation and navigation tasks, HIDIO achieves higher success rates with greater sample efficiency than regular RL baselines and two state-of-the-art hierarchical RL methods.

"Exploring the limits of hierarchical world models in reinforcement learning" (Scientific Reports, 2024) presents a novel HMBRL framework that constructs hierarchical world models using Recurrent State Space Models (RSSMs) stacked with higher levels representing the environment at coarser temporal resolutions [19]. A hierarchy of agents communicates top-down by proposing goals to subordinate agents. A central challenge identified is "model exploitation" at the abstract level of the world model stack.

### 2.6 Unsupervised Skill Discovery

#### 2.6.1 Overview

Unsupervised Skill Discovery (USD) refers to a family of methods for autonomously learning a broad set of diverse, reusable behaviors without externally provided reward functions [20]. The goal is to generate latent-conditioned policies that can serve as primitives for rapid adaptation and efficient hierarchical control in downstream tasks.

Key approaches include Mutual Information Maximization (e.g., DIAYN), Distance-Maximizing methods (e.g., LSD), and Contrastive and Ensemble objectives (e.g., CIC, CeSD).

#### 2.6.2 Controllability-aware Skill Discovery (CSD)

CSD (ICML 2023) addresses the limitation of prior approaches (like DIAYN and LSD) that tend to discover only simple, easy-to-learn skills while ignoring more complex behaviors [21]. CSD uses a learned controllability-aware distance function that assigns larger values to hard-to-control state transitions, actively incentivizing the discovery of challenging skills. The method progressively learns more complex skills over training as the jointly trained distance function reduces rewards for easy-to-achieve skills. Results across six robotic manipulation and locomotion environments (Kitchen, Fetch, Ant, HalfCheetah) show CSD significantly outperforms prior methods.

#### 2.6.3 METRA: Scalable Unsupervised RL

METRA (Metric-Aware Abstraction, ICLR 2024) proposes a novel unsupervised RL objective designed to scale to complex, high-dimensional environments [22]. The key insight is to learn diverse behaviors that cover a compact latent space connected to the state space by temporal distances, rather than attempting to cover the entire state space directly.

This is formalized as maximizing the Wasserstein Dependency Measure (WDM) between states and skills, which is metric-aware (unlike mutual information) and encourages behaviors that are maximally different in terms of temporal distance. METRA learns a non-linear "temporal PCA" that discovers the most temporally spread-out manifolds of the state space.

METRA is the first unsupervised RL method to discover diverse locomotion behaviors in pixel-based Quadruped and Humanoid environments. It achieves the best state/task coverage and downstream task performance compared to both pure exploration methods (RND, ICM, APT) and skill discovery methods (DIAYN, DADS, CIC, LSD). METRA also enables zero-shot goal-reaching by using the learned abstraction to select skills that move toward goal states.

#### 2.6.4 Discovery of Mixture Skills (DiMS)

DiMS (AAAI 2024) introduces a novel URL algorithm that learns a latent Gaussian mixture prior for skill discovery [23]. Unlike existing methods that use either discrete categorical codes or unimodal continuous skill priors, DiMS employs a hierarchical Gaussian Mixture Variational Autoencoder (GMVAE) trained jointly with the unsupervised policy. An auxiliary macro-latent dynamically adjusts mixture component locations to prevent mode collapse. DiMS combines a skill-agnostic exploration bonus (RND) with a skill-conditioned intrinsic reward, enabling simultaneous exploration, skill discovery, and policy learning. DiMS achieves state-of-the-art performance on the URLB, outperforming 11 peer methods including DIAYN, EDL, CIC, APS, Metra, CeSD, and BeCL across 12 downstream tasks.

### 2.7 Information-Theoretic Exploration Methods

#### 2.7.1 VIME and Variational Information Gain

VIME (Variational Information Maximizing Exploration, NeurIPS 2016) uses variational information gain using Bayesian neural networks as an intrinsic reward [24]. This approach grounds exploration in the principled objective of reducing uncertainty about the environment's dynamics.

#### 2.7.2 VIB-IG: Information Bottleneck with Information Gain

"Information-Theoretic Intrinsic Motivation for Reinforcement Learning in Combinatorial Routing" (Entropy, 2026) proposes VIB-IG, a framework that integrates the Information Bottleneck (IB) principle with RL [25]. The framework defines intrinsic motivation signals based on information-theoretic quantities: learning compact latent state representations via the IB principle (balancing compression of observations with preservation of predictive information), and defining intrinsic rewards as pointwise mutual information (information gain) within this bottlenecked latent space. Neural mutual information estimators (MINE) enable scalable estimation. On TSP and SDVRP, VIB-IG improves exploration efficiency, training stability, and solution quality.

#### 2.7.3 RFIG: Random Feature Information Gain

"Information-Based Exploration via Random Features for Reinforcement Learning" (arXiv:2607.17981) introduces Random Feature Information Gain (RFIG), a new exploration bonus grounded in Bayesian kernel methods theory [26]. RFIG uses random Fourier features to approximate information gain in non-countable spaces, avoiding the black-box aspects and hyperparameter sensitivity of neural network-based uncertainty estimation.

Key technical contributions include deriving RFIG from Gaussian process information gain, providing theoretical error bounds on information gain approximation, and showing that the required feature dimension scales linearly with problem dimension and logarithmically with desired accuracy. RFIG demonstrates competitive performance with RND and VIME while offering superior theoretical interpretability and lower hyperparameter sensitivity. This work challenges the prevailing assumption that effective exploration requires increasingly sophisticated neural architectures.

### 2.8 Hybrid Approaches: NGU and Agent57

#### 2.8.1 Never Give Up (NGU)

Never Give Up (NGU) by Puigdomènech Badia et al. (ICLR 2020) combines episodic and life-long novelty for directed exploration [27]. NGU uses: (1) episodic novelty (encouraging visits to states distinct from previous states in the same episode via an episodic memory and inverse dynamics model), (2) life-long novelty (RND-based curiosity), and (3) the Universal Value Function Approximator (UVFA) framework to simultaneously learn different trade-offs between exploration and exploitation.

On hard exploration Atari games, NGU significantly outperforms baselines, notably achieving the first non-zero reward in Pitfall! (8.4k score) without demonstrations or hand-crafted features, and reaching 100.0k in Private Eye. Even without extrinsic rewards, NGU achieves superhuman performance on dense reward games, showing its exploration policy is a highly effective prior.

#### 2.8.2 Agent57

Agent57 by DeepMind (ICML 2020) is the first deep RL agent to achieve above-human baseline performance on all 57 Atari 2600 games [28]. Agent57 combines an efficient exploration algorithm (building on NGU) with a meta-controller that adaptively balances exploration vs. exploitation and adjusts the time horizon for credit assignment.

Key innovations include a distributed architecture with actors, a prioritized replay buffer, and a learner (similar to R2D2); short-term memory via LSTM combined with off-policy learning; episodic memory for detecting and exploring novel states; intrinsic motivation rewards using both long-term novelty (RND) and short-term novelty (episodic memory); and a meta-controller using a sliding-window UCB bandit algorithm that selects which policy (exploration vs. exploitation trade-off, and time horizon) each actor should use.

The Q-function is decomposed into separate extrinsic and intrinsic components, each optimized with separate networks. This significantly increases training stability across a large range of intrinsic reward scales. Agent57 achieves 100% capped human normalized score across all 57 Atari games, surpassing the human benchmark on 51 games within the first 5 billion frames. The agent uses a family of 32 policies (β, γ pairs) with discount factors ranging from 0.99 to 0.9999.

### 2.9 Meta-Learning Approaches for Exploration

#### 2.9.1 Meta-RL Foundations

Meta-RL aims to enable agents to leverage experience from previous tasks to learn new tasks with less data [29]. Black-box meta-RL methods train a sequence model (transformer, RNN, or recurrent network) that takes as input the agent's collected experience (states, actions, rewards) and outputs actions. The policy conditions on this training dataset and is trained across multiple MDPs. Transformers generally outperform LSTMs, and off-policy algorithms (e.g., SAC) are more data-efficient for meta-training than on-policy methods (e.g., PPO).

#### 2.9.2 Meta-Learned Curiosity Algorithms

Alet et al. (ICLR 2020) took a unique approach to discovering new curiosity algorithms by meta-learning pieces of code in a domain-specific language (DSL) represented as Directed Acyclic Graphs (DAGs) [30]. The search discovered two primary algorithms:

- **FAST (Fast Action Space Transition):** Contains a single policy-mimicking network that predicts the agent's action given a state. The intrinsic reward is the L2 distance between predicted actions for consecutive states.
- **CCIM (Cycle-Consistency Intrinsic Motivation):** Uses three neural networks (random, backward, and random+forward networks). The intrinsic reward is the L2 distance between backward-transformed embeddings of consecutive states.

In empty grid-world, FAST and CCIM performed comparably to RND and BYOL-Explore Lite, covering more map area. However, in deep sea environments, they performed worse than baselines. A major concern is that FAST and CCIM intrinsic rewards did NOT decrease during training (unlike RND, BYOL-Explore, and CCIM-slimmed), identified as a flaw.

#### 2.9.3 LaMer: Meta-RL for LLM Agents

"Meta-RL Induces Exploration in Language Agents" (LaMer, arXiv:2512.16848) presents a Meta-RL framework for training LLM agents to actively explore and adapt in multi-turn, long-horizon tasks [31]. LaMer consists of two key components: (i) a cross-episode training framework to encourage exploration and long-term rewards optimization, and (ii) in-context policy adaptation via reflection. It uses a trajectory discount factor (γ_traj) to incentivize exploration in early episodes for better exploitation later.

Using Qwen3-4B, LaMer outperforms prompting and RL baselines across four environments (Sokoban, MineSweeper, Webshop, ALFWorld), with performance gains over the best RL baseline of 11% on Sokoban, 14% on Webshop, and 19% on MineSweeper at pass@3. This is the first time a meta-RL framework is used for LLM agent training.

### 2.10 Recent Conference Trends (2024–2026)

The curated GitHub repository "Awesome Exploration Methods in Reinforcement Learning" (OpenDILab, updated May 2026) categorizes methods into Augmented Collecting Strategy and Augmented Training Strategy [32]. Key trends include:

**ICML 2026 (20 papers):** Topics include Joint-Space Empowerment, NonZero MCTS exploration, Rubric-scaffolded reasoning for LLMs, Uncertainty-guided exploration, Covariance Volume Maximization, Variance Driven Exploration, Multi-Objective RL, Task-Aware Exploration, Episodic Memory-guided synthesis, and Exploration Hacking in LLMs.

**ICLR 2026 (22 papers):** Topics include Exploratory Diffusion Models, Spectral Bellman Methods, Epistemic Uncertainty Bayesian RL, Q-learning with Posterior Sampling, Graph-Theoretic Intrinsic Rewards, Temporal Representations, Count-based intrinsic rewards for LLM reasoning (MERCI), and Thompson Sampling via LLM fine-tuning.

**NeurIPS 2025 (19 papers), ICML 2025 (17 papers), ICLR 2025 (11 papers), NeurIPS 2024 (13 papers), ICML 2024 (15 papers), ICLR 2024 (14 papers):** Spanning state entropy regularization, LLM-Explorer, uncertainty-guided AlphaZero, safe exploration, Monte Carlo Tree Diffusion, behavioral exploration, dormant ratio minimization, and long-term novelty-based exploration.

---

## 3. Exploration Under Constraints

### 3.1 Constrained Markov Decision Processes (CMDPs)

The core paradigm for safe RL is the Constrained Markov Decision Process (CMDP), where safety constraints are added to the standard reward maximization objective [33]. A CMDP is specified as (S, A, P, r, {c(i)}, γ, μ) with state space S, action space A, transition kernel P, reward r, cost functions c(i), discount factor γ, and initial state distribution μ.

For finite CMDPs, there exists an optimal stationary policy, potentially randomized if there are multiple constraints. Strong duality holds, enabling primal-dual algorithms alternating between augmented reward optimization and dual ascent on constraint violations. Constraint types covered include: instantaneous constraints (torque/force limits, collision avoidance, voltage/current limits), probability of failure constraints (spacecraft landing, robot falling, patient mortality), risk measure constraints (variance, CVaR for portfolio optimization), and multi-objective trade-offs [34].

### 3.2 Constrained Policy Optimization Methods

#### 3.2.1 Constrained Policy Optimization (CPO)

Constrained Policy Optimization (CPO) by Achiam et al. (ICML 2017) is a trust region method for constrained RL that uses approximations to predict how constraint costs might change after each update, choosing the update that maximizes performance while keeping costs below limits [35]. CPO is the first algorithm to make deep RL practical for constrained settings with theoretical performance guarantees. The algorithm provides theoretical guarantees on both the performance of trust region methods and worst-case constraint violations after CPO updates. However, CPO can be conservative, achieving lower rewards than some alternatives while guaranteeing safety constraints.

#### 3.2.2 Projection-Based CPO (PCPO)

PCPO (ICLR 2020) is a two-step iterative algorithm: (1) a reward improvement step using trust region optimization within a KL divergence constraint, followed by (2) a projection step that projects the policy back onto the constraint set using either L2 norm or KL divergence as distance measures [36]. Theoretical analysis provides lower bounds on reward improvement and upper bounds on constraint violation. PCPO averages 3.5 times less constraint violation and approximately 15% higher reward compared to baseline methods. The projection step enables efficient recovery from constraint-violating states without extensive hyperparameter tuning.

#### 3.2.3 First Order Constrained Optimization (FOCOPS)

FOCOPS (NeurIPS 2020) uses a two-step method: (1) Given a current policy, find the optimal update policy by solving a constrained optimization problem in the nonparameterized policy space, yielding a near-closed form solution. (2) Project this policy back into the parametric policy space by minimizing a KL divergence loss function using first-order gradient methods [37].

Advantages include being first-order only (no Fisher information matrix inversion needed), providing an approximate upper bound for worst-case constraint violation throughout training, and avoiding approximation errors from second-order Taylor expansions. FOCOPS consistently enforces approximate constraint satisfaction while having higher performance on five out of six robot speed-limit tasks compared to CPO, PPO-Lagrangian, and TRPO-Lagrangian.

#### 3.2.4 Constrained Update Projection (CUP)

CUP (NeurIPS 2022) provides rigorous safety guarantees while maximizing reward [38]. Key theoretical contributions include new surrogate functions with generalized policy performance difference bounds that extend to Generalized Advantage Estimator (GAE), providing the first rigorous theoretical analysis linking GAE to safe RL surrogate functions. CUP is a two-step approach: Step 1 updates policy using a surrogate objective with GAE and KL-divergence penalty; Step 2 projects the policy back onto the safe region if constraints are violated, using a primal-dual approach.

Theorem 2 provides worst-case performance degradation guarantees and constraint satisfaction bounds. Unlike CPO and PCPO which require convex approximations and expensive inverse Fisher information matrix computations, CUP uses only first-order optimizers, making it computationally efficient for high-dimensional problems. In Hopper-v3, CUP achieved 2025.56 reward vs. 1687.72 for FOCOPS (the next best).

#### 3.2.5 Constraint-Sensitive Policy Optimization (CSPO)

CSPO (ICML 2026) introduces a first-order primal-dual method that addresses limitations in existing methods for solving CMDPs, including "dual-lag" effects, delayed constraint correction, and oscillatory behavior near safety boundaries [39]. CSPO augments the primal objective with a constraint-sensitive correction derived from the shortest signed distance to the safety boundary. It incorporates the local constraint gradient norm to scale corrective updates: large gradient norms (steep boundaries) receive cautious steps, while small gradient norms (flat regions) receive stronger corrective updates.

Theoretical properties include preserving the same KKT solutions as the original constrained problem, achieving O(L³G²λ_max²/ε⁶) convergence rate to ε-stationary points, and guaranteeing local constraint decrease when violations exceed a threshold. Evaluated on 9 Safety Gymnasium tasks against 11 baselines, CSPO achieves competitive or superior constrained returns while respecting cost limits, with most pronounced gains in navigation tasks. CSPO demonstrates faster safety recovery, reduced oscillations near boundaries, and a +15.6% average improvement in constrained returns.

#### 3.2.6 C-TRPO: Safe Trust Region Methods

C-TRPO (ICML 2025) modifies the geometry of the policy space based on safety constraints, yielding trust regions composed exclusively of safe policies [40]. The key insight is to augment the standard KL divergence with a barrier-like function that goes to infinity at the constraint boundary, creating trust regions entirely contained within the safe policy set. Theoretical analysis shows safety during training (invariance of the safe set under C-NPG dynamics), global convergence to optimal safe policies, and worst-case constraint violation bounds strictly better than CPO. C-TRPO reduces oscillations around the cost threshold, mitigating overshoot behaviors that cause constraint violations.

### 3.3 Lagrangian and PID Methods

#### 3.3.1 PID Lagrangian

The PID Lagrangian method (Stooke, Achiam, Abbeel, ICML 2020) proposes a novel Lagrange multiplier update method that utilizes derivatives of the constraint function (PID control principles) [41]. The method addresses the challenge of responsive safety in constrained RL, where agents must satisfy safety constraints during training.

The PID Lagrangian method mitigates transient violations by interpreting the dual update as a feedback controller: the multiplier λ regulates the constraint cost around the setpoint. The standard Lagrangian dual update is equivalent to an integral-only controller. Augmenting it with proportional and derivative terms yields the PID multiplier update: λ_{t+1} = [K_P(J_c - l) + K_I Σ(J_c - l) + K_D(J_c(t) - J_c(t-1))_+]_+, where the derivative term responds only to increases in violation. Stabilization mechanisms include separate value and cost-value critics to prevent interference, and gradient rescaling by 1/(1+λ).

#### 3.3.2 Reward Constrained Policy Optimization (RCPO)

RCPO (ICLR 2019) frames safe RL as a CMDP and uses a Lagrangian multiplier λ to balance the main reward objective with a safety constraint [42]. The Lagrangian multiplier λ can be treated as a learnable parameter and updated via gradient descent. Intuitively, λ determines how much weight is put onto the constraint. If λ is set to 0, the constraint is ignored; if λ is set very high, the constraint is enforced very strictly. The adaptive RCPPO agent achieves the best balance between reward and constraint satisfaction.

### 3.4 Safety Critics and Shielding Approaches

#### 3.4.1 Conservative Safety Critics

"Conservative Safety Critics for Exploration" (Bharadhwaj et al., ICLR 2020) theoretically characterizes the tradeoff between safety and policy improvement, shows that safety constraints are likely to be satisfied with high probability during training, and derives provable convergence guarantees [43]. The method demonstrates efficacy on a suite of challenging navigation, manipulation, and locomotion tasks.

#### 3.4.2 Shielding

Safe RL via shielding is a framework that enforces formal safety specifications on RL agents by supplementing the control loop with an external "shield"—a runtime filter that restricts actions or corrects unsafe ones [44]. This decouples safety logic from reward-driven policy optimization. Two principal architectures exist: Pre-decision shielding (action space restricted to safe actions before policy selection) and Post-decision shielding (shield monitors and vetoes/corrects unsafe actions in real time).

Extensive benchmarks show shielded RL achieves orders-of-magnitude reductions in safety violations and accelerates learning. In Safety Gymnasium, violations are reduced 50–60% with reward within 5–10% of baseline. In Multi-Agent Navigation, collision rate goes to zero with 20–40% faster learning. Shielding differs from constrained RL and reward-shaping by enforcing hard or probabilistic safety constraints a priori, rather than in expectation, via separation of verification and learning.

#### 3.4.3 SAILR: Advantage-Based Intervention

SAILR (ICML 2021) uses an intervention mechanism based on advantage functions to keep the agent safe throughout training [45]. The method transforms the safe RL problem into an unconstrained MDP problem by constructing a surrogate MDP that penalizes intervened state-action pairs. SAILR provides formal theoretical guarantees: if the base RL algorithm finds an ε-suboptimal policy for the surrogate MDP, the returned policy is roughly ε-suboptimal in the original MDP with safety comparable to the backup policy. SAILR requires only a backup policy that is safe from the initial state (not globally). Experiments on point robot and half-cheetah tasks show SAILR dramatically reduces safety violations during training (orders of magnitude fewer than baselines like CPO and PDO) while achieving competitive deployment performance.

#### 3.4.4 Approximate Model-Based Shielding (AMBS)

AMBS formalizes model-based shielding within a PCTL framework, derives PAC-style probabilistic bounds on constraint violation estimation, and implements the method using DreamerV3 as the world model [46]. AMBS uses a look-ahead shielding procedure that simulates future trajectories via the learned model, checks for bounded safety violations, and falls back to a safe policy when violations are likely. Experiments on five Atari games with state-dependent safety-labels show AMBS significantly reduces cumulative safety violations during training compared to vanilla DreamerV3, DreamerV3 with Lagrangian penalties, and model-free baselines, while achieving comparable or better episode returns.

#### 3.4.5 Proactive Projection

"Reducing Safety Interventions in Provably Safe Reinforcement Learning" (Thumm, Pelat, & Althoff, 2023) proposes two novel intervention reduction methods: proactive replacement (replacing actions that would trigger a failsafe with verified randomized actions) and proactive projection (finding nearby verified actions by projecting to intersection-free space) [47]. Both methods use set-based reachability analysis to verify safety before execution, incorporating uncertainties and time delays. This is the first RL agent to guarantee zero constraint violations on the OpenAI Safety Gym benchmark, with real-world demonstration on a Schunk LWA 4P manipulator.

### 3.5 Lyapunov-Based Safe RL

#### 3.5.1 Foundational Lyapunov Approach (Chow et al., 2018)

"A Lyapunov-based Approach to Safe Reinforcement Learning" (Chow, Nachum, Ghavamzadeh, NIPS 2018) presents a Lyapunov-based approach to safe RL under the framework of CMDPs [48]. Key contributions include: a novel Lyapunov method for solving CMDPs, including an LP-based algorithm to construct Lyapunov functions that guarantee feasibility and optimality; two safe dynamic programming algorithms—Safe Policy Iteration (SPI) and Safe Value Iteration (SVI)—with analysis of feasibility and convergence; and scalable off-policy safe RL algorithms: Safe DQN (SDQN) and Safe Deep Policy Improvement (SDPI).

The approach works by constructing a Lyapunov function L such that policies induced by L are guaranteed to be feasible. A key lemma shows that with appropriate cost-shaping, the optimal policy's constraint value function can be transformed into a Lyapunov function. Empirical evaluation on a 25×25 grid-world safety benchmark shows that Lyapunov-based methods outperform baselines (Lagrangian, step-wise surrogate, super-martingale surrogate, dual LP) in balancing constraint satisfaction and performance.

#### 3.5.2 Lyapunov-Assisted Deep RL

Lyapunov-Assisted DRL integrates classical Lyapunov stability theory into DRL pipelines to ensure safety and stability in dynamic systems [49]. Key techniques include learning Lyapunov proxy functions from data, incorporating Lyapunov decrease penalties into rewards or constraints, and using Lyapunov functions to define safe sets, guide exploration, and restrict policy improvement. Theoretical guarantees include closed-loop stability, safety constraints via forward-invariant sublevel sets, improved sample complexity, and formal verification via neural Lyapunov-barrier certificates. Empirical validations span continuous stabilization and robotics (acrobot, quadrotor, hopper, walker), safe navigation (near-zero collision rates), and decentralized multi-agent control.

### 3.6 Control Barrier Functions and Reachability

#### 3.6.1 RL-CBF: End-to-End Safe RL through Barrier Functions

"End-to-End Safe Reinforcement Learning through Barrier Functions for Safety-Critical Continuous Control Tasks" (AAAI-19) introduces RL-CBF, a framework combining three components: a model-free RL-based controller, model-based control barrier functions (CBFs) to guarantee safety, and online learning of unknown system dynamics using Gaussian Processes [50].

The key innovation is that CBFs constrain the set of explorable policies to a safe region, ensuring that safety is maintained with high probability throughout the entire learning process, not just after convergence. Two architectures are developed: a compensating controller that filters unsafe actions, and a guiding controller that actively shapes policy exploration. RL-CBF was tested on balancing an inverted pendulum and autonomous car-following, maintaining safety in both tasks while achieving significantly faster learning and higher sample efficiency compared to standard TRPO and DDPG baselines.

#### 3.6.2 Reachability Constrained Reinforcement Learning (RCRL)

RCRL (ICML 2022) uses reachability analysis to characterize the largest feasible set—the subset of states from which persistent safety can be guaranteed [51]. Key contributions include establishing a "self-consistency condition" for the safety value function, enabling computation of feasible sets via temporal difference learning, and formulating a constrained optimization problem that maximizes reward while ensuring persistent safety.

Experiments on three benchmarks show: Double integrator: RCRL learns the exact largest feasible set (HJ viability kernel), outperforming conservative MPC-CBF and MPC-Terminal baselines; Safe-control-gym (quadrotor tracking): zero violations with near-optimal tracking; Safety-Gym (high-dimensional tasks): the best constraint satisfaction with comparable or better returns than PPO-Lagrangian, PPO-CBF, and PPO-SI baselines. RCRL explores the boundary of the feasible sets instead of conservatively staying inside them, leading to more violations during the early training stage but less conservatism overall.

#### 3.6.3 Black-box Reachability-based Safety Layer (BRSL)

BRSL combines data-driven reachability analysis for a black-box robot model, a trajectory rollout planner using an ensemble of neural networks trained online, and a differentiable polytope collision check between reachable sets and obstacles [52]. The method provides a formal safety guarantee (Theorem 1) proving that the robot is guaranteed to be safe at all times if assumptions hold. BRSL achieved 0% collision rates across all tested environments (Turtlebot 3, quadrotor, point mass, hexarotor), outperforming all baselines.

#### 3.6.4 ATACOM and Directional Constraints

The ATACOM framework (Acting on the TAngent Space of the COnstraint Manifold) provides a model-based safe exploration method that exploits knowledge of robot dynamics and constraints to construct a constraint manifold and a safe action space, theoretically proven to be a safe controller and deployable on real robots [53]. ATACOM-DC (submitted July 2026) extends this by introducing directional constraints that analyze the sign of the constraint function's time derivative under the proposed action, selectively restricting only actions that point toward the constraint boundary while allowing actions moving away from boundaries to pass unmodified.

Evaluated on a Kuka iiwa robot performing air hockey and a quadrotor tracking task, ATACOM-DC showed faster learning convergence, superior final performance maintaining near-zero costs while achieving target tracking accuracy comparable to unconstrained methods, and greater robustness to the safety margin parameter. By addressing the symmetric morphing problem, the authors show it is possible to maintain rigorous safety guarantees without the heavy "exploration tax" usually associated with safety filters.

### 3.7 Model-Based Safe Exploration

#### 3.7.1 Conservative and Adaptive Penalty (CAP)

CAP (AAAI-22) presents a model-based safe RL framework that addresses the challenge of ensuring safety constraints during training when using imperfect learned transition models [54]. Key contributions include: a conservative cost penalty that derives an uncertainty-aware penalty function that inflates predicted costs, with theoretical proof that policies satisfying this conservative cost constraint are guaranteed to be feasible in the true environment; and an adaptive penalty tuning mechanism using a proportional-integral (PI) controller that balances conservativeness with performance.

In tabular MDPs, the authors prove with high probability that solutions to the conservative LP are feasible in the true environment, and that all training episodes remain safe. In HalfCheetah (velocity-constrained), CAP achieves comparable returns to state-of-the-art model-free methods (FOCOPS, PPO-Lag) with 5–10× fewer environment steps, and incurs only ~1.7 violations vs 108–378 for baselines.

#### 3.7.2 Safe Model-Based Policy Optimization (SMBPO)

SMBPO (NeurIPS 2021/2022) proposes a reward penalty framework where a terminal cost C is assigned to unsafe states, with theoretical guarantees that with a sufficiently large penalty and a calibrated dynamics model, an optimal policy will avoid safety violations [55]. The practical algorithm builds on MBPO and uses an ensemble of probabilistic dynamics models, short-horizon model-based rollouts, and a modified Q-function update that penalizes unsafe states.

Experiments on MuJoCo continuous control tasks (Hopper, Cheetah-no-flip, Ant, Humanoid) show that SMBPO achieves comparable or better performance with far fewer safety violations compared to model-free safe RL baselines (Recovery RL, Lagrangian relaxation, SQRL, RCPO). SMBPO's predictive capability enables proactive avoidance, making it more suitable for environments where mistakes have severe consequences.

#### 3.7.3 Constrained Model-Based Policy Optimization (CMBPO)

CMBPO addresses the challenge that model-free safe RL algorithms are prohibitively sample-inefficient, while model-based approaches suffer from model bias and accumulating prediction errors [56]. The authors derive a theoretical bound relating the difference in expected returns between policies under true dynamics to an optimization term under learned model dynamics plus a penalty term. The practical algorithm uses an ensemble of probabilistic dynamics models, an adaptive resampling scheme, and adaptive rollout horizons. On simulated robot locomotion tasks (AntSafe, HalfCheetahSafe, AntCircle), CMBPO reaches model-free asymptotic performance with 10–20× reduction in training samples.

#### 3.7.4 Sampling-Based Safe RL (SBSRL)

SBSRL (arXiv:2605.19469) introduces a model-based RL algorithm for safe exploration in continuous state-action spaces [57]. The core innovation is enforcing safety constraints jointly across a finite set of sampled dynamics models rather than solving an intractable worst-case optimization over uncertain dynamics. Under standard assumptions (RKHS dynamics, Gaussian noise, feasible safe initialization), SBSRL guarantees safety with high probability at every episode and provides a finite-time sample complexity bound. The algorithm is successfully deployed on a real robotic race car (60 Hz, 45-dimensional observation space) using deep ensembles, improving reward while maintaining safety during online learning.

### 3.8 Recovery RL and Backup Policy Approaches

#### 3.8.1 Recovery RL

Recovery RL (Balakrishna et al., ICRA/RAL 2021) addresses the tradeoff between exploration and safety by: (1) using offline data to learn about constraint-violating zones before policy learning, and (2) separating task performance and constraint satisfaction across two policies—a task policy that optimizes reward and a recovery policy that guides the agent to safety when constraint violation is likely [58]. A safety critic estimates the probability of near-future constraint violation, determining which policy to execute at each step.

Evaluated on 6 simulation domains (including contact-rich manipulation and image-based navigation) and an image-based obstacle avoidance task on a physical robot (da Vinci Research Kit), Recovery RL outperformed the next best method across all domains. It traded off constraint violations and task successes 2–80 times more efficiently in simulation and 3 times more efficiently in physical experiments.

#### 3.8.2 RLBUS: Backup Control Barrier Functions

RLBUS (L4DC 2025) uses Backup Control Barrier Functions (BCBFs) with multiple backup policies to synthesize an implicit control forward invariant subset of the safe set, ensuring safety under input constraints [59]. It addresses the conservatism of traditional BCBFs by using model-free RL to train an additional backup policy, enlarging the forward invariant safe subset. The approach enables safe exploration of larger state space regions with zero safety violations during training.

#### 3.8.3 SOOPER: Safe Exploration via Policy Priors

SOOPER (NeurIPS 2025 Workshop ARLET) uses suboptimal yet conservative policies as priors, with probabilistic dynamics models to optimistically explore while pessimistically falling back to the conservative policy prior when needed [60]. The authors prove that SOOPER guarantees safety throughout learning and establishes convergence to an optimal policy by bounding its cumulative regret.

### 3.9 Almost Surely Safe Exploration

"Almost Surely Safe Exploration and Exploitation for Deep Reinforcement Learning with State Safety Estimation" (Lin et al., Information Sciences, 2024) proposes Safe Proximal Policy Optimization (SPPO), which uses Gaussian process uncertainty estimation to evaluate states' safety values, creating a safe state set that intervenes in the agent's exploration [61]. The authors theoretically prove that the agent will not violate safety constraints with almost 100% probability during learning. Unlike CMDP-based approaches that only guarantee safety in the final policy, SPPO is a model-free approach that ensures safety throughout the entire learning process. Extensive experiments show superior performance over existing CRL algorithms in four environments.

### 3.10 Generalized Safe Exploration (GSE)

"Safe Exploration in Reinforcement Learning: A Generalized Formulation and Algorithms" presents a unified formulation for safe RL that encompasses cumulative constraints, state constraints, and instantaneous constraints [62]. The authors prove that all three problem types can be transformed into the GSE problem, which uses an instantaneous safety constraint with a time-varying threshold.

The proposed MASE (Meta-algorithm for Safe Exploration) combines an unconstrained RL algorithm with an uncertainty quantifier to guarantee safety with high probability during training. MASE uses an "emergency stop" action that resets the environment when no safe action exists. Two variants are presented: GLM-MASE (based on Generalized Linear Models, providing theoretical guarantees of safety and near-optimality with Õ(H√(d³(T−t*))) regret) and a practical variant combining Gaussian processes for safety with deep RL for reward maximization. Experiments on Safety Gym benchmarks show MASE satisfies safety constraints in every episode during training, outperforming TRPO, CPO, TRPO-Lagrangian, and Sauté RL.

### 3.11 Extreme Value Policy Optimization (EVO)

EVO (ICML 2025) addresses a key limitation of standard CRL methods: expectation-based cost constraints overlook rare but catastrophic "black swan" events in the tail distribution [63]. EVO leverages Extreme Value Theory (EVT) and the Generalized Pareto Distribution to model extreme samples in the cost tail distribution, reformulating constraints as extreme quantile constraints.

The methodology has three key components: integration of EVT-based constraints into a trust-region policy optimization framework with adaptive exploitation range, an extreme prioritization mechanism for replay buffer sampling that amplifies learning from rare high-impact events, and off-policy importance resampling to augment data for stable GPD parameter estimation. Theoretically, EVO guarantees strict constraint satisfaction at a zero-violation quantile level. Extensive experiments across Safety Gymnasium and Safety MuJoCo environments demonstrate EVO consistently maintains near-zero constraint violations while achieving competitive policy performance, with minimal computational overhead and robustness even with as few as 10–20 extreme samples.

### 3.12 Resource-Constrained Exploration

#### 3.12.1 Resource-Restricted RL (R3L) with RAEB

"Efficient Exploration in Resource-Restricted Reinforcement Learning" (AAAI-23) introduces Resource-Restricted Reinforcement Learning (R3L), a formalization of RL problems where actions consume non-replenishable resources (e.g., energy in robotics, consumable items in games) [64]. The authors observe that popular RL methods like PPO, SAC, and Surprise-based exploration suffer from poor sample efficiency in R3L tasks because they exhaust resources rapidly.

To address this, they propose a Resource-Aware Exploration Bonus (RAEB) that incorporates both novelty (via surprise-based intrinsic motivation using KL-divergence) and remaining resource quantities. The authors provide theoretical results showing RAEB achieves √T regret in the finite-horizon tabular setting. Experiments on nine R3L environments demonstrate that RAEB significantly outperforms state-of-the-art exploration strategies, improving the sample efficiency by up to an order of magnitude.

#### 3.12.2 Efficient Safe Policy Optimization (ESPO)

ESPO (NeurIPS 2024) enhances sample efficiency of safe RL through dynamic sample manipulation [65]. Safe RL suffers from sample inefficiency due to fixed sample sizes that waste resources on simple tasks and provide insufficient exploration for complex tasks. ESPO uses a three-mode optimization framework (reward-only, cost-only, and balanced reward-cost) and dynamically adjusts sample sizes based on gradient conflict signals between reward and safety objectives. It achieves 25–29% fewer samples and 21–38% reduced training time while improving reward performance and maintaining safety.

### 3.13 Offline-to-Online Safe Exploration

#### 3.13.1 SaGui: Guided Safe Exploration

"Reinforcement Learning by Guided Safe Exploration" (SaGui, Yang et al., 2023) introduces a framework for safe transfer learning in CMDPs [66]. The authors propose a three-step approach: (1) train a "guide" policy in a reward-free source task that only uses safety signals (costs) to explore safely, (2) distill this guide into a "student" policy dedicated to the target task via policy distillation with KL divergence regularization, and (3) compose a behaviour policy that mixes the guide and student using either linear-decay or control-switch sampling strategies.

Empirical evaluations on SafetyGym environments show that SaGui achieves safe exploration without violating constraints during training, outperforms learning-from-scratch (SAC-λ, CPO) and pre-training baselines, and matches expert-guided methods (EGPO) in performance. Key findings include that auxiliary rewards improve exploration diversity, safety-adaptive regularization speeds convergence, and control-switch outperforms linear-decay.

#### 3.13.2 Offline-to-Online RL (O2O RL)

Offline-to-Online RL is a learning framework that integrates static offline datasets with dynamic online interactions to maximize sample efficiency and safe deployment [67]. The framework operates in two phases: an offline phase where the agent learns from a pre-collected dataset, and an online phase where the agent interacts with the environment. Core challenges include distribution shift and extrapolation error, the stability-plasticity dilemma, and Q-value bias.

Algorithmic approaches are organized around replay buffer and data mixing, policy and value function regularization, pessimism/uncertainty/ensemble methods, distributional and exploration-aware planning, and Q-value debiasing. The stability-plasticity principle predicts three distinct regimes recommending either policy-anchoring or data-centric replay depending on baseline performance.

### 3.14 Formal Verification Methods

#### 3.14.1 Verified Safe RL (VSRL)

"Verified Safe Reinforcement Learning for Neural Network Dynamic Models" (NeurIPS 2024) presents VSRL, a novel approach for learning verified safe control policies in nonlinear neural dynamical systems while maximizing overall performance [68]. The approach has three key components: a curriculum learning scheme that iteratively increases the verified safe horizon, leveraging incremental verification during gradient-based learning to reuse prior verification information, and learning multiple verified initial-state-dependent controllers for complex domains. Experiments on five safe control problems demonstrate that the trained controllers achieve verified safety over horizons that are as much as an order of magnitude longer than state-of-the-art baselines, with a perfect safety record over entire episodes.

#### 3.14.2 Step-Wise Violation Constraints (Safe-RL-SW)

"Provably Safe Reinforcement Learning with Step-wise Violation Constraints" (NeurIPS 2023) introduces a novel safe RL problem with "step-wise violation constraints" (Safe-RL-SW), which is stricter than prior approaches that use episode-wise expected violation constraints [69]. The proposed SUCBVI algorithm uses optimistic estimation of costs and transition dynamics along with a dynamic programming procedure to recursively identify "potentially unsafe states" and determine safe action sets. SUCBVI achieves: Regret: Õ(√(H³SAT)) and Step-wise violation: Õ(√(ST)). A key theorem shows that achieving sublinear violation forces at least Ω(√T) regret, even in instances where o(√T) regret would be possible without safety constraints. The paper also extends the framework to Safe Reward-Free Exploration (Safe-RFE-SW) with the SRF-UCRL algorithm.

#### 3.14.3 VELM: Formal Verification via Symbolic Models

VELM (CAV 2024) learns symbolic environment models (using symbolic regression) rather than neural network models, enabling formal reachability analysis over the entire task horizon [70]. It constructs a safety shield by distilling a neural policy into a time-varying linear controller that can be formally verified. Across continuous control benchmarks, VELM demonstrates significantly fewer safety violations during training compared to existing safe RL techniques, without compromising reward performance.

### 3.15 Penalty-Based Reward Shaping

Penalty-based reward shaping is a family of techniques wherein the reward function is augmented with explicit penalty terms to discourage undesirable behaviors, enforce safety, or guide the agent toward preferred solutions [71]. The shaped reward = r_env + P, where P can be state-visit penalties, transition/dynamics penalties, or policy-dependent penalties.

The ROSARL Minmax Penalty framework (Tasse et al., 2023) assigns a calibrated penalty value for unsafe terminal states, guaranteeing that the optimal policy under the penalty simultaneously minimizes failure probability for any reward function. Bi-Level Shaping Weight Optimization (Hu et al., 2020) learns penalty weights online via meta-gradient methods, consistently penalizing detrimental shaping signals while amplifying useful ones. EXPLORS (NeurIPS 2022) combines extrinsic reward, self-supervised intrinsic rewards learned via meta-gradients, and count-based intrinsic bonuses for exploration, achieving significantly lower sample complexity in sparse reward environments [72].

---

## 4. Implications for Trajectory Planning

### 4.1 Curiosity-Driven Exploration for Motion Planning

#### 4.1.1 Curious Sample Planner (CSP)

The Curious Sample Planner (CSP), introduced at ICML 2020, fuses elements of Task and Motion Planning (TAMP) with Deep RL to achieve flexible and efficient long-range multi-step planning in sparse reward environments [73]. CSP uses curiosity-guided sampling combined with imitation learning to accelerate planning, avoiding the need for logical preconditions/effects required by TAMP while overcoming the sparse reward challenges that plague DRL.

The system architecture consists of action selection networks (actor-critic with PPO) that learn to select macro-actions maximizing curiosity, a geometric motion planning module, a forward dynamics module, and a curiosity module that scores novelty. CSP builds a search tree over state space, using curiosity signals to bias exploration toward novel states.

Tested on four physically realistic 3D robotics tasks (Block-Stack, Push-Away, Bookshelf, Launch-Block), CSP dramatically outperformed baselines (Vanilla PPO, HER, RND-PPO, RRT, and random exploration), often solving tasks where baselines failed entirely within a 10^7 sample limit. RND emerged as the best general-purpose curiosity metric. CSP also demonstrated effective task transfer, where action selection networks learned from one task could improve efficiency on related tasks.

#### 4.1.2 Curiosity-Driven Motion Planning on Humanoids

Frank, Leitner, Stollenga, Förster, and Schmidhuber (Frontiers in Neurorobotics, 2014) presented the first embodied, curious agent for real-time motion planning on the iCub humanoid robot [74]. The framework integrates reactive control (low-level) with a high-level curious RL agent, learning compact Markov models to represent the iCub's configuration space through intelligent exploration driven by information gain maximization (KL divergence-based artificial curiosity).

The configuration space is discretized into Voronoi regions (states) from sampled points. Actions involve setting attractor goals that drive the robot via a dynamical system. The artificial curiosity reward—computed as KL divergence between updated and previous state transition distributions—naturally focuses exploration on "interesting" state-actions that encounter constraints (non-deterministic outcomes). In static environment experiments, curiosity-driven exploration significantly outperforms random and least-tried strategies, achieving full coverage in roughly 2/3 the time. The system handles non-static environments that would break traditional PRM planners.

#### 4.1.3 Bi-Model: Curiosity-Driven Imagination for Open-World Adaptation

Bi-Model (arXiv, March 2025) proposes a hybrid planning and learning system that integrates two models for robotic manipulation adaptation to open-world novelties: a low-level neural network with an Intrinsic Curiosity Module (ICM) that learns stochastic transitions and drives exploration, and a high-level symbolic planning model that learns abstract operators, enabling planning in an "imaginary" space and generating Linear Temporal Logic (LTL) reward machines to densify reward signals [75]. Evaluated in RoboSuite's Pick and Place Can task, Bi-Model converges faster and achieves higher asymptotic success rates than state-of-the-art hybrid methods, reaching convergence 20% faster than HyGOAL.

### 4.2 RL-Guided Sampling-Based Planning

#### 4.2.1 PSST: Policy-guided Stable Sparse-RRT

PSST (Policy-guided Stable Sparse-RRT, ICRA 2022) is a sampling-based kinodynamic motion planning algorithm that integrates offline-trained RL policies to improve planning efficiency in high-dimensional spaces [76]. The algorithm augments the SST algorithm in two key ways: (1) it replaces purely random action sampling with a mixture of actions drawn from a random policy, a goal-conditioned policy, and a state-conditioned policy; and (2) it performs gradient descent on sampled states using the learned Q-value function to bias tree growth toward the goal region.

The method trains two sub-optimal policies offline using Soft Actor-Critic with Hindsight Experience Replay, and importantly does not require the policies to be fully converged to be effective. Experiments on 2D kinodynamic planning problems and several Fetch robot arm manipulation tasks (FetchPush, FetchPickAndPlace, FetchSlide) show that PSST significantly outperforms SST, pure RL, and the RL-RRT baseline in terms of success rate and path quality. Notably, PSST shows improvement from training earlier than the policy itself, and remains effective even under distributional shift where the RL agent performs poorly on its own. The method maintains the asymptotic completeness guarantees of SST by retaining a portion of purely random samples.

#### 4.2.2 RRT-RL: Combining RRT with DQN

RRT-RL (Rapidly Exploring Random Trees Reinforcement Learning, Electronics, 2025) combines RRT algorithms with Deep Q-Network (DQN) training to improve sample efficiency in RL, particularly in environments with sparse reward signals [77]. The key innovation is using cosine similarity as a domain-independent distance metric in the RRT algorithm's tree construction, operating on the softmax-normalized Q-vectors from the DQN network. This replaces traditional trial-and-error exploration with systematic state space exploration via RRT, reducing redundant samples.

Evaluated on Cartpole, Acrobot, and Mountain Car, RRT-RL consistently outperforms both standard DQN training and a fixed-buffer baseline approach. In Acrobot, the method achieved superior performance with a quarter of the training samples, and in Mountain Car, with a tenth of the samples. The approach is applicable to any model-free RL method that uses a memory buffer.

#### 4.2.3 RRT-Guided Experience Generation for Autonomous Lane Keeping

This paper (Scientific Reports, 2024) by Tamás Bécsi investigates using RRT to guide experience generation for RL in autonomous lane keeping [78]. The key problem addressed is that standard RL exploration strategies (like ε-greedy) often cover only a narrow portion of the state space, hindering learning, especially in sparse reward environments. By leveraging RRT to broaden the experience pool, the agent can learn a better policy. The classic exploration falls on challenging tracks, reaching the final 250th step once in every eight trials, while the agent trained on the broader pool only fails once out of ten tries.

#### 4.2.4 RRT-LIB: Library of Paths

RRT-LIB (Rapidly-exploring Random Trees with a Library of Paths, Robotics and Autonomous Systems) addresses the narrow passage problem by reusing past planning experiences through a library of precomputed paths [79]. The method stores paths for template objects in a library during a preparation phase, using RRT-IR (RRT with Inhibited Regions) to find multiple distinct paths. In the planning phase, for a new query object, the most similar template object is identified using a genetic algorithm-based shape matching method, and the library paths are transformed accordingly to serve as guiding paths for sampling. Results show speed improvements of up to 85% decrease in required time, with 96–100% success rates in challenging scenarios where other planners fail entirely.

### 4.3 Hierarchical RL for Long-Horizon Trajectory Planning

#### 4.3.1 Motion Planning-Augmented HRL (Kim and Choi, 2026)

This paper proposes a motion planning (MP)-augmented hierarchical reinforcement learning (HRL) architecture for long-horizon mobile manipulation tasks [80]. Three key contributions: (1) SMDP-based hierarchical decomposition chains modular subtasks to reduce long-horizon reward sparsity; (2) MP-guided reward shaping embeds collision-free RRT*-generated trajectories in the full joint configuration space into the RL reward as dense per-step shaping signals, guiding exploration; (3) Region-goal mechanism replaces rigid point-to-point hand-offs with a continuous feasible region derived analytically from inverse kinematics.

Tested in ManiSkill-HAB (MS-HAB) simulation on two long-horizon tasks (TidyHouse and SetTable), the proposed method improved subtask success rates across all six evaluated subtasks, with notable gains of +22 pp in Place and +17 pp in Pick. Convergence speedup reached up to 3× reduction in training steps. The region-goal navigation converged to ~76% success rate vs ~30% for point-goal baseline.

#### 4.3.2 ARCH: Hierarchical Hybrid Learning for Contact-Rich Robotic Assembly

ARCH (Adaptive Robotic Compositional Hierarchy, CoRL) is a hierarchical framework for long-horizon, contact-rich, high-precision robotic assembly [81]. The method combines a low-level primitive library (including both motion planning algorithms and RL policies for skills like grasping and inserting) with a high-level policy (based on a Diffusion Transformer) trained via imitation learning from only 10 demonstrations. The low-level RL primitives are trained in simulation with domain randomization and transferred zero-shot to the real world.

Evaluated on three assembly tasks (FMB Multi-peg Assembly with 9 objects on a real robot, 5-part Beam Assembly, and 9-part Stool Assembly), ARCH achieves success rates of 55% (FMB real), 55% (Beam sim), and 45% (Stool sim), significantly outperforming baselines including E2E RL (0%), E2E IL Diffusion Policy (0%), and MimicPlay (10–20%). Key features include the hybrid MP-RL low-level primitives enabling both efficiency and contact-rich adaptability, and robustness to failures through automatic retry mechanisms.

#### 4.3.3 LARAP: LLMs Augmented HRL with Action Primitives

LARAP (Scientific Reports, 2025) is a framework for solving long-horizon robotic manipulation tasks [82]. The hierarchical agent integrates LLMs with parameterized action primitives. The LLM provides high-level guidance (commonsense priors) to improve sample efficiency, while a set of predefined action primitives (atomic, reach, grasp, push, open) handles low-level control. The framework decomposes tasks into "what" (subtask prediction via RL task policy + LLM guidance) and "how" (action execution via parameterized primitives). Experimental results show LARAP significantly outperforms baseline methods across various simulated manipulation tasks.

#### 4.3.4 Relay Policy Learning (RPL)

Relay Policy Learning (Gupta, Kumar, Lynch, Levine, and Hausman, 2019) is a two-phase method for solving multi-stage, long-horizon robotic manipulation tasks by combining imitation learning with RL fine-tuning [83]. The approach consists of Relay Imitation Learning (RIL), which uses a novel relay data relabeling algorithm to train bi-level hierarchical policies from unstructured, unsegmented human demonstrations, and Relay Reinforcement Fine-tuning (RRF), which improves the policies via goal-conditioned natural policy gradient augmented with demonstration-based maximum likelihood objectives. Evaluated on a simulated 9-DoF Franka robot kitchen manipulation environment with tasks requiring up to 4 sequential steps, RPL significantly outperformed baselines including flat behavior cloning, flat GCBC, and HIRO trained from scratch.

### 4.4 Model-Based RL and Model Predictive Control (MPC)

#### 4.4.1 MB-MPO: Model-Based Meta-Policy-Optimization

MB-MPO (Rothfuss et al., CoRL 2018) combines model-based data efficiency with model-free asymptotic performance [84]. The algorithm learns an ensemble of dynamics models and meta-learns a policy (using MAML) that can quickly adapt to any model in the ensemble with one policy gradient step. The meta-policy internalizes consistent dynamics predictions among the ensemble while shifting the burden of handling model discrepancies to the adaptation step.

Key benefits include a regularization effect where the policy exhibits higher plasticity where model uncertainty is high, tailored data collection exploring regions where models are inaccurate, and fast fine-tuning capability. MB-MPO matches asymptotic performance of model-free methods (DDPG, TRPO, PPO, ACKTR) with 10–100× less data, and outperforms prior model-based methods (ME-TRPO, MB-MPC) in complex tasks. Achieves optimal policy in complex quadrupedal locomotion within ~2 hours of real-world data.

#### 4.4.2 MPC + RL for Quadrotor Guidance

Greatwood and Richards (Autonomous Robots, 2019) present a method for enabling quadrotor MAV navigation in unknown environments using RL and MPC, deployed on embedded hardware (dSpace MicroAutoBox with 900MHz PowerPC processor) [85]. MPC provides vehicle control and obstacle avoidance through online optimization using Fast MPC with soft constraints, operating at 10 Hz. RL (temporal difference learning) guides the MAV through complex environments where dead-end corridors may be encountered, enabling backtracking. RL is used solely for waypoint selection (discrete choice), compensating for the susceptibility of locally convex MPC to explore local minima. Flight tests demonstrated the algorithms perform well with modest computing requirements and robust navigation.

#### 4.4.3 MPC + PPO for Vehicle Parking

This paper (Sensors, 2023) proposes a two-stage automatic vehicle-parking trajectory planning method combining MPC and PPO [86]. Stage 1 uses MPC for trajectory tracking from the initial position to the starting point of the parking operation. Stage 2 employs PPO to transform parking behavior into a learning process, with a four-dimensional reward function evaluating the strategy. The PPO-based method achieves learning times totaling only 30% of DDPG and 37.5% of TD3 algorithms, converging 75% faster than DDPG and 68% faster than TD3.

#### 4.4.4 Model-Based RL for Legged Robots

Yang et al. (CoRL 2020/MLR 2020) present a model-based RL framework for quadruped robot locomotion that achieves walking on a Minitaur robot using only 4.5 minutes of data (45,000 control steps) [87]. Key technical contributions include: a multi-step loss function for training a neural network dynamics model that prevents error accumulation over long prediction horizons, an MPC framework using the Cross Entropy Method (CEM) parallelized on GPU with asynchronous control that compensates for planning latency, and safe exploration via trajectory generators (TGs) that embed prior knowledge of periodic leg trajectories into the action space, preventing actuator damage during learning.

The robot learns to track a desired speed of 0.66 m/s (1.6 body lengths/second) in 36 episodes. The learned dynamics model generalizes zero-shot to unseen tasks (walking backwards, turning) by simply changing the reward function. Compared to model-free methods (PPO, SAC), the approach is more than an order of magnitude more sample efficient.

#### 4.4.5 RL for Reduced-Order Models of Legged Robots

Chen et al. (2024) combine model-based control with RL to learn reduced-order models (ROMs) for bipedal locomotion on the Cassie robot platform [88]. The authors formulate a model-based RL problem where a ROM is learned within an MPC framework. The key innovation is jointly optimizing the ROM and the induced control policy, using the ROM planner as the policy within an RL framework. The optimization uses Covariance Matrix Adaptation Evolutionary Strategy (CMA-ES) with curriculum learning. Results demonstrate a 49% improvement in viable task region size and a 21% reduction in motor torque cost compared to the Linear Inverted Pendulum Model (LIP) baseline.

#### 4.4.6 CACTO: Continuous Actor Critic with Trajectory Optimization

CACTO (Grandesso, PhD thesis, University of Trento) combines RL and Trajectory Optimization to address the non-convexity of co-design optimization problems [89]. It addresses two main limitations: trajectory optimization can get stuck in poor local minima when not initialized close to a "good" minimum, and RL training can be excessively long and dependent on exploration strategy. The algorithm learns a "good" control policy via TO-guided RL policy search, which then provides an initial guess for TO to avoid poor local optima. Validated on several reaching problems with non-convex obstacle avoidance, showing better computational efficiency than DDPG and PPO.

### 4.5 Inverse Reinforcement Learning for Trajectory Planning

#### 4.5.1 CIIRL: Goal-Oriented Navigation for Social Robots

This paper (Scientific Reports, 2025) presents a Goal-Oriented Autonomous Decision-Making (GO-ADM) method for social robots navigating pedestrian environments [90]. The authors propose a Collaborative Interactive Inverse Reinforcement Learning (CIIRL) framework that learns from Goal-Oriented Expert Demonstrations derived from the seq-eth dataset. The methodology involves defining goal-oriented expert demonstrations that include goal information, developing a training environment with 15 dynamic pedestrians, using maximum entropy deep inverse reinforcement learning to learn reward functions, and integrating social safety constraints via penalty functions.

Under longitudinal dominant navigation tasks, the robot's final average deviation from destination was less than 0.13 m (deviation rate less than 0.18%). Under lateral dominant navigation tasks, deviation was less than 0.23 m (deviation rate less than 1.1%). GO-ADM achieved higher success rates than other social navigation algorithms, and with maximum noise of 0.5 m, the success rate exceeded 75%.

#### 4.5.2 IRL-TP for UAV Trajectory Planning

IRL-TP (Computers, Materials and Continua, 2026) is a framework for UAV trajectory planning in complex and interference-constrained environments using deep inverse reinforcement learning [91]. A deep reward network is constructed to parametrize the unknown reward function, implicitly modeling multiple objectives such as flight safety, collision avoidance, trajectory smoothness, and navigation efficiency. Entropy regularization through the learned reward function is used to optimize continuous control policy with a soft actor-critic (SAC) agent.

Key results include a 97.6% success rate in dense obstacle environments, instability metric as low as 0.044, convergence in ~340 episodes (much faster than other methods), and inference time of 2.6 ms per step. Superior performance is demonstrated compared to DQN, PPO, SAC, BC, and GAIL in trajectory efficiency, safety margins, motion smoothness, and training stability.

#### 4.5.3 Gradient-Based IRL with TD-MPC for Robotic Manipulation

This paper presents a gradient-based IRL framework for robotic arm manipulation that learns cost functions purely from visual human demonstrations [92]. The system uses keypoint detectors to extract low-dimensional visual features from RGB images, a pre-trained dynamics model to predict action outcomes in that feature space, and TD-MPC (Temporal-Difference Model Predictive Control) for action optimization. The key innovation is differentiating through the inner optimization step to enable stable and efficient learning of cost functions via gradient-based bi-level optimization. Experiments using a simulated Franka Emika Panda arm in PyBullet performing a pick-and-place task show decreasing loss and increasing reward as training progresses, with the arm successfully performing the task with good generalizability.

#### 4.5.4 GraphIRL: Learning from Diverse Videos

GraphIRL (Kumar et al., CoRL 2022) is a method for learning reward functions from diverse third-person video demonstrations via graph abstraction [93]. The key insight is that tasks can be described by entity interactions forming a graph, which helps remove irrelevant visual information while preserving task-relevant spatial relationships. On the X-MAGICAL benchmark, GraphIRL significantly outperforms vision-based baselines (XIRL, TCN, LIFS) in cross-embodiment cross-environment settings. In real robot experiments, GraphIRL outperforms XIRL in all three tasks (Reach: 0.86 vs 0.26, Push: 0.60 vs 0.27, Peg in Box: 0.53 vs 0.06).

#### 4.5.5 IRL for Autonomous Navigation via Semantic Mapping

This paper (Autonomous Robots, 2023) presents an IRL approach for autonomous navigation that uses distance and semantic category observations to infer a cost function from expert demonstrations [94]. The model has two main components: a map encoder that infers semantic category probabilities from observation sequences, and a cost encoder defined as a deep neural network over semantic features. The approach allows learned behavior to generalize to new environments with different spatial configurations of semantic categories. The method is demonstrated to learn traffic rules in the CARLA autonomous driving simulator by relying on semantic observations of buildings, sidewalks, and road lanes.

### 4.6 Safe Exploration for Autonomous Driving

#### 4.6.1 Plan-R1: Safe and Feasible Trajectory Planning (ICLR 2026)

Plan-R1 is a two-stage trajectory planning framework for autonomous driving that decouples principle alignment from behavior learning [95]. Stage 1 (Pre-training) trains a general trajectory predictor on expert driving data (nuPlan dataset) using next-motion-token prediction to capture diverse, human-like driving behaviors. Stage 2 (Fine-tuning) fine-tunes the model with rule-based rewards using Group Relative Policy Optimization (GRPO) to explicitly align ego planning with safety, comfort, and traffic rule compliance.

A key technical contribution is the identification of a limitation of standard GRPO in planning: group-wise normalization erases cross-group scale differences, causing rare safety-violation groups to have similar advantages as abundant safe groups, suppressing optimization for safety-critical objectives. The proposed Variance-Decoupled GRPO (VD-GRPO) replaces normalization with centering and fixed scaling to preserve absolute reward magnitudes, ensuring safety-critical objectives remain dominant.

On the nuPlan benchmark, Plan-R1 achieves state-of-the-art performance, particularly in realistic reactive settings. On Val14, it achieves 88.98 NR-CLS and 87.69 R-CLS (without post-processing), and 94.72/93.54 with post-processing. It surpasses Diffusion Planner by +4.89, +7.98, and +7.11 points on reactive settings across Val14, Test14-hard, and Test14-random splits. VD-GRPO reduces unsafe group ratio from 6.7% to 4.7% (29.8% reduction).

#### 4.6.2 COX-Q: Constrained Optimistic Exploration (ICLR 2026)

COX-Q (Constrained Optimistic eXploration Q-learning) is an off-policy safe RL algorithm that integrates cost-bounded online exploration and conservative offline distributional value learning [96]. COX-Q integrates two main components: Cost-Constrained Optimistic Exploration (COX) that extends Optimistic Actor-Critic (OAC) to multi-objective safe RL, using Policy-MGDA to resolve gradient conflicts between reward and cost in the action space, and Truncated Quantile Critics (TQC) that uses distributional value learning with truncated quantile critics to stabilize cost value learning.

Evaluated on Safe Velocity (4 robot locomotion tasks), Safe Navigation (5 tasks), and SMARTS safe autonomous driving (3 scenarios), COX-Q demonstrates superior sample efficiency over on-policy baselines (CUP, RCPO, PPOSimmerPID, CPPOPID) and better safety performance than off-policy baselines (SACLag-UCB, CAL, WCSAC, ORAC). The autonomous driving experiments demonstrate COX-Q achieves the best safety performance with minimal timeouts and collisions.

#### 4.6.3 SafeHIL-RL: Safety-Aware Human-in-the-Loop RL

This paper presents a safety-aware human-in-the-loop RL approach for autonomous driving [97]. Key contributions include a Frenet-based Dynamic Potential Field (FDPF) safety assessment module, a Curriculum Guidance Mechanism with three phases (Continual guidance, Intermittent guidance, and Self-learning), and Dynamic Control Authority Allocation based on FDPF safety assessment. The method is validated in two highway scenarios under dense traffic flows using the SMARTS platform, achieving 71.52% efficiency improvement over PHIL-RL, 28.38% improvement over HIRL, 80.76% improvement over SAC, and 100% success rate in testing (vs. 70% for PHIL-RL, 90% for HIRL, 75% for SAC).

#### 4.6.4 Contingency-Aware NMPC for Lane Changing

This paper presents a contingency-aware spatiotemporal optimization framework for autonomous vehicle lane changing that integrates dynamic risk assessment and trajectory optimization [98]. The framework consists of a Dynamic Risk Field (DRF) method, a spatiotemporal safety corridor construction scheme, and a contingency-aware Nonlinear Model Predictive Control (NMPC) framework that incorporates prediction uncertainty of surrounding vehicles. Results demonstrate up to 95% reductions in longitudinal and lateral accelerations, a 27% decrease in lane-changing time (4.84s vs 6.63s for baselines), smoother trajectories, improved stability, and enhanced safety margins.

### 4.7 Applications to Legged Locomotion

#### 4.7.1 Adaptive Motion Planning for Quadrupedal Robots

This paper (Scientific Reports, 2026) uses DRL with curriculum learning, achieving 94.6% success in Webots and 91.2% in PyBullet, and recovering from external pushes within 1.6 seconds [99].

#### 4.7.2 DRL for Bipedal Locomotion Survey

A comprehensive survey (Artificial Intelligence Review, 2026) categorizes end-to-end and hierarchical frameworks for bipedal locomotion, noting the first successful sim-to-real transfer on Cassie in 2020 [100]. The survey identifies that a unified framework for DRL-based bipedal locomotion with standardized benchmarks remains far from being realized.

### 4.8 Theoretical Connections

#### 4.8.1 Exploration Bonuses as Shaping Rewards

The connection between exploration bonuses in RL and cost functions in trajectory optimization can be understood through several mechanisms:

- **MP-guided reward shaping** (Kim and Choi, 2026): Collision-free RRT*-generated trajectories are embedded directly into the RL reward function as dense per-step shaping signals, creating a direct bridge between the cost function used in the sampling-based planner (optimizing for path length, collision avoidance) and the exploration bonus serving as a curriculum [80].

- **Curiosity as exploration bonus** (Frank et al., 2014): The artificial curiosity reward computed as KL divergence between updated and previous state transition distributions serves as an intrinsic motivation signal that naturally focuses exploration on "interesting" state-actions that encounter constraints—exactly the regions where trajectory optimization would benefit from denser sampling [74].

- **Plan-R1's rule-based rewards**: The GRPO fine-tuning uses rule-based rewards that explicitly encode safety, comfort, and traffic rule compliance as reward components, with Variance-Decoupled GRPO preserving absolute reward magnitudes to ensure safety-critical objectives remain dominant [95].

- **Safe exploration cost functions** (COX-Q, 2026): The cost-constrained optimistic exploration strategy resolves gradient conflicts between reward and cost in the action space, creating a direct algorithmic bridge between the exploration bonus and the cost function [96].

#### 4.8.2 Duality of Exploration and Trajectory Optimization

In trajectory optimization, the objective is typically to minimize a cost function subject to dynamics constraints. In RL exploration, the objective is to maximize information gain or reduce uncertainty. These are fundamentally dual objectives—the trajectory planner seeks the best path given current knowledge, while the explorer seeks to improve the knowledge itself.

The KL divergence-based artificial curiosity used by Frank et al. (2014) provides a principled objective for exploration that can be formalized as maximizing the information gain about the system dynamics. This connects to trajectory optimization through the concept of "interesting" regions—state-action pairs where the dynamics are non-deterministic or non-linear require denser sampling for accurate modeling, which is analogous to the need for denser trajectory optimization in regions with high curvature or constraints.

The Generalized Safe Exploration (GSE) problem provides a unified formulation that encompasses cumulative constraints, state constraints, and instantaneous constraints, proving that these three safe RL problem types can be transformed into a single formulation [62]. This provides a theoretical framework for understanding how safety constraints in trajectory optimization (collision avoidance, actuator limits) map to constraints in RL exploration.

#### 4.8.3 Asymptotic Completeness of Hybrid Methods

PSST maintains the asymptotic completeness guarantees of SST by retaining a portion of purely random samples, providing a theoretical bridge between the probabilistic completeness of sampling-based planners and the convergence guarantees of RL [76]. This is a crucial insight: hybrid methods can preserve the formal guarantees of classical planning approaches while benefiting from the data-driven adaptation of RL.

### 4.9 Key Open Challenges and Future Directions

#### 4.9.1 Safety Guarantees for ML-Based Models

Multiple sources emphasize that ML-based models may not guarantee safety; therefore, they should be combined with explicit safety constraints [101]. The dynamic nature of real-world traffic, high computational costs, and diversity of road design make designing, testing, and validating safe RL algorithms difficult [102].

#### 4.9.2 Sample Efficiency

Model-free RL with high-dimensional inputs remains sample-inefficient, particularly in scenarios where rewards are sparse and goals are difficult to explore [103]. While model-based approaches improve sample efficiency, they struggle with model accuracy and bias [84].

#### 4.9.3 Reward Function Design

Designing effective reward functions that balance exploration and exploitation, multiple objectives (safety, efficiency, comfort), and avoid reward hacking remains a key challenge [101][104]. The need for manual cost function design in safe RL is a significant limitation [105].

#### 4.9.4 Scalability of Hybrid Methods

As the symbolic domain grows in hybrid planning-learning systems, planning costs increase and learning slows down [75]. CSP's capabilities are constrained by available macro-actions [73]. Scalability challenges in hierarchical RL include inefficient training and poor transferability [82].

#### 4.9.5 Sim-to-Real Transfer

Simulation-to-real-world transfer gaps remain a major challenge, including sensor noise, safety concerns, and partial observability [78][100]. While domain randomization helps, it does not fully bridge the gap.

#### 4.9.6 Standardized Benchmarks

The need for standardized evaluation benchmarks and simulation-to-real adaptation strategies is highlighted across multiple domains [101][100].

#### 4.9.7 Future Research Directions

Key future directions identified across the literature include:

- **Combining heuristics with DRL**: Hybrid models leveraging domain-specific knowledge alongside adaptive capabilities represent a promising direction [78]. This includes integrating RL with classical sampling-based planners, MPC, and safety layers [101].

- **Integrated designs combining RL with safety layers**: Findings highlight the need for integrated designs combining RL with safety layers (e.g., MPC/CBFs), cooperative multi-agent decision-making, and explainable mechanisms [101].

- **Uncertainty/density estimation**: Future work should incorporate uncertainty/density estimation in hybrid planning-learning approaches [103].

- **Multiple sensor modalities**: Incorporating multiple sensor modalities for richer state representations [103].

- **Online exploration**: Developing online exploration methods that can adapt to changing environments without retraining [103].

- **Prior knowledge/pretrained models**: Leveraging prior knowledge and pretrained models (including foundation models and LLMs) to bootstrap exploration [82][103].

- **Formal safety guarantees**: Addressing key challenges such as interpretability, formal safety guarantees, and robustness against adversarial disruptions for real-world deployment [78].

- **Language-guided exploration**: Integrating natural language for task specification and exploration guidance [105][106].

- **Scalable symbolic planning**: Developing more scalable approaches for hybrid symbolic-neural planning systems [75].

---

## 5. Conclusion

The past decade has witnessed remarkable progress in reinforcement learning exploration methods, with two parallel tracks—sparse reward exploration and constrained exploration—converging toward practical solutions for trajectory planning problems. The key developments can be summarized as follows:

On the sparse reward front, intrinsic motivation methods have evolved from simple prediction error (ICM) to principled information gain (RND, BYOL-Explore, RFIG) and structured exploration (Go-Explore, NGU, Agent57). The recognition that the primary bottleneck in hard exploration is not sophisticated action selection but rather the ability to systematically build upon previous discoveries (Go-Explore) has been transformative. Hierarchical methods (HIDIO, UOS, GEAPS) and unsupervised skill discovery (METRA, DiMS, CSD) have shown that learning reusable behaviors without task rewards can dramatically accelerate downstream learning.

On the constrained exploration front, the field has moved from simple Lagrangian penalties to sophisticated methods that provide formal guarantees. Trust region methods (CPO, PCPO, FOCOPS, CUP, CSPO, C-TRPO) offer theoretical safety guarantees during optimization. Shielding and safety critics provide runtime safety guarantees. Lyapunov-based methods and control barrier functions integrate classical control theory with RL. Model-based methods (CAP, SMBPO, CMBPO, SBSRL) offer dramatic sample efficiency improvements. Extreme value methods (EVO) address the critical challenge of rare catastrophic events. Formal verification methods (VSRL, VELM) provide the strongest possible safety guarantees.

The implications for trajectory planning are profound and multifaceted. Curiosity-driven exploration can guide sampling-based planners toward informative regions of configuration space (CSP, PSST, RRT-RL). Hierarchical RL can decompose long-horizon planning problems into manageable subproblems (ARCH, LARAP, RPL). Model-based RL can accelerate trajectory optimization and MPC (MB-MPO, CEM, CACTO). Inverse RL can learn reward functions from demonstrations for trajectory planning. Safe exploration methods provide the theoretical foundation for ensuring that trajectory planning algorithms satisfy safety constraints during both learning and deployment.

The integration of these methods with classical trajectory planning approaches—RRT, PRM, MPC, trajectory optimization—represents a particularly promising direction. Hybrid methods that preserve the formal guarantees of classical approaches (asymptotic completeness, safety certificates) while benefiting from the data-driven adaptation of RL are likely to be the most impactful for real-world applications.

Key challenges remain, including sample efficiency, safety guarantees for learned models, reward function design, scalability of hierarchical methods, and sim-to-real transfer. However, the trajectory of research suggests that RL-based exploration methods will increasingly become standard tools in the trajectory planning toolkit, particularly for problems involving long horizons, sparse feedback, and critical safety constraints.

---

## Sources

[1] Coding Curiosity: Intrinsic Motivation Tutorial (2025): https://robocloud-dashboard.vercel.app/learn/blog/curiosity-exploration

[2] Curiosity-driven Exploration by Self-supervised Prediction: https://pathak22.github.io/noreward-rl

[3] Exploration by Random Network Distillation: https://iclr.cc/virtual/2019/poster/1093

[4] Exploration and Anti-Exploration with Distributional Random Network Distillation: https://icml.cc/virtual/2024/poster/32960

[5] BYOL-Explore: Exploration by Bootstrapped Prediction: https://arxiv.org/abs/2206.08332

[6] The impact of intrinsic rewards on exploration in Reinforcement Learning: https://link.springer.com/article/10.1007/s00521-025-11340-0

[7] Go-Explore: a New Approach for Hard-Exploration Problems: https://www.alphaxiv.org/paper/1901.10995

[8] Intelligent Go-Explore: https://proceedings.iclr.cc/paper_files/paper/2025/hash/369a30aac2765950865efd318cef7f76-Abstract-Conference.html

[9] Go-Explore Framework in RL: https://www.emergentmind.com/topics/go-explore-framework

[10] Curiosity-driven Exploration in Sparse-reward Multi-agent Reinforcement Learning: https://www.semanticscholar.org/paper/Curiosity-driven-Exploration-in-Sparse-reward-Li-Gajane/7aaf8f4a37f4af88e75509f0f01f5aee0ec9d851

[11] Hindsight Experience Replay: https://www.alphaxiv.org/abs/1707.01495

[12] Hindsight Experience Replay (Emergent Mind): https://www.emergentmind.com/topics/hindsight-experience-replay

[13] DHER: Hindsight Experience Replay for Dynamic Goals: https://iclr.cc/virtual/2019/poster/775

[14] Improving Option Learning with Hindsight Experience Replay: https://ala-workshop.github.io/papers/ALA2025_paper_7.pdf

[15] Enabling Option Learning in Sparse Rewards with Hindsight Experience Replay: https://arxiv.org/html/2602.13865v1

[16] Hierarchical reinforcement learning with unlimited option scheduling for sparse rewards in continuous spaces: https://www.sciencedirect.com/science/article/abs/pii/S0957417423019693

[17] Goal exploration augmentation via pre-trained skills for sparse-reward long-horizon goal-conditioned reinforcement learning: https://link.springer.com/article/10.1007/s10994-023-06503-w

[18] Hierarchical Reinforcement Learning by Discovering Intrinsic Options: https://iclr.cc/virtual/2021/poster/2805

[19] Exploring the limits of hierarchical world models in reinforcement learning: https://www.nature.com/articles/s41598-024-76719-w

[20] Unsupervised Skill Discovery in RL: https://www.emergentmind.com/topics/unsupervised-skill-discovery-usd

[21] Controllability-aware Skill Discovery: https://seohong.me/projects/csd

[22] METRA: Scalable Unsupervised RL with Metric-Aware Abstraction: https://proceedings.iclr.cc/paper_files/paper/2024/file/516593a423838642a2eb4e9c5b9c7f44-Paper-Conference.pdf

[23] Discovery of Mixture Skills for Unsupervised Reinforcement Learning: https://ojs.aaai.org/index.php/AAAI/article/view/39606/43567

[24] Exploration Strategies in Deep Reinforcement Learning: https://lilianweng.github.io/posts/2020-06-07-exploration-drl

[25] Information-Theoretic Intrinsic Motivation for Reinforcement Learning in Combinatorial Routing: https://www.mdpi.com/1099-4300/28/2/140

[26] Information-Based Exploration via Random Features for Reinforcement Learning: https://arxiv.org/html/2607.17981v1

[27] Never Give Up: Learning Directed Exploration Strategies: https://www.semanticscholar.org/paper/Never-Give-Up%3A-Learning-Directed-Exploration-Badia-Sprechmann/086159600bede14e00f96043c733d4f3b45855aa

[28] Agent57: Outperforming the Atari Human Benchmark: https://proceedings.mlr.press/v119/badia20a/badia20a.pdf

[29] Stanford CS224R Deep Reinforcement Learning, Lecture 13: Meta RL: https://www.youtube.com/watch?v=wSiyEpvoGkA

[30] Exploring Meta-learned Curiosity Algorithms: https://iclr-blogposts.github.io/2024/blog/exploring-meta-learned-curiosity-algorithms

[31] Meta-RL Induces Exploration in Language Agents: https://arxiv.org/html/2512.16848v2

[32] Awesome Exploration Methods in Reinforcement Learning: https://github.com/opendilab/awesome-exploration-rl

[33] Safe MDP Exploration Techniques: https://www.emergentmind.com/topics/safe-mdp-exploration

[34] A Survey of Safe Reinforcement Learning and Constrained MDPs: https://arxiv.org/html/2505.17342v2

[35] Constrained Policy Optimization: http://bair.berkeley.edu/blog/2017/07/06/cpo

[36] PCPO (Projection-Based Constrained Policy Optimization): https://sites.google.com/view/iclr2020-pcpo

[37] First Order Constrained Optimization in Policy Space: https://proceedings.neurips.cc/paper/2020/file/af5d5ef24881f3c3049a7b9bfe74d58b-Paper.pdf

[38] Constrained Update Projection Approach to Safe Policy Optimization: https://proceedings.neurips.cc/paper_files/paper/2022/file/3ba7560b4c3e66d760fbdd472cf4a5a9-Paper-Conference.pdf

[39] CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning: https://icml.cc/virtual/2026/poster/66410

[40] Embedding Safety into RL: A New Take on Trust Region Methods: https://icml.cc/virtual/2025/poster/46451

[41] Responsive Safety in Reinforcement Learning by PID Lagrangian Methods: https://arxiv.org/abs/2007.03964

[42] Adaptive Reward Penalty in Safe Reinforcement Learning: https://iclr-blogposts.github.io/staging/blog/2023/Adaptive-Reward-Penalty-in-Safe-Reinforcement-Learning

[43] Conservative Safety Critics for Exploration: https://www.semanticscholar.org/paper/Conservative-Safety-Critics-for-Exploration-Bharadhwaj-Kumar/a334f9897a330abddf99cfec0b5a70f751e9497b

[44] Safe Reinforcement Learning via Shielding: https://www.emergentmind.com/topics/safe-reinforcement-learning-via-shielding

[45] Safe Reinforcement Learning Using Advantage-Based Intervention: https://homes.cs.washington.edu/~bboots/files/SAILR.pdf

[46] Approximate Model-Based Shielding for Safe Reinforcement Learning: https://spiral.imperial.ac.uk/server/api/core/bitstreams/f848067c-3129-47b0-af2d-5b5fe8e70623/content

[47] Reducing Safety Interventions in Provably Safe Reinforcement Learning: https://mediatum.ub.tum.de/doc/1721595/umf5arlbi5kx1ryog4r0gtok4.root.pdf

[48] A Lyapunov-based Approach to Safe Reinforcement Learning: https://mohammadghavamzadeh.github.io/PUBLICATIONS/nips18-safety.pdf

[49] Lyapunov-Assisted Deep Reinforcement Learning: https://www.emergentmind.com/topics/lyapunov-assisted-deep-reinforcement-learning-drl

[50] End-to-End Safe Reinforcement Learning through Barrier Functions for Safety-Critical Continuous Control Tasks: https://websites.umich.edu/~orosz/articles/AAAI_2019_Richard_Richard_Joel.pdf

[51] Reachability Constrained Reinforcement Learning: https://proceedings.mlr.press/v162/yu22d/yu22d.pdf

[52] Safe Reinforcement Learning Using Black-Box Reachability Analysis: https://arxiv.org/html/2204.07417v2

[53] Safe Reinforcement Learning for Robotics: From Exploration to Policy Learning: https://tuprints.ulb.tu-darmstadt.de/entities/publication/fa9e8410-854c-4549-bfc4-1d4a6b1f83e3

[54] Conservative and Adaptive Penalty for Model-Based Safe Reinforcement Learning: https://cdn.aaai.org/ojs/20478/20478-13-24491-1-2-20220628.pdf

[55] Safe Reinforcement Learning by Imagining the Near Future: https://proceedings.neurips.cc/paper/2021/file/73b277c11266681122132d024f53a75b-Paper.pdf

[56] Safe Continuous Control with Constrained Model-Based Policy Optimization: https://arxiv.org/pdf/2104.06922

[57] Sampling-Based Safe Reinforcement Learning: https://arxiv.org/html/2605.19469v1

[58] Offline Recovery RL: https://bcommons.berkeley.edu/offline-recovery-rl-offline-reinforcement-learning-safe-online-adaptation

[59] Safe Exploration in Reinforcement Learning: Training Backup Control Barrier Functions with Zero Training-Time Safety Violations: https://proceedings.mlr.press/v283/rabiee25a.html

[60] Safe Exploration via Policy Priors: https://neurips.cc/virtual/2025/136104

[61] Almost Surely Safe Exploration and Exploitation for Deep Reinforcement Learning with State Safety Estimation: https://www.sciencedirect.com/science/article/abs/pii/S0020025524001749

[62] Safe Exploration in Reinforcement Learning: A Generalized Formulation and Algorithms: https://arxiv.org/pdf/2310.03225

[63] Extreme Value Policy Optimization for Safe Reinforcement Learning: https://icml.cc/virtual/2025/poster/46527

[64] Efficient Exploration in Resource-Restricted Reinforcement Learning: https://ojs.aaai.org/index.php/AAAI/article/view/26224/25996

[65] Enhancing Efficiency of Safe Reinforcement Learning via Sample Manipulation: https://proceedings.neurips.cc/paper_files/paper/2024/file/1ef130b8249625e47ef96a7b27464845-Paper-Conference.pdf

[66] Reinforcement Learning by Guided Safe Exploration: https://tdsimao.github.io/assets/pdf/Yang2023reinforcement.pdf

[67] Offline-to-Online Reinforcement Learning: https://www.emergentmind.com/topics/offline-to-online-reinforcement-learning-o2o-rl-3a8a0a94-9168-4be4-a93a-63e8967e2b1b

[68] Verified Safe Reinforcement Learning for Neural Network Dynamic Models: https://neurips.cc/virtual/2024/poster/93347

[69] Provably Safe Reinforcement Learning with Step-wise Violation Constraints: https://proceedings.neurips.cc/paper_files/paper/2023/file/aa3e67220ca4cd50010165c950fc8056-Paper-Conference.pdf

[70] Safe Exploration in Reinforcement Learning by Reachability Analysis over Learned Models: https://link.springer.com/chapter/10.1007/978-3-031-65633-0_11

[71] Penalty-Based Reward Shaping in RL: https://www.emergentmind.com/topics/penalty-based-reward-shaping

[72] Exploration-Guided Reward Shaping for Reinforcement Learning: https://proceedings.neurips.cc/paper_files/paper/2022/file/266c0f191b04cbbbe529016d0edc847e-Supplemental-Conference.pdf

[73] Curious Sample Planner: http://proceedings.mlr.press/v119/curtis20a/curtis20a.pdf

[74] Curiosity driven reinforcement learning for motion planning on humanoids: https://www.frontiersin.org/journals/neurorobotics/articles/10.3389/fnbot.2013.00025/full

[75] Curiosity-Driven Imagination: Discovering Plan Operators and Learning Associated Policies for Open-World Adaptation: https://arxiv.org/html/2503.04931v1

[76] Learning-Guided Exploration for Efficient Sampling-Based Motion Planning: http://rl.cs.rutgers.edu/publications/LiamICRA2022.pdf

[77] Rapidly Exploring Random Trees Reinforcement Learning: https://www.mdpi.com/2079-9292/14/3/443

[78] RRT-guided experience generation for reinforcement learning in autonomous lane keeping: https://www.nature.com/articles/s41598-024-73881-z

[79] Enhancing Sampling-based Planning with a Library of Paths: https://arxiv.org/html/2510.12962v1

[80] Motion Planning-Augmented Hierarchical Reinforcement Learning for Long-Horizon Mobile Manipulation: https://www.mdpi.com/1424-8220/26/12/3845

[81] ARCH: Hierarchical Hybrid Learning for Long-Horizon Contact-Rich Robotic Assembly: https://www.research.autodesk.com/publications/arch-hierarchical-hybrid-learning-for-robotic-assembly

[82] LLMs augmented hierarchical reinforcement learning with action primitives for long-horizon manipulation tasks: https://www.nature.com/articles/s41598-025-20653-y

[83] Relay Policy Learning: https://relay-policy-learning.github.io

[84] Model-Based Reinforcement Learning via Meta-Policy-Optimization: https://h2t.iar.kit.edu/pdf/Rothfuss2018.pdf

[85] Reinforcement learning and model predictive control for robust embedded quadrotor guidance and control: https://link.springer.com/article/10.1007/s10514-019-09829-4

[86] Model-Based Predictive Control and Reinforcement Learning for Planning Vehicle-Parking Trajectories: https://www.mdpi.com/1424-8220/23/16/7124

[87] Data Efficient Reinforcement Learning for Legged Robots: https://proceedings.mlr.press/v100/yang20a/yang20a.pdf

[88] Reinforcement Learning for Reduced-order Models of Legged Robots: https://dair.seas.upenn.edu/assets/pdf/Chen2024.pdf

[89] CACTO: Reinforcement Learning and Trajectory Optimization for the Concurrent Design of High-Performance Robotic Systems: https://tesidottorato.depositolegale.it/bitstream/20.500.14242/93894/1/phd_unitn_Gianluigi_Grandesso.pdf

[90] Goal-oriented autonomous decision-making for social robots via collaborative interactive inverse reinforcement learning: https://www.nature.com/articles/s41598-025-11412-0

[91] IRL-TP: Deep Inverse Reinforcement Learning-Based Trajectory Planning for UAVs: https://www.sciencedirect.com/org/science/article/pii/S1546221826005229

[92] Robotic Arm Manipulation with Inverse Reinforcement Learning & TD-MPC: https://arxiv.org/html/2407.12941v1

[93] Graph Inverse Reinforcement Learning from Diverse Videos: https://proceedings.mlr.press/v205/kumar23a/kumar23a.pdf

[94] Inverse reinforcement learning for autonomous navigation via differentiable semantic mapping and planning: https://link.springer.com/article/10.1007/s10514-023-10118-4

[95] Plan-R1: Safe and Feasible Trajectory Planning: https://proceedings.iclr.cc/paper_files/paper/2026/file/28a80012e6f564c0cc8e7661e1db83fe-Paper-Conference.pdf

[96] Off-Policy Safe Reinforcement Learning with Constrained Optimistic Exploration: https://openreview.net/pdf/36111b7869598bcb726c1a06858a8fe3cf31cab5.pdf

[97] Safety-aware human-in-the-loop reinforcement learning with curriculum guidance: https://dr.ntu.edu.sg/bitstreams/91e13b6e-e5f8-46c5-b8cf-f82ffe1bf90f/download

[98] Contingency-Aware Spatiotemporal Optimization for Safe Lane Changing: https://eprints.gla.ac.uk/361957/2/361957.pdf

[99] Adaptive motion planning for legged robots in unstructured terrain using deep reinforcement learning: https://www.nature.com/articles/s41598-025-34956-7

[100] Deep reinforcement learning for robotic bipedal locomotion: a brief survey: https://link.springer.com/article/10.1007/s10462-025-11451-z

[101] Reinforcement Learning for Lane-Changing Decision Making in Autonomous Vehicles: A Survey: https://www.mdpi.com/2624-6511/9/1/9

[102] A comprehensive review on safe reinforcement learning for autonomous vehicle control in dynamic environments: https://www.sciencedirect.com/science/article/pii/S2772671124003905

[103] Synergies between Policy Learning and Sampling-based Planning: https://kth.diva-portal.org/smash/get/diva2:1824523/FULLTEXT01.pdf

[104] Comprehensive Overview of Reward Engineering and Shaping in Advancing Reinforcement Learning Applications: https://arxiv.org/html/2408.10215v1

[105] From Text to Trajectory: Exploring Complex Constraint Representation: https://proceedings.neurips.cc/paper_files/paper/2024/file/e356ed5f27885c79c7cb597bb1107c94-Paper-Conference.pdf

[106] Intrinsic Motivation Exploration: https://www.emergentmind.com/topics/intrinsic-motivation-exploration
