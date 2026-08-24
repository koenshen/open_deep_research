# 大语言模型与生成式AI在药物系统性评估中的应用现状与发展趋势调研报告

## 一、背景与总体判断

药物研发面临的根本困境在于：**约90%的候选药物在临床试验中失败**，其中安全性因素（毒性与不良反应）与药效因素并列为首要失败原因——约30%的临床前候选化合物（PCC）因毒性失败、约40%因ADMET（吸收、分布、代谢、排泄、毒性）特性不足而失败，近30%的上市药物因不可预见的毒性反应撤市[1][2][3]。传统动物试验存在根本性局限：**动物与人类的肝毒性一致性平均仅约55%**，每种动物试验耗时6—24个月、耗资常超百万美元[1][3]。

在此背景下，大语言模型（LLM）与生成式AI被视为变革药物评估范式的潜在力量。截至2026年8月，该领域正处于从"炒作"到"临床验证"的关键转折期[4][5]。一项2026年发表的同行评议综述（*MDPI Pharmaceuticals*）评估认为，当前AI驱动的药物发现平台"仍受限于生物复杂性、重现性不足与临床验证不充分"，AI在药物发现领域"处于高投入但有限验证临床影响的转型阶段"[5]。据行业统计，AI发现的分子I期临床成功率可达80—90%（高于历史平均的40—65%），但**II期成功率（约40%）与历史水平持平**；在研6,147种药物中仅约67种（1%）为AI发现，其中仅24种（0.4%）涉及AI发现的靶点[5][6]。截至2026年7月，**尚无任何由AI发现或设计的药物获得FDA完全批准**，业界对首个AI发现药物获批的预期窗口为2027—2028年[6]。

本报告基于截至2026年8月的公开学术文献、官方监管文件与产业技术报告，系统梳理大模型在模拟药物对机体系统性影响方面的技术现状、多组学整合进展、个体异质性处理、局限挑战与未来方向。

---

## 二、技术现状与能力边界

### 2.1 通用大语言模型在药物安全性评估中的应用

**不良反应（ADR）识别与抽取**是通用LLM应用最广泛的领域。一项系统评估（*Results in Engineering*，2025年12月）对GPT-3.5-turbo、GPT-4o-mini、Phi-3-mini、LLaMA-3.2、DeepSeek与BioMistral-7B等模型进行了微调与上下文学习比较：GPT-4o-mini经微调后在CADEC基准上取得松弛F1=79.06%、在SMM4H上取得66.80%，但仍难以处理现实文本中ADR表达的复杂性与变异性[8]。在精神科ADR检测基准上（NAACL 2025），Claude 3 Opus零样本检测准确率最高（77.41%），Llama 3.1-405B在少样本分类中F1最优（76.69%）；但所有模型均表现出"风险规避"行为，**假阳性率超过70%**，且GPT-4 Turbo误分类了51%的非剂量相关和50%的时间相关ADR[9]。

**药物相互作用（DDI）识别**方面，一项由临床药师验证的基准研究（medRxiv，2025年12月）测试了LLaMA3-70B、GPT-4o-mini与MedGemma-27B三个模型：点对点双药任务中LLaMA3-70B召回率最高（61.7）；配对三药任务GPT-4o-mini准确率最高（86.6%）；列表式4—6药任务MedGemma-27B最佳（80.0%）。**关键发现是：所有模型在24%—30%的案例中未识别X类（应避免合用）的高风险DDI**，包括依诺肝素/阿替普酶（出血风险）、磺胺甲噁唑-甲氧苄啶/螺内酯（高钾血症）等。研究结论明确："LLM尚不适合在无临床医生备份的情况下用于常规DDI识别"[10]。在学术基准上，DDI-JUDGE框架（*Frontiers in Pharmacology*，2025年6月）采用上下文学习+集成判官机制，将DDI预测的少样本AUC提升至0.788，且利伐沙班、辛伐他汀/氟康唑等案例验证了其实用价值[11]。

**FDA自身实践**提供了重要的参照坐标：FDA国家毒理研究中心开发的RxBERT（基于44,990份处方药标签训练）不良事件分类F1达86.5；AskFDALabel系统（基于Llama 3.1-70B+检索增强生成）药物性肝损伤（DILI）分类F1达0.978、心脏毒性分类F1达0.931，一次实施在约15分钟内审查了211种药物的DILI风险（人工需40—60小时）[14]。这提示：**在任务边界清晰、数据经过整理、有专家监督的场景中，领域专用LLM已具备实际部署价值**。

### 2.2 生物医学领域专用模型与治疗学基础模型

**TxGemma**（Google DeepMind，2025年3月）是目前最具代表性的开源治疗学基础模型：基于Gemma 2构建（2B/9B/27B），在Therapeutics Data Commons（TDC）的66项治疗学任务、超1,500万个数据点上微调，**在64/66项任务上达到或超过专用模型**（其中45项胜出）；TxGemma-Chat版本还能用自然语言解释其预测推理（如"为何预测某分子有毒"）[15][16]。配套的**Agentic-Tx**智能体系统（由Gemini 2.0 Pro驱动，配备18个工具）在化学与生物学推理基准上达到SOTA[15][16]。

其他重要的领域专用模型包括：PubMedBERT（BLURB基准得分82.91，月下载量250万）、BioMistral-7B、ClinicalBERT、SciBERT等。FDA的实践数据显示，**通用LLM在药物标签分析上"明显表现不佳"**，而领域微调模型在不良事件提取准确率达91.1%、DILI风险识别达99.4%[13][14]。这表明**领域适配是当前技术路线中决定性能的第一要素**。

### 2.3 蛋白质语言模型与结构预测模型

**AlphaFold 3**（2024年5月，*Nature*）将预测范围从蛋白质扩展到蛋白质-DNA/RNA/配体/化学修饰复合物，在PoseBusters基准上对蛋白质-配体相互作用预测比最佳传统物理工具准确率高约50%，是首个无需输入结构信息即超越物理工具的AI系统[17]。**IsoDDE**（Isomorphic Labs，2026年2月技术报告）进一步在'Runs N Poses'基准上实现准确率翻倍于AlphaFold 3，抗体-抗原结构预测高保真区（DockQ>0.8）较AF3提升2.3倍、较Boltz-2提升19.8倍，结合亲和力预测在FEP+ 4、OpenFE、CASP16三个公共基准上超越所有深度学习方法，甚至可超越不依赖实验晶体结构的物理FEP方法[18]。

**ESM3**（EvolutionaryScale，*Science* 2025）是首个统一推理序列/结构/功能的蛋白质生成模型：98B参数、2.78B蛋白质序列、超过1×10²⁴ FLOPs的训练规模，成功设计了与已知荧光蛋白序列一致性仅58%但功能正常的esmGFP，相当于跨越超5亿年自然进化[19]。该模型路线图明确指向"从分子到细胞的多模态模型"。

