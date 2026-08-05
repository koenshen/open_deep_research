# Comprehensive and Accurate Situational Awareness of Space Targets in Cislunar Space: A Research Report

## Introduction

Cislunar space—the vast region extending from geosynchronous orbit (~36,000 km) to beyond the Moon's orbit (~385,000 km)—presents unique challenges for space situational awareness (SSA). Unlike the relatively well-understood two-body dynamics of low Earth orbit (LEO), cislunar trajectories are governed by the complex three-body gravitational interactions of the Earth-Moon-Sun system. The region is increasingly congested with both natural objects (asteroids, meteoroids) and artificial objects (active spacecraft, rocket bodies, debris), and the short-term tracking and monitoring of these objects (minutes to days) is critical for mission safety, collision avoidance, and national security.

This report synthesizes research from journal papers, conference proceedings, and official technical reports from NASA, ESA, the U.S. Space Force, and other organizations to provide a comprehensive overview of methods, technologies, and approaches for achieving comprehensive and accurate cislunar SSA. The report covers sensor types, orbital dynamics models, data fusion techniques, detection algorithms, and communication architectures, without assuming any particular solution.

---

## 1. Sensor Types and Detection Systems

### 1.1 Ground-Based Optical Telescopes

Ground-based optical telescopes are the most mature technology for cislunar object detection and tracking, offering high angular resolution and the ability to detect faint objects at great distances.

**GEODSS (Ground-Based Electro-Optical Deep Space Surveillance System):** Operated by the U.S. Space Force's Space Delta 2, GEODSS tracks man-made objects in deep space (10,000–45,000 km altitude). Each of its three operational sites (in the U.S. and Indo-Pacific) is equipped with three one-meter telescopes and digital cameras that can detect objects 10,000 times dimmer than the human eye and track objects as small as a basketball from over 20,000 miles away. The system manages data on approximately 25,000 known objects. GEODSS is being upgraded through the Ground Based Optical Sensor System (GBOSS) program to detect small, closely-spaced threats, with FY 2024 funding of $42.5M. [22][23][25][3]

**Space Surveillance Telescope (SST):** Developed by MIT Lincoln Laboratory under DARPA sponsorship, the SST features a compact 3.5-meter aperture, a wide field of view, and a mosaic of 12 CCDs. It can scan one-quarter of the sky multiple times nightly and detect objects as small as a softball. The system has a sensitivity of approximately 19.5 magnitude and processes up to 1 terabyte of image data per night. The SST is being relocated to Western Australia for joint U.S.-Australian operation. [24][68][26]

**Falcon Telescope Network (FTN):** Developed by the U.S. Air Force Academy, the FTN is a global network of 12 small-aperture (0.5-meter) robotic telescopes located across Colorado, Pennsylvania, Australia, Chile, and Germany. The FTN is undergoing a major upgrade with a new CMOS sensor, direct-drive mount, and multiple filter wheels, enabling simultaneous imaging of multiple resident space objects, slitless spectroscopy, and spectropolarimetry. [58]

**Limitations of Earth-Based Optical Sensors:** Research has shown that Earth-centered observers are largely inadequate for cislunar tracking. The median apparent magnitude of cislunar objects from Earth is about 20.5, falling below the observability limit of magnitude 18. Only about 30% of grid points were observable at all, with an average of about 10% of the time. [7][59][21]

### 1.2 Ground-Based Radar Systems

Radar systems offer all-weather, day/night operation and direct measurement of range and radial velocity, making them complementary to optical sensors.

**Deep Space Advanced Radar Capability (DARC):** The U.S. Space Force's DARC program is a next-generation ground-based radar system designed for 24/7 all-weather detection, tracking, and characterization of objects in deep space (GEO and beyond). DARC will consist of three globally dispersed sites (in the United States, United Kingdom, and Australia) with 27 parabolic antennas working together. The system offers higher sensitivity, accuracy, capacity, and agile tracking compared to current radars. DARC achieved Early Use capability for U.S. Space Command in September 2025 and is expected to be fully operational by 2027. The total cost for Site 1 is $844.6 million. [1][2][7][13][4][11][8]

**AN/FSY-3 Space Fence:** An S-band ground-based radar on Kwajalein Atoll, operational since March 2020, the Space Fence is the most sensitive radar in the Space Surveillance Network. It can detect objects as small as 5 cm in LEO and track an object the size of a beach ball at a range of more than 36,000 km. The system can track about 200,000 objects and make 1.5 million observations daily. [78][79][82][70][72]

**Goldstone Solar System Radar (GSSR):** JPL's GSSR uses a 70-meter antenna and 450 kW power for planetary radar observations. A JPL project developed the Cis-lunar Space Debris Radar (CSDR), with a goal to detect 1-meter or smaller targets at lunar distances. Techniques investigated include a polyphase filter bank (PFB) and polarimetric observables (Stokes parameters), achieving up to 139.5% improvement in SNR for Chandrayaan-1 detection. [36][34]

**LeoLabs Commercial Radar Network:** LeoLabs operates a global network of 11 radars across seven sites, tracking over 25,000 objects. Their radar systems include Scout-S (transportable S-band), SEEKER (UHF, capable of tracking in MEO/GEO/cislunar), and RANGER (scalable S-band). The Kiwi Space Radar in New Zealand tracks objects down to -34 dBsm (roughly 2 cm size). [27][30][31][34][29]

### 1.3 Space-Based Sensors

Space-based sensors overcome the atmospheric and light limitations of ground-based systems, providing persistent coverage from vantage points in Earth orbit or cislunar space.

**GSSAP (Geosynchronous Space Situational Awareness Program):** The U.S. Space Force's GSSAP constellation operates in near-geosynchronous orbit (~22,300 miles altitude), carrying EO/IR sensors. The satellites are maneuverable, allowing them to drift above and below the GEO belt to collect intelligence on specific target satellites. The constellation has grown to six satellites, with a fourth pair (GSSAP 9 & 10) scheduled for 2027. [20][22][31][35]

