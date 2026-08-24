# 先进制程芯片金属薄膜沉积设备全面调研报告（2023–2026）

## 一、概述

在当今先进制程（7nm及以下，含5nm、3nm、2nm）芯片制造中，金属薄膜沉积已形成以**物理气相沉积（PVD）、化学气相沉积（CVD）、原子层沉积（ALD）**三大类设备为核心的生产体系；而**电子束蒸发沉积（e-beam evaporation）**和**分子束外延（MBE）**在主流逻辑芯片量产产线中几乎不被采用，主要局限于研发（R&D）、化合物半导体、量子器件及特种光学/磁性薄膜等细分领域。这一格局由台阶覆盖能力、薄膜纯度、热预算、沉积速率与成本效益共同决定。

先进逻辑芯片的金属化层通常包含10–15层以上的互连结构，每一层都要经历"阻挡层/衬垫沉积 → 种子层沉积 → 电镀填充 → CMP平坦化 → 盖帽层沉积"的循环 [1]。在这一体系中，PVD负责铜种子层和部分阻挡层/衬垫层，CVD负责钨/钴/钼的填充和钴/钌衬垫，ALD负责超薄共形阻挡层、成核层和新兴金属（钌、钼）沉积。以下分别详述。

---

## 二、五类设备在先进制程中沉积的具体金属薄膜及应用场景

### 2.1 物理气相沉积（PVD，磁控溅射）

PVD（主要是磁控溅射）是先进制程中应用最广泛的金属沉积设备之一。行业资料明确指出，PVD用于沉积"半导体制造中的每一层主要金属化层，包括BEOL大马士革互连的铜种子层、钛/氮化钛阻挡层、钽/氮化钽扩散阻挡层、钨接触衬垫、铝焊盘、先进节点钴接触，以及5nm以下新兴的钌/钼替代材料" [1]。溅射靶材要求纯度达到5N至7N（99.999%–99.99999%），并严格控制晶粒结构、密度和尺寸公差 [2]。

具体而言，PVD在先进制程中沉积的金属薄膜包括：

| 薄膜材料 | 应用场景 | 说明 |
|---|---|---|
| **Ta / TaN** | 铜互连扩散阻挡层 | 自1990年代末起成为铜互连标准阻挡层材料，通过PVD溅射沉积 [5]；在7nm以下逐步被ALD TaN取代，但PVD Ta仍用于部分场景 |
| **Cu 种子层** | 铜互连电镀种子层 | 6N（99.9999%）超高纯铜靶材，用于大马士革铜互连的种子层，是PVD在先进节点保留的核心应用 [3][4] |
| **Ti / TiN** | 钨接触的粘附层/阻挡层、栅极金属、硬掩膜、UBM、TSV | Ti靶材纯度4N5–5N5；TiN也可通过反应溅射（钛在氮气等离子体中）沉积 [3][4] |
| **Co** | 接触层、硅化物、栅极金属 | 高纯钴（5N）靶材用于先进节点钴接触；Endura平台上有集成PVD钴方案 [3][4][6] |
| **W** | 栅极电极、接触层 | 5N钨靶材，用于栅极电极等 [3] |
| **Al** | 焊盘/UBM、成熟节点互连 | 铝及Al-Cu合金溅射仍是焊盘和晶圆级封装UBM的标准工艺 [6] |
| **Ru / Mo** | 新兴互连金属（2nm及以下） | GAA晶体管向2nm节点迁移催生新的钌/钼溅射靶材需求 [7] |

Applied Materials的**Endura平台**是PVD设备的行业标杆，被描述为"半导体设备行业历史上最成功的金属沉积系统"，全球几乎所有先进芯片制造商都在使用，截至2000年已出货2,000台 [8][9]。其产品线覆盖：Endura CuBS（铜阻挡层/种子层系统）、Endura Cirrus HTX（用于10nm以下节点的TiN硬掩膜，可实现紧密线宽控制和通孔套刻对准）、Endura Amber（用于1x nm节点的铜回流填充）、Endura Ioniq W（纯钨接触金属化）等 [6][10][11]。

**关键历史演变**：在28nm平面节点，PVD足以覆盖所有BEOL阻挡层（Ta/TaN）和铜种子层；但到14nm FinFET和7nm FinFET节点，极高深宽比通孔使PVD无法沉积连续扩散阻挡层（阴影效应导致台阶覆盖不足），行业转向混合集成——用ALD沉积超薄共形阻挡层（如ALD TaN），同时保留专用离子化PVD（iPVD）沉积需要高纯度和良好润湿性的铜种子层 [12]。

**2021年Applied Materials发布的Endura Copper Barrier Seed系统**是PVD+ALD协同的典型：它利用选择性ALD仅将钽涂覆在互连沟槽侧壁（而非底部），消除了通孔底部的高电阻钽阻挡层，使3nm芯片铜线电阻降低50%，并支持将互连线宽缩小至15nm [13]。

### 2.2 化学气相沉积（CVD）

CVD在先进制程中主要用于**间隙填充**和**衬垫/盖帽层**沉积，核心应用包括：

**（1）钨（W）接触/通孔填充**

钨是MOL（中段制程）接触插塞的标准材料，通过WF₆前驱体沉积：先用硅烷（SiH₄）还原进行成核，再用氢气（H₂）还原进行体填充 [14]。Lam Research的**ALTUS系列**是钨CVD/ALD填充的行业标准设备，采用"脉冲成核层（PNL）ALD + 原位CVD体填充"技术，解决传统CVD钨填充因阻挡层悬突导致的空洞问题，应用于接触插塞、通孔填充、3D NAND字线等 [15]。

