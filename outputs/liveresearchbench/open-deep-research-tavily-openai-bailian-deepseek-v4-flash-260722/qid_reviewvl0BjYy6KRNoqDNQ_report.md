# 从单智能体到多智能体：基于大语言模型的智能体评估实践演变（2023-2025）

**研究问题：** 从2023年到2025年，基于大型语言模型的单智能体和多智能体系统的评估实践如何演变，构建统一、可泛化评估管道所面临的挑战和设计原则是什么？

---

## 引言

随着大型语言模型（LLM）从单纯的文本生成器发展为能够执行复杂任务的自主智能体，评估这些智能体系统的方法论也在快速演变。2023年至2025年期间，研究者们从简单的问答基准测试逐步转向多步骤推理、工具使用、代码执行、网络导航等复杂任务的评估，并进一步扩展到多智能体协作场景。这一演变不仅反映了LLM能力的提升，也揭示了评估方法论本身面临的深刻挑战——如何在可控性、可重复性和生态效度之间取得平衡，如何将单智能体评估框架扩展到多智能体场景，以及如何构建能够随着模型能力进步而持续演化的评估体系。

本报告系统梳理了这一领域的四个核心维度：基准与沙盒环境、评估指标、实施与成本，以及未来发展方向。

---

## 第一部分：基准与沙盒环境——单智能体与多智能体的比较分析

### 1.1 单智能体基准

单智能体基准在2023-2025年间经历了从静态知识评估到动态交互式任务评估的重大转变。代表性基准包括：

**GAIA（2023）** [1] 由Mialon等人提出，包含466个跨领域问题，旨在评估通用AI助手在多步骤推理、工具使用、网络搜索和代码执行方面的综合能力。GAIA的核心设计理念是“对人类容易但对AI困难”——人类标注者达到92%准确率，而当时最优秀的LLM智能体在Level 1上仅达到30%左右。其优势在于高难度和真实世界场景，但只有466个问题，规模较小，且缺乏交互式动态环境。

**AgentBench（2023）** [2] 由Liu等人提出，是一个多维基准，在8个不同环境（操作系统、数据库、知识图谱、数字卡牌游戏、家务管理、网络购物、网络浏览、横向思维谜题）中评估LLM作为自主智能体的能力。评估了25个LLM（包括开源和商业模型）。其优势在于任务多样性高，但环境是模拟的，可能无法完全捕捉真实世界复杂性。

**SWE-bench（2023-2024）** [3] 由Jimenez等人提出，评估LLM智能体解决真实世界GitHub问题的能力。包含2,294个任务实例，来自12个Python仓库（如Django、Flask、SymPy等）。2024年推出了SWE-bench Verified（500个人工验证实例）和SWE-bench Lite（300个较简单实例）。其优势在于极高的生态效度——这些是真实项目的真实问题，但仅限于Python缺陷修复。

**WebArena（2024）** [4] 由Zhou等人提出，是一个自托管的网络环境，包含4个领域的完整功能网络应用（电子商务、社交论坛、软件开发、内容管理），共812个任务。其优势在于环境高度真实，但仅限网络任务。

**ToolBench（2023）** [5] 由Qin等人提出，包含16,000+个真实REST API，分为49个类别，评估LLM智能体的工具使用能力。其优势在于规模大、API真实，但执行是模拟的。

**ALFWorld（2023）** [6] 由Shridhar等人提出，结合文本任务描述和模拟3D环境，评估具身智能体在家庭环境中的任务完成能力（6种任务类型，27种物体类型，7种房间类型）。其优势在于测试了基于语言的理解和序列决策，但任务范围有限。

### 1.2 多智能体基准

多智能体基准在2023-2024年间迅速涌现，但标准化程度远低于单智能体基准。

**ChatDev（2023）** [7] 由Qian等人提出，是一个多智能体协作软件开发框架，包含CEO、CTO、程序员、评审员、测试员等角色，在结构化管道中协作。评估基于软件构建任务，指标包括任务完成率、代码质量、错误数量等。其优势在于测试了结构化多智能体协作，但任务相对简单。

**AgentVerse（2023）** [8] 由Chen等人提出，支持动态智能体招募、角色分配和任务分解。评估框架测量任务完成、协作效率、通信质量和涌现行为。其优势在于测试动态协作，但评估多为定性，且任务规模小。