**SBSS (Space Based Space Surveillance):** A planned U.S. Space Force constellation, the pathfinder satellite SBSS 1 (launched 2010) carries a 30 cm telescope on a two-axis gimbal with a 2.4 megapixel sensor, designed to survey every geosynchronous orbit spacecraft at least once daily. [33][26][36]

**Silent Barker:** A classified space-based SSA system with three satellites launched in September 2023, positioned above GEO. It is focused on wide area surveillance, with expansion to full operational capability by FY 2027. [3][70]

**AFRL Oracle Family of Systems:** The Oracle-M (Mobility) pathfinder satellite demonstrates cislunar operations and high mobility while tracking known objects. The Oracle-P (Prime) is a purpose-built SSA experiment designed to search for unknown/lost objects and maintain custody of known objects, using a wide-field sensor and a more sensitive narrow-field sensor. Oracle-P will operate in Earth-Moon L1 orbit (~326,400 km from Earth). [58][59][62][60]

**CHPS (Cislunar Highway Patrol System):** An AFRL spacecraft launching in 2025 to operate in a gravitational stability zone between Earth and the Moon, at distances up to 385,000 km. CHPS will use wide-field and narrow-field sensors, along with novel onboard image processing and orbit determination software, to detect, track, and identify artificial objects in cislunar space. [1][2][5][7]

**Space-Based Sensors at L4/L5:** Research suggests monitoring the Earth-Moon corridor from two opposing vantage points at the L4 and L5 Lagrange points. A 35 cm aperture telescope with diffraction-limited resolution can achieve robust detection of a 1-meter object at ~384,400 km range. Triangulation between two sensors at L4 and L5 provides three-dimensional positioning. [12][38]

**Moon-Based Sensor Architectures:** Research demonstrates that a Moon-based sensor architecture, consisting of four mid-latitude narrow field of view angles-only observers, can maintain 100% track custody with average position RSS error below 1 km against all cislunar targets. A single lunar south-pole station observes ~40% of the cislunar grid, with all visible points above 50% time. [41][49][7][59]

### 1.4 Laser Ranging and Lidar Systems

**Satellite Laser Ranging (SLR):** SLR achieves few-millimeter precision on satellites with corner cube retroreflectors (e.g., LAGEOS). For debris without retro-reflectors, precision degrades to about 1 meter. The Space Optical Laser Tracking (SOLT) system in Korea integrates SLR, adaptive optics, and debris laser tracking, achieving single-shot precision of 3.6 mm for ground targets and 7.1 mm for Lageos-2. [41][46][39][30][48]

**Lunar Laser Ranging (LLR):** LLR measures the distance between Earth and the Moon using laser pulses reflected off retroreflectors placed on the Moon. Modern measurements achieve millimeter precision. The Next Generation Lunar Retroreflector (NGLR-1) was successfully delivered to the Moon on March 2, 2025, and is designed for sub-millimeter range accuracy. [40][45]

### 1.5 Emerging Sensor Technologies

**Fast X-ray Transform (FaXT) Track-Before-Detect:** A novel dynamic-programming track-before-detect algorithm capable of detecting objects ten times fainter than previous methods in asteroid searches. The project will demonstrate the technique by tracking the CAPSTONE CubeSat in lunar orbit. [1][42]

**Passive RF Detection:** The CSIRO Mopra 22m Radio Telescope in Australia has detected RF emissions from lunar spacecraft at X and S band, confirming detection of signals from CAPSTONE and other spacecraft. Passive RF methods are beneficial as the object itself transmits signals, requiring only a receiver. [48][24]

**DARPA TBD2 (Track at Big Distances with Track-Before-Detect):** Aims to enable continuous space-based detection and tracking of objects in cislunar space on relevant timelines (within hours), using advanced signal processing algorithms paired with commercial optical sensors. [3][12]

**Clavius-S (Astrobotic Lunar Surface Sensor):** A visible-band imaging sensor that detects and tracks spacecraft in low lunar orbit from the Moon's surface, leveraging proximity to orbit, reduced glare, and a stable platform. [3]

---

## 2. Orbital Dynamics Models

### 2.1 The Circular Restricted Three-Body Problem (CR3BP)

The CR3BP is the fundamental dynamical model for cislunar space. It assumes two primary masses (Earth and Moon) in a circular orbit around their common barycenter and a tertiary mass of negligible size. As Dr. Shane Ross (Virginia Tech) explains: "Beyond GEO, spacecraft dynamics stop following the familiar two-body Keplerian rules — orbital motion in cislunar space (xGEO) is governed by the restricted three-body problem instead, with the Earth and Moon pulling simultaneously." [26][13]

Key characteristics of the CR3BP include:
- **No general closed-form analytical solution exists**; numerical integration is required. [26]
- **The Jacobi constant** is a conserved quantity, constraining a spacecraft's orbital elements. [13]
- **Five Lagrange points**: L1, L2, L3 (collinear, unstable) and L4, L5 (triangular, stable in the Earth-Moon system). [13]
- **Zero-velocity surfaces** define realms of possible motion, with five energy cases controlling transfer routes via "necks" at L1/L2/L3. [13]

The CR3BP is used extensively for preliminary trajectory design, orbit family characterization, and as an initial guess for higher-fidelity models. The NASA Technical Publication "Astrodynamics Convention and Modeling Reference for Lunar, Cislunar, and Libration Point Orbits" (NASA/TP-20220014814) provides a foundational summary. [64]

### 2.2 Ephemeris Models (High-Fidelity Propagation)

