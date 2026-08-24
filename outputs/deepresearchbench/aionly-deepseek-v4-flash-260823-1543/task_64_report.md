# Comprehensive Research Report: Enhancing PID-Based Attitude Control for Unmanned Aerial Vehicles

## Introduction

The attitude control problem for unmanned aerial vehicles (UAVs) remains a critical challenge, particularly because most open-source flight controllers (PX4, ArduPilot) implement cascaded PID control algorithms that perform optimally only within narrow flight envelopes. A single set of PID gains tuned for hover conditions degrades significantly under varying flight states—including changes in airspeed, altitude, payload, wind disturbances, and actuator faults. This report synthesizes peer-reviewed research and official documentation across five dimensions: adaptive/gain-scheduling methods, optimal tuning approaches, practical implementation guidelines, comparative analysis of enhancement techniques, and the current state of the art.

---

## 1. Adaptive and Gain-Scheduling PID Methods

### 1.1 Gain Scheduling Based on Flight State

Gain scheduling addresses the fundamental limitation of fixed-gain PID controllers by pre-designing multiple sets of PID gains for different operating points and interpolating between them as the flight condition changes.

**Airspeed-Based Gain Scheduling for Fixed-Wing UAVs:** Poksawat, Wang, and Mohamed (2018) developed a gain-scheduled PID cascade control system for fixed-wing UAVs where controllers are automatically selected via an airspeed sensor positioned ahead of the aircraft. The gain scheduling is implemented through interpolation between linear closed-loop system family members to ensure smooth transitions between operating points. Wind tunnel experimental results demonstrated significant performance improvement over a linear control system without controller adaptation [1].

**Fuzzy Gain-Scheduling PID for Quadrotor Position and Altitude:** Melo et al. (2022) proposed a novel dual fuzzy gain scheduler that adjusts PID gains for both altitude and position controllers. The altitude scheduler adjusts gains based on altitude error and its derivative, enabling aggressive response when far from target and smoother response when close. Critically, the position scheduler uses altitude error to moderate position control effort, prioritizing altitude stability over position accuracy during disturbances—a feature not present in other implementations. Real-world experiments using a Pixhawk 2.4.8 with ArduPilot firmware showed that under critical load conditions (95% of designed load), the fuzzy scheduler maintained an average height error of 0.765 m compared to 2.038 m without it, while position error was 2% lower than comparative approaches [2].

**Neural Network Supervisor for Gain Scheduling:** Adıgüzel, Kurtuluş, and Türker (2024) proposed a gain-scheduling controller with a supervisor neural network for quadrotor attitude control. Different operating points are selected based on a proposed rule in the working region, and a radial basis function neural network (RBFNN) is trained using gradient descent-based supervised learning to ensure robustness against time-varying disturbances. The controller, which is "not so different from conventional controllers in terms of processor power," provides the desired performance criteria across a wide operating region [3].

**Angle-of-Attack Scheduling for LPV Systems:** A 2025 study in *The Aeronautical Journal* presented a robust gain-scheduled adaptive control strategy combining LQR with fractional-order PID (FOPID) controllers, supervised by an adaptive switching law based on a moving time-window cost function. The scheduling variable is the angle-of-attack α, with six different models (α values between 6.9° and 20°). The fractional-order case (λ=0.8, μ=0.6) demonstrated no overshoot, while the integer-order case showed important peaks at step instants, with superior robustness against measurement noise [4].

**Scheduling Control Frequencies via Deep Reinforcement Learning:** Kang, Park, and Choi (2022) discovered that optimal PID control frequencies vary depending on trajectory type and external disturbances. Their approach combines a Control Frequency Agent (CFA)—a deep reinforcement learning model that schedules the ratio of position and attitude control frequencies—with a Quadrotor Future Predictor (QFP) neural network that predicts the next state and estimates external disturbances. The combined CFA+QFP approach reduced travel time compared to conventional fixed-frequency PID controllers, especially under complex wind disturbances [5].

### 1.2 Fuzzy Logic-Based PID Controllers

Fuzzy PID controllers use expert knowledge encoded as fuzzy rules to dynamically adjust PID gains in real-time based on error and error rate.

**Self-Tuning Fuzzy PID for Quadcopter:** Baharuddin and Basri (2023) proposed a simple fuzzy algorithm incorporated into a PID controller, addressing the challenge of quadrotors' nonlinear, coupled, and underactuated dynamics. The fuzzy system uses two inputs (error e and rate of error ė) with seven fuzzy subsets each, and three outputs (α, β, γ) to adjust PID gains via formulas: Kp = Kp_min + (Kp_max - Kp_min) × α, Kd = Kd_min + (Kd_max - Kd_min) × β, and Ki = γ × Kp²/Kd. The fuzzy self-tuning controller demonstrated no overshoot compared to the PID controller alone when disturbances were applied [6].

**Cascaded Fuzzy-PID for Cost-Effective Platforms:** A 2025 study proposed a cascaded fuzzy-PID architecture using classical PID in the inner loop for rapid attitude stabilization and fuzzy logic in the outer loop to dynamically adjust PID gains for improved disturbance rejection. Under wind disturbances, the cascade fuzzy PID controller reduced steady-state error, shortened pitch and roll angle stabilization time by 45%, yaw angle stabilization time by 31%, and recovery time to stability by 44% under identical disturbance conditions. The computational efficiency satisfies embedded deployment requirements on ARM Cortex-M3 platforms [7].

**Fuzzy Adaptive PID with Disturbance Observer:** A 2022 study in *Aerospace Science and Technology* combined fuzzy logic system approximation of unmodeled dynamics with a disturbance observer for external disturbance estimation. Command filtering and error compensation mechanisms further improved tracking accuracy. Experimental results on the QBall 2 testbed (with OptiTrack indoor positioning system) verified that the proposed method achieves full 6-DOF control with smaller tracking error compared to traditional PID control [8].

### 1.3 Neural Network-Based PID Approaches

Neural networks offer powerful nonlinear approximation capabilities for online PID gain adaptation.

**RBF Neural Network Intelligent-PID:** Kim and Suh (2024) proposed an intelligent-PID (I-PID) controller augmented with an RBF neural network (2-5-1 structure with Gaussian activation functions) and an adaptive robust term. The adaptive law was designed based on Lyapunov stability to satisfy control system stability. Position control results showed X-axis convergence in 1.145s (max error 0.05) vs PID's 1.532s (max error 0.125), Z-axis convergence in ~1.5s (error 0.117) vs PID's 6.316s (error 0.161). The controller can be configured similarly to conventional PID controllers but exhibits enhanced robustness and tracking accuracy [9].

**Neural Network PID with Ziegler-Nichols Initialization:** Siwek et al. (2024) optimized PID gains initially determined via the Ziegler-Nichols II method using a recurrent back-propagation neural network (PIDNN) with a three-layer architecture (2 input neurons, 3 hidden neurons performing proportional/integral/derivative operations, 1 output neuron). For supersonic flight (2 Ma) at 6000m start altitude, PIDNN achieved regulation time of 0s vs classical PID's 104.8s, with steady-state errors reduced to between 1.44 m and 2.09 m. The classical PID showed significant limitations—at 6000m start altitude, subsonic flight (0.65 Ma) caused large oscillations and the UAV dropped below the surface [10].

**ISSA-BP-PID-LESO Framework:** Wang et al. (2025) proposed an improved sparrow search algorithm with chaotic mapping for BPNN weight optimization, enabling adaptive PID tuning through an integrated ISSA-BP-PID-LESO framework. A linear extended state observer (LESO) estimates and compensates for time-varying external disturbances in real time. Results showed tracking error reduction by 65.5%, overshoot by 88.9%, and steady-state error by 98.3% compared with standard PID, with RMSE improved by 33.4% [11].

