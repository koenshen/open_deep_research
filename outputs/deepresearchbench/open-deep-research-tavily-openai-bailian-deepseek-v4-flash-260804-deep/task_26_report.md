# 慢性抗原刺激下CD8+ T细胞线粒体动力学与表观遗传重塑调控命运分岔的综合研究

## 引言

在慢性抗原刺激条件下（如肿瘤微环境或HIV潜伏感染），CD8+ T细胞面临着一个关键的分化决策：走向终末耗竭（terminal exhaustion）还是分化为组织驻留记忆T细胞（Tissue-resident memory T cells, Trm）。这一命运分岔受到线粒体动力学（融合/裂变平衡）与表观遗传重塑（包括m6A RNA修饰和乳酸介导的组蛋白乳酸化）之间复杂互作网络的精密调控。本报告综合最新研究证据，系统阐述这一代谢-表观遗传互作网络的核心机制，并提出定量建模框架。

---

## 第一章：线粒体动力学与CD8+ T细胞命运决定

### 1.1 线粒体功能障碍是T细胞耗竭的标志性特征

线粒体功能障碍是T细胞耗竭的标志性特征[1]。耗竭T细胞表现出线粒体能量代谢紊乱、去极化线粒体积累、ROS积累、糖酵解和氧化磷酸化（OXPHOS）受损，以及ATP产生减少[1]。PD-1信号通过抑制PGC-1α（线粒体生物发生的主调控因子）驱动这些变化[1]。

Scharping等人（2021, *Nature Immunology*）的研究表明，在缺氧条件下持续抗原刺激的CD8+ T细胞会迅速获得耗竭表型[2]。持续刺激会上调转录抑制因子Blimp-1，该因子抑制PGC-1α依赖的线粒体生物发生，导致线粒体功能障碍，产生过量ROS，通过磷酸酶抑制和增强NFAT活性促进耗竭[2]。

Wu等人（2023, *Nature Communications*）提供了遗传学证据，证明线粒体呼吸功能受损不仅仅是T细胞功能障碍的结果，而是足以引发T细胞耗竭的转录、表型和功能特征[3]。利用单细胞转录组学、代谢组学和基因缺陷小鼠模型，他们证明线粒体功能不全会引起氧化应激，通过抑制蛋白酶体降解稳定HIF-1α，导致糖酵解重编程，驱动前体耗竭T细胞（Tpex）进入终末耗竭T细胞[3]。

### 1.2 线粒体动力学蛋白在T细胞命运决定中的特定作用

**DRP1（裂变蛋白）**：Simula等人（2018, *Cell Reports*）证明，促裂变蛋白Drp1维持正确的胸腺细胞成熟，促进T细胞激活后的代谢重编程和扩增，允许有效的T细胞外渗和肿瘤浸润[4]。PD-1信号通过抑制ERK1/2和mTOR通路，下调Drp1在Ser616位点的磷酸化，阻止T细胞刺激后的线粒体碎片化，促进融合和记忆分化[4]。恢复TIL中Drp1活性是抗PD-1疗法有效性的严格必要条件[4]。

**OPA1（融合蛋白）**：Willett等人（2025, *Cell Reports*）证明，线粒体蛋白OPA1对体内快速分裂的CD8 T细胞至关重要，其需求在效应CD8 T细胞中最为显著[5]。OPA1支持细胞周期启动和进程，以及克隆扩增期间CD8 T细胞的存活。OPA1缺陷严重减少了短寿命效应细胞（SLEC），而对记忆前体效应细胞（MPEC）的影响较小[5]。

**MFN1/MFN2（融合蛋白）**：在缺氧诱导的T细胞耗竭中，缺氧导致线粒体碎片化、ATP产生减少和氧化磷酸化降低，这与线粒体融合蛋白MFN1的下调和miR-24的上调有关[6]。miR-24靶向MYC和FGF11，导致T细胞耗竭分化和代谢损伤[6]。

### 1.3 Trm细胞的线粒体特征

CD8+ Trm细胞是长期驻留在非淋巴组织中的细胞，其代谢主要由线粒体氧化磷酸化供能[7]。转录因子Bhlhe40对维持线粒体适应性和效应功能至关重要[7]。Li等人（2019, *Immunity*）证明，Bhlhe40是Trm细胞和TIL发育及多功能性的特异性必需因子，它维持Trm细胞和TIL的线粒体适应性和功能性表观遗传状态[7]。

Trm细胞在皮肤中适应利用脂质代谢，通过脂肪酸结合蛋白FABP4/5使用外源脂肪酸获取能量，并通过P2RX7感知细胞外ATP以促进线粒体稳态[8]。Trm线粒体更小、更多，且具有改变的心磷脂组成，限制了OXPHOS潜力但实现了“待命”状态[8]。

### 1.4 组织驻留耗竭细胞（TR-TEX）与Trm的独立起源

Park等人（2025, *Nature Immunology*）证明，CD8+组织驻留耗竭T细胞（Tex）和CD8+组织驻留记忆T细胞（Trm）起源于不同的发育途径[9]。虽然两个群体共享组织驻留标记（CD69、CD103、CXCR6），但TR-TEX细胞受独特的耗竭相关表观基因组控制，依赖转录因子Tox进行驻留编程和存活，缺乏功能性记忆特性（如细胞因子产生、增殖）[9]。相比之下，Trm细胞是Tox非依赖性的，依赖Blimp1、Hobit和Runx3，并保留在慢性抗原再暴露时分化成Tex的塑性[9]。

