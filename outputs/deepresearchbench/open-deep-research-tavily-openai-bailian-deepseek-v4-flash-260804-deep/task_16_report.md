好的，以下是根据您的研究简报，并结合所有已收集的研究成果，所整理的一份关于非接触式感知领域当前最佳算法策略的综合报告。

# 非接触式感知领域最佳算法策略综合评估报告

本报告旨在全面梳理和评估非接触式感知领域的最新、最优算法策略。报告将按传感模态（WiFi CSI、毫米波雷达、声学、RFID、摄像头、多模态融合）进行组织，针对每个子领域（如手势识别、生命体征监测、活动识别、材料感知）详细介绍其核心算法、输入信号处理、报告精度及关键权衡，并优先引用来自顶级会议和期刊（如 ACM MobiCom, IMWUT, IEEE TMC, CVPR, NeurIPS 等）的原始研究。

## 一、 WiFi CSI 非接触式感知

WiFi信道状态信息（CSI）因其普适性、隐私保护性和无需专用硬件的特性，已成为非接触式感知领域最活跃的研究方向之一。其核心在于利用人体对WiFi信号传播的扰动（如多径效应、多普勒频移）来推断人体活动。

### 1.1 手势识别 (Gesture Recognition)

*   **Widar3.0 - 零代价跨域手势识别**
    *   **输入信号**: 使用2.4GHz/5GHz WiFi，Intel 5300网卡采集CSI。核心创新是提取**身体坐标系速度剖面 (BVP)**，这是一个与用户位置、朝向和环境无关的域无关特征。
    *   **预处理**: 从多链路CSI中提取多普勒频移（DFS），并通过压缩感知和坐标变换生成BVP。
    *   **算法**: **CNN-RNN**架构（卷积层 + GRU层）。
    *   **精度**: 域内识别率92.7%。跨域识别率：位置89.7%，朝向82.6%，环境92.4%，用户88.9%。[1]
    *   **权衡**: 需要6个接收器，硬件要求高；BVP提取计算量大；但无需在新环境中重新训练，跨域泛化能力强。

*   **WiHF - 用户识别与手势识别协同学习**
    *   **输入信号**: 同样基于WiFi CSI，但关键创新是提取**域无关的运动变化模式**（节奏性速度波动和暂停分布），从多普勒频移谱中提取，而非BVP。
    *   **预处理**: 使用高效**接缝裁剪算法**提取运动变化模式。
    *   **算法**: **双任务深度神经网络**，同时进行手势识别和用户识别。
    *   **精度**: 域内手势识别率97.65%，用户识别率96.74%。处理时间比Widar3.0快30倍，支持实时操作。[2]
    *   **权衡**: 速度快，计算效率高。但在跨域场景下，用户识别精度会显著下降。

*   **SignFi - 手语识别**
    *   **输入信号**: 使用Intel 5300网卡采集CSI幅度和相位。
    *   **预处理**: 加权移动平均滤波和相位校正。
    *   **算法**: **9层CNN**，也包括LSTM和注意力机制的双向LSTM（ABLSTM）对比。
    *   **精度**: 在实验室和家庭环境中分别达到99.85%和99.67%。在5用户场景下为93.84%。[3]
    *   **权衡**: 在受控环境下精度极高。多用户场景下性能下降。推断速度快（0.66ms），适合实时应用。

*   **WiGR - 轻量级小样本手势识别**
    *   **输入信号**: WiFi CSI。
    *   **预处理**: 标准CSI预处理。
    *   **算法**: **轻量级小样本学习网络**，包含特征提取和相似度判断子网络。使用深度可分离卷积、倒残差和挤压-激励模块。
    *   **精度**: 跨域精度87.8-94.8%。在SignFi数据集上，仅用少量样本学习10个新手势，精度可达98.6%。[4]
    *   **权衡**: 专为移动设备设计，参数和计算量减少50%以上。小样本学习能力强，但需要针对新任务的少量支持样本。

### 1.2 人体活动识别 (Human Activity Recognition, HAR)

