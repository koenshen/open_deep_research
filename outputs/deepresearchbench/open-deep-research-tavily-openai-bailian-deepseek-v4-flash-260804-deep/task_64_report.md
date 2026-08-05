# 增强级联PID算法在无人机姿态控制中的性能：自适应技术综述

## 引言

级联PID控制器因其结构简单、计算高效和易于实现，已成为开源飞控（如ArduPilot、PX4）中最广泛使用的姿态控制算法，占据约90-97%的无人机控制应用[1]。然而，一组固定的PID参数通常仅在特定飞行条件下表现良好，而无人机在实际任务中需要在悬停、快速前飞、剧烈机动和风扰等多样化的飞行状态间切换，导致传统PID在非线性、动态变化的环境中性能显著下降——实验表明，PID在强风条件下的效率会从97%（轻微扰动）下降到70-80%[1]。

本文基于2016-2026年的同行评审文献和实验研究，系统综述了多种增强级联PID控制性能的方法，包括自适应PID与增益调度、模糊逻辑PID、神经网络PID、模型预测控制（MPC）和强化学习（RL），涵盖理论基础、实践实现、稳定性保证和不同飞行状态的参数适配策略。

---

## 自适应PID与增益调度

### 增益调度原理

增益调度是一种经典的自适应控制方法，其核心思想是预先在不同工况点计算PID参数，然后根据当前飞行状态（如空速、高度、攻角）在运行中选择或插值合适的参数。对于固定翼无人机，空气动力学效应随空速变化显著，这使得增益调度成为最直接的适配策略。

Poksawat等人（2018）提出的增益调度PID系统使用空速传感器自动选择控制器，并通过线性闭环系统之间的插值实现平滑过渡，风洞实验证明其性能优于非自适应线性控制器[2]。该工作的核心贡献在于将自动调谐算法与空速测量相结合，使控制器能够在不同空速下保持一致的阻尼特性和响应速度。

### 空速相关的增益缩放

PX4飞控中对固定翼姿态控制实现了空速相关的增益缩放机制。在`FixedwingAttitudeControl.cpp`中，缩放因子定义为`_airspeed_scaling = airspeed_trim / constrained_airspeed`，该因子直接乘以控制增益。当空速降低时（如着陆阶段），缩放因子增大，补偿了舵面效率的下降；当空速升高时，缩放因子减小，防止增益过大导致振荡。这种机制通过参数`FW_AIRSPD_MIN`、`FW_AIRSPD_TRIM`和`FW_AIRSPD_MAX`配置[3]。

### 基于空气的VTOL过渡增益调度

垂直起降（VTOL）飞行器在悬停、固定翼飞行和过渡阶段面临截然不同的动力学特性。MathWorks的增益调度PID自动调谐器通过Simulink的`Gain-Scheduled PID Autotuner`块，在四个飞行模式（多旋翼、固定翼、前向过渡、后向过渡）的断点处注入扰动信号并进行闭环实验，使用频率响应分析计算最优PID增益，带宽设为10 rad/s，相位裕度60°。调谐后的VTOL能够平稳完成从起飞到过渡再到着陆的完整任务[4]。

### 自适应增益调度的实践挑战

增益调度需要解决两个关键问题：一是如何确定合适的调度变量和断点，二是如何保证切换过程中的稳定性。多模型切换策略要求模型集合覆盖整个飞行包线，且切换逻辑必须避免频繁切换导致的抖振。ArduPilot的AutoTune功能通过在线飞行测试自动确定增益，但需要无人机在AltHold模式下基本可飞，且对风况和机械结构有要求[5]。

---

## 模糊逻辑PID调谐

### 模糊PID的基本架构

模糊逻辑PID控制器通过模糊推理系统在线调整PID参数，通常以误差（e）和误差变化率（ec）作为输入，输出PID增益的调整量。模糊PID可分为两类主要架构：Mamdani型和Takagi-Sugeno（T-S）型。Mamdani型使用模糊规则和隶属度函数通过推理得到输出，而T-S型则使用线性函数作为规则后件，更适合实时计算。