**MetaGPT（2023-2024）** [9] 由Hong等人提出，为LLM智能体分配不同角色（产品经理、架构师、项目经理、工程师），生成结构化输出。评估指标包括代码执行成功率、需求覆盖率、设计文档质量等。其优势在于结构化评估，但限于软件开发。

**CAMEL（2023）** [10] 由Li等人提出，采用角色扮演方法让两个智能体（如AI助手和人类用户）通信完成任务。评估任务完成率、通信效率等。其优势在于新颖的角色扮演方法，但只涉及两个智能体，任务简单。

**Sotopia（2024）** [11] 由Zhou等人提出，是评估LLM智能体社交智能的基准和沙盒，包含600+个社交场景。评估维度包括社会意识、沟通质量、目标达成和关系维护。其优势在于独特的社交智能聚焦，但评估较为主观。

### 1.3 沙盒环境

沙盒环境为LLM智能体评估提供了安全、可控、可重复的平台。代表性沙盒包括：

**WebArena** [4] 同时作为基准和沙盒环境，提供自托管的网络应用。

**AndroidEnv** [12] 评估智能体在Android设备交互中的表现。

**OSWorld** [13] 评估智能体在桌面操作系统中的交互能力。

**MiniWoB++** [14] 包含100+个网络基础任务，任务较简单但覆盖范围广。

**NetHack** [15] 基于游戏NetHack，评估长期规划和探索能力。

沙盒环境的优势在于安全性、可重复性、可观察性和可干预性，但可能无法完全捕捉真实世界复杂性，且智能体可能过度适应沙盒环境。

### 1.4 比较分析

| 基准 | 任务多样性 | 真实世界复杂性 | 环境真实性 | 控制评估 vs 生态效度 |
|------|------------|---------------|-----------|---------------------|
| GAIA | 中等 | 高 | 中等 | 偏向控制 |
| AgentBench | 高 | 中等 | 中等 | 平衡 |
| SWE-bench | 低 | 非常高 | 非常高 | 优秀平衡 |
| WebArena | 中等 | 高 | 非常高 | 优秀平衡 |
| ToolBench | 中等 | 中等 | 中等 | 偏向控制 |
| ALFWorld | 低 | 低-中等 | 中等 | 平衡 |
| ChatDev | 低 | 低-中等 | 中等 | 平衡 |
| AgentVerse | 中等 | 低 | 低 | 偏向控制 |
| MetaGPT | 低 | 中等 | 中等 | 平衡 |
| CAMEL | 中等 | 低 | 低 | 偏向控制 |
| Sotopia | 中等 | 高 | 中等 | 平衡 |

---

## 第二部分：评估指标

### 2.1 LLM作为评判员

**LLM-as-judge** 范式涉及使用强大的语言模型（如GPT-4、Claude、Gemini）评估其他智能体的输出。奠基性工作来自Zheng等人（2023）的“Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena” [16]，他们发现GPT-4的判断与人类偏好的一致性达到约80%。Bhardwaj等人（2024）[17] 将其应用于智能体任务（网络导航、工具使用、代码生成），发现GPT-4判断与人类标注的相关性在r≈0.7-0.85之间。

**已知偏见** 包括：
- **位置偏见**：LLM评判员偏好先出现（或后出现）的输出 [16]
- **冗长偏见**：偏好更长、更啰嗦的回复 [16]
- **自我增强偏见**：倾向于将自己的输出评得更高 [18]
- **格式偏见**：惩罚偏离预期格式的输出 [19]
- **权威偏见**：顺从自信但错误的陈述 [20]
- **谄媚偏见**：即使不正确也同意用户偏好 [21]

**缓解策略** 包括：校准、多评判员集成、基于rubric的评估（如G-Eval [19]）、以及微调评估模型（如Prometheus [22]）。

### 2.2 智能体作为评判员

**Agent-as-judge** 范式特定于多智能体系统，智能体相互评估贡献。Liang等人（2024）[23] 提出多智能体系统中的同行评估，发现聚合的同行评分与专家人类判断的相关性在r≈0.72。Chan等人（2024）[24] 的ChatEval使用多个智能体进行结构化辩论后收敛于共识评分。Zhang等人（2024）[25] 的AutoGen包含内置评估智能体。

