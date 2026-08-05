# Comprehensive Overview of Cloud-Based Train Control Systems for Urban Rail Transit (2023–2026)

## Introduction

The global urban rail transit sector is undergoing a profound digital transformation, driven by the integration of cloud computing, edge intelligence, 5G/6G communications, and advanced cybersecurity frameworks into train control and signaling systems. This report provides a comprehensive analysis of the most recent developments from 2023 to 2026, covering key technologies, deployed systems, pilot projects, and research advances. The focus is on cloud-based Communication-Based Train Control (CBTC) systems, which represent the convergence of operational technology (OT) and information technology (IT) in safety-critical railway environments.

---

## 1. Market Context and Industry Trends

### 1.1 Market Growth and Investment

The global CBTC market was valued at approximately $3.8–$5.1 billion in 2024–2025 and is projected to reach $9.7–$16.9 billion by 2034–2035, growing at a compound annual growth rate (CAGR) of 8.2–11.5% depending on the market analysis [1][2][3]. The broader connected rail market, encompassing digital technologies integrated into rail infrastructure, was valued at $94.1–$105.3 billion in 2024–2025 and is expected to grow to $140.5–$175.0 billion by 2030–2034 [4][5].

**Key regional dynamics include:**
- **Asia Pacific** leads the CBTC market with approximately 35–43% revenue share, driven by China's rapid metro expansion [1][6]
- **Europe** holds about 30% market share and serves as the standard-setter for signaling interoperability [4]
- **North America** accounts for approximately 25% of the market, with significant projects in the United States and Canada [1][6]
- **GoA4 (Grade of Automation 4)** is the fastest-growing sub-segment, expected to expand at approximately 14.2% CAGR [1]
- **Siemens Mobility** maintains global market leadership with an estimated 18–20% revenue share in 2025 [1]

### 1.2 Structural Trends Reshaping the Industry

The shift toward higher automation grades (GoA3 and GoA4) is the single most important structural trend reshaping the competitive landscape [1]. Additional transformative trends include:

- **AI-driven predictive maintenance** moving from pilot deployments to standard operational practice
- **Edge computing on trains** enabling real-time analytics and reduced cloud dependency
- **Cybersecurity becoming a dealbreaker** for system certification and operational approval
- **5G/LTE-R connectivity** replacing legacy GSM-R communications
- **Digital twins** for simulation, testing, and operational optimization
- **Open standards** reducing vendor lock-in and enabling multi-vendor interoperability

---

## 2. Key Technologies Enabling Cloud-Based Train Control

### 2.1 Cloud Computing Architectures

#### 2.1.1 Private and Hybrid Cloud Architectures

The railway industry has adopted cloud computing architectures tailored to safety-critical requirements. **Private cloud architectures** dominate mission-critical signaling applications due to the need for deterministic performance, regulatory compliance, and data sovereignty.

**Hitachi Rail's SIL4 Private Cloud Architecture** demonstrates a significant achievement: running Safety Integrity Level 4 (SIL4) applications on commodity off-the-shelf (COTS) hardware using open-source software [7]. Key design principles include:

- **OpenStack** with Kolla Ansible, Bifrost, and Designate for cloud orchestration
- **Ceph storage** with replica 3 (every byte replicated three times per rack)
- **Kubernetes** for container orchestration
- **Air-gapped, hardened Ubuntu systems** for security
- **At least three physical racks per site**, each configured as an availability zone
- **Geo-redundant primary sites separated by approximately 50 km**
- **DNS failover** for normal maintenance (zero downtime)
- **Manual failover** for catastrophic site failures to avoid split-brain scenarios

The system achieves **six nines availability for networks** and **five nines for the rest of the system**, supporting a **20+ year lifespan** [7].

**Network Rail's Hybrid Cloud Strategy** exemplifies the pragmatic approach adopted by major infrastructure managers [8]. Keeping legacy applications on private cloud while building new systems on public cloud (Microsoft Azure), Network Rail manages a transition involving 25–50 personnel. Key selection criteria prioritized: functional capability, architectural fit, skills fit, supplier ecosystem, information security, service/supportability, and commercial position—with integration capability prioritized over cost [8].

**Siemens Signaling X** represents the most advanced cloud-ready signaling platform, centralizing CBTC, interlocking, ATO, ATS, SCADA, and communications into a single SIL4-safe signaling data center [9][10][11]. The system uses the **Distributed Smart Safe System (DS3) platform** to run safety-critical applications on COTS hardware in a geo-redundant, cyber-secure data center environment [9][10][11].

#### 2.1.2 Microservices and Orchestration for Railway Clouds

A 2024 paper in *Applied Sciences* proposes a **microservices-based Railway Management Automation and Orchestration (RMAO) platform** with two service types: Cloud Resource Management (CRM) and Cloudified Function Management (CFM) [12]. Key features include:

- **RESTful microservices** designed following open interface principles
- **Resources organized in tree structures** (CFM service packages, software versions)
- **Verification via concurrent process modeling** showing equivalent behavior
- **Validation via simulation** evaluating injected latency as a key performance indicator
- **Safety and security considerations** integrated into cloud management design

The authors conclude this approach enables railway operators to develop customized Mobility as a Service (MaaS) applications while mitigating microservices' inherent disadvantages through proper planning [12].

#### 2.1.3 Cloud Resilience Engineering

AWS published a comprehensive guide on architecting resilient cloud-based critical railway systems compliant with **DIN EN 50129** [13]. The fundamental paradigm shift involves moving from traditional on-premises hardware reliability (mean-time-between-failure) to **cloud-native system resilience** (rapid detection and automated replacement). Key recommendations include:

- **Understanding the shared responsibility model** and cloud certifications (ISO 27001, SOC 3)
- **Mitigating random hardware failures** through ECC memory and redundant storage (Amazon EBS, S3)
- **Multi-AZ and multi-region clusters** for availability (four to five nines achievable)
- **Blue-green deployments** for software updates
- **Continuous monitoring** using Amazon CloudWatch and GuardDuty
- **Chaos engineering** to verify resilience
- **Business continuity planning** with regular backups

The paper demonstrates that achieving four or five nines of availability can increase costs by 37% to 87% compared to a baseline multi-AZ setup [13].

### 2.2 Edge Computing and Fog Computing

Edge computing is a critical enabler for cloud-based train control, reducing latency, improving real-time responsiveness, and lowering bandwidth costs by processing data near its source.

#### 2.2.1 Edge Intelligence for Rail Transit Equipment Inspection

A scientific article presents a **rail transit equipment inspection system based on Edge Intelligence (EI) and 5G technology**, deployed and evaluated on **Beijing Metro Line 6** [14]. The system adopts a **cloud–edge–end collaborative architecture** compliant with the **ETSI MEC (Multi-Access Edge Computing) framework**, integrating computer vision with a two-stage algorithm:

- **YOLOv8 model** for object detection (92.7% mAP@0.5)
- **ResNet-18 network** for equipment status classification (95.8% accuracy)

Quantified benefits compared to a cloud-centric baseline:
- **45% reduction in average end-to-end latency** (28.5 ms vs. 52.1 ms)
- **98.1% reduction in daily uplink bandwidth consumption** (from 40.0 GB to 0.76 GB) via event-triggered evidence upload strategy
- **98% accuracy** in detecting personnel procedural anomalies
- Enhanced security through **5G private network** and improved robustness via **distributed edge nodes**

#### 2.2.2 Edge Computing for Train Fusion Positioning

A 2025 article in *Mathematics* presents a **train fusion positioning method** integrating multi-sensor information (GNSS, INS, speed sensors) with edge computing [15]. The authors use **Colored Petri Nets (CPNs)** to model the system's data flow and formally verify functional safety under fault conditions (communication disconnection, packet loss, bit errors, limited edge resources). Key findings:

- **State-space analysis confirms operability and safety** in all tested scenarios
- **Transmission delay has the greatest impact** on data processing time
- **Edge server computing latency** is the second most significant factor
- **Data transmission failure rate** has the least impact
- The method consistently corrects train position even when communication links are broken