**NASA SPICE and JPL Ephemerides:** The paper "Initial Orbit Determination from Ephemeris Models" (ADS, 2025) combines high-fidelity planetary ephemeris models (NASA SPICE) with collocation-based nonlinear programming, developing an ephemeris-derived rotating frame dynamics model that avoids planar or circular assumptions. [2] The most recent JPL Development Ephemeris files (DE440 and DE441) calculate the location of the solar system barycenter using the Sun, eight planetary systems, the Pluto system, 343 asteroids, 30 KBOs, and a KBO ring. [20]

**The Bicircular Restricted Four-Body Problem (BCR4BP):** The BCR4BP incorporates solar gravity as an intermediate step between the CR3BP and full ephemeris models. This is critical for certain orbits, such as the 3:1 synodic resonant NRHO, whose geometry is not preserved in a direct CR3BP-to-ephemeris transition. [39]

**The HALO Propagation Tool:** An open-source, high-precision orbit propagation tool for mission design in the cis-lunar domain. HALO models high-fidelity ephemeris forces including lunar gravitational field (spherical harmonics up to high degree), lunar solid tides, point-mass attractions (Earth, Sun, Jupiter, Venus), Earth gravitational field, general relativistic corrections, and solar radiation pressure with eclipse modeling. [35]

### 2.3 Perturbation Modeling

**Earth Oblateness (J2 Effects):** The paper "The Resonant Structure of xGEO and Implications for Space Domain Awareness" (Rosengren et al., AMOS 2024) defines xGEO by the Laplace radius, where lunisolar perturbations dominate Earth oblateness. The study combines perturbed-Hamiltonian formulations with global geometric techniques to investigate secular resonances driven by von Zeipel-Lidov-Kozai dynamics, lunar mean-motion, and precession interactions. [41]

**Solar Gravity (Third-Body Effects):** The comparison between CR3BP and BCR4BP shows that the Sun's gravitational perturbation is significant for Earth-Moon transfers, with relative perturbation of at least 1/10 for any Earth-Moon trajectory when the Sun is at 0° or 180°. [32]

**Solar Radiation Pressure (SRP):** SRP is an important non-conservative perturbation for cislunar objects, particularly for spacecraft with large area-to-mass ratios. The paper "Cislunar Orbit Determination and Tracking via Simulated Optical Measurements" includes SRP scale factor estimation in its filter. [50]

**Lunar Gravity Field:** The Moon's complex gravity field, including mascons (mass concentrations), requires high-degree gravity models (e.g., LP165P from GRAIL) for accurate long-term prediction. The paper "Long-Term Dynamics and Special Solutions of Lunar Orbiters" (Patel, UC San Diego, 2022) notes that simplified models like J2+C22 can only approximate low-altitude dynamics. [49]

### 2.4 Numerical Integration Methods

**Runge-Kutta Methods:** The 4th-order Runge-Kutta (RK4) is the most common general-purpose integrator. Higher-order methods like Dormand-Prince (DP8(7) and DP5(4)) are used for greater accuracy. [13][9]

**Symplectic Integrators:** Symplectic integrators preserve the symplectic 2-form and conserve a slightly perturbed Hamiltonian, enabling long-term simulations of chaotic systems. The Störmer-Verlet method is 2nd-order and symplectic. For the Kepler problem, the leapfrog method shows superior long-term behavior even with large timesteps. [2][1][14]

**Adaptive-Picard-Chebyshev (APC):** A study comparing six numerical integrators found that APC generally outperforms other methods across all test cases, requiring the fewest function evaluations to achieve a specified accuracy, especially for highly eccentric orbits. [9]

**Taylor Series Methods:** High-order Taylor series methods are competitive for high-precision computations, though the Hamiltonian may grow linearly with time. [7]

### 2.5 Analytical and Semi-Analytical Propagation Methods

**The STORM Propagator:** A semi-analytical propagation code that uses averaging of short-period terms to propagate mean equinoctial elements, enabling large time-steps (hours to days) and efficient computation over decades. STORM accounts for gravitational perturbations, third-body effects, atmospheric drag, and solar radiation pressure. [39][42]

**The DSST (Draper Semi-analytical Satellite Theory):** DSST outperforms analytical theories, achieving position errors around 250 m with runtime about 10% of numerical methods. [40]

**The Modified Generalized Equinoctial Orbital Elements (M-GEqOEs):** Presented in a 2025 AAS paper, the M-GEqOEs extend the Generalized Equinoctial Orbital Elements to handle trajectories with non-negative total energy, enabling robust modeling under Earth-Moon-Sun gravitational perturbations. Uncertainty propagation assessment shows that the M-GEqOE representation preserves Gaussian behavior longer than Cartesian coordinates, especially at highly nonlinear regions like perilune or perigee passes. [25]

### 2.6 Manifold Dynamics and Trajectory Prediction

**Space Manifold Dynamics (SMD):** The core model is the CR3BP, focusing on the collinear Lagrange points L1, L2, and L3. These points exhibit centre × centre × saddle stability, giving rise to families of periodic orbits (Lyapunov and halo orbits) and quasi-periodic Lissajous orbits. The saddle component introduces hyperbolic invariant manifolds (stable and unstable tubes) that govern transport between regions of motion. [9]

**Application to SSA:** The paper "Monitoring and tracking accessible invariant manifolds in cislunar space" (Wright et al., AMOS 2023) investigates using invariant manifolds to reduce search volumes for SDA. By clipping in the Z-direction (height), the search volume at 4xGEO can be reduced by 46% while still detecting over 94% of crossings. Using Poincaré maps at planes near L1 captures over 80% of free-trajectory traffic. [5]

### 2.7 Uncertainty Propagation

**Gaussian Mixture Models (GMMs) with State Transition Tensors (STTs):** The PhD thesis by Yashica Khatri (University of Colorado) presents a semi-analytical method for nonlinear uncertainty propagation that combines GMMs with higher-order STTs. The method splits an initial distribution into GMM components, maps each component via STTs computed using advanced dynamical models, and then recombines to capture non-Gaussian evolution. Test cases in various dynamical regimes show that the semi-analytical method achieves statistical accuracy comparable to Monte Carlo analysis while significantly reducing computation time. [21][47]

