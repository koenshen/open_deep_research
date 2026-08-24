# 基于PRM与凸分解自动生成GCS安全凸集的系统性研究

## 引言

Graph of Convex Sets（GCS）是近年来运动规划领域的重要突破，它将离散图搜索与连续凸优化有机结合，在多种机器人平台上展现出卓越的规划性能。然而，GCS框架当前面临一个关键瓶颈：其所需的凸安全区域（凸集）主要依赖人工手动播种结合离线自动化工具生成，这种方式不仅耗时，而且难以保证对自由空间的充分覆盖，尤其是在复杂或高维的配置空间中。

本报告基于对GCS算法、PRM变体、凸区域生成算法（IRIS家族）以及多种替代方法的系统性研究，深入分析提出的“PRM + 凸分解 → 自动生成凸集 → GCS”管道的技术可行性，提供详细的实施路线图，并全面比较其他优化策略。研究旨在为GCS自动化提供一套完整、可操作的技术方案。

---

## 一、技术可行性分析

### 1.1 理论基础的直接支撑

该管道的理论基础在GCS原始文献中已被明确阐述。Tobia Marcucci等人的Science Robotics论文指出：“GCS可以被视为PRM的泛化，其中每个无碰撞样本被扩展为一个无碰撞凸区域，并尽可能向障碍物膨胀。”[1] 这一陈述直接建立了PRM采样与凸区域生成之间的理论联系——PRM提供的离散无碰撞点正是IRIS算法所需的种子点。

GCS的混合整数凸规划（MICP）公式化保证了在凸分解内求解的全局最优性。研究表明，在95%的测试环境中，GCS设计的轨迹与全局最优解的差距δopt ≤ 1%，最差情况仅为δopt = 2.9% [1]。这意味着，只要自动生成的凸集能够充分覆盖相关自由空间，GCS就能提供高质量的规划结果。

### 1.2 关键组件已被独立验证

管道中的每个核心组件在文献中都有充分的验证：

- **PRM及其变体**：由Kavraki于1996年提出的PRM算法是成熟的采样规划方法，具有概率完备性[2]。桥测试PRM（Randomized Bridge Builder）通过检查短线段端点碰撞而中点无碰撞来增加窄通道中的样本密度，有效解决了标准PRM在窄通道中的困难[3]。

- **IRIS凸区域生长算法**：Deits和Tedrake（2014）提出的IRIS算法通过交替优化分离超平面和最大内切椭球，从种子点开始生长出最大体积的无碰撞凸多面体[4]。其后续版本IRIS-NP（2023）将非线性规划引入，可处理配置空间到任务空间的非线性运动学映射[5]。

- **GCS求解器**：GCS已集成在Drake开源机器人框架中，并经过7-DOF机械臂、14-DOF双臂操作、四旋翼飞行器等复杂系统的验证，其求解时间通常在秒级[1]。

### 1.3 直接验证性工作

**EI-ZO（Edge Inflation Zero-Order）算法**是这一管道最直接的验证。该算法将无碰撞线段（而非点）膨胀为概率无碰撞的凸多面体，并保证膨胀后的区域包含原线段[6]。这恰好对应了将PRM的边（无碰撞线段）膨胀为凸集的操作。实验表明，EI-ZO比非线性轨迹优化基线快17.1倍，可靠性提升27.9%，在KUKA iiwa 7机器人上得到验证[6]。

**Mark Petersen的博士论文**直接呈现了几乎相同的管道：使用IRIS-NP将自由空间分解为凸无碰撞区域，然后使用GCS轨迹优化进行规划，最后使用TOPP-RA进行动态可行性调整[7]。这一工作从实践上验证了管道的可行性。

### 1.4 结论：技术可行

综合以上分析，PRM + 凸分解 → GCS管道在理论上是刚性的，在实践上已有多个独立工作验证了其核心步骤。该管道不仅是可行的，而且是对GCS框架的合理延伸和自动化改进。

---

## 二、实施路线图

### 2.1 环境表示与碰撞检测

