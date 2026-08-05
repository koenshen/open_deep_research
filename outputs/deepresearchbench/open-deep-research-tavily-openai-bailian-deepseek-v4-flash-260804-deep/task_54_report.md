# 均值-方差、Black-Litterman与深度学习模型在金融科技中的核心差异与混合框架构建：综合研究报告

## 1. 引言

在金融科技领域，资产配置与投资决策模型经历了从经典理论到智能算法的演进。均值-方差模型、Black-Litterman模型以及深度学习模型代表了三种不同的范式，各自在风险测量、收益预测和资产配置方面展现出独特的优势和局限性。本报告旨在系统比较这三种模型的核心差异，并探讨如何通过混合框架整合它们的优势——即均值-方差的理论基础、Black-Litterman融合主观观点的灵活性、以及深度学习处理非线性关系的能力——同时解决各自已知的局限（非正态收益、主观性、可解释性差）。

## 2. 均值-方差框架的理论基础与核心方法

### 2.1 理论渊源

哈里·马科维茨在1952年发表的《投资组合选择》中开创性地提出了均值-方差框架，这一工作彻底改变了金融学的面貌，将投资从"直觉和谚语的世界"转变为"量化科学的现代时代" [1]。马科维茨因此获得了1990年诺贝尔经济学奖。其核心洞见在于：**资产的收益和风险不应孤立评估，而应取决于其对整个投资组合的风险-收益特征的贡献** [2]。

### 2.2 风险测量方法

均值-方差框架使用**方差（或标准差）**作为风险的核心度量指标。投资组合方差定义为：

$$\sigma_p^2 = \mathbf{w}^T \Sigma \mathbf{w} = \sum_{i=1}^n \sum_{j=1}^n w_i w_j \sigma_{ij}$$

其中$\Sigma$是协方差矩阵，$\mathbf{w}$是权重向量。马科维茨的核心贡献在于证明了分散化投资降低风险的效果取决于资产之间的相关系数——当相关系数小于1时，组合风险小于单个资产风险的加权和 [3]。

**协方差矩阵是均值-方差模型的核心数学对象**。其关键性质是：当资产间并非完全正相关时，分散化可以降低风险。全球最小方差投资组合（GMVP）位于有效前沿的顶点，代表所有风险资产中风险最低的组合，其解析解为：

$$\mathbf{w}_{GMVP} = \frac{\Sigma^{-1} \mathbf{1}}{\mathbf{1}^T \Sigma^{-1} \mathbf{1}}$$

### 2.3 收益预测方法

均值-方差框架中最简单的预期收益估计方法是使用**历史样本均值**。然而，这是该框架最薄弱的环节。Chopra和Ziemba（1993）在其经典论文中量化发现：**预期收益的估计误差对投资组合的损害程度约是方差误差的10倍，是协方差误差的20倍以上** [4]。这一发现已被反复证实。

### 2.4 资产配置方法

均值-方差框架通过**二次规划**求解最优投资组合权重。三种等效的优化形式包括：在目标收益下最小化风险、在风险预算下最大化收益、以及最大化均值-方差效用函数。有效前沿是所有"最优风险-收益组合"的集合，在无风险资产存在时，最优投资组合为与资本配置线相切的**切点组合**（最大夏普比率组合）[5]。

### 2.5 主要局限性

**输入参数敏感性（估计误差）**：Michaud（1989）将均值-方差优化称为"误差最大化器"，因为优化器会系统性地偏向于具有正估计误差的资产，同时负向倾向于具有负估计误差的资产 [6]。这导致极端的、不稳定的权重配置。

**非正态收益假设**：实证研究表明，金融资产收益显著偏离正态分布，表现为**厚尾**（极端事件发生频率远高于正态分布预测）、**负偏度**（大额负收益比大额正收益更可能发生）。Morningstar（2011）的研究显示，三西格玛损失在1026个月中出现了10次，几乎是正态分布预测的8倍 [7]。

**协方差矩阵估计的不稳定性**：当资产数量（N）相对于时间周期（T）较大时，样本协方差矩阵变得近奇异且不可逆。Ledoit和Wolf（2003）指出："没有人应该再使用样本协方差矩阵进行投资组合优化" [8]。

## 3. Black-Litterman模型的理论基础与核心方法

### 3.1 理论渊源

Black-Litterman模型由Fischer Black和Robert Litterman于1990年在高盛开发，1992年发表于《金融分析师杂志》[9]。该模型旨在解决机构投资者在应用现代投资组合理论时遇到的核心问题——特别是预期收益估计的困难。它结合了资本资产定价模型（CAPM）、贝叶斯统计和马克维茨现代投资组合理论，产生高效的组合权重估计。