然而，到7nm节点，钨接触遇到严重瓶颈：传统的TiN阻挡层和钨成核层占据的接触体积比例过大——在7nm芯片中，接触孔直径仅约20nm，而包覆层（衬垫+阻挡层）厚度未按比例缩小，导致钨仅占接触体积的25% [16][17]。为此，Applied Materials推出了**Endura Volta Selective W CVD**系统，通过选择性沉积实现自下而上的钨填充，完全消除衬垫/阻挡层和成核层，使接触电阻降低40%，该设备于2020年发布并已在高量产（HVM）中使用 [16][18]。

**（2）钴（Co）接触填充、衬垫与盖帽**

钴在10nm/7nm/5nm节点大规模取代钨作为接触金属，同时作为铜互连的衬垫和盖帽层。Applied Materials的**Endura Volta Cobalt CVD**系统被描述为"15年来铜互连领域最大的材料变革"，实现两个关键工艺步骤 [19][20]：

- **共形钴衬垫（CVD）**：使铜种子层更薄、更连续，实现无空洞铜填充；
- **选择性钴盖帽（CVD）**：在铜CMP后沉积，将铜原子固定在表面并增强与后续介电层的粘附，使电迁移寿命提高一个数量级 [19]。

钴接触的优势在于：钴可以使用更薄的阻挡层、不需要成核层，在5nm节点提供6nm的填充体积（对比钨），且可通过退火消除接缝 [20][21]。行业数据显示，用钴取代钨接触可使接触线电阻改善约60%；TSMC已采用钴-钨混合金属化方案，通孔链电阻降低15–25% [22]。

**（3）钌（Ru）衬垫**

东京电子（TEL）与Novellus（现属Lam Research）联合开发了"离子化PVD TaN或Ti阻挡层 + 超薄CVD Ru衬垫（≤2nm）+ 铜湿法种子层（DirectSeed）+ 电化学铜沉积"的集成方案，用于2x nm及以下节点，CVD Ru衬垫在TEL的Trias Tandem系统中沉积，具有优异的共形性和最低的耗材成本 [23]。

**（4）钼（Mo）填充（新兴）**

Lam Research于2025年2月发布**ALTUS Halo**——全球首款用于钼沉积的原子层沉积设备，支持钼在先进逻辑、3D NAND（1,000层）和DRAM（4F²）中的高量产应用 [24]。该设备已被美光（Micron）在其先进NAND产品中采用，并已进入所有主要芯片制造商的认证和爬坡阶段 [25][26]。

### 2.3 原子层沉积（ALD）

ALD凭借其自限制表面化学反应，是唯一能够在极高深宽比（>60:1，当前3D NAND中甚至超过100:1）结构内实现100%共形覆盖的沉积方法 [27]。在先进制程中，ALD沉积的金属薄膜包括：

**（1）TaN阻挡层（铜互连）**

TSMC早在2002年就发表了90nm铜双大马士革工艺中采用ALD TaN阻挡层的研究，证明ALD TaN相比传统PVD TaN提供共形台阶覆盖和约10Å的厚度控制，且电迁移、应力迁移和偏压温度测试可靠性更优 [28]。Applied Materials的Endura iCuB/S系统（2002年发布，面向65nm节点）率先将ALD TaN集成到铜阻挡层/种子层流程中 [29]。到3nm节点，Applied Materials 2021年的Endura Copper Barrier Seed系统进一步采用选择性ALD Ta涂覆沟槽侧壁，消除了通孔底部的高电阻钽层 [13]。

东京电子的专利技术展示了ALD TaN/TaAlN阻挡层与CVD Ru衬垫的集成方案：在20nm宽、200nm深的沟槽中实现无空洞铜填充，而PVD TaN阻挡层在25nm线宽即失效 [30]。

**（2）TiN（接触阻挡层、DRAM电容电极、字线阻挡层、金属栅极）**

TEL的**Triase+ EX-II TiN**系列采用ASFD（Advanced Sequential Flow Deposition）技术，沉积高质量TiN薄膜，用于接触阻挡层、电容电极、字线阻挡层和金属栅极，可实现<10Å的连续薄膜和1σ<1%的厚度均匀性 [31][32]。其高温版本（TiN Plus HT）在DRAM埋入式字线和第二代3D NAND中实现更低电阻和更低杂质含量的TiN [33]。TEL在该领域拥有约40%的全球CVD/ASFD市场份额 [34]。

**（3）W成核层（PNL-ALD）**

Lam Research的ALTUS系统采用PNL（脉冲成核层）ALD工艺沉积钨成核层，再进行CVD体填充。2004年的ALTUS DirectFill系统用WN/W集成方案取代了传统的Ti/TiN/W多设备流程，使接触电阻降低50%，且所有工艺温度低于400°C [35]。

**（4）Ru（钌）衬垫与填充**

Lam Research的专利（US10731250B2）描述了用于10nm以下节点的钌ALD沉积工艺：先在还原条件下通过ALD沉积1–2nm的Ru衬垫层，再通过氧化反应进行Ru填充。钌具有较短的电子平均自由程，在10nm以下尺寸电阻率优于铜，且无需扩散阻挡层 [36]。

**（5）Co（钴）成核与填充**