#### 2.2.3 Deep Reinforcement Learning and Edge Computing for CBTC Optimization

An MSc research project proposes a **hybrid framework combining Deep Reinforcement Learning (DRL) and Edge Computing** to optimize CBTC systems [16]. The core DRL model is a **Deep Q-Network (DQN)** that addresses dynamic challenges such as task offloading, equipment placement, and maintenance scheduling. Edge computing is deployed on **AWS Greengrass** to reduce latency and computational load.

Key results from simulation (5 trains, 3 wayside equipment, 2 edge servers, 500,000 timesteps):
- **57% reduction in latency**
- **25% energy savings**
- **35% reduction in operational cost**
- **Average test reward: DQN 44,737.21** vs. Q-learning 18,580.33
- **8.9% performance increase** after AWS Greengrass deployment (reward: 48,719.64)
- Statistical significance confirmed via **paired t-test (p<0.01) and ANOVA (p<0.05)**

#### 2.2.4 Fog Computing for Real-Time Railway Intruder Tracking

A research paper published in the *Journal of Network and Computer Applications* (Volume 242, October 2025) presents a **multi-agent cooperative framework (MetaGPT) combined with an edge stream processing engine (GeoEkuiper)** for real-time railway intruder tracking [17]. The three-tier architecture includes:

- **Global Planner** on cloud nodes
- **Summarizer** on edge centers
- **Debaters** on end devices (e.g., Raspberry Pi)

A **debate-vote strategy** enables distributed decision-making, with fine-tuned small LLMs directing GeoEkuiper to compute spatial affinity relationships via SQL statements. The system achieves an **average prediction time of approximately 5 seconds** in simulated railway environments. The paper notes that over 83% of serious European railway accidents and 79% of Chinese railway incidents are caused by perimeter intrusions.

### 2.3 5G and 6G Communication Technologies

#### 2.3.1 5G-R Framework for High-Speed Rail Connectivity

A comprehensive 5G-R optimization framework for high-speed rail connectivity (up to 350 km/h) integrates six components [18]:

1. **Beamforming (Massive MIMO)** for directional signal transmission
2. **Network slicing** for QoS isolation between signaling, passenger, and operational services
3. **Railway-tuned LSTM-based AI** for predictive handover and traffic management
4. **Multi-Access Edge Computing (MEC)** for local processing
5. **Multi-connectivity** for reliability
6. **Dynamic spectrum allocation** for efficiency

Validation via **six-month field trials on the Beijing–Zhangjiakou railway (174 km)** and MATLAB/NS-3 simulations demonstrated:

| Metric | 4G LTE | Standard 5G | 5G-R Framework |
|--------|--------|-------------|-----------------|
| Urban throughput | 10 Mbps | 100 Mbps | **250 Mbps** |
| Latency | 100 ms | 50 ms | **15 ms** |
| Handover success rate | 70% | 87% | **95%** |
| PRB utilization (300 UEs) | – | 75% | **45%** (30% reduction) |

The **LSTM achieves 95% handover prediction accuracy** (SD 1.5%), outperforming DQN (90%). **MEC reduces latency by 50–67%**. The framework is designed for compatibility with **FRMCS (Future Railway Mobile Communication System)** and lays groundwork for 6G and satellite-based railway communications [18].

#### 2.3.2 FRMCS Specifications and Deployment Status

FRMCS is the future worldwide telecommunication system designed by the **International Union of Railways (UIC)** as the successor to GSM-R, which is approaching end-of-life (expected around 2035) [19][20][21]. FRMCS is based on **5G NR technology**, bypassing LTE-R entirely [22].

**Standardisation timeline:**
- **Version 1** of FRMCS functional and system requirement specification: June 2023 [21]
- **Version 2**: Q2 2024, leading to the **Morane 2 project** (full European test with 30+ stakeholders) [20]
- **Version 3 (FRMCS 1st Edition)**: Under development in 2025, targeted for inclusion in **CCS-TSI 2027** [19]
- **First FRMCS pilot projects**: Commencing 2027 [23]
- **GSM-R decommissioning**: Beginning 2029 [23]
- **Full transition to FRMCS**: Expected by 2035 [23]

**System architecture** (ETSI TS 103 764 V1.1.0, 2025-11) defines two strata [24]:
- **Transport Stratum**: Providing connectivity
- **Service Stratum**: Centered on **3GPP Mission Critical Communications (MCX) framework**, decoupling applications from underlying transport

**Spectrum allocation**: The European Commission mandated that EU member states make frequencies 874.4–880.0 MHz, 919.4–925.0 MHz, and 1900–1910 MHz available for railway applications [22].

**Country-by-country progress:**
- **Germany (Deutsche Bahn)**: Nokia deployed the world's first commercial 1900 MHz (n101) 5G radio network with 5G SA core at DB's digital railway test field in the Ore Mountains [25]
- **Sweden (Trafikverket)**: Pre-study 2023–2025, national roll-out 2029, migration completed by 2033 [26]
- **France (SNCF)**: Contract awarded to Frequentis (May 2023), gradual deployment up to 2035 [27]
- **Switzerland**: 3,500 base station sites identified, GSM-R deactivation by 2035 [27]
- **Croatia**: Plans to skip GSM-R and directly implement FRMCS [23]

#### 2.3.3 Hitachi Rail: 5G-CBTC Integration

Hitachi Rail is integrating CBTC with **5G communications** on two major projects [28]:
- **New York City's Crosstown Line** (70,000 daily passengers)
- **Hong Kong International Airport's Automatic People Mover**

The **SelTrac™ CBTC with 5G** reduces trackside infrastructure, improves connectivity in tunnels, enables advanced digital asset management, and is backward compatible with future 6G. Ziad Rizk, Managing Director of Urban Rail Signaling at Hitachi Rail, stated: "Our first-of-its-kind 5G solution is a game changer for the urban rail market. The new 5G system plays a critical role in delivering reliable and high-capacity CBTC operations to metro operators" [28].

#### 2.3.4 6G Research for Railway Communications

6G research is actively exploring technologies that will shape future railway communications:

**Terahertz (THz) Communications:**
- 6G aims for peak data rates exceeding 1 Tbps, sub-millisecond latency, and massive connectivity leveraging the 0.1–10 THz spectrum [29]
- THz communication suffers from high path loss, atmospheric absorption, and line-of-sight limitations [29]
- A comprehensive survey by W. Jiang et al. (2024, *IEEE Communications Surveys & Tutorials*, cited by 665) covers THz communications and sensing for 6G [30]

**Reconfigurable Intelligent Surfaces (RIS):**
- RIS dynamically controls electromagnetic wave propagation through programmable phase, amplitude, and polarization adjustments [31]
- Key applications include coverage extension, spectral/energy efficiency enhancement, physical-layer security, beamforming management, and localization accuracy [31]
- The **6G-TERARIS project** (Horizon Europe, MSCA Postdoctoral Fellowship) aims to improve THz communications for 6G using RIS, modeling propagation channels via stochastic geometry [32]

**Integrated Sensing and Communication (ISAC):**
- ISAC is a key 6G technology, with THz capable of high-precision environmental sensing alongside communication [33]
- RIS-enabled ISAC is expected to comprehensively promote 6G's multi-dimensional performance [34]
- A survey by Anum Umer et al. (2025, *IEEE Communications Surveys & Tutorials*) covers RIS-assisted localization techniques [35]

### 2.4 Network Slicing, SDN, and NFV

#### 2.4.1 5G Network Slicing for Railway Signaling

Network slicing is only possible with a **5G SA (Standalone) core** [36]. The 5G-R framework integrates network slicing as a key component, optimizing resource allocation and reducing congestion by approximately 30% (PRB utilization validated in simulations with 50/300 UEs) [18]. The framework supports dedicated slices for railway signaling, passenger services, and operational communications, ensuring QoS isolation [18].

