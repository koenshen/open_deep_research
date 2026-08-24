# 低代码/无代码平台对传统开发流程的影响：效率提升与维护成本的深度权衡

## 一、研究概要

本报告基于对全球及中国市场低代码/无代码（LCNC）平台的系统研究，从行业趋势、效率数据、维护成本、不同视角对比、案例实证和未来展望六个维度，全面回答核心研究问题：**低代码/无代码平台是否真正提高了开发效率，还是在特定场景下反而增加了维护成本？**

---

## 二、行业趋势与市场规模：增长迅猛但并非万能

### 2.1 全球市场规模的高速增长

全球低代码/无代码市场正处于爆发式增长阶段。据多家权威机构数据，2025年全球市场规模在 **128.6亿至373.9亿美元** 之间（口径差异），预计到2030-2035年将增长至 **958亿至3,769亿美元**，年复合增长率（CAGR）在 **19.5%至29.1%** 之间 [1][2][3]。

核心驱动因素包括：
- **开发者短缺**：全球有超过140万个未填补的软件开发职位，87%的IT领导者认为低代码/无代码有助于缓解人才缺口 [4]。
- **数字化转型加速**：2021-2023年间数字化转型投资增长53%，约70%的企业正在进行数字化转型 [1]。
- **成本压力**：84%的企业正在利用低代码/无代码解决方案填补技术缺口 [5]。

### 2.2 中国市场的特殊性与增长动力

中国低代码/无代码市场呈现出更快的增长态势。2024年中国市场规模达 **40.3亿至52.1亿元人民币**，预计2029年将增至 **129.8亿至131.2亿元**，CAGR在 **20.3%至26.4%** 之间 [6][7][8]。

中国市场有几个独特趋势：
- **信创适配成为刚需**：金融、政府、军工等行业要求全链路兼容国产芯片、操作系统、数据库和中间件 [9]。
- **AI赋能效率提升**：主流平台已集成多模态大模型，通过自然语言建模、智能调试等功能，使开发效率提升 **300%-500%** [9]。
- **高低代码融合成为主流**：Gartner预测，2026年将有 **85%的企业级低代码平台** 采用“80%标准场景+20%复杂核心场景”的混合架构 [9]。

### 2.3 各行业采用情况

全球范围内，金融服务业采用率最高（82%），其次是医疗健康（74%）、零售（71%）、制造业（63%）和教育（56%）[4]。中国市场中，制造业因产业链长、场景丰富而渗透率最高，金融业紧随其后 [10]。

---

## 三、生产力提升：数据支持的效率优势

### 3.1 开发时间与成本的大幅缩减

多个权威来源一致证实低代码/无代码平台能显著缩短开发时间：

- **McKinsey（2020年）**：低代码/无代码工具使开发时间减少 **60%**，成本降低 **30-40%** [11]。
- **Forrester研究**：Appian客户构建应用的速度提高了 **20倍** [12]。
- **JNPF实测（2026年）**：六款主流低代码平台的设备维保管理系统实测中，从需求到上线周期缩短 **62%**，研发成本平均下降 **45%** [13]。
- **Integrate.io**：组织报告开发时间最多减少 **90%**，数据集成方面开发时间减少 **60-70%** [14]。
- **Capgemini**：84%实施低代码/无代码平台的企业实现了更快的上市时间并改善了业务与IT协作 [11]。

### 3.2 投资回报率（ROI）数据

- 低代码项目的平均3年ROI为 **342%**，**91.9%** 的项目在第一年内收回投资 [15]。
- 公司使用无代码平台每年可节省高达 **140万美元** [15]。
- **Ricoh** 实现 **253%** 的ROI，7个月完全收回投资 [16]。
- 低代码项目平均 **3.2周** 完成，而传统方式需 **14.8周**（快 **74%**）[4]。
- 简单业务应用使用低代码成本约 **8,000美元**，而传统方式需 **45,000美元**（节省 **82%**）[4]。

### 3.3 中国企业具体案例数据

来源：2025年低代码开发平台行业研究报告 [17]

