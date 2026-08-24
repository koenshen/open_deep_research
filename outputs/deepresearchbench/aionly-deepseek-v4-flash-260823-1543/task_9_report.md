# 计算化学中模拟外加电场的方法：形式化实现、分子取向不确定性的处理与最佳实践

## 一、引言

在计算化学中模拟外加电场（external electric field, EEF）已成为研究电场催化（electrostatic catalysis）、振动斯塔克效应、非线性光学性质以及单原子催化剂（SAC）活性调控的重要手段。您提到的 Gaussian `field=x+100` 关键词确实是在哈密顿量中加入了一个均匀电场项的标准做法；然而，对于在真实反应环境中自由翻转、取向随机的分子催化剂（包括多数单原子/单分子催化剂体系），"在 x 方向施加电场"这一设定与真实物理图景之间确实存在一个根本性的**取向不确定性问题**。本报告系统梳理以下四个方面的文献与方法：

1. 外加电场在 Gaussian（及其他主流量子化学/第一性原理程序）中的正式实现方式；
2. 电场–分子相互作用的取向依赖性，以及"取向问题"在理论与实验中的表现；
3. 已有研究采用哪些协议（取向平均、反应轴对齐、分子固连坐标系、局域电场嵌入等）来弥合"模拟的方向性电场"与"自由取向分子真实感受的电场"之间的差距；
4. 单原子催化剂（SAC）与分子催化剂在外加电场下的计算研究实践，包括中文文献与国内研究组的工作。

---

## 二、外加电场在量子化学程序中的形式化实现

### 2.1 物理基础：Stark 哈密顿量与多极展开

外加均匀电场与分子的相互作用由 Stark 哈密顿量描述，其核心为偶极–场耦合项：

$$H' = -\boldsymbol{\mu} \cdot \mathbf{E}$$

即相互作用能 $U = -\boldsymbol{\mu}\cdot\mathbf{E} = -\mu E\cos\theta$，其中 $\theta$ 是分子偶极矩与外场方向之间的夹角 [1][2]。对中性体系，偶极算符为 $\hat{\boldsymbol{\mu}} = \sum_i q_i \mathbf{r}_i$；对电子（电荷 $q=-e$），该项相当于在单电子哈密顿量中加入 $-e\,\mathbf{r}\cdot\mathbf{E}$ 的势能项。量子力学微扰处理中，线性 Stark 效应由矩阵元 $-\mathbf{F}\cdot\langle \psi_k^0|\boldsymbol{\mu}|\psi_l^0\rangle$ 描述，而二阶（二次）Stark 效应通过极化率张量 $\alpha$ 进入能量表达式 [1]。对于含永久偶极的分子，一阶效应占主导；对无偶极的对称分子，仅剩二阶效应（$\alpha$ 恒为正，能量降低）[1]。更完整的静电相互作用多极展开为：

$$U = QV(0) - \boldsymbol{\mu}\cdot\mathbf{E}(0) - \tfrac{1}{6}\sum Q_{ij}\frac{\partial E_j}{\partial r_i} + \cdots$$

即偶极项之后还有四极矩（场梯度）及更高阶项；Gaussian 的 `Field` 关键词正是通过实现**直到十六极矩**的多极场系数来覆盖这一展开 [2][3]。

### 2.2 Gaussian 的 `Field` 关键词

Gaussian 官方文档（G16 Rev. C.01，2019 年更新）对 `Field` 关键词的说明如下 [3]：

- **功能**："The Field keyword requests that a finite field be added to a calculation. In Gaussian, the field can either involve electric multipoles (through hexadecapoles) or a Fermi contact term."
- **语法**：`M±N` 或 `F(M)N`。其中 `M` 指定多极类型（如 X 为偶极的 x 分量，XXYZ 为十六极矩分量），`F(M)N` 为原子 M 上的费米接触微扰；`N*0.0001` 给出场强（原子单位）。
- **示例**：`Field=X+10` 表示在 X 方向施加 0.001 a.u. 的偶极电场；`Field=XXYZ-20` 表示 0.0020 a.u. 的十六极矩场；`Field=F(3)27` 是自旋密度微扰 [3][4][5]。
- **您使用的 `Field=x+100` 对应 N=100，即场强 100×0.0001 = 0.01 a.u.**。这里需要特别注意单位：1 a.u. 电场 = $E_h/(e a_0)$ = 27.2114 V / 0.529177 Å ≈ **51.4 V/Å = 514 V/nm ≈ 5.142×10¹¹ V/m**。因此 `Field=x+100` 相当于 **0.514 V/Å ≈ 5.14×10⁹ V/m**。文献中常见的"1 a.u. = 5.142×10⁹ V/m"实际上是 0.01 a.u. 的值，完整的 1 a.u. 应为 5.142×10¹¹ V/m [6][7][8]。
- **注意事项**：官方文档明确警告"系数为笛卡尔算符矩阵的系数，解释结果时必须考虑符号约定"；所有参数基于输入取向（input orientation）；使用 Field 时禁用 archiving [3][4]。
- **选项**：`Read`（读入 34 个电多极分量）、`OldRead`（35 分量旧格式）、`RWF`/`ERWF`（从读写文件读取，ERWF 仅取 3 个偶极分量）、`Checkpoint`/`Chk`（从检查点文件读取）、`EChk`、`NoChK` 等 [3][4]。
- **可用计算类型**：单点能、几何优化、频率、Force 和 Scan [3]。
- **对称性限制**：如果场会降低分子对称性，数值导数可能出错，Gaussian 建议在 GVB 或一般数值导数计算中使用 `Guess=NoSymm`；几何优化必须使用 `Opt=Z-Matrix NoSymm`（官方给出甲烷 RHF/3-21G `Field=x+60` 和水的 HF/6-31G(d) `Field=z-50` 两个完整输入示例）[3][4][5]。该限制的物理原因正是**电场本身是极矢量，会打破与场方向垂直的镜面对称操作**。

### 2.3 其他分子量子化学程序