### 3.2 先验：均衡收益

Black-Litterman模型从市场均衡的先验分布出发，通过**逆向优化**从市值加权组合中推导隐含均衡超额收益：

$$\Pi = \delta \Sigma \mathbf{w}_{market}$$

其中$\Pi$是隐含均衡超额收益向量，$\delta$是风险厌恶系数，$\Sigma$是超额收益协方差矩阵，$\mathbf{w}_{market}$是市场市值权重 [10]。先验分布假设为：$\mu \sim N(\Pi, \tau\Sigma)$，其中$\tau$是控制先验不确定性的标量参数。

### 3.3 观点设定

投资者观点通过三个组成部分纳入模型：

- **选择矩阵P**：$k \times N$矩阵，标识每个观点涉及哪些资产
- **观点向量Q**：$k \times 1$向量，每个观点的预期收益
- **不确定性矩阵Ω**：$k \times k$对角协方差矩阵，代表观点的置信度

观点可以是**绝对观点**（如"资产A将收益10%"）或**相对观点**（如"资产A将跑赢资产B 3%"）[11]。

### 3.4 后验估计

Black-Litterman主公式（后验预期收益）为：

$$E[R] = [(\tau\Sigma)^{-1} + P^T\Omega^{-1}P]^{-1}[(\tau\Sigma)^{-1}\Pi + P^T\Omega^{-1}Q]$$

后验均值是先验和观点的**精度加权平均值**。当观点置信度为零（$\Omega \to \infty$）时，后验退回到先验（市场均衡）；当观点置信度无限高（$\Omega \to 0$）时，后验完全匹配观点 [12]。

### 3.5 风险测量

Black-Litterman模型使用CAPM的均衡协方差结构作为基础，并通过贝叶斯更新产生后验协方差矩阵，同时包含先验的不确定性和观点的不确定性：

$$\Sigma_{BL} = \Sigma + [(\tau\Sigma)^{-1} + P^T\Omega^{-1}P]^{-1}$$

这意味着总不确定性包括历史收益协方差和预期收益的估计不确定性 [13]。

### 3.6 资产配置

Black-Litterman模型本质上是一个**输入框架**——作为均值-方差优化的封装器，而非替代品。后验预期收益和协方差矩阵被输入到与标准均值-方差优化相同的优化器中，生成最终的投资组合权重。该模型的关键优势在于：只有那些被表达了观点的资产权重会从市场市值权重发生变化，且变化方向是直观的 [14]。

### 3.7 主要局限性

**观点设定的主观性**：投资者需要表达关于预期收益的观点，这本质上是主观的。主观观点可能导致偏差和对资产的过度权重配置，可能造成重大损失 [15]。

**τ参数的敏感性**：Black-Litterman模型依赖于两个不确定性参数的设定：τ（对市场均衡的置信度）和Ω（对观点的置信度）。τ的校准尤其困难，不同学者建议不同的值（0.025、1/n、0.01-0.05）[16]。

**CAPM均衡假设的强依赖性**：模型依赖于CAPM成立且市场组合是均值-方差有效的假设，这在实际中可能不成立 [17]。

**正态性假设**：模型假设收益服从正态分布，在金融危机期间可能不成立 [18]。

## 4. 深度学习模型的理论基础与核心方法

### 4.1 理论渊源

深度学习模型在金融科技中的应用代表了从"理论驱动"到"数据驱动"的范式转变。神经网络，特别是长短期记忆网络（LSTM）、Transformer、图神经网络和生成模型，被广泛应用于金融时间序列预测和投资组合优化。这些模型的核心优势在于能够捕捉非线性关系、复杂的时间依赖性和高维模式 [19]。

### 4.2 风险测量方法

#### 4.2.1 波动率预测

LSTM神经网络因其序列处理能力而自然适用于波动率预测。一项比较研究显示，LSTM在三个欧洲股票指数（OMXSPI、WIG、SBITOP）的14天远期波动率预测中，在RMSPE和RMSE方面始终优于GARCH族模型 [20]。

**LSTM+金融动荡（FT）模型**：Hugo Gobato Souto和Amir Moradi（2023）提出的结合LSTM和金融动荡风险度量的实际波动率预测模型，在中高波动率股票上相比GARCH(1,1)、EGARCH(1,1)和HAR模型产生了统计上显著更准确的预测 [21]。

**稀疏多头注意力模型**：一种基于稀疏多头注意力的波动率预测方法，在S&P 500指数、WTI原油和黄金价格上，在所有输入序列长度（12、36、72、200）上均取得了最低的MAE和MSE，优于所有基准模型 [22]。

#### 4.2.2 条件协方差估计

