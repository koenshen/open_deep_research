# AI算法提升电子学读出时幅修正方法：全面调研报告

## 1. 引言

高能物理探测器、核电子学及高速数据采集系统中的时幅修正（time-walk correction）是影响时间分辨精度的关键问题。传统时幅修正方法在信号幅度动态范围大、噪声环境复杂、计数率高等场景下存在固有局限性。近年来，深度学习与机器学习方法在电子学读出时间修正领域展现出显著潜力，已在多个探测器系统中实现超越传统方法的性能提升。本报告基于对2021-2026年最新研究的系统调研，从传统方法局限性、AI算法应用现状、性能对比、技术可行性及未来趋势五个维度进行全面分析。

---

## 2. 传统时幅修正方法及其局限性

### 2.1 前沿甄别法（Leading Edge Discrimination, LED）

**原理**：前沿甄别法是最简单的定时提取方法，通过比较器在信号超过固定阈值时记录时间。由于固定阈值，信号幅度越大，阈值越早被跨越，产生"时间游走"（time walk）误差。信号幅度必须在逐事件基础上记录，以便进行离线时间游走校正[1]。

**典型时间分辨率**：
- PET探测器（LYSO+SiPM，2.5×2.5×20 mm³晶体）：未校正时CTR为389.0±12.0 ps，LED自校正后提升至367.3±0.5 ps
- 双端读出TOF-PET：CTR从260.7±1.0 ps提升至229.4±1.0 ps（通过时间游走和时间偏移联合校正）[2]

**局限性**：
- **幅度依赖性时间游走**：这是根本性限制，信号幅度越大会导致越早触发
- **低阈值噪声敏感**：为提高时间分辨率而降低阈值会增加噪声敏感度
- **有限动态范围**：幅度变化范围大时，校正效果有限
- **需要离线校正**：增加计算开销
- **上升时间依赖性**：上升时间变化也会引起时间游走

### 2.2 过零甄别法（Zero-Crossing Discrimination）

**原理**：将单极性信号转换为双极性信号（通常通过微分或CR-RC成形），在信号过零点进行定时。过零点与信号幅度无关，理论上可实现幅度无关定时。

**典型时间分辨率**：
- 模拟过零法（BC501液体闪烁体n/γ甄别）：FOM值1.19-1.65
- 数字过零法（FPGA二阶导数）：脉冲发生器测试28 ps，LaBr₃(Ce)探测器<500 ps[3]

**局限性**：
- **需要双极性成形**：增加额外模拟电路复杂度
- **过零点噪声敏感**：低幅度信号在过零点附近的斜率很小，噪声影响大
- **硅探测器电阻率波动**：电荷收集时间依赖于撞击点，限制了粒子甄别能力
- **有限能量阈值**：低能量下甄别能力下降
- **采样率限制**：数字实现在低采样率下性能不如模拟方法

### 2.3 恒比甄别法（Constant Fraction Discrimination, CFD）

**原理**：CFD通过将输入信号分成延迟和衰减两路，输入比较器，在信号恒定比例（通常~20%）处触发。对于相同上升时间的信号，CFD的触发时间与幅度无关，可有效消除时间游走[4]。

**典型时间分辨率**：
- 商业NIM模块CFD：100:1动态范围内时间游走约100 ps
- Twin_Peaks_CFD1（紧凑型模拟CFD）：10:1幅度变化下标准偏差60 ps
- 数字CFD（1 GS/s，Xilinx Virtex-6）：脉冲发生器测试28 ps，LaBr₃(Ce)探测器<500 ps
- SAMPIC波形数字化器+CFD：合成信号4 ps，硅探测器信号40 ps

**局限性**：
- **大动态范围下时间游走：** 当输入信号动态范围过大时，CFD仍会表现出显著的残余时间游走[5]
- **上升时间依赖性：** 假设所有信号上升时间相同，对上升时间变化的信号不完全消除时间游走
- **模拟电路复杂度高：** 需要高速运放（>100 MHz），成本高、功耗大
- **延迟线要求：** 模拟CFD需要精密延迟线，增加体积和成本
- **脉冲对分辨率（死时间）：** 不同CFD型号的脉冲对分辨率为5-30 ns，限制最大计数率
- **数字CFD的有限改进：** 理论分析表明，数字CFD相比模拟方法的时间分辨率改进因子仅为sqrt(3/2)=1.23，且当采样点相关时改进更小[6]

### 2.4 波形采样+内插拟合方法