**第一步：建立适用于PRM和IRIS的环境模型**

环境表示需要同时支持PRM的碰撞检测和IRIS的凸区域生长。推荐方案：

- **使用有符号距离场（SDF）或占据网格**：对工作空间进行离散化，支持快速碰撞查询。对于IRIS-NP，需要支持从配置空间到工作空间的运动学映射。
- **利用Drake的几何优化模块**：Drake提供了HPolyhedron、Hyperellipsoid、ConvexSet等抽象类，以及IRIS区域生成本身，可直接用于凸集合表示和操作[8]。
- **处理非凸障碍物**：IRIS-NP通过非线性规划处理从配置空间到工作空间的非线性映射，无需显式计算配置空间障碍物，这对于具有复杂运动学关系的机器人至关重要[5]。

### 2.2 PRM采样与图构建

**第二步：生成无碰撞样本并构建连通图**

PRM的采样策略直接影响后续凸集生成的质量。推荐采用混合采样策略：

- **基础采样器**：使用均匀随机采样作为基础，确保对整个自由空间的基本覆盖。
- **桥测试采样器**：针对窄通道场景，实现桥测试（RBB）采样器，在窄通道中增加样本密度[3]。桥测试通过检查三个点：如果线段两端点碰撞而中点无碰撞，则接受中点为里程碑。
- **自适应采样**：根据环境复杂度动态调整采样密度。在障碍物密集区域增加采样，在开阔区域减少采样。

**关键参数设置**：
- 节点数量：根据环境复杂度动态调整，一般建议从数百到数千个节点
- 连接距离：基于最近邻（k-NN）或半径阈值（r）连接节点。半径r应足够大以保证连通性，但又不能过大导致过度连接
- 局部规划器：使用直线插值，检查整条路径是否无碰撞

**可视化建议**：构建PRM图后，应可视化节点分布和边，检查是否存在明显的覆盖盲区。

### 2.3 种子点选择策略

**第三步：从PRM图中选择IRIS种子点**

种子点选择是决定凸集质量的关键步骤。需要避免冗余种子，同时确保覆盖完整性：

- **策略一：所有节点作为种子**。最直接的方法，但可能导致大量冗余凸集，增加GCS求解复杂度。
- **策略二：聚类后选代表**。对PRM节点进行聚类，每个聚类选择一个种子（如聚类中心或最远离障碍物的点）。这可以显著减少IRIS调用次数。
- **策略三：基于连通性选择**。选择高度连接的枢纽节点、位于瓶颈区域的节点、或位于路径关键转折点的节点。
- **策略四：稀疏化后再播种**。使用SPARS/SPARS2算法构建稀疏道路图，其节点数量远少于PRM*，但保持渐近近优性。SPARS2的节点添加概率随时间收敛到0，意味着最终图大小有限[9]。

**种子质量评估**：好的种子应位于自由空间中心区域，远离障碍物，具有较大的ϵ-清晰距离。IRIS算法从种子点向外生长，靠近边界的种子会产生较小的凸集。

### 2.4 凸区域生长

**第四步：使用IRIS/IRIS-NP从种子点生长凸集**

推荐使用**IRIS-NP2**或**IRIS-ZO**作为主要区域生长算法，它们在速度和区域质量上均优于原始IRIS-NP：

- **IRIS-NP2**：采用贪心或射线采样策略高效决定哪些碰撞对需要考虑，而不是遍历所有对。在“精确”设置下，IRIS-NP2（贪心）比IRIS-NP快33.9倍，且使用少2.4倍的超平面[10]。
- **IRIS-ZO**：使用零阶优化（仅碰撞检测，无梯度信息），可通过GPU并行化获得额外一个数量级的加速。在“快速”设置下，比IRIS-NP快11.9-15.5倍[10]。

**关键参数**：
- 终止条件：基于Chernoff界的概率终止条件，允许用户指定可允许的碰撞体积分数ε和置信度δ，消除了IRIS-NP中调参的困难[10]。
- 最大迭代次数：一般5-10次迭代后区域体积增长趋于收敛。
- 非线性约束：对于具有复杂运动学关系的机器人，应使用IRIS-NP处理非线性配置空间-任务空间映射。