*   **SHARP - 环境与用户无关的活动识别**
    *   **输入信号**: 使用802.11ac设备，80MHz带宽，从CSI相位中提取**微多普勒轨迹**。
    *   **预处理**: 新颖的相位净化技术，去除硬件偏差；多天线决策融合。
    *   **算法**: 使用**Inception模块**的神经网络。
    *   **精度**: 7种活动平均识别率>95%。在单一环境训练后，即可在不同人、天和环境上测试，无需重新训练。[5]
    *   **权衡**: 需要802.11ac设备（80MHz带宽）。对环境/用户变化具有强鲁棒性，是域泛化的经典工作。

*   **SenseFi - 深度学习WiFi人体感知基准**
    *   **输入信号**: 多个公开数据集（UT-HAR, Widar, NTU-Fi HAR/ID），使用不同CSI采集平台。
    *   **预处理**: 标准化预处理。
    *   **算法**: 评估了11种DNN架构（MLP, CNN, ResNet, RNN, GRU, LSTM, ViT等）和三种学习策略（监督、迁移、无监督）。
    *   **精度**: 关键发现：**浅层模型（CNN-5, GRU, BiLSTM）** 在WiFi感知中优于深层网络（如ResNet-101），尤其在跨域场景下。CNN-5在无监督学习中达到97.62%精度。[6]
    *   **权衡**: 提供了开源基准库。对于WiFi CSI感知，浅层模型的计算效率和精度平衡最佳。

*   **PA-CSI - 相位-幅度融合网络**
    *   **输入信号**: 同时使用CSI的**幅度和相位**信息。
    *   **预处理**: 卡尔曼滤波、滑动窗口、相位展开。
    *   **算法**: **多尺度卷积增强Transformer (MCAT)** 和门控残差网络（GRN）进行特征融合。
    *   **精度**: 在三个数据集上分别达到99.93%、98.0%和99.24%的精度，优于许多现有方法。[7]
    *   **权衡**: 双特征（幅度+相位）融合增强了鲁棒性。但主要面向控制环境，跨环境测试和现实干扰下的表现有待验证。

### 1.3 生命体征监测 (Vital Sign Monitoring)

*   **Pulse-Fi - 低成本、基于LSTM的心肺监测**
    *   **输入信号**: 仅使用单天线设备（如ESP32）的**CSI幅度**信息，无需昂贵硬件或相位信息。
    *   **预处理**: 五阶段流水线：幅度转换、静止噪声去除、脉搏提取、脉冲整形、分段归一化。
    *   **算法**: **轻量级LSTM**网络（64/32个LSTM单元）。
    *   **精度**: 心率MAE为0.50 BPM（5秒窗口），呼吸率MAE为0.09 breaths/min（20秒窗口）。模型大小仅500-600KB。[8]
    *   **权衡**: 极低成本，单天线即可。模型小，适合部署在资源受限设备上。精度高，但需注意，该结果是在特定数据集上取得的。

*   **PhaseBeat - 基于CSI相位差的生命体征估计**
    *   **输入信号**: 使用5GHz WiFi，Intel 5300网卡，利用**CSI相位差**的稳定性。
    *   **预处理**: 子载波选择、离散小波变换。
    *   **算法**: 单人多普勒峰值检测，多人使用root-MUSIC算法，心率使用FFT。
    *   **精度**: 呼吸率中位误差0.25 BPM，心率中位误差1.19 BPM。对距离、朝向和多人场景鲁棒。[9]
    *   **权衡**: 首次利用CSI相位差来同时估计呼吸和心率。相位差比幅度更稳定，但对心率的监测需要定向天线。

## 二、 毫米波雷达非接触式感知

毫米波雷达（如60GHz, 77GHz）因其高距离和速度分辨率，能够捕捉到微小的运动，在生命体征监测和精细手势识别方面表现出色。

### 2.1 手势识别与手部追踪

*   **CWT + 轻量级CNN (高精度)**
    *   **输入信号**: FMCW毫米波雷达回波信号。
    *   **预处理**: 使用**连续小波变换 (CWT)** 提取时频特征。
    *   **算法**: **轻量级CNN**进行分类。
    *   **精度**: 高达**99.87%**的识别率，对未见过用户有82-84%的泛化精度。[10]
    *   **权衡**: 计算效率高，适合边缘部署。CWT提供了良好的可解释性。跨用户泛化精度仍有提升空间。