**原理**：将整个信号或前沿部分数字化，然后应用数字算法提取到达时间。包括数字恒比甄别（dCFD）、数字前沿+内插、互相关法、脉冲形状拟合、机器学习/神经网络方法等。

**典型时间分辨率**：
- SAMPIC：合成信号4 ps，硅探测器信号40 ps，TINL校正后降至3.5 ps RMS
- SAMPIC + 多时间过阈值(mToT)：PICOSEC气体探测器48.8 ps
- 神经网络（LHCb ECAL Upgrade II）：无堆积下~18.3 ps，有堆积下~66.2 ps[7]
- 多电荷过阈值(mCoT)：PICOSEC探测器44.9 ps（整体），23.2 ps（嵌入事件）

**局限性**：
- **高数据吞吐量：** 波形数字化产生大量数据，需要高速数据传输和存储能力
- **采样率和ADC分辨率权衡：** 时间分辨率主要由有效位数决定，而非采样率
- **内插偏差：** 线性内插在快边沿时产生分布偏差，需要"金发姑娘"边沿速率
- **功耗高：** 高速ADC和FPGA功耗显著
- **INL/DNL校正要求：** 积分非线性校正对时间分辨率至关重要
- **死时间/计数率限制：** 采样存储单元数量有限，限制计数率

---

## 3. AI/ML算法在电子学读出时间修正中的应用现状

### 3.1 深度神经网络用于CMS-PPS金刚石定时探测器

**研究来源**：M. Kocot等，2023年，arXiv:2312.05883

**问题**：CMS-TOTEM精密质子谱仪（PPS）的金刚石定时探测器存在"时间游走效应"——粒子沉积电荷的统计涨落导致到达时间测量误差。标准CFD算法虽简单有效，但未充分利用时间序列中的所有电压样本。

**方法论**：
- 使用DESY-II同步加速器测试束数据（2020年），MCP-PMT作为参考（精度~10 ps），金刚石传感器（50-100 ps）
- SAMPIC读出芯片每156.25 ps采样一次，产生64个样本的10 ns窗口波形
- 预处理后数据集约500,000个波形条目

**三种网络架构**：
- MLP（2737个参数）
- CNN（36865个参数）
- UNet（456965个参数）

**关键结果**：
- UNet模型达到最佳时间精度（60.71 ps），优于CNN（62.83 ps）和MLP（63.90 ps）
- 相比CFD基线，改进幅度为8%至23%，取决于读出通道
- 基础实验中，精度从71.6 ps提升至58.4 ps（改进17%）
- LHC条件下（24样本时间序列），精度从73.3 ps提升至62.1 ps（改进15%）
- 推理仅需~10 ms CPU时间，适合在线处理

### 3.2 LSTM用于MRPC飞行时间探测器

**研究来源**：EIC提案，2022年

**背景**：为电子-离子对撞机（EIC）开发的高精度密封MRPC（sMRPC），具有32个104 μm气隙，宇宙射线测试中本征分辨率16 ps。

**方法论**：使用长短期记忆（LSTM）网络进行时间分析，相比传统Time-Over-Threshold（ToT）方法。

**关键结果**：
- LSTM改进的时间分辨率：~16.8 ps
- 传统ToT方法：23 ps
- 改进幅度：约27%
- 高计数率下（15 kHz/cm²），分辨率降至~20 ps

### 3.3 MLP用于PICOSEC气体探测器定时

**研究来源**：I. Manthos等，HEP 2021

**背景**：PICOSEC探测器针对HL-LHC堆积减轻，目标20-30 ps时间分辨率。

**测试方法对比**：
- CFD（参考方法）：50.5 ps（整体），24.4 ps（嵌入事件）
- 前沿-多时间过阈值（mToT，7个阈值）：48.8 ps
- 前沿-多电荷过阈值（mCoT）：44.9 ps（整体），23.2 ps（嵌入事件）——**优于CFD**
- 神经网络（MLP）：输入ToT在10/50/100 mV阈值，46.0 ps（整体），25.2 ps（嵌入事件）

**结论**：当前端电子学提供电荷信息时，mCoT优于CFD，神经网络结果与解析方法相当。

### 3.4 CNN用于BGO飞行时间PET

**研究来源**：*EJNMMI Physics*，2025年

**背景**：比较不同定时估计方法在BGO闪烁体TOF-PET中的应用。

**关键结果（2×2×3 mm³晶体）**：
- LED：157±3 ps CTR
- 双阈值时间游走校正（TWC）：129±2 ps（改进18%）
- CNN：115±2 ps（改进26%）

