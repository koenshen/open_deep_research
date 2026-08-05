# 计算化学中模拟外加电场时分子取向随机性的系统性解决方案

## 一、问题概述与核心挑战

在计算化学中，使用Gaussian等软件通过`Field=x+100`等关键词模拟外加电场是一种常规做法。然而，对于单原子分子催化剂（SACs）这类体系，在真实反应环境中分子的朝向是随机且不确定的，而理论模拟中施加的固定方向电场（如x方向）与实际实验中各向同性取向的分子所感受到的电场效应存在显著差异。这一问题的核心在于：**计算化学中施加的电场是实验室坐标系中的固定矢量，而实验中的分子在溶液中自由旋转，其取向是随机的**。

本报告基于系统性文献调研，从以下几个方面提供全面的解决方案：①主流量子化学软件中的电场模拟方法与取向处理策略；②相关文献案例；③公认的协议与指南；④可操作的代码/输入示例。

---

## 二、Gaussian软件中的电场模拟：方法与取向处理

### 2.1 Field关键字的基本用法与原理

Gaussian中的`Field`关键字用于向计算添加有限电场。其基本格式为`Field=M±N`，其中M表示多极矩（如X、Y、Z表示偶极方向），N×0.0001以原子单位（a.u.）指定场强[1][2]。

**关键原理**：
- 1 a.u. = 51.4 V/Å，是一个相当大的电场单位[3]
- 所有电场参数都在输入取向（input orientation）中指定
- 使用Field时存档功能被禁用

**示例：水分子在Z方向电场中的优化**：
```
#P B3LYP/6-31G(d) Opt=Z-Matrix NoSymm Field=Z+10

Water with Z+10 field

0 1
O 0 0 0
H 0 0 1
H 0 1 0
```

### 2.2 标准取向（Standard Orientation）问题的关键发现

**这是Gaussian模拟电场时最容易被忽视的关键问题**：在Gaussian中，`Field=z+n`关键字添加的电场是在"标准取向"（standard orientation）的Z方向，而不是"输入取向"（input orientation）。标准取向可能与输入取向不同，因为Gaussian会根据对称性自动旋转分子[4][5]。

**解决方法**：
1. **使用`NoSymm`关键字**：防止分子重新取向，使所有计算在输入取向中进行
2. **使用`NoSymmetry`关键字**：功能与NoSymm相同，但程序仍尝试识别点群
3. **使用`Symmetry=None`**：完全禁用对称性

**重要说明**（来自Gaussian官方文档）[1]：
> "如果使用对称性，分子在计算前可能会被旋转到不同的坐标系，称为标准取向。导数随后被旋转回原始（输入）取向。轨道在标准取向中打印。性质和背景电荷分布的输入必须在标准取向中指定。"

### 2.3 几何优化中的电场设置

对于带电场的几何优化，必须使用[1][2]：
```
Opt=Z-Matrix NoSymm
```
并且输入几何必须用传统的Z-矩阵坐标或符号Cartesian坐标定义。

### 2.4 关于"各向同性电场"的可行性

**直接结论**：Gaussian **没有内置的"各向同性电场"或"球形平均电场"模型**。Field关键字只能施加沿固定Cartesian轴的均匀电场方向。因此，处理随机取向问题的核心策略是**取向平均**（见下文第三节）。

---

## 三、处理分子取向随机性的核心策略：取向平均方法

### 3.1 理论基础：旋转平均（Rotational Averaging）

旋转平均是将分子尺度的性质转换为宏观实验观测量的标准方法。Andrews在2004年发表于*Journal of Chemical Education*的论文中提供了完整的数学框架[6]：

**各向同性平均定义**：
⟨f⟩ = (1/8π²) ∫₀²π ∫₀^π ∫₀²π f(θ,φ,χ) sinθ dθ dφ dχ

**关键物理结果**（对于各向同性系综）：
- 固定偶极在均匀电场中的平均能量：⟨U⟩ = 0
- 可极化分子在电场中的平均能量：⟨U⟩ = -E² Tr(α)/6，其中Tr(α)是极化率张量的迹
- 各向同性样品的平均吸收截面是最大值的1/3