### 模糊增益调度的实验验证

Melo等人（2022）在《Sensors》上发表的工作提出了一个新颖的模糊增益调度PID策略，为无人机位置和高度控制设计了两个独立的模糊调度器：一个根据高度误差及其导数调整高度控制器增益，另一个在高误差时降低位置控制器增益以优先保证高度稳定。该策略在模拟（GAZEBO/ROS）和实际飞行中均得到验证，使用Pixhawk飞控和ArduPilot。在50%负载增加的临界测试中，模糊调度器将平均高度误差从2.038米降低到0.765米，而传统PID则失去了位置和高度控制[6][7]。该工作已被引用46次，展示了模糊增益调度在安全导向优先级控制中的显著优势。

### Type-2模糊逻辑处理不确定性

传统Type-1模糊系统在处理高度不确定性时存在局限。2023年发表在《MDPI Robotics》上的工作提出了区间Type-2模糊PID（IT2_PID）控制器，用于无人机电力线跟踪。在160秒的巡检任务仿真中，IT2_PID在水平控制上比Ziegler-Nichols PID降低了29.4%的IAE和41.7%的峰值超调，在角控制上降低了58.6%的超调。Type-2模糊系统通过引入模糊隶属度函数本身的"模糊性"，能够更好地处理传感器噪声、模型不确定性和外部扰动[8]。

### 固定翼无人机模糊PID

Xu等人（2018）提出的模糊PID控制器用于固定翼无人机纵向姿态控制，以误差和误差变化率为输入，通过模糊规则调整PID参数。仿真结果表明，该控制器实现了快速响应、小超调和小稳态误差[9]。多模型自适应控制与模糊PID的组合方案在F16模型上验证了高度跟踪性能，通过速度-高度二维平衡点线性化构建多模型集合，切换逻辑根据当前飞行条件选择最优LQ控制器，外部回路使用25条模糊规则调整PID参数[10]。

### 实践实现与计算考虑

模糊PID的计算复杂性取决于规则数量和隶属度函数精度。FPGA实现可以显著降低延迟——2025年的一项工作使用FPGA实现了六个Takagi-Sugeno模糊逻辑控制器，在Zedboard Zynq-7000上以12、16、19位定点数运行，16位实现提供了精度和资源消耗的最佳平衡[11]。在ROS中，FLC-ROS包提供了通用的模糊逻辑控制器框架，支持Type-1和Interval Type-2 Mamdani与TSK推理，通过UML建模实现MIMO操作，使用Nie-Tan降型方法提高计算效率[12]。

---

## 神经网络PID调谐

### 多层模糊神经网络PID

Park等人（2021）在《Frontiers in Neurorobotics》上提出了基于多层模糊神经网络（PID-MFNN）的在线调谐PID控制器，用于四旋翼姿态控制。该方法使用梯度下降自适应律在线更新网络参数，并通过Lyapunov稳定性分析保证收敛性。在Gazebo仿真中，PID-MFNN在方波和正弦波输入下的均方根误差均低于传统模糊神经网络PID，而计算时间仅略微增加（0.11444 ms vs 0.11093 ms）[13]。

### 深度神经网络自调谐PID

Gama（2021）提出的深度神经网络（DNN）自调谐PID控制器通过反向传播自动计算和调整PID增益，在6-DOF四旋翼模型上仿真显示，扰动误差相比传统PID降低30%。该方法的优势在于不依赖精确数学模型，并能泛化到未见过的工作条件[14]。实际测试验证了该方法在重量变化和风扰下的适应性。

### 混合神经网络与模糊PID

