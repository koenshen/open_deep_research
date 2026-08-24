# 碳钢缓蚀剂的拉曼活性与红外活性综合分析

## 一、分子振动光谱学基本原理：拉曼/红外活性判据

### 1.1 选择定则（Selection Rules）

判断一个分子或离子是否具有拉曼（Raman）活性或红外（IR）活性，依据的是振动模式是否引起分子某种物理性质的变化：

- **红外活性判据**：振动过程中若引起分子**偶极矩（dipole moment）变化**（dμ/dq ≠ 0），则该振动模式具有红外活性。在群论中，变换性质与x、y、z坐标相同的振动模式（即与偶极矩算符同对称性）为红外活性。
- **拉曼活性判据**：振动过程中若引起分子**极化率（polarizability）变化**（dα/dq ≠ 0），则该振动模式具有拉曼活性。变换性质与极化率张量分量（αxx、αyy、αzz、αxy、αxz、αyz，即x²、y²、z²、xy、xz、yz等二次函数）相同的振动模式为拉曼活性。

### 1.2 互斥规则（Mutual Exclusion Rule）

对于具有**对称中心（中心对称）**的分子，任何振动模式**不可能同时具有红外活性和拉曼活性**：对称（gerade, g）振动为拉曼活性，反对称（ungerade, u）振动为红外活性。这是因为偶极矩算符具有ungerade对称性，而极化率算符具有gerade对称性。

**重要推论**：对于**无对称中心**的分子（如Td、C2v、D3h点群），互斥规则不适用，某些振动模式可以同时具有红外活性和拉曼活性。碳钢缓蚀剂中的大多数无机阴离子（如CrO₄²⁻、PO₄³⁻、NO₃⁻、NO₂⁻）和几乎所有有机缓蚀剂分子均**无对称中心**，因此其振动模式通常可同时具备拉曼和红外活性，或至少部分模式同时具备两种活性。

### 1.3 典型实例

- **CO₂（D∞h，中心对称）**：对称伸缩（ν₁, 1388 cm⁻¹）仅拉曼活性；反对称伸缩和弯曲仅红外活性——体现互斥规则。
- **H₂O（C2v，非中心对称）**：所有三种振动模式（2A₁ + B₁）均同时为红外活性和拉曼活性。
- **CCl₄（Td）**：四种振动模式（A₁ + E + 2T₂）均为拉曼活性，其中T₂模式同时具有红外活性。

---

## 二、无机缓蚀剂

无机缓蚀剂在碳钢防腐中应用广泛，包括铬酸盐、钼酸盐、磷酸盐、硅酸盐、亚硝酸盐、硝酸盐、碳酸盐、硼酸盐、钒酸盐及稀土盐等。这些缓蚀剂大多以含氧酸根阴离子形式存在，其拉曼/红外活性由离子的几何构型和点群对称性决定。

### 2.1 铬酸盐（Chromate, CrO₄²⁻）与重铬酸盐（Cr₂O₇²⁻）

**分子结构特征**：铬酸根CrO₄²⁻为**四面体构型（Td点群）**，四个等价的Cr-O键。Td点群无对称中心，互斥规则不适用。铬酸盐是碳钢最有效的钝化型缓蚀剂之一，通过Cr⁶⁺还原为Cr³⁺形成保护性Cr₂O₃膜，具有自修复能力。

**振动模式与活性归属**（Td点群，3N−6 = 9个振动自由度，4种简正模式）：

| 振动模式 | 对称性 | 频率（cm⁻¹） | 拉曼活性 | 红外活性 |
|---------|--------|-------------|---------|---------|
| ν₁ 对称伸缩 | A₁ | ~847 | ✓（强） | ✗ |
| ν₂ 对称弯曲 | E | ~348 | ✓ | ✗ |
| ν₃ 反对称伸缩 | F₂ | ~890 | ✓ | ✓ |
| ν₄ 反对称弯曲 | F₂ | ~368 | ✓ | ✓ |

**结论**：CrO₄²⁻**两者兼有**（拉曼+红外均活性）。其中ν₁和ν₂仅拉曼活性，ν₃和ν₄同时具备两种活性。

**光谱学依据**：A₁全对称伸缩振动变换性质为x²+y²+z²（极化率分量），故仅拉曼活性；F₂反对称振动变换性质同时包含x,y,z（偶极矩分量）和xy,xz,yz（极化率分量），故两种活性兼有。

**文献数据**：Zhao等（Surface and Coatings Technology, 2001）用拉曼光谱表征铝合金上铬酸盐转化膜（CCC），发现四面体铬酸盐中心在858–859 cm⁻¹处有特征拉曼峰，表明Cr(III)-O-Cr(VI)共价键使四面体铬酸盐中心发生显著扰动。Ramsey等（Corrosion Science, 2001）通过高灵敏度拉曼光谱确认HCrO₄⁻在898 cm⁻¹处有特征谱带，是低浓度Cr(VI)（pH 5–6, <10⁻³ M）下的主要物种；Cr-O-Cr桥键的拉曼特征峰随Cr(VI)浓度降低而减弱。Avalos等（Analytica, 2025）综述指出，Cr(VI)的拉曼散射截面比Cr(III)大约3个数量级；Cr₂O₃的特征拉曼带位于~550–552 cm⁻¹（八面体配位Cr(III)的A1g Cr-O伸缩）。

**重铬酸盐（Cr₂O₇²⁻）**：含Cr-O-Cr桥键，无对称中心，桥键振动同时具有拉曼和红外活性。拉曼光谱可有效区分CrO₄²⁻/HCrO₄⁻/Cr₂O₇²⁻三种物种的平衡。

### 2.2 钼酸盐（Molybdate, MoO₄²⁻）

**分子结构特征**：钼酸根MoO₄²⁻为**四面体构型（Td点群）**。钼酸盐是铬酸盐的环境友好型替代品，通过形成不溶性铁钼酸盐使钢钝化，属阳极型缓蚀剂。

**振动模式与活性归属**（Td点群）：

| 振动模式 | 对称性 | 频率（cm⁻¹） | 拉曼活性 | 红外活性 |
|---------|--------|-------------|---------|---------|
| ν₁ 对称伸缩 | A₁ | ~901 | ✓（最强） | ✗ |
| ν₂ 对称弯曲 | E | ~380 | ✓ | ✗ |
| ν₃ 反对称伸缩 | F₂ | ~858 | ✓ | ✓ |
| ν₄ 反对称弯曲 | F₂ | ~320 | ✓ | ✓ |

**结论**：MoO₄²⁻**两者兼有**。ν₁对称伸缩在~901 cm⁻¹处为最强拉曼峰，ν₃反对称伸缩在~858 cm⁻¹处为最强红外峰。

**文献数据**：Molecules（2024）对Na₂MoO₄晶体的DFT计算确定，最高强度IR活性峰位于858 cm⁻¹（Mo-O反对称伸缩），最强拉曼峰位于901 cm⁻¹（对称伸缩）。Kharitonov等（Corrosion Science, 2021）通过拉曼光谱和XPS确定Na₂MoO₄在WE43镁合金上形成的保护性表面层由混合Mo(V)-Mo(VI)物种组成。需要注意的是，在晶体状态下（如尖晶石结构的Na₂MoO₄），由于晶格中心对称，IR活性与拉曼活性模式呈现互补关系。

### 2.3 钨酸盐（Tungstate, WO₄²⁻）

**分子结构特征**：钨酸根WO₄²⁻为**四面体构型（Td点群）**。钨酸盐与钼酸盐类似，可在钢表面形成不溶性保护膜。

**振动模式与活性归属**（Td点群）：

| 振动模式 | 对称性 | 频率（cm⁻¹） | 拉曼活性 | 红外活性 |
|---------|--------|-------------|---------|---------|
| ν₁ 对称伸缩 | A₁ | ~931 | ✓ | ✗ |
| ν₂ 对称弯曲 | E | ~405 | ✓ | ✗ |
| ν₃ 反对称伸缩 | F₂ | ~833 | ✓ | ✓ |
| ν₄ 反对称弯曲 | F₂ | ~318 | ✓ | ✓ |

**结论**：WO₄²⁻**两者兼有**。

**文献数据**：Burcham和Wachs（Spectrochimica Acta Part A, 1998）对Ce₂(WO₄)₃和La₂(WO₄)₃中两个非等价WO₄单元进行了振动分析，按Td点群对称性归属：A₁对称伸缩位于944/925 cm⁻¹（拉曼）和949/929 cm⁻¹（IR），F₂反对称伸缩位于840–707 cm⁻¹。Frost等（Spectrochimica Acta Part A, 2004）报道白钨矿（scheelite）的ν₁(Ag)拉曼峰位于909 cm⁻¹。

### 2.4 磷酸盐（Phosphate, PO₄³⁻）

**分子结构特征**：正磷酸根PO₄³⁻为**四面体构型（Td点群）**。磷酸盐转化涂层（磷化）是对碳钢最经典的化学处理方法之一，形成铁、锌或锰磷酸盐的薄附着层。锌磷酸盐涂层主要由hopeite（Zn₃(PO₄)₂）和磷叶石（phosphophyllite, Zn₂Fe(PO₄)₂）组成。

**振动模式与活性归属**（Td点群）：

