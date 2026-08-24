# 二维半导体低接触电阻的统一物理机制：方法梳理、理论比较与未来展望

## 引言

二维半导体（以MoS₂为代表）被视为后硅时代晶体管沟道材料的有力候选者，但金属–半导体接触电阻（Rc）过高长期制约其性能发挥。近年来，科研人员发展出多种降低接触电阻的策略——半金属（Bi、Sb）接触、纯金属（Au、Sc、Ni等）接触、相工程（2H→1T）、插层、掺杂、边缘接触、范德华接触——其中多种方案已将接触电阻推进到与硅基技术相当甚至超越的水平（如Bi接触的123 Ω·µm、Sb接触的42 Ω·µm）。然而，每种方法几乎都有各自独立的理论解释：有的归因于"金属诱导能隙态（MIGS）抑制"，有的归因于"费米能级退钉扎"，有的归因于"能带杂化"，有的归因于"简并掺杂"。这种理论上的碎片化使得领域缺乏统一发展方向。

本报告围绕一个核心问题展开：**这些降低接触电阻的方法之间是否存在共通的物理机制？能否构建统一的理论框架？基于此，未来方向何在？** 报告首先系统梳理主要低接触电阻方法及其理论依据，继而深入比较共性物理机制，评估已有统一框架的解释力，最后展望未来发展趋势。

---

## 第一部分：主要低接触电阻方法系统梳理

### 1.1 半金属接触（Bi、Sb）

**铋（Bi）接触。** 2021年，Shen等人（MIT、TSMC等合作）在《Nature》报道了半金属Bi与单层MoS₂之间的超低接触电阻——**123 Ω·µm**，同时实现创纪录的**1135 µA/µm**导通电流密度，接触电阻接近量子极限，与Si、GaN、InGaAs等传统半导体相当，肖特基势垒完全消除[1]。其理论解释称为"能隙态饱和（Gap State Saturation）"：Bi作为半金属在费米能级处态密度为零，且表面键饱和，因此MIGS被充分抑制，同时接触区TMD中自发形成简并态[1]。值得指出，后续有媒体将此解读为"1nm节点突破"，实属夸大——该工作解决的是接触电阻问题，并非制造了符合1nm节点标准的超短沟道器件[2]。

**锑（Sb）接触。** 2021年TSMC在IEDM上报道了Sb半金属接触，在单层MoS₂上实现近零肖特基势垒和**0.66 kΩ·µm**的接触电阻，短沟道器件导通电流超过600 µA/µm（VDS=1V）[3]。Sb熔点630.6°C，远高于Bi（271.5°C）和Sn（231.9°C），Sb接触器件在400°C退火后仍完全工作，而Bi接触器件300°C即明显退化——这对后道工艺（BEOL）兼容性至关重要。DFT还预测Bi-Sb合金可在保持低接触电阻的同时提升热稳定性（Bi₀.₅Sb₀.₅预测势垒高度0.10 eV，熔点540°C）[3]。

**接近量子极限的Sb接触。** 2023年Li等人在《Nature》报道，通过强范德华相互作用下MoS₂能带与半金属Sb的杂化，将接触电阻进一步推进到**42 Ω·µm**，接近理论量子极限[4]。该器件实现1.23 mA/µm导通电流、10⁸开关比、74飞秒本征延迟，且在125°C下保持优异稳定性，性能"超越同等硅CMOS技术并满足2028年路线图目标"[4]。

**理论机制深化。** Tong等人（2023）的DFT系统研究表明，Bi/Sb的费米能级（−4.12 eV/−4.25 eV）与TMDC导带底（约−4 eV）天然对齐；半金属/TMDC接触的层间距显著大于金属/TMDC接触（>3 Å），导致接触形成时TMDC仅发生"弱金属化"，产生**半金属诱导能隙态（SMIGS）**，这些态延伸至导带底以下，从而降低或消除n型肖特基势垒[5][6]。2025年Chen等人利用扫描隧道显微镜/谱（STM/S）**直接可视化**了MoS₂/Au(111)与MoS₂/Bi(111)界面的MIGS分布差异：Au接触的MIGS几乎遍布整个带隙（−1.74 eV至+0.41 eV），而Bi接触的MIGS仅集中在价带顶附近（−1.46 eV至−0.57 eV），且Q谷能带结构得以保留[7]。这为半金属接触的"弱金属化"机制提供了直接的实验证据。

### 1.2 纯金属接触与功函数工程

**低功函数金属。** Das等人（Appenzeller组，2013）系统研究了Sc（Φ=3.5 eV）、Ti（4.3 eV）、Ni（5.0 eV）、Pt（5.9 eV）与MoS₂的接触，提取的肖特基势垒高度分别为约**30 meV（Sc）**、50 meV（Ti）、150 meV（Ni）、230 meV（Pt），Sc接触的10 nm厚MoS₂器件室温有效迁移率达**700 cm²/(V·s)**[8]。该工作明确指出MoS₂/金属界面受到近导带的费米能级钉扎影响，与III-V族半导体和硅类似[8]。

**超高真空沉积Ni。** 2024年Sun等人（Purdue/UT Dallas）报道，在超高真空（3×10⁻¹¹ mbar）下沉积CMOS兼容的Ni接触，可将单层MoS₂接触电阻降至**约500 Ω·µm**——比高真空沉积低5倍[9]。XPS分析显示，UHV沉积增强了Ni/MoSₓ键合物种，避免了高真空中MoO₃的形成（MoO₃生成自由能−266.67 kJ/mol远低于MoS₂的−112.95 kJ/mol，热力学上优先形成）[9]。这一发现表明，通过界面化学调控，传统共价金属也能达到与vdW型接触相当的接触电阻。