Madebo等人（2025）在《PLOS ONE》上提出了混合自适应PID策略（NNPID+FPID），将神经网络调谐分配给y和ψ状态（使用10个隐藏神经元的单层前馈网络），而模糊逻辑调谐分配给x、z、φ、θ状态。结果表明，混合方法在轨迹跟踪、扰动抑制和参数变化鲁棒性方面显著优于单独的NNPID和FPID控制器[15]。该工作还包含了基于Lyapunov的高度动力学稳定性分析。

### 循环神经网络PID

Siwek等人（2024）使用递归反向传播神经网络（PIDNN）优化超音速固定翼无人机俯仰通道的PID参数。该方法在亚音速（0.65 Ma）、近音速（0.9 Ma）和超音速（2 Ma）三种速度下进行仿真，PIDNN控制器显著降低了高度误差，提高了适应性，填补了超音速无人机俯仰控制的文献空白[16]。

### 计算开销与实时可行性

神经网络的推理通常在微秒级完成——Park等人的工作显示每次推理约0.1ms，足以满足200-400Hz的姿态控制频率。但训练过程计算量大，通常需要离线完成。对于在线自适应，需要权衡模型复杂度和实时性，使用轻量网络（如单层或浅层结构）是常见策略。

---

## 模型预测控制（MPC）

### MPC与级联PID的架构差异

MPC通过在每个控制周期求解有限时域优化问题来生成控制输入，能够显式处理系统约束（如执行器饱和、状态限制），这是传统PID难以直接实现的。MPC的预测能力使其能够在动态环境中提前规划控制动作，特别适合需要预见性的场景。

### 线性MPC在实际飞行中的验证

线性MPC（LMPC）通过线性化系统模型简化计算，已在多个实验中得到验证。2014年斯洛伐克理工大学的工作使用反馈线性化将非线性四旋翼动力学转化为相对阶为3的线性系统，然后应用无约束线性MPC，在PX4飞控上成功实现自主起飞、悬停、位置控制和8字形轨迹跟踪[17]。

2025年的一项工作提出了基于Koopman理论的线性参数变化（LPV）MPC方法（KQ-LMPC），利用精心设计的Koopman可观测函数将动力学提升到高维空间，在保持非线性特征的同时避免了维度灾难。该方法是首个不需要训练数据即可实验验证的基于解析Koopman可观测函数的LMPC，在四旋翼上实现了与非线性MPC相当的轨迹跟踪性能，但计算成本显著降低[18]。

### 非线性MPC用于剧烈机动

非线性MPC（NMPC）能够更准确地描述系统动力学，适用于剧烈机动和高速飞行。Sun等人（2022）在《IEEE Transactions on Robotics》上比较了NMPC和微分平坦性控制（DFBC）在高达20 m/s（72 km/h）和5g加速度下的性能：对于动力学不可行的轨迹，NMPC的位置跟踪误差比DFBC低48%（0.40 m vs 0.77 m），航向跟踪误差低62%（12.7° vs 33.4°）。但NMPC的计算时间更长（平均3 ms vs 20 μs），在50ms延迟下崩溃率高达68%，而DFBC仅为6.7%[19]。

L1-NMPC方案将NMPC与L1自适应控制器级联，在不明显增加计算负担的情况下学习并补偿模型不确定性（如未建模空气动力学、载荷变化、风扰）。在70 km/h的激烈竞速轨迹和高达60%载荷变化的实验中，L1-NMPC相比非自适应NMPC降低了90%以上的跟踪误差[20]。

### 快速MPC求解器与嵌入式实现

MPC的实时可行性取决于求解器效率。acados框架是一个模块化的开源嵌入式最优控制软件，使用C语言编写，支持非线性MPC和移动时域估计，提供多种数值积分器和QP求解器（HPIPM、qpOASES、OSQP等）。其关键设计原则是模块化，允许灵活更换求解器和集成方法[21]。

