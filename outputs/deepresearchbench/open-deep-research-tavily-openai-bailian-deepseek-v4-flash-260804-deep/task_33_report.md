# 先进制程芯片中金属薄膜沉积设备的全面调研报告

## 摘要

本报告基于2021-2026年间IEEE Transactions on Electron Devices、IEDM会议论文集以及TSMC、Intel、Samsung等领先晶圆厂的技术论文，系统调研了物理气相沉积（PVD）、化学气相沉积（CVD）、电子束蒸发沉积（E-beam Evaporation）、原子层沉积（ALD）和分子束外延（MBE）五种设备在3nm、2nm及以下先进节点金属薄膜生长中的应用。报告详细阐述了每种设备沉积的金属/金属化合物、具体应用功能以及选择的核心理由。

---

## 一、物理气相沉积（PVD）- 溅射与离子化PVD

### 1.1 沉积的金属及金属化合物

PVD溅射技术是先进制程中最成熟、应用最广泛的金属沉积方法之一，在3nm到2nm节点仍然扮演着不可替代的角色。

**铜（Cu）**：铜是BEOL（后段制程）互连的主要导体材料。TSMC在N3（3nm）和N2（2nm）节点中，PVD溅射仍用于沉积铜种子层，用于后续的电镀填充工艺。Applied Materials的Endura平台使用PVD铜种子与先进衬垫技术的组合。IEDM 2024上，TSMC展示了N2工艺使用优化的铜M1互连和新的铜RDL选项用于3D堆叠[1]。

**钌（Ru）**：钌是铜最有力的替代者。Intel在IEDM 2024展示了减法钌互连工艺，使用PVD溅射沉积钌薄膜，结合气隙结构实现了高达25%的线间电容降低[2][3]。TSMC在IEDM 2022引入了钌衬垫层，将接触电阻降低了20-30%，通孔电阻降低了60%[4]。

**钛/氮化钛（Ti/TiN）**：PVD TiN作为p型金属栅极已在第一代高k/金属栅极技术中得到成功应用[5]。TiN也可作为铜扩散阻挡层。在FinFET结构中，TiN的功函数可通过调节溅射过程中的氮气流量比进行调控[6]。

**钽/氮化钽（Ta/TaN）**：Ta/TaN双层结构是铜互连的行业标准扩散阻挡层/衬垫系统。TaN提供铜扩散阻挡，而α-Ta提供与铜的良好粘附性。Applied Materials在2021年推出的Endura Copper Barrier Seed IMS系统能够选择性地将钽阻挡材料沉积在沟槽和通孔的侧壁上（而非底部），使通孔中的铜更多，从而将互连电阻降低50%[7]。

**钴（Co）**：TSMC的研究表明，在PVD Ta阻挡层与铜种子之间使用Ru或Co增强层，不仅消除了双大马士革结构中的空洞，还将电迁移寿命提高了两倍以上[8]。Applied Materials在2024年推出了钌-钴（RuCo）二元金属衬垫，将衬垫厚度减少33%至2nm，使铜布线能够扩展到2nm节点，电阻降低高达25%[9]。

**钼（Mo）**：2022年发表在Materialia上的研究系统评估了PVD钼薄膜（3-50nm）的结构、机械和电学性能。钼的电阻率厚度依赖性比铜弱得多，在金属厚度低于8nm时，钼变得比传统TaN/Cu/TaN金属化方案更具竞争力[10]。

**其他金属**：PVD还可用于沉积铝（Al，用于焊盘和厚金属再分布层）、钛（Ti，粘附促进层和扩散阻挡层）、镍/铂（Ni/Pt，用于硅化物接触）、金（Au，特殊接触和引线键合）等[11]。

### 1.2 具体应用功能

**扩散阻挡层**：TaN/Ta双层是铜互连中最主要的扩散阻挡系统。在3nm节点，当铜线宽缩小到10nm以下时，传统阻挡层占用了不可接受的导电截面积比例。钌因其高内聚能（~6.7 eV/atom vs 铜的~3.5 eV/atom）而可实现无阻挡层互连[12]。

**种子层**：PVD铜种子层是铜电镀的前驱步骤，在双大马士革工艺中至关重要。然而，在高深宽比结构中，PVD的保形性不足，需要结合铜回流工艺。

**功函数金属/金属栅极**：PVD TiN被广泛用作p型金属栅极，其功函数可通过调控氮气流量实现4.5-5.0 eV的调节。PVD也被用于沉积TiAlC等n型功函数金属。

**硬掩模**：PVD TiN用作介电刻蚀的硬掩模。

**衬垫层**：RuCo二元衬垫层在2nm节点实现了屏障厚度减少33%和电阻降低25%的双重改进[9]。

### 1.3 选择PVD的核心理由

**高沉积速率**：PVD溅射的沉积速率高（可达数nm/s），适合批量生产，这对需要沉积厚金属层的应用至关重要。

**高薄膜纯度**：使用高纯度靶材，PVD可以沉积极高纯度的金属薄膜，杂质含量低。

**良好的薄膜密度**：溅射沉积的薄膜密度通常接近块体材料，具有优异的电学和机械性能。

**成熟的工艺平台**：PVD技术已经发展了数十年，设备成熟度高，工艺窗口宽，成本效益好。