**功函数工程的限度。** Stanford Pop组（2020）对Y、Sc、Ag、Al、Ti、Au、Ni七种金属的系统研究发现：超薄氧化Al可使MoS₂产生>2×10¹² cm⁻²的n型掺杂（不损伤迁移率）；Ag、Au、Ni沉积会造成不同程度的损伤；Ti、Sc、Y等活泼金属与MoS₂发生化学反应形成金属氧化物和硫化物；薄金属几乎不引起应变[10]。其结论是：接触电阻不能简单地由金属功函数预测，需要综合考虑界面反应、损伤和掺杂效应[10]。

### 1.3 相工程（2H→1T/1T'）

**奠基性工作。** Kappera等人（2014，《Nature Materials》）通过正丁基锂处理在2H相MoS₂纳米片的接触区域局部诱导出金属性1T相，实现**200–300 Ω·µm**的零栅压接触电阻[11]。器件在空气中迁移率约50 cm²V⁻¹s⁻¹、亚阈值摆幅<100 mV/dec、开关比>10⁷。关键实验证据是：不同金属沉积对器件性能影响有限，说明**1T/2H界面本身控制载流子注入**[11]。该工作被引用超过1600次。

**机制深化与p型接触。** Hu等人（2018）的DFT研究表明，所有六种1T/2H MoS₂堆垛构型均形成p型接触，p型肖特基势垒0.44–0.67 eV，显著低于Au/MoS₂的n型势垒（0.88 eV）——1T相功函数更接近2H相价带顶，因此1T相可作为TMD晶体管的通用空穴注入层[12]。Ouyang等人（2018）通过Bader电荷分析揭示了界面电荷转移对相稳定性的关键作用：只有当金属向MX₂单层转移足够电荷时，才会发生向T相（1T'或1T''）的相变，并据此筛选出七个可形成零肖特基势垒接触的体系（如1T''-MoSe₂/Sc、1T''-WS₂/Zr等）[13]。

**可规模化1T相制备。** Sharma等人（2018）利用微波等离子体处理实现>70%面积的稳定1T相（环境稳定>27天，热稳定至300°C），1T相薄层电阻108 Ω/□，载流子浓度约2.3×10¹⁵ cm⁻²（比2H相高两个数量级），满足Ioffe-Regel金属判据[14]。2025年Fa等人报道了反向溅射诱导的2H→1T转变：在75 W/10 s最优条件下，接触电阻从1126 kΩ·µm降至**413 kΩ·µm**，输出电流提升约150倍[15]。

### 1.4 插层与掺杂

**表面电荷转移掺杂。** Kiriya等人（2014，JACS）使用具有极高还原电位的苄基紫精（BV）对MoS₂进行表面电荷转移掺杂，实现**1.2×10¹³ cm⁻²**的电子面密度（达到MoS₂简并掺杂极限），接触电阻降低约3倍（3.3→1.1 kΩ·µm），在低栅压下降低超过100倍[16]。机制是简并掺杂使肖特基势垒变薄，隧穿注入占主导[16]。

**替位掺杂。** Suh等人（2014，《Nano Letters》）通过化学气相输运实现Nb对MoS₂的替位掺杂，空穴浓度达**1.8×10¹⁴ cm⁻²**（简并p型），并证明简并掺杂使Ti接触变为欧姆接触——"电荷隧穿压过肖特基势垒"[17]。

**稀土掺杂诱导金属化。** 2024年Jiang等人在《Nature Electronics》报道了钇（Y）掺杂诱导的二维相变金属化：通过等离子体沉积-退火工艺，仅1 nm Y层即可实现**0.5 nm深度**的选区单原子层表面掺杂，实现全固态、CMOS兼容的超短沟道MoS₂弹道晶体管[18]。

### 1.5 边缘接触（1D接触）

**概念起源（石墨烯）。** Wang等人（2013，《Science》）首次提出一维边缘接触：将石墨烯完全封装在hBN中，通过刻蚀暴露边缘后蒸镀金属，形成2D材料与3D金属之间的1D界面，接触电阻低至**100 Ω/µm**（按接触宽度归一化），并实现15 µm弹道输运[19]。

**MoS₂边缘接触。** Jain等人（2019，《Nano Letters》）将边缘接触推广到hBN封装的单层MoS₂，实现与顶接触相当的低接触电阻和高迁移率[20]。2025年Xiao等人（北京大学）通过纯Ar等离子体刻蚀优化边缘悬挂键，在单层MoS₂上实现**1.25 kΩ·µm**的边缘接触电阻（边缘接触MoS₂器件中的纪录）、肖特基势垒低至**32 meV**、导通电流436 µA/µm（Vds=1V）[21]。其理论解释是：边缘接触通过金属与2D材料边缘的共价键合形成金属化接触界面，避免了表面接触中导致n型钉扎的轨道重叠态，使接触遵循Schottky-Mott规则（钉扎因子可达**0.98**）[22][23]。

**理论深化。** Parto等人（2021，《Physical Review Applied》）的DFT-NEGF研究表明，由于本征终止边缘态的存在，MoS₂边缘接触的电荷中性能级更接近价带，呈现**p型特性**——与顶接触相反。这种肖特基势垒各向异性使得边缘接触在p型导电方面优于顶接触[24]。Guo等人的计算也发现边缘接触的p型势垒比顶接触低约0.7 eV[25]。

### 1.6 范德华（vdW）接触

**接近Schottky-Mott极限。** Liu等人（2018，《Nature》）通过将原子级平整的金属薄膜直接层压到无悬挂键的2D半导体上，形成无化学键合的vdW金属-半导体结，界面S参数达**0.96**——半导体史上最接近Schottky-Mott理想极限（S=1）的值[26]。这从根本上克服了长期困扰半导体物理的费米能级钉扎问题。

**低熔点金属In。** Wang等人（2019，《Nature》）报道了In/Au超净vdW接触：STEM证实In与MoS₂界面原子级锐利，vdW间隙仅2.4 Å（单层）/2.7 Å（多层），无化学反应或氧化。单层MoS₂接触电阻**3000±300 Ω·µm**，多层MoS₂为**800±200 Ω·µm**，超薄NbS₂上仅**220±50 Ω·µm**[27]。In/Pd合金可调功函数（4.23 eV vs In/Au的4.05 eV）而不破坏界面洁净度[27]。