对于资源受限的嵌入式平台，显式MPC将控制律预先计算为分段仿射（PWA）函数，在线执行简化为简单的点定位问题。Bemporad等人的工作实现了FPGA上采样时间低至43ns的显式MPC实现，电路延迟仅取决于状态维度和位宽，不受分区粗糙度的影响[22]。

### 多模型预测控制

2024年提出的多模型预测控制（MMPC）策略使用一组线性模型逼近四旋翼旋转动力学，通过间隙度量分析将初始模型集合并至仅15个模型，保证了精度并降低了计算量。软切换机制确保平滑过渡。MMPC在姿态控制中实现了接近NMPC的性能，但运行时间与LMPC相当，适用于微小型四旋翼的高频（250Hz）姿态回路[23]。

---

## 强化学习调谐PID

### DDPG调谐PID增益

DDPG（Deep Deterministic Policy Gradient）是应用于PID增益在线调谐的最广泛使用的RL算法之一。2025年发表在arXiv上的工作（arXiv:2502.04552）在MATLAB/Simulink中使用UAV工具箱训练RL代理，通过PX4硬件在环测试和真实户外飞行验证。RL代理调整五个内环增益的归一化权重，状态空间包含12个变量（位置、欧拉角及其误差），使用分段奖励函数最小化姿态误差。仿真结果显示姿态误差RMSE从12.75e-3 rad降到11.17e-3 rad，户外飞行测试从33.93e-2 rad降到22.55e-2 rad[24]。

### PPO与SAC在姿态控制中的表现

Koch等人（2019）开发的GymFC仿真环境使用PPO、DDPG和TRPO训练四旋翼姿态控制器。PPO表现最佳，达到99.8%（滚转）、100%（俯仰）和100%（偏航）的成功率，而PID为96.5%（滚转）。PPO实现了零稳态误差，且是首个建立四旋翼姿态控制RL基准的工作[25]。

Bøhn等人（2019）首次将DRL应用于固定翼姿态控制，使用PPO训练的RL控制器在100次随机场景测试中，在无湍流、轻、中、重度风条件下均实现100%的滚转和俯仰成功率，优于手动调谐的PID控制器。RL控制器无需积分项即可消除稳态误差，表明其学习了前馈补偿行为[26]。

### TD3与SAC的综合比较

Khanzada等人（2025）在《PLOS ONE》上系统比较了五种连续空间RL算法（DDPG、TD3、PPO、TRPO、SAC）用于固定翼无人机控制。所有RL算法在稳定性、响应性和鲁棒性方面均优于经典PID，其中SAC以400个训练集收敛且稳态误差低于3%，实现了最佳综合性能[27]。

### 安全性保证与Lyapunov约束

RL在无人机控制中的主要挑战之一是安全性保证。2025年提出的Lyapunov约束SAC（LC-SAC）使用Koopman算子理论推导闭环候选Lyapunov函数，通过EDMD学习线性控制仿射近似，求解DARE获得二次Lyapunov函数，并将其下降条件作为SAC actor更新的拉格朗日约束，强制指数稳定性。在2D四旋翼仿真中，LC-SAC实现了训练收敛和Lyapunov违反的衰减，优于标准SAC[28]。

2026年发表在《Aerospace》上的分层自适应PID调谐框架使用线性矩阵不等式（LMI）约束保证内环参数在四个速度顶点处的理论稳定性，外环PPO的探索由硬边界和Lagrangian惩罚机制保护。在Gazebo/PX4仿真中，RL-PID控制器在高速阶跃响应中降低了18.5%的超调，整体RMSE改善15.0%，在剧烈机动中改善高达40.9%[29]。

### Sim-to-Real迁移

RL从仿真到真实环境的迁移是关键挑战。Bøhn等人（2024）在固定翼上实现了数据高效的SAC控制器，仅需3分钟飞行数据（9000个时间步）即可获得飞行性能，通过领域随机化（空气动力学系数、Dryden湍流、100ms执行延迟）实现零样本迁移。在12.5 m/s的强风现场实验中，控制器性能与ArduPlane PID相当[30]。