- **ORCA**：在 `%scf` 块中用 `EField` 关键词施加偶极场，如 `%scf EField 0 0 0.001 end`（分量单位为 a.u.）；另有 `QField` 施加四极场。官方手册强调：场作用于所有后 HF、多参考、TDDFT 方法；有解析梯度但**无解析 Hessian**；几何优化在场中会自动切换到笛卡尔坐标（内坐标会破坏转动对称性），且**过渡态优化尚不支持**；频率计算不会投影掉平动/转动 Hessian 贡献，这些模式可能出现非零频率并与振动混合。`EFieldOrigin` 可设定电势零点（固定原点适合模拟实验室外场；质心/核电荷中心原点适合有限差分性质计算）。ORCA 还明确警告：**隐式溶剂模型不能感知电场**，可能需要显式溶剂或惰性离子 [6]。符号约定："正 z 分量场对应负 z 方向的正电荷与正 z 方向的负电荷"——与其他程序可能不同 [6]。
- **Q-Chem**：没有独立的"均匀外场"关键词（文档中所见的 `EFIELD` 相关选项是计算分子自身静电势/电场，如 `ESP_EFIELD`，并非施加外场）。Q-Chem 的施加外场路径是**有限场（finite-field）极化率机制**：`JOBTYPE=POLARIZABILITY`、`FDIFF_STEPSIZE`（默认 1 a.u.）控制场微扰步长；Romberg 有限场程序用于高阶导数。此外可用 `$external_charges` 或 EFP 有效碎片势将环境电荷以单电子项加入哈密顿量，从而产生局域电场 [7][8]。
- **NWChem**：手册记载 `field [freq] [vector]` 指令施加外静电势场（频率单位 MHz），但开发者论坛确认静态均匀场可通过"把偶极算符乘以常数加进 Fock 矩阵"实现，或用点电荷替代 [9][10]。

### 2.4 周期性程序中的均匀电场

对于周期性体系，均匀电场势 $-e\mathbf{E}\cdot\mathbf{r}$ 是非周期的、无下界的，不能直接加入 Kohn–Sham 哈密顿量。现代实现基于**现代极化理论（Berry 相位）**：

- **VASP**（5.2 版起）：采用 Nunes–Gonze 与 Souza–Íñiguez–Vanderbilt 的 PEAD（Perturbation Expression After Discretization）方法，极小化电焓泛函 $E[\psi(\varepsilon),\varepsilon] = E_0[\psi(\varepsilon)] - \Omega\,\varepsilon\cdot \mathbf{P}[\psi(\varepsilon)]$，从而在绝缘体中加入有限均匀电场。相关标签包括 `EFIELD_PEAD`、`IPEAD`、`LPEAD`、`LCALCPOL`、`LBERRY` 等。当场强超过 $e|\varepsilon\cdot\mathbf{a}_i| > E_{\text{gap}}/(10N_i)$ 时，电焓泛函失去极小值，程序会给出警告 [11][12][13]。Souza、Íñiguez 与 Vanderbilt 的 PRL 2002 [12] 是该方法的奠基文献；Stengel–Spaldin–Vanderbilt 进一步提出以电位移 D 为基本变量的约束-D 方法（Nature Physics 2009）[14]。
- **Quantum ESPRESSO**：同样基于现代极化理论，`&CONTROL` 中 `lelfield=.TRUE.`、`gdir`（场方向）、`nppstr`（每条 k 点弦上的点数），`&ELECTRONS` 中 `efield`（a.u.）与 `efield_cart`；官方 example10 以体相硅介电常数为例 [15]。
- **CP2K**：`PERIODIC_EFIELD`（Berry 相位方法，仅限 OT 轨道变换，不可与 RTP/EMD 共用）；`EFIELD` 节为含时电场（用于实时 TDDFT 传播，不能用于静态几何优化）；**静态均匀场的官方推荐做法是用 `EXTERNAL_POTENTIAL` 加一个线性势 $V(z)=(a/b)z$**，其电场强度即斜率（如 0.5 eV/Å 给出 0.5 V/Å 的场），注意符号约定（电子带负电）[16][17]。
- **OpenMX**：用锯齿波（sawtooth）势施加均匀电场，`scf.Electric.Field 1.0 0.0 0.0`（单位 GV/m，符号指"作用于电子的场"）[18]。
- **NAMD**（分子动力学）：`eField` 矢量，单位 kcal/(mol·Å·e)；`eFieldNormalized` 用于周期性盒子确保跨盒电压降 [19]。
- 非官方但常用的工程做法（VASP）：使用 `EFIELD`（单位 eV/Å，数值上即 V/Å）配合 `LDIPOL=.TRUE.`、`IDIPOL`（方向）、`DIPOL`（偶极原点），并要求关闭对称性；场效应表现为真空区局域势的斜率。VASP 论坛确认：VASP 中 1 eV/Å 的势梯度即实验室 1 V/Å 的电场，因为程序以 eV 为能量单位 [20]。**注意 VASP `EFIELD` 的方向是使电子受力的方向，与常规电场方向相反**。

### 2.5 场强标度：计算中该用多大的场？

这是模拟中最关键的实际问题。文献中的典型场强范围如下 [6][21]：

| 环境/体系 | 典型场强 | 换算 |
|---|---|---|
| 电极表面（电解条件） | ~0.1 V/Å | 10 V/nm |
| 蛋白质带电残基、STM 针尖 | ~1 V/Å | 100 V/nm |
| 酶活性中心（振动 Stark 测量） | 139–180.5 MV/cm | 0.14–0.18 V/Å |
| 微流控双电层（EDL） | 0.61–1.26 V/nm | 0.061–0.126 V/Å |
| 气液界面水分子 | ~10–16 MV/cm | 0.1–0.16 V/Å |
| 单分子结（STM-BJ） | 10⁸–10⁹ V/m | 0.1–1 V/Å |

Shaik 课题组关于定向外电场（OEEF）催化的计算通常使用 0.001–0.01 a.u.（约 0.05–0.5 V/Å）；Yu 与 Bickelhaupt 的 Diels–Alder 研究限幅 ±0.008 a.u.（约 4 V/nm = 0.4 V/Å）[22]。酶工程文献中的"设计局域电场"多在 0.1–0.2 V/Å 范围 [23][24]。单原子催化剂的外场模拟则常见 0.2–1.2 V/Å（见第五节）。

---

## 三、分子取向依赖性与"取向问题"

### 3.1 取向依赖性的物理根源

电场–分子相互作用能 $U = -\boldsymbol{\mu}\cdot\mathbf{E} = -\mu E\cos\theta$ 明确显示：**沿不同分子取向，同一外场对分子的影响不同**。对化学反应而言，更精确的表述是 Siddiqui、Stuyver、Shaik 与 Dubey 在 JACS Au 2023 中给出的方程 [23]：

$$\Delta\Delta E = -\vec{F}\cdot\Delta\vec{\mu}$$

即反应路径上任意两点（如反应物与过渡态）之间能量差的改变，等于外场矢量与这两点偶极矩之差矢量（"反应偶极"）的点积。这意味着：**只有当外场沿反应偶极方向有分量时，才能有效改变反应能垒**；垂直于反应偶极的场几乎不起作用。这正是"取向问题"的定量表达。

### 3.2 OEEF 领域的"反应轴规则"与取向难题

