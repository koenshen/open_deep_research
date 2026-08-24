# 机器学习与深度学习在材料元素组合配比优化中的研究进展、模型应用现状与产业化前景报告

## 摘要

本报告系统梳理了机器学习（ML）与深度学习（DL）在优化材料元素组合配比、实现目标材料性能方面的研究进展。调研覆盖全球活跃课题组、代表性论文、常用材料数据库、模型准确度指标、领域挑战、工程可行性及产业化距离七个维度。结果显示：以Materials Project、OQMD、JARVIS等为代表的高通量DFT数据库与图神经网络（GNN）的结合已成为该领域的主流范式，形成能预测精度已达约20 meV/atom量级（接近DFT自身误差）；以A-Lab、GNoME等为代表的"AI预测—自主实验—闭环验证"体系已初步打通从虚拟筛选到真实合成的路径。但数据稀缺与不平衡、DFT与实验的系统性偏差、多目标优化、模型可解释性及实验验证瓶颈仍是制约大规模产业落地的核心障碍。基于现有证据，本报告判断：**计算筛选侧技术成熟度已达产业化前夜（3–5年内有望成为主流研发工具），而"合成—表征—制造"全链路闭环的大规模产业化仍处于早期（预计5–10年）**，后者属基于现有证据的合理推测。

---

## 一、活跃研究课题组

### 1.1 美国

#### （1）Gerbrand Ceder 团队（CEDER Group）— 加州大学伯克利分校 / 劳伦斯伯克利国家实验室（LBNL）

**负责人**：Gerbrand Ceder，加州大学伯克利分校材料科学与工程系教授、劳伦斯伯克利国家实验室高级科学家，Materials Project 联合创始人、Radical AI（AI+自动化材料开发公司）联合创始人[1][2]。

**研究方向**：通过量子力学计算、统计力学与实验和机器人技术相结合，建立材料结构与物化性质间的映射，重点覆盖锂/钠/多价离子储能、固态电池等。该组近年聚焦**AI驱动的自主实验室（A-Lab）**，将计算筛选、机器学习、主动学习、文献挖掘与机器人实验整合为闭环[2][3]。

**代表性成果**：2023年在 *Nature* 发表的A-Lab系统（见第二部分论文表）在17天内从58个目标中合成41种新化合物，成功率63%[4]；2025年在 *Nature Materials* 发表Materials Project进展报告，称该数据库已被全球60万+研究者使用[3]。

#### （2）Kristin Persson 团队（Persson Group）— 加州大学伯克利分校 / LBNL

**负责人**：Kristin Persson，UC Berkeley材料科学与工程教授，Materials Project创始负责人。

**研究方向**：数据驱动的功能材料筛选，特别是电催化、电池材料。代表性工作是与CMU Ulissi团队合作的**双金属电催化剂筛选**（*J. Chem. Phys.* 2022）：使用改进的DimeNet++图神经网络预测O/N吸附能（R²=0.85、MAE=0.35 eV），从59,390种二元过渡金属合金中经五级筛选出20种经济可行的硝酸盐还原电催化剂候选[5]。

#### （3）Chris Wolverton 团队 — 西北大学

**负责人**：Chris Wolverton，西北大学材料科学与工程Frank C. Engelhart教授，开放量子材料数据库OQMD创始人，2025年获MRS Theory Award[6]。

**研究方向**：第一性原理计算+机器学习+材料信息学，覆盖锂离子电池正极、储氢、热电材料、高强度合金析出物筛选等。其目标被形象地表述为"像Netflix推荐电影一样推荐新材料"[6]。

**代表性成果**：OQMD数据库（详见第三部分）；*npj Computational Materials*（2015）对1,670个实验生成焓的最大规模DFT-实验对比，表观MAE为0.096 eV/atom[7]；其团队2025年在 *Science Advances* 发表基于"推荐引擎"思想预测新稳定化合物的论文[6]。

#### （4）Heather Kulik 团队 — 麻省理工学院（MIT）

**负责人**：Heather Kulik，MIT化学工程系教授。

**研究方向**：过渡金属配合物的DFT+ML加速发现，开发开源工具包molSimplify，聚焦自旋交叉配合物、液流电池材料等。

**代表性成果**：*ACS Central Science*（2020）展示从近300万候选材料中仅用5周选出8种最有前景的液流电池材料（传统方法估计需50年），核心创新为**Pareto多目标优化+不确定性量化**技术[8][9]。

#### （5）Rafael Gómez-Bombarelli 团队 — MIT材料科学与工程系

**负责人**：Rafael Gómez-Bombarelli，MIT DMSE副教授，材料发现公司Calculario联合创始人[10]。

**研究方向**：将物理模拟与ML融合加速材料发现，包括逆设计（图神经网络+生成模型）、SMILES变分自编码器、Transformer模型、主动学习循环；成功虚拟筛选沸石并发明用于柴油发动机尾气净化的新材料[10]。该团队在学术交流中特别指出"化学空间以臭名昭著的方式难以插值"，随机数据划分会高估模型性能[10]。

#### （6）Rodrigo Freitas 团队 — MIT

**负责人**：Rodrigo Freitas，MIT TDK Career Development Professor。

**研究方向**：金属合金行为的ML建模，化学无序材料模拟。2026年在 *Science Advances* 发表基于**信息论构建训练数据集**的方法（通过替换冗余原子样本使模型接触更广泛的局部化学环境），其训练模型优于Google和Microsoft创建的大型模型，并准确预测与实验匹配的相图；传统蛮力方法为单一材料生成训练数据需超100,000小时计算[11]。

#### （7）Zachary Ulissi 团队 — 卡内基梅隆大学（CMU）

**研究方向**：电催化剂发现的通用ML模型。牵头发布 **Open Catalyst 2020（OC20）数据集**（*ACS Catalysis* 2021），含1,281,121个DFT弛豫结果（约2亿CPU小时计算量），并组织年度Open Catalyst挑战赛[12]。

#### （8）Tian Xie 与 Jeffrey C. Grossman — MIT

**代表性成果**：2018年提出**晶体图卷积神经网络（CGCNN）**（*Physical Review Letters* 120, 145301），从晶体原子连接直接学习性质，仅用10⁴个数据点即可高精度预测8种DFT性质，并具可解释性（可提取局部化学环境贡献）[13]。该论文已被引用约2,800次并被25项专利引用，是材料ML领域引用量最高的基础工作之一。

### 1.2 欧洲

#### （9）Matthias Scheffler 团队 — 德国马普学会弗里茨·哈伯研究所（FHI）/ NOMAD实验室

**负责人**：Matthias Scheffler，FHI理论部主任（1988年起）、柏林工业大学BIFOLD的NOMAD实验室主任[14]。

**研究方向**：材料科学"第四范式"（数据中心科学），FAIR与AI-ready数据基础设施，**描述符（descriptor）理论**。2015年在 *PRL* 提出"大数据的成败关键在于描述符"这一论断——当描述符与驱动机制之间的科学联系不清晰时，学习到的关系因果性存疑[15]；2018年提出**SISSO方法**（压缩感知+符号回归），从海量候选特征中系统发现低维描述符，小样本下仍稳定，已成功预测压力诱导绝缘体-金属转变[16]。其团队建设的NOMAD数据库是全球最大的计算材料科学数据仓库。

#### （10）Luca Ghiringhelli 团队 — 埃尔朗根-纽伦堡大学（FAU）