**Hybrid Neural Network and Fuzzy Logic Adaptive PID:** Madebo (2025) presented a novel hybrid approach where neural networks fine-tune PID gains for y and ψ (yaw) states while fuzzy logic handles x, z, φ (roll), and θ (pitch) dynamics. A single-layer neural network with 10 hidden neurons adjusts PID gains using proportional, integral, and derivative errors, with weights updated via gradient descent. The FPID controller reduces position errors by 87% and attitude errors by 70% relative to traditional PID. The paper claims this is the first comprehensive integration of neural networks and fuzzy logic for adaptive PID gain tuning across all UAV dynamic states [12].

### 1.4 Linear Parameter-Varying (LPV) Approaches

LPV techniques provide a systematic framework for gain-scheduled multivariable control with formal stability guarantees.

**LPV Control Theory for Aerospace:** Balas (2002) established that LPV techniques provide a systematic design procedure for gain-scheduled multivariable controllers, allowing performance, robustness, and bandwidth limitations to be incorporated into a unified framework. Three design approaches exist: Linear Fractional Transformation (LFT) based on the small gain theorem, Single Quadratic Lyapunov Function (SQLF), and Parameter-Dependent Quadratic Lyapunov Function (PDQLF). A crucial distinction is between methods using a single Lyapunov function (more conservative but simpler) and parameter-dependent Lyapunov functions (less conservative but more computationally demanding) [13].

**Observer-Based LPV Control with Anti-Windup:** Theis et al. (2020) proposed a low-complexity anti-windup compensation scheme for LPV controllers. The key innovation is a novel synthesis algorithm that splits the problem into an observer synthesis and a subsequent state feedback synthesis, resulting in a controller structure that enables a differential implementation (calculating the derivative of the control signal rather than the signal itself). This allows straightforward incorporation of conventional anti-windup logics such as back-calculation or integrator clamping without increasing controller complexity. The method avoids three practical issues with standard LPV approaches: poor scaling of semidefinite programs, dependence on time-derivatives of scheduling parameters, and difficulty of including anti-windup compensation [14].

**Fractional-Order LPV with LQR+FOPID:** The 2025 *Aeronautical Journal* study combined LQR with fractional-order PID controllers for LPV systems, with the FOPID+LQR scheme demonstrating superior robustness against measurement noise. The fractional-order case (λ=0.8, μ=0.6) presented no overshoot, while the integer-order case showed important peaks at step instants [4].

**H∞ Control with LPV Models for Multi-Rotor Dynamics:** Kumar and Bhattacharya (2025) established a systematic framework for representing nonlinear multi-rotor dynamics within the LFT formalism, treating trigonometric nonlinearities and parameter-dependent terms as structured uncertainties. Robust H∞ controller synthesis using only gyroscope measurements was tested under Dryden turbulence with gust velocities up to 15 m/s. The PID controller exhibited peak error exceeding 30°, while the H∞ controller reduced peak error to 7.12° with RMSE of 1.35° vs PID's 5.67° [15].

### 1.5 Model Reference Adaptive Control (MRAC) and Other Adaptive Strategies

**Modified MRAC with Updated MIT-Rule:** Rothe et al. (2020) designed a modified MRAC for UAV altitude control. The M-MRAC multiplies an adaptive gain θ to the existing PID controller output and adds a PID controller to the adjustment mechanism to handle abrupt changes. The standard MIT-rule (θ̇ = -γ'·e·yₘ) fails when the reference model output yₘ = 0; the authors modified the rule to depend on the plant output y instead: θ̇ = -γ·e·(y/θ), with normalization to prevent instability. When a 100g mass (nearly half the UAV's weight) was attached, the M-MRAC showed a peak overshoot of only 0.1m and returned to the desired position almost immediately, while the standard controller had a peak overshoot of 0.6m and could not recover within 20 seconds [16].

**Decentralized Robust Direct MRAC:** Jurado (2024) proposed a decentralized robust direct MRAC for quadrotor attitude control, with a σ-modification (leakage factor) added to the update law to enforce robustness: Θ̂̇ = ΓΘ Φ x e^T P B - σΘ̂. A theorem proves uniform ultimate boundedness (UUB) of all signals in the closed-loop system without requiring any prior information on system perturbation upper bounds. Simulation results showed that parameter estimates do not drift to infinity when the decentralized MRAC deals with perturbations [17].

**Combined MRAC (CMRAC):** Ghaffar (2021) presented CMRAC with a baseline controller allowing in-flight switching between the two, using an augmented state to improve tracking performance. The CMRAC implementation provides a shorter transient phase, faster parameter convergence, and closer tracking of the desired reference model response compared with standard MRAC [18].

### 1.6 Sliding Mode Augmented PID and Disturbance Observer-Based Methods

**Adaptive PID Using Sliding Mode Control (APIDC):** Noordin, Basri, and Mohamed (2021) proposed an auto-tuning adaptive PID control system where sliding mode control provides the adaptive mechanism to tune PID gains online, with a fuzzy compensator to eliminate chattering. The auto-tuning process is based on gradient descent and the Lyapunov stability theorem. The paper has 116 citations, indicating significant impact [19].

**Real-World Validation of APIDC:** Noordin et al. (2023) evaluated APIDC on a Parrot Mambo Minidrone (mass 0.063 kg) for position tracking under wind gusts. In real-time experiments with wind gusts (~1.6 m³/min), APID outperformed PID by 26.2% (x-axis) and 45.1% (y-axis) for waypoint tracking, and showed 6.6% (x-axis) and 25.8% (y-axis) improvement for orbit tracking. The APID control scheme enhances resilience and stability of MAVs for surveillance, search and rescue, and environmental monitoring applications [20].

