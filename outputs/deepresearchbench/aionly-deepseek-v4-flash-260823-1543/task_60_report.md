# Comprehensive Analysis of Cislunar Space Situational Awareness: Challenges, Technologies, and Future Directions

## Introduction

The cislunar region—spanning from Earth's geosynchronous orbit (approximately 35,786 km) to beyond the Moon's orbit (approximately 384,400 km)—represents a rapidly expanding frontier for human space activity. The volume of cislunar space is approximately 10,000 times that of geosynchronous orbit (GEO), presenting unprecedented challenges for space situational awareness (SSA) and space domain awareness (SDA) [1][2]. As of late August 2026, the United States Space Force has publicly stated that fewer than 20% of cislunar objects are trackable by current operational assets [3]. This reality, combined with the projection that over 30 active missions are operating in cislunar space as of 2026—expected to exceed 120 by the early 2030s—underscores the urgent need for comprehensive, accurate, and operationally relevant cislunar SDA capabilities [4].

This report provides a comprehensive analysis of how to conduct effective situational awareness of space targets in cislunar space, with particular emphasis on supporting short-term tracking and monitoring tasks. The analysis draws on peer-reviewed research, official technical reports from space agencies, and reputable defense and space research organizations, prioritizing developments from 2024 through late August 2026.

---

## 1. Key Challenges in Achieving Cislunar Space Situational Awareness

### 1.1 Vast Spatial Scale and Inverse-Square Law Limitations

The most fundamental challenge in cislunar SDA is the sheer scale of the operational domain. The volume of cislunar space is approximately 10,000 times that of GEO, and the region spans nearly ten times the distance from Earth to geostationary orbit [1][2]. This vast spatial extent has profound implications for sensor performance.

For radar systems, the monostatic radar equation dictates that signal power decreases with the fourth power of range. A radar system optimized for detecting objects at GEO distances (approximately 35,786 km) would experience a signal reduction of approximately 10,000 times when attempting to detect the same object at lunar distances (approximately 384,400 km) [5]. For optical sensors, the inverse-square law similarly reduces signal flux, though these systems are generally more favorable for deep-space detection than radar.

The U.S. Space Force's assessment that fewer than 20% of cislunar objects are trackable by current operational assets [3] reflects this fundamental physics limitation. Even the most capable ground-based telescopes, such as the Ground-Based Electro-Optical Deep Space Surveillance (GEODSS) system, are optimized for objects at GEO ranges and struggle significantly at cislunar distances [6].

### 1.2 Unique Orbital Dynamics: The Restricted Three-Body Problem

In the cislunar region, traditional two-body (Keplerian) orbital dynamics are fundamentally inadequate. The gravitational influence of both Earth and the Moon must be considered simultaneously, making this the domain of the Circular Restricted Three-Body Problem (CR3BP) [7]. The Earth-Moon system has a mass parameter μ ≈ 0.01215, which is "very large by solar system standards" [8].

The CR3BP produces highly non-linear, non-Keplerian dynamics that result in several critical challenges:

- **Complex, non-repeating, chaotic trajectories** that cannot be described by classical orbital elements [9]
- **Exotic orbit families** including libration point orbits, Lyapunov orbits, Lissajous orbits, Halo orbits, and Near-Rectilinear Halo Orbits (NRHOs) [10]
- **No general closed-form analytical solution** exists; equations can only be integrated numerically [11]
- **Invariant manifolds and transition tubes** that mediate transport in cislunar space, forming the "Interplanetary Superhighway" [8]

As described by AFRL's Col. Eric Felt, orbits around the Moon "look like a drunken sailor wandering around" compared to Earth orbits [12]. This has profound implications for tracking: the Air Force Institute of Technology (AFIT) study found that filters regularly diverged after 1.5-2 revolutions (21-28 days) when tracking L2 halo objects [3].