**h-BN插层。** Cui等人（2017，《Nano Letters》）在Co与MoS₂之间插入单层h-BN，将Co功函数从5.0 eV修饰至3.3 eV（XPS证实），同时作为隧穿势垒阻断金属-MoS₂相互作用，平带肖特基势垒仅**16 meV**（直接Co接触为38 meV），1.7 K下接触电阻3 kΩ·µm[28]。

**Se缓冲层法。** Kwon等人（2022，《Nature Electronics》）利用Se缓冲层实现"无相互作用、无缺陷"的vdW接触，钉扎因子达**−0.91**（即基本未钉扎），Au vdW接触的WSe₂ p型器件实现1.25 kΩ·µm接触电阻和60 meV肖特基势垒[29]。

**2D金属接触。** Cl掺杂SnSe₂（Cl-SnSe₂）作为高功函数（4.71 eV）金属性2D材料，与WSe₂形成**S=1**的完全退钉扎接触，接触电阻仅**83±59 Ω·µm**；交叉TEM显示原子级洁净界面，而蒸镀金属（Pd、Au、Ti）无论功函数高低均使WSe₂呈n型——直接证明蒸镀损伤是钉扎的根源[30]。

---

## 第二部分：共性物理机制比较分析

### 2.1 费米能级钉扎的本质：两种竞争理论

理解所有低接触电阻策略的起点，是回答"什么钉扎了费米能级"。文献中存在两个竞争的理论阵营：

**阵营A："非寻常机制"（Gong等人，2014，《Nano Letters》）。** 对Al、Ag、Ir、Au、Pd、Pt六种金属（功函数4.2–6.1 eV）与单层MoS₂的DFT研究表明，费米能级在带隙中0.5–0.64 eV窗口内**部分钉扎**，斜率0.71。钉扎源于两个协同效应：（1）界面电荷重新分布形成偶极，修改金属功函数；（2）金属-S相互作用削弱层内S-Mo键合，产生**以Mo d轨道为主的能隙态**——这些态局域在Mo原子上，而非直接接触的S原子上[31]。关键预测：当界面间距增大到6.0 Å时，所有接触均遵循Schottky-Mott模型——"在金属与MoS₂之间插入缓冲材料可以退钉扎费米能级并形成欧姆接触"[31]。

**阵营B：MIGS模型（Guo/Liu/Robertson；Sotthewes等人）。** Cambridge团队的DFT计算表明，"尽管TMD内键合主要约束在层内，肖特基势垒仍大体遵循金属诱导能隙态（MIGS）模型，与三维半导体类似"，MoS₂的钉扎因子S≈0.3[25]。Sotthewes等人（2019）通过高空间分辨率C-AFM/STM对MoSe₂、WSe₂、WS₂、MoTe₂的研究，区分了完美区与缺陷区：**完美区钉扎因子0.11–0.30，缺陷区仅0.04–0.11**，且电荷中性能级均靠近导带[32]。Bampoulis等人（2017）进一步揭示，天然MoS₂中的亚表面金属样缺陷（可能是Mo空位或反位缺陷）使肖特基势垒降低30–50%——此前在大接触中观察到的强钉扎（S≈0.1）主要源于这些缺陷，而非通常认为的S空位[33]。

**综合判断：** 两阵营并非不可调和。Gong等人的"Mo d轨道能隙态"实际上描述的是MIGS在2D材料中的具体微观形态——MIGS并非简单的"金属波函数渗入半导体"，而是通过金属-S键削弱层内键合、在Mo原子上产生局域态。Sotthewes等人的MIGS结论与Gong等人的"非寻常机制"在"界面态源于金属-硫族元素相互作用"这一点上是一致的。真正的分歧在于对钉扎强度的定量描述。**对这一争论的理解是统一框架的基础：无论具体称呼如何，钉扎的物理根源都是金属接触在半导体带隙内引入了态，这些态的能量位置和密度决定了钉扎强度。**

### 2.2 界面态密度与MIGS的谱学证据

2025年Chen等人的STM/S工作提供了迄今最直接的MIGS可视化证据[7]：

- **MoS₂/Au(111)（金属接触）**：MIGS分布几乎覆盖整个带隙（−1.74 eV至+0.41 eV），从导带和价带两侧延伸，衰减长度0.5–1.5 nm振荡；Q谷峰在接触区消失；肖特基势垒0.51 eV。
- **MoS₂/Bi(111)（半金属接触）**：MIGS分布窄得多，仅集中在价带顶附近（−1.46 eV至−0.57 eV）；平均衰减长度1.1–2.5 nm（更长，说明MIGS密度更低）；Q谷能带结构完整保留；CBM估计约−0.11 eV，呈简并半导体特征。

这一对比直接说明：**半金属的低态密度（LDOS）减少了能隙态的渗入，使电荷中性能级移向导带底，从而产生零肖特基势垒**。更重要的是，Q谷保留意味着半金属接触不破坏MoS₂的能带结构，降低了接触区本征薄层电阻[7]。

### 2.3 肖特基势垒高度的形成与调控

肖特基势垒高度（SBH）由金属功函数与半导体电子亲和势之差决定（Schottky-Mott规则），钉扎因子S=|dφB/dφm|从0（完全钉扎）到1（完全退钉扎）[34]。所有降低接触电阻的策略，本质上都在做一件事：**让SBH趋向Schottky-Mott极限，或让隧穿压过残余势垒**。

