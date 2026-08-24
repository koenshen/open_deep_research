# Improving Static Noise Margin (SNM) of SRAM Cells Through Advanced Manufacturing Processes: A Comprehensive Analysis

## Introduction

The Static Noise Margin (SNM) of SRAM cells represents one of the most critical parameters determining memory stability, reliability, and bit-flip immunity in modern integrated circuits. As semiconductor manufacturing has progressed from planar transistors through FinFETs to Gate-All-Around (GAA) nanosheet architectures, the fundamental approaches to improving SNM have evolved dramatically. This report provides a comprehensive analysis of how advancements in chip manufacturing processes can improve SRAM SNM, covering fundamental definitions, process technology evolution, manufacturing parameter optimization, layout techniques, variability mitigation, trade-offs, and the latest industrial implementations from leading foundries and research institutes.

---

## 1. Understanding Static Noise Margin (SNM): Definition, Measurement, and Critical Importance

### 1.1 Definition and Fundamental Concept

Static Noise Margin (SNM) is defined as the maximum DC noise voltage that an SRAM storage cell can tolerate without erroneously flipping its stored data state. If the applied noise exceeds the SNM, the cell's stored bit is corrupted, resulting in a data retention failure [1][2]. The SNM is determined by analyzing the voltage transfer characteristics (VTCs) of the two cross-coupled inverters that form the core of an SRAM cell.

The fundamental principle is that an SRAM cell must maintain bistability—it must have two distinct, stable operating points representing logic "0" and logic "1". The SNM quantifies the robustness of this bistability against external disturbances [3].

### 1.2 Measurement Methods

#### Butterfly Curve Method

The traditional and most widely used method for measuring SNM involves constructing a "butterfly curve" from the overlapping voltage transfer characteristics of the two inverters. The SNM corresponds to the side length of the largest square that can be nested inside the butterfly loop [1][4].

The methodology involves:
- Plotting the VTC of inverter 1 (Vout1 vs. Vin1) and the inverse VTC of inverter 2 (Vin2 vs. Vout2)
- Rotating the coordinate system by 45 degrees to find the maximum inscribed square
- Computing the SNM as the side length of this square [2]

The butterfly curve method provides a clear visual representation of cell stability. However, it has limitations: it cannot be used for inline testing, it is time-consuming, and it may give inaccurate results when supply voltage is scaled down, causing distorted VTC curves [7].

#### N-Curve Method

The N-curve method addresses limitations of the butterfly approach by providing both voltage and current information simultaneously. Four key parameters are extracted from the N-curve [6][7]:

- **SVNM (Static Voltage Noise Margin):** The voltage noise margin during read operation
- **SINM (Static Current Noise Margin):** The current noise margin during read operation
- **WTV (Write Trip Voltage):** The voltage required to write the cell
- **WTI (Write Trip Current):** The current required to write the cell

The N-curve method offers significant advantages: it enables inline testing, provides additional current-domain stability information, can analyze power dissipation during read/write operations, and overcomes the scaling limit of Vdd/2 for read stability [7][9].

A critical insight from N-curve analysis is that two different SRAM cells can have identical SNM and SVNM values but different SINM values, meaning they are not equally stable. This difference is only visible through the N-curve's current information, making it essential for nanometer SRAM design [9].

### 1.3 Hold SNM vs. Read SNM

SRAM cells exhibit different noise margins depending on their operating mode:

- **Hold Static Noise Margin (HSNM):** Measured when the cell is in standby mode (word line deactivated). The cell is isolated from bit lines, and the two inverters form a stable feedback loop. HSNM is generally larger than RSNM [5][13].