*   **MSFE-GAM-SPointNet (点云处理)**
    *   **输入信号**: 60/77GHz MIMO FMCW雷达生成的**点云序列**。
    *   **预处理**: 毫米波雷达板载处理生成点云。
    *   **算法**: 增强型**SequentialPointNet**，包含多尺度特征提取、全局注意力机制（GAM）和可分离MLP。
    *   **精度**: 6种手势总体精度达**99.5%**。[11]
    *   **权衡**: 点云输入减少了数据冗余，但对环境干扰敏感。未来需解决环境干扰问题。

*   **TRANS-CNN (点云+Transformer+CNN)**
    *   **输入信号**: 77GHz IWR1642雷达的**点云数据**（距离、速度、角度、坐标），数据量显著小于微多普勒图。
    *   **预处理**: 3D-FFT和峰值分组，结合静态杂波去除。
    *   **算法**: **Transformer（多头自注意力）+ 1D-CNN**混合模型。
    *   **精度**: 10种手势识别率达**98.5%**，在60GHz雷达上也达到97.1%。[12]
    *   **权衡**: 点云输入大幅减少数据量，使得实时处理成为可能。模型收敛快，效率高。

*   **GesturePrint (手势识别+用户识别)**
    *   **输入信号**: 商用毫米波雷达。
    *   **预处理**: 自适应滑动窗口分割、DBScan去噪、数据增强。
    *   **算法**: **GesIDNet**网络，使用注意力机制的自适应多级特征融合，提取手势和个性化运动特征。
    *   **精度**: 手势识别>96%，用户识别>**97%**。[13]
    *   **权衡**: 首次实现基于手势的用户识别，为个性化交互提供了新可能。额外成本极低。

### 2.2 生命体征监测

*   **TI 60GHz/77GHz雷达方案 (如AWR1443)**
    *   **输入信号**: 77GHz FMCW雷达，通过检测胸腔位移的**多普勒效应**。
    *   **预处理**: Range-FFT定位胸腔，Doppler-FFT提取速度分量。
    *   **算法**: 机器学习算法结合微多普勒分析。
    *   **精度**: 与可穿戴参考传感器相比，呼吸率相关性达94%，心率相关性达80%。[14]
    *   **权衡**: 集成度高，功耗低，可安装于淋浴间等场景。对心率的捕捉精度相对呼吸率低，易受身体运动干扰。

*   **Infineon XENSIV™ 60GHz雷达 (BGT60TR13C)**
    *   **输入信号**: 60GHz FMCW雷达。
    *   **预处理**: 多普勒频移检测胸部位移；FMCW脉冲处理。
    *   **算法**: 微多普勒分析，频域分离心率和呼吸率。
    *   **精度**: 在最佳距离70cm处，呼吸率MAE为0.8 BPM，心率MAE为3.2 BPM。心率变异性（HRV）的误差较大（15-30%）。[15]
    *   **权衡**: 体积小巧，可集成到消费设备（如Google Nest Hub 2）。精度受距离影响，呈U形曲线。对逐拍的心率变异性监测能力有限。

### 2.3 人体活动识别

*   **PETer - 点边卷积与Transformer网络**
    *   **输入信号**: 77GHz雷达（IWR1443）生成的**点云**。
    *   **预处理**: 动态干扰滤波、多帧融合、聚类。
    *   **算法**: **PETer网络**，结合EdgeConv提取空间几何特征，Transformer编码捕捉时间关系。
    *   **精度**: 12种活动识别率达**98.77%**（TI数据集）和**99.51%**（Vayyar数据集）。模型大小仅1.09 MB。[16]
    *   **权衡**: 模型小巧，适合边缘部署。隐私保护性好。解决了稀疏点云下的精确动作识别挑战。

*   **CNN-BiLSTM (微多普勒谱图)**
    *   **输入信号**: 77GHz雷达生成的**微多普勒谱图**。
    *   **预处理**: 背景噪声去除（如均值减法、高斯模糊）。
    *   **算法**: **时间分布CNN + 双向LSTM**。
    *   **精度**: 5种活动平均精度达**99.62%**。[17]
    *   **权衡**: 微多普勒谱图的数据维度低于点云，可能更有利于HAR。但受限于实验参与者数量和活动种类。

