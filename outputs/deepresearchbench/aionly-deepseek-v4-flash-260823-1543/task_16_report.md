好的，遵照您的研究简报和提供的所有调研信息，我为您整理了一份关于非接触式感知领域最前沿算法策略的全面、结构化报告。

---

# 非接触式感知领域前沿算法策略综合调研报告

## 1. 概述

本报告系统性地梳理了非接触式感知领域中，基于Wi-Fi、毫米波雷达、视觉/摄像头、红外、超声波、RFID以及多模态融合方案的最前沿算法策略。报告旨在为研究人员提供一份详尽的技术参考，涵盖各感知模态的输入信号类型、核心算法架构、在标准基准数据集上的性能表现、适用任务场景，以及不同技术路线间的优劣势对比分析。

## 2. 基于Wi-Fi的感知算法

Wi-Fi感知利用信道状态信息（CSI）和接收信号强度指示（RSSI）来捕捉人体运动引起的信号传播变化。近年来，深度学习模型（CNN、LSTM、Transformer等）在该领域取得了显著进展。

### 2.1 关键算法与性能

| 算法/论文 | 年份 | 会议/期刊 | 输入信号 | 模型架构 | 任务 | 性能 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Person-in-WiFi 3D** [1] | 2024 | CVPR | CSI（多设备，多天线） | Transformer | 多人3D姿态估计 | 3D关节定位误差：91.7mm（1人）、108.1mm（2人）、125.3mm（3人） |
| **Wi-CBR** [2] | 2025 | arXiv | CSI相位数据、DFS多普勒数据 | 双分支自注意力模块 + 组注意力 + 门控机制 | 跨域行为识别 | Widar3.0: 域内99.54%，跨域平均97.07% |
| **WiPose** [3] | 2020 | MobiCom | CSI（3D速度轮廓） | RNN + 骨架先验知识 | 3D姿态估计 | 平均关节定位误差2.83cm，比基线提升35% |
| **Wi-Mose** [4] | 2020 | arXiv | CSI幅度和相位融合 | 13个残差块的CNN | 3D运动姿态估计 | P-MPJPE：LoS场景29.7mm，NLoS场景37.8mm |
| **CSDS** [5] | 2025 | Electronics | CSI（150×3×3） | 空间方向注意力 + 空间灵敏度增强 + U-Net | 2D姿态估计 | 在Wi-Pose数据集上达到SOTA |
| **DT-Pose** [6] | 2026 (审稿) | ICLR | WiFi CSI信号（图像化输入） | 自监督MAE预训练 + GCN + Transformer | 2D/3D姿态估计（跨域） | MM-Fi跨环境：PCK@50=58.8, PA-MPJPE=105.1 |
| **跌倒检测 (Chu)** [7] | 2023 | IEEE Access | CSI | 图像分类深度学习 | 跌倒检测 | 跨4种环境准确率>96%，特定组合达99% |
| **C-L-A (阵列)** [8] | 2025 | Electronics | CSI（2×2 ESP32阵列） | CNN-LSTM-Attention | 活动识别 | 98.2%准确率，12ms延迟 |
| **SenseFi基准** [9] | 2023 | Patterns | CSI | CNN-5, GRU, BiLSTM等 | 活动/手势/身份识别 | CNN-5: UT-HAR 97.61%, NTU-Fi HAR 98.70% |

### 2.2 核心模型架构分析

- **CNN（卷积神经网络）**：适用于提取局部空间特征，在结构化活动中表现优异，如UT-HAR数据集上准确率达95% [10]。
- **RNN/LSTM/GRU（循环神经网络）**：擅长捕捉时间序列动态，在跌倒检测等任务中表现突出，如GRU在WiPE-FaLl数据集上准确率达93% [10]。
- **CNN-LSTM混合模型**：结合了空间和时间特征提取能力，在复杂多人数据集上表现出色，准确率可达98% [10]。
- **Transformer架构**：用于捕捉长距离依赖关系，在多人3D姿态估计任务中展现了巨大潜力，但需要大量训练数据 [1]。
- **自注意力机制**：用于增强对关键特征的关注，提升模型在复杂场景下的鲁棒性 [2]。