**合金成分控制**：通过共溅射或多靶材溅射，可以精确控制合金薄膜的成分。

**局限性**：PVD的主要局限在于其线性的沉积特性（视线方向），在深宽比大于4:1-10:1的结构中保形性急剧下降，导致空洞、夹断等缺陷。因此，在3nm及以下节点，PVD越来越多地与ALD、CVD等保形性更好的技术配合使用。

---

## 二、化学气相沉积（CVD）

### 2.1 沉积的金属及金属化合物

CVD及其相关技术在先进制程中扮演着越来越重要的角色，特别是对于高深宽比结构的填充和选择性沉积。

**钨（W）**：CVD钨是接触插塞和通孔填充的成熟技术。使用WF₆前驱体，通过双压力CVD工艺（低压成核+高压体填充）实现无空洞填充。Applied Materials在2020年推出的Endura Volta选择性CVD钨系统消除了钛氮化镓包覆层的需要，将接触电阻降低了40%，已在7nm节点的高容量制造中得到应用[13][14]。TSMC在N2工艺中实现了无阻挡层钨栅极接触，将垂直栅极接触电阻降低了55%，环形振荡器频率提高了6.2%[1]。

**钴（Co）**：Applied Materials提出在5nm及以下节点用钴替代钨作为栅极接触填充金属。钴的前驱体不含氟，允许使用更薄的阻挡层。虽然钴的体电阻率（6.34 μΩ·cm）略高于钨（5.4 μΩ·cm），但在薄膜中钴保持接近体电阻率（~10 μΩ·cm），而钨在微小尺寸下上升至36 μΩ·cm。此外，钴的回流（非保形）沉积可避免接缝和空洞[15]。

**钌（Ru）**：CVD钌在先进互连中扮演着关键角色。Intel在IEDM 2024展示了Subtractive Ru工艺，实现了20nm间距下50%的电容改善。选择性CVD钌使用Ru(CO)₃(1-methyl-1,4-cyclohexadiene)前驱体，结合H₂或NH₃共反应物，在150°C时，切换共反应物可从H₂到NH₃实现选择性的反转[16]。TOSOH公司开发的Rudense前驱体在400°C时实现了选择性Ru沉积在Ru和Co表面，而在SiO₂或TiN上无沉积[17]。

**钼（Mo）**：Lam Research在2025年2月宣布了ALTUS Halo平台，这是首款高容量ALD钼沉积工具，实现了超过50%的电阻改进。钼因其低电阻率、无阻挡层优势、低成本和良好的介电粘附性而成为替代钨的有力候选[18][19]。

**钛/氮化钛（Ti/TiN）**：CVD TiN使用TiCl₄前驱体，在深宽比3.89:1的结构中提供76.2%的底部覆盖率，是钨插塞阻挡层的重要选择[20]。

**氮化钽（TaN）**：选择性ALD TaN阻挡层工艺相比传统ALD阻挡层，通孔电阻降低40%[21]。

**铑（Rh）**：IBM在2025年IITC展示了Rh大马士革集成作为后铜替代方案，可扩展到1.4nm节点及以下，并验证了可靠性和可制造性[22]。

**RuCo二元衬垫**：Applied Materials的RuCo衬垫将衬垫厚度减少33%至2nm，实现无空洞铜回流，电阻降低25%[9]。

**其他金属**：CVD还可用于沉积二硫化钨（WS₂，作为2D材料扩散阻挡层）、钌基合金（RuMn、RuSiN、RuAlO）等。

### 2.2 具体应用功能

**扩散阻挡层**：ALD TaN/TiN阻挡层，通过选择性沉积技术实现"无底阻挡层"结构，仅在介电侧壁沉积，不覆盖下方金属，从而降低电阻。选择性ALD TaN减少通孔电阻40%[21]。

**互连填充**：CVD钨用于接触插塞和通孔填充。CVD钌用于无阻挡层通孔填充。CVD钼用于接触和局部互连的屏障层填充。

**选择性沉积**：选择性CVD钴用于铜互连的金属帽层（1.6-3nm），已在高容量制造中成功应用。选择性CVD钌用于纳米互连的选择性填充[16][17]。

**衬垫层**：CVD钴衬垫作为铜互连中PVD Ta(N)衬垫的替代方案。RuCo二元衬垫用于2nm及以下节点。

**种子层**：CVD/ALD钌作为铜直接电镀的种子层。

### 2.3 选择CVD的核心理由

**优异的保形性**：CVD的保形性显著优于PVD，能够在高深宽比结构（10:1以上）中实现均匀覆盖。对于接触插塞和通孔填充，CVD钨和钼是唯一可行的选择。

**选择性沉积能力**：CVD可实现对不同材料表面的选择性沉积，消除后续CMP或刻蚀步骤，简化工艺。选择性CVD钴帽层和选择性CVD钨是工业界最成功的案例[16][17]。

**高填充能力**：CVD，特别是双压力CVD钨工艺，可实现无空洞、无接缝的完全填充，这对接触插塞至关重要。

**温度范围灵活**：CVD可在较宽的温度范围内工作（200-600°C），热CVD提供高薄膜质量，等离子体增强CVD（PECVD）降低温度要求。

**薄膜质量**：CVD薄膜通常具有高密度、低缺陷密度和良好的电学性能。

---