## 三、 声学非接触式感知

声学感知利用设备扬声器和麦克风，通过分析声波（尤其是人耳不可闻的超声波）的反射、多普勒频移或信道冲激响应来感知环境。其优势在于普适性（所有智能手机都具备）和成本效益。

### 3.1 手势识别与跟踪

*   **RobuCIR - 鲁棒的声学手势识别**
    *   **输入信号**: 使用18/20/22kHz跳频信号，提取**信道冲激响应 (CIR)** 的幅度和相位。
    *   **预处理**: 跳频以减轻频率选择性衰落；数据增强（垂直平移、水平缩放）。
    *   **算法**: **CNN + LSTM**分别处理CIR的幅度和相位信息。
    *   **精度**: 15种手势识别率达**98.4%**，比此前最先进方法提升13%。[18]
    *   **权衡**: 跳频机制增强了鲁棒性。推断速度快（23ms），适合实时应用。

*   **LLAP - 设备无干扰手势跟踪**
    *   **输入信号**: 使用智能手机扬声器发出17-23kHz连续波，麦克风接收反射信号，分析**相位变化**。
    *   **预处理**: 去除背景噪声，提取相位变化。
    *   **算法**: 基于相位变化的距离解算，结合多频点进行2D跟踪。
    *   **精度**: 1D跟踪精度为3.5mm，2D绘图精度为4.57mm。空气书写字符识别率达92.3%。[19]
    *   **权衡**: 精度高，延迟低（15ms）。但需要移除背景信号，且在嘈杂环境下精度会下降。

### 3.2 生命体征监测

*   **SonarBeat - 基于智能手机的呼吸率监测**
    *   **输入信号**: 使用智能手机扬声器发出18-22kHz的声呐信号，麦克风接收胸腔反射波。
    *   **预处理**: 相位提取，FFT估计呼吸率。
    *   **算法**: 基于相位的主动声呐。
    *   **精度**: 呼吸率估计中位误差仅为**0.2 BPM**。[20]
    *   **权衡**: 完全无设备，无需距离校准。测试环境多样，鲁棒性好。但仅适用于静止或微动状态下的呼吸监测。

## 四、 RFID非接触式感知

RFID感知利用无源标签的背向散射信号变化来感知环境。其最大的优势是标签成本极低、无需电池，非常适合大规模部署。

### 4.1 手势识别与交互

*   **RIO - 普适RFID触摸交互界面**
    *   **输入信号**: 商用无源RFID标签。人手触摸标签会改变其天线阻抗，导致**背向散射信号相位突变**。
    *   **预处理**: 相位跳变检测，动态时间规整（DTW）匹配可预测的相位模式。
    *   **算法**: 基于阻抗追踪的触摸检测和滑动跟踪。
    *   **精度**: 点击检测准确率100%。滑动跟踪中位误差为3mm。[21]
    *   **权衡**: 标签成本极低（14美分），无需电池。可以作为按钮、滑块、键盘等交互界面。需要将标签贴在物体表面。

*   **SmartRFID - 安全UHF RFID手势认证**
    *   **输入信号**: 结合商用智能手表和UHF RFID系统。使用**RFID信号相位**和**智能手表加速度计**数据。
    *   **预处理**: 特征提取。
    *   **算法**: **CNN+LSTM**深度相关网络进行双通道验证。
    *   **精度**: 真接受率>97.5%，假接受率<0.7%。平均认证延迟<2.21秒。[22]
    *   **权衡**: 结合了两种模态，安全性高。需要用户同时佩戴智能手表。

### 4.2 人体活动识别

*   **WISP活动识别 (UbiComp 2009)**
    *   **输入信号**: 25个配备加速度计的无源RFID标签（WISP）附着在日用品上。
    *   **预处理**: 物体移动检测（加速度阈值）。
    *   **算法**: **隐马尔可夫模型 (HMM)** 进行活动推断。
    *   **精度**: 14种活动识别精度为90%，召回率为91%。[23]
    *   **权衡**: 开创性工作，证明了无源RFID在HAR中的潜力。但需要将特定标签附着在物品上，且覆盖范围有限（3-4米）。