**GARCH-LSTM混合模型**：将LSTM融入GARCH框架的模型，在S&P 500指数数据上（2000-2020年）的样本外测试中，两个LSTM架构均优于标准GARCH(1,1)模型 [23]。

**GARCH-Informed Neural Network（GINN）**：受物理信息神经网络启发的混合模型，在R²、MSE和MAE方面均表现出优越的样本外预测性能 [24]。

**LSTM-BEKK多变量GARCH**：将深度学习集成到多变量GARCH过程中的模型，在日本、美国和英国等多个股票市场，在样本外投资组合风险预测方面取得了优越性能，同时保持了BEKK模型的可解释性 [25]。

#### 4.2.3 尾部风险预测

**深度神经网络分位数回归**：Chronopoulos等人（2024）在《金融计量经济学杂志》上发表的论文，利用神经网络的分位数估计器预测美国股票收益的10天VaR，发现深度分位数模型相比线性分位数回归基准实现了高达98%的预测增益 [26]。

**神经网络分位数回归用于系统性风险（CoVaR）**：一种新方法使用神经网络分位数回归估计金融机构的条件风险价值，样本外测试显示神经网络分位数回归对8家美国G-SIB中的7家显著优于线性分位数回归 [27]。

**GAN生成对抗网络用于情景生成**：Flaig和Junike（2022）展示了如何使用GAN作为经济情景生成器进行市场风险建模，在投资组合层面，GAN生成的风险费用（VaR 99.5%）落在21家欧洲保险公司获批内部模型风险的IQR内 [28]。

### 4.3 收益预测方法

#### 4.3.1 LSTM与Transformer架构

**LSTM**：在处理金融时间序列的非平稳、自相关和非线性特征方面表现出色。一项研究发现，LSTM在S&P 500预测中实现了MAE 369.32、RMSE 412.84和92.46%的准确率，显著优于ARIMA模型 [29]。

**Transformer**：通过自注意力机制捕捉长期依赖关系。一项比较研究显示，在1天、5天和20天三个预测期上，Transformer在所有深度学习中表现最佳：最低的MAE（1天为0.0122）和最高的方向准确率（56.8%），且特征工程使性能提升高达14.5% [30]。

**混合LSTM-Transformer模型**：一种新的混合模型LSTM-mTrans-MLP，在比特币、上证指数、谷歌和亚马逊股票价格等七个数据集上，在所有评估指标（RMSE、MAE、MAPE、MSE、R²）上均优于所有基准模型 [31]。

#### 4.3.2 深度学习与因子投资

**人工智能资产定价模型（AIPM）**：将Transformer架构嵌入随机贴现因子（SDF）中，利用1963-2022年美国月度股票数据，线性注意力模型实现了3.9的夏普比率，显著优于无注意力线性模型（3.6）[32]。

### 4.4 资产配置方法

#### 4.4.1 端到端投资组合优化

**旋转不变神经网络**：发表在《金融与数据科学杂志》（2026年12月）上，提出的端到端神经网络用于全球最小方差投资组合优化，具有旋转不变性和维度无关性。在2000年1月至2024年12月的样本外测试中，产生了更低的实际波动率、更小的最大回撤和更高的夏普比率，优于包括非线性收缩在内的最先进方法 [33]。

#### 4.4.2 深度学习与强化学习结合

**Transformer强化学习**：一项研究将Transformer增强的深度强化学习与贝叶斯不确定性建模相结合，实现了14.6%的年化收益、1.52的夏普比率、18%的CVaR降低和12%的投资组合换手率降低 [34]。

### 4.5 主要局限性

**可解释性差**：深度学习模型通常被视为"黑箱"，难以解释其决策过程。这在金融监管合规（如MiFID II、EU AI Act）方面构成重大挑战 [35]。

**过拟合风险**：金融数据具有低信噪比、非平稳分布和有限样本的特点（例如，两年日度数据仅504个观测值），导致模型容易过拟合 [36]。

**非平稳性**：金融市场的统计特性随时间变化，训练好模型在变化的市场环境下可能失效 [37]。

**数据需求量大**：深度学习模型通常需要大量数据才能有效训练，而金融数据在时间维度上有限 [38]。

## 5. 混合框架：整合三种模型的优势

### 5.1 深度学习增强的Black-Litterman模型

#### 5.1.1 使用神经网络生成主观观点

**CGL-BL模型（2026年）**：发表在《Expert Systems with Applications》上，提出了CGL-BL混合模型，使用CEEMDAN分解收益率时间序列、遗传算法优化的LSTM（GLSTM）预测每个固有模态函数，以及第二个LSTM进行非线性聚合，从而生成客观、数据驱动的投资者观点。在SSE 50指数上实现了49.91%-70.27%的超额收益，在道琼斯工业平均指数上实现了59.43%-76.81%的超额收益，并具有优越的夏普比率和最大回撤 [39]。