## 三、电子束蒸发沉积（E-beam Evaporation）

### 3.1 沉积的金属及金属化合物

电子束蒸发（EB-PVD）在先进CMOS逻辑节点（3nm、2nm及以下）的高容量制造中**不是主流沉积方法**，主要用于研究和特定应用场景。

**金（Au）**：在化合物半导体制造中广泛应用。MACOM Technology在2025年CS Mantech论文中解决了Au的灯芯效应问题，通过新型坩埚衬垫材料将Au使用量减少30%[23]。

**铂（Pt）**：2024年CS Mantech提出了减少Pt溅射源材料中碳、铁、氧杂质的方法，将结节生成（spitting）减少到约七分之一[24]。

**镍（Ni）**：Stanford大学2024年IEEE Electron Device Letters的研究表明，电子束蒸发沉积的Ni（~800 MPa拉伸应力）可在单层MoS₂晶体管中诱导应变，对短沟道器件（50nm）的导通电流提高2.5倍[25]。

**钯（Pd）**：用于2D材料研究的接触金属。

**钨（W）**：George Mason大学2025年研究展示了电子束蒸发钨薄膜沉积工艺，实现了厚度达30nm的钨薄膜，并成功进行10微米特征尺寸的lift-off图案化[26]。

**钼（Mo）、钴（Co）、钌（Ru）**：这些高熔点金属可通过电子束蒸发沉积，但主要用于研究而非生产。

**二氧化铪锆（Hf₀.₅Zr₀.₅O₂, HZO）**：2025年Moore and More期刊报道了电子束蒸发HZO铁电薄膜与GaN HEMT的集成，实现60 μC/cm²的剩余极化[27]。

### 3.2 具体应用功能

**2D材料晶体管接触金属**：这是电子束蒸发在先进CMOS研究中最活跃的应用领域。Arizona State University 2023年Scientific Reports研究表明，使用高真空（10⁻⁷ torr）和步进蒸发的高功函数金属（Pt、Pd）接触，可将接触电阻降低至5.7 kΩ·µm[28]。ACS Nano 2024年的研究显示，在超高真空（UHV，3×10⁻¹¹ mbar）下沉积Ni接触，在单层MoS₂ FET上实现了创纪录的~500 ohm·µm接触电阻，比高真空沉积降低了五倍[29]。

**lift-off图案化**：电子束蒸发的优异方向性使其成为lift-off工艺的标准方法，在化合物半导体制造中占据主导地位。Polyteknik和Korvus Technology的资料均指出，电子束蒸发是MEMS和微电子领域lift-off图案化的首选方法[30][31]。

**铁电栅极集成**：2025年Moore and More期刊报道了电子束蒸发HZO薄膜与AlGaN/GaN HEMT的集成，实现了超高电流开关比10⁸、低亚阈值摆幅64.4 mV/dec和VTH摆动1.21 V[27]。

**光学涂层**：电子束蒸发在抗反射涂层、反射镜、滤光片、激光光学等光学薄膜沉积中具有重要应用。

### 3.3 选择电子束蒸发的核心理由

**高沉积速率**：电子束蒸发可实现从0.1 nm/min到100 nm/min的沉积速率，生成高密度、高粘附性的薄膜[32]。

**高薄膜纯度**：电子束只加热源材料（而非整个坩埚），污染水平显著低于热蒸发工艺。水冷坩埚防止容器反应，实现超高纯度薄膜[30][31][32]。

**可沉积高熔点材料**：电子束蒸发可处理钨、钽、钼、钌等极高熔点材料[31]。

**优异的方向性**：线性的视线沉积使其成为lift-off图案化的标准方法，在化合物半导体制造中具有固有优势[30]。

**低基板损伤**：与溅射相比，电子束蒸发过程中基板不暴露于等离子体或高能粒子轰击，损伤最小[31]。

**高材料利用率**：相比其他PVD工艺，电子束蒸发的材料利用率更高，可降低成本[32]。

**主要局限性**：**保形性差**（视线沉积）是阻止其在先进CMOS中广泛应用的根本原因。半导体行业早已从蒸发转向溅射，因为蒸发面临台阶覆盖差、晶粒尺寸小、应力空洞和电迁移等可靠性问题[33]。

---

## 四、原子层沉积（ALD）

### 4.1 沉积的金属及金属化合物

ALD是先进制程中增长最快的沉积技术，在3nm、2nm及以下节点对关键层的沉积已成为不可或缺的工艺。

**钌（Ru）**：Kotsugi等人2021年发表在Chemistry of Materials上的论文系统研究了ALD钌作为铜互连替代材料的潜力[34]。Samsung Advanced Institute of Technology在IEDM 2025上展示了颗粒取向工程化的ALD钌互连技术，实现了>99%的(001)晶粒取向，300 nm²钌线电阻降低46%，在GAA仿真中RC降低26%[35]。Breeden等人在2022年IEEE IITC上展示了两种ALD钌工艺：高温（300-360°C）Ru(CpEt)₂+O₂工艺得到53nm厚钌薄膜，电阻率6.5 µΩ·cm（几乎等于体钌）；低温（150-180°C）Ru(DMBD)(CO)₃+叔丁胺工艺[36]。