**并行化**：由于每个种子点的IRIS生长是独立的，可以轻松并行化。IRIS-ZO的GPU版本可以同时处理大量种子点。

### 2.5 集合合并与修剪

**第五步：合并重叠区域，去除冗余集合**

IRIS从多个种子点生长出的区域往往存在大量重叠，需要合并和修剪以构建高效的GCS图：

- **去除完全包含**：如果一个凸集完全包含在另一个凸集中，去除较小的集合。
- **合并高度重叠**：如果两个凸集的重叠体积超过阈值（如各占50%以上），考虑合并为它们的凸包（需验证合并后仍无碰撞）。
- **保持连通性**：确保合并后的凸集集合仍然覆盖相关的连通分量。GCS的“相交图”公式依赖凸集间的重叠来定义边[1]。

**GCS图公式选择**：
- **重叠图公式**：将控制点放置在每个自由区域，并在重叠区域约束端点相等。这是推荐的主要公式，因为它参数化更广泛的轨迹类别，支持更广泛的优化问题[11]。
- **共轭图公式**：将无碰撞集合的交集作为图节点。当大量凸集重叠时，共轭图的大小会显著增长，可能抵消预处理优势[11]。

### 2.6 GCS图构建与求解

**第六步：构建GCS图并求解轨迹优化**

- **顶点**：每个凸集对应一个顶点，每个顶点关联一个凸集X_i ⊂ ℝ^d，需要选择点x_i ∈ X_i。
- **边**：连接存在重叠的凸集。边约束确保轨迹连续性——在边界处的点必须位于两个凸集的交集中。
- **成本函数**：使用路径长度（ℓ_{i,j}(x_i, x_j) = |x_i - x_j|₂）或时间成本。
- **轨迹参数化**：使用Bézier曲线，利用其凸包性质保证无碰撞。Bézier曲线的凸包性质允许通过线性约束对所有时间点的位置和导数进行约束[12]。

**GCS求解**：
- 首先求解凸松弛（通常为LP或SOCP），然后使用随机舍入算法恢复整数解。
- 对于大规模图，可以使用A*-GCS、IxG/IxG*等高效搜索算法，这些算法比全批量优化快数个数量级[13]。
- 后处理：使用Projected Gradient Descent（PGD）优化非凸目标（如真实距离），同时保持凸约束，可进一步缩短路径长度20.60%，减少轨迹时间31.02%[14]。

---

## 三、关键挑战与应对策略

### 3.1 凸集重叠管理

**挑战**：重叠是双刃剑——需要重叠确保连通性，但过多重叠使图变得稠密，增加优化复杂度。共轭图公式尤其敏感，当大量凸集重叠时，图大小会显著增长[11]。

**应对策略**：
- 采用重叠图公式，它对重叠的处理更优雅，参数化更灵活[11]。
- 使用IxG/IxG*等隐式图搜索方法，避免显式构建完整GCS图，仅优化搜索路径上的凸集[13]。
- 在合并阶段保持适度重叠（约10-20%的体积重叠），既保证连通性又不增加过多冗余。

### 3.2 覆盖完整性

**挑战**：确保凸集的并集覆盖连通自由空间。GCS的完备性受限于凸分解的保守性，如果分解遗漏了自由空间区域，GCS可能找不到路径[1]。

**应对策略**：
- 使用足够多的种子点，确保PRM样本覆盖整个自由空间。
- 在规划阶段，如果GCS求解失败，可以检测到失败区域，并在该区域增加种子点重新生长凸集——形成迭代反馈循环。
- 考虑使用C-IRIS进行严格认证，它提供了首个在任意维度中非零体积无碰撞集的严格证书[15]。
- 覆盖质量评估：通过蒙特卡洛采样，估计自由空间中被凸集覆盖的比例。

### 3.3 窄通道处理