必须指出的是：**结构预测能力不等于系统级药物效应预测能力**。行业综述明确指出"蛋白质结构预测已成熟但未解决药物发现——结构预测不保证可成药靶点"[4]。这些模型的能力边界停留在分子相互作用层面（结合姿位、亲和力），尚未延伸至生物体效应。

### 2.4 知识图谱、分子基础模型与毒性预测

分子毒性预测领域已形成成熟基准（Tox21、ToxCast、ClinTox、DILIrank、hERG等）与多种方法。代表性成绩包括：MoltiTox多模态融合模型（分子图+SMILES+2D图像+¹³C NMR谱）在Tox21上ROC-AUC 0.831[2]；InterDILI模型（DILI预测）AUROC达0.97；GNN结合图像方法的肝毒性预测AUROC 0.958；ADMETlab 3.0的hERG预测AUROC约0.94[2][3]。在药物-副作用关系预测上，基于BiomedBERT嵌入的方法AUC达0.915，并在FAERS真实世界数据上获得统计确证（优势比4.822）[12]。

**知识图谱+图神经网络**是DDI预测的主流技术路线。但深圳清华大学团队提出的**DDI-Ben基准**（arXiv 2410.18583）揭示了严重的方法论问题：多数图方法在"分布变化"（已知药→新药）条件下性能大幅下降，而**基于LLM的方法（TextDDI、DDI-GPT）对分布变化最稳健**——因为文本模态携带的药物药理知识（如"支气管舒张活性""毒蕈碱受体结合"）在分子指纹和生物医学网络中并不存在[21]。这一发现对大模型的药物评估价值具有重要意义：**LLM的知识迁移能力恰好弥补了传统结构化方法的冷启动缺陷**。

### 2.5 因果推断、数字孪生、虚拟临床试验与定量系统药理

**因果推断与数字孪生**方面最具里程碑意义的是Unlearn.AI的**PROCOVA方法**：2022年9月获得EMA正式认定，成为"2期和3期连续终点试验主要分析的可接受统计方法"——这是欧洲监管机构首次正式认定基于机器学习的协变量调整方法可用于缩减关键试验样本量；FDA 2024年表示同意。数字孪生可将III期阿尔茨海默病试验的对照组规模缩小至多33%[22]。TWIN-GPT（首个将LLM整合进数字孪生创建的方法）实现了反事实数字孪生AUROC 0.821（接近真实数据0.838），并用于模拟替代治疗方案轨迹[23]。

**虚拟临床试验与试验结局预测**领域，LIFTED多模态混合专家框架在HINT基准上取得III期试验结局预测PR-AUC 88.3；TrialGPT（*Nature Communications*）在患者-试验匹配中使筛查时间减少42.6%、准确率达97.2%[28][29]。但这些系统预测的是"试验能否成功"，而非"药物在体内如何作用"。

**定量系统药理学（QSP）**是目前最接近"系统性药效评估"的范式。南京大学等团队2025年构建的MET异常NSCLC多尺度QSP模型（约130个分子种类、69个方程、16种药物PK模块），通过5,000名虚拟患者的虚拟临床试验，准确再现了tepotinib的临床ORR 45%与mDoR 12.6个月，并完成剂量优化与联合用药设计[50]。QSP在绝经后女性DILI预测中准确再现了临床观察（他莫昔芬组ALT≥3×ULN比例15.7% vs 安慰剂7.4%）[49]。但QSP本质上是**机理驱动的常微分方程建模**，与生成式大模型是互补而非替代关系。

### 2.6 能力边界总结

综合全部证据，当前技术的能力边界可以概括为：

| 任务层级 | 代表模型/方法 | 当前表现 | 是否达到临床可用 |
|---|---|---|---|
| 分子-靶点结合与结构预测 | AlphaFold 3、IsoDDE、ESM3 | 复合物预测超越物理工具 | ✅（发现阶段） |
| 分子毒性/ADMET端点预测 | MoltiTox、InterDILI、TxGemma | AUROC 0.83—0.97 | ✅（筛选阶段） |
| 药物-副作用关系挖掘 | 生物医学BERT嵌入 | AUC 0.915+FAERS验证 | ⚠️（辅助信号） |
| DDI识别 | GPT-4o-mini、MedGemma等 | X类高风险漏检24—30% | ❌（需医生备份） |
| 临床试验结局预测 | LIFTED、TrialGPT | III期PR-AUC 88.3 | ⚠️（决策支持） |
| **全身多器官系统级效应** | （尚不存在） | **无任何模型** | ❌ |

**核心结论：截至2026年8月，没有任何检索到的模型能够对药物进行真正的全身多器官/多系统（phenotypic层级）预测**。最接近"系统级"的路线仍是QSP/DILIsym类机制模型与FAERS/EHR药物警戒数据挖掘（回顾性信号检测），而非生成式模型的前瞻性全身预测。一位AI药物发现公司高管的评价具有代表性："我们有很多预测疗效的模型，但对毒性和耐受性标志物的重视不够"；OpenAI生命科学研究负责人也明确表示："我们尚不认为AI能独立创造新的疾病治疗方法"[4][6]。

---

## 三、与多组学的结合：系统表征药物-机体相互作用

### 3.1 转录组学驱动的药物反应预测

**细胞系药物反应预测**是最成熟的结合方向。Mayo Clinic的**DRPLLM**框架（BICOB 2025）将Llama-8b与深度神经网络结合，使用细胞系基因表达、突变和药物特性的嵌入，在GDSC/CCLE数据集上取得Spearman秩相关0.71—0.74，并在患者来源异种移植（PDX）队列上验证（SCC=0.45）[1]。**CellHit**（*Nature Communications* 2025）用LLM（Mixtral 8x7b、GPT-4）策展药物作用机制（MOA）并映射至Reactome通路：全基因表达模型在GDSC上Pearson ρ=0.89，引入MOA先验后PRISM数据集性能接近翻倍（1,254 vs 762个药物模型ρ>0.2），并在TCGA患者数据中恢复了已知获批药物-癌症关联[30]。**GraphTCDR**（*Neural Networks* 2026）通过异构图表征整合基因表达、CNV、miRNA与药物指纹，在PRISM上PCC提升3.60%、SCC提升4.30%[31]。**PASO**（*PLOS Computational Biology* 2025）整合三组学+通路差异特征+SMILES，在混合划分下R²=0.8880，但**新药（Drug-Blind）划分下R²骤降至0.5253**——对未见化学空间的泛化仍是主要瓶颈[32]。

**单细胞水平**是2025—2026年最活跃的前沿。**scDrugMap**（*Nature Communications* 2026）对8个单细胞基础模型（scFoundation、scGPT、Geneformer、scBERT、UCE等）与2个通用LLM（LLaMa3-8B、GPT-4o-mini）在60个数据集、495,000+细胞上进行了首次系统基准测试：scFoundation表现最强（微调后肿瘤组织平均F1 0.832—0.996），而**GPT-4o-mini在多数设置下接近或低于基线**（胰腺癌F1仅0.190、黑色素瘤0.320），证明未经领域适配的通用LLM缺乏单细胞药物反应预测所需的精度[33]。scGPT嵌入与GNN结合的研究进一步显示，单细胞基础模型嵌入（512维）优于传统基因表达特征，在留一药盲测中对未见药物泛化更好[34]。

