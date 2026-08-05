# 二维半导体低电阻接触的统一物理机制与未来研究方向：以MoS₂为模型系统

## 引言

二维半导体，特别是二硫化钼（MoS₂），因其优异的电学性能和原子级厚度，被视为延续摩尔定律的有力候选材料。然而，金属电极与二维半导体之间的高接触电阻始终是制约高性能器件发展的核心瓶颈。近年来，研究者们提出了多种降低接触电阻的策略，包括半金属接触（如铋、锑）、纯金接触、相工程、范德华间隙工程、化学掺杂以及边缘接触等，每种方法都取得了令人瞩目的成果，但每种方法背后的理论解释各不相同，使得该领域缺乏一个统一的发展方向。

本报告基于对大量原始实验和理论文献的系统梳理，深入分析了各种低接触电阻策略的物理机制，识别出其中的共通原理，并提出了一个以“界面耦合强度”为核心参数的统一理论框架。基于该框架，我们进一步探讨了该领域未来的关键研究方向。

## 现有低接触电阻策略的机制概览

### 半金属接触（铋Bi与锑Sb）

铋（Bi）半金属接触是近年来最受瞩目的突破。Shen等人（2021年）在《Nature》上报道，半金属铋与单层MoS₂之间实现了欧姆接触，接触电阻低至**123 Ω·µm**，开态电流密度高达**1,135 µA/µm** [来源: Ultralow contact resistance between semimetal and monolayer semiconductors](http://ciqm.harvard.edu/uploads/2/3/3/4/23349210/shensu2021.pdf)。其核心机制在于：铋在费米能级处具有**极低的态密度（DOS）**，这有效抑制了金属诱导的间隙态（MIGS）的形成，使得MoS₂在接触区发生自发简并掺杂，从而消除了肖特基势垒 [来源: Ultralow contact resistance between semimetal and monolayer semiconductors](http://ciqm.harvard.edu/uploads/2/3/3/4/23349210/shensu2021.pdf)。

随后，锑（Sb）半金属接触被证明具有更优的热稳定性（熔点630.6°C，远高于Bi的271.5°C），并实现了**42 Ω·µm**的接触电阻，接近量子极限 [来源: Antimony Semimetal Contact with Enhanced Thermal Stability for High Performance 2D Electronics](https://hanwang6.github.io/Lab_Website/iedm_2021.pdf)。Su等人（2023年）的DFT研究进一步揭示了半金属接触的“弱金属化”机制：半金属与TMDC之间的层间距显著大于传统金属，仅引起TMDC的弱金属化，产生“半金属诱导的间隙态”（SMIGSs），这些态从导带底下方延伸，有效降低n型肖特基势垒高度 [来源: Semimetal contacts to monolayer semiconductor: weak metalization as an effective mechanism to Schottky barrier lowering](https://scholar.hit.edu.cn/en/publications/semimetal-contacts-to-monolayer-semiconductor-weak-metalization-a)。

### 金属诱导间隙态（MIGS）与费米能级钉扎

传统金属（如Au、Pt、Ni、Ti）沉积在MoS₂上时，会形成强烈的化学键合，金属的波函数渗入MoS₂的带隙中，形成MIGS。这些间隙态钉扎了费米能级，使得肖特基势垒高度对金属功函数不敏感，导致高接触电阻。Gong等人（2014年）在《Nano Letters》中指出，金属-MoS₂界面的费米能级钉扎机制是独特的，区别于传统的Bardeen钉扎效应，其根源在于金属d轨道与MoS₂轨道的杂化 [来源: The Unusual Mechanism of Partial Fermi Level Pinning at Metal-MoS₂ Interfaces](https://www.semanticscholar.org/paper/The-unusual-mechanism-of-partial-Fermi-level-at-Gong-Colombo/53a66fa2904a0ab4cd22324936861d2f7cc025f3)。

2025年发表在《ACS Nano》上的扫描隧道显微镜/光谱学（STM/S）研究，**首次直接可视化**了MIGS在MoS₂/Au(111)和MoS₂/Bi(111)界面的分布。结果显示：Au接触导致MIGS遍布整个带隙（-1.74 eV至+0.41 eV），产生0.51 eV的肖特基势垒；而Bi接触则将MIGS限制在价带附近（-1.46 eV至-0.57 eV），远离导带底，从而实现欧姆接触 [来源: Direct Visualization of Metal-Induced Gap State Distribution and Valley Band Modulation at Monolayer MoS₂ Interfaces](https://pmc.ncbi.nlm.nih.gov/articles/PMC12120976)。

### 相工程接触

Kappera等人（2014年）在《Nature Materials》上开创性地提出了相工程策略：通过锂插层等方法，将半导体2H相MoS₂局部转化为金属性1T相，在接触区形成1T/2H同质结。该策略将接触电阻降至**200-300 Ω·µm**，且不同金属沉积对器件性能影响有限，表明1T/2H界面控制了载流子注入 [来源: Phase-engineered low-resistance contacts for ultrathin MoS₂ transistors](https://pubmed.ncbi.nlm.nih.gov/25173581)。1T相MoS₂的费米能级穿过简并的dxy轨道，具有真正金属性，其电导率可比2H相高10⁷倍。

### 范德华间隙工程

范德华间隙是影响接触性能的关键结构参数。Khakbaz等人（2022年）的DFT研究表明，金属-MoS₂距离（d）是控制费米能级钉扎的关键参数：在最小能距（~0.25-0.30 nm）时，界面间隙态出现并钉扎费米能级；当d增大至0.8 nm时，间隙态被抑制，肖特基势垒高度可按Schottky-Mott规则调制 [来源: A quantum touch of bismuth](https://communities.springernature.com/posts/a-quantum-touch-of-bismuth)。通过插入h-BN、Al₂O₃、TiO₂等缓冲层，可以有效增加界面距离，抑制MIGS，降低接触电阻。

### 功函数工程与化学掺杂

通过化学掺杂（如苯基紫精BV、碘化钾KI、聚乙烯亚胺PEI）在MoS₂接触区引入高浓度载流子，可以有效降低肖特基势垒宽度，促进隧穿注入。Kiriya等人（2014年）利用BV掺杂实现了~1.2×10¹³ cm⁻²的电子密度，使接触电阻降低超过3倍 [来源: Air-stable surface charge transfer doping of MoS₂ by benzyl viologen](https://pubs.acs.org/doi/10.1021/ja5025974)。掺杂策略的核心在于在接触区实现**简并半导体**状态，使费米能级进入导带，从而消除肖特基势垒。

### 边缘接触

边缘接触通过消除金属与MoS₂之间的范德华间隙，直接形成共价键合，可以有效恢复Schottky-Mott规则。2019年《Advanced Materials》报道的1D边缘接触实现了钉扎因子S=0.975，接近理想值，并实现了p型MoS₂ FETs，空穴迁移率高达432 cm² V⁻¹ s⁻¹ [来源: Fermi-Level Depinned 1D Edge Contacts for MoS₂](https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.201902009)。2025年的最新研究进一步将边缘接触的接触电阻降低至**1.25 kΩ·µm**，肖特基势垒高度仅为32 meV [来源: High-Performance Edge-Contact Monolayer Molybdenum Disulfide Transistors](https://spj.science.org/doi/10.34133/research.0593)。

## 共通物理机制的识别：界面耦合强度作为主控参数

通过对上述各种低接触电阻策略的深入比较，我们可以识别出它们的**共通物理机制**。所有策略本质上都在调控一个核心参数——**界面耦合强度**，即金属与MoS₂之间相互作用的强弱程度。这可以从以下四个维度来理解：

### 维度一：MIGS的抑制

MIGS的产生源于金属波函数向半导体的渗入，其强度和分布范围直接由界面耦合强度决定。所有低接触电阻策略都直接或间接地抑制了MIGS：

- **半金属接触**：利用Bi、Sb在费米能级处极低的DOS，从源头上减少可渗入MoS₂的波函数，是“主动抑制”MIGS的典型案例。
- **范德华间隙工程**：通过插入缓冲层增加物理距离，使金属波函数在到达MoS₂前衰减，是“被动抑制”MIGS，这与DFT研究中“增大d可抑制间隙态”的结论完全一致 [来源: A quantum touch of bismuth](https://communities.springernature.com/posts/a-quantum-touch-of-bismuth)。
- **边缘接触**：直接将金属键合到MoS₂的边缘，避免了顶部接触中的大面积MIGS形成，通过改变接触几何来抑制MIGS。

### 维度二：费米能级的去钉扎

费米能级钉扎（FLP）是导致高接触电阻的直接原因。钉扎的强弱可以用钉扎因子S（S = |dΦSB/dΦM|）来量化，S=1为理想Schottky-Mott极限，S=0为完全钉扎。实验中，传统金属对MoS₂的S值仅约0.1（强钉扎），而边缘接触的S值可达0.975（近乎去钉扎）。所有低电阻策略都致力于提高S值：

- **半金属接触**：通过弱金属化，使肖特基势垒高度由SMIGS、界面偶极子和费米能级移动共同决定，提出了修正的Schottky-Mott规则 [来源: Semimetal contacts to monolayer semiconductor: weak metalization as an effective mechanism to Schottky barrier lowering](https://scholar.hit.edu.cn/en/publications/semimetal-contacts-to-monolayer-semiconductor-weak-metalization-a)。
- **范德华间隙工程**：通过增大物理距离，使界面趋近于Schottky-Mott极限，S值从0.37（紧密接触）提升至0.49（vdW接触）[来源: The Contact Properties of Monolayer and Multilayer MoS₂-Metal van der Waals Interfaces](https://www.mdpi.com/2079-4991/14/13/1075)。
- **相工程**：利用1T相的金属性，在接触区形成金属-金属界面，完全消除了肖特基势垒的困扰。

### 维度三：界面偶极子的调控

界面偶极子源于接触时电荷的重新分布，会改变金属的有效功函数，从而影响势垒高度。Gong等人（2014年）指出，界面偶极子是导致部分钉扎的两个机制之一 [来源: The Unusual Mechanism of Partial Fermi Level Pinning at Metal-MoS₂ Interfaces](https://www.semanticscholar.org/paper/The-unusual-mechanism-of-partial-Fermi-level-at-Gong-Colombo/53a66fa2904a0ab4cd22324936861d2f7cc025f3)。2026年发表在《Physical Review B》上的“统一键合偶极子理论”进一步揭示了界面偶极子的微观起源：半导体表面悬挂键与金属轨道之间的局域键合，即使在单层金属存在时也足以产生强钉扎 [来源: A unified bond dipole theory for metal-semiconductor interfaces](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.113.045301)。不同策略都在减少这种由悬挂键-金属轨道键合引起的偶极子：

- **半金属接触**：弱轨道杂化减少界面偶极子。
- **范德华接触**：弱范德华力减少键合强度。
- **相工程**：1T相MoS₂本身具有金属性，其悬挂键状态与2H相不同。

### 维度四：接触区的金属化/简并化

无论是通过半金属诱导的弱金属化、相工程实现的1T相金属化，还是化学掺杂实现的简并半导体，所有低接触电阻策略都在接触区创造了一个“导电通道”，使得载流子无需跨越肖特基势垒即可注入。这实际上是**接触电阻问题的本质**——将金属-半导体接触转化为金属-金属或金属-简并半导体接触。

- **半金属接触**：MoS₂在接触区发生自发简并掺杂，费米能级进入导带。
- **相工程**：1T相MoS₂直接提供金属性通道。
- **化学掺杂**：高浓度掺杂使肖特基势垒变薄，促进场发射隧穿。

## 统一理论框架：界面耦合强度模型

基于上述分析，我们提出一个以**界面耦合强度（Γ）**为核心参数的统一理论框架。该框架的核心理念是：所有降低接触电阻的策略，都是通过降低界面耦合强度Γ来实现的，而Γ由以下四个因素共同决定：

1. **金属费米能级处的态密度（DOS(EF)）**：DOS越低，可渗入半导体的波函数越少，Γ越小。这是半金属接触成功的根本原因。
2. **界面物理分离距离（d）**：距离越大，波函数衰减越强，Γ越小。这是范德华间隙工程的理论基础。
3. **轨道杂化强度（H）**：金属d轨道与MoS₂轨道的杂化越强，Γ越大。这是选择金属种类（如Sc、Ti强杂化 vs. Au弱杂化）的依据。
4. **界面悬挂键密度（DDB）**：悬挂键越多，可与金属键合的位点越多，Γ越大。这是2026年统一键合偶极子理论的核心发现 [来源: A unified bond dipole theory for metal-semiconductor interfaces](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.113.045301)。

所有低接触电阻策略都可以在这个框架下得到统一解释：

| 策略 | 降低Γ的主要途径 | 具体机制 |
|------|----------------|---------|
| 半金属接触（Bi, Sb） | 降低DOS(EF) | 低态密度抑制MIGS |
| 范德华间隙工程 | 增大d | 缓冲层增加物理距离 |
| 相工程 | 改变H和DDB | 1T相与2H相具有不同的轨道杂化特性 |
| 化学掺杂 | 改变接触区电子态 | 简并掺杂使接触区金属化 |
| 边缘接触 | 消除界面 | 改变接触几何，避免大面积界面 |
| 纯金接触（UHV） | 降低H和DDB | 超净表面减少悬挂键和杂质 |

## 基于统一框架的未来研究方向

基于上述统一理论框架，我们提出以下未来研究方向，这些方向应重点通过**原始实验和理论论文**（而非综述文章）来推进：

### 研究方向一：新型半金属材料的系统探索

当前研究主要集中在Bi和Sb两种半金属上。Bi的接触电阻虽低，但热稳定性差（熔点271.5°C）；Sb的热稳定性好，但接触电阻（42 Ω·µm）仍有优化空间。未来的研究应系统探索其他半金属或拓扑绝缘体材料，如：

- **Bi-Sb合金**：已有研究显示，拓扑绝缘体Bi-Sb合金（7-22% Sb）接触可增强开态电流，并可能通过组分调控来优化势垒高度与熔点的权衡 [来源: Topological Insulator Bismuth-Antimony Alloy Contact for Two-Dimensional Semiconductor Based Electronics](https://iopscience.iop.org/article/10.1149/MA2024-02352472mtgabs)。
- **二维金属**：如H-NbS₂、N掺杂石墨烯（C₂₀N）等，其二维特性可能提供更弱的界面耦合和更优的能级对齐 [来源: Van der Waals metal-semiconductor junction: Weak Fermi level pinning enables effective tuning of Schottky barrier](https://advances.sciencemag.org/content/2/9/e1600069)。
- **MXene材料**：如TiCT，其可调功函数（4.33-5.32 eV）和范德华接触特性，已实现钉扎因子S=0.87 [来源: MXene Contact Engineering for Suppressing Fermi Level Pinning in MoS₂ Transistors](https://onlinelibrary.wiley.com/doi/10.1002/adfm.202203308)。

**关键预测**：最优半金属应具有极低的DOS(EF)（以抑制MIGS），同时功函数与MoS₂导带对齐（以实现简并掺杂），并具有高熔点（以保证热稳定性）。Bi-Sb合金体系可能是满足这些条件的候选体系。

### 研究方向二：界面耦合强度的精确调控

统一框架提出了四个可控参数（DOS(EF)、d、H、DDB），未来的研究需要发展精确调控这些参数的方法：

- **插层工程**：在金属与MoS₂之间插入单原子层（如石墨烯、h-BN），系统研究插入层种类和厚度对界面耦合强度的影响。DFT研究已预测，石墨烯插入可使Mg、In、Sc、Ti等金属实现负SBH（欧姆接触）[来源: First-principles study of graphene-inserted MoS₂/metal contacts](https://www.nature.com/articles/s41598-024-52567-8)。
- **界面应力调控**：比较研究显示，金属-半导体界面对应力调制比半金属-半导体界面更敏感，应力对界面偶极子（ΔV）的影响在M-S界面最为显著 [来源: Comparative study of the micro-mechanism of charge redistribution at metal–semiconductor and semimetal–semiconductor interfaces](https://www.sciencedirect.com/science/article/abs/pii/S0169433223007134)。这为通过应力工程调控接触性能提供了新思路。
- **悬挂键钝化**：基于统一键合偶极子理论，通过钝化MoS₂表面的悬挂键，可以降低界面偶极子，减弱FLP。这可以通过氢化、氟化或其他表面处理来实现。

**关键实验测试**：设计一系列具有不同d值（通过不同厚度缓冲层实现）的金属-MoS₂接触，系统测量接触电阻与d的关系，验证Γ∝exp(-d/λ)的指数衰减关系（其中λ为MIGS衰减长度）。STM/S研究已测得Bi的MIGS衰减长度为1.1-2.5 nm，Au为0.5-1.5 nm [来源: Direct Visualization of Metal-Induced Gap State Distribution and Valley Band Modulation at Monolayer MoS₂ Interfaces](https://pmc.ncbi.nlm.nih.gov/articles/PMC12120976)，这为定量验证提供了基础。

### 研究方向三：相工程与半金属策略的融合

相工程（1T/1T'相）和半金属接触是目前最成功的两种策略，但二者的机制似乎不同。未来的研究应探索将二者融合：

- **半金属诱导的相变**：研究Bi或Sb接触是否能在接触区诱导局部的2H→1T/1T'相变，将两种机制的优势结合起来。
- **1T'相MoS₂作为接触材料**：1T'相MoS₂是半金属性的，其本身就可以作为半金属接触材料，无需额外沉积金属。这一方向有望实现“无金属”的二维半导体器件。
- **激光/等离子体辅助的局部相变**：已有研究通过激光照射（532 nm）在MoTe₂中实现2H→1T'相变，接触电阻降低22.5% [来源: MoTe₂ Field-Effect Transistors with Low Contact Resistance through Phase Tuning by Laser Irradiation](https://www.mdpi.com/2079-4991/11/11/2805)。类似方法应用于MoS₂，结合半金属电极，可能实现更低的接触电阻。

**关键预测**：在1T'相MoS₂上沉积半金属Bi/Sb，应能实现比在2H相上更低的接触电阻，因为1T'相本身具有半金属性，且两侧均为半金属，界面耦合强度最小。

### 研究方向四：混合接触几何的优化

2026年《Physical Review Applied》的理论研究比较了边缘、顶部和混合接触的接触电阻，发现混合接触（结合顶部和边缘）在接触长度小于10 nm时性能最优，可接近量子极限 [来源: Theoretical Comparison of Contact Resistance for Edge, Top, and Hybrid Contacts to MoS₂ Monolayers](https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.25.044028)。这一发现为未来器件缩放提供了重要方向。

**关键实验测试**：使用半金属（如Sb）同时实现顶部和边缘接触，系统研究混合接触几何对接触电阻的影响，验证理论预测。

### 研究方向五：理论计算与实验验证的闭环

统一框架的建立和验证需要理论计算与实验的紧密结合：

- **第一性原理计算**：利用DFT+NEGF方法，系统计算不同金属（包括半金属）与MoS₂界面的Γ值，建立Γ与接触电阻的定量关系。Su等人（2023年）提出的修正Schottky-Mott规则（考虑SMIGS、界面偶极子和费米能级移动）为这一方向提供了理论基础 [来源: Semimetal contacts to monolayer semiconductor: weak metalization as an effective mechanism to Schottky barrier lowering](https://scholar.hit.edu.cn/en/publications/semimetal-contacts-to-monolayer-semiconductor-weak-metalization-a)。
- **直接成像与谱学**：STM/S、准粒子干涉（QPI）成像等技术可直接可视化MIGS的分布，是验证理论预测的关键工具。2025年的STM/S研究已展示了这一能力 [来源: Direct Visualization of Metal-Induced Gap State Distribution and Valley Band Modulation at Monolayer MoS₂ Interfaces](https://pmc.ncbi.nlm.nih.gov/articles/PMC12120976)。
- **统计性与系统性实验**：制备大量器件的统计性研究，系统变化金属种类、处理条件、MoS₂层数等参数，测量接触电阻、SBH、钉扎因子等，与理论预测进行对比。Nanotechnology（2022）对CVD-MoS₂的统计性研究已展示了这种方法的价值 [来源: Reduced Schottky barrier heights and Fermi level pinning in CVD-grown MoS₂ FETs](https://iopscience.iop.org/article/10.1088/1361-6528/ac4e9b)。

## 结论

本研究通过对二维半导体（特别是MoS₂）低接触电阻策略的系统综述，识别出所有成功策略的共通物理机制：**降低界面耦合强度**。这可以通过四种途径实现：（1）降低金属费米能级处的态密度（半金属接触）；（2）增大界面物理距离（范德华间隙工程）；（3）改变轨道杂化强度（相工程）；（4）减少界面悬挂键密度（边缘接触、超净表面处理）。所有策略的最终目标都是在接触区创造金属-金属或金属-简并半导体的导电通道，同时最小化对半导体本征性能的破坏。

基于此，我们提出了以界面耦合强度（Γ）为核心参数的统一理论框架，该框架能够解释大多数已知的低接触电阻方法。该框架预测，最优的接触策略应同时实现以下几个条件：极低的金属DOS(EF)以抑制MIGS、合适的功函数以实现能级对齐、足够的物理分离以弱化耦合但不过度增加隧穿电阻、以及清洁的界面以减少悬挂键和杂质。

未来的研究方向应聚焦于：（1）系统探索新型半金属材料（如Bi-Sb合金、二维金属、MXene）；（2）发展精确调控界面耦合强度的方法（插层工程、应力调控、悬挂键钝化）；（3）融合相工程与半金属策略；（4）优化混合接触几何；（5）建立理论计算与实验验证的闭环。这些方向将推动二维半导体接触电阻从“经验性优化”走向“按设计定制”，为二维半导体器件的实际应用奠定基础。

---

### Sources

[1] Ultralow contact resistance between semimetal and monolayer semiconductors: http://ciqm.harvard.edu/uploads/2/3/3/4/23349210/shensu2021.pdf

[2] Ultralow contact resistance between semimetal and monolayer semiconductors (KAUST Repository): https://repository.kaust.edu.sa/bitstreams/f00e55c2-160a-467c-b7c5-5a3c17804f17/download

[3] Antimony Semimetal Contact with Enhanced Thermal Stability for High Performance 2D Electronics: https://hanwang6.github.io/Lab_Website/iedm_2021.pdf

[4] Semimetal contacts to monolayer semiconductor: weak metalization as an effective mechanism to Schottky barrier lowering: https://scholar.hit.edu.cn/en/publications/semimetal-contacts-to-monolayer-semiconductor-weak-metalization-a

[5] Direct Visualization of Metal-Induced Gap State Distribution and Valley Band Modulation at Monolayer MoS₂ Interfaces: https://pmc.ncbi.nlm.nih.gov/articles/PMC12120976

[6] The Unusual Mechanism of Partial Fermi Level Pinning at Metal-MoS₂ Interfaces: https://www.semanticscholar.org/paper/The-unusual-mechanism-of-partial-Fermi-level-at-Gong-Colombo/53a66fa2904a0ab4cd22324936861d2f7cc025f3

[7] Phase-engineered low-resistance contacts for ultrathin MoS₂ transistors: https://pubmed.ncbi.nlm.nih.gov/25173581

[8] A quantum touch of bismuth: https://communities.springernature.com/posts/a-quantum-touch-of-bismuth

[9] A unified bond dipole theory for metal-semiconductor interfaces: https://journals.aps.org/prb/abstract/10.1103/PhysRevB.113.045301

[10] Comparative study of the micro-mechanism of charge redistribution at metal–semiconductor and semimetal–semiconductor interfaces: https://www.sciencedirect.com/science/article/abs/pii/S0169433223007134

[11] The Contact Properties of Monolayer and Multilayer MoS₂-Metal van der Waals Interfaces: https://www.mdpi.com/2079-4991/14/13/1075

[12] Van der Waals metal-semiconductor junction: Weak Fermi level pinning enables effective tuning of Schottky barrier: https://advances.sciencemag.org/content/2/9/e1600069

[13] First-principles study of graphene-inserted MoS₂/metal contacts: https://www.nature.com/articles/s41598-024-52567-8

[14] High-Performance Edge-Contact Monolayer Molybdenum Disulfide Transistors: https://spj.science.org/doi/10.34133/research.0593

[15] MoTe₂ Field-Effect Transistors with Low Contact Resistance through Phase Tuning by Laser Irradiation: https://www.mdpi.com/2079-4991/11/11/2805

[16] Topological Insulator Bismuth-Antimony Alloy Contact for Two-Dimensional Semiconductor Based Electronics: https://iopscience.iop.org/article/10.1149/MA2024-02352472mtgabs

[17] MXene Contact Engineering for Suppressing Fermi Level Pinning in MoS₂ Transistors: https://onlinelibrary.wiley.com/doi/10.1002/adfm.202203308

[18] Theoretical Comparison of Contact Resistance for Edge, Top, and Hybrid Contacts to MoS₂ Monolayers: https://journals.aps.org/prapplied/abstract/10.1103/PhysRevApplied.25.044028

[19] Reduced Schottky barrier heights and Fermi level pinning in CVD-grown MoS₂ FETs: https://iopscience.iop.org/article/10.1088/1361-6528/ac4e9b

[20] Study of gold and bismuth electrical contacts to a MoS₂ monolayer: https://www.sciencedirect.com/science/article/abs/pii/S0038109824004010

[21] Low contact resistance on monolayer MoS₂ field-effect transistors with CMOS-compatible metal contacts: https://par.nsf.gov/servlets/purl/10531719

[22] Fermi Level Pinning Dependent 2D Semiconductor Devices: Challenges and Solutions: https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202108425

[23] Uncovering the Different Components of Contact Resistance to Atomically Thin Semiconductors: https://poplab.stanford.edu/pdfs/BerGrady-ComponentsContactResistance-aem23.pdf

[24] Air-stable surface charge transfer doping of MoS₂ by benzyl viologen: https://pubs.acs.org/doi/10.1021/ja5025974

[25] Bismuth Confinement: A Strategy for Low Resistance and Good Thermal Endurance of Integrated Contacts to MoS₂: https://pmc.ncbi.nlm.nih.gov/articles/PMC13045353

[26] Contact engineering for temperature stability improvement of Bi-contacted MoS₂ field effect transistors: https://link.springer.com/article/10.1007/s11432-023-3942-2

[27] First-principles study of van der Waals interactions and lattice mismatch at MoS₂/metal interfaces: https://ris.utwente.nl/ws/files/6998823/PhysRevB.93.085304.pdf

[28] A Computational Study of Metal-Contacts to Beyond-Graphene 2D Semiconductor Materials: https://djena.engineering.cornell.edu/papers/2012/iedm12_2d_contacts.pdf

[29] Fermi-Level Pinning Mechanism in MoS₂ Field-Effect Transistors: https://www.mdpi.com/2076-8517/10/8/2754

[30] Improved Contacts to MoS₂ Transistors by Ultra-High Vacuum Metal Deposition: https://poplab.stanford.edu/pdfs/English-MoS2contactsUHV-nl16.pdf