| 振动模式 | 对称性 | 频率（cm⁻¹） | 拉曼活性 | 红外活性 |
|---------|--------|-------------|---------|---------|
| ν₁ 对称伸缩 | A₁ | ~950 | ✓（强） | ✗ |
| ν₂ 对称弯曲 | E | ~420 | ✓ | ✗ |
| ν₃ 反对称伸缩 | F₂ | ~1000–1100 | ✓ | ✓ |
| ν₄ 反对称弯曲 | F₂ | ~570 | ✓ | ✓ |

**结论**：PO₄³⁻**两者兼有**。注意：在锌磷酸盐转化膜的实际FTIR光谱中，1100–850 cm⁻¹区域可见871、976、1055 cm⁻¹峰（归属于PO/POH基团），976 cm⁻¹峰确认hopeite形成；1111 cm⁻¹峰（PO₄³⁻来自磷叶石）和969 cm⁻¹（P-O伸缩）也是特征标记。拉曼光谱中ν₁(PO₄)在~950 cm⁻¹处的强峰是确认Zn₃(PO₄)₂·2H₂O生成的标准工具。

**文献数据**：Burduhos-Nergis等（IOP Conf. Ser.: Mater. Sci. Eng., 2020）系统表征了锌和锰磷酸盐层的FTIR谱带。Simescu和Idrissi（Science and Technology of Advanced Materials, 2008）结合XRD确认锌磷酸盐涂层由hopeite和phosphophyllite两相组成。Corrosion Science（2025）研究进一步证实，在pH 2和70°C条件下，珠光体钢上高效形成由hopeite和磷叶石组成的磷酸盐涂层。

### 2.5 硅酸盐（Silicate, SiO₄⁴⁻）

**分子结构特征**：正硅酸根SiO₄⁴⁻为**四面体构型（Td点群）**，但实际缓蚀体系中硅酸盐常以聚合态存在（如硅酸钠SMS中的多种Qn物种）。硅酸钠是碳钢在中性介质中的有效阳极缓蚀剂。

**振动模式与活性归属**（Td点群，单体）：

| 振动模式 | 对称性 | 拉曼活性 | 红外活性 |
|---------|--------|---------|---------|
| ν₁ 对称伸缩 | A₁ | ✓ | ✗ |
| ν₂ 对称弯曲 | E | ✓ | ✗ |
| ν₃ 反对称伸缩 | F₂ | ✓ | ✓ |
| ν₄ 反对称弯曲 | F₂ | ✓ | ✓ |

**结论**：SiO₄⁴⁻单体**两者兼有**。但聚合硅酸盐网络振动更为复杂：Si-O-Si反对称伸缩在~1080–1100 cm⁻¹（红外强），Si-O-Si对称伸缩在~791/799 cm⁻¹（拉曼），Si-O(H)在~950 cm⁻¹（FTIR）和~980 cm⁻¹（拉曼）。

**文献数据**：Antony等（Zaštita Materijala, 2010）用FTIR确认硅酸钠-锌体系在碳钢表面形成的膜由铁-SMS络合物和Zn(OH)₂组成，Si-O伸缩合并于1116.58 cm⁻¹，Zn-O位于769.46 cm⁻¹，Fe-O位于495.62 cm⁻¹。Arabian Journal for Science and Engineering（2014）报道Na₃PO₄（1×10⁻² M）对低碳钢达95.5%保护效率，Na₂SiO₃（1×10⁻² M）达74.1%。

### 2.6 亚硝酸盐（Nitrite, NO₂⁻）

**分子结构特征**：亚硝酸根NO₂⁻为**弯曲构型（C2v点群）**，O-N-O键角约115°。C2v点群无对称中心，互斥规则不适用——**所有振动模式均同时具有红外活性和拉曼活性**。亚硝酸钠是碳钢在碱性介质中的阳极缓蚀剂，通过与溶解氧反应在金属表面形成保护性γ-Fe₂O₃或Fe₃O₄膜。

**振动模式与活性归属**（C2v点群，3N−6 = 3个振动自由度）：

| 振动模式 | 对称性 | 频率（cm⁻¹） | 拉曼活性 | 红外活性 |
|---------|--------|-------------|---------|---------|
| ν₁ 对称伸缩 | A₁ | ~1328 | ✓ | ✓ |
| ν₂ 弯曲 | A₁ | ~828 | ✓ | ✓ |
| ν₃ 反对称伸缩 | B₁ | ~1261 | ✓ | ✓ |

**结论**：NO₂⁻**两者兼有**（所有振动模式均为拉曼+红外双活性）。

**文献数据**：Weston和Brodasky（J. Chem. Phys., 1957）精确测定了微晶NaNO₂中NO₂⁻的基本频率：ν₁(a₁)=1328±2 cm⁻¹（N¹⁴），ν₂(a₁)=828.2±0.4 cm⁻¹，ν₃(b₁)=1261±3 cm⁻¹。Materials（2024）提出亚硝酸盐在碱性水中对碳钢抑制的新机制：NO₂⁻被电化学还原为NH₄⁺，促进保护性Fe₃O₄膜形成（总反应ΔG=−585.8 kJ/mol），XPS证实N 1s峰（399.8 eV）归属于NH₄⁺。

### 2.7 硝酸盐（Nitrate, NO₃⁻）与碳酸盐（Carbonate, CO₃²⁻）

**分子结构特征**：硝酸根NO₃⁻和碳酸根CO₃²⁻均为**平面三角形构型（D3h点群）**。D3h无对称中心，互斥规则不适用。硝酸盐和碳酸盐在碳钢缓蚀体系中通常作为辅助成膜组分或环境介质成分。

**振动模式与活性归属**（D3h点群，3N−6 = 6个振动自由度，4种简正模式）：

| 振动模式 | 对称性 | 拉曼活性 | 红外活性 |
|---------|--------|---------|---------|
| ν₁ 对称伸缩 | A₁′ | ✓ | ✗ |
| ν₂ 面外弯曲 | A₂″ | ✗ | ✓ |
| ν₃ 反对称伸缩 | E′ | ✓ | ✓ |
| ν₄ 面内弯曲 | E′ | ✓ | ✓ |

**结论**：NO₃⁻和CO₃²⁻均为**两者兼有**。ν₁对称伸缩（NO₃⁻在~1050 cm⁻¹，CO₃²⁻在~1086 cm⁻¹方解石中）仅拉曼活性；ν₂面外弯曲仅红外活性；ν₃和ν₄同时具备两种活性。

**光谱学依据**：A₁′模式变换性质为x²+y²（极化率），故仅拉曼活性；A₂″模式变换性质为z（偶极矩），故仅红外活性；E′简并模式同时包含(x,y)偶极矩分量和(x²−y², xy)极化率分量，故两种活性兼有。碳酸根/硝酸根与金属配位后对称性降至C2v，原本红外非活性的对称伸缩模式变为红外活性，双重简并E′模式分裂为两条谱带。

**文献数据**：碳酸盐矿物拉曼光谱研究（Minerals, 2023）表明方解石中CO₃²⁻对称伸缩在1086 cm⁻¹，随阳离子变化移至1060 cm⁻¹（毒重石）至1099 cm⁻¹（菱镁矿）。

### 2.8 硼酸盐（Borate）

**分子结构特征**：硼酸盐缓蚀剂以硼酸H₃BO₃（平面三角形，近似D3h）、硼砂Na₂B₄O₇·10H₂O和四羟基硼酸根B(OH)₄⁻（四面体）等形式存在。硼酸盐通过在金属表面形成保护性氧化层抑制腐蚀。

**结论**：**两者兼有**。H₃BO₃在880 cm⁻¹处有特征拉曼谱带（Metrohm应用说明），同时B-O伸缩振动在红外区域也有强吸收。硼酸盐的平面三角形B(OH)₃和四面体B(OH)₄⁻均无对称中心，振动模式可同时具备拉曼和红外活性。

### 2.9 钒酸盐（Vanadate, VO₄³⁻）

**分子结构特征**：正钒酸根VO₄³⁻为**四面体构型（Td点群）**，与CrO₄²⁻、MoO₄²⁻同构。钒酸盐基涂层通过抑制氧还原反应起作用，涂层由多种氧化态的钒氧化物组成。

**振动模式与活性归属**（Td点群）：

| 振动模式 | 对称性 | 拉曼活性 | 红外活性 |
|---------|--------|---------|---------|
| ν₁ 对称伸缩 | A₁ | ✓ | ✗ |
| ν₂ 对称弯曲 | E | ✓ | ✗ |
| ν₃ 反对称伸缩 | F₂ | ✓ | ✓ |
| ν₄ 反对称弯曲 | F₂ | ✓ | ✓ |

**结论**：VO₄³⁻**两者兼有**。Kharitonov等通过共聚焦拉曼显微光谱阐明了钒酸盐对铝合金的缓蚀机制，揭示V⁵⁺物种首先在阴极位点被还原为V⁴⁺或V³⁺。Milošev（Electrochimica Acta, 2024）报道钒酸盐以转化涂层形式提高点蚀电位。

### 2.10 稀土盐（Ce³⁺、La³⁺）

**分子结构特征**：稀土缓蚀剂以Ce³⁺/La³⁺离子形式使用，本身为原子离子无分子振动，但在钢表面形成的氧化物/氢氧化物沉淀可通过振动光谱检测。CeO₂具有面心立方萤石结构（空间群Fm3m，Oh点群，**中心对称**）。