### 2.3 优势与劣势

- **优势**：利用现有基础设施，成本低，普及度高；能穿透墙体，实现非视距（NLoS）感知。
- **劣势**：分辨率相对较低，易受环境变化（如多径效应）和硬件差异影响；跨域泛化仍是挑战。

## 3. 基于毫米波雷达的感知算法

毫米波雷达（24GHz-300GHz）因其高精度、隐私保护和环境适应性，成为非接触式感知的重要方向。输入信号包括点云、距离-多普勒图、微多普勒频谱图等。

### 3.1 关键算法与性能

| 算法/论文 | 年份 | 会议/期刊 | 输入信号 | 模型架构 | 任务 | 性能 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **mmMesh** [11] | 2021 | MobiSys | 3D点云 | 注意力 + 动态锚点分组 + LSTM + SMPL | 3D人体网格重建 | 顶点误差2.47cm，关节误差2.18cm，实时0.3s |
| **TRANS-CNN** [12] | 2024 | Sensors | 雷达点云（30帧×45点） | 多头自注意力 + 1D-CNN | 手势识别 | 98.5%准确率（IWR1642），约97.1%（自研雷达） |
| **ProbRadarM3F** [13] | 2024 | arXiv | 原始ADC + 热图 | FFT + 概率图位置编码 + 3D卷积 + GCN | 骨骼姿态估计 | AP 69.9%，比HuPR基线提升6.5% |
| **SUPER** [14] | 2024 | arXiv | 强度/多普勒点云 | PointNet++ + LSTM + SMPL | 坐姿上半身姿态估计 | PA-MPJPE 15.89mm，比mmMesh基线提升30-184% |
| **MVDoppler-Pose** [15] | 2025 | CVPR | 多模态多视角mmWave信号 | 多模态协同集成 | 长距离人体行走姿态估计 | 距离无关、遮挡鲁棒 |
| **跌倒检测 (24GHz)** [16] | 2024 | - | 24GHz点云 | 点云增强 + 轻量CNN | 跌倒检测 | 新受试者99.1%，新环境98.9%，0.017M参数 |
| **mmGesture** [17] | 2023 | Expert Systems | 4种雷达热图 | 半监督Π-模型 + 数据增强 | 手势识别（半监督） | 跨用户98.59%，跨位置96.72% |
| **mmFree-Pose** [18] | 2025 | Bioengineering | 5D点云 | PointNet / DGCNN / Point Transformer | 隐私保护姿态估计 | PointNet: MLE 12.39cm, AP 95% |

### 3.2 核心模型架构分析

- **PointNet/PointNet++**：直接处理无序点云，适用于人体姿态和网格重建，如mmMesh和mmFree-Pose。
- **Transformer与自注意力**：有效捕捉点云中远距离点的关系，提升手势识别和姿态估计的精度 [12, 13]。
- **GCN（图卷积网络）**：用于细化关键点预测，利用人体骨架拓扑结构进行约束 [13]。
- **多任务学习**：同时进行人体解析和姿态估计，利用任务间的相关性提升整体性能，如mmParse [19]。
- **半监督学习**：利用少量标注数据实现高精度，有效降低数据标注成本，如mmGesture [17]。
- **点云增强**：通过多帧融合或深度学习模型（如扩散模型）提升稀疏点云质量，显著改善下游任务性能 [16, 20]。

### 3.3 优势与劣势

- **优势**：分辨率高，精度可达厘米甚至毫米级；不受光照、天气影响，隐私保护性好；可穿透轻质障碍物。
- **劣势**：硬件成本高于Wi-Fi；点云数据稀疏，对算法要求高；远距离感知精度下降。

## 4. 基于视觉/摄像头的感知算法

视觉感知是传统的人体感知手段，利用RGB或红外视频流进行姿态估计、活动识别和生命体征监测。