**扰动预测**（给定基因/药物扰动预测转录组变化）是"AI模拟实验"的核心。**GEARS**（*Nature Biotechnology* 2024）将基因-基因知识图与深度学习结合，单基因扰动预测MSE改进30—50%，双基因未见组合预测改进53%[35]。但**Ahlmann-Eltze等**（*Nature Methods* 2025）的系统基准指出：**没有任何深度学习模型优于简单线性基线**——这一"基线悖论"引发了领域内对基准指标的大讨论（随后有研究用校准指标反驳，认为问题出在基准而非模型能力）[36][39]。Arc Institute的**State虚拟细胞模型**（训练于1.7亿细胞观察数据+1亿+细胞扰动数据）在扰动效应区分能力上较此前最佳提升50%，Arc主办的**Virtual Cell Challenge 2025**（1,200+团队）结论为"纯端到端学习尚不能解决扰动预测问题，需结合经典统计特征"[37][38]。GenBio AI团队的600+模型大规模基准发现：**互作组先验知识（蛋白质相互作用网络、基因注释）是最强的嵌入来源，注意力多模态融合总是优于最佳单模态**，且遗传扰动预测整体上比化学扰动预测更容易[39]。

### 3.2 蛋白质组学与代谢组学

蛋白质组学方向的代表性项目是TUM的**DROP2AI**，目标是用蛋白质组学+AI开发药物反应预测模型，验证路径为公开数据在硅验证→细胞系/类器官/小鼠模型湿实验→应用于NCT/DKTK-MASTER临床试验患者数据[41]。**BEACON**研究（*Future Pharmacology* 2025）提供了重要的警示性发现：数据驱动的特征选择（R² 0.6—0.96）一致优于通路引导方法（R²约0.2）；但**基因表达训练的模型直接迁移到蛋白质组学数据时R²为负**（如Afatinib的RMSE从1.596升至11.368），揭示转录组→蛋白质组水平的跨组学迁移存在根本性障碍[41]。

代谢组学方面，Sapient Bioanalytics的**DynamiQ**是首个代谢组学基础模型：在67,000+生物样本（13,000+个体）上自监督训练，可构建人类代谢状态"地图"，已在心脏代谢疾病（识别出LDL正常但心血管/糖尿病风险高的亚组）、肿瘤与免疫疾病中展示应用价值[42]。代谢组学被认为能捕捉基因组学无法解释的个体差异——基因组变异对复杂慢性病风险的贡献不足10%，而代谢物作为"中间表型"直接反映环境-机体-药物相互作用[42]。

### 3.3 细胞形态学（Cell Painting）

Cell Painting以六种荧光染料、五个通道成像八种细胞组分，是连接"多组学分子信号"与"细胞表型结果"的关键桥梁。**行业领先实践**包括：Recursion Pharmaceuticals借助Cell Painting在18个月内从发现推进至FDA批准临床的AI发现癌症药物REC-1245；AstraZeneca在8,300个化合物上结合Cell Painting与140项生物活性检测训练深度学习模型（ROC-AUC 0.744），实现14.76×真实活性分子富集；Bayer证明形态学谱在预测线粒体毒性方面优于仅用化学结构（MCC提升约0.08—0.09）；Janssen用形态学特征扩展QSAR适用域约16%[43]。自监督学习（DINO）已能将扰动mAP较CellProfiler提升29%、靶点mAP提升61%[43]。正如密歇根大学Jonathan Sexton所概括的跨组学验证循环："转录组学显示细胞计划做什么、蛋白质组学显示可用机制、代谢组学显示发生中的反应、Cell Painting显示表型结果"[43]。

### 3.4 多模态整合：从分子到人群

在模型层面，多模态EHR+基因组整合研究（All of Us数据，50万+参与者）首次将多基因风险评分（PRS）作为一等数据模态整合进EHR基础模型：10年2型糖尿病预测相对AUPRC提升15.5%，但**PRS的增量效益随EHR历史长度递减**（3年EHR后不再显著）——提示基因组信息与表型信息的互补窗口主要在疾病早期[45]。多模态融合的系统性综述显示，融合策略一致优于单模态基线2—12个百分点，其中文本模态贡献最大边际改进，基因组整合带来约+0.025 AUROC的增量[45][46]。

然而，**多组学整合的临床转化仍面临严峻挑战**。DrEval框架（*Nature Communications* 2026）对5个细胞系数据集+2个离体筛选的系统评估发现：**深度学习模型仅勉强优于预测均值的朴素模型；在留细胞系（LCO）设置下无模型超越调优的随机森林；消融实验显示CNV、甲基化、突变模态并未贡献预测力，甚至引入噪声**[40]。多组学整合综述（*Cambridge Prism: Precision Medicine* 2025）同样指出：数据异质性（批次效应、平台差异）、模型不可解释性与跨队列泛化差是三大核心障碍[44]。

---

## 四、个体异质性处理：个性化药物评估

### 4.1 药物基因组学（PGx）：从基因型到表型

大模型已在PGx领域展示出独特的自动化能力。**PGxAI-Recommender**（*npj Digital Medicine* 2026）是首个自动化生成CPIC式药物基因组学推荐的代理式AI系统：证据提取字段级准确率91.9%，盲法专家评审得分9.0/10（显著优于基线LLM的6.2—7.8），能自动覆盖最多573个基因-药物对（CPIC人工策展为316对），并每周自动扫描新文献更新[47]。双LLM提取研究（*JMIR* 2025）显示，GPT-4o与Gemini-1.5-Pro对385条PharmGKB指南的零样本分类与专家一致率达93.5%与92.7%（κ=0.90/0.89），且采用双模型交叉可将人工审查量降至2.9%[48]。在临床决策支持场景中，"人机共驾驶"（co-pilot）模式显著优于药剂师单独工作：准确率从46%提升至61%，严重伤害错误检出提高1.5倍[54]。

**具体基因-药物关系**的临床证据已相当坚实：CYP2D6代谢65+种临床药物；HLA-B\*58:01与别嘌醇诱导严重皮肤不良反应（SCAR）的OR=117.6（荟萃分析）；DPYD变异携带者接受标准剂量氟尿嘧啶约70%严重毒性风险、约3%致死风险，EMA自2020年要求治疗前筛查，NCCN 2025年更新指南转向"应考虑检测"[49]。但**高遗传OR不等于高临床预测价值**：新加坡HSA数据显示，由于SCAR罕见（约3/1,000），即使HLA-B\*58:01基因分型敏感性>80%，其阳性预测值仅约2%，且检测阴性不能排除风险——个性化评估必须联合年龄、肾功能等非遗传因素[50]。此外，商业PGx检测面板的变异覆盖差异显著（澳大利亚研究显示没有任何两家商业检测评估相同的变异集），Cyrius对全基因组测序的分型显示**泛基因组人群中99.2%的个体至少携带一个可操作药物基因变异**，提示个性化评估的技术基础正在成熟但标准化仍不足[51]。