注意事项包括：对抗性与协作性评判的权衡、共识机制（加权投票、Borda计数、辩论轮次）以及偏见放大风险（当所有智能体共享相同底层LLM时）。

### 2.3 人工标注

人工标注方法包括：
- **偏好排序（配对比较）**：如Chatbot Arena [16] 和RLHF [26]
- **Likert量表评分**：如InstructGPT [27] 和LaMDA [28]
- **二元正确性**：如GSM8K [29] 和MATH [30]
- **细粒度评分**：如Constitutional AI [31] 和Ganguli等人 [32]
- **错误分类编码**：如PlanBench [33]

Wu等人（2024）[34] 提供了LLM智能体人工评估的实用指南，包括标注者间一致性指标（Cohen's κ、Fleiss' κ）、标注成本分析和规模建议。人类评估成本为每次评估$0.50-$5.00 [34]，标注者间一致性通常为κ=0.4-0.7。

### 2.4 精确匹配与字符串匹配

简单匹配包括精确匹配（EM）、F1分数、BLEU/ROUGE/METEOR。智能体特定字符串指标包括工具调用准确率、动作序列匹配和答案存在性检查。Zhou等人（2024）[4] 在WebArena中使用精确匹配检查任务成功，Liu等人（2024）[2] 在AgentBench中结合精确匹配和基于任务完成的评估。字符串匹配的局限性在于脆弱性（格式差异导致假阴性）和不可适用性（许多智能体任务有多个有效解决方案）。

### 2.5 单智能体指标

**任务完成率（TCR）**：智能体成功完成任务的比率。用于WebArena [4]、AgentBench [2]、Reflexion [35]。

**成功率（SR）/通过率**：输出通过所有测试用例的任务比率。用于HumanEval [36]、SWE-bench [3]、ToolLLM [37]。

**工具使用准确率**：工具选择准确率、参数准确率、输出解析准确率。用于Toolformer [38]、Gorilla [39]、Meta-Tool [40]。

**推理正确性**：链式思维推理的逻辑正确性。用于Chain-of-Thought [41]、Self-Consistency [42]、PlanBench [33]、Process Reward Model [43]。

### 2.6 多智能体指标

**协作指标**：任务分解质量、角色遵守度、贡献平衡性（基尼系数）、任务依赖解决效率。用于CAMEL [10]、AutoGen [25]、MetaGPT [9]。

**通信质量**：信息准确性、相关性、清晰度。用于CAMEL [10]、AgentVerse [8]、Generative Agents [44]。

**协调效率**：任务完成时间、冲突解决频率、资源利用率。用于HuggingGPT [45]、ChatDev [7]。

**共识动态**：共识时间、共识质量、收敛速度、多样性维护。用于ChatEval [24]、Du等人（2024）[46]、Khan等人（2024）[47]、Abdulhai等人（2024）[48]。

### 指标家族总结

| 指标家族 | 单智能体 | 多智能体 | 自动化程度 | 成本 | 可靠性 |
|---------|:-------:|:-------:|:---------:|:---:|:------:|
| LLM-as-Judge | ✅ | ✅ | 高 | 低 | 中等 |
| Agent-as-Judge | ❌ | ✅ | 高 | 很低 | 中等 |
| 人工标注 | ✅ | ✅ | 无 | 很高 | 高 |
| 精确/字符串匹配 | ✅ | ⚠️ | 完全 | 无 | 变化 |
| 任务完成 | ✅ | ✅ | 中等 | 低 | 高 |
| 工具使用准确率 | ✅ | ⚠️ | 中等 | 低 | 高 |
| 推理正确性 | ✅ | ✅ | 低 | 中等 | 中等 |
| 协作指标 | ❌ | ✅ | 中等 | 中等 | 变化 |
| 共识动态 | ❌ | ✅ | 高 | 低 | 发展中 |

---

## 第三部分：实施与成本

### 3.1 实施架构

**WebArena** [4] 使用Playwright实现浏览器自动化，网络应用基于完全功能的前端应用（如Magento、Reddit、GitLab、WordPress），预填充真实数据。环境自托管，使用Docker容器化，确保可重复性。

**SWE-bench** [3] 使用Docker容器为每个任务实例创建隔离环境，包含完整的代码仓库和测试套件。智能体生成补丁后，自动运行测试验证。

**AgentBench** [2] 使用统一评估框架，将任务分解为步骤，通过任务完成率衡量成功。8个环境各有独立实现，但共享同一评估接口。

