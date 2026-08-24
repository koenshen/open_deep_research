# 慢性抗原刺激下CD8+ T细胞线粒体动力学与表观遗传重塑驱动命运分岔的系统调研报告

## 执行摘要

本报告系统梳理了慢性抗原刺激（肿瘤微环境、HIV潜伏感染等）条件下，CD8+ T细胞线粒体动力学（融合/裂变平衡）如何通过代谢-表观遗传互作网络（m6A RNA甲基化修饰、乳酸介导的组蛋白乳酸化等）驱动终末耗竭（terminal exhaustion）与组织驻留记忆（Tissue-Resident Memory, Trm）细胞命运分岔的分子机制。报告涵盖五大模块：①线粒体动力学在T细胞分化中的动态变化与功能影响；②线粒体动力学与m6A修饰、组蛋白乳酸化之间的交叉调控网络；③代谢-表观遗传互作驱动命运分岔的转录因子枢纽机制；④定量建模分析框架；⑤截至2026年的最新进展、治疗靶点与未解决问题。

**重要文献信息更正**：经核查，研究简报中提及的三篇关键文献存在引用信息错误，本节集中更正如下（详细内容见对应模块）：

| 文献 | 实际发表信息 | 正确DOI/PMID |
|------|-------------|-------------|
| Buck et al. 线粒体动力学控制T细胞命运 | **Cell** 2016, 166(1):63-76（非Nature） | DOI: 10.1016/j.cell.2016.05.035；PMID: 27293185 |
| Bengsch et al. PD-1与CD8+ T细胞耗竭代谢 | **Immunity** 2016, 45(2):358-373（非2017年） | DOI: 10.1016/j.immuni.2016.07.008；PMID: 27496729 |
| Yu et al. 肿瘤浸润CD8+ T细胞线粒体动力学紊乱 | **Nature Immunology** 2020, 21(12):1540-1551（非Cell 2015） | DOI: 10.1038/s41590-020-0793-3；PMID: 33020660 |
| Zhang et al. 组蛋白乳酸化首次报道 | **Nature** 2019, 574(7779):575-580 | DOI: 10.1038/s41586-019-1678-1；PMID: 31645732（非31367043） |
| Li et al. m6A与T细胞稳态 | **Nature** 2017（标题为"m6A mRNA methylation controls T cell homeostasis by targeting the IL-7/STAT5/SOCS pathways"） | PMID: 28792938（非28111072） |

---

## 模块一：线粒体动力学（融合/裂变平衡）在CD8+ T细胞分化中的动态变化

### 1.1 奠基性发现：线粒体重塑是指导T细胞代谢编程的信号机制

2016年，Pearce团队发表了该领域里程碑式论文，确立了线粒体动力学对T细胞命运的因果调控地位[1]。核心发现如下：

- **效应T（TE）细胞具有点状（punctate）线粒体**，线粒体裂变（fission）占主导；
- **记忆T（TM）细胞维持融合的线粒体网络**，融合蛋白OPA1介导的线粒体融合占主导；
- **Opa1是感染后记忆T细胞（而非效应T细胞）所必需的**；在效应T细胞中强制融合可赋予其记忆T细胞特征并增强抗肿瘤功能；
- 机制层面：记忆T细胞中的线粒体融合通过改变嵴（cristae）形态，配置电子传递链（ETC）复合物关联，有利于氧化磷酸化（OXPHOS）和脂肪酸氧化（FAO）；而效应T细胞中的裂变导致嵴扩张、降低ETC效率并促进有氧糖酵解；
- 药理学上，使用M1 + Mdivi-1联合促进融合可改善过继细胞免疫治疗的抗肿瘤效果；人类CD8+ T细胞同样经历线粒体重塑，提示转化相关性[1]。

这一发现奠定了"线粒体形态→代谢编程→T细胞命运"的因果框架：**融合=记忆/长寿/OXPHOS，裂变=效应/短寿/糖酵解**。

### 1.2 效应T细胞中的线粒体裂变：Drp1的调控机制

Drp1（DNM1L）是主要的促裂变蛋白。其活性受磷酸化修饰调控：非活性状态下定位于胞质，**丝氨酸637磷酸化抑制其活性，丝氨酸616磷酸化激活其线粒体碎片化功能**；对接至线粒体外膜由Mff、hFis1、MiD49/51等受体介导[11][37]。

Drp1介导的裂变在T细胞激活中的多重功能包括[11][37]：
- **免疫突触钙信号**：TCR刺激后，线粒体迁移至免疫突触下方的质膜，摄取钙以维持T细胞激活所需的持续低水平钙内流；Drp1依赖性碎片化允许线粒体沿微管向免疫突触移动；
- **mTOR-cMyc-糖酵解轴**：Drp1消融导致胞质钙增加、AMPK过度激活、mTOR/cMyc下调、糖酵解参与不良，损害克隆扩增；
- **迁移与趋化**：快速定向迁移期间，Drp1 Ser616磷酸化（由ERK通路驱动）使线粒体定位于uropod提供ATP；
- **活化诱导的细胞死亡（AICD）**：Drp1转位至线粒体、碎片化并开放嵴，释放死亡执行因子。

但2024年Stevens等人的研究对DRP1在记忆细胞形成中的作用提出了更精细的刻画[7]：DRP1缺陷导致体外刺激后>75%的CD8+ T细胞呈现细长线粒体（对照组25%），但备用呼吸能力（SRC）和OXPHOS无显著改变；DRP1缺失损害初级CD8+ T细胞反应（降低2.5-3倍），伴随CD3ζ磷酸化显著降低和增殖延迟；**但在混合骨髓嵌合体竞争实验中，DRP1缺陷T细胞在初级、记忆和次级反应中均无法与野生型竞争**（初级反应小6倍、次级反应小2.5倍）。该研究还警示：**Mdivi-1对DRP1的特异性已受到质疑（其实际抑制ETC复合物I）**，既往药理学结论需重新审视[7]。

### 1.3 记忆T细胞中的线粒体融合：OPA1与MFN2