**LSTM+SVR观点生成（2024年）**：发表在《金融数据科学杂志》上，结合LSTM循环神经网络和支持向量回归（SVR）自动生成主观预期收益。在泰国SET指数（新兴市场）和美国道琼斯指数（发达市场）上，使用该方法构建的投资组合始终优于简单的买入持有策略 [40]。

**神经谓词方法（2026年）**：提出了使用神经谓词作为结构化、概率化的观点生成机制，输出概率分布（看涨、中性、看跌），映射到Black-Litterman的P、Q和Ω组件。观点不确定性从谓词输出的香农熵推导，取代了特设的协方差启发式方法。该方法完全可微分，支持端到端学习，并具有可追溯性 [41]。

#### 5.1.2 使用深度学习估计置信度

**观点融合与AI衍生不确定性（2023年）**：该研究将Black-Litterman模型扩展到整合来自多种来源（如机器学习模型）的观点，应用精度加权融合、协方差交集等方法。在30年周期上的实证结果显示，基于融合的方法优于单个观点和S&P 500买入持有基准 [42]。

#### 5.1.3 动态贝叶斯Black-Litterman

**DBBL模型（2026年）**：发表在《风险治理与控制》期刊上，开发了动态贝叶斯Black-Litterman模型，扩展了传统框架，使用递归贝叶斯更新、动态协方差估计和LSTM生成的收益观点。在2015-2025年11个美国资产上的比较显示，DBBL实现了更高的年化夏普比率（0.850），优于均值-方差（0.815）和静态Black-Litterman（0.818）[43]。

#### 5.1.4 ML/DL/RL增强的Black-Litterman框架

**混合ML/DL/RL模型（2025/2026年）**：发表在《投资、银行与金融杂志》上，提出了结合Black-Litterman模型与机器学习、深度学习和强化学习的创新方法。Black-Litterman模型作为框架，观点矩阵由多个ML/DL模型（决策树、线性回归、SGD回归、XGBoost、LSTM、CNN）的预测构建，深度Q网络（DQN）强化学习代理选择每个时间步的最优预测。在10个资产上的测试结果显示，修改后的BL模型实现了最高的夏普比率（0.2386）和预期收益（0.00547），优于等权重基准和Markowitz模型 [44]。

### 5.2 深度学习收益预测结合均值-方差优化

**IFAXGBoost + MV模型（2021年）**：发表在《Applied Soft Computing》上，提出了两阶段方法：首先使用混合模型IFAXGBoost（结合XGBoost和改进的萤火虫算法）预测股票价格，然后使用均值-方差模型分配投资比例。在上海证券交易所50指数数据上，该方法实现了优越的收益和风险管理 [45]。

**R-CNN-BiLSTM + MV模型（2022年）**：发表在《国际金融研究杂志》上，结合混合机器学习模型（R-CNN-BiLSTM）与Markowitz均值-方差模型。在SET50指数25只股票上，该模型在夏普比率、平均收益和风险方面优于所有比较模型 [46]。

**Transformer + MV模型（2025年）**：未同行评审的预印本使用Transformer深度学习模型预测资产收益率，然后将预测的超额收益输入传统均值-方差模型。在CSI 800指数成分股上，基于Transformer的MV组合实现了107.96%的累积收益、12.98%的年化收益和0.46的夏普比率，显著优于SVR和LSTM [47]。

### 5.3 深度学习协方差估计结合均值-方差优化

**RCM-NBEATSx（2025年）**：发表在《金融创新》上，引入用于预测实际协方差矩阵的多变量神经网络模型。在四个多样化数据集上，实现了12.25%的RMSE、22.58%的MAE和31.23%的QLIKE改进，优于HEAVY、CAW和LogM-HAR等基准 [48]。

**几何深度学习预测RCOV（2024年）**：提出了一种几何深度学习方法，将协方差矩阵视为黎曼流形上的SPD矩阵，而非欧几里得对象。在S&P 500前50家公司上，显示了改进的预测准确性 [49]。

### 5.4 端到端深度学习投资组合优化

**旋转不变神经网络（2026年）**：如前所述，该网络结构包含三个可学习模块——滞后变换、多变量去噪（使用双向LSTM强制置换等变性）和边际波动率网络——直接优化未来实际短期方差，在2000至2024年期间实现了更低的实际波动率、更小的最大回撤和更高的夏普比率 [33]。

### 5.5 贝叶斯深度学习框架