**挑战**：窄通道对PRM和凸区域生长都是挑战。PRM在窄通道中采样困难，IRIS在窄通道中生长出的区域较小。

**应对策略**：
- 使用桥测试PRM，其设计目标就是增加窄通道中的样本密度[3]。
- 采用EI-ZO方法（将边膨胀为凸集），它直接膨胀PRM的无碰撞边，确保凸集包含整个边，这对窄通道特别有效，因为边本身横穿了通道[6]。
- 使用IRIS-NP，它在窄通道和杂乱环境中表现出色[5]。
- 考虑ST-GCS的精确凸分解方案，它通过避免随机采样，系统性地覆盖整个自由空间，在窄通道中具有独特优势[16]。

### 3.4 计算复杂度

**挑战**：PRM采样、IRIS区域生长、GCS优化三者的计算开销累积。

**应对策略**：
- **IRIS阶段**：使用IRIS-ZO和GPU并行化，单次区域生长时间从约1分钟降至亚秒级[6]。
- **GCS阶段**：使用IxG/IxG*等高效搜索算法，比标准GCS快数个数量级[13]。
- **种子减少**：使用SPARS/SPARS2构建稀疏道路图，节点数量比PRM*少数个数量级，从而减少IRIS调用次数[9]。
- **在线/离线分工**：将PRM构建和IRIS区域生长作为离线预处理，GCS求解作为在线查询。对于多查询场景，这种分工非常高效。

### 3.5 高维缩放

**挑战**：PRM和IRIS都受维度诅咒影响。PRM的期望样本数量随维度指数增长，IRIS在高维配置空间中的区域生长也更复杂。

**应对策略**：
- GCS相比PRM的优势在于，将点样本替换为大凸区域，减少了组合复杂度。在7-DOF机械臂上，GCS比标准PRM和带捷径的PRM都更快找到更短的轨迹[1]。
- IRIS-NP已在14-DOF双臂操作手上得到验证，可生成合理的无碰撞区域[5]。
- 对于超高维问题（如20+ DOF），考虑使用IxG*等隐式图搜索方法，它通过仅搜索部分路径来避免全图优化[13]。
- 对于具有连续旋转关节的机器人，使用GGCS（Geodesically-Convex Sets）处理非欧几里得配置空间[17]。

---

## 四、替代优化策略

### 4.1 单元分解方法

**精确单元分解**（梯形分解、三角剖分）：将自由空间精确分解为凸单元，适用于2D低维空间。优点是覆盖完全，理论保证强；缺点是在高维空间中不可行，计算复杂度随维度指数增长[18]。

**近似单元分解**（四叉树、八叉树、体素网格）：将空间分层离散化，分辨率完备。优点是实现简单，成熟；缺点是内存需求随维度指数增长，适用于3D及以下空间[18]。

**BSP/KD树分解**：递归使用超平面分割空间，生成凸子空间。优点是确定性、精确（对多边形环境）；缺点是构建耗时，高维中复杂度高[19]。

**适用场景**：对于2D/3D的低维配置空间，单元分解方法可作为PRM的替代，提供更确定性的自由空间分解。

### 4.2 优化基区域生长（无需PRM）

**可见性团覆盖（VCC）**：在自由空间中随机采样点，构建可见性图，然后求解MaxClique整数规划得到团覆盖，每个团对应一个凸集。实验表明，对于7-DOF机械臂，VCC仅需约46个区域和1小时即可覆盖70%的自由空间，而传统方法需要10倍区域和10倍时间[20]。

**最优凸覆盖**：将问题建模为椭球、多面体和中间路径点的联合优化，迭代更新找到最优解。在5-10次迭代内，覆盖体积可达最大体积的90%以上[21]。

**适用场景**：当需要比PRM更系统的覆盖，但又不想使用单元分解的高维不可行方法时，VCC是最有前景的替代方案。

### 4.3 学习方法

**Neural GCS**：使用图注意力网络（GAT）预测候选路径，替代昂贵的凸松弛求解。在四旋翼规划中，求解时间从28.8秒降至0.027秒（1000倍加速），保持100%成功率[22]。

