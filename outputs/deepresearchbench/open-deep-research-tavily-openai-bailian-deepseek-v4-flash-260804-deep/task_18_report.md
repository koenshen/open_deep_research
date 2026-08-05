# 自动化生成GCS凸安全集：基于PRM与凸分解的优化方案及替代路径综合分析

## 1. 引言

Graph of Convex Sets（GCS）算法是近年来机器人运动规划领域的一项重大突破，由Tobia Marcucci在其MIT博士论文中系统提出，并发表于*Science Robotics*（2023年）[Marcucci et al., 2023](https://www.science.org/doi/10.1126/scirobotics.adf7843)。GCS的核心思想是将离散图搜索的全局性与连续凸优化的高效性相结合，通过将自由配置空间分解为一系列凸集（convex safety sets），构建一个“凸集图”，然后在该图上求解最短路径问题，从而同时优化离散路径选择和连续轨迹参数。该方法在95%的测试问题上能获得接近全局最优（差距<1%）的轨迹，且求解时间与采样方法相比具有显著优势。

然而，GCS的广泛应用面临一个关键瓶颈：**凸安全集的生成目前主要依赖人工手动播种（manual seeding）结合自动化工具（如IRIS算法）**。用户需要手动指定种子点，算法从该点开始“膨胀”出一个凸的碰撞自由区域。在复杂、高维的机器人配置空间中，手动播种不仅耗时且难以保证覆盖质量。因此，探索一种自动化、高质量生成凸安全集的方法，对于推动GCS的实际部署至关重要。

本研究简报的核心探索方向是：**将PRM（Probabilistic Roadmap）算法（或其改进版本）生成的静态连通图，与凸分解算法相结合，自动构造可直接输入GCS求解器的凸集**。同时，研究也要求探讨其他可能的GCS优化思路。本报告将基于对GCS、PRM、凸分解算法（IRIS系列）及GCS扩展研究的全面文献调研，提供一个结构化、深度的分析，涵盖该方案的可行性、实施步骤、潜在挑战，以及一系列替代优化路径。

---

## 2. 核心方案分析：PRM + 凸分解自动生成GCS凸集

### 2.1 方案总体思路

用户提出的方案可概括为以下三步流程：

1. **PRM采样与图构建**：在机器人配置空间中随机采样碰撞自由点，并通过局部规划器（如直线插值）连接近邻点，构建一个静态连通图（PRM Roadmap）。
2. **凸分解**：基于该PRM图的拓扑结构或节点信息，使用凸分解算法（如IRIS）自动生成凸安全集。
3. **GCS求解**：将生成的凸集作为GCS图的顶点，构建交集图（Overlap Graph），然后求解GCS优化问题获得最优轨迹。

### 2.2 已有相关工作的关键发现：VCC算法

在深入分析这个方案前，必须指出，**已有研究几乎完全沿着类似思路进行了探索，但使用了“可见性图”（Visibility Graph）而非PRM图**，这就是Peter Werner等人于ICRA 2024发表的**VCC（Visibility Clique Cover）算法**[Werner et al., 2024](https://wernerpe.github.io/publication/cliquese)。

VCC算法的工作流程为：
1. 在C_free中随机采样点，构建**可见性图**：连接所有具有“互视线”（mutual line of sight）的点对。
2. 在该图中贪婪地提取**大团（Clique）**，即完全连通子图。
3. 用**最小体积包围椭球**包裹每个团内的点。
4. 以这些椭球的中心和主轴为种子，运行**单次IRIS迭代**，膨胀出大的碰撞自由多面体。
5. 重复直到覆盖C_free的指定比例。

VCC的核心洞察是：**随着采样点增多，可见性图中的完全连通子图（团）越来越近似于底层配置空间中的碰撞自由凸集**[Werner et al., 2024](https://wernerpe.github.io/publication/cliquese)。实验结果表明，对于7自由度KUKA IIWA机器人，VCC仅需约46个凸区域即可覆盖70%的C_free，而基线方法（Iterative Obstacle Seeding, IOS）需要483个区域，且VCC速度提升约16倍。

### 2.3 PRM图 vs. 可见性图：关键差异与对方案可行性的影响

用户提出的PRM方案与VCC的可见性方案在核心思想上高度相似，但存在一个**根本性的结构差异**，这决定了**直接使用PRM图的连通性信息进行凸分解在理论上是次优的**。

| 对比维度 | VCC（可见性图） | 标准PRM图 |
|---------|---------------|----------|
| **连接准则** | 全局互视线（任意距离） | 局部规划器连接（近邻节点） |
| **图的稠密度** | 稠密（最坏情况O(n²)边） | 稀疏（通常O(kn)边，k为小常数） |
| **团（Clique）的语义** | 团内点互有视线 → 强凸性指示 | 团内点局部连接 → 不保证互视线 |
| **凸分解的可靠性** | 高（团是凸集的好近似） | 低（局部的团可能不构成凸集） |

**关键问题**：PRM的连接策略是基于“近邻+局部碰撞检测”，而不是“全局互视线”。两个近邻点之间有一条直线路径是碰撞自由的，并不意味着它们之间所有点对都有互视线，更不意味着它们被一个公共的凸集所包含。因此，**对PRM图进行团分解，得到的团可能并不对应C_free中的凸子集**，其凸壳可能包含障碍物洞穴。

**结论**：直接使用标准PRM图作为凸分解的图结构，在理论支撑上弱于VCC的可见性图。**VCC算法的可见性图方案是更符合“凸性近似”理论基础的方案**。

### 2.4 一个更可行的替代方案：PRM采样 + IRIS播种

虽然直接使用PRM的图结构不可取，但**PRM的采样点可以作为IRIS凸区域生成的种子点**，这是一个更直接、更有效的思路。这正是VCC方案中“采样”环节的简化版，但VCC进一步通过团和椭球对种子点进行了“优化”（选择团中心作为种子，比随机点作为种子更好）。

**方案步骤**：
1. **PRM式采样**：在C_free中随机采样大量点。
2. **种子点选择**：直接使用这些采样点，或通过简单的聚类（如基于距离的聚类）选择代表性点，作为IRIS的种子。
3. **运行IRIS**：对每个种子点，运行IRIS算法膨胀出凸区域。
4. **构建重叠图**：计算凸区域间的重叠关系，构建GCS的重叠图。
5. **GCS求解**：在重叠图上求解最短路径问题。

**挑战**：
- **种子冗余**：随机采样点可能高度冗余，导致IRIS生成大量重叠度极高的凸区域，增加GCS问题的规模，降低求解效率。VCC通过团筛选种子，有效避免了这个问题。
- **覆盖不均匀**：随机采样在窄通道区域密度低，导致这些关键区域可能缺乏种子点，IRIS无法覆盖。
- **计算开销**：对每个采样点运行IRIS可能计算量巨大，尤其是高维空间。

### 2.5 实施步骤（带详细技术细节）

如果决定采用“PRM采样 + IRIS”框架，一个可行的实施流程如下：

**步骤1：配置空间采样与碰撞检测**
- 使用**均匀随机采样**或**桥测试（Bridge Test）**[Hsu et al., 2003](https://ieeexplore.ieee.org/document/1241778) 采样策略，在C_free中获取N个点。桥测试能有效提高窄通道区域的采样密度。
- 建立碰撞检测管线（如使用FCL或Drake的SceneGraph）。

**步骤2：IRIS凸区域膨胀**
- 对每个采样点（或经聚类后的代表性点），运行IRIS算法。
- 对于**高维或复杂运动学机器人**（如机械臂），使用**IRIS-NP**[Petersen & Tedrake, 2023](https://arxiv.org/abs/2303.14737) 或**IRIS-ZO**[Werner et al., 2024](https://arxiv.org/html/2410.12649v1)。IRIS-ZO使用零阶优化，仅需碰撞检测器，可并行化，速度比IRIS-NP快一个数量级。
- 对于需要**严格无碰撞保证**的场景，在IRIS-NP生成初始区域后，使用**C-IRIS**[Dai et al., 2024](https://journals.sagepub.com/doi/abs/10.1177/02783649231201437) 进行严格认证。
- 记录每个凸区域的H-表示（半平面表示）：$S_i = \{x \mid A_i x \leq b_i\}$。

**步骤3：构建重叠图**
- 计算每对凸区域$S_i$和$S_j$是否相交。这可以通过求解线性规划或使用多边形碰撞检测库（如Gilbert-Johnson-Keerthi算法）来完成。
- 如果两个区域相交，则在GCS图中的对应顶点之间添加一条边。
- 这个步骤的计算复杂度为$O(R^2)$，其中$R$是凸区域数量，是主要瓶颈之一。

**步骤4：GCS图构建与优化**
- 使用Drake的`GraphOfConvexSets`类[Drake Documentation](https://drake.mit.edu/doxygen_cxx/classdrake_1_1geometry_1_1optimization_1_1_graph_of_convex_sets.html) 构建图。
- 每个顶点关联一个凸集$S_i$和一个连续变量$x_i \in S_i$（通常对应Bézier曲线的控制点）。
- 每条边关联一个凸成本函数$\ell(x_i, x_j)$（如最小化轨迹长度、时间或能量）。
- 求解**混合整数凸规划（MICP）**。通常，求解**凸松弛（Convex Relaxation）** + **舍入（Rounding）** 即可获得高质量解，无需分支定界。

### 2.6 潜在挑战与应对策略

| 挑战 | 描述 | 应对策略 |
|------|------|---------|
| **窄通道采样困难** | PRM在高维空间的窄通道中采样密度低，导致这些区域没有种子点，凸集无法覆盖。 | 使用**桥测试**或**高斯采样**策略；或采用VCC的可见性团方法，它天然能处理窄通道（因为可见性图中窄通道内的点可能形成小团）。 |
| **凸区域冗余** | 大量随机种子点导致IRIS生成大量重叠区域，GCS图规模膨胀。 | 使用**聚类**（如K-means或DBSCAN）对种子点进行预处理；或采用VCC的团提取方法，直接获得高质量的种子。 |
| **计算开销** | 在C_free中运行大量IRIS优化代价高昂。 | 使用**IRIS-ZO**（零阶优化，可大规模并行）；使用**GPU加速**（如EI-ZO算法[Werner et al., 2025](https://sites.google.com/view/fastiris) 实现17倍加速）。 |
| **高维空间尺度灾难** | 凸分解在高维空间（>10D）中质量下降，IRIS产生的小区域过多。 | 采用**学习驱动的方法**（如ILD[Yang et al., 2026](https://arxiv.org/abs/2606.12027) 或学习特征场分解），或使用**GCS*等隐式搜索方法**避免显式构建全图。 |
| **凸集不一定覆盖整个C_free** | 生成的凸集可能存在空洞，导致GCS无解。 | 采用**迭代方法**：运行GCS后，在无解区域补充采样和IRIS膨胀；或使用**VCC**的覆盖确保机制，直到覆盖率达到目标阈值。 |

---

## 3. GCS算法的其他优化思路

除了PRM+凸分解方案，近年来GCS领域涌现了大量创新性优化思路，从不同角度解决了GCS的效率、可扩展性和适用性问题。

### 3.1 搜索导向优化：IxG* 与 GCS*

**IxG (Incremental Search on GCS) 和 IxG*** [RSS 2024](https://arxiv.org/html/2410.08909v1) 的核心思想是：**GCS问题的解通常只涉及图中小部分凸集**。因此，不必一次性构建并求解整个MICP，而是将图搜索与凸轨迹优化交错进行，仅在探索到的部分图上进行优化。IxG* 通过允许重扩展和剪枝，提供了有界次优性保证。

- **优势**：在2D迷宫环境中，IxG* 的求解时间为1.26秒，而标准GCS用时6.73秒；在15m UAV森林场景中，IxG* 仅需1.85秒，GCS需要112.87秒。对于18-DOF的双臂操作任务，GCS甚至无法加载问题，而IxG* 平均用时31.62秒。
- **适用场景**：凸集数量巨大（数千甚至数万）的复杂环境。

**GCS*** [WAFR 2024](https://link.springer.com/chapter/10.1007/978-3-031-77521-5_10) 将A*搜索推广到GCS设置。它面临的核心挑战是**标准A*的支配性剪枝（dominance pruning）在GCS中失效**，因为到某个顶点的代价是一个凸函数，而不是一个标量。GCS* 提出了两种剪枝策略：`ReachesCheaper`（基于代价支配，保证最优性）和`ReachesNew`（基于可达性支配，保证完备性但次优）。它支持多面体包容和采样两种实现。

- **优势**：可以处理高达$10^9$个凸集和$10^{18}$条边的图（如STACK任务），在21.9秒内找到解，这是传统方法完全无法企及的规模。
- **适用场景**：凸集数量极其庞大，但解路径经过的凸集很少的场景（如任务与运动规划中有大量组合分支）。

### 3.2 时间维度扩展：ST-GCS（Space-Time GCS）

**ST-GCS**[Tang et al., 2025](https://arxiv.org/abs/2503.00583) 将GCS扩展到时空域，用于**多机器人运动规划**。核心创新包括：
1. **时空凸集**：在时空域中定义碰撞自由区域，同时处理空间和时间约束。
2. **精确凸分解（ECD）**：动态地将高优先级机器人的预留轨迹作为障碍物，分解时空域凸集。
3. **最佳优先搜索（BFS）求解器**：使用可采纳启发式函数和支配性检查，部分评估候选路径。

- **优势**：在多机器人场景中，ST-GCS比基于采样的方法快几个数量级。例如，它能解决100个机器人的规划问题，用时仅约95.9秒，成功部署于9台差分驱动机器人的室内重排任务。
- **适用场景**：多机器人协同、动态环境下的运动规划。

### 3.3 非欧几里得空间扩展：GGCS（Geodesically Convex Sets）

**GGCS**[Cohn et al., RSS 2023](https://www.roboticsproceedings.org/rss19/p097.pdf) 将GCS从欧几里得空间推广到黎曼流形。它证明了**在平坦流形（零曲率）**上，如SE(2)、环面（T^n）等，GGCS与GCS具有相同的理论保证（松弛紧致性、全局最优性）。它使用**黎曼法坐标**（Riemannian normal coordinates）和**凸性半径**（convexity radius）来保证流形上的测地凸性。

- **优势**：能够处理具有连续旋转关节的机器人，其配置空间是环面而非欧几里得空间。在16-DOF的PR2双臂移动操作手上，GGCS能生成全局最优或近优轨迹，而传统方法难以保证。
- **局限**：**正曲率流形**（如SO(3)）上的距离函数是非凸的，GGCS无法直接处理，需要进一步研究。

### 3.4 非凸约束处理：非凸GCS与“扭曲校正”

**非凸GCS**[von Wrangel, MIT Thesis, 2024](https://dspace.mit.edu/handle/1721.1/156598) 通过引入**凸代理（convex surrogate）**（如McCormick包络、线性近似）来扩展GCS，使其能够处理加速度、加加速度、任务空间约束和动态障碍物等非凸约束。它采用**分层GCS结构**：将不同任务阶段或替代路径组合成子图，然后通过“凸全局优化 + 非凸局部舍入”的混合策略求解。

- **优势**：可以在Spot四足机器人上实现50维协调运动，处理多阶段操作任务。

**“扭曲校正”方法**[Garg et al., 2024] 解决了非线性参数化（如欧拉角、运动学链）导致优化景观扭曲的问题。它通过引入非凸目标函数来“校正”这种扭曲，同时保持可行性保证，从而显著缩短路径长度和轨迹持续时间。

### 3.5 多查询场景优化：两阶段SPP求解

**多查询SPP**[Morozov et al., WAFR 2024](https://arxiv.org/abs/2409.19543) 针对需要在**静态环境中反复求解不同起点-终点规划问题**的场景。它采用两阶段方法：
1. **离线阶段**：使用半定规划（SDP）在整个GCS图上合成一个粗略的、凸的代价函数下界。
2. **在线阶段**：使用这个下界指导一个贪婪的多步前瞻策略，通过求解短期凸规划来增量构建路径。

- **优势**：离线阶段仅需约6秒，在线查询仅需2-11毫秒，比从零开始求解GCS快两个数量级，比短路PRM快110倍，且平均路径长度仅增加7%。
- **适用场景**：仓库机器人、自动驾驶等需要频繁重规划的任务。

### 3.6 旅行商问题扩展：GHOST

**GHOST**[Tang et al., AAAI 2026](https://arxiv.org/abs/2511.06471) 将GCS推广到旅行商问题（TSP），即需要顺序访问多个目标点的场景。它采用层次化框架，结合组合巡回搜索和凸轨迹优化。

- **优势**：比统一的MICP公式快几个数量级，能处理最多25个顶点、50条边的实例，而MICP在小型实例上就失效。在62.0-95.2%的案例中找到最优解，平均误差仅0.03-0.25%。
- **适用场景**：覆盖规划、巡检规划、任务与运动规划（TAMP）。

### 3.7 学习驱动方法

**ILD（Invertible Latent Decomposition）**[Yang et al., 2026](https://arxiv.org/abs/2606.12027) 通过学习一个可逆映射，将C_free映射到潜在空间中的显式凸多面体并集。它使用可逆神经网络，保证潜在空间中的凸区域映射回C_free后仍是有效的碰撞自由区域。它使用**可见性引导采样（VGS）** 来改善区域间连通性，并通过**测试时微调**来纠正假阳性。

- **优势**：在14-DOF双臂操作任务中，ILD比IRIS快100倍以上，且覆盖率和连通性更好。
- **适用场景**：需要快速、覆盖广泛的凸分解，且环境结构相对固定的场景。

**学习凸分解特征场**[Yang et al., CVPR 2026](https://cvpr2026.thecvf.com/) 使用自监督对比学习，在3D形状上学习连续特征，使得聚类这些特征就能得到好的凸分解。该方法可泛化到开放世界物体，并实现5倍加速的碰撞检测。

### 3.8 GPU加速方法

**EI-ZO (Efficient IRIS-ZO)** [Werner et al., RSS 2025](https://sites.google.com/view/fastiris) 将IRIS-ZO算法在GPU上大规模并行化。它利用零阶优化仅需碰撞检测器的特性，在GPU上同时处理大量种子点或碰撞点。

- **优势**：比CPU上的IRIS-NP快约17倍，可靠性提高27.9%。在消费级GPU上，可以在几十毫秒内生成一个高质量凸集。
- **适用场景**：**在线运动规划**，即在机器人运行时动态生成凸集，应对动态环境或模型变化。

---

## 4. 结论与展望

**对于PRM + 凸分解的核心方案**：
直接使用标准PRM图的连通结构进行凸分解，在理论基础上弱于已经存在的**VCC（可见性团覆盖）算法**。VCC使用的可见性图更准确地反映了“凸性”这一概念，其团分解具有更强的理论支撑，且实验效果显著优于基于PRM的替代方案。因此，**建议放弃“直接使用PRM图连通性进行凸分解”的思路，转而采用“PRM采样 + 可见性图 + 团分解 + IRIS”的VCC范式**。如果必须使用PRM，则将其简化为**采样工具**，仅用于生成IRIS的种子点，但必须配合聚类或团筛选来避免冗余，并使用桥测试等策略提高窄通道采样质量。

**对于其他优化思路**：
GCS领域正在快速发展，涌现了多种互补的优化方向，它们分别解决了GCS的不同瓶颈：

- **搜索效率**：IxG* 和 GCS* 是解决“凸集数量巨大”问题的最佳方案，它们通过隐式搜索避免构建整个MICP，适用于复杂环境下的单次规划。
- **多机器人/动态环境**：ST-GCS 是处理多机器人协同和时空约束的正确框架。
- **非欧几里得/高维空间**：GGCS 和 IRIS on Manifolds 为处理流形上的规划提供了理论保证。
- **非凸约束**：非凸GCS通过凸代理和混合优化策略扩展了GCS的适用范围。
- **多查询/重规划**：两阶段SPP方法为静态环境下的频繁规划提供了实时能力。
- **速度/在线应用**：GPU加速的IRIS-ZO（EI-ZO）使得在线凸集生成成为可能，是实现完全在线GCS规划的关键技术。
- **学习驱动**：ILD等学习范式为超快速凸分解提供了新的可能性，但泛化性和保证性仍需进一步验证。

**最终建议**：一个完整的、自动化的GCS运动规划系统，应结合多种技术。例如，**离线阶段使用VCC生成高质量、覆盖广泛的凸集库；在线阶段，使用GCS*或两阶段SPP方法进行快速重规划；对于动态变化的环境，使用GPU加速的IRIS-ZO在线生成新凸集；对于高维复杂系统，考虑使用GGCS或非凸GCS扩展。** 这种组合式方法能够充分发挥GCS框架的潜力，实现从“手动播种”到“全自动、高效、鲁棒”的范式转变。

---

### 5. 来源

[1] Marcucci et al., "Motion Planning around Obstacles with Convex Optimization" (Science Robotics, 2023): https://www.science.org/doi/10.1126/scirobotics.adf7843

[2] Werner et al., "Approximating Robot Configuration Spaces with few Convex Sets using Clique Covers of Visibility Graphs" (ICRA 2024): https://wernerpe.github.io/publication/cliquese

[3] Marcucci et al., "Shortest Paths in Graphs of Convex Sets" (SIAM Journal on Optimization, 2024): https://arxiv.org/abs/2101.11565

[4] Petersen & Tedrake, "Growing Convex Collision-Free Regions in Configuration Space using Nonlinear Programming" (IRIS-NP, 2023): https://arxiv.org/abs/2303.14737

[5] Werner et al., "Faster Algorithms for Growing Collision-Free Convex Polytopes in Robot Configuration Space" (IRIS-ZO, IRIS-NP2, 2024): https://arxiv.org/html/2410.12649v1

[6] Deits & Tedrake, "Computing large convex regions of obstacle-free space through semidefinite programming" (WAFR 2014): https://groups.csail.mit.edu/robotics-center/public_papers/Deits14.pdf

[7] Dai et al., "Certified polyhedral decompositions of collision-free configuration space" (C-IRIS, 2024): https://journals.sagepub.com/doi/abs/10.1177/02783649231201437

[8] Werner et al., "Implicit Graph Search for Planning on Graphs of Convex Sets" (IxG, IxG*, RSS 2024): https://arxiv.org/html/2410.08909v1

[9] Chew Chia et al., "GCS*: Forward Heuristic Search on Implicit Graphs of Convex Sets" (WAFR 2024): https://link.springer.com/chapter/10.1007/978-3-031-77521-5_10

[10] Tang et al., "Space-Time Graphs of Convex Sets for Multi-Robot Motion Planning" (ST-GCS, 2025): https://arxiv.org/abs/2503.00583

[11] Cohn et al., "Non-Euclidean Motion Planning with Graphs of Geodesically-Convex Sets" (GGCS, RSS 2023): https://www.roboticsproceedings.org/rss19/p097.pdf

[12] von Wrangel, "Guiding Nonconvex Trajectory Optimization with Hierarchical Graphs of Convex Sets" (MIT Thesis, 2024): https://dspace.mit.edu/handle/1721.1/156598

[13] Morozov et al., "Multi-Query Shortest-Path Problem in Graphs of Convex Sets" (WAFR 2024): https://arxiv.org/abs/2409.19543

[14] Tang et al., "GHOST: Solving the Traveling Salesman Problem on Graphs of Convex Sets" (AAAI 2026): https://arxiv.org/abs/2511.06471

[15] Yang et al., "Learning Unions of Convex Sets via Invertible Latent Decomposition for Path Planning" (ILD, 2026): https://arxiv.org/abs/2606.12027

[16] Yang et al., "Learning Convex Decomposition via Feature Fields" (CVPR 2026): https://cvpr2026.thecvf.com/

[17] Werner et al., "Superfast Configuration-Space Convex Set Computation on GPUs for Online Motion Planning" (EI-ZO, RSS 2025): https://sites.google.com/view/fastiris

[18] Drake Documentation - GraphOfConvexSets Class: https://drake.mit.edu/doxygen_cxx/classdrake_1_1geometry_1_1optimization_1_1_graph_of_convex_sets.html

[19] Hsu et al., "The Bridge Test for Sampling Narrow Passages with Probabilistic Roadmap Planners" (ICRA 2003): https://ieeexplore.ieee.org/document/1241778

[20] Kavraki et al., "Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces" (IEEE T-RA, 1996): https://ieeexplore.ieee.org/document/508439

[21] Karaman & Frazzoli, "Sampling-based Algorithms for Optimal Motion Planning" (PRM*, RRT*, 2011): https://journals.sagepub.com/doi/10.1177/0278364911406761

[22] Garg et al., "Planning Shorter Paths in Graphs of Convex Sets by Undistorting...": https://dspace.mit.edu/handle/1721.1/156598

[23] Tang et al., "Search-Based Spatiotemporal and Multi-Robot Motion Planning on Graphs of Space-Time Convex Sets": https://arxiv.org/abs/2607.00444

[24] FastIris Project Page: https://sites.google.com/view/fastiris

[25] Marcucci, "Graphs of Convex Sets with Applications to Optimal Control and Motion Planning" (MIT PhD Thesis, 2024): https://hdl.handle.net/1721.1/156598

[26] MIT News: "A new optimization framework for robot motion planning" (Nov 2023): https://news.mit.edu/2023/new-optimization-framework-robot-motion-planning-1130

[27] Tommy Cohn Blog: "Reimplementing GCS (Shortest Paths in Graphs of Convex Sets)": https://blog.tommycohn.com/2022/09/reimplementing-gcs-shortest-paths-in.html

[28] Werner et al., "Fast Path Planning Through Large Collections of Safe Boxes" (IEEE T-RO, 2024): https://ieeexplore.ieee.org/

[29] Boor et al., "The Gaussian Sampling Strategy for Probabilistic Roadmap Planners" (ICRA 1999): https://ieeexplore.ieee.org/document/772755

[30] Sun et al., "Narrow Passage Sampling for Probabilistic Roadmap Planning" (IEEE T-RO, 2005): https://ieeexplore.ieee.org/document/1549754

[31] Geraerts & Overmars, "Sampling Techniques for Probabilistic Roadmap Planners" (Technical Report, 2004): https://www.researchgate.net/publication/228580996

[32] Hauser, "Lazy Collision Checking in Asymptotically-Optimal Sampling-Based Motion Planning" (ICRA 2015): https://ieeexplore.ieee.org/document/7139645

[33] Janson et al., "Deterministic Sampling-Based Motion Planning: Optimality, Complexity, and Performance" (IJRR, 2018): https://journals.sagepub.com/doi/10.1177/0278364917735328

[34] LaValle et al., "On the Relationship Between Classical Grid Search and Probabilistic Roadmaps": https://www.researchgate.net/publication/228580996

[35] Amice et al., "Finding and Optimizing Certified, Collision-Free Regions in Configuration Space for Robot Manipulators" (C-IRIS, 2022): https://alexandreamice.github.io/publication/amice-2022-finding/amice-2022-finding.pdf

[36] Kreho et al., "GBur-IRIS: Leveraging Distance Information to Compute Collision-Free Volumes in Robot Configuration Space" (ICAT 2025): https://ieeexplore.ieee.org/document/11189269

[37] Cohn, "Constrained Bimanual Planning with Analytic Inverse Kinematics" (MIT Thesis, 2024): https://dspace.mit.edu/handle/1721.1/156598

[38] 2024 MIT 6.4210 Lecture: "Motion Planning around Obstacles with Convex Optimization": https://www.youtube.com/watch?v=FoqAAgqgn-o