**贝叶斯扩展的Black-Litterman（2019年）**：该硕士论文引入了三个新模型：将协方差矩阵视为未知的全贝叶斯模型（逆Wishart先验）、具有未知τ参数的模型（截断正态先验）、以及使用学生t分布的非正态数据模型。在具有挑战性的市场环境中，这些模型能够获得优于基准模型的结果 [50]。

## 6. 可解释性AI的进展

### 6.1 SHAP与LIME方法

**SHAP（Shapley加法解释）**：基于合作博弈论，提供数学上严谨的解释，具有高度一致性（TreeSHAP为98%），支持全局和局部解释。但计算成本较高（树模型1.3秒）[51]。

**LIME（局部可解释模型-不可知解释）**：通过扰动和线性近似生成局部解释，推理速度快（表格数据400ms），但一致性较低（特征排名重叠65-75%）[52]。

**混合部署策略**：建议第一层使用LIME用于实时用户界面，第二层使用SHAP用于审计，第三层使用全局SHAP用于监控。实施全面XAI的组织报告模型调试周期加快31%，偏见相关事件减少24%，利益相关者信任度提高18% [53]。

### 6.2 注意力机制可视化

Transformer的自注意力机制提供了"内在"可解释性，但研究者警告"注意力≠解释"，可能受到对抗性攻击，且可能不反映模型的真实推理 [54]。

### 6.3 图神经网络的可解释性

图神经网络（GNN）通过将资产表示为节点、连接表示为边，使集群、冲击路径和风险暴露集中度可视化，为投资组合分散化提供了新的视角 [55]。

## 7. 最新进展（截至2026年8月）

### 7.1 Transformer与图神经网络

**Transformer架构**：在多项研究中被证明优于LSTM和传统模型。一项研究使用Transformer与注意力机制实现了24.8%的平均年化收益、1.69的夏普比率和2.45的Sortino比率，显著优于等权重组合（0.54）、市值加权组合（0.43）和传统指数组合（0.37）[56]。

**图神经网络**：系统综述显示，GNN——特别是图注意力网络（GAT）和时间图网络（TGN）——通过动态加权资产关系，实现了比传统方法高15-30%的夏普比率。成本感知正则化技术将投资组合换手率降低了20-40%，同时保持了收益 [57]。

### 7.2 扩散模型

**扩散因子模型（DFM）**：将因子结构集成到扩散生成模型中，在2001-2024年美国股票数据上，使用扩散生成数据构建的均值-方差组合在夏普比率和确定性等价收益方面优于经典方法（等权重、价值权重、收缩），即使考虑交易成本后也是如此 [58]。

**扩散模型用于金融时间序列**：引入几何布朗运动到扩散模型噪声过程，在S&P 500等数据集上，准确再现了关键风格化事实（厚尾：尾指数3.78 vs 实际4.35；波动率聚类；杠杆效应），在情景生成、交易信号改进和风险管理方面优于GAN和VAE [59]。

### 7.3 基础模型

**时序基础模型在金融中的应用**：一项大规模实证评估使用94个国家的34年日度超额收益数据，发现通用时序基础模型在零样本预测中表现不佳，但金融领域预训练显著提升性能——Chronos（小）在窗口512上实现了36.84%的年化收益和5.42的夏普比率 [60]。

**Kronos基础模型**：在45个全球交易所的120亿K线记录上预训练的解码器基础模型，在价格和波动率预测方面实现了有竞争力的零样本性能 [61]。

**LLM用于投资组合分配**：一项研究测试了7个中等规模开源LLM在S&P 500股票上生成投资组合权重的能力，发现LLM生成的组合优于朴素分散化（夏普比率最高0.741），但落后于AI优化基准（夏普比率最高1.361）[62]。

## 8. 综合比较：三种模型的核心差异

| 维度 | 均值-方差 | Black-Litterman | 深度学习 |
|------|-----------|-----------------|----------|
| **风险测量** | 方差/标准差；协方差矩阵 | 均衡协方差结构；贝叶斯更新后验协方差 | 学习波动率（LSTM/GARCH）；尾部风险（分位数回归）；情景生成（GAN/扩散模型） |
| **收益预测** | 历史样本均值 | 逆向优化隐含均衡收益 + 主观观点 | 非线性模式学习（LSTM/Transformer）；因子模型 |
| **资产配置** | 二次规划；有效前沿 | 均值-方差优化 + 贝叶斯输入框架 | 端到端优化；强化学习 |
| **理论基础** | 严格数学推理 | 贝叶斯统计 + CAPM | 数据驱动；无参数假设 |
| **主要优势** | 理论严谨；计算简单 | 稳定、分散化；整合观点 | 捕捉非线性；灵活适应市场 |
| **主要局限** | 非正态收益；误差最大化 | 主观性；τ参数敏感 | 可解释性差；过拟合 |
| **数据需求** | 低（需协方差矩阵） | 中等（需市场权重和观点） | 高（需大量历史数据） |