钴ALD可实现>98%的台阶覆盖（5:1深宽比鳍结构），在250–350°C通过TaN/TiN预处理实现成核；Applied Materials的专利描述了通过钌掺杂抑制钴团聚、实现无空洞间隙填充的方法 [22][37]。

**（6）Mo（钼）填充（2025年起量产）**

Lam Research的ALTUS Halo是钼ALD的开创性设备。钼相比钨在纳米尺度具有更低电阻率，且无需粘附层或阻挡层，简化工艺流程并提高良率 [24][25][38]。

此外，ASM International是ALD设备的主要供应商，其**XP4 Pulsar**反应器用于沉积高k栅介质（HfO₂、硅酸铪）和金属栅功函数调节层，帮助实现了45nm节点向铪基高k栅介质的转换；ASM的Tenza ALD技术可填充深宽比大于100:1的结构，已被多个3D NAND应用采用 [39][40][41]。

### 2.4 电子束蒸发沉积（E-beam Evaporation）

**在先进制程（7nm及以下）主流量产产线中，电子束蒸发不作为金属互连/接触薄膜的沉积设备使用。** 其根本原因是电子束蒸发是典型的"视线方向"（line-of-sight）沉积工艺，蒸气沿直线传播，在先进节点的高深宽比通孔和沟槽中会产生严重的阴影效应，导致极差的台阶覆盖能力 [42][43]。行业对比资料明确列出：蒸发提供差的台阶覆盖（定向通量），溅射提供好的台阶覆盖（全向通量）[43]。

电子束蒸发在半导体领域的实际应用集中在：
- **lift-off剥离工艺**：其良好的方向性使侧壁不被覆盖，是MEMS和微电子lift-off图案化的标准方法 [44][45]；
- **光学镀膜**：抗反射膜、反射镜、带通滤波器（TiO₂/SiO₂交替层）[44][46]；
- **贵金属接触、多层膜、高纯厚膜、难熔金属** [43]；
- **研究实验室和原型器件** [44]。

电子束蒸发的优势在于高沉积速率（化合物可达~100nm/s，金属可达~1µm/s，比溅射高2–3个数量级）、超高纯度（自坩埚效应避免容器污染）和低衬底加热 [46][47]。但其劣势同样明显：均匀性差（需要行星夹具或掩膜）、薄膜密度较低、二次电子可能电离残留气体造成污染、高能电子可能导致化合物分解、灯丝寿命短、厚度控制不如溅射精确 [46][48]。

### 2.5 分子束外延（MBE）

**MBE同样不用于先进制程逻辑芯片的金属薄膜量产。** MBE是一种在超高真空（10⁻⁸–10⁻¹² Torr）环境下、以极低速率（通常<3,000 nm/小时）逐原子层外延生长单晶薄膜的技术，主要用于III-V族化合物半导体、二维材料、量子结构等 [49][50]。

MBE市场数据显示其研发属性：
- 2025年全球MBE市场约**8.4亿美元**，预计2034年达17.2亿美元（CAGR 8.3%）[51]；
- 终端用户中**研究机构占52.3%**，工业制造仅占35.1% [51]；
- MBE每批仅处理**1–4片晶圆**，而MOCVD可处理50–100片以上 [51]；
- 单腔成本高达150万–500万美元，集群工具超过1,500万美元 [51]。

MBE的主要应用领域为：激光二极管、LED、光电探测器、HEMT晶体管、红外探测器、量子计算器件等 [49][52]。量子计算是增长最快的细分市场（2025年占15.4%，CAGR 13.8%）[51]。在先进制程逻辑芯片产线中，MBE不用于任何金属互连/接触层的量产沉积。

---

## 三、设备选择的技术与经济动因

### 3.1 台阶覆盖与共形性：决定性的技术因素

先进节点（7nm及以下）的金属化面临极高深宽比结构（M1/M2金属间距将达21nm，通孔临界尺寸仅12–14nm [53]），台阶覆盖能力成为设备选择的首要因素：

- **PVD（溅射）**本质上是视线方向沉积，在深沟槽中典型台阶覆盖仅20–30% [54]。在28nm节点尚可接受，但14nm/7nm后无法用于连续阻挡层，仅保留离子化PVD（iPVD）用于铜种子层——iPVD通过二次RF线圈高度电离溅射金属通量，结合衬底偏压实现方向性控制，在10:1深宽比沟槽中可实现约20%的底部覆盖 [12][55]。
- **CVD**依靠气相化学反应实现80–90%的共形性，是钨/钴间隙填充的理想选择 [54]。
- **ALD**通过自限制表面反应实现近100%的共形覆盖，是唯一能在深宽比>60:1（甚至300:1）结构中均匀沉积的方法 [27][56]。对于阻挡层，ALD可在10Å厚度级别实现精确控制 [28]。

### 3.2 薄膜质量（纯度、密度、应力）

- **PVD溅射**：薄膜致密、附着力好（高能原子到达）、可精确保持合金成分（如CuMn、NiPt），适用于需要高纯度种子层和阻挡层的场景 [43][57]。但PVD TiN薄膜晶粒较小、（111）晶面占优，可能引起更高的界面氧化和缺陷密度 [12]。
- **CVD**：可沉积高纯度、低缺陷密度的薄膜；但钨CVD存在氟杂质问题（β-W相导致电阻率升高）和高张应力（可导致晶圆翘曲）[14]。
- **ALD**：薄膜无针孔，允许更薄的薄膜达到与厚膜相同的性能；但金属ALD的杂质（C、O、N）可能提高电阻率，需要通过还原剂优化和退火处理 [36][58]。
- **电子束蒸发**：薄膜密度通常低于溅射膜，附着力较差，可能需要额外的粘附层 [42][43]。
- **MBE**：由于超高真空和无载气，可达到最高的薄膜纯度 [50]。