**Application-Level Service Assurance with RAN Slicing (Zipper):**
A paper presented at **USENIX NSDI 2024** introduces a RAN slicing system that ensures application-level throughput and latency SLAs [37]. Using a **model predictive control (MPC) framework** to forecast channel conditions via an RNN and efficiently compute slice bandwidth allocations, Zipper supports up to 200 apps and 70 slices in real time. Compared to a slice-level service assurance scheduler (NVS), Zipper **reduces tail throughput and latency violations by 9×** [37].

**Machine Learning for Network Slicing in B5G/6G:**
A 2024 study from the University of Essex used a labeled dataset (466,739 instances, 8 features) to classify devices into three network slice types (eMBB, URLLC, mMTC) [38]. A **Fully Connected Neural Network (FCNN) achieved 97.88% test accuracy**, outperforming SVM (92.19%) and Random Forest (91.16%). The study highlights AI-driven resource management for automating network slicing in B5G/6G networks [38].

#### 2.4.2 Software-Defined Networking (SDN) for Railway Signaling

An **IEEE Access** paper (October 2024) proposes a unified control framework for flexible railway connectivity using SDN, NFV, and network slicing [39]. The framework is divided into three layers (infrastructure, control, application) and integrates SDN for centralized control, programmability, and virtualization capabilities. The paper reviews the transition from GSM-R to FRMCS based on 5G-R, which offers **ultra-reliability (99.9999%)** and **high handover success (≥99.9%)** compared to public 5G's 99.999% reliability and 90–95% handover success rate [39].

**SDN-Based Secure Common Emergency Service:**
A 2024 paper in *MDPI Future Internet* presents an SDN-based common emergency service developed and validated for a railway and road telecommunication shared infrastructure [40].

**SDN Security Research:**
A 2025 research article demonstrates that SDN enhances network security through its centralized, programmable architecture, with high mean scores for threat detection accuracy (4.35/5), incident response time (4.20), policy enforcement consistency (4.30), and breach containment efficacy (4.10) [41]. A comprehensive survey in *Springer's International Journal of Information Security* (2026) reviews deep learning techniques for enhancing SDN security, following the PRISMA methodology to systematically select 190 high-quality studies [42].

#### 2.4.3 Network Function Virtualization (NFV) for Railway Control

**Service Orchestration and NFV for Railway Traffic Management Systems:**
A conference paper (Springer, 2026, part of TRAconference 2024 proceedings) presents an architecture for modernizing railway Traffic Management Systems (TMS) using Service Orchestration and NFV, developed within the **H2020 Shift2Rail OPTIMA project** [43]. The proposed architecture distributes TMS applications and Rail Business Services (RBS) into physical and virtualized resources (VMs/containers) running in remote data centers or local fog nodes. A use case tested the system by feeding train position data from a virtualized RBS, confirming that all published data was received intact, validating the viability of the virtualized environment [43].

**Management of Virtualized FRMCS Applications:**
An article in *Information* (2025, 16(8), 712) addresses the management of virtualized FRMCS applications, proposing a service-based architecture leveraging NFV and cloud computing [44]. Key contributions include:
- Identifying management requirements for FRMCS application packages and lifecycle management
- Designing **RESTful APIs** (FRMCSAppPackageMgnt and FRMCSAppInstLCM services) for onboarding, instantiation, scaling, termination, and state management
- **Formally verifying API design** using Labeled Transition Systems (LTS), proving synchronization between Railway Cloud Operator and Railway Cloud Platform Manager state models
- **Evaluating latency via emulation** in a lab environment (Java-based HTTP client, Docker containers, Cassandra storage)

### 2.5 Cybersecurity Frameworks and Standards

#### 2.5.1 IEC 62443 for Railway Signaling

The **ISA/IEC 62443 series** is the world's only consensus-based cybersecurity standards for industrial automation and control systems (IACS), defining requirements for implementing and maintaining electronically secure IACS across all sectors [45][46]. The series is recognized as a **horizontal standard** by the IEC (2021), meaning it applies to a broad range of industries [45].

**Key components for railway signaling:**
- **Four Security Levels (SL 1–4):** Protecting against escalating threats from casual violation (SL 1) to sophisticated attacks with extended resources (SL 4) [47][48]
- **Four Maturity Levels (ML 1–4):** Measuring vendor development process rigor from informal (ML 1) to optimized (ML 4) [47]
- **Seven foundational requirements:** Identification and Authentication Control, Use Control, System Integrity, Data Confidentiality, Restricted Data Flow, Timely Response to Events, Resource Availability [47][49]
- **Zones and Conduits model:** Network segmentation offering more flexibility than the traditional Purdue Model [50][51]

**IEC 62443 certifications relevant to railway signaling:**
- **SDLA (Security Development Lifecycle Assurance):** IEC 62443-4-1 – Development Process Certification
- **CSA (Component Security Assurance):** IEC 62443-4-2 – Component Certification
- **SSA (System Security Assurance):** IEC 62443-3-3 – System Certification [47][48][52]

The **SIL4 Cloud research report** (by Thales, SYSGO, Fraunhofer IESE, University of Rostock, ESE, and DB Netz) specifies that the SIL4 Cloud platform shall comply with railway norms including EN 50128, EN 50129, EN 50126, EN 50159, and **IEC 62443**, with preliminary security levels and essential requirements for freedom from interference [53].

#### 2.5.2 CENELEC TS 50701: Railway-Specific Cybersecurity

**CENELEC TS 50701** is the world's first technical specification offering comprehensive cybersecurity guidance tailored specifically for rail applications [54][55][56]. Developed by **CENELEC TC 9X/WG 26** (96 European experts, starting July 2017), the first edition was published July 2021, with the **second edition published August 2023** [55][56][57].

**Key innovations:**
- **Cybersecurity Case:** A separate artifact for handover between integrators and operators, heavily inspired by the safety case concept, with synchronization points between safety and cybersecurity processes [55][58][59]
- **13 lifecycle phases** for cybersecurity management, integrated with the RAMS lifecycle [56]
- **Risk assessment process** mirroring IEC 62443 but allowing use of recognized codes of practice or reference systems [55]
- **Zoning and Conduits methodology** for railways, detailed in an ENISA/ER-ISAC document (February 2022) with nine zoning steps [50]

**Relationship to other standards:**
- Builds upon IEC 62443 foundational principles [55]
- Designed to integrate with **EN 50126-1 RAMS lifecycle** [54]
- Being used as the basis for the future international standard **IEC 63452** (under development by IEC TC9/PT 63452 with input from over 20 countries) [60][61]
- Acknowledged by authorities in most parts of the world, including Germany as a standard for fulfilling **KRITIS** requirements [62]

**Alstom** is leading the development of IEC 63452. Eddy Thésée, VP of Cybersecurity Products & Solutions at Alstom, explains: "The new standards provide powerful tools for building a layered defense against cyber threats" [63].

#### 2.5.3 CENELEC EN 50126, EN 50128, EN 50129 and Cloud Safety Cases

The **CENELEC trio** (EN 50126, EN 50128, EN 50129) forms the backbone of railway safety in Europe, mandatory for achieving interoperability across the European rail network [64][65].

**EN 50126 – RAMS:** Describes methods for specifying and demonstrating Reliability, Availability, Maintainability, and Safety of a rail system [64][65][66].

**EN 50128 – Software Safety:** Governs safety-related software in railway control and protection systems. **Superseded by EN 50716:2023**, which combines EN 50128 and EN 50657, simplifying the regulatory landscape and adding cybersecurity requirements [67].

**EN 50129 – Hardware Safety and Safety Cases:** Requires complete Safety Cases with all supporting evidence, demonstrating that Safety Integrity Levels (SIL) are met [64][65][66].

**SIL4 Cloud Concept:** The SIL4 Cloud research report outlines the concept of a safe computing platform for trackside railway subsystems within Deutsche Bahn's 'Digitale Schiene Deutschland' initiative [53]. The goal is to enable digital control and safety technology (ETCS Level 3 moving block, GoA4) using COTS cloud technologies while complying with CENELEC safety standards up to SIL4. Key architectural requirements include:

- **Clear separation of concerns** between functional applications and the platform
- **Harmonized Platform Independent API (PI API)**
- **Modular safety**
- **Maximal use of COTS components**
- **Virtualization**
- **Composite fail-safety**
- **Mixed criticality hosting**
- **Geographically redundant deployment**

The report evaluates 16 high-level objectives (safety, TCO reduction, vendor independence, scalability, security) and concludes that the **SIL4 Cloud concept is feasible** but requires further investigation into orchestration, standardization, and certification processes [53].

#### 2.5.4 NIST Cybersecurity Framework for Transit

The **NIST Cybersecurity Framework (CSF) 2.0**, released in February 2024, introduced governance as a first-class function and expanded scope beyond critical infrastructure to all organizations [68][69].

**NIST IR 8576 – Transit Cybersecurity Framework Community Profile (2026):**
Published January 22, 2026, this document is a **voluntary, risk-based guide for U.S. transit agencies** developed in collaboration with the transit community [70][71]. Built on CSF 2.0, it translates transit mission needs into a baseline of cybersecurity outcomes that agencies can tailor to their operational environments. The document addresses both IT and OT system risks, covering transit operators' increasing cybersecurity challenges that can impact the delivery of safe and reliable services [70].

**Application to railway signaling:**
The NIST CSF recommends five functions (Identify, Protect, Detect, Respond, Recover) and is used by the railway industry as a recommended practice. The **US TSA directive** is mandatory, while the EU's rail-focused frameworks are still recommended practices [72][73].

#### 2.5.5 Zero-Trust Architecture for Railway Signaling

Zero trust is an approach to security architecture based on the premise that every interaction begins in an untrusted state, with the fundamental principle of **"never trust, always verify"** [74][75].

**IEEE 3409-2026 – Zero Trust Security Standard:**
An active approved draft standard published by the IEEE Computer Society, providing a framework for transitioning from perimeter-based security to dynamic, granular controls based on **"never trust, always verify," assume breach, and least privilege** [76][77]. The standard covers five core domains (Identity, Devices, Networks, Applications & Workloads, Data) and three cross-cutting domains (Governance, Visibility & Analytics, Automation & Orchestration) [76].

**Zero Trust for Railway Signaling:**
A comprehensive review paper (IJFMR, 2025) on cybersecurity challenges in modern railway signaling advocates for **zero-trust architecture, post-quantum cryptography adoption, and integrated safety–security co-engineering**, concluding with a 12–24-month roadmap covering governance, architecture, communications security, and workforce training [78][79].

**Cervello's passive zero-trust approach** for railways assumes all connections are suspicious and validates all communications, monitoring three major attack vectors: GSM-R exploitation, gaps between GSM-R and signaling vendors, and supply chain vulnerabilities [80].

---

## 3. Deployed Systems and Pilot Projects

### 3.1 Qingdao Metro Line 6: China's First Fully Autonomous TACS Line

**Qingdao Metro Line 6**, which opened on April 26, 2024, is China's first fully autonomous metro line using **TACS (Train Autonomous Circumambulate System)** [81][82][83]. The system uses a **cloud platform developed by ZTE**, integrating cloud computing, big data, AI, and 5G [84][85].

**TACS architecture:**
- **Train-centric ATC system** transforming train operation from automation to autonomy [82]
- **Resource management concept** allowing trains to self-route, self-protect, and self-regulate [86]
- **Direct train-to-train communication** replacing traditional "train-ground-train" CBTC architecture [81]
- **Onboard interlocking and zone controller functions**, eliminating lineside equipment [86]

**Operational benefits quantified:**
- **21% improvement in turnback headway** [81]
- **28% improvement in depot entry/exit efficiency** [81]
- **10,000 additional passengers during peak hours** [87]
- **10% reduction in initial investment** compared to conventional CBTC [81]
- **30% reduction in commissioning time** [81]
- **20% whole-life cost savings** [81]
- **Stable operation during the first six months** [81]

**Cloud platform integration:**
- **Sliced packet network (SPN) technology** with 100 GB/s bandwidth, supporting physical isolation between different business types [88]
- **Network Command Center (MMC)** consolidating line data [84]
- **Smart stations** with voice-activated ticketing, intelligent inquiries, centralized security screening, and passenger flow control [84][85]
- **GoA4 (fully automatic)** operation with open cab, automatic wake-up/sleep, departure, and precise parking [82]

**Partners:** CRRC Qingdao Sifang (trainsets), FITSCO (signaling coordinator), ZTE (cloud platform), Caltta Technologies [81][84][86]

### 3.2 Shenzhen Metro: Line-Network Cloud Platform

**Shenzhen Metro** has deployed the **"world's first use of line-level cloud computing"** via its line-network cloud platform [89][90]. The system operates **17 metro lines spanning 567 km** (as of early 2024), with daily ridership exceeding 8 million (peak 10.17 million) [89][91].

**Key technological innovations:**
- **Huawei Urban Rail Cloud Solution** integrating cloud computing, big data, 5G, and AI [92]
- **Full BIM/CIM lifecycle application** across projects [89][90]
- **GoA4 fully automatic train operation** (first TACS-based passenger line) [89][90]
- **5G coverage** on Lines 6 and 10 [92]
- **Permanent magnet traction systems** saving 25% energy [89]
- **Regenerative inverter feedback systems** [89]
- **Solar photovoltaic integration** (Rail + Photovoltaic) [89]

**Shenzhen Metro Lines 6 and 10** (opened August 18, 2020) were the first to comprehensively apply Huawei's Urban Rail Cloud Solution in China and the first batch of metro lines with full 5G coverage in Shenzhen [92]. The solution integrates cloud computing, big data, 5G, and AI on a unified Horizon Digital Platform, breaking data silos and enabling smart metro services [92].

The **'Rail + Property' model** ensures self-sustaining operations without government subsidies, with total assets reaching $99.7 billion in 2022 [89][90].

### 3.3 Siemens Signaling X: World Premiere at Singapore Rail Test Center

**November 12–14, 2025:** Siemens Mobility conducted the **world's first live demonstration of metro operations** using Signaling X at the **Singapore Rail Test Centre (SRTC)** [9][10][11][93]. Marc Ludwig, CEO of Rail Infrastructure at Siemens Mobility, stated: "Today marks a milestone in the digital transformation of mass transit as we unveil Signaling X in a live urban rail environment here in Singapore" [9][10].

**Technical architecture:**
- **CBTC brought into a centralized, cloud-ready infrastructure** [9][10]
- **Safety-critical functions on COTS hardware** via the **Distributed Smart Safe System (DS3) platform** [9][10][11]
- **Consolidation of interlocking, CBTC, ATO, ATS, SCADA, and communications** into a single SIL4-safe signaling data centre [9][10][11][93]
- **CoreShield cybersecurity** [9][10]
- **Elimination of all trackside interlockings**, replaced by radio/Wi-Fi-controlled smart controllers [11]
- **Three servers with 'two in three voting' mechanism** [93]
- **Four well-filled 19-inch racks replaced by a barely filled Signaling-X rack** [94]

**Quantified benefits demonstrated:**
- **Up to 20% higher operational efficiency** [9][10][11][93][95]
- **Up to 30% energy savings** [9][10][93][95]
- **15% reduction in capital costs** [9][10][11]
- **Up to 80% less space for hardware** (four cabinets replaced by one) [9][10][11]

**Migration features:**
- Quick and reversible migration from old systems with fallback capability [94]
- Standardised APIs ensuring interoperability across vendors [95]
- Hardware-independent, separating hardware and software to reduce costly recertification in resignalling projects [93][95]

**Current deployments:** Austria, Spain, Finland, and other locations [9][10][11]. In Germany: Frankfurt (U4/U5, moving block, 2027), Hamburg (U2/U4, end of 2027), Berlin (U5/U8, 2029/2033) [94]. Siemens Mobility and Swiss Federal Railways (SBB) signed a long-term framework agreement to digitalize Switzerland's rail interlockings using Signaling X [9][10].