### 3.2 数值取向平均方法：五种主要求积方法

Goetz等人在2024年发表于*Journal of Chemical Physics*的论文中系统比较了五种数值取向平均方法[7]：

1. **球面Gauss求积**（如Lebedev-Laikov）：对光滑被积函数最优，可实现数值精确积分
2. **球面Chebyshev求积**：适用于特定对称性
3. **近似均匀球面覆盖**：对低秩或高对称性被积函数更经济
4. **乘积求积**：结合于一维和二维求积
5. **Monte Carlo方法**：适用于高维或有噪声的被积函数

**关键发现**：
- 对于电偶极类计算，仅需少量Lebedev求积点（如LD14网格，14个点）即可完全收敛[8]
- 作者提供了名为**'orientavg'**的Python包，提供多种求积方法的灵活接口[7]

### 3.3 在Gaussian中实现取向平均的脚本流程

**方法A：使用Lebedev求积点（推荐）**
```python
# 使用orientavg包中的Lebedev求积生成均匀分布取向
from orientavg import lebedev_quadrature
import numpy as np
from scipy.spatial.transform import Rotation as R

# 生成Lebedev求积点（代表均匀分布的方向）
points, weights = lebedev_quadrature(degree=14)  # 14个点即可收敛

# 对每个方向，将分子旋转使某参考向量与该方向对齐
for i, (direction, weight) in enumerate(zip(points, weights)):
    # 计算旋转矩阵
    rotation = R.align_vectors([direction], [[0, 0, 1]])[0]
    rotated_coords = rotation.apply(original_coords)
    
    # 写入Gaussian输入文件（带NoSymm和Field关键字）
    write_gaussian_input(rotated_coords, field_vector=[0,0,0.01], filename=f"job_{i}.com")
    
    # 运行Gaussian并提取结果
    energy = run_gaussian(f"job_{i}.com")
    
    # 加权平均
    weighted_avg += weight * energy
```

**方法B：随机取向采样（适用于高维或复杂情况）**
```python
import numpy as np
from scipy.spatial.transform import Rotation as R

n_orientations = 100
results = []

for i in range(n_orientations):
    # 生成随机旋转矩阵
    r = R.random()
    rotated_coords = r.apply(original_coords)
    
    # 写入Gaussian输入文件（带NoSymm和Field关键字）
    write_gaussian_input(rotated_coords, field_vector=[0,0,0.01], filename=f"random_{i}.com")
    
    # 运行Gaussian并提取结果
    energy = run_gaussian(f"random_{i}.com")
    results.append(energy)

# 计算各向同性平均值
isotropic_avg = np.mean(results)
```

**方法C：固定分子，旋转电场方向（最简单近似）**
- 保持分子不变
- 分别在X、Y、Z方向施加电场（Field=X+10, Field=Y+10, Field=Z+10）
- 对三个方向的结果取平均，可近似各向同性响应

### 3.4 关于"直接omers"（Directomers）的重要发现

2026年arXiv预印本[9]揭示了OEEF下分子构型的全新现象：
> "A major challenge is that an applied field exerts a torque on a molecule, reorienting the molecular frame and complicating the interpretation of orientation-dependent electric-field effects. Thus, free polar molecules experience orienting rather than oriented fields, such that the field response drives the molecular orientation rather than the other way around."

该研究使用CO和OCS为模型体系，展示了在0.01–0.05 a.u.场强下，各向异性极化率可以产生双阱旋转势能面（rPES），在平行和反平行场取向处存在稳定构型（称为"directomers"）。这为理解电场如何驱动分子取向提供了新的理论框架。

---

## 四、各向同性电场近似：反应场模型（SCRF）的应用

### 4.1 SCRF模型与各向同性电场的相似性

连续溶剂化模型将溶剂视为连续的各向同性介质[10][11]。SCRF（Self-Consistent Reaction Field）模型通过建立一个依赖于溶质电子密度的"反应场"来模拟溶剂环境。虽然SCRF**不是**外加电场的直接替代品，但其物理本质——环境作为各向同性介质的响应——与各向同性电场环境有一定的相似性。