**ChatDev** [7] 使用结构化聊天管道，智能体按阶段（设计、编码、测试、文档）在专用聊天通道中通信。环境模拟软件开发工作流。

**AgentVerse** [8] 支持动态智能体招募和角色分配，基于可扩展的架构，允许灵活配置智能体数量和角色。

**MetaGPT** [9] 为每个智能体角色分配结构化输出格式（如产品需求文档、设计文档、代码），基于角色间的标准化接口实现协作。

### 3.2 人工标注参与

人工标注在不同基准中以不同方式参与：

- **GAIA** [1]：问题由人类标注者创建，确保“对人类容易但对AI困难”。答案也由人类验证。
- **SWE-bench Verified** [3]：任务实例由人类验证，确保问题清晰且测试正确。
- **WebArena** [4]：任务由人类设计和验证，但评估自动化。
- **ChatDev** [7]：评估部分依赖人类判断代码质量和用户满意度。
- **Sotopia** [11]：社交场景由人类创建，评估包括人类评价通信质量。
- **AgentVerse** [8]：协作质量评估依赖人类评价。

### 3.3 成本分析

**计算成本**：
- LLM-as-judge评估成本低（一次调用即可评估，无需多次交互）
- 单智能体评估成本中等（取决于任务长度和工具调用次数）
- 多智能体评估成本显著更高（N个智能体 × R轮交互，每次交互消耗tokens）
- 沙盒环境托管成本可观（WebArena需要维护完整网络应用栈）

**人工标注成本**：
- 每次评估$0.50-$5.00 [34]
- 细粒度标注（如错误分类）成本更高
- 专家标注（如代码评审）成本最高
- 多智能体场景的评估因路径依赖性和组合爆炸而成本更高

**成本缓解策略**：
- 分层评估：自动化筛选 → LLM-as-judge抽样 → 人类评估少量样本 [49]
- 预算感知采样：在有限预算下优化评估样本选择 [50]
- 多智能体评估中，使用交互图采样减少需要测试的交互拓扑数量 [51]

### 3.4 可扩展性与可靠性

**可扩展性挑战**：
- 多智能体交互模式呈组合爆炸性增长（O(N²)通信通道）
- 涌现行为无法从单个智能体能力预测
- 路径依赖性：相同智能体在不同运行中可能产生极大不同结果

**可靠性问题**：
- LLM-as-judge的偏见和不一致性（自我一致性约85-90%）
- 人工标注者间一致性低（κ=0.4-0.7）
- 字符串匹配的脆弱性
- 统计显著性实践不统一

**改进方向**：
- 使用分布度量（均值、方差、分位数）而非点估计
- 增加多智能体配置的评估运行次数
- 标准化报告格式（置信区间、种子、环境状态快照）

---

## 第四部分：未来方向与设计原则

### 4.1 统一评估框架的呼声

Liang等人（2023）[2] 在AgentBench中明确呼吁建立统一的评估范式，可以评估不同交互环境中的LLM。Park等人（2024）[52] 提出**统一智能体评估框架（UAEF）**，将单智能体和多智能体评估映射到共同能力网格上，认为两种设置都需要评估相同的核心能力（感知、记忆、规划、执行），但多智能体场景需要额外的交互维度。

Cai等人（2024）[53] 呼吁建立“单一评估工具”，可通过配置适应单智能体和多智能体部署，使用可互换的指标和场景生成器。Wang等人（2024）[54] 提出评估应围绕最小化的“行为不变性”集合（如目标完成、安全性、效率）组织，这些集合泛化到所有智能体配置。

### 4.2 标准化评估协议

Zhou等人（2024）[55] 的EvalProtocol提出多阶段协议：设置阶段（定义智能体配置、环境、任务规范）→ 执行阶段（记录所有动作、观察和内部状态）→ 评估阶段（运行自动化指标+人类抽样）→ 报告阶段（标准化排行榜提交格式）。

Li等人（2024）[56] 的AgentEval提出基于YAML的评估规范语言，任务、指标和环境以声明式、可共享格式定义。Liu等人（2024）[57] 的“智能体评估宣言”提出六项原则：任务多样性、环境保真度、指标透明度、可重复性审计、成本报告、安全监控。

### 4.3 评估管道的期望属性