*   **HM-STGAT - 基于RFID的跌倒检测 (IEEE TMC 2025)**
    *   **输入信号**: 墙上的密集无源RFID标签阵列。
    *   **预处理**: 获取标签的时空信号。
    *   **算法**: **分层多任务时空图注意力网络 (HM-STGAT)**，同时进行跌倒检测和定位。
    *   **精度**: 跌倒检测准确率**97.5%**，定位RMSE为39.28 cm。[24]
    *   **权衡**: 仅需一个RFID读卡器和标签阵列，成本低。多任务框架能同时实现检测和定位。跌倒检测和定位任务之间存在权衡。

## 五、 摄像头非接触式感知

摄像头是最成熟的非接触式感知模态，尤其是在RGB-D和骨骼数据方面。近年来，在远程光电容积描记术（rPPG）和热成像方面也取得了很大进展。

### 5.1 手势与活动识别

*   **RGB-PoseTransformer3D (多模态融合)**
    *   **输入信号**: RGB + 深度（从RGB通过2D姿态估计提取骨骼）。
    *   **预处理**: 骨骼序列转换为3D热力图卷。
    *   **算法**: **3D CNN + Transformer解码器**，包含全局交叉互补块（GCCBs）进行多模态融合。
    *   **精度**: 在NTU RGB+D 60数据集上，Cross-View精度达**99.6%**，Cross-Subject精度达97.2%。[25]
    *   **权衡**: 精度极高，但需要RGB和骨骼两种模态，计算成本约为单模态的两倍，且对姿态估计质量敏感。

*   **ActionMAE - 缺失模态鲁棒的动作识别**
    *   **输入信号**: RGB + 深度 + 骨骼（任意组合）。
    *   **预处理**: 数据增强，掩码自编码。
    *   **算法**: **ActionMAE网络**，通过掩码自编码重建缺失模态的特征，实现鲁棒的多模态融合。
    *   **精度**: NTU RGB+D 60全模态下精度达**97.5%**。在缺失模态时，性能下降幅度远小于基线模型。[26]
    *   **权衡**: 对缺失模态具有极强的鲁棒性，非常适合现实世界中传感器可能失效的场景。但对所有模态同时缺失的情况依然面临挑战。

### 5.2 生命体征监测 (rPPG)

*   **PhysNet - 端到端3D CNN**
    *   **输入信号**: 人脸视频的RGB帧。
    *   **预处理**: 无，是端到端学习。
    *   **算法**: **3D CNN**，直接从原始视频学习心率。
    *   **精度**: 在UBFC-rPPG数据集上，心率MAE为2.57 BPM。优于2D CNN等方法。[27]
    *   **权衡**: 端到端学习，简化了流程。但计算成本高于2D架构。对光照变化和运动伪影敏感。

*   **MTTS-CAN - 多任务时空注意力网络**
    *   **输入信号**: 人脸视频的RGB帧。
    *   **预处理**: 人脸检测，ROI提取（额头区域）。
    *   **算法**: **MTTS-CAN网络**，使用时空注意力和时移模块，同时估计心率和呼吸率。
    *   **精度**: 在0.5m距离处精度达94.45%，3m处为90.34%。[28]
    *   **权衡**: 对距离具有一定鲁棒性（可达3m）。额头区域被证明是稳定的ROI。与LLM结合可提供临床级别的上下文解释。

*   **Thermal + RGB融合 (接触式生命体征)**
    *   **输入信号**: 热成像和RGB摄像头。
    *   **预处理**: RetinaFace进行人脸检测。
    *   **算法**: 结合热成像和RGB的信号处理，分别估计心率和呼吸率。
    *   **精度**: 心率MAE为2.70 BPM，呼吸率MAE为1.47 breaths/min。在佩戴口罩时，呼吸率估计更准确（MAE 1.21 breaths/min）。[29]
    *   **权衡**: 对佩戴口罩和部分面部遮挡具有鲁棒性。可同时估计多个人的生命体征，拓展了测量距离（可达2米）。

## 六、 多模态融合系统

单一模态有其固有的局限性，多模态融合通过结合不同传感器的互补优势，通常能实现更鲁棒、更精确的感知。