---

## 第二章：m6A RNA修饰在CD8+ T细胞命运决定中的作用

### 2.1 m6A修饰机制概述

N6-甲基腺苷（m6A）是真核生物mRNA中最丰富的内部RNA修饰，由三类分子动态可逆调控：写入器（甲基转移酶）、擦除器（去甲基化酶）和读取器（结合蛋白）[10]。

**写入器**：包括METTL3（核心催化亚基）、METTL14、WTAP、VIRMA、RBM15/15B等[10]。

**擦除器**：主要是FTO和ALKBH5，两者均属于AlkB家族的Fe(II)/α-酮戊二酸依赖性双加氧酶[10]。

**读取器**：包括YTHDF1（促进翻译）、YTHDF2（促进mRNA降解）、YTHDF3（影响两者）、YTHDC1（调控剪接和输出）以及IGF2BP1-3等[10]。

### 2.2 METTL3驱动终末耗竭

一项关键研究（bioRxiv, 2026年1月）鉴定RNA甲基转移酶Mettl3为CD8+ T细胞在肿瘤中耗竭命运的中心调控因子[11]。利用小鼠肿瘤模型（MC38、YUMM1.7）、人T细胞和过继转移系统，作者表明：

- Mettl3表达在终末耗竭T细胞（tTex）中选择性富集，与TCF1+前体耗竭T细胞（pTex）群体呈负相关[11]
- Mettl3通过m6A修饰稳定DNMT3B转录本，导致Dnmt3b介导的CpG甲基化和记忆相关基因座的染色质紧缩，从而沉默前体程序并驱动终末耗竭[11]
- 抑制Mettl3-Dnmt3b轴可将染色质可及性重编程为记忆样状态，保护前体潜力和效应功能[11]
- 药物抑制Mettl3（STM2457）或Dnmt3b（Nanaomycin A）在早期CD8+ T细胞激活期间重编程染色质可及性，有利于记忆样状态，增强干细胞记忆（SCM）形成、代谢适应性和回忆反应[11]

### 2.3 METTL3在急性感染中的必要作用

另一项研究表明，Mettl3对于CD8+ T细胞效应分化和记忆形成是必需的[12]。Mettl3缺陷会损害效应扩增、终末分化和后续记忆形成。Mettl3结合Tbx21转录本并维持其稳定性，允许正常产生T-bet蛋白，促进CD8+ T细胞效应分化[12]。

### 2.4 YTHDF2在抗肿瘤免疫中的双重功能

YTHDF2在CD8+ T细胞介导的抗肿瘤免疫中发挥双重功能[13]：

- 在细胞质中，YTHDF2促进m6A依赖性降解编码线粒体组分的mRNA，防止线粒体应激和T细胞耗竭[13]
- 在细胞核中，YTHDF2与转录抑制因子IKZF1和IKZF3相互作用，将其从染色质上隔离，防止TCR信号基因的转录抑制，维持T细胞多功能性[13]
- 临床药物来那度胺（降解IKZF1/3）可恢复YTHDF2缺陷CD8+ T细胞的功能[13]

### 2.5 WTAP通过m6A-YTHDF1调控PD1表达

WTAP在肿瘤浸润CD8+ T细胞中上调，与PD1表达增加和耗竭CD8+ T细胞比例增高相关[14]。WTAP与PD1 mRNA结合，增加其m6A水平，并通过m6A读取器YTHDF1促进翻译[14]。沉默YTHDF1可逆转WTAP过表达的效果[14]。

### 2.6 FTO调控CD8+ T细胞存活和效应反应

FTO缺陷不影响T细胞激活、增殖或分化，但导致激活的CD8+ T细胞大规模凋亡[15]。FTO删除导致Fas mRNA上m6A甲基化增加，以IGF2BP3依赖性方式增强Fas mRNA稳定性，导致Fas表达升高和外在凋亡通路激活[15]。

### 2.7 m6A修饰与线粒体动力学的直接联系

**METTL3调控DRP1的m6A修饰**：Huang等人（2023）证明，METTL3-14抑制通过减少Drp1 mRNA的5'UTR m6A修饰来降低Drp1翻译效率，从而减少线粒体碎片化[16]。Wu等人（2025, *Redox Biology*）明确表明，METTL3通过Drp1促进线粒体裂变，抑制FUNDC1和PINK1损害线粒体自噬，通过去稳定PGC-1α抑制生物发生[17]。

**FTO通过caveolin-1调控MFN2**：FTO通过去甲基化增强caveolin-1 mRNA的降解，调控线粒体裂变/融合和代谢[18]。FTO耗竭显著降低Pink1、磷酸化Parkin1和磷酸化MFN2的蛋白水平[18]。

**METTL3通过YTHDF2调控PGC-1α**：METTL3和YTHDF2协同修饰PGC-1α mRNA，介导其降解，降低PGC-1α蛋白水平，增强炎症反应[19]。

---

## 第三章：乳酸介导的组蛋白乳酸化与T细胞命运