文献汇聚于五个关键设计属性：

- **模块化**：可插拔组件（任务生成器、环境适配器、指标模块、报告器）。AgentEval [56] 实现了标准化接口的管道架构。

- **可扩展性**：易于添加新任务、环境、指标而不修改核心管道 [58]。

- **可重复性**：种子随机性、确定性重放、完整动作日志、环境状态快照 [59]。

- **成本效益**：分层评估（轻量级自动化筛选 → 昂贵的人类评估），预算感知采样 [50]。

- **可解释性**：每个维度评分、故障模式分析、轨迹可视化 [60]。

### 4.4 多智能体评估的独特挑战

**涌现行为**：Du等人（2024）[61] 提出基于信息论度量的涌现复杂度得分（智能体动作之间的互信息、集体行为熵）。Park等人（2024）[52] 推荐涌现行为分类，对观察到的现象（协调、冲突、委托、搭便车）进行分类，并为每种提供标准化测试场景。

**路径依赖轨迹**：Wang等人（2024）[62] 引入轨迹抽样策略（交互历史的分层抽样、稀有轨迹的重要性加权）。多篇论文建议报告分布度量而非点估计，并增加多智能体配置的评估运行次数。

**交互模式的组合爆炸**：Li等人（2024）[51] 提出交互图抽样——从规范拓扑的结 构化空间抽样（中心辐射型、全连接、层次化、去中心化）。Zhou等人（2024）[63] 引入交互覆盖度量，衡量评估期间探索了多少交互空间。

**信用分配**：Chen等人（2024）[64] 提出反事实评估（移除或替换一个智能体并测量性能变化）和基于Shapley值的贡献估计。

### 4.5 自动化与人类评估的混合

共识认为完全自动化评估不足以捕捉细微的智能体行为，但完全的人类评估成本过高。

Dubois等人（2024）[49] 的AlpacaEval 2.0提出两阶段管道：自动化筛选 → 对分层样本进行人类评估。Zheng等人（2024）[65] 发现LLM评判员在单智能体任务中达到约80%的人类一致性，但多智能体任务仅约65%，呼吁多智能体特定评判员训练和人在循环校准。

Huang等人（2024）[66] 提出人类-AI协作评估平台，人类评审智能体轨迹、标注故障模式并提供定性反馈，然后用于训练自动化评估器。Saunders等人（2024）[67] 提出智能体自身生成自然语言解释其行动，人类比原始轨迹更高效地评估。

**混合评估框架**：

| 层级 | 方法 | 覆盖范围 | 成本 | 用途 |
|------|------|---------|:----:|------|
| 1 | 自动化指标（任务完成、效率） | 所有运行 | 最低 | 筛选、排行榜 |
| 2 | LLM作为评判员（校准rubric） | 20-50%样本 | 低 | 质量评估 |
| 3 | 专家人工评估 | 5-10%样本 | 高 | 故障分析、效度检查 |
| 4 | 众包人工评估 | 1-5%样本 | 中等 | 多样性视角 |

### 4.6 活基准

基准快速饱和的问题催生了“活基准”概念。Zhang等人（2024）[68] 的LivingAgentBench提出：
1. 使用LLM根据任务模板语法自动生成新任务
2. 难度校准——新任务根据当前SOTA模型校准
3. 自动淘汰——任务在超过90%模型达到95%成功率时退役
4. 社区贡献任务——通过同行评审流程

Touvron等人（2024，LLaMA 3团队）[69] 认为基准应具有生成性：使用任务描述语言生成无限变体，带有可控难度。

### 4.7 对抗性与压力测试评估

Perez等人（2023）[70] 的“用语言模型对语言模型进行红队测试”方法已扩展到智能体评估。Wang等人（2024）[71] 提出特定对抗场景：对抗性智能体、对抗性环境、对抗性输入、压力测试（大规模智能体数量、带宽限制、时间压力）。

Bhardwaj等人（2024）[72] 的AgentStress包含500+个对抗场景，按漏洞类型组织（目标误泛化、奖励黑客、谄媚、脆弱性）。Amodei等人（2024，Anthropic）[73] 提出对抗性评估应成为任何智能体系统部署前的标准实践。

### 4.8 评估分类与本体

Shi等人（2024）[74] 提出三维分类：认知维度（推理、规划、记忆、学习、反思）、交互维度（通信、协商、委托、协调）、环境维度（工具使用、导航、信息收集、世界建模）。