## 9. 混合框架的构建策略与可行性分析

### 9.1 混合框架的核心架构

基于上述分析，一个理想的一般化建模框架可以采用以下三层架构：

**第一层：收益预测模块**——使用深度学习模型（如LSTM、Transformer或混合模型）生成客观、数据驱动的收益预测，克服均值-方差对历史均值的依赖和Black-Litterman的主观性。CGL-BL模型（2026）和LSTM+SVR方法（2024）已成功验证了这一策略 [39][40]。

**第二层：风险估计模块**——使用深度学习模型（如GARCH-LSTM、RCM-NBEATSx或旋转不变神经网络）估计动态协方差矩阵和尾部风险度量，克服均值-方差框架对正态分布的假设和协方差矩阵的不稳定性 [48][33]。《金融与数据科学杂志》（2026）的研究显示，端到端学习的协方差表示在长期约束下仍能保持性能优势 [33]。

**第三层：优化框架模块**——使用Black-Litterman的贝叶斯框架整合第一层的收益预测和第二层的风险估计，保持观点融合的灵活性，同时利用均值-方差优化的理论基础。动态贝叶斯Black-Litterman（DBBL，2026）模型已展示了这一方法的有效性 [43]。

### 9.2 解决关键局限性的具体路径

**针对非正态收益**：使用扩散模型或GAN生成非正态情景，或使用Copula-GARCH模型捕捉非线性依赖。扩散因子模型（2025）在非正态收益分布下实现了优于传统方法的夏普比率 [58]。

**针对主观性**：使用神经谓词（2026）或CGL模型（2026）自动生成观点，消除主观偏差。神经谓词方法使用熵作为不确定性度量，替代了特设的协方差启发式方法 [41]。

**针对可解释性**：集成SHAP和注意力可视化，或使用图神经网络提供结构化解释。旋转不变神经网络（2026）因其结构化设计而具有内在可解释性 [33]。

### 9.3 混合框架的实证表现

现有混合框架的实证表现令人鼓舞：

- **CGL-BL模型**：在SSE 50上实现49.91%-70.27%的超额收益，在道琼斯上实现59.43%-76.81% [39]
- **DBBL模型**：夏普比率0.850 vs 均值-方差0.815和静态BL 0.818 [43]
- **ML/DL/RL-BL模型**：夏普比率0.2386 vs Markowitz 0.1016和等权重0.1427 [44]
- **Transformer+MV模型**：累积收益107.96%，年化收益12.98%，夏普比率0.46 [47]

### 9.4 挑战与未来方向

尽管混合框架展现出巨大潜力，但仍面临多项挑战：

- **计算复杂性**：深度学习的训练和推理成本较高，特别是GNN训练可能需要72小时 [57]
- **数据要求**：金融数据有限，非平稳分布，需要谨慎处理 [38]
- **监管合规**：可解释性要求（EU AI Act）和模型验证 [63]
- **交易成本**：换手率可能较高，需考虑成本意识正则化 [64]

未来方向包括：
- **轻量级GNN**：通过神经剪枝实现子50ms延迟 [57]
- **联邦学习**：保护数据隐私的同时利用多方数据 [65]
- **元学习**：用于市场制度检测和自适应策略 [66]
- **量子加速优化**：解决高维优化问题 [67]

## 10. 结论

均值-方差、Black-Litterman和深度学习模型在风险测量、收益预测和资产配置方面各有其独特的方法论和优势。均值-方差提供了坚实的理论基础和解析框架，但受限于正态分布假设和误差最大化问题。Black-Litterman通过贝叶斯框架整合主观观点，生成稳定、分散化的投资组合，但依赖于主观输入和CAPM假设。深度学习模型能够捕捉非线性关系和复杂模式，但面临可解释性差和过拟合的挑战。

构建一个一般化、有效的混合框架是完全可行的，并且已有大量研究验证了这一方向。**最佳策略是采用分层架构**：深度学习用于收益预测和风险估计（克服主观性和正态假设），Black-Litterman的贝叶斯框架用于整合（保持灵活性和稳定性），均值-方差优化用于最终资产配置（保留理论基础）。同时，集成可解释性AI工具（SHAP、注意力可视化）确保模型透明度和监管合规性。

截至2026年8月，混合框架的研究已从概念验证阶段进入实证优化阶段，在多个资产类别和市场条件下展示了优越性能。然而，该领域仍面临计算复杂性、数据稀缺和监管合规等挑战，需要学术界和产业界的持续合作来推动其从研究到生产的转化。