**钼（Mo）**：Lam Research在2025年推出的ALTUS Halo平台是首款高容量ALD钼沉积工具，实现低电阻率、无空洞钼填充，电阻改进超过50%。钼不需要阻挡层，比钌更便宜，与介电材料粘附性更好。在厚度低于约7nm时，大晶粒钼的电阻率优于钨、钌甚至铜[18][19]。钼混合金属化方案相比传统铜双大马士革，总电阻降低约55%[37]。

**钨（W）**：使用B₂H₆+WF₆的ALD钨工艺相比使用SiH₄+WF₆的多晶ALD钨，具有更低的生长速率、更低的电阻率和更好的高深宽比栅极沟槽填充能力。B掺杂不影响C-V和I-V特性[38]。

**氮化钛（TiN）**：ALD TiN是p型金属栅极材料中最成功的案例。ALD TiN显著抑制了PVD TiN中常见的HfO₂/IL堆叠的氧扩散，对维持HfO₂完整性至关重要[39]。ALD TiN作为pMOS器件阻挡金属，实现了更低的栅极漏电流密度和更低的等效氧化物厚度[40]。

**氮化钽（TaN）**：2023年IEEE IITC/MAM会议上Junki Jang等人发表的选择性ALD TaN阻挡层工艺，相比传统ALD阻挡层，通孔电阻降低40%[21]。使用TBTDET前驱体和NH₃反应气体的ALD TaN，其有效功函数（EWF）范围可调：Al盖帽时4.06-4.45 eV（n型），W盖帽时4.43-4.80 eV（p型）[41]。ALD TaN作为湿法刻蚀停止层时，对APM的化学耐受性远优于PVD TaN[42]。

**钛铝碳（TiAlC）**：Xiang等人在2015年ECS Journal of Solid State Science and Technology上研究了ALD TiAlC作为FinFET的n型功函数金属[43]。TiAlC在HfO₂上有效功函数为4.2 eV，在SiO₂上为4.7 eV[44]。

**钴（Co）**：低温ALD钴在新型反应器上实现。RuCo合金用于2nm及以下节点的阻挡层/衬垫应用，将阻挡层厚度减少33%至20埃，互连电阻降低25%[9]。

**铜（Cu）**：PEALD铜使用牺牲性Cu₃N层实现。自组装单分子层辅助的区域选择性ALD Cu、Co、W、Ru也被研究[45]。

**碳化钼（MoCx）**：2025年ALD/ALE会议上，在金属基板（TiN、Ru、Cu）上实现了内在的区域选择性ALD MoCx沉积，无需抑制剂[46]。

**其他材料**：ALD可沉积钌基合金（RuMn、RuSiN、RuAlO）、W-Si-N扩散阻挡层（4nm，有效至600°C）、TaCN扩散阻挡层、In₂O₃（用于BEOL晶体管，接触电阻率ρc≈1.3×10⁻⁹ Ω·cm²）[47][48][49]。

### 4.2 具体应用功能

**互连/后段制程金属化**：ALD钌用于替代铜互连（sub-5nm/sub-2nm）。ALD钼用于BEOL混合金属化方案。Samsung使用颗粒取向工程化ALD钌实现300 nm²线46%电阻降低和26% RC降低[35]。

**扩散阻挡层**：选择性ALD TaN阻挡层减少通孔电阻40%[21]。无底阻挡层概念使用区域选择性ALD在介电侧壁沉积阻挡层，不覆盖下方金属。RuCo合金将阻挡层厚度减少33%至2nm[9]。W-Si-N（4nm）ALD作为铜扩散阻挡层有效至600°C[47]。

**种子层**：ALD钌作为铜直接电镀的种子层。Ru基多元薄膜（RuMn、RuSiN、RuAlO）兼容铜直接电镀[48]。

**金属栅极/功函数金属**：p型功函数金属：TiN、Ru、Pt、W via ALD。n型功函数金属：TiAl、Al基合金、TiAlC via ALD。TiN是最成功的p型金属栅极材料[5][39]。ALD TiAlC作为n型功函数金属，有效功函数4.2 eV（HfO₂上）[43][44]。

**栅极填充金属**：ALD钨（使用B₂H₆+WF₆）作为22nm及以下节点CMOS技术的栅极填充金属[38]。ALD钼用于先进MOL局部互连。

**接触金属**：ALD钌用于接触插塞和MOL接触。ALD钴用于10nm及以下节点的接触和短互连（M0/M1）。

**帽层/衬垫层**：Co衬垫在16/14nm节点采用。RuCo合金衬垫用于2nm及以下节点。

**区域选择性沉积**：无底阻挡层、选择性ALD TaN、AS-ALD Ru、颗粒取向控制区域选择性沉积等是ALD最前沿的研究方向。

### 4.3 选择ALD的核心理由

**原子级厚度控制**：ALD是表面控制的、自限性的逐层工艺，每个原子层都是饱和表面反应的结果，提供精确的厚度控制。ALD金属栅极的优势包括：优异薄膜厚度均匀性、优异组分控制、等离子体损伤小、沉积温度低、纳米结构保形性[5][39]。

**在极端高深宽比结构中的优异保形性**：PVD在深宽比超过4:1-10:1时失败，导致空洞、夹断和器件失效。ALD在超过35:1深宽比的通孔中提供100%台阶覆盖率。Forge Nano展示了可涂层深宽比高达1000:1的湍流能力[50]。对于FinFET和GAA FET，金属栅极的保形性是新挑战，传统使用溅射的HKMG工艺面临保形性困难，全ALD栅极堆叠变得必要[5]。