**OPA1**是记忆T细胞线粒体融合的关键执行者。Buck 2016年研究证明Opa1对记忆T细胞必需[1]。2025年Willett等人的新研究进一步揭示OPA1的复杂功能：**OPA1对体内快速分裂的效应CD8+ T细胞同样至关重要**，且删除MFN1和MFN2不能完全重现OPA1缺陷表型，提示OPA1具有非融合相关功能——OPA1缺陷细胞"严重缺乏氨基酸"，其对效应细胞扩增的需求与细胞分裂时的氨基酸可用性相关[8]。胸腺发育研究也表明，OPA1是DN3阶段胸腺细胞成熟所必需的，DN3细胞高度依赖OXPHOS，Opa1缺失损害其呼吸并导致存活的成熟T细胞无法产生代谢健康的长期记忆细胞[16→见1.6。

**MFN2**在CD8+ T细胞抗肿瘤功能中的新机制于2023年由Science Immunology报道[5]：**MFN2通过与内质网嵌入的Ca²⁺-ATPase SERCA2相互作用增强线粒体-内质网接触（MERC）**，促进高效线粒体代谢所需的线粒体Ca²⁺内流；MFN2刺激SERCA2的内质网Ca²⁺回收活性，防止过量线粒体Ca²⁺积累和凋亡——这是一种"栓系-缓冲机制"（tethering-and-buffering mechanism）。CD8+ T细胞中Mfn2基因消融损害线粒体代谢和功能、促进肿瘤进展；**癌症患者中CD8+ T细胞的MFN2表达与更好的生存相关**，增强MFN2表达可改善小鼠癌症免疫治疗疗效[5]。

**PGC-1α与线粒体生物发生**：Dumauthioz等人2021年证明，强制PGC-1α表达可促进CD8+ T细胞的中央记忆（Tcm）形成（而非Trm生成），增加线粒体质量、呼吸能力和SRC，在B16-OVA黑色素瘤模型中显著延缓肿瘤生长；TIL中PGC-1α表达较脾脏CD8+ T细胞降低，提示肿瘤微环境抑制线粒体生物发生[12]。

### 1.4 耗竭T细胞中的线粒体形态与功能障碍

慢性抗原刺激下，耗竭T细胞（Tex）的线粒体呈现独特的病理性改变。综合多篇原始论文与权威综述[1][2][3][9][10][38]，其特征可归纳为：

| 特征 | 效应T细胞 | 记忆T细胞 | 耗竭T细胞 |
|------|----------|----------|----------|
| 线粒体形态 | 碎片化/点状（Drp1裂变） | 细长融合网络（OPA1融合） | 去极化线粒体积累；形态异常（慢性LCMV早期为融合伴嵴延长；TIL中碎片化伴ROS积累） |
| 嵴形态 | 嵴扩张、ETC效率低 | 紧密嵴、ETC超复合物 | 嵴异常（CHCHD3/CHCHD10减少） |
| 代谢模式 | 有氧糖酵解 | FAO + OXPHOS + 高SRC | 糖酵解和OXPHOS均受抑（生物能量不足）；终末Tex依赖糖酵解 |
| ROS水平 | 中等/瞬时（信号） | 低 | 高（积累） |
| 线粒体自噬 | 正常 | 正常 | 受损（PINK1/Parkin通路障碍） |

**Bengsch等人2016年的关键发现**奠定了"代谢失调是耗竭的早期驱动因素而非仅仅后果"这一范式[2]：
- 在慢性LCMV Clone 13感染的第一周内——严重功能障碍发展之前——病毒特异性CD8+ T细胞已无法匹配急性感染效应T细胞的生物能量水平；
- 早期Tex细胞具有更高的线粒体质量但显著更多的**去极化线粒体**，线粒体ROS增加，线粒体形态改变（融合线粒体伴嵴延长）；
- **PD-1被确定为早期代谢功能障碍的关键上游调节因子**：PD-1抑制PGC-1α表达；基因删除PD-1可增加葡萄糖摄取、减少线粒体去极化、改善呼吸和糖酵解能力；逆转录病毒过表达PGC-1α可纠正代谢改变并改善发育中Tex细胞的效应功能；
- 在已建立的慢性感染中，抗PD-L1阻断治疗**特异性地在PD-1^Int T-bet^Hi祖细胞亚群中重编程代谢**（而非PD-1^Hi Eomes^Hi终末分化亚群）；
- 短期雷帕霉素治疗减少线粒体质量但以剩余效应功能为代价[2]。

**Yu等人2020年的研究**将线粒体功能障碍与耗竭的表观遗传重编程直接因果关联[3]：
- 肿瘤浸润T淋巴细胞（TIL）因**线粒体自噬活性降低**而积累去极化线粒体，表现出终末耗竭的功能、转录组和表观遗传特征；
- 机制上由TCR刺激、微环境应激因素和PD-1信号的协同作用诱导；
- **用药理学抑制剂强制积累去极化线粒体可诱导向终末耗竭的表观遗传重编程**——直接证明线粒体失调导致（而非伴随）T细胞耗竭；
- **补充烟酰胺核苷（nicotinamide riboside, NR）**可增强T细胞线粒体适应性并改善对抗PD-1治疗的反应性[3]。

### 1.5 慢性抗原刺激下PD-1对线粒体动力学的双重抑制

PD-1信号对线粒体功能存在双重抑制机制：

**第一重：抑制线粒体生物发生。** PD-1通过Blimp1介导的PGC-1α抑制促使代谢改变，该机制在HIV-1病毒血症感染者的耗竭CD8+ T细胞中尤为突出[9][10]。

**第二重：抑制线粒体裂变。** Simula等人2022年证明[6]：PD-1信号通过抑制TCR/CD28信号下游的ERK1/2和mTOR通路，**下调Drp1在Ser616位点的磷酸化**，从而阻止T细胞刺激后的线粒体碎片化。在MC38肿瘤和人类结肠癌中，PD-1^pos CD8+ TIL显示Drp1活性下调（Ser616磷酸化降低）和更细长/融合的线粒体。功能后果是：Drp1活性下调降低PD-1^pos肿瘤浸润T细胞的运动性和增殖。**治疗意义极为重要**：在T细胞特异性Drp1消融（Drp1-cKO）小鼠中，抗PD-1治疗的疗效从约60%降至约20%——说明完整的Drp1裂变程序是检查点阻断治疗起效的前提[6]。

这两重抑制造成一个悖论性局面：**PD-1既损害线粒体质量（通过抑制PGC-1α），又阻止线粒体裂变（通过抑制Drp1）**，使T细胞陷入"低质量、低动态、融合但功能障碍"的线粒体状态。

### 1.6 线粒体ROS、氧化应激与HIF-1α介导的糖酵解重编程

Wu等人2023年发表于Nature Communications的研究提供了迄今最完整的"线粒体功能障碍→耗竭"因果链[4]：

```
线粒体呼吸受损（Slc25a3/mPiC缺失）
    → 戊糖磷酸途径代谢物和NADPH可用性降低
    → 线粒体ROS增加（氧化应激）
    → HIF-1α蛋白酶体降解受抑 → HIF-1α稳定化
    → 糖酵解重编程（HK2、PKM2等上调）
    → Tpex向Tex终末分化转变（TIM-3、LAG-3、PD-1上调，IFNγ/IL-2下调，凋亡增加）
```

关键实验证据[4]：
- **基因删除线粒体磷酸盐载体（mPiC/Slc25a3）**废除线粒体呼吸，足以驱动耗竭标志物表达——即便在急性LCMV Armstrong感染（无慢性抗原）中也出现耗竭表型，证明**线粒体损伤独立于抗原持续存在即可驱动耗竭**；
- 单细胞RNA测序显示：终末Tex细胞从线粒体OXPHOS向有氧糖酵解转换，而前体耗竭T细胞（Tpex）更依赖线粒体呼吸，且Tpex具有更高的线粒体周转率；
- Slc25a3过表达可增强线粒体呼吸并将细胞转向Tpex表型；
- 删除Hif1a可减少糖酵解并使表型转向Tpex特征；
- 药理学上，**2-脱氧葡萄糖（2-DG，糖酵解抑制剂）可改善慢性病毒感染中的CD8+ T细胞功能**，并在CAR-T细胞中轻微改善抗肿瘤反应。

该研究通讯作者Martin Vaeth团队指出："线粒体呼吸是耗竭T细胞干性（stemness）的前提"，并鉴定出这一此前未知的HIF-1α依赖性机制为**T细胞耗竭过程中的"代谢检查点"**[4]。

### 1.7 HIV/慢性感染背景下的线粒体动力学

HIV感染背景下，线粒体动力学存在直接病毒操纵证据：**HIV-1 Vpr蛋白通过VprBP-DDB1-CUL4A泛素连接酶以蛋白酶体依赖方式显著下调线粒体中MFN2的表达水平**[39]。这提示HIV可能通过直接破坏CD8+ T细胞的线粒体融合能力来加速其代谢功能障碍。此外，耗竭T细胞中PD-1通过Blimp1介导的PGC-1α抑制在HIV-1病毒血症感染者中尤为突出[9]。线粒体靶向抗氧化剂可显著改善耗竭的HBV特异性CD8+ T细胞的抗病毒活性，提示ROS在慢性病毒感染相关T细胞耗竭中的关键作用[9→综合]。

### 1.8 模块一未解决问题

1. **线粒体呼吸如何影响T细胞的表观遗传编程**——具体分子连接（代谢物→染色质修饰酶）仍需完整阐释[4]；
2. Drp1在耗竭T细胞中的表达变化和机制仍有待阐明；大多数研究在体外模拟TME，与体内条件不同[11]；
3. Mdivi-1的特异性问题（抑制复合物I而非Drp1）挑战了既往药理学结论，需要遗传学验证[7][11]；
4. 线粒体转移（TNTs、EVs等）效率低（约10%），临床转化困难[9]；
5. 线粒体动力学在不同组织微环境（营养供应、氧张力）中的具体调控机制需进一步研究[4]。

---

## 模块二：m6A RNA修饰与T细胞命运决定

### 2.1 m6A修饰机制概述

m6A（N6-甲基腺嘌呤）是真核生物mRNA中最丰富的内部修饰，约占腺苷总量的0.1-0.6%，主要发生于5'-[AG]GAC-3'（DRACH）基序，集中于终止密码子附近和3'UTR[13→综述][24→综述]。其调控由三类酶执行：

- **Writers（写入器）**：核心复合物为METTL3（催化亚基）+ METTL14（结构/RNA结合平台）+ WTAP，另有VIRMA、RBM15/15B、HAKAI、ZC3H13等辅助亚基。METTL3的甲基转移酶结构域（MTD）结合S-腺苷甲硫氨酸（SAM）作为甲基供体，锌指结构域（ZFD）识别RNA GGACU共有序列；METTL3的甲基转移酶活性受SUMO化修饰抑制[24→综述]；
- **Erasers（擦除器）**：FTO和ALKBH5，均为非血红素Fe(II)/α-酮戊二酸（α-KG）依赖性双加氧酶——**这一生化特性直接构成线粒体代谢（TCA循环产生α-KG）与m6A修饰之间的连接点**；
- **Readers（阅读器）**：YTHDF1/2/3（胞质，调控翻译和降解）、YTHDC1/2（核内，调控剪接和出核）、IGF2BP家族、HNRNP家族等。功能分工为：YTHDF1主要促进翻译，YTHDF2促进mRNA降解，YTHDF3协调两者。

### 2.2 奠基性发现：m6A通过IL-7/STAT5/SOCS通路控制T细胞稳态

Li HB等人2017年发表于Nature的研究（PMID: 28792938）首次证明了m6A在T细胞中的体内生物学功能[13]：

- 在小鼠T细胞中删除m6A writer蛋白METTL3（或METTL14，表型一致）破坏T细胞稳态和分化；
- 在淋巴细胞减少性过继转移模型中，Mettl3缺陷的初始T细胞无法进行稳态扩增，维持初始状态长达12周，从而预防结肠炎；
- **机制：SOCS家族基因（SOCS1、SOCS3、CISH）的mRNA带有m6A标记，在Mettl3缺陷的初始T细胞中降解减慢、表达升高；增加的SOCS活性抑制IL-7介导的STAT5激活和T细胞稳态增殖与分化**；
- 因此，m6A的作用是"在IL-7刺激下诱导Socs mRNAs的快速降解"，使IL-7-JAKs信号能够激活下游STAT5，启动初始T细胞的增殖和分化重编程；
- 回补野生型METTL3（而非催化失活的METTL3）可拯救分化缺陷；siRNA敲低Socs1可部分拯救Mettl3缺陷T细胞的体内分化缺陷[13]。

这一研究确立了m6A作为**信号依赖性mRNA快速降解的进化保守机制**，为后续m6A在T细胞耗竭/记忆中的研究奠定了范式。

### 2.3 m6A与CD8+ T细胞分化与耗竭

**METTL3与效应/记忆分化**：METTL3对CD8+ T细胞的效应分化和记忆形成至关重要，Tbx21（T-bet）是METTL3的直接靶标；METTL3缺陷细胞在二次免疫应答中失败[24→综述]。

**METTL3是终末耗竭的中央调控因子（2026年最新发现）**：Ghosh等人2026年的研究（bioRxiv预印本，经多肿瘤模型验证）将METTL3确立为Tex命运的"中央调节因子"[15]：

- **表达模式**：在小鼠肿瘤模型（MC38、YUMM1.7）、人类多种恶性肿瘤（乳腺癌、结直肠癌、宫颈癌、黑色素瘤）的单细胞数据中，**METTL3表达选择性富集于终末耗竭T细胞（tTex），与TCF1+前体耗竭T细胞（pTex）呈负相关**；慢性TCR刺激上调METTL3，而IL-15/IL-7记忆诱导条件降低之；
- **功能**：METTL3敲低损害Tex分化（PD-1+Tim-3+、PD-1+CD39+频率降低）、增加TCF1和记忆标志物（TCF1、FOXO1、CCR7）、改善细胞因子产生（IFN-γ、TNF-α）、增强回忆应答；METTL3过表达则增强耗竭；
- **机制——Mettl3-m6A-Dnmt3b轴**：**METTL3通过m6A修饰稳定DNMT3B转录本，DNMT3B在记忆相关基因座执行CpG甲基化和染色质压缩**，从而确立"表观转录调控→表观遗传重塑"的直接因果链；
- **治疗意义**：抑制Mettl3-Dnmt3b轴可将染色质可及性重编程为记忆样状态，保留祖细胞潜能和效应功能，T细胞持久性更长、回忆应答更强，且对PD-1阻断的响应增强[15]。

**YTHDF2：m6A读者连接线粒体功能与T细胞多能性（Nature Communications 2024）**[16]：

- **表达模式**：YTHDF2在早期效应细胞和效应样CD8+ T细胞（包括Tpex及其转型中的耗竭后代）中选择性上调；在早期T细胞激活和PD-1阻断诱导的复活中高表达；
- **亚细胞定位新发现**：T细胞激活触发YTHDF2核转位，发挥促进新生RNA合成的核内功能；
- **线粒体功能调控（直接连接m6A与线粒体）**：**YTHDF2启动m6A依赖性线粒体相关基因（Coa3、Mrpl16、Mrps12、Tefm）的RNA降解，防止线粒体功能障碍、ROS积累和T细胞耗竭**；METTL3对该调控至关重要；
- **染色质调控**：核内YTHDF2与转录抑制因子IKZF1/3（Ikaros/Aiolos）相互作用，将其从靶基因上隔离，促进活性染色质状态和多能性基因表达（Stat5a、Rasgrp1）；
- **治疗意义**：临床可用的IKZF1/3抑制剂**来那度胺（lenalidomide）**在YTHDF2缺陷背景下与ICB联用可基本恢复免疫治疗疗效[16]。

**WTAP/PD-1轴**：在肝细胞癌中，WTAP对PDCD1 mRNA的m6A修饰通过YTHDF1增强PD-1翻译，抑制CD8+ T细胞功能[24→综述]。

**METTL14在肿瘤免疫中的髓系角色**：Dong等人2021年Cancer Cell研究证明，肿瘤相关巨噬细胞（C1q+ TAMs）中METTL14缺失导致Ebi3转录本m6A降低、EBI3表达增加，驱动CD8+ T细胞功能障碍；EBI3中和抗体可拯救功能障碍的CD8+ T细胞并克服免疫抑制[17]。

**m6A与耗竭的动态全景**：Ji等人2025年的泛癌分析整合了31个m6A调控因子与518-675个TEX相关基因，在单细胞水平发现28个m6A调控因子在细胞毒性T细胞与耗竭T细胞间差异表达；鉴定出三种泛癌亚型（TexHm6AH高m6A高耗竭-免疫沙漠型、TexLm6AL低m6A低耗竭-免疫活跃型、TexLm6AH低m6A高耗竭-间质/转移型），其中ELAVL1连接度最高[20]。

**m6A与耗竭/记忆转录因子的直接联系**：
- **TCF7**：METTL3稳定TCF7 mRNA以启动Tfh分化[24→综述]；Mettl3敲低增加TCF1[15]；TCF7 mRNA属于带有ARE-flanking m6A位点的"meta-unstable"mRNA[14]；
- **TOX**：m6A对TOX mRNA的直接调控证据仍有限，但METTL3表达与TOX正相关（终末耗竭）[15]。

### 2.4 m6A与记忆/初始性维持的关联

Gameiro等人2026年发表于Nature Communications的研究揭示了m6A在CD8+ T细胞激活早期决定记忆命运的关键机制[14]：

- 应用改进的miCLIP和抗体非依赖的GLORI方法绘制人CD8+ T细胞激活前后的m6A图谱；
- 发现一类新的功能性m6A位点亚类——**"ARE-flanking m6A位点"**（经典RRACH基序侧翼±4nt内存在AU富集元件ARE）；
- 携带此类位点的mRNA为**"meta-unstable"（元不稳定）mRNA**，在CD8+ T细胞激活后迅速降解；**这些mRNA编码晚期效应和记忆蛋白，包括ZFP36L1、ZFP36L2、CD28、CD69、BCL2、CXCR4、IL7R、TCF7、TNF**；
- METTL3抑制可增加这些靶mRNA（如IL7R、TNF）的稳定性——提示**METTL3介导的m6A降解是"清除"记忆潜能转录本、允许效应分化的开关**；
- 该机制对理解"慢性抗原刺激下m6A持续高表达→记忆基因转录本持续降解→终末耗竭"具有重要意义：在慢性刺激下，持续的METTL3活性可能不断降解TCF7、IL7R等记忆/干性转录本，推动细胞不可逆地走向终末耗竭。

### 2.5 线粒体代谢状态对m6A酶活性的调控

m6A修饰与线粒体代谢之间存在多个层面的生化耦联：

**（1）SAM（S-腺苷甲硫氨酸）——writer的甲基供体**：METTL3的甲基转移酶结构域以SAM为辅因子[24→综述]。SAM由甲硫氨酸经蛋氨酸腺苷转移酶合成，其再生依赖叶酸循环和甲硫氨酸循环，后者与线粒体一碳代谢密切相关。肠道菌群综述明确指出：微生物通过叶酸、甲硫氨酸和TCA循环调节SAM和α-KG的可用性，**维生素B12缺乏可降低整体m6A水平**；甲硫氨酸在早期TCR信号期间的可用性影响NFAT1激活和耗竭[24→综述]。

**（2）α-KG/Fe(II)——eraser的辅因子**：FTO和ALKBH5是"非血红素Fe(II)/α-KG依赖性双加氧酶"[24→综述]，α-KG直接来自线粒体TCA循环。因此，**线粒体TCA通量直接调控m6A擦除活性**——线粒体功能障碍导致α-KG水平变化，将直接影响FTO/ALKBH5的去甲基化能力。

**（3）肿瘤代谢物对FTO的抑制**：Su等人2018年发表于Cell的研究证明，突变IDH1/2产生的**致癌代谢物R-2-羟基戊二酸（R-2HG）通过竞争性抑制FTO活性**，增加全局m6A水平，降低MYC/CEBPA转录本稳定性，发挥抗白血病活性[18]。R-2HG在胶质瘤中可积累至30 mM，竞争性抑制α-KG依赖性酶（包括JmjC组蛋白去甲基化酶、TET DNA去甲基化酶和FTO/ALKBH RNA去甲基化酶）[18→相关]。

**（4）线粒体功能与m6A调控T细胞功能的汇聚**：YTHDF2通过m6A降解线粒体基因转录本（Coa3、Mrpl16、Mrps12、Tefm）防止线粒体功能障碍[16]；在NK细胞中，METTL3缺失导致IL-15刺激后最大呼吸和SRC降低[19]——说明m6A machinery是线粒体适应性的上游调节者，而线粒体代谢产物（SAM、α-KG）又反馈调节m6A酶活性，构成**双向调控回路**。

**直接证据缺口**：目前尚无原始论文直接证明T细胞线粒体内SAM循环/α-KG水平控制METTL3/FTO/ALKBH5活性，这是该交叉领域的关键未解决问题[24→综述]。

### 2.6 m6A与Trm的关联及未解决问题

**直接证据缺乏**：目前尚无原始研究论文直接证明m6A修饰调控CD8+ Trm细胞分化。间接证据包括：
- Mettl3敲低在记忆条件下促进干细胞样记忆（SCM）细胞形成（CD45RA+CD62L+），升高TCF1、FOXO1、CCR7，并在再挑战时增强回忆应答[15]；
- 携带ARE-flanking m6A位点的meta-unstable mRNA编码CD69等Trm相关分子[14]；
- 一般性综述指出m6A调节T细胞向效应、记忆和调节亚型分化[24→综述]。

**关键未解决问题**：
1. m6A writers/erasers/readers在Trm分化中的细胞固有作用；
2. 组织微环境（如皮肤、肠道、肺）的代谢状态（氧张力、乳酸）如何通过m6A影响Trm驻留程序的建立；
3. METTL3-DNMT3B轴是否在Trm命运决定中同样发挥作用（目前证据限于肿瘤Tex）；
4. m6A与乳酸化之间的直接交叉（Xiong等人2022年在髓系细胞中证明乳酸化驱动METTL3表达[22]，该机制是否在CD8+ T细胞中保守）[22]。

---

## 模块三：乳酸介导的组蛋白乳酸化与T细胞命运

### 3.1 乳酸化的发现与生化机制

**Zhang等人2019年发表于Nature的原始论文**首次报道了组蛋白赖氨酸乳酸化（histone lactylation, Kla）[21]：

- 在人类和小鼠细胞的核心组蛋白上鉴定出**28个乳酸化位点**；
- 缺氧和细菌刺激通过糖酵解诱导乳酸产生，乳酸作为前体直接刺激组蛋白乳酸化；
- 以细菌刺激的M1巨噬细胞为模型，**组蛋白乳酸化与乙酰化具有不同的时间动态**：M1极化晚期乳酸化增加，诱导参与伤口愈合的稳态基因（包括Arg1）——作者提出内源性"乳酸时钟"（lactate clock）概念；
- 外源乳酸可提升多种人细胞系的组蛋白Kla水平；LDHA/LDHB敲除降低Kla水平；
- **p300以p53依赖性方式催化组蛋白乳酸化**，并在体外从重组染色质直接刺激转录；
- 在LLC和B16肿瘤模型的肿瘤相关巨噬细胞中，组蛋白Kla水平与Arg1表达正相关[21]。

**乳酸化的生化路径**：乳酸与辅酶A缩合形成乳酰辅酶A（lac-CoA）→ writer酶（p300/CBP、HBO1、KAT8）将乳酰基转移到赖氨酸残基 → eraser酶（class I HDACs、SIRT1-3）移除。**reader蛋白尚未鉴定**。**核内lactyl-CoA浓度比acetyl-CoA低20-350倍**，p300/CBP对lactyl-CoA亲和力较低——这构成"动力学阈值"模型的基础[31]。

### 3.2 乳酸化与肿瘤微环境中的T细胞耗竭

乳酸化在肿瘤微环境中的免疫抑制功能已有大量原始文献支持。肿瘤组织乳酸浓度可达10-30 mM（肿瘤核心区高达50 mM），远高于正常血清的1.5-3 mM[30→综述]。关键机制包括：

**（1）乳酸化驱动METTL3/m6A/JAK1/STAT3轴（Xiong等，Molecular Cell 2022）**——代谢-表观遗传交叉的直接证据[22]：
- 肿瘤浸润髓系细胞（TIMs）中METTL3表达增加与结肠癌患者预后不良相关；
- **肿瘤微环境中积累的乳酸通过H3K18乳酸化诱导TIMs中METTL3上调**；
- METTL3介导Jak1 mRNA上的m6A修饰，m6A-YTHDF1轴增强JAK1蛋白翻译效率和随后的STAT3磷酸化；
- 在METTL3的锌指结构域中鉴定出两个乳酸化修饰位点，对METTL3捕获靶RNA至关重要；
- 该研究首次建立了"乳酸化→m6A修饰→免疫抑制"的跨层次因果链。

**（2）H3K18la驱动CD8+ T细胞排斥和anti-PD-1耐药（Zhu等，Cell Reports 2026）**[27]：
- 高肿瘤糖酵解驱动的H3K18la水平与HCC免疫治疗耐药、CD8+ T细胞浸润受限和不良预后相关；
- H3K18la增加TRPS1和ETV1启动子的染色质可及性，表观遗传上调其转录；
- TRPS1强化糖酵解和GLUT1介导的CD8+ T细胞旁观者杀伤抵抗，而ETV1驱动的CCL2创造限制CD8+ T细胞积累的免疫抑制生态位——共同驱动双重免疫治疗耐药；
- **GLUT1抑制剂BAY-876 + 抗CCL2抗体 + 抗PD-1抗体的三联组合疗法增强CD8+ T细胞抗肿瘤免疫**。

**（3）FOXK1-TOX乳酸化轴（Scientific Reports 2026）**——**目前最直接的"乳酸化-TOX-耗竭"证据**[28]：
- FOXK1调控糖脂代谢，其敲低降低乳酸、脂质、葡萄糖摄取，抑制卵巢癌细胞增殖；
- FOXK1敲低增加CD8+ T细胞增殖和免疫因子（IFN-γ、TNF-α、PRF1、GzmB），减少CD8+ T细胞凋亡；乳酸钠处理产生相反效应；
- **Co-IP证实TOX与泛乳酸化抗体（Pan lac）相互作用——TOX蛋白本身存在乳酸化修饰**；FOXK1敲低降低组蛋白泛乳酸化水平；
- 结论：FOXK1调控的糖脂代谢通过TOX乳酸化驱动高级别浆液性卵巢癌中CD8+ T细胞耗竭[28]。

**（4）免疫抑制网络视角**：Ye等人2026年提出"乳酸化-免疫抑制网络"框架[31]：组蛋白乳酸化通过长期表观遗传编程建立稳定的免疫抑制转录组，非组蛋白乳酸化则快速动态调节蛋白活性。在T细胞中呈现"平行增强"模式——CD8+ T细胞被抑制（组蛋白乳酸化上调ANGPTL4和circATXN7，诱导功能障碍和AICD敏感性），而Tregs被增强（H3K18la上调CCR8、CD39/CD73、TNFR2；MOESIN和APOC2非组蛋白乳酸化支持其功能）。免疫检查点方面：组蛋白乳酸化（H3K18la、H3K14la）促进PD-L1、B7-H3和CD47转录；非组蛋白PD-L1乳酸化（K270）阻断降解、增加稳定性和表面表达。

**（5）葡萄糖驱动的乳酸化与胶质母细胞瘤免疫抑制（De Leo等，Immunity 2024）**[26]：
- 单核细胞来源巨噬细胞（MDMs）在GBM中高度糖酵解，GLUT1+ MDMs是关键免疫抑制群体；
- **胞内葡萄糖来源的乳酸（而非胞外乳酸）是Kla的主要来源**；葡萄糖代谢驱动组蛋白乳酸化，p300介导该表观遗传修饰在启动子水平调控IL-10表达；
- 髓系细胞中删除GLUT1损害其抑制能力并延长生存；靶向PERK增强4-1BB激动剂免疫治疗疗效[26]。

### 3.3 乳酸化与CD8+ T细胞自身代谢：H3K9la与H3K18la的分工

**Raychaudhuri等人2024年发表于Nature Immunology的研究**首次系统刻画了乳酸化在CD8+ T细胞自身功能中的作用[23]：

- **H3K9la在naïve、活化及记忆CD8+ T细胞中发挥关键作用，而H3K18la特异性地在活化CD8+ T细胞中作为主要调节因子**；
- **H3K9la富集于naive/memory相关基因（Tcf7、Ccr7、Batf3）**；H3K9la支持naive和记忆细胞中持续的线粒体代谢（OXPHOS）；
- **H3K18la与线粒体裂变（fission）相关，H3K9la与线粒体融合（fusion）相关**——这直接连接乳酸化与线粒体动力学；
- H3K9la由糖酵解和线粒体代谢通路共同驱动，而H3K18la选择性来源于糖酵解——形成前馈循环；
- **药理学意义**：抑制HDAC1-3（组蛋白去乳酸化酶）配合MS275可增加乳酸化、效应基因表达和抗原特异性杀伤；在小鼠肿瘤模型中，MS275治疗增加肿瘤来源CD8+ T细胞中的乳酸化、增加瘤内granzyme B+效应细胞并减少肿瘤生长；反之，抑制乳酸产生（LDHA抑制剂）或CBP/EP300减少乳酸化和T细胞杀伤能力[23]。

这一发现具有重大意义：**乳酸化并非笼统地促进耗竭，而是以位点特异性的方式区分了记忆/静息程序（H3K9la）与激活/效应程序（H3K18la）**，为理解"乳酸悖论"（低乳酸促进免疫 vs 高乳酸抑制免疫）提供了表观遗传解释。

### 3.4 乳酸化与乙酰化的竞争及HDAC的双重角色

**HDAC1-3作为去乳酸化酶（2022）**：Moreno-Yruela等人证明class I HDAC1-3是体外最高效的赖氨酸去乳酸化酶，且HDAC1和HDAC3具有位点特异性去乳酸化酶活性[30→对应]。这一发现意味着**HDAC抑制剂同时影响乙酰化和乳酸化**，既往许多归因于"抑制去乙酰化"的免疫效应可能部分通过"抑制去乳酸化"介导。

**HDAC1-3作为乳酸化催化剂（2025年颠覆性发现）**：Gonzatti等人2025年发表于JBC的研究证明，**class I HDAC1/2/3可通过逆转其典型去乙酰化反应催化赖氨酸乳酸化（Kla）形成**[33]：

- HDAC催化的赖氨酸乳酸化占细胞中Kla形成的**大部分**；
- 重组HDAC1/2/3在体外直接催化赖氨酸乳酸化，该活性被HDAC抑制剂曲古抑菌素A（TSA）抑制；
- HDAC2活性位点突变体（H141A、H179A、Y304F）降低乳酸化活性；
- **HDAC抑制剂（丁酸、TSA、SAHA、MS-275）降低基础Kla水平，同时增加乙酰化，但不影响胞内乳酸浓度**；
- 直接定量胞内lactyl-CoA发现**Kla丰度可与lactyl-CoA水平解偶联**——支持"HDACs通过乳酸直接缩合反应催化乳酸化，而非需要lactyl-CoA中间体"的模型[33]。

**ENO1-HDAC1耦合（PNAS 2026）**：Zhai等人2026年证明糖酵解酶烯醇化酶-1（ENO1）易位至细胞核并与染色质上的HDAC1相互作用，通过局部产生的磷酸烯醇式丙酮酸（PEP）抑制HDAC1活性，**促进组蛋白赖氨酸乳酸化并驱动肝脏恶性肿瘤的致癌转录重编程**[35]。这构成了"糖酵解酶局部调控表观遗传酶"的直接机制。

**乙酰化与乳酸化的竞争-协同关系**：正常条件下核内lactyl-CoA稀缺（比acetyl-CoA低20-350倍）限制乳酸化，允许乙酰化占主导；但在高乳酸TME中，过量乳酸可能使核内lactyl-CoA超过阈值，乳酸化占主导[31]。组蛋白乙酰化在数小时内快速达峰，而乳酸化在24小时内逐渐积累[31→相关]——乳酸化作为**持续代谢应激的整合子**，在慢性抗原刺激（持续数周至数月）的时间尺度上具有独特的病理意义。

### 3.5 线粒体功能障碍→糖酵解→乳酸化：自强化恶性循环

将模块一与模块三整合，可以构建一个完整的病理循环：

```
慢性抗原刺激 → PD-1信号 → PGC-1α↓（线粒体生物发生↓）
    → 线粒体呼吸受损（Slc25a3/ETC功能↓）
    → NADPH↓ → 线粒体ROS↑ → HIF-1α稳定化
    → 糖酵解重编程（HK2、PKM2、LDHA↑）
    → 乳酸产生↑（有氧糖酵解终产物）
    → 组蛋白乳酸化↑（H3K18la/H3K9la等）
    → 耗竭基因（PDCD1、HAVCR2、LAG3、TOX）表观遗传激活 / 效应基因（IFNG、GZMB、PRF1）抑制
    → 线粒体功能进一步恶化（如H3K18la下调线粒体融合相关基因）
    → 恶性循环
```

该循环的每一环节都有原始文献支撑：线粒体功能障碍→HIF-1α→糖酵解（Wu 2023 [4]）；糖酵解→乳酸→乳酸化（Zhang 2019 [21]）；乳酸化→耗竭基因/代谢基因重编程（Zhu 2026 [27]；FOXK1-TOX [28]）；乳酸化与线粒体动力学关联（H3K18la-裂变/H3K9la-融合，Raychaudhuri 2024 [23]）；乳酸化→METTL3→m6A→免疫抑制（Xiong 2022 [22]）。

Ma & Yu 2025年的综述将此概括为"**代谢-线粒体-表观遗传**"回路：线粒体功能障碍驱动细胞转向糖酵解→乳酸积累→乳酸化加剧线粒体损伤（通过PDHA1、CPT2、MDH2等关键酶和组蛋白的乳酸化）[36→对应]。

### 3.6 乳酸化与Trm的关联及未解决问题

**直接证据极为有限**。目前仅有的间接线索：
- 银屑病复发模型中，"透邪祛银方"通过调节组蛋白乳酸化介导的Fabp45和组织驻留记忆T细胞改善银屑病复发[37→对应]，但该研究为中药复方研究，机制细节有限；
- H3K9la富集于naive/memory相关基因（Tcf7、Ccr7、Batf3）并支持naive和记忆细胞中的OXPHOS[23]——提示**低水平的H3K9la可能支持Trm样程序**，而高乳酸环境下的H3K18la优势可能抑制Trm形成；
- 慢性抗原刺激驱动CD8+组织驻留耗竭T细胞（Tres）的产生，其发育起源和功能与Trm不同，但两者的命运分岔是否受乳酸化调控尚无直接证据。

**模块三未解决问题**：
1. 细胞中产生乳酰辅酶A的酶及细胞中lactyl-CoA的浓度仍未知（2019年原始论文遗留问题）[21]；
2. 乳酸化的reader蛋白尚未鉴定[30→综述]；
3. p300/CBP和HDACs/sirtuins同时控制乙酰化和乳酸化，难以将效应特异性归因于乳酸化（特异性困境）[31]；
4. 乳酸化的双向作用（免疫抑制 vs 免疫刺激）取决于环境、浓度和T细胞代谢状态的机制尚需阐明[30→综述]；
5. Lactyl-CoA非依赖的HDAC催化乳酸化模型（2025 [33]）与p300/lactyl-CoA模型的关系需要进一步整合；
6. **乳酸化与Trm命运决定的直接机制完全缺乏原始文献**。

---

## 模块四：代谢-表观遗传互作网络驱动"耗竭"与"Trm"命运分岔

### 4.1 转录因子枢纽：TOX、TCF-1、EOMES、PRDM1/Blimp-1、Hobit

**TOX——耗竭的主调控因子**。2019年五篇背靠背论文（Khan等Nature、Seo等PNAS、Scott等Nature、Alfei等Nature、Yao等Nature Immunology）确立了TOX作为耗竭主调控因子的地位[32]：
- TOX在持续抗原呈递条件下特异性发挥作用（急性感染中非必需）；
- TOX通过染色质重塑和RNA转录组改变驱动耗竭CD8+ T细胞形成；诱导高表达抑制性受体、降低炎症细胞因子产生；
- TOX表达由钙调磷酸酶/NFAT通路诱导（初始经钙调磷酸酶-NFAT2，持续阶段独立于钙调磷酸酶）；
- Khan等发现TOX是耗竭T细胞中差异表达最显著的基因，通过染色质重塑抑制KLRG1+效应分化并调控PD-1、TIGIT、LAG3、Eomes、TCF1；
- Alfei等证明TOX诱导依赖于抗原量而非亲和力；TOX对TCF1+祖细胞T细胞的长期维持必需；
- Yao等（单细胞RNA测序，慢性LCMV）显示祖细胞样细胞共表达Tox和Tcf7；Tox敲除使分化转向KLRG1+短寿命效应细胞。

**TCF-1（Tcf7）——干性/祖细胞维持因子**。TCF-1维持对PD-1阻断敏感的祖细胞样耗竭T细胞（Tpex）亚群[30→综述]。m6A层面，METTL3稳定TCF7 mRNA[24→综述]，而慢性刺激下METTL3高表达通过DNMT3B轴关闭记忆位点（包括TCF7位点）[15]；TCF7 mRNA属于激活后迅速降解的meta-unstable mRNA[14]。

**STAT5对抗TOX（Beltra等，Immunity 2023）**[33]：组成型激活Stat5a在慢性LCMV中驱动更多CD8+ T细胞向效应样分化而非Tex前体，降低每个细胞的Tox表达；Tox基因座本身含有大量Stat5直接结合位点；STAT5操纵不仅触发对耗竭的持久抵抗，还能部分拯救已完全进入耗竭谱系的细胞——但"耗竭的表观遗传疤痕仍然存在"。

**EOMES——终末耗竭标志**：PD-1^Hi Eomes^Hi终末分化亚群对抗PD-L1阻断的代谢重编程不敏感（Bengsch 2016 [2]）。TOX调控Eomes表达[32]。

**PRDM1/Blimp-1——代谢-表观遗传连接的关键节点**：
- **Blimp-1（由Prdm1编码）抑制PGC-1α表达**，导致线粒体生物发生下降和ROS积累——这是PD-1信号下游驱动代谢障碍的核心机制之一[9]；
- 缺氧促进Blimp-1表达，抑制PGC-1α介导的线粒体重编程[10]；
- 敲低Blimp-1或过表达PGC-1α可逆转代谢失调[35→对应]。

**Hobit（Zfp683）与PRDM1——Trm程序的核心转录因子**：Hobit和Blimp-1共同驱动组织驻留记忆T细胞程序。目前尚无直接证据表明线粒体动力学或m6A/乳酸化直接调控Hobit，但Hobit/ZFP683驱动的Trm程序（CD69+CD103+）与Tpex/Tex程序之间的拮抗关系（TCF-1 vs TOX）提示：**任何推动TOX/耗竭程序的力量（慢性TCR、线粒体功能障碍、乳酸化）都可能间接抑制Trm程序**。

### 4.2 命运分岔的整合机制模型

综合现有证据，可以构建慢性抗原刺激下CD8+ T细胞命运分岔的整合模型：

**（1）信号层面**：慢性TCR刺激 → 钙调磷酸酶-NFAT2通路上调TOX；同时PI3K-AKT通路持续磷酸化并抑制FOXO1，导致E3泛素连接酶KLHL6持续下调——KLHL6泛素化并靶向TOX和PGAM5降解，其下调使TOX积累（加速耗竭）和PGAM5积累（通过Drp1促进过度线粒体碎片化和代谢功能障碍）[34]。

**（2）代谢层面**：PD-1双重抑制（PGC-1α↓ + Drp1 Ser616磷酸化↓）→ 线粒体呼吸不足 + 裂变受阻 → NADPH↓/ROS↑ → HIF-1α稳定 → 糖酵解重编程 → 乳酸↑。

**（3）表观遗传层面**：乳酸↑ → 组蛋白乳酸化（H3K18la为主）→ 染色质可及性重塑（耗竭基因座开放、效应/记忆基因座关闭）+ METTL3上调 → m6A介导的DNMT3B稳定 → DNA甲基化锁定记忆位点 → 表观遗传"锁定"。

**（4）命运分岔点**：Tpex（TCF-1+CXCR5+PD-1^Int）是分岔关键节点：
- 若线粒体功能维持（高OXPHOS、低ROS、正常线粒体自噬）→ TCF-1维持 → 可响应PD-1阻断 → 向Trm或记忆方向分化（需要Hobit/Blimp-1程序、组织驻留信号如TGF-β/CD103）；
- 若线粒体功能障碍（呼吸↓、ROS↑、自噬↓）→ HIF-1α→糖酵解→乳酸→乳酸化→METTL3→DNMT3B → TOX持续高表达 → 不可逆终末耗竭。

### 4.3 机制图解

```
慢性抗原刺激（肿瘤/HIV）
    │
    ├──► 慢性TCR信号 ──► NFAT2 ──► TOX↑ ──────────────┐
    │        │                                           │
    │        └──► PI3K-AKT ──► FOXO1↓ ──► KLHL6↓ ──► TOX↑（降解↓）
    │                                                   │
    ├──► PD-1信号 ──► PGC-1α↓（生物发生↓）               │
    │      │        ► Drp1-Ser616-P↓（裂变受阻）          │
    │      ▼                                            ▼
    │  线粒体呼吸不足 ◄── 线粒体自噬↓（去极化线粒体积累） 耗竭程序
    │      │                                    ↑        │
    │      ▼                                    │        │
    │  NADPH↓ → mtROS↑ → HIF-1α稳定 ──► 糖酵解重编程     │
    │                                    │               │
    │                                    ▼               │
    │                              乳酸产生↑             │
    │                                    │               │
    │                                    ▼               │
    │                          组蛋白乳酸化（H3K18la）    │
    │                                    │               │
    │                          ┌─────────┴─────────┐     │
    │                          ▼                   ▼     │
    │                   耗竭基因开放           METTL3↑    │
    │                   （PDCD1/TOX/           │          │
    │                    HAVCR2/LAG3）         ▼          │
    │                                       m6A↑         │
    │                                       │            │
    │                                       ▼            │
    │                                 DNMT3B稳定 ──► DNA甲基化锁定
    │                                                │
    └────────────────────────────────────────────────┘
                    表观遗传锁定 → 不可逆终末耗竭

    命运分岔点：Tpex（TCF-1+CXCR5+）
        ├── 线粒体功能维持 → TCF-1+ → PD-1阻断响应 → 记忆/Trm命运
        └── 线粒体功能障碍 → 上述恶性循环 → 终末耗竭
```

### 4.4 模块四未解决问题

1. Tpex→Tex与Tpex→Trm分岔是否受同一代谢开关控制，还是存在独立的代谢检查点；
2. Klhl6-FOXO1轴在Trm命运决定中的角色完全未知[34]；
3. 乳酸化位点特异性（H3K9la vs H3K18la）如何在不同T细胞亚群中被差异化写入；
4. pTex向Texint/Texterm转变过程中线粒体动力学与表观遗传变化的先后时序（哪个是"第一推动力"）[4]；
5. 组织微环境信号（TGF-β、组织氧张力）如何与代谢-表观遗传轴交互决定Trm vs Tres（组织驻留耗竭T细胞）命运[37→对应]。

---

## 模块五：定量建模分析——代谢-表观遗传互作网络的预测性计算模型

### 5.1 已有模型框架与数据基础

目前该领域尚无统一发表的"线粒体动力学-表观遗传-命运分岔"整合定量模型，但已有若干可用的计算框架与数据基础：

**（1）基于单细胞多组学的m6A-TEX计算模型**：Ji等人2025年整合31个m6A调控因子和518-675个TEX相关基因，结合530个细胞系样本、8种癌症类型的scRNA-seq、29种肿瘤类型的9,487例泛癌样本和两个免疫治疗队列，鉴定出三种m6A-TEX亚型并可预测免疫治疗响应（Gide队列C3亚型79.4%响应 vs C1 35.7%）；9个m6A调控因子被发现在Tpex（PD-1+TCF7+）与终末TEX（PD-1+TCF7-）之间调节动态[20]。

**（2）单细胞分化轨迹推断**：Wu等人2023年的scRNA-seq数据揭示了Tpex→Tex的连续分化轨迹及其代谢转换（OXPHOS→糖酵解），为构建基于代谢状态的命运决策模型提供了定量数据基础[4]；Ghosh等人2026年对9,056个小鼠CD8+ T细胞和4,588个人类肿瘤浸润CD8+ T细胞的分析为METTL3作为Tex命运调节因子的定量关系提供了参数来源[15]。

**（3）表观遗传锁定计算概念**：耗竭T细胞的"表观遗传疤痕"（约6,000个独特开放染色质区域不被αPD-L1重编程；PD-1启动子在病毒载量下降后仍保持去甲基化）提示命运决策模型需要包含**不可逆状态变量**（如DNA甲基化状态），而非仅依赖可逆的基因表达变量[30→综述]。

### 5.2 建模策略建议

**策略一：常微分方程（ODE）模型——核心基因调控网络的动力学**

建议构建以关键转录因子和代谢物为状态变量的ODE模型：

```
变量：T（TOX）、F（TCF-1）、M（METTL3）、L（乳酸/乳酸化水平）、
      R（线粒体呼吸功能）、H（HIF-1α）、D（DNMT3B/DNA甲基化锁定程度）
```

核心方程骨架（Hill动力学形式）：

- dT/dt = a_T·NFAT(TCR) / (K_T + ...) − b_T·KLHL6·T （TOX受NFAT诱导、KLHL6降解）
- dF/dt = a_F − b_F·M·F − c_F·T·F （TCF-1受METTL3-m6A降解、TOX抑制）
- dM/dt = a_M·L / (K_M + L) − b_M·M （METTL3受乳酸化诱导——Xiong 2022机制）
- dR/dt = a_R·PGC1α(PD-1) − b_R·ROS·R （线粒体功能受PD-1抑制、ROS损伤）
- dL/dt = a_L·H·G − b_L·L （乳酸产生受HIF-1α-糖酵解驱动）
- dD/dt = a_D·M − b_D·D （DNA甲基化锁定受METTL3-DNMT3B轴驱动，慢时间尺度）

**参数选择建议**：
- 时间尺度分离：基因表达（小时）、代谢物（分钟-小时）、DNA甲基化锁定（天-周）——使用慢-快动力学系统；
- 退化率参数可参考已有mRNA半衰期数据（如meta-unstable mRNA中位数半衰期2.2-3.6小时[14]）；
- TOX/TCF-1互作参数可参考Beltra等人STAT5实验的定量表型[33]；
- 使用IC50/EC50数据校准乳酸对METTL3诱导的剂量-响应关系（肿瘤乳酸10-30 mM阈值[30→综述]）；
- 不可逆性参数：DNMT3B介导的甲基化锁定可用双稳态势阱建模（耗竭与记忆两个吸引子）。

**策略二：布尔网络模型——命运分岔的离散逻辑**

基于模块四的整合机制图，构建布尔网络（节点约15-20个）：

```
节点：TCR、NFAT、TOX、TCF1、PD1、PGC1A、HIF1A、GLUT1、LDHA、
      LACTATE、KLA、METTL3、DNMT3B、KLHL6、FOXO1、EOMES、HOBIT
规则示例：
  TOX* = NFAT AND NOT KLHL6
  TCF1* = NOT TOX AND NOT METTL3  （受m6A降解）
  KLHL6* = FOXO1 AND NOT TCR_Chronic
  KLA* = LACTATE（阈值以上）
  METTL3* = KLA
  DNMT3B* = METTL3
  HOBIT* = NOT TOX AND TCF1 AND Tissue_Signal（代表Trm命运）
  EOMES_terminal* = TOX AND NOT TCF1
```

布尔网络可系统搜索吸引子（耗竭吸引子、记忆吸引子、Trm吸引子），并模拟扰动（如PD-1阻断=持续关闭PD1节点；METTL3抑制=关闭METTL3节点）观察状态转移。

**策略三：基于单细胞多组学的机器学习方法**

- **轨迹推断与RNA速度**：应用scRNA-seq/snATAC-seq数据（如Wu 2023的LCMV数据集[4]、Ghosh 2026的肿瘤数据集[15]）推断Tpex→Tex的连续轨迹，以线粒体基因模块评分（如OXPHOS/糖酵解基因集）和表观遗传模块评分（如m6A靶基因、乳酸化靶基因）作为流形坐标；
- **多组学整合**：将m6A位点（miCLIP/GLORI数据[14]）、乳酸化ChIP-seq（H3K18la/H3K9la）、ATAC-seq和DNA甲基化数据整合为每细胞的"表观遗传状态向量"；
- **细胞命运预测**：使用CellRank等框架，以线粒体状态（膜电位、ROS水平、形态学参数——可通过Met-Flow成像流式获得）和表观遗传状态为初始条件，预测单细胞向Tex/Trm分岔的概率；
- **因果推断**：利用遗传扰动数据（Slc25a3-cKO [4]、Mettl3-cKO [15]、Ythdf2-cKO [16]、Drp1-cKO [6]）构建扰动-响应矩阵，应用因果推理算法（如Perturb-CITE-seq分析框架）识别命运决定的关键驱动节点。

### 5.3 验证策略

1. **时序验证**：在慢性LCMV（Clone 13）和肿瘤模型中，在多个时间点（第3、7、14、30天）同时测量线粒体功能（Seahorse、TMRE、MitoSOX）、表观遗传修饰（H3K18la ChIP-seq、m6A miCLIP、ATAC-seq、甲基化测序）和表型（Tpex/Tex/Trm标志物），验证模型预测的时序关系；
2. **扰动验证**：对模型预测的关键节点进行遗传（Slc25a3、Mettl3、Ythdf2、Drp1、Klhl6条件敲除）和药理（2-DG [4]、MS-275 [23]、NR [3]、STM2457类METTL3抑制剂）扰动，比较模型预测与实验表型；
3. **参数可识别性**：使用profile likelihood或MCMC方法评估关键参数的可识别性，优先设计实验测量敏感参数（如乳酸化阈值、METTL3降解速率）；
4. **跨系统验证**：在肿瘤模型（MC38、B16）、慢性感染模型（LCMV Clone 13）和HIV体外模型之间交叉验证模型预测；
5. **预测-实验闭环**：模型预测"在某时间点干预某节点可将X%的细胞从耗竭吸引子转移到记忆吸引子"，然后设计实验检验该定量预测。

---

## 模块六：最新研究进展（截至2026年）与治疗干预靶点

### 6.1 2025-2026年关键新发现

**（1）KLHL6-FOXO1轴：T细胞耗竭的上游主开关（2026年1月）** [34]：两项互补研究（Nature + Immunity & Inflammation）证明：持续TCR信号作为主开关抑制转录因子FOXO1，导致E3泛素连接酶KLHL6持续下调——这是启动耗竭程序的先前未被认识的关键事件。**KLHL6泛素化并靶向两种蛋白降解：TOX（耗竭主转录因子）和PGAM5（线粒体动力学调节因子）**。慢性刺激下KLHL6减少使TOX积累（加速耗竭）和PGAM5积累（通过Drp1促进过度线粒体碎片化和代谢功能障碍）。KLHL6过表达可拯救FOXO1缺陷T细胞的抗肿瘤功能和记忆潜能——**KLHL6是FOXO1有益效应的主要下游执行者，首次将转录因子、泛素化、线粒体动力学和耗竭整合为单一通路**。

**（2）HDAC1-3作为乳酸化催化酶（2025年JBC）** [33]：颠覆了"p300/lactyl-CoA是乳酸化唯一途径"的认知，证明class I HDACs通过乳酸直接缩合反应催化大部分Kla形成，且该活性与去乙酰化共用活性位点——这一发现对HDAC抑制剂（已广泛用于肿瘤治疗）的免疫效应解释有重大影响。

**（3）ENO1-HDAC1耦合调节组蛋白乳酸化（2026年PNAS）** [35]：糖酵解酶ENO1核转位与HDAC1互作，通过局部PEP抑制HDAC1活性促进Kla——"糖酵解酶-表观遗传酶"的直接空间耦合机制。

**（4）Mettl3-Dnmt3b轴决定Tex命运（2026年）** [15]：METTL3通过m6A稳定DNMT3B转录本，以DNA甲基化锁定记忆位点，确立终末耗竭的表观遗传不可逆性。

**（5）H3K18la驱动肝癌anti-PD-1耐药（2026年Cell Reports）** [27]：TRPS1/ETV1双机制驱动CD8+ T细胞排斥，三联疗法（BAY-876 + anti-CCL2 + anti-PD-1）可克服耐药。

**（6）YTHDF2核转位与IKZF1/3隔离（2024年Nature Communications）** [16]：m6A读者在核内的非经典功能，以及来那度胺恢复免疫治疗效力的转化潜力。

**（7）OPA1对效应CD8+ T细胞扩增的必需性（2025年Cell Reports）** [8]：OPA1非融合功能（氨基酸代谢）的发现。

### 6.2 潜在治疗干预靶点

| 靶点/策略 | 干预方式 | 阶段 | 关键文献 |
|-----------|---------|------|---------|
| 线粒体呼吸增强 | Slc25a3过表达、NR补充、PGC-1α过表达/激动剂（bezafibrate） | 临床前 | [3][4][12] |
| 糖酵解限制 | 2-DG | 临床前/机制验证 | [4] |
| 线粒体自噬增强 | NR（烟酰胺核苷） | 临床前 | [3] |
| 线粒体ROS清除 | MitoQ、MitoTEMPO、NAC | 临床前 | [9][10] |
| Drp1活性调节 | 注意Mdivi-1特异性问题；开发Drp1-Ser616磷酸化通路的ERK/mTOR调节 | 临床前 | [6][7][11] |
| MFN2增强 | MFN2过表达/内质网-线粒体接触增强 | 临床前 | [5] |
| KLHL6/FOXO1 | KLHL6激动剂、靶向TOX/PGAM5的蛋白降解剂 | 概念验证 | [34] |
| METTL3抑制 | STM2457、STC-15（已在AML进入I期临床，NCT05584111） | 临床前/早期临床 | [24→综述] |
| YTHDF2下游 | 来那度胺（IKZF1/3抑制剂）联合ICB | 临床前 | [16] |
| HDAC1-3抑制 | MS-275（增强乳酸化+乙酰化，增加效应功能） | 临床前 | [23][30→对应] |
| 乳酸化写入/擦除 | p300/CBP抑制剂（需权衡）；LDHA抑制剂（oxamate、FX-11）；MCT1/4抑制剂（AZD3965已进入I期） | 临床前/早期临床 | [30→综述][31] |
| 乳酸化-糖酵解正反馈 | GLUT1抑制剂BAY-876 + anti-CCL2 + anti-PD-1三联 | 临床前 | [27] |
| 检查点阻断代谢增效 | 抗PD-1联合PGC-1α强制表达（加性获益趋势） | 临床前 | [12] |

### 6.3 关键未解决问题清单（前沿问题）

**线粒体动力学层面**：
1. 线粒体融合/裂变如何精确调控表观遗传酶（如p300、HDAC、DNMT3B）的核内可及性？是否存在线粒体-核信号（如线粒体代谢物、mitokine）直接调控表观遗传酶活性的机制？
2. Drp1/OPA1/MFN2在不同T细胞亚群（Tpex/Tex/Trm）中的动态表达图谱尚不完整；
3. 线粒体DNA损伤在慢性抗原刺激下的积累及其通过cGAS-STING或表观遗传途径对T细胞命运的影响。

**m6A层面**：
4. T细胞线粒体代谢状态（SAM循环、α-KG水平）对METTL3/FTO/ALKBH5活性的直接调控缺乏T细胞原始数据；
5. m6A在Trm分化中的直接作用完全没有原始文献；
6. m6A修饰在HIV潜伏感染CD8+ T细胞中的全局图谱缺失。

**乳酸化层面**：
7. 乳酸化reader蛋白的鉴定；
8. lactyl-CoA非依赖的HDAC催化乳酸化模型（2025）与p300/lactyl-CoA模型的整合；
9. 位点特异性乳酸化（H3K9la vs H3K18la vs H3K27la）如何被差异化调控并执行不同功能；
10. 乳酸化在Trm命运决定中的直接机制证据缺失。

**命运分岔与建模层面**：
11. "代谢-表观遗传锁定"的时间窗口：在哪个时间点之前干预可逆，之后不可逆？
12. 现有模型均为定性/半定量，缺乏符合数据共享标准的、可复用的整合定量模型；
13. 肿瘤微环境中的空间异质性（乳酸浓度梯度、氧梯度）如何影响单细胞水平的命运分岔——需要空间转录组+模型结合。

---

## 综合研究展望

基于上述分析，该领域未来5年的优先研究方向可归纳为：

**第一，建立"线粒体动力学→表观遗传重塑→命运分岔"的因果时序图谱。** 现有证据已分别建立了线粒体功能障碍→耗竭（[1][2][3][4]）、乳酸化→METTL3→免疫抑制（[22]）、乳酸化→耗竭基因（[27][28]）、m6A→DNMT3B→表观遗传锁定（[15]）等因果链，但缺乏在同一实验系统中、跨时间尺度的整合因果分析。建议在慢性LCMV和肿瘤模型中开展多时间点、多组学（线粒体功能组学+miCLIP+乳酸化ChIP-seq+ATAC-seq+甲基化测序+scRNA-seq）纵向研究。

**第二，解析Trm命运的表观代谢决定机制。** 现有文献对"耗竭"路径的代谢-表观遗传机制已较丰富，但对"Trm"路径的同等问题（线粒体动力学如何支持Trm驻留程序？m6A/乳酸化是否调控CD69/CD103/ITGAE/Hobit表达？）几乎空白——Trm与Tres（组织驻留耗竭T细胞）的分岔机制是未来最富饶的研究方向。

**第三，发展整合定量模型。** 建议以模块五提出的ODE+布尔网络+机器学习三级框架为基础，结合即将产生的大规模纵向多组学数据，建立可预测的T细胞命运决策模型，并用于指导CAR-T/TCR-T的代谢-表观遗传工程改造。

**第四，推动治疗转化。** 最有希望的近期转化方向包括：①METTL3抑制剂（STC-15类）在实体瘤T细胞耗竭中的应用；②HDAC抑制剂（MS-275类）通过乳酸化增强CD8+ T细胞效应功能的重新评价（考虑到HDAC1-3的乳酸化催化新发现[33]）；③NR/MitoQ等线粒体靶向营养干预与ICB的联合；④KLHL6激动剂/TOX-PGAM5降解剂（[34]）；⑤以"乳酸-乳酸化-糖酵解"正反馈回路为靶点的组合疗法（BAY-876+anti-CCL2+anti-PD-1，[27]）。

**第五，HIV潜伏感染背景的特化研究。** HIV-1 Vpr下调MFN2[39]的发现提示HIV对CD8+ T细胞线粒体动力学的直接操纵，但该机制在HIV特异性CD8+ T细胞耗竭和潜伏库维持中的角色尚未被研究。建议开展HIV感染者CD8+ T细胞的线粒体动力学-m6A-乳酸化整合分析。

---

### Sources

[1] Buck MD et al. Mitochondrial dynamics controls T cell fate through metabolic programming. Cell 2016;166(1):63-76. PMID: 27293185: https://pubmed.ncbi.nlm.nih.gov/27293185

[2] Bengsch B et al. Bioenergetic insufficiencies due to metabolic alterations regulated by the inhibitory receptor PD-1 are an early driver of CD8+ T cell exhaustion. Immunity 2016;45(2):358-373. PMID: 27496729: https://pmc.ncbi.nlm.nih.gov/articles/PMC4988919

[3] Yu YR et al. Disturbed mitochondrial dynamics in CD8+ TILs reinforce T cell exhaustion. Nature Immunology 2020;21(12):1540-1551. PMID: 33020660: https://pubmed.ncbi.nlm.nih.gov/33020660

[4] Wu H et al. Mitochondrial dysfunction promotes the transition of precursor to terminally exhausted T cells through HIF-1α-mediated glycolytic reprogramming. Nature Communications 2023;14:6858: https://www.nature.com/articles/s41467-023-42634-3

[5] Yang JF et al. Mitochondria-ER contact mediated by MFN2-SERCA2 interaction supports CD8+ T cell metabolic fitness and function in tumors. Science Immunology 2023;8(87):eabq2424: https://www.science.org/doi/10.1126/sciimmunol.abq2424

[6] Simula L et al. PD-1-induced T cell exhaustion is controlled by a Drp1-dependent mechanism. Molecular Oncology 2022;16(1):188-205: https://iris.unipa.it/retrieve/handle/10447/532047/1275532/SIMULA%20ET%20AL%20PD-1-INDICED%20T%20CELL%20EXHAUUSTION%20IS%20CONTROLLED%20BY%20A%20DRP-1-DEPENDENT%20MECHANISM.pdf

[7] Stevens MG et al. The mitochondrial fission protein DRP1 influences memory CD8+ T cell formation and function. J Leukoc Biol 2024;115(4):679. PMID: 38057151: https://pmc.ncbi.nlm.nih.gov/articles/PMC10980353

[8] Willett B et al. Mitochondrial protein OPA1 is required for the expansion of effector CD8 T cells. Cell Reports 2025: https://www.semanticscholar.org/paper/Mitochondrial-protein-OPA1-is-required-for-the-of-T-Willett-Thompson/1760abf2cb9cea63a0a7f02e96b33dd755f44937

[9] Li Y et al. Mitochondrial Metabolism in T-Cell Exhaustion. Int J Mol Sci 2025;26(15):7400: https://www.mdpi.com/1422-0067/26/15/7400

[10] Yang S et al. Targeting mitochondria: restoring antitumor efficacy of exhausted T cells. Molecular Cancer 2024;23:260: https://link.springer.com/article/10.1186/s12943-024-02175-9

[11] Ma J et al. Impact of Drp1-Mediated Mitochondrial Dynamics on T Cell Immune Modulation. Frontiers in Immunology 2022;13:873834: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2022.873834/full

[12] Dumauthioz N et al. Enforced PGC-1α expression promotes CD8 T cell fitness, memory formation and antitumor immunity. Cellular & Molecular Immunology 2021;18:1761-1771: https://www.nature.com/articles/s41423-020-0365-3

[13] Li HB et al. m6A mRNA methylation controls T cell homeostasis by targeting the IL-7/STAT5/SOCS pathways. Nature 2017;548:338-345. PMID: 28792938: https://pubmed.ncbi.nlm.nih.gov/28792938

[14] Gameiro et al. Meta-unstable mRNAs in activated CD8+ T cells are defined by interlinked AU-rich elements and m6A mRNA methylation. Nature Communications 2026;17:160: https://www.nature.com/articles/s41467-025-67762-w

[15] Ghosh P et al. Mettl3-catalyzed m6A methylation determines CD8+ T cell differentiation fate in tumor. bioRxiv 2026: https://www.biorxiv.org/content/10.64898/2026.01.06.697843v1.full-text

[16] YTHDF2 upregulation and subcellular localization dictate CD8 T cell polyfunctionality in anti-tumor immunity. Nature Communications 2024;15:9559: https://www.nature.com/articles/s41467-024-53997-6

[17] Dong L et al. The loss of RNA N6-adenosine methyltransferase Mettl14 in tumor-associated macrophages promotes CD8+ T cell dysfunction and tumor growth. Cancer Cell 2021;39(7):945-957.e10: https://www.sciencedirect.com/science/article/pii/S1535610821002245

[18] Su R et al. R-2HG Exhibits Anti-tumor Activity by Targeting FTO/m6A/MYC/CEBPA Signaling. Cell 2018;172(1-2):90-105: https://www.stemcell.com/r-2hg-exhibits-anti-tumor-activity-by-targeting-fto-m6a-myc-cebpa-signaling.html

[19] Song H et al. METTL3-mediated m6A RNA methylation promotes the anti-tumour immunity of natural killer cells. Nature Communications 2021;12:5522: https://www.nature.com/articles/s41467-021-25803-0

[20] Ji W et al. Pan-cancer characterization of m6A-mediated regulation of T cell exhaustion dynamics. Molecular Therapy: Nucleic Acids 2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC11847731

[21] Zhang D et al. Metabolic regulation of gene expression by histone lactylation. Nature 2019;574(7779):575-580. PMID: 31645732: https://pubmed.ncbi.nlm.nih.gov/31645732

[22] Xiong J et al. Lactylation-driven METTL3-mediated RNA m6A modification promotes immunosuppression of tumor-infiltrating myeloid cells. Molecular Cell 2022;82(9):1660-1677.e10. PMID: 35320754: https://www.sciencedirect.com/science/article/pii/S1097276522002076

[23] Raychaudhuri D et al. Histone lactylation drives CD8 T cell metabolism and function. Nature Immunology 2024;25:2140-2151（ACIR述评）: https://acir.org/weekly-digests/2024/october/understanding-histone-lactylation-to-enhance-immunotherapy

[24] Butt YA et al. Role of m6A RNA Methylation in T Cell Biology and Immunotherapy. Immuno 2026;6(3):50: https://www.mdpi.com/2673-5601/6/3/50

[25] Moreno-Yruela C et al. Class I histone deacetylases (HDAC1–3) are histone lysine delactylases. Science Advances 2022;8(3):eabi6696: https://www.science.org/doi/10.1126/sciadv.abi6696

[26] Gonzatti MB et al. Class I histone deacetylases catalyze lysine lactylation. J Biol Chem 2025;301(10):110602: https://www.jbc.org/article/S0021-9258(25)02453-6/fulltext

[27] De Leo A et al. Glucose-driven histone lactylation promotes the immunosuppressive activity of monocyte-derived macrophages in glioblastoma. Immunity 2024: https://dmsp.web.uniroma1.it/sites/default/files/allegati/2026-04/Rughetti-Glucose.pdf

[28] Zhu J et al. H3K18 lactylation drives CD8+ T cell exclusion and anti-PD-1 resistance in hepatocellular carcinoma. Cell Reports 2026;45(8):117761: https://www.sciencedirect.com/science/article/pii/S2211124726008399

[29] FOXK1-regulated glycolipid metabolism in mediating TOX-induced histone lactylation to promote CD8⁺ T cell exhaustion in high-grade serous ovarian cancer. Scientific Reports 2026;16:5390: https://www.nature.com/articles/s41598-025-32938-3

[30] Li C et al. Epigenetic regulation of CD8+ T cell exhaustion: recent advances and update. Frontiers in Immunology 2025;16:1700039: https://pmc.ncbi.nlm.nih.gov/articles/PMC12582961

[31] Ye J et al. The lactylation-immunosuppression network in cancer: driving a metabolic-epigenetic axis. Frontiers in Immunology 2026;17:1752934: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2026.1752934/full

[32] ACIR Weekly Digest. TOX is so exhausting! 2019（综述Khan/Seo/Scott/Alfei/Yao五篇TOX原始论文）: https://acir.org/weekly-digests/2019/july/tox-is-so-exhausting

[33] ACIR Weekly Digest. Stat5 battles Tox for epigenetic control of T cell exhaustion. 2023（报道Beltra et al. Immunity 2023）: https://acir.org/weekly-digests/2023/december/stat5-battles-tox-for-epigenetic-control-of-t-cell-exhaustion

[34] EurekAlert. FOXO1-KLHL6 axis controlling T cell exhaustion. 2026（报道Nature及Immunity & Inflammation两项研究）: https://www.eurekalert.org/news-releases/1115990

[35] Huang Y, Si X. Rewiring mitochondrial metabolism to counteract exhaustion of CAR-T cells. J Hematol Oncol 2022;15:38: https://www.springermedizin.de/rewiring-mitochondrial-metabolism-to-counteract-exhaustion-of-ca/20264340

[36] Li S, Zhang Q. Rewiring Mitochondrial Metabolism for CD8+ T Cell Memory Formation. Frontiers in Immunology 2020;11:1834: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.01834/full

[37] Simula L, Campello S. Targeting Drp1 and mitochondrial fission for therapeutic immune modulation. Pharmacological Research 2019: https://art.torvergata.it/retrieve/360a6605-396f-48ec-9b32-fd0c3ca331e9/39%202019%20Simula%20PharmRes%20rev.pdf

[38] Zhang T et al. Mitochondria dysfunction in CD8+ T cells as an important contributing factor for cancer development and a potential target for cancer treatment. J Exp Clin Cancer Res 2022;41:227: https://link.springer.com/article/10.1186/s13046-022-02439-6

[39] NCBI Gene. MFN2 mitofusin 2 [Homo sapiens]（含HIV-1 Vpr下调MFN2的信息）: https://www.ncbi.nlm.nih.gov/gene/9927

[40] Ma F, Yu W. The Roles of Lactate and Lactylation in Diseases Related to Mitochondrial Dysfunction. Int J Mol Sci 2025;26(15):7149: https://www.mdpi.com/1422-0067/26/15/7149

[41] Zhai et al. ENO1 couples HDAC1 to regulate histone lactylation and gene transcription. PNAS 2026;123(25):e2535245123: https://www.pnas.org/doi/10.1073/pnas.2535245123

[42] Touxie Quyin Compound regulates histone lactylation-mediated Fabp45 and tissue-resident memory T cells to improve psoriasis recurrence in mice: https://www.researchgate.net/publication/404442894_Touxie_Quyin_Compound_regulates_histone_lactylation-mediated_Fabp45_and_tissue-resident_memory_T_cells_to_improve_psoriasis_recurrence_in_mice