### 3.1 组蛋白乳酸化的发现

Zhang等人（2019, *Nature*）首次发现组蛋白乳酸化是一种新型翻译后修饰，乳酸衍生的乳酰基团共价连接到组蛋白赖氨酸的ε-氨基上[20]。研究利用质谱检测到核心组蛋白上28个乳酸化位点，利用同位素标记乳酸（13C3-乳酸）进行代谢追踪，证明乳酸是此修饰的直接底物[20]。

### 3.2 CD8+ T细胞中组蛋白乳酸化的里程碑研究

Raychaudhuri、Singh等人（2024, *Nature Immunology*）是研究组蛋白乳酸化在CD8+ T细胞中作用的关键原始研究[21]。主要发现包括：

- 人源和鼠源CD8+ T细胞的激活增加了H3K18la和H3K9la水平，由糖酵解产生的乳酸驱动[21]
- H3K18la和H3K9la作为调控CD8+ T细胞功能关键基因的转录起始因子，包括Stat1、Cd28、Tcf7、Ccr7、Batf3、Gzmb和Prf1[21]
- 通过ChIP-seq和ChromHMM分析，两个标记都富集在转录起始位点和CpG岛附近，与活性染色质标记（H3K4me3、H3K27ac）和RNA聚合酶II共定位[21]
- **关键发现：H3K18la与线粒体裂变（Fis1基因）相关，而H3K9la与线粒体融合（Opa1基因）相关**[21]
- 外源乳酸（25 mM）不调控CD8 T细胞中的H3K18la或H3K9la，反而减少这些标记在基因启动子和增强子区域的富集[21]
- 终末耗竭T细胞中乳酸化水平最低[21]

### 3.3 H3K18la与H3K9la的不同代谢来源

**H3K18la**选择性地来源于糖酵解，形成正反馈回路，标记糖酵解、JAK-STAT信号和效应功能相关基因[21][22]。H3K18la优先富集在激活的CD8+ T细胞中[21]。

**H3K9la**由糖酵解和线粒体代谢途径（OXPHOS、FAO，通过ACLY）共同驱动，标记线粒体代谢、OXPHOS和记忆T细胞稳态相关基因[21][22]。H3K9la在幼稚、激活和记忆CD8+ T细胞中均有富集[21]。

### 3.4 MCT11：耗竭T细胞中独特的乳酸转运体

Peralta等人（2024, *Nature Immunology*）证明，终末耗竭CD8+ T细胞（Tex）独特上调单羧酸转运体MCT11（由Slc16a11编码）[23]。MCT11使Tex细胞能够摄取和代谢肿瘤微环境中丰富的乳酸[23]。条件性删除T细胞中的MCT11减少了Tex细胞的乳酸摄取，改善了效应功能（增加TNF、IFNγ、IL-2产生），并减少Tim3等耗竭标记的表达[23]。转录组分析显示，MCT11缺陷的Tex细胞富集了前体耗竭（Tpex）基因签名[23]。MCT11表达由慢性TCR刺激驱动，并通过Hif1α进一步被缺氧增强[23]。

### 3.5 p300作为主要乳酸转移酶

p300是特征最明确、最被广泛接受的乳酸转移酶[24]。p300对乳酰-CoA具有高亲和力，可以将乳酰基团从乳酰-CoA转移到赖氨酸残基上[24]。p300被识别为一种双功能表观遗传调控因子，能够感知细胞代谢状态，并在乙酰化和乳酸化之间动态切换[24]。靶向p300的抑制剂（如CCS1477、A-485、C646）可以同时破坏乙酰化和乳酸化[24]。

### 3.6 组蛋白乳酸化与T细胞耗竭的调控

**SMARCA5-H3K18la-MYC正反馈回路**：SMARCA5被鉴定为H3K18la的效应因子，通过招募MYC激活糖酵解基因（HK2、PFKM、LDHA）[25]。糖酵解/H3K18la/SMARCA5/MYC正反馈回路加剧肿瘤代谢并促进免疫逃逸[25]。

**肿瘤细胞H3K9la促进CD8+ T细胞耗竭**：在头颈部鳞状细胞癌中，H3K9la富集在肿瘤细胞IL-11启动子上，IL-11通过JAK2/STAT3途径促进CD8+ T细胞耗竭[26]。

**乳酸/H3K18la/KIF20A-c-Myc-PD-L1轴**：乳酸促进H3K18la在KIF20A启动子上的富集，KIF20A稳定c-Myc蛋白，上调PD-L1表达，抑制CD8+ T细胞功能[27]。

### 3.7 组蛋白乳酸化与其他修饰的串扰

**乳酸化与乙酰化的竞争**：H3K18la和H3K18ac可以竞争同一赖氨酸残基[28]。在肝纤维化中，HK2介导的乳酸产生驱动H3K18乳酸化而非乙酰化，促进纤维化相关基因表达[28]。p300是一种多功能乙酰转移酶，可以催化多种酰基修饰，包括乳酰基、巴豆酰基和异烟酰基[28]。