**学习凸分解**（NVIDIA Research）：通过自监督学习预测连续特征场，聚类后得到凸分解。在3D形状分解中，凸近似使碰撞检测快5倍[23]。

**MPNet（运动规划网络）**：编码器-规划器架构，直接从环境编码、起始和目标生成无碰撞路径，用于自适应采样[24]。

**适用场景**：对于重复性规划任务（环境布局相似），Neural GCS是最具潜力的加速方法。对于需要跨不同几何形状泛化的任务，学习凸分解值得关注。

### 4.4 混合方法

**EI-ZO + DRM管道**：将动态道路图（DRM）用于路径查找，EI-ZO用于膨胀路径为凸集，分解基运动规划器（DBMP）用于轨迹优化。整个管道平均运行时间0.82秒，其中凸集构建仅0.12秒[6]。

**多分辨率GCS**：使用粗粒度GCS进行全局规划，细粒度局部规划器进行精细调整。在宽广区域使用大凸集，在狭窄区域使用小凸集。

**增量/任意时间方法**：快速多查询GCS使用离线SDP计算成本下界，在线增量生成可行解。在仓库场景中，比现有方法快100倍[25]。

**适用场景**：混合方法通常是最实用的选择，结合了不同方法的优势。

### 4.5 方法比较表格

| 方法 | 理论可靠性 | 实现复杂度 | 预期性能 | 最佳适用场景 |
|------|-----------|-----------|---------|------------|
| **PRM + IRIS（本文）** | 高 | 中等 | 良好 | 中等维度、多查询场景 |
| **精确单元分解** | 很高 | 高 | 低维高性能 | 2D/3D多边形环境 |
| **BSP/KD树** | 高 | 中等 | 静态环境佳 | 多边形环境、离线预处理 |
| **VCC** | 中等 | 高 | 区域数少10倍 | 高维、需系统覆盖 |
| **最优凸覆盖** | 高 | 中等 | 质量高 | 复杂环境、需高质量轨迹 |
| **Neural GCS** | 中等 | 高 | 1000倍加速 | 重复性任务、环境相似 |
| **EI-ZO + DRM** | 中高 | 中等 | 17倍加速 | 在线规划、GPU可用 |
| **IxG/IxG*** | 很高 | 中等 | 数量级加速 | 大规模图、复杂初始条件 |
| **ST-GCS** | 高 | 高 | 多机器人场景优 | 多机器人、动态环境 |

---

## 五、结论与建议

### 5.1 核心结论

1. **PRM + 凸分解 → GCS管道在技术上是可行的**。该管道有坚实的理论基础（GCS本身就是PRM的泛化），各核心组件已被独立验证，且有直接验证性工作（EI-ZO、Petersen博士论文）。

2. **推荐的具体实施路径**：
   - 使用桥测试PRM生成高质量样本，确保覆盖窄通道
   - 使用SPARS/SPARS2进行稀疏化，减少种子数量
   - 使用IRIS-NP2或IRIS-ZO进行区域生长，利用GPU并行化
   - 使用重叠图公式构建GCS图
   - 使用IxG/IxG*进行高效搜索

3. **关键挑战**包括重叠管理、覆盖完整性、窄通道处理、计算复杂度和高维缩放，但每个挑战都有成熟的应对策略。

### 5.2 进阶建议

- **迭代反馈环**：将GCS的求解质量反馈到种子生成阶段。如果GCS返回的轨迹质量差或求解失败，在相关区域增加种子点重新生长凸集。
- **混合策略**：对于简单环境使用单元分解，对于复杂环境使用PRM+IRIS，对于重复性任务使用Neural GCS。根据环境特性动态选择方法。
- **安全关键应用**：使用C-IRIS提供严格认证的凸集，确保轨迹安全无碰撞[15]。
- **非欧几里得空间**：对于具有连续旋转关节的机器人，使用GGCS处理测地凸性[17]。

### 5.3 实施建议