**关键区别**：
- Field关键字施加的是**外部均匀电场**，方向固定
- SCRF施加的是**溶剂反应场**，由溶质电荷分布诱导产生，是各向异性的（取决于溶质形状和电荷分布）
- **Gaussian中没有直接的关键字可以施加"各向同性外部电场"**

### 4.2 Gaussian中的SCRF模型选择

Gaussian 16中，SCRF的默认方法是IEFPCM（积分方程形式极化连续模型）[12]：

| 模型 | 特点 | 适用场景 |
|------|------|----------|
| **IEFPCM**（默认） | 通用溶质-溶剂静电相互作用 | 大多数情况 |
| **SMD** | IEFPCM + 原子表面张力非静电力项 | 推荐用于计算溶剂化自由能 |
| **CPCM** | 类导体PCM，高介电常数溶剂的高效近似 | 水溶液等 |
| **Dipole**（Onsager） | 球形空穴，最简单近似 | 基础教学示例 |

**SMD模型计算水溶剂化能示例**：
```
#P B3LYP/6-31G(d) SCRF=(SMD,Solvent=Water)

Water solvation energy

0 1
[分子坐标]
```

### 4.3 Field + SCRF组合使用的注意事项

ORCA手册明确警告[3]：
> "While the program allows to combine the electric field with the implicit solvation model, the results must be interpreted cautiously as the solvent medium does not feel the field."

因此，在SCRF计算中同时施加Field时，溶剂反应场不会对外加电场产生响应。对于需要同时考虑溶剂和电场的情况，建议使用显式溶剂化或分子动力学模拟。

### 4.4 AuF（Adduct under Field）方法

Shenderovich和Denisov（2021）提出的AuF方法使用外部电场在静态量子化学计算中对溶质-溶剂相互作用进行建模[13]。关键发现：
- 对于小扰动，PCM近似是可选的；但接近解离时强烈推荐使用PCM
- PCM与外部电场的组合比在气相近似下使用外部电场提供更可靠和稳定的结果
- 该方法可用于区分宏观反应场效应和特定溶质-溶剂相互作用

---

## 五、文献案例：单原子催化剂与分子催化剂中的电场效应模拟

### 5.1 单原子催化剂（SACs）的OEEF调控

**Pan et al. (2022) — Nature Communications**[14]

该研究展示了OEEF对锚定在二维原子晶体上的单原子催化剂性能的系统调控：
> "Inspired by the electrostatic interaction within specific natural enzymes, here we show the performance of model single-atom catalysts anchored on two-dimensional atomic crystals can be systematically and efficiently tuned by oriented external electric fields."

**研究体系**：锚定在n型MoS₂上的Pt单原子，以及WSe₂、石墨烯上的Co等单原子
**催化反应**：析氢反应（HER）和析氧反应（OER）
**取向处理方式**：采用定向OEEF方法，电场沿垂直于催化剂表面方向施加，**未讨论取向平均问题**

**Lu et al. (2022) — Physica B**[15]：研究了OEEF对Pt/石墨烯单原子上O₂活化的调控，同样采用固定方向电场。

### 5.2 各向同性电场方法（Isotropic Field Approach）——最直接相关的文献

**JCTC 2026**[16]（DOI: 10.1021/acs.jctc.6c00732）：
> "Second, we employed an isotropic field approach, applying equal-magnitude electric field vectors in randomized orientations around the..."

该工作对Hurd-Claisen重排反应中的电场效应进行了全面计算研究，研究对象包括含酯基和含腈基的底物，在定向OEEF和各向同性电场条件下进行。这是目前文献中**极少数明确采用"各向同性电场近似"来处理分子取向随机性的计算化学工作之一**。

### 5.3 800个随机取向的电场效应研究

**Scheele et al. (2023) — PCCP**[17]：
> "The electric field was applied along 800 randomly chosen orientations, and the rupture force of the scissile bond was determined at a 0.5 nN resolution."

该工作是目前最系统地处理分子取向不确定性的OEEF理论研究之一。通过沿**800个随机选择取向**施加电场，系统获得了电场方向依赖性的完整图谱——断裂力降低程度高度依赖于电场相对于键轴的角度。