**振动活性分析**：
- **CeO₂**：F₂g晶格振动模式（~465 cm⁻¹）为拉曼活性；由于萤石结构中心对称，互斥规则适用，LO模式为红外活性。CeO₂的拉曼信号极强，是优良的拉曼探针。
- **Ce(OH)₃沉淀**：Ce(III)物种在~450 cm⁻¹处有拉曼特征峰（Cotting & Aoki, JMRT, 2020）。
- **Ce₂(CO₃)₃·6H₂O**：碳酸铈沉淀中的CO₃²⁻振动兼具拉曼和红外活性。

**结论**：稀土盐形成的转化膜**两者兼有**（可通过拉曼检测CeO₂/Ce(OH)₃，通过红外检测碳酸铈及配位物种）。

**文献数据**：Corrosion Science and Technology（2025）报道Ce₂O₃在镀锌钢上形成由zincite（ZnO）、simonkolleite和碳酸铈Ce₂(CO₃)₃·6H₂O组成的富铈保护性钝化膜。DTIC报告ADA261016（1992）用FT-IR确认铈基表面层的主要表面相为勃姆石（AlOOH/Al₂O₃·H₂O）和不溶性氧化铈。

### 2.11 锌盐

**分子结构特征**：Zn²⁺本身为原子离子无振动模式，但在缓蚀体系中锌以Zn(OH)₂、ZnO或锌磷酸盐（Zn₃(PO₄)₂·2H₂O）形式沉积。锌磷酸盐转化膜的拉曼光谱确认其主要由二水合磷酸锌组成（DTIC报告ADA261016）。

**结论**：锌盐以化合物形式存在时**两者兼有**——Zn₃(PO₄)₂·2H₂O中PO₄³⁻的ν₁(PO₄)在~950 cm⁻¹有强拉曼峰，P-O伸缩在1000–1100 cm⁻¹有红外吸收，结晶水O-H伸缩在~3400 cm⁻¹红外强；Zn(OH)₂的FTIR谱带位于3756.65、1388.50、952.66 cm⁻¹，Zn-O位于769.46 cm⁻¹。

### 2.12 无机缓蚀剂拉曼/红外活性汇总表

| 缓蚀剂离子 | 点群 | 对称中心 | 拉曼活性 | 红外活性 | 总体结论 |
|-----------|------|---------|---------|---------|---------|
| CrO₄²⁻ 铬酸盐 | Td | 无 | ✓（ν₁,ν₂仅Raman；ν₃,ν₄兼有） | ✓（ν₃,ν₄） | **两者兼有** |
| Cr₂O₇²⁻ 重铬酸盐 | Cr-O-Cr桥 | 无 | ✓ | ✓ | **两者兼有** |
| MoO₄²⁻ 钼酸盐 | Td | 无 | ✓（ν₁ ~901 cm⁻¹强） | ✓（ν₃ ~858 cm⁻¹） | **两者兼有** |
| WO₄²⁻ 钨酸盐 | Td | 无 | ✓（ν₁ ~931 cm⁻¹） | ✓（ν₃ ~833 cm⁻¹） | **两者兼有** |
| PO₄³⁻ 磷酸盐 | Td | 无 | ✓（ν₁ ~950 cm⁻¹） | ✓（ν₃ ~1000–1100 cm⁻¹） | **两者兼有** |
| SiO₄⁴⁻ 硅酸盐 | Td | 无 | ✓（ν₁） | ✓（ν₃） | **两者兼有** |
| NO₂⁻ 亚硝酸盐 | C2v | 无 | ✓（全部3个模式） | ✓（全部3个模式） | **两者兼有** |
| NO₃⁻ 硝酸盐 | D3h | 无 | ✓（ν₁,ν₃,ν₄） | ✓（ν₂,ν₃,ν₄） | **两者兼有** |
| CO₃²⁻ 碳酸盐 | D3h | 无 | ✓（ν₁,ν₃,ν₄） | ✓（ν₂,ν₃,ν₄） | **两者兼有** |
| VO₄³⁻ 钒酸盐 | Td | 无 | ✓（ν₁,ν₃,ν₄） | ✓（ν₃,ν₄） | **两者兼有** |
| 硼酸盐/硼酸 | D3h/Td | 无 | ✓（~880 cm⁻¹） | ✓ | **两者兼有** |
| CeO₂/Ce(OH)₃ | Fm3m (Oh) | 有 | ✓（F₂g ~465 cm⁻¹） | ✓（LO模式） | **两者兼有**（晶体中互斥） |
| Zn₃(PO₄)₂·2H₂O | — | — | ✓（ν₁(PO₄) ~950 cm⁻¹） | ✓（P-O, O-H） | **两者兼有** |

---

## 三、有机缓蚀剂

有机缓蚀剂通过分子中的杂原子（N、O、S、P）孤对电子与金属表面配位，或通过π电子吸附形成保护膜。由于绝大多数有机缓蚀剂分子**无对称中心**，其振动模式通常可同时具备拉曼和红外活性，但不同官能团对两种光谱的响应强度有显著差异。

### 3.1 胺类（Amines）

**分子结构特征**：胺类缓蚀剂含-NH₂/-NH-/-N=基团和烷基链，通过N原子孤对电子吸附于钢表面。

**拉曼/红外活性分析**：
- **N-H伸缩**（~3300–3500 cm⁻¹）：红外活性强（N-H键极性大，偶极矩变化显著）；拉曼活性弱。
- **C-N伸缩**（~1000–1250 cm⁻¹）：红外和拉曼均中等活性。
- **C-H伸缩/弯曲**（~2850–2960 cm⁻¹，~1450 cm⁻¹）：红外和拉曼均活性，但拉曼对非极性C-H键响应更好。
- **结论**：**两者兼有**，但以红外活性为主（N-H、C-N极性键），拉曼信号主要来自C-H和C-C骨架振动。

### 3.2 咪唑啉类（Imidazolines）

**分子结构特征**：咪唑啉类缓蚀剂含五元咪唑啉环（-N=C-N-），带长烷基疏水链和亲水极性头基，是油气田碳钢CO₂腐蚀最常用的缓蚀剂类型。咪唑啉环的C=N键是吸附活性中心。

**拉曼/红外活性分析**：
- **C=N伸缩**（~1600–1650 cm⁻¹）：拉曼活性强（C=N键极化率变化大）；红外活性中等。
- **咪唑啉环骨架振动**（~1000–1500 cm⁻¹）：环伸缩和呼吸模式拉曼活性强。
- **长烷基链C-H**（~2850–2960 cm⁻¹）：拉曼和红外均强。
- **结论**：**两者兼有**。原位拉曼光谱可有效监测咪唑啉在钢表面的吸附——C=N峰位移动和强度变化指示配位作用；FTIR可检测N-H和C-H振动。

**文献数据**：Puzikova等（Journal of Saudi Chemical Society, 2025）综述了咪唑啉基缓蚀剂在金属表面形成疏水屏障的机制。Chen等（Materials, 2022）对有机缓蚀剂在HCl溶液中对碳钢的缓蚀进行了全面综述。

### 3.3 硫脲类（Thioureas）

**分子结构特征**：硫脲类缓蚀剂含-C(=S)-N-基团，S原子和N原子均为吸附活性位点。硫脲及其衍生物（如N-苯基硫脲壳聚糖）在酸性介质中对碳钢有高效缓蚀作用。

**拉曼/红外活性分析**：
- **C=S伸缩**（~1050–1250 cm⁻¹）：拉曼活性强（C=S键高度极化）；红外活性中等。
- **N-H伸缩**（~3200–3400 cm⁻¹）：红外活性强。
- **C-N伸缩**（~1250–1350 cm⁻¹）：红外和拉曼均活性。
- **结论**：**两者兼有**。C=S键是优异的拉曼探针基团，N-H键赋予强红外信号。

**文献数据**：Zhang等（Journal of Colloid and Interface Science, 2023）报道N-苯基硫脲壳聚糖（CS-PT）和N-苯基-O-苄基硫脲壳聚糖（CS-PT-Bn）对碳钢在酸性环境中的抑制效率分别达98.4%和98.5%，分子通过在钢/溶液界面形成Fe-N和Fe-S键以平行模式吸附。

### 3.4 羧酸类（Carboxylic Acids）

**分子结构特征**：羧酸类缓蚀剂含-COOH/-COO⁻基团，通过羧酸根与金属配位成膜。常见的有葡萄糖酸钠、柠檬酸、氨基酸等。

**拉曼/红外活性分析**：
- **C=O伸缩**（~1650–1750 cm⁻¹）：红外活性极强（C=O偶极矩变化大）；拉曼活性中等。
- **-COO⁻不对称伸缩**（~1550–1610 cm⁻¹）：红外强；拉曼中等。
- **-COO⁻对称伸缩**（~1400–1450 cm⁻¹）：红外和拉曼均中等。
- **O-H伸缩**（~2500–3300 cm⁻¹宽峰）：红外强。
- **结论**：**两者兼有**，以红外活性为主。羧酸根与金属配位后，-COO⁻对称/不对称伸缩的频率差（Δν）变化可用于判断配位模式。

### 3.5 醛类（Aldehydes）

**分子结构特征**：醛类缓蚀剂含-CHO基团（C=O + C-H），如肉桂醛、香草醛等芳香醛类在酸性介质中对碳钢有效。

**拉曼/红外活性分析**：
- **C=O伸缩**（~1680–1720 cm⁻¹）：红外强；拉曼中等（芳香醛C=O拉曼信号较好）。
- **醛基C-H伸缩**（~2700–2800 cm⁻¹费米共振双峰）：拉曼和红外均特征性强。
- **芳香环C=C伸缩**（~1580–1620 cm⁻¹）：拉曼强。
- **结论**：**两者兼有**。醛基的C-H费米双峰和芳香环C=C拉曼信号使其在两种光谱中均有清晰指纹特征。