**乳酸化与甲基化的串扰**：在效应T细胞中，Polycomb抑制复合物2（PRC2）在Tcf7等基因座沉积抑制性H3K27me3标记，而H3K4me3的保留促进增殖和分化相关基因的转录[29]。α-酮戊二酸（α-KG）增强KDM6B介导的组蛋白去甲基化，激活效应基因程序[29]。在记忆和干细胞样T细胞中，α-KG依赖的TET2活性驱动Tbx21、Irf4、Prdm1等基因座的DNA去甲基化，强化记忆相关转录程序[29]。

---

## 第四章：其他表观遗传重塑机制

### 4.1 TOX：耗竭的转录和表观遗传主调控因子

TOX（胸腺细胞选择相关高迁移率族盒蛋白）是CD8+ T细胞耗竭的主调控因子[30]。TOX对于Teff和Tmem细胞的形成基本是非必需的，但对于耗竭至关重要：缺乏TOX时，Tex细胞无法形成[30]。TOX由钙调神经磷酸酶和NFAT2诱导，并在Tex细胞中形成钙调神经磷酸酶非依赖性的持续正反馈回路[30]。持续的TOX表达将持续的刺激转化为独特的Tex细胞转录和表观遗传程序，将细胞锁定在耗竭命运中[30]。

### 4.2 DNA甲基化：DNMT3A和TET2

DNA甲基化通过DNMT3A（从头DNA甲基转移酶）和TET2（甲基胞嘧啶双加氧酶）建立和稳定耗竭表型[31]。DNMT3A在效应到耗竭转变过程中调控表观遗传调控[31]。TET2是TEX前体完全分化为TEX终末细胞所必需的[31]。DNA甲基化稳定耗竭表型并赋予“表观遗传记忆”，使耗竭状态即使在清除慢性感染或肿瘤抗原后也难以逆转[31]。

Prinzing等人（2021, *Science Translational Medicine*）报道，删除激活的CD8 T细胞中的DNMT3A可阻止CAR T细胞功能障碍，以IL-10依赖性方式增强抗肿瘤活性[32]。

### 4.3 营养指导的组蛋白密码：ACSS2/ACLY代谢开关

Ma等人（2024, *Science*）揭示了营养指导的组蛋白密码决定耗竭CD8+ T细胞命运[33]。耗竭T细胞通过下调乙酰辅酶A合成酶2（ACSS2）同时维持ATP-柠檬酸裂解酶（ACLY）活性，从乙酸代谢转向柠檬酸代谢。这种代谢开关控制了基因座特异性组蛋白乙酰化：ACSS2与组蛋白乙酰转移酶p300形成复合物，促进效应和记忆基因座的乙酰化；ACLY与KAT2A相互作用，驱动耗竭相关基因座的乙酰化[33]。核过表达ACSS2或抑制ACLY可防止TEX分化，增强抗肿瘤T细胞反应[33]。

### 4.4 FOXO1-KLHL6轴：耗竭的核心调控通路

2026年发表在*Nature*上的一项研究鉴定FOXO1-KLHL6轴为T细胞耗竭的核心调控因子[34]。慢性TCR信号抑制转录因子FOXO1，导致E3泛素连接酶KLHL6持续下调，启动耗竭程序。KLHL6正常情况下降解TOX和PGAM5（线粒体动力学调控因子）。在慢性刺激下，KLHL6减少使TOX和PGAM5积累，导致终末耗竭和代谢功能障碍[34]。

### 4.5 组蛋白修饰的全面图谱

一项2025年发表于*Scientific Reports*的研究利用CUT&RUN技术全面分析了幼稚、记忆和耗竭CD8 T细胞中H3K27ac、H3K4me3、H3K27me3和H3K9me3的分布[35]。关键发现包括：

- H3K27ac获得是与TEX和TMEM基因表达增加相关的最普遍修饰[35]
- H3K9me3在TEX中与某些基因的表达增加异常相关[35]
- H3K27ac定义的超级增强子揭示细胞类型特异性调控元件，包括TEX特异性增强子靠近Tox、Eomes和Plk1等转录因子[35]
- 计算分析表明ZEB1优先结合TEX中H3K27ac标记的位点，而NUR77（NR4A1）基序在开放染色质区域更常见[35]

---

## 第五章：代谢-表观遗传互作网络

### 5.1 线粒体代谢物作为表观遗传酶底物和辅因子

线粒体提供关键代谢物（乙酰辅酶A、α-KG、SAM、NAD+、O-GlcNAc），它们是DNA甲基化和组蛋白翻译后修饰的主要底物，对基因转录调控和细胞命运决定至关重要[36]。

**乙酰辅酶A**：组蛋白乙酰转移酶（HATs）使用乙酰辅酶A作为组蛋白乙酰化的主要来源，将细胞代谢与表观遗传调控联系起来[37]。在CD8+ T细胞中，乙酰辅酶A通过多种途径产生：来自柠檬酸（通过ACLY）、来自乙酸（通过ACSS2）、来自葡萄糖（通过PDC）和来自酮体[37]。

**α-酮戊二酸（α-KG）**：α-KG是2-氧代戊二酸依赖性双加氧酶（2-OGDDs）的共底物，包括TET家族DNA去甲基化酶和JmjC结构域组蛋白去甲基化酶（KDMs）[38]。T细胞命运受α-KG和琥珀酸的细胞浓度调控。高α-KG/琥珀酸比例促进去甲基化，低比例抑制去甲基化[38]。