### 3.3 工艺温度与热预算兼容性

BEOL工艺必须在**400–450°C以下**进行，以保护铜/低k互连和掺杂分布 [59]：

- **CVD**通常需要400–900°C的高温，是其主要限制 [60]。但钨CVD和钴CVD均可在400°C以下运行（如ALTUS DirectFill所有工艺温度低于400°C [35]；钴CVD在300–450°C热工艺、200–350°C PECVD [22]）。
- **ALD**的优势在于低温沉积：热ALD可在室温至350°C运行，等离子体增强ALD（PEALD）可在50–100°C运行，满足低热预算要求 [40][61]。TEL的EX-II TiN Plus HT通过高温工艺（但仍受限于整体热预算）实现更低电阻和更低杂质 [33]。
- **PVD溅射**通常在低温下运行，衬底加热可控（200–370°C），适合热预算敏感工艺 [22]。
- 低k介质（如Black Diamond™，k=2.5–2.7）的玻璃化转变温度高于450°C，所有沉积工艺必须与之兼容 [62]。

### 3.4 沉积速率与生产率

- **PVD溅射**：沉积速率高（钴溅射可达1.92–3.37 nm/s [22]），适合厚膜和高产量需求。
- **CVD**：钨CVD和钴CVD具有高填充速率（钴CVD 5–20 nm/min [22]），是间隙填充的首选。
- **ALD**：速率最慢（0.5–2 Å/周期，即1–10 nm/min），是其主要瓶颈 [63]。但ALD仅需沉积极薄层（阻挡层1–5nm、成核层<2nm），且其厚度精确性避免了过沉积和返工。ASM通过高速ALD工艺将HfO₂吞吐量提高一倍 [64]；混合前驱体ALD可实现2–5倍速率提升 [63]。
- **电子束蒸发**：沉积速率极高（100nm/s–1µm/s）[47]，但无法满足先进节点的共形性要求。
- **MBE**：速率极低（<3,000 nm/h），仅适用于需要原子级精确控制的外延生长 [50]。

### 3.5 成本效益

- **PVD**：设备成本相对低、运行成本低（无需昂贵前驱体），是铜种子层和阻挡层成本效益最高的方案 [57]。
- **CVD**：前驱体成本较高（WF₆、钴有机金属前驱体），但高沉积速率降低了单次工艺成本；选择性CVD（如选择性钨）消除了阻挡层/成核层步骤，显著降低总体拥有成本 [16][18]。
- **ALD**：设备投资高（混合前驱体ALD系统需25–40%更高的资本投入），但工艺步骤简化和良率提升可在18–24个月内实现盈亏平衡 [63]。ALD设备市场2025年估值39.8亿美元，预计2034年达95.5亿美元（CAGR 10.2%），超过85%的领先逻辑产能扩张将在2030年前采用ALD [65]。
- 溅射靶材市场2025年估值48亿美元，预计2034年达92亿美元（CAGR 7.5%），纯金属靶材占44.2% [7]。

### 3.6 与现有工艺步骤的兼容性

先进制程金属化是一个高度集成的真空系统流程：例如Applied Materials的Endura平台在同一真空环境下集成预清洁、ALD阻挡层、PVD种子层、CVD衬垫和铜回流工艺，避免界面氧化 [13][19]。这种集成能力是设备选择的另一关键因素：

- PVD和CVD在Endura平台上集成（如Endura Volta Co CVD与PVD CuBS同平台）[19]；
- ALD与PVD/CVD在单一集群工具中集成（如Endura CBS、TEL Trias-Tandem）[13][30]；
- 选择性沉积（ASD）需要在真空密封环境中完成多步表面处理（如Endura Volta Selective W）[18]。

---

## 四、电子束蒸发与MBE在量产中的实际应用程度：研发 vs 大规模量产

### 4.1 电子束蒸发：几乎不用于先进制程量产

**结论：电子束蒸发在先进制程芯片量产中的实际应用程度极低，几乎完全被排除在HVM产线之外，主要用于研发、特种光学镀膜和lift-off工艺。**

原因总结：

1. **台阶覆盖能力不足**：先进节点（7nm及以下）的通孔和沟槽深宽比通常超过5:1，甚至达到10:1以上。电子束蒸发的视线方向沉积导致侧壁覆盖极差，无法形成连续的阻挡层和种子层 [42][43]。
2. **均匀性差**：蒸发源的扩展角分布导致大面积均匀性需要行星夹具或掩膜补偿，300mm晶圆上难以满足<2%的均匀性要求 [42]。
3. **薄膜质量限制**：蒸发膜密度低于溅射膜，附着力差，易形成柱状晶结构 [42][43]。
4. **合金成分控制困难**：不同材料蒸气压不同导致合金成分偏离目标 [43]。
5. **污染风险**：二次电子电离残留气体、高能电子导致化合物分解 [46][48]。

行业对比资料明确建议：**lift-off图案化、贵金属接触、多层膜、高纯厚膜、光学镀膜、难熔金属**选电子束蒸发；**合金膜、粘附/阻挡层、共形镀膜、互连金属化、大直径晶圆**选溅射 [43]。先进制程互连金属化恰恰属于后者。