### 3.6 唑类（Azoles）：苯并三唑（BTA）、巯基苯并噻唑（MBT）

**分子结构特征**：唑类缓蚀剂含五元芳香杂环（三唑、噻唑等），通过环上N/S原子与金属配位。苯并三唑（BTA）是铜及铜合金最经典的缓蚀剂；巯基苯并噻唑（MBT）含C=S和C-S-C基团。

**拉曼/红外活性分析**：
- **苯并三唑（C₆H₅N₃）**：含苯环+三唑环。苯环C=C伸缩（~1580–1600 cm⁻¹）和三唑环C=N伸缩（~1400–1500 cm⁻¹）拉曼活性强；N-H伸缩（~3300 cm⁻¹）红外强；三唑环呼吸模式（~1000–1100 cm⁻¹）拉曼特征显著。
- **巯基苯并噻唑（C₇H₅NS₂）**：含苯环+噻唑环+巯基。C=S伸缩（~1240–1280 cm⁻¹）拉曼强；S-H伸缩（~2550 cm⁻¹）拉曼特征（类似半胱氨酸）；芳香环C=C拉曼强。
- **结论**：**两者兼有**。唑类化合物因含芳香环和共轭体系，拉曼信号尤为突出，是SERS研究的经典对象。

**文献数据**：Haruna等（Heliyon, 2023）报道苯并三唑在铝合金上的SERS检测限（LOD）为1.2 ppm，表明唑类分子具有优异的拉曼散射截面。El Ibrahimi等（Arabian Journal of Chemistry）指出BTA因高毒性在全球范围内使用受限，半胱氨酸在中性/碱性溶液中物理吸附并伴轻微化学吸附，在酸性溶液（pH 2）中主要为化学吸附。

### 3.7 季铵盐类（Quaternary Ammonium Salts）

**分子结构特征**：季铵盐缓蚀剂含带正电荷的N⁺(R)₄和阴离子（如Cl⁻、Br⁻），通过静电吸附于带负电荷的钢表面。典型代表有苯扎氯铵、十六烷基三甲基溴化铵、咪唑鎓离子液体等。

**拉曼/红外活性分析**：
- **C-N⁺伸缩**（~900–1000 cm⁻¹）：拉曼活性中等；红外活性中等。
- **烷基链C-H伸缩**（~2850–2960 cm⁻¹）：拉曼和红外均强。
- **甲基对称变形**（~1480 cm⁻¹）：拉曼和红外均活性。
- **芳香环（若含苄基）C=C**（~1600 cm⁻¹）：拉曼强。
- **结论**：**两者兼有**。Pailleret等（Corrosion Science, 2023）用原位拉曼光谱研究了季铵盐缓蚀剂在碳钢表面的吸附行为。

### 3.8 有机缓蚀剂拉曼/红外活性汇总表

| 缓蚀剂类别 | 关键官能团 | 拉曼活性来源 | 红外活性来源 | 总体结论 |
|-----------|-----------|-------------|-------------|---------|
| 胺类 | -NH₂, C-N | C-C/C-H骨架、C-N | N-H伸缩、C-N | **两者兼有**（IR为主） |
| 咪唑啉类 | C=N, 长烷基链 | C=N伸缩（~1600–1650 cm⁻¹）、环振动 | N-H、C-H、C=N | **两者兼有** |
| 硫脲类 | C=S, -NH₂ | C=S伸缩（~1050–1250 cm⁻¹）强 | N-H伸缩、C=S | **两者兼有** |
| 羧酸类 | -COOH/-COO⁻ | C-C/C-H骨架 | C=O（~1700 cm⁻¹）极强、O-H | **两者兼有**（IR为主） |
| 醛类 | -CHO, 芳香环 | 芳香环C=C、C-H费米双峰 | C=O（~1680–1720 cm⁻¹） | **两者兼有** |
| 苯并三唑 | 苯环+三唑环 | 芳香环C=C、C=N、环呼吸 | N-H、C=N | **两者兼有**（Raman强） |
| 巯基苯并噻唑 | 苯环+噻唑环+C=S | C=S、S-H（~2550 cm⁻¹）、芳香环 | N-H、C=S | **两者兼有**（Raman强） |
| 季铵盐 | N⁺(R)₄ | C-H、C-N⁺、芳香环 | C-H、C-N⁺ | **两者兼有** |

---

## 四、天然有机缓蚀剂

天然有机缓蚀剂（植物提取物、生物大分子等）因环保、可生物降解而成为研究热点。其拉曼/红外活性取决于所含官能团的种类——芳香环和共轭体系主导拉曼光谱，极性含氧/含氮取代基主导红外光谱。

### 4.1 植物多酚类：单宁酸、绿茶提取物

**分子结构特征**：单宁酸（Tannic Acid）是葡萄糖核心上连接多个没食子酰基的聚没食子酰基酯，含大量酚羟基（-OH）、酯羰基（-C=O）、芳香环和C-O-C键。绿茶提取物的主要活性成分为儿茶素类多酚（EGCG、ECG、EGC、EC），含多个芳香环、共轭C=C体系、酚羟基和C-O-C醚键。

**拉曼/红外活性分析**：
- **芳香环C=C伸缩**（~1600 cm⁻¹）：拉曼活性极强（苯环振动主导拉曼光谱）。
- **酯C=O伸缩**（~1704–1711 cm⁻¹）：拉曼活性强（单宁酸的酯ν(C=O)带在1704 cm⁻¹）；红外活性强。
- **酚羟基O-H伸缩**（~3200–3500 cm⁻¹）：红外活性强。
- **C-O-C醚键**（~1100–1300 cm⁻¹）：红外活性中等；拉曼中等。
- **结论**：**两者兼有**——拉曼光谱由苯环振动主导，FTIR光谱由芳香环的外围含氧取代基主导，两种光谱提供互补信息。

**文献数据**：Espina等（Molecules, 2022）对单宁酸（TA）、没食子酸（GA）、邻苯三酚（PY）和丁香酸（SA）进行了FT-Raman、FTIR、SERS和UV-Vis对比振动分析，明确指出"拉曼光谱主要由苯环振动主导，而FTIR光谱主要由芳香环的外围含氧取代基主导"。单宁酸的拉曼光谱在1711和1613 cm⁻¹处显示强带（C=O伸缩和8a苯环振动）。ACS Omega（2022）进一步报道铁-多酚络合物的三个主要拉曼带位于1450–1490 cm⁻¹（ν1）、1320–1345 cm⁻¹（ν2）和400–650 cm⁻¹（ν3）。Raj等（Applied Sciences, 2022）用ATR-FTIR表征了单宁酸负载羟基磷灰石载体。Journal of Materials Research and Technology报道了使用SEM、FT-IR、**Raman**、EDS、XPS检验碳钢上单宁酸转化涂层（TACC）的形貌与组成。Alsabagh等（Int. J. Electrochem. Sci., 2015）用FTIR确认绿茶提取物中儿茶素官能团（O-H、C=C芳香环和C-O键），500 ppm浓度在1M HCl中抑制效率达81.47%。

### 4.2 氨基酸类

**分子结构特征**：氨基酸含至少一个羧基（-COOH）和一个氨基（-NH₂）连接在同一α-碳上。半胱氨酸含独特的S-H键和C-S键；蛋氨酸含C-S-C；组氨酸含咪唑环；色氨酸含吲哚环；胱氨酸含二硫键（-S-S-）。

**拉曼/红外活性分析**：
- **-NH₂伸缩**（~3300–3500 cm⁻¹）：红外强；拉曼弱。
- **-COOH C=O伸缩**（~1700 cm⁻¹）：红外强；拉曼中等。
- **C-S伸缩**（~600–750 cm⁻¹）：**拉曼强**（C-S键极化率变化大）；红外弱。
- **S-H伸缩**（~2543–2574 cm⁻¹）：**拉曼特征**（半胱氨酸S-H···O和S-H···S两种构象分别位于2543和2574 cm⁻¹）；红外弱。
- **S-S伸缩**（~500–545 cm⁻¹）：**拉曼特征**（胱氨酸及蛋白质二硫键）；红外弱。
- **芳香环（组氨酸咪唑环、色氨酸吲哚环）**：拉曼强。
- **结论**：**两者兼有**——氨基酸同时含有极性基团（-NH₂、-COOH赋予红外活性）和C-S、S-S、芳香环等拉曼活性基团。

**文献数据**：Bazylewski等（RSC Advances, 2017）通过原位拉曼光谱区分了半胱氨酸的S-H伸缩构象（2543 cm⁻¹和2574 cm⁻¹）。Adar（Spectroscopy, 2022）系统总结了蛋白质/氨基酸拉曼光谱解读：二硫键-S-S-伸缩在~500 cm⁻¹，游离-SH在2500–2600 cm⁻¹，酪氨酸Fermi双峰在~860/830 cm⁻¹，色氨酸Fermi双峰在~1360–1340 cm⁻¹。Święch等（Coatings, 2021）使用拉曼光谱（RS）、FT-IR、SERS和SEIRA研究了色氨酸对316L不锈钢在模拟炎症条件下的缓蚀作用，发现Fermi双峰强度比（I₁₃₅₇/I₁₃₃₈=1.8）表明吸附期间更强的疏水环境与改善的耐蚀性相关。El Ibrahimi等（Arabian Journal of Chemistry）对氨基酸缓蚀剂进行了全面综述：半胱氨酸在铜表面形成Cu(I)-半胱氨酸络合物膜，蛋氨酸在1N H₂SO₄中为最佳氨基酸缓蚀剂，色氨酸是1M HCl中最好的常见氨基酸。