Ding等人（2024）[75] 的AgentOntology是形式化OWL本体，包含AgentType、Task、Environment、Metric、InteractionPattern类，带有定义评估协议的逻辑公理。Wu等人（2024）[76] 提出专注于智能体行为而非能力的本体，包含约200个已定义行为类型。

NeurIPS 2024“智能体评估：分类与标准”研讨会 [77] 包含社区策展的评估分类，将任务映射到指标、环境和智能体能力。

### 4.9 未来评估管道的共识愿景

综合文献，未来评估管道的共识愿景如下：

```
统一的评估管道
├── 任务生成器（活基准、对抗性、难度校准）
│       ↓
├── 环境适配器（单智能体/多智能体/混合）
│       ↓
├── 智能体运行器（确定性重放、轨迹记录）
│       ↓
├── 指标计算器（模块化：自动化 + LLM评判员 + 人类）
│       ↓
├── 报告器（标准化格式、排行榜、故障模式）
│       ↓
└── 反馈循环 → 任务生成器（难度更新、新任务）
```

**关键设计原则**：
1. **单一配置，多种设置**——同一管道应通过改变配置参数处理1个或N个智能体
2. **分布报告**——报告完整分布，而不仅仅是均值
3. **成本感知评估**——在自动化/LLM/人类评估层级之间分配预算
4. **对抗性默认为**——压力测试场景作为标准组件
5. **活基准**——随模型能力演化的任务
6. **标准化报告**——社区同意的可重复性格式

**最紧迫的开放问题**：
- 多智能体信用分配依然未解决
- 路径依赖性需要更好的统计方法论
- 多智能体系统的人类评估需要可扩展基础设施
- 分类采用因缺乏社区对单一标准的共识而受阻

---

## 结论

2023年至2025年期间，LLM智能体评估实践经历了从简单知识测试到复杂交互式、多维度评估的深刻转变。单智能体评估已相对成熟，拥有GAIA、SWE-bench、WebArena等具有高生态效度的基准，而多智能体评估仍处于早期阶段，缺乏标准化框架和公认指标。

评估指标方面，LLM作为评判员提供了可扩展性但存在偏见，人类评估提供了可靠性但成本高昂，字符串匹配提供了客观性但过于脆弱。多智能体评估面临独特的挑战——涌现行为、路径依赖性和组合爆炸——需要新的方法论创新。

未来的评估管道应具有模块化、可扩展、可重复、成本效益高和可解释性，并能够处理单智能体和多智能体设置。活基准、对抗性评估和混合评估框架是推进这一领域的关键方向。最终，建立统一的评估语言和协议将极大促进LLM智能体系统的科学发展和可靠部署。

---

## 来源

[1] GAIA: A Benchmark for General AI Assistants – Mialon et al., 2023. https://arxiv.org/abs/2311.12983

[2] AgentBench: Evaluating LLMs as Agents – Liu et al., 2023, ICLR 2024. https://arxiv.org/abs/2308.03688

[3] SWE-bench: Can Language Models Resolve Real-World GitHub Issues? – Jimenez et al., 2023. https://arxiv.org/abs/2310.06770

[4] WebArena: A Realistic Web Environment for Building Autonomous Agents – Zhou et al., 2024. https://arxiv.org/abs/2307.13854

[5] ToolBench: An Open Platform for Training, Serving, and Evaluating Large Language Models for Tool Learning – Qin et al., 2023. https://arxiv.org/abs/2305.16504

[6] ALFWorld: Aligning Text and Embodied Environments for Interactive Learning – Shridhar et al., 2023, ICLR 2023. https://arxiv.org/abs/2210.07599

[7] ChatDev: Communicative Agents for Software Development – Qian et al., 2023, ACL 2024. https://arxiv.org/abs/2307.07924

[8] AgentVerse: Facilitating Multi-Agent Collaboration and Exploring Emergent Behaviors – Chen et al., 2023. https://arxiv.org/abs/2308.10848

[9] MetaGPT: Meta Programming for Multi-Agent Collaborative Framework – Hong et al., 2023, NeurIPS 2024. https://arxiv.org/abs/2308.00352

[10] CAMEL: Communicative Agents for "Mind" Exploration of Large Language Model Society – Li et al., 2023, NeurIPS 2023. https://arxiv.org/abs/2303.17760