| 平台 | 客户/案例 | 核心效果 |
|------|-----------|----------|
| 普元低代码 | 某国有银行核心系统 | 业务响应从小时级压缩至秒级，运维成本降低 **40%** |
| 阿里云·宜搭 | 吉利汽车供应链系统 | 3周交付，订单处理时间减少 **40%**，库存周转率提升 **30%** |
| 腾讯微搭 | 某零售连锁小程序矩阵 | 日PV超500万，转化率提升 **25%** |
| 用友 YonBuilder | 某制造集团MES系统 | 开发效率提升 **40%**，数据同步时间减少 **50%** |
| 金蝶云·苍穹 | 某快消品渠道管理系统 | 响应速度提升 **5倍**，数据准确率达 **99.8%** |
| 明道云 | 某生物医药LIMS系统 | 研发流程100%数字化，研发周期缩短 **60%** |

### 3.4 公民开发者与生产力民主化

低代码/无代码平台的一个重要生产力价值在于赋能“公民开发者”——非技术背景的业务人员：

- 全球有 **1,620万** 公民开发者，预计到2028年将超过专业开发者 **4倍** [4]。
- 到2026年，正式IT部门之外的开发者将占低代码开发工具用户群的至少 **80%** [18]。
- 中国低代码使用人员规模达 **42.6万人**，其中业务人员占比 **25%** [19]。
- 70%的低代码开发者在零经验的情况下，一个月内学会构建应用 [16]。

**关键发现**：卡塞尔大学的一项实证研究 [20] 对10名参与者（5名有编程经验，5名无经验）进行了受控实验，发现在任务正确性方面两组无统计学显著差异（9/10参与者达到100%成功率），工具在易用性和可学习性方面获得高度评价（中位数4/5）。这表明低代码/无代码平台确实有效降低了开发门槛。

---

## 四、维护成本与风险：被低估的长期代价

### 4.1 隐性成本与“省开发钱、亏运维钱”的困境

尽管低代码/无代码平台在前端开发成本上具有明显优势，但多项研究揭示了其长期维护成本可能远超预期：

- **行业数据显示**，低代码项目隐性成本可占整体投入的 **40%以上**，长期运维成本甚至远超初期采购与开发投入 [21]。
- 低代码平台稳定运营后，**每年维护成本约占初期投入的15%-20%**，多应用场景下，专职运维人力成本会持续累加 [21]。
- 前期成本对比：$5万-$15万（低代码）vs. $25万+（自定义开发），但隐藏的长期成本包括供应商锁定、不断升级的许可费用（起始约$3k/月但随规模扩展急剧增加），以及用“财务债务”替代“技术债务” [22]。

### 4.2 供应商锁定（Vendor Lock-in）

供应商锁定是低代码/无代码平台最常被提及的长期风险之一：

- 大多数低代码平台使用专有DSL和运行时，**迁移几乎不可能，如需迁移相当于完全重建应用** [21]。
- 企业一旦深度落地，积累大量低代码应用后，无法自由迁移、无法替换平台。若厂商服务终止、版本停更、价格上涨，企业只能二选一：持续高价续费，或全部应用重构重建 [21]。
- 相比传统开源架构，低代码的迁移重构成本几乎是 **100%**，长期绑定风险极高 [21]。
- 约 **37%的企业** 担忧供应商锁定风险 [5]。

### 4.3 技术债务的积累机制

低代码/无代码平台是否减少了技术债务？研究结论并不乐观：

- **国际学术论文（Startup Hakk, 2025年）**：无代码/低代码平台正在引入技术债务而非消除它。研究显示大多数组织已经花费超过三分之一的IT预算来服务技术债务，而无代码通常使情况恶化 [23]。
- **葡萄城开发者文章**：低代码降低了开发门槛，但**抬高了运维门槛**——无标准化代码、逻辑全部藏在配置中，问题排查无头绪、故障定位难度大。非开发人员快速随意的配置会积累混乱、冗余的逻辑，当规模扩大时变得不可持续且无法优化 [21]。
- **Gartner 2026年预测**：无治理的低代码会创建大量技术债务，**预计2027-2028年将出现质量清算** [24]。
- 专业开发者对低代码质量的看法存在分歧：**39%表示低代码提高了质量，23%表示降低了质量** [24]。