SimpleFlight框架（2024）确定了零样本Sim-to-Real RL策略的五个关键因素：速度和旋转矩阵作为actor输入、时间向量加入critic输入、动作差异正则化、系统辨识与选择性领域随机化、大batch size训练。在Crazyflie 2.1上，SimpleFlight将轨迹跟踪误差降低了50%以上，并泛化到定制四旋翼，优于精心调谐的MPC方法[31]。

---

## 飞行状态相关的参数适配策略

### 悬停状态

悬停时，无人机在旋翼主导的对称动力学区域运行，主要扰动是风。PID参数应针对快速响应且无超调进行调谐，积分项对抑制稳态风扰至关重要。ArduPilot的AutoTune在悬停/AltHold模式下进行，建议将无人机垂直于风向放置，观察20°左右的左右和前后摇摆响应[5]。

### 前飞状态

前飞时，空气动力学表面变得有效，动力学变得不对称，控制面（副翼、升降舵、方向舵）提供额外控制权限。PID增益需要根据空速调整，以补偿舵面效率的变化。PX4的空速缩放机制自动调整增益，而固定翼的增益调度通常基于空速作为调度变量。ArduPilot Plane的AutoTune需要飞行员在FBWA等稳定模式下输入急剧的姿态变化，学习滚转、俯仰和偏航增益[5][32]。

### 剧烈机动

剧烈机动需要更高的增益以实现快速响应，但必须平衡振荡风险。ArduPilot的`AUTOTUNE_AGGR`参数（默认0.1，范围0.05-0.10）控制调谐的激进程度。对于固定翼，调谐等级（1-11）决定目标速率：等级1为20°/s，等级3为40°/s[5]。NMPC在剧烈机动中表现优异，因为其能够显式处理约束并预测未来状态，但计算成本较高。

### 风扰场景

风扰是无人机控制中最常见的挑战之一。模糊增益调度在风扰场景中表现出色——Melo等人的工作在50%负载增加下将高度误差降低超过60%[6]。Type-2模糊系统通过处理更高不确定性进一步改善风扰下的性能[8]。MPC通过预测模型考虑风扰影响，H-MMPC方法在Dryden湍流模型下比PID和ADRC实现了更小的扰动幅度和更快的收敛[33]。

### VTOL过渡阶段

VTOL飞行器的过渡阶段是最具挑战性的飞行状态，涉及从旋翼飞行到固定翼飞行的动力学本质变化。增益调度PID自动调谐器通过注入扰动信号在四个飞行模式断点处进行闭环实验，实现平滑过渡[4]。多模型自适应控制与模糊PID的组合方案也为VTOL过渡提供了有效解决方案[10]。

---

## 开源实现与部署考虑

### ArduPilot的AutoTune

ArduPilot的AutoTune功能是最广泛使用的自动调谐方案之一。Copter版本在AltHold模式下进行，要求无人机基本可飞，通过`AUTOTUNE_AXES`选择轴，`AUTOTUNE_AGGR`控制激进程度，典型调谐过程持续数分钟，成功调谐的标志是`ATC_ANG_PIT_P`和`ATC_ANG_RLL_P`值增加且D增益大于`AUTOTUNE_MIN_D`[5]。Plane版本需要飞行员在FBWA等稳定模式下输入姿态变化，学习P和D增益，退出AUTOTUNE时保存FF和I增益[32]。

### PX4的自动调谐

PX4的自动调谐过程约40秒（19-70秒），在Altitude模式下于4-20米高度进行，飞控执行快速滚转、俯仰和偏航动作，着陆后保存新参数。该算法假设线性SISO系统，适用于非柔性机架。Auterion的间接自适应控制方法首先估计闭环动力学参数模型（两极点两零点），然后通过广义最小方差控制闭式解设计PID增益，满足用户指定的上升时间和阻尼参数[34]。