### 5.4 Shaik等人的OEEF系列工作

**Shaik et al. (2016) — Nature Chemistry**[18]（被引>650次）：
> "An OEEF along the direction of electron reorganization (the so-called reaction axis) will catalyse nonpolar reactions by orders of magnitude, control regioselectivity and induce spin-state selectivity."

该文明确讨论了反应物取向相对于电场方向是OEEF应用的关键挑战，实验验证（Aragonès et al., 2016）使用了STM裂结技术将反应物固定在电极之间以克服取向不确定性问题。

**Shaik et al. (2018) — Chemical Society Reviews**[19]（被引>360次）：
提供了OEEF的教程综述，教导研究者如何概念化和设计电场对键、结构和反应的影响。

**Shaik et al. (2025) — Accounts of Chemical Research**[20]：
> "OEEF usage will change chemical education, chemical practice, and the art of making molecules."

该文指出OEEF像"镊子"一样定向极性的分子物种，使其沿反应轴排列，并讨论了溶剂的取向重组产生的屏蔽效应。

### 5.5 从酶到分子催化剂的电场效应

**Léonard et al. (2021) — ACS Catalysis**[21]（被引>100次）：
> "An oriented electrostatic field of appropriate magnitude can direct chemical interactions, reactivity, and catalysis by manipulating activation energies as a function of molecular orientation."

该视角文章系统讨论了酶、有机反应和过渡金属催化体系中的电场效应，强调了理解电场方向性对设计分子催化剂的重要性。

---

## 六、分子动力学与电场模拟的结合：MD+QM/MM方法

### 6.1 MD+QM/MM揭示OEEF的溶剂屏蔽效应

**JACS 2020**[22]（被引>70次）：
> "When and how do external electric fields (EEFs) lead to catalysis in the presence of a (polar or nonpolar) solvent? This is the question that is addressed here using a combination of molecular dynamics (MD) simulations, quantum mechanical/molecular mechanical calculations with EEF, and quantum mechanical/(local) electric field calculations."

**关键结果**（Menshutkin反应：CH₃I + 吡啶）：
- 在乙腈中，外加电场几乎完全被反向溶剂场屏蔽，直到介电饱和发生
- 一旦外加电场超过溶剂反电场（0.5 V/Å），催化出现：反应能垒从18.9 kcal/mol（无场）降至8.3 kcal/mol
- 在非极性和弱极性溶剂中，OEEF催化的可行性更高

### 6.2 溶剂预有序化实现静电催化

**Xu et al. (2020) — JACS**[23]（被引68次）：
> "Our results show that a 0.2 V/Å external electric field, which is below the threshold for bond breaking of solvent molecules, leads to significant ordering of bulk methanol solvent and the ionic liquid [EMIM][BF₄]."

**关键结果**（o-烷基苯基酮的氢转移反应）：
- 有序化甲醇（0.2 V/Å预有序化）：活化能从44.20降至24.19 kcal/mol（降低20.01 kcal/mol）
- 有序化离子液体[EMIM][BF₄]：活化能从44.34降至13.49 kcal/mol（降低30.85 kcal/mol）
- **方法**：经典MD（Drude振子可极化力场）+ 量子化学计算 + ONIOM多尺度方法

### 6.3 PNNP MD：机器学习加速的电场响应模拟

**Nature Communications 2024**[24]：
该方法使用两个神经网络（委员会NNP和等变图神经网络APTNN），仅在零场构型上训练，但可外推到有限场。在液态水上的验证显示：
- 静介电常数：79.3 ± 2.2（实验值78.4）
- 取向弛豫动力学时间常数：~5.9 ps
- 正确预测O-H伸缩模式的场致红移和摆动模式的蓝移

---

## 七、其他计算工具中的电场模拟方法

### 7.1 ORCA

**EField关键字**[3]：在`%scf`块中指定x,y,z分量（原子单位）：
```
! B3LYP def2-SVP Opt
%scf
  EField 0, 0, 0.01   ! 0.01 au (0.514 V/Å) along z
end
*xyz 0 1
[coordinates]
*
```