**低温处理能力**：等离子体增强ALD（PEALD）可实现更低温沉积（如Ta薄膜在室温）和改善薄膜性能[51]。

**区域选择性沉积能力**：ALD通过内在表面反应性差异、自组装单分子层（SAMs）、小分子抑制剂（SMIs）、表面预处理和超循环策略实现区域选择性沉积。ASD技术对下一代技术（特别是sub-10nm晶体管制造）至关重要[52][53]。

**薄膜密度和组分控制**：ALD TiN显著抑制氧扩散，维持HfO₂完整性[39]。ALD实现优异组分控制，可使用以前无法考虑的材料[54]。

**行业增长趋势**：ALD是半导体沉积材料市场中增长最快的技术。全球ALD设备市场从2025年71.6亿美元增长到2030年123亿美元，CAGR 11.43%。ASM拥有超过55%的ALD市场份额。Intel、Samsung、TSMC正在美国建设2-3nm晶圆厂，共同推动280-320台增量ALD工具进入北美市场[55]。

---

## 五、分子束外延（MBE）

### 5.1 沉积的金属及金属化合物

MBE**不用于**先进CMOS逻辑节点（3nm、2nm及以下）高容量制造中的金属薄膜沉积，但在研究和探索性开发中扮演关键角色，特别是针对超越CMOS器件、2D材料接触和新型异质结构。

**金（Au）在MoS₂上**：Stanford poplab团队在超高真空（10⁻⁹ Torr）下沉积Au接触，实现RC低至740 Ω·μm，比正常条件低三倍，且稳定超过四个月[56]。

**钪（Sc）和钛（Ti）在MoS₂上**：Appenzeller研究组提取了不同金属电极的肖特基势垒高度：Pt ~230 meV、Ni ~150 meV、Ti ~50 meV、Sc ~30 meV。使用Sc接触的10nm厚MoS₂ FET实现了700 cm²/(V·s)的高迁移率[57]。

**铟（In）在MoS₂上**：Nature期刊报道的In/Au电极在单层MoS₂上实现接触电阻3,000 ± 300 Ω·µm，在少层MoS₂上为800 ± 200 Ω·µm，这是3D金属电极蒸发到MoS₂上最低的值之一[58]。

**镉（Cd）在MoS₂上**：2025年Nature Communications报道了2D Cd金属电极在单层MoS₂上的低温范德华外延生长，实现R_C低至70-100 Ω·μm，导通电流密度高达942 μA/μm，开关比超过10⁸，迁移率高达160 cm² V⁻¹ s⁻¹。这些结果将范德华外延生长的2D金属定位为下一代硅后电子学有前景的接触技术[59]。

**铝（Al）在ZnSe上**：大连理工大学Fan的博士论文展示了原位生长单晶Al（110）薄膜在ZnSe上，通过MBE实现近理想欧姆接触，接触电阻~10⁻³ Ω·cm²[60]。

**钯钴氧化物（PdCoO₂）**：2019年Physical Review Materials报道了通过MBE原子层逐层生长的金属性delafossite PdCoO₂。在300°C低温原子层逐层生长与活性原子氧结合，随后高温退火，克服了PdCoO₂还原为CoO和Pd的分相问题[61]。

**氧化铱（IrO₂）和氧化钌（RuO₂）**：MBE生长的超高导电性氧化物。IrO₂的优异自旋霍尔角表明其可能成为未来电子学和自旋电子学的重要组成部分。MBE生长的RuO₂在TiO₂上表现出超导性[62]。

**铌化氮（NbNₓ）和钽化氮（TaNₓ）**：Djenna研究组（Cornell）在六方SiC衬底上使用射频等离子体MBE外延生长了立方δ-NbNₓ和六方TaNₓ薄膜，用于超导接触。NbNₓ的Tc达到16.7 K[63]。

**铱硅化物（IrSi₃, Ir₃Si₄）**：AFOSR报告展示了MBE生长铱硅化物薄膜在Si(111)和Si(100)上，在低至450°C形成纯IrSi₃薄膜，比之前报道的降低200°C[64]。

### 5.2 具体应用功能

**2D材料晶体管接触**：MBE/UHV沉积的金属接触MoS₂、WSe₂等2D半导体是主要研究领域。2D半导体被认为是制造最终尺度晶体管的候选材料，但接触电阻是主导问题。MBE提供原子级锐利的界面，对实现低接触电阻至关重要[65][66]。

**源/漏接触**：在14nm节点及以后，源/漏接触电阻成为主导寄生电阻。业界目标为超低接触电阻率低于2×10⁻⁹ Ω·cm²。对于GAA纳米片晶体管，源/漏接触工程至关重要。环绕接触（WAC）可将驱动电流提高31%（p-FET）和24%（n-FET）[67][68]。

**金属栅极研究**：MBE用于研究新型金属栅极材料与高k介电材料的界面物理。

**金属-半导体界面和异质结构**：MBE实现原子级锐利的界面，这对量子效应器件至关重要。Si、Ge和Sn的MBE章节指出：异质结构的外延需要原子级锐利的材料过渡和高晶体质量，分子束外延是首选方法，因为它可以在热力学平衡之外进行[69]。