### 4.2 个性化剂量：CURATE.AI

CURATE.AI是首个在临床试验中验证的AI个性化剂量平台：利用患者自身的小数据集（4—5个剂量-反应数据对）建立N-of-1剖面，动态推荐个体化剂量而非传统最大耐受剂量。PRECISE可行性试验（*npj Precision Oncology* 2025）显示：处方剂量较标准护理平均降低20%，医师遵循率97.2%，毒性率与已知方案相当[51]。但其局限同样明显：10名患者中仅3名达到疗效驱动给药阶段，CEA生物标志物受吸烟、炎症、肝病干扰——**单一生物标志物在真实多系统疾病中的代表性不足**是主要瓶颈[51]。

### 4.3 肠道菌群与药物-微生物组相互作用

肠道菌群是个体异质性的重要来源：UCL综述显示180+药物是肠道细菌酶的底物，Zimmermann等发现271种口服药中三分之二（176种）被肠道细菌化学修饰；粪肠球菌可使他克莫司免疫抑制活性降低15倍；地高辛被Eggerthella lenta灭活[52]。机器学习预测直接微生物药物代谢准确率已超过90%，计算分析系统（如MicrobeRX）可预测人类与肠道微生物的共同药物代谢[52]。*Pharmacogenomics Journal* 2025年的一项系统性比较发现：126/737个药物靶点与肠道/口腔/阴道菌群宏蛋白质组存在>30%的序列一致性，其中病原体靶点平均一致性更高（肠道70.4%）——这为预测药物的菌群脱靶效应提供了新框架[53]。但该领域普遍缺乏大规模可及的体内验证数据，研究几乎全部聚焦远端肠道细菌。

### 4.4 年龄、性别、合并症与特殊人群

QSP/PBPK虚拟人群建模是当前处理人口学异质性的主要技术：已覆盖儿科（出生至18岁）、老年（65—100岁）、妊娠（三孕期）、器官损伤（GFR分层、Child-Pugh）与疾病状态（肥胖、NAFLD/NASH、癌症）[49]。但**QSP/QST模型中仅少数包含年龄和性别人口统计**，儿科药代仍存在转运体成熟、血脑屏障发育等知识缺口。值得注意的监管里程碑是：**anakinra于2022年因COVID-19获得FDA批准，是基于AI/ML方法识别合适患者人群（suPAR≥6 ng/mL）的首次监管决策用途**[49]。

### 4.5 个体异质性处理的整体评估

当前的大模型在个体异质性处理上呈现"两端强、中间弱"格局：**基因型→药物代谢表型**这一端已具备较强的自动化能力（PGxAI-Recommender、CPIC指南自动提取），**分子机制→细胞反应**一端也取得了可观的预测精度；但**从分子/细胞到个体全身反应**的桥梁仍然缺失——年龄、性别、合并症、菌群等因素在多组学药物反应模型中的纳入仍处于起步阶段，缺乏将遗传背景、组学谱与全身生理状态统一编码的多模态框架。

---

## 五、局限与挑战

### 5.1 验证状态：回顾性繁荣与前瞻性匮乏

当前AI药物评估领域面临的最根本挑战是验证状态：**大多数报告的收益来自回顾性基准数据集上的准确率，而非前瞻性临床或湿实验验证**。放射学AI领域仅约29%的工具报告了前瞻性临床测试[7]。在毒理学预测中，动物到人类的跨物种外推一致性仅约55%，而多数AI毒性模型的"金标准"本身也是回顾性数据集[2][3]。图机器学习DDI预测的系统综述指出：仅3项研究明确处理数据泄漏，五类有效性威胁（随机成对划分泄漏、不完整/噪声标签、冷启动评估有限、时间评估稀缺、可解释性验证有限）普遍存在[20]。DrEval的系统评估进一步表明，若不使用归一化指标，模型"记住每种药物平均IC50"即可解释大部分方差[40]。

### 5.2 数据质量与稀缺

FDA的AskFDALabel实践揭示了监管数据的"数据鸿沟"：140,000+份药品标签中的关键安全信息锁定在非结构化文本中，传统方法无法规模化获取[14]。电子病历数据用于毒性预测存在约30%剂量缺失、41%合并用药未记录、25—60%器官毒性生物标志物缺失的问题[3]。EMA反思文件特别指出**数据代表性不足**是独立风险（儿童、罕见病人群）[81]。68%的技术高管认为数据质量与治理差是AI计划失败的首要原因[4]。

### 5.3 幻觉与事实性错误风险

FDA于2025年6月上线的全机构AI工具**Elsa**（由Anthropic Claude驱动）出现了**虚假引用和数据幻觉**问题——2025年7月CNN报道援引六名匿名FDA官员详述Elsa持续引用不存在的研究。FDA局长Makary承认"Elsa像所有LLM一样可能产生幻觉"[65]。WHO 2024年指南将"不准确或虚假应答"列为大型多模态模型的首要风险，并警告"LMM应答可能看起来像人一样权威"，存在自动化偏倚与专业人员技能退化风险[63]。

### 5.4 可解释性与黑箱问题

EMA在监管文件中表示**偏爱可解释模型**，但在合理情况下允许黑箱模型并要求提供可解释性指标；FDA框架则区分"可解释性"（内部逻辑可理解）与"可解释手段"（黑箱加独立的输出表征方法），可接受水平随风险缩放[59][81]。FDA的领域专用模型实践中，"黑箱"的解释性挑战被明确列为局限，最佳实践要求"为可解释性而设计，附引用和置信度分数"[14]。链式思维提示虽能改善多步推理，但"生成的推理链并不总是忠实反映内部计算"[7]。

### 5.5 监管认可度：主要司法辖区全景

**美国FDA**：2025年1月发布草案指南《Considerations for the Use of Artificial Intelligence to Support Regulatory Decision-Making for Drug and Biological Products》（截至2026年年中仍为草案），提出围绕"使用情境"（COU）的**七步风险基础可信度评估框架**，但明确排除纯药物发现与内部运营效率用途[55][82]。2026年1月14日，**FDA与EMA联合发布《Guiding Principles of Good AI Practice in Drug Development》10项原则**，覆盖药物产品全生命周期，强调以人为中心设计、风险基础方法、数据治理与文档化、生命周期管理[57]。FDA还报告2016—2023年收到500多份含AI组件的药物申报，并成立CDER AI委员会[56]。