**负责人**：Luca M. Ghiringhelli，SISSO、Big Data of Materials Science等核心论文的共同作者，现任职FAU材料模拟系，开发SISSO的CPU/GPU高性能实现[16]。

#### （11）Michele Ceriotti 团队（COSMO实验室）— 瑞士洛桑联邦理工学院（EPFL）

**负责人**：Michele Ceriotti，EPFL计算科学与建模实验室负责人，h-index 79（Google Scholar总引用26,887次）[17]。

**研究方向**：原子尺度ML、SOAP/GAP类表示、路径积分分子动力学、核量子效应；近年提出"无约束模型"理念——直接从数据学习物理约束往往优于手工注入物理先验。代表成果 **PET-MAD**：基于Point Edge Transformer的通用机器学习原子间势，仅用95,595个结构（覆盖85种元素，比其他通用势训练集小1–3个数量级）即达到SevenNet和GNoME精度，在Matbench Discovery排行榜登顶[17]。

#### （12）马普钢铁研究所（MPI für Eisenforschung，杜塞尔多夫）

**代表性成果**：与清华大学、TU Darmstadt等合作的**高熵合金（HEA）闭环主动学习发现**（ReALML 2022）：整合Wasserstein自编码器生成模型（HEA-GAD）+两阶段集成回归（TERM，50个MLP+50个GBDT）+实验反馈，仅表征17种新合金即发现2种低热膨胀Invar合金和2种Kovar合金，将文献数据规模从696条扩展到自主实验数据[18]。

### 1.3 中国与亚太

#### （13）日本国立材料科学研究所（NIMS）

- **Ryo Tamura团队**（材料信息学方向）：与旭化成、三菱化学、三井化学、住友化学合作，开发仅用易测数据（XRD、力学性能）提高ML预测精度的方法，在75种聚丙烯数据库上验证[19]。
- **数据驱动无机材料组（CBRM）**（负责人Xu Yibin）：构建电池材料文献数据库AtomWork Battery，结合第一性原理计算与ML设计无机材料[20]。
- **Lambard-ML团队**：维护SMILES-X、MADGUI（贝叶斯优化辅助组分/工艺优化GUI）等开源工具[20]。
- **JST PRESTO"先进材料信息学"领域**（东京大学Shinji Tsuneyuki主持，2015年启动）：共40个项目，涵盖ML晶体界面探索、电解质设计、非晶结构拓扑分析、荧光分子自动设计等[21]。

#### （14）韩国 POSTECH（浦项科技大学）

**负责人**：Seungchul Lee（机械工程）、Hyungyu Jin、Hyoung Seop Kim（材料科学与工程）。

**代表性成果**：基于**条件生成对抗网络（cGAN）**的HEA相预测模型（*Materials & Design* 2020），通过数据增强使模型反映尚未发现的HEA样本，提高相预测精度，同时开发了具解释性的描述性AI模型[22]。

#### （15）韩国高丽大学 — Yoonmook Kang 团队

**代表性成果**：*Materials*（2026）从元素组成直接预测HEA屈服强度：Gradient Boosting模型R²=0.8538、RMSE=192.99 MPa、MAPE=23.62%，在AIxHfNbTaTiZr系外部验证MAPE仅2.44%[23]。

#### （16）中国高校与科研机构

| 机构 | 负责人 | 方向与代表性成果 |
|---|---|---|
| 清华大学物理系 | Jun Ni（倪军） | HEA机器学习综述（*Entropy* 2024）：系统梳理描述符（VASE香农熵、SISSO等）、GNN应用与可解释性（SHAP、t-SNE分类精度93.17%）[24] |
| 北京航空航天大学 | Zhimei Sun（孙志梅） | ML辅助HEA发现综述（*J. Mater. Inf.* 2026）：相形成预测（>95%测试精度）、多目标优化（约100万候选筛选出3种Al-Nb-Ti-V-Cr-Mo合金）、机器学习势[25] |
| 上海交通大学 | Chao Yang（杨超） | AI for HEA系统综述（*Metals* 2025，Editor's Choice）：指出AI模型应同时包含热力学描述符（ΔHmix、Ω）与动力学描述符（扩散激活能、冷却速率）[26] |
| 南京航空航天大学 | Wanlin Guo（郭万林） | SVM相预测模型（*Phys. Rev. Materials* 2019）：322个样本、>90%交叉验证精度，预测369个FCC+267个BCC等原子比HEA，11种与后续实验一致[27] |
| 香港城市大学 | P.K. Liaw（刘锦川）、Tao Yang（杨涛） | HEA计算设计方法大型综述（*High Entropy Alloys & Materials* 2025）；增材制造+ML设计单相到多相HEA（*J. Mater. Inf.* 2022）[28] |
| 中国科学院金属研究所（IMR, CAS） | 陈星秋等 | 主办《金属学报》等6本期刊；担任JMI特刊"ML/AI辅助高性能合金开发"客座编辑[29][30] |
| 重庆大学 | Qian Li（李谦） | 镁合金性能ML预测与多尺度计算（JMI特刊多篇论文）[30] |
| 北京科技大学 | Shu Yanjing团队等 | 多目标优化框架合成24种难熔HEA并验证Zr-Nb-Mo-Hf-Ta；遗传算法自动生成描述符实现90.2%（FCC）/88.1%（BCC）/82.7%（双相）分类精度[26] |

#### （17）其他国际团队（补充）

- **印度理工学院古瓦哈提（IIT Guwahati）等**：*Scientific Reports*（2023）对1,200种HEA组分测试5种ML算法，随机森林最佳（84%平均精度、ROC-AUC 0.9649），并实验合成新HEA Ni25Cu18.75Fe25Co25Al6.25[31]。
- **美国洛斯阿拉莫斯国家实验室（LANL）**：*Materials & Design*（2023）发布硬度预测模型（留一法验证R²=0.9716、RMSE=39.25）与组分优化模型，经实验验证[32]。
- **台湾清华大学An-Chou Yeh团队**：*JOM*（2019）用ANN+模拟退火优化AlCoCrFeMnNi体系组分，bootstrap量化不确定性，发现硬度高于文献最佳值的新组分[33]。

---

## 二、已发表代表性论文及其核心贡献

