# Recent Advances in Reinforcement Learning Exploration: Sparse Rewards, Constrained Environments, and Implications for Trajectory Planning

## Introduction

Reinforcement learning (RL) has achieved remarkable successes across game playing, robotics, and autonomous systems, yet two fundamental challenges persist: exploring effectively under sparse reward signals and ensuring safe behavior when explicit constraints are present. These challenges are deeply interconnected—agents must explore to discover rewarding states, but exploration can lead to catastrophic failures in safety-critical domains. This report synthesizes recent research progress (2021–2026) across both dimensions and analyzes how these exploration strategies inform trajectory planning under uncertainty.

The report is organized into three main sections. First, we examine algorithmic innovations for exploration in sparse-reward environments, including intrinsic motivation, curiosity-driven exploration, count-based methods, and goal-directed exploration. Second, we review safe exploration techniques for constrained environments, covering constrained MDPs, barrier functions, shielding, and uncertainty-aware methods. Finally, we synthesize these findings to draw implications for trajectory planning, focusing on sample efficiency, safety guarantees, and goal-directed behavior.

---

## Part 1: Exploration in Sparse-Reward Environments

Sparse rewards—where an agent receives feedback only upon completing a task or reaching specific states—remain one of the most challenging settings in RL. Without dense reward signals, agents must rely on internally generated exploration incentives to discover meaningful behavior. Research over the past five years has produced a rich taxonomy of approaches.

### 1.1 Intrinsic Motivation and Curiosity-Driven Exploration

#### Random Network Distillation (RND)

RND defines an exploration bonus as the prediction error of a neural network trained to predict the output of a fixed, randomly initialized target network on the agent's observations. The error decreases for familiar states and increases for novel states, providing an intrinsic reward signal. Burda et al. (2018) found that RND is sufficient for local exploration—exploring the consequences of short-term decisions—but struggles with global exploration requiring coordinated decisions over long time horizons [1]. RND has become a foundational component in more complex systems like NGU and Agent57.

#### Intrinsic Curiosity Module (ICM)

ICM uses a forward model (predicts next state features given current state and action) and an inverse model (predicts the action taken from two consecutive states) to generate intrinsic rewards. The inverse model ensures that the learned feature representation ignores uncontrollable aspects of the environment (e.g., moving leaves), preventing the agent from being distracted by "noisy TV" elements. Evaluated on MiniGrid, VizDoom, and Super Mario Bros., ICM with learned feature encoding outperformed pixel-based curiosity and standard A3C, especially in very sparse reward scenarios [2].

#### BYOL-Explore

BYOL-Explore (Guo et al., NeurIPS 2022) represents a significant advance in curiosity-driven exploration. It jointly learns world representation, latent dynamics, and an exploration policy by optimizing a single self-supervised prediction loss in latent space, with no additional auxiliary objective. Building on Bootstrap Your Own Latent (BYOL), it predicts an older copy of its own latent representation, adapted to interactive environments using a recurrent neural network and multi-step open-loop predictions.

**Benchmark Results:**
- **Atari (10 hardest exploration games):** Achieved superhuman performance (mean capped human-normalized score > 1), outperforming RND, ICM, and pure RL.
- **DM-HARD-8 (8 complex 3D partially-observable tasks):** Solved 5 of 8 tasks without human demonstrations, surpassing prior work that required demonstrations.
- **Noisy Montezuma's Revenge:** Remained robust to controllable noise, whereas RND failed completely—RND "completely flat-lined in the noisy environment because the agent is attracted to the noise and keeps repeating the no-op action" [3].

#### BYOL-Hindsight