### 4.2 分子束外延（MBE）：研究机构主导，不用于量产金属互连

**结论：MBE在先进制程芯片量产中的应用程度同样极低，其角色高度集中于研发、化合物半导体和量子器件领域。**

原因总结：

1. **极低沉积速率**：<3,000 nm/h，无法满足量产产线的吞吐量需求 [50]。
2. **超高真空要求**：10⁻⁸–10⁻¹² Torr，设备复杂、维护成本高 [50]。
3. **极低产能**：每批仅1–4片晶圆，而MOCVD可处理50–100片以上 [51]。
4. **极高成本**：单腔150万–500万美元，集群工具超1,500万美元 [51]。
5. **应用领域错位**：MBE擅长单晶外延生长（III-V族、二维材料、量子阱），而非多晶金属薄膜沉积 [49][50]。

MBE市场终端用户中研究机构占52.3% [51]，超过85%的领先量子硬件公司依赖MBE生长的材料 [51]。在MRAM/STT-MRAM领域，虽然MBE可用于磁性多层膜研究 [52][66]，但量产产线中的MTJ（磁性隧道结）沉积主要采用PVD溅射工具（如Singulus TIMARIS）和CMOS兼容工艺，而非MBE [67][68]。

### 4.3 与PVD溅射的对比

PVD溅射之所以成为量产主力，是因为其在沉积速率、台阶覆盖、合金保真度、薄膜密度和成本之间取得了最优平衡。Applied Materials的Endura平台出货超2,000台、被"几乎所有先进芯片制造商"使用的事实，印证了PVD溅射在先进制程金属化中的不可替代地位 [8][9]。TSMC早在1990年代末就将Endura集成Ti/TiN衬垫/阻挡层系统称为"助力盈利和成本效益的量产主力设备" [69]。

---

## 五、2023–2026年主流晶圆厂先进节点（7nm及以下）的实际量产工艺

### 5.1 TSMC（N7 → N3 → N2）

- **7nm（N7，2018年量产）**：开始用钴取代钨作为接触金属，铜互连采用"PVD TaN/Ta阻挡层 + PVD Cu种子层 + 电镀铜填充 + CVD Co衬垫/盖帽"方案 [20][21]。TSMC还采用钴-钨混合金属化，通孔链电阻降低15–25% [22]。
- **5nm（N5，2020年量产）**：ALD TaN阻挡层取代PVD TaN以支持36nm以下间距；铜回流（copper reflow）在钴衬垫上实现 [21]。到5nm节点，若不缩减阻挡层/衬垫层，钨接触中将无纯金属剩余 [20]。
- **3nm（N3，2022年底量产）**：Applied Materials的Endura Copper Barrier Seed系统（选择性ALD Ta + PVD Cu种子 + 铜回流）实现3nm铜线电阻与5nm相当的突破 [13]。
- **2nm（N2，2025年Q4量产）**：TSMC首个纳米片GAA（全环绕栅极）节点，进入量产时良率据报道达70–80%，产能预计2026年底达约9万片/月 [70][71]。N2未采用背面供电（BSPDN），该技术推迟到A16节点 [70]。在2nm测试芯片中，Applied Materials展示了RuCo合金衬垫带来2.5%的性能提升 [5]。

### 5.2 Samsung（SF3 → SF2）

- **3nm（SF3，2022年量产）**：Samsung是首个商业化GAA（MBCFET）的厂商。其铜互连中采用Ru-Co双层衬垫，实现87%的空洞减少和14%的线电阻改善 [72]。
- **2nm（SF2，2025年Q4量产）**：Exynos 2600成为首发产品；良率约50%，低于竞争对手 [70][73]。SF2P计划2026年底推出 [70]。

### 5.3 Intel（Intel 7 → Intel 18A）

- **Intel 18A（2025年下半年HVM）**：Intel首个高量产RibbonFET（GAA）+ PowerVia（背面供电）节点，驱动Core Ultra Series 3（Panther Lake），于2026年CES发布 [70][74]。
- **IEDM 2024**：Intel展示了"减法式钌（subtractive Ru）"互连工艺，在≤25nm间距下实现高达25%的线间电容降低，且无需昂贵的光刻空气间隙排除区或自对准通孔流程，该方案可能出现在Intel Foundry未来节点上 [75]。

### 5.4 2nm及以下节点的金属化趋势（2023–2026）

- **钌（Ru）**：在36nm间距下性能已略微优于铜（imec数据）[72]。Ru无需阻挡层、电子平均自由程短（6–8nm vs 铜的40nm）、抗电迁移能力强，被视为2nm以下最紧间距金属层（M1/M2）的替代金属 [75][76]。imec已演示30nm间距的Ru半大马士革+空气间隙2层互连 [77]。
- **钼（Mo）**：在DRAM字线、3D NAND接触/插塞和逻辑接触中取代钨。几乎所有主要芯片制造商都在不同阶段进行钼认证 [72]。Lam Research的ALTUS Halo于2025年2月发布，美光已在先进NAND中采用 [24][26]。
- **钴（Co）**：仍是MOL接触和局部互连的主力金属，与铜、钌、钼形成混合金属化方案 [22][72]。
- **IRDS 2022路线图**指出："互连电阻已进入指数增长区间，原因是铜的非理想阻挡层缩放；需要新的阻挡层材料、ALD基阻挡层或非铜金属化" [78]。imec路线图提出：M1/M2金属间距将达21nm，通孔CD仅12–14nm；混合金属化（Ru/W/Mo通孔+铜线）、半大马士革方案和埋入式电源轨是主要演进方向 [53]。