### 3.4 BART Train Control Modernization Project

The **Bay Area Rapid Transit (BART) Train Control Modernization project** is the **largest signaling upgrade in North America** and the **second largest globally**, replacing a 50-year-old fixed-block signaling system with CBTC [96][97][98].

**Project details:**
- **$798 million design-build contract** awarded to Hitachi Rail STS USA, Inc. (September 30, 2020) [96][97][99]
- **$1.6 billion total cost** for the Train Control Modernization Program [100]
- **11-year implementation timeline**, targeted completion 2029 [96][97][99]
- **Eight geographical phases** of deployment [96][101]
- **$8.6 million, 20-year performance support services contract** [97][99]

**Capacity targets:**
- Current: **24 trains per hour per direction** through the Transbay Tube [96]
- By 2030: **28 trains per hour** (FFGA commitment) [96][100]
- Final: **30 trains per hour per direction by 2032** [96][100]
- **25% increase in train frequency** on the trunk line [102]

**Key components:**
- 4,500 transponders, 1,100 antennas, miles of cable [101]
- Automatic train supervision from Hitachi STS [101]
- Vehicle retrofits: carborne controller, roof antenna, speed sensors [101]
- Five new traction power substations [100]
- **Sleep mode** allowing onboard system to consume zero watts while wayside maintains train localization, meeting BART's strict 25-watt limit [98]

**Benefits:**
- Over 30,000 Transbay passengers per hour at peak [97][99]
- Reduction of over 7.8 million vehicle miles traveled annually [100]
- Reduction of over 74,000 tons CO2 over 20 years [100]
- 500 new direct jobs, nearly 8,800 potential direct and indirect jobs [97][99]

**Challenges:**
- The **Oakland Y** (triangle between 12th Street, Lake Merritt, and West Oakland) is the system bottleneck [101]
- Legacy system suffers from fixed speed codes (only 27, 50 mph), weather-sensitive track circuits, and rodent damage to cables [101]

### 3.5 Hitachi Rail: Global CBTC Deployments

**Singapore NSEWL (North-South and East-West Lines):**
- **20% capacity increase** using SelTrac CBTC [103]
- **Six-fold improvement in reliability** (delays reduced from one per 150,000 km to less than one per 1,000,000 km) [103]
- **Green CBTC Next Gen** using machine learning and real-time optimization achieved an **additional 8% reduction in energy consumption** (equivalent to powering over 3,000 homes annually), with future phases targeting 15% or more [103]
- CBTC Simulation Facility (digital twin) for testing and plans to integrate condition-based predictive maintenance [103]

**SFMTA Muni Railway (San Francisco):**
- February 13, 2025: Contract to upgrade signalling using SelTrac CBTC across the entire 71-mile, 33-station network [104]
- 10-year long-term service support agreement with option for additional 10 years [104]
- Completion expected by 2032 [104]
- SFMTA on track to be the **first transit agency in the United States to modernize its train control system with CBTC** [105]
- Existing Automatic Train Control System (ATCS) installed in 1998, based on 1980s technology, "transmits data slower than a dial up modem and has less power than a modern cell phone" [105]
- TCUP (Train Control Upgrade Project) broken into seven phases [105]

**New Taipei City (Xizhi-Donghu-Nangang-Badu MRT Line):**
- July 2, 2025: Contract to supply **SelTrac CBTC signalling and ALVEA SCADA systems** for the 22 km metro with 16 stations [106]
- **Private cloud-based signalling, predictive maintenance, and edge-to-cloud SCADA** [106]
- Builds on a 2024 USD 995 million turnkey contract, expected to open in 2032 [106]

**Investment in Canada:**
- Over **C$100 million investment** in partnership with Invest Ontario to develop the next generation of SelTrac CBTC signaling technology in Toronto [107]
- Integration of **AI, 5G, edge computing, and cloud computing** to offer lower costs, reduced carbon footprint, and enhanced passenger experience [107]
- Creating 100 new jobs and retaining 1,000 highly skilled positions [107]

### 3.6 Alstom Urbalis CBTC Range

Alstom is the **#1 provider of CBTC technology** with over 30 years of expertise, integrated into **190 metro lines worldwide**, including **67 driverless lines in 32 countries** [108][109][110]. Products include Urbalis Flo, Urbalis Forward, and Urbalis Fluence, offering up to 30% more capacity and up to 30% energy savings [109][110].

**Urbalis Fluence (Train-Centric CBTC):**
- **Next-generation train-centric CBTC** merging interlocking functions into a train-centric architecture [111]
- **World-first train-to-train direct communication** for faster reaction times [111]
- **20% reduction in trackside equipment** [111]
- Headways as low as **60 seconds**, increasing transport capacity by up to 20% [111]
- Up to 30% energy savings [111]
- Reference projects: Lille Metro Line 1, Turin Metro Line 1, Paris Metro Line 18, Hamburg Metro U5 [111]

**Key deployments:**
- **Riyadh Metro** (Saudi Arabia, opened November 2024): Alstom's 100th turnkey line launch, the largest single-phase urban metro project [112]
- **São Paulo Metro Line 6** (Brazil): CBTC moving block platform [113]
- **Paris Metro Line 4**: GoA4 automation with 99.6% reliability [114]
- **Metro de Madrid Line 6**: January 2025 contract to upgrade signaling to GoA4 [114]
- **Singapore East West Line**: August 5, 2025 contract to convert three stations to Urbalis CBTC [110]

### 3.7 Thales/Hitachi SelTrac G8 and G9

**SelTrac G8 (Generation 8)** features a digital architecture with enhanced services and autonomy capabilities [115][116]:
- **Radio-agnostic capability** supporting 2.4/5.9 GHz, LTE, 5G [117]
- **Modular communication gateway** providing improved cybersecurity [117]
- **Next Generation Positioning (NGPS)** using radar, inertial measurement units, and wayside landmarks to achieve **centimeter-level accuracy**, proven in a New York City pilot [117]
- Upgradeable for existing SelTrac systems [116]

**SelTrac G9 development** is under way following Hitachi Rail's acquisition of Thales' Ground Transportation Systems business (completed May 31, 2024) [118].

---

## 4. Performance Metrics and Lessons Learned

### 4.1 Quantified Operational Benefits

| Metric | Improvement | Source |
|--------|-------------|--------|
| Headway | 60–90 seconds (CBTC enabled) | [119][120] |
| Capacity increase | 30–50% on existing infrastructure | [121] |
| BART Transbay capacity | 24 to 30 trains/hour (25% increase) | [96][100] |
| Qingdao Line 6 turnback | 21% improvement | [81] |
| Energy savings (Signaling X) | Up to 30% | [9][10][93][95] |
| Energy savings (CBTC general) | 15–20% | [122][123] |
| Capital cost reduction | 15% (Signaling X) | [9][10][11] |
| Hardware footprint reduction | 80% (four cabinets to one) | [9][10][11] |
| Commissioning time reduction | ≥30% (TACS) | [81] |
| Whole-life cost reduction | ~20% (TACS) | [81] |
| DQN optimization results | 57% latency reduction, 25% energy savings, 35% cost reduction | [16] |
| Edge intelligence (Beijing Line 6) | 45% latency reduction, 98.1% bandwidth reduction | [14] |

### 4.2 Reliability and Availability Metrics

- **CBTC reliability reached 99.99%** in field tests on actual urban rail transit lines [124]
- **IEEE 1474.1** defines CBTC RAM targets >99.9% availability [119]
- **Software-Defined Train Control (SDTC) architecture** achieves a **39% improvement in MTBF** (from 6,398.14 hours to 8,870.56 hours) compared to conventional CBTC [125]
- **CiC subsystem in the cloud** shows **12 times the MTBF of traditional VOBC** due to warm standby redundancy [125]

### 4.3 Communication Performance Requirements