| 代表性论文 | 期刊（年份） | 核心贡献 |
|---|---|---|
| An autonomous laboratory for the accelerated synthesis of novel materials | Nature 624, 86–91 (2023) | A-Lab自主实验室：17天合成41/58种新化合物（63%成功率）；SynTERRA知识库从24,304篇论文提取33,343条合成流程；ARROWS3主动学习优化[4] |
| Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties | Phys. Rev. Lett. 120, 145301 (2018) | 提出CGCNN框架，10⁴数据点预测8种DFT性质，可解释性强[13] |
| Big Data of Materials Science: Critical Role of the Descriptor | Phys. Rev. Lett. 114, 105503 (2015) | 揭示描述符选择对材料ML因果性的决定性作用[15] |
| SISSO: A compressed-sensing method for identifying the best low-dimensional descriptor | Phys. Rev. Materials 2, 083802 (2018) | 压缩感知+符号回归的描述符发现方法，小样本稳定[16] |
| Accurate Multiobjective Design in a Space of Millions of Transition Metal Complexes | ACS Central Science (2020) | 3百万候选→8种液流电池材料，5周vs传统50年；Pareto+UQ[8] |
| The Open Catalyst 2020 (OC20) Dataset and Community Challenges | ACS Catalysis (2021) | 128万DFT弛豫数据+图神经网络基线，推动催化ML标准化[12] |
| The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies | npj Comput. Mater. 1, 15010 (2015) | 30万DFT计算；与1,670实验值对比MAE 0.096 eV/atom[7] |
| Atomistic Line Graph Neural Network (ALIGNN) | npj Comput. Mater. 7, 185 (2021) | 显式编码键角信息，MP形成能MAE 0.022 eV/atom[51] |
| Evaluation of the MACE force field architecture | J. Chem. Phys. 159, 044118 (2023) | 多体原子簇展开ML力场，在域内外推任务上代表SOTA[54] |
| PET-MAD: A Lightweight Universal Interatomic Potential | Nat. Commun. 16, 10653 (2025) | 95,595结构训练通用势，覆盖85元素，Matbench Discovery登顶[17] |
| Machine learning-enabled high-entropy alloy discovery | ReALML (2022) | 生成模型+集成回归+实验闭环，发现4种Invar/Kovar合金[18] |
| cGAN-based HEA phase prediction | Materials & Design (2020) | cGAN数据增强提升HEA相预测精度[22] |
| Machine-learning model for predicting phase formations of high-entropy alloys | Phys. Rev. Materials 3, 095005 (2019) | SVM在322样本上>90%精度，预测636个新HEA[27] |
| Accelerating High-Entropy Alloy Design via ML: Predicting Yield Strength from Composition | Materials 19, 19010196 (2026) | GB模型R²=0.8538；高屈服强度区（≥1000 MPa）90.9%在±30%误差内[23] |
| Phase prediction and experimental realisation of a new high entropy alloy using ML | Scientific Reports (2023) | 随机森林84–87.5%精度+实验合成验证[31] |
| Prediction and design of high hardness high entropy alloy through ML | Materials & Design 235, 112454 (2023) | 硬度R²=0.9716；可解释+智能优化框架[32] |
| Screening of bimetallic electrocatalysts for water purification with ML | J. Chem. Phys. 157, 074102 (2022) | GNN吸附能R²=0.85；五级筛选20种催化剂候选[5] |
| A better way to model the behavior of metal alloys | Science Advances (2026) | 信息论采样构建训练集，优于Google/Microsoft大型模型[11] |
| Transformer-generated atomic embeddings | Nat. Commun. 16, 1210 (2025) | 通用原子嵌入提升ALIGNN形成能MAE 18%（0.022→0.018 eV/atom）[57] |
| MatterChat: A multi-modal LLM for materials science | Nat. Machine Intelligence 8, 588 (2026) | 结构感知多模态LLM，12个材料任务上优于GPT-4/Gemini/DeepSeek[62] |
| Machine Learning Advances in High-Entropy Alloys: A Mini-Review | Entropy 26, 1119 (2024) | 清华团队对HEA-ML的全面综述[24] |
| AI Design for High Entropy Alloys: Progress, Challenges and Future Prospects | Metals 15, 1012 (2025) | 上交团队综述：热力学+动力学双描述符、CGAN反向设计、主动学习[26] |
| Machine Learning-Based Computational Design Methods for HEA | High Entropy Alloys & Materials 3, 41–100 (2025) | 香港城大综述：覆盖数据质量、文本挖掘、描述符、ML模型与反向设计[28] |
| Graph comparison of molecular crystals in band gap prediction | ACS Omega (2023) | CrystGraph+MEGNet对10,472有机晶体带隙R²=0.895、MAE=0.240 eV[59] |
| Recent advances and applications of ML in solid-state materials science | npj Comput. Mater. 5, 83 (2019) | 高被引综述（2,485次）：确立"第二次计算革命"叙事、模型评估协议[75] |

---

## 三、常用材料数据库分析

### 3.1 Materials Project（材料项目）

**数据规模与更新**：由LBNL于2011年创立，是使用最广泛的无机材料开放知识库，**注册用户超40万**，每天有四篇以上引用它的论文发表[34][35]。当前版本为v2026.04.13（2026年6月上线），核心数据向S3 Delta表迁移，新增74,052个GNoME材料（r2SCAN级，累计117k），并开始用r2SCAN重算核心数据集[34]。

**数据类型**：晶体结构（CIF/POSCAR）、电子结构（带隙、能带、态密度）、热力学性质（形成能、能量高于凸包e_above_hull）、弹性张量、声子、XAS、压电、介电、电池电极数据等；2023年新增MPcules扩展（17万+DFT分子计算）[34][36]。

**在模型训练中的应用**：是CGCNN、ALIGNN、MEGNet、Matformer、GNoME、MatterGen等几乎所有主流材料ML模型的训练数据来源。其形成能与凸包稳定性（e_above_hull）已成为材料筛选的标准基准[34][36]。**已知局限**：PBE带隙系统性低估约50%（官方FAQ承认）；晶格常数系统性高估1–3%；层状材料因缺范德华修正误差大；2025年有研究指出MP中存在近10,000个近重复结构（约6%条目）[69]。

### 3.2 OQMD（开放量子材料数据库）

**数据规模**：西北大学Wolverton团队2010年创建，**2021年中突破1,022,603个收敛DFT化合物**（其中37,624个来自ICSD），通过B1/B2/L1₀/L1₂/Heusler等原型"装饰"生成海量假设化合物[37][7]。

**数据类型**：DFT总能、形成能、带隙、磁性、凸包稳定性。与实验形成能对比表观MAE 0.096 eV/atom，但不同实验测量间MAE即达0.082 eV/atom，说明大量"DFT误差"实为实验不确定性[7]。

**在模型训练中的应用**：iCGCNN在约20万OQMD化合物上形成能MAE 30.5 meV/atom；用于高强度合金析出物筛选（34个L12、29个D019、50个L21候选）；钙钛矿、热电、太阳能燃料等方向[37]。数据采用CC-BY 4.0许可，支持SQL/API/OPTIMADE访问[37]。

### 3.3 AFLOW / AFLOWLIB

**数据规模**：目前（2026年检索时）**3,929,948个材料化合物、超8.17亿个计算属性**（含388万形成焓、32万带结构、55万Bader电荷），完整数据集超40 TB，是规模最大的计算材料数据库[38][39]。

**数据类型**：带结构、态密度、凸包（AFLOW-CHULL）、声子、弹性/热性质、Bader电荷等；Prototype Encyclopedia收录1,100+晶体学原型。AFLOW是材料基因组计划（MGI）在NIST网站上正式介绍的联盟基础设施，提供AFLOW-ML在线ML预测工具[39][40]。

### 3.4 JARVIS（NIST联合自动化存储库）

**数据规模**：**80,000+材料、100万+属性**（JARVIS-DFT首页数字）；另有JARVIS-FF（约2,000材料/100+力场）、JARVIS-QETB（80万+材料的PBEsol DFT数据）、JARVIS-ML（143万ML数据点）、JARVIS-Leaderboard（1,300+基准、900万数据点）[41][42]。

**独特优势**：(1) 使用vdW-DF-OptB88泛函（晶格常数MAE 0.11 Å，优于PBE的0.13 Å）；(2) 提供TBmBJ/HSE06等高精度带隙（TBmBJ的MAE 0.51 eV vs Materials Project的1.45 eV）；(3) 独特属性集：剥离能、拓扑spillage、SLME太阳能效率、热电Seebeck系数、Wannier紧束缚、STM图像、异质结构（22.7万）等[42][43]。其ALIGNN模型（含89元素通用力场）是NIST官方生产级工具[53]。