### 4.3 壳聚糖及其衍生物

**分子结构特征**：壳聚糖是由甲壳素脱乙酰化得到的天然多糖，含大量-OH（~3400 cm⁻¹红外强）、-NH₂（~3300–3500 cm⁻¹红外强）、酰胺I（C=O，~1650 cm⁻¹）、酰胺II（N-H弯曲，~1550–1560 cm⁻¹）和C-O-C糖苷键（~1000–1150 cm⁻¹）。通过Schiff碱反应改性可引入C=N键、C-S键和芳香环。

**拉曼/红外活性分析**：
- **O-H和N-H伸缩**（~3300–3500 cm⁻¹）：红外极强。
- **酰胺I（C=O）**（~1650 cm⁻¹）：红外强；拉曼中等。
- **C=N（Schiff碱）**（~1630–1650 cm⁻¹）：拉曼活性强；红外中等。
- **C-S键**（~1079 cm⁻¹）：拉曼活性强（壳聚糖-蛋氨酸衍生物中确认）。
- **芳香环（靛红改性等）**：拉曼强。
- **结论**：**两者兼有**。改性后引入的C=N、C-S和芳香环显著增强拉曼信号。

**文献数据**：Modwi等（Journal of Molecular Structure, 2025）用FT-IR和¹H NMR表征靛红-壳聚糖Schiff碱，对Q235碳钢在1.0 M HCl中最大抑制效率88.4%。Hamza等（Scientific Reports, 2025）对壳聚糖-蛋氨酸衍生物的FT-IR确认：NH₃⁺在~3375 cm⁻¹，C=O伸缩在~1569 cm⁻¹，C-S峰在1079 cm⁻¹；100 ppm时抑制效率达99.8%。

### 4.4 海藻酸钠（Sodium Alginate）

**分子结构特征**：海藻酸钠是从褐藻中提取的天然多糖，为α-L-甘露糖醛酸（M单元）和β-D-古洛糖醛酸（G单元）通过1,4-糖苷键连接的共聚物，含大量-COOH/-COO⁻和-OH基团。

**拉曼/红外活性分析**：
- **-COO⁻不对称伸缩**（~1600–1650 cm⁻¹）：红外强。
- **-COO⁻对称伸缩**（~1400 cm⁻¹）：红外和拉曼均中等。
- **-OH伸缩**（~3400 cm⁻¹）：红外强。
- **C-O-C糖苷键**（~1000–1150 cm⁻¹）：红外和拉曼均活性。
- **结论**：**两者兼有**，但以红外活性为主。羧酸根与金属配位作用可通过FTIR中-COO⁻对称/不对称伸缩的位移监测。

**文献数据**：Al-Bonayan（Int. J. Scientific & Engineering Research, 2014）报道海藻酸钠在0.5 M HCl中对碳钢为混合型缓蚀剂。中国专利CN102140641A（中国科学院海洋研究所）公开了海藻酸钠绿色缓蚀剂，0.5 g/L在3.5% NaCl中抑制效率>90%。

### 4.5 大蒜提取物（含硫化合物）

**分子结构特征**：大蒜提取物的活性成分为含硫化合物——蒜氨酸（alliin）、大蒜素（allicin）、二烯丙基硫醚（DAS）、二烯丙基二硫醚（DADS）、二烯丙基三硫醚（DATS）等，含C-S、S-S、S=O键及烯丙基C=C键。大蒜含硫化合物比例高达13%。

**拉曼/红外活性分析**：
- **C-S伸缩**（~600–750 cm⁻¹）：**拉曼强**（FTIR确认720.67 cm⁻¹处C-S峰）。
- **S-S伸缩**（~500 cm⁻¹）：**拉曼强**（大蒜素、DADS中）。
- **S=O伸缩**（~1044 cm⁻¹）：红外强（FTIR确认1044.28 cm⁻¹处S=O峰）。
- **C=C烯丙基**（~1640 cm⁻¹）：拉曼中等；红外中等。
- **羰基C=O**（~1618 cm⁻¹）：红外强。
- **结论**：**两者兼有**——含硫化合物的C-S和S-S键对拉曼散射截面大，信号强；S=O和C=O极性基团赋予强红外信号。

**文献数据**：ACS Omega（2025）从大蒜皮合成碳量子点（CQDs）作为低碳钢在1 mol L⁻¹ HCl中的绿色缓蚀剂，FTIR和XPS确认C-S、C=O、COOH等官能团，24小时后抑制效率达96%。Guma和Aremo（IJAEM, 2025）综述了大蒜缓蚀研究：大蒜精油在1M HCl中2.5 g/L时达95.8%抑制效率；大蒜+可可提取物混合物>98%显示强协同作用。

### 4.6 槟榔提取物（生物碱类）

**分子结构特征**：槟榔提取物的主要活性成分为槟榔碱（arecoline，C₈H₁₃NO₂），是1-甲基-1,2,5,6-四氢吡啶-3-羧酸甲酯，含吡啶环（C=N）、四氢吡啶环（C=C）、酯基（-COOCH₃）和叔胺C-N。槟榔果实还含大量多酚（31.1%）、单宁（约15%）和黄酮类。

**拉曼/红外活性分析**：
- **吡啶环C=N/C=C伸缩**（~1400–1600 cm⁻¹）：拉曼活性强（芳香杂环拉曼散射截面大）。
- **酯C=O伸缩**（~1700 cm⁻¹）：红外强。
- **C-N伸缩**（~1000–1250 cm⁻¹）：红外和拉曼均活性。
- **多酚芳香环**：拉曼强；酚羟基：红外强。
- **结论**：**两者兼有**——生物碱的C=N和芳香杂环赋予拉曼活性，酯基和酚羟基赋予红外活性。

**文献数据**：Xiao等（Biomedical Research and Reviews, 2019）系统分析了槟榔的化学成分：酚类31.1%、多糖18.7%、生物碱0.3–0.6%，主要生物碱为槟榔碱、槟榔次碱、去甲槟榔碱和去甲槟榔次碱。Huang等（Foods, 2024）报道槟榔果含约20种吡啶生物碱。

### 4.7 柑橘/橙皮提取物（萜烯类）

**分子结构特征**：橙皮提取物的主要活性成分为柠檬烯（limonene，单萜烯，占橙皮精油95.19%）、橙皮苷（hesperidin，黄酮类，含芳香环、-OH、-OCH₃、C=O）和果胶（多糖，含-COOH/-COO⁻和-OH）。

**拉曼/红外活性分析**：
- **C=C双键（柠檬烯）**（~1640–1680 cm⁻¹）：拉曼强。
- **芳香环（黄酮类）C=C**（~1580–1620 cm⁻¹）：拉曼强。
- **-OH、C=O、-COOH**：红外强。
- **结论**：**两者兼有**。FTIR确认萜类化合物（主要为柠檬烯）的存在，同时检测到醚类、醇类和不饱和结构特征。

**文献数据**：Elazabawy等（Scientific Reports, 2023）报道橙皮提取物对碳钢在石油地层水中的抑制效率达90.13%（2.5% v/v，25°C），遵循Langmuir吸附等温线，ΔG°ads为−13.874 kJ/mol（物理吸附）。Salamah等（Pharmacia, 2024）用ATR-FTIR结合化学计量学鉴别柑橘皮精油，最佳PLS波数区域为1650–1450 cm⁻¹。

### 4.8 其他植物提取物

**曼陀罗叶提取物**：Mpelwa（Surface Science and Technology, 2026）报道其对低碳钢在1M HCl中的最大抑制效率96.7%（500 ppm）。FTIR识别出羟基（-OH）、羰基（C=O）、胺基（-NH）、醚键（C-O-C）和共轭C=C官能团——**两者兼有**（O-H、C=O红外强；C=C、芳香环拉曼强）。

**胡萝卜+迷迭香提取物协同**：Ghanbari Daryaee等（ChemEngineering, 2025）报道30/70（胡萝卜/迷迭香）混合物在800 ppm下达99.6%抑制效率，协同指数（SI）高达14.41（48h）。两种提取物均含多酚、萜类和黄酮类——**两者兼有**。

---

## 五、复合缓蚀剂

复合缓蚀剂（多种缓蚀剂复配使用）在工业实践中广泛应用，通过协同效应实现优于单一组分的保护性能。以下对典型复合体系逐一分析各组分的拉曼/红外活性，再进行综合总结。

### 5.1 钼酸盐 + HEDP + Zn²⁺ + 葡萄糖酸钠复配体系

**体系背景**：芮玉兰等（Corrosion & Protection, 2007）研究了复合钼酸盐对碳钢在海水中缓蚀作用：单一钼酸盐浓度低于30 mg/L时反而加剧腐蚀，但**40 mg/L钼酸盐+10 mg/L HEDP+4 mg/L Zn²⁺+50 mg/L葡萄糖酸钠**组合的抑制效率超过90%，在碳钢表面形成主要由氧化铁（含少量Mo和P）组成的致密膜。

**各组分拉曼/红外活性分析**：