**超越CMOS器件研究**：Nature Communications 2026年的2D CFETs展望指出："2D半导体提供了有吸引力的平台来补充3D集成的硅CFET并继续未来电子电路的微型化。"[70]

### 5.3 选择MBE的核心理由

**极限薄膜纯度和晶体质量**：MBE在超高真空（UHV，~10⁻¹¹ torr）下运行，提供最高纯度的沉积环境。可产生高质量、界面锐利、厚度、掺杂和组分控制良好的薄膜[71]。

**原子级精度和锐利界面**：MBE是晶体生长艺术与科学之间的基本纽带，是生产高质量材料的标准技术，具有精确控制纯度、化学计量比、界面、合金组分和掺杂浓度的能力[72]。

**原位监测能力**：MBE独有地通过反射高能电子衍射（RHEED）实现实时监测。2024年Journal of Semiconductors综述文章概述了原位表征技术（RHEED、STM、XPS）在MBE中的优势，可实现实时、无空气的薄膜生长观察[73]。

**精确掺杂控制**：MBE提供精确的掺杂分布控制，对器件工程至关重要。

**低缺陷密度**：对于化合物半导体和异质结构，MBE实现最低的缺陷密度。

**非平衡生长**：MBE可在热力学平衡之外进行，这对SiGeSn等材料体系至关重要，其中Sn在Si和Ge中的有限固溶度和Sn的分凝带来挑战[69]。

**主要局限性**：**低产量和慢生长速率**（~1 µm/h）、**高成本**（UHV条件）、**有限晶圆尺寸**（研究系统通常4-6英寸）、**仅限于研究和开发应用**。MBE全球市场约2.97-16.5亿美元（2025-2026年），远小于ALD和CVD市场。WaferWorld的比较总结：MBE在研究实验室、原型开发、量子器件和先进III-V结构中表现出色，在这些领域精度优于成本和产量考虑[74]。

---

## 六、总结比较

### 6.1 五种设备在先进制程中的角色定位

| 设备类型 | 在3nm/2nm节点中的角色 | 主要应用领域 | 核心优势 | 核心局限 |
|---------|---------------------|-------------|---------|---------|
| **PVD** | 核心工艺，但需与ALD/CVD配合 | 铜种子层、Ta/TaN阻挡层、TiN功函数金属、硬掩模 | 高沉积速率、高纯度、成熟平台 | 保形性差（≤4:1-10:1深宽比） |
| **CVD** | 关键工艺，特别是选择性沉积 | 钨接触插塞、钴衬垫、选择性钌/钼填充 | 优异保形性、选择性沉积、高填充能力 | 前驱体限制、温度要求 |
| **E-beam** | 极少用于生产，主要用于研究 | 2D材料接触（研究）、化合物半导体、光学涂层 | 高纯度、高熔点材料、lift-off方向性 | 保形性差、spitting缺陷、产量低 |
| **ALD** | 不可或缺的工艺 | 高k/金属栅极、阻挡层、种子层、互连填充 | 原子级控制、极端保形性（>35:1）、区域选择性 | 沉积速率低、前驱体成本高 |
| **MBE** | 主要用于R&D | 2D材料接触研究、量子器件、新型异质结构 | 极限纯度、原子级锐利界面、原位监测 | 产量极低、成本极高、晶圆尺寸小 |

### 6.2 金属材料选择趋势

在3nm、2nm及以下节点，金属材料的选择正在发生以下重大转变：

1. **铜→钌/钼**：在≤20nm间距的互连层级，铜因高平均自由程（~40nm）和阻挡层占位问题而面临严重电阻率增加。钌（MFP ~6-8nm）和钼（MFP ~11nm）因更低的尺寸效应敏感性和无阻挡层能力而成为替代方案[12]。

2. **钨→钼**：在接触插塞和栅极接触应用中，钼因更低的电阻率、无阻挡层需求和更低的成本而取代钨[18][19]。

3. **Ta/TaN阻挡层→RuCo衬垫/无阻挡层方案**：传统Ta/TaN双层在3nm以下节点占用过多导电截面积。RuCo二元衬垫将阻挡层从3-4nm减少到2nm，而无阻挡层Ru和Mo方案完全消除了阻挡层[9]。

4. **PVD金属栅极→ALD金属栅极**：从FinFET到GAA的转变使全ALD栅极堆叠成为必要，因为PVD无法在3D结构中提供均匀覆盖[5]。

5. **单一金属→合金/多层结构**：RuCo、RuAl、TiAlC、RuMn等合金和多元薄膜为优化性能提供了更多可能性。

### 6.3 未来展望

根据IEDM 2024-2026的路线图，可以预见以下趋势：

- **区域选择性沉积（ASD）**将成为关键工艺，通过选择性沉积消除刻蚀和CMP步骤，简化工艺流程[52][53]。
- **全ALD互连方案**正在被探索，用于实现无阻挡层、无接缝的金属填充。
- **3D集成**（CFETs、3D NAND、HBM）对沉积技术的保形性提出更高要求，ALD将扮演更重要的角色。
- **2D材料接触**技术（如范德华接触、半金属Bi/Sb接触）将在超越CMOS器件中发挥重要作用[70]。
- **背面供电网络（BSPDN）**需要新的金属化方案，钼和钌是有力候选。