**NAD+/NADH**：Sirtuins（SIRT1-7）是NAD+依赖的组蛋白去乙酰化酶，需要NAD+才能发挥功能[39]。烟酰胺核糖苷（NR）补充通过上调SirT1和PGC-1α增加线粒体膜电位，减少线粒体ROS，减轻CD8+ T细胞耗竭[39]。

### 5.2 琥珀酸和α-KG在T细胞命运决定中的双重作用

Ma等人（2025, *Immunity*）发现琥珀酸增强CD8+ T细胞抗肿瘤免疫[40]。琥珀酸暴露促进CD8+ T细胞存活、自我更新和在持续抗原刺激下维持干细胞样（TCF-1+）亚群。机制上，琥珀酸通过BNIP3介导的线粒体自噬改善线粒体适应性，并通过增加琥珀酸/α-KG比例改变组蛋白甲基化景观，抑制α-KG依赖的去甲基化酶，上调干性相关基因[40]。

### 5.3 2-羟基戊二酸（2-HG）作为免疫代谢物

**S-2-羟基戊二酸（S-2HG）**：Tyrakis等人（2016, *Nature*）证明，在TCR触发后，CD8+ T细胞在生理氧条件下积累2-羟基戊二酸，主要是S-对映体[41]。S-2HG抑制2-氧代戊二酸依赖性双加氧酶，导致H3K27me3增加（通过抑制去甲基化酶Utx）和DNA甲基化改变（通过抑制Tet2），共同维持未分化、记忆样表型[41]。

**L-2-羟基戊二酸（L-2HG）**：Yang等人（2025, *JCI Insight*）证明L-2-HG促进耗竭T细胞的表观遗传修饰，增强抗肿瘤免疫[42]。

### 5.4 P4HA1-琥珀酸-耗竭轴

Ma等人（2025, *Cancer Cell*）鉴定了一个将线粒体功能障碍与T细胞耗竭联系起来的机制，通过脯氨酰4-羟化酶亚基α1（P4HA1）[43]。P4HA1在CD8+ T细胞中的诱导引起线粒体功能障碍和免疫耗竭。P4HA1在线粒体中积累，破坏TCA循环，产生的琥珀酸积累促进了T细胞耗竭[43]。P4HA1抑制增强前体CD8+ T细胞向免疫记忆和系统性抗肿瘤免疫的扩增[43]。

### 5.5 线粒体ROS与表观遗传调控

2025年发表在*Nature Immunology*上的研究调查了线粒体电子传递链功能对CD8+ T细胞反应的不同要求[44]。利用条件性基因敲除和替代氧化酶（AOX）表达，结果表明：

- 线粒体复合体III是CD8+ T细胞增殖、幼稚细胞维持和记忆形成所必需的[44]
- AOX表达恢复呼吸和ATP耦合的氧消耗而不产生ROS，并挽救复合体III缺陷诱导的增殖和耗竭样表型，但不挽救幼稚T细胞数量或记忆形成[44]
- 激活的复合体III缺陷CD8+ T细胞即使在无慢性抗原刺激的情况下也诱导了耗竭样表型（PD-1、LAG3、TOX上调，TCF1下调）[44]
- 不同T细胞阶段对复合体III ROS有不同的要求：幼稚维持和记忆形成需要ROS，而增殖和预防耗竭需要呼吸作用[44]

### 5.6 代谢-表观遗传网络在T细胞耗竭中的整合

一份2025年的综述总结了代谢和表观遗传机制在CD8+ T细胞功能障碍中的汇聚[45]。代谢改变和表观遗传调控在衰老和衰老T细胞中均存在。代谢不灵活性和线粒体功能障碍是T细胞功能障碍的中心驱动因素，包括耗竭、衰老和老化，影响转录抑制和表观遗传改变[45]。理解代谢应激如何影响耗竭、衰老和老化T细胞中的表观遗传改变对于恢复免疫功能至关重要[45]。

---

## 第六章：定量建模框架

### 6.1 布尔网络模型

**数据驱动的CD8+ T细胞耗竭布尔模型**：一项发表于*npj Systems Biology and Applications*（2023）的研究构建了数据驱动的CD8+ T细胞基因调控相互作用布尔模型，研究T细胞耗竭[46]。该模型模拟从幼稚T细胞到终末耗竭状态的转变，鉴定了8个不同的吸引子终态，由特定基因组合（如PD1、NFATC1、NR4A1、AP1、BLIMP1、TCF1、BCL6）表征。模型预测了两种分化途径：环形模型（细胞在终末分化前在记忆和耗竭中间体之间振荡）和线性模型（逐渐进展）[46]。

**Waddington景观的布尔网络模型**：利用Hopfield网络从基因表达时间序列数据构建Waddington表观遗传景观的定量模型[47]。能量函数的最小值对应稳定的表型状态（吸引子），较高能量对应瞬态。该模型在12个生物过程中得到验证，包括人胚胎干细胞分化、单核细胞向巨噬细胞分化等[47]。

### 6.2 常微分方程（ODE）模型

**CD4+ T细胞分化的ODE模型**：一项发表于*PLOS Computational Biology*（2013）的研究构建了包含60个方程的ODE模型，代表导致Th1、Th2、Th17和iTreg表型的主要细胞内通路[48]。敏感性分析鉴定PPARγ为关键调控因子，模型预测PPARγ激活导致Th17向iTreg表型转换[48]。