调控SBH的具体途径包括：
- **界面偶极工程**：TiO₂插层（1.5 nm）将SBH从168 meV降至22 meV，接触电阻从8.2 kΩ·µm降至4 kΩ·µm——机制是阻止金属电子波函数渗入（MIGS理论）并形成界面偶极[35]。Al₂O₃插层（0.8 nm）将SBH从102 meV降至27 meV，接触电阻从59.9降至1.3 kΩ·µm[36]。
- **层数依赖**：Pei等人（2024）的DFT表明，vdW接触的钉扎因子（S=0.49）高于紧密接触（S=0.37），且1L→3L时S从0.49升至0.65（钉扎减弱），4L时回落至0.47[37]。
- **边缘接触的势垒各向异性**：边缘接触的p型SBH比顶接触低约0.7 eV，源于键合和晶体场的各向异性[24][25]。

### 2.4 轨道杂化：强杂化与弱杂化的双重面孔

Zhong等人（2016）将MoS₂-金属带杂化分为三类：**强杂化（Sc、Ti）**——MoS₂金属化，垂直肖特基势垒消失，隧穿概率100%；**中等杂化（Ni、Pt、Ag）**——隧穿概率53–74%；**弱杂化（Au）**——隧穿概率仅4.74%[38]。这揭示了核心矛盾：**强杂化消除隧穿势垒但引入钉扎，弱杂化消除钉扎但引入隧穿势垒。**

Shan等人（2024，《Nano Research》）明确表述了这一两难：纯vdW接触隧穿概率最低仅3.11%（势垒高度4.11–5.00 eV），而通过诱导表面氮空位使界面C原子从sp²转为sp³杂化、形成跨界面共价C-Si键后，隧穿概率提升至48.73%，同时由于MSi₂N₄的带边态由内层M-N亚层贡献（受外层Si-N亚层保护），弱钉扎和欧姆接触得以保持[39]。**这是文献中罕见的"同时解决隧穿势垒与钉扎"的方案**，其思路——用亚层保护带边态、用外层实现界面键合——对统一框架有重要启示。

### 2.5 电荷转移与简并掺杂

电荷转移在多种策略中扮演核心角色：

- **界面偶极**：金属-MoS₂界面电荷重新分布形成偶极，修改金属有效功函数（Gong 2014）[31]。
- **相变驱动**：Ouyang等人（2018）证明界面电荷转移量决定2H→T相变是否发生——"1T相能量始终远高于其他相，界面电荷本身不会诱导2H→1T转变"，但足够的电荷转移可诱导向1T'/1T''的转变[13]。
- **简并掺杂压过势垒**：Suh等人（2014）的Nb掺杂MoS₂使Ti接触变为欧姆——"简并掺杂使电荷隧穿压过肖特基势垒"[17]；Kiriya等人（2014）的BV掺杂同样通过势垒变薄实现3倍接触电阻降低[16]。
- **积累型欧姆接触**：Andrews等人利用p⁺-MoS₂（0.5% Nb）底接触与近本征WSe₂形成vdW结，由于p⁺-MoS₂功函数大于WSe₂电离能，WSe₂侧形成自由空穴积累层（面密度≥4×10¹² cm⁻²），接触势垒消失，开关比10⁸，室温双端迁移率约200 cm²V⁻¹s⁻¹——"不需要对接触区掺杂或栅控"的欧姆接触[40]。

### 2.6 范德华间隙：退钉扎与隧穿代价

范德华间隙的作用可以从Liu、Stradins & Wei（2016，《Science Advances》）的奠基性工作中理解：**2D金属与2D半导体通过vdW相互作用结合时，弱钉扎源于MIGS的抑制**，因此肖特基势垒可调且可消失（如H-NbS₂）[41]。Gong等人（2014）的计算预测（6.0 Å间距→Schottky-Mott行为）为这一机制提供了理论基础[31]。Liu等人（2018）的S=0.96实验[26]和Wang等人（2019）的2.4 Å间隙观察[27]是实验验证。

但vdW间隙也有代价：**隧穿势垒**。Duflou的ab initio NEGF研究表明，顶接触的电流主要由边缘注入决定（金属终止处），只要输运方向有数纳米重叠区，接触电阻就不随表面积线性扩展——**"vdW间隙本身并不固有地阻碍顶接触电流"**[42]。这意味着vdW间隙的隧穿代价可以通过几何设计（边缘注入）和掺杂来缓解。

---

## 第三部分：统一理论框架的评估

### 3.1 文献中的部分统一框架

**目前文献中尚未出现一个能够定量统一所有策略（半金属、纯金属、相工程、掺杂、边缘接触、vdW接触）的单一理论。** 但存在多个部分统一框架，各有其解释力和局限：

**框架A："弱杂化/弱金属化"框架。** 核心命题：钉扎强度由金属-半导体轨道杂化程度决定，弱杂化=弱钉扎=低SBH。支持证据包括：Gong等人的"Mo d轨道能隙态"机制[31]；Su等人的"弱金属化"SMIGS机制[5][6]；Zhong等人的杂化分类[38]；Chen等人的MIGS直接可视化[7]。**局限**：无法定量解释Sc等强杂化金属为何也能实现近欧姆接触（Sc的隧穿概率100%，n-SBH仅0.15 eV）[38]；也无法解释Mo金属（强键合）的低接触电阻[43]。

**框架B："MIGS消除（通过vdW间隙）"框架。** Liu/Stradins/Wei（2016）明确提出：vdW金属-半导体结的弱钉扎归因于MIGS抑制[41]。这一框架涵盖2D金属接触、转移金属接触、低熔点金属接触、缓冲层插入等所有"增大界面间距"的策略，并得到S=0.96（Liu 2018）[26]、S≈0.91（Se缓冲层）[29]、S=1（Cl-SnSe₂）[30]等实验支持。**局限**：无法解释半金属Bi接触（其成功关键是费米能级处零态密度和键饱和，而非间隙本身）[1]；无法解释边缘接触（根本没有vdW间隙，而是悬挂键金属化）[22]；无法解释相工程（同质材料接触）[11]；且纯vdW接触的隧穿概率可能极低（3.11%）[39]，框架必须辅以杂化/掺杂工程。