**深层原因分析**：低代码平台将技术债务隐藏于友好的界面之下，使其在无声中积累利息。真正的成本不是构建时显现的，而是在需要适应、扩展或迁移时才会暴露——此时大多数企业发现自己已被困住 [23]。

### 4.4 可扩展性瓶颈

- **46%的IT专业人士** 指出有限的可扩展性是首要担忧 [25]。
- 低代码平台存在“性能天花板”——预构建组件和拖放工具导致大数据集下性能低下，运营成本高 [26]。
- **JNPF 2026年高并发压测**显示，不同平台在并发性能上差异显著：最优平台（JNPF）可支持 **12,500** 并发，而最弱平台（用友BIP）仅支持 **6,000** 并发 [13]。
- 抽象层使得调试困难，缺乏健壮的单元测试支持，产生“黑盒”区域，阻碍维护和安全 [26]。

### 4.5 影子IT与安全风险

- 在对212家中国企业的调查中，**73.6%的企业** 承认存在常态化的影子IT现象，其中 **62%** 的影子IT应用涉及客户数据或财务数据流转 [27]。
- 某快消品企业（F公司）案例：378个低代码应用中的417个是未经批准的影子IT，导致数据泄露、监管违规和为期四个月的修复工作 [27]。
- 超过 **50%的安全事件** 与影子IT应用的数据泄露有关，低代码平台上构建的应用占其中的 **32%** [27]。
- **61%的IT领导者** 将影子IT风险列为首要障碍 [4]。

---

## 五、开发者视角 vs. 管理视角的深度对比

### 5.1 管理层/业务视角：成本降低与速度优先

管理者普遍对低代码/无代码平台持积极态度，主要关注以下价值：

- **速度**：低代码平台可以将应用开发速度提升数倍甚至数十倍，大大缩短从项目启动到上线的时间周期 [17]。
- **成本**：362%的平均ROI，91.9%的项目第一年收回投资 [15]。
- **赋能业务**：低代码平台赋能“平民开发者”，让最熟悉业务的员工在现代应用开发流程中发挥积极作用 [28]。
- **敏捷性**：43%使用低代码的公司表示比以前更敏捷 [16]。
- **解决人才短缺**：84%的企业采用低代码/无代码来减少IT积压 [29]。
- **ROI证据充足**：100%的企业报告从其低代码采用中获得ROI [30]。

### 5.2 开发者视角：灵活性受限与技术债务担忧

开发者对低代码/无代码平台的态度更为谨慎和批判：

- **定制化受限**：低代码平台对底层代码的抽象化限制了应用结构和行为的控制级别。对33,766篇Stack Overflow帖子的实证研究发现，“应用定制化”是开发者最常讨论的话题（占30%），表明开发者最关注如何在低代码平台上实现定制功能 [31]。
- **质量争议**：39%的专业开发者表示低代码提高了质量，但23%表示降低了质量 [24]。
- **角色转变与焦虑**：专业开发者的角色正从编码转向架构、系统设计和治理。被商品化的技能包括UI标记和简单CRUD应用。专业开发者市场正在分化为“精英架构师”和“商品化编码员”两个群体 [24]。
- **“黑盒”问题**：抽象层使调试困难，缺乏健壮单元测试，产生“黑盒”区域，阻碍维护和安全 [26]。
- **知识传递问题**：无代码系统缺乏文档，当团队成员离开时产生巨大的知识传递问题 [23]。
- **架构复杂性未简化**：低代码减少了编码，但无助于系统设计、数据建模或技术架构决策 [32]。

### 5.3 核心矛盾：短期收益 vs. 长期代价

管理层和开发者之间的视角差异，本质上反映了 **短期财务收益与长期技术可持续性之间的根本矛盾**：