**重要注意事项**：
- ORCA不提供内置的各向同性电场或取向平均功能
- 电场破坏旋转对称性，几何优化自动切换到笛卡尔坐标
- 隐式溶剂化可与电场结合，但溶剂介质不"感受"电场
- 带电分子在纯偶极场中优化时，平移自由度被冻结
- 频率计算不投影平移/旋转模式，可能混合振动

### 7.2 Q-Chem

**`$multipole_field`关键字**[25]：用于施加多极场。

**`$external_charges`关键字**[26]：用于将外部电荷纳入计算。

**符号约定问题**[27]：Q-Chem采用的电场方向约定与物理教科书相反（从负到正电荷的方向），需注意。

**SYM_IGNORE关键字**：用于防止程序重新取向分子，相当于Gaussian的NoSymm。

### 7.3 VASP

**Berry相位方法（PEAD）**[28]：用于周期性体系中的有限电场计算，通过`EFIELD_PEAD`标签控制。

**锯齿势（Sawtooth）方法**[29]：用于表面/分子计算，通过设置`EFIELD`（eV/Å）、`LDIPOL=.TRUE.`、`IDIPOL`和`DIPOL`实现。

**重要注意事项**：
- 锯齿势不适用于周期性体相体系（会导致势能不连续）
- 电场方向由IDIPOL=1-3设置，仅限于晶格矢量方向
- VASP没有处理分子取向随机性的内置功能

### 7.4 专业工具与脚本

**A.V.E.D.A.**[30]：Automated Variable Electric-Field DFT Application，开源工具，自动化评估OEEF对化学反应的影响。工作流程：在递增电场（0至–10.0×10⁻³ a.u.）下沿反应偶极轴优化结构和过渡态。MIT许可证，GitHub上可用。

**TUPÃ**[31]：基于Python的MD电场分析工具，三种计算模式（原子、键、坐标），包含PyMOL插件用于3D电场矢量可视化。免费提供：https://mdpoleto.github.io/tupa/

**pyEF**[32]：用于从QM计算中计算电场、静电势和静电相互作用的Python包，支持多种电荷类型。

---

## 八、公认协议与最佳实践指南

### 8.1 将各向同性电场效应纳入量子化学计算的标准化协议

基于综合文献调研，以下是四种主要方法的总结：

**方法A：隐式溶剂化/反应场方法（适用于各向同性介质中电场效应的平均处理）**
1. 选择SCRF模型（推荐IEF-PCM/SS(V)PE用于高精度，C-PCM用于计算效率）
2. 定义空腔（使用Bondi半径缩放，van der Waals表面或SAS/SES）
3. 设定溶剂介电常数（对于各向同性介质，使用宏观介电常数）
4. 执行SCF计算（溶剂反应场自洽迭代）
5. 对于非平衡过程（如垂直激发），选择LR或SS方法

**方法B：显式电场+取向平均（推荐用于需要各向同性场下分子性质的情况）**
1. 使用MD模拟生成分子取向的Boltzmann分布（或使用Lebedev求积点）
2. 从MD轨迹中提取分子取向分布（取样大量构型）
3. 对每个取向执行量子化学计算（施加固定方向的外部电场，使用NoSymm/SYM_IGNORE防止重新取向）
4. 对所有取向的量子化学结果进行数值平均（使用旋转平均公式）
5. 或者，使用Andrews的旋转平均解析公式直接计算体相响应

**方法C：AuF方法（适用于模拟溶剂效应作为电场效应）**
1. 将目标分子置于气相或PCM环境中
2. 施加外部电场（沿特定方向，强度可调）
3. 优化几何或计算性质
4. 与实验数据比较，调整场强以匹配

**方法D：MD模拟中的直接电场（适用于非平衡动力学）**
1. 在MD模拟中施加外部电场（GROMACS: E0参数; NAMD: eField关键词）
2. 使用适当的热浴和边界条件
3. 从MD轨迹计算平均性质
4. 注意：对于Ewald静电，默认导电边界条件会将有效场高估系统介电常数倍