---

## 六、总结

在先进制程（7nm及以下）芯片金属薄膜沉积中：

1. **PVD（磁控溅射）**用于沉积Ta/TaN阻挡层、Cu种子层、Ti/TiN粘附层/阻挡层、Co接触、Al焊盘/UBM等，是铜互连阻挡层/种子层体系的核心设备。选择理由：高纯度、高沉积速率、良好的合金保真度、成熟的设备生态（Endura平台），但对高深宽比结构的台阶覆盖不足。

2. **CVD**用于沉积W（接触/通孔填充）、Co（接触填充、互连衬垫/盖帽）、Ru（衬垫）、Mo（新兴填充）等。选择理由：优异的间隙填充能力、较好的共形性、可选择性沉积（消除阻挡层）、400°C以下工艺兼容性。

3. **ALD**用于沉积TaN（铜扩散阻挡层）、TiN（接触阻挡层/DRAM电极）、W成核层、Ru（衬垫/填充）、Co（成核/填充）、Mo（新兴填充）等。选择理由：近100%共形覆盖（可应对>60:1深宽比）、原子级厚度控制（~10Å）、低温工艺、无针孔薄膜质量，但沉积速率慢、成本较高。

4. **电子束蒸发**不用于先进制程量产金属化，主要限于研发、lift-off工艺、光学镀膜和特种薄膜。原因：视线方向沉积导致台阶覆盖差、均匀性差、薄膜密度低。

5. **分子束外延（MBE）**不用于先进制程量产金属化，主要限于化合物半导体、量子器件和磁性薄膜研究。原因：沉积速率极低、超高真空要求、产能极小、成本极高；其市场以研究机构为主（52.3%）。

2023–2026年间，台积电（N2）、三星（SF2）和英特尔（18A）的实际量产工艺显示：钴（接触/衬垫）、钌（衬垫/新兴互连）、钼（DRAM/NAND/逻辑接触）正在逐步取代或补充钨和铜，而PVD+CVD+ALD三类设备将共同支撑这一金属化变革，设备厂商Applied Materials、Lam Research、ASM International和Tokyo Electron分别在其中扮演关键角色。

---

## 来源