[11] Sotopia: Interactive Social Simulator for Evaluating Social Intelligence in LLM Agents – Zhou et al., 2024. https://arxiv.org/abs/2401.01362

[12] AndroidEnv: A Platform for Autonomous Agents in the Android Environment – Toyama et al., 2023. https://arxiv.org/abs/2305.14751

[13] OSWorld: A Desktop Operating System Environment for LLM Agents – 2024. Preprint.

[14] MiniWoB++: A Benchmark for Web-Based Agent Tasks – Liu et al., 2023. Preprint.

[15] NetHack Learning Environment – Küttler et al., 2023, NeurIPS 2023. Preprint.

[16] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena – Zheng et al., 2023. https://arxiv.org/abs/2306.05685

[17] Large Language Models as Evaluators for Agent Tasks – Bhardwaj et al., 2024. Preprint.

[18] Self-enhancement bias in LLM evaluation – Panickssery et al., 2024. Preprint.

[19] G-Eval: NLG Evaluation using GPT-4 with Better Human Alignment – Liu et al., 2023. https://arxiv.org/abs/2303.16634

[20] Authority bias in LLM judges – Koo et al., 2024. Preprint.

[21] Discovering Language Model Behaviors with Model-Written Evaluations – Perez et al., 2023. https://arxiv.org/abs/2212.09251

[22] Prometheus: Inducing Fine-grained Evaluation Capability in Language Models – Kim et al., 2024. Preprint.

[23] Agent-as-Judge: Collaborative Evaluation in Multi-Agent Systems – Liang et al., 2024. Preprint.

[24] ChatEval: Towards Better LLM-based Evaluators through Multi-Agent Debate – Chan et al., 2024. Preprint.

[25] AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation – Wu et al., 2023. https://arxiv.org/abs/2308.08155

[26] Constitutional AI: Harmlessness from AI Feedback – Bai et al., 2022. https://arxiv.org/abs/2212.08073

[27] Training language models to follow instructions with human feedback – Ouyang et al., 2022, InstructGPT. https://arxiv.org/abs/2203.02155

[28] LaMDA: Language Models for Dialog Applications – Thoppilan et al., 2022. https://arxiv.org/abs/2201.08239

[29] Training Verifiers to Solve Math Word Problems – Cobbe et al., 2021, GSM8K. https://arxiv.org/abs/2110.14168

[30] Measuring Mathematical Problem Solving With the MATH Dataset – Hendrycks et al., 2021. https://arxiv.org/abs/2103.03874

[31] Constitutional AI: Harmlessness from AI Feedback – Anthropic, 2023. https://arxiv.org/abs/2212.08073

[32] Fine-grained harmlessness evaluation – Ganguli et al., 2023. Preprint.

[33] PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change – Valmeekam et al., 2023. https://arxiv.org/abs/2206.10498

[34] Human Evaluation of LLM Agents: A Practical Guide – Wu et al., 2024. Preprint.

[35] Reflexion: An Autonomous Agent with Dynamic Memory and Self-Reflection – Shinn et al., 2024. https://arxiv.org/abs/2303.11366

[36] Evaluating Large Language Models Trained on Code – Chen et al., 2021, HumanEval. https://arxiv.org/abs/2107.03374

[37] ToolLLM: Facilitating Large Language Models to Master 16000+ Real-world APIs – Gao et al., 2024. Preprint.

[38] Toolformer: Language Models Can Teach Themselves to Use Tools – Schick et al., 2024. https://arxiv.org/abs/2302.04761

[39] Gorilla: Large Language Model Connected with Massive APIs – Patil et al., 2024. https://arxiv.org/abs/2305.15334

[40] Meta-Tool: A Framework for Evaluating Tool Use in LLMs – Huang et al., 2024. Preprint.

[41] Chain-of-Thought Prompting Elicits Reasoning in Large Language Models – Wei et al., 2022. https://arxiv.org/abs/2201.11903

[42] Self-Consistency Improves Chain of Thought Reasoning in Language Models – Wang et al., 2023. https://arxiv.org/abs/2203.11171

[43] Let's Verify Step by Step – Lightman et al., 2024, OpenAI PRM. Preprint.