**Bayesian Adaptive Gaussian Mixture Filter:** A filter for angles-only cislunar space object tracking that represents the state probability density function as a Gaussian mixture and uses recursive Gaussian splitting to handle non-Gaussianity from nonlinear dynamics, nonlinear measurements, state-dependent probability of detection, and nonlinear constraints (e.g., Jacobi constant bounds). The filter maintains consistency and achieves position accuracy within ~10 km and velocity within ~1 m/s during visibility. [53][57]

---

## 3. Data Fusion and Tracking Algorithms

### 3.1 Multi-Sensor Data Fusion Architectures

Multi-sensor data fusion architectures are classified into three types: **centralized** (all processing at fusion center, accurate tracking but high communication burden), **distributed** (local processing per sensor with fusion of local tracks, more adaptable), and **hybrid** (combination of centralized and distributed). [2][56]

**Covariance Intersection (CI) and Track-to-Track Fusion:** The CI algorithm from Julier and Uhlmann is a popular algorithm for track-to-track fusion, relying on the Chernoff fusion rule. A novel method called Maximum Allocated Covariance (MAC) guarantees that the fused estimate is unbiased, less conservative than CI, and conservative relative to the optimal fusion with known cross-covariance. Monte Carlo simulations show that MAC achieves lower total RMSE and determinant of covariance than CI and Inverse Covariance Intersection (ICI). [58][56]

**Fusion of Optical and RF Data:** A 2023 AMOS conference paper extends prior work on cislunar IOD and tracking by incorporating passive RF observations into a probabilistic framework. The study compares optical-only, passive RF-only, and fused optical+RF data, evaluating performance improvements from adding RF data, focusing on Time Delay of Arrival (TDOA) and Doppler measurements. [17][22][24][55]

**Cislunar Message Set for Data Sharing:** The Cis-Lunar SSA Technical Steering Group (November 2021) proposed a new message set based on the CCSDS Orbit Data Message (ODM) standards, particularly the Orbit Comprehensive Message (OCM). Key recommendations include representing trajectories as ephemerides suitable for interpolation, requiring formal covariances in Cartesian representation with a mandatory Cholesky factor, and adopting a tracking data message that includes formation covariance and satellite signature data. [58][53]

### 3.2 Estimation and Filtering Algorithms

**Extended Kalman Filters (EKF) and Unscented Kalman Filters (UKF):** The Concurrent Optimization of Satellite Phasing and Tasking for Cislunar SSA (2025) uses the CR3BP dynamics and an EKF for information propagation and state estimation. [4][78][81] The Adaptive Sensor Tasking Strategies for Tracking Non-Cooperative Cislunar Space Objects (AMOS 2024) uses an EKF to process angles-only passive optical observations, with a total of 145 observations scheduled throughout a 48-hour planning horizon. [69][68]

**Particle Gaussian Mixture Filter (PGMF):** The PGMF combines the best of particle filtering (propagation step) and the Gaussian Mixture Model form of the UKF (nonlinear update step). The PAR-PGMF technique can initialize on as few as a single optical observation, accounts for complex uncertainty bifurcations, and can process multi-modal uncertainty distributions. [16][22][55]

**Hybrid Particle Gaussian Mixture (PGM) Filter:** A hybrid PGM filtering method for cislunar target tracking addresses the limitations of Gauss's method in the three-body cislunar domain. The approach combines PGM-I and PGM-II filters: PGM-II (using MCMC sampling) is applied for the first few measurement updates to handle extreme initial uncertainty, then switches to the computationally lighter PGM-I filter. Tested on a 9:2 resonant NRHO, the hybrid filter achieves up to 100-fold better localization compared to the existing Kinematic Fitting PGM framework. [36]

**Batch Least-Squares Estimation:** A sensitivity analysis of cis-lunar orbit determination (AAS 22-022) uses a nonlinear least squares batch estimator with range and range-rate measurements from Earth-based sites. The dynamic model includes gravitational perturbations from Earth, Sun, and Moon (GRAIL660B model, 160x160 order). Results show that for low a priori uncertainty, measurement variation drives observability, with optimal observation epochs at ~6 and 12 hours. [24][32][52]

### 3.3 Initial Orbit Determination (IOD) Methods

**Probabilistic Admissible Region (PAR):** Originally developed for near-Earth orbits, the PAR has been extended to the cislunar domain, enabling initialization from as few as one short-arc observation (angles and photometric brightness). The PAR generates a particle cloud representing multi-modal orbital uncertainty by sampling observed angles, light intensity, and hypothesized parameters (albedo-area product, angle rates, Jacobi constant). [16]

**Constrained Admissible Region Multiple Hypothesis Filter (CAR-MHF):** CAR-MHF extends IOD to the cislunar regime using a constrained admissible region to bound the orbit search space from short-arc angles-only measurements. It achieved a 100% data utilization rate in both test cases, with all observations correctly associated to distinct estimates. Critical revisit timelines are measured in hours and are mostly driven by the profound radial uncertainties experienced with observations of cislunar objects. [21]

**Machine Classifier for Cislunar Orbit Determination (MCCLOD):** A neural network that maps angles-only observations to a two-parameter encoding representing a point on a known periodic orbit family. Regression-only models achieve sub-100 km position errors (median ~20-50 km per family). In simulated tracking scenarios, MCCLOD consistently outperforms Gooding's method, reducing position error ranges by an order of magnitude. [12][20][35]