| 维度 | 管理层视角 | 开发者视角 |
|------|-----------|-----------|
| **时间维度** | 关注项目交付速度（数周） | 关注系统生命周期（数年） |
| **成本维度** | 初始开发成本（显性） | 长期维护成本（隐性） |
| **技术维度** | 功能是否实现 | 架构是否可扩展、可维护 |
| **风险维度** | 业务风险（延迟交付） | 技术风险（技术债务、供应商锁定） |
| **人才维度** | 降低对高级开发者的依赖 | 专业技能被商品化的焦虑 |

---

## 六、案例实证：成功与失败的边界条件

### 6.1 成功案例的共同模式

**国际成功案例**：

| 企业 | 平台 | 成果 | 关键启示 |
|------|------|------|----------|
| McDermott（能源） | Kissflow | 6人IT团队支持6,000用户，一年内实现 **10倍ROI** | 治理与赋能并重 |
| Rabobank（银行） | Power Platform | 处理时间从 **三周缩短至三分钟**，自动化40-50%客户电话 | 流程自动化场景最佳 |
| PostNL（物流） | Mendix | 核心订单管理系统，日处理超10,000包裹，**99.95%** 正常运行时间 | 可支撑关键业务 |
| Kaneka Malaysia（制造） | Mendix | 18个月内重建55个手动流程，交付13个新系统，节省 **80%-100%** 时间 | 制造流程自动化 |

来源：[33][34][35][36]

**中国成功案例**：
- **华住集团**使用飞书低代码平台，覆盖数千家酒店门店的巡检系统，处理数千万条数据记录 [37]。
- **禾赛科技**使用飞书低代码平台取代西门子PLM（Teamcenter），整体效率提升 **2倍以上**，评审周期从 **8天缩短至4天** [37]。
- **某国有银行**使用普元低代码平台构建核心系统，业务响应速度从小时级压缩至秒级，运维成本降低 **40%** [17]。

**共同成功模式**：
1. **场景匹配**：流程自动化、内部管理工具、表单应用等中等复杂度场景。
2. **治理先行**：建立卓越中心（CoE），明确使用规范和安全策略。
3. **混合模式**：80%标准场景用低代码，20%核心逻辑用传统开发。
4. **IT与业务协作**：60%的低代码开发计划涉及业务用户和IT开发人员之间的协作 [38]。

### 6.2 失败与局限的典型案例

**Thoughtworks的“不可能三角”分析** [39]：

Thoughtworks提出了低代码平台中固有的“不可能三角”：**易于使用、功能强大和低系统复杂度**这三个目标无法同时实现。

- 易于使用 + 功能强大 = 高系统复杂度（例如AI编程）
- 易于使用 + 低系统复杂度 = 功能受限（例如Scratch）
- 功能强大 + 低系统复杂度 = 高使用成本（例如通用编程语言）

Thoughtworks建议对声称无所不能的平台保持怀疑，并推荐“逃生舱”（Escape Hatch）方法——设计平台时提供机制（如底层API、扩展点），允许高级用户在必要时绕过平台限制。

**“低码开发一时爽，数据治理火葬场”** [32]：

有评论者指出，低代码平台（尤其是“零代码”或“表单驱动”平台）在应用扩展时会产生严重的数据质量和可维护性问题。据估计，在典型项目中，编码占总工作量的不到40%，其中只有约20%可以由低代码平台处理。当低代码和传统开发共存时，整体团队效率实际上可能下降。

**特定不适用场景** [40][41]：

| 场景 | 原因 | 建议方案 |
|------|------|----------|
| 复杂的核心企业系统 | 需要大量定制化和模块化 | 传统开发或混合架构 |
| 高可扩展性和高性能要求 | 低代码平台可能达到扩展性天花板 | 传统开发 |
| 严格的安全和合规要求 | 低代码的“黑盒”特性会带来漏洞 | 传统开发或经认证的企业级平台 |
| 高度复杂的业务逻辑 | 平台通常无法满足深入定制需求 | 传统开发 |
| 深度遗留系统集成 | 需要超出公民开发者能力的定制化专业知识 | 传统开发 |

---

## 七、学术研究与实证证据

### 7.1 卡塞尔大学实证研究 [20]

德国卡塞尔大学的研究采用了**定量实验**方法，使用自定义构建的无代码构建器原型，对10名参与者进行受控实验：