**关键结果（2×2×20 mm³晶体）**：
- LED：280±8 ps
- TWC：241±7 ps（改进14%）
- CNN：239±7 ps（改进15%）

**结论**：对于长BGO晶体，简单双阈值TWC方法捕获了大部分关键信息，CNN的额外收益有限。CNN在抑制时间分布尾部方面表现更好。

### 3.5 梯度提升决策树用于PET定时校准

**研究来源**：S. Naunheim等，2024年，DOI: 10.1088/1361-6560/ad63ec

**背景**：系统性评估基于机器学习的PET定时校准方法。

**方法论**：使用梯度提升决策树（GBDT）结合残差物理，LSO闪烁体+TOFPET2 ASIC读出，移动²²Na放射源。

**关键结果**：
- CTR从304±5 ps（传统解析校准）提升至216±1 ps（ML校准）
- 校准时间从43小时减少至约3分钟（加速因子1000），不牺牲质量
- 首次在模拟读出技术上验证，证明技术独立性

### 3.6 显式TOF校正：基于残差物理的机器学习方法

**研究来源**：S. Naunheim等，2025年，arXiv:2502.07630

**背景**：引入"显式校正"方法，直接预测定时残差的校正值，而非之前的"隐式校正"方法。

**关键结果**：
- 显式校正方法消除了对训练步宽（源位置间距）的强依赖性
- 即使训练数据稀疏采样时，仍保持线性
- 定时性能从371±6 ps提升至281±5 ps（430-590 keV能量窗口）
- 模型可指数级缩小，适合高吞吐量PET扫描仪

### 3.7 深度神经网络用于双读出量能器波形分解

**研究来源**：arXiv:2604.26090v1

**背景**：为下一代Higgs工厂（如FCC-ee）的同质双读出量能器分离闪烁光和契伦科夫光成分。

**关键结果**：
- 紧凑全连接网络（16→24→8→3神经元）直接从数字化波形回归信号参数
- 312.5 MHz采样率下的ML模型持续优于同采样率的模板拟合
- 10.4 MHz采样率下，ML实现与3.125 GHz模板拟合竞争的性能
- 定时分辨率：312.5 MHz下ML为0.10-0.14 ns，模板拟合为0.39-0.66 ns
- 模型压缩后FPGA实现≤25 ns延迟，30k-330k LUTs

### 3.8 其他重要应用

- **PETNet（脉冲神经网络）**：用于PET数据中光子符合对的检测，临床数据集F1=95.2%，经典算法F1=93.3%，推理速度~20倍于经典方法
- **MLP用于PET TOT位置校正**：使用HLS4ML实现，FPGA上PSNR=22.90 dB，SSIM=0.9161，达到与QDC类似的性能
- **ML辅助TDC自校准**：FPGA上实现，ML模型校正残余非线性，时间精度达13.6 ps，比传统编码器FPGA TDC提升10.5倍
- **MAC/UMAC自编码器架构**：用于闪烁体晶体量能器定时重建，UMAC模型将平均时间差降至-0.003 ns，可分辨亚纳秒精度

---

## 4. AI算法与传统方法的关键性能对比

### 4.1 时间分辨率改进

| 方法 | 应用场景 | 传统方法 | AI/ML方法 | 改进幅度 |
|------|---------|---------|-----------|---------|
| DNN (UNet) | CMS-PPS金刚石探测器 | 71.6 ps (CFD) | 58.4 ps | 17% |
| LSTM | MRPC TOF探测器 | 23 ps (ToT) | 16.8 ps | ~27% |
| MLP | PICOSEC气体探测器 | 50.5 ps (CFD) | 46.0 ps | ~9% |
| CNN | BGO TOF-PET (3mm) | 157 ps (LED) | 115 ps | 26% |
| 双阈值TWC | BGO TOF-PET (3mm) | 157 ps (LED) | 129 ps | 18% |
| GBDT | PET定时校准 | 304 ps (解析) | 216 ps | 29% |
| ML辅助TDC | FPGA TDC | ~143 ps (传统) | 13.6 ps | 10.5倍 |
| SNN (PETNet) | PET符合事件 | 93.3% F1 | 95.2% F1 | 2% 提升 |

### 4.2 处理速度

**FPGA推理延迟典型值**：
- **小MLP（三层隐藏层）**：75-150 ns（200 MHz时钟）
- **CNN（触发处理）**：~5 μs
- **RNN/LSTM**：1.7-38.8 μs（取决于模型大小）
- **GNN**：1.4 μs
- **超小ML（<1K LUTs）**：可低至数十纳秒
- **hls4ml框架**：支持10 ns到微秒级的推理延迟，取决于模型复杂度[8]