### 3.5 NOMAD（诺瓦材料发现中心）

**数据规模**：**超1,880万个上传条目、111.6 TB**（re3data记录）；自2014年成立以来收录来自50多种原子级代码的输入/输出文件，总计超1亿次总能计算[44][45][46]。

**定位**：不是"整理好的属性表"，而是保留完整溯源的FAIR原始数据仓库，提供OPTIMADE API和浏览器内NOMAD AI Toolkit（Jupyter分析环境）。对于训练可迁移的基础模型而言，NOMAD的价值在于其代码无关的元数据模式和完整计算溯源[46]。

### 3.6 Citrination / Citrine Informatics

由材料信息学公司Citrine Informatics运营，曾是实验数据与计算数据混合的开放平台（含Philips实验数据、Materials Project超17.5万计算点、NREL/Solvay/Chevron等数据集），2017年入选达沃斯技术先锋，其与HRL Laboratories合作设计的铝合金成为**第一个官方注册用于3D打印的铝合金**[47]。**重要现状：Open Citrination已退役（decommissioned），公共数据集仍可通过DOI永久链接访问，但统一开放平台不再可用**；Citrine以商业AI平台形式继续运营[47]。

### 3.7 其他重要数据库

- **Atomly**（中国科学院物理研究所+松山湖材料实验室）：中国首个世界级材料基因组知识库，**18万+无机化合物、约12,000种介电、8,000种力学、近5万个相图**，配套中国首个"数据增强型"超算设施（投资5.5亿元）[48]。
- **GNoME扩充数据**（Google DeepMind，2023）：向MP捐赠近40万新化合物，为MP史上最大单次贡献；GNoME整体预测2.2M晶体结构（381,000个新稳定材料），将已知稳定晶体从约48,000扩大至421,000个[35][36]。2025年有独立研究指出GNoME与MP中存在近重复结构问题（见第五部分）[69]。
- **Open MatSciML Toolkit**（Intel Labs）：整合约150万地面态材料（跨MP/OQMD/NOMAD/OpenCatalyst等），支持多任务、多数据集训练[50]。
- **matminer数据集包**（LBNL）：45个策展数据集，含matbench_mp_e_form（132,752条）、matbench_mp_gap（106,113条）、jarvis_dft_3d（25,923条）、superconductivity2018（约1.6万条实验超导Tc）等，是模型复现与基准测试的事实标准集[49]。

### 3.8 数据库对比快照

| 数据库 | 规模 | 数据类型 | 泛函/方法 | ML应用定位 |
|---|---|---|---|---|
| Materials Project | 50万+材料（含GNoME）；40万+用户 | 结构/电子/热/弹性/声子/介电 | PBE/PBE+U，r2SCAN重算中 | 主流训练基准（CGCNN/ALIGNN/GNoME/MatterGen） |
| OQMD | 100万+化合物 | 热力学为主（形成能、凸包） | PBE | 合金稳定性、假设化合物挖掘 |
| AFLOW | 393万化合物/8.17亿属性 | 结构/电子/热/弹性/声子/Bader | PBE | 最大规模数据源、原型百科全书 |
| JARVIS | 8万+材料/100万+属性 | 含TBmBJ带隙、拓扑、SLME、热电、力场 | vdW-DF-OptB88 | 高精度带隙+生产级ML工具（ALIGNN-FF） |
| NOMAD | 1,880万条目/1亿+计算 | 原始输入输出文件（全溯源） | 多代码 | FAIR/AI-ready基础数据设施 |
| Atomly | 18万+无机化合物 | 结构/电子/介电/力学/相图 | — | 中国材料基因组核心基础设施 |
| Open MatSciML | 150万材料（整合） | 多数据集ML基准 | — | 多任务/多数据集训练 |

---

## 四、模型准确度评估

### 4.1 图神经网络（GNN）——当前性能上限的代表

- **CGCNN**（2018）：在MP数据上形成能MAE约0.039 eV/atom；金属/半导体分类AUC 0.95；钙钛矿e_above_hull预测MAE约0.130 eV/atom[51]。后续改进（iCGCNN、OGCNN、等变GCNN）使形成能MAE最多再降54%[51]。
- **ALIGNN**（2021）：引入线图显式编码键角，在MP 69,239材料上形成能MAE **0.022 eV/atom**、带隙MAE **0.218 eV**——形成能较CGCNN提升43.6%；在JARVIS-DFT 55,722材料上形成能MAE 0.033 eV/atom、带隙（OPT）0.14 eV、体模量10.40 GPa、剪切模量9.48 GPa；凸包稳定性分类ROC-AUC **0.94**[51][52]。其扩展ALIGNN-FF可对**89种元素**任意组合建模（训练数据约7.5万材料、400万能量-力条目），支持力预测与大规模原子模拟[52][53]。
- **CPGN**（配位多面体图网络，2026）：在MP 69,239结构上带隙MAE **0.292 eV（最优）**、形成能0.060 eV/atom，稳定性分类accuracy 0.9882、ROC-AUC 0.9913[58]。
- **ESNet等元素知识图谱融合模型**：MP数据集上形成能MAE低至20.05 meV/atom、带隙0.177 eV，为GNN家族目前的领先水平之一[68]。
- **CrystalTransformer通用原子嵌入**（*Nat. Commun.* 2025）：预训练原子嵌入可迁移至CGCNN/MEGNet/ALIGNN，形成能MAE分别降低14%/4%/18%（ALIGNN达0.018 eV/atom）；在钙钛矿等小数据场景提升高达34%[57]。
- **MACE**（多体原子簇展开力场，2023）：在MD22大分子基准上能量误差低至**0.058–0.141 meV/atom**、力误差2.8–12.0 meV/Å；从50个随机构型即可复现实验振动光谱；在无序晶体（37元素）上优于NequIP和TeaNet超30%——目前公认为ML力场架构的SOTA[54]。
- **SchNet**：QM9基准MAE 0.31 kcal/mol（11万分子训练）；晶体形成能低至0.035 eV/atom；但缺乏显式角度依赖[55]。
- **DimeNet++**：较DimeNet快8倍、精度高10%（QM9）；定向消息传递显式编码角度[12]。

### 4.2 传统机器学习（RF、XGBoost、SVM、GPR）——小数据场景的主力

- 华盛顿大学Jacobs等（*Mach. Learn.: Sci. Technol.* 2024）用**随机森林**为33种材料性质建模（数据集规模137–18,928点）：**19/33性质获得极佳拟合（RMSE/σy < 0.4），11/33中等，仅3/33拟合差**；16个与文献对比的性质中5个误差略高约10–15%，2个更低；并系统引入**误差校准（z-score重标定）与适用域（KDE特征距离）**，28/33数据集的z-score分布改善[60]。
- HEA屈服强度预测（高丽大学2026）：Gradient Boosting最佳，R²=0.8538、RMSE=192.99 MPa、MAPE=23.62%；高屈服强度区（≥1000 MPa）90.9%预测落在±30%误差内[23]。
- HEA硬度预测（LANL 2023）：可解释ML+固溶强化理论，留一法R²=0.9716、RMSE=39.25（HV）[32]。
- HEA相预测（IIT Guwahati 2023）：随机森林84%平均测试精度、ROC-AUC 0.9649、十折交叉验证0.9315，调参后约87.49%[31]。
- HEA相分类（南航2019）：SVM在322样本上>90%交叉验证精度[27]。
- **SISSO描述符方法**（FHI）：小样本稳定，成功发现压力诱导绝缘体-金属转变候选[16]。