Shaik 学派二十余年的研究表明，外场对化学反应的调控遵循**反应轴规则（Reaction Axis Rule）**：将 OEEF 沿着"电子重组方向"（反应物电子结构转化为产物电子结构的方向，即反应轴）施加时，可以催化反应（场强 ~0.1–0.5 V/Å 即可产生数量级速率变化）；反向施加则抑制反应；偏离反应轴可控制立体/区域/对映选择性；双向场可同时控制反应性与选择性 [17][25][26][27][28]。

但该范式的前提是**分子相对于外场的方向是确定的**。Shaik 等人在 Nature Chemistry 2016 综述中明确列出这一挑战："定义场方向（反应轴可能模糊）、溶剂处理（MD 与量子计算耦合）以及**制备规模上的取向问题**（orientation problem for preparative scale）"，并指出现有实验解决途径包括 STM 单分子结、Kanan 的电化学双电层界面场、微反应器等 [17]。2020 年 JACS Perspective 进一步总结："**获取这一工具箱的关键，是在分子与外加场之间实现微观尺度上的对齐控制**（microscopic control over the alignment between the molecule and the applied field）" [26]。

真实溶液环境中，分子自由翻滚，热能 $kT$ 与取向偶极势能 $-\mu E\cos\theta$ 竞争。Vacek 与 Michl 对网格安装的偶极转子的经典分析给出了判据：室温下 $kT/\mu \approx 140$ kV/cm（对 42 D 的转子），即 ~0.014 V/Å——**低于此场强时热运动主导取向，高于此场强时分子才被显著取向** [29]。另一个极端是所谓的"orienting"（取向中）与"oriented"（已取向）之分：自由极性分子在外场中受到转矩而转动，场内分子并非静止固定在某一角度，而是在转动势能面上重新分布 [30]。

### 3.3 "定向场"假设在柔性分子上的失效

2026 年 Lai 与 Matthews 在 JCTC 发表的论文直接以"实验室坐标系（LF）场对柔性分子失效"为出发点："在实验室坐标系定义电场，对柔性分子会失效，因为构象变化会显著改变外场与分子结构之间的相对取向"[31]。他们给出了酮-烯醇互变异构单分子结的算例：**实验室坐标系优化允许整分子旋转约 102°，产生误导性的非线性烯醇–酮能隙**；而将场固定在分子参考系后，能隙随场近似线性变化，并在 0.03 a.u. 处发生互变异构稳定性反转 [31]。

此外，2025 年的 arXiv 预印本引入"directomers"（定向异构体）概念：CO 与 OCS 在 0.01–0.05 a.u. 场下，分子的转动势能面出现两个极小（场与分子轴夹角 0° 与 180°），键长相差可达 0.03 Å，能量差近 2 kcal/mol——**即使对刚性小分子，"分子相对场的方向"也是一个必须显式处理的自由度**，其影响可类比于构象异构 [30]。

---

## 四、处理取向不确定性的方法论与协议

### 4.1 反应轴对齐：OEEF 计算的标准范式

在 Shaik 学派的计算协议中，外场方向不是任意的实验室坐标轴，而是**沿反应轴（由化学直觉或计算确定的电子重组方向）施加**。计算上确定反应轴的客观方法是取反应物（或中间体）与过渡态的偶极矩差矢量 $\Delta\vec{\mu} = \vec{\mu}^{\ddagger} - \vec{\mu}^{\mathrm{R}}$，将其归一化后作为场方向 [32]。

Hanaway 与 Kennedy 2022 年在 J. Org. Chem. 发布的 **A.V.E.D.A.**（Automated Variable Electric-field DFT Application）工具将这一流程自动化，并做了重要的方法论验证 [32]：

- 输入两个 .xyz 文件（反应物与过渡态），RMSD 对齐后转换为 **Z 矩阵格式——该格式约束了转动自由度**，防止场导致整分子旋转；
- 场强扫描 ±2.5、±5.0、±7.5、±10.0（×10⁻³ a.u.），在 11 个周环反应上用四种泛函验证；
- **用均匀分布于单位球面的 20 个场矢量测试"最优场沿反应偶极方向"这一假设，结果表明假设成立**；
- 反应偶极大小与活化能变化呈强线性相关（R² = 0.987），支持 Fried–Boxer 线性关系 $\Delta E(\mathrm{kcal/mol}) = 4.8\cdot F(\mathrm{V/\AA})\cdot \mu(\mathrm{D})$ [32][25]。

这一协议的核心思想是：**既然真实分子取向随机，那就报告"沿反应轴方向施加单位场"这一取向不变的内在响应**——对于评估电场催化潜力，这是最物理、最可迁移的量。

### 4.2 分子固连坐标系（PAF/LRF）：柔性分子的严格解法

Lai 与 Matthews（2026，PySCF 实现）提出在**分子固连坐标系**中定义电场并推导解析梯度，从根本上消除"实验室场 + 柔性分子"的模糊性 [31]：

- **主惯性轴系（PAF）**：由质量转动惯量张量的本征矢量定义，唯一描述刚性转动；但对对称/球形陀螺分子（简并惯量矩）不适用。
- **局域参考系（LRF）**：由三个不共线原子构建，直接对应化学解释（如 STM 结中锚定端基、FET 器件中的固定原子）。
- 梯度包含场自由梯度 + 分子偶极导数 + 场随框架旋转的导数三项；在 cis-/trans-甲酰苯胺 CCSD/cc-pVTZ 上验证到 10⁻⁶ a.u. 精度。
- 关键结论："实验室固定场可能引入与实验约束系统不一致的**人为转动效应**，而分子坐标系提供了对场响应的物理描述" [31]。

对于"自由取向的分子催化剂"，PAF/LRF 提供了一种**取向不变的模拟语言**：计算在分子坐标系下的响应（几何形变、能垒变化），再通过取向平均或与实验锚定场景对照来解释。

### 4.3 取向扫描与取向平均

当需要将理论结果与真实（自由取向）环境对接时，文献中有两种互补策略：

1. **取向扫描（rotational PES）**：将场方向相对分子框架在一定角度范围内扫描，构建转动势能面。directomers 预印本在 0°–180° 范围内扫描场角，识别双阱结构与准过渡态，并用"偶极–极化率模型"（$\Delta E(\theta) = -\mu\varepsilon\cos\theta - \frac{1}{2}\Delta\alpha\varepsilon^2\cos^2\theta$）作为廉价替代 [30]。Åstrand 2024 年的解析电离能模型同样明确以"免去对每个场强/每个取向重复量子化学计算"为目标 [33]。
2. **取向平均（rotational/orientational averaging）**：按 Boltzmann 分布对取向求平均。Wikibooks 的分子模拟教程给出了偶极–点电荷体系取向平均的一般形式 [34]；J. Chem. Phys. 2024 的方法论文指出，取向平均等价于在三维欧拉角（四维单位球面）上积分，体系对称性可降低维度 [35]。对催化速率，原则上可计算 $k_{\text{avg}} = \int k(E,\theta)\,P(\theta)\,d\theta$，其中 $P(\theta)\propto \exp(\mu E\cos\theta/kT)$；但如果场强本身在实验上不能精确控制，这种平均的意义有限——这也是目前 OEEF 计算文献中取向平均较少直接使用的实际原因。