### 8.2 关键建议与最佳实践

1. **始终使用`NoSymm`**：在Gaussian中进行电场计算时，始终使用NoSymm关键字防止分子重新取向，确保电场方向与输入几何一致[4][5]。

2. **使用足够弥散的基组**：准确电场响应需要灵活、弥散的基组，如Sadlej基组或aug-cc-pVTZ[3][33]。

3. **检查收敛标准**：数值微分需要紧密甚至非常紧密收敛的SCF计算[3]。

4. **测试场强范围**：实验室相关场强约为0.1 V/Å（0.002 a.u.），远低于1 a.u.。避免使用过强场强导致非物理结果[3]。

5. **考虑溶剂屏蔽效应**：在极性溶剂中，外加电场可能被溶剂反电场部分屏蔽，需使用MD+QM/MM方法定量评估[22]。

6. **使用取向平均的解析公式**：对于可极化分子的能量响应，可使用Andrews公式⟨U⟩ = -E² Tr(α)/6直接计算各向同性平均[6]。

7. **验证取向平均的收敛性**：使用Lebedev求积时，从少量点（如14个）开始，逐步增加直到结果稳定[7][8]。

---

## 九、可操作的解决方案综述

### 9.1 针对单原子催化剂（SACs）的推荐方案

对于单原子催化剂体系，由于催化剂通常锚定在二维材料（如MoS₂、石墨烯）上，其取向相对固定（垂直或平行于表面）。因此，**建议采用定向OEEF方法**，电场沿表面法向施加，并结合取向平均验证。

**具体步骤**：
1. 构建SAC模型（如Pt/MoS₂）
2. 在表面法向方向施加电场（Field=Z+10，使用NoSymm）
3. 优化几何并计算反应能垒
4. 对于溶液中随机取向的SACs，使用MD+QM/MM方法获取取向分布
5. 使用Lebedev求积或随机采样进行取向平均

### 9.2 针对溶液中分子催化剂的推荐方案

对于溶液中自由旋转的分子催化剂，**推荐采用取向平均方法**。

**具体步骤**：
1. 使用Python脚本（基于orientavg包或自行编写）生成均匀分布的分子取向
2. 对每个取向，在固定方向（如Z方向）施加电场，使用NoSymm关键字
3. 批量运行Gaussian计算
4. 对结果进行加权平均（对于各向同性系综，使用均匀权重）

### 9.3 推荐的输入文件模板

**Gaussian输入文件模板（取向平均）**：
```
%chk=job_001.chk
#P B3LYP/6-31G(d) NoSymm Field=Z+10

SAC in electric field - orientation 001

0 1
[旋转后的分子坐标]
```

**Gaussian输入文件模板（SCRF+Field组合）**：
```
%chk=job_scrf.chk
#P B3LYP/6-31G(d) SCRF=(SMD,Solvent=Water) NoSymm Field=Z+10

SAC in solvent with electric field

0 1
[分子坐标]
```

### 9.4 当前领域的共识结论

1. **理论模拟与实验之间的差距**：固定方向电场与随机取向分子之间的差异是OEEF催化领域公认的核心挑战，Shaik等人明确称其为"取向问题"（orientational problem）[18]。

2. **取向平均是标准方法**：旋转平均是将分子尺度性质转换为宏观实验观测量的标准方法，Andrews 2004年的工作提供了完整的数学框架[6]。

3. **各向同性电场方法正在兴起**：JCTC 2026年首次明确采用"各向同性电场方法"处理取向随机性[16]，代表了该领域的最新进展。

4. **MD+QM/MM是定量评估溶剂屏蔽效应的关键工具**：JACS 2020年的工作建立了MD+QM/MM方法定量评估溶剂对OEEF的屏蔽效应[22]。

5. **没有"一键式"解决方案**：目前没有任何主流量子化学软件提供内置的各向同性电场或取向平均功能。用户需要自行编写脚本或使用第三方工具实现取向平均。

6. **A.V.E.D.A.等工具正在降低使用门槛**：自动化工具如A.V.E.D.A.[30]和TUPÃ[31]正在使电场模拟更加用户友好。