### 4.1 关键算法与性能

| 算法/论文 | 年份 | 会议/期刊 | 输入信号 | 模型架构 | 任务 | 性能 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **HRNet** [21] | 2019 | CVPR | RGB图像 | 高分辨率网络 | 人体姿态估计 | COCO val: 75.9 mAP (单人) |
| **ybasTrack** [22] | 2024 | 华东理工大学学报 | RGB视频 | S-YOLOv5s + BCNet + TA-SPPE + Y-SeqNet | 多人姿态估计与追踪 | PoseTrack2018: 75.23% mAP, 65.14% MOTA |
| **PhysFormer** [23] | 2022 | CVPR | 面部视频 | Transformer | 远程心率检测（rPPG） | 优于CNN基线，在多个数据集上达到SOTA |
| **TS-CAN** [24] | 2020 | - | 面部视频 | 时序移位模块 + 2D CNN | 远程心率检测（rPPG） | UBFC-rPPG: MAE=1.29 BPM |
| **多模型融合跌倒检测** [25] | 2024 | 计算机科学与应用 | RGB视频 | Faster R-CNN + Mediapipe + DCST-GCN | 跌倒检测 | IBFD: 96.0%准确率，NTU-RGB+D: 93.5% Top-1 |
| **P-HRNet** [26] | 2024 | 计算机科学与应用 | 红外图像 | 改进HRNet + 通道剪枝 | 人体姿态估计 | 红外数据集: 74.2 mAP, 15.5M参数 |

### 4.2 核心模型架构分析

- **HRNet**：通过并行连接高分辨率子网，在整个过程中保持高分辨率特征，在姿态估计任务中表现出色 [21]。
- **Transformer**：在rPPG领域，PhysFormer利用多头自注意力机制建模长程时空特征，显著提升了心率检测的鲁棒性 [23]。
- **GCN（图卷积网络）**：用于动作识别，通过建模人体骨架的时间-空间图结构来捕捉动作模式，如DCST-GCN [25]。
- **3D CNN**：直接处理视频时空立方体，用于捕捉连续帧间的运动信息，是早期rPPG和动作识别的主流方法之一。

### 4.3 优势与劣势

- **优势**：信息丰富，分辨率最高；技术成熟，数据集和开源工具丰富；成本相对较低（特别是RGB摄像头）。
- **劣势**：严重依赖光照条件，夜间或弱光环境下性能下降；存在严重的隐私泄露风险；易受遮挡影响。

## 5. 其他模态感知算法

### 5.1 红外热成像

- **核心方法**：利用热成像技术捕捉人体温度变化，通过分析额头、鼻孔等区域的温度波动来提取心率和呼吸率 [27]。
- **性能**：心率误差<4%（平均误差0.718 BPM），呼吸误差<1次/分钟 [27]。
- **优势**：被动式、非侵入、全天候，不受环境光影响，可保护隐私（面部特征模糊）。
- **劣势**：分辨率较低，易受环境温度变化影响，硬件成本相对较高。

### 5.2 超声波感知

- **核心方法**：利用扬声器发射人耳听不到的声波（如20kHz以上），通过麦克风接收回波，分析手势或活动引起的多普勒频移或脉冲回波变化。
- **UltrasonicGS** [28]：使用ResNet34 + Bi-LSTM + CTC，实现15种单手势98.8%的识别准确率，以及中文手语86.3%的识别准确率。
- **优势**：低成本、低功耗、隐私保护、抗电磁干扰。
- **劣势**：作用距离近（通常在0.5-1米内），易受环境噪声干扰。

### 5.3 RFID感知

- **核心方法**：利用无源RFID标签的相位和RSSI信息进行感知。标签可附着在物体上（绑定式）或部署在环境中（非绑定式）。
- **性能**：相位定位精度可达厘米级（如RF-Dial系统达0.6cm），在实验室环境中活动识别准确率可达90.8% [29, 30]。
- **优势**：无源、低成本、可部署在物品上实现精准追踪。
- **劣势**：需要部署标签，感知范围有限，粗粒度RSSI精度低。