### 4.3 Transformer与大型语言模型（LLM）

- **LLM4Mat-Bench**（*Mach. Learn.: Sci. Technol.* 2025）是当前最大LLM材料性质预测基准：约**190万晶体结构、45种性质（60回归+5分类）**，覆盖OQMD、JARVIS-QETB、GNoME、MP、hMOF、Cantor HEA等10个数据源。关键结论：(1) **小而任务专用的预测模型（LLM-Prop 35M、MatBERT 109.5M）显著优于大而通用的生成模型（Llama 2/3、Gemma 2、Mistral 7B）**，尽管体积小64–200倍；(2) 通用生成LLM在CIF输入时经常幻觉或无法生成有效属性值；(3) 晶体文本描述优于CIF文件或化学式；(4) 能量类性质预测一致更准[61]。
- **MatterChat**（*Nat. Machine Intelligence* 2026）：冻结CHGNet/MACE+冻结Mistral 7B的对齐架构，在MP 142,899结构上训练12个任务，分类任务（金属性、稳定性、磁性）优于专用物理模型CHGNet，数值性质（形成能、e_above_hull、带隙）RMSE最低，且具备科学推理能力（如GaN MOCVD工艺方案、YIG 3:5配比合成方案）[62]。
- **LLM vs GNN的边界**：在OGB分子数据集上LLM全面落后于GNN（如ogbg-molhiv最佳LLM ROC-AUC 0.5892 vs GIN 0.7601）；LLM最有效角色是**增强现有ML模型**（特征增强可提升2–8个百分点）；GPT-4相对GPT-3.5收益微小但成本高20倍、延迟高10倍[74]。

### 4.4 泛化与分布外（OOD）评估——一个常被忽视的关键指标

- **QMALL基准**（NeurIPS 2022）：在QM9训练、在Alchemy（Al10/Al11/Al12更大分子）上测试，发现**更好的域内精度不总是意味着更好的OOD外推**——DimeNet++和ET在ϵHOMO预测上OOD MAE超过1,000–2,000 meV（灾难性失败），而SchNet保持123.77 meV[56]。
- **MD-HIT研究**（*npj Comput. Mater.* 2024）：数据冗余在随机划分时会高估性能；去除冗余后OOD测试MAE改善10.03%、R²改善31.6%。该研究同时发出带隙数据偏差警告：去冗余时意外选择了更多近零带隙样本（阈值0.7时92.43%vs全集48.64%）[64]。
- **Rafael Gómez-Bombarelli团队**的观察：随机数据划分高估模型性能，scaffold splitting使性能急剧下降；混合未见化学物质时误差上升10–50倍[10]。

### 4.5 模型架构对比小结

| 架构 | 典型任务表现 | 优势 | 局限 |
|---|---|---|---|
| 随机森林/XGBoost/GB | 33性质19个极佳拟合；HEA屈服R²=0.85 | 小样本稳健、可解释、训练快 | 无法外推至未见过化学空间（插值工具） |
| SVM | HEA相分类>90% | 小样本分类强 | 需手工描述符 |
| GPR | 多目标主动学习代理（Pareto采样） | 内置不确定性 | 高维扩展受限 |
| CGCNN/MEGNet/SchNet | MP形成能0.02–0.08 eV/atom | 端到端结构学习 | 小样本数据/参数效率低 |
| ALIGNN/CPGN/ESNet | 形成能0.018–0.060 eV/atom；带隙0.14–0.30 eV | 键角/多面体/知识图谱增强 | 训练成本高 |
| MACE等MLIP | 力误差meV/Å级；OOD优于GNN | 能量守恒、多体序 | 需DFT级训练数据 |
| Transformer（CrystalTransformer等） | 通用嵌入迁移提升10–18% | 跨数据库迁移 | 预训练成本极高 |
| 专用预测LLM（MatBERT等） | 接近CGCNN（4/10数据集超越） | 文本描述零样本 | 幻觉、token限制 |
| 通用生成LLM（GPT-4/Llama） | 材料任务全面落后专用模型 | 推理/方案设计 | 幻觉、数值不精确、成本高 |

**总体判断**：在"含结构信息"的晶态体系性能预测上，**GNN（尤其ALIGNN类）已接近DFT精度的工程上限**；在"仅组分信息"的HEA/合金设计上，**集成树模型仍是性价比最高的选择**；在数据稀缺场景，**迁移学习+主动学习+不确定性量化**是提升准确度的三大杠杆。

---

## 五、当前面临的主要挑战

### 5.1 数据稀缺性与类别不平衡

- 材料数据本质多模态（结构、文本、光谱、图像）且标注数据有限；训练集规模常仅数百至数千条（如Jacobs等33性质数据集中最小仅137条；HEA实验中常用数据集为Borg等1,545条）[60][24]。
- 小数据下GNN参数/数据效率低；HEA领域类别不平衡显著（FCC/BCC/双相/金属间化合物样本数严重不均），SMOTE等合成过采样在材料中被证明不可靠[31]。
- 每类材料的"成功实验"（性能优越的配比）天然稀少，失败的负样本极少被发表，造成系统性选择偏差。

### 5.2 数据质量与标准化问题

- **DFT与实验的系统性偏差**：PBE带隙低估约50%（MP官方FAQ承认）；晶格常数系统性高估1–3%；OQMD研究中DFT-实验表观MAE 0.096 eV/atom，而实验内部差异即达0.082 eV/atom——大量"模型误差"实为实验不确定性，这为模型精度设定了物理上限[7][34]。
- **数据库重复/近重复结构**：2025年C&EN报道，GNoME中被发现1,224对完全重复及43个三重重复结构，超过10%的"新稳定晶体"可能是现有晶体的近重复；Materials Project有近10,000个近重复结构（约6%）；此类冗余在随机划分时导致**信息泄漏与性能高估**（OOD R²被高估31.6%）[69][64]。
- **计算水平不统一**：不同数据库使用不同泛函（PBE vs vdW-DF-OptB88 vs r2SCAN）、不同收敛标准、不同赝势，跨库合并训练时需谨慎处理。
- **实验数据的不可比性**：同一种材料在不同文献中的合成工艺（冷却速率、退火温度、加工方式）不同，导致性能数据分散甚至矛盾。

### 5.3 多目标优化难题

- 材料设计几乎总是多目标的：强度vs延展性（经典"强韧悖论"）、硬度vs耐腐蚀、能量密度vs溶解度（Kulik团队液流电池案例：改善其一往往恶化另一）[8][66]。
- 现有方法以Pareto前沿+标量化（加权和/ε-约束）+进化算法为主，但高维Pareto前沿的采样效率、代理模型误差对前沿位置的影响、偏好引导均未成熟[65]。
- 主动学习与多目标结合（LCB/HVI采集函数）已有突破性进展（聚合物复合材料5轮迭代即达Pareto平台），但推广到合金等多体系仍需验证[66]。

### 5.4 模型可解释性

- 深度模型"黑箱"问题持续存在：为什么该组分预测性能好？哪个元素/特征起决定作用？这直接制约工程师对模型建议的信任度。
- 现有可解释性工具（SHAP、t-SNE、注意力权重）只能提供"相关性"而非"因果性"；SISSO类符号回归可给出解析描述符，但覆盖范围有限[15][16]。
- 材料科学界对"物理可解释的AI"需求远高于一般领域，因为工程师需要将模型建议转化为合金设计原则[24][25]。