**关键优势**：
- FPGA推理延迟远低于传统软件处理（毫秒级）
- 典型L1触发要求数百纳秒延迟，hls4ml在200 MHz下可达75-150 ns
- 数字CFD在1 GS/s采样率下需要每次采样进行插值，延迟约为FPGA时钟周期的数十倍
- 神经网络推理可通过流水线实现恒定延迟，与输入速率无关

### 4.3 资源消耗

**FPGA资源消耗典型值**：

| 模型 | 应用 | LUTs | DSPs | BRAM | FFs | 延迟 |
|------|------|------|------|------|-----|------|
| MLP (64,32,32) | 喷注分类 | 36k (5%) | 954 (17%) | - | 53k (3%) | 75-150 ns |
| CNN (SVHN) | 基准测试 | 可调 | 可减少97-99% | - | - | ~5 μs |
| 2D CNN (DUNE) | 中微子实验 | 20% | 38% | 4% | 10% | 23.4 μs |
| MLP (PID) | EIC | - | 3% | - | - | 65 ns |
| RNN/LSTM | 径迹拟合 | - | 19% (剪枝后) | - | - | 1 μs |
| 超小ML | 簇计数 | ~1K | 0 | - | - | <100 ns |

**资源消耗优化策略**：
- **hls4ml框架**：支持延迟、资源、分布式算术三种实现策略
- **剪枝+量化感知训练**：可减少99%的DSP消耗，仅损失6%精度
- **SparseLUT框架**：通过聚合PolyLUT子神经元，LUT减少2.0×-13.9×，延迟改进1.2×-1.6×
- **DA4ML工具链**：实现无HLS的直接RTL转换，资源消耗降低20倍

**功耗对比**：
- FPGA加速器（Xilinx Alveo U50）：75W
- GPU（NVIDIA V100）：300W
- FPGA功耗优势显著，适合嵌入式读出系统

### 4.4 关键优势与劣势总结

**AI算法优势**：
- **更高时间分辨率**：利用完整波形信息，实现8-27%的改进
- **自适应能力**：可学习噪声、信号形状变化等复杂模式
- **端到端优化**：直接从数字化波形映射到时间输出
- **多任务能力**：可同时估计时间、能量、位置等多参数
- **可硬件实现**：通过hls4ml等工具链，可部署在低功耗FPGA上

**AI算法劣势**：
- **训练数据需求**：需要大量高质量标注数据（通常数十万到数百万样本）
- **泛化挑战**：跨通道、跨探测器泛化能力有限，通常需要针对特定通道训练
- **辐射耐受性**：需要专用辐射加固FPGA或eFPGA方案
- **校准漂移**：环境变化可能导致性能退化，需要定期重校准
- **可解释性不足**：难以理解网络决策逻辑
- **资源消耗**：复杂模型可能超出FPGA资源限制

---

## 5. 技术可行性、潜在挑战与未来发展趋势

### 5.1 技术可行性

**硬件平台**：
- **hls4ml框架**已成熟，可自动将Keras/PyTorch模型转换为FPGA固件，支持Xilinx、Intel、Microchip PolarFire等平台
- **辐射加固FPGA**：Microchip PolarFire系列已通过hls4ml验证，可部署于LHC等高辐射环境
- **嵌入式FPGA（eFPGA）**：SLAC已完成28nm节点eFPGA原型验证，结合FPGA灵活性和ASIC效率
- **超小模型**：<10K LUTs的模型可实现片上实时处理，无需外部存储

**性能指标**：
- 推理延迟可低至10 ns（小MLP）至微秒级（CNN/Transformer）
- 流水线架构可实现40 MHz触发率要求
- 资源消耗可通过剪枝、量化、SparseLUT等方法大幅降低

**训练数据**：
- 测试束数据（如CMS-PPS使用DESY-II数据）
- 模拟数据（Geant4等）可补充训练，但需注意模拟-真实差异
- 自监督/半监督方法可减少标注需求
- 自校准方法（如PET LED自校正）无需外部参考

### 5.2 潜在挑战

**挑战1：训练数据获取与标注**
- 精确参考时间（如MCP-PMT）在实际探测器设置中不可用
- 模拟数据可能引入偏差，需要专门的去偏技术
- 跨通道/跨探测器泛化需要大量多样化数据