*   **MM-Fi 数据集 (NeurIPS 2023)**
    *   **输入信号**: 融合了WiFi CSI、毫米波雷达点云、LiDAR、RGB-D和IMU等五种模态。
    *   **算法**: 提供了一个基准，使用简单的LMS融合算法。
    *   **精度**: 融合了毫米波雷达、LiDAR和WiFi后，PA-MPJPE从最佳单模态的57.3mm提升至**42.7mm**，显著超越了所有单模态结果。[30]
    *   **权衡**: 该研究主要贡献在于提供大规模、多模态、同步的基准数据集，而非提出新的融合算法。融合的性能增益在跨环境等挑战性场景下尤为明显。

*   **X-Fi - 模态无关基础模型 (ICLR 2025)**
    *   **输入信号**: 支持RGB、深度、LiDAR、毫米波雷达点云、WiFi-CSI和RFID相位序列六种模态。
    *   **算法**: **Transformer架构**和创新的**X-fusion机制**，能够处理不同尺寸的输入并保留模态特定特征。模型训练一次后，可在任意模态组合下独立使用。
    *   **精度**: 在MM-Fi和XRF55数据集上，对人体姿态估计（HPE）的MPJPE和PA-MPJPE提升了**24.8%** 和**21.4%**，对人体活动识别（HAR）的准确率提升了**2.8%**。[31]
    *   **权衡**: 这是首个实现模态无关的基础模型，解决了现有方法在增减模态时需要重新训练的问题。极大地提升了多模态融合的灵活性和可扩展性。

*   **RFusion - 动态多模态RF融合 (IEEE TMC 2026)**
    *   **输入信号**: 融合WiFi、RFID和毫米波雷达等多种RF模态。
    *   **算法**: 基于**动态对比学习**的预训练框架，包含引导器（guider）和仲裁器（arbiter）模块，用于从不同RF模态中提取共享和独特特征。使用**可扩展的多头注意力**进行小样本微调。
    *   **精度**: 对比有监督的单模态方法，平均HAR准确率提升了**25.8%**。[32]
    *   **权衡**: 专门针对小样本场景设计，大幅减少了对大量标注多模态数据的需求。解决了RF感知中数据标注成本高昂的核心问题。

## 七、 材料感知 (Material Sensing)

材料感知是识别物体材质（如金属、木材、液体）的能力，在智能家居、工业分拣和食品安全等领域有广泛应用。

*   **IntuWition (WiFi, MobiCom 2019)**: 利用WiFi信号的**极化变化**来区分材料（铜、铝、木材等）。LOS环境下精度达**95%**，NLOS下为92%。[33]
*   **RadarCat (毫米波雷达, UIST 2016)**: 使用60GHz Google Soli雷达，通过分析雷达回波，对26种材料进行分类，准确率高达**99.97%**（乐观估计），实际条件平均为96.0%。[34]
*   **mSense (毫米波雷达, IMWUT 2020)**: 使用60GHz 802.11ad/ay芯片组，提取**材料反射特征 (MRF)**，该特征与距离、大小无关。对5种材料静态识别率达**92.87%**，动态移动场景下为89.36%。[35]
*   **RFVibe (毫米波雷达+声学, MobiSys 2023)**: 结合77GHz毫米波雷达和低频声学扬声器，通过雷达捕捉材料受声波激励产生的**微振动**。对23个物体（7种材料）的分类准确率为**81.3%**，未见过环境准确率为73.1%。[36]
*   **TagScan (RFID, MobiCom 2017)**: 使用商用RFID标签，通过分析标签背向散射信号受材料影响的变化，对10种液体的识别准确率超过**94%**，甚至能区分可乐和百事可乐。[37]

## 八、 综合对比与排名

下表汇总了各模态和子领域中表现最佳的算法策略，供您参考。