**框架C："接触金属相/金属性"框架。** 半金属（零DOS）与金属性1T相（同质接触）被归为同一类：通过消除或最小化金属态与半导体带隙态的耦合来实现欧姆接触。Shen等人的"能隙态饱和"[1]和Kappera等人的1T相工程[11]在此框架下统一。Ouyang等人的"Type 3接触"（相变使隧穿势垒和肖特基势垒同时消失）是理论表达[13]。**局限**：本质是材料选择原则而非定量理论；不涉及掺杂和边缘接触。

**框架D："费米能级退钉扎（降低界面态密度）"框架。** 所有策略都可表述为降低界面处MoS₂带隙内的态密度（MIGS、DIGS、缺陷态）。支持证据：缺陷区S=0.04–0.11 vs 完美区0.11–0.30[32]；间距控制抑制IGS[44]。**局限**：CVD生长的MoS₂"缺陷更多、钉扎反而更弱"（S≈0.5，SBH降低）[45]这一反例说明，**界面态密度本身不是充分描述符——态在带隙中的能量位置和轨道特征同样关键**。

**框架E：多描述符图景。** 比较DFT研究的一致结论是：**不存在单一普适描述符**。Gong发现功函数斜率0.71[31]；Zhong发现SBH同时取决于功函数和杂化，且能带计算方案在MoS₂-Sc界面失效，必须用量子输运模拟[38]；Li等人（2024）明确断言"接触电阻不能简单地由金属功函数或费米能级钉扎单独预测，而是由界面偶极、MIGS和金属化效应等多个相互作用因素共同决定"[43]；Zha等人（2026）提出包含垂直界面偶极的修正Schottky-Mott规则[46]；Su等人（2023）提出包含SMIGS能量窗口、偶极势和费米能级移动的修正规则[5]。

### 3.2 一个综合性的统一图景

综合上述分析，可以提炼出一个**事实上的共通机制**（de facto common mechanism）：

> **所有降低接触电阻的策略，其共通物理本质是：降低金属在半导体带隙内引入的界面态密度（从而退钉扎费米能级、使带对齐趋向Schottky-Mott极限），同时通过足够的轨道重叠、简并掺杂或几何设计（边缘注入）保证隧穿势垒足够薄。策略之间的差异在于实现这两点的路径不同。**

各策略在此图景中的定位：

| 策略 | 降低界面态密度的途径 | 解决隧穿势垒的途径 |
|---|---|---|
| 半金属Bi/Sb | 费米能级处零DOS + 键饱和（能隙态饱和）[1] | 弱金属化产生SMIGS辅助带对齐[5] |
| vdW接触/缓冲层 | 物理间距增大抑制MIGS[26][41] | 边缘注入主导电流[42]；低熔点金属缩小间隙[27] |
| 1T/1T'相工程 | 同质金属相接触，无外来金属态[11] | 金属性1T相本身无隧穿势垒[13] |
| 简并掺杂 | 势垒变薄后隧穿压过势垒[16][17] | 掺杂本身使耗尽区变薄[17] |
| 边缘接触 | 悬挂键金属化避免轨道重叠态[22] | 共价键合无vdW间隙[22] |
| 低功函数金属（Sc等） | 强杂化使FL钉扎在CBM附近（对n型有利）[8] | 强杂化金属化消除垂直隧穿势垒[38] |
| 缺陷工程（CVD） | 缺陷增强金属化降低SBH[45] | 杂化增强隧穿[45] |

这一图景的**核心洞察**是：钉扎和隧穿是同一枚硬币的两面——强杂化消除隧穿但引入钉扎，弱杂化消除钉扎但引入隧穿。成功的策略要么在两者之间找到平衡点（如1T相工程、半金属、边缘接触），要么用第三种手段（掺杂、几何设计）绕过这一权衡。

**该统一框架的局限**：它目前仍是定性框架，缺乏一个统一的第一性原理描述符（如"带隙内金属诱导态的光谱权重"）来定量预测任意金属-半导体组合的接触电阻。此外，不同策略的最优工作区间（载流子浓度、温度、层数）差异较大，统一框架需纳入这些维度。

---

## 第四部分：未来发展方向

### 4.1 新型接触材料设计

**半金属合金工程。** TSMC的IEDM工作已展示Bi-Sb合金的DFT预测价值：通过调节Sb比例（40%–100%保持半金属性），可在保持低接触电阻的同时将熔点提升至BEOL兼容水平（≥400°C）[3]。未来可系统探索Bi-Sb-Sn等多元半金属合金、以及具有更高熔点的其他半金属体系。

**二维金属接触材料。** Cl-SnSe₂（S=1，Rc=83 Ω·µm）[30]证明了2D金属作为"钉扎免疫"接触材料的潜力。NbS₂、NbSe₂、TaS₂等金属性TMD的功函数覆盖4.0–6.0 eV（突破石墨烯功函数可调范围±0.3 eV的限制）[34]。V掺杂WSe₂在石墨烯上的STM/S研究也证实了vdW半金属对MIGS的抑制[47]。此外，金属性MBene被计算预测可接近量子极限接触电阻[48]。

**理论预测的极限材料。** Cu插层双层MoS₂电极的DFT+NEGF预测接触电阻仅**16.7–30.0 Ω·µm**（低于量子极限30 Ω·µm）——机制是插层消除了vdW间隙隧穿势垒并形成欧姆接触[49]。Fe₃GaTe₂/MX₂异质结的隧穿比电阻低至1.78×10⁻¹⁰ Ω·cm²，且在−0.16至0.14 V/Å外场下可实现p-欧姆→p-肖特基→n-肖特基→n-欧姆的可逆调控[46]。这些理论预测为实验提供了靶向材料清单。

### 4.2 接触界面工程