**挑战2：辐射环境下的可靠性**
- 辐射可能导致FPGA配置位翻转，影响推理结果
- 需要TMR（三模冗余）等加固技术
- 辐射加固FPGA（如PolarFire）性能低于商用FPGA

**挑战3：校准漂移与长期稳定性**
- 温度、电压变化可能导致模型性能退化
- 需要定期重校准或在线适应机制
- 自校准方法可减少人工干预

**挑战4：资源限制与模型复杂度**
- 大型模型可能超出FPGA片上资源
- 量化/剪枝可能导致精度损失
- 需要硬件-算法协同设计优化

**挑战5：实时性与吞吐量要求**
- LHC L1触发要求<1 μs延迟
- 高计数率（>1 MHz）需要流水线架构
- 复杂模型（如Transformer）可能难以满足实时要求

### 5.3 未来发展趋势

**趋势1：片上学习与运行时重配置**
- hls4ml正在扩展支持运行时重配置，可适应环境变化
- 在线微调可基于小批量数据调整模型
- 梯度下降在FPGA上的实现正在探索中

**趋势2：脉冲神经网络（SNN）**
- PETNet已展示SNN在PET符合检测中的应用，推理速度~20倍于经典方法
- 低功耗神经形态硬件可实现高效的片上处理
- 多目标损失函数结合脉冲计数和定时信息

**趋势3：Transformer架构**
- hls4ml现已支持Transformer（多头注意力），推理延迟<2 μs
- 注意力机制可捕获波形中的长程依赖关系
- 适用于复杂脉冲形状分析

**趋势4：混合模拟-神经方法**
- 前端模拟电路（如NINO芯片）提供电荷信息，配合数字神经网络
- 简单阈值方法（如mCoT）可捕获大部分关键信息，结合AI优化
- 前端模拟处理+后端数字神经网络的混合架构

**趋势5：超小模型与硬件-算法协同设计**
- 目标：<10K LUTs的片上模型，无需DSP
- DA4ML工具链支持无HLS的直接RTL转换
- 代理式EDA（AI辅助设计）加速硬件设计流程

**趋势6：Kolmogorov-Arnold网络（KAN）**
- HEP ML Living Review已纳入KAN作为新兴架构
- KAN在可解释性和参数效率方面有潜力
- 可作为时间游走建模的替代方案

**趋势7：基础模型与迁移学习**
- 预训练基础模型可适应不同探测器类型
- 迁移学习减少新应用的数据需求
- 模型可作为通用波形特征提取器

---

## 6. 结论与建议

### 6.1 关键结论

1. **AI算法可显著提升时幅修正性能**：在多个探测器系统中，AI/ML方法实现8-27%的时间分辨率改进，最高达10.5倍的性能提升

2. **FPGA实现可行性已充分验证**：hls4ml等工具链支持从10 ns到微秒级推理延迟，资源消耗可控，已在实际LHC实验中使用

3. **简单方法（如mCoT、双阈值TWC）在多数场景下足够**：对于长BGO晶体等应用，简单阈值方法与CNN性能相当，AI方法在短晶体和尾部抑制方面更有优势

4. **训练数据与泛化是主要挑战**：需要数十万到数百万样本，且跨通道泛化能力有限，但自校准方法和模拟数据可缓解

5. **未来趋势指向片上学习、SNN、Transformer和混合架构**

### 6.2 研究建议

- **优先尝试简单方法**：对于时间分辨率要求<100 ps的应用，双阈值TWC或mCoT可能足够，且实现简单
- **高精度需求选择DNN**：对于<50 ps目标，UNet等深度架构可提供8-17%的改进
- **利用hls4ml进行FPGA部署**：成熟的工具链加速从训练到部署的流程
- **关注辐射加固方案**：PolarFire FPGA或eFPGA是LHC等辐射环境的可行选择
- **结合模拟与真实数据**：使用Geant4等产生训练数据，配合少量真实数据微调

---

## 7. 参考文献

[1] A Time-Walk Correction Method for PET Detectors Based on Leading Edge Discriminators: https://pmc.ncbi.nlm.nih.gov/articles/PMC5739333

[2] A Time-Walk and Timing-Shift Correction Method for Dual-Ended Readout TOF-PET Detectors: https://pmc.ncbi.nlm.nih.gov/articles/PMC12493018

[3] FPGA Implementation of a Digital Constant Fraction for Fast Timing: https://proceedings.jacow.org/ICALEPCS2013/papers/tuppc083.pdf