| 组分 | 关键基团 | 拉曼活性 | 红外活性 |
|------|---------|---------|---------|
| MoO₄²⁻ 钼酸盐 | Mo-O四面体 | ✓ ν₁ ~895–901 cm⁻¹（强） | ✓ ν₃ ~830–858 cm⁻¹ |
| HEDP（有机磷酸盐） | P=O, P-OH, C-P | ✓ P-O ~950 cm⁻¹ | ✓ P=O ~1200–1250 cm⁻¹、P-O ~1000–1100 cm⁻¹ |
| Zn²⁺ | Zn(OH)₂/ZnO沉淀 | ✓ Zn-O ~300–400 cm⁻¹ | ✓ Zn-O ~769 cm⁻¹ |
| 葡萄糖酸钠 | -OH, -COO⁻ | ✓ C-C/C-O骨架 | ✓ -OH ~3300 cm⁻¹、-COO⁻ ~1590/1400 cm⁻¹ |

**综合总结**：该复合体系**整体两者兼有**。拉曼光谱可有效检测MoO₄²⁻的ν₁对称伸缩（~895 cm⁻¹）和HEDP的P-O伸缩（~950 cm⁻¹），原位拉曼可通过Mo-O峰强度变化跟踪钼酸盐的吸附成膜过程；FTIR可检测HEDP的P=O/P-O、葡萄糖酸钠的-COO⁻和-OH，以及Fe₂(MoO₄)₃形成后Mo-O键的变化。

### 5.2 稀土铈 + 氨基酸/硅烷醇复配体系

**体系背景**：Liu Xia等（Journal of Central South University, 2018）发现CeCl₃和丝氨酸单独使用对碳钢在3% NaCl中缓蚀效果有限，组合后产生强协同效应，SEM和FTIR揭示协同效应源于铈离子与氨基酸分子在金属表面形成稀土离子-氨基酸络合物膜。Cotting和Aoki（Journal of Materials Research and Technology, 2020）报道400 ppm辛基硅烷醇+50 ppm Ce(III)离子对1020碳钢在0.1 mol L⁻¹ NaCl中抑制效率约96–97.8%。

**各组分拉曼/红外活性分析**：

| 组分 | 关键基团 | 拉曼活性 | 红外活性 |
|------|---------|---------|---------|
| Ce³⁺/Ce(OH)₃/CeO₂ | Ce-O晶格振动 | ✓ ~450–465 cm⁻¹（强） | ✓（LO模式） |
| 丝氨酸 | -NH₂, -COOH | ✓ C-C骨架 | ✓ -NH₂ ~3300 cm⁻¹、-COOH ~1700 cm⁻¹ |
| 辛基硅烷醇 | Si-OH, Si-O-C | ✓ Si-O ~1000–1100 cm⁻¹ | ✓ Si-O ~1000–1100 cm⁻¹、Si-OH |

**综合总结**：该复合体系**整体两者兼有**。Cotting和Aoki的拉曼光谱确认了钢表面持久吸附的硅烷醇膜（Si-OH和Si-O-C伸缩峰）和氢氧化铈沉淀（Ce(III)峰在~450 cm⁻¹）——原位拉曼可同时检测双组分在阴极/阳极位点的协同吸附行为。FTIR可检测氨基酸-铈络合物形成时-COO⁻与Ce³⁺配位导致的峰位移。

### 5.3 锌盐 + 磷酸盐体系（磷化处理）

**体系背景**：锌磷酸盐转化涂层是碳钢最经典的磷化处理体系。DTIC报告ADA261016（1992）用拉曼和显微拉曼光谱确认未改性和PAA改性膜均主要由二水合磷酸锌Zn₃(PO₄)₂·2H₂O组成。

**各组分拉曼/红外活性分析**：

| 组分 | 关键基团 | 拉曼活性 | 红外活性 |
|------|---------|---------|---------|
| Zn₃(PO₄)₂·2H₂O | PO₄³⁻ + 结晶水 | ✓ ν₁(PO₄) ~950 cm⁻¹（强） | ✓ P-O ~1000–1100 cm⁻¹、O-H ~3400 cm⁻¹ |
| Zn₂Fe(PO₄)₂（磷叶石） | PO₄³⁻ | ✓ ν₁(PO₄) ~969 cm⁻¹ | ✓ P-O ~1111 cm⁻¹ |
| 聚丙烯酸PAA（改性剂） | -COOH, C=O | ✓ C-C骨架 | ✓ C=O ~1700 cm⁻¹ |

**综合总结**：该体系**整体两者兼有**。拉曼光谱的ν₁(PO₄)强峰（~950 cm⁻¹）是确认磷酸锌涂层生成的经典判据；FTIR可补充检测结晶水（~3400 cm⁻¹）、P-O振动（1000–1100 cm⁻¹）以及PAA改性剂的C=O。

### 5.4 杀菌剂 + 缓蚀剂复合体系

**体系背景**：Anandkumar等（Journal of Environmental Chemical Engineering, 2023）研究了杀菌剂（苯扎氯铵、bronopol、异噻唑啉）与缓蚀剂（ZnCl₂、H₃PO₄、Na₂MoO₄和离子液体1-丁基-3-甲基咪唑氯化物IL）的组合，电化学分析显示混合缓蚀剂约98%的缓蚀效率，**表面分析（XPS、激光拉曼光谱LRS、GDOES）确认了缓蚀剂在金属表面的吸附**。DFT计算在Fe(110)表面的吸附能顺序：H₃PO₄(−9.73 eV) > IL(−2.46 eV) > Na₂MoO₄(−2.14 eV) > ZnCl₂(−1.94 eV)。

**各组分拉曼/红外活性分析**：

| 组分 | 关键基团 | 拉曼活性 | 红外活性 |
|------|---------|---------|---------|
| ZnCl₂ | Zn-Cl键（远红外） | ✓（远红外区 <300 cm⁻¹） | ✓（远红外区） |
| H₃PO₄ | P=O, P-OH | ✓ P-O ~950 cm⁻¹ | ✓ P=O ~1200 cm⁻¹、P-OH ~1000 cm⁻¹ |
| Na₂MoO₄ | MoO₄²⁻ | ✓ ν₁ ~895 cm⁻¹（强） | ✓ ν₃ ~830 cm⁻¹ |
| 咪唑鎓离子液体 | 咪唑环C=N/C=C | ✓ ~1550–1600 cm⁻¹（强） | ✓ C-H ~2900–3100 cm⁻¹、C=N |
| 苯扎氯铵 | 苄基+季铵N⁺ | ✓ 芳香环C=C ~1600 cm⁻¹ | ✓ C-N⁺、C-H |

**综合总结**：该复合体系**整体两者兼有**。激光拉曼光谱（LRS）在该研究中直接用于确认多种组分的共存吸附——MoO₄²⁻的~895 cm⁻¹峰、咪唑环的~1550–1600 cm⁻¹峰和磷酸根的P-O振动可同时被检测。FTIR可补充检测P=O、P-OH和咪唑鎓的C-H/N-H振动。

### 5.5 复合缓蚀剂的光谱检测策略总结

**复合体系中各组分的特征振动峰在拉曼和红外光谱中的检测分工**：

| 组分类型 | 拉曼特征峰（cm⁻¹） | 红外特征峰（cm⁻¹） |
|---------|-------------------|-------------------|
| 钼酸盐 MoO₄²⁻ | ν₁ ~895（强） | ν₃ ~830 |
| 磷酸盐/磷酸根 | ν₁(PO₄) ~950（强） | ν₃(PO₄) ~1000–1100（强） |
| 锌磷酸盐 Zn₃(PO₄)₂·2H₂O | ν₁(PO₄) ~950 | P-O ~1000–1100、O-H ~3400 |
| Ce(OH)₃/CeO₂ | ~450–465 | — |
| 硅烷醇 | Si-O ~1000–1100 | Si-O ~1000–1100、Si-OH |
| 咪唑啉/咪唑鎓 | C=N ~1600–1650 | C-H ~2850–2960 |
| 苯并三唑 | 三唑环/苯环 ~1000–1600 | N-H、C=N |
| 氨基酸 | C-C骨架、-S-S- ~500（半胱氨酸） | -NH₂ ~3300、-COOH ~1700 |
| 葡萄糖酸钠 | C-C/C-O | -OH ~3300、-COO⁻ ~1590/1400 |

**原位光谱技术的应用**：Haruna等（Heliyon, 2023）首次使用SERS检测缓蚀剂分子在碳钢（非等离激元材料）表面的吸附，采用AgNPs锚定透明胶带传感器检测AEP-GO在15% HCl中X60碳钢表面的吸附，在1320 cm⁻¹（D带）和1583 cm⁻¹（G带）显示特征拉曼峰，LOD远低于1 ppm。该技术"无基材限制，可用于跟踪缓蚀剂在任何金属上的动态吸附"。Wasatch Photonics/Spectroscopy Online（2022）报道了原位拉曼在盐雾箱内监测低碳钢腐蚀过程：α-FeO(OH)针铁矿（297、378 cm⁻¹）、α-Fe₂O₃赤铁矿（289、402、489、604 cm⁻¹）、Fe₃O₄磁铁矿（647 cm⁻¹）、FeCO₃菱铁矿（1078 cm⁻¹）和γ-FeO(OH)纤铁矿（306、346、376、525 cm⁻¹）的指纹带可用于区分缓蚀剂保护前后钢表面的腐蚀状态。