- **Read Static Noise Margin (RSNM):** Measured during read operations when the word line is activated and access transistors are turned on. The read operation creates a disturbance because the internal storage node cannot reach true 0V (it becomes 0 + ΔV'), shrinking the butterfly loop and reducing the maximum nested square size [5][14].

RSNM is significantly smaller than HSNM because during read operations, pass gate transistors are active, disturbing internal storage nodes. The NMOS portion of the VTC gets distorted due to current flow, while the PMOS portion remains relatively unaffected [5]. As supply voltage scales down, this effect becomes more pronounced. For example, at 400mV VDD, the nested square is 105mV; at 250mV VDD, it shrinks to 45mV [5].

### 1.4 Why SNM is Critical for SRAM Stability and Bit-Flip Immunity

SNM is critical for three primary reasons:

**1. Data Integrity Assurance:** SNM determines the cell's ability to retain stored data in the presence of noise. If SNM is too low, even small disturbances from power supply noise, thermal noise, coupling from adjacent cells, or radiation-induced charge injection can cause bit flips [1][2].

**2. Read Stability:** During read operations, the read disturbance mechanism makes cells particularly vulnerable. The read static noise margin (RSNM) is the most degraded parameter, especially in the pull-down transistor during read operations [14]. If the read disturbance exceeds the cell's tolerance, the cell can flip before the data is sensed, causing a read failure.

**3. Low-Voltage Operation:** As supply voltages scale down to reduce power consumption, SNM decreases proportionally. This creates a fundamental challenge for energy-efficient designs: lower voltage operation requires higher SNM, but the two are inherently in conflict [3][5].

The SNM also directly impacts the minimum operating voltage (Vmin) of the SRAM array. Below Vmin, the cell's SNM becomes insufficient to guarantee data retention, limiting the extent of voltage scaling for power reduction [15].

---

## 2. Process Technology Advancements for SNM Improvement

### 2.1 Planar to FinFET Transition

The transition from planar MOSFETs to FinFETs represented a major breakthrough in SRAM stability. FinFETs provide superior electrostatic control through a three-sided gate structure that wraps around the channel fin, significantly reducing short-channel effects and improving subthreshold slope [1][11].

#### SNM Improvement Quantified

FinFET-based SRAM cells achieve dramatic SNM improvements over planar designs:

- The optimal FinFET SRAM configuration with fin thickness (T_fin) of 10nm and fin height (H_fin) of 40nm demonstrates three times larger read and write noise margins compared to planar SRAM bit-cells, despite fin thickness variation [1].

- 6T FinFET-based SRAM cells with built-in feedback achieve up to 2x improvement in SNM without area penalty [11][12].

- Conventional 6T FinFET DG cells with high Vt achieve 175mV read SNM, representing a 30% improvement over bulk-Si with β-ratio=1.5. Upsizing the pull-down transistor by one fin yields 240mV SNM (16.6% area penalty) [4].

- 6T FinFET with built-in feedback (back-gate connection) achieves 300mV SNM—a 71% improvement over conventional double-gate design—with no area penalty (2% area reduction). Standby leakage is less than 0.2nA/cell [4].

#### Variability Reduction

One of the most significant advantages of FinFETs for SRAM is the elimination of heavy doping in the channel. This minimizes Vt variations due to statistical dopant fluctuation effects, which were a major source of SNM degradation in planar technologies [4]. FinFET-based SRAM cells have tighter SNM distributions (sigma = 5-6.6mV) compared to bulk-Si (sigma = 16mV) [6].

#### Scaling Benefits

FinFET technology enables better control over short-channel effects, allowing continued scaling while maintaining acceptable SNM. The 10nm node FinFET SRAM demonstrates that reduced fin width and increased fin height structures provide high radiation hardness, with displacement defects at the fin top interfering with the main current path but causing less SNM degradation than in planar designs [14].

### 2.2 FinFET to Gate-All-Around (GAA) Nanosheet Transition

The transition from FinFETs to GAA nanosheet transistors represents the next major architecture evolution, driven by the physical limitations of FinFETs at gate lengths below approximately 7nm. At these dimensions, the FinFET's three-sided gate can no longer prevent the drain's electric field from penetrating the channel—a failure mode known as drain-induced barrier lowering (DIBL) [23][24].

#### Why GAA Replaces FinFET

Several factors drive this transition:
- FinFET's three-sided gate provides insufficient electrostatic control at sub-7nm gate lengths
- Fin profiles are never perfectly straight, causing leakage at the bottom of the fin
- As scaling forces a move from two-fin to single-fin devices, the single fin would need to be impractically tall (e.g., 100nm vs. 50nm), introducing excessive parasitics [24]

The nanosheet solution involves "chopping" a single fin into stacked horizontal slabs (typically 20-25nm tall) with gate wrapping around all four sides, offering superior electrostatic control and effective width while minimizing parasitics [24].

#### GAA Electrostatic Superiority

GAA nanosheet FETs provide superior gate control by surrounding the gate around all four sides of the channel, producing higher 'ON' current and improved electrostatic control compared to FinFETs [23]. GAA transistors achieve a 65 mV/dec subthreshold swing at short gate lengths, with gate structures surrounding all four sides of the channel to deliver higher ON current [23].

#### Nanosheet Design Flexibility

A key advantage of GAA over FinFET is the ability to tune nanosheet width for specific applications. In FinFETs, the channel perimeter (Weff) is quantized in discrete fin multiples. GAA offers continuous width adjustment within the nanosheet design [19].

For the same channel perimeter, GAA NMOS and PMOS show 23% higher and 14% lower drive-current respectively than FinFET NMOS and PMOS [19]. Research on nanosheet width optimization for 3nm GAA SRAM found that non-equal nanosheet widths (16nm for NMOS and 12nm for PMOS) are optimum, leading to 17% higher write-ability and 7-9% lower write delay than FinFET SRAM [19].

#### Variability Considerations at N3

At the 3nm node, variability analysis reveals that Metal Gate Granularity (MGG) is the dominant source of variability for both FinFET and nanosheet technologies. Given the low channel doping, Random Discrete Dopants (RDD) have a small impact compared to other variability sources. Nanosheet FETs show better mean subthreshold slope compared to FinFETs, but the reduction of metal gate grain sizes is crucial to reduce variability at N3 for both architectures [21].

### 2.3 Forksheet Architecture

The forksheet device architecture, introduced by IMEC in 2017, represents a natural evolution of the GAA nanosheet device. It places a dielectric wall between nMOS and pMOS devices, enabling tighter n-to-p spacing and cell area reduction [17][18].

#### Key Advantages

- Allows track height scaling from 5T to 4.3T while maintaining performance gain
- Provides 10% performance increase compared to nanosheet devices
- Achieves 24% power reduction at constant speed
- Enables more than 20% cell area reduction [17][22]

#### Outer Wall Forksheet (2025)

IMEC's latest outer wall forksheet design places the dielectric wall at the standard cell boundary (as a p-p or n-n wall), allowing it to be thicker (~15nm) and shared with neighboring cells. Key improvements include [21]:

- A wall-last integration approach using mainstream silicon dioxide
- Relaxed wall width for process simplification
- Easily connected n-p gates
- Superior gate control via an Ω-gate structure (achieved by 5nm wall etch-back, boosting drive current by ~25%)
- Ability to achieve full channel strain through effective source/drain stressors

Benchmarking showed a 22% area reduction for outer wall forksheet-based SRAM cells compared to A14 nanosheet designs [21].

### 2.4 Complementary FET (CFET)

CFET architecture represents the ultimate scaling approach, where nMOS and pMOS devices are stacked vertically on top of each other. This maximizes effective channel width while minimizing area [18][23].

#### Double-Row CFET (IMEC, 2024)

IMEC proposed a new CFET-based standard cell architecture featuring two rows of CFETs with a shared signal routing wall in between. Designed for the A7 technology node, it allows standard cell heights to be reduced from 4 to 3.5T compared to conventional single-row CFETs, translating to a 15% area reduction for SRAM cells and more than 40% area shrinkage compared to A14 nanosheet technology [39].

#### 3-Tier CFET SRAM

The 3-Tier CFET architecture demonstrates a significant cell area reduction of approximately 29.5% compared with conventional 2-Tier structures. This miniaturization lowers internal-node capacitance by 13-22%, yielding markedly better write performance (e.g., >39% lower write energy). The optimized design (2P4N+3N_Access) improves read-access time by 11.9% while maintaining robust write characteristics [10].

---

## 3. Process-Level Parameters Affecting SNM

### 3.1 Channel Doping Profiles and Halo Implants

Channel doping profiles have a profound effect on SRAM SNM through their influence on threshold voltage (Vt), short-channel effects, and variability.

#### Sensitivity to Dopant Fluctuations

Research on the sensitivity of SNM to random dopant variations in 6T SRAM cells reveals that the most sensitive regions to doping fluctuations extend approximately 10nm below the oxide/semiconductor interface and are located in the middle of the conduction channels for both p-channel and n-channel transistors [3]. This means that precise control of the channel doping profile is essential for maintaining consistent SNM across the array.

#### Halo Implant Engineering

Halo implantation creates locally confined doping profiles that provide several benefits:
- Enables VDD-scalable subthreshold operation with constant band-to-band tunneling (BTBT) current
- Provides additional design knobs (halo energy and tilt angle) to reduce tunneling current
- Improves short-channel behavior compared to retrograde doping profiles
- Enables leakage suppression with reduced ion dose while maintaining equivalent Vt [10]

In advanced nodes, halo engineering is critical for managing gate-induced drain leakage (GIDL), which becomes a significant leakage mechanism at scaled dimensions. The IBM ultralow-power SRAM technology paper notes that a significant portion of development effort focused on GIDL reduction through halo and extension implant engineering [7].

#### Proximity Effects

Proximity effects significantly influence doping and stress profiles in 6T SRAM cells, impacting performance by over 10%. Three-dimensional TCAD simulations show that static noise margin exhibits a 6-8% difference between continuous and discrete 6T SRAM cell simulations. Doping shadowing and stress reduction have counteractive effects on SRAM cell characteristics, complicating performance prediction [4].

### 3.2 Gate Oxide Thickness and High-k/Metal Gate

The transition to high-k/metal gate (HKMG) stacks was driven by the fundamental limitations of SiO₂ scaling. At the 45nm node, SiO₂ gate oxide thickness reached approximately 7.5Å, where direct tunneling leakage becomes prohibitive [9].

#### HKMG Benefits

The switch to high-k + metal gate represents one of the major changes since the advent of CMOS technology. Key benefits include:
- Equivalent oxide thickness (EOT) scaling while maintaining low gate leakage
- 25× (NMOS) and 1000× (PMOS) gate leakage reduction at the 45nm node
- 32% drive current improvement [9]

#### EOT Scaling Requirements

Further scaling demands even smaller EOT: 32nm node requires 8Å, and 22nm requires 6Å. The HKMG approach is not merely a materials swap—it represents a fundamental rethinking of gate stack physics, process integration strategy, and device design methodology [10].

#### Work Function Setting

The effective work function (EWF) is not purely an intrinsic material property; it is also influenced by the physical geometry of the gate trench, becoming increasingly significant at sub-28nm dimensions [10]. Two main integration approaches are used:

**Gate First Technology:** WF is set via dipole formation at the interface between the SiON interfacial layer and high-k dielectric, using La for NMOS and Al for PMOS, driven in by high-temperature anneal.

**Gate Last Technology:** NMOS uses Al (WF 4.1 eV) with TiN/TaN protection layers to prevent Al spiking; PMOS uses TiN (WF tunable ~5 eV). WF is defined by metal-metal interdiffusion in a multilayer stack [7].

### 3.3 Threshold Voltage (Vt) Engineering

Threshold voltage engineering is a powerful tool for improving SRAM SNM. For 6T-SRAM, cell stability can be improved by selecting device threshold voltages: low pFET Vt for pull-up transistors and high nFET Vt for pass-gate transistors [17].

#### Vt Optimization Strategies

The optimal Vt configuration for SRAM involves:
- **Pull-up transistors (PMOS):** Low Vt to provide strong feedback and improve write margin
- **Pull-down transistors (NMOS):** Moderate Vt to balance read stability and leakage
- **Access transistors (NMOS):** High Vt to reduce read disturbance and improve RSNM [17]

#### Process Corners and SNM

SNM is highly sensitive to process corners. Under 40nm technology, Hspice simulation shows noise margin values ranging from 35.7mV to 152.1mV across different process corners (TT, SS, FF, SF, FS) at various voltages (0.8V, 1.0V) and temperatures (25°C, -40°C, 125°C) [2]. This wide variation underscores the importance of process control for maintaining consistent SNM.

### 3.4 Strain Engineering

Strain engineering is a critical technique for improving carrier mobility and, consequently, SRAM performance and stability.

#### SiGe Channel Engineering

In the FinFET era, SiGe strain engineering became a key innovation alongside HKMG and contact-on-gate structures [1][6]. SiGe channels for PMOS devices introduce compressive strain that enhances hole mobility, improving the pull-up transistor's drive strength and benefiting write margin.

#### Stress-Related Local Layout Effects

PMOS FinFETs are consistently more sensitive to local layout perturbations than n-type devices. PMOS current variations can exceed 10% (approaching ±12% in calibrated models), while NMOS shifts typically stay below 5%. This is because PMOS is strongly driven by longitudinal stress variations, whereas NMOS responds to a mixed combination of stress components that can partially compensate [9].

The strongest layout-dependent effects appear around structures that modify the local mechanical boundary conditions of the channel, especially Diffusion Breaks and Gate Cuts [9].

#### Stress Management in Advanced Nodes

- Single Diffusion Breaks (SDB)—etched late in the process after epitaxial growth—act as a sudden release of mechanical energy, causing PMOS to lose up to 15% of linear drain current
- Double Diffusion Breaks (DDB), defined early in the process, limit degradation to approximately 8%
- NMOS shows a more complex response (-2% to +5%) due to competing effects from trench etch relaxation and dielectric fill recompression [9]

### 3.5 Beta Ratio (β-ratio) and Transistor Sizing

The beta ratio (β = W/L of pull-down transistor divided by W/L of access transistor) is a critical design parameter that directly influences SNM.

#### Quantitative Impact

For a 6T-SRAM cell in 32nm technology, the impact of β-ratio variation is dramatic [1]:

| β-ratio | SNM (mV) | Qcrit (fC) | Write Time (ps) | Power (µW) |
|---------|----------|------------|-----------------|------------|
| 1       | 27.4     | 1.64       | 35.38          | 6.54       |
| 2       | 79.7     | 1.86       | 47.48          | 9.38       |
| 3       | 102.8    | 2.04       | 57.17          | 12.04      |

SNM improves more than 2x as the β-ratio changes from 1 to 3, demonstrating the effectiveness of transistor sizing for stability enhancement [1].

#### Sizing Hierarchy

The fundamental transistor sizing hierarchy for 6T SRAM is:
- **Pull-down (NMOS):** Strongest (largest W/L)
- **Access (NMOS):** Intermediate
- **Pull-up (PMOS):** Weakest

This hierarchy is captured by the β ratio (pull-down to access ratio) and the γ ratio (access to pull-up ratio). The read margin and write margin are in direct conflict: making the pull-down stronger helps read stability but hurts write-ability, and vice versa [18].

---

## 4. Cell Layout Optimizations and Patterning Techniques

### 4.1 EUV Lithography for Tighter Cell Pitches

Extreme Ultraviolet (EUV) lithography at 13.5nm wavelength has become essential for advanced SRAM scaling by enabling single-exposure patterning at dimensions beyond the limits of 193nm immersion lithography.

#### Resolution Enhancement

EUV's shorter wavelength enables single-exposure patterning of features that would require complex multi-patterning with 193i lithography. At 7nm, manufacturers use EUV on select layers to reduce multi-patterning requirements. At 5nm, 193i becomes too costly, requiring unsustainable numbers of process steps. Single patterning with EUV requires only 10 process steps per mask compared to 120 for self-aligned quadruple patterning (SAQP) [7].

#### Scaling Limits

EUV single-patterning reaches limits at 32-30nm pitches with current 0.33 NA technology, primarily due to stochastic failures. For imec N5 (foundry N3) with 21nm pitches, EUV multi-patterning techniques are needed: SADP (self-aligned double patterning), LELE (litho-etch litho-etch), or 193nm immersion-based SAQP/SAOP [8].

Next-generation high-NA EUVL systems (NA=0.55) are being developed to push single-exposure resolution further, which will be critical for continued SRAM cell scaling [8].

#### Stochastic Failure Mitigation

Stochastic failures depend heavily on exposure dose, target CD, and pitch. Higher exposure doses (45mJ/cm² for logic, 33mJ/cm² for memory) help mitigate failures despite cost trade-offs. Post-processing resist smoothening techniques (e.g., quasi-atomic layer etching) show 20-30% LER improvement. Computational lithography techniques like SRAFs and retargeting improve exposure latitude, depth-of-focus, and defect-free CD process windows [9].

### 4.2 Self-Aligned Contacts (SAC)

Self-Aligned Contacts (SAC) represent a critical layout optimization for improving SRAM cell density and performance.

#### Implementation and Benefits

TSMC introduced SAC for the first time at N3B. SAC reduced contact resistance by 45% and variation by 50%. TSMC's scheme on N3B allows the leakage at the gate-contact junction to remain constant even at wider gate lengths and process variations [3].

SAC enables tighter cell layouts by reducing the margin required between contacts and gates, directly contributing to cell area reduction and improved SRAM density.

### 4.3 Diffusion Breaks

Diffusion breaks are critical for defining transistor active regions in SRAM cells and have significant implications for stress management and cell area.

#### Single vs. Double Diffusion Breaks

- **Single Diffusion Breaks (SDB):** Etched late in the process after epitaxial growth, they act as a sudden release of mechanical energy, causing PMOS to lose up to 15% of linear drain current
- **Double Diffusion Breaks (DDB):** Defined early in the process, they limit PMOS degradation to approximately 8% [9]

#### Area Implications

Cell heights depend on contacted poly pitch (CPP) and whether a cell uses DDB or SDB. A DDB adds an additional one-half CPP to each side of a cell. CPP is limited to about 40nm due to device issues [7]. TSMC's N5 uses Continuous Diffusion (CNOD) for horizontal cell separation, which sacrifices some vertical scaling to achieve horizontal savings, unlike the more common SDB approach [8].

### 4.4 Buried Power Rails

Buried Power Rail (BPR) technology places power distribution rails below the active transistor layer rather than on traditional metal layers, enabling significant improvements in SRAM performance and density.

#### Performance Benefits

For SRAM specifically, IMEC's BPR implementation etched deep, narrow trenches between transistor fins and filled them with ruthenium to create buried power lines. The read speed of the resulting memory cells was about 31% faster than conventional SRAM, and writing required 340mV less voltage. Wider bit lines were nearly 75% less resistant, and the new word lines cut resistance by more than 50% [3][5].

#### IR Drop Reduction

A 2019 paper by ARM and IMEC researchers showed BPRs with front-side power delivery improved worst-case IR drop from 70mV to 42mV (1.7× reduction). BPRs with backside power delivery reduced IR drop to 10mV (7× reduction) [1][3][4].

#### Material Considerations

IMEC's BPRs are made from tungsten (4× higher resistance than copper), with via interconnects using ruthenium. The BPRs showed no electromigration failures after 900 hours of continuous use at 330°C at 4 mA/cm² [1][3].

### 4.5 Alternative Cell Architectures

#### 8T SRAM

The 8T SRAM cell provides a much greater enhancement in stability by eliminating cell disturbs during read access. The addition of two FETs eliminates read disturb issues, improving SNM. A ~30% area penalty is incurred with the addition of two extra FETs, but 8T SRAM can allow for continued scaling beyond that which is possible with traditional 6T SRAM [16][17].

The smallest demonstrated 6T half-cell was 0.124 µm², and the smallest full 8T cell was 0.1998 µm² [17]. An optimized 8T cell design shows a 2.1x improvement in read margin over the 6T cell in 90nm technology with a 24% area penalty, and a 9.78x improvement in 32nm technology with a 29% area overhead [4].

#### 9T SRAM

The 9T SRAM cell provides higher stability in read margin due to the use of pass-gate transistors and isolating the read current path. At 45nm/1V, 27°C, the 9T SRAM shows: SVNM=321.67mV, SINM=382.6µA, WTV=594.5mV, WTI=122.4µA, Leakage=11.1pA, compared to 6T: SVNM=320.9mV, SINM=181.2µA, WTV=547.5mV, WTI=78.96µA, Leakage=13.84pA [6].

#### 10T SRAM

The 10T architecture provides superior balance of stability, power efficiency, and performance. An Optimized High Performance 10T (OHP10T) SRAM cell at 22nm technology node demonstrates [43]:
- 40% smaller read delay compared to LP10T
- 15% higher Write Static Noise Margin (WSNM) compared to LP10T (286 mV vs 312 mV)
- 48% higher Read SNM (RSNM) compared to 6T (214 mV vs 81 mV at VDD=0.8V)
- 38% area overhead compared to 6T

#### MediaTek xBIT (ISSCC 2026)

MediaTek presented a novel 10-transistor cell (xBIT) achieving 22-63% higher density than standard 8T bitcells. Average read/write power reduced by over 30%, leakage reduced 29% at 0.5V. Operates from 100 MHz at 0.35V to 4 GHz at 0.95V [6].

---

## 5. Manufacturing Process Variations and Mitigation Strategies

### 5.1 Random Dopant Fluctuations (RDF)

Random dopant fluctuations represent a fundamental source of variability in scaled transistors. In SRAM cells, RDF causes Vt mismatch between adjacent transistors, directly degrading SNM.

#### Sensitivity Analysis

The most sensitive regions to doping fluctuations extend approximately 10nm below the oxide/semiconductor interface and are located in the middle of the conduction channels for both p-channel and n-channel transistors [3]. This means that precise control of the channel doping profile is essential for maintaining consistent SNM across the array.

#### Mitigation: FinFETs and GAA

The elimination of heavy doping in the channel minimizes Vt variations due to statistical dopant fluctuation effects. FinFET-based SRAM cells have tighter SNM distributions (sigma = 5-6.6mV) vs. bulk-Si (sigma = 16mV) [6]. GAA nanosheet transistors further reduce doping-related variability because they operate with even lower channel doping than FinFETs, relying on work function engineering for Vt setting [13].

### 5.2 Line-Edge Roughness (LER)

Line-edge roughness (LER) and line-width roughness (LWR) are caused by stochastic events in lithography and etching processes. In EUV lithography, the challenge is particularly acute because the number of photons is 14 times smaller than in ArF lithography, leading to photon shot noise [14].

#### LER Impact

LER decreases with increasing exposure dose before saturating. There exists an optimum acid diffusion length that minimizes LER. The post-exposure bake (PEB) temperature and time are the dominant factors for LER in EUV processes [14].

For 5nm gate length FinFETs, LER-induced variations in drain current are significant. The absolute drain currents with fat-fin, thin-fin, and big-drain FWRs shift rightward with increasing gate voltage [14].

#### LER-RDF Interaction

LER and RDF must be modeled together for accurate variability predictions. IM-FinFETs and TFETs exhibit significant interactions between LER and RDF, with errors in σI_OFF reaching 97% when assuming independence. Different transistor structures yield varying dependencies between LER and RDF due to localized versus distributed variability [12].

### 5.3 Metal-Gate Workfunction Variation (WFV/MGG)

Metal gate granularity (MGG) has emerged as the dominant variability source in advanced nodes, surpassing RDF and LER at the 22nm technology node and beyond [11].

#### Physical Model

The physical model of work function variability (WFV) in dual metal gate MOSFETs is based on grain orientation differences in polycrystalline metal gates. As gate dimensions contract below 5nm, the number of grains under the gate shrinks to single-digit figures, transforming MGG from a statistical nuisance into a device-limiting, quasi-deterministic mismatch source [6].

#### Impact on SRAM

SRAM circuit analysis shows that write/read failures are underestimated by 9 orders of magnitude by the area-weighted averaged work function model [11]. Below 5nm, the gate volume accommodates only a handful of metal grains, invalidating central-limit-theorem averaging and making σVt non-Gaussian [6].

#### Mitigation Strategies

Several process engineering strategies have been developed for mitigating MGG:

1. **Equiaxed grain deposition by RF-PVD** (STMicroelectronics, 2019): Produces geometrically uniform grains
2. **Amorphous interlayer insertion** (Shanghai Huali): 5-50Å silicon layer between TiN and TaN, annealed to form amorphous TiSiN/TaSiN
3. **Oxygen vacancy passivation in HfO₂** via compressive strain (Vellore Institute of Technology, 2024)
4. **Amorphous top-cap barrier layers** to block oxygen diffusion (Shanghai Huali, 2022): Addressing TiAl oxidation that shifts work function by 66-157% [6]

### 5.4 Advanced Annealing Techniques

#### Laser Spike Anneal (LSA)

Laser Spike Anneal (LSA) is an advanced thermal processing technology that uses short, intense laser pulses to rapidly heat only the near-surface region of a silicon wafer to ultra-high temperatures for sub-millisecond to nanosecond durations. This non-equilibrium thermal process allows the crystal to recrystallize and the dopants to activate before Fickian diffusion can smear the precisely implanted spatial profiles [11].

#### Benefits for SRAM

LSA creates highly activated, ultra-shallow junctions with near diffusion-less boundaries in silicon. This produces more uniform temperature and stress distributions in product wafers than lamp-based short-time annealing processes [14].

LSA became essential at 65nm CMOS, standard at 28nm planar for source/drain extensions, and evolved for 14nm FinFETs to provide conformal activation across high-aspect-ratio fins. At 7nm and beyond, sub-millisecond to nanosecond regimes are required to preserve delicate strain engineering [11].

Dual-beam LSA configurations provide:
- Long dwell applications (~10 msec) using a second preheat laser to enable defect annealing, solid phase regrowth, and stress reduction
- Low temperature applications (500-1000°C) enabling nickel silicide formation and post-silicide dopant re-activation with minimal pattern effects [13]

### 5.5 Statistical Design Optimization

With the worst-case design approach, meeting the SINM constraint results in over-designing for the actual read stability (~25% for 130nm and ~40% for 65nm) and for the area (~15% for 130nm and ~26% for 65nm). The increasing over-design and the hard-to-meet design criteria make statistically-aware circuit optimization very promising for SRAM cell designs in future technology nodes [9].

---

## 6. Trade-offs Between SNM and Other SRAM Metrics

### 6.1 Read Stability vs. Write Margin

The fundamental trade-off in 6T SRAM design is between read stability and write-ability. The same feedback mechanism that makes the cell stable during hold makes it difficult to read without disturbing the state, and difficult to write against its own resistance [18].

#### Quantitative Trade-off

Increasing cell ratio (β) improves read stability (SINM improves ~50% when ratio increases from 1.33 to 2) but degrades write-ability. Decreasing pull-up ratio improves write-ability but degrades read stability [9]. As SVNM increases, WTV decreases, illustrating the trade-off between read margin and write margin [6].

#### Assist Circuit Techniques

Read and write assist circuits have been developed to manage this trade-off, but they introduce their own complexities:

**Write Assist Techniques (all improve write margin but degrade read noise margin):**
- Reducing VDD of the SRAM cell
- Increasing VSS (cell ground)
- Word Line Boosting
- Negative Bit Line (NBL) [25][26]

**Read Assist Techniques (improve read static noise margin by reducing read disturb):**
- Under-driven word line
- Reduced bit line VDD
- Suppressed word line [25]

### 6.2 Cell Area vs. Stability

There is a direct trade-off between cell area and SNM. Increasing transistor sizes improves SNM but increases cell area, reducing memory density.

#### Quantitative Example

For FinFET-based SRAM:
- Upsizing the pull-down transistor by one fin yields 240mV SNM but incurs a 16.6% area penalty
- Rotating the NPD to (100) plane yields 200mV SNM with a 13.3% area penalty [4]

#### Alternative Cell Topologies

Different cell topologies offer different trade-offs between area and stability:

| Cell Type | Area Overhead vs. 6T | SNM Improvement |
|-----------|---------------------|-----------------|
| 8T | ~30% | Eliminates read disturb |
| 9T | ~40% | Higher read margin |
| 10T | ~38% | 48% higher RSNM |
| 11T | ~50% | >6x SNM improvement |

### 6.3 Leakage Power vs. SNM

There is a fundamental tension between reducing leakage power and maintaining SNM, particularly at low voltages.

#### Leakage Reduction Techniques

Five circuit-level leakage reduction techniques have been investigated, each with different impacts on SNM [8]:

1. **Body Biasing:** Reverse body biasing raises Vt to reduce sub-threshold leakage, but effectiveness decreases with scaling. Maximum leakage savings of 1.18x for raising VNWELL to 1.4V and 1.46x for VPWELL at -0.4V.

2. **Source Biasing:** Raising source voltage to 0.4V achieved 8.16x leakage reduction, but at the cost of decreased SNM and increased delay.

3. **Dynamic VDD:** 0.5V standby VDD obtains maximum 15.8 times leakage energy saving, but reduces hold-SNM to only 169.2 mV, which may cause retention data flipping failures.

4. **Negative Word Line:** Maximum 1.22x leakage reduction at -1.2V, but gate leakage increases.

5. **Bit Line Floating:** Maximum 1.25x leakage reduction; saves 24% leakage power in I-cache memories.

#### Sub-3nm Leakage Management

At below-3nm nodes, no single technique is sufficient. State-of-the-art implementations combine high-Vt cell transistors, adaptive body biasing, power gating with virtual rails, dynamic retention voltage scaling, and asymmetric device doping to simultaneously address sub-threshold, gate, GIDL, and junction leakage [8].

### 6.4 Access Time vs. SNM

Increasing SNM generally comes at the cost of reduced access time. The β-ratio optimization demonstrates this clearly: the write time increases from 35.38ps at β=1 to 57.17ps at β=3 [1].

#### Read Delay Trade-offs

For the 10T SRAM, the OHP10T achieves 40% smaller read delay compared to LP10T while also providing 15% higher WSNM, demonstrating that clever circuit design can partially mitigate the trade-off [43].

#### Vmin Scaling

The minimum operating voltage (Vmin) is a measure of the process quality and is driven by defect control. Vmin is not a design parameter but rather is controlled by the foundry [18]. Lower Vmin enables greater voltage scaling for power reduction but requires higher SNM to maintain data integrity.

---

## 7. Most Promising Recent Industrial Results

### 7.1 TSMC Results

#### TSMC N5 (5nm, ISSCC 2020)

TSMC's 5nm process featured the world's smallest SRAM cell at 0.021 µm², using more than 10 EUV mask patterning steps and High Mobility Channel (HMC) technology. The process achieved 1.84x logic density improvement compared to 1.35x SRAM density improvement [9].

Write assist techniques demonstrated:
- Negative Bit Line (NBL) improves Vmin by 300mV
- 24% Lower Cell VDD (LCV) improves Vmin independently by over 300mV

A high-speed SRAM array for L1 cache application achieved 4.1GHz at 0.85V on a 135 Mb test chip [9].

#### TSMC N3 (3nm, IEDM 2022)

N3 is TSMC's last FinFET node. N3E has the same SRAM bit-cell size as the N5 family (0.021 µm²). The N3 processes use FINFLEX technology, allowing variable numbers of fins for different power/performance/area trade-offs in the same process [33].

SRAM scaling has completely decoupled from logic scaling at N3: the node delivered 1.7x transistor scaling but only 1.0x SRAM scaling [6][7][8].

#### TSMC N2 (2nm, IEDM 2024 / ISSCC 2025)

TSMC's N2 process with GAA nanosheet transistors achieves a high-density SRAM bit cell size of approximately 0.0175 µm², enabling SRAM density of approximately 38 Mb/mm² [7][15].

**Key Performance Metrics:**
- 24-35% less power consumption or 15% more performance at the same voltage
- 1.15x higher transistor density compared to N3
- ~20% clock boost and ~75% standby power reduction at 0.5V-0.6V low voltage ranges
- 20-35 mV reduction in minimum operational voltage (Vmin) for SRAM
- Barrier-free tungsten wiring cutting vertical gate contact resistance by 55%
- Six voltage threshold levels (6-Vt) spanning a 200 mV range [30]

**SRAM-Specific Innovations:**
- Doubles the maximum bitline loading from 256 to 512 cells per bitline due to improved on-to-off current ratios in nanosheet technology
- Achieves 38.1 Mb/mm² density—a 10% improvement over the previous node [19]

**Yield Status:**
- >80% average yield and >90% peak yield on a 256 Mb SRAM array
- Yields for 256 Mb SRAM devices reached approximately 70% average (March 2024), up from 35% in April 2023 [7][32]

**Production:** N2 entered volume production in Q4 2025 [7].

### 7.2 Samsung Results

#### Samsung 3nm GAA MBCFET (ISSCC 2021)

Samsung demonstrated a 256 Mb MBCFET SRAM chip with a 56mm² die size at ISSCC 2021. By using transistors with wider channels for pass gates and transistors with narrower channels for pull-ups, Samsung decreased writing voltage by 230 mV compared to a regular SRAM cell [16][34].

Samsung's proprietary MBCFET technology utilizes nanosheets with wider channels, allowing higher performance and greater energy efficiency compared to GAA technologies using nanowires with narrower channels [13].

**Performance Claims vs. 5nm:**
- First-generation 3nm: 45% reduced power consumption, 23% improved performance, 16% smaller surface area
- Second-generation 3nm: 50% reduced power consumption, 30% improved performance, 35% smaller area [13]

#### Samsung Adaptive Dual-Bitline (ADBL) and Adaptive Cell-Power (ACP) (ISSCC 2021)

Samsung exploited the ability to adjust nanosheet width to tune SRAM bitcell transistors, improving the PU:PG:PD ratio beyond the 1:1:1 limitation of FinFETs. Key features:
- ADBL adds a switchable second bitline to reduce write resistance by 70%
- ACP uses two power switches at the array top and bottom to selectively increase write margin
- Cumulative VMIN reduction was up to 230 mV [34]

#### Samsung SF2 (2nm, 2025)

Samsung SF2 started mass production since Q4 2025, targeting the Exynos 2600 (Galaxy S26). Yields are ~50% (lower than competitors). SF2P is targeted for late 2026 [13].

### 7.3 Intel Results

#### Intel 18A (1.8nm, ISSCC 2025)

Intel 18A combines RibbonFET (GAA) transistors with PowerVia backside power delivery technology. The SRAM bit cell areas are [17][18][19]:
- High-Current Cell (HCC): 0.023 µm²
- High-Density Cell (HDC): 0.021 µm²
- Macro bit density: 38.1 MBit/mm², matching TSMC's N2 node

**Performance vs. Intel 3:**
- 25% higher frequency at iso-voltage (1.1V)
- 36% lower power at same frequency
- Up to 38% power savings at low voltage (<0.65V)
- Over 30% density scaling [16][17]

**Process Specifications:**
- Contacted Poly Pitch (CPP) = 50 nm
- M0 Pitch = 32 nm
- 10ML frontside metal layers (low cost/high density) or 14-16ML (high performance)
- 3ML+3ML backside metal layers [17]

Intel 18A is in high-volume manufacturing since late 2025, powering Core Ultra Series 3 (Panther Lake), launched CES 2026 [13].

#### Industry Positioning

Based on analysis, Intel 18A is believed to have the highest performance among 2nm-class processes, with TSMC in second place and Samsung in third place. TSMC leads in high-density logic cell transistor density, followed by Intel and Samsung [32].

### 7.4 IMEC Research Results

#### Forksheet Device (2017-2025)

IMEC introduced the forksheet in 2017 as a scalable device architecture to extend the GAA nanosheet-based logic roadmap. The first electrical demonstration of integrated forksheet FETs was reported at VLSI 2021, showing short-channel control (SSSAT=66-68 mV/dec) comparable to GAA nanosheet devices down to 22nm gate length [23].

The outer wall forksheet (VLSI 2025) demonstrates a 22% area reduction for SRAM cells compared to A14 nanosheet designs, with the ability to achieve full channel stress through effective source/drain stressors [21].

#### CFET Development (2024-2026)

IMEC's double-row CFET architecture (IEDM 2024) for the A7 technology node allows standard cell heights to be reduced from 4 to 3.5T, translating to a 15% area reduction for SRAM cells and more than 40% area shrinkage compared to A14 nanosheet technology [39].

A DTCO study on scaling monolithic CFET across A7, A5, and A3 nodes (February 2026) identified required performance boosters:
- **A7 node:** Minimizing gate parasitic capacitance; optionally implementing an M0 power rail
- **A5 node:** Requires introduction of an outer wall forksheet architecture with omega-shaped gate
- **A3 node:** Requires hybrid channel orientations (different orientations for n- and pMOS) [40]

#### IMEC's Sub-2nm Roadmap

IMEC's chip scaling roadmap projects an introductory pace of 2 to 2.5 years per node, reaching from 7nm to 0.2nm (2 ångström) by 2036. The roadmap outlines:
- Standard FinFET transistors lasting until 3nm
- GAA nanosheet designs entering high-volume production in 2024
- Forksheet designs at 2nm and A7 (0.7nm)
- Complementary FET (CFET) at A10 (1nm, 2028)
- 2D monolayer materials (WS2, molybdenum) for the ångström age (0.2nm/2Å by 2036) [20][24]

---

## 8. Summary and Future Outlook

The improvement of Static Noise Margin in SRAM cells through manufacturing process advancements has evolved through several distinct phases, each building on the previous:

1. **Planar to FinFET Transition:** Achieved ~3x SNM improvement through better electrostatic control and reduced variability from undoped channels
2. **FinFET to GAA Nanosheet:** Further improved electrostatic control with 360° gate encirclement, enabling continued scaling and providing design flexibility through variable nanosheet widths
3. **Forksheet and CFET:** Pushing toward ultimate area efficiency with n-p gate sharing and vertical device stacking

Key process-level optimizations that contribute to SNM improvement include:
- Channel engineering (doping profiles, halo implants, strain engineering)
- Gate stack optimization (high-k dielectrics, work function tuning)
- Transistor sizing (beta ratio optimization)
- Advanced annealing (laser spike anneal for ultra-shallow junctions)
- Variability mitigation (MGG reduction, LER control)

The most promising recent results demonstrate that:
- TSMC N2 and Intel 18A both achieve approximately 38 Mb/mm² SRAM density
- Samsung's 3nm GAA MBCFET achieves 230mV write voltage reduction through nanosheet width optimization
- IMEC's forksheet and CFET architectures promise continued scaling beyond 2nm

The fundamental trade-offs between SNM, cell area, read/write margin, leakage power, and access time remain, but advanced process technologies and circuit techniques continue to push the boundaries of what is achievable. The transition to GAA nanosheet technology at 2nm-class nodes represents a significant inflection point, enabling SRAM scaling that had stalled at 3nm to resume meaningful progress.

---

## Sources

[1] Rajendran, A. (2011). Noise Margin, Critical Charge and Power-Delay Tradeoffs for SRAM Design Space Exploration: https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=case1307667225&disposition=inline

[2] CN102915771A - SRAM noise margin measuring method: https://patents.google.com/patent/CN102915771A/en

[3] Oniciuc, L. & Andrei, P. (2008). Sensitivity of static noise margins to random dopant variations in 6-T SRAM cells: https://www.semanticscholar.org/paper/fb8b229ac7879a9bc6a739a74ac111c621705ff1

[4] Kucherov, A. & Tian, S. (2000). Investigation of Proximity Effects in a 6T SRAM Cell Using Three-Dimensional TCAD Simulations: https://www.academia.edu/43090285/Investigation_of_Proximity_Effects_in_a_6T_SRAM_Cell_Using_Three_Dimensional_TCAD_Simulations

[5] NPTEL-NOC. 4.2 SRAM - Noise Margin Analysis: https://www.youtube.com/watch?v=lZw_DUvMV6Q

[6] Malleshaiah, G.V. & Srinivasaiah, H.C. (2015). Study of SRAM Cell for Balancing Read and Write Margins in Sub-100nm Technology: https://www.ijert.org/research/study-of-sram-cell-for-balancing-read-and-write-margins-in-sub-100nm-technology-using-noise-curve-method-IJERTV4IS060626.pdf

[7] Materials Today: Proceedings (2023). Methods for noise margin analysis of conventional 6T and 8T SRAM cell: https://www.sciencedirect.com/science/article/abs/pii/S2214785323018722

[8] A Black Box Method for Stability Analysis of Arbitrary SRAM Cell Structures: http://blaauw.engin.umich.edu/wp-content/uploads/sites/342/2017/11/412.pdf

[9] Grossar et al. (2006). Read Stability and Write-Ability Analysis of SRAM Cells for Nanometer Technologies: https://lirias.kuleuven.be/retrieve/109654

[10] 3-Tier CFET 6T-SRAM with 2D-TMDs channels for Angstrom technology node: https://www.nature.com/articles/s41598-026-37881-5

[11] Guo, Z. et al. (2005). FinFET-Based SRAM Design: https://ieeexplore.ieee.org/document/1522725

[12] Guo, Z. et al. (2005). FinFET-Based SRAM Design (ISLPED'05): https://www.cecs.uci.edu/~papers/islped05/PAPERS/2005/ISLPED05/PDFFILES/ISLPED05_002.PDF

[13] IEEE ICCSP 2019. Performance Analysis of 6T SRAM Cell on Planar and FinFET Technology: https://ieeexplore.ieee.org/document/8697928

[14] Micromachines (2023). Performance Degradation in SRAM of 10nm Node FinFET Owing to Displacement Defects: https://pmc.ncbi.nlm.nih.gov/articles/PMC10221633

[15] SemiWiki (2020). TSMC's 5nm 0.021um2 SRAM Cell Using EUV and High Mobility Channel: https://semiwiki.com/semiconductor-manufacturers/tsmc/283487-tsmcs-5nm-0-021um2-sram-cell-using-euv-and-high-mobility-channel-with-write-assist-at-isscc2020

[16] IEEE Spectrum (2025). Intel 18A, TSMC N2 Make Tiniest SRAMs: https://spectrum.ieee.org/sram-intel-tsmc

[17] Chang, L. et al. (2005). Stable SRAM Cell Design for the 32 nm Node and Beyond: https://ptacts.uspto.gov/ptacts/public-informations/petitions/1511996/download-documents

[18] Pethe, A. (2024). SRAM Read, Write & Stability Explained: https://www.youtube.com/watch?v=qr9tJlktp2M

[19] Nanosheet Width Investigation for GAA Devices Targeting SRAM Applications at the 3nm Node: http://in4.iue.tuwien.ac.at/pdfs/sispad2021/S1.4.pdf

[20] Kola, S.R. & Li, Y. (2025). Simultaneously Estimating PVE, WKF, and RDF of GAA Si NS CFETs: https://www.mdpi.com/2079-4991/15/17/1306

[21] Microelectronics Journal (2023). On the SRAM with comb-shaped nano FETs: https://www.sciencedirect.com/science/article/abs/pii/S0026269223001556

[22] Electronics, MDPI (2022). A Review of the GAA Nanosheet FET Process Opportunities: https://www.mdpi.com/2079-9292/11/21/3589

[23] Patsnap. GAA transistors at 2nm: nanosheet architecture explained: https://www.patsnap.com/resources/blog/articles/gaa-transistors-at-2nm-nanosheet-architecture-explained

[24] TrendForce (2024). TSMC Reveals N2 Nanosheet Details: https://www.trendforce.com/news/2024/12/16/news-tsmc-reveals-n2-nanosheet-details

[25] IIT Roorkee (2018). Lec 37: Read and Write-Assist Circuits in 6T SRAM: https://www.youtube.com/watch?v=1tQQqBmQ8Z8

[26] IJSTE. Low Voltage and Low Power in SRAM Read and Write Assist Techniques: https://www.academia.edu/30761510/Low_Voltage_and_Low_Power_in_SRAM_Read_and_Write_Assist_Techniques

[27] Valaee, A. (2011). SRAM Read-Assist Scheme for Low Power High Performance Applications: https://spectrum.library.concordia.ca/id/eprint/36175/1/Valaee_MASc_S2012.pdf

[28] Abu-Rahma, M.H. & Anis, M.H. (2013). Variation-Tolerant SRAM Write and Read Assist Techniques: https://www.semanticscholar.org/paper/Variation-Tolerant-SRAM-Write-and-Read-Assist-Abu-Rahma-Anis/bcdda430a996edc5ef624746ad7144ade43c2392

[29] Texas Instruments. US20140241089A1 - Read assist circuit for an SRAM: https://patents.google.com/patent/US20140241089A1/en

[30] Tom's Hardware (2024). TSMC shares deep-dive details about 2nm process node at IEDM 2024: https://www.tomshardware.com/tech-industry/tsmc-shares-deep-dive-details-about-its-cutting-edge-2nm-process-node-at-iedm-2024-35-percent-less-power-or-15-percent-more-performance

[31] TSMC Research (2024). TSMC at IEDM 2024: https://research.tsmc.com/english/collaborations/events/IEDM2024.html

[32] SemiWiki (2025). IEDM 2025 – TSMC 2nm Process Disclosure: https://semiwiki.com/semiconductor-services/techinsights/352972-iedm-2025-tsmc-2nm-process-disclosure-how-does-it-measure-up

[33] Cadence Community (2023). IEDM: TSMC N3 Details: https://community.cadence.com/cadence_blogs_8/b/breakfast-bytes/posts/iedm-tsmc-n3-details

[34] Samsung Semiconductor. 3nm GAA MBCFET: Unrivaled SRAM Design Flexibility: https://semiconductor.samsung.com/news-events/tech-blog/3nm-gaa-mbcfet-unrivaled-sram-design-flexibility

[35] Samsung Semiconductor. Process Technology - Logic Node: https://semiconductor.samsung.com/foundry/process-technology/logic-node

[36] Gul, W. et al. (2022). SRAM Cell Design Challenges in Modern Deep Sub-Micron Technologies: https://pmc.ncbi.nlm.nih.gov/articles/PMC9416021

[37] Samsung Semiconductor (2022). Developing Next-Generation MRAM: https://semiconductor.samsung.com/news-events/tech-blog/developing-the-industrys-most-energy-efficient-next-generation-mram-selected-as-iedm-highlight-paper

[38] IMEC (2024). Imec proposes double-row CFET for the A7 technology node: https://www.imec-int.com/en/press/imec-proposes-double-row-cfet-a7-technology-node

[39] IMEC (2026). Scaling monolithic CFET across multiple logic technology nodes: https://www.imec-int.com/en/articles/performance-boosters-scale-monolithic-cfet-across-multiple-logic-technology-nodes

[40] Springer (2025). A novel 8T SRAM cell using PFC and PPC VS-CNTFET transistor: https://link.springer.com/article/10.1186/s44147-025-00579-y

[41] Choudhary & Yadav (2021). Analysis of Power, Delay and SNM of 6T & 8T SRAM Cells: https://www.semanticscholar.org/paper/Analysis-of-Power%2C-Delay-and-SNM-of-6T-%26-8T-SRAM-Choudhary-Yadav/0a7429fe6c5d155418527b4e8210a23d0446eece

[42] Yadav et al. (2016). Optimized High Performance 10T SRAM Cell Characterization: https://www.ijcaonline.org/research/volume134/number5/yadav-2016-ijca-907964.pdf

[43] Soni, D. & Saha, S. (2023). Leakage Power Reduction and Stability Analysis of 5nm node GAA CNTFET SRAM: https://dspace.nitrkl.ac.in/dspace/bitstream/2080/4315/1/2023_ICCWC_DSoni_Leakage.pdf

[44] IMEC (2025). Outer wall forksheet: bridging nanosheet and CFET: https://www.imec-int.com/en/articles/outer-wall-forksheet-bridge-nanosheet-and-cfet-device-architectures-logic-technology

[45] IMEC (2021). First electrical demonstration of integrated forksheet devices: https://www.imec-int.com/en/press/imec-reports-first-electrical-demonstration-integrated-forksheet-devices-extend-nanosheets

[46] Semiconductor Digest (2019). Imec Presents Forksheet Device: https://www.semiconductor-digest.com/imec-presents-forksheet-device-as-the-ultimate-solution-to-push-scaling-towards-the-2nm-technology-node

[47] IEEE Spectrum (2019). Buried Power Lines Make Memory Faster: https://spectrum.ieee.org/buried-power-lines-make-memory-faster

[48] SemiWiki (2022). Imec Buried Power Rail and Backside Power Delivery: https://semiwiki.com/semiconductor-services/techinsights/314464-imec-buried-power-rail-and-backside-power-delivery-at-vlsi

[49] PDF Solutions. What Silicon Really Says: Diffusion Breaks, Gate Cuts, and LLEs: https://www.pdf.com/what-silicon-really-says-diffusion-breaks-gate-cuts-and-the-anatomy-of-stress-related-lles

[50] PatSnap. Metal gate granularity and threshold voltage at 5nm: https://www.patsnap.com/de/resources/blog/articles/metal-gate-granularity-and-threshold-voltage-at-5nm

[51] Kim, S.-K. (2021). LER from EUV to FinFET: Computational Study: https://pmc.ncbi.nlm.nih.gov/articles/PMC8706712

[52] IBM Research (2009). Physical model of metal grain work function variability: https://research.ibm.com/publications/physical-model-of-the-impact-of-metal-grain-work-function-variability-on-emerging-dual-metal-gate-mosfets-and-its-implication-for-sram-reliability

[53] Veeco. Laser Spike Annealing Advantages: https://www.veeco.com/company/blogs/why-laser-spike-annealing-is-the-right-choice-for-the-digital-transformation

[54] SemiFlows Blog. Laser Spike Anneal (LSA): https://semiflows.com/blog/what-is-laser-spike-anneal-in-semiconductor-manufacturing

[55] Windbacher, R. High-k Gate Stacks: https://www.iue.tuwien.ac.at/phd/windbacher/node13.html

[56] SemiFlows Blog. High-K Metal Gate (HKMG): https://semiflows.com/blog/what-is-high-k-metal-gate-in-semiconductor-manufacturing

[57] Erben, E. et al. (2018). Work Function Setting in High-k Metal Gate Devices: https://www.intechopen.com/chapters/61888

[58] Mann, R.W. et al. (2003). Ultralow-power SRAM technology: http://bitsavers.informatik.uni-stuttgart.de/pdf/ibm/IBM_Journal_of_Research_and_Development/475/mann.pdf

[59] Singh et al. (2011). Leakage power reduction techniques of 45nm SRAM: https://academicjournals.org/journal/IJPS/article-full-text-pdf/029735518905

[60] SemiAnalysis (2026). ISSCC 2026: https://newsletter.semianalysis.com/p/isscc-2026-nvidia-and-broadcom-cpo

[61] TechPowerUp (2025). Intel 18A Node SRAM Density On-Par with TSMC: https://www.techpowerup.com/332850/intel-18a-node-sram-density-on-par-with-tsmc-backside-power-delivery-a-big-bonus

[62] Tom's Hardware (2025). TSMC's N2 process has a major advantage over Intel's 18A: https://www.tomshardware.com/tech-industry/tsmcs-n2-process-has-a-major-advantage-over-intels-18a-sram-density

[63] Samsung Newsroom (2022). Samsung Begins Chip Production Using 3nm Process: https://news.samsung.com/global/samsung-begins-chip-production-using-3nm-process-technology-with-gaa-architecture

[64] TechPowerUp (2021). Samsung Demonstrates 256 Gb 3nm MBCFET Chip: https://www.techpowerup.com/279625/samsung-demonstrates-256-gb-3-nm-mbcfet-chip-at-isscc-2021

[65] WCCFTech (2025). Intel 18A Process Node Details: https://wccftech.com/intel-18a-process-node-25-percent-higher-frequency-36-percent-lower-power-vs-intel-3