- **任务正确性**：程序员和公民开发者无统计学显著差异（9/10参与者达到100%成功率）。
- **处理时间**：两组无统计学显著差异，但观察到有经验参与者完成速度略快的趋势（无经验者中位时间23分钟，有经验者19分钟）。
- **用户体验**：工具在易用性（中位数4/5）和可学习性（中位数4/5）方面获得高度评价。

**结论**：低代码/无代码平台可以民主化软件开发，使企业以最低培训成本经济高效地开发必要应用。对公民开发者过度培训成本的担忧可能被夸大了。

### 7.2 《Journal of Systems and Software》系统文献综述 [42]

由Dongmei Gao等人撰写的系统文献综述（2026年），对2021年至2025年初发表的226篇文章进行了分析：

- **有充分证据表明低代码加速了开发**。
- **质量和复杂性的结果好坏参半且依赖于上下文**。
- **关于成本和安全性的问题仍然悬而未决**。

这表明学界对低代码/无代码平台的效果持谨慎乐观态度——承认其在加速开发方面的价值，但对长期质量和安全性的影响尚未形成定论。

### 7.3 Stack Overflow实证研究 [31]

发表于《Empirical Software Engineering》（2022年）的研究，分析了33,766篇关于38个流行低代码开发平台（LCSD）的帖子：

- 开发者最常讨论的话题是**应用定制化**（30%），表明这是最核心的使用挑战。
- **How类问题**（57%）在所有类别中最常见，表明开发者主要面临“如何做”的实际操作困难。
- **消息队列和库依赖管理**话题最难获得被接受的答案，表明这些领域存在最大挑战。

### 7.4 中国低代码行业研究报告 [10][19]

艾瑞咨询（2023年）和多家中国研究机构的数据显示：
- 90%的受访员工了解低代码/无代码概念，24%能熟练使用。
- 76%的用户将提升开发效率作为核心需求，67%的企业将降低成本列为重要考量。
- 低代码平台平均节省 **34%的工作量**，但顶级平台最高可节省 **70%**。
- 使用低代码的企业平均每年开发 **5.2个产品**。

---

## 八、未来展望：完全转向还是混合共存？

### 8.1 共识：不会完全转向，而是融合

多方权威来源一致认为，企业不会完全转向低代码/无代码，而是将走向融合模式：

- **Gartner**：到2029年，**80%的关键任务应用**将依赖低代码，但这不是100%替代 [24]。
- **IDC**：低代码/无代码仍然需要IT以某种形式参与，尤其是当应用与关键任务系统和全企业系统接口和互连时 [38]。
- **Thoughtworks**：对于开放问题域，任何单一方案至多只能满足其 **80%场景**，剩余20%的复杂逻辑、边缘情况和优化消耗了不成比例的时间和专业知识 [39]。
- 低代码平台不会消除对开发者的需求，但会**成倍放大他们的影响力**——80%的组织报告称，开发者被释放出来从事更高层次的项目 [33]。

### 8.2 “80/20墙”与混合开发模式

- **AI可以快速生成约80%的功能性应用**，但剩余20%的复杂逻辑、边缘情况和优化消耗了不成比例的时间和专业知识 [43]。
- 混合开发模式被推荐为最优解：
  - **低代码**用于：内部工作流自动化、表单/仪表盘、快速原型设计和遗留系统增强。
  - **传统开发**用于：关键任务系统、高容量应用、独特IP和极致性能要求 [22]。
- 成功组织将采用**混合方法**——在适当场景使用低代码的速度，同时保持传统开发对核心系统、复杂业务逻辑和关键任务应用的控制 [44]。

### 8.3 AI驱动的范式转变

AI正在从根本上改变低代码/无代码领域的格局：