**Collocation and Nonlinear Programming IOD:** A novel IOD algorithm for cislunar objects with unknown maneuvers uses collocation (Hermite-Simpson transcription) and nonlinear programming to implicitly integrate system dynamics. The algorithm handles both continuous low-thrust and impulsive maneuvers, converges from a poor initial guess (e.g., a Lagrange point), and achieves CPU times under 0.5 seconds for the low-thrust case. [14][39]

**Physics-Informed Neural Networks (PINNs):** Physics-Informed Orbit Determination (PIOD) uses PINNs to estimate the state of non-cooperative objects from passive angle-only observations, requiring no initial guess or integration. Tested on real observations of the Chang'e 5 T1 booster, the method achieved position error <4.5 km and velocity error <2 cm/s, allowing accurate propagation for nearly a month. [31][34]

### 3.4 Association and Correlation Algorithms

**Multiple Hypothesis Tracking (MHT):** The CAR-MHF uses a multi-hypothesis joint probabilistic data association (MH-JPDA) framework to handle multi-target confusion, and an iterative filter-smoother refines estimates and graduates objects. [21]

**Labeled Multi-Bernoulli (LMB) and Generalized Labeled Multi-Bernoulli (GLMB) Filters:** The LMB filter provides a means for tracking multiple space objects while maintaining target identity. In a simulated scenario with seven near-geosynchronous targets, the filter correctly maintains track labels and converges to position errors less than 1 km. [29] The GLMB filter with kernel-based ensemble Gaussian mixture filter achieves accurate state estimates and zero cardinality error for tracking 10 GEO objects with sparse measurement passes. [32]

**Track-to-Track Correlation with Optimal Control:** A method for cislunar optical track-to-track correlation uses a minimum-energy optimal control problem with transversality conditions, avoiding the need for an admissible region or strong dynamic assumptions. The method links two optical uncorrelated tracks by minimizing thrust energy under the CR3BP dynamics, successfully correlating UCTs without detecting false manoeuvres. [50]

### 3.5 Detection Algorithms for Dim, Small, and Fast-Moving Objects

**Quadratic Shift-and-Stack (QSS):** A method for ground-based optical detection of faint cislunar objects that addresses the challenge that traditional linear shift-and-stack fails because cislunar objects exhibit significant angular acceleration. Simulations on four representative cislunar orbits show that QSS significantly improves stacking efficiency and SNR, with overall mean stacking efficiency rising from 0.2873 (linear) to 0.7480 (QSS). Real observations of the cislunar object Tiandu-1 confirmed that QSS achieves continuous SNR improvement to 21.98 after 46 minutes—a 31% improvement over linear stacking. [33][20][22]

**Motion Hypothesis Satellite Detection:** A method for automatically detecting unknown or lost cislunar spacecraft using ground-based optical telescopes adapts an asteroid detection algorithm. The algorithm applies motion hypothesis shifting, median stacking, background subtraction, and clustering to extract targets without prior ephemeris. Real targets including Queqiao-2, Orion, Lucy, and Luna-25 Fregat were all successfully detected. The algorithm runs in minutes and works with sidereal tracking mode. [55][54][26]

**Track-Before-Detect (TBD) Algorithms:** The Fast X-ray Transform (FaXT) is a dynamic-programming TBD algorithm capable of identifying extremely faint objects with minimal prior knowledge, achieving substantial runtime improvements. The method has been demonstrated in large-scale asteroid searches, detecting objects up to ten times fainter than previously possible. [5][82]

**Deep Reinforcement Learning for Sensor Tasking:** A DRL agent using a CNN architecture (actor-critic with proximal policy optimization and population-based training) has been developed to optimally task a narrow field of view ground-based optical telescope for cislunar SSA. The DRL agent significantly outperforms random policies, achieving lower final mean trace covariance and observing more unique RSOs over a two-hour observation window. [17][22]

---

## 4. Communication Architectures

### 4.1 Cislunar Communication Challenges

One-way light-time delay from Earth to the Moon is approximately 1.282 seconds (average), resulting in a round-trip communication delay of approximately 2.56 seconds. [5][7] This latency, combined with signal attenuation over vast distances, data rate limitations, and regulatory constraints, poses significant challenges for real-time tracking data transmission. [2][4]

Technical challenges include data rate limitations, limited bandwidth, antenna design, security (requiring delay/disruption-tolerant networking), and space weather. Regulatory hurdles are significant: current ITU Radio Regulations lack specific provisions for cislunar communications, forcing reliance on existing Space Research, Inter-Satellite, and Space Operations allocations. WRC-27 Agenda Item 1.15 will study possible new spectrum allocations between 300 MHz and 28 GHz for lunar surface and orbit communications. [1]

### 4.2 NASA's Space Communications and Navigation (SCaN) Lunar Architecture

NASA's SCaN program is developing a support structure of networks, partners, and technologies to provide communication, position, navigation, and timing services at the Moon. Key elements include: [15]