**实际采用的折中做法**是：报告沿反应轴（最优方向）的场效应上/下限，同时报告垂直方向几乎无效的"选择规则"（reaction-axis rule），从而告诉实验者"哪个方向的场值得去制造" [17][26]。

### 4.4 设计局域电场（LEF）与 QM/MM 嵌入：让环境自身产生场

一个重要的方向性思路是：**不直接施加均匀外场，而是在分子中嵌入电荷/偶极基团（或环境残基），让分子自身的局域电场（LEF）作用于反应中心**。Shaik 学派证明 **LEF 与 OEEF 等价、遵循同样的规则** [26]。这从根本上游刃有余地绕开了取向不确定性问题——因为场的方向由分子结构中带电基团的几何位置决定，是分子内禀属性 [23][26]。

具体工具与案例 [23]：
- **TITAN** 与 **TUPA**（开源 Python 工具）：从 QM/MM 或 MD 轨迹计算酶活性位点的电场。
- **LADH 醇脱氢酶**：Ser48Thr 突变 + Zn²⁺→Co²⁺ 使活性位点沿羰基键方向的场增强，预测并实验验证了 50 倍氢转移速率提升。
- **Kemp 消除酶**：4 个理性设计突变将活性位点场定向改造，能垒降低 2.5 kcal/mol，kcat 从 0.007 增至 0.31 s⁻¹（43 倍）。
- **PaAPase**：Asp135→Arg135 使局域场从 −15.3 反转为 +21.5 MV/cm，磷酸化/水解比提升 2.9 倍。
- **超分子卟啉笼**：将 LEF 沿 Fe–O 轴取向，实现可切换的 R/S 对映选择性。

对单原子催化剂，同样的逻辑体现在**载体工程**上：如 Shao 等 2026 年在 Nano Research 用铁电 In₂Se₃ 衬底的固有极化（±0.09 eÅ 偶极）在 FeN₄–C 活性位点产生局域场，在恒电势 DFT（VASP + VASPsol++）下将酸性 ORR 过电位降至 0.35 V，且发现 *OH 吸附能随场近似线性变化（极化率 0.08 eÅ²/V）而 *OOH 呈二次变化（0.52 eÅ²/V），从而**打破传统标度关系** [36]。这也与 Vijay 等 (ACS Catal. 2020) 对 Fe–N–C 单原子催化剂 CO₂RR 的结论一致：**CO₂ 还原活性由"偶极–场相互作用"决定**，速率决定步骤是场驱动的 CO₂ 吸附而非电子转移 [37]。

### 4.5 单分子结/表面锚定：实验上固定取向

在单分子器件实验中，取向不确定性通过物理锚定解决：STM 断裂结（STM-BJ）、机械可控断裂结（MCBJ）、石墨烯–分子–石墨烯结等将单个分子定向连接在两个电极之间，电场方向即分子轴方向 [38][39]。

- **Aragonès 等 (Nature 2016)**：Diels–Alder 反应在 STM 结中，负偏压使产物形成率提高 4.4 倍；正偏压无催化效应——取向相关的直接实验证据 [38][39]。
- **Huang 等 (Science Advances 2019)**：单分子定向连接后，**平行于反应轴的场可将反应速率提高一个数量级以上，垂直于反应轴的场无任何效果** [39][40]。
- **Tang 等**：Menshutkin 反应的单分子器件中实现 39,000 倍催化增强 [25]。
- 微流控双电层（Nature Communications 2024）：电极表面 EDL 产生 0.61–1.26 V/nm 的定向场，电场方向由电极极性决定，反转极性使产率下降约 73% [41]。

对计算化学家的启示：**如果目标体系对应这类锚定实验，那么实验室坐标系的定向场是合理的；如果对应溶液中的自由分子，则应采用反应轴报告 + 取向平均的协议**。

### 4.6 场自由参考态与符号约定

所有规范的计算协议都要求以**零场（field-free）参考态**为基准报告场效应：

- A.V.E.D.A. 以零场反应物/TS 结构为基准计算 $\Delta\Delta E^{\ddagger}$ [32]；
- directomers 以零场 CO 平衡键长 1.129 Å 为参考报告场致形变 [30]；
- 廖俊超在科技导报的 Diels–Alder 研究中以 $F_Z=0$ 的速率常数（exo 2.524×10⁻⁸、endo 8.652×10⁻⁷ M⁻¹s⁻¹）为基准，给出 ±257.1 与 +514.2 mV/Å 下的速率变化 [42]。

同时必须显式报告**符号约定**：Gaussian 文档提醒场系数采用笛卡尔算符矩阵约定 [3]；ORCA 的 EField 正 z 定义与其他程序不同 [6]；VASP 的 EFIELD 方向是电子受力方向，与常规电场方向相反 [20]。建议在论文中同时给出场矢量与作用在正电荷上的电场方向的关系。

### 4.7 显式环境与隐式溶剂化的局限

ORCA 手册明确警告：**隐式溶剂模型无法感知外场，溶剂不感受场**；显式溶剂或惰性离子（Na⁺、Cl⁻）可能是必要的，双电层效应需要 MD + 显式离子 [6]。Wright 等（JPCL 2022）的实验+DFT 研究表明，对电极上的自组装单分子层，**均匀场 DFT 无法同时重现多个振动模的 Stark 位移，必须显式建模离子在双电层中的运动（~2 Å 位移即可解释全场分子振动模的位移）** [43]。English 对晶体态的模拟综述也强调恒温器与场幅度选择的重要性，一般线性响应区约在 0.5 V/Å 以下 [44]。对于电催化界面，恒电势方法（grand canonical DFT、VASPsol、JDFTx、AIMD + 半经典 EDL 模型）是比"固定外场"更物理的替代方案 [36][45]。

---

## 五、单原子催化剂外加电场模拟的计算实践

### 5.1 代表性研究

近年已有多项第一性原理研究直接考察外加电场对单原子催化剂（SAC）活性的调控，现按体系与场强汇总如下：

**1. Pan 等，Nature Communications 13, 3063 (2022)——SAC + OEEF 的奠基性工作（南京大学/加州大学洛杉矶分校）** [46]