- **72%的无代码平台**现已集成AI功能 [4]。
- Gartner预测，到2028年，**45%的所有新应用代码**将通过低代码/无代码界面由AI生成 [4]。
- **“智能体低编码”（Agentic Low-Coding）** 被视为低代码的下一个前沿——用户描述所需结果，AI智能体处理端到端编码过程 [45]。
- **“Vibe Coding”**（由AI研究员Andrej Karpathy推广）代表了一种即兴的、对话式的开发方法，实现高达 **55%** 的更快完成时间 [46]。
- **主要风险**：研究表明 **40-62%的AI生成代码** 包含安全漏洞。一名研究人员在单个AI构建的应用中发现16个漏洞（6个严重），暴露18,000+用户记录 [47]。

### 8.4 关键趋势总结

| 趋势 | 具体内容 | 对传统开发的影响 |
|------|----------|------------------|
| AI与低代码深度融合 | 从“辅助功能”到“核心架构” | 加速简单场景开发，但对复杂场景的安全挑战加剧 |
| 高低代码融合 | 85%的企业级平台采用混合架构 | 传统开发与低代码从竞争走向协作 |
| 治理成为核心差异化因素 | 受治理的低代码是运营支柱，不受治理的就变成影子IT | 开发者角色从编码转向架构与治理 |
| 平台整合 | 预计24-36个月内市场出现整合 | 大型供应商主导，供应商锁定风险增加 |
| 开源替代方案崛起 | n8n、Langflow、Appsmith等获得关注 | 提供数据主权和成本可预测性选项 |

来源：[24][43][46][47]

---

## 九、综合结论：场景决定适用性，治理决定成败

### 9.1 核心回答

**低代码/无代码平台在特定场景下确实显著提高了开发效率**，其效率提升在短周期、中等复杂度的应用构建中得到了充分验证（开发时间减少60-90%，成本降低30-45%，ROI达342%）。然而，**在复杂的核心业务系统、高并发/高性能要求、严格安全合规等场景下，这些平台可能带来更高的维护成本**（隐性成本可占整体投入的40%以上，每年维护成本约占初期投入的15-20%）。

### 9.2 场景匹配矩阵

| 场景类型 | 低代码/无代码适用性 | 预期效率提升 | 维护成本风险 | 建议方案 |
|----------|---------------------|--------------|--------------|----------|
| 内部工作流自动化 | 非常适合 | 高（60-90%时间节省） | 低-中 | 低代码/无代码首选 |
| 简单CRUD应用/表单 | 非常适合 | 高（80-90%时间节省） | 低 | 无代码首选 |
| 原型开发/MVP验证 | 非常适合 | 高（数天vs数月） | 极低（可丢弃） | 低代码/无代码 |
| 客户门户/自服务应用 | 适合 | 中-高（40-70%时间节省） | 中 | 低代码+治理 |
| 移动应用开发 | 中等 | 中（30-50%时间节省） | 中-高 | 低代码（如Mendix/OutSystems） |
| 复杂核心企业系统 | 不适合 | 低（可能因定制化而抵消） | 高（供应商锁定+技术债务） | 传统开发或混合架构 |
| 高并发/高性能系统 | 不适合 | 低（性能瓶颈） | 高 | 传统开发 |
| 高度监管行业核心系统 | 谨慎 | 中 | 高（合规风险+黑盒问题） | 经认证的企业级平台+传统开发 |

### 9.3 决策建议

1. **明确场景边界**：低代码/无代码不是传统开发的替代品，而是在特定场景下的有力补充。选择前需清晰评估业务需求复杂度、性能要求和长期可维护性。

2. **建立治理框架**：避免影子IT风险，建议建立三层治理模型——制度层（企业级使用政策）、卓越中心（技术赋能与最佳实践）和安全文化（培养安全意识）[27]。

3. **关注供应商锁定**：选择支持代码导出、可私有化部署的平台，或采用开源方案以降低长期绑定风险。

4. **采用混合架构**：遵循“80%标准场景+20%复杂核心场景”的模式，在简单场景中用低代码加速，在关键业务中用传统开发保障。

5. **重视培训与技术储备**：低代码/无代码平台仍需要IT以某种形式参与，企业应培养兼具业务理解和技术能力的交叉人才。

6. **对AI生成代码保持审慎**：AI与低代码的融合是未来方向，但需建立自动化安全扫描和代码质量审查机制，避免引入新的技术债务。

### 9.4 最终判断