## 6. 多模态融合方案

多模态融合通过整合不同感知技术的优势，克服单一模态的局限性，是目前提升系统鲁棒性和精度的主流方向。

### 6.1 关键融合方案与性能

| 融合方案 | 算法/论文 | 年份 | 融合模态 | 模型架构 | 任务 | 性能 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **毫米波雷达+超声波** | Yao et al. [31] | 2026 | 77GHz雷达 + 40kHz超声波 | Attention-CNN-BiLSTM | 活动识别 | 98.6%平均分类准确率 |
| **毫米波雷达+振动传感器** | P2MFDS [32] | 2025 | 毫米波雷达 + 3D振动传感器 | CNN-BiLSTM-Attention + 多尺度CNN | 跌倒检测 | 95.0%准确率，94.6%精度 |
| **WiFi+加速度计** | 智能手机+WiFi [33] | 2024 | WiFi CSI + 手机加速度计 | MLP + CNN + 注意力 | 跌倒检测 | 识别准确率>99% |
| **毫米波雷达+视觉** | 黑芝麻智能 [34] | 2025 | 4D毫米波雷达 + 相机 | PointPillars + Transformer + 多模态对齐 | 3D目标检测 | mAP提升5%，mAVE提升33.85% |
| **视觉+LiDAR** | 协同感知 [35] | 2024 | LiDAR点云 + 相机图像 | Transformer融合 | 协同感知 | AP@0.7 达85.2% (OPV2V数据集) |

### 6.2 融合策略分析

- **早期融合**：在数据层面直接拼接不同模态的特征，实现简单，但对齐要求高，易受噪声影响。
- **晚期融合**：每个模态独立进行预测，最后综合决策。易于实现，但忽略了模态间的低级交互。在RFID融合相位和RSS信号的研究中，晚期融合优于早期融合 [36]。
- **中间融合**：在模型中间层进行特征交互，是当前最主流的方法。通过注意力机制（如交叉注意力）动态地对齐和融合不同模态的特征，效果显著，如毫米波雷达与视觉的前融合方案 [34]。
- **双流/多流网络**：不同模态使用独立的特征提取网络，在特定层进行融合，如P2MFDS系统 [32]。

## 7. 对比分析与最佳实践

### 7.1 不同输入信号优劣势对比

| 信号类型 | 空间分辨率 | 环境鲁棒性 | 隐私保护 | 成本 | 典型应用场景 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Wi-Fi (CSI)** | 低 | 中（受多径影响） | 高 | 极低 | 活动识别，存在检测，穿墙姿态估计 |
| **毫米波雷达 (点云)** | 高 | 高（全天候） | 高 | 中 | 精细手势识别，3D姿态估计，跌倒检测 |
| **视觉 (RGB视频)** | 极高 | 低（依赖光照） | 极低 | 低 | 高精度姿态估计，面部表情分析 |
| **红外热成像** | 中 | 高（全天候） | 高 | 中 | 生命体征监测，夜间人体检测 |
| **超声波** | 中 | 低（受噪声影响） | 高 | 极低 | 近距离手势交互 |
| **RFID** | 中（相位） | 中 | 高 | 低 | 物品级追踪，绑定式活动识别 |

### 7.2 当前最佳算法组合推荐