### 5.5 实验验证闭环缺失

- **计算预测速度远超合成验证能力**是当前最大瓶颈：GNoME一次性预测2.2M候选，但DFT或实验验证只能覆盖极小比例[35][36]。
- 计算预测与真实合成之间的鸿沟：A-Lab失败案例分析显示，反应动力学慢、前驱体挥发性、产物非晶化、0 K DFT计算局限均会导致"热力学稳定但合成失败"[4]。
- DFT/MD的尺度瓶颈：500原子CoCrFeMnNi的DFT需约10⁵ CPU小时；经典MD只能模拟10⁻⁷秒，而实验退火需10²–10⁴秒[26]。
- 自主实验室（self-driving lab）尚处早期阶段，通量、成本、标准化仍受限。

### 5.6 LLM特有挑战

- 幻觉（特别是CIF输入时无法生成有效属性值）；token长度限制（只能摘要级提取）；多晶型等细微结构差异的文本表征困难；闭源模型成本高、可复现性差[61][73][74]。

---

## 六、模型可行性分析

### 6.1 预测可靠的体系 vs 不可靠的体系

**可靠性高（可工程使用）**：
- 晶态材料的**能量类性质**（形成能、凸包稳定性）：ALIGNN等模型MAE 0.018–0.060 eV/atom，已接近DFT自身精度；LLM4Mat基准中能量类预测一致更准[61]。
- **带隙/电子结构**（有高质量DFT标签）：带隙MAE 0.14–0.30 eV（JARVIS体系）；但需注意DFT-PBE本身低估约50%，预测的是"DFT带隙"而非实验带隙[51][52]。
- **金属/非金属、稳定/不稳定等分类任务**：ROC-AUC 0.91–0.99[52][58]。
- **HEA相形成（固溶体vs金属间化合物、FCC vs BCC）**：各团队报告90–96%精度[25][27]。
- **有机分子QM9类性质**：SchNet/DimeNet++已达化学精度（约1 kcal/mol）量级[55]。

**可靠性低（需谨慎）**：
- **OOD外推**：分子尺寸增大后能量预测灾难性失败（MAE>2 eV的案例）[56]。
- **多晶型物**：训练集中缺乏多晶型数据时误差显著（ROY多晶型MAE 0.40 eV）[59]。
- **聚合物/复合材料**：表示、架构、数据可用性均受限[74]。
- **稀土/锕系等稀有化学**：通用ML力场覆盖差[68]。
- **部分力学性质**：33性质中3个拟合差（RMSE/σy>0.7）[60]。
- **实验性能（非DFT量）**：涉及工艺参数（冷却速率、热处理）时误差显著放大——这是组分优化模型与真实工程之间的核心鸿沟[23][25]。

### 6.2 适用边界

- **输入维度**：以"组分（composition）"为输入的模型（如Magpie、RF、XGBoost）适合快速筛选但丢失结构信息；以"结构"为输入的GNN/MLIP精度高但需有效晶体结构（实验前不可得）——因此"组分→性能"与"结构→性能"两类模型适用于设计流程的不同阶段。
- **数据规模**：训练数据<1,000条时建议RF/GB/XGBoost+SISSO描述符；1,000–10⁵条时GNN适用；>10⁵条时可考虑Transformer/基础模型[57][60]。
- **ML力场的规模边界**（QuantumATK 2026文档总结）：应用专用MLFF约10⁵原子、10–100 ns、近DFT精度（快100–1,000倍）；通用MLFF约10⁴原子、1–10 ns、中等精度（快10–100倍）；>10⁶原子仍需经典力场；<500原子直接上DFT[68]。
- **"最复杂的图并非最优"**：分子晶体研究显示存在最优图复杂度，中等复杂度图反而最佳[59]。

### 6.3 改进方向（有实证支撑的路径）

1. **迁移学习**：TL-CGCNN在小数据下MAE降低最多19.2%；CrystalTransformer通用嵌入跨库迁移提升10–18%；通用MLFF微调<100个结构即可适配新体系[57][68]。
2. **主动学习/闭环**：GNoME的"数据飞轮"（GNN筛选→DFT验证→再训练）、A-Lab的ARROWS3算法、HEA Invar合金闭环设计（仅17个实验）均证明主动学习可将实验次数压缩1–2个数量级[4][18][36]。
3. **多任务学习**：MT-CGCNN提升8%；CrystalTransformer多任务嵌入（同时训练形成能+带隙）优于单任务[57]。
4. **物理约束/等变架构**：能量守恒（SchNet/MLIP）、旋转等变（DimeNet、MACE）、配位多面体先验（CPGN）[54][55][58]。
5. **不确定性量化+适用域**：MAST-ML的z-score校准+KDE适用域方法已证明可系统性识别模型失败区域[60]。
6. **数据去冗余**：MD-HIT证明去冗余后OOD性能显著提升，应成为标准预处理步骤[64]。
7. **LLM与GNN混合**：MatterChat架构（结构编码器+LLM）为"自然语言交互+数值预测"提供了可行范式[62]。

---

## 七、产业化距离评估

### 7.1 技术成熟度：已有明确进展

- **计算筛选侧已经"量产"**：GNoME预测220万+结构（381,000稳定材料）；Materials Project与GNoME集成后稳定材料扩容近10倍；ALIGNN-FF、MACE、PET-MAD等通用MLIP已具备生产级代码与预训练权重[35][36][17]。
- **合成验证侧开始"自动化"**：A-Lab实现了63%的自动化合成成功率（58个目标中41个成功），但其目标来自计算筛选，尚不能处理复杂多元合金的熔炼/铸造问题[4]。
- **产业应用案例已经出现**：
  - Citrine Informatics与HRL Laboratories设计的铝合金成为**首个官方注册用于3D打印的铝合金**[47]；
  - MOFGen成功合成5种"AI梦想"MOF[73]；
  - 多团队完成HEA的ML预测+实验验证闭环（郭万林团队11种预测与实验一致；LANL硬度模型实验验证；Li等6种高饱和磁化强度+硬度HEA经实验验证）[27][32][65]；
  - MatterGen生成的钽铬氧化物预测体模量200 GPa、实测169 GPa（误差20%内）[74]；
  - CGCNN原始论文已被25项专利引用，显示工业界直接采纳[13]。
- **时间线压缩证据**：行业分析指出AI加速材料发现将周期从10–20年压缩至1–2年；NIST的JARVIS-ALIGNN/ALIGNN-FF已被官方定位为工业应用工具（合金、电接触、触摸屏、晶体管、电池、复合材料、催化剂）[53][70]。

### 7.2 TRL水平分维度评估

| 维度 | TRL估计 | 依据 |
|---|---|---|
| 性质预测模型（GNN/MLIP） | TRL 6–7（系统级演示） | 生产级代码、预训练权重、跨体系验证、工业案例 |
| 组分优化/反向设计 | TRL 4–5（实验室验证） | 多个实验验证案例，但泛化性不足 |
| 自主合成（A-Lab类） | TRL 4（原型演示） | 仅限无机粉末固态合成，成功率63% |
| 全流程闭环（预测→合成→测试→迭代） | TRL 3–4 | 仅少数案例，无标准化 |
| 大规模制造落地 | TRL 2–3 | 制造环节瓶颈明显 |