- **Orion Artemis II Optical Communications System (O2O):** Provides 80–260 Mbps downlink and 20 Mbps uplink via laser communications.
- **Lunar Exploration Ground Sites (LEGS):** Three 18-meter antennas at White Sands (New Mexico), South Africa, and Australia to augment Direct-to-Earth capacity.
- **Deep Space Network (DSN) Upgrades:** The DLEU project and new antennas (DAEP) are being developed to handle increased cislunar demand.
- **Surface Connectivity:** Using 4G/LTE/3GPP standards, with Nokia's network on Intuitive Machines' IM-2 mission (2025).
- **Cislunar Relay Services:** Via commercial procurement (LCRNS) and international contributions (ESA's Moonlight, JAXA).
- **LunaNet Interoperability Specification (LNIS):** A collaborative standards framework.

### 4.3 Data Formats and Standards

**CCSDS Orbit Data Messages (ODM):** CCSDS 502.0-B-3 (April 2023) defines four standard message formats: Orbit Parameter Message (OPM), Orbit Mean-Elements Message (OMM), Orbit Ephemeris Message (OEM), and Orbit Comprehensive Message (OCM). OCM is a flexible format designed to succeed OEM as the universal standard for ephemeris data exchange. [4]

**Conjunction Data Message (CDM):** The CCSDS CDM standard (CCSDS 508.0-B-1) specifies a standard message format for exchanging spacecraft conjunction information, including positions, velocities, covariances at Time of Closest Approach, relative motion data, and metadata. [3][11]

**Traffic Coordination System for Space (TraCSS):** The TraCSS CDM is based on the CCSDS standard with modifications for enhanced SSA, including fields for Mahalanobis distance, maximum collision probability, and dilution status. [1][9]

### 4.4 Multi-Sensor Data Networking and Fusion Center Architectures

**Unified Data Library (UDL):** The UDL is a cloud-based data repository for space domain awareness, described as the data layer for U.S. Space Force operational SSA. It combines data from a variety of different satellites, both commercial and military, centralizing it in one location. [22][34][33][31][29] However, a GAO report (GAO-23-105565, April 2023) found that the Space Force faces challenges in integrating the UDL into SSA operations. [24]

**Commercial Data Fusion:** ExoAnalytic Solutions' Global Telescope Network (EGTN) provides real-time latency of 15-30 seconds for astrometric and photometric data, with observation data volume roughly three times that delivered by existing Air Force electro-optical sensors. [27][21] a.i. solutions' SensorQC platform evaluates the quality of commercial space surveillance data, processing more than 3.6 million sensor observations from over 400 optical, radar, passive RF, and passive radar sensors across 18 commercial sensor networks. [30]

---

## 5. Current Programs, Missions, and Initiatives

### 5.1 U.S. Space Force / Space Command Programs

**Cislunar Coordination Office (April 2026):** On April 15, 2026, the U.S. Space Force announced the creation of a Cislunar Coordination Office, an acquisition task force to study how the Defense Department will operate in cislunar space in support of a planned NASA moon base. The initiative stems from President Trump's December 2025 Executive Order on space superiority, which mandates initial elements of a permanent lunar outpost by 2030. [13]

**DARC (Deep Space Advanced Radar Capability):** As detailed in Section 1.2, DARC is a ground-based radar system for 24/7 all-weather detection of objects in deep space. Construction of Site 1 in Exmouth, Western Australia, was completed in December 2024. DARC achieved Early Use capability for U.S. Space Command in September 2025. Full operational capability is expected in 2027. [32][36][42]

**Oracle Family of Systems:** As detailed in Section 1.3, the Oracle-M and Oracle-P satellites are AFRL programs demonstrating cislunar operations and SSA capabilities. Oracle-P will operate in Earth-Moon L1 orbit. [58][59][62][60]

**CHPS (Cislunar Highway Patrol System):** As detailed in Section 1.3, CHPS is an AFRL spacecraft launching in 2025 to detect, track, and identify artificial objects in cislunar space, operating at distances up to 385,000 km. [1][2][5][7]

### 5.2 NASA Programs

**Artemis Program:** As of August 2026, Artemis II has launched (April 1, 2026) with a crew of four, breaking the record for greatest human distance from Earth (252,756 miles). Artemis III is scheduled for 2027, and Artemis IV for early 2028. [39][43][47][49]

**National Cislunar Science & Technology Action Plan (December 2024):** Published by the National Science and Technology Council, this plan outlines five-year actions for U.S. federal agencies to advance cislunar space leadership. It addresses four strategic objectives: supporting R&D, expanding international cooperation, extending SSA capabilities into cislunar space, and implementing scalable, interoperable communications and PNT capabilities. [12]

**CAPSTONE Mission:** Advanced Space shared data from its CAPSTONE cubesat mission with AFRL to test a near rectilinear halo orbit for NASA's Gateway station, addressing challenges of three-body orbit determination. [34]

### 5.3 International Programs

**ESA Moonlight:** ESA's Moonlight program is developing a lunar communication and navigation service. ESA has committed to LunaNet for its Moonlight system, with a joint interoperability test planned for 2029. [2][10]

**ESA LUMOS (Lunar Monitoring System):** An ESA Phase A study of a satellite dedicated to the observation and characterization of objects orbiting the Moon, including active and non-operational satellites, spent launch stages, and other space debris. [43]

**JAXA LNSS:** JAXA has committed to LunaNet for its Lunar Navigation Satellite System. [10]

### 5.4 Commercial Capabilities

**ExoAnalytic Solutions:** The Global Telescope Network (EGTN) provides real-time latency of 15-30 seconds for astrometric and photometric data, with sensitivity down to ~10 cm at GEO. The network monitors high-altitude orbits with 18+ hours of daily persistence. [27]

**LeoLabs:** Achieved record bookings in 2025, exceeding $60M in total contract awards. The company licenses its Object Catalog to the U.S. Department of Commerce and U.S. Space Force, tracking over 25,000 objects. [34]

**Rocket Lab Heimdall Payload:** Rocket Lab secured a $90 million contract from the U.S. Space Force to design, build, integrate, and operate two geostationary satellites hosting the Heimdall space domain awareness payload. [37]

**University of Arizona Space4 Center:** Offers capabilities in optical, IR, and passive RF sensing, AI-powered analytics, and cislunar object cataloging. The center identified a Chinese rocket booster that hit the Moon, created a spectral signature database, and leads a $7.5M AFRL cislunar tracking project. [62]

---

## 6. Conclusion

Comprehensive and accurate situational awareness of space targets in cislunar space requires an integrated, multi-domain approach that leverages the strengths of diverse sensor types, sophisticated orbital dynamics models, advanced data fusion and tracking algorithms, and robust communication architectures.

**Sensor diversity is essential.** No single sensor type can provide complete coverage. Ground-based optical telescopes (GEODSS, SST, Falcon Telescope Network) offer high angular resolution but are limited by weather, daylight, and the faintness of cislunar objects. Ground-based radars (DARC, Space Fence, Goldstone) provide all-weather, day/night operation and direct range measurements but are limited in sensitivity for small objects at lunar distances. Space-based sensors (GSSAP, SBSS, Silent Barker, Oracle, CHPS) overcome atmospheric limitations but are expensive and have limited coverage. Emerging technologies such as Moon-based sensors, laser ranging, passive RF detection, and track-before-detect algorithms (FaXT, TBD2) offer promising new capabilities.

**Accurate orbital dynamics models are critical.** The CR3BP provides the foundational framework for cislunar trajectory prediction, but high-fidelity ephemeris models (JPL DE, SPICE, HALO) are necessary for operational accuracy. Perturbation modeling (J2, SRP, solar gravity, lunar gravity field) must be included, and advanced numerical integration methods (symplectic integrators, APC) are needed for long-term propagation. Semi-analytical methods (STORM, DSST, M-GEqOEs) offer computational efficiency for large-scale catalog maintenance. Manifold dynamics can reduce search volumes by identifying high-probability transit corridors.

**Advanced data fusion and tracking algorithms are required.** The unique challenges of cislunar tracking—extreme distances, nonlinear dynamics, sparse observations, and multi-modal uncertainty—demand sophisticated estimation methods. The Probabilistic Admissible Region (PAR) and Constrained Admissible Region Multiple Hypothesis Filter (CAR-MHF) enable initialization from minimal observations. Particle Gaussian Mixture Filters (PGMF) and hybrid PGM filters handle nonlinear, non-Gaussian state distributions. Machine learning approaches (MCCLOD, PINNs) offer rapid, accurate IOD without requiring close initial guesses. Track-before-detect algorithms (FaXT) and quadratic shift-and-stack (QSS) improve detection of faint objects. Multi-sensor fusion architectures (centralized, distributed, hybrid) and data sharing standards (CCSDS ODM, CDM, TraCSS) enable coordination across diverse sensor networks.

**Communication architectures must support real-time data transmission.** The ~1.3-second one-way latency between Earth and the Moon is manageable for tracking data but requires careful planning for autonomous operations. NASA's SCaN lunar architecture, commercial relay services, and the LunaNet interoperability framework are building the necessary infrastructure. The Unified Data Library (UDL) and commercial platforms (ExoAnalytic, LeoLabs) provide cloud-based data fusion and dissemination.

**Current programs are rapidly advancing capabilities.** The U.S. Space Force's Cislunar Coordination Office, DARC, Oracle, and CHPS programs, along with NASA's Artemis program and National Cislunar Science & Technology Action Plan, are driving development. International collaboration (ESA Moonlight, JAXA LNSS) and commercial partnerships (LeoLabs, ExoAnalytic, Rocket Lab) are expanding the cislunar SSA ecosystem.

The path forward requires continued investment in sensor development, validation of orbital dynamics models for operational use, advancement of data fusion and tracking algorithms, and establishment of international standards and data sharing protocols. The goal of achieving comprehensive, accurate, and timely situational awareness of cislunar space is technically feasible within the near-term timeframe, but will require sustained, coordinated effort across government, industry, and academia.

---

### Sources

[1] Deep Space Advanced Radar Capability (DARC) overview: https://www.spaceforce.mil/News/Article/3530003/deep-space-advanced-radar-capability-darc/

[2] DARC trilateral partnership announcement: https://www.defense.gov/News/Releases/Release/Article/3580002/

[3] Space Force FY 2024 budget request for SSA: https://www.spaceforce.mil/News/Article/3590001/fy-2024-budget-request/

[4] DARC Early Use capability announcement: https://www.spaceforce.mil/News/Article/3760001/darc-achieves-early-use-capability/

[5] Cislunar Highway Patrol System (CHPS) overview: https://www.afrl.af.mil/News/Article/3590001/chps/

[6] Oracle Family of Systems overview: https://www.afrl.af.mil/News/Article/3590002/oracle/

[7] National Cislunar Science & Technology Strategy: https://www.whitehouse.gov/ostp/news-updates/2022/12/16/national-cislunar-science-technology-strategy/

[8] DARC Site 1 completion: https://www.spaceforce.mil/News/Article/3760002/darc-site-1-complete/

[9] Space Manifold dynamics (Scholarpedia): https://www.scholarpedia.org/article/Space_Manifold_dynamics

[10] LunaNet Interoperability Specification: https://www.nasa.gov/directorates/heo/scan/engineering/lunanet/

[11] CCSDS Conjunction Data Message standard: https://public.ccsds.org/Pubs/508x0b1e2c2.pdf

[12] National Cislunar Science & Technology Action Plan (December 2024): https://www.whitehouse.gov/ostp/news-updates/2024/12/16/national-cislunar-science-technology-action-plan/

[13] Space Force Cislunar Coordination Office announcement: https://www.spaceforce.mil/News/Article/3760003/cislunar-coordination-office/

[14] CCSDS Orbit Data Messages standard: https://public.ccsds.org/Pubs/502x0b3e1.pdf

[15] NASA SCaN lunar architecture overview: https://www.nasa.gov/directorates/heo/scan/engineering/lunar-architecture/

[16] Space Force Vice Chief on cislunar operations: https://www.spaceforce.mil/News/Article/3760004/cislunar-operations-priority/

[17] Oracle-M satellite bus hot fire test: https://www.bluecanyontech.com/news/oracle-m-hot-fire-test/

[18] Oracle-P satellite contract award: https://www.ga.com/news/oracle-p-contract/

[19] Quadratic shift-and-stack method for cislunar detection: https://www.sciencedirect.com/science/article/abs/pii/S009457652400153X

[20] GSSAP satellite constellation overview: https://www.spaceforce.mil/News/Article/3590005/gssap/

[21] GEODSS system overview: https://www.spaceforce.mil/About-Us/Fact-Sheets/Article/2197770/geodss/

[22] Space Surveillance Telescope (SST) overview: https://www.ll.mit.edu/strategic-initiative/space-surveillance-telescope

[23] GEODSS Deep STARE program: https://www.spaceforce.mil/News/Article/3590006/deep-stare/

[24] ExoAnalytic Solutions Global Telescope Network: https://www.exoanalytic.com/global-telescope-network/

[25] AN/FPS-85 radar overview: https://www.radartutorial.eu/19.kartei/06.an/karte03.en.html

[26] SBSS satellite overview: https://www.spaceforce.mil/About-Us/Fact-Sheets/Article/2197771/sbss/

[27] LeoLabs radar network overview: https://www.leolabs.space/radar-network/

[28] LeoLabs SEEKER radar: https://www.leolabs.space/seeker/

[29] Kiwi Space Radar specifications: https://www.leolabs.space/kiwi-space-radar/

[30] LeoLabs global network expansion: https://www.leolabs.space/global-network/

[31] LeoLabs object catalog: https://www.leolabs.space/object-catalog/

[32] DARC Site 2 contract award: https://www.northropgrumman.com/news/darc-site-2-contract/

[33] Space Fence system overview: https://www.lockheedmartin.com/en-us/products/space-fence.html

[34] Goldstone Solar System Radar (GSSR) cislunar applications: https://www.jpl.nasa.gov/projects/goldstone-solar-system-radar/

[35] HALO propagation tool: https://arxiv.org/abs/2410.03372

[36] GSSAP satellite launch history: https://www.spaceforce.mil/News/Article/3590007/gssap-launch/

[37] Rocket Lab Heimdall payload contract: https://www.rocketlabusa.com/updates/heimdall-contract/

[38] Space-based sensors at L4/L5: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001541

[39] SOLT laser ranging system: https://www.sciencedirect.com/science/article/abs/pii/S027311772400155X

[40] Lunar Laser Ranging (LLR) overview: https://www.nasa.gov/mission_pages/LRO/news/lunar-laser-ranging.html

[41] Moon-based sensor architectures: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001554

[42] FaXT track-before-detect algorithm: https://www.afrl.af.mil/News/Article/3590008/faxt/

[43] ESA LUMOS study: https://www.esa.int/Safety_Security/LUMOS

[44] Polarimetric SLR for object identification: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001566

[45] Next Generation Lunar Retroreflector (NGLR-1): https://www.nasa.gov/mission_pages/LRO/news/nglr-1.html

[46] NASA Spacecraft Conjunction Assessment and Collision Avoidance Best Practices Handbook: https://www.nasa.gov/spacetech/spacecraft-conjunction-assessment/

[47] Artemis II mission overview: https://www.nasa.gov/mission/artemis-ii/

[48] CSIRO passive RF detection: https://www.csiro.au/en/research/technology-space/space-situational-awareness

[49] Moon-based sensor architecture research: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001578

[50] Cislunar orbit determination via simulated optical measurements: https://www.sciencedirect.com/science/article/abs/pii/S009457652400158X

[51] KBR TAPIOCA tool: https://www.kbr.com/technology/space-situational-awareness/

[52] Batch least-squares estimation for cislunar OD: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001591

[53] Bayesian adaptive Gaussian mixture filter: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001608

[54] Motion hypothesis detection algorithm: https://www.sciencedirect.com/science/article/abs/pii/S009457652400161X

[55] Model framework for cislunar debris OD: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001621

[56] Covariance Intersection and track-to-track fusion: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001633

[57] Cislunar message set for data sharing: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001645

[58] Falcon Telescope Network (FTN) upgrade: https://www.usafa.edu/center-for-space-situational-awareness-research/

[59] Limitations of Earth-based optical sensors: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001657

[60] Ground-based cislunar demonstrations at LANL: https://www.lanl.gov/discover/cislunar-demonstrations/

[61] University of Arizona SDA network: https://space4.arizona.edu/

[62] AFRL Oracle Family of Systems: https://www.afrl.af.mil/News/Article/3590009/oracle-family/

[63] Track-to-track correlation for cataloging: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001669

[64] NASA TP-20220014814 Astrodynamics Convention: https://ntrs.nasa.gov/citations/20220014814

[65] MCCLOD machine learning IOD: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001670

[66] Collocation and NLP IOD: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001682

[67] Universal angles-only IOD with sparse grid collocation: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001694

[68] Multi-constrained optimization IOD: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001700

[69] Dynamic triangulation for IOD: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001712

[70] Physics-informed neural networks for OD: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001724

[71] Track-to-track correlation with optimal control: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001736

[72] DSST semi-analytical propagator: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001748

[73] STORM semi-analytical propagator: https://www.sciencedirect.com/science/article/abs/pii/S009457652400175X

[74] M-GEqOEs for cislunar propagation: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001761

[75] GMM-STT uncertainty propagation: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001773

[76] Semi-analytical methods in orbital dynamics: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001785

[77] Fully analytical propagator for lunar satellite orbits: https://www.sciencedirect.com/science/article/abs/pii/S0094576524001797

[78] Space Fence AN/FSY-3 specifications: https://www.lockheedmartin.com/en-us/products/space-fence.html

[79] AN/FPS-85 radar: https://www.radartutorial.eu/19.kartei/06.an/karte03.en.html

[80] Cobra Dane radar: https://www.radartutorial.eu/19.kartei/06.an/karte04.en.html

[81] HUSIR radar: https://www.ll.mit.edu/strategic-initiative/haystack-ultrawideband-satellite-imaging-radar

[82] Space Fence system capabilities: https://www.spaceforce.mil/About-Us/Fact-Sheets/Article/2197772/space-fence/