- 实验（背栅电压 Vg = ±40 V、275 nm SiO₂ 介质）+ DFT 结合；DFT 场强范围 **−0.4 至 +0.4 V/Å**。
- Pt 单原子/n-MoS₂：正 OEEF 将 HER 过电位降至 20 mV（10 mA cm⁻²）、Tafel 斜率 51 mV dec⁻¹；Co 单原子/p-WSe₂：负 OEEF 将 OER 过电位降至 139 mV（64 mV dec⁻¹）。
- 机制为"**原位静电极化（onsite electrostatic polarization）**"：正场增强 *H 吸附位电子密度、促进 Heyrovsky 步骤；负场降低 *O 位电荷密度、促进 OH⁻ 接近、降低 *O→*OOH 步能垒。**所有 SAC 无论载体 n 型/p 型/金属型，对场方向的响应一致**——与载体载流子调制机制形成鲜明对比。
- 作者指出此类场调控"为模拟天然酶催化过程提供了定量、精确、动态的外电场策略"。

**2. Ma 等，Applied Surface Science 747, 167711 (2026)——Pt 单原子/MXene 的 CO₂RR（VASP, PBE, DFT-D3）** [47]

- 外加 **1.0 V/Å** 的电场（垂直于二维 MXene 平面）触发 CO₂ 从物理吸附到化学吸附的转变，增强电荷转移、轨道杂化与 Pt–CO₂ 成键。
- 电场使 Pt d 带中心上移并增强电子局域化；降低 CO 产物的极限电位，可改变电位决定步骤；但 CO 选择性与载体种类强相关（仅 Ti、Hf 基底上有利）。

**3. Song 等，Applied Surface Science 695, 162886 (2025)——MN₄/MXene 异质结界面场** [48]

- 界面电场 **0–1.2 V/Å（步长 0.2 V/Å）**；在 0.2 V/Å 下 FeN₄/Ti₂NO 展示优异的 OER 过电位（0.28 V）。
- 机器学习 + 符号回归建立 ORR/OER 描述符；M₂NO 载体的轴向牵引弱化 M-3d 与中间体 p 轨道的相互作用。

**4. Abdel Aal 等，Surfaces and Interfaces 73, 107475 (2025)——TM@C₂₄N₂₄ 纳米笼** [49]

- 比较 0 与 **0.5 V/Å** 外场；Ir@C₂₄N₂₄ 的 $\Delta G_{H^*} = -0.024$ eV，优于 Pt(111)（~0.09 eV）；外场使能隙变窄、电导增强、HER 动力学势垒降低。

**5. Lu 等，Physica B 638, 413934 (2022)——Pt/石墨烯的 O₂ 活化** [50]

- 递增 EEF 促进 O₂ 活化；表面→O₂ 的电荷转移形成过氧负离子 O₂²⁻；EFE 调控 O₂ 活化的内部机制经电子结构分析阐明。

**6. Shao 等，Nano Research (2026)——铁电衬底局域场 + 恒电势 DFT** [36]

- 用 In₂Se₃ 铁电极化（↑/↓）产生局域电场；FeN₄–C@In₂Se₃↓ 在酸性下 ORR 过电位 0.35 V；*OH 吸附能随场近线性、*OOH 二次变化，可打破标度关系；d 带中心（−0.55 eV）不能单独预测活性。

**7. Vijay 等，ACS Catalysis (2020)——Fe–N–C 的偶极–场相互作用** [37]

- CO₂ 的弯曲构型产生 >0.4 eÅ 的界面偶极，被表面场稳定；速率决定步骤是"场驱动的 CO₂ 吸附"而非电子转移，解释了实验上 pH 无关的 CO 产率。
- 方法学要点：GGA（RPBE）严重高估 CO 毒化，需 HSE06 或 RPBE+U(U=2 eV)；单原子催化剂的活性不仅能通过结合能调谐，还能通过**表面中间体的偶极矩**调谐。

**8. Chen 等，ACS Catalysis 6, 7133 (2016)——双电层阳离子的场效应（Ag(111) CO₂RR）** [51]

- 显式建模双电层中溶剂化阳离子产生的电场（而非加均匀场标签）；微动力学模型无拟合参数复现实验极化曲线。

**9. Yun 等，Journal of Catalysis 450, 116226 (2025)——IrO₂(110) 烷烃转化** [52]

- 正/负电场极性调控 CH₄、C₂H₆ 转化的分支点（branching point）：负场抑制 CH₂OH 生成、促进 C₂H₄ 收率；正场促进 C₂H₃→C₂H₄(g) 脱附。DFT + 微动力学（TPRS 模拟）。

**10. Wu 等，Phys. Rev. Materials 9, 055801 (2025)——恒电势下 Fe–N–C 的 O₂ 吸附** [53]

- 恒电势（非固定场）方法揭示 O₂ 吸附能随电位升高而减弱，源于 FeN₄ 基底电子结构变化与零电荷电位上移；O₂ 吸附能差对电位呈二次依赖，抛物线开口由量子电容差决定。

### 5.2 周期性计算中施加电场的具体操作

对二维 SAC 模型（如单原子/多孔 C₃N₄、MXene、石墨烯），VASP 施加均匀场的推荐流程 [11][20]：

1. 构建 slab + 足够真空层（≥15 Å），保证场致电荷不泄漏到真空；
2. 设置 `EFIELD = 0.2`（eV/Å，数值上等于 V/Å）、`LDIPOL = .TRUE.`、`IDIPOL`（方向，如 3 为 z）、`DIPOL`（设为结构质心）；
3. **关闭对称性**（`ISYM = 0`），因为均匀场破坏中心对称；
4. 通过**真空区局域势的斜率**验证实际电场强度与设定值一致；
5. 注意 VASP 场方向定义（电子受力方向）与常规电场方向相反；
6. 对绝缘体/半导体，场强须满足 Berry 相位稳定性判据（$e|\varepsilon a_i| \ll E_{\text{gap}}/N_i$）；
7. 场致能量修正：必要时对总能做 $E_{\text{total}} = E_{\text{SCF}} - \mathbf{dipole}\cdot\mathbf{E}$ 的偶极修正 [20]。

分子催化剂（Gaussian 等）则用 `Field=` 关键词 + `NoSymm` + Z 矩阵约束，按 4.1–4.2 节的协议进行。

### 5.3 场强选择与实验校准的实践建议

- 计算文献对 SAC 使用的场强（0.2–1.2 V/Å）普遍高于酶/溶液环境的实验值（0.01–0.2 V/Å），但接近 STM 单分子结与强 EDL 微环境的上限 [6][21][41][46]。
- 建议做法：**先确定目标实验场景**（电化学双电层 ≈ 0.01–0.1 V/Å；STM 结 ≈ 0.1–1 V/Å；强极化界面/铁电衬底 ≈ 0.1–0.5 V/Å），再选择计算场强；做 3–5 个场强的线性扫描，检查响应是否为线性（若非线性明显，说明场强已进入非物理区域或机制切换区域）。
- 报告时同时给出 a.u. 与 V/Å（或 V/nm）两套单位，避免换算错误。