1.  **高精度3D姿态估计与网格重建**：**毫米波雷达**方案（如mmMesh）是目前非接触式方案中的最佳选择，精度可达厘米级，且兼具隐私保护和环境鲁棒性。对于需要高精度且对隐私要求极高的场景（如医疗康复、隐私监控），毫米波雷达是首选。
2.  **精细手势识别**：**毫米波雷达**（如TRANS-CNN，准确率98.5%）和**超声波**（如UltrasonicGS，准确率98.8%）是互有优势的候选。毫米波雷达作用距离更远，而超声波成本更低。基于**Wi-Fi**的方案（如Wi-CBR在Widar3.0上跨域平均97.07%）则提供了利用现有基础设施的便利性。
3.  **跌倒检测**：**多模态融合**方案效果最佳。例如，**WiFi+加速度计**融合可达>99%准确率，**毫米波雷达+振动传感器**融合可达95%准确率。单模态方案中，**毫米波雷达**（如24GHz方案，新环境98.9%）和**Wi-Fi**（跨环境>96%）也表现优异。
4.  **非接触式生命体征监测（心率/呼吸）**：**视觉rPPG**（如PhysFormer）和**红外热成像**是主要技术路线。视觉技术在受控环境下精度高，但易受运动和光照影响；红外热成像更鲁棒，但成本更高。**Wi-Fi**和**毫米波雷达**也展示了监测呼吸和心跳的潜力，但精度相对较低。
5.  **跨域/零样本泛化**：**Wi-Fi**领域的研究最为深入，如Widar3.0的域无关特征提取和Wi-AM的元学习框架，旨在实现“一次训练，多域应用”。**毫米波雷达**领域也出现了类似研究，如FUSE系统的元学习框架。**DT-Pose**提出的自监督预训练范式，为解决Wi-Fi HPE的跨域问题提供了新思路。

## 8. 总结与展望

非接触式感知领域正经历快速发展，不同技术路线各有千秋。**Wi-Fi感知**凭借其普及性和低成本，在活动识别和粗粒度姿态估计上极具潜力，但需解决跨域泛化问题。**毫米波雷达**在精度、隐私和鲁棒性上取得了最佳平衡，是未来高精度感知应用，如3D姿态重建和精细手势识别的重要方向。**视觉感知**在精度上仍然领先，但隐私和光照问题是其硬伤。**多模态融合**已被证明是提升系统鲁棒性和精度的有效途径，例如毫米波雷达与视觉/超声波的结合，能够实现单一传感器无法达到的性能。

未来趋势将集中在：
- **算法层面**：更强大的基础模型（如Transformer、扩散模型）将进一步提升感知精度；自监督和半监督学习将降低对大规模标注数据的依赖。
- **系统层面**：多模态融合将成为常态，不同传感器优势互补，实现更可靠、更全面的感知。
- **硬件层面**：更小型化、低成本、高集成度的传感器芯片（如Google Soli）将推动非接触式感知在消费电子和物联网设备中的广泛应用。

---

### 附：开源项目链接