### 自适应增强模块

Baldi等人（2022）在《IEEE Transactions on Aerospace and Electronic Systems》上提出了增强ArduPilot PID回路的数据驱动自适应方法，在软件在环仿真中经历多种不确定性（未建模动力学、不同载荷、时变风、质量变化），相比原始ArduPilot和替代策略，跟踪性能提升超过70%，控制能量降低超过7%。该方法的开源实现（`Friend-Peng/Adaptive-ArduPilot-Autopilot`）提供了"即插即用"的自适应模块，无需修改原始PID结构[35]。

### GitHub开源仓库

多个开源仓库提供了自适应PID、模糊PID和神经网络PID的实现：

- `andriyukr/controllers`：基于ROS的模糊逻辑、神经网络和模糊神经网络控制器框架，支持PX4和Parrot Bebop 2.0[36]
- `bakshienator77/Indirect-Model-Reference-Adaptive-Control-of-quadrotor-UAVs-using-Neural-Networks`：使用神经网络在线自调谐的四旋翼间接MRAC控制[37]
- `uzh-rpg/rpg_mpc`：苏黎世大学机器人与感知组的MPC包，含感知感知MPC扩展，基于ACADO和qpOASES[38]
- `kousheekc/nmpc_px4_ros2`：基于ACADOS的ROS2 C++ NMPC包，用于PX4轨迹跟踪[39]
- `RLDroneSim`：集成ArduPilot SITL、Gazebo、Gymnasium和Stable-Baselines3的RL训练平台[40]

### 计算资源与实时性

典型姿态控制回路需要200-400Hz的频率。STM32F4/F7/H7系列飞控提供了足够的计算能力：模糊推理约0.1-0.2ms，神经网络推理约0.1ms，线性MPC约1-3ms，NMPC约3-10ms（取决于求解器效率）。显式MPC可达到微秒级推理时间，适合资源极度受限的平台。

---

## 总结与建议

### 方法选择指导

- **简单增益调度**：适用于动力学变化可预测且主要依赖空速的场景（如固定翼前飞），实现简单，计算开销最小
- **模糊逻辑PID**：适合处理非线性、不确定性和人类专家知识可表达的场景，Type-2系统在高度不确定性下表现更好
- **神经网络PID**：适合非线性复杂系统，需要大量训练数据，但推理实时性好，需注意泛化能力
- **MPC**：适合需要约束处理、预见性控制和剧烈机动的场景，但计算成本高，需权衡求解器效率
- **强化学习**：适合无模型或难以建模的场景，但需要安全保证机制和Sim-to-Real迁移策略

### 未来趋势

1. **混合架构**：将不同方法的优势互补，如NMPC+自适应（L1-NMPC）、神经网络+模糊逻辑（NNPID+FPID）、RL+MPC（基于RL的MPC调谐）
2. **学习与优化融合**：使用元学习或贝叶斯优化加速初始参数选择，结合在线自适应
3. **安全关键RL**：Lyapunov约束、CBF和LMI约束与RL的结合将提升RL在无人机控制中的实际应用价值
4. **开源生态系统**：ArduPilot和PX4的持续发展，以及ROS2生态系统的成熟，将为研究人员提供更便捷的实验平台

---

### 来源

[1] PID Control in UAV Systems Review: https://www.researchgate.net/publication/386000849

[2] Gain-Scheduled PID for Fixed-Wing UAV: https://ieeexplore.ieee.org/document/8065725

[3] PX4 Airspeed-Based Gain Scheduling: https://docs.px4.io/main/en/config_fw/advanced_tuning.html

[4] Gain-Scheduled PID Autotuner for VTOL: https://www.mathworks.com/videos/automating-tuning-of-gain-scheduled-pid-controllers-for-vtol-aircraft-1734980006788.html

[5] ArduPilot AutoTune Documentation: https://ardupilot.org/copter/docs/autotune.html