[4] Constant Fraction Discriminator - Wikipedia: https://en.wikipedia.org/wiki/Constant_fraction_discriminator

[5] Off-line correction for excessive constant-fraction-discriminator walk in neutron time-of-flight experiments: https://www.sciencedirect.com/science/article/abs/pii/S016890020303345X

[6] What is the theoretical time precision achievable using a dCFD algorithm? (arXiv:1606.05541): https://arxiv.org/pdf/1606.05541

[7] Enabling low-latency machine learning on radiation-hard FPGAs with hls4ml: https://iopscience.iop.org/article/10.1088/2632-2153/ae8218

[8] hls4ml: A Flexible, Open-Source Platform for Deep Learning Acceleration on Reconfigurable Hardware (arXiv:2512.01463): https://arxiv.org/html/2512.01463v1

[9] Using deep neural networks to improve the precision of fast-sampled particle timing detectors (arXiv:2312.05883): https://arxiv.org/pdf/2312.05883

[10] Signal processing techniques for precise timing with novel gaseous detectors: https://indico.cern.ch/event/1047066/contributions/4399272/attachments/2265836/3847074/Manthos_timing_hep21.pdf

[11] Improving timing resolution of BGO for TOF-PET: a comparative analysis with and without deep learning: https://pmc.ncbi.nlm.nih.gov/articles/PMC11739447

[12] Holistic evaluation of a machine learning-based timing calibration method for PET detectors: https://iopscience.iop.org/article/10.1088/1361-6560/ad63ec

[13] Rethinking timing residuals: advancing PET detectors with explicit TOF corrections (arXiv:2502.07630): https://arxiv.org/abs/2502.07630

[14] Machine Learning Enables Real-Time Waveform Decomposition for Dual-Readout Calorimetry (arXiv:2604.26090): https://arxiv.org/abs/2604.26090v1

[15] PETNet – Coincident Particle Event Detection using Spiking Neural Networks: https://publikationen.bibliothek.kit.edu/1000171804/153702751

[16] Deep Learning Based Position and Non-Linearity Correction for High-Performance PET Detector Using a Time-Over-Threshold Readout Method: https://jnm.snmjournals.org/content/65/supplement_2/241567

[17] A novel FPGA-based time-to-digital converter featuring machine learning-aided self-calibration: https://www.sciencedirect.com/science/article/pii/S2667305326000190

[18] Fast Neural Network Inference on FPGAs for Triggering on Long-Lived Particles at Colliders (arXiv:2307.05152): https://arxiv.org/html/2307.05152v2

[19] Machine Learning, But Make It Hardware: Embedded FPGAs for Particle Detectors: https://a3d3.ai/machine-learning-but-make-it-hardware-embedded-fpgas-for-particle-detectors

[20] Co-Design for Ultra-Small ML on FPGAs with an Open-Source Toolchain: https://indico.global/event/14708/contributions/146623/attachments/70968/137819/OS_AI_221.pdf

[21] HEP ML Living Review: https://iml-wg.github.io/HEPML-LivingReview

[22] hls4ml GitHub Repository: https://github.com/fastmachinelearning/hls4ml

[23] Development of High Precision and Eco-friendly MRPC TOF Detector for EIC: https://www.jlab.org/sites/default/files/eic_rd_prgm/files/2022_Proposals/MRPC_for_EIC_TOF_Final_EICGENRandD2022_16.pdf

[24] Dual threshold input receiver FPGA-only signal digitization method for time-of-flight positron emission tomography: https://link.springer.com/article/10.1007/s13534-024-00380-5

[25] Design of Time-to-Digital Converters for Time-Over-Threshold Measurement in Picosecond Timing Detectors: https://ieeexplore.ieee.org/document/9394205

[26] Online AI triggering and data compression method and apparatus for particle detector readout electronics (Patent CN122119664A): https://patents.google.com/patent/CN122119664A

[27] Enhancing LUT-based Deep Neural Networks Inference through Architecture and Connectivity Optimization (SparseLUT, arXiv:2601.09773): https://arxiv.org/html/2601.09773v1

[28] Fast convolutional neural networks on FPGAs with hls4ml: https://cds.cern.ch/record/2751704/files/fulltext.pdf

[29] Ultra-low latency recurrent neural network inference on FPGAs: https://people.ece.uw.edu/hauck/publications/RNN_J.pdf

[30] Real-Time Inference With 2D Convolutional Neural Networks on FPGAs for High-Rate Particle Imaging Detectors: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2022.855184/full