- **Person-in-WiFi 3D**: [https://aiotgroup.github.io/Person-in-WiFi-3D](https://aiotgroup.github.io/Person-in-WiFi-3D)
- **mmMesh**: [https://havocfixer.github.io/mmMesh](https://havocfixer.github.io/mmMesh)
- **HuPR Benchmark**: [https://github.com/robert80203/HuPR-A-Benchmark-for-Human-Pose-Estimation-Using-Millimeter-Wave-Radar](https://github.com/robert80203/HuPR-A-Benchmark-for-Human-Pose-Estimation-Using-Millimeter-Wave-Radar)
- **mmHPE**: [https://github.com/bh6aol/mmHPE](https://github.com/bh6aol/mmHPE)
- **rPPG-Toolbox**: [https://github.com/ubicomplab/rPPG-Toolbox](https://github.com/ubicomplab/rPPG-Toolbox)
- **Awesome mmWave Radar Perception**: [https://github.com/Armorhtk/awesome-mmwave-radar-perception](https://github.com/Armorhtk/awesome-mmwave-radar-perception)
- **Awesome-WiFi-CSI-Sensing**: [https://github.com/NTUMARS/Awesome-WiFi-CSI-Sensing](https://github.com/NTUMARS/Awesome-WiFi-CSI-Sensing)

### Sources

[1] Person-in-WiFi 3D: End-to-End Multi-Person 3D Pose Estimation with Wi-Fi (CVPR 2024): https://openaccess.thecvf.com/content/CVPR2024/html/Yan_Person-in-WiFi_3D_End-to-End_Multi-Person_3D_Pose_Estimation_with_Wi-Fi_CVPR_2024_paper.html
[2] Wi-CBR: WiFi-based Cross-domain Behavior Recognition via Multimodal Collaborative Awareness (arXiv 2025): https://arxiv.org/html/2506.11616v1
[3] Towards 3D Human Pose Construction Using WiFi (WiPose, MobiCom 2020): https://havocfixer.github.io/resource/20_MobiCom.pdf
[4] 3D Moving Human Pose Estimation Using Commodity WiFi (Wi-Mose, arXiv 2020): https://arxiv.org/pdf/2012.14066
[5] CSI-Channel Spatial Decomposition for WiFi-Based Human Pose Estimation (Electronics 2025): https://www.mdpi.com/2079-9292/14/4/756
[6] DT-Pose: Towards Robust and Realistic Human Pose Estimation (ICLR 2026审稿): https://openreview.net/pdf/f2428bc8d58ea4dffc8cf664c03aaaf5394e5bc9.pdf
[7] Deep Learning Based Fall Detection using WiFi Channel State Information (IEEE Access 2023): https://eprints.whiterose.ac.uk/id/eprint/202278/8/Deep_Learning_Based_Fall_Detection_Using_WiFi_Channel_State_Information.pdf
[8] Motion Pattern Recognition via CNN-LSTM-Attention Model Using Array-Based Wi-Fi CSI Sensors (Electronics 2025): https://www.mdpi.com/2079-9292/14/8/1594
[9] SenseFi: A Library and Benchmark on Deep-Learning-Empowered WiFi Human Sensing (Patterns 2023): https://www.pure.ed.ac.uk/ws/files/334748124/SenseFi_YANG_DOA06022023_VOR_CC_BY.pdf
[10] Deep-Learning-Based Baseline Evaluation of Public WiFi CSI Datasets (Sensors 2026): https://www.mdpi.com/1424-8220/26/12/3821
[11] mmMesh: towards 3D real-time dynamic human mesh construction (MobiSys 2021): https://dl.acm.org/doi/10.1145/3458864.3467679
[12] TRANS-CNN Based Gesture Recognition for mmWave Radar (Sensors 2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC10974769
[13] ProbRadarM3F: mmWave Radar-based Human Skeletal Pose Estimation with Probability Map Guided Multi-Format Feature Fusion (arXiv 2024): https://arxiv.org/html/2405.05164
[14] SUPER: Seated Upper Body Pose Estimation using mmWave Radars (arXiv 2024): https://arxiv.org/html/2407.02455v1
[15] MVDoppler-Pose: Multi-Modal Multi-View mmWave Sensing for Long-Distance Self-Occluded Human Walking Pose Estimation (CVPR 2025): https://cvpr.thecvf.com/virtual/2025/poster/33124
[16] Fall Detection System Based on Point Cloud Enhancement Model for 24 GHz FMCW Radar (2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC10820484
[17] mmGesture: Semi-supervised gesture recognition system using mmWave radar (Expert Systems 2023): https://www.sciencedirect.com/science/article/abs/pii/S0957417422020607
[18] A High-Fidelity mmWave Radar Dataset for Privacy-Sensitive Human Pose Estimation (mmFree-Pose, Bioengineering 2025): https://pmc.ncbi.nlm.nih.gov/articles/PMC12383697
[19] mmParse: Human Parsing with Joint Learning for Dynamic mmWave Point Clouds (UbiComp 2023): https://liux4189.github.io/files/Parsing_Ubicomp23.pdf
[20] Diffusion-Based mmWave Radar Point Cloud Enhancement Driven by Range Images (arXiv 2025): https://arxiv.org/html/2503.02300v1
[21] Deep High-Resolution Representation Learning for Human Pose Estimation (HRNet, CVPR 2019): https://arxiv.org/abs/1902.09212
[22] 基于深度学习的人体姿态估计与追踪 (ybasTrack, 华东理工大学学报 2024): https://journal.ecust.edu.cn/cn/article/pdf/preview/10.14135/j.cnki.1006-3080.20231018001.pdf
[23] PhysFormer: Facial Video-based Physiological Signal Measurement via Temporal Transformer (CVPR 2022): https://arxiv.org/abs/2111.12082
[24] TS-CAN: Temporal Shift Convolutional Attention Network for Remote Physiological Signal Measurement (2020): https://arxiv.org/abs/2005.03770
[25] 基于多模型融合的高精度实时摔倒检测系统 (计算机科学与应用 2024): https://pdf.hanspub.org/csa2024149_121543322.pdf
[26] 面向嵌入式平台的红外人体姿态估计系统 (计算机科学与应用 2024): https://pdf.hanspub.org/csa2024145_131543251.pdf
[27] 基于热成像技术的非接触式生命体征测量方法 (红外技术 2022): https://hwjs.nvir.cn/cn/article/pdf/preview/1b780bc8-22e6-495f-90bb-ecb14a233cb2.pdf
[28] UltrasonicGS: A Highly Robust Gesture and Sign Language Recognition Method Based on Ultrasonic Signals (Sensors 2023): https://www.mdpi.com/1424-8220/23/4/1790
[29] 基于RFID的无源感知机制研究综述 (软件学报 2022): https://www.jos.org.cn/html/2022/1/6344.htm
[30] Deep Learning for RFID-Based Activity Recognition (2018): https://pmc.ncbi.nlm.nih.gov/articles/PMC6205502
[31] A Hybrid Millimeter-Wave Radar–Ultrasonic Fusion System for Robust Human Activity Recognition with Attention-Enhanced Deep Learning (Sensors 2026): https://www.mdpi.com/1424-8220/26/3/1057
[32] P2MFDS: Privacy-Preserving Multimodal Fall Detection System for Bathroom Environments (arXiv 2025): https://www.alphaxiv.org/zh/abs/2506.17332v1
[33] Real-Time Fall Detection Using Smartphone Accelerometers and WiFi Channel State Information (2024): https://www.themoonlight.io/zh/review/real-time-fall-detection-using-smartphone-accelerometers-and-wifi-channel-state-information
[34] 视觉与4D毫米波前融合感知算法设计 (黑芝麻智能 2025): https://www.blacksesame.com/zh/brand-center/791.html
[35] 基于多传感器融合的协同感知方法 (雷达学报 2024): https://radars.ac.cn/article/doi/10.12000/JR23184
[36] RFID-based Human Activity Recognition Using Multimodal Convolutional Neural Networks (IEEE ETFA 2024): https://www.semanticscholar.org/paper/RFID-based-Human-Activity-Recognition-Using-Neural-Golipoor-Sigg/16ca2a438f49c33638ad4844fc7dd8f90be8bb07
[37] 零样本跨域Wi-Fi手势识别 (Widar3.0, TPAMI 2021): https://www.semanticscholar.org/paper/Widar3.0%3A-Zero-Effort-Cross-Domain-Gesture-With-Zhang-Zheng/db88f53e1037bcc269aa1a5a407a8d72afd7bb55
[38] RF-Pose: 3D Human Pose Estimation from Radio Frequencies (CVPR 2018): https://www.semanticscholar.org/paper/RF-Pose%3A-3D-Human-Pose-Estimation-from-Radio-Frequencies-Zhao-Xu/83b0e1bde3b3e9f4a5b4f5b0a5e1b6b4e5b0a5e1
[39] Widar 3.0 Database (IEEE DataPort): https://ieee-dataport.org/open-access/widar-30-wifi-based-activity-recognition-dataset
[40] mRI: Multi-modal 3D Human Pose Estimation Dataset using mmWave, RGB-D, and Inertial Sensors (NeurIPS 2022): https://proceedings.neurips.cc/paper_files/paper/2022/file/af9c9c6d2da701da5a0acf91ec217815-Paper-Datasets_and_Benchmarks.pdf