低代码/无代码平台的真正价值不在于“替代”传统开发，而在于**重新定义开发活动的分工结构**——让专业开发者聚焦核心架构与复杂业务逻辑，让业务人员通过可视化工具快速实现简单需求，让AI代理自动化重复性编码工作。

**短期开发效率的提升，绝不能以长期运维失控、技术债堆积、厂商锁定、合规失效、架构不稳定为代价** [21]。低代码/无代码平台是强大的工具，但“正确地使用”远比“快速使用”更为重要。

---

## 十、主要来源列表

[1] Low-Code Development Platform Market Size to Surpass USD 95.82 Bn by 2035: https://www.precedenceresearch.com/low-code-development-platform-market

[2] Low Code Development Platform Market Size, Share [2034]: https://www.fortunebusinessinsights.com/low-code-development-platform-market-102972

[3] Low Code Development Platform Market Size, Share & Growth 2026: https://www.datamintelligence.com/research-report/low-code-development-platform-market

[4] No-Code & Low-Code Statistics 2026 | 50+ Data Points & Insights: https://searchlab.nl/en/statistics/no-code-low-code-statistics-2026

[5] Low-Code and No-Code Development Platforms Market: https://www.precedenceresearch.com/low-code-and-no-code-development-platforms-market

[6] IDC：预计到2029年中国低代码与零代码软件市场规模将达到129.8亿元: https://www.cls.cn/detail/2074887

[7] IDC：低代码与零代码深度融合生成式AI，重构开发范式: https://mfe-prod.idc.com/getdoc.jsp?containerId=prCHC53666825

[8] 2025主流低代码平台盘点：AI赋能下的企业数字化新引擎: https://mtz.china.com/touzi/2025/1017/197614.html

[9] 2025年主流低代码开发平台全景洞察：趋势、选型与实践: https://t.cj.sina.cn/articles/view/7670233722/1c92e7a7a00101ftkq

[10] 中国低代码行业研究报告（艾瑞咨询）: https://pdf.dfcfw.com/pdf/H3_AP202208191577363820_1.pdf

[11] Low-Code/No-Code Development Platforms: Empowering the Next Generation of Developers (IJRES, 2025): https://ijres.org/papers/Volume-13/Issue-4/1304229232.pdf

[12] No-Code Transformations Usage Trends — 45 Statistics Every Data Leader Should Know in 2026: https://www.integrate.io/blog/no-code-transformations-usage-trends

[13] 低代码平台快速开发排名：从需求到上线周期实测对比: https://knowledge.jnpfsoft.com/posts/2026-05-25/didaipingtaikuaisukaifapaimingcongxuqiudaoshangxianzhouqishiduibi

[14] No-Code Transformations Usage Trends — 45 Statistics Every...: https://www.integrate.io/blog/no-code-transformations-usage-trends

[15] No‑Code Platform Statistics 2026: Usage Trends Now: https://sqmagazine.co.uk/nocode-platform-statistics

[16] Low-Code Growth: Key Statistics That Show Its Impact: https://joget.com/low-code-growth-key-statistics-facts-that-show-its-impact

[17] 2025年低代码开发平台行业研究报告：普元引领，众商竞逐: https://t.cj.sina.cn/articles/view/7869353232/1d50ccd1000101lu36

[18] Game-Changing Top 60 No-Code Low-Code Citizen Development Statistics: https://quixy.com/blog/no-code-low-code-citizen-development-statistics-facts

[19] 2025中国十大低代码平台深度解析与选型: https://developer.aliyun.com/article/1678970

[20] Low-code vs. the developer: An empirical study on the developer experience and efficiency of a no-code/low-code development platform (University of Kassel): https://www.uni-kassel.de/eecs/index.php?eID=dumpFile&t=f&f=40025&token=b1a175d421589348da54f15ffb99610ac0d45cd4

[21] 低代码平台隐藏成本揭秘：从开发效率到长期维护的权衡: https://grapecity.csdn.net/6a18f3bd662f9a54cb78339f.html