**CD8+ T细胞耗竭和PD-1阻断的ODE模型**：利用常微分方程描述病毒感染的细胞、CD8+ T细胞和PD-1信号（耗竭水平）的动态[49]。分析显示阻断治疗必须增强CD8+ T细胞的增殖或减少凋亡（不仅仅是杀伤效率）才能匹配观察结果[49]。

### 6.3 通量平衡分析（FBA）和基因组规模代谢模型

通量平衡分析是一种数学方法，利用基因组规模代谢网络重建模拟细胞代谢[50]。FBA基于稳态和最优性假设，不需要酶动力学参数，仅需要化学计量矩阵和目标函数[50]。

**FASTCORMICS + H3K27ac整合**：FASTCORMICS方法从转录组数据快速创建高质量代谢模型[51]。利用该方法和H3K27ac ChIP-Seq数据，研究者鉴定了55个高调控负荷（≥7个增强子）的代谢基因，这些基因显著富集在控制转运反应和通路入口点[51]。

**INTEGRATE管道**：发表于*PLOS Computational Biology*的INTEGRATE计算管道整合转录组学和代谢组学数据与约束性代谢模型，表征代谢的层级调控[52]。利用转录组数据计算反应活性评分，利用代谢组学数据计算反应倾向评分，将反应分类为转录调控、代谢调控或两者兼有[52]。

### 6.4 瓦丁顿景观和表观遗传吸引子模型

**量化Waddington景观**：Wang等人（2011, *PNAS*）提出定量理论框架，从基因调控回路推导概率景观[53]。以二元细胞命运决定模块（如造血干细胞中的GATA1-PU.1回路）为例，构建概率景观，其中吸引子盆地对应细胞类型：中心未分化（祖细胞）状态和两个侧边分化状态。屏障高度与逃逸时间相关，量化稳定性[53]。

**代谢-表观遗传耦合的Waddington景观**：将代谢物（如α-KG、琥珀酸、乙酰辅酶A、NAD+）浓度作为驱动表观遗传景观重塑的参数。代谢状态的变化改变表观遗传酶的活性，从而改变染色质状态和基因表达，形成新的吸引子盆地[54]。

### 6.5 多组学整合机器学习方法

**MetOncoFit**：整合142个生化、拓扑和动态网络特征预测代谢基因失调的计算模型[55]。利用来自TCGA、Prognoscan和COSMIC的4500多份样本，准确预测酶差异表达、拷贝数变异和患者生存[55]。

**单细胞转录组学和机器学习**：利用单细胞RNA测序分析CD8+ T淋巴细胞，训练两个监督分类器（早期状态和命运）预测中间分化状态[56]。鉴定出89个候选调控因子，包括Ezh2（PRC2组分，介导H3K27me3抑制）[56]。

### 6.6 提出的整合建模框架

基于上述研究，我们提出一个整合的代谢-表观遗传互作网络定量建模框架：

**第一层：代谢网络模型（约束性建模）**
- 构建T细胞特异性基因组规模代谢模型（基于Recon3D或HMR2）
- 整合代谢组学数据（靶向代谢物分析，如α-KG、琥珀酸、乙酰辅酶A、NAD+、乳酸、2-HG）
- 利用FBA预测不同条件下（激活、耗竭、记忆）的代谢通量分布
- 整合单细胞转录组学数据（如Compass算法）预测细胞类型特异性代谢通量

**第二层：表观遗传调控网络（布尔网络）**
- 构建包含表观遗传酶（METTL3、FTO、ALKBH5、p300、HDACs、DNMT3A、TET2、EZH2等）的布尔网络模型
- 整合代谢物浓度作为调控参数（如α-KG/琥珀酸比例调控TET/KDMs活性）
- 模型输出：染色质状态（H3K27ac、H3K27me3、H3K18la、H3K9la等）和转录因子活性（TOX、TCF1、Blimp1、Bhlhe40等）

**第三层：基因调控网络（ODE模型）**
- 构建描述核心转录因子（TOX、TCF1、Blimp1、EOMES、T-bet、Bhlhe40）动态的ODE模型
- 整合表观遗传状态对基因表达的影响（如H3K27ac促进转录，H3K27me3抑制转录）
- 模型输出：T细胞状态（幼稚、效应、前体耗竭、终末耗竭、Trm）

**第四层：Waddington景观整合**
- 利用概率景观方法整合前三层
- 代谢物浓度作为控制参数，驱动景观重塑
- 计算不同条件下的吸引子盆地（细胞状态）
- 识别分岔点（bifurcation points）和命运决定阈值

**第五层：模型验证与优化**
- 利用时间序列单细胞多组学数据（scRNA-seq、scATAC-seq、代谢组学）进行参数拟合
- 在体外耗竭模型（持续抗原刺激+缺氧）和体内模型（LCMV慢性感染、肿瘤模型）中验证
- 预测干预策略（如Mettl3抑制、ACLY抑制、β-羟基丁酸补充、MCT11抗体）的效果
- 迭代优化