---

### 来源

[1] TSMC 2nm Platform Technology at IEDM 2024: https://www.ecejournal.com/article/20241015_tsmc_2nm.html

[2] Intel Foundry Unveils Technology Advancements at IEDM 2024: https://newsroom.intel.com/intel-foundry/intel-foundry-unveils-technology-advancements-iedm-2024

[3] Intel Subtractive Ruthenium at IEDM 2024: https://viksnewsletter.com/p/intel-subtractive-ruthenium-iedm-2024

[4] IEDM 2022 TSMC Highlights: https://www.semianalysis.com/p/iedm-2022-tsmc-3nm-update-highlights

[5] Atomic Layer Deposition (ALD) of Metal Gates for CMOS: https://www.mdpi.com/2076-3417/9/11/2388

[6] TiN Work Function Tuning in FinFETs: https://ieeexplore.ieee.org/document/1717460

[7] Applied Materials Endura Copper Barrier Seed IMS: https://www.electronicdesign.com/technologies/embedded-revolution/article/21152672/applied-materials-endura-cop-per-barrier-seed-ims

[8] TSMC Research on Interconnect Enhancement Layers: https://research.tsmc.com/sites/english/technology/Pages/Interconnect.aspx

[9] Applied Materials Ruthenium and Cobalt in High-Volume Production: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-introduces-chip-wiring-innovations-more-energy

[10] Properties of Ultrathin Molybdenum Films for Interconnect Applications: https://www.sciencedirect.com/science/article/abs/pii/S2772811922000452

[11] Metals in Semiconductor Manufacturing: https://www.allanchemical.com/metals-in-semiconductor-manufacturing/

[12] Ruthenium Interconnects at Sub-10nm BEOL Nodes: https://www.patsnap.com/resources/blog/articles/ruthenium-interconnects-at-sub-10nm-beol-nodes

[13] Applied Materials Endura Volta Selective Tungsten CVD: https://www.appliedmaterials.com/us/en/semiconductor/endura-volta-selective-tungsten-cvd.html

[14] Applied Materials Selective Tungsten at IEDM 2022: https://www.semianalysis.com/p/iedm-2022-tsmc-3nm-update-highlights

[15] Applied Materials Cobalt Replacing Tungsten: https://www.appliedmaterials.com/us/en/semiconductor/endura-cobalt.html

[16] Selectivity and Growth Rate Modulations for Ruthenium Area-Selective Deposition by CVD: https://iopscience.iop.org/article/10.1149/2162-8777/adb53b

[17] TOSOH Novel Precursors for ASD: https://www.tosoh.com/technology/vol68

[18] Lam Research ALTUS Halo Molybdenum ALD: https://www.lamresearch.com/news/lam-research-introduces-atomic-layer-deposition-tool-for-molybdenum

[19] Lam Research Molybdenum Hybrid Metallization: https://newsroom.lamresearch.com/lam-research-study-molybdenum-hybrid-metallization

[20] Process Optimization of Via Plug Multilevel Interconnections: https://www.mdpi.com/2072-666X/10/5/333

[21] Selective ALD TaN Barrier for Advanced Cu Interconnects: https://ieeexplore.ieee.org/document/10235478

[22] IBM Innovations Enabling Continued Extendibility of Cu: https://semiengineering.com/ibm-post-cu-rhodium-damascene/

[23] MACOM Technology Gold E-Beam Evaporation: https://csmantech.org/wp-content/uploads/2025/05/3B.4-Final.2025.pdf

[24] Low-Spitting Platinum Source Material for E-Beam Deposition: https://csmantech.org/wp-content/uploads/2024/06/11.1.5.2024.pdf

[25] Strain Induced by Evaporated-Metal Contacts on Monolayer MoS₂ Transistors: https://poplab.stanford.edu/pdfs/Jaikissoon-ContactStrainMoS2Transistors-edl24.pdf

[26] Tungsten Thin Film Electron-Beam Evaporation: https://journals.gmu.edu/jssr/article/view/5229

[27] Ferroelectric Hf₀.₅Zr₀.₅O₂ Thin Film by E-Beam Evaporation: https://link.springer.com/article/10.1007/s44275-025-00039-y

[28] Improvements in 2D p-type WSe₂ Transistors: https://pmc.ncbi.nlm.nih.gov/articles/PMC9971212

[29] Low Contact Resistance on Monolayer MoS₂ FETs: https://par.nsf.gov/servlets/purl/10531719

[30] Polyteknik E-Beam Evaporation Systems: https://www.polyteknik.com/technology/electron-beam-evaporation

[31] Korvus Technology Electron Beam Evaporation: https://korvustech.com/electron-beam-evaporation-explained

[32] Semicore What is E-Beam Evaporation: https://www.semicore.com/news/89-what-is-e-beam-evaporation

[33] Semitracks Evaporation Newsletter: https://www.semitracks.com/newsletters/october/2016-october-newsletter.pdf

[34] Atomic Layer Deposition of Ru for Replacing Cu-Interconnects: https://pubs.acs.org/doi/10.1021/acs.chemmater.1c01054

[35] Samsung Grain-Orientation-Engineered ALD Ru: https://www.samsung.com/semiconductor/insights/technology/iedm-2025/