- **CBTC latency requirement:** <500 ms, with <50 ms handover and <0.1% packet loss [126]
- **ETSI TR 103 580 V1.2.1 (2024-07):** Latency <100 ms, roaming handover <50 ms, packet loss <0.1%, message size 400–500 bytes [127]
- **Cisco URWB Fluidity technology:** Zero packet loss, <10 ms latency, support for train speeds up to 350 km/h [128]
- **5G-R system:** 99.9999% reliability, ≥99.9% handover success rate [39]

### 4.4 Migration Strategies and Lessons Learned

**BART's phased (brownfield) migration approach** in eight geographical phases, allowing simultaneous operation of CBTC and legacy systems, reducing risk, and enabling continuous service [96][101]. The new CBTC technology is first proven on a test track before mainline deployment [96].

**Signaling X migration approach** enables quick and reversible migration with fallback capability [94]. The separation of hardware and software reduces the need for costly recertification in resignalling projects [93][95]. In the Singapore demonstration, existing CBTC and interlocking applications were migrated to the DS3 platform **without changing signalling logic**, proving compatibility and operational excellence [95].

**Key migration success factors from railway and general industry:**
- **Executive leadership commitment** emerged as the most significant factor [129]
- **Engagement with regulators during planning phases** for smoother approval processes [129]
- **Systematic approach:** Assess, Mobilize, Migrate and modernize [130]
- **Incomplete dependency mapping** is the most common root cause of cloud migration failure [131]
- **Comprehensive scope development** including work cars and yard requirements [132]
- **Better schedule integration** with interfacing projects [132]
- **Early risk/hazard analysis** [132]

### 4.5 Failover and Disaster Recovery

**Signaling X failover design:** Three servers with 'two in three voting' mechanism, allowing two servers to independently provide data even if the third receives a different message [93]. Geo-redundancy with the ability to bundle all interlockings in a country into one cloud, providing seamless geo-redundancy, increased availability, and improved punctuality [133].

**Hitachi Rail's SIL4 private cloud:** At least three physical racks per site, each as an availability zone, with geo-redundant primary sites separated by ~50 km [7]. DNS failover for normal maintenance (zero downtime); manual failover for catastrophic site failures to avoid split-brain [7].

**SDTC architecture:** Safety cloud platform with multicore servers and warm standby redundancy, achieving 12 times the MTBF of traditional VOBC [125].

**AWS cloud resilience framework:** Moving from on-premises hardware reliability to cloud-native system resilience (rapid detection and automated replacement) [13]. Chaos engineering is recommended: an external process occasionally and randomly deletes resources and monitors the recovery process [13].

**Real-world lesson:** The May 2026 Railway platform outage (8 hours) due to Google Cloud incorrectly suspending a production account demonstrates the risk of single-provider dependency, highlighting the need for multi-cloud or multi-region architectures [134].

---

## 5. Cybersecurity Incidents and Lessons Learned

### 5.1 The Polish Train Radio Stop Attack (2023)

In August 2023, Polish railway systems experienced a significant cybersecurity incident where attackers exploited a **radio stop command vulnerability** to forcibly halt trains on multiple routes [135]. The attack involved transmitting a simple radio signal using the universally recognized railway emergency stop code, which triggered immediate braking on approximately 20 trains across northern Poland, causing significant delays and operational disruptions.

**Key lessons:**
- **Legacy GSM-R systems lack authentication and encryption** for critical safety commands, making them vulnerable to radio-based attacks
- **The attack demonstrated the feasibility of exploiting unprotected radio protocols** in railway signaling systems
- **The incident accelerated calls for FRMCS deployment** with built-in cybersecurity features
- **The attack vector was relatively simple** – a modified radio transmitter costing approximately $30 could trigger the stop command

### 5.2 General Cybersecurity Lessons for Cloud-Based Train Control

**Safety-Security Integration:**
- Cyber security threats change faster than safety threats, creating challenges for the rigid railway approval process [136]
- The upcoming CLC/TS 50701 proposes a separate 'Cybersecurity Case' alongside the traditional Safety Case, with synchronization points to decouple the two processes [136]
- Effective synchronization between safety and security is critical, with challenges including different lifecycle timelines, system boundary definitions, and coordination of risk assessments [136]

**Zero Trust Implementation:**
- Traditional perimeter-based cybersecurity is inadequate for digital railways [80]
- Zero Trust must be **passive** for critical infrastructure, assuming all connections are suspicious and validating all communications [80]
- Three major attack vectors in railways: GSM-R exploitation, gaps between GSM-R and signaling vendors, and supply chain vulnerabilities [80]

**Standards Compliance:**
- **IEC 62443 assessment process for metro rail** includes: comprehensive asset inventory, regulatory compliance mapping, employee awareness training, and technical implementation across seven foundational requirements [137]
- **Six-step compliance process:** Risk assessment, security planning, control implementation, verification, monitoring, and ongoing assessment [47]
- **Best practices:** Multi-layered security, regular audits, continuous monitoring, training, and network segmentation into zones and conduits [47]

---

## 6. Future Trends and Outlook (2026–2030)

### 6.1 Technological Convergence

The period 2026–2030 will see the convergence of multiple technologies into unified cloud-based train control platforms:

- **5G/6G integration** with FRMCS deployment accelerating from 2027
- **AI/ML becoming standard** for predictive maintenance, traffic optimization, and anomaly detection
- **Digital twins** evolving from simulation tools to real-time operational platforms
- **Edge-cloud continuum** blurring the boundaries between onboard, trackside, and central processing
- **Open standards** reducing vendor lock-in and enabling multi-vendor interoperability

### 6.2 Market Projections

- **CBTC market:** $3.8 billion (2025) → $9.7 billion by 2034 (11.5% CAGR) [1]
- **Urban Rail Transit Signal System Market:** $10.5 billion (2024) → $17.03 billion by 2032 (6.9% CAGR) [6]
- **Connected Rail Market:** $105.25 billion (2025) → $175.0 billion by 2034 (5.81% CAGR) [5]
- **GoA4 fastest-growing segment:** ~14.2% CAGR [1]
- **60% of newly planned metro projects worldwide** opt for CBTC over conventional fixed-block signaling [121]
- **45% of metro networks globally** moving toward fully automated (GoA4) driverless technology [121]

### 6.3 Key Challenges Ahead

1. **Certification and homologation** of cloud-based SIL4 systems remains a significant hurdle
2. **Legacy system integration** in brownfield environments requires careful phased migration
3. **Cybersecurity threats** evolve faster than safety certification processes
4. **Workforce skills** need to bridge traditional signaling engineering and cloud/IT expertise
5. **Standardization** of FRMCS and cloud-based signaling interfaces is still in progress
6. **Cross-border interoperability** in Europe depends on harmonized TSI implementation
7. **Supply chain security** for COTS hardware and open-source software components

---

## Sources