**"亚层保护"策略。** Shan等人的sp²→sp³杂化转变工作展示了界面工程的精巧方向：用外层亚层实现强共价键合（隧穿概率48.73%），同时保护内层亚层的带边态（弱钉扎保持）[39]。这一"功能分层"思路可推广到更多材料体系。

**缺陷态的能谱工程。** CVD-MoS₂中缺陷增强金属化降低SBH的反直觉发现[45]，提示缺陷不必然是坏事——关键在于缺陷引入的态位于带隙何处、具有何种轨道特征。未来可通过可控缺陷工程（如反向溅射[15]、等离子体处理）在接触区制造"有益缺陷"。

**MIGS可视化指导的界面优化。** Chen等人的STM/S方法[7]提供了直接评估接触质量的实验工具——未来可用它系统筛选接触材料，建立"MIGS分布图→接触电阻"的数据库。

### 4.3 规模化制造可行性

**热稳定性与BEOL兼容。** 这是当前最紧迫的工程挑战。Bi在400°C退火下失效，而BEOL集成要求400°C H₂环境退火。2026年ACS Nano报道的**Bi限域（confinement）策略**——用AlOₓ和/或TiN阻挡层封装Bi接触——在400°C退火10分钟后仍保持<200 Ω·µm接触电阻，且通过Fab相关集成测试（<40 nm SiO₂沟槽内PVD沉积Bi + ALD TiN阻挡层 + W插塞）[50]。Sb接触器件在400°C退火后保留64%性能[3]，Bi/Sb/Au叠层接触改善了120°C加热稳定性[51]。UHV-Ni的研究还表明，Bi/Au接触在Au帽层保护+高真空退火条件下可稳定至400°C[9]——热稳定性问题有解决方案，但需系统优化。

**统计性与良率。** 领域正在从"单个器件创纪录"走向"大批量统计验证"：Purdue团队的120+器件统计研究[9]、Stanford的720晶体管对比研究（In/Au合金190 Ω·µm、Sn/Au合金270 Ω·µm）[52]、TSMC的IEDM工作[3]代表了这一趋势。未来需建立标准化的接触电阻提取协议和可靠性测试体系。

**选区相工程与掺杂的可控性。** Kappera等人（2014）已指出准确相转移特定区域和1T亚稳性是挑战[11]。Y掺杂的0.5 nm深度选择性[18]和微波等离子体的Al掩模选区1T化[14]是重要进展，但距离晶圆级工艺仍有距离。

### 4.4 面向实际器件的可靠性问题

**长期稳定性。** 1T相的环境稳定性（>27天）[14]、BV掺杂的空气稳定性（9天）[16]、Bi接触的时间稳定性（PMMA封装下2个月）[51]都需要进一步提升。非化学计量盐插层稳定碱金属掺杂的PRL理论方案[53]提供了思路。

**温漂与自热。** 半金属的低熔点本质上是材料本征属性，限域策略[50]和合金化[3]是两条可行路径。Sb的125°C稳定性数据[4]为消费电子级应用提供了参考，但车规级（175°C）和HPC级要求仍待验证。

**接触电阻的尺寸依赖。** 随着器件微缩，接触面积减小，缺陷（特别是亚表面金属样缺陷）的影响将"在结面积减小时愈发突出"[33]。1D边缘接触[22]和1D半金属接触（碳纳米管电极，接触长度进入亚2 nm区域）[54]是应对微缩的两条路径。

### 4.5 统一理论的完善方向

从统一理论的角度，未来最重要的研究方向是：**建立以"带隙内金属诱导态的光谱权重"为核心、可定量预测的描述符体系**。具体包括：
- 利用STM/S直接测量的MIGS分布数据[7]校准DFT计算，建立MIGS光谱-接触电阻的定量关联；
- 将量子输运模拟（NEGF）[38][42]与材料筛选结合，实现"计算预测→实验验证"的闭环；
- 将层数依赖（1L→4L钉扎强度非单调变化[37]）、界面偶极[46]、SMIGS[5]等修正项纳入统一的修正Schottky-Mott规则。

---

## 结论

本报告的核心结论是：**二维半导体低接触电阻的各种方法虽然各有其理论表述，但存在一个共通的物理机制——降低金属在半导体带隙内引入的界面态密度以退钉扎费米能级，同时保证隧穿势垒足够薄。** 半金属接触通过零态密度和键饱和实现"能隙态饱和"；vdW接触通过物理间距抑制MIGS；相工程通过同质金属相消除异质界面问题；简并掺杂通过势垒变薄使隧穿压过势垒；边缘接触通过改变键合几何避免轨道重叠态。这五种路径本质上是在解决同一个"钉扎-隧穿权衡"问题的不同侧面。

目前文献中尚无定量统一所有策略的单一理论，但框架A-E（弱杂化、MIGS消除、金属相、界面态密度、多描述符）共同勾勒出一个综合图景的轮廓。未来方向应聚焦于：（1）基于"界面态光谱权重"概念的定量描述符构建；（2）半金属合金、2D金属、插层电极等新型接触材料的系统探索；（3）热稳定性与BEOL兼容性的工程突破（限域、合金化、封装）；（4）从单器件纪录走向统计性验证和可靠性认证。这一领域正处于从"经验性材料筛选"向"机制驱动的理性设计"转变的关键阶段。

---

### 来源

[1] Ultralow contact resistance between semimetal and monolayer semiconductors (Shen et al., Nature 2021): https://www.semanticscholar.org/paper/Ultralow-contact-resistance-between-semimetal-and-Shen-Su/6c5e2a9b0456c6b8c1e6b8ae0c89faecf226bfe9

[2] A Claim That TSMC Has a 1nm Process Hits the Headlines (Semiconductor Digest): https://www.semiconductor-digest.com/a-claim-that-tsmc-has-a-1nm-process-hits-the-headlines

[3] Antimony Semimetal Contact with Enhanced Thermal Stability for 2D Electronics (TSMC, IEEE IEDM 2021): https://hanwang6.github.io/Lab_Website/iedm_2021.pdf