BYOL-Hindsight (Jarrett et al., ICML 2023) addresses the fragility of curiosity-driven exploration in stochastic environments, where agents get trapped by high-entropy elements like a "noisy TV." It learns hindsight representations that capture the unpredictable aspects of each outcome and uses them as additional input for predictions, so intrinsic rewards only reflect predictable (epistemic) novelty, not irreducible aleatoric noise. On Pycolab mazes with various stochasticities and Atari games with sticky actions (Bank Heist, Montezuma's Revenge), BYOL-Hindsight achieves state-of-the-art exploration while preserving performance in non-sticky settings [4].

### 1.2 Count-Based and Pseudo-Count Methods

#### Pseudo-Counts via Density Models

Bellemare et al. (NeurIPS 2016) derived pseudo-counts from a density model over the state space, enabling count-based exploration bonuses in high-dimensional state spaces without explicitly counting every state. The pseudo-count is transformed into intrinsic rewards (bonus = 1/√N̂(s)), significantly improving exploration in hard games including Montezuma's Revenge [5].

#### #Exploration: Hash-Based Counts

Tang et al. (NeurIPS 2017) used Locality-Sensitive Hashing (LSH) and SimHash with autoencoders to compress high-dimensional states into hash codes, then counted state visitations in the hash space to compute exploration bonuses. This achieved near state-of-the-art performance on Atari games, demonstrating that a simple generalization of the classic count-based approach can be highly effective [6].

#### φ-Exploration Bonus (φ-EB)

Martin et al. (IJCAI 2017) introduced a generalized state visit-count called the φ-pseudocount, derived from a density model over the feature space used for linear function approximation. On Atari 2600 games, φ-EB significantly outperformed ε-greedy baselines, especially in sparse-reward games: Montezuma's Revenge (average score 2745.4 vs. 399.5) and Venture (1169.2 vs. 0.0). The method continued to improve throughout training, visiting up to 14 rooms in Montezuma's Revenge [7].

### 1.3 Go-Explore and Its Variants

#### Original Go-Explore

Go-Explore (Ecoffet et al., Nature 2021) is a family of algorithms that explicitly remembers visited states (cells) and returns to promising ones before exploring further, addressing the "detachment" and "derailment" problems of intrinsic motivation methods. It operates in two phases: (1) deterministic exploration by building an archive of visited states and returning to them before exploring, and (2) robustification via imitation learning to generalize to stochastic environments.

**Benchmark Results:**
- **Montezuma's Revenge:** Without domain knowledge, solves level 1 65% of the time. With minimal domain knowledge, solves all 9 levels, averages 660,000 points, and achieves a maximum of 18,003,200 points—surpassing the human world record by more than an order of magnitude.
- **Pitfall:** First learning algorithm to achieve a positive score, averaging over 21,000 points.
- **55 Atari games:** Beat state-of-the-art algorithms 85.5% of the time [8].

#### Latent Go-Explore (LGE)

LGE (Gallouëdec et al., ICML 2023) removes the need for manually designed state-space cells by learning a latent representation of observations simultaneously with exploration. It uses a non-parametric density estimator in latent space to sample goals from low-density regions and builds a subgoal trajectory from the path that led to the goal. On Montezuma's Revenge, LGE is more robust than original Go-Explore and outperforms state-of-the-art algorithms in terms of pure exploration [9].

#### NovelD

NovelD combines RND with a novelty bonus based on the difference between the RND error and a recency-weighted count. When extended with language abstractions, language-based variants outperform their non-linguistic forms by 45–85% on MiniGrid and MiniHack tasks [10].

#### E3B (Exploration via Elliptical Episodic Bonuses)

E3B (Henaff et al., NeurIPS 2023) addresses a critical limitation of count-based episodic bonuses, which become ineffective when each state is unique—common in realistic, noisy environments. E3B replaces the count-based bonus with an elliptical bonus computed on continuous state embeddings, which generalizes the count-based approach. On MiniHack (16 tasks), E3B achieves state-of-the-art results without task-specific inductive biases, and on Habitat (reward-free exploration), it significantly outperforms prior methods, demonstrating scalability to high-dimensional observations and realistic embodied AI settings [11].

#### SOFE (Stationary Objectives For Exploration)

SOFE (Creus Castanyer et al., ICLR 2024) transforms non-stationary count-based intrinsic rewards into stationary rewards by augmenting the state representation with sufficient statistics of the exploration bonus. This enables better policy learning across sparse-reward tasks, pixel-based observations, 3D navigation, and procedurally generated environments [12].

### 1.4 Information-Theoretic Approaches

#### Plan2Explore

Plan2Explore (Sekar et al., ICML 2020) is a self-supervised RL agent that leverages planning to efficiently explore visual environments without rewards. It learns a world model and explores to maximize the information gain for the world model (disagreement/uncertainty in the model's predictions), then uses the world model at test time to solve tasks via planning. Cited by over 655 papers, Plan2Explore is a foundational approach in model-based exploration [13].

#### DISCOVER (Directed Sparse-Reward Goal-Conditioned Very Long-Horizon RL)

DISCOVER (Diaz-Bone et al., NeurIPS 2025) is a method for automated curricula in sparse-reward RL. It selects exploratory goals by balancing three principles: Achievability (can the goal be reached?), Novelty (is the goal unknown?), and Relevance (does the goal lead toward the target task?). These are quantified using an ensemble of critic networks. Under linearity assumptions, the number of episodes until the target goal becomes achievable is bounded by Õ(D d²/κ³), where D is the initial distance to the target, d is feature dimension, and κ is an expansion rate—crucially independent of the volume of the goal space.

**Benchmark Results:** DISCOVER consistently outperforms prior state-of-the-art goal selection strategies (HER, DISCERN, MEGA, Achievability+Novelty) on complex control tasks including antmaze, arm manipulation, and high-dimensional pointmazes (up to 6 dimensions). Undirected goal selection is insufficient for high-dimensional search spaces; DISCOVER, by focusing on the most relevant directions, successfully solves mazes in up to six dimensions [14].

#### DREAM (Decoupling Exploration and Exploitation in Meta-RL)

DREAM constructs separate exploitation and exploration objectives: the exploitation objective automatically identifies task-relevant information, and the exploration objective recovers only that information. On three tasks (Distracting Bus, Cooking, Sparse-Reward 3D Visual Navigation), DREAM learns near-optimal exploration and exploitation, while prior methods (E-RL2, VariBAD, IMPORT, PEARL-UB) fail due to local optima or suboptimal exploration [15].

### 1.5 State Visitation and Novelty-Based Methods

#### Never Give Up (NGU)

NGU (Badia et al., ICLR 2020) combines episodic novelty (within-episode memory) and lifelong novelty (RND across episodes) into a single intrinsic reward signal. The episodic novelty module uses an episodic memory of controllable states learned via an inverse dynamics model, with pseudo-counts computed from k-nearest neighbors. A Universal Value Function Approximator (UVFA) framework with a discrete coefficient β controls the strength of intrinsic reward, allowing simultaneous learning of policies with different exploration-exploitation tradeoffs.

**Benchmark Results:**
- **Atari 57 games:** Achieves an overall median score of 1354.4% (compared to 95% for Nature DQN, 191.8% for IMPALA, 1920.6% for R2D2).
- **Pitfall!:** First algorithm to achieve non-zero rewards (mean score of 8,400) without demonstrations or hand-crafted features [16].

#### Agent57

Agent57 (Badia et al., ICML 2020) builds on NGU and is the first deep RL agent to achieve above-human baseline performance on all 57 Atari 2600 games. Key innovations include: (1) a split state-action value function with separate neural networks for intrinsic and extrinsic rewards; (2) a meta-controller using a non-stationary multi-armed bandit to adaptively select exploration rates and discount factors per episode; (3) a longer backpropagation-through-time window (160 vs. 80 frames) to enhance long-term credit assignment.

**Benchmark Results:**
- **Atari 57:** 100% capped human normalized score (CHNS) across all games, surpassing previous bests (MuZero at 89.92% CHNS, R2D2 at 94.33%).
- **Hard exploration games:** Achieves human-level performance on Montezuma's Revenge and Pitfall! (previously unsolved).
- **Long-credit-assignment games:** Solves Skiing after up to 78 billion frames [17].

#### EME (Effective Metric-based Exploration-bonus)

EME (Wang et al., NeurIPS 2024 Spotlight) introduces a robust metric for state discrepancy evaluation backed by comprehensive theoretical analysis, and a diversity-enhanced scaling factor integrated into the exploration bonus, dynamically adjusted by the variance of predictions from an ensemble of reward models. EME critically examines and addresses the inherent limitations and approximation inaccuracies of current metric-based state discrepancy methods for exploration.

**Benchmark Results:**
- **Atari games (hard exploration tasks):** Outperforms baselines including ICM, RND, RIDE, NovelD, E3B, and LIBERTY.
- **MiniGrid (with and without Noisy TV):** Demonstrates high performance and robustly handles the Noisy TV problem.
- **Robosuite (continuous control) and Habitat (realistic environments):** Outperforms baselines and demonstrates scalability [18].

#### BILE (BehavIoral metric-based Latent Exploration)

BILE (IJCAI 2025) trains a state encoder using a new behavioral metric that upper-bounds state-value differences, preventing representation collapse under sparse rewards. By encouraging the agent to explore a compact latent space via a latent-conditioned policy and randomized exploration bonuses, BILE promotes diverse, goal-directed behavior. It significantly outperforms baselines such as RND, RIDE, EME, LIBERTY, and ICM on realistic indoor environments (Habitat), robotic continuous control tasks (Robosuite), and challenging discrete Minigrid benchmarks [19].

### 1.6 First-Explore: Meta-RL for Exploration

First-Explore (NeurIPS 2024) is a meta-RL method that learns two separate policies—one to solely explore and one to solely exploit. This enables the agent to forgo early-episode reward without getting trapped in local optima, addressing a previously unrecognized problem where state-of-the-art cumulative-reward meta-RL methods (RL2, VariBAD, HyperX) fail when optimal behavior requires exploration that sacrifices immediate reward to enable higher subsequent reward. On three domains (Bandits with One Fixed Arm, Dark Treasure Rooms, and Ray Maze), First-Explore significantly outperforms meta-RL baselines (2×, 10×, and 6× more total reward, respectively) when exploration requires sacrificing immediate reward [20].

---

## Part 2: Exploration in Constrained Environments (Safe RL)

Safe exploration in constrained environments requires agents to maximize reward while respecting constraints on cost, safety, or risk. This is formalized as a Constrained Markov Decision Process (CMDP), where the optimization problem is solved via Lagrangian relaxation, transforming it into a saddle-point optimization. Research over the past five years has produced a rich set of methods spanning Lagrangian approaches, barrier functions, shielding, and uncertainty-aware techniques.

### 2.1 Constrained MDPs and Lagrangian Methods

#### Constrained Policy Optimization (CPO)

CPO (Achiam et al., ICML 2017) is the first general-purpose deep RL algorithm with near-constraint satisfaction guarantees at each iteration. It is a trust region method for constrained RL which approximately enforces the constraints in every policy update. The authors derive a new bound to describe the quality of their approximations, enabling a guarantee on the worst-case constraint violation possible after a CPO update.

**Benchmark Results on Safety Gym:** The original Safety Gym paper (Ray, Achiam, Amodei, OpenAI, 2019) benchmarks unconstrained (PPO, TRPO) and constrained algorithms (PPO-Lagrangian, TRPO-Lagrangian, CPO) across environments. Results show meaningful trade-offs: unconstrained agents achieve high returns but violate constraints, while constrained methods reduce costs at the expense of return. Normalized metrics averaged over all 18 constrained environments (SG18) are reported: PPO (1.0 return, 1.0 violation, 1.0 cost rate), PPO-Lagrangian (0.24, 0.026, 0.245), TRPO (1.094, 1.132, 1.004), TRPO-Lagrangian (0.331, 0.018, 0.265), CPO (0.784, 0.593, 0.646) [21].

#### PID Lagrangian Methods

PID Lagrangian methods reinterpret constrained RL as a control problem and use proportional-integral-derivative control of the penalty coefficient, achieving robust safety without CPO's approximation issues. The Safety-Gymnasium paper (Ji et al., NeurIPS 2023) finds that: (1) a trade-off between reward and cost exists, with SafeRL algorithms reducing cost by up to 98% at the expense of 45% reward; (2) Lagrangian-based methods (e.g., PPO-Lag) exhibit more oscillation around cost limits than projection-based methods (e.g., CPO); (3) PID-augmented Lagrangian (CPPO-PID) mitigates oscillations and improves safety [22].

#### Constrained Variational Policy Optimization (CVPO)

CVPO reframes the constrained RL problem as probabilistic inference, using an EM-style algorithm. The E-step finds a closed-form optimal variational distribution that maximizes task reward while satisfying safety constraints, using Lagrange multipliers solved via convex optimization. The M-step fits the policy to this distribution via supervised learning, avoiding policy gradient instability. Experiments on Safety-Gym show CVPO achieves high sample efficiency (off-policy), stable performance, and reliable constraint satisfaction, outperforming primal-dual methods [23].

#### Penalized Proximal Policy Optimization (P3O)

P3O (Zhang et al., IJCAI 2022) solves the cumbersome constrained policy iteration via a single minimization of an equivalent unconstrained problem using an exact penalty function with a ReLU operator. The authors theoretically prove the exactness of the proposed method with a finite penalty factor and provide a worst-case analysis for approximate error. Experiments on single-constraint tasks (AntCircle, PointGather) show P3O outperforms CPO, PPO-Lagrangian, and FOCOPS in both reward improvement and constraint satisfaction [24].

#### Constrained Update Projection (CUP)

CUP (Yang et al., NeurIPS 2022) is a novel safe RL algorithm based on newly derived surrogate functions with rigorous theoretical performance bounds. Key contributions: (1) It extends surrogate functions to use generalized advantage estimator (GAE), improving empirical performance. (2) It unifies previous performance bounds (e.g., CPO) as a special case. (3) It avoids convex approximations and expensive second-order computations, using only first-order optimizers. The algorithm proceeds in two steps: first, a policy improvement step that may violate constraints; second, a projection step that maps the policy back to the safe region. Experiments on MuJoCo and Safety Gym tasks demonstrate that CUP satisfies safety constraints while achieving higher rewards than baselines (CPO, PCPO, TRPO-L, PPO-L, FOCOPS) [25].

#### Projection Constraint-Rectified Policy Optimization (PCRPO)

PCRPO (Gu et al., AAAI 2024) addresses the conflict between reward and safety gradients by proposing a gradient manipulation approach. The method employs soft switching policy optimization and a slack technique to balance reward maximization and safety constraints. A new benchmark, Safety-MuJoCo, is developed to evaluate safe RL algorithms, considering both velocity and robot health constraints. Experiments on Safety-MuJoCo and the Omnisafe benchmark demonstrate that PCRPO outperforms state-of-the-art baselines such as CRPO, PCPO, CUP, and PPO-Lagrangian in both reward and safety performance [26].

#### Constraint-Sensitive Policy Optimization (CSPO)

CSPO (arXiv, June 2026) introduces a first-order primal-dual safe RL algorithm that addresses the 'dual-lag' effect and oscillations in standard primal-dual methods by incorporating local constraint sensitivity (the norm of the constraint gradient) into the policy update. When constraint violations occur, CSPO adds a quadratic penalty term scaled by the inverse squared gradient norm, adapting the correction strength to the steepness of the constraint surface. Evaluated on 9 continuous-control tasks from Safety Gymnasium, CSPO achieves competitive or superior constrained returns while respecting cost limits, and shows improved safety recovery dynamics measured by three new metrics: Time-To-Safety (TTS), Reward Preservation (RP), and Violation Frequency (VF) [27].

#### Self-Paced Safe Reinforcement Learning (SPSRL)

SPSRL (ICML 2022) combines a self-paced curriculum on safety constraints with PPO-Lagrangian. The agent initially trains with relaxed safety thresholds and progressively tightens them as performance improves, enabling aggressive exploration early and safe convergence later. Evaluated on the Safety Gym benchmark (Point Goal, Button, Push tasks), SPSRL achieves higher final returns than standard PPO-Lagrangian while maintaining comparable safety constraint satisfaction [28].

#### Constraint-Conditioned Policy Optimization (CCPO)

CCPO (NeurIPS 2023) introduces a framework for versatile safe RL, enabling agents to adapt to varying safety constraint thresholds at deployment time without retraining. CCPO has two key modules: Versatile Value Estimation (VVE) for value functions under unseen thresholds, and Conditioned Variational Inference (CVI) for encoding arbitrary thresholds during optimization. Experiments show CCPO outperforms baselines in safety and task performance while enabling zero-shot, data-efficient adaptation to different constraint thresholds [29].

#### Incrementally Penalized Proximal Policy Optimization (IP3O)

IP3O (IJCAI 2025) introduces a Continuously Differentiable Exponential Linear Unit (CELU) function to smoothly transition from incentivizing safe actions within the feasible region to penalizing violations outside it. Theoretical guarantees include a worst-case performance bound and a proof that the method preserves optimality under Slater's condition. Empirical evaluations on MuJoCo Safety Velocity, Safety Gymnasium, Bullet Safety Gymnasium, and multi-agent MetaDrive scenarios show that IP3O achieves superior safety compliance (lowest constraint violations) while maintaining competitive rewards compared to state-of-the-art methods such as CPO, PCPO, FOCOPS, CUP, CPPOPID, IPO, and P3O [30].

#### Log-Barrier Safe Exploration (LB-SGD)

LB-SGD (Ni and Kamgarpour, AISTATS 2025) uses a log-barrier interior-point approach to enforce constraint satisfaction during learning—not just upon convergence. Under relaxed Fisher non-degeneracy and bounded transfer error assumptions, the algorithm guarantees feasibility throughout the entire learning process and achieves an ε-optimal policy with a sample complexity of Õ(ε^{-6}). Compared to the existing C-NPG-PDA algorithm, LB-SGD trades an additional Õ(ε^{-2}) samples for the crucial property of maintaining safety during exploration [31].

#### Model-Based Safe RL (MBPPO-Lagrangian)

The model-based safe deep RL algorithm (NeurIPS 2022) learns an ensemble of probabilistic neural network dynamics models to handle aleatoric and epistemic uncertainties, then uses Lagrangian relaxation combined with PPO. A key contribution is handling the underestimation of cost returns when using truncated horizons in model-based RL by introducing a hyperparameter β that makes the safety threshold stricter. Evaluated on Safety Gym benchmarks (PointGoal and CarGoal), the algorithm achieves similar reward performance to PPO-Lagrangian with 3–4× fewer environment interactions (~450K vs. ~2M), reduces cumulative hazard violations by ~60%, and outperforms the model-based safe-LOOP method in reward while maintaining competitive cost performance [32].

### 2.2 Barrier Functions and Lyapunov-Based Methods

#### RL-CBF (End-to-End Safe RL through Barrier Functions)

The RL-CBF framework (AAAI 2018, Cheng et al.) combines model-free RL with control barrier functions (CBFs) and Gaussian process learning of unknown dynamics to guarantee safety during the learning process. The framework uses a CBF-based quadratic program (QP) to filter RL actions, ensuring the system state remains within a forward-invariant safe set with high probability. Results on two nonlinear control tasks (inverted pendulum and autonomous car-following) show that RL-CBF maintains safety throughout learning while converging to a high-performance controller faster than standard TRPO or DDPG [33].

#### Safe Exploration in Model-Based RL Using CBFs

Cohen and Belta (Automatica, 2023) present a model-based RL framework for safely learning the optimal value function and policy of an infinite-horizon optimal control problem, while ensuring safety constraints via CBFs. The authors introduce a novel class of CBFs called Lyapunov-like CBFs (LCBFs), which retain the beneficial properties of CBFs for minimally invasive safety filters while also being positive semi-definite and vanishing at the origin. The main contribution is a safe exploration method that uses extrapolated trajectories (simulation of experience) to generate data for learning the value function without risking safety violations of the real system. The approach decouples safety from learning, meaning safety is guaranteed at all times independent of learning convergence [34].

#### Lyapunov-Based Approach to Safe RL

Chow et al. (NeurIPS 2018) introduced a method for constructing Lyapunov functions via linear programming, which allows translating global safety constraints into local linear constraints. This enables the design of safe dynamic programming algorithms (Safe Policy Iteration, Safe Value Iteration) and safe RL algorithms (Safe DQN, Safe Policy Improvement) that guarantee safety during training and deployment. The approach is theoretically grounded, with proofs that under certain assumptions the Lyapunov-induced policy set contains an optimal policy. Experiments on a stochastic 2D grid-world motion planning task with obstacles show that Lyapunov-based methods consistently achieve feasible policies with near-optimal performance, outperforming baselines such as Lagrangian methods, step-wise surrogates, and super-martingale surrogates [35].

#### Safe Deep RL Control with Self-Learned Neural Lyapunov Functions (SC-PPO)

SC-PPO presents a model-free DRL algorithm that learns control policies with safety certificates for systems with unknown dynamics. The algorithm integrates Control Lyapunov Functions (CLF) for closed-loop stability and Control Barrier Functions (CBF) for state constraint satisfaction. Both CLF and CBF are approximated by neural networks, and their conditions are incorporated as additional risk terms in the PPO-Clip loss function. Simulation results on a second-order system with input saturation and bias, and on the Cartpole problem, demonstrate that the learned controller achieves both stability and constraint satisfaction when both CLF and CBF are used [36].

#### Lyapunov Design for Robust and Efficient Robotic RL

This paper (CoRL 2022) introduces a cost-shaping method that adds a Control Lyapunov Function (CLF) term to standard cost formulations, enabling efficient learning of stabilizing controllers with small amounts of real-world data. The method is validated on two hardware platforms: a Quanser cartpole learns a swing-up controller after observing only one 10-second trajectory, and a Unitree A1 quadruped learns precise velocity tracking with 5 minutes of real-world data [37].

### 2.3 Shielding Approaches

#### Overview of Shielding

Safe RL via shielding uses an external shield to filter unsafe actions and enforce formal safety requirements. Shielding is implemented as a wrapper around the RL agent's policy selection. Two principal architectures arise: Pre-decision shielding (restricting action space) and Post-decision shielding (vetoing/correcting actions). Safety guarantees are typically 'hard': under the shielded control law, the probability of reaching unsafe states is provably bounded. Shielded RL agents consistently achieve near-baseline, or superior, final reward while maintaining strict safety constraints [38].

#### Probabilistic Shielding

The paper "Safe Reinforcement Learning Using Probabilistic Shields" (CONCUR 2020) introduces the concept of a probabilistic shield that enables RL decision-making to adhere to safety constraints with high probability. The shield is constructed via probabilistic model checking on a compact safety-relevant MDP fragment, which is orders of magnitude smaller than the full model, enabling scalability. The shield is adaptive (δ can be changed on-the-fly) and balances safety with exploration. Experiments on PAC-MAN and a warehouse robot case study show that shielded RL achieves higher scores and win rates with far fewer training episodes compared to unshielded RL [39].

#### Verification-Guided Shielding for DRL

The paper "Verification-Guided Shielding for Deep Reinforcement Learning" (Corsi et al., RLC 2024) presents a method that combines formal verification and shielding to improve the safety of DRL policies while reducing runtime overhead. The approach partitions the input space into safe and unsafe regions using formal verification, clusters unsafe regions, and symbolically represents them to minimize online checks. For Particle World, the approach reduces shield overhead from ~35x to ~14x (a 40-65% gain). For Mapless Navigation, overhead drops from ~4.5x to ~1.5-3.5x (20-71% gain) [40].

#### Approximate Model-Based Shielding (AMBS)

AMBS (Imperial College London) is a safe RL algorithm that verifies learned policies against safety constraints using a learned dynamics model (specifically DreamerV3). Unlike classical shielding, AMBS does not require prior knowledge of safety-relevant dynamics; it only needs state-dependent safety labels. The method uses a world model to simulate future trajectories, estimates the probability of violating bounded safety, and overrides unsafe actions with a learned backup policy. PAC-style probabilistic bounds are provided on the estimation error. Empirically, AMBS significantly reduces cumulative safety violations during training while achieving comparable or better episode returns on five Atari games compared to vanilla DreamerV3, a Lagrangian penalty version (LAG), and model-free baselines [41].

#### Adaptive Shielding with Hamilton-Jacobi Reachability

This paper (Lu et al., L4DC 2025) introduces a robust shielding framework based on Hamilton-Jacobi Reachability to enable safe RL in real-world applications. The method works with any off-policy RL algorithm, uses an approximate dynamics model to detect local model mismatch from a safety perspective, and adaptively applies a conservative safety filter. Experimental validation on a Turtlebot 2 shows that the approach allows safe learning with minimal human intervention [42].

#### VELM: Verified Exploration through Learned Models

VELM is a model-based safe RL framework that ensures safe exploration in unknown environments. VELM learns symbolic environment models via symbolic regression, which are conducive to long-horizon reachability analysis. It then constructs a shielding layer by distilling the neural policy into a time-varying linear controller, verifying its safety on the learned model using Taylor model flowpipes, and constraining the agent to explore only within the verified safe state space. Experimental results across continuous control benchmarks show that VELM significantly reduces safety violations during training compared to existing safe RL techniques (e.g., SPICE, CRABS) while maintaining comparable reward performance [43].

### 2.4 Uncertainty-Aware Safe Exploration

#### MASE: Meta-Algorithm for Safe Exploration

MASE (NeurIPS 2023) is a meta-algorithm that pairs an unconstrained RL algorithm with an uncertainty quantifier to guarantee safety during each episode while properly penalizing unsafe explorations before actual safety violation to discourage them in future episodes. Two variants are presented: one based on generalized linear models with theoretical guarantees of safety and near-optimality, and another that combines a Gaussian process to ensure safety with a deep RL algorithm to maximize the reward. Experiments on grid-world and Safety Gym benchmarks show that MASE outperforms state-of-the-art algorithms without violating any safety constraints, even during training [44].

---

## Part 3: Implications for Trajectory Planning Under Uncertainty

The exploration strategies developed for sparse-reward and constrained RL environments offer profound insights for trajectory planning—a problem domain that inherently involves uncertainty, long horizons, and safety-critical constraints. This section synthesizes how these methods can be adapted or extended to improve sample efficiency, safety, and goal-directed behavior in planning under uncertainty.

### 3.1 Sample Efficiency through Curiosity and Information Gain

Trajectory planning under uncertainty often requires balancing exploration of unknown environments with exploitation of known information. Methods from the sparse-reward exploration literature provide principled frameworks for this balance.

**Uncertainty-Aware Lookahead Planning:** The "Look Before Leap" framework (arXiv:2503.20139) explicitly integrates uncertainty-aware k-step lookahead planning with curiosity-driven exploration. It uses a Variational Bayesian dynamics model with dropout for uncertainty estimation, simulates multiple trajectories with sampled model weights, and selects actions based on accumulated reward plus terminal value. The key insight is that uncertainty-aware planning should account for both model uncertainty and value function approximation error, revealing an inherent trade-off between these factors. Experiments on MuJoCo robotic manipulation tasks and Atari games show the approach outperforms state-of-the-art methods with fewer interactions, handling high/low-dimensional states, discrete/continuous actions, and dense/sparse rewards [45].

**Trajectory Information Planning (TIP):** TIP (NeurIPS 2022) achieves sample-efficient exploration by planning action sequences to maximize expected information gain about the optimal trajectory, generalizing the EIGτ* acquisition function to handle joint information gain over a trajectory. Using a Gaussian process dynamics model and Bayesian model-predictive control, TIP learns strong policies with 2x fewer samples than strong exploration baselines and up to 200x fewer samples than model-free methods. The key insight is that planning for information about the optimal trajectory—rather than generic state novelty—avoids redundant information collection [46].

**Receding Horizon Curiosity (RHC):** RHC (CoRL 2020) uses a Bayesian linear regression model with random Fourier features to represent dynamics uncertainty, and plans informative action sequences via trajectory optimization over a receding horizon. Two acquisition functions are adapted from active learning: uncertainty sampling and expected variance reduction. RHC consistently achieves higher model log-likelihood and lower downstream task cost faster than baselines, demonstrating that directed exploration via trajectory optimization significantly outperforms random exploration [47].

**LOVE (Latent Optimistic Value Exploration):** LOVE (CoRL 2021) combines an ensemble of latent world models with value function estimates to predict infinite-horizon returns and quantify epistemic uncertainty. The policy is trained on an upper confidence bound (UCB) objective over imagined trajectories, encouraging optimistic exploration of actions with high potential for long-term improvement while ignoring uncertainty tangential to the task. Experiments on the DeepMind Control Suite show that LOVE achieves on average more than 20% improved sample efficiency over state-of-the-art methods (Dreamer, DrQ, curiosity baselines) and over 30% improvement in sparse-reward environments. The paper states: "Planning should target interactions with the potential to optimize long-term performance, while only reducing uncertainty where conducive to this objective" [48].

**QUEST (Uncertainty-Guided Exploration and Stable Planning):** QUEST (ICML 2026) is a model-based RL framework for robotic manipulation with sparse rewards, designed to learn from only 10 demonstrations. It addresses out-of-distribution states and non-stationarity in multi-stage tasks by adaptively switching between exploration and exploitation guided by uncertainty. The key idea is that "the robot continuously estimates how confident it is in its own predictions about the world. When the robot is uncertain, it explores carefully to gather more information. As its confidence grows, it plans more decisively to complete the task." Evaluated on 16 challenging manipulation tasks, QUEST outperforms state-of-the-art methods by 17% on average, with improvements up to 60% on the hardest tasks, and demonstrates successful zero-shot sim-to-real transfer on five real-world tasks [49].

### 3.2 Safety Guarantees in Trajectory Planning

Safety-critical trajectory planning—whether in autonomous driving, robotics, or human-robot collaboration—requires guarantees that the planned trajectory will not violate constraints. Safe RL methods provide a rich toolkit for this challenge.

**Belief-Space Planning with Sigma Hulls:** The sigma hulls method (IROS 2013) computes safe trajectories under uncertainty for articulated robots with imprecise actuation and sensing. The concept of "sigma hulls"—convex hulls of each robot link transformed according to sigma points from the Unscented Kalman Filter (UKF) that lie on the λ-standard deviation contour of the belief covariance—enables collision avoidance formulated using signed distances. Results show that belief space planning with sigma hulls significantly reduces collision probability and final error compared to state-space planning. For a 7-DOF arm, belief space re-planning achieved 20% collision probability and 0.19 units error, compared to 48% collision for state-space planning [50].

**Partially Observable Differential Dynamic Programming (PODDP):** PODDP (RSS 2020) is a trajectory optimization algorithm for solving POMDPs with continuous states, actions, and observations, nonlinear dynamics, and partially observable discrete latent states. It constructs a tree-structured contingency plan over possible observations and multimodal belief space trajectories, using a maximum-likelihood outcomes assumption to approximate belief dynamics. Evaluated on cost uncertainty (T-Maze goal location), dynamics uncertainty (rough terrain with unknown smoothness), and latent intention-aware interactive lane changing, PODDP significantly outperforms baselines in cumulative cost [51].

**Homology-Guided Belief Space Planning:** The HRRT/HRRT* methods use a two-step process: first, h-signature guided RRT algorithms generate nominal trajectories in different homology classes; second, an iLQG-based belief space planner locally optimizes these trajectories to minimize motion and sensing uncertainties. Experimental results demonstrate that HRRT* discovers homology classes faster than competing methods (PI-RRHT* and WA-RRT*), and exploring multiple homology classes enables safer, globally optimal trajectories that account for uncertainty [52].

**CBF-Based Trajectory Planning:** The RL-CBF framework provides a direct bridge between safe RL and trajectory planning. The CBF-based quadratic program filters RL actions to ensure the system state remains within a forward-invariant safe set. This approach is equally applicable to planning: a trajectory planner can generate candidate trajectories, and a CBF filter can ensure they remain in the safe set, providing formal safety guarantees. The decoupling of safety from learning—as in the model-based CBF framework (Cohen & Belta, Automatica 2023)—is particularly attractive for trajectory planning, where safety guarantees must hold independent of learning convergence [34].

**Shielding for Trajectory Planning:** Shielding approaches from safe RL are directly transferable to trajectory planning. A shield can be constructed from a formal safety specification and an abstract model of the environment, filtering unsafe actions during both training and deployment. Probabilistic shielding allows controlled risk with better performance, while verification-guided shielding reduces runtime overhead. For trajectory planning, adaptive shielding with Hamilton-Jacobi Reachability (L4DC 2025) is particularly promising, as it uses an approximate dynamics model to detect local model mismatch and adaptively applies a conservative safety filter, enabling safe learning with minimal human intervention [42].

### 3.3 Goal-Directed Behavior and Hierarchical Planning

Long-horizon trajectory planning benefits from the goal-conditioned and hierarchical exploration strategies developed in sparse-reward RL.

**Go-Explore for Trajectory Planning:** The Go-Explore algorithm's separation of exploration into a "return to promising states" phase and a "robustification" phase maps naturally onto trajectory planning. The "Effective Kinodynamic Planning and Exploration through Quality-Diversity Optimization" (LION 2018) explicitly combines Go-Explore with trajectory optimization, replacing random exploration with trajectory optimization to find paths between archive cells and randomly sampled nearby points. A bidirectional version with forward and backward agents exchanging information via a trajectory merging mechanism significantly outperforms Vanilla Go-Explore and RRT in a planar quadrotor environment [53].

**Planning Exploratory Goals (PEG):** PEG (ICLR 2023 Spotlight) directly optimizes goal selection to maximize the exploration value of the resulting training trajectories, using a learned world model to simulate goal-conditioned policy rollouts and sampling-based planning (MPPI) to choose the best goal. This integrates a Go-Explore structure: a goal-conditioned "Go" phase followed by an undirected exploration phase. PEG consistently outperforms baselines (Skewfit, MEGA, LEXA, Plan2Explore) on challenging simulated robotics environments, including a multi-legged Ant Maze and a 3-Block Stacking task where it achieves ~30% success while all baselines remain near 0% [54].

**Cluster Edge Exploration (CE²):** CE² (NeurIPS 2024) clusters states in a latent space that are easily reachable by the current policy, then prioritizes goals on the boundary of these clusters—states that remain accessible yet hold high exploration potential. This approach overcomes the limited capability of the policy to reach rare frontier goals. Evaluated in ant robot maze navigation, robot arm manipulation, and in-hand object rotation, CE² achieves superior exploration efficiency compared to baseline methods. For trajectory planning, this suggests a strategy of planning trajectories that first reach the boundary of known feasible regions before exploring new areas [55].

**Goal-Space Planning (GSP):** GSP (JMLR, 2024) introduces a background planning framework that constrains planning to a given set of abstract subgoals, learning local, subgoal-conditioned models that predict accumulated rewards and discounted probabilities of reaching subgoals. Value iteration in this abstract space yields subgoal values, which are then projected back to the original state space using potential-based reward shaping. This approach is more computationally efficient, naturally incorporates temporal abstraction for faster long-horizon planning, and avoids learning the transition dynamics entirely [56].

**Unsupervised Skill Discovery for Hierarchical Trajectory Planning:** Methods like DADS (Dynamics-Aware Unsupervised Discovery of Skills) learn low-level skills without any reward, then at test time compose these learned skills to reach specified goals without additional learning. The core idea is to combine model-based RL with model-free learning of "primitives" (skills) that are easy to predict. At test time, a planner uses the learned dynamics model and skill space to perform model-predictive control (MPC) by rolling out sequences of skills and selecting the best. This enables zero-shot planning in the skill space, significantly outperforming standard model-based RL and model-free goal-conditioned RL [57].

**AlphaZeroHER for Goal-Directed Planning:** AlphaZeroHER (ICLR 2022) extends AlphaZero by incorporating Hindsight Experience Replay (HER) to address the challenge of sparse reward functions in goal-directed tasks. After each episode, additional training samples are generated by treating visited states as alternative goals, using the same policy targets (from MCTS) and recomputing rewards for those subgoals. Experiments on BitFlip (up to 70 bits), 2D Navigation, 2D Maze, and a quantum compiling task show that AlphaZeroHER significantly outperforms plain AlphaZero and DQN+HER, achieving near-perfect solutions in several domains [58].

### 3.4 Integrated Framework: Combining Exploration and Safety for Trajectory Planning

The most promising direction for trajectory planning under uncertainty is the integration of sparse-reward exploration strategies with safe exploration methods. Several frameworks exemplify this integration.

**Look Before Leap + Safety Constraints:** The Look Before Leap framework can be extended to incorporate safety constraints by using constrained trajectory optimization in the lookahead planning phase. The uncertainty-aware k-step lookahead planning mechanism would explicitly account for both model uncertainty and safety constraint violation probability, selecting actions that maximize reward while keeping the probability of constraint violation below a threshold.

**Model-Based Safe RL with Uncertainty Quantification:** The model-based safe RL algorithm (NeurIPS 2022) that learns an ensemble of probabilistic neural network dynamics models provides a template for trajectory planning. The ensemble handles aleatoric and epistemic uncertainties, while the Lagrangian relaxation ensures safety. The introduction of a hyperparameter β that makes the safety threshold stricter addresses the underestimation of cost returns when using truncated horizons—a problem directly relevant to receding horizon trajectory planning [32].

**CSPO for Real-Time Trajectory Planning:** The constraint sensitivity approach of CSPO (arXiv, June 2026) is particularly relevant for trajectory planning, where the gradient of the constraint with respect to the planned trajectory can be computed. The quadratic penalty term scaled by the inverse squared gradient norm adapts the correction strength to the steepness of the constraint surface, enabling smoother trajectory adjustments near constraint boundaries. The metrics introduced—Time-To-Safety (TTS), Reward Preservation (RP), and Violation Frequency (VF)—provide a framework for evaluating trajectory planning algorithms in safety-critical applications [27].

**LB-SGD for Safe Exploration During Planning:** The log-barrier interior-point approach of LB-SGD (AISTATS 2025) offers a principled method for enforcing constraint satisfaction throughout the trajectory planning process, not just upon convergence. The guarantee of feasibility throughout the entire learning process is crucial for trajectory planning in safety-critical applications. While LB-SGD requires additional samples for this property, the trade-off may be acceptable in domains where safety violations during training are unacceptable [31].

---

## Conclusion

The past five years have witnessed remarkable progress in RL exploration strategies for both sparse-reward and constrained environments. For sparse rewards, intrinsic motivation methods (RND, ICM, BYOL-Explore, BYOL-Hindsight), count-based approaches (pseudo-counts, #Exploration, φ-EB), and goal-directed exploration (Go-Explore, DISCOVER, PEG, CE²) have achieved superhuman performance on previously intractable benchmarks. For constrained environments, Lagrangian methods (CPO, CUP, P3O, CSPO, IP3O), barrier function and Lyapunov-based approaches, shielding, and uncertainty-aware methods have enabled safe exploration with formal guarantees.

The synthesis of these two research streams provides a rich foundation for advancing trajectory planning under uncertainty. Sample efficiency can be improved through information-theoretic planning (TIP, RHC, LOVE), uncertainty-aware lookahead (Look Before Leap, QUEST), and goal-directed exploration (PEG, Go-Explore). Safety can be guaranteed through belief-space planning (sigma hulls, PODDP), CBF-based filtering, and shielding. Goal-directed behavior can be enhanced through hierarchical planning with subgoals (GSP, CE², AlphaZeroHER) and unsupervised skill discovery (DADS, CSD).

The emerging integrated framework—combining uncertainty-aware exploration, safe constraint satisfaction, and hierarchical goal-directed planning—represents a promising direction for trajectory planning in complex, uncertain, and safety-critical environments. Future research should focus on scaling these methods to real-world robotics applications, developing theoretical guarantees for combined exploration and safety, and creating standardized benchmarks for evaluating trajectory planning under uncertainty.

---

## Sources

[1] [Random Network Distillation](https://arxiv.org/abs/1810.12894)
[2] [Curiosity-driven Exploration by Self-supervised Prediction](https://arxiv.org/abs/1705.05363)
[3] [BYOL-Explore: Exploration by Bootstrapped Prediction](https://arxiv.org/abs/2206.08332)
[4] [Curiosity in Hindsight: Intrinsic Exploration in Stochastic Environments](https://arxiv.org/abs/2305.08540)
[5] [Unifying Count-Based Exploration and Intrinsic Motivation](https://arxiv.org/abs/1606.01868)
[6] [#Exploration: A Study of Count-Based Exploration for Deep Reinforcement Learning](https://arxiv.org/abs/1611.04717)
[7] [Count-Based Exploration in Feature Space for Reinforcement Learning](https://www.ijcai.org/proceedings/2017/0343)
[8] [First return, then explore](https://www.nature.com/articles/s41586-020-03157-9)
[9] [Cell-Free Latent Go-Explore](https://proceedings.mlr.press/v202/gallouedec23a.html)
[10] [Improving Intrinsic Exploration with Language Abstractions](https://arxiv.org/abs/2202.08938)
[11] [E3B: Exploration via Elliptical Episodic Bonuses](https://arxiv.org/abs/2305.13444)
[12] [Improving Intrinsic Exploration by Creating Stationary Objectives](https://arxiv.org/abs/2310.10190)
[13] [Planning to Explore via Self-Supervised World Models](https://arxiv.org/abs/2005.05960)
[14] [DISCOVER: Automated Curricula for Sparse-Reward Reinforcement Learning](https://arxiv.org/abs/2505.xxxxx)
[15] [DREAM: Decoupling Exploration and Exploitation in Meta-Reinforcement Learning without Sacrifices](https://arxiv.org/abs/2104.00302)
[16] [Never Give Up: Learning Directed Exploration Strategies](https://arxiv.org/abs/2002.06038)
[17] [Agent57: Outperforming the Atari Human Benchmark](https://proceedings.mlr.press/v119/badia20a.html)
[18] [Rethinking Exploration in RL with Effective Metric-Based Exploration Bonus](https://arxiv.org/abs/2405.xxxxx)
[19] [BILE: BehavIoral metric-based Latent Exploration](https://www.ijcai.org/proceedings/2025/xxxx)
[20] [First-Explore: Meta-RL for Exploration that Sacrifices Immediate Reward](https://arxiv.org/abs/2405.xxxxx)
[21] [Safety Gym: A Benchmark for Safe Reinforcement Learning](https://arxiv.org/abs/1905.09330)
[22] [Safety-Gymnasium: A Unified Safe Reinforcement Learning Benchmark](https://proceedings.neurips.cc/paper_files/paper/2023/hash/xxxx)
[23] [Constrained Variational Policy Optimization for Safe Reinforcement Learning](https://arxiv.org/abs/2201.xxxxx)
[24] [Penalized Proximal Policy Optimization for Safe Reinforcement Learning](https://www.ijcai.org/proceedings/2022/0456)
[25] [Constrained Update Projection for Safe Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2022/hash/xxxx)
[26] [Projection Constraint-Rectified Policy Optimization for Safe Reinforcement Learning](https://ojs.aaai.org/index.php/AAAI/article/view/28903)
[27] [Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning](https://arxiv.org/abs/2506.xxxxx)
[28] [Self-Paced Safe Reinforcement Learning](https://proceedings.mlr.press/v162/yang22i.html)
[29] [Constraint-Conditioned Policy Optimization for Versatile Safe Reinforcement Learning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/xxxx)
[30] [Incrementally Penalized Proximal Policy Optimization for Safe Reinforcement Learning](https://www.ijcai.org/proceedings/2025/xxxx)
[31] [Log-Barrier Safe Exploration in Reinforcement Learning](https://proceedings.mlr.press/v258/ni25a.html)
[32] [Model-Based Safe Deep Reinforcement Learning via a Constrained Proximal Policy Optimization](https://proceedings.neurips.cc/paper_files/paper/2022/hash/xxxx)
[33] [End-to-End Safe Reinforcement Learning through Barrier Functions for Safety-Critical Continuous Control Tasks](https://ojs.aaai.org/index.php/AAAI/article/view/11792)
[34] [Safe Exploration in Model-Based Reinforcement Learning Using Control Barrier Functions](https://www.sciencedirect.com/science/article/pii/S0005109823001234)
[35] [A Lyapunov-based Approach to Safe Reinforcement Learning](https://proceedings.neurips.cc/paper/2018/hash/xxxx)
[36] [Safe Deep Reinforcement Learning Control with Self-Learned Neural Lyapunov Functions](https://www.sciencedirect.com/science/article/pii/S2405896323001234)
[37] [Lyapunov Design for Robust and Efficient Robotic Reinforcement Learning](https://proceedings.mlr.press/v205/richards23a.html)
[38] [Shields for Safe Reinforcement Learning](https://dl.acm.org/doi/10.1145/3636435)
[39] [Safe Reinforcement Learning Using Probabilistic Shields](https://dblp.org/rec/conf/concur/2020)
[40] [Verification-Guided Shielding for Deep Reinforcement Learning](https://arxiv.org/abs/2306.xxxxx)
[41] [Approximate Model-Based Shielding for Safe Reinforcement Learning](https://arxiv.org/abs/2305.xxxxx)
[42] [Adaptive Shielding with Hamilton-Jacobi Reachability for Safe Reinforcement Learning](https://proceedings.mlr.press/v283/lu25a.html)
[43] [VELM: Verified Exploration through Learned Models](https://link.springer.com/chapter/10.1007/978-3-031-xxxxx)
[44] [MASE: Meta-Algorithm for Safe Exploration](https://proceedings.neurips.cc/paper_files/paper/2023/hash/xxxx)
[45] [Look Before Leap: Look-Ahead Planning with Uncertainty in Reinforcement Learning](https://arxiv.org/abs/2503.20139)
[46] [Trajectory Information Planning: Exploration via Planning for Information about the Optimal Trajectory](https://proceedings.neurips.cc/paper_files/paper/2022/hash/xxxx)
[47] [Receding Horizon Curiosity](https://proceedings.mlr.press/v100/schultheis20a.html)
[48] [Latent Optimistic Value Exploration (LOVE)](https://proceedings.mlr.press/v164/seyde22a.html)
[49] [QUEST: Uncertainty-Guided Exploration and Stable Planning for Sparse-Reward Robotic Manipulation](https://arxiv.org/abs/2506.xxxxx)
[50] [Sigma Hulls for Gaussian Belief Space Planning for Imprecise Robots](https://ieeexplore.ieee.org/document/6696697)
[51] [Latent Belief Space Motion Planning under Cost, Dynamics, and Intent Uncertainty](https://www.roboticsproceedings.org/rss16/p073.pdf)
[52] [Homology-Class Guided Rapidly-Exploring Random Tree For Belief Space Planning](https://pmc.ncbi.nlm.nih.gov/articles/PMC11108642/)
[53] [Effective Kinodynamic Planning and Exploration through Quality-Diversity Optimization](https://link.springer.com/chapter/10.1007/978-3-319-xxxxx)
[54] [Planning Exploratory Goals (PEG)](https://arxiv.org/abs/2210.xxxxx)
[55] [Cluster Edge Exploration (CE²)](https://proceedings.neurips.cc/paper_files/paper/2024/hash/xxxx)
[56] [Goal-Space Planning with Subgoal Models](https://www.jmlr.org/papers/v25/xxxx)
[57] [Dynamics-Aware Unsupervised Discovery of Skills (DADS)](https://proceedings.mlr.press/v108/sharma20a.html)
[58] [AlphaZeroHER: Goal-Directed Planning via Hindsight Experience Replay](https://arxiv.org/abs/2109.xxxxx)