**Disturbance Observer-Enhanced Adaptive Fault-Tolerant Control:** Hu et al. (2023) proposed an adaptive sliding mode control (ASMC) strategy with an integral sliding surface and a disturbance observer for active compensation. The adaptive scheme is formulated with both the sliding variable and boundary layer thickness—adaptation stops when the sliding variable is inside the boundary layer. Under actuator fault (#1) combined with disturbances and parametric uncertainties, only the Disturbance Observer-based ASMC (DOASMC) maintained stable performance, while ASMC showed chattering and baseline SMC deteriorated [21].

**Variable Disturbance Observer-Based Control (VDOBC):** Jeong, Suk, and Kim (2024) proposed VDOBC that overcomes limitations in DOBC by introducing a variable nominal model that adapts according to flight speed, derived from high-fidelity dynamic modeling based on wind-tunnel testing. The Q-filter time constant is dynamically selected by analyzing closed-loop pole stability. Flight tests demonstrated that VDOBC outperforms conventional DOBC in attitude tracking accuracy during a round-trip flight with a slung load [22].

**Sliding Mode Control with Improved Extended State Observer (SMC-IESO):** A 2025 study in *Electronics* presented SMC-IESO with an improved sliding mode control law incorporating observation error compensation. By introducing position observation error feedback and exploiting the relationship between observation and disturbance estimation errors, the method reduces the required sliding gain, effectively suppressing chattering. Position tracking RMSE was less than 0.0824 m, approximately 40% improvement over PID control, with attitude tracking RMSE less than 3.7667° [23].

---

## 2. Optimal PID Parameter Tuning Methods

### 2.1 Classical Tuning Methods

**Ziegler-Nichols Closed-Loop (Continuous Cycling) Method:** This empirical method involves setting the controller to P-only mode, slowly increasing Kp until sustained, stable oscillations occur, then recording the ultimate gain (Ku) and ultimate period (Pu). PID parameters are computed as Kp = 0.6·Ku, Ti = Pu/2, Td = Pu/8. The method produces aggressive control behavior with a 25% maximum step overrun as the design condition. Zhao (2023) applied Ziegler-Nichols to cascade PID control for quadrotor UAVs, yielding inner loop gains of Kd=5.225, Kp=13.550, Ki=16.504 and outer loop gains of Kd=0.08, Kp=0.009, Ki=0.00003. The quadrotor achieved target position (50,50,30) with settling times of 2.8s (X), 3s (Y), and 14.7s (Z), with robustness validated against 1 kg camera load and wind disturbances [24].

**Ziegler-Nichols Open-Loop (Process Reaction Curve) Method:** A step test is performed in open loop, measuring dead time (τdead), response time (τ), and ultimate steady-state value (Mu). Parameters are computed as R = τdead/τ and Ko = (Xo/Mu)(τ/τdead). This method is quick and robust but depends on purely proportional measurement and approximations may be inaccurate [25].

**Cohen-Coon Method:** Developed specifically for processes with significant time delays, Cohen-Coon uses process reaction curve data to determine controller parameters with improved disturbance rejection. For PID controllers: Kp = (1.2/Kp)·(τ/θ), Ti = 2·θ, Td = 0.5·θ. The method is designed for processes where delay time is less than 2× time constant, providing quicker closed-loop response than Ziegler-Nichols for time-delayed processes. However, it produces faster response but with more overshoot than Ziegler-Nichols [26].

**Applicability to UAV Attitude Loops:** Classical methods are useful for initial gain estimation but have significant limitations. As noted in the SimpleFOC community, "Ziegler-Nichols method is not really intended for smooth operation or for great performance... it does not guarantee much more than stability of the system" [27]. These methods provide a starting point but require significant refinement for UAV attitude control.

### 2.2 Optimization-Based Approaches

**Genetic Algorithm (GA) and GA-PSO Hybrid:** Li, Bai, and Zhou (2024) optimized a cascaded PID controller using GA combined with PSO (GA-PSO). GA performs global exploration (150 total iterations; 100 for GA, then 50 for PSO), while PSO fine-tunes the parameters. The cost function is Integral of Time-weighted Absolute Error (ITAE). The proposed GAPSOPID-FuzzyLADRC controller outperformed PID-PID, PID-LADRC, and PID-FuzzyLADRC by 62.16%, 22.02%, and 19.04% respectively in X-axis trajectory tracking. Under external disturbances (time-varying wind with Gaussian white noise), the maximum overshoot was reduced by 1409%, 138.6%, and 131.8% compared to the other controllers. The controller tracked trajectories faster (4.25s vs 5.45s/5.25s/11.26s for position tracking from 0 to 1m) [28].

**Particle Swarm Optimization (PSO):** Rodriguez and Lu (2024) tuned six PID control schemes (roll, pitch, yaw for attitude; thrust, x-position, y-position for positional control) totaling 18 parameters using PSO over 70 iterations. PSO demonstrated rapid convergence (typically between iterations 20-30). For the Pac-Man course: Default had log10SSE 5.2249 in 9m55s; PSO-Tuned 4.4850 in 3m50s; PSO-Global-Best 4.3598 in 2m33s—approximately four times faster than default. Final tuned parameters: ThrottlePID Kp 1.52±0.13, Ki 0.22±0.06, Kd 0.57±0.14; YawPID Kp 0.84±0.17, Ki 0.13±0.05, Kd 0.28±0.18 [29].

**Differential Evolution (DE):** An IEEE SSCI 2016 paper proposed a two-stage automatic PID tuning scheme using DE. The first stage tunes inner-loop attitude PD controllers (roll, pitch, yaw) for fast transient response. The second stage tunes outer-loop position PID controllers for smooth trajectory tracking. An adaptive mutation operator maintains population diversity early and accelerates convergence later. The cost function incorporates time-domain performance indexes of x/y and altitude channels. DE showed superior cost minimization across all channels compared to GA and PSO [30].

Gün (2023) compared DE, PSO, Gravity Search Algorithm (GSA), and Charged System Search (CSS) for minimizing torque/energy consumption in quadrotor attitude control. Although DE had a higher cost minimization convergence value, the PID coefficients obtained from DE produced lower torque values in the control program, leading to better energy efficiency compared to PSO (the closest competitor) [31].

**Cuckoo Search Algorithm (CSA):** Soyinka, Ikpaya, and Luka (2025) compared CSA and PSO for tuning PID gains under static wind gust disturbance. PSO achieved convergence errors of 2.85E-07 (roll), 2.89E-08 (pitch), and 1.45E-07 (yaw). CSA achieved superior convergence errors of 1.80E-08 (roll), 4.51E-09 (pitch), and 3.34E-09 (yaw). A Wilcoxon signed-rank test confirmed a statistically significant difference (p = 1.91×10⁻⁶) favoring CSA [32].

**Comprehensive Metaheuristic Comparison:** Çopur, Balta, and Bilgic (2025) employed PSO, Grey Wolf Optimization (GWO), Artificial Bee Colony (ABC), and DE to optimally tune PID parameters within a cascade control architecture. Multiple fitness measures were compared including IAE, ISE, ITAE, and ITSE. The study explored robustness against environmental effects and parametric uncertainties [33].

**Multi-Objective Optimization Comparison (Metaheuristics vs Bayesian Optimization vs DRL):** A 2025 arXiv preprint compared three families of gradient-free optimizers: metaheuristics, Bayesian Optimization (BO), and Deep Reinforcement Learning (DRL). The framework uses a cascade PID architecture inspired by PX4 flight stacks with five controllers (position, altitude, attitude, horizontal speed, vertical speed), yielding 15 tunable gain parameters. **Key findings**: Metaheuristics consistently improved performance over the manually tuned Ziegler-Nichols baseline, with GWO producing optimal results. Bayesian Optimization was sample-efficient but carried higher per-iteration overhead and depended heavily on design domain definition. Reinforcement learning agents did not surpass the baseline in the current setup, suggesting the problem formulation requires further refinement [34].

### 2.3 Model-Based Tuning Methodologies

**LQR-Inspired PID Tuning:** Guardeño, López, and Sánchez (2019) developed a pre-tuning method for multivariable PID controllers for quadrotor attitude and altitude control using LQR/LQG theory with a single pre-tuning parameter, considerably simplifying the design process. The method yields the twelve gains of a standard control structure (four PID controllers: three for attitude, one for altitude) through a single pre-tuning parameter. The method is robust to parametric uncertainty, disturbances at the plant input, and sensor measurement and estimation errors. Validation was performed on a DJI-F450 quadrotor with a custom PCB flight controller, with experimentally characterized rotor dynamics, sensor noise/bias from low-cost commercial sensors, and sensor fusion algorithms [35].

**Pole Placement Based PID Design:** Yang et al. (2013) presented a self-tuning PID controller based on adaptive pole placement for quadrotor control that tunes PID parameters online according to system changes. Simulation results showed accurate control with enough adaptability and robustness [36].

**Internal Model Control (IMC) Based Tuning:** Song et al. (2016) proposed a cascaded control structure for attitude control of multi-rotor UAVs using the Simple Internal Model Control (SIMC) method for PID tuning. A systematic procedure was proposed involving flight tests, system identification using the frequency sweep method, and SIMC-based PID tuning. Application to the roll axis resulted in PID-PID cascade control, while application to the yaw axis resulted in PID-PI cascade control, validated experimentally [37].

**Loop-Shaping for Cascaded Attitude Control:** Zhang and Peng (2025) developed a loop-shaping methodology for fixed-wing UAV attitude control focusing on achieving desired frequency-domain characteristics. Design specifications included inner-loop crossover frequency of ~8 rad/s, outer-loop bandwidth of ~2 rad/s, minimum phase margin of 70°, gain margin exceeding 6 dB, and high gain at low frequencies for disturbance rejection with rapid high-frequency roll-off (−60 dB/dec). Real flight tests on a Sky Surfer 1400 fixed-wing UAV confirmed the method achieves the intended bandwidth and stability margins [38].

### 2.4 System Identification for Building Attitude Dynamics Models

**Frequency-Domain System Identification (CIFER):** Wei et al. (2015) used frequency-domain system identification techniques to extract a bare-airframe dynamic model of a quadrotor in hover condition. The bare-airframe dynamics were found to be highly unstable with a time-to-double amplitude of ~0.55 seconds, "renders the bare-airframe essentially un-flyable without a feedback control system." High symmetry between pitch and roll derivatives was observed, while bare-airframe yaw and heave dynamics are stable and characterized by first-order systems. The identified model was verified in the time-domain using dissimilar flight test data, with all verification costs below the guideline of 2 [39].

**Sine Wave Injection System Identification:** Kaputa and Owens developed a quadrotor system identification method using model-based design and in-flight sine wave injections, validated with a camera-based motion tracking system (OptiTrack). Linear transfer function models for roll, pitch, yaw, vertical speed, and horizontal position were derived, accounting for motor dynamics, propeller characteristics, and digital update delays. An antiresonance effect was identified in the horizontal speed response caused by a 2cm offset between the CG and OptiTrack sensor reference point. After gain optimization, the drone achieved position holding accuracy of ~1cm horizontal and 2mm vertical in hover [40].

**Continuous-Time Black-Box System Identification:** Noormohammadi-Asl et al. (2020) performed continuous-time black-box system identification based on experimental frequency response data to obtain a nominal linear model and a multiplicative uncertainty block for H∞ control synthesis. No prior model or CAD parameters of the quadrotor were available, making the system identification phase critical [41].

---

## 3. Practical Implementation Considerations for Cascaded Attitude Control

### 3.1 Cascaded Control Architecture and Tuning Order

**PX4 Multicopter Control Architecture:** PX4 uses a standard cascaded control design mixing P and PID controllers. The angular rate controller is a K-PID controller with limited integral authority (anti-windup), outputs limited to -1 and 1, with a low-pass filter on the derivative path. The IMU pipeline flows from gyro data through calibration, bias removal, notch filter, low-pass filter, then derivative through another LPF. The attitude controller is quaternion-based, implemented from an ETH research article, using a 2nd-order critically-damped reference model (MC_REF_W_N) for setpoint smoothing, with feedforward scaled by MC_REF_FF and clipped by MC_REF_FF_MAX. The velocity controller has anti-reset windup, and the position controller is a simple P controller commanding velocity, saturated by MPC_XY_VEL_MAX [42].

**ArduPilot Copter Attitude Control Architecture:** A P controller converts the angle error into a desired rotation rate, followed by a PID controller that converts the rotation rate error into a high-level motor command. The system runs at 400Hz on Pixhawk and 100Hz on APM2.x boards. The AC_AttitudeControl library provides 5 attitude control methods. The AP_Motors library handles "motor mixing"—converting roll, pitch, yaw, and throttle values into absolute motor PWM outputs—including a "stability patch" that prioritizes one axis over another when requests exceed physical limits [43].

**Critical Tuning Order:** Both PX4 and ArduPilot emphasize that tuning must proceed from innermost to outermost loop. ArduPilot's Chris Rosser emphasizes the specific order: **D → P → I → Derivative Feedforward → Feedforward**. The D term prevents the P term from oscillating (correct P:D ratio needed), the P term prevents the I term from oscillating (correct P:I ratio needed), and derivative feedforward depends on the P term value. Tuning in this order creates a one-way flow so earlier terms don't need to be re-adjusted [44].

### 3.2 Guidelines for Selecting Initial PID Gains

**PX4 Rate Controller Initial Gains:**
- Typical D values (standard form): between 0.01 (4" racer) and 0.04 (500 size); parallel form between 0.0004 and 0.005
- Typical I values (standard form): between 0.5 (VTOL plane), 1 (500 size) and 8 (4" racer); parallel form between 0.3 and 0.5
- Usually the same tuning gains can be used for roll and pitch
- Pitch usually needs slightly higher I values than roll [45][46]

**PX4 Attitude Controller Initial Gains:** P gains are typically default values; parameters include MC_ROLL_P, MC_PITCH_P, MC_YAW_P, plus maximum rotation rates (MC_ROLLRATE_MAX, MC_PITCHRATE_MAX, MC_YAWRATE_MAX). Tune in Stabilized mode by increasing P gains until oscillations appear, then back off [45][46].

**ArduPilot Helicopter Initial Parameter Values:**
- Pitch and Roll Axes: ATC_ANG_PIT_P = 4.5, ATC_ANG_RLL_P = 4.5, ATC_RAT_PIT_I = 0.1, ATC_RAT_PIT_ILMI = 0.05, ATC_RAT_PIT_IMAX = 0.40, ATC_RAT_PIT_P = 0, ATC_RAT_PIT_FF = 0.15 (same values for RLL)
- Yaw Axis: ATC_ANG_YAW_P = 4.5, ATC_RAT_YAW_D = 0.003, ATC_RAT_YAW_FF = 0.0 (for UAV helicopters with low headspeed, set to 0.05 before first test hover) [47]

**Key Tuning Guidelines:**
- All gains should be increased very slowly, by 20-30% per iteration, and even 5-10% for final fine-tuning. Too large gains may cause dangerous oscillations
- Always land quickly after changing a parameter, then slowly increase throttle to check for oscillations
- Tune around the hovering thrust point
- Always disable MC_AIRMODE when tuning a vehicle
- A well-tuned vehicle in acro mode will not tilt randomly towards one side but keeps the attitude for tens of seconds even without any corrections [45][46]

### 3.3 Rate Limits and Angular Acceleration Limits

**ArduPilot ACCEL_MAX:** Limits maximum angular acceleration demanded by the attitude controller. Small drones (up to 8-inch props) can set these to 0 to disable. Critical to calculate for larger drones. The maximum lean angle is calculated as: max lean angle = arccos(weight / (80% of max thrust)). This ensures the drone can maintain altitude at max lean angle using only 80% of max motor thrust, leaving 20% for control. Recommend max angle of 30° for most applications [44].

**PX4 Maximum Rotation Rate Parameters:** MC_ROLLRATE_MAX, MC_PITCHRATE_MAX, MC_YAWRATE_MAX. Rate setpoints are limited based on auto or manual mode rate limits [46].

### 3.4 Anti-Windup Mechanisms

Three main anti-windup methods are documented in the literature:

**Integral Clamping:** Limits the integrator output to specified minimum and maximum values. Simple, no new gain parameter needed, but can produce non-smooth behavior and may be slow to recover [48].

**Conditional Integration:** Uses a switch to turn off integration when the actuator is saturated (i.e., when the controller output ≠ actuator output and the product of error and controller output is not helping to unsaturate). Moderate complexity, no new gain parameter [48].

**Back-Calculation:** Adds a feedback correction term to the integrator input: the difference between actuator output and controller output, multiplied by an anti-windup gain (K_aw). This is the smoothest method, providing fast recovery, no steady-state error, but requires tuning the anti-windup gain. The recommended starting value is Kb = 0.5 (equal to Ki). If recovery from saturation is too slow, increase Kb. If the controller oscillates after saturation, decrease Kb. Typical range is 0.1 to 1.0 [49].

**PX4 Implementation:** The angular rate controller has limited integral authority (anti-windup), outputs limited to -1 and 1. The velocity controller has anti-reset windup. Horizontal thrust is prioritized by the z (vertical) control first to give altitude priority—if z control saturates, x-y control is skipped [42].

**A novel hybrid anti-windup strategy** combines conditional integration with dynamic back-calculation, providing a two-stage correction: immediate conditional clipping followed by smooth recovery via back-calculation. The tracking time constant is computed as Tt = α·Ti, where α is always less than 1 [50].

### 3.5 Actuator Saturation and Control Allocation

**PX4 Mixer Saturation and Airmode:** Mixing converts torque commands and scalar thrust into individual motor commands; saturation occurs when a motor command becomes negative (or exceeds 100%). With Airmode disabled, commanded torque is reduced so no motor command is below zero (requires minimum thrust for attitude correction). With Airmode enabled, commanded thrust is boosted so no motor command is negative, allowing attitude/rates to be tracked at low or zero throttle, but can cause continued ascent when throttle is reduced to zero. Once the vehicle flies well, Airmode can be enabled via the MC_AIRMODE parameter [46].

**Thrust Curve / TPA:** The THR_MDL_FAC parameter adjusts the thrust-to-PWM curve (0 = linear, 1 = quadratic). Typical values are between 0.3 and 0.5. Higher values indicate a quadratic relationship between PWM and thrust. Changing this parameter requires rate controller re-tuning. Throttle PID Attenuation (TPA) linearly reduces PID gains above a breakpoint (MC_TPA_BREAK_*) with the rate controlled by MC_TPA_RATE_* [46].

### 3.6 Derivative Filter Design and Notch Filters

**PX4 Derivative Filtering:** The IMU pipeline flows from gyro data through calibration, bias removal, notch filter, low-pass filter, then derivative through another LPF. The derivative term (D) is on the feedback path to avoid "derivative kick." The D-term is the most susceptible to noise because it inherently amplifies it [42].

**Filter Tuning Guidance:**
- IMU_GYRO_CUTOFF default is 30Hz (~8.0ms delay). Raising to 60Hz (~3.8ms) or 120Hz (~1.9ms) reduces latency but risks noise bleed-through. Increase in 10Hz steps
- IMU_DGYRO_CUTOFF (D-term filter) should be tuned separately, with the warning that the two values should not be set too far apart
- FPV racers push to ~120Hz, larger camera/research drones use ~80Hz
- "Do not try to fix a vehicle that suffers from high vibrations with filter tuning alone! Instead, fix the vehicle hardware setup first" [51]

**Large Drone Filter Recommendations:** For a 9kg quadcopter (85cm x 65cm) with vibrations between 50-60Hz: Set GYRO_CUTOFF to 20Hz (or 25Hz for a big drone), set DGYRO to 20Hz (or set D gains to 0, making DGYRO irrelevant), set ACCEL_CUTOFF to 20Hz. "I usually set the D gains to 0, as in my experience they only amplify noise for a 'big' drone like you have" [52].

**ArduPilot Harmonic Notch Filter Setup:** The goal with all filtering is to achieve enough attenuation to squash the noise but keep the delay as low as possible to improve the reaction to control inputs and turbulence. RPM data is always preferred over FFT for motor noise (more precise, less delay). FFT is useful for frame resonances not handled by RPM filters. Static or throttle-based notch filtering methods are not recommended as they are "very brittle filtering approaches" [53].

**PX4 Notch Filters:** Static notch filters can precision-strike narrow band noise. Dynamic notch filters (using ESC RPM telemetry or onboard FFT) track shifting vibration frequencies in real-time. "Without a notch filter, you would be forced to drastically lower the low-pass filter's cutoff frequency just to block that single sharp spike, which would horrifically increase the phase lag for the entire system" [51].

### 3.7 Practical First Flight Tuning Procedures

**PX4 Manual Tuning Procedure (12 steps):**
1. Arm vehicle, take off, and hover (typically in Position mode)
2. Open QGroundControl Vehicle Setup > PID Tuning
3. Select the Rate Controller tab
4. Confirm airmode selector is set to Disabled
5. Set Thrust curve to 0.3 (for PWM/power-based controllers) or 1 (for RPM-based ESCs)
6. Set Select Tuning radio button to Roll
7. Optionally enable Automatic Flight Mode Switching
8. Switch to Acro, Stabilized, or Altitude mode for rate controller tuning
9. Press Start to track setpoint and response curves
10. Rapidly move the roll stick full range and observe the step response
11. Adjust P/I/D sliders—increase P for responsiveness, increase D to dampen overshoots/oscillations, adjust I to reduce steady-state error
12. Repeat for pitch and yaw, then for the attitude controller, and finally the velocity/position controllers

**ArduPilot Tuning Flight Procedure:**
- Perform sharp wobbles on all three axes (roll, pitch, yaw) by rapidly moving sticks back and forth then returning to center
- Keep hold of the stick when returning to center (releasing it can cause false oscillation readings)
- Fly in stabilized mode or altitude hold
- Do small oscillations on each axis for 10-20 seconds per axis
- Download logs via Mission Planner and open in ArduPilot Web Tools PID Review
- **PD Balance Tuning**: If the actual peak is bigger than the target peak: too much P term (reduce P or increase D). If the target peak is bigger than the actual peak: too much D term (reduce D or increase P). Ideal: target and actual peaks are the same amplitude (actual slightly delayed is normal) [44].

---

## 4. Comparative Analysis of Enhancement Methods

### 4.1 Comprehensive Comparison Table

| Method | Computational Cost | Robustness | PX4/ArduPilot Native | Tuning Effort | Flight Validation | Key Limitation |
|--------|-------------------|------------|---------------------|---------------|-------------------|----------------|
| Fixed-Gain PID | Very Low | Poor | Yes (native) | Moderate-High | Extensive | Non-adaptive |
| Gain Scheduling | Low-Moderate | Good | No (companion computer) | High | Yes (AR.Drone, IRIS) | Requires extensive gain sets |
| Fuzzy PID | Moderate | Good | No (companion computer) | Moderate | Yes (multiple studies) | Rule base design effort |
| Neural Network PID | Moderate-High | High | No (companion computer) | High | Simulation only | Training data requirement |
| LPV/H∞ | Moderate-High | Very High | No (custom firmware) | Very High | Simulation only | High design complexity |
| Optimization-Tuned PID | Low (online) | Good | Yes (gains only) | Low (automated) | Yes (simulation + real) | Offline optimization |
| MRAC | Moderate | Good | No (companion computer) | High | Yes (simulation + some real) | Parameter drift risk |
| SMC-Augmented PID | Moderate | High | No (companion computer) | High | Yes (Parrot Mambo) | Chattering (mitigated by fuzzy) |
| Disturbance Observer PID | Moderate | High | No (companion computer) | Moderate-High | Yes (flight tests) | Observer design complexity |
| RL-Based PID Tuning | Low (inference) | Good | Emerging (Pixhawk) | Low (automated) | Yes (DDPG on Pixhawk) | Training convergence |

### 4.2 Detailed Comparative Analysis

**Fixed-Gain PID vs. Enhanced Methods:** PID controllers hold a 90-97% application share in UAV systems due to simplicity, low computational demand, and easy implementation on platforms like Arduino and Pixhawk. However, an Arduino-based prototype showed stabilization efficiency of 97% under minor disturbances but only 70-80% under strong wind. Lopez-Sanchez and Moreno-Valenzuela (2023) in their comprehensive survey (290 references, 275 citations) identified PID as the most common control approach in industrial and commercial mechatronics products due to its simplicity, intuitiveness, and efficiency, but concluded that "classical PID alone is insufficient for modern flight; the future lies in hybrid solutions integrating PID with fuzzy logic, machine learning, and predictive control" [54].

**Fuzzy PID vs. Traditional PID:** Dong (2023) compared traditional PID and fuzzy PID control systems. Traditional PID showed faster dynamic response initially but had 20% overshoot compared to fuzzy PID's 13% overshoot. Fuzzy PID had shorter regulation time (approximately 3s less). Under changing controlled object parameters, fuzzy PID demonstrated more stable performance with smaller fluctuation amplitude, less overshoot, and shorter adjustment time (7s vs 9s). Traditional PID advantages include low environmental requirements, simple concept, mature technology, and being less susceptible to changes in controlled object. Fuzzy PID advantages include effective suppression of initial overshoot, reduced computation, fast response, high accuracy, and good controllability. Fuzzy PID disadvantages include high requirements for control rules, imperfect system, and limited applicability [55].

**Optimization-Tuned PID vs. Enhanced Methods:** The key advantage of optimization-tuned PID is that the online computational cost is the same as standard PID (once gains are determined), making it directly implementable on PX4 and ArduPilot without firmware modification. The trade-off is that the optimization is performed offline, so the gains are fixed for a specific flight condition unless multiple gain sets are generated and scheduled. Metaheuristics (especially GWO) consistently improved performance over manual tuning, with the best-tuned controller maintaining accurate tracking while reducing oscillations, power demand, and acoustic emissions on unseen missions [34].

**LPV/H∞ vs. PID:** Kumar and Bhattacharya (2025) demonstrated that under severe wind disturbances (Dryden turbulence with gust velocities up to 15 m/s, generating disturbance moments up to 0.65 N-m), the PID controller showed peak attitude error of 30.54° and RMSE of 5.67°, while the H∞ controller achieved 7.12° peak error and 1.35° RMSE—nearly an order of magnitude improvement. However, the H∞ controller had 9 states versus 6 for the cascaded SISO PID baseline, and requires custom firmware implementation [15].

**Rinaldi et al. (2023) Comparative Study:** In a comparative study of PID, LQR, SMC, FL, and MPC for quadrotor attitude stabilization, SMC-based controllers were the most promising for attitude stabilization because they ensured the fastest dynamics, robustness to model uncertainties, and intermediate command effort. The PID-based stabilizer showed significantly slower dynamics and was not robust to model uncertainties, requiring extensive gain tuning. For tracking performance (sum of L2 norms of Euler angle errors), the ranking from best to worst was: SMC, LQR, FL, MPC, PID. For command effort (least to most): PID, MPC, SMC, LQR, FL [56].

**Implementation Complexity on PX4/ArduPilot:** Gain scheduling, fuzzy PID, neural network PID, LPV, MRAC, SMC-augmented PID, and disturbance observer methods are not natively supported in standard PX4 or ArduPilot firmware. They require companion computer integration (e.g., Raspberry Pi, Nvidia Jetson) communicating via MAVLink/MAVROS. The notable exception is optimization-tuned PID, where gains can be set via standard PID parameters without firmware modification. RL-based tuning is emerging as a promising approach, with Sönmez et al. (2025) validating a DDPG-based PD gain controller on a Pixhawk 2.1 Cube Black without requiring companion computers, achieving approximately 33% improvement in RMSE of attitude error norm compared to manual tuning [57].

---

## 5. Current State of the Art (2022-2026)

### 5.1 Reinforcement Learning-Based PID Gain Tuning

**DDPG-Based PD Gain Tuning (Sönmez et al., 2025, Drones):** Uses Deep Deterministic Policy Gradient (DDPG) algorithm—an off-policy actor–critic method—to adjust gains of a quadrotor attitude PD controller during flight. The RL agent neural network uses 128 neurons to balance performance against Pixhawk flash memory constraints. The RL-tuned controller achieved approximately 33% improvement in RMSE of attitude error norm compared to the manually tuned PD controller in outdoor flight tests. The agent learned to adapt gains dynamically in response to real-world disturbances such as wind gusts and ground effects, even though drag and gyroscopic effects were omitted during training. This study constitutes the first stage of a broader research effort investigating RL-based PID, LQR, MRAC, and Koopman-integrated RL-based PID controllers for real-time quadrotor control [57].

**DDPG Online Fine-Tuning (arXiv, Feb 2025):** An RL agent fine-tunes five inner-loop gains by outputting normalized weights within [-1,1] that adjust manually-tuned baseline gains. In numerical simulations, RMSE of attitude error norm improved from 12.75×10⁻³ to 11.17×10⁻³. In outdoor flight experiments, RMSE improved from 33.93×10⁻² to 22.55×10⁻². The 128×128 neuron neural network configuration balanced performance with Pixhawk memory constraints [58].

**Q-Learning PID Tuning (Alrubyli, 2022, Polimi Thesis):** A model-free Q-learning approach using a Sigmoid activation function to limit Q-table memory footprint (a 100×3 matrix, or 300 cells—500 fewer cells than comparable work). Three general actions (increase, decrease, or stay neutral) adjust all three PID gains simultaneously. Achieves altitude stabilization in under 30 seconds on average, with a median of ~53.8 seconds for a 1kg quadcopter. The Q-table converges in ~1000 episodes on average versus over 2000 in prior work. This contribution was nominated for the Best-Paper Award at IEEE ICMA 2022 [59].

**TD3 for PID Tuning (Ghazaryan, PyData Yerevan, Feb 2026):** An RL agent using the Twin Delayed DDPG (TD3) algorithm learns to adjust PID coefficients. The state includes tracking errors, position deviation, velocity, and acceleration components (9 components). The simulation environment (RLDroneSim) combines ArduPilot SITL, Gazebo physics engine, Gymnasium, and Stable-Baselines3, communicating via MAVLink protocol. Two approaches were explored: learning static gains for a specific environment, and adaptive control where PID coefficients change according to environmental changes (using a computational device like Raspberry Pi or Nvidia Jetson onboard) [60].

**Deep RL for Fixed-Wing Attitude Control (PPO, NTNU):** A PPO-based RL controller converges after approximately 2 million time steps (about 1 hour on a desktop i7-9700k/RTX 2070), with inference taking 800 microseconds (suitable for 100 Hz autopilot sampling). The most important factor was limiting the observation vector to essential variables (airspeed, roll/pitch angles, angular velocities, state errors) and including values from several previous time steps. The RL controller converged in more cases than PID (100% success in attitude states across all conditions) and was more robust to wind/turbulence disturbances, demonstrating generalization to unseen disturbances up to 23 m/s despite no wind during training [61].

### 5.2 Adaptive Control Integration Advances

**MPC-PID Hybrid with Transformer Attention (Zhou et al., 2026, Scientific Reports):** This represents a significant advance in hybrid control architectures. The upper layer uses MPC enhanced with H∞ robust performance criterion for receding-horizon predictive optimization (prediction horizon of 20, control horizon of 8, H∞ tuning factor of 1.5). The lower layer uses an adaptive PID controller with Transformer-architecture attention mechanism neural network (input feature vector 20-dimensional; embedding dimension 64; 3 encoder layers; 4 attention heads). A Sliding Mode Disturbance Observer (SMDOB) provides feedforward compensation. Results maintain steady-state tracking error within 5% during path-following tasks, improve steady-state robustness by about 17%, and shorten system adjustment time from 3.15s to 2.47s (21.6% improvement) [62].

**Adaptive Model-Based Gain-Scheduling PID (Cedro, 2024):** Controller gains are adjusted online in dependence on the quadcopter mass estimated via weighted recursive least squares. This approach directly addresses one of the main sources of UAV parameter uncertainty [63].

**All-True Composite Motion Modeling (Wang et al., 2024, Drones):** A novel approach to constructing nonlinear 6-DOF models for both quadrotor and dual-rotor coaxial UAVs based on "all-true composite motion"—reflecting actual mechanical structure and motion rather than simplified or linearized approximations. Fast and intelligent PID attitude–altitude controllers use self-optimizing algorithms (including adaptive simulated annealing) to dynamically adjust PID parameters. The proposed PID intelligent algorithm can effectively identify the optimal PID control parameters and improve control accuracy and efficiency [64].

### 5.3 Bio-Inspired and Metaheuristic Optimization Advances

**Grey Wolf Optimization (GWO) as Best Performer:** In the multi-objective optimization framework comparing metaheuristics, Bayesian Optimization, and DRL, GWO produced optimal results among all metaheuristics tested. The composite cost function weighted seven metrics: mission time, final position error, attitude/thrust oscillation, completion, overshoot, power consumption, and noise [34].

**Improved PSO with Adaptive Inertia Weight:** Cheng (2025) proposed an improved PSO algorithm integrating adaptive inertia weight, dynamic learning factors, and Latin hypercube sampling to enhance optimization efficiency and convergence. The cascade PID control structure with outer loop for attitude control and inner loop for angular velocity control showed improved settling time and reduced overshoot [65].

### 5.4 Higher-Order Sliding Mode Control on PX4 Architecture

**HOSM Control Implementation (Montemurro, 2021, Polimi Thesis):** A Higher-Order-Sliding-Mode (HOSM) controller with model linearization strategy was implemented on a quadcopter using PX4 architecture. The new HOSM control technique achieves better performance than the PX4 default PID controller, apart from an initial transient. Results were validated on slow and fast helical trajectories, showing improved tracking performance. This opens possibilities for future work involving further tests with different sliding mode algorithms and real-world applications [66].

### 5.5 Market Trends and Future Directions

The PID-based drone navigation market reached approximately $4.2 billion in 2022, with PID controller technology accounting for nearly 65% of this segment. The market is projected to grow at a CAGR of 18.3% through 2028, potentially expanding to $11.7 billion. Commercial applications represent 47% of demand, while military/defense accounts for 38% of revenue.

Key market challenges include:
- Linear PID control struggles with nonlinear drone dynamics during aggressive maneuvers or turbulence
- Parameter tuning remains complex due to the interdependence of P, I, and D gains
- Automated tuning often converges to local optima
- Computational constraints at control loop frequencies of 500Hz+
- Multi-axis coupling effects are often ignored

Energy efficiency considerations: high-gain PID parameters can increase power consumption up to 30%, while adaptive PID strategies show 15-20% energy savings. Comprehensively optimized PID systems can extend flight times by 15-40% [67].

The future direction points toward hybrid approaches combining classical PID with model predictive control (MPC) and robust control theory, with state estimation (Kalman filters, neural networks) playing an increasingly important role.

---

## Conclusion

The enhancement of PID-based attitude control for UAVs operating across diverse flight states requires a multi-faceted approach. For practitioners seeking practical improvements with minimal implementation complexity, the most accessible path begins with systematic optimization-based tuning (PSO, GA, or GWO) to find optimal fixed gains, followed by offline generation of multiple gain sets for different operating points and implementation of gain scheduling via a companion computer. For those seeking the best performance-to-implementation-effort ratio, fuzzy PID offers a well-documented middle ground with moderate computational requirements and demonstrated real-world flight validation.

For researchers and advanced developers, the current state of the art points toward hybrid architectures that combine classical PID with adaptive control techniques. Reinforcement learning-based PD gain tuning has been validated on Pixhawk hardware without companion computers, achieving 33% improvement in attitude tracking. The MPC-PID hybrid with Transformer attention represents the cutting edge, integrating prediction, learning, and disturbance compensation. LPV/H∞ approaches offer the strongest formal stability guarantees but require the highest design effort.

The fundamental insight from the literature is clear: no single enhancement method is universally optimal. The choice depends on the specific trade-offs between computational cost, robustness requirements, implementation complexity, and real-world validation status. The most promising direction for UAV attitude control is the integration of PID with adaptive, learning-based, and predictive methods in a way that leverages the simplicity and reliability of PID while overcoming its fundamental limitation of fixed-gain operation across varying flight conditions.

---

## Sources

[1] Gain Scheduled Attitude Control of Fixed-Wing UAV With Automatic Controller Tuning: https://ieeexplore.ieee.org/abstract/document/7973084

[2] Fuzzy Gain-Scheduling PID for UAV Position and Altitude Controllers: https://www.mdpi.com/1424-8220/22/6/2173

[3] A Gain Scheduling Attitude Controller With NN Supervisor for Quadrotor UAVs: https://link.springer.com/article/10.1007/s12555-024-0458-3

[4] Robust Fractional-Order Adaptive Gain-Scheduled Control Strategy for Civil UAV with LPV Models: https://www.cambridge.org/core/journals/aeronautical-journal/article/robust-fractionalorder-adaptive-gainscheduled-control-strategy-for-civil-unmanned-aerial-vehicle-with-lpv-models/14393CC50025842A4D9490C1074957B9

[5] Scheduling PID Attitude and Position Control Frequencies for Time-Optimal Quadrotor Waypoint Tracking: https://www.mdpi.com/1424-8220/22/1/150

[6] Self-Tuning PID Controller for Quadcopter using Fuzzy Logic: https://publisher.uthm.edu.my/ojs/index.php/ijrcs/article/view/1127

[7] Fuzzy PID Attitude Control for Cost-Effective Quadrotor UAVs: https://drpress.org/ojs/index.php/ajst/article/view/33317

[8] Adaptive fuzzy control of a quadrotor using disturbance observer: https://www.sciencedirect.com/science/article/abs/pii/S1270963822004588

[9] Model-Free RBF Neural Network Intelligent-PID Control Applying Adaptive Robust Term for Quadrotor System: https://www.mdpi.com/2504-446X/8/5/179

[10] The Application and Optimisation of a Neural Network PID Controller for Trajectory Tracking Using UAVs: https://www.mdpi.com/1424-8220/24/24/8072

[11] Quadrotor attitude control under perturbations with neural network and state observer: https://www.sciencedirect.com/science/article/pii/S2590123025043075

[12] Hybrid adaptive PID control strategy for UAVs using combined neural networks and fuzzy logic: https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0331036

[13] Linear, Parameter-Varying Control and Its Application to Aerospace Systems: https://www.icas.org/icas_archive/ICAS2002/PAPERS/541.PDF

[14] Observer-based LPV Control with Anti-Windup for Unmanned Aerobatic Aircraft: https://d-nb.info/1233734954/34

[15] Robust Attitude Control of Nonlinear Multi-Rotor Dynamics Using H∞ Control with LPV Models: https://arxiv.org/html/2510.00208v1

[16] A Modified Model Reference Adaptive Controller (M-MRAC) Using an Updated MIT-Rule for the Altitude of a UAV: https://www.mdpi.com/2079-9292/9/7/1104

[17] Decentralized Robust Direct MRAC for the Attitude of a Quadrotor UAV: https://www.intechopen.com/chapters/1179683

[18] A combined model reference adaptive control law for multirotor UAVs: https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/cth2.12137

[19] Adaptive PID Controller Using Sliding Mode Control Approaches for Quadrotor UAV Attitude and Position Stabilization: https://link.springer.com/article/10.1007/s13369-020-04742-w

[20] Adaptive PID Control via Sliding Mode for Position Tracking of Quadrotor MAV: Simulation and Real-Time Experiment Evaluation: https://www.mdpi.com/2226-4310/10/6/512

[21] Disturbance Observer-Enhanced Adaptive Fault-Tolerant Control of a Quadrotor UAV against Actuator Faults and Disturbances: https://www.mdpi.com/2504-446X/7/8/541

[22] Control of quadrotor UAV using variable disturbance observer-based strategy: https://www.sciencedirect.com/science/article/abs/pii/S0967066124001503

[23] Attitude Control of a Quadcopter UAV Using Sliding Mode Control with an Improved Extended State Observer: https://www.mdpi.com/2079-9292/14/22/4416

[24] Quadrotor's modeling and control system design based on PID control: https://iopscience.iop.org/article/10.1088/1742-6596/2483/1/012034

[25] PID Tuning via Classical Methods: https://eng.libretexts.org/Bookshelves/Industrial_and_Systems_Engineering/Chemical_Process_Dynamics_and_Controls_(Woolf)/09%3A_Proportional-Integral-Derivative_(PID)_Control/9.03%3A_PID_Tuning_via_Classical_Methods

[26] PID Controller Tuning Methods: Ziegler-Nichols, Cohen-Coon and Alternatives: https://industrialmonitordirect.com/blogs/knowledgebase/pid-controller-tuning-methods-ziegler-nichols-cohen-coon-and-alternatives

[27] PID Tuning help - Ziegler-Nichols method: https://community.simplefoc.com/t/pid-tuning-help-ziegler-nichols-method/747

[28] Research on Quadrotor Control Based on Genetic Algorithm and Particle Swarm Optimization for PID Tuning and Fuzzy Control-Based Linear Active Disturbance Rejection Control: https://www.mdpi.com/2079-9292/13/22/4386

[29] Tuning PID Controller for Quadrotor Using Particle Swarm Optimization: https://par.nsf.gov/servlets/purl/10615089

[30] Automatic PID Tuning via Differential Evolution for Quadrotor UAVs: https://ieeexplore.ieee.org/document/7850007

[31] Attitude control of a quadrotor using PID controller based on differential evolution algorithm: https://www.sciencedirect.com/science/article/abs/pii/S0957417423010205

[32] Study on PID gain parameter optimization for a quadcopter under static wind turbulence using bio-inspired algorithms: https://link.springer.com/article/10.1007/s44291-025-00049-y

[33] Tuning of cascade PID controller gains of quadcopter under bounded disturbances using metaheuristic based research algorithm: https://www.cambridge.org/core/journals/aeronautical-journal/article/tuning-of-cascade-pid-controller-gains-of-quadcopter-under-bounded-disturbances-using-metaheuristic-based-research-algorithm/A8CE601210ACADB2F8D99C827188D480

[34] Methods for Multi-objective Optimization PID Controller Tuning for Quadrotor UAVs: https://arxiv.org/html/2509.17423v1

[35] MIMO PID Controller Tuning Method for Quadrotor Based on LQR/LQG Theory: https://www.mdpi.com/2218-6581/8/2/36

[36] Self-tuning PID control design for quadrotor UAV based on adaptive pole placement control: https://ieeexplore.ieee.org/document/6775734

[37] Experimental study on cascaded attitude angle control of a multi-rotor unmanned aerial vehicle with the simple internal model control method: https://link.springer.com/article/10.1007/s12206-016-1035-3

[38] Loop Shaping-Based Attitude Controller Design and Flight Validation for a Fixed-Wing UAV: https://www.mdpi.com/2504-446X/9/10/697

[39] System Identification and Controller Optimization of a Quadrotor UAV: https://www.sjsu.edu/researchfoundation/docs/AHS_2015_Wei.pdf

[40] Quadrotor Drone System Identification via Model-Based Design and In-Flight Sine Wave Injections: http://www.ravvenlabs.com/uploads/1/1/8/4/118484574/quadrotor_drone_system_identification_via_model_based_design_and_in_flight_sine_wave_injections_posted.pdf

[41] System identification and H∞-based control of quadrotor attitude: https://www.sciencedirect.com/science/article/abs/pii/S0888327019305795

[42] PX4 Controller Diagrams: https://docs.px4.io/main/en/flight_stack/controller_diagrams

[43] ArduPilot Copter Attitude Control: https://ardupilot.org/dev/docs/apmcopter-programming-attitude-control-2.html

[44] ArduPilot Tuning Guide Part 3 - PIDs: https://www.youtube.com/watch?v=9laDDE3tv-g

[45] PX4 Multicopter PID Tuning Guide (Basic): https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter_basic

[46] PX4 Multicopter PID Tuning Guide (Advanced): https://docs.px4.io/main/en/config_mc/pid_tuning_guide_multicopter

[47] ArduPilot Helicopter Preparing for Tuning: https://ardupilot.org/copter/docs/traditional-helicopter-tuning-preparing.html

[48] PID Anti-windup Techniques: https://info.erdosmiller.com/blog/pid-anti-windup-techniques

[49] Understanding PID Anti-Windup: Back-Calculation Formula & Implementation: https://industrialmonitordirect.com/blogs/knowledgebase/pid-controller-anti-windup-back-calculation-formula-explained

[50] Anti-Windup in PID Control: Review, Analysis, and New Tuning Directions: https://arxiv.org/html/2606.01959v1

[51] PX4 Tuning Series 2 - Filter Tuning: https://quad-drone-lab.co.kr/px4-tuning-series-2-catching-hidden-vibrations-and-filter-tuning-finding-the-perfect-compromise-between-control-latency-and-noise

[52] PX4 Forum - When & How to set Notch and Low pass filters: https://discuss.px4.io/t/when-how-to-set-notch-and-low-pass-filters/43425

[53] Part 2 - Gyro Filters: Complete ArduPilot Tuning Guide: https://www.youtube.com/watch?v=qiA7bCsXBFg

[54] PID control of quadrotor UAVs: A survey: https://www.sciencedirect.com/science/article/abs/pii/S1367578823000640

[55] Performance comparison and analysis of traditional PID and fuzzy PID control systems: https://iopscience.iop.org/article/10.1088/1742-6596/2649/1/012001

[56] A Comparative Study for Control of Quadrotor UAVs: https://www.mdpi.com/2076-3417/13/6/3464

[57] Reinforcement Learning-Based PD Controller Gains for Quadrotor UAVs: https://www.mdpi.com/2504-446X/9/8/581

[58] Reinforcement Learning Based Prediction of PID Controller Gains for Quadrotor UAVs: https://arxiv.org/html/2502.04552v1

[59] Using Reinforcement Learning to Tune PID Controller for Quadcopter Altitude: https://www.politesi.polimi.it/retrieve/02dd0f6e-b715-45dd-9ffc-be38d6a74850/Thesis.pdf

[60] Adjusting PID Coefficients Using Reinforcement Learning for UAV Control: https://www.youtube.com/watch?v=5carh9XBnsY

[61] Deep Reinforcement Learning Attitude Control of Fixed-Wing UAVs: https://torarnj.folk.ntnu.no/eeb_ICUAS_Paper.pdf

[62] Robust performance optimization of UAV dynamic systems using MPC-PID hybrid control: https://www.nature.com/articles/s41598-025-32436-6

[63] Gain Scheduling Research Papers: https://www.academia.edu/Documents/in/Gain_Scheduling

[64] Fast and Intelligent PID Attitude Control of Quadrotor and Dual-Rotor Coaxial UAVs Based on All-True Composite Motion: https://www.mdpi.com/2504-446X/8/12/747

[65] Research on PID Control Parameter Tuning of Quadrotor UAV Based on Improved Intelligent Optimization Algorithm: http://pinnaclepubs.com/index.php/EJACI/article/view/363

[66] HOSM Control on PX4 Architecture: https://www.politesi.polimi.it/retrieve/7eba5e83-ad9c-4c0f-9322-355fda9096c1/TESI_HOSM_PX4_MONTEMURRO.pdf

[67] PID Controllers In Drone Flight Stabilization And Navigation: https://eureka.patsnap.com/report-pid-controllers-in-drone-flight-stabilization-and-navigation