### 7.3 商业化障碍

1. **实验验证瓶颈是最大障碍**：计算预测通量（百万级/天）与实验合成通量（几个/天）相差5–6个数量级；工程界流传的观点认为"瓶颈不在发现，而在制造——制造材料才是价值流失之处"[70][74]。
2. **数据知识产权与竞争壁垒**：高质量实验数据是商业机密；DFT计算数据虽开放但可复现性强；NIMS与日本化工企业的合作模式表明产学数据共享是可行路径但需法律框架[19]。
3. **模型可靠性与责任归属**：幻觉、OOD失败、不确定性的量化缺失，在航空航天、医疗等监管敏感领域难以通过认证[73][74]。
4. **成本结构**：训练大型基础模型成本极高（GPT-4级别推理成本是小型专用模型20倍），但材料领域专用小型模型已证明性价比更高[61][74]。
5. **多尺度整合缺失**：从电子（DFT/MLIP）→原子（MD）→微观组织相场/CALPHAD→宏观性能（有限元）的跨尺度链条尚未打通，现有模型各自为战。

### 7.4 时间线预估（以下为基于现有证据的分析性判断，属推测性质）

- **短期（3–5年，2026–2031）**：通用MLIP+主动学习闭环将成为材料研发机构的标准配置；"预测→合成→表征"自主实验室在无机粉末、MOF、部分聚合物体系实现商业化运行；模型评估从"MSE竞赛"转向"校准误差+适用域+OOD"标准；数据共享联盟（类似NOMAD/OPTIMADE生态）在特定行业（电池、催化）建立。
- **中期（5–10年，2031–2036）**：组分配比优化在特种合金（高熵合金、高温合金）、电池材料、催化剂领域实现**小批量高价值产品的量产应用**；数字孪生+工艺参数优化（熔炼、铸轧、3D打印）落地；材料基础模型（类似LLM的材料大模型）出现并主导设计流程；数据标准（FAIR+AI-ready）成为行业准入要求。
- **长期风险**：如果实验验证技术（高通量合成、微型化表征）不能同步突破，全流程闭环的产业化时间线将显著延后——这是该领域最大的"已知未知"。

---

## 结论

机器学习与深度学习在材料元素组合配比优化领域已从"论文概念"进入"工程工具"阶段：活跃课题组遍布全球顶尖机构，GNN类模型在DFT性质预测上逼近精度上限（形成能MAE约20 meV/atom），主动学习与自主实验闭环已多次证明可将新材料发现时间压缩1–2个数量级（A-Lab 17天41种新化合物、HEA 17个实验发现2种Invar合金、液流电池材料5周vs 50年）。核心瓶颈不在于"模型精度"本身，而在于**数据生态（稀缺、冗余、标准化）、多目标决策、可解释性以及实验验证通量**的协同突破。产业化方面，计算筛选侧已接近成熟（3–5年窗口），而覆盖"合成—表征—制造"的全链路大规模应用预计需要5–10年——这一判断基于现有技术增速的合理外推，需随实验自动化技术进展动态修正。该领域的最终成功标准，不是更低的MAE，而是**模型建议被工程界无条件接受并直接进入量产工艺**的那一天。

---

### Sources