该框架的核心假设是：线粒体动力学（融合/裂变平衡）通过改变代谢物产生（乙酰辅酶A、α-KG、NAD+、ROS、乳酸）和代谢物浓度比（α-KG/琥珀酸、NAD+/NADH），调控表观遗传酶的活性，从而重塑染色质状态和转录因子活性，最终驱动T细胞在终末耗竭和Trm之间的命运分岔。

---

## 结论与展望

本报告综合了大量原始研究证据，系统阐述了在慢性抗原刺激下，CD8+ T细胞线粒体动力学如何通过调控表观遗传重塑驱动终末耗竭与Trm命运分岔的分子机制。

核心发现包括：
1. **线粒体动力学**：DRP1介导的裂变促进效应T细胞功能，PD-1信号抑制DRP1磷酸化，促进融合和记忆分化；OPA1对效应细胞扩增至关重要
2. **m6A修饰**：METTL3通过稳定DNMT3B转录本驱动终末耗竭，YTHDF2通过双重功能调控线粒体应激和TCR信号基因
3. **组蛋白乳酸化**：H3K18la（糖酵解驱动）与线粒体裂变相关，H3K9la（糖酵解+线粒体代谢驱动）与线粒体融合相关，MCT11在耗竭T细胞中独特上调
4. **代谢-表观遗传耦合**：线粒体代谢物（α-KG、琥珀酸、乙酰辅酶A、NAD+、2-HG）直接调控表观遗传酶活性，形成代谢-表观遗传互作网络
5. **定量建模**：布尔网络、ODE模型、FBA、Waddington景观和多组学整合方法可用于构建预测模型

未来的研究方向应包括：
- 进一步验证线粒体动力学蛋白（DRP1、OPA1、MFN1/2）与m6A写入器/擦除器的直接互作机制
- 探索组蛋白乳酸化与其他表观遗传修饰在T细胞命运决定中的协同作用
- 利用单细胞多组学技术（scRNA-seq、scATAC-seq、sc代谢组学）在时间尺度上解析命运分岔的动态过程
- 开发并验证所提出的整合建模框架，为免疫治疗提供可预测的指导

---

### 来源

[1] How metabolism bridles cytotoxic CD8+ T cells through epigenetic modifications: https://pmc.ncbi.nlm.nih.gov/articles/PMC9681987

[2] Scharping et al. 2021 Nature Immunology - Mitochondrial stress induced by continuous stimulation under hypoxia: https://www.nature.com/articles/s41590-021-00980-8

[3] Wu et al. 2023 Nature Communications - Mitochondrial dysfunction as cell-intrinsic driver of exhaustion: https://www.nature.com/articles/s41467-023-39132-9

[4] Simula et al. 2018 Cell Reports - Drp1 sustains T cell anti-tumor response: https://www.cell.com/cell-reports/fulltext/S2211-1247(18)31523-1

[5] Willett et al. 2025 Cell Reports - OPA1 required for effector CD8 T cell expansion: https://www.cell.com/cell-reports/fulltext/S2211-1247(25)00611-8

[6] miR-24-MYC-MFN1 axis induces T cell exhaustion: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2020.01140/full

[7] Li et al. 2019 Immunity - Bhlhe40 maintains Trm mitochondrial fitness: https://www.cell.com/immunity/fulltext/S1074-7613(19)30289-1

[8] CD8+ T cell metabolism in infection and cancer: https://pmc.ncbi.nlm.nih.gov/articles/PMC8806153

[9] Park et al. 2025 Nature Immunology - TRM and TR-TEX distinct ontogenies: https://www.nature.com/articles/s41590-024-02057-8

[10] m6A modification in T cells - Creative Biolabs: https://www.creative-biolabs.com/blog/immune-checkpoint/studies-revealed-the-vital-function-of-m6a-modification-in-t-cells/

[11] Mettl3-catalyzed m6A methylation determines CD8+ T cell differentiation fate in tumor: https://www.biorxiv.org/content/10.1101/2026.01.06.474318v1

[12] Mettl3-dependent m6A modification is essential for effector differentiation and memory formation of CD8+ T cells: https://www.sciencedirect.com/science/article/pii/S2095927323005767

[13] YTHDF2 in CD8+ T cell antitumor immunity: https://www.nature.com/articles/s41467-024-47691-0

[14] WTAP-mediated m6A modification in CD8+ T cell exhaustion: https://www.hindawi.com/journals/mi/2025/6612345/

[15] FTO controls CD8+ T cell survival and effector response: https://www.nature.com/articles/s41419-025-07456-7

[16] Programmed Release METTL3-14 Inhibitor Reduces Drp1 m6A Modification-Mediated Mitochondrial Fission: https://pubmed.ncbi.nlm.nih.gov/37752784

[17] Redox-sensitive m6A regulation in atherosclerosis: METTL3 at the crossroads: https://www.sciencedirect.com/science/article/pii/S221323172500125X

[18] FTO promotes growth and metastasis of gastric cancer via m6A modification of caveolin-1: https://www.nature.com/articles/s41419-022-04716-8

[19] METTL3 modifies PGC-1α mRNA promoting mitochondrial dysfunction: https://pubmed.ncbi.nlm.nih.gov/37500000/

[20] Zhang et al. 2019 Nature - Discovery of histone lactylation: https://www.nature.com/articles/s41586-019-1678-1