---

## 十、结论

本报告系统性地回答了计算化学中模拟外加电场时分子取向随机性的问题。核心结论是：

1. **Gaussian等主流量子化学软件没有内置的各向同性电场模型**，需要用户通过取向平均方法自行实现。

2. **取向平均方法**（包括Lebedev求积、随机采样、解析旋转平均）是处理取向随机性的标准方法，Goetz等人2024年的工作提供了实用的Python包（orientavg）[7]。

3. **SCRF反应场模型**不能直接替代外加电场，但可以作为各向同性环境的近似，与Field组合使用时需注意溶剂介质不响应外加电场。

4. **MD+QM/MM方法**是定量评估溶剂屏蔽效应和取向分布的关键工具，JACS 2020年的工作提供了重要参考[22]。

5. **各向同性电场方法**（JCTC 2026）[16]和**800随机取向采样**（PCCP 2023）[17]代表了该领域的最新进展。

6. **推荐的可操作方案**：对于单原子催化剂，采用定向OEEF+表面法向方向；对于溶液中分子催化剂，采用Lebedev求积取向平均+NoSymm关键字。

---

### 来源

[1] Gaussian Field keyword: https://gaussian.com/field

[2] Gaussian 09 Field manual: https://thiele.ruc.dk/~spanget/help/g09/k_field.htm

[3] ORCA 6.1 Manual - Finite Electric Fields: https://orca-manual.mpi-muelheim.mpg.de/contents/essentialelements/finEfield.html

[4] Gaussian Symmetry keyword: https://gaussian.com/symmetry

[5] ResearchGate - Gaussian field option uses standard instead of input orientation: https://www.researchgate.net/post/Gaussian-field_option_uses_standard_instead_of_input_orientation-how_to_overcome_this

[6] Andrews, S.S. (2004) "Using Rotational Averaging To Calculate the Bulk Response of Isotropic and Anisotropic Samples from Molecular Parameters", J. Chem. Educ.: https://www.smoldyn.org/andrews/papers/Andrews_2004.pdf

[7] Goetz, R.E. et al. (2024) "Numerical evaluation of orientation averages and its application to molecular physics", J. Chem. Phys. 161, 131501: https://pubs.aip.org/aip/jcp/article/161/13/131501/3315373/Numerical-evaluation-of-orientation-averages-and

[8] List, N.H.; Saue, T.; Norman, P. (2017) "Rotationally averaged linear absorption spectra beyond the electric-dipole approximation", Mol. Phys. 115, 2081: https://doi.org/10.1080/00268976.2017.1333643

[9] arXiv:2605.08494 (2026) "On the existence of distinct equilibrium configurations of molecules under oriented external electric fields": https://arxiv.org/abs/2605.08494

[10] Herbert, J.M. (2021) "Dielectric continuum methods for quantum chemistry", WIREs Comput. Mol. Sci. 11, e1519: https://www.asc.ohio-state.edu/herbert.44/reprints/WCMS_11_e1519.pdf

[11] Skyner, R.E. et al. (2015) "A review of methods for the calculation of solution free energies", Phys. Chem. Chem. Phys. 17, 6174: https://pubs.rsc.org/cp/article/17/9/6174/471596/A-review-of-methods-for-the-calculation-of

[12] Gaussian SCRF keyword: https://gaussian.com/scrf

[13] Shenderovich, I.G.; Denisov, G.S. (2021) "Adduct under Field (AuF) method", Molecules 26, 1283.

[14] Pan, Y. et al. (2022) "Boosting the performance of single-atom catalysts via external electric field polarization", Nature Communications 13, 3077: https://doi.org/10.1038/s41467-022-30766-x

[15] Lu, Z. et al. (2022) "Tuning the activation of O₂ on Pt single-atom catalyst using external-electric field", Physica B 638, 413937: https://doi.org/10.1016/j.physb.2022.413937

[16] JCTC (2026) "Unveiling Electric Field-Driven Stereocontrol in Hurd–Claisen Rearrangements": https://pubs.acs.org/doi/10.1021/acs.jctc.6c00732