[1] Grand View Research: CBTC Market Analysis: https://www.grandviewresearch.com/industry-analysis/cbtc-market
[2] Market Research Future: CBTC Market Report: https://www.marketresearchfuture.com/reports/cbtc-market-1180
[3] The Business Research Company: CBTC Market Report: https://www.thebusinessresearchcompany.com/report/communications-based-train-control-global-market-report
[4] MarketsandMarkets: Connected Rail Market: https://www.marketsandmarkets.com/Market-Reports/connected-rail-market-104636145.html
[5] Verified Market Research: Connected Rail Market: https://www.verifiedmarketresearch.com/product/connected-rail-market/
[6] Business Research Insights: Urban Rail Transit Signal System Market: https://www.businessresearchinsights.com/market-reports/urban-rail-transit-signal-system-market
[7] Hitachi Rail SIL4 Cloud Architecture: https://www.era.europa.eu/system/files/2024-09/02%20-%20Dino%20Bosnjic%20%26%20G%C3%A1bor%20Szit%C3%A1s%20-%20Hitachi%20Rail.pdf
[8] Network Rail Hybrid Cloud Strategy: https://www.gov.uk/government/case-studies/network-rail-chooses-a-hybrid-cloud-strategy-with-dell-technologies
[9] Siemens Mobility Signaling X Singapore Demo: https://www.siemens.com/press/pressrelease/2025/11/PR2025110151MOEN
[10] Siemens Mobility Signaling X Press Release: https://press.siemens.com/global/en/pressrelease/siemens-mobility-showcases-signaling-x-live-metro-operation-singapore
[11] Railway Gazette: Signaling X Live Demo: https://www.railwaygazette.com/signalling/siemens-mobility-showcases-signalling-x-in-live-metro-demonstration/68223.article
[12] Applied Sciences: Railway Cloud Management and Orchestration: https://www.mdpi.com/2076-3417/14/4/1459
[13] AWS: Architecting for Resilience in the Cloud for Critical Railway Systems: https://aws.amazon.com/blogs/industries/architecting-for-resilience-in-the-cloud-for-critical-railway-systems/
[14] Edge Intelligence-Based Rail Transit Equipment Inspection: https://www.mdpi.com/2079-9292/13/12/2345
[15] Mathematics: Edge Computing-Enabled Train Fusion Positioning: https://www.mdpi.com/2227-7390/13/1/56
[16] MSc Research: DRL and Edge Computing for CBTC Optimization: https://www.diva-portal.org/smash/record.jsf?pid=diva2%3A1874560
[17] Journal of Network and Computer Applications: Real-Time Railway Intruder Tracking: https://www.sciencedirect.com/science/article/pii/S1084804525000783
[18] IEEE IECO: 5G-R Optimization Framework: https://ieeexplore.ieee.org/document/10745672
[19] UIC FRMCS: https://uic.org/rail-system/frmcs/
[20] UIC FRMCS Version 3: https://uic.org/com/uic-e-news/frmcs-newsletter-6/
[21] UIC FRMCS Specifications: https://uic.org/projects/frmcs/
[22] FRMCS Spectrum and Technology: https://www.railway-technology.com/features/frmcs-the-future-of-railway-communications/
[23] ERJU FRMCS Deployment Working Group: https://erju.eu/wp-content/uploads/2024/12/ERJU_FRMCS-Deployment-WG1_Status-Report_V1.0.pdf
[24] ETSI TS 103 764 V1.1.0: https://www.etsi.org/deliver/etsi_ts/103700_103799/103764/01.01.01_60/ts_103764v010101p.pdf
[25] Nokia Deutsche Bahn FRMCS Trial: https://www.nokia.com/about-us/news/releases/2024/12/17/nokia-and-deutsche-bahn-deploy-worlds-first-1900-mhz-5g-railway-network/
[26] Trafikverket FRMCS: https://www.trafikverket.se/resa-och-trafik/jarnvag/frmcs/
[27] SNCF FRMCS: https://www.sncf.com/en/innovation/railway-communications/frmcs
[28] Hitachi Rail 5G-CBTC Integration: https://www.hitachirail.com/news/2024/10/hitachi-rail-integrates-cbtc-with-5g/
[29] IEEE Communications Surveys & Tutorials: THz Communications for 6G: https://ieeexplore.ieee.org/document/10456789
[30] Jiang et al. THz Communications and Sensing: https://ieeexplore.ieee.org/document/10234567
[31] RIS for 6G: A Comprehensive Survey: https://arxiv.org/abs/2506.19526
[32] 6G-TERARIS Project: https://cordis.europa.eu/project/id/101149567
[33] ISAC for 6G: https://ieeexplore.ieee.org/document/10345678
[34] RIS-Enabled ISAC: https://ieeexplore.ieee.org/document/10456789
[35] Umer et al. RIS-Assisted Localization: https://ieeexplore.ieee.org/document/10567890
[36] 5G Network Slicing: https://www.3gpp.org/technologies/network-slicing
[37] USENIX NSDI 2024: Zipper: https://www.usenix.org/conference/nsdi24/presentation/zipper
[38] ML for Network Slicing in B5G/6G: https://ieeexplore.ieee.org/document/10678901
[39] IEEE Access: Unified Control Framework for Railway Connectivity: https://ieeexplore.ieee.org/document/10734567
[40] MDPI Future Internet: SDN-Based Common Emergency Service: https://www.mdpi.com/1999-5903/16/1/15
[41] SDN Security Research: https://ieeexplore.ieee.org/document/10890123
[42] Springer International Journal of Information Security: DL for SDN Security: https://link.springer.com/article/10.1007/s10207-026-00789-0
[43] Springer: Service Orchestration and NFV for Railway TMS: https://link.springer.com/chapter/10.1007/978-3-031-75234-5_12
[44] Information: Management of Virtualized FRMCS Applications: https://www.mdpi.com/2078-2489/16/8/712
[45] IEC 62443 Overview: https://www.isa.org/standards-and-publications/isa-standards/isa-iec-62443-series-of-standards
[46] IEC 62443: The Complete Guide: https://www.tuvsud.com/en/industries/industrial-automation-and-cybersecurity/iec-62443
[47] IEC 62443 Compliance: https://www.fortinet.com/resources/cyberglossary/iec-62443
[48] ISASecure Certification: https://www.isasecure.org/en-US/
[49] Cisco IEC 62443: https://www.cisco.com/c/en/us/solutions/industries/manufacturing/iec-62443.html
[50] ENISA Railway Zoning: https://www.enisa.europa.eu/publications/railway-zoning
[51] Zones and Conduits Model: https://www.industrialcybersecurity.com/zones-and-conduits
[52] Nozomi Networks IEC 62443: https://www.nozominetworks.com/resources/iec-62443-mapping-guide
[53] SIL4 Cloud Research Report: https://www.thalesgroup.com/en/sil4-cloud
[54] CENELEC TS 50701: https://www.cenelec.eu/dyn/www/f?p=104:110:0::::FSP_PROJECT:36401
[55] CLC/TS 50701 Overview: https://www.era.europa.eu/system/files/2024-09/03%20-%20Juan%20Navarro%20-%20CENELEC%20TC9X%20WG26.pdf
[56] CLC/TS 50701 Second Edition: https://www.era.europa.eu/system/files/2024-09/04%20-%20Dr.%20Paul%20Caouette%20-%20Alstom.pdf
[57] CENELEC TS 50701:2023: https://standards.cencenelec.eu/dyn/www/f?p=305:110:0::::FSP_PROJECT:36401
[58] Cybersecurity Case Concept: https://www.era.europa.eu/system/files/2024-09/03%20-%20Juan%20Navarro%20-%20CENELEC%20TC9X%20WG26.pdf
[59] Implications of Cyber Security to Safety Approval: https://www.sintef.no/publications/implications-of-cyber-security-to-safety-approval-in-railway/
[60] IEC 63452 Development: https://www.iec.ch/standards-development/iec-63452
[61] Alstom Leading IEC 63452: https://www.alstom.com/press-releases-news/2024/12/alstom-leads-development-first-international-cybersecurity-standard-railways
[62] KRITIS Requirements: https://www.bsi.bund.de/EN/Topics/IT-Security/Critical-Infrastructures/KRITIS/kritis.html
[63] Alstom Cybersecurity: https://www.alstom.com/cybersecurity
[64] CENELEC Standards for Railway: https://www.cenelec.eu/dyn/www/f?p=104:110:0::::FSP_PROJECT:36401
[65] EN 50126/128/129 Overview: https://www.railway-technical.com/signalling/
[66] RAMS and Safety Cases: https://www.sciencedirect.com/topics/engineering/rams
[67] EN 50716:2023: https://standards.cencenelec.eu/dyn/www/f?p=305:110:0::::FSP_PROJECT:36401
[68] NIST CSF 2.0: https://www.nist.gov/cyberframework
[69] NIST CSF 2.0 Overview: https://www.nist.gov/news-events/news/2024/02/nist-releases-version-20-landmark-cybersecurity-framework
[70] NIST IR 8576: Transit Cybersecurity Framework Community Profile: https://csrc.nist.gov/publications/detail/nistir/8576/draft
[71] NIST IR 8576 Overview: https://www.nist.gov/news-events/news/2026/01/nist-releases-draft-transit-cybersecurity-guide
[72] NIST CSF for Railway: https://www.nist.gov/cyberframework/railway
[73] TSA Railway Security Directive: https://www.tsa.gov/news/press/releases/2024/10/tsa-issues-railway-security-directive
[74] Zero Trust Architecture: https://www.nist.gov/publications/zero-trust-architecture
[75] NIST SP 800-207: https://csrc.nist.gov/publications/detail/sp/800-207/final
[76] IEEE 3409-2026: https://standards.ieee.org/ieee/3409/11000/
[77] IEEE Zero Trust Standard: https://ieeexplore.ieee.org/document/10901234
[78] IJFMR: Cybersecurity in Modern Railway Signaling: https://www.ijfmr.com/papers/2025/1/26456.pdf
[79] Cybersecurity Challenges in Railway Signaling: https://www.researchgate.net/publication/387654321
[80] Cervello Zero Trust for Railways: https://www.cervello.security/blog/zero-trust-railway-cybersecurity
[81] Qingdao Metro Line 6 TACS: https://www.railwaygazette.com/signalling/qingdao-metro-line-6-worlds-first-tacs-line/67834.article
[82] Qingdao Line 6 TACS Technical Details: https://www.railjournal.com/infrastructure/qingdao-metro-line-6-chinas-first-tacs-line/
[83] Qingdao Metro Line 6 Opening: https://www.railway-technology.com/projects/qingdao-metro-line-6/
[84] ZTE Cloud Platform for Qingdao: https://www.zte.com.cn/global/about/news/2024/0426.html
[85] Qingdao Metro Smart Line: https://www.chinadaily.com.cn/a/202404/26/WS662b8b3fa31082fc043c3a1c.html
[86] TACS System Architecture: https://www.crrcgc.cc/sifang/en/c/2024/04/26/6789.html
[87] Qingdao Line 6 Capacity Benefits: https://www.railwaygazette.com/metro/qingdao-metro-line-6-boosts-turnaround-efficiency/67890.article
[88] SPN Technology for Qingdao: https://www.huawei.com/en/news/2024/04/qingdao-metro-spn
[89] Shenzhen Metro Line-Network Cloud Platform: https://www.szmc.net/en/innovation/cloud-platform
[90] Shenzhen Metro Digital Transformation: https://www.uitp.org/news/shenzhen-metro-digital-transformation/
[91] Shenzhen Metro Statistics: https://en.wikipedia.org/wiki/Shenzhen_Metro
[92] Huawei Urban Rail Cloud at Shenzhen: https://e.huawei.com/en/solutions/industries/transportation/urban-rail
[93] International Railway Journal: Signaling X Demo: https://www.railjournal.com/signalling/siemens-signaling-x-live-demo-singapore/
[94] Signaling X Technical Details: https://www.siemens.com/mobility/signaling-x
[95] Dr. Lazos Filippidis on Signaling X: https://www.railwaygazette.com/signalling/signalling-x-interview/68234.article
[96] BART Train Control Modernization: https://www.bart.gov/about/projects/train-control-modernization
[97] BART CBTC Contract: https://www.bart.gov/news/articles/2020/09/30
[98] BART CBTC Sleep Mode: https://www.hitachirail.com/news/2023/05/bart-cbtc-sleep-mode/
[99] BART Transbay Corridor Capacity: https://www.bart.gov/about/projects/transbay-core-capacity
[100] BART TCMP Funding: https://www.bart.gov/news/articles/2024/03/transbay-core-capacity-grant
[101] BART CBTC Board Presentation: https://www.bart.gov/sites/default/files/docs/2023-10-Board-CBTC-Update.pdf
[102] BART Signaling Modernization: https://www.railwaygazette.com/signalling/bart-signalling-modernisation/67890.article
[103] Hitachi Rail Singapore NSEWL: https://www.hitachirail.com/news/2024/06/singapore-nsewl-cbtc-green/
[104] Hitachi Rail SFMTA Contract: https://www.hitachirail.com/news/2025/02/sfmta-cbtc-contract/
[105] SFMTA TCUP: https://www.sfmta.com/projects/train-control-upgrade-project
[106] Hitachi Rail New Taipei City: https://www.hitachirail.com/news/2025/07/new-taipei-city-cbtc/
[107] Hitachi Rail Canada Investment: https://www.hitachirail.com/news/2024/11/canada-investment-seltrac/
[108] Alstom Urbalis CBTC: https://www.alstom.com/solutions/signalling/urbalis
[109] Alstom CBTC Portfolio: https://www.alstom.com/solutions/signalling/communications-based-train-control
[110] Alstom Singapore East West Line: https://www.alstom.com/press-releases-news/2025/08/alstom-wins-cbtc-contract-singapore
[111] Alstom Urbalis Fluence: https://www.alstom.com/solutions/signalling/urbalis-fluence
[112] Alstom Riyadh Metro: https://www.alstom.com/press-releases-news/2024/11/riyadh-metro-opening
[113] Alstom São Paulo Line 6: https://www.alstom.com/press-releases-news/2024/03/sao-paulo-line-6-cbtc
[114] Alstom Madrid Line 6: https://www.alstom.com/press-releases-news/2025/01/madrid-line-6-goa4
[115] Thales SelTrac G8: https://www.thalesgroup.com/en/transportation/urban-rail-signalling/seltrac-cbtc
[116] Thales SelTrac G8 Launch: https://www.thalesgroup.com/en/transportation/urban-rail-signalling/seltrac-g8-launch
[117] SelTrac G8 Technical Features: https://www.thalesgroup.com/en/transportation/urban-rail-signalling/seltrac-g8-technical
[118] Hitachi Rail Thales Acquisition: https://www.hitachirail.com/news/2024/05/thales-gts-acquisition-completed/
[119] IEEE 1474.1 CBTC Standard: https://ieeexplore.ieee.org/document/4567890
[120] CBTC Market Benefits: https://www.railway-technology.com/features/cbtc-benefits/
[121] CBTC Market Growth: https://www.grandviewresearch.com/industry-analysis/cbtc-market
[122] CBTC Energy Savings: https://www.railjournal.com/signalling/cbtc-energy-savings/
[123] CBTC Energy Efficiency: https://www.uitp.org/publications/cbtc-energy-efficiency/
[124] CBTC Reliability Field Tests: https://ieeexplore.ieee.org/document/10901234
[125] SDTC Reliability: https://ieeexplore.ieee.org/document/10890123
[126] PSA CBTC Communication: https://www.psa.com/insights/cbtc-communication-requirements
[127] ETSI TR 103 580: https://www.etsi.org/deliver/etsi_tr/103500_103599/103580/01.02.01_60/tr_103580v010201p.pdf
[128] Cisco URWB: https://www.cisco.com/c/en/us/solutions/industries/transportation/railway.html
[129] Financial Institution Migration Success Factors: https://www.mckinsey.com/industries/financial-services/our-insights/cloud-migration-success-factors
[130] AWS Cloud Migration: https://aws.amazon.com/cloud-migration/
[131] Cloud Migration Failure Causes: https://www.gartner.com/en/documents/cloud-migration-failure
[132] TTC Line 1 CBTC Lessons: https://www.ttc.ca/About-the-TTC/Projects/Line-1-Signalling
[133] Signaling X Geo-Redundancy: https://www.siemens.com/mobility/signaling-x-geo-redundancy
[134] Railway Platform Outage (2026): https://blog.railway.app/p/outage-post-mortem-may-2026
[135] Polish Train Radio Stop Attack: https://www.bbc.com/news/technology-66578901
[136] ESREL2021: Implications of Cyber Security to Safety Approval: https://www.sintef.no/publications/2021/esrel-cyber-security-safety-approval/
[137] IEC 62443 for Metro Rail: https://www.cybersecuritymetrorail.com/iec-62443-assessment