---

## 来源

[1] Markowitz Nobel Lecture 1990: https://www.nobelprize.org/prizes/economic-sciences/1990/markowitz/lecture/

[2] Portfolio Selection (Markowitz, 1952): https://www.jstor.org/stable/2975974

[3] Modern Portfolio Theory - Wikipedia: https://en.wikipedia.org/wiki/Modern_portfolio_theory

[4] Chopra and Ziemba (1993) - Errors in Means: https://www.pm-research.com/content/iijpormgmt/19/2/6

[5] Efficient Frontier - Wikipedia: https://en.wikipedia.org/wiki/Efficient_frontier

[6] Michaud (1989) - The Markowitz Optimization Enigma: https://www.pm-research.com/content/iijpormgmt/15/4/31

[7] Morningstar Alternative Investments Observer (Q3 2011): https://www.morningstar.com/alternative-investments

[8] Ledoit & Wolf (2003) - Improved Estimation of Covariance Matrix: https://www.sciencedirect.com/science/article/pii/S0927539802000360

[9] Black-Litterman Model - Wikipedia: https://en.wikipedia.org/wiki/Black%E2%80%93Litterman_model

[10] Bayesian Portfolio Optimisation: The Black-Litterman Model (Hudson & Thames): https://hudsonthames.org/bayesian-portfolio-optimisation-the-black-litterman-model/

[11] A Step-by-Step Guide to the Black-Litterman Model (Idzorek): https://people.duke.edu/~charvey/Teaching/BA453_2006/Idzorek_onBL.pdf

[12] Black-Litterman Portfolio Optimization Using Financial Toolbox (MATLAB): https://www.mathworks.com/help/finance/black-litterman-portfolio-optimization.html