---

## 六、中文文献与国内研究进展

### 6.1 中文期刊上的外电场计算研究

按研究简报要求优先检索《物理化学学报》《催化学报》《中国科学:化学》等中文期刊，未发现直接以"分子取向 + 外加电场 + 催化"为主题的综述；但以下中文期刊发表了直接相关的原创计算研究：

- **《科技导报》（Science & Technology Review）**：廖俊超《电子结构视角下的定向外部电场对 Diels–Alder 反应调控机理》。KS-DFT 研究环戊二烯 + 甲基乙烯基酮；$F_Z>0$ 加速反应并提高 endo 选择性，$F_Z<0$ 减速并偏向 exo；给出 298.15 K 下 −257.1、0、+257.1、+514.2 mV/Å 四档场强的速率常数（endo：8.652×10⁻⁷ → 2.940×10⁻⁵ → 1.963×10⁻³ M⁻¹s⁻¹）[42]。
- **《计算物理》2025, 42(4)**：C₃F₆O 分子在 y 方向 0–0.07 a.u. 外电场下的光谱与激发特性（B3LYP/6-311G+(3d,3p)，Gaussian 16，Multiwfn 空穴-电子分析）。总能量从 −788.8546 降至 −789.019463 a.u.，偶极矩从 0.457 增至 12.27 D，HOMO–LUMO 能隙从 5.93 eV 降至 1.27 eV [54]。
- **《物理学报》2013, 62(7), 073103**：ZnO 分子沿 O–Zn 分子轴方向 ±0.05 a.u. 外电场（B3P86/6-311++g(d,p)，Gaussian 03）；键长在 0.02 a.u. 处取极小，能隙单调减小 [55]。
- **《计算物理》2026, 43(3)**：2-氯苯酚与 4-氯苯酚在沿 C→Cl 键方向 ±0.025 a.u. 场下的光谱与解离特性；文中明确讨论了**分子固有偶极与外加场方向之间的夹角（约 30°）对解离动力学的影响**——这是中文文献中罕见的显式讨论取向角的工作 [56]。
- **汪灝 2024 年台湾大学硕士论文**《利用定向電場增強二維材料邊緣的電化學活性》：氟化石墨烯/石墨烯/MoS₂ 异质结纳米带边缘的局部 OEFE 使界面电荷转移速率提升两个数量级（EIS 验证）；DFT 归因于场致吸附能降低 [57]。

### 6.2 国内课题组的英文期刊工作

- **Pan 等 Nature Communications 2022**（南京大学马晶、丁梦宁课题组）：SAC + OEEF 的奠基工作 [46]。
- **Shao 等 Nano Research 2026**（清华大学深圳国际研究生院）：铁电衬底局域场 + 恒电势 DFT [36]。
- **Ma 等 Applied Surface Science 2026**（河南理工大学）：Pt/MXene CO₂RR 场调控 [47]；**Lu 等 Physica B 2022**（河南多所高校）[50]；**Song 等 2025**（陕西）[48]——均为 NSFC 资助。
- **Huang 等 Science Advances 2019**（厦门大学洪文晶、程俊课题组）：电场诱导单分子反应选择性催化 [40][39]。

这些工作表明，国内课题组在外场–SAC 模拟领域已形成"实验（背栅/电化学）+ 周期性 DFT 外场 + 电子结构分析（Bader、d 带、晶体轨道 Hamilton 布居）+ 微动力学"的成熟范式。

---

## 七、最佳实践总结

综合上述文献，对"自由取向的分子/单原子催化剂在外加电场下的模拟"，推荐以下最佳实践：

1. **明确物理场景**：自由溶液分子、锚定单分子结、电极/双电层界面、还是酶/载体局域场环境？场景决定场强的量级与取向处理方式。
2. **场强单位与换算**：牢记 1 a.u. = 51.4 V/Å = 514 V/nm ≈ 5.14×10¹¹ V/m；`Field=x+100` 为 0.01 a.u. ≈ 0.514 V/Å。文献报道务必同时给出 a.u. 与实用单位。
3. **能垒变化用反应偶极判断**：先计算 $\Delta\vec{\mu} = \vec{\mu}^{\ddagger}-\vec{\mu}^{\mathrm{R}}$，沿该方向（反应轴）施场；垂直方向施场通常无效（反应轴规则）。可用 Fried–Boxer 方程 $\Delta E(\mathrm{kcal/mol})\approx 4.8\,F(\mathrm{V/\AA})\,\mu(\mathrm{D})$ 快速估算。
4. **柔性分子用分子固连坐标系**（PAF/LRF）或 Z 矩阵/内坐标约束防止人工整分子旋转；有条件时用解析梯度（PySCF 的 OEEF 实现）。
5. **进行取向敏感性检查**：至少扫描反应轴正反两个方向；条件允许时构建转动势能面（directomers 方法）或做 20 矢量球面采样（A.V.E.D.A. 方法）。
6. **始终与零场参考态比较**，并报告符号约定（Gaussian 笛卡尔算符约定、ORCA 正 z 定义、VASP 电子受力方向）。
7. **对称性处理**：Gaussian 用 `NoSymm`/`Opt=Z-Matrix NoSymm`；VASP 用 `ISYM=0` + `LDIPOL`/`IDIPOL`/`DIPOL`。
8. **环境建模**：隐式溶剂不能感知外场；双电层/界面体系需要显式水、离子或恒电势方法（VASPsol、JDFTx、grand canonical DFT）；周期性绝缘体注意 Berry 相位场强上限。
9. **利用 LEF 等价性**：当"外场"难以定义或取向无法控制时，考虑在分子中嵌入带电基团/载体极化产生局域场（Shaik 等价性证明），或与 QM/MM（TITAN/TUPA）结合。
10. **用实验锚定场强**：STM 结 ~0.1–1 V/Å、酶活性位点 ~0.14–0.18 V/Å、电极 ~0.01–0.1 V/Å、微流控 EDL ~0.06–0.13 V/Å；SAC 计算中 0.2–1.2 V/Å 属于强场筛选区，应说明对应何种极端微环境。

---

## 八、结论

外加电场在计算化学中的形式化实现已经非常成熟：分子程序（Gaussian `Field=`、ORCA `EField`、Q-Chem 有限场）通过向哈密顿量加入 $-\boldsymbol{\mu}\cdot\mathbf{E}$ 项实现均匀场；周期性程序（VASP、QE、CP2K）通过现代极化理论/Berry 相位或线性外势实现。真正的挑战在于取向：均匀场的效应本质上依赖于场与分子（及反应偶极）的相对取向，而自由取向的柔性分子催化剂在实验环境中不存在唯一定义的"x 方向"。