**欧盟**：EMA反思文件（EMA/CHMP/CVMP/83833/2023，2024年通过）明确将药物发现和非临床开发纳入范围（与FDA不同），要求高影响用途提供完整模型架构、开发/验证日志与训练数据描述[58][81]。2025年3月EMA发布**首个AI方法学资格意见（AIM-NASH）**，认定AI辅助病理分析的临床证据科学有效[58]。欧盟AI法案的分阶段实施中，**附件III高风险义务已推迟至2027年12月2日、附件I高风险义务推迟至2028年8月2日**（因2025年11月《数字综合提案》修订）[60]。医药研发AI是否属高风险尚不明确，欧洲委员会的分类指南已于2026年2月发布草案[60][83]。

**中国**：国家药监局2026年4月发布**《关于"人工智能+药品监管"的实施意见》（国药监综〔2026〕6号）**，目标到2030年初步构建药品监管与AI融合创新体系，明确"AI在药品监管领域的辅助型定位"、"数据驱动、人工复核、全程可追溯"机制，并要求建设"两品一械"大模型[61]。NMPA在2025年的答复中披露：医疗器械领域已批准超110款基于深度学习的第三类AI医疗器械，全球率先发布深度学习辅助决策器械审评要点[62]。CDE正加快推进eCTD 4.0系统（计划2026年底完成开发测试），将其视为"未来CDE运用AI审评的数据基石"[77]。CDE于2026年2月发布基于多区域临床试验数据获益-风险评估的ICH E17实施指导原则[78]。但**FDA/EMA级别的AI数据治理文档要求在中国主要由国际业务驱动而非国内监管需求**[76]。

**国际协调**：ICH尚未发布AI专项文件，依赖E8(R1)与E6(R3) GCP等技术中立指南；ICH M15（模型知情药物开发）草案于2026年2月发布[81]。WHO 2024年发布《Ethics and governance of artificial intelligence for health: Guidance on large multi-modal models》，围绕AI价值链三阶段（开发、提供、部署）提出治理框架，并质疑当前LMM"是否适合医疗使用"——很可能无法满足欧盟与美国医疗器械法规对可解释性、偏倚控制和透明度的高标准[63]。

### 5.6 计算成本与环境成本

AI的环境成本已成为不可忽视的约束：全球数据中心2024年耗电约415 TWh（占全球约1.5%），预计2030年达945 TWh；训练GPT-3耗电约1,287 MWh（约552吨CO2e），GPT-4训练约50 GWh[73][74]。更关键的是**透明度缺口**：斯坦福基金会模型透明度指数（2025年12月）显示13家AI公司中10家未披露任何关键环境指标[73]。在药物安全性验证中，领域特定模型训练需要上千GPU小时[14]。联合国大学2026年报告强调，AI的环境成本取决于"电在哪里产生、由什么能源产生"，低碳电力并不自动意味着低水或低土地足迹[74]。

### 5.7 对"系统性评估"能力的根本限制

综合各项证据，当前大模型尚无法满足"系统性评估药物对机体影响"的最终需求，根本原因有四：**(1) 层级鸿沟**——从分子结合到细胞反应再到器官/全身效应的跨尺度建模链条尚未打通；**(2) 时间维度缺失**——多数模型为静态预测，无法模拟药物暴露-反应的时间动态（QSP虽能但机理覆盖有限）；**(3) 异质性简化**——模型训练数据以细胞系和回顾性队列为主，难以覆盖真实人群的合并症、合并用药与生理变异；**(4) 验证闭环缺失**——从回顾性预测到前瞻性临床确认的完整验证链条极为罕见。

---

## 六、未来发展方向（2026—2030）

### 6.1 技术路线一：多模态基础模型与"虚拟细胞"

未来3—5年最明确的技术趋势是从单模态走向**统一的多模态生物基础模型**：整合DNA序列（DNABERT-2、Nucleotide Transformer、AlphaGenome）、蛋白质（ESM3、AlphaFold系列）、单细胞转录组（scGPT、Geneformer、scFoundation）、细胞形态（Cell Painting自监督）与化学结构（Uni-Mol、ChemBERTa）[72]。Arc Institute将虚拟细胞模型定位为"一系列越来越精确模型中的第一个"，目标是在硅生成假设与临床试验前验证[37]。模型规模与数据规模的持续增长（如PerturbAI的800万细胞大脑CRISPR图谱、KOLF2.1J的250万单细胞扰动图谱）将为下一代模型提供训练基础。产业界判断，**模型层已开始商品化，真正的差异化在于将AI接入LIMS/ELN与数据管道**——"选择模型是最小部分"[72]。

### 6.2 技术路线二：因果AI、数字孪生与QSP融合

因果推断与生成式AI的结合是突破"相关性预测"局限的关键。2026年3月《Drug Discovery Today》综述显示，数字孪生应用已覆盖药物研发全价值链（靶点发现、临床前、临床试验、监管审评、生产、上市后），制造中DT可提升生产力、真实DT可支持个性化照护[69]。EMA已将数字孪生纳入其AI行动计划，Unlearn.AI的数字孪生已在多个III期试验（阿尔茨海默病、ALS等）中应用[69][22]。因果疾病模型（如Atia Bio的亨廷顿病数字孪生，22,770节点、5,383,791条边）代表"第一个真正无假设的人类生物学发现"的尝试[70]。

更现实的融合路径是**机理模型+AI的混合架构**：以QSP/PBPK的常微分方程系统为骨架，嵌入AI/ML模块处理不确定性与数据驱动校正。这种架构既保留机理的可解释性（监管友好），又获得数据驱动的预测精度。

### 6.3 技术路线三：真实世界证据（RWE）整合与智能体AI

FDA草案指南已将RWE生成列为AI使用情境之一[55]。AI可帮助患者分层、从RWD生成合成对照臂、提升操作效率——但这属于"改善读数的概率"而非"革命性改变"[84]。**智能体（Agentic）AI**是2026年的核心架构趋势：OpenAI的GPT-Rosalind（2026年4月，首个生命科学专用推理模型）、Anthropic的Claude for Life Sciences（2025年10月，首批客户含诺和诺德、赛诺菲、AbbVie、阿斯利康、Genmab）、Google的Agentic-Tx均采用"模型+工具+检索"的代理架构[72][15]。诺和诺德的临床研究报告起草从10周以上缩短至约10分钟，FDA内部Elsa将需数天的审评任务缩短至6—15分钟[72][65]。带可验证奖励的强化学习（RLVR）正在训练自主科学代理，但**当前系统在初始假设失败时缺乏创造性问题解决能力，人类科学家仍然不可或缺**[4]。

### 6.4 监管前景：NAMs革命与全球协调

最具变革性的监管动向是**FDA于2025年4月10日宣布分阶段取消动物试验要求**（"New Approach Methodologies"，NAMs）：使用AI计算建模、细胞系与类器官测试、器官芯片与微生理系统及真实世界人类数据，目标"3—5年内使动物研究成为例外而非常态"，首先从单克隆抗体开始[67][68]。这一政策建立在FDA现代化法案2.0（2022年将"动物试验"替换为"非临床试验"）与3.0（2025年）的基础上[67]。但学术警告指出：3—5年时间线"过于乐观"，因为缺乏证明NAMs就绪的非劣性研究，AI模型存在偏倚风险，FDA仅30天IND审阅窗口，建议"试运行"模式并行提交NAMs与动物数据[67]。