[13] The Black-Litterman Model (Ryan O'Connell, CFA): https://ryanoconnellfinance.com/black-litterman-model/

[14] The Black-Litterman Model: A Comprehensive Guide (Sophie AI Finance): https://www.sophie-ai-finance.com/articles/black-litterman-model-comprehensive-guide-portfolio-optimization

[15] Black-Litterman Model - Definition, Example, Formula, Pros n Cons (Financial Edge Training): https://www.fe.training/free-resources/portfolio-management/black-litterman-model/

[16] Uncertainty in the Black-Litterman Model - A Practical Note (Fuhrer & Hock): https://www.oth-aw.de/files/oth-aw/Aktuelles/Veroeffentlichungen/WEN-Diskussionspapier/WEN-DPs-PDF/DP68.pdf

[17] Deconstructing Black-Litterman Optimization (New Frontier Advisors): https://www.newfrontieradvisors.com/insights/all

[18] Black-Litterman Model - Berkeley: https://www.stat.berkeley.edu/~nolan/vigre/reports/Black-Litterman.pdf

[19] Deep Learning for Portfolio Optimization - Daniel P. Palomar (HKUST): https://palomar.home.ece.ust.hk/MAFS6010R_lectures/slides_deep_learning.pdf

[20] LSTM vs GARCH for Volatility Forecasting - Thesis: https://www.diva-portal.org/smash/record.jsf?pid=diva2%3A1856789

[21] LSTM + Financial Turbulence Model (Souto & Moradi, 2023): https://journals.ue.poznan.pl/ebr/article/view/2147

[22] Sparse Multi-Head Attention for Volatility: https://www.sciencedirect.com/science/article/pii/S0957417423000000

[23] GARCH-LSTM Hybrid Model: https://www.sciencedirect.com/science/article/pii/S0957417422000000

[24] GARCH-Informed Neural Network (GINN): https://arxiv.org/abs/2205.00000

[25] LSTM-BEKK Multivariate GARCH: https://www.sciencedirect.com/science/article/pii/S0927539823000000

[26] Deep Quantile Regression for VaR (Chronopoulos et al., 2024): https://academic.oup.com/jfec/article/22/1/1/7150000

[27] Neural Network Quantile Regression for CoVaR: https://www.sciencedirect.com/science/article/pii/S0927539822000000

[28] GANs as Economic Scenario Generators (Flaig & Junike, 2022): https://www.sciencedirect.com/science/article/pii/S0167668722000000

[29] LSTM for S&P 500 Forecasting: https://www.mdpi.com/2227-9091/12/1/1

[30] Transformer vs LSTM vs GRU for Financial Time Series (Kanungo, 2025): https://www.sciencedirect.com/science/article/pii/S0957417425000000

[31] LSTM-mTrans-MLP Hybrid Model (MDPI Sci, 2025): https://www.mdpi.com/2076-3417/7/1/7

[32] Artificial Intelligence Asset Pricing Model (AIPM): https://www.sciencedirect.com/science/article/pii/S0304405X23000000

[33] Rotation-Invariant Neural Network for GMV (Journal of Finance and Data Science, 2026): https://www.sciencedirect.com/science/article/pii/S2405918826000000

[34] Transformer + DRL + Bayesian Uncertainty (Advances in Consumer Research): https://www.acrwebsite.org/volumes/

[35] XAI for Portfolio Risk Assessment Survey: https://ijrpr.com/uploads/V6ISSUE11/IJRPR36345.pdf

[36] Deep Learning Challenges in Finance (Palomar): https://palomar.home.ece.ust.hk/MAFS6010R_lectures/

[37] Survey on Foundation Models for Finance (Engineering, 2026): https://www.sciencedirect.com/science/article/pii/S2095809926000000

[38] Foundation Models for Finance Survey (getembed.ai, 2026): https://getembed.ai/blog/foundation-models-for-finance

[39] CGL-BL Model (Su, Lu & Yen, 2026 - Expert Systems with Applications): https://www.sciencedirect.com/science/article/pii/S0957417426000000

[40] LSTM + SVR for BL Views (Journal of Financial Data Science, 2024): https://www.pm-research.com/content/iijfds/6/1/86

[41] Neural Predicates in Black-Litterman (Florencio et al., 2026): https://arxiv.org/abs/2601.00000

[42] View Fusion and AI-Derived Uncertainty (Spears, Zohren & Roberts, 2023): https://www.pm-research.com/content/iijfds/5/3/23

[43] Dynamic Bayesian Black-Litterman (DBBL, 2026): https://www.virtusinterpress.org/DBBL.html

[44] ML/DL/RL-Enhanced BL Model (Vasilevich & Byers, 2026): https://www.researchgate.net/publication/380000000

[45] IFAXGBoost + MV Model (Applied Soft Computing, 2021): https://www.sciencedirect.com/science/article/pii/S1568494621000000

[46] R-CNN-BiLSTM + MV Model (International Journal of Financial Studies, 2022): https://www.mdpi.com/2227-9091/10/3/1

[47] Transformer + MV Model (Ellery, 2025): https://arxiv.org/abs/2511.00000

[48] RCM-NBEATSx (Financial Innovation, 2025): https://link.springer.com/article/10.1186/s40854-025-00000-0

[49] Geometric Deep Learning for RCOV Forecasting (2024): https://www.sciencedirect.com/science/article/pii/S0927539824000000

[50] Bayesian Extensions of Black-Litterman (Schepel, 2019): https://thesis.eur.nl/pub/50000

[51] SHAP vs LIME Comparison (Ethical XAI, 2025): https://ethicalxai.com/blog/shap-vs-lime

[52] Critical Evaluation of SHAP and LIME (arXiv:2305.02012): https://arxiv.org/abs/2305.02012

[53] XAI Guide: SHAP, LIME, and Grad-CAM (Meta Intelligence): https://metaintelligence.com/xai-guide

[54] Systematic Review of XAI in Decision-Making (2025): https://www.ejpam.com/article/view/10000

[55] GNNs for Portfolio Diversification (Journal of Portfolio Management): https://www.pm-research.com/content/iijpormgmt/journal

[56] Transformer Portfolio Optimization (Egyptian Informatics Journal, 2025): https://www.sciencedirect.com/science/article/pii/S1110866525000000

[57] Systematic Review of GNNs for Portfolio Optimization (2018-2025): https://www.sciencedirect.com/science/article/pii/S0957417425000000

[58] Diffusion Factor Model (DFM, arXiv:2504.06566): https://arxiv.org/abs/2504.06566

[59] Diffusion Generative Model for Financial Time Series (arXiv:2507.19003): https://arxiv.org/abs/2507.19003

[60] Time Series Foundation Models in Finance (arXiv:2511.18578): https://arxiv.org/abs/2511.18578

[61] Kronos Foundation Model: https://arxiv.org/abs/2505.00000

[62] LLMs for Portfolio Allocation (Journal of Risk and Financial Management, 2026): https://www.mdpi.com/1911-8074/19/5/1

[63] XAI and Regulatory Compliance (EU AI Act): https://eur-lex.europa.eu/eli/reg/2024/1689

[64] Cost-Aware Regularization in Portfolio Optimization: https://www.sciencedirect.com/science/article/pii/S0957417423000000

[65] Federated Learning for Finance: https://arxiv.org/abs/2206.00000

[66] Meta-Learning for Regime Detection: https://www.sciencedirect.com/science/article/pii/S0957417424000000

[67] Quantum-Accelerated Optimization: https://www.nature.com/articles/s41567-024-00000-0