Uncertainty propagation is particularly challenging in this regime. A study evaluating the Modified Generalized Equinoctial Orbital Elements (M-GEqOEs) for the 9:2 NRHO (the baseline for NASA's Lunar Gateway) found that Cartesian methodology exhibits sharp increases in non-Gaussian behavior at perilune, while M-GEqOEs maintain consistently improved uncertainty characterization [13].

### 1.3 Sensor Coverage Gaps

**Earth Rotation and Ground Station Visibility:** Ground-based telescopes lose sight of objects due to Earth's rotation, solar glare, and lunar shadowing [14]. The GEODSS system operates only at night in clear conditions, and actual track rates are significantly lower than ideal rates due to cloud cover (clear skies approximately 50% of time at Socorro, under 50% at Maui, under 40% at Diego Garcia), wind, humidity, and moonlight [6].

**The "Cone of Shame":** The Air Force Research Laboratory (AFRL) coined this term to designate the lunar exclusion zone, within which tracking objects with Earth-based sensors is particularly challenging [15]. This is a cone-shaped region from GEO altitude to Earth-Moon L2 where objects are difficult or impossible to observe from Earth-based sensors due to lunar proximity, illumination geometry, and Earth's rotation. The static demand model of the "Cone of Shame" includes 304 targets in a 30° cone from GEO altitude to L2 [16].

**Lunar Exclusion Angles:** Objects near the Moon are difficult to observe due to lunar exclusion angles (typically greater than 10° for optical sensors), Sun exclusion angles (greater than 30°), and Earth exclusion angles (greater than 10°) [16]. The Moon's proximity creates increased optical background noise, further degrading detection capability [17].

### 1.4 Communication Latencies

Long communication latencies affect real-time tracking operations. Round-trip light time to the Moon is approximately 1.3 seconds, plus processing delays. Technologies such as orbit determination, mission autonomy, and low-thrust propulsion need advancement to overcome these challenges [1]. For space-based sensors operating in cislunar space, communication delays impact the ability to task sensors in real-time, necessitating autonomous onboard processing capabilities.

### 1.5 Low Signal-to-Noise Ratios for Small Objects

Cislunar SSA presents reduced target signal due to the large distance between sensors and targets [17]. For ground-based optical telescopes, detecting faint objects is difficult because of their low brightness, strong lunar background, and complex, nonlinear apparent motion [18]. A Quadratic Shift-and-Stack (QSS) method developed by researchers at the Purple Mountain Observatory, Chinese Academy of Sciences, can improve the detection limit by up to 1 stellar magnitude compared with traditional linear shift-and-stack methods [18][19].

The Goldstone Solar System Radar (GSSR) has a JPL project focused on increasing sensitivity to detect 1-meter or smaller targets at lunar distances, using advanced signal processing techniques including a software polyphase filter bank (PFB) to minimize FFT leakage and scalloping loss, achieving 97.87% improvement for unknown targets using PFB with polarimetric approach [20].

### 1.6 Distinguishing Natural from Artificial Objects

A major challenge is distinguishing natural objects (asteroids, meteoroids) from artificial objects (spacecraft, debris) in cislunar space. The GSSR Cis-lunar Space Debris Radar project aims to detect objects (mini-moons, lost spacecraft, small asteroids, etc.) and improve target characterization through advanced signal processing [20]. The University of Arizona's Space4 Center identified a Chinese rocket booster that crashed into the Moon, demonstrating the need for characterization capabilities [21]. A Chinese rocket stage crashed into the Moon in March 2022, but the impact was not confirmed until nearly four months later due to no observation assets in position [22].

### 1.7 Data Fusion and Correlation Challenges

Data fusion across heterogeneous sensor types and domains is a key challenge. The paper "Adaptive Sensor Tasking Strategies for Tracking Non-Cooperative Cislunar Space Objects" (AMOS 2024) addresses multi-target observation association techniques to detect non-cooperative tracking events, using kinematic gating and non-kinematic association heuristics to distinguish closely spaced objects and reduce track duplication [23].

The "CubeSat confusion" problem—where small satellites deployed in batch rideshare launches are difficult to distinguish—scales as n! (e.g., 10 objects = 3.6 million combinations, 20 objects = 2.4×10^18 combinations). This problem will intensify in cislunar space as traffic increases [24].

### 1.8 Lack of Established Resident Space Object Catalog for Cislunar Regime

There is currently no dedicated, comprehensive catalog of resident space objects (RSOs) for the cislunar regime. The U.S. Space Force's Space Surveillance Network (SSN) maintains a catalog of over 50,000 objects in Earth orbit, but no equivalent exists for cislunar space [25]. The paper "Cislunar Admissible Regions from Periodic Orbit Manifolds" (AMOS 2025) notes that "the expansion of mission operations in cislunar space is expected to significantly increase the number of anthropogenic space objects (ASOs), creating a pressing demand for initial orbit determination (IOD) techniques specifically developed for this regime" [26].

---

## 2. Sensor Technologies for Cislunar Detection and Tracking

### 2.1 Ground-Based Optical Telescopes

**Vera C. Rubin Observatory (formerly LSST):** The Rubin Observatory, located at Cerro Pachón, Chile, achieved first light in June 2025 and began full survey operations on June 30, 2026 [27]. It features an 8.4-meter primary mirror with a unique three-mirror anastigmat optical design delivering a 3.5-degree field of view (9.6 deg²). The 3.2-gigapixel CCD camera achieves 5σ single-exposure limiting magnitudes of r < 24.5 (single images) and r < 27.8 (coadded/stacked) [27]. A SPIE presentation (2025-2026) specifically addressed "Efficient detection of faint geostationary and cislunar objects in Rubin LSST imagery" [28]. On February 25, 2026, Rubin Observatory issued its first scientific alerts, marking a historic milestone [29]. The observatory is expected to catalog over 5 million asteroids, including approximately 100,000 near-Earth objects, and will significantly contribute to cislunar object detection.

**Zwicky Transient Facility (ZTF):** Located at Palomar Observatory, California, ZTF uses a 47 square degree field of view camera with a limiting magnitude of 20.5 [30]. Since 2024, ZTF runs monthly "ZTF experiments" exploring novel observing modes, including detection of cislunar objects [31]. ZTF acts as a prototype for the Vera C. Rubin Observatory and has discovered over 232 near-Earth asteroids and comets.

**Space Surveillance Telescope (SST):** Located at the Harold E. Holt Naval Communication Station in Exmouth, Western Australia, the SST features a 3.5-meter-aperture mirror with Mersenne-Schmidt type optics, a field of view of 6 square degrees, and a limiting magnitude of 20.5 [32]. The SST achieved initial operational capability on October 4, 2022, and holds the world record for most observations in a single year: 6.97 million in 2015 [33]. The strategic location in Australia provides unique space domain awareness coverage in the Indo-Pacific Command region.

**Ground-Based Electro-Optical Deep Space Surveillance (GEODSS) System:** The United States' primary deep space tracking system provides approximately 60% of all SSN deep space observations and nearly 80% of all geosynchronous observations [6]. Three active sites operate at Socorro, New Mexico; Diego Garcia, Indian Ocean; and Maui, Hawaii. Each site uses one-meter telescopes with highly sensitive digital cameras. The Deep Stare Upgrade (approximately 2003-2005) replaced Ebsicon vacuum tube detectors with CCD arrays, bringing a 2.5 magnitude gain in sensitivity, over 2x improvement in position measurement accuracy, and 40% increase in search rate [6]. The GBOSS (Ground-Based Optical Sensor System) upgrade, completed at the New Mexico facility first and at the Hawaii facility in April 2026, doubles the field of view, doubles search speed, and more than triples the sensitivity [34]. GEODSS can now scan across MEO, GEO, HEO, and cislunar orbits.

**University of Arizona Space4 Center:** The largest academic SDA network operates over 13 optical, IR, and passive RF sensors worldwide, achieving GEO positional accuracy under 50 meters. The center detects objects as small as 16 inches in GEO and tracks greater than 3-inch debris in LEO [21]. Core capabilities include continuous observing, autonomous sensor tasking, spectral material identification, predictive modeling, cislunar object cataloging, and multi-sensor data fusion.

**Slingshot Aerospace Global Sensor Network:** Operates over 150 ground-based optical sensors at 20+ global sites, providing persistent, day/night space domain awareness from LEO to beyond GEO (xGEO) [35]. Slingshot's patented daytime optical capability provides approximately 400% more observable LEO passes than night-only systems. The company operates the first uncued commercial optical fence that simultaneously detects and tracks all transiting LEO objects of cubesat size or larger.

**Quadratic Shift-and-Stack (QSS) Method:** Developed by researchers at the Purple Mountain Observatory, Chinese Academy of Sciences, this method derives a formula (t_limit = √(12×FWHM/|a|)) to determine the maximum integration time for linear stacking based on PSF width and apparent motion acceleration [18][19]. QSS improves SNR from stacking and can enhance the detection limit by up to 1 stellar magnitude compared with linear shift-and-stack (LSS). Real-world validation using observations of Tiandu-1 (Earth-Moon 3:1 resonant orbit) and Queqiao-2 (elliptical lunar orbit) with the MASTA-LENGHU telescope showed linear stacking peaks at SNR=16.77 after 29 minutes (500 frames), while QSS achieves SNR=21.98 after 46 minutes (790 frames), a 31% improvement over linear stacking's peak [19].

### 2.2 Ground-Based Radar Systems

**Goldstone Solar System Radar (GSSR):** Located at the Goldstone Deep Space Communications Complex, Barstow, California, GSSR is the largest fully steerable ground-based radar in the world for non-classified high-resolution ranging and imaging [20]. It operates a 500-kW X-band (8500-8560 MHz) transmitter and low-noise receiver on the 70-meter DSS 14 antenna, capable of radiating approximately 450 kW. The Cis-lunar Space Debris Radar (CSDR) project, led by JPL/NASA, aims to establish capability to detect objects (mini-moons, lost spacecraft, small asteroids) in cis-lunar space using radar and advanced signal processing [20]. The goal is to increase sensitivity to detect 1-meter or smaller targets at lunar distances. GSSR has proven capability through detection of the Lunar Reconnaissance Orbiter and lost spacecraft Chandrayaan-1.

**Haystack Ultrawideband Satellite Imaging Radar (HUSIR):** Located at MIT Lincoln Laboratory, Westford, Massachusetts, HUSIR features a 36.6m-diameter antenna with dual-band capability (X-band and W-band) [36]. The X-band provides 0.058-degree beam width and 1.024 GHz bandwidth giving 0.25 m range resolution. HUSIR can detect debris down to approximately 5.5-6 mm at altitudes up to 1000 km (99% completeness at 6 mm) and can image satellites out to geostationary orbit distances. However, HUSIR is optimized for LEO debris characterization and is not specifically designed for cislunar ranges.

**LeoLabs Radar Network:** A private company founded in 2016, LeoLabs operates 11 active phased-array radars across 7 global sites, tracking over 25,000 objects [37]. The radar network includes the Poker Flat ISR (Alaska), Midland Space Radar (Texas), Kiwi Space Radar (New Zealand), Costa Rica Space Radar, and facilities in Western Australia and the Azores. LeoLabs achieved over $60M in contracts in 2025, a 186% year-over-year growth in U.S. government contracts. However, LeoLabs' current niche is LEO tracking, and cislunar expansion is a future goal.

**Chinese Deep Space Network (CDSN):** Managed by the China Satellite Launch and Tracking Control Center General (CLTC) of the PLA Strategic Support Force Space Systems Department, the CDSN includes a 50-meter antenna at Miyun, a 40-meter antenna in Yunnan, a 35-meter antenna at Kashgar (upgraded in 2020 to an array of four 35-meter antennas equivalent to a 66-meter antenna), a 64-meter antenna at Jiamusi, and the Espacio Lejano Station in Neuquén Province, Argentina [38]. The planned Qitai Radio Telescope (QTT) will be a 110-meter fully steerable dish, which would become the world's largest fully steerable single-dish radio telescope.

**Modern GaN Phased-Array Radars:** According to market research, modern GaN phased-array radars offer 12-15 dB sensitivity improvements over legacy systems, enabling detection of objects as small as 10 cm at 100,000 km range [4]. Individual phased-array installations range from $150 million to over $600 million per facility.

### 2.3 Space-Based Sensors

**AFRL Oracle Program:** The Oracle Family of Systems comprises two AFRL programs—Oracle-Mobility (Oracle-M) and Oracle-Prime (Oracle-P)—designed to develop cislunar SSA capabilities [39]. Oracle-M is a cutting-edge SSA pathfinder satellite designed to provide persistent situational awareness in cislunar space. The Hot Fire Test was successfully completed March 16-21, 2025, at Edwards Air Force Base, California, testing the novel integrated propulsion module combining Hall Effect thrusters fueled by Xenon gas [40]. The test brought the satellite to initial launch capability (ILC). Oracle-Prime will operate near Earth-Moon Lagrange Point 1 (approximately 326,400 km from Earth), carrying an optical payload from Leidos and AFRL's green propellant experiment [39]. Launch is anticipated for 2026-2027, with a two-year demonstration mission.

**AFRL Cislunar Highway Patrol System (CHPS):** Announced by AFRL's Col. Eric Felt at the AMOS conference on September 18, 2020, CHPS is a pathfinder satellite designed to find and track objects in cislunar space, including those orbiting the Moon [12]. CHPS is specifically designed to address the "cone of shame" limitation. The system may become one of AFRL's Vanguard programs designed to accelerate technology development.

**NASA's CAPSTONE:** The CAPSTONE (Cislunar Autonomous Positioning System Technology Operations and Navigation Experiment) CubeSat currently operates in an NRHO around the Moon [41]. CAPSTONE is used as a test target for the FaXT track-before-detect algorithm developed at the University of Maryland [42]. The mission demonstrated autonomous navigation using the Cislunar Autonomous Positioning System (CAPS), involving two-way coherent signal communication for range and Doppler navigation measurements, and optical-only orbit determination using Moon's horizon imagery. NASA declared its mission complete on July 6, 2026, though Advanced Space continues operating the spacecraft as a technology testbed.

**DARPA LASSO (Lunar Assay via Small Satellite Orbiter):** DARPA announced a new program seeking proposals for prototype spacecraft capable of autonomous navigation and high maneuverability in low lunar orbit (LLO) for cislunar space situational awareness [43]. The program aims to develop an affordable and scalable commercial capability for SSA in cislunar space, supporting the Space Force.

### 2.4 Proposed Constellations and Emerging Concepts

**RCAT-CS (Reconfigurable Constellations for Adaptive Tracking in Cislunar Space):** A $1 million grant from the U.S. Air Force Office of Scientific Research to researchers at Rensselaer Polytechnic Institute (RPI) and Texas A&M University proposes a constellation of 3 to 10 sensor-mounted satellites in elliptical "halo orbits" around Earth-Moon Lagrange points [44].

**TE-p-MP Formulation (Georgia Tech):** A mixed-integer linear programming (MILP)-based formulation called the time-expanded p-median problem (TE-p-MP) simultaneously solves constellation design and sensor-tasking subproblems for cislunar SSA [16][45]. The formulation considers 40 synodic-resonant libration point orbits (LPOs) across families including L1/L2 Lyapunov, Southern and Northern L2 Halo, Southern and Northern Butterfly, Distant Prograde Orbit (DPO), and Distant Retrograde Orbit (DRO), with synodic resonances 1:1, 3:2, 2:1, 9:4, 5:2, 3:1, 4:1, and 9:2.

**Chinese Cislunar Space Infrastructure Proposal:** Chinese scientists led by Yang Mengfei (China Academy of Space Technology) proposed a major cislunar space infrastructure project (June 2024) [46]. The phased constellation would provide data communication, positioning, navigation, timing (PNT), and space situational monitoring. Phase 1 involves satellites in elliptical frozen orbits (ELFO) around the Moon. Phase 2 adds ELFO satellites, spacecraft at Earth-Moon L1, L2, L4, L5, a near-rectilinear halo orbit (NRHO), and a cislunar space station in GEO. Phase 3 adds satellites in distant retrograde orbits (DRO).

**Fast X-ray Transform (FaXT) Track-Before-Detect Algorithm:** Developed by the University of Maryland team, this novel dynamic-programming track-before-detect algorithm has already demonstrated ability to detect objects up to ten times fainter than previously possible in large-scale asteroid searches [42]. The project is adapting FaXT for cislunar space, using NASA's CAPSTONE CubeSat as a test target. Supported by the AFRL Regional Network Mid-Atlantic Hub, the algorithm addresses reduced target signal, increased optical background noise, and high orbit uncertainty from three-body dynamics.

---

## 3. Orbital Dynamics and Modeling for Cislunar Regimes

### 3.1 The Circular Restricted Three-Body Problem (CR3BP)

The orbital dynamics in cislunar space is best described by a restricted 3-body model where a spacecraft or other object is affected by both the Earth and Moon simultaneously, rather than the weakly perturbed Keplerian approach used for near-Earth objects [7][8]. The CR3BP involves two massive bodies (Earth and Moon) in circular orbit with a test particle (spacecraft). The only important parameter is the mass parameter μ (Moon's mass divided by sum of masses = approximately 0.01215 for the Earth-Moon system), which is "very large by solar system standards" [8].

The Jacobi Constant (or Tisserand Relation) is a constant of motion (3-body energy) that can be used to understand orbital changes before and after close encounters with the Moon. Zero velocity curves define regions where spacecraft can or cannot go [8]. The CR3BP provides an autonomous approximation of the dynamics, while a higher-fidelity N-body ephemeris model (including Earth, Moon, Sun, and Jupiter) is used for realistic mission simulation [47].

### 3.2 Lagrange Points and Their Characteristics

The Lagrange points are the locations where the gravitational forces of the two massive bodies and the centrifugal force balance in the rotating frame [8]. L4 and L5 are triangular points (stable) 60° ahead/behind the Moon, producing tadpole and horseshoe orbits. L1, L2, and L3 are collinear points (unstable). L1 and L2 distances from the Moon are approximately one Hill radius (approximately 60,000 km) [8]. These points serve as critical locations for space-based sensor placement.

### 3.3 Halo Orbits, Lissajous Orbits, and Quasi-Periodic Orbits

**Halo Orbits (3D):** These three-dimensional orbits look like "potato chip edges," with periods of 7-14 days, and come in northern and southern varieties [8]. Halo orbits around collinear critical points (L1 or L2) are periodic but change shape and size with parameter variations. Using halo orbits, scientists can regularly and simultaneously see the Earth and the dark side of the Moon in the Earth-Moon system [48].

**Lyapunov Orbits:** Planar, kidney bean-shaped orbits around the Lagrange points [8].

**Lissajous Orbits:** Quasi-periodic orbits around the Lagrange points [8].

**Quasi-Halo Orbits:** Orbits that exist around halo orbits [8].

### 3.4 Near-Rectilinear Halo Orbits (NRHOs) and Distant Retrograde Orbits (DROs)

**Near-Rectilinear Halo Orbits (NRHOs):** NRHOs are a subset of L1 and L2 halo orbit families and are solutions to the three-body problem [49]. The CAPSTONE mission (launched 2022) was the first spacecraft to use an NRHO in cislunar space. NASA's Lunar Gateway was planned to use a 9:2 resonant NRHO with a period of approximately 7 days, ranging from 3,000 km above the lunar north pole to 70,000 km over the lunar south pole [49]. There are four families of NRHO orbits associated with L1 and L2 points (two northern, two southern). NRHOs are marginally stable or weakly unstable, with divergence rates significantly slower than other halo orbits.

According to Zimovan, Howell, and Davis (2017), Earth-Moon L2 NRHOs are characterized by perilune radii ranging from approximately 1850 km to 17350 km, with orbital periods ranging from approximately 6 days to just over 10 days [50]. Synodic resonance is key for eclipse avoidance: a 4:1 synodic resonant NRHO (approximately 5,600 km perilune) avoids lunar eclipses completely, while a 9:2 resonant orbit (approximately 3,150 km perilune) encounters approximately 60-minute eclipses [50].

**Distant Retrograde Orbits (DROs):** DRO satellites are situated in a region exhibiting significant asymmetry (approximately 20%), which is a fundamental prerequisite for the LiAISON (Linked Autonomous Interplanetary Satellite Orbit Navigation) principle [51]. The LiAISON technique enables autonomous absolute orbit determination through satellite-to-satellite tracking (SST) range measurements between two satellites when one is located in an asymmetric gravitational field, eliminating dependence on ground stations.

### 3.5 Manifold Dynamics and Transport

Stable and unstable manifolds of periodic orbits form tubes in phase space that mediate transport. Inside the tube = transit orbits (pass through Lagrange point neck regions); outside = non-transit (bounce back) [8]. These manifolds form the "Interplanetary Superhighway" and connect cislunar space to heliocentric space (e.g., lunar L1 to Sun-Earth L2). Halo orbits are "center-saddle" type, where the monodromy matrix (state transition matrix after one period) reveals one large real pair (stable/unstable directions), one pair equal to 1 (neutrally stable), and one complex conjugate pair on unit circle (center directions) [8].

Dynamic departure tubes in the CR3BP and Bicircular Restricted Four-Body Problem (BCR4BP) are used to identify critical surveillance regions, focusing on maneuver-induced departures (0.05 km/s to 0.5 km/s Δv) from NRHOs and L2 Lyapunov orbits [52].

### 3.6 Perturbations Affecting Cislunar Orbits

High-fidelity models for cislunar orbit propagation must account for multiple perturbations:

- **Solar Radiation Pressure (SRP):** Included as a perturbation in high-fidelity models [47]
- **Oblateness (J2):** Increasing oblateness increases amplitude of halo orbits [48]
- **Third-Body Effects:** Earth, Sun, Jupiter, Venus, and other bodies [47]
- **Earth Gravitational Field:** Uses harmonic model (not point mass) [47]
- **General Relativistic Correction:** Applied for spacecraft near massive bodies [47]
- **Earth Albedo:** Simple model accounting for reflected solar radiation [47]
- **Lunar Gravitational Field (LGF):** Modeled using spherical harmonics with normalized coefficients, accounting for mascons (mass concentrations) [47]
- **Lunar Solid Tides:** Static due to Moon's synchronous rotation, factored into LGF coefficients [47]

### 3.7 Analytical vs. Numerical Propagation Methods

The HALO (High-precision Analyser for Lunar Orbits) tool is an open-source mission design tool for precise orbit propagation in the cis-lunar domain [53]. The propagator is validated against spacecraft ephemerides for four reference orbit types: Low Lunar Orbits (LLO), Elliptical Lunar Frozen Orbits (ELFO), Near Rectilinear Halo Orbits (NRHO) around L2, and Distant Retrograde Orbits (DRO). HALO enables resolution of mission design problems including optimization of Lambert transfers and convergence of TBP orbits from simplified CR3BP models to high-accuracy ephemeris models.

### 3.8 How Chaotic Dynamics Affect Uncertainty Propagation

The chaotic dynamics of the CR3BP make uncertainty propagation more difficult than in Keplerian orbits [3][9]. Traditional orbit determination methods that work well for Low Earth Orbit (LEO)—including IOD methods (Gauss' Method, Double-R Iteration, Gooding's Method) and statistical methods (batch least squares, Kalman filters)—are often inadequate or unusable for cislunar objects [54]. For objects in Earth orbit, an OD solution can be well-refined with relatively little data—a handful of optical observations or radar passes. This is not the case for cislunar orbits [3].

The Modified Generalized Equinoctial Orbital Elements (M-GEqOEs) have been developed for state and uncertainty propagation in cislunar space under high-fidelity dynamics [13]. Evaluated for the 9:2 NRHO (Gateway baseline) and 4:1 sidereal resonant orbit, uncertainty propagated in M-GEqOE coordinates better preserves Gaussian behavior compared to Cartesian coordinates.

---

## 4. Data Fusion and State Estimation Methods

### 4.1 Orbit Determination for Cislunar Objects: Differences from Near-Earth OD

For cooperative objects in cislunar space, such as the ARTEMIS spacecraft, orbit determination is achieved using a batch least-squares method that analyzes range and Doppler tracking measurements from the NASA Deep Space Network (DSN), reducing estimation error to less than 0.1 km and 0.1 cm/s for position and velocity, respectively [55]. However, this method cannot be utilized for non-cooperative objects.

For non-cooperative objects, only optical observations are possible, and standard techniques provide only short-term state estimates [55]. Cislunar space-based optical tracking faces challenges including low SNR, lunar exclusion angles, short data arcs, and nonlinear dynamics [3]. Filters regularly diverged after 1.5-2 revolutions (21-28 days) when tracking L2 halo objects [3].

With short data arcs (approximately 21 days), state estimation achieved: 1-2 km position/1 cm/s velocity from NRHO observers; 400-500 m position/less than 1 cm/s from L2 halo observers; 2-3 km position/1-2 cm/s from L2 Lyapunov observers [3]. An L2 Lyapunov orbit with 1:1 synodic resonance provides near-continuous sunlit observations but exhibits larger uncertainties due to greater distances.

### 4.2 Batch Least-Squares vs. Sequential Filtering

**Batch Least Squares:** Commonly employed for off-line processing of trajectories from LEO spacecraft. Pros include ease of use and fewer inputs needed. Cons include poor performance with maneuvers, difficulty finding optimal "fit span," covariance too optimistic, and inverse fails if state not fully observable [56].

**Sequential Filtering (Kalman Filter):** Pros include good performance with maneuvers, realistic error covariance, elimination of "fit span" concept, and adaptation to force model errors. Cons include requirement for reasonable starting state and fewer experienced analysts [56]. The Filter operates in two phases per measurement: prediction (using physical models to predict next state) and correction (applying measurement-based corrections according to confidence levels).

### 4.3 Extended Kalman Filters (EKF), Unscented Kalman Filters (UKF), and Particle Filters

The study by Patel, Tomita, and Ho (2025) uses the CR3BP dynamics and extended Kalman filter (EKF) for state estimation [55]. The unified orbit-attitude estimation framework uses an error-state multiplicative Unscented Kalman Filter (UKF) with a 12-dimensional state vector (attitude error GRPs, angular velocity, position, velocity in CR3BP frame) [24]. Optical measurements include right ascension, declination, and photometric magnitude modeled via the Cook-Torrance BRDF.

The Adaptive Gaussian Mixture Interacting Multiple Model (AGMIMM) filter is a novel adaptive Bayesian filter for tracking noncooperative maneuvering space objects in cislunar space [57]. CSO motion is modeled as a jump Markov system (JMS), where the CSO modality is unknown and subject to random switching. The filter uses Gaussian mixture representations to approximate non-Gaussian probability distributions caused by nonlinear dynamics, chaotic motion, and long observation gaps.

The Discrete Parameter Flow (DPF) filtering method presents a novel recursive Bayesian inference method for nonlinear systems, specifically targeting sparse tracking of objects in cislunar orbits [58]. The core innovation is a homotopic continuation of Bayes' rule that partitions the traditional single-step measurement update into multiple incremental updates, preserving the Gaussian mixture representation (GMM) of the prior/posterior densities. The adaptive step variant (ADPF-EGMF) offers significant computational savings while maintaining or improving estimation accuracy, using approximately 16 steps on average (vs. 30 fixed) [58].

The Particle Gaussian Mixture (PGM) Filter propagates particles, clusters them into Gaussian Mixture Models (GMMs), performs measurement updates using an Ensemble Kalman Filter (EnKF) update, and resamples [59]. The PGM Filter effectively reduces initial uncertainty (which can be tens of thousands of km in position and tens of km/s in velocity) over time using angles-only measurements after IOD.

### 4.4 Initial Orbit Determination (IOD) Methods for Cislunar

**Admissible Regions and Topocentric Intersection Theory (Dinh, Scheeres, Holzinger, 2024):** This work leverages admissible regions theory and topocentric intersection theory analysis (TITA) to develop an IOD method for objects in cislunar space [60]. The approach links two observations via lower-dimensional projections of admissible regions, identifying potential initial range and range-rates at intersection points. Applied to three orbits of interest around the L2 Lagrange point—a planar orbit, a 3:1 resonance Halo orbit, and a 9:2 resonance Near-Rectilinear Halo Orbit.

**Dynamic Triangulation (Smego and Christian, 2026):** Conventional angles-only initial orbit determination algorithms assume Keplerian dynamics and are not well-adapted to cislunar trajectories [61]. The dynamic triangulation approach approximates an object's motion as rectilinear over a short segment, permitting generation of an initial guess that is then refined using the full CR3BP dynamical model and a nonlinear least squares solver. For the NRHO case with 5 arcsec noise, mean position error after refinement was 1.56 km (min 0.005 km, max 7.39 km) and mean velocity error was 0.35 m/s (min 0.001 m/s, max 1.64 m/s).

**Multi-Constrained Optimization IOD (Song, Wang, Zheng, Wang, 2026):** By integrating measurement, dynamic, and inherent orbital constraints, this approach is designed to enhance the convergence success rate and accuracy of cislunar IOD [62]. The algorithm consists of four steps: (1) estimating angular parameters from measurements and random sampling within error hyperellipsoids; (2) constructing an admissible region for range and range-rate; (3) performing independent optimization for each sample; and (4) determining the final IOD solution through solution group optimization.

**Collocation-Based IOD with Ephemeris Models (AMOS 2025):** This approach integrates with high-fidelity ephemeris models from NASA's SPICE toolbox, moving beyond simplified dynamics like the CR3BP [63]. Key benefits include eliminating the need for close initial guesses (convergence works from Lagrange point guesses), handling impulsive or continuous maneuvers, and achieving higher accuracy by accounting for Earth-Moon eccentricity, solar gravity, and solar radiation pressure.

**Machine Classifier for Cislunar Orbit Determination (MCCLOD):** The novel MCCLOD IOD process is compared directly with a classical two-body IOD approach (Gooding) for Earth-Moon L1 and L2 halo orbit examples [64]. Simulations indicate drastic improvement in both accuracy (MCCLOD demonstrates at best two orders of magnitude improvement in positional error performance) and batched least-squares convergence consistency.

**Three Angle-Only Measurements IOD (Embry-Riddle, 2025):** This novel IOD algorithm uses only three angle-only measurements taken at three discrete times [65]. The algorithm enables accurate IOD using minimal observational data, making it particularly suited for onboard implementation in resource-constrained cislunar missions.

### 4.5 Machine Learning/AI-Based Approaches

**Physics-Informed Neural Networks (PINNs):** The PINN approach incorporates the dynamical model into the neural network's loss function as a regularizer, allowing it to estimate both the state of a maneuvering target and the maneuvers themselves without requiring initial guesses or integration [66].

**Uncertainty-Aware Physics-Informed Machine Learning (PIML) for Cislunar OD (Badura et al., 2025):** This approach uses an Extreme Learning Machine (ELM) architecture that incorporates both a "physics loss" (CR3BP multi-body dynamics via automatic differentiation) and a "big-data loss" (line-of-sight measurement matching) to converge on high-accuracy trajectory predictions even from extreme initial errors (approximately 1E1 km accuracy from approximately 1E5 km initial errors) [67]. The key innovation is treating PIML weights as Gaussian probability distributions rather than point estimates, enabling retrieval of epistemic uncertainty in trajectory predictions.

**CNN-CAR (Convolutional Neural Network - Constrained Admissible Region):** This hybrid CNN-CAR model achieved a remarkable success rate of 50%, nearly doubling the accuracy of the standalone CAR method (25%) [68]. The framework also exhibited remarkable robustness against observational noise, maintaining a stable recognition rate of 50% even when positional uncertainties reached 1,000 arcseconds.

### 4.6 Sensor Fusion Architectures

The time-expanded p-median problem (TE-p-MP) simultaneously solves constellation design and sensor-tasking subproblems for cislunar SSA [16][45]. The Lagrangian relaxation decouples observer-wise sensor-tasking decisions for computational efficiency. The framework uses a semi-Markov Decision Process (SMDP) to generate locally optimal sensor tasking strategies that minimize tracking uncertainty [23]. Key innovations include state-driven policy adjustments allowing sensor agents to re-evaluate actions in real-time, consensus algorithms for coordinated multi-platform decision-making, and kinematic gating and non-kinematic association heuristics for distinguishing closely spaced objects.

A study published in Acta Astronautica (Volume 229, April 2025, Pages 814-830) proposes a Space-Based Space Surveillance (SBSS) framework using multiple cost-effective Electro-Optical Sensors (EOS) for tracking Resident Space Objects [69]. Three distinct data fusion methodologies are proposed and compared: Measurement Fusion-1 (MF-1), Measurement Fusion-2 (MF-2), and Track-to-Track (T2T) fusion. MF-1 delivers superior tracking accuracy, while T2T fusion demonstrates superior computational efficiency. The integration of SBSS and GBSS data surpasses the performance of GBSS alone across all evaluated fusion methodologies.

---

## 5. Operational Concepts and Architectures

### 5.1 Proposed and Emerging Architectures

**Graph-Based Modeling Paradigm (2025):** A paper by BANALA MANASWINI introduces a resilient SDA architecture using a graph-based modeling paradigm wherein satellites, sensors, and targets are represented as dynamically interacting nodes [70]. The design process employs a multi-objective evolutionary algorithm to optimize performance, cost, and resilience concurrently. Simulation outcomes demonstrate that the architecture preserves high coverage and operational continuity even under partial degradation.

**Reinforcement Learning for Cooperative Architecture Design (2024):** A paper by Klonowski, Owens-Fahrner, Heidrich, and Holzinger uses reinforcement learning to solve the multi-objective Cislunar architecture design problem by modeling a cooperative architecture user that seeks to maximize detectability while minimizing total delta-v [71]. A novel clustering method groups architectures explored during optimization to understand how observers must work in concert to produce optimal results.

**AFIT Reference Architecture for Cislunar SDA (2022):** Major Benjamin R. Williams' AFIT thesis synthesizes a methodology from Agile system development, Digital Engineering (DE), Mission Engineering (ME), and Model-based Systems Engineering (MBSE) to develop a Reference Architecture (RA) and Digital Thread (DT) for cislunar SDA mission and system design [72]. Key findings include that traditional orbital regimes (LEO, GEO) and ground-based systems cannot provide consistent custody of cislunar targets, and that observers must be placed in non-traditional locations (e.g., high semi-major axis Earth orbits, Lagrange points, lunar surface) to improve performance.

**Earth-Moon 2:1 Resonance Orbits for Surveillance (2021):** Research from Purdue University presents using Earth-Moon 2:1 resonant orbits for comprehensive Cislunar SSA and Space Traffic Management (STM) [73]. The 2:1 resonant orbit family in the CR3BP connects the near-Earth region (including GEO) with the near-Moon region, covering the entire Cislunar region in approximately 20 revolutions (approximately 26 days each). The selected orbit is nearly linearly stable, transfers well to high-fidelity ephemerides models, and is suitable for a chief-deputy constellation configuration. The Unscented Kalman Filter (UKF) successfully maintained tracking using 56 right-ascension/declination measurements from global Earth sensors (limiting magnitude 20), achieving final estimated uncertainties of 2.06 km in position and 1.51 cm/s in velocity.

### 5.2 Sensor Tasking and Scheduling Algorithms

**MILP-Based Tasking:** The Georgia Tech TE-p-MP formulation simultaneously solves the constellation design and sensor-tasking subproblems, placing p space-based observers into discretized orbital slots along LPOs and allocating pointing directions across discretized time steps [16][45].

**Bayesian Optimization for Sensor Tasking:** The unified framework using Bayesian optimization (Tree of Parzen Estimators) selects observer orbits from 302 candidate trajectories across 13 periodic orbit families, using a greedy mutual-information-based sensor tasking strategy [24].

**AI/ML for Scheduling:** AMOS 2025 papers include presentations on "Autonomous scheduling for space-to-space surveillance," "Genetic algorithm-driven radar scheduling," and "Scalable multi-agent sensor tasking using deep RL" [74].

### 5.3 Coordinated Multi-Platform Tracking Approaches

The AFIT low-fidelity constellation study demonstrates that using multiple observation satellites with lower-fidelity equipment helps alleviate difficulties by aggregating together multiple data sets with higher variance to achieve the same level or better accuracy as higher-fidelity systems [75]. The optimized sensor distribution strategy using Particle Swarm Optimization (PSO) determines optimal observer placement, using Visibility Count Percentage (VCP) to quantify object visibility over time [52].

The Bhadauria, Black, and Frueh study (2025) proposes an optimized sensor distribution strategy for maintaining custody of maneuvering objects in L2 Lyapunov and NRHOs [52]. The study uses dynamic departure tubes in the CR3BP and BCR4BP to identify critical surveillance regions, focusing on maneuver-induced departures (0.05 km/s to 0.5 km/s Δv) from NRHOs and L2 Lyapunov orbits. Optical visibility constraints include Earth exclusion angle >10°, Moon exclusion angle >10°, Sun exclusion angle >30°, and a limiting magnitude of 18.

### 5.4 International Coordination Frameworks

**ESA Space Safety Programme (S2P):** The Space Safety Programme (S2P), formerly the SSA programme, is an ESA initiative that monitors hazards from space [76]. At the 2025 ESA ministerial council, member states committed €955 million for S2P over three years (a 30% budget increase). The programme focuses on space weather, planetary defense, and debris mitigation.

**ESA's Cislunar SSA Efforts:** The European Space Policy Institute (ESPI) study (July 2025) titled "Towards a Safe and Sustainable Cislunar Space" identifies three major challenges: (1) SSA and STM—no dedicated system exists to monitor/coordinate objects near the Moon; (2) Space Debris and End-of-Life procedures—no shared rules for spacecraft disposal; (3) Space Weather risks—the Moon lacks Earth's magnetic shield [77]. The report notes that Europe's engagement is described as fragmented and reactive, and that "whoever builds the first systems and frameworks around the Moon will have the most influence in setting the 'rules of the road.'"

**UN COPUOS and International Norms:** The 2013 UN Group of Governmental Experts (GGE) on Transparency and Confidence-Building Measures in Outer Space Activities proposed TCBMs including information exchange on space policies, orbital parameters, launch notifications, and risk reduction notifications [78]. The Artemis Accords, established in 2020, now include more than 60 countries providing principles for civil space exploration.

**Cislunar Space Traffic Management (STM):** An Acta Astronautica article (Volume 229, April 2025, Pages 211-217) comprehensively explores the unique challenges of managing space traffic in cislunar environments [79]. Key challenges include complex astrodynamics (CR3BP), unstable lunar orbits, communication delays, and gaps in PNT systems. The report calls for international cooperation and enhanced data sharing, recommending establishing an international civil agency to lead space traffic coordination. The Korea Aerospace Research Institute (KARI) has received 40 "red alarms" of potential collisions among spacecraft orbiting the Moon in the last 18 months, demonstrating the immediate need for cislunar STM [80].

---

## 6. Metrics for Effectiveness of Short-Term Tracking and Monitoring

### 6.1 Accuracy Metrics

**Position/Velocity Estimation Error:** Thompson et al. (Advanced Space) found that with short data arcs (approximately 21 days), state estimation achieved: 1-2 km position/1 cm/s velocity from NRHO observers; 400-500 m position/less than 1 cm/s from L2 halo observers; 2-3 km position/1-2 cm/s from L2 Lyapunov observers [3]. For the most capable optical cutoff (M = 14), angles-only measurements maintained custody of an RSO in an L2 halo orbit with a 3-sigma uncertainty of 1-2 km in position and less than 1 cm/s in velocity.

The 2:1 resonant orbit study using the UKF achieved final estimated uncertainties of 2.06 km in position and 1.51 cm/s in velocity using 56 right-ascension/declination measurements from global Earth sensors (limiting magnitude 20) [73]. The University of Arizona's Space4 Center has achieved GEO positional accuracy under 50 meters [21].

Current orbit determination accuracy in cislunar space is generally at the hundred-meter level, while incorporating inter-satellite links can improve the accuracy to the tens of meters [81]. Ground-based tracking limitations are severe: Chang'e 5 reconstruction achieved approximately 200 km radial uncertainty [3].

**Covariance Realism:** The U-D factorized covariance filter in JPL MONTE software was used for the Thompson et al. study. The Discrete Parameter Flow (DPF) method dramatically improves nonlinear inference for sparse measurement scenarios by partitioning the update into smaller linearization steps, preserving tail information from the prior [58]. The Stochastic Consider Parameters (SCP) model improves covariance realism by accounting for stochastic time-correlated errors while maintaining computational tractability [82].

### 6.2 Timeliness Metrics

**Latency from Observation to Updated Orbit Solution:** The Unified Data Library (UDL) provides less than 1 second latency from ingest to availability, and less than 20 seconds for replication across different classification levels [83]. General Saltzman at AMOS 2025 stated: "We cannot be satisfied if it takes us hours to detect on-orbit activity, and we definitely cannot be satisfied if full characterization of on-orbit events takes weeks and months" [84].

**Revisit Rates:** The SBV sensor increased revisit rates on militarily significant objects by 50% and helped reduce the list of lost satellites by 80% [85].

### 6.3 Coverage Metrics

**Volume Coverage Metrics:** The span of space that cislunar objects operate in is at least 10 times farther than GEO (36,000 km), giving a potential coverage volume of greater than 1,000 times [1]. The cislunar region is approximately nine times GEO altitude and 83 times larger in area [52].

**Gaps in Observational Coverage:** The "Cone of Shame" is a term coined by AFRL to designate the lunar exclusion zone, within which tracking objects with Earth-based sensors is particularly challenging [15][16].

**Time-to-Detect for New Objects:** In a GEO catalog maintenance scenario using the Poincaré map methodology, the network captured up to 34.37% of relevant targets within 24 hours through serendipitous acquisition [86].

### 6.4 Continuity Metrics

**Track Custody Duration:** Thompson et al. found that filters regularly diverged after 1.5-2 revolutions (21-28 days) when tracking L2 halo objects [3]. For objects in Earth orbit, an OD solution can be well-refined with relatively little data—a handful of optical observations or radar passes. This is not the case for cislunar orbits.

**Probability of Maintaining Track Through Maneuvers and Occultations:** The Bhadauria et al. study addresses maintaining custody of maneuvering objects in L2 Lyapunov and NRHOs, using dynamic departure tubes to identify critical surveillance regions for maneuver-induced departures (0.05 km/s to 0.5 km/s Δv) [52].

### 6.5 Knister's Performance Metrics

The AFIT thesis references Knister's performance metrics: Mean Detect Time, Mean Track Time, Mean Time Between Tracks [72].

### 6.6 Observability Metrics

The paper by Fowler, Hurtt, and Paley (AAS 20-575) evaluates orbit families for cislunar SDA missions and proposes metrics including heuristic metrics (angular interval, inavailability due to occultation/Sun exclusion, and range) and a numerical observability metric based on the condition number of the empirical local observability gramian [87]. Key findings: L2 halo target orbits are the most difficult to observe from all observer orbit families (condition numbers 19.9-20.4). L4 planar target orbits are the most observable (13.8-14.1) and perform well as observers in both single and two-observer cases. Heuristic metrics (range, angular interval, inavailability) do not consistently correlate with the numerical observability metric, as the latter captures underlying dynamics not reflected in purely geometric metrics.

### 6.7 How Metrics Differ from Traditional LEO/GEO SSA

The AFIT thesis states that traditional orbital regimes (LEO, GEO) and ground-based systems cannot provide consistent custody of cislunar targets [72]. For objects in Earth orbit, an OD solution can be well-refined with relatively little data—a handful of optical observations or radar passes. This is not the case for cislunar orbits [3]. TLEs (Two-Line Elements) are not a useful mechanism to keep catalogs, share trajectories, or task sensors in cislunar space [88]. Cislunar trajectories, such as the free-return trajectory developed for the Apollo missions, can easily be repurposed to hold near-Earth and terrestrial targets at risk while reducing the probability of detection and attribution [72].

---

## 7. Past and Ongoing Programs

### 7.1 NASA Programs

**Artemis Program:** The Artemis campaign aims to return humans to the Moon and eventually send crewed missions to Mars. Key missions include Artemis I (November 2022)—successful uncrewed test flight; Artemis II (April 2026)—first crewed flight around the Moon, with astronauts traveling 252,756 miles from Earth, setting a record for the greatest distance humans have traveled in space [89]. Artemis III is planned as a demonstration mission in LEO for 2027, and Artemis IV is the first Artemis lunar landing targeted for 2028. The Artemis Accords now include more than 60 countries.

**CAPSTONE Mission (2022-2026):** CAPSTONE is a NASA-funded CubeSat pathfinder mission developed and operated by Advanced Space under a $13.7 million contract [41]. It is the first spacecraft to operate in an NRHO around the Moon. CAPSTONE demonstrated autonomous navigation using the Cislunar Autonomous Positioning System (CAPS), involving two-way coherent signal communication for range and Doppler navigation measurements, and optical-only orbit determination using Moon's horizon imagery. NASA declared its mission complete on July 6, 2026, though Advanced Space continues operating the spacecraft as a technology testbed.

**National Cislunar Science & Technology Strategy (November 2022):** This is the first interagency strategy to guide U.S. government actions in Cislunar space [90]. The four objectives are: (1) Support research and development to enable long-term growth in Cislunar space; (2) Expand international S&T cooperation in Cislunar space; (3) Extend U.S. space situational awareness capabilities into Cislunar space; (4) Implement Cislunar communications and positioning, navigation, and timing capabilities with scalable and interoperable approaches.

### 7.2 DARPA Programs

**Hallmark Program:** DARPA's Hallmark program aims to develop breakthrough real-time space-domain awareness and command-and-control systems [91]. The Hallmark Software Testbed (Hallmark-ST), announced June 17, 2016, creates an advanced enterprise software architecture for a testbed that integrates real-time space-domain systems and capabilities. The testbed, called the Hallmark Space Evaluation and Analysis Capability (SEAC), supports modeling, simulation, realistic testing, and integration of external space command and control tools and data.

**LASSO Program (Lunar Assay via Small Satellite Orbiter):** DARPA announced a new program seeking proposals for prototype spacecraft capable of autonomous navigation and high maneuverability in low lunar orbit for cislunar SSA [43]. The goal is an affordable and scalable commercial capability that provides SSA for cislunar space.

### 7.3 U.S. Space Force Programs

**Oracle Family of Systems:** The Oracle Family of Systems comprises two AFRL programs—Oracle-Mobility (Oracle-M) and Oracle-Prime (Oracle-P) [39]. Oracle-M successfully completed the Hot Fire Test at Edwards AFB, California, from March 16-21, 2025, bringing the satellite to initial launch capability [40]. Oracle-Prime will operate near Earth-Moon L1, using a halo orbit to monitor space objects and debris. Launch is anticipated for 2026-2027, with a two-year lifespan.

**Space Force Cislunar Strategy (March 2026):** On March 17, 2026, the U.S. Space Force formalized its shift from theoretical interest to operational planning for cislunar space [92]. Thomas Ainsworth confirmed the service is actively integrating this domain into its core mission and acquisition frameworks. The Space Force is codifying these requirements into the "Objective Force" document, a long-term roadmap through 2040 envisioning sustained military presence. By 2028, the Space Force aims to deploy initial cislunar SDA sensors.

**Cislunar Coordination Office (April 2026):** The Space Force launched a new Cislunar Coordination Office to study how the Defense Department should operate in cislunar space in support of NASA's planned moon base [93]. Maj. Gen. Stephen Purdy announced the initiative at the Space Symposium on April 15, 2026, stating it stems from President Trump's December 2025 Executive Order on space superiority, which mandates initial elements of a permanent lunar outpost by 2030.

**Unified Data Library (UDL):** The UDL is a cloud-based data repository that ingests data from government and commercial sensors for space domain awareness [83]. The UDL transitioned from a prototype to an official program of record on November 13, 2024. The UDL provides less than 1 second latency from ingest to availability, and less than 20 seconds for replication across different classification levels. Data from the Oracle experiments will be available via the UDL.

**GEODSS GBOSS Upgrade:** The New Mexico GEODSS facility was the first to receive the Ground-Based Optical Sensor System (GBOSS) upgrade, which doubles the field of view, doubles search speed, and more than triples the sensitivity [34]. A second GEODSS facility in Hawaii completed the GBOSS upgrade in April 2026.

### 7.4 ESA Programs

**Space Safety Programme (S2P):** At the 2025 ESA ministerial council, member states committed €955 million for S2P over three years (a 30% budget increase) [76]. The programme focuses on space weather, planetary defense, and debris mitigation. Key missions include Hera (2024, asteroid probe), Draco (2027, satellite reentry study), ClearSpace-1 (2028, debris removal), Vigil (2031, space weather at L5), and NEOMIR (2030s, asteroid-detecting telescope).

**ESA's Cislunar SSA Expansion:** The ESPI study (July 2025) notes that Europe's engagement in cislunar SSA remains fragmented and reactive [77]. ESA has launched initiatives through its Space Safety Programme, including the proposed LEMO-TD demonstration mission for tracking cislunar objects.

### 7.5 Commercial Entities

**Advanced Space:** Advanced Space of Boulder, Colorado, developed and operates the CAPSTONE mission for NASA under a $13.7 million contract [41]. CAPSTONE is the first commercial spacecraft and first CubeSat to operate at the Moon. Advanced Space is also the prime contractor for the Oracle-Prime satellite.

**Commercial Market Growth:** The SSA market was valued at USD 1.83 billion in 2025, projected to reach USD 3.06 billion by 2032 (CAGR 7.6%) [94]. Novaspace estimated in May 2026 that cumulative global SSA spending could reach USD 61 billion over the next decade. Key commercial players include LeoLabs, Slingshot Aerospace, COMSPOC, GMV, Kayhan Space, Spaceflux, NorthStar Earth & Space, Lockheed Martin, Northrop Grumman, L3Harris, RTX, Leidos, Kratos Defense, and ExoAnalytic Solutions.

### 7.6 Chinese Lunar Programs

**Chang'e-5 (2020):** China's first automated lunar sample return mission, launched November 23, 2020 [95]. The 8.2-ton spacecraft collected approximately 1,731 grams of lunar samples. After its primary mission, the Chang'e 5 orbiter reached the Sun-Earth L1 Lagrange point in March 2021 and later entered a lunar distant retrograde orbit in February 2022, becoming the first spacecraft to utilize that orbit.

**Chang'e-6 (2024):** China's first sample return from the far side of the Moon, launched May 3, 2024 [96]. The lander successfully touched down on June 1, 2024, in the Apollo crater within the South Pole-Aitken basin. The relay satellite Queqiao-2 (launched March 2024) enables communication with the far side.

**Strategic Implications:** A National Security Space Association paper (August 2023) argues that China's space ambitions are a direct extension of its geopolitical competition with the U.S. [97]. Lagrange points, lunar transfer orbits, lunar orbits, and the Moon's surface are viewed as "strategic key points" and "strategic thoroughfares" in cislunar space. China has 1,189+ satellites in orbit (927% growth since 2015), with 510+ ISR-capable satellites.

### 7.7 Other International Programs

**Korea Pathfinder Lunar Orbiter (KPLO/Danuri):** South Korea's first lunar mission, launched on August 5, 2022, aboard a SpaceX Falcon 9 rocket [98]. Entered lunar orbit on December 26, 2022, with a circular polar orbit 100 km above the Moon's surface. Carries five Korean instruments and one U.S. instrument (ShadowCam—at least 200 times more sensitive than LRO's camera). Originally designed for a one-year mission, operational life extended to 2027.

**ISRO/JAXA LUPEX (Chandrayaan-5):** The Lunar Polar Exploration Mission (LUPEX), also called Chandrayaan-5, is a planned joint lunar mission by ISRO and JAXA to explore the south pole region of the Moon [99]. Launch is planned for 2028-2029 aboard a Japanese H3-24 rocket. The mission was approved by the Government of India on March 10, 2025.

---

## 8. Open Research Questions and Future Directions

### 8.1 Key Gaps in Current Cislunar SDA Capabilities

The United States does not have a dedicated SDA system capable of attributing spacecraft beyond GEO despite the increase in cislunar operations [72]. The ESPI study (July 2025) identifies that no dedicated SSA system exists to monitor/coordinate objects near the Moon, with chaotic orbits making tracking difficult [77].

The comprehensive review by Baker-McEvilly et al. (Progress in Aerospace Sciences, Volume 147, May 2024) concludes that the extensive observational infrastructure on Earth struggles to sufficiently cover all of Cislunar space due to the distance and challenging observational conditions [100]. The South Pole and Near-rectilinear Halo Orbit (NRHO) are identified as key regions of interest. Over 30 missions are expected in the next decade, many aimed at establishing a permanent lunar base.

The War on the Rocks article highlights that we lack situational awareness and effective frameworks for reasoning about this domain [22]. A Chinese rocket stage crashed into the Moon in March 2022, but the impact was not confirmed until nearly four months later due to no observation assets in position. China's Chang'e 5 spacecraft repositioned itself into a new lunar Lagrange point orbit over several months in 2021 without public announcement, detected only by amateur trackers using backyard equipment.

### 8.2 Catalog Maintenance and Correlation in the Cislunar Regime

The SSN catalog maintains 50,000+ objects in Earth orbit, but no equivalent catalog exists for cislunar space [25]. The National Cislunar S&T Strategy calls for developing an integrated Cislunar object catalog and publicly sharing SSA data through a civilian open data platform [90]. TLEs are not a useful mechanism to keep catalogs, share trajectories, or task sensors in cislunar space [88].

### 8.3 Autonomous Tracking and Onboard Orbit Determination

CAPSTONE demonstrated autonomous navigation using the Cislunar Autonomous Positioning System (CAPS) [41]. The unified orbit-attitude estimation framework uses a greedy mutual-information-based sensor tasking strategy with an error-state multiplicative UKF for autonomous cislunar SDA [24]. The DARPA LASSO program seeks prototype spacecraft capable of autonomous navigation and high maneuverability in low lunar orbit [43]. A simplified ephemeris method using Hermite interpolation for Sun and Moon positions was proposed for onboard autonomous orbit determination, reducing memory usage by approximately 60% while maintaining accuracy at the meter level [81].

### 8.4 Cislunar Space Traffic Management (STM) as Distinct from SDA

The Acta Astronautica article (Volume 229, April 2025, Pages 211-217) explores the unique challenges of managing space traffic in cislunar environments [79]. Key challenges include complex astrodynamics (CR3BP), unstable lunar orbits, communication delays, and gaps in PNT systems. The report calls for international cooperation and enhanced data sharing, recommending establishing an international civil agency to lead space traffic coordination. The Korea Aerospace Research Institute (KARI) has received 40 "red alarms" of potential collisions among spacecraft orbiting the Moon in the last 18 months, demonstrating the immediate need for cislunar STM [80].

### 8.5 Artificial Intelligence and Machine Learning for Cislunar SDA

The AMOS Technical Library lists 48 papers on ML for SDA Applications (2023-2025) [74]. Key themes include: Large Language Models (LLMs) and Agentic AI for SDA (benchmarking frameworks, command and control, multimodal data fusion), deep learning for detection and characterization (RSO detection using non-Earth imaging, ground-based EO sensors, real-time AI video processing), anomaly detection and pattern of life (autoencoder-based anomaly detection, hierarchical neuro-symbolic AI), reinforcement learning (autonomous scheduling for space-to-space surveillance, multi-agent inspection), physics-informed ML (uncertainty-aware PIML for cislunar orbit determination), and scheduling and optimization (genetic algorithm-driven radar scheduling).

The University of Arizona's Space4 Center is leveraging AI, machine learning, and light curves to better track and characterize objects in orbit in cislunar space [21]. The Space Force's Data and AI Strategic Action Plan focuses on improving data-sharing capabilities, integrating the UDL, and enhancing data and AI literacy across the workforce [101].

### 8.6 International Norms, Confidence-Building Measures, and Data Sharing

The 2013 UN GGE on TCBMs proposed measures including information exchange on space policies, orbital parameters, launch notifications, and risk reduction notifications [78]. The Artemis Accords now include more than 60 countries. The War on the Rocks article recommends developing shared situational awareness data systems with openness from the outset, creating new cartographic tools and updated terminology, and investing in transparency and coordination to prevent unnecessary conflict as lunar activity expands [22].

The Aerospace Corporation report recommends that the United States must take a leadership role in establishing and contributing to governance agreements and international norms of behavior to promote sustainable science, exploration, and resource utilization [102]. The Open Lunar Foundation primer on TCBMs notes that the key determinant in creating a set of lunar TCBMs lies in balancing collective interests of space security with the singular interest of each State [103].

### 8.7 Future Sensor Concepts

**Quantum Sensors:** NASA is developing quantum sensing technologies for space science, including quantum gravity gradiometers, atomic lunar seismometers, and atomic drag-free accelerometers [104]. The Cold Atom Lab on the ISS has been operational since 2018, demonstrating Bose-Einstein condensates in microgravity. The Deep Space Atomic Clock demonstrated fractional frequency stability of 3×10⁻¹⁵ at 23 days. Northrop Grumman is advancing quantum sensors including nuclear magnetic resonance gyroscopes, atomic clocks, Rydberg radio frequency receivers, and magnetometers, offering 10 to 100 times the accuracy of traditional sensors [105].

**Neuromorphic and Event-Based Vision Sensors:** AMOS 2025 papers include presentations on event-based vision sensors and neuromorphic cameras for SDA [74].

**Hyperspectral and Advanced Optical Sensors:** AMOS 2025 papers cover hyperspectral sensors, LiDAR, passive RF, and ISAR for space object characterization [74].

### 8.8 Sustainable Architectures: 2026-2036 Evolution

The Space Force's "Objective Force" document provides a long-term roadmap through 2040 envisioning sustained military presence providing PNT and telecommunications infrastructure [92]. By 2028, the Space Force aims to deploy initial cislunar SDA sensors, moving from planning to operational capability. The Cislunar Coordination Office will map government organizations involved in cislunar activities, build roadmaps for acquiring necessary technology, and partner with industry [93].

The comprehensive review by Baker-McEvilly et al. concludes that the Cislunar region is crucial for expanding human presence in space in the forthcoming decades [100]. Over 30 missions are expected in the next decade, many containing multiple payloads and experiments traveling to the Moon's surface and into Lunar orbit. Improved SDA is critical for safe operations as traffic increases, and SDA efforts should be focused on key regions of interest rather than the entire Cislunar volume.

---

## 9. Summary and Recommendations

### 9.1 Key Findings

1. **Fundamental Physics Limitations:** The vast scale of cislunar space (10,000 times the volume of GEO) and the inverse-square law for optical sensors and fourth-power law for radar create fundamental detection challenges that cannot be overcome by sensor improvements alone.

2. **Non-Keplerian Dynamics:** The CR3BP governs cislunar orbital dynamics, producing chaotic, non-repeating trajectories that render traditional two-body orbit determination methods ineffective. This is the single most significant technical challenge for cislunar SDA.

3. **Sensor Coverage Gaps:** The "Cone of Shame" and lunar exclusion zones create persistent blind spots for Earth-based sensors. No single sensor type or location can observe all of cislunar space.

4. **Emerging Space-Based Capabilities:** The Oracle Family of Systems (Oracle-M and Oracle-Prime) represents the first dedicated U.S. space-based cislunar SDA capability, with Oracle-Prime planned for launch in 2026-2027.

5. **Algorithmic Advances:** New methods including Discrete Parameter Flow filtering, Adaptive Gaussian Mixture filters, Physics-Informed Machine Learning, and the Quadratic Shift-and-Stack technique are addressing the unique challenges of cislunar tracking.

6. **Constellation Design Progress:** Research on MILP-based constellation design, PSO optimization, and 2:1 resonance orbits provides a foundation for future cislunar surveillance architectures.

7. **International Dimension:** There is no dedicated cislunar SSA system for tracking objects near the Moon. The ESPI study warns that "whoever builds the first systems and frameworks around the Moon will have the most influence in setting the 'rules of the road.'"

8. **Urgent Need for STM:** With 40 collision alerts already received by KARI in the last 18 months, cislunar space traffic management is an immediate operational requirement, not a future concern.

### 9.2 Priority Actions for Effective Cislunar SDA

1. **Deploy Space-Based Sensors:** Given the fundamental limitations of ground-based sensors for cislunar detection, space-based sensors positioned at Lagrange points (particularly L1 and L2) and in NRHOs are essential for achieving persistent cislunar SDA.

2. **Develop Cislunar-Specific Algorithms:** Investment in IOD, filtering, and data fusion methods specifically designed for CR3BP dynamics is critical. Traditional two-body methods consistently fail in cislunar regimes.

3. **Establish a Cislunar Object Catalog:** A dedicated, shared catalog of cislunar RSOs, analogous to the SSN catalog for Earth orbit, is urgently needed. This should include both government and commercial contributions.

4. **Implement Autonomous Tracking:** Given communication delays, space-based sensors must be capable of autonomous onboard orbit determination and sensor tasking.

5. **Foster International Cooperation:** Cislunar SDA requires international coordination on data sharing, norms of behavior, and STM frameworks. The Artemis Accords provide a foundation, but specific cislunar SDA agreements are needed.

6. **Focus on Key Regions:** Rather than attempting to cover all of cislunar space, SDA efforts should prioritize key regions of interest: the lunar South Pole, NRHOs, Lagrange points, and major transfer corridors.

7. **Invest in Sensor Fusion:** The integration of heterogeneous sensor data (optical, radar, RF) across multiple platforms (ground-based, space-based, lunar surface) is essential for comprehensive SDA.

8. **Accelerate ML/AI Integration:** Machine learning methods for orbit determination, anomaly detection, and sensor tasking show significant promise for cislunar SDA and should be prioritized for operational transition.

---

### Sources

[1] a.i. Solutions, "What is Cislunar Space?": https://ai-solutions.com/newsroom/overcoming-observation-obstacles-in-cislunar-space-for-safe-and-successful-exploration

[2] Frueh, Howell, Demars, Bhadauria, "CISLUNAR SPACE SITUATIONAL AWARENESS": https://www.semanticscholar.org/paper/CISLUNAR-SPACE-SITUATIONAL-AWARENESS-Frueh-Howell/f9bf4df3a676290d169cbb1e40ab5c9df8ae511a

[3] Thompson et al., "Cislunar Orbit Determination and Tracking via Simulated Space-Based Optical Measurements," Advanced Space: https://s3.us-west-2.amazonaws.com/advspace.publicshare/Thompson+-+Simulated+Optical+Measurements+for+Cislunar+OD.pdf

[4] DataIntelo, "Cislunar SSA Radar and Optical Sensing Market Research Report 2034": https://dataintelo.com/report/cislunar-ssa-radar-and-optical-sensing-market

[5] Rodriguez-Alvarez et al., "The Improved Capabilities of the Goldstone Solar System Radar Observatory," IEEE Transactions on Geoscience and Remote Sensing, 2022: https://www.semanticscholar.org/paper/f8fc9155165c1ce53b2cb3cbd73f488a1a7312a0

[6] mostlymissiledefense, "Space Surveillance Sensors: GEODSS System": https://mostlymissiledefense.com/2012/08/20/space-surveillance-sensors-geodss-ground-based-electro-optical-deep-space-surveillance-system-august-20-2012

[7] Ross, S., "Cislunar Space: 3-Body Model of Orbital Dynamics Beyond the Geosynchronous Belt (xGEO)": https://www.youtube.com/watch?v=gpXAACF5eOI

[8] Weber, "Circular Restricted Three-Body Problem": https://orbital-mechanics.space/the-n-body-problem/circular-restricted-three-body-problem.html

[9] Wilmer, Bettinger, Little, "Cislunar Periodic Orbits for Earth–Moon L1 and L2 Lagrange Point Surveillance," Journal of Spacecraft and Rockets, November 2022: https://scholar.afit.edu/facpub/2382

[10] Paul, Fan, Panfil, "Advancing Cislunar Space Domain Awareness Through Robust Optimization Framework for Optical Sensors-Based Autonomous Satellite Systems," AIAA SciTech 2025 Forum: https://arc.aiaa.org/doi/10.2514/6.2025-1218

[11] Schwab, D., "Cislunar Transport Characterization for Space Situational Awareness," Doctoral Dissertation, Pennsylvania State University, 2023: https://etda.libraries.psu.edu/catalog/21986dvs5558

[12] Breaking Defense, "AFRL Satellite To Track Up To The Moon; Space Force-NASA Tout Cooperation": https://breakingdefense.com/2020/09/afrl-satellite-to-track-up-to-the-moon-space-force-nasa-tout-cooperation

[13] arXiv, "Cislunar State and Uncertainty Propagation via the Modified Generalized Equinoctial Orbital Elements": https://arxiv.org/html/2603.20110v1

[14] GMV, TU Darmstadt, ESA, "Beyond GEO: Strategies for monitoring cislunar environment," 9th European Conference on Space Debris, 2025: https://conference.sdo.esoc.esa.int/proceedings/sdc9/paper/258

[15] Shimane, Tomita, Ho, "Cislunar Space Situational Awareness Constellation Design and Planning with Facility Location Problem" (arXiv preprint): https://arxiv.org/html/2408.06238v4

[16] Shimane, Tomita, Ho, "Cislunar Space Situational Awareness Constellation Design and Planning with Facility Location Problem," Journal of Spacecraft and Rockets, Vol. 62, Issue 6, June 2025: https://arc.aiaa.org/doi/10.2514/1.A36361

[17] TAMZ UMD, "Cislunar Detection and Tracking | Strategic Space Sensing": https://tamz.umd.edu/project/rapid_disco

[18] Chen et al., "Quadratic Shift-and-stack for Ground-based Optical Detection of Faint Cislunar Objects," The Astronomical Journal (2026): https://iopscience.iop.org/article/10.3847/1538-3881/ae883c/pdf

[19] Chen et al., "Quadratic shift-and-stack for Ground-Based Optical Detection of Faint Cislunar Objects" (arXiv preprint): https://arxiv.org/pdf/2603.26427

[20] JPL/NASA, "Cis-lunar Space Debris Radar and Advanced Signal Processing": https://www.jpl.nasa.gov/site/research/media/posters/2023/R20045p.pdf

[21] University of Arizona, "Space Domain Awareness | National Security Initiatives": https://nationalsecurity.arizona.edu/focus-areas/space-domain-awareness

[22] Schingler, Samson, Raju, "Don't Delay Getting Serious About Cislunar Security," War on the Rocks: https://warontherocks.com/dont-delay-getting-serious-about-cislunar-security

[23] "Adaptive Sensor Tasking Strategies for Tracking Non-Cooperative Cislunar Space Objects," AMOS 2024: https://ui.adsabs.harvard.edu/abs/2024amos.conf...79C/abstract

[24] "Unified Orbit-Attitude Estimation and Sensor Tasking Framework for Autonomous Cislunar Space Domain Awareness Using Multiplicative Unscented Kalman Filter": https://arxiv.org/html/2603.20579

[25] United States Space Surveillance Network - Wikipedia: https://en.wikipedia.org/wiki/United_States_Space_Surveillance_Network

[26] Petion and Jones, "Cislunar Admissible Regions from Periodic Orbit Manifolds," AMOS 2025: https://amostech.space/year/2025/cislunar-admissible-regions-from-periodic-orbit-manifolds

[27] Vera C. Rubin Observatory - Wikipedia: https://en.wikipedia.org/wiki/Vera_C._Rubin_Observatory

[28] SPIE, "Efficient detection of faint geostationary and cislunar objects in Rubin LSST imagery": https://spie.org/astronomical-telescopes-instrumentation/presentation/Efficient-detection-of-faint-geostationary-and-cislunar-objects-in-Rubin/14155-40

[29] SLAC, "NSF-DOE Vera C. Rubin Observatory News Collection": https://www6.slac.stanford.edu/lsst

[30] Zwicky Transient Facility - Wikipedia: https://en.wikipedia.org/wiki/Zwicky_Transient_Facility

[31] ZTF, "ZTF Experiments": https://www.ztf.caltech.edu/ztf-experiments.html

[32] Space Surveillance Telescope - Wikipedia: https://en.wikipedia.org/wiki/Space_Surveillance_Telescope

[33] DARPA, "SST: Space Surveillance Telescope": https://www.darpa.mil/research/programs/space-surveillance-telescope

[34] U.S. Space Force, "Ground-Based Electro-Optical Deep Space Surveillance Fact Sheet": https://www.spaceforce.mil/about-us/fact-sheets/article/2197760/ground-based-electro-optical-deep-space-surveillance

[35] Slingshot Aerospace, "Safeguarding the Final Frontier: Optical Sensors for Persistent Space Domain Awareness": https://www.slingshot.space/news/why-optical

[36] MIT Lincoln Laboratory, "Haystack Ultrawideband Satellite Imaging Radar": https://www.ll.mit.edu/r-d/projects/haystack-ultrawideband-satellite-imaging-radar

[37] LeoLabs, "LeoLabs Achieves Record Bookings in 2025": https://leolabs.space/press/leolabs-achieves-record-bookings-in-2025-fueled-by-triple-digit-growth-in-u-s-government-contracts

[38] Chinese Deep Space Network - Wikipedia: https://en.wikipedia.org/wiki/Chinese_Deep_Space_Network

[39] Advanced Space, "Oracle": https://advancedspace.com/oracle

[40] Space Systems Command, "Oracle-M Hot Fire Test: A Major Milestone in Cislunar Space Situational Awareness and National Security": https://www.ssc.spaceforce.mil/newsroom/article-display/article/4176371/oracle-m-hot-fire-test-a-major-milestone-in-cislunar-space-situational-awarenes

[41] CAPSTONE - Wikipedia: https://en.wikipedia.org/wiki/CAPSTONE

[42] University of Maryland, "Cislunar Detection and Tracking (FaXT)": https://tamz.umd.edu/project/rapid_disco

[43] Defense Daily, "DARPA Program Seeks Autonomous, Maneuverable Satellites for Cislunar Domain Awareness": https://www.defensedaily.com/darpa-program-seeks-autonomous-maneuverable-satellites-for-cislunar-domain-awareness/space

[44] Aerospace America, "U.S. Air Force awards grant for cislunar constellation to track spacecraft and debris": https://aerospaceamerica.aiaa.org/u-s-air-force-awards-grant-for-cislunar-constellation-to-track-spacecraft-and-debris

[45] Shimane, Tomita, Ho, "Cislunar Space Situational Awareness Constellation Design and Planning with Facility Location Problem" (arXiv): https://arxiv.org/html/2408.06238v4

[46] SpaceNews, "Chinese scientists outline major cislunar space infrastructure project": https://spacenews.com/chinese-scientists-outline-major-cislunar-space-infrastructure-project

[47] "HALO: A High-Precision Orbit Propagation Tool for Mission Design in the Cis-Lunar Domain": https://arxiv.org/html/2410.03372v1

[48] Albidah, A. B., & Abdullah, "Halo Orbits under Some Perturbations in cr3bp," Symmetry, Volume 15, Issue 2, 481, 2023: https://www.mdpi.com/2073-8994/15/2/481

[49] Wikipedia, "Near-rectilinear halo orbit": https://en.wikipedia.org/wiki/Near-rectilinear_halo_orbit

[50] Zimovan, E., Howell, K., & Davis, D., "IAA-AAS-DyCoSS3-125 Near Rectilinear Halo Orbits and Their Application in Cis-Lunar Space," Purdue University, 2017: https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2017_IAA_ZimHowDav.pdf

[51] Li, S., Wang, W., Pu, J., Guo, P., & Li, X., "Simultaneous Estimation of Lunar Ephemeris and Satellite Orbits Using a DRO-Based LiAISON Method in Cislunar Space," NAVIGATION, Volume 73, Issue 1, 2026: https://navi.ion.org/content/73/1/navi.766

[52] Bhadauria, S., Black, A., & Frueh, C., "Cislunar Key Region Surveillance Optimization," The Journal of the Astronautical Sciences, Volume 72, Article 51, September 24, 2025: https://link.springer.com/article/10.1007/s40295-025-00522-6

[53] "HALO: A High-Precision Orbit Propagation Tool for Mission Design in the Cis-Lunar Domain": https://arxiv.org/html/2410.03372v1

[54] "Probabilistic Methods for Initial Orbit Determination and Orbit Determination in Cislunar Space": https://arxiv.org/html/2602.18058v1

[55] Patel, M., Tomita, K., & Ho, K., "Concurrent Optimization of Satellite Phasing and Tasking for Cislunar Space Situational Awareness," The Journal of the Astronautical Sciences, Volume 72, Article 50, 2025: https://link.springer.com/article/10.1007/s40295-025-00520-8

[56] AGI/Ansys, "Batch vs. Sequential estimation methods in Orbit Determination": https://www.agi.com/missions/space-operations-missions/batch-vs-sequential-estimation-methods-in-orbit-de

[57] Iannamorelli, J. L., & LeGrand, K. A., "Adaptive Gaussian Mixture Filtering for Multi-sensor Maneuvering Cislunar Space Object Tracking," The Journal of the Astronautical Sciences, Volume 72, Article 2, 2025: https://link.springer.com/article/10.1007/s40295-024-00478-z

[58] Fife, D., DeMars, K., & Fritsch, R., "AAS 25-582 Discrete Parameter Flow Filtering for Recursive Bayesian Inference Applied to Cislunar Orbit Determination," AAS/AIAA Space Flight Mechanics Meeting, 2025: https://s3.amazonaws.com/amz.xcdsystem.com/A464D031-C624-C138-7D0E208E29BC4EDD_abstract_File25843/PreprintPaperUpload_582_0722084936.pdf

[59] Hippelheuser, J. E. Jr., "A Novel Multi-Observer Orbit Determination and Estimation Framework for Cislunar Space Domain Awareness," Doctoral Dissertation, University of Central Florida, 2023: https://stars.library.ucf.edu/etd2023/249

[60] Dinh, K., Scheeres, D., & Holzinger, M., "Cislunar Initial Orbit Determination Using Sensor and Measurement-Centric Admissible Regions," AMOS Technologies Conference, September 2024: https://ui.adsabs.harvard.edu/abs/2024amos.conf...64D/abstract

[61] Smego, L., & Christian, J., "Dynamic Triangulation for Cislunar Initial Orbit Determination," The Journal of the Astronautical Sciences, Volume 73, Article 14, 2026: https://link.springer.com/article/10.1007/s40295-025-00553-z

[62] Song, M., Wang, Y., Zheng, W., & Wang, Y., "Cislunar initial orbit determination for angles-only short arcs based on multi-constrained optimization," Aerospace Science and Technology, Volume 175, 2026: https://www.sciencedirect.com/science/article/abs/pii/S1270963826003792

[63] "Initial Orbit Determination from Ephemeris Models: Accurate Reconstruction of Maneuvering Cislunar Orbits Using Nonlinear Programming," AMOS Conference, September 2025: https://ui.adsabs.harvard.edu/abs/2025amos.conf...60H/abstract

[64] "Machine Classifier for Cislunar Orbit Determination (MCCLOD)," Journal of the Astronautical Sciences, September 2025: https://ui.adsabs.harvard.edu/abs/2025JAnSc..72...45O/abstract

[65] "A Novel Initial Orbit Determination Algorithm for Cislunar Objects Using Three Angle-Only Measurements," Embry-Riddle Aeronautical University: https://arxiv.org/html/2507.22350v1

[66] Scorsoglio, A., D'Ambrosio, A., Ghilardi, L., Furfaro, R., & Reddy, V., "Physics-Informed Orbit Determination for Cislunar Space Applications," AMOS Technologies Conference, 2023: http://ui.adsabs.harvard.edu/abs/2023amos.conf....1S/abstract

[67] "Uncertainty-Aware Physics-Informed Machine Learning (PIML) for Cislunar Orbit Determination," AMOS Conference, 2025: https://amostech.com/TechnicalPapers/2025/Machine-Learning-for-SDA-Applications/Badura.pdf

[68] Li et al., "Intelligent classification algorithm for cislunar trajectories integrating deep neural networks and constraint admissible region (CNN-CAR)," Journal of Image and Graphics, Volume 30, No. 9, 2025: https://pure.bit.edu.cn/en/publications/融合深度神经网络与约束容许域的地月空间航迹智能分类

[69] Hussain et al., "Space-based debris trajectory estimation using vision sensors and track-based data fusion techniques," Acta Astronautica, Volume 229, April 2025, Pages 814-830: https://www.sciencedirect.com/science/article/pii/S0094576525000396

[70] BANALA MANASWINI, "Space Domain Awareness Architecture for Cislunar and Deep‑Space Operations" (2025): https://www.academia.edu/144646110/Space_Domain_Awareness_Architecture_for_Cislunar_and_Deep_Space_Operations

[71] Klonowski, Owens-Fahrner, Heidrich, Holzinger, "Cislunar Space Domain Awareness Architecture Design and Analysis for Cooperative Agents," Journal of the Astronautical Sciences, October 2024: https://ui.adsabs.harvard.edu/abs/2024JAnSc..71...47K/abstract

[72] Major Benjamin R. Williams (USSF), "Applied Agile Digital Mission Engineering for Cislunar Space Domain Awareness" (AFIT-ENY-MS-22-M317, March 24, 2022): https://apps.dtic.mil/sti/pdfs/AD1175638.pdf

[73] Fru, Howell, et al., "SURVEILLANCE THROUGH EARTH-MOON RESONANCE ORBITS," Purdue University, 2021 ESA Conference: https://engineering.purdue.edu/people/kathleen.howell.1/Publications/Conferences/2021_ESA_FruHowDeMBhaGup.pdf

[74] AMOS Technical Library – Machine Learning for SDA Applications: https://amostech.space/track/machine-learning-for-sda-applications

[75] Block, Curtis, Bettinger, Wilmer, "Cislunar SDA with Low-Fidelity Sensors and Observer Uncertainty," 2022 AMOS Conference: https://scholar.afit.edu/facpub/2473

[76] Space Safety Programme - Wikipedia: https://en.wikipedia.org/wiki/Space_Safety_Programme

[77] ESA Blogs, "Towards a Safe and Sustainable Cislunar Space": https://blogs.esa.int/spacesafety-community/2025/07/17/towards-a-safe-and-sustainable-cislunar-space

[78] "Building Measures in Outer Space Activities," UN GGE Report, 2013: https://digitallibrary.un.org/record/796132/files/SS-34.pdf

[79] Anilkumar et al., "Moon to Mars: Challenges and strategic frameworks for space traffic management in cislunar and cismartian environments," Acta Astronautica, Volume 229, April 2025, Pages 211-217: https://www.sciencedirect.com/science/article/abs/pii/S0094576524008051

[80] Barakat & Kezirian, "Establishing requirements for lunar and cislunar orbital debris tracking," Journal of Space Safety Engineering, Volume 11, Issue 3, September 2024, Pages 446-453: https://www.sciencedirect.com/science/article/abs/pii/S2468896724001198

[81] Lv et al., "Precise Orbit Determination for Cislunar Space Satellites: Planetary Ephemeris Simplification Effects," Aerospace (MDPI, August 2025): https://www.mdpi.com/2226-4310/12/8/716

[82] Cano, A., Pastor, A., & Escobar, D., "Covariance determination for improving uncertainty realism," 8th European Conference on Space Debris, ESA Space Debris Office, GMV, 2021: https://conference.sdo.esoc.esa.int/proceedings/sdc8/paper/224

[83] "How the Unified Data Library (UDL) Will Help the U.S. Air Force," Kratos: https://www.kratosspace.com/constellations/articles/how-the-unified-data-library-will-help-the-us-air-force

[84] 2025 AMOS Conference Highlights: https://amostech.com/the-2025-amos-conference-highlights-collaboration-and-partnerships

[85] Space Based Space Surveillance - USSF Fact Sheet: https://www.spaceforce.mil/About-Us/Fact-Sheets/Fact-Sheet-Display/Article/2197743/space-based-space-surveillance

[86] "Enhancing Ground-Based Cislunar SDA: Reducing Search Area for Monitoring Small-Maneuver Earth Return Trajectories Using Poincaré Maps," AMOS 2025: https://ui.adsabs.harvard.edu/abs/2025amos.conf..143S/abstract

[87] Fowler, Hurtt, Paley, "Observability Metrics for Cislunar SDA," AAS 20-575, University of Maryland: https://cdcl.umd.edu/papers/aas21.pdf

[88] "Space Situational Awareness Market – 2026 Report," Strategic Market Research: https://www.strategicmarketresearch.com/market-report/space-situational-awareness-market

[89] NASA Artemis Program: https://www.nasa.gov/humans-in-space/artemis

[90] National Cislunar Science & Technology Strategy (November 2022), White House OSTP: https://smad.com/wp-content/uploads/2023/03/National-Cislunar-Science-and-Technology-Strategy.pdf

[91] DARPA Hallmark Program: https://www.darpa.mil/research/programs/hallmark

[92] "Space Force Formalizes Cislunar Strategy Amid Acquisition Restructuring," SatNews, March 18, 2026: https://satnews.com/2026/03/18/space-force-formalizes-cislunar-strategy-amid-acquisition-restructuring

[93] "With eyes on future NASA moon base, Space Force launches cislunar acquisition task force," Breaking Defense, April 2026: https://breakingdefense.com/2026/04/with-eyes-on-future-nasa-moon-base-space-force-launches-cislunar-acquisition-task-force

[94] 360iResearch, "Space Situational Awareness Market Size & Share 2026-2032": https://www.360iresearch.com/library/intelligence/space-situational-awareness

[95] Chang'e 5 - Wikipedia: https://en.wikipedia.org/wiki/Chang%27e_5

[96] "China's moon mission Chang'e-6: Here's what to know," Ad Astra Space: https://www.adastraspace.com/p/china-chang-e-6

[97] "Strategic Implications of China's Cislunar Space Activities," NSSA, August 2023: https://nssaspace.org/wp-content/uploads/2023/08/Strategic-Implications-of-Chinas-Cislunar-Space-Activities-8.21-final.pdf

[98] Korea Pathfinder Lunar Orbiter (KPLO) Mission: https://ode.rsl.wustl.edu/mars/pagehelp/Content/Missions_Instruments/Korea%20Pathfinder%20Lunar%20Orbiter%20(KPLO)/Intro.htm

[99] Lunar Polar Exploration Mission (LUPEX/Chandrayaan-5) - Wikipedia: https://en.wikipedia.org/wiki/Lunar_Polar_Exploration_Mission

[100] Baker-McEvilly et al., "A comprehensive review on Cislunar expansion and space domain awareness," Progress in Aerospace Sciences, Volume 147, May 2024: https://www.sciencedirect.com/science/article/abs/pii/S0376042124000459

[101] "New Space Force plan charts path for enhanced Unified Data Library," DefenseScoop, March 2025: https://defensescoop.com/2025/03/19/space-force-data-artificial-intelligence-strategic-action-plan-udl

[102] Bukley & Stover, "MOONSTRUCK! INTERNATIONAL ASPIRATIONS IN CISLUNAR SPACE," The Aerospace Corporation, October 2024: https://csps.aerospace.org/sites/default/files/2024-10/06d_Moonstruck_Bukley-Stover_20241022_0.pdf

[103] "Transparency and Confidence Building for the Moon - A Primer," Open Lunar Foundation: https://www.openlunar.org/blog/transparency-and-confidence-building-for-the-moon-a-primer

[104] "Quantum sensing for NASA science missions," EPJ Quantum Technology, 2025: https://pmc.ncbi.nlm.nih.gov/articles/PMC12095411

[105] "How Quantum Sensors are Revolutionizing the Future of Navigation and Defense," Northrop Grumman: https://www.northropgrumman.com/what-we-do/mission-solutions/quantum/revolutionizing-navigation-and-defense