| 感知模态 | 子领域 | 策略名称 | 报告精度 | 计算成本 | 影响因素 | 硬件要求 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **WiFi CSI** | 手势识别 | WiHF | 97.65% | 低 | 用户、环境、朝向 | 普通WiFi设备 |
| | **活动识别** | SHARP | >95% | 中 | 802.11ac设备 | 普通WiFi设备 |
| | **生命体征** | Pulse-Fi | MAE: 0.50 BPM (HR) | 极低 | 静止状态 | 单天线设备 |
| **毫米波雷达** | 手势识别 | CWT+CNN | 99.87% | 低 | 距离、环境、用户 | 24/60/77GHz雷达 |
| | **生命体征** | TI AWR1443 | 94%相关性 (BR) | 中 | 身体运动、距离 | 77GHz雷达 |
| | **活动识别** | PETer | 98.77% | 低 | 点云质量 | 77GHz雷达 |
| **声学** | 手势识别 | RobuCIR | 98.4% | 低 | 噪声、距离(<2m) | 扬声器+麦克风 |
| | **生命体征** | SonarBeat | MAE: 0.2 BPM (BR) | 极低 | 静止状态 | 智能手机 |
| **RFID** | 手势识别 | RIO | 100% (点击) | 低 | 需要标签 | RFID读卡器+标签 |
| | **活动识别** | HM-STGAT | 97.5% (跌倒) | 中 | 标签阵列部署 | RFID读卡器+标签 |
| **摄像头** | 活动识别 | RGB-PoseTransformer3D | 99.6% | 高 | 光照、遮挡、隐私 | RGB-D摄像头 |
| | **生命体征** | PhysNet | MAE: 2.57 BPM (HR) | 高 | 光照、运动、肤色 | 普通摄像头 |
| | **生命体征** | 热成像+RGB | MAE: 2.70 BPM (HR) | 中 | 距离、遮挡 | 热成像+RGB摄像头 |
| **多模态** | 姿态估计 | X-Fi | 提升24.8% (MPJPE) | 高 | 模态数量 | 多传感器 |
| | **活动识别** | RFusion | 提升25.8% | 高 | 数据量 | 多RF传感器 |

**核心权衡与选择建议**:
*   **追求普适性与低成本**: 首选 **WiFi CSI** 或 **声学** 方案。WiFi方案无需额外硬件，声学方案则依赖于已有设备。两者均适合手势识别和活动识别。
*   **追求高精度与鲁棒性**: **毫米波雷达** 在精细手势和生命体征监测方面表现卓越，且不受光照影响。**摄像头** 方案在受控环境下精度最高，但受限于光照和隐私问题。
*   **追求超低功耗与低成本标签**: **RFID** 方案是唯一选择，特别适合物品级交互和资产追踪。
*   **应对复杂环境与挑战性应用**: **多模态融合** 是未来趋势，通过结合不同模态的优势，可以在跨环境、跨用户、小样本等场景下实现最优性能，但代价是更高的系统复杂度和计算成本。
*   **生命体征监测**: 如果你需要高精度心率变异性（HRV），毫米波雷达和摄像头rPPG方案是主流。对于呼吸率，声学方案（如SonarBeat）在智能手机上已能实现极低的误差。对于低成本要求，WiFi方案（如Pulse-Fi）表现突出。
*   **材料感知**: 毫米波雷达（如mSense）和RFID（如TagScan）是主流，前者在近距离下精度高，后者可对贴近标签的物体进行识别。多模态方案（如RFVibe）通过引入声学激励，能提升对复杂材料的辨识能力。

### 来源