[4] Approaching the quantum limit in two-dimensional semiconductor contacts (Li et al., Nature 2023): https://www.semanticscholar.org/paper/Approaching-the-quantum-limit-in-two-dimensional-Li-Gong/79ed9142e0a503055b5c4a4c4b77d1b5983eba6e

[5] Semimetal contacts to monolayer semiconductor: weak metalization as an effective mechanism to Schottky barrier lowering (Su et al., J. Phys. D 2023): http://ui.adsabs.harvard.edu/abs/2023JPhD...56w4001S/abstract

[6] Semimetal contacts to monolayer semiconductor (arXiv:2212.03003): https://arxiv.org/pdf/2212.03003

[7] Direct Visualization of Metal-Induced Gap State Distribution and Valley Band Evolution at Metal Versus Semimetal MoS2 Interfaces (Chen et al., ACS Nano 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12120976

[8] Schottky-barrier Injection research (Das et al., Nano Letters 2013, Appenzeller group): https://www.purdue.edu/discoverypark/nanotechnology/membership/Appenzeller/research_2d_sbfet.html

[9] Low Contact Resistance on Monolayer MoS2 Field-Effect Transistors Achieved by CMOS-Compatible Metal Contacts (Sun et al., ACS Nano 2024): https://par.nsf.gov/servlets/purl/10531719

[10] Uncovering the Effects of Metal Contacts on Monolayer MoS2 (Stanford, Pop group, arXiv:2007.14431): https://arxiv.org/pdf/2007.14431

[11] Phase-engineered low-resistance contacts for ultrathin MoS2 transistors (Kappera et al., Nature Materials 2014): https://www.semanticscholar.org/paper/Phase-engineered-low-resistance-contacts-for-MoS2-Kappera-Voiry/639d67e83ce5714200ebe21c69be72bbd5e553bf

[12] 1T phase as an efficient hole injection layer to TMDs transistors (Hu et al., 2D Materials 2018): https://krasheninnikov.de/publ/Hu_2018_2D_Mater._5_031012.pdf

[13] Tunable phase stability and contact resistance of monolayer transition metal dichalcogenides contacts with metal (Ouyang et al., npj 2D Materials and Applications 2018): https://www.nature.com/articles/s41699-018-0059-1

[14] Stable and scalable 1T MoS2 with low temperature-coefficient of resistance (Sharma et al., Scientific Reports 2018): https://www.nature.com/articles/s41598-018-30867-y

[15] Contact Resistance Optimization in MoS2 Field-Effect Transistors through Reverse Sputtering-Induced Structural Modifications (Fa et al., ACS AMI 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12022942

[16] Air-Stable Surface Charge Transfer Doping of MoS2 by Benzyl Viologen (Kiriya et al., JACS 2014): https://nano.eecs.berkeley.edu/publications/JACS_2014_MoS2-BV-doping.pdf

[17] Doping against the native propensity of MoS2: degenerate hole doping by cation substitution (Suh et al., Nano Letters 2014): https://www.academia.edu/20326639/Doping_against_the_native_propensity_of_MoS2_degenerate_hole_doping_by_cation_substitution

[18] New yttrium-doping strategy enhances 2D transistors (Jiang et al., Nature Electronics 2024): https://techxplore.com/news/2024-06-yttrium-doping-strategy-2d-transistors.html

[19] Making electrical contact along 1-D edge of 2-D materials (Wang et al., Science 2013): https://www.sciencedaily.com/releases/2013/10/131031142740.htm

[20] One-dimensional edge contacts to a monolayer semiconductor (Jain et al., Nano Letters 2019): https://www.semanticscholar.org/paper/One-dimensional-edge-contacts-to-a-monolayer-Jain-Szab%C3%B3/d4e1bed5adf038a314ac72ac08d93b8f68eb0729

[21] High-Performance Edge-Contact Monolayer Molybdenum Disulfide Transistors (Xiao et al., Research 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC11739435

[22] A Fermi-Level-Pinning-Free 1D Electrical Contact at the Intrinsic 2D MoS2–Metal Junction (Samudrala, Advanced Materials 2019): https://www.academia.edu/112480753/A_Fermi_Level_Pinning_Free_1D_Electrical_Contact_at_the_Intrinsic_2D_MoS2_Metal_Junction

[23] Fermi Level Pinning-Free 1D Electrical Contact at a Metal-2D Semiconductor Junction (Yang et al., GrapheneUS 2019): https://phantomsfoundation.com/GRAPHENEFORUS/2019/Abstracts/grapheneforus2019_Yang_Zheng_29.pdf

[24] One-Dimensional Edge Contacts to Two-Dimensional Transition-Metal Dichalcogenides (Parto et al., Physical Review Applied 2021): https://link.aps.org/doi/10.1103/PhysRevApplied.15.064068

[25] 3D Behavior of Schottky Barriers of 2D Transition-Metal Dichalcogenides (Guo, Liu, Robertson, Cambridge): https://www.repository.cam.ac.uk/bitstreams/4711c49c-2061-4c87-b5f3-89a671713bc1/download

[26] Approaching the Schottky–Mott limit in van der Waals metal–semiconductor junctions (Liu et al., Nature 2018): https://techtransfer.universityofcalifornia.edu/NCD/29749.html

[27] Van der Waals contacts between three-dimensional metals and two-dimensional semiconductors (Wang et al., Nature 2019): https://www.repository.cam.ac.uk/bitstreams/14aa1559-2115-46f7-b66f-2dc8e8f3eaac/download

[28] Low-Temperature Ohmic Contact to Monolayer MoS2 by van der Waals Bonded Co/h-BN Electrodes (Cui et al., Nano Letters 2017): https://ciqm.harvard.edu/uploads/2/3/3/4/23349210/cui_shin2017.pdf

[29] Interaction- and defect-free van der Waals contacts between metals and two-dimensional semiconductors (Kwon et al., Nature Electronics 2022): https://yonsei.elsevierpure.com/en/publications/interaction-and-defect-free-van-der-waals-contacts-between-metals

[30] Fermi-Level Pinning-Free WSe2 Transistors via 2D Van der Waals Metal Contacts (Cl-SnSe₂, Advanced Materials 2022): https://d-nb.info/1254874194/34

[31] The unusual mechanism of partial Fermi level pinning at metal-MoS2 interfaces (Gong et al., Nano Letters 2014): https://cgong.weebly.com/uploads/1/2/1/2/121277864/2014-nano_letter-the_unusual_mechanism_of_partial_fermi_level_pinning_at_metal%E2%88%92mos2_interfaces.pdf

[32] Universal Fermi-Level Pinning in Transition-Metal Dichalcogenides (Sotthewes et al., J. Phys. Chem. C 2019): https://pmc.ncbi.nlm.nih.gov/articles/PMC6410613

[33] Defect Dominated Charge Transport and Fermi Level Pinning in MoS2/Metal Contacts (Bampoulis et al., ACS AMI 2017): https://pmc.ncbi.nlm.nih.gov/articles/PMC5465510

[34] Brief Review of van der Waals Contact for Two-Dimensional Electronics (Jang & Park, ASCT 2026): https://www.e-asct.org/journal/view.html?uid=2097&vmd=Full

[35] MoS2 Transistors with Low Schottky Barrier Contact by Optimizing the Interfacial Layer Thickness (Energies 2022, TiO₂ MIS study): http://www.cityu.edu.hk/phy/appkchu/Publications/2022/22.90.pdf

[36] Monolayer MoS2-based transistors with low contact resistance by inserting ultrathin Al2O3 interfacial layer (Chen et al., Science China Tech. Sci. 2023): https://link.springer.com/article/10.1007/s11431-022-2330-3

[37] The Contact Properties of Monolayer and Multilayer MoS2-Metal van der Waals Interfaces (Pei et al., Nanomaterials 2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11243427

[38] Interfacial Properties of Monolayer and Bilayer MoS2 Contacts with Metals: Beyond the Energy Band Calculations (Zhong et al., Scientific Reports 2016): https://pmc.ncbi.nlm.nih.gov/articles/PMC4772071

[39] sp2 to sp3 hybridization transformation in 2D metal-semiconductor contact interface suppresses tunneling barrier and Fermi level pinning simultaneously (Shan et al., Nano Research 2024): https://link.springer.com/article/10.1007/s12274-024-6877-x

[40] Accumulation-Type Ohmic van der Waals Contacts to Nearly Intrinsic WSe2 (Andrews et al., OSTI): https://www.osti.gov/servlets/purl/1807195

[41] Van der Waals metal-semiconductor junction: Weak Fermi level pinning enables effective tuning of Schottky barrier (Liu, Stradins & Wei, Science Advances 2016): https://pmc.ncbi.nlm.nih.gov/articles/PMC4846439

[42] Fundamentals of low-resistive 2D-semiconductor metal contacts: an ab-initio NEGF study (Duflou, npj 2D Materials and Applications): http://materialscommunity.springernature.com/posts/fundamentals-of-low-resistive-2d-semiconductor-metal-contacts-an-ab-initio-negf-study

[43] The study on influence factors of contact properties of metal-MoS2 interfaces (Li et al., Solid-State Electronics 2024): https://www.sciencedirect.com/science/article/abs/pii/S0038110124001412

[44] Engineering of metal-MoS2 contacts to overcome Fermi level pinning (Khakbaz et al., Solid-State Electronics 2022): https://www.sciencedirect.com/science/article/abs/pii/S0038110122001502

[45] Analysis of Schottky barrier heights and reduced Fermi-level pinning in monolayer CVD-grown MoS2 (Xie et al., Nanotechnology 2022): https://par.nsf.gov/servlets/purl/10531719

[46] Fermi-Level Pinning Suppression in 2D Ferromagnetic Fe3GaTe2/MX2 Heterostructures (Zha et al., Applied Surface Science 2026): https://www.sciencedirect.com/science/article/abs/pii/S0169433226011712

[47] Layer-dependent Schottky contact at van der Waals interfaces: V-doped WSe2 on graphene (Stolz et al., npj 2D Materials and Applications 2022): https://www.nature.com/articles/s41699-022-00342-4

[48] Ultralow contact resistance between metal and semiconductor (Cong Su research page): https://www.congsu.net/research/ultralow-contact-resistance

[49] Achieving low contact resistance through copper-intercalated bilayer MoS2 electrodes (Wang et al., arXiv:2412.18385): https://arxiv.org/pdf/2412.18385

[50] Bismuth Confinement: A Strategy for Low Resistance and Good Thermal Endurance of Integrated Contacts to MoS2 (ACS Nano 2026): https://pmc.ncbi.nlm.nih.gov/articles/PMC13045353

[51] Contact engineering for temperature stability improvement of Bi-contacted MoS2 field effect transistors (Liu et al., Science China Information Sciences 2024): https://link.springer.com/article/10.1007/s11432-023-3942-2

[52] Sub-200 Ω·µm Alloyed Contacts to Synthetic Monolayer MoS2 (Kumar et al., IEEE IEDM 2021): https://www.semanticscholar.org/paper/Sub-200-%CE%A9%C2%B7%C2%B5m-Alloyed-Contacts-to-Synthetic-MoS2-Kumar-Schauble/ba5aaf71c726d876dcce9f5248c225a1d1d75f50

[53] Nonstoichiometric Salt Intercalation as a Means to Stabilize Alkali Doping of 2D Materials (Wang et al., PRL 2022): https://link.aps.org/doi/10.1103/PhysRevLett.129.266401

[54] One-dimensional semimetal contacts to two-dimensional semiconductors (Nature Communications 2023): https://www.nature.com/articles/s41467-022-35760-x