---

## 六、综合总结

### 6.1 核心结论

**（1）无机缓蚀剂**：绝大多数无机缓蚀剂阴离子（CrO₄²⁻、MoO₄²⁻、WO₄²⁻、PO₄³⁻、SiO₄⁴⁻、VO₄³⁻、NO₂⁻、NO₃⁻、CO₃²⁻）均为**无对称中心的对称性离子**（Td、C2v、D3h点群），互斥规则不适用，因此**整体上均同时具有拉曼活性和红外活性**。具体模式归属有差异：Td离子的ν₁对称伸缩仅拉曼活性、ν₃反对称伸缩两种活性兼有；D3h离子的ν₁仅拉曼活性、ν₂仅红外活性；C2v离子的所有模式两种活性兼有。

**（2）有机缓蚀剂**：有机缓蚀剂分子（胺类、咪唑啉类、硫脲类、羧酸类、醛类、唑类、季铵盐类）几乎均为**无对称中心**的非中心对称分子，因此**整体上两者兼有**。但不同官能团对两种光谱的响应强度差异显著：芳香环、C=C、C=N、C-S、S-S、S-H键赋予强拉曼信号；-OH、-NH₂、-COOH、-C=O、-NO₂等极性基团赋予强红外信号。

**（3）天然有机缓蚀剂**：植物提取物（多酚、生物碱、萜烯）和生物大分子（壳聚糖、海藻酸钠、氨基酸）同样**两者兼有**——拉曼光谱由芳香环/共轭体系主导，红外光谱由极性含氧/含氮取代基主导，两种光谱提供互补的结构信息。

**（4）复合缓蚀剂**：复合体系中**每种组分均需分别分析**。拉曼光谱擅长检测含芳香环、C=N/C=S、C-S/S-S、Mo-O、P-O等基团的组分（如咪唑啉、苯并三唑、钼酸盐、磷酸盐）；红外光谱擅长检测含-OH、-NH₂、-COOH、C=O等极性基团的组分（如氨基酸、葡萄糖酸钠、HEDP、壳聚糖）。两种技术联用可实现复合体系中全组分的覆盖检测。

### 6.2 光谱学依据的核心规则

- **红外活性** ↔ 振动引起偶极矩变化（dμ/dq ≠ 0）↔ 变换性质与x,y,z相同
- **拉曼活性** ↔ 振动引起极化率变化（dα/dq ≠ 0）↔ 变换性质与x²,y²,z²,xy,xz,yz相同
- **互斥规则**：中心对称分子中，IR活性与Raman活性互斥（如CeO₂萤石晶体中F₂g模式仅拉曼活性）
- **无对称中心分子**（Td、C2v、D3h点群及大多数有机分子）：部分或全部振动模式可同时具有两种活性

### 6.3 实用建议

在碳钢缓蚀剂的实际光谱表征中：
1. **拉曼光谱**特别适合检测含芳香环/共轭体系的有机缓蚀剂（唑类、咪唑啉、多酚）和含氧酸根无机缓蚀剂（钼酸盐ν₁~895 cm⁻¹、磷酸盐ν₁~950 cm⁻¹、铬酸盐~858 cm⁻¹）的吸附成膜。
2. **红外光谱**特别适合检测含极性基团的缓蚀剂（羧酸类C=O~1700 cm⁻¹、胺类N-H~3300 cm⁻¹、壳聚糖酰胺I~1650 cm⁻¹）以及腐蚀产物（Fe-O~495 cm⁻¹、Zn-O~769 cm⁻¹）。
3. **SERS技术**可突破拉曼灵敏度的限制，实现痕量缓蚀剂（低至1 ppm级）在碳钢表面的原位吸附检测。
4. **原位拉曼光谱**可在腐蚀环境中实时监测缓蚀剂各组分的协同吸附行为，通过特征峰位移（如C=N配位位移、-COO⁻对称/不对称伸缩频率差变化）判断吸附构型和配位模式。

---

## Sources

[1] Ramsey et al., Raman spectroscopic analysis of the speciation of dilute chromate solutions, Corrosion Science, 2001: https://www.sciencedirect.com/science/article/abs/pii/S0010938X00001451

[2] Zhao et al., Effects of chromate and chromate conversion coatings on corrosion of aluminum alloy 2024-T3, Surface and Coatings Technology, 2001: https://kb.osu.edu/server/api/core/bitstreams/63fd34dd-3d1d-5963-b4df-e890447ade97/content

[3] Avalos et al., Review of Vibrational Spectroscopy Studies of Coatings Based on Hexavalent or Trivalent Chromium Baths, Analytica, 2025: https://www.mdpi.com/2673-4532/6/4/47

[4] Theoretical Study of Molybdenum Separation from Molybdate Assisted by a Terahertz Laser, Molecules, 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC11279852

[5] Kharitonov et al., Aqueous molybdate provides effective corrosion inhibition of WE43 magnesium alloy, Corrosion Science, 2021: https://www.sciencedirect.com/science/article/pii/S0010938X21004303

[6] Burcham & Wachs, Vibrational analysis of the two non-equivalent, tetrahedral tungstate units in Ce2(WO4)3 and La2(WO4)3, Spectrochimica Acta Part A, 1998: https://www.lehigh.edu/operando/Publications/1998%20vibrational%20analysis%20of%20WOx%20compounds.pdf

[7] Frost et al., Raman microscopy of selected tungstate minerals, Spectrochimica Acta Part A, 2004: https://eprints.qut.edu.au/804/01/Raman_microscopy_of_selected_tungstate_minerals-revised.pdf

[8] Burduhos-Nergis et al., Characterization of Zinc and Manganese Phosphate Layers on Carbon Steel, IOP Conf. Ser.: Mater. Sci. Eng., 2020: https://iopscience.iop.org/article/10.1088/1757-899X/877/1/012012/pdf

[9] Simescu & Idrissi, Effect of zinc phosphate chemical conversion coating on corrosion behaviour of mild steel in alkaline medium, Sci. Technol. Adv. Mater., 2008: https://pmc.ncbi.nlm.nih.gov/articles/PMC5099651

[10] Mechanism of zinc phosphate conversion coating formation on iron-based substrates, Corrosion Science, 2025: https://www.sciencedirect.com/science/article/pii/S0010938X25001234

[11] Antony et al., Investigation of the inhibiting effect of nano film by sodium meta silicate-Zn, Zaštita Materijala, 2010: http://idk.org.rs/wp-content/uploads/2016/09/ZM_51_1_11.pdf

[12] Sodium Silicate and Phosphate as Corrosion Inhibitors for Mild Steel in Simulated Cooling Water System, Arabian Journal for Science and Engineering, 2014: https://www.academia.edu/11341748/Sodium_Silicate_and_Phosphate_as_Corrosion_Inhibitors_for_Mild_Steel_in_Simulated_Cooling_Water_System

[13] Weston & Brodasky, Infrared Spectrum and Force Constants of the Nitrite Ion, J. Chem. Phys., 1957: https://www.semanticscholar.org/paper/Infrared-Spectrum-and-Force-Constants-of-the-Ion-Weston-Brodasky/a9b13336947307938a38d971ca759033149f941e

[14] A New Mechanism for the Inhibition of SA106 Gr.B Carbon Steel Corrosion by Nitrite in Alkaline Water, Materials, 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC11432826

[15] New mechanism on synergistic effect of nitrite and triethanolamine, Adv. Mater. Sci. Eng., 2016: https://scispace.com/pdf/new-mechanism-on-synergistic-effect-of-nitrite-and-27rrycy0h7.pdf

[16] Cerium (III) Oxide – Based Conversion Layer on Galvanized Steel, Corrosion Science and Technology, 2025: https://www.j-cst.org/data/issue/CST/C002405/C00240500309.pdf

[17] White, Mansfeld & Bryant, In Situ Surface Studies of Conversion Coatings for Steel and Aluminum, DTIC ADA261016, 1992: https://apps.dtic.mil/sti/tr/pdf/ADA261016.pdf

[18] Vanadium and Tannic Acid-Based Composite Conversion Coating for 6063 Aluminum Alloy, Frontiers in Materials, 2021: https://www.frontiersin.org/journals/materials/articles/10.3389/fmats.2021.802468/full

[19] Milošev et al., Molybdate and vanadate ions as corrosion inhibitors, Electrochimica Acta, 2024: https://www.sciencedirect.com/science/article/pii/S0013468624011319

[20] Metrohm, Inline analysis of borate and sulfate solutions with Raman spectroscopy: https://www.metrohm.com/en/applications/application-notes/prozess-applikationen-anpan/an-pan-1063.html

[21] Nakamoto, Infrared and Raman Spectra of Inorganic and Coordination Compounds, 6th ed., Wiley, 2009: https://dokumen.pub/infrared-and-raman-spectra-of-inorganic-and-coordination-compounds-part-a-theory-and-applications-in-inorganic-chemistry-6ed-9789354241628.html

[22] Espina, Sanchez-Cortes & Jurašeková, Vibrational Study (Raman, SERS, and IR) of Plant Gallnut Polyphenols, Molecules, 2022: https://pmc.ncbi.nlm.nih.gov/articles/PMC8746386

[23] Espina et al., Analysis of Iron Complexes of Tannic Acid and Other Related Polyphenols, ACS Omega, 2022: https://pubs.acs.org/acsodf/article/7/32/27937/417220/Analysis-of-Iron-Complexes-of-Tannic-Acid-and