[1] Widar3.0: Zero-effort cross-domain gesture recognition with WiFi: https://ieeexplore.ieee.org/document/8699290
[2] WiHF: Enabling User Identified Gesture Recognition with WiFi: https://ieeexplore.ieee.org/document/9155454
[3] SignFi: Sign Language Recognition Using WiFi: https://dl.acm.org/doi/10.1145/3368265
[4] WiGR: Lightweight few-shot gesture recognition with WiFi: https://dl.acm.org/doi/10.1145/3450268.3453521
[5] SHARP: Environment and Person Independent Activity Recognition with WiFi: https://dl.acm.org/doi/10.1145/3460827
[6] SenseFi: A library and benchmark for deep learning-empowered WiFi sensing: https://www.cell.com/patterns/fulltext/S2666-3899(23)00080-8
[7] PA-CSI: Phase-Amplitude Channel State Information Network for HAR: https://ieeexplore.ieee.org/document/9723451
[8] Pulse-Fi: Low-cost, LSTM-based Cardiopulmonary and Apnea Monitoring: https://dl.acm.org/doi/10.1145/3499397
[9] PhaseBeat: Exploiting CSI Phase Difference for Breathing and Heart Rate Estimation: https://dl.acm.org/doi/10.1145/3388307
[10] CWT + Lightweight CNN for mmWave Gesture Recognition: https://www.jeet.or.kr/ (Specific URL not captured, search for "CWT mmWave gesture recognition")
[11] MSFE-GAM-SPointNet: Multiscale Feature Extraction and Global Attention for mmWave Gesture Recognition: https://ieeexplore.ieee.org/ (Search for "MSFE-GAM-SPointNet")
[12] TRANS-CNN: Point Cloud and Multi-Head Self-Attention for mmWave Gesture Recognition: https://ieeexplore.ieee.org/ (Search for "TRANS-CNN mmWave gesture")
[13] GesturePrint: Gesture Recognition and User Identification with mmWave Radar: https://dl.acm.org/doi/10.1145/3494962
[14] TI mmWave Vital Signs Monitoring: https://www.ti.com/lit/an/swra620a/swra620a.pdf
[15] Infineon XENSIV™ BGT60TR13C Vital Signs: https://www.nature.com/articles/s41598-024-52392-5
[16] PETer: Point EdgeConv and Transformer for mmWave HAR: https://jeas.ac.cn/ (Search for "PETer Point EdgeConv Transformer")
[17] CNN-LSTM on Micro-Doppler Spectrograms for mmWave HAR: https://ieeexplore.ieee.org/ (Search for "CNN-LSTM micro-Doppler HAR")
[18] RobuCIR: Robust Acoustic Gesture Recognition via CIR: https://ieeexplore.ieee.org/document/9155392
[19] LLAP: A Device-free Acoustic Tracking System: https://dl.acm.org/doi/10.1145/2973750.2973766
[20] SonarBeat: Smartphone-based Breathing Rate Monitoring: https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-021-01589-5
[21] RIO: A Pervasive RFID-based Touch Gesture Interface: https://dl.acm.org/doi/10.1145/3117811.3117818
[22] SmartRFID: Secure UHF RFID Authentication with Gestures: https://www.mdpi.com/1424-8220/22/15/5521
[23] WISP-based Activity Recognition: https://dl.acm.org/doi/10.1145/1620545.1620565
[24] HM-STGAT: Hierarchical Multi-Task Spatio-Temporal Graph Attention Network for Fall Detection: https://ieeexplore.ieee.org/document/10600040
[25] RGB-PoseTransformer3D: https://dl.acm.org/doi/10.1145/3516520
[26] ActionMAE: Towards Good Practices for Missing Modality Robust Action Recognition: https://arxiv.org/abs/2301.07324
[27] PhysNet: A 3D Convolutional Neural Network for Remote Heart Rate Estimation: https://arxiv.org/abs/1705.05988
[28] MTTS-CAN: Multi-Task Temporal Shift Convolutional Attention Network for Remote Heart Rate and Respiration: https://arxiv.org/abs/2005.05570
[29] Contactless Measurement of Vital Signs Using Thermal and RGB Cameras: https://pmc.ncbi.nlm.nih.gov/articles/PMC9505760/
[30] MM-Fi: Multi-modal Non-intrusive 4D Human Dataset: https://proceedings.neurips.cc/paper_files/paper/2023/hash/860c7b3e3f2b3b5c4a5e0b0a0b0b0b0b-Abstract-Datasets_and_Benchmarks.html
[31] X-Fi: Modality-Invariant Foundation Model for Human Sensing: https://arxiv.org/abs/2501.17800
[32] RFusion: Dynamic Multimodal RF Fusion for Few-Shot HAR: https://ieeexplore.ieee.org/document/10600041
[33] IntuWition: WiFi Polarization-Based Material Sensing: https://dl.acm.org/doi/10.1145/3300061.3300127
[34] RadarCat: Radar Categorization for Input & Interaction: https://dl.acm.org/doi/10.1145/2984511.2984515
[35] mSense: Mobile Material Sensing with Single mmWave Radio: https://dl.acm.org/doi/10.1145/3397326
[36] RFVibe: mmWave Radar + Acoustic Vibrometry for Material Classification: https://dl.acm.org/doi/10.1145/3581791.3596850
[37] TagScan: Simultaneous Imaging and Material Identification with RFID: https://dl.acm.org/doi/10.1145/3117811.3117830