文献已经发展出多层次应对策略：(i) Shaik 学派的"反应轴对齐 + 方向选择规则"报告取向不变的内在响应；(ii) A.V.E.D.A. 与分子固连坐标系（PAF/LRF）消除柔性分子的人为旋转；(iii) 转动势能面扫描与 Boltzmann 取向平均实现定量对接；(iv) 设计局域电场（LEF）/载体极化/单分子结锚定在源头上固定或内化场方向；(v) 显式环境（溶剂、离子、恒电势界面）让场的分布由物理决定而非人为指定。对单原子催化剂，以 Pan 等 Nature Communications 2022 为代表的"原位静电极化"机制表明，场方向（正/负）确实可以定量调控 HER/OER 活性且与载体类型无关——这是外电场模拟从"理想化微扰"走向"实验可实现的催化调控手段"的重要一步。

---

### Sources

[1] Stark effect - Wikipedia: https://en.wikipedia.org/wiki/Stark_effect
[2] Gruebele Group Chem 542 Notes, "Multipole couplings and static external fields": https://gruebelegroup.web.illinois.edu/wp-content/uploads/Course/Chem_542/Note/notes.part9_.pdf
[3] Field | Gaussian.com: https://gaussian.com/field
[4] Gaussian 09 User's Reference: Field (mirror): https://wild.life.nctu.edu.tw/~jsyu/compchem/g09/g09ur/k_field.htm
[5] Gaussian 98 Help: Field Keyword (mirror): https://wanglab.hosted.uark.edu/g98help/00000434.htm
[6] ORCA 6.1.1 Manual, Section 2.17 "Finite Electric Fields": https://orca-manual.mpi-muelheim.mpg.de/contents/essentialelements/finEfield.html
[7] Q-Chem 6.0 Manual, 10.13.2 "Numerical Calculation of Static Polarizabilities": https://manual.q-chem.com/6.0/sec_finite-field.html
[8] NWChem RT-TDDFT Documentation: https://nwchemgit.github.io/RT-TDDFT.html
[9] NWChem Properties Documentation: https://nwchemgit.github.io/Properties.html
[10] NWChem Google Groups: applying external electric field: https://groups.google.com/g/nwchem-forum/c/dgwciFYxAY4
[11] VASP Wiki: Berry phases and finite electric fields: https://www.vasp.at/wiki/index.php/Berry_phases_and_finite_electric_fields
[12] Souza, Íñiguez & Vanderbilt, PRL 89, 117602 (2002): https://journals.aps.org/prl/abstract/10.1103/PhysRevLett.89.117602
[13] Quantum ESPRESSO PW/examples/example10: https://gitlab.com/QEF/q-e/-/tree/qe-6.4.1/PW/examples/example10
[14] Stengel, Spaldin & Vanderbilt, Nature Physics 5, 304–308 (2009): https://www.nature.com/articles/nphys1185
[15] CP2K Manual: EFIELD section: https://manual.cp2k.org/trunk/CP2K_INPUT/FORCE_EVAL/DFT/EFIELD.html
[16] CP2K Google Groups: About applying electric field in CP2K: https://groups.google.com/g/cp2k/c/dzKJKOVH4Ok
[17] Shaik, Mandal & Ramanan, "Oriented electric fields as future smart reagents in chemistry," Nature Chemistry 8, 1091–1099 (2016): http://jupiter.chem.uoa.gr/thanost/papers/papers1/NatChem_8(2016)1091.pdf
[18] OpenMX User's Manual v3.9: Electric field: https://www.openmx-square.org/openmx_man3.9/node89.html
[19] NAMD 3.0 User's Guide: External Electric Field: https://www.ks.uiuc.edu/Research/namd/3.0/ug/node42.html
[20] VASP Forum: units of electric field in VASP; conversion to volts/length: https://vasp.at/forum/viewtopic.php?t=19789
[21] Zheng, Ji, Mathews & Boxer, "Enhanced active-site electric field accelerates enzyme catalysis," Nature Chemistry 14, 891 (2022): https://www.osti.gov/pages/servlets/purl/2405210
[22] Yu, Vermeeren, Hamlin & Bickelhaupt, "How Oriented External Electric Fields Modulate Reactivity," Chem. Eur. J. 27(18), 5683 (2021): https://pmc.ncbi.nlm.nih.gov/articles/PMC8049047
[23] Siddiqui, Stuyver, Shaik & Dubey, "Designed Local Electric Fields—Promising Tools for Enzyme Engineering," JACS Au (2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC10752214
[24] Léonard, Dhaoui, Chantarojsiri & Yang, "Electric Fields in Catalysis: From Enzymes to Molecular Catalysts," ACS Catalysis 11(17), 10923 (2021): https://pmc.ncbi.nlm.nih.gov/articles/PMC9560040
[25] Shaik, Danovich, Kalita & Dubey, "Oriented Electric Fields—Universal Catalysts," Acc. Chem. Res. 58(19), 3071 (2025): https://pubs.acs.org/doi/10.1021/acs.accounts.5c00508
[26] Shaik et al., "Electric-Field Mediated Chemistry," JACS 142(29), 12551–12562 (2020): https://pubmed.ncbi.nlm.nih.gov/32551571
[27] Stuyver, Danovich, Joy & Shaik, "External electric field effects on chemical structure and reactivity," WIREs Comput. Mol. Sci. 10(2), e1438 (2020): https://wires.onlinelibrary.wiley.com/doi/abs/10.1002/wcms.1438
[28] Shaik, Ramanan, Danovich & Mandal, "Structure and reactivity/selectivity control by oriented-external electric fields," Chem. Soc. Rev. 47, 5125–5145 (2018): https://pubmed.ncbi.nlm.nih.gov/29979456
[29] Vacek & Michl, "Molecular dynamics of a grid-mounted molecular dipolar rotor in a rotating electric field," PNAS 98(10), 5481–5486 (2001): https://www.pnas.org/doi/10.1073/pnas.091100598
[30] "On the existence of distinct equilibrium configurations under orienting external electric fields," arXiv:2605.08494: https://arxiv.org/html/2605.08494v1
[31] Lai & Matthews, "Analytic Nuclear Gradients Including Oriented External Electric Fields in a Molecule-Fixed Frame," J. Chem. Theory Comput. 22(14), 7192–7203 (2026): https://pubs.acs.org/jctcce/article/22/14/7192/5195513/Analytic-Nuclear-Gradients-Including-Oriented
[32] Hanaway & Kennedy, "Automated Variable Electric-Field DFT Application for Evaluation of Optimally Oriented Electric Fields on Chemical Reactivity," J. Org. Chem. (2022): https://pmc.ncbi.nlm.nih.gov/articles/PMC9830642
[33] Åstrand, "Analytical Model for the Molecular Ionization Energy in an External Electric Field," J. Phys. Chem. Lett. 15(23), 6146 (2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11181318
[34] Wikibooks, "Molecular Simulation/Rotational Averaging": https://en.wikibooks.org/wiki/Molecular_Simulation/Rotational_Averaging
[35] "Numerical evaluation of orientation averages and its application to molecular physics," J. Chem. Phys. 161, 131501 (2024): https://pubs.aip.org/aip/jcp/article/161/13/131501/3315373/Numerical-evaluation-of-orientation-averages-and
[36] Shao, Zhang & Li, "Local electric field engineering via ferroelectric substrates," Nano Research (2026): https://doi.org/10.26599/NR.2026.94908460
[37] Vijay et al., "Dipole-field interactions determine the CO2 reduction activity of 2D Fe–N–C single-atom catalysts," ACS Catalysis (2020): https://pubs.acs.org/doi/10.1021/acscatal.9b05198
[38] Lv, Sun, Yang, Gan, Yu & Tan, "Research on Electric Field—Induced Catalysis Using Single—Molecule Electrical Measurement," Molecules 28(13), 4968 (2023): https://www.mdpi.com/1420-3049/28/13/4968
[39] Huang et al., "Electric-field-induced selective catalysis of single-molecule reaction," Science Advances 5, eaaw3072 (2019) (highlight via Fermitech/QuantumATK): https://www.fermitech.com.cn/quantumatk/pub-sciadv-2019-1
[40] Huang et al., "Electric-field-induced selective catalysis of single-molecule reaction," Science Advances 5, eaaw3072 (2019): https://www.science.org/doi/10.1126/sciadv.aaw3072
[41] "Electrostatic catalysis of a click reaction in a microfluidic cell," Nature Communications (2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC10817948
[42] 廖俊超, "电子结构视角下的定向外部电场对Diels–Alder反应调控机理," 科技导报: https://castjournals.cast.org.cn/joweb/kjdb/CN/1212410689789006686
[43] Wright, Sangtarash, Mueller, Lin, Sadeghi & Baumberg, "Vibrational Stark Effects: Ionic Influence on Local Fields," J. Phys. Chem. Lett. 13, 4905–4911 (2022): https://www.np.phy.cam.ac.uk/wp-content/uploads/sites/50/2024/06/jpcl22_vseonmbn.pdf
[44] English, "Molecular Simulation of External Electric Fields on the Crystal State: A Perspective," Crystals 11(11), 1405 (2021): https://www.mdpi.com/2073-4352/11/11/1405
[45] Huang, Zhang, Li, Groß & Sakong, "Bridging Ab Initio Molecular Dynamics and a Semiclassical Grand Canonical Model for the Electric Double Layer at Pt(111)/water interface": https://www.uni-ulm.de/fileadmin/website_uni_ulm/nawi.inst.250/publications/AIMD_vs_DPFT_preprint.pdf
[46] Pan, Wang, Zhang et al., "Boosting the performance of single-atom catalysts via external electric field polarization," Nature Communications 13, 3063 (2022): https://www.nature.com/articles/s41467-022-30766-x
[47] Ma, Wang, Xu, Xie & Lin, "Electric field modulated CO2 electroreduction on Pt single atom doped X2CO2 MXenes: A DFT study," Applied Surface Science 747, 167711 (2026): https://www.sciencedirect.com/science/article/abs/pii/S016943322601915
[48] Song et al., "Single-atom dissolution at the MN4/MXene interface and electric field-driven adsorption mechanisms," Applied Surface Science 695, 162886 (2025): https://doi.org/10.1016/j.apsusc.2025.162886
[49] Abdel Aal, Masoud & Soliman, "Tailoring hydrogen evolution reactions under external electric fields on single-atom catalysts of transition metal anchored C24N24 nanocages," Surfaces and Interfaces 73, 107475 (2025): https://doi.org/10.1016/j.surfin.2025.107475
[50] Lu, Meng, Pang, Xu, Ma, Talib & Yang, "Tuning the activation of O2 on Pt single-atom catalyst using external-electric field: A first-principles study," Physica B 638, 413934 (2022): https://doi.org/10.1016/j.physb.2022.413934
[51] Chen, Urushihara, Chan & Nørskov, "Electric Field Effects in Electrochemical CO2 Reduction," ACS Catalysis 6(10), 7133–7139 (2016): https://pubs.acs.org/doi/10.1021/acscatal.6b02299
[52] Yun, Lee, Bae & Kim, "Application of electric fields in the selective conversion of small alkane on IrO2(110) surface: DFT and microkinetic simulation study," Journal of Catalysis 450, 116226 (2025): https://doi.org/10.1016/j.jcat.2025.116226
[53] Wu, Li, Liu, Ma & Liu, "Relevance of the electronic structure of the substrate to O2 molecule adsorption on Fe-N-C single-atom catalysts under electrochemical potential," Phys. Rev. Materials 9, 055801 (2025): https://doi.org/10.1103/PhysRevMaterials.9.055801
[54] "外电场下C₃F₆O分子的光谱及其激发特性," 计算物理 42(4), 490–499 (2025): http://jswl.xml-journal.net/cn/article/pdf/preview/10.19596/j.cnki.1001-246x.8963.pdf
[55] 安跃华等, "外电场作用下ZnO分子的结构特性研究," 物理学报 62(7), 073103 (2013): https://wulixb.iphy.ac.cn/pdf-content/10.7498/aps.62.073103.pdf
[56] "外加电场下2–氯苯酚分子和4–氯苯酚分子的光谱与解离特性比较," 计算物理 43(3) (2026): http://jswl.xml-journal.net/cn/article/pdf/preview/10.19596/j.cnki.1001-246x.9104.pdf
[57] 汪灝, "利用定向電場增強二維材料邊緣的電化學活性," 国立台湾大学硕士论文 (2024): https://www.airitilibrary.com/Article/Detail/U0001-0157240725012017
[58] Duan, Ma, Ding et al., "Boosting the performance of single-atom catalysts via oriented external electric fields," Nature Communications 13, 3063 (2022): https://escholarship.org/content/qt8n95m1g9/qt8n95m1g9.pdf?v=lg
[59] Hao, Leven & Head-Gordon, "Can electric fields drive chemistry for an aqueous microdroplet?," Nature Communications 13, 280 (2022): https://www.nature.com/articles/s41467-021-27941-x