建议从以下步骤开始实施：
1. 在Drake框架中实现基础的PRM采样器，验证其与GCS的接口兼容性
2. 实现桥测试采样器，处理窄通道场景
3. 集成IRIS-NP2（Drake已包含），从PRM节点生长凸集
4. 实现凸集合并与修剪，构建GCS图
5. 使用GcsTrajectoryOptimization求解
6. 进行基准测试，评估覆盖质量、求解时间、最优性差距

---

## 六、来源

[1] Motion planning around obstacles with convex optimization: https://www.researchgate.net/publication/375669203_Motion_planning_around_obstacles_with_convex_optimization

[2] Probabilistic roadmap - Wikipedia: https://en.wikipedia.org/wiki/Probabilistic_roadmap

[3] The bridge test for sampling narrow passages: https://ui.adsabs.harvard.edu/abs/2003robo....3..245H/abstract

[4] Computing Large Convex Regions of Obstacle-Free Space through Semidefinite Programming: https://www.semanticscholar.org/paper/Computing-Large-Convex-Regions-of-Obstacle-Free-Deits-Tedrake/661e755613b7abf6b2252ae530285629f888a70d

[5] Growing Convex Collision-Free Regions in Configuration Space using Nonlinear Programming: https://arxiv.org/abs/2303.14737

[6] Superfast Configuration-Space Convex Set Computation on GPUs for Online Motion Planning: https://arxiv.org/html/2504.10783v1

[7] Dynamic Collision-Free Motion Planning for Robotic Manipulation using Graphs of Convex Sets: https://dash.harvard.edu/entities/publication/8d05ca5f-b920-434e-bdf6-0bf3f455b3a4

[8] Drake: Geometry Optimization: https://drake.mit.edu/doxygen_cxx/group__geometry__optimization.html

[9] SPARS2 - Improving Sparse Roadmap Spanners: https://www.cs.rutgers.edu/~kb572/pubs/spars2.pdf

[10] Faster algorithms for growing collision-free convex regions: https://arxiv.org/html/2410.12649v1

[11] Differing Formulations of GCS for Motion Planning: https://blog.tommycohn.com/2023/03/differing-formulations-of-gcs-for.html

[12] Ch. 6 - Motion Planning - Robotic Manipulation: http://manipulation.csail.mit.edu/trajectories.html

[13] Implicit Graph Search for Planning on Graphs of Convex Sets: https://arxiv.org/html/2410.08909v1

[14] Planning Shorter Paths in Graphs of Convex Sets by Undistorting the Optimization Landscape: https://arxiv.org/html/2411.18913v2

[15] Certified Polyhedral Decompositions of Collision-Free Space: http://groups.csail.mit.edu/robotics-center/public_papers/Dai23.pdf

[16] Space-Time Graphs of Convex Sets for Multi-Robot Motion Planning: https://arxiv.org/html/2503.00583v1

[17] Non-Euclidean Motion Planning with Graphs of Geodesically-Convex Sets: https://arxiv.org/html/2305.06341v2

[18] Motion Planning with Cell Decomposition | Mobile Robotics: https://www.youtube.com/watch?v=WeHFTW1Quw8

[19] Binary Space Partitioning - Wikipedia: https://en.wikipedia.org/wiki/Binary_space_partitioning

[20] Approximating Robot Configuration Spaces with few Convex Sets using Clique Covers of Visibility Graphs: https://arxiv.org/html/2310.02875v2

[21] Optimal Convex Cover as Collision-free Space for Trajectory Generation: https://arxiv.org/html/2406.09631v1

[22] Accelerating Mixed Discrete-Continuous Motion Planning via Graph Attention Networks: https://arxiv.org/html/2608.15440v1

[23] Learning Convex Decomposition via Feature Fields: https://research.nvidia.com/labs/sil/projects/learning-convex-decomp

[24] Neural Motion Planning: https://ucsdarclab.com/projects/neural-motion-planning-mpnet

[25] Fast Multi-query Planning in Graphs of Convex Sets: https://dspace.mit.edu/entities/publication/a49aef2d-3455-4050-9b3e-96d34d29dd81