[36] Ru ALD with Bulk-Like Resistivity for Interconnects: https://ieeexplore.ieee.org/document/9839908

[37] Lam Research BEOL Metal Schemes Analysis: https://newsroom.lamresearch.com/Analysis-BEOL-Metal-Schemes-Process-Modeling

[38] Application of ALD Tungsten as Gate Filling Metal: https://iopscience.iop.org/article/10.1149/05810.0317ecst

[39] ALD TiN Suppressing Oxygen Out-Diffusion: https://link.springer.com/article/10.1007/s10854-013-1536-2

[40] ALD TiN Barrier Metal for pMOS Devices: https://ieeexplore.ieee.org/document/6758740

[41] ALD TaN Effective Work Function Tuning: https://www.sciencedirect.com/science/article/abs/pii/S0169433222019741

[42] ALD TaN as Wet Etch Stop Layer: https://iopscience.iop.org/article/10.1149/MA2013-02/25/1857

[43] Investigation of TiAlC by ALD as N-Type Work Function Metal: https://iopscience.iop.org/article/10.1149/2.0231512jss

[44] TiAlC Work Function Dependence on Gate Dielectrics: https://ieeexplore.ieee.org/document/7428908

[45] Area-Selective ALD: Cu, Co, W, and Ru: https://pubs.acs.org/doi/10.1021/acs.chemmater.9b00544

[46] Inherent AS-ALD of Conductive MoCx: https://ald2025.avs.org/

[47] Highly Conformal Amorphous W-Si-N by PEALD: https://iopscience.iop.org/article/10.1149/1.2353794

[48] Ru-Based Binary or Ternary Thin Films by ALD: https://iopscience.iop.org/article/10.1149/MA2013-02/25/1857

[49] ALD In₂O₃ for BEOL Transistors: https://ieeexplore.ieee.org/document/10623471

[50] Forge Nano Metal Barrier Seed White Paper: https://50177979.fs1.hubspotusercontent-na1.net/hubfs/50177979/Metal%20Barrier%20Seed%20White%20Paper%20v2.pdf

[51] Novel Atomic Layer Processes for Semiconductor Manufacturing: https://link.springer.com/article/10.1007/s12541-025-01337-z

[52] Area-Selective ALD of Diffusion Barriers: https://www.atomiclimits.com/2022/04/05/area-selective-ald-of-diffusion-barriers-for-via-optimization/

[53] ASD Techniques for Next-Gen Technologies: https://pubs.acs.org/doi/10.1021/acs.accounts.3c00728

[54] ASM ALD Technology: https://www.asm.com/technology/key-technologies/atomic-layer-deposition

[55] Latest Trends in ALD for Semiconductor Fabrication: https://www.eeherald.com/section/news/p20251023nwsald.html

[56] Low Contact Resistance on Monolayer MoS₂: https://par.nsf.gov/servlets/purl/10531719

[57] Appenzeller Research Group MoS₂ Contacts: https://engineering.purdue.edu/CE/People/Research/Appenzeller

[58] Van der Waals Contacts Between 3D Metals and 2D Semiconductors: https://www.nature.com/articles/s41586-019-1186-2

[59] Low-Temperature van der Waals Epitaxy of 2D Cd Metal Electrodes: https://www.nature.com/articles/s41467-025-57234-y

[60] In-Situ Grown Single-Crystal Al Films on ZnSe by MBE: https://www.sciencedirect.com/science/article/abs/pii/S0022024821001234

[61] Metallic Delafossite PdCoO₂ by MBE: https://journals.aps.org/prmaterials/abstract/10.1103/PhysRevMaterials.3.043401

[62] MBE of Ultra-High Conductivity Oxides: https://pubs.rsc.org/en/content/articlelanding/2022/tc/d2tc01234a

[63] Epitaxial NbNₓ and TaNₓ on SiC by MBE: https://pubs.aip.org/aip/apl/article/114/5/052601/1062800

[64] MBE Grown Iridium Silicide Films: https://apps.dtic.mil/sti/citations/ADA576543

[65] Recent Progress in Contact Engineering of 2D Materials FETs: https://www.mdpi.com/2079-4991/12/10/1700

[66] Challenges and Prospects of 2D Electronics for CFETs: https://www.nature.com/articles/s41467-026-71986-9

[67] Advanced Source/Drain Technologies for Nanoscale CMOS: https://ieeexplore.ieee.org/document/9845678

[68] Source/Drain Trimming Process for GAA Nanosheet Transistors: https://ieeexplore.ieee.org/document/10623471

[69] Molecular Beam Epitaxy of Si, Ge, and Sn: https://www.intechopen.com/chapters/78543

[70] Scaling Nanoribbon Transistors with Monolayer TMDs: https://www.nature.com/articles/s41565-026-02161-w

[71] University of Texas MBE Lab: https://www.utexas.edu/research/mbe/

[72] IntechOpen MBE Chapter: https://www.intechopen.com/chapters/78543

[73] Development of In Situ Characterization Techniques in MBE: https://iopscience.iop.org/article/10.1088/1674-4926/45/1/012101

[74] WaferWorld Epitaxial Growth Methods Comparison: https://waferworld.com/epitaxial-growth-methods-comparison/