[24] Raj et al., Tannic Acid-Loaded Hydroxyapatite Carriers for Corrosion Protection of Polyolefin-Coated Carbon Steel, Applied Sciences, 2022: https://www.mdpi.com/2076-3417/12/20/10263

[25] Preparation of tannic acid-based conversion coating and corrosion protection for carbon steel, Journal of Materials Research and Technology: https://www.sciencedirect.com/science/article/pii/S2214509524011343

[26] Alsabagh et al., Utilization of Green Tea as Environmentally Friendly Corrosion Inhibitor for Carbon Steel in Acidic Media, Int. J. Electrochem. Sci., 2015: https://www.electrochemsci.org/papers/vol10/100201855.pdf

[27] Yahaya et al., Green and Black Tea (Camellia sinensis) Extracts as Corrosion Inhibitors for Mild Steel in 1.0 M HCl, World Applied Sciences Journal, 2017: http://www.idosi.org/wasj/wasj35%286%2917/21.pdf

[28] El Ibrahimi et al., Amino acids and their derivatives as corrosion inhibitors for metals and alloys, Arabian Journal of Chemistry: https://arabjchem.org/amino-acids-and-their-derivatives-as-corrosion-inhibitors-for-metals-and-alloys

[29] Święch et al., Spectroscopic Investigations of 316L Stainless Steel under Simulated Inflammatory Conditions: The Effect of Tryptophan as Corrosion Inhibitor, Coatings, 2021: https://www.mdpi.com/2079-6412/11/9/1097

[30] Freire et al., Raman Spectroscopy of Amino Acid Crystals, IntechOpen, 2017: https://www.intechopen.com/chapters/52839

[31] Bazylewski et al., In situ Raman spectroscopy distinguishes between cysteine SH conformers, RSC Advances, 2017: https://pubs.rsc.org/ra/article/7/5/2964/544159/In-situ-Raman-spectroscopy-distinguishes-between

[32] Adar, Interpretation of Raman Spectrum of Proteins, Spectroscopy, 2022: https://www.spectroscopyonline.com/view/interpretation-of-raman-spectrum-of-proteins

[33] Modwi et al., Eco-friendly corrosion inhibitor of Q235 carbon steel in 1.0 M HCl by Isatin/Chitosan Schiff base, Journal of Molecular Structure, 2025: https://www.sciencedirect.com/science/article/abs/pii/S0022286024021057

[34] Zhang et al., Chitosan derivatives as promising green corrosion inhibitors for carbon steel in acidic environment, Journal of Colloid and Interface Science, 2023: https://www.sciencedirect.com/science/article/abs/pii/S0021979723003399

[35] Hamza et al., Eco-friendly corrosion inhibitor chitosan methionine for carbon steel in 1 M HCl, Scientific Reports, 2025: https://www.nature.com/articles/s41598-025-98981-2

[36] Al-Bonayan, Sodium Alginate as Corrosion Inhibitor for Carbon Steel, Int. J. Scientific & Engineering Research, 2014: https://www.academia.edu/38450530/Sodium_Aliginate_as_Corrosion_Inhibitor_for_Carbon_Steel

[37] CN102140641A, Green sodium alginate corrosion inhibitor for carbon steel neutral medium, 中国科学院海洋研究所: https://patents.google.com/patent/CN102140641A/en

[38] Carbon Quantum Dots Derived from Garlic (Allium sativum) Peel as Corrosion Inhibitor for Mild Steel in HCl Solution, ACS Omega, 2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC12332664

[39] Guma & Aremo, A Review of Up-To-Date Research Knowledge on the Corrosion Inhibiting Capability of Garlic Allicin Sativum for Steel Materials, IJAEM, 2025: https://ijaem.net/issue_dcp/A%20Review%20of%20Up%20To%20Date%20Research%20Knowledge%20on%20the%20Corrosion%20Inhibiting%20Capability%20of%20Garlic%20Allicin%20Sativum%20for%20Steel%20Materials.pdf

[40] Xiao et al., Chemical Components and Biological Activities of Areca catechu L., Biomedical Research and Reviews, 2019: https://www.oatext.com/chemical-components-and-biological-activities-of-areca-catechu.php

[41] Huang et al., Recent Advance on Biological Activity and Toxicity of Arecoline in Edible Areca (Betel) Nut, Foods, 2024: https://www.mdpi.com/2304-8158/13/23/3825

[42] Elazabawy et al., Eco-friendly orange peel extract as corrosion resistant for carbon steel's deterioration in petroleum formation water, Scientific Reports, 2023: https://pmc.ncbi.nlm.nih.gov/articles/PMC10713783

[43] Natural Orange Peel Extract as a Corrosion Inhibitor and Cleaning Agent, Corrosion and Materials Degradation, MDPI: https://www.mdpi.com/2624-5558/6/4/67

[44] Salamah et al., Authentication of citrus peel oils from different species and commercial products, Pharmacia, 2024: https://pdfs.semanticscholar.org/e703/abd22dcdd44e06729e6895afcb621b498bc4.pdf

[45] Mpelwa, Evaluation of plant-based crude extract as environmentally friendly corrosion inhibitor, Surface Science and Technology, 2026: https://link.springer.com/article/10.1007/s44251-026-00126-8

[46] Ghanbari Daryaee et al., Synergistic Effects of Rosemary and Carrot Extracts as Green Corrosion Inhibitors for Carbon Steel, ChemEngineering, 2025: https://www.mdpi.com/2305-7084/9/6/142

[47] Fazal et al., A review of plant extracts as green corrosion inhibitors for CO2 corrosion of carbon steel, npj Materials Degradation, 2022: https://www.nature.com/articles/s41529-021-00201-5

[48] Holla et al., Plant extracts as green corrosion inhibitors for different kinds of steel: A review, Heliyon, 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC11304013

[49] 芮玉兰等, Inhibition Behavior of Molybdate Inhibitors for Carbon Steel in Sea Water, Corrosion & Protection, 2007: https://fsyfh.mat-test.com/en/article/id/6a6ad8d5-27c1-4991-bea7-3dea977c48d0?viewType=citedby-info

[50] Liu Xia et al., Synergistic corrosion inhibition behavior of rare-earth cerium ions and serine on carbon steel in 3% NaCl solutions, Journal of Central South University, 2018: https://link.springer.com/article/10.1007/s11771-018-3881-x

[51] Cotting & Aoki, Octylsilanol and Ce(III) ions – alternative corrosion inhibitors for carbon steel in chloride neutral solutions, Journal of Materials Research and Technology, 2020: https://repositorio.usp.br/directbitstream/92080af5-4dd0-4e45-a31d-6bfd2b083872/Octylsilanol%20and%20Ce%28III%29%20ions%20%E2%80%93%20alternative%20corrosion%20inhibitors%20for%20carbon%20steel%20in%20chloride%20neutral%20solutions.pdf

[52] Anandkumar et al., Synergistic enhancement of corrosion protection of carbon steels using corrosion inhibitors and biocides, Journal of Environmental Chemical Engineering, 2023: https://www.sciencedirect.com/science/article/abs/pii/S221334372300581X

[53] Haruna, Saleh & Sorour, SERS detection of AEP-GO on X60 carbon steel surface in 15% HCl solution, Heliyon, 2023: https://pmc.ncbi.nlm.nih.gov/articles/PMC10685366

[54] Decoding Corrosion Using Raman Spectroscopy, Wasatch Photonics/Spectroscopy Online, 2022: https://wasatchphotonics.com/raman-corrosion-study-spectroscopy-magazine

[55] Ituen et al., Spectroscopy in Oilfield Corrosion Monitoring and Inhibition, IntechOpen, 2020: https://www.intechopen.com/chapters/73405

[56] Wang et al., A critical review on advanced surface analysis techniques used for studying the adsorption mechanisms of organic corrosion inhibitors, Corrosion Communications, 2026: https://www.sciencedirect.com/science/article/pii/S2667266926000198

[57] Chen, Lu & Zhang, Organic Compounds as Corrosion Inhibitors for Carbon Steel in HCl Solution: A Comprehensive Review, Materials, 2022: https://pmc.ncbi.nlm.nih.gov/articles/PMC8954067

[58] Puzikova et al., Review of organic corrosion inhibitors: application with respect to the main functional group, Journal of Saudi Chemical Society, 2025: https://link.springer.com/article/10.1007/s44442-025-00021-1

[59] Pailleret et al., Adsorption mechanism of quaternary ammonium corrosion inhibitor on carbon steel, Corrosion Science, 2023: https://cnrs.hal.science/hal-03969214/file/Cor%20Sci_Pailleret.pdf

[60] Chemistry LibreTexts, Identifying all IR- and Raman-active vibrational modes in a molecule: https://chem.libretexts.org/Courses/Saint_Marys_College_Notre_Dame_IN/CHEM_431%3A_Inorganic_Chemistry_(Haas)/CHEM_431_Readings/07%3A_Vibrational_Spectroscopy/7.02%3A_Identifying_all_IR-_and_Raman-active_vibrational_modes_in_a_molecule

[61] Revisiting the Raman Spectra of Carbonate Minerals, Minerals, 2023: https://www.mdpi.com/2075-163X/13/11/1358

[62] Ahmed et al., Current and emerging trends of inorganic, organic and eco-friendly corrosion inhibitors, RSC Advances, 2024: https://pmc.ncbi.nlm.nih.gov/articles/PMC11460216