[22] Low-Code Platforms for Large Corporations: Guide & Best Practices: https://phenomenonstudio.com/article/low-code-and-no-code-platforms-in-large-corporations-opportunities-and-limitations

[23] No-code and Low-code Just introducing technical Debt in Software Development: https://www.youtube.com/watch?v=XcOx3cgya78

[24] Low‑Code Trends & Statistics Shaping Enterprise IT in 2026 (Updated): https://kissflow.com/low-code/low-code-trends-statistics

[25] 无代码和低代码开发平台软件市场规模和增长报告，2035年: https://www.marketgrowthreports.com/zh/market-reports/no-code-and-low-code-development-platforms-software-market-107271

[26] Inherent limitations: Where low code platforms fall short: https://www.okoone.com/spark/technology-innovation/inherent-limitations-where-low-code-platforms-fall-short

[27] 全民开发时代，如何规避低代码带来的"影子IT"风险？: https://knowledge.jnpfsoft.com/soft/2026-08-12/quanminkaifashiruhuiguididaidailaideyingziitfeng

[28] 什么是低代码/无代码开发？| SAP: https://www.sap.cn/resources/what-is-low-code-no-code

[29] How Low-Code and No-Code Apps Fuel Digital Transformation: https://www.reworked.co/information-management/whats-behind-the-explosion-of-low-code-and-no-code-applications

[30] Forrester Wave on Low-Code Development Platforms Report 2026: https://blog.tooljet.com/forrester-wave-on-low-code-development-platforms

[31] Developer discussion topics on the adoption and barriers of low code software development platforms (Empirical Software Engineering, 2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC9643911

[32] 用低代码？请三思而后行: https://idealworld.group/2025/01/10/use-low-code-please-wait

[33] Why Accounting Teams Need Workflow Management Software (Kissflow Case Studies): https://kissflow.com/low-code/low-code-case-studies

[34] Microsoft is a leader in 2025 Forrester Wave™ for low-code platforms: https://www.microsoft.com/en-us/power-platform/blog/power-apps/microsoft-is-a-leader-in-2025-forrester-wave-low-code-platforms-for-professional-developers

[35] 低代码示例和用例（Mendix）: https://www.mendix.com/zh-CN/%E4%BD%8E%E4%BB%A3%E7%A0%81%E6%8C%87%E5%8D%97/%E4%BD%8E%E4%BB%A3%E7%A0%81%E7%94%A8%E4%BE%8B

[36] The 2025 Forrester Wave™ and the future of app development: https://www.outsystems.com/blog/posts/application-generation-future

[37] 飞书低代码平台应用案例精选: https://www.feishu.cn/content/feishu-lowcode-case-selection

[38] Low-Code/No-Code Platforms: Benefits, Limits & Use Cases: https://cdp.com/articles/low-code-no-code-development

[39] 低代码平台中的"不可能三角": https://www.thoughtworks.com/zh-cn/insights/blog/platforms/impossible-triangle-in-low-code-platform

[40] Why Most Low-Code Platforms Eventually Face Limitations: https://www.baytechconsulting.com/blog/why-most-low-code-platforms-eventually-face-limitations-and-strategic-considerations-for-the-future

[41] When Business Technologists Should Avoid Low-Code: https://www.planetcrust.com/when-business-technologists-avoid-low-code

[42] What does current research say about the viability of low-code development? (Journal of Systems and Software, 2026): https://www.sciencedirect.com/science/article/pii/S0164121226001263

[43] AI Low-Code Development Platforms 2026: Trends & Future Outlook: https://www.ainformat.com/detail/1915

[44] Low Code vs Pro Code, What Fits Your Enterprise Needs: https://blog.tooljet.com/low-code-vs-pro-code

[45] 什么是低代码应用开发？| Google Cloud: https://cloud.google.com/discover/what-is-low-code?hl=zh-CN

[46] Dead or Transformed? The Future of Low-Code Development Platforms in an AI-Driven World: https://shiftasia.com/column/dead-or-transformed-the-future-of-low-code-development-platforms-in-an-ai-driven-world

[47] The State of No-Code in 2026: Market Trends and What's Next: https://www.caspio.com/blog/state-of-no-code-2026