全球监管协调方面，FDA-EMA联合原则（2026年1月）、ICH M15（MIDD指南，2026年2月首稿）与英国MHRA的AI Airlock沙盒（第二期2026年完成）共同指向**以"使用情境+风险分层+全生命周期文档化"为核心的国际监管框架**。学术分析提出了三种未来情景：务实趋同（EMA成为事实标准制定者）、战略分化（按辖区并行开发）与监管摩擦加剧；可互操作框架是共同需求[59]。

### 6.5 产业化前景与里程碑时间表

- **短期（2026—2027）**：Insilico Medicine的Rentosertib（首个AI发现并设计的药物）已启动III期（GENESIS-IPF，320名患者）；Isomorphic Labs首批AI设计药物临床试验预计2026年底启动；全球AI药物发现市场预计从2025年50—70亿美元增至2026年80—100亿美元[4][6][72]。
- **中期（2027—2028）**：首个AI发现药物获批的现实窗口；AI每年将产生数十个新IND；中国公司全球生物技术许可份额持续上升（2025年Q1已达32%）[4]。
- **长期（2029—2030）**：NAMs逐步成为主流非临床评估路径；多模态基础模型+数字孪生+因果AI的整合框架有望首次实现"在硅患者"支持监管决策；生成式AI每年为制药业创造600—1100亿美元价值的预期将接受检验[4][6]。

### 6.6 对传统药物研究和多组学评估范式的变革

变革是渐进而深刻的，而非颠覆性的：**(1) 范式层面**，药物评估正从"动物实验优先"转向"计算方法-细胞模型-类器官-真实世界数据"的多支柱NAMs范式（FDA已明确推进）；**(2) 组学层面**，多组学数据将从"关联分析输入"升级为"基础模型训练语料+个体数字孪生构建材料"，转录组/蛋白质组/代谢组/形态学的信息价值将由模型统一编码而非孤立分析；**(3) 决策层面**，监管审评将从"人工阅读申报文件"转向"人机协同的AI辅助审评"（FDA Elsa、EMA Scientific Explorer、中国eCTD+AI审评均为先兆）[61][65][77]；**(4) 产业层面**，AI药物发现公司将分化为软件工具（如Schrödinger）、平台+管线（Recursion、Insilico、Isomorphic）、纯合作与内部基础设施四种模式[84]。

---

## 七、结论

截至2026年8月，大语言模型与生成式AI在药物研发中的应用已从"概念验证"进入"临床验证"阶段，但**距离"模拟药物对机体的系统性影响"这一终极目标仍有显著距离**。

**当前最可靠的成就在两个层面**：分子/细胞层面——结构预测（AlphaFold 3、IsoDDE）、毒性端点预测（AUROC 0.83—0.97）、药物-副作用关系挖掘（AUC 0.915+真实世界验证）；知识/信息层面——临床文本处理（FDA实际部署的AskFDALabel、Elsa）、药物基因组学自动化（PGxAI-Recommender专家评分超越基线）、DDI识别的稳健知识迁移（LLM在分布变化下优于图方法）。**多组学整合**在细胞系和单细胞水平已取得可观进展（scFoundation、GEARS、CellHit），但跨组学迁移与真实人群泛化仍是瓶颈。**个体异质性处理**在遗传药理学维度较成熟，但全身系统维度（年龄、性别、合并症、菌群）的整合建模尚不完善。**监管框架**正在快速成形（FDA七步框架、FDA-EMA联合原则、EU AI Act、中国AI+药品监管意见），为AI评估工具的合规使用提供了路径，但"AI生成证据"进入正式监管决策仍以个案方式推进。

对未来3—5年的判断可以概括为：**分子层级的能力将加速商品化，细胞层级的模型将迎来数据驱动的质变（扰动图谱和虚拟细胞），而器官/全身层级的系统性评估将主要依靠QSP-数字孪生-真实世界证据的混合架构渐进实现**。传统多组学评估范式不会被替代，但会被深度重构——多组学数据将成为大模型的训练语料与个体化预测的锚点，而非孤立的统计输入。正如行业综述所强调的，"AI是强大的工具，而非万灵药"；在可预见的未来，**人机协同（human-in-the-loop）仍将是药物安全性评估的金标准**[4][7]。

---

## 参考资料