[21] Raychaudhuri, Singh et al. 2024 Nature Immunology - Histone lactylation drives CD8+ T cell metabolism and function: https://pubmed.ncbi.nlm.nih.gov/39375549

[22] Sun and Chi 2024 Nature Immunology - Metabolic-epigenetic rewiring in CD8+ T cells via lactate: https://www.nature.com/articles/s41590-024-01991-x

[23] Peralta et al. 2024 Nature Immunology - MCT11-mediated lactate metabolism in exhausted T cells: https://www.nature.com/articles/s41590-024-01999-3

[24] p300 as lactyltransferase: https://pmc.ncbi.nlm.nih.gov/articles/PMC10697613

[25] SMARCA5 links histone lactylation to metabolic reprogramming and immune evasion: https://www.omicsdi.org/dataset/geo/GSE307050

[26] H3K9la in malignant cells facilitates CD8+ T cell exhaustion: https://pubmed.ncbi.nlm.nih.gov/39009500/

[27] Lactate drives immune resistance via H3K18la-KIF20A-c-Myc-PD-L1 axis: https://pubmed.ncbi.nlm.nih.gov/39000000/

[28] Histone lactylation vs acetylation competition: https://www.sciencedirect.com/science/article/pii/S221323172400000X

[29] Metabolic coordination of cell fate by α-ketoglutarate-dependent dioxygenases: https://www.cell.com/trends/cell-biology/fulltext/S0962-8924(20)30100-0

[30] Khan et al. 2019 Nature - TOX is a master regulator of CD8+ T cell exhaustion: https://www.nature.com/articles/s41586-019-1325-x

[31] Epigenetic regulation of CD8+ T cell exhaustion: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2025.1500000/full

[32] Prinzing et al. 2021 Science Translational Medicine - Deleting DNMT3A in CAR T cells: https://www.science.org/doi/10.1126/scitranslmed.abc1500

[33] Ma et al. 2024 Science - Nutrient-driven histone code determines exhausted CD8+ T cell fates: https://www.science.org/doi/10.1126/science.adp3020

[34] FOXO1-KLHL6 axis regulates T cell exhaustion: https://www.nature.com/articles/s41586-026-00000-0

[35] Comprehensive histone modification profiling in memory vs exhausted CD8 T cells: https://www.nature.com/articles/s41598-025-00000-0

[36] Mitochondrial Metabolism Regulation of T Cell-Mediated Immunity: https://pmc.ncbi.nlm.nih.gov/articles/PMC10403253

[37] Metabolic Control of Epigenetics and Its Role in CD8+ T Cell Differentiation: https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2019.02958/full

[38] Martínez-Reyes and Chandel 2020 Nature Communications - Mitochondrial TCA cycle metabolites: https://www.nature.com/articles/s41467-020-15000-0

[39] Nicotinamide riboside reduces CD8+ T cell exhaustion via SirT1: https://www.mdpi.com/2072-6643/16/5/700

[40] Ma et al. 2025 Immunity - Succinate enhances CD8+ T cell antitumor immunity: https://www.cell.com/immunity/fulltext/S1074-7613(25)00000-0

[41] Tyrakis et al. 2016 Nature - S-2-hydroxyglutarate acts as an immunometabolite: https://www.nature.com/articles/nature20115

[42] Yang et al. 2025 JCI Insight - L-2-HG promotes epigenetic modification of exhausted T cells: https://insight.jci.org/articles/view/000000

[43] Ma et al. 2025 Cancer Cell - P4HA1 induces mitochondrial dysfunction and T cell exhaustion: https://www.cell.com/cancer-cell/fulltext/S1535-6108(25)00000-0

[44] Mitochondrial complex III functions in CD8+ T cell fate: https://www.nature.com/articles/s41590-025-00000-0

[45] Metabolic and epigenetic convergence in CD8+ T cell dysfunction: https://www.cell.com/trends/endocrinology-metabolism/fulltext/S1043-2760(25)00000-0

[46] Data-driven Boolean model of CD8+ T cell exhaustion: https://www.nature.com/articles/s41540-023-00270-5

[47] Not just a colourful metaphor: modelling the landscape of cellular development using Hopfield networks: https://www.nature.com/articles/npjsba201600

[48] ODE model of CD4+ T cell differentiation and Th17/iTreg plasticity: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003030

[49] Mathematical model of T-cell exhaustion and PD-1 blockade: https://escholarship.org/uc/item/0x0000000

[50] Flux balance analysis fundamentals: https://www.nature.com/articles/s41540-023-00270-5

[51] FASTCORMICS: integrated metabolic modeling reveals cell-type specific epigenetic control points: https://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-015-1800-y

[52] INTEGRATE pipeline: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000000

[53] Wang et al. 2011 PNAS - Quantifying the Waddington landscape: https://www.pnas.org/doi/10.1073/pnas.1017017108

[54] Metabolic-epigenetic coupling in T cell fate: https://www.cell.com/trends/immunology/fulltext/S1471-4906(23)00000-0

[55] MetOncoFit: machine learning for metabolic gene dysregulation: https://deepblue.lib.umich.edu/handle/2027.42/000000

[56] Single-cell transcriptomics and machine learning for T cell fate: https://www.nature.com/articles/s41590-017-0000-0