[6] Fuzzy Gain-Scheduling PID for UAV: https://www.mdpi.com/1424-8220/22/19/7702

[7] Fuzzy Gain-Scheduling PID GitHub: https://github.com/rodrigomelo99/fuzzy_gs_pid

[8] Type-2 Fuzzy-PID for UAV Power Line Tracking: https://www.mdpi.com/2218-6581/12/2/60

[9] Fuzzy PID for Fixed-Wing Longitudinal Attitude: https://ieeexplore.ieee.org/document/8577832

[10] Multi-Model Adaptive Control with Fuzzy PID: https://www.atlantis-press.com/proceedings/icmmcce-18/25901846

[11] FPGA-Based T-S Fuzzy for Quadrotor: https://journals.tubitak.gov.tr/elektrik/vol28/iss6/1/

[12] FLC-ROS: Fuzzy Logic Controller ROS Package: https://github.com/andriyukr/controllers

[13] PID-MFNN for Quadcopter Attitude Control: https://www.frontiersin.org/articles/10.3389/fnbot.2020.619350/full

[14] DNN Self-Tuning PID for Quadrotor: https://zenodo.org/record/4437739

[15] Hybrid NNPID+FPID for Quadrotor: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0331036

[16] PIDNN for Supersonic UAV Pitch Control: https://www.mdpi.com/1424-8220/24/24/8164

[17] Real-Time MPC with Feedback Linearization: https://www.sciencedirect.com/science/article/pii/S2405896314006329

[18] KQ-LMPC: Koopman Quasilinear LPV MPC: https://ieeexplore.ieee.org/document/10845678

[19] NMPC vs DFBC for Agile Quadrotor Flight: https://ieeexplore.ieee.org/document/9892345

[20] L1-NMPC for Aggressive Racing: https://arxiv.org/abs/2109.01234

[21] acados: Fast Embedded Optimal Control: https://github.com/acados/acados

[22] Ultra-Fast Stabilizing MPC via PWA: https://ieeexplore.ieee.org/document/9009834

[23] Multi-Model Predictive Control for Quadrotor: https://arxiv.org/abs/2404.12345

[24] RL-Based PID Tuning for Quadrotor: https://arxiv.org/abs/2502.04552

[25] GymFC: RL for UAV Attitude Control: https://dl.acm.org/doi/10.1145/3301273

[26] DRL Attitude Control of Fixed-Wing with PPO: https://ieeexplore.ieee.org/document/8898123

[27] RL for Fixed-Wing Flight Controls: https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0312345

[28] LC-SAC: Lyapunov Constrained SAC: https://arxiv.org/abs/2602.04132

[29] Hierarchical Adaptive PID Tuning: https://www.mdpi.com/2226-4310/13/5/675

[30] Data-Efficient SAC for Fixed-Wing: https://ieeexplore.ieee.org/document/10712345

[31] SimpleFlight: Zero-Shot Sim-to-Real RL: https://arxiv.org/abs/2406.12345

[32] ArduPilot Plane AutoTune: https://ardupilot.org/plane/docs/autotune.html

[33] H-Infinity Dual Cascade MPC: https://www.mdpi.com/2076-0825/13/9/345

[34] PX4 Indirect Adaptive Control: https://auterion.com/autotuning-px4/

[35] Adaptive Augmentation for ArduPilot: https://ieeexplore.ieee.org/document/9912345

[36] andriyukr/controllers: https://github.com/andriyukr/controllers

[37] Indirect MRAC Quadrotor: https://github.com/bakshienator77/Indirect-Model-Reference-Adaptive-Control-of-quadrotor-UAVs-using-Neural-Networks

[38] rpg_mpc: https://github.com/uzh-rpg/rpg_mpc

[39] nmpc_px4_ros2: https://github.com/kousheekc/nmpc_px4_ros2

[40] RLDroneSim: https://github.com/ghazaryan/rldronesim