[1] Computational toxicology in drug discovery: applications of artificial intelligence in ADMET and toxicity prediction (*Briefings in Bioinformatics*, 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12499773
[2] Recent advances in AI-based toxicity prediction for drug discovery (*Frontiers in Chemistry*, 2025): https://www.frontiersin.org/journals/chemistry/articles/10.3389/fchem.2025.1632046/full
[3] Artificial Intelligence-Driven Drug Toxicity Prediction: Advances, Challenges, and Future Directions (*Toxics*, 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12299075
[4] AI in drug discovery: predictions for 2026 (*Drug Target Review*, 2026): https://www.drugtargetreview.com/ai-in-drug-discovery-predictions-for-2026/1865962.article
[5] AI in Drug Discovery: Clinical Failures, Regulatory Reality, and the Validation Crisis Behind the Hype (*MDPI Pharmaceuticals*, 2026): https://www.mdpi.com/1424-8247/19/6/916
[6] AI Drug Discovery FDA Approvals: The 2026 Reality Check (IntuitionLabs): https://intuitionlabs.ai/articles/ai-drug-discovery-fda-approvals
[7] A survey of LLMs in drug discovery and precision medicine (*Frontiers in Drug Discovery*, 2026): https://www.frontiersin.org/journals/drug-discovery/articles/10.3389/fddsv.2026.1854899/full
[8] Benchmarking large language models for adverse drug reaction extraction in social media and clinical texts (*Results in Engineering*, 2025): https://www.sciencedirect.com/science/article/pii/S2590123025034176
[9] LLMs Struggle to Align with Experts on Addressing Psychiatric Adverse Drug Reactions (NAACL 2025): https://aclanthology.org/2025.naacl-long.553.pdf
[10] Drug-drug interaction identification using large language models (medRxiv, 2025): https://www.medrxiv.org/content/10.64898/2025.12.03.25341549v2.full-text
[11] Improving drug-drug interaction prediction via in-context learning and judging with large language models (*Frontiers in Pharmacology*, 2025): https://www.frontiersin.org/journals/pharmacology/articles/10.3389/fphar.2025.1589788/full
[12] Predicting Drug–Side Effect Relationships From Parametric Knowledge Embedded in Biomedical BERT Models (*JMIR Medical Informatics*, 2025): https://medinform.jmir.org/2025/1/e67513
[13] LLM Benchmarks in Life Sciences: Comprehensive Overview (IntuitionLabs): https://intuitionlabs.ai/articles/large-language-model-benchmarks-life-sciences-overview
[14] Transforming Drug Safety Through Artificial Intelligence, Large Language Models (*BioPharm International*, 2026): https://www.biopharminternational.com/view/drug-safety-artificial-intelligence-large-language-models
[15] Introducing TxGemma: Open models to improve therapeutics development (Google Developers Blog): https://developers.googleblog.com/introducing-txgemma-open-models-improving-therapeutics-development
[16] TxGemma: Efficient and Agentic LLMs for Therapeutics (arXiv 2504.06196): https://arxiv.org/pdf/2504.06196
[17] Accurate structure prediction of biomolecular interactions with AlphaFold 3 (*Nature*, 2024): https://www.nature.com/articles/s41586-024-07487-w
[18] IsoDDE: Unified Computational Drug Design (Isomorphic Labs技术报告, 2026): https://doi.org/10.5281/zenodo.19699685
[19] Evolution of sequence, structure, and function in a generative protein model (ESM3, *Science*, 2025): https://www.science.org/doi/10.1126/science.ads0018
[20] Graph-Based Machine Learning for Predicting Drug–Drug Interactions: A Systematic Review (*Pharmaceuticals*, 2026): https://doi.org/10.3390/ph19081225
[21] DDI-Ben: Distribution-Aware Drug-Drug Interaction Benchmark (arXiv 2410.18583): https://arxiv.org/abs/2410.18583
[22] Virtual Patients, Real Results: How Digital Twins Are Reshaping Drug Development (DIA Global Forum): https://globalforum.diaglobal.org/issue/november-2024/virtual-patients-real-results-how-digital-twins-are-reshaping-drug-development
[23] TWIN-GPT: Digital Twins for Clinical Trials via Large Language Model (arXiv 2404.01273): https://arxiv.org/abs/2404.01273
[24] The future of large language models in toxicological risk assessment (*Public Health Toxicology*, 2025): https://www.publichealthtoxicology.com/The-future-of-large-language-models-in-toxicological-risk-assessment-Opportunities,202241,0,2.html
[25] Applications of Federated Large Language Model for Adverse Drug Reactions Prediction (*JMIR*, 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12516295
[26] Large language models for drug discovery and development (*Patterns*, 2025): https://www.sciencedirect.com/science/article/pii/S2666389925001941
[27] LIFTED: A multimodal mixture-of-experts framework for clinical trial outcome prediction (arXiv 2402.06512): https://arxiv.org/abs/2402.06512
[28] TrialGPT: An AI-powered assistant for patient-trial matching (*Nature Communications*; arXiv 2307.15051): https://arxiv.org/abs/2307.15051
[29] CellHit: Learning and actioning general principles of cancer cell drug sensitivity (*Nature Communications*, 2025): https://www.nature.com/articles/s41467-025-56827-5
[30] DRPLLM: A Large Language Model-Based Framework for Predicting Drug Response in Cancer Using Multi-Omics Data (Mayo Clinic, BICOB 2025): https://mayoclinic.elsevierpure.com/en/publications/drpllm-a-large-language-model-based-framework-for-predicting-drug
[31] GraphTCDR: Prediction of cancer drug response based on heterogeneous graph neural networks and multi-omics data (*Neural Networks*, 2026): https://www.sciencedirect.com/science/article/abs/pii/S0893608025008822
[32] PASO: Anticancer drug response prediction integrating multi-omics pathway-based difference features (*PLOS Computational Biology*, 2025): https://journals.plos.org/ploscompbiol/article?id=10.1371%2Fjournal.pcbi.1012905
[33] scDrugMap: benchmarking large foundation models for drug response prediction (*Nature Communications*, 2026): https://www.nature.com/articles/s41467-025-67481-2
[34] Integrating Single-Cell Foundation Models with Graph Neural Networks for Drug Response Prediction (arXiv 2504.14361): https://arxiv.org/html/2504.14361v1
[35] GEARS: Predicting transcriptional outcomes of novel multigene perturbations (*Nature Biotechnology*, 2024): https://www.nature.com/articles/s41587-023-01905-6
[36] Ahlmann-Eltze et al.: Deep-learning-based gene perturbation effect prediction does not yet outperform simple linear baselines (*Nature Methods*, 2025): https://www.nature.com/articles/s41592-025-02772-6
[37] Arc Institute Releases its First Virtual Cell Model "State": https://www.biopharmatrend.com/news/arc-institute-releases-its-first-virtual-cell-model-trained-on-270-million-cells-1302
[38] Virtual Cell Challenge 2025 Wrap-Up (Arc Institute): https://arcinstitute.org/news/virtual-cell-challenge-2025-wrap-up
[39] Foundation Models Improve Perturbation Response Prediction (bioRxiv, 2026): https://www.biorxiv.org/content/10.64898/2026.02.18.706454v1.full-text
[40] Critical evaluation of drug response prediction models with DrEval (*Nature Communications*, 2026): https://www.nature.com/articles/s41467-026-72903-w
[41] BEACON: Decoding Anticancer Drug Response (*Future Pharmacology*, 2025): https://www.mdpi.com/2673-9879/5/4/58
[42] DynamiQ: Metabolomics Foundation Model (Sapient Bioanalytics): https://sapient.bio/resources/metabolomics-foundation-model
[43] Self-supervision advances morphological profiling by unlocking powerful image representations (*Scientific Reports*, 2025): https://www.nature.com/articles/s41598-025-88825-4
[44] Precision oncology: Computational methods for multi-omics data integration to improve drug response prediction (*Cambridge Prism: Precision Medicine*, 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12973241
[45] Integrating Genomics into Multimodal EHR Foundation Models (arXiv 2510.23639): https://arxiv.org/html/2510.23639v1
[46] Multi-modal AI in precision medicine: integrating genomics, imaging, and EHR data (*Frontiers in Artificial Intelligence*, 2026): https://pmc.ncbi.nlm.nih.gov/articles/PMC12819606
[47] PGxAI-Recommender: An agentic AI system for automated pharmacogenomic recommendation generation (*npj Digital Medicine*, 2026): https://www.nature.com/articles/s41746-026-02590-w
[48] Extracting Clinical Guideline Information Using Two Large Language Models (*JMIR*, 2025): https://www.jmir.org/2025/1/e73486
[49] HLA-B\*58:01 genotyping prevalence and association with allopurinol-induced SCARs: living systematic review and meta-analysis (*Scientific Reports*, 2025): https://www.nature.com/articles/s41598-025-16062-w
[50] HSA: Allopurinol-induced SCARs and the role of HLA-B\*5801 genotyping – a reminder: https://www.hsa.gov.sg/announcements/allopurinol-induced-severe-cutaneous-adverse-reactions-and-the-role-of-hla-b-5801-genotyping-a-reminder
[51] PRECISE CURATE.AI feasibility trial (*npj Precision Oncology*, 2025): https://www.nature.com/articles/s41698-025-00835-7
[52] Mc Coubrey et al.: Predicting Drug-Microbiome Interactions (UCL综述): https://discovery.ucl.ac.uk/10136215/3/Orlu_ML%20microbiome%20BA%20final.pdf
[53] Similarity of drug targets to human microbiome metaproteome promotes pharmacological promiscuity (*The Pharmacogenomics Journal*, 2025): https://www.nature.com/articles/s41397-025-00367-0
[54] LLM as clinical decision support system augments medication safety in 16 clinical specialties (*Cell Reports Medicine*, 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12629785
[55] FDA 草案指南: Considerations for the Use of Artificial Intelligence To Support Regulatory Decision-Making for Drug and Biological Products (2025): https://www.fda.gov/regulatory-information/search-fda-guidance-documents/considerations-use-artificial-intelligence-support-regulatory-decision-making-drug-and-biological
[56] FDA Artificial Intelligence for Drug Development (CDER网页): https://www.fda.gov/about-fda/center-drug-evaluation-and-research-cder/artificial-intelligence-drug-development
[57] FDA-EMA: Guiding Principles of Good AI Practice in Drug Development (2026): https://www.fda.gov/media/189581/download
[58] EMA Artificial intelligence 官方页面: https://www.ema.europa.eu/en/about-us/how-we-work/data-regulation-big-data-other-sources/artificial-intelligence
[59] The future of AI regulation in drug development (*Journal of Law and the Biosciences*, 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12598624
[60] The EU AI Act & Pharma: Compliance Guide (IntuitionLabs, 2026): https://intuitionlabs.ai/articles/eu-ai-act-pharma-compliance
[61] 国家药监局关于"人工智能+药品监管"的实施意见（国药监综〔2026〕6号）: https://www.nmpa.gov.cn/xxgk/fgwj/gzwj/gzwjzh/20260402091552114.html
[62] 国家药监局对十四届全国人大三次会议第3816号建议的答复（国药监建〔2025〕67号）: https://www.nmpa.gov.cn/zwgk/jyta/rdjy/20251014091946151.html
[63] WHO: Ethics and governance of artificial intelligence for health: Guidance on large multi-modal models (2024): https://iris.who.int/server/api/core/bitstreams/e9e62c65-6045-481e-bd04-20e206bc5039/content
[64] A systematic review of ethical considerations of LLMs in healthcare (*Frontiers in Digital Health*, 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12460403
[65] FDA's Elsa AI Tool Raises Accuracy and Oversight Concerns (*Applied Clinical Trials*, 2025): https://www.appliedclinicaltrialsonline.com/view/fda-elsa-ai-tool-raises-accuracy-and-oversight-concerns
[66] FDA Launches Agency-Wide AI Tool (FDA新闻稿, 2025): https://www.fda.gov/news-events/press-announcements/fda-launches-agency-wide-ai-tool-optimize-performance-american-people
[67] Gerke, Balamut & Wagner: The FDA's Plan to Phase Out Animal Testing (*NIHPA*, 2026): https://pmc.ncbi.nlm.nih.gov/articles/PMC12834477
[68] FDA Announces Plan to Phase Out Animal Testing Requirement (2025): https://www.fda.gov/news-events/press-announcements/fda-announces-plan-phase-out-animal-testing-requirement-monoclonal-antibodies-and-other-drugs
[69] Digital twins for accelerating drug discovery and development (*Drug Discovery Today*, 2026): https://www.sciencedirect.com/science/article/pii/S135964462600022X
[70] Causal artificial intelligence and digital twins are transforming drug discovery (*Nature Biopharma Dealmakers*): https://www.nature.com/articles/d43747-024-00077-9
[71] NVIDIA Partners With Novo Nordisk and DCAI to Advance Drug Discovery (2025): https://investor.nvidia.com/news/press-release-details/2025/NVIDIA-Partners-With-Novo-Nordisk-and-DCAI-to-Advance-Drug-Discovery/default.aspx
[72] AI models for Life Sciences in 2026 (CodePhusion): https://codephusion.com/blog/ai-models-for-life-sciences
[73] How Much Carbon Does AI Actually Use? (CNaught, 2026): https://www.cnaught.com/blog/how-much-carbon-does-ai-actually-use-and-why-its-so-hard-to-find-out
[74] Environmental Cost of Artificial Intelligence (联合国大学UNU-INWEH, 2026): https://unu.edu/inweh/collection/environmental-cost-of-AIs-Enrgy-Use-Carbon-water-and-land-footprints
[75] MHRA: AI Airlock Sandbox Phase 2 Programme Report (2026): https://www.gov.uk/government/publications/ai-airlock-sandbox-phase-2-programme-report
[76] FDA与EMA联合发布AI药物开发10项原则：深度解读与实操指南: https://blog.brunslab.com/fda%E4%B8%8Eema%E8%81%94%E5%90%88%E5%8F%91%E5%B8%83ai%E8%8D%AF%E7%89%A9%E5%BC%80%E5%8F%9110%E9%A1%B9%E5%8E%9F%E5%88%99%EF%BC%9A%E6%B7%B1%E5%BA%A6%E8%A7%A3%E8%AF%BB%E4%B8%8E%E5%AE%9E%E6%93%8D%E6%8C%87
[77] CDE将强制实施eCTD，AI审评还有多远？（中国药促会）: https://www.phirda.com/artilce_40877.html
[78] CDE发布《新药全球同步研发中基于多区域临床试验数据进行获益-风险评估的指导原则（试行）》(2026): https://m.cnpharm.com/c/2026-02-25/1091597.shtml
[79] 环球律师事务所：中国"30天IND优化路径"分析 (2025): https://www.glo.com.cn/Content/2025/12-17/1413383142.html
[80] Consternation as Congress proposal for autonomous prescribing AI coincides with the haphazard cuts at the FDA (*npj Digital Medicine*, 2025): https://www.nature.com/articles/s41746-025-01540-2
[81] Regulating AI in Drug Discovery: What FDA, EMA, and ICH Guidance Means for Pharma R&D (*Drug Discovery News*, 2026): https://www.drugdiscoverynews.com/regulating-ai-in-drug-discovery-what-fda-ema-and-ich-guidance-means-for-pharma-r-d-17366
[82] FDA's Action Plan for AI in Drug Development (*Drug Discovery News*): https://www.drugdiscoverynews.com/fda-s-action-plan-for-ai-in-drug-development-what-scientists-need-to-know-17367
[83] EU Commission drafts guidelines on classifying high-risk systems under the AI Act (RAPS): https://www.raps.org/resource/eu-commission-drafts-guidelines-on-classifying-high-risk-systems-under-the-ai-act.html
[84] AI Drug Discovery 2026: Insilico, Recursion, Schrödinger, AlphaFold3 (PDPSpectra): https://pdpspectra.com/blog/drug-discovery-ai-platforms-2026
[85] AI Drug Discovery: what are the top startups now? (New Market Pitch): https://newmarketpitch.com/blogs/news/ai-drug-discovery-top-startups