[17] Scheele, T. et al. (2023) "Using Oriented External Electric Fields to Manipulate Rupture Forces of Mechanophores", Phys. Chem. Chem. Phys. 25, 28973: https://doi.org/10.1039/D3CP03965J

[18] Shaik, S. et al. (2016) "Oriented electric fields as future smart reagents in chemistry", Nature Chemistry 8, 1091: https://doi.org/10.1038/nchem.2651

[19] Shaik, S. et al. (2018) "Structure and reactivity/selectivity control by oriented-external electric fields", Chem. Soc. Rev. 47, 5125: https://doi.org/10.1039/C7CS00136G

[20] Shaik, S. et al. (2025) "Oriented Electric Fields—Universal Catalysts", Acc. Chem. Res.: https://doi.org/10.1021/acs.accounts.5c00508

[21] Léonard, N.G. et al. (2021) "Electric Fields in Catalysis: From Enzymes to Molecular Catalysts", ACS Catalysis 11, 10923: https://doi.org/10.1021/acscatal.1c02084

[22] JACS (2020) "Solvent Organization and Rate Regulation of a Menshutkin Reaction by Oriented External Electric Fields are Revealed by Combined MD and QM/MM Calculations", 142, 10815: https://doi.org/10.1021/jacs.0c02952

[23] Xu, L. et al. (2020) "Ordered Solvents and Ionic Liquids Can Be Harnessed for Electrostatic Catalysis", JACS 142, 12826: https://doi.org/10.1021/jacs.0c05643

[24] Nature Communications (2024) "Machine learning the electric field response of condensed phase systems using perturbed neural network potentials", 15, 8196: https://doi.org/10.1038/s41467-024-52491-3

[25] Q-Chem 5.3 Manual - $multipole_field: https://manual.q-chem.com/5.3/topic_3.5.html

[26] Q-Chem 5.4 Manual - $external_charges: https://manual.q-chem.com/5.4/topic_C.1.8.html

[27] Q-Chem Talk - Sign convention for electric field: https://talk.q-chem.com/t/change-in-energy-in-electric-field-is-not-what-i-would-expect/123

[28] VASP Wiki - Berry phases and finite electric fields: https://www.vasp.at/wiki/index.php/Berry_phases_and_finite_electric_fields

[29] VASP Wiki - EFIELD: https://www.vasp.at/wiki/index.php/EFIELD

[30] A.V.E.D.A. - Automated Variable Electric-Field DFT Application: https://github.com/ (PMC9830642)

[31] TUPÃ - Electric field analyses for molecular simulations: https://mdpoleto.github.io/tupa/

[32] pyEF - A Python Framework for QM and QM/MM Atom-Wise Electric Field: https://github.com/ (J. Chem. Theory Comput. 2026)

[33] Matter Modeling Stack Exchange - Quantum chemistry in external electrostatic field: https://mattermodeling.stackexchange.com/questions/6714

[34] Matter Modeling Stack Exchange - How to calculate energy of a molecule in an aligned electric field: https://mattermodeling.stackexchange.com/questions/1075

[35] Gaussian Prop keyword: https://wild.life.nctu.edu.tw/~jsyu/compchem/g09/g09ur/k_prop.htm

[36] Fried, S.D.; Boxer, S.G. (2015) "Measuring Electric Fields and Noncovalent Interactions Using the Vibrational Stark Effect", Acc. Chem. Res. 48, 998: https://doi.org/10.1021/ar500464j

[37] Sowlati-Hashjin, S.; Matta, C.F. (2013) "The chemical bond in external electric fields", J. Chem. Phys. 139, 144101: https://doi.org/10.1063/1.4824107

[38] Bursch, M. et al. (2022) "Best‐Practice DFT Protocols for Basic Molecular Computational Chemistry", Angew. Chem. Int. Ed. 61, e202205735.

[39] GROMACS 2025.2 Documentation - Electric Fields: https://manual.gromacs.org/documentation/2025.2/reference-manual/special/electric-fields.html

[40] NAMD 3.0 User's Guide - External Electric Field: https://www.ks.uiuc.edu/Research/namd/3.0/ug/node42.html