[1] SemiconductorX – Metallization: Copper Damascene, Cobalt & Ruthenium Interconnects: https://semiconductorx.com/mfg-front-end-metallization.html
[2] SemiconductorX – Wafer Sputtering Targets: https://semiconductorx.com/wafer-sputtering-targets.html
[3] JX Advanced Metals – Sputtering Target (PVD) for Semiconductor: https://www.jx-nmm.com/english/products/sputtering/semiconductor_st
[4] DataIntelo – Semiconductor Sputtering Targets Market Research Report 2034: https://dataintelo.com/report/global-semiconductor-sputtering-targets-market
[5] Allan Chemical – Advances in Barrier Layers for Cu Interconnects: https://allanchem.com/advances-barrier-layers-cu-interconnects
[6] Applied Materials – Endura PVD Product Page: https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html
[7] DataIntelo – Semiconductor Sputtering Targets Market (2025–2034): https://dataintelo.com/report/global-semiconductor-sputtering-targets-market
[8] Applied Materials Press Release – 2,000 Endura Systems Shipment: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-sets-new-industry-record-shipment-2000-endura
[9] Applied Materials – Endura PVD: https://www.appliedmaterials.com/us/en/product-library/endura-pvd.html
[10] Applied Materials – Endura Cirrus HTX PVD: https://www.appliedmaterials.com/us/en/product-library/endura-cirrus-htx-pvd.html
[11] Applied Materials – Endura Amber PVD: https://www.appliedmaterials.com/us/en/product-library/endura-amber-pvd.html
[12] SemiFlows – Physical Vapor Deposition (PVD) in Semiconductor Manufacturing: https://semiflows.com/blog/what-is-physical-vapor-deposition-in-semiconductor-manufacturing
[13] Electronic Design – Applied Materials Says New Tool Eases Resistance in Chip Interconnects: https://www.electronicdesign.com/technologies/embedded/article/21167739/electronic-design-applied-materials-says-new-tool-eases-resistance-in-chip-interconnects
[14] SemiFlows – Tungsten Metallization in Advanced Semiconductor Manufacturing: https://semiflows.com/blog/what-is-tungsten-in-semiconductor-manufacturing
[15] Lam Research – ALTUS Product Family: https://www.lamresearch.com/product/altus-product-family
[16] IEEE Spectrum – Applied Materials Says New Tool Breaks Chip Resistance Bottleneck: https://spectrum.ieee.org/applied-materials-says-new-tool-breaks-chip-resistance-bottleneck
[17] Applied Materials – Endura Volta Selective W CVD: https://www.appliedmaterials.com/us/en/product-library/endura-volta-selective-w-cvd.html
[18] Applied Materials – Endura Volta Selective W CVD (product library): https://www.appliedmaterials.com/us/en/product-library/endura-volta-selective-w-cvd.html
[19] Applied Materials – Endura Volta Cobalt CVD: https://www.appliedmaterials.com/us/en/product-library/endura-volta-cvd-cobalt.html
[20] Applied Materials Blog – Enabling the AI Era with a New Integrated Materials Solution: https://www.appliedmaterials.com/us/en/blog/blog-posts/enabling-the-ai-era-with-a-new-integrated-materials-solution.html
[21] Applied Materials Blog – Cobalt Enables Power and Performance Scaling at Single-Digit Logic Nodes: https://www.appliedmaterials.com/us/en/blog/blog-posts/cobalt-enables-power-and-performance-scaling-at-single-digit-logic-nodes.html
[22] Patsnap Eureka – Cobalt Semiconductor Material: https://eureka.patsnap.com/materials/cobalt-semiconductor-vlsi
[23] Lam Research Newsroom – Tokyo Electron and Novellus Announce Breakthrough Results on Copper Process Technology for 2Xnm and Beyond: https://newsroom.lamresearch.com/2008-12-01-Tokyo-Electron-and-Novellus-Systems-Announce-Breakthrough-Results-and-Collaboration-on-Copper-Process-Technology-for-2Xnm-and-Beyond
[24] Lam Research Newsroom – ALTUS Halo for Molybdenum ALD (Feb 19, 2025): https://newsroom.lamresearch.com/2025-02-19-Lam-Research-Ushers-in-New-Era-of-Semiconductor-Metallization-with-ALTUS-R-Halo-for-Molybdenum-Atomic-Layer-Deposition
[25] Semiconductor Digest – Molybdenum – The Metal Enabling Next Big Leap In Chip Manufacturing for the AI Era: https://www.semiconductor-digest.com/molybdenum-the-metal-enabling-next-big-leap-in-chip-manufacturing-for-the-ai-era
[26] Counterpoint Research – Molybdenum-Based Metallization Unlocking New Economies of Scale: https://counterpointresearch.com/en/insights/post-insight-cp-conversations-counterpoint-conversations-molybdenumbased-metallization-unlocking-new-economies-of-scale-in-semiconductor-manufacturing
[27] PatSnap Eureka – ALD Conformal Coating in 3D NAND: https://www.patsnap.com/resources/blog/rd-blog/ald-conformal-coating-in-3d-nand-patsnap-eureka
[28] TSMC Research – Interconnect Research: https://research.tsmc.com/japanese/research/interconnect/on-chip-interconnect/publish-time-2.html
[29] Semiconductor Digest – ALD/PVD Copper Barrier/Seed System (Endura iCuB/S): https://sst.semiconductor-digest.com/2002/11/ald-pvd-copper-barrier-seed-system
[30] Google Patents – US20150221550A1 (Tokyo Electron, ALD barrier + CVD Ru liner for void-free Cu filling): https://patents.google.com/patent/US20150221550A1/en
[31] Tokyo Electron – Triase+ Series: https://www.tel.com/product/triase.html
[32] Tokyo Electron IR Day 2021 Presentation: https://www.dcsmodule.com/js/htmledit/kindeditor/attached/20220729/20220729144841_77612.pdf
[33] BALD Engineering – Tokyo Electron Release Triase+ EX-II TiN Plus HT: https://www.blog.baldengineering.com/2016/01/tokyo-electron-release-triase-ex-ii-tin.html
[34] Nomad Semi – Tokyo Electron Deep Dive - Part 2: https://www.nomadsemi.com/p/tokyo-electron-deep-dive-part-2
[35] Lam Research Newsroom – Novellus Launches ALTUS DirectFill 153 for 65nm and Below: https://newsroom.lamresearch.com/2004-11-24-NOVELLUS-LAUNCHES-ALTUS-R-DIRECTFILL-153-TUNGSTEN-NITRIDE-TUNGSTEN-DEPOSITION-SYSTEM-FOR-65-NM-AND-BELOW
[36] Google Patents – US10731250B2 (Lam Research, Depositing ruthenium layers in interconnect metallization): https://patents.google.com/patent/US10731250B2/en
[37] Google Patents – US20180211872A1 (Applied Materials, Enhanced cobalt agglomeration resistance by ruthenium doping): https://patents.google.com/patent/US20180211872A1/en
[38] Entegris Blog – Molybdenum's Role in Ultra-Fast Computing: https://blog.entegris.com/molybdenums-role-in-ultra-fast-computing-the-metal-behind-the-speed
[39] ASM International – ALD (Atomic Layer Deposition): https://www.asm.com/our-technology-products/ald
[40] ASM International – Pulsar XP ALD: https://www.asm.com/our-technology-products/ald/xp4-pulsar
[41] ASM International – How ALD enables next-generation 3D semiconductor scaling: https://www.asm.com/news/beyond-moore-s-law-ald-powers-vertical-innovation
[42] Korvus Technology – Evaporation vs Sputtering: https://korvustech.com/evaporation-vs-sputtering
[43] Rogue Valley Microdevices – E-Beam Evaporation vs. Sputter Deposition: https://roguevalleymicrodevices.com/e-beam-evaporation-vs-sputter-deposition
[44] Polyteknik – E-Beam Evaporation Systems: https://www.polyteknik.com/technology/electron-beam-evaporation
[45] AEM Deposition – Thin Film Deposition Methods: PVD, Sputtering & Evaporation Explained: https://www.aemdeposition.com/blog/thin-film-deposition-methods.html
[46] ScienceDirect Topics – Electron-Beam Evaporation: https://www.sciencedirect.com/topics/engineering/electron-beam-evaporation
[47] Stanford Advanced Materials – Electron Beam Evaporation: https://www.samaterials.com/content/electron-beam-evaporation.html
[48] Korvus Technology – Electron Beam Evaporation Applications: https://korvustech.com/electron-beam-evaporation-applications
[49] University of Iowa Prineas Research Group – Molecular Beam Epitaxy: https://jprineas.lab.uiowa.edu/research/molecular-beam-epitaxy
[50] Wikipedia – Molecular-beam epitaxy: https://en.wikipedia.org/wiki/Molecular-beam_epitaxy
[51] Dataintelo – Molecular Beam Epitaxy (MBE) Market Research Report 2034: https://dataintelo.com/report/global-molecular-beam-epitaxy-mbe-market
[52] UniversityWafer – Molecular Beam Epitaxy (MBE) Substrates: https://www.universitywafer.com/mbe.html
[53] imec – A view on the logic technology roadmap: https://www.imec-int.com/en/articles/view-logic-technology-roadmap
[54] PatSnap Eureka – Compare Physical Vapor Deposition vs CVD for Thin Films: https://eureka.patsnap.com/report-compare-physical-vapor-deposition-vs-cvd-for-thin-films
[55] Semiconductor Digest – Achieving High Aspect Ratio TSVs: https://sst.semiconductor-digest.com/2008/03/achieving-high-aspect-ratio-tsvs
[56] GP Plasma – Atomic Layer Deposition: https://gpplasma.com/atomic-layer-deposition
[57] Wafer World – Comparing PVD, ALD, and CVD: https://www.waferworld.com/post/silicon-manufacturing-comparing-physical-vapor-atomic-layer-and-chemical-vapor-deposition
[58] Wikipedia – Atomic Layer Deposition: https://en.wikipedia.org/wiki/Atomic_layer_deposition
[59] Emergent Mind – CMOS BEOL Integration: https://www.emergentmind.com/topics/cmos-back-end-of-line-integration
[60] Wafer World – Silicon Manufacturing: Comparing PVD, ALD, and CVD: https://www.waferworld.com/post/silicon-manufacturing-comparing-physical-vapor-atomic-layer-and-chemical-vapor-deposition
[61] AtomicLimits – Conformal deposition and gap-fill by plasma ALD: https://www.atomiclimits.com/2021/05/24/conformal-deposition-and-gap-fill-by-plasma-ald-some-great-tem-images-and-recently-published-cover-art
[62] IntechOpen – Mechanical Characterization of Black Diamond (Low-k) Structures: https://www.intechopen.com/chapters/40033
[63] PatSnap Eureka – How To Enhance Growth Rates In Atomic Layer Deposition Using Mixed Precursors: https://eureka.patsnap.com/report-how-to-enhance-growth-rates-in-atomic-layer-deposition-using-mixed-precursors
[64] ASM International – High-Speed ALD Process Doubles Throughput (SEC filing): https://www.sec.gov/Archives/edgar/data/351483/000119312508253388/dex991.htm
[65] DataIntelo – Atomic Layer Deposition Equipment (ALD) Market Research Report 2034: https://dataintelo.com/report/atomic-layer-deposition-equipment-market
[66] PMC – Magnetic-Field-Assisted Molecular Beam Epitaxy of Fe3O4 Ultrathin Films: https://pmc.ncbi.nlm.nih.gov/articles/PMC9964408
[67] MRAM-Info – STT-MRAM: Introduction and market status: https://www.mram-info.com/stt-mram-introduction-and-market-status
[68] Google Patents – US10283246B1 (GlobalFoundries, MTJ structures and methods): https://patents.google.com/patent/US10283246B1/en
[69] Applied Materials Press Release – Integrated Liner/Barrier Solution Hits 100th System Shipment: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-unique-integrated-linerbarrier-solution-hits
[70] Cyberraiden – 2nm Nodes in 2026: TSMC N2, Intel 18A, and Samsung SF2: https://cyberraiden.wordpress.com/2026/03/11/comparing-the-leading-2nm-nodes-in-2026-tsmc-n2-intel-18a-and-samsung-sf2-density-performance-yields-and-ecosystem
[71] UST – TSMC N2 vs Samsung 2GAP vs Intel 18A: https://www.ust.com/en/insights/tsmc-n2-vs-samsung-2gap-vs-intel-18a
[72] Semiconductor Engineering – Interconnects Approach Tipping Point: https://semiengineering.com/interconnects-approach-tipping-point
[73] TechInsights – 2nm Process Comparison Webinar: https://www.techinsights.com/webinar/2nm-process-comparison
[74] SemiconductorX – Process Nodes: N3, N2, 18A, SF3: https://semiconductorx.com/mfg-process-nodes.html
[75] Vik's Newsletter – Ruthenium: The Next Step in Interconnects for Advanced Logic: https://www.viksnewsletter.com/p/is-ruthenium-the-next-step-in-interconnects
[76] SemiFlows – Ruthenium Metallization: https://semiflows.com/blog/what-is-ruthenium-in-semiconductor-manufacturing
[77] eenewseurope – Ruthenium shows way to 2nm: https://www.eenewseurope.com/en/ruthenium-shows-way-to-2nm
[78] IEEE IRDS – 2022 More Moore: https://irds.ieee.org/images/files/pdf/2022/2022IRDS_MM.pdf
[79] SemiEngineering – Ruthenium Interconnects On Tap: https://semiengineering.com/ruthenium-interconnects-on-tap
[80] arXiv – Selecting Alternative Metals for Advanced Interconnects: https://arxiv.org/html/2406.09106v1