[1] Gerbrand Ceder - Wikipedia: https://en.wikipedia.org/wiki/Gerbrand_Ceder
[2] Gerbrand Ceder | Research UC Berkeley: https://vcresearch.berkeley.edu/faculty/gerbrand-ceder
[3] Gerbrand Ceder | Publications | Lawrence Berkeley National Lab: https://profiles.lbl.gov/11542-gerbrand-ceder/publications
[4] An autonomous laboratory for the accelerated synthesis of novel materials - Nature: https://www.nature.com/articles/s41586-023-06734-w
[5] Screening of bimetallic electrocatalysts for water purification with machine learning - J. Chem. Phys.: https://perssongroup.lbl.gov/papers/tran_screening_bimetallic_2022.pdf
[6] Chris Wolverton - Northwestern Engineering: https://www.mccormick.northwestern.edu/research-faculty/directory/profiles/wolverton-chris.html
[7] The Open Quantum Materials Database (OQMD): assessing the accuracy of DFT formation energies - npj Computational Materials: https://oa.tib.eu/renate/items/845c9719-3ced-4492-b2af-81264f41d570
[8] Accurate Multiobjective Design in a Space of Millions of Transition Metal Complexes - ACS Central Science: https://pmc.ncbi.nlm.nih.gov/articles/PMC7181321
[9] Neural networks facilitate optimization in the search for new materials - MIT News: https://news.mit.edu/2020/neural-networks-optimize-materials-search-0326
[10] Rafael Gómez-Bombarelli - MIT DMSE: https://dmse.mit.edu/people/faculty/rafael-gomez-bombarelli
[11] A better way to model the behavior of metal alloys - MIT News: https://news.mit.edu/2026/better-way-to-model-metal-alloys-behavior-0619
[12] The Open Catalyst 2020 (OC20) Dataset and Community Challenges - arXiv: https://arxiv.org/abs/2010.09990
[13] Crystal Graph Convolutional Neural Networks for an Accurate and Interpretable Prediction of Material Properties - Physical Review Letters: https://link.aps.org/doi/10.1103/PhysRevLett.120.145301
[14] Matthias Scheffler Group - Fritz Haber Institute: https://www.fhi.mpg.de/2014991/Scheffler
[15] Big Data of Materials Science: Critical Role of the Descriptor - Physical Review Letters: https://link.aps.org/doi/10.1103/PhysRevLett.114.105503
[16] SISSO: A compressed-sensing method for identifying the best low-dimensional descriptor - Physical Review Materials: https://link.aps.org/doi/10.1103/PhysRevMaterials.2.083802
[17] PET-MAD: A Lightweight Universal Interatomic Potential - arXiv: https://arxiv.org/html/2503.14118v2
[18] Machine learning-enabled high-entropy alloy discovery - MPI für Eisenforschung (ReALML): https://realworldml.github.io/files/cr/paper43.pdf
[19] Improving machine learning for materials design - NIMS/Asia Research News: https://www.asiaresearchnews.com/content/improving-machine-learning-materials-design-0
[20] Data-driven Inorganic Materials Group - NIMS CBRM: https://www.nims.go.jp/cbrm/en/about/tmjnkn0000000069.html
[21] JST PRESTO - Advanced Materials Informatics: https://www.jst.go.jp/kisoken/presto/en/research_area/ongoing/areah27-4.html
[22] AI speeds up development of new high-entropy alloys - POSTECH/EurekAlert: https://www.eurekalert.org/news-releases/520767
[23] Accelerating High-Entropy Alloy Design via Machine Learning: Predicting Yield Strength from Composition - Materials: https://pmc.ncbi.nlm.nih.gov/articles/PMC12786949
[24] Machine Learning Advances in High-Entropy Alloys: A Mini-Review - Entropy: https://pmc.ncbi.nlm.nih.gov/articles/PMC11675871
[25] Machine learning-assisted high-entropy alloy discovery: a perspective - Journal of Materials Informatics (北航): https://www.oaepublish.com/articles/jmi.2025.79
[26] AI Design for High Entropy Alloys: Progress, Challenges and Future Prospects - Metals (上海交大): https://www.mdpi.com/2075-4701/15/9/1012
[27] Machine-learning model for predicting phase formations of high-entropy alloys - Physical Review Materials (南航): https://link.aps.org/doi/10.1103/PhysRevMaterials.3.095005
[28] Machine Learning-Based Computational Design Methods for High-Entropy Alloys - CityUHK Scholars: https://scholars.cityu.edu.hk/en/publications/machine-learning-based-computational-design-methods-for-high-entr
[29] Institute of Metal Research, CAS: http://english.imr.cas.cn
[30] Machine Learning/AI-Assisted Development of High-Performance Alloys - JMI Special Topic: https://www.oaepublish.com/specials/jmi.2330
[31] Phase prediction and experimental realisation of a new high entropy alloy using machine learning - Scientific Reports: https://pmc.ncbi.nlm.nih.gov/articles/PMC10036487
[32] Prediction and design of high hardness high entropy alloy through machine learning - Materials & Design (LANL): https://lanlexperts.elsevierpure.com/en/publications/prediction-and-design-of-high-hardness-high-entropy-alloy-through
[33] Prediction of the Composition and Hardness of High-Entropy Alloys by Machine Learning - JOM: http://ui.adsabs.harvard.edu/abs/2019JOM....71j3433C/abstract
[34] Database Versions - Materials Project Documentation: https://docs.materialsproject.org/changes/database-versions
[35] Google DeepMind Adds Nearly 400,000 New Compounds to Berkeley Lab's Materials Project - Berkeley Lab: https://newscenter.lbl.gov/2023/11/29/google-deepmind-new-compounds-materials-project
[36] Scaling deep learning for materials discovery (GNoME) - Nature: https://pmc.ncbi.nlm.nih.gov/articles/PMC10700131
[37] Reflections on one million compounds in the Open Quantum Materials Database (OQMD) - J. Phys. Mater.: https://iopscience.iop.org/article/10.1088/2515-7639/ac7ba9/ampdf
[38] Aflow - Automatic FLOW for Materials Discovery: https://aflowlib.org
[39] aflow.org: A web ecosystem of databases, software and tools - Computational Materials Science: https://www.sciencedirect.com/science/article/abs/pii/S0927025622005195
[40] Automatic Flow for Materials Discovery (AFLOW) - Materials Genome Initiative: https://www.mgi.gov/content/automatic-flow-materials-discovery-aflow
[41] NIST-JARVIS: https://jarvis.nist.gov
[42] JARVIS-DFT Documentation: https://jarvis-materials-design.github.io/dbdocs/jarvisdft
[43] The joint automated repository for various integrated simulations (JARVIS) - npj Computational Materials: https://www.nature.com/articles/s41524-020-00440-1
[44] NOMAD: A distributed web-based platform for managing materials science research data - JOSS: https://pure.mpg.de/rest/items/item_3684784_3/component/file_3684785/content
[45] NOMAD - re3data.org: https://www.re3data.org/repository/r3d100011583
[46] The NOMAD Artificial-Intelligence Toolkit - npj Computational Materials: https://www.nature.com/articles/s41524-022-00935-z
[47] Citrination（Open Citrination退役公告）: https://citrination.com
[48] Atomly materials database—Institute of Physics, CAS: https://english.iop.cas.cn/news/202107/t20210716_275954.html
[49] Table of Datasets - matminer Documentation: https://hackingmaterials.lbl.gov/matminer/dataset_summary.html
[50] MatSciML: A Broad, Multi-Task Benchmark for Solid-State Materials Modeling - arXiv: https://arxiv.org/abs/2309.05934
[51] Atomistic Line Graph Neural Network (ALIGNN) - npj Computational Materials: https://www.nature.com/articles/s41524-021-00650-1
[52] usnistgov/alignn - GitHub: https://github.com/usnistgov/alignn
[53] JARVIS-ALIGNN, JARVIS-ALIGNN-FF - NIST: https://www.nist.gov/programs-projects/jarvis-alignn-jarvis-alignn-ff
[54] Evaluation of the MACE force field architecture - Journal of Chemical Physics: https://pubs.aip.org/aip/jcp/article/159/4/044118/2904837/Evaluation-of-the-MACE-force-field-architecture
[55] SchNet - EmergentMind: https://www.emergentmind.com/topics/schnet
[56] QMALL: Do Better QM9 Models Extrapolate as Better Quantum Chemical Property Predictors? - NeurIPS 2022 ML4PS: https://ml4physicalsciences.github.io/2022/files/NeurIPS_ML4PS_2022_56.pdf
[57] Transformer-generated atomic embeddings - Nature Communications: https://pmc.ncbi.nlm.nih.gov/articles/PMC11782585
[58] CPGN: Dual-Level Atomic and Coordination Geometry Learning for Crystal Property Prediction - arXiv: https://arxiv.org/html/2607.24818v1
[59] Graph Comparison of Molecular Crystals in Band Gap Prediction Using Neural Networks - ACS Omega: https://pmc.ncbi.nlm.nih.gov/articles/PMC10601046
[60] Jacobs et al., Machine Learning: Science and Technology 5, 045051 (2024): https://www.osti.gov/pages/servlets/purl/2583997
[61] LLM4Mat-bench: Benchmarking large language models for materials property prediction - Machine Learning: Science and Technology: https://iopscience.iop.org/article/10.1088/2632-2153/add3bb
[62] MatterChat: A multi-modal LLM for materials science - Nature Machine Intelligence: https://www.nature.com/articles/s42256-026-01214-y
[63] Matbench: Benchmarking Materials Property Prediction Methods - GitHub/npj Comput. Mater.: https://github.com/materialsproject/matbench
[64] MD-HIT: Machine learning for material property prediction with dataset redundancy control - npj Computational Materials: https://www.nature.com/articles/s41524-024-01426-z
[65] Multi-objective optimization in machine learning assisted materials design and discovery - Journal of Materials Informatics: https://www.oaepublish.com/articles/jmi.2024.108
[66] Machine learning guided resolution of mechanical trade-off in polymer composites - Nature Communications: https://www.nature.com/articles/s41467-026-69872-5
[67] Multi-objective Optimization for Materials Discovery via Adaptive Design - Scientific Reports: https://pmc.ncbi.nlm.nih.gov/articles/PMC5829239
[68] Machine Learned Force Fields - QuantumATK Documentation: https://docs.quantumatk.com/atomistic/Machine_Learned_Forcefields.html
[69] Duplicate structures haunt crystallography databases - C&EN: https://cen.acs.org/research-integrity/Duplicate-structures-haunt-crystallography-databases/103/web/2025/12
[70] AI-Accelerated Materials Discovery in 2026 - Cypris: https://www.cypris.ai/insights/ai-accelerated-materials-discovery-in-2025-how-generative-models-graph-neural-networks-and-autonomous-labs-are-transforming-r-d
[71] A Survey of AI for Materials Science: Foundation Models, LLM Agents, Datasets, and Tools - arXiv: https://arxiv.org/html/2506.20743v1
[72] Applications of natural language processing and LLMs in materials discovery - npj Computational Materials: https://www.nature.com/articles/s41524-025-01554-0
[73] Large language models in materials science and the need for open-source approaches - arXiv: https://arxiv.org/html/2511.10673v1
[74] Benchmarking LLMs for Molecular Property Prediction: https://hunterheidenreich.com/notes/chemistry/llm-applications/benchmarking-llms-molecule-prediction
[75] Recent advances and applications of machine learning in solid-state materials science - npj Computational Materials: https://www.nature.com/articles/s41524-019-0221-0