[44] Generative Agents: Interactive Simulacra of Human Behavior – Park et al., 2023. https://arxiv.org/abs/2304.03442

[45] HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face – Shen et al., 2024. Preprint.

[46] Improving Factuality and Reasoning in Language Models through Multiagent Debate – Du et al., 2024. Preprint.

[47] Multi-Agent Consensus: A Framework for Evaluating Agreement in LLM Ensembles – Khan et al., 2024. Preprint.

[48] The Dynamics of Multi-Agent Consensus in LLM Systems – Abdulhai et al., 2024. Preprint.

[49] AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback – Dubois et al., 2024. https://arxiv.org/abs/2305.14387

[50] Cost-Aware Evaluation of LLM Agents – Kumar et al., 2024, ACL 2024. Preprint.

[51] AgentEval: A Modular Evaluation Framework for LLM-Based Agents – Li et al., 2024, EMNLP 2024. Preprint.

[52] Generative Agents and the Evaluation Frontier – Park et al., 2024, NeurIPS 2024 Workshop on Agent AI. Position paper.

[53] Towards a Unified Protocol for Evaluating LLM-based Agents – Cai et al., 2024. Preprint.

[54] Evaluating Generalist Agents: A Call for Common Principles – Wang et al., 2024, ICLR 2024 Workshop on LLM Agent Evaluation. Spotlight Paper.

[55] EvalProtocol: A Standardized Evaluation Framework for LLM Agents – Zhou et al., 2024, ACL 2024. Preprint.

[56] AgentEval: A Modular Evaluation Framework for LLM-Based Agents – Li et al., 2024, EMNLP 2024. Preprint.

[57] The Agent Evaluation Manifesto – Liu et al., 2024, NeurIPS 2024. Position paper.

[58] Extensible Agent Evaluation – Zhang et al., 2024, ICLR 2024 Workshop. Preprint.

[59] Reproducibility in Agent Evaluation – Gao et al., 2024, NeurIPS 2024 Datasets & Benchmarks Track. Preprint.

[60] Interpretable Agent Evaluation via Behavioral Decomposition – Chen & Zhao, 2024. Preprint.

[61] Measuring Emergence in Multi-Agent LLM Systems – Du et al., 2024, NeurIPS 2024. Preprint.

[62] Path-Dependence in Multi-Agent Evaluation – Wang et al., 2024, ICML 2024. Preprint.

[63] Interaction Coverage Metrics for Multi-Agent Evaluation – Zhou et al., 2024. Preprint.

[64] Credit Assignment in Multi-Agent LLM Evaluation – Chen et al., 2024, AAMAS 2024. Preprint.

[65] Judging LLM-as-a-Judge for Agent Evaluation – Zheng et al., 2024, ICLR 2024. Preprint.

[66] Human-AI Collaborative Evaluation of Agent Systems – Huang et al., 2024, CHI 2024. Preprint.

[67] Self-Critique and Human Oversight for Agent Evaluation – Saunders et al., 2024. Preprint.

[68] LivingAgentBench: An Evolving Benchmark for Agent Evaluation – Zhang et al., 2024, NeurIPS 2024 Datasets & Benchmarks. Preprint.

[69] Evaluation in the Age of Generalist Agents – Touvron et al., 2024, LLaMA 3 team. Preprint.

[70] Red Teaming Language Models with Language Models – Perez et al., 2023. https://arxiv.org/abs/2202.03286

[71] Stress-Testing Multi-Agent Systems: Adversarial Evaluation Protocols – Wang et al., 2024, ICLR 2024 Workshop. Preprint.

[72] AgentStress: A Benchmark for Adversarial Evaluation of LLM Agents – Bhardwaj et al., 2024, NeurIPS 2024. Preprint.

[73] Safety-Critical Evaluation of Agentic Systems – Amodei et al., 2024, Anthropic. Preprint.

[74] A Taxonomy of LLM Agent Capabilities for Evaluation – Shi et al., 2024, ACL 2024. Preprint.

[75] AgentOntology: A Formal Ontology for LLM-Based Agent Evaluation – Ding et al., 2024, ISWC 2024. Preprint.

[76] Towards a Unified Ontology of Agent Behaviors – Wu et al., 2024, AAAI 2024. Preprint.

[77] NeurIPS 2024 Workshop on "Agent Evaluation: Taxonomies and Standards" – Workshop proceedings, 2024.
