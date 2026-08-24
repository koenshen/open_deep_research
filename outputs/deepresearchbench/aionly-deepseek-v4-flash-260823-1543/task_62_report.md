# Scaling Ion Trap Quantum Computing: Strategies, Feasibility, and Pathways to Fault-Tolerant Systems

## Executive Summary

Trapped ions are among the most mature and highest-fidelity qubit platforms available, holding records for two-qubit gate fidelity (99.99%), single-qubit gate fidelity (99.9999%), coherence times (up to 600 seconds), and quantum error correction efficiency (2:1 physical-to-logical qubit ratios) [1][2][3]. However, the platform's central scaling challenge is architectural: a single chain of ions becomes unusable for high-fidelity gates beyond roughly 20–50 ions because of motional-mode crowding, and the community has converged on several distinct architectural strategies to overcome this limit.

The major scaling strategies are: (1) **QCCD (Quantum Charge-Coupled Device) shuttling architectures**, now commercialized by Quantinuum up to 98 physical qubits with junction-based 2D routing; (2) **modular architectures with photonic interconnects**, demonstrated by Oxford, Duke, Innsbruck, and IonQ, which enable distributed quantum computing across optical links; (3) **monolithic 2D arrays and Penning traps**, including the ETH Zurich micro-Penning trap that eliminates RF fields entirely and has demonstrated record-low heating rates; (4) **junction-based surface trap arrays** enabling 2D shuttling and routing, such as Sandia's 200-ion-capacity "Enchilada" trap; (5) **multiplexed/grid-based QCCD designs** that solve the control-wiring problem via electrode cowiring; and (6) **hybrid approaches**, including deterministic electric-field matter links between modules (Universal Quantum), laser-free electronic qubit control (Oxford Ionics/IonQ), and microwave-driven architectures with on-chip control electronics.

This report assesses each strategy against technical feasibility, engineering limits, current experimental state of the art, practical implementation challenges, and projected timelines. The comparative evaluation concludes that **QCCD-style architectures—especially when combined with electronic (microwave) qubit control, grid-based multiplexing, and semiconductor foundry manufacturing—are the most likely near-term path to fault-tolerant scale**, with modular electric-field and photonic interconnects serving as the natural extension to thousands of qubits. The micro-Penning trap approach is the most promising long-term dark horse because it eliminates RF power scaling entirely. Key milestones to watch include IonQ's 256-qubit system (2026), Quantinuum's Sol (~192-qubit 2D grid, 2027) and Apollo (thousands of qubits, 2029), and Universal Quantum's DLR multi-module machines.

---

## 1. Introduction: The Scaling Challenge

Trapped-ion quantum computing has satisfied all five DiVincenzo criteria for over two decades, with the world's best qubit quality metrics across the board: hyperfine qubit coherence up to 600 s with dynamical decoupling, single-qubit gate fidelities up to 99.9999%, two-qubit entangling gates at 99.9–99.99%, readout fidelity above 99.99%, and coherence-to-gate-time ratios of 10⁷–10⁹ [1][3]. Ions are inherently identical atomic clock standards—identical to 1 part in 10¹⁵—eliminating the fabrication-variability problem that plagues solid-state qubits [2]. Trapped ions also offer all-to-all connectivity within a register, and their properties have enabled the most efficient quantum error correction demonstrated to date: Quantinuum's Helios system converts 98 physical qubits into 48 logical qubits (a 2:1 ratio) using "iceberg" codes, versus roughly 97:1 for Google's superconducting Willow and 10:1 for IBM's qLDPC approach [3]. By one estimate, factoring RSA-2048 would require only ~2,800 physical trapped ions (given ~1,400 logical qubits at a 2:1 code rate), compared with 1–2 million superconducting qubits under a surface code [3].

The fundamental scaling wall is **motional-mode crowding**. Entangling gates in ion traps operate by exciting collective Coulomb phonon modes; in a large crystal, the motional spectrum becomes so dense that individual modes can no longer be addressed spectroscopically, and gate fidelity degrades [1][2][20]. Industry consensus places the practical limit at roughly 20–50 ions per chain for useful gates, though ~100-ion chains and ~300–400-ion Penning crystals have been controlled for simulation purposes [1][2][3]. As the Weizmann group's analysis puts it: there is no fundamental limit to the number of ions confinable in a single 1D register, but long crystals suffer from high heating rates and a dense motional spectrum from "softening" of modes—both of which impede high-fidelity gates [20].

Because ion qubits themselves are so uniform, the scaling problem is overwhelmingly an **architecture and engineering problem** rather than a physics problem [2][3]. Six architectural families have emerged to address it.

---

## 2. The Major Proposed Scaling Strategies

### 2.1 QCCD (Quantum Charge-Coupled Device) Architectures

**Concept.** Proposed by Kielpinski, Monroe, and Wineland in 2002, the QCCD architecture stores ions in memory regions of a segmented trap and physically shuttles them between interaction (gate) zones, splitting and recombining crystals as needed [4]. The key insight is to keep crystals small enough for high-fidelity gates while providing all-to-all connectivity through ion motion. The original proposal included sympathetic cooling with a second species, decoherence-free-subspace encoding to suppress transport dephasing, and transport through T/X junctions [4].

**Demonstrated state of the art.** Honeywell (now Quantinuum) built the first complete QCCD processor, reported in Nature in 2021: a cryogenic 2D surface trap with 198 independently controlled DC gold electrodes and 16 trapping zones, integrating multi-crystal operations, fast transport (intrazone shift 58 μs, interzone shift 283 μs, split/combine 128 μs, swap 200 μs), qubit phase tracking across zones, sympathetic cooling with ¹³⁸Ba⁺ coolant ions, and parallelized operations in two gate zones [5]. Quantinuum then moved to a racetrack (periodic boundary) geometry in H2, which achieved 56 fully connected qubits with all-to-all connectivity, quantum volume 2²⁵, >99.99% single-qubit fidelity, and >99.9% two-qubit fidelity [6][7][8]. Quantinuum's latest system, Helios (launched November 2025), is a 98-qubit processor built on ¹³⁷Ba⁺ with a four-way X-junction connecting memory and logic regions—the first commercial processor with 2D junction-based routing—and achieves 99.921% average two-qubit gate fidelity across all operational zones [3].

**Assessment.** QCCD is the most experimentally mature scaling strategy, with a clear commercial track record and demonstrated fault-tolerant logical qubits. Its limits, analyzed as early as 2016, place single QCCD devices in the ~50–1,000 qubit range before control complexity and transport overhead dominate [2]. Transport and cooling are the runtime bottlenecks: in quantinuum-style QCCD accounting, gate pulses consume only ~2% of runtime, ion movement ~27%, and cooling ~68% [23][24]. Junction transit adds motional excitation that must be cooled before gates. Scaling beyond ~1,000 qubits requires combining QCCD with modular interconnects or grid architectures.

### 2.2 Modular / Networked Architectures with Photonic Interconnects

**Concept.** The Modular Universal Scalable Ion-Trap Quantum Computer (MUSIQC) architecture, patented by Monroe, Kim, and Raussendorf, divides the processor into Elementary Logic Units (ELUs)—each a small ion-trap register—connected by probabilistic photonic entanglement links. Communication ions in each ELU emit photons that interfere at a central Bell-state analyzer; successful detection heralds entanglement between modules. A fully non-blocking N×N optical cross-connect (OXC) switch supports up to N_ELU/2 parallel remote-entanglement operations, with success probabilities approaching p ≈ 10⁻³ per attempt [9]. The architecture can support thousands of qubits from demonstrated components and was explicitly designed to avoid the technical complexity and crosstalk of large segmented traps [2][9].

**Demonstrated state of the art.** The modular approach has been validated step by step: Hucul et al. (2015) demonstrated modular entanglement of atomic qubits using both phonon (within-module) and photon (between-module) buses [10]. Stephenson et al. at Oxford achieved heralded remote entanglement between two trapped-ion nodes with 94% fidelity at 182 Bell pairs/second over a 4-meter fiber link [29]. In 2025, Main et al. at Oxford reported the first fully distributed quantum computation across an optical network link: deterministic teleportation of a controlled-Z gate between circuit qubits in separate modules at 86.2(9)% fidelity, remote entanglement at 96.89(8)% fidelity, and a distributed Grover search algorithm with 71(1)% success rate [11]. At Innsbruck, Krutyanskiy et al. built the first trapped-ion quantum repeater node, distributing entanglement over 50 km of fiber (two 25-km spools) with 0.72 state tomography fidelity at 9.2 Hz—and modeled a network of 17 such nodes connecting nodes 800 km apart [12]. At Duke, the Monroe group has improved photonic entanglement rates by ~6 orders of magnitude over two decades, reaching 250 Hz—the fastest photonic interconnect between quantum memories yet demonstrated—with >97% fidelity using time-bin encoding [61]. IonQ announced in April 2026 that it had photonically interconnected two commercial trapped-ion systems for the first time, in collaboration with the Air Force Research Laboratory [55].

**Assessment.** Photonic interconnects are the only strategy that natively supports distributed, reconfigurable networks without opening vacuum or cryogenic systems, and they are platform-agnostic at the photon interface [11]. The bottleneck is link rate and fidelity: typical rates are ~100 Hz, projected to approach ~10 kHz with advanced photonics [2], and teleported-gate fidelity (86%) remains far below local gate fidelity (99.9%+), requiring entanglement distillation for fault tolerance [3][11]. Industry analysis rates effective photonic entanglement rates at 1–10 Hz, still orders of magnitude below what distributed fault-tolerant computation would need [3].

### 2.3 Monolithic 2D Arrays, Penning Traps, and Micro-Penning Traps

**Concept.** Rather than linear chains, ions can be arranged in 2D Coulomb crystals (in Penning traps or specially designed RF Paul traps) or in 2D arrays of individual micro-traps. NIST has maintained 2D Penning-trap crystals of 100–400 ⁹Be⁺ ions for quantum simulation of long-range Ising models and spin squeezing, though without arbitrary-pair entanglement [1]. Richerme proposed 2D ion crystals in RF Paul traps for simulators, noting micromotion limits resolvability to approximately N ≈ 4/q² ≈ 250 ions [15].

**The decisive advance: the micro-Penning trap.** In 2020, Jain, Alonso, Grau, and Home at ETH Zurich proposed scalable arrays of micro-Penning traps—static electric quadrupole sites in a uniform magnetic field—which eliminate the RF drive entirely and thus remove the dominant power-scaling and junction challenges of Paul traps [14]. In 2024, the same group demonstrated a fully functioning cryogenic micro-Penning trap: a single ⁹Be⁺ ion held 152 μm above a sapphire chip in a static 3 T field, with ground-state cooling of all three motional modes, flexible 2D transport with no measurable motional heating (demonstrated by drawing the ETH Zurich logo), and the **lowest heating rates ever measured in a comparably sized trap** (axial heating rate 0.088(9) s⁻¹; electric-field noise spectral density 3.4×10⁻¹⁶ V²m⁻²Hz⁻¹) [13][43]. The design also enables detaching trap electrodes from external voltage sources mid-operation, further reducing heating [13]. The Zurich spin-out ZuriQ has since built a 9-ion 3×3 array on Infineon's production lines—the largest 2D array of its kind—and plans a 40-ion processor, with qubit density scaling quadratically with chip area [48].

**Assessment.** Micro-Penning arrays are architecturally the cleanest path to massive 2D scaling because static fields avoid RF power dissipation (which scales as roughly n³ with trap length in Paul traps) and junctions altogether [13][14][26]. However, the platform is the least mature: full quantum control has been demonstrated on a single ion, and multi-ion entangling gates in a micro-Penning array remain to be shown at high fidelity. Strong magnetic fields (3 T) also complicate laser systems and require cryogenic operation with a superconducting magnet [13][43].

### 2.4 Junction-Based Surface-Electrode Trap Arrays (2D Shuttling and Routing)

**Concept.** Extend QCCD-style shuttling to 2D by fabricating traps with T-, X-, and Y-junctions so ions can be routed between arbitrary zones. This is the approach NIST identified as providing the best all-to-all connectivity for large-scale fault-tolerant computing, versus O(n) swap overhead for 1D arrays and O(√n)/O(³√n) for 2D/3D lattices without junctions [18].

**Demonstrated state of the art.** Junction transport has progressed dramatically since the first T-junction demonstration in 2006 (which lost ions and imparted ~1 eV of energy, requiring extensive Doppler recooling) [16]. NIST's X-junction transport in 2009 preserved coherence with only a few motional quanta of energy gain [17], and NIST subsequently demonstrated full two-ion reordering through an X-junction with average motional excitation of just 1.1–1.7 quanta [18]. Quantinuum's Helios now operates a four-way X-junction commercially, and Quantinuum has proven the ability to route multiple species (¹⁷¹Yb⁺ and ¹³⁸Ba⁺) through junctions [3][6]. Sandia's "Enchilada" trap—a 2D layout with six Y-junctions and five long linear sections each capable of holding 50 ions—is designed to house up to 200 ions in multiple chains, with the RF electrode raised onto a sixth metal layer and 80% of the underlying dielectric removed to cut power dissipation from 101.6 mW to 38.7 mW [26][27]. The trap's 302 control electrodes are cowired to just 75 independent signals [26].

**Assessment.** Junction arrays are the proven workhorse for 2D connectivity, but junction transit still adds motional excitation that must be cooled, and fabrication complexity grows with junction count. The approach is best viewed as the routing layer within QCCD-grid architectures rather than a standalone scaling strategy.

### 2.5 Multiplexed / Grid-Based QCCD Designs and Optical Segmentation

**Concept.** Two complementary approaches address the two dominant scaling bottlenecks of QCCD: control wiring and serialized operation.

**Grid-based cowiring.** Quantinuum's Delaney et al. (2024) solved the "wiring problem" for 2D QCCD grids by combining electrode cowiring (electrodes at translationally symmetric locations in each grid site share a fixed number of analog voltage signals) with sitewise digital switches (one digital input per site). The number of analog control signals is thus constant regardless of grid size. They demonstrated conditional intrasite crystal reordering and conditional ion exchange between adjacent sites in two-species grids (¹⁷¹Yb⁺–¹³⁸Ba⁺ and ¹³⁷Ba⁺–⁸⁸Sr⁺) with **sub-quanta motional excitation** at exchange rates of 2.5 kHz [19].

**Optical-potential segmentation.** The Weizmann group (Schwerdt et al., 2024) proposed dynamically operated optical tweezers that instantaneously segment a long ion crystal into small, nearly independent cells, enabling **parallel entangling gates on all cells simultaneously**, reconfigurable connectivity, and efficient mid-circuit measurement, with a protocol to compensate crosstalk [20]. This directly attacks the mode-crowding limit of long chains while retaining global register coherence.

**Assessment.** Grid cowiring is arguably the most important control-engineering breakthrough in trapped-ion scaling to date: it makes 2D qubit arrays practical without exponentially growing analog electronics, and it underpins Quantinuum's Sol system (~192 qubits, 2D grid, targeted 2027) [19][32]. Optical segmentation remains at the proposal stage but could enable much larger effective registers by restoring parallel gate throughput.

### 2.6 Hybrid Approaches: Matter Links, Electronic Qubit Control, and Microwave Architectures

**Deterministic matter links (Universal Quantum).** Instead of probabilistic photonic links, Universal Quantum demonstrated deterministic qubit transfer between adjacent ion-trap microchip modules via electric field links: 2,424 ions/second across a 684 μm distance including a 10 μm inter-module gap, with ion-loss infidelity below 7×10⁻⁸ (over 15 million consecutive successful links), no measurable coherence degradation (T₂* = 560(40) ms before and after), and the transported ion accumulating 10.26 km of travel [21][53]. This extends QCCD from a single chip to a multi-chip processor, with the stated goal of linking hundreds or thousands of microchips [53][54].

**Laser-free electronic qubit control (Oxford Ionics, now IonQ).** Oxford Ionics' Electronic Qubit Control (eQC) replaces per-ion laser beams with on-chip microwave/RF electrodes and static magnetic-field gradients, making the qubit-control layer compatible with standard semiconductor manufacturing (fabricated with Infineon). eQC has produced the world's highest published gate fidelities: 99.97% two-qubit and 99.9992% single-qubit (2024), and IonQ reported >99.99% two-qubit fidelity in October 2025—achieved **without ground-state cooling**, removing a major runtime bottleneck [23][30]. As one industry analysis put it: "If eQC scales to hundreds of qubits while maintaining 99.97% two-qubit fidelity, it transforms the trapped-ion modality from a precision-optics discipline into a semiconductor-electronics discipline" [3].

**Microwave-driven QCCD blueprint (Sussex).** Lekitsch et al. (2017) published a complete engineering blueprint for a microwave-driven trapped-ion computer using 1296 X-junctions per 90×90 mm² module, 150 T/m magnetic-field gradients, global microwave fields (a fixed number of radiation fields independent of ion count), on-chip photodetectors, and wafer-stacked DAC electronics—projecting >2 million junctions per vacuum chamber and cycle times of ~235 μs [22].

**Rapid exchange cooling (Georgia Tech).** Fallek et al. (2024) demonstrated exchange cooling—a same-species coolant-ion bank that exchanges energy with hot computational ions via Coulomb interaction—at 107.3 μs per cooling cycle, an order of magnitude faster than sympathetic cooling, removing >96% of axial motional energy. This attacks the 68%-of-runtime cooling bottleneck directly [24].

**Assessment.** Hybrid approaches are where the field is actually converging. Every leading vendor now combines QCCD-style shuttling with one or more of: electronic control (IonQ), grid multiplexing (Quantinuum), electric-field modularity (Universal Quantum), and photonic networking (IonQ, Oxford, academic groups). The modular photonic and matter-link approaches are complementary rather than competitive at this stage.

---

## 3. Technical Feasibility Assessment

### 3.1 Error-Rate Scalability

- **Monolithic chains:** two-qubit gate fidelities of 99.9%+ are routine in small crystals, but gate speed slows and fidelity degrades with chain length due to mode crowding; useful chains are limited to ~20–50 ions [1][2][20].
- **QCCD:** local gates are performed on small crystals, preserving 99.9–99.99% fidelities at system scale (Helios: 99.921% average across all pairs of 98 qubits) [3]. Two-qubit gate errors on Helios are 7.9(2)×10⁻⁴; single-qubit errors 2.5(1)×10⁻⁵ [3].
- **Photonic modular:** local gates match monolithic fidelities; remote teleported gates are the bottleneck at 86% fidelity (Oxford 2025), with error budgets dominated by local mixed-species gates and remote entanglement infidelity [11]. High-fidelity mixed-species gates (99.8%) have been demonstrated locally, suggesting the 86% figure is technically improvable [11][28].
- **2D/Penning:** no demonstration of arbitrary high-fidelity entangling gates in large 2D crystals to date; micro-Penning arrays expect high-fidelity gates via local modes with dipolar coupling rates exceeding decoherence, but only single-ion full control is demonstrated [13][14].
- **Junction/grid arrays:** junction transport has been reduced to sub-quanta excitation (1.1–1.7 quanta for 2D reordering; sub-quanta for grid exchange), so shuttling need not degrade gate fidelity if recooling is applied [18][19].

### 3.2 Ion Shuttling and Transport

Measured transport primitives: ~50 μs over 1.2 mm (>10 m/s) in the original NIST demonstration (with <0.6% Ramsey contrast loss) [4]; 58–283 μs zone operations in H1 [5]; 2.5 kHz grid-site exchange [19]; 2,424 s⁻¹ inter-module matter links [21]. Junction transit is the hardest primitive: early T-junction work imparted ~1 eV (10⁸ quanta), while optimized NIST X-junction transport achieves near-ground-state preservation with failure rates <0.01% [16][17]. Heating sources are well characterized: RF noise, DAC sampling noise, and pseudopotential "bumps" at junctions [17][18]. Transport and recooling dominate runtime, motivating exchange cooling and parallelism [23][24].

### 3.3 Crosstalk and Anomalous Heating

Temperature-dependent electrode-surface noise ("anomalous heating") is the dominant decoherence source for ion motion near surfaces and scales steeply with reduced ion-electrode distance [25]. Cryogenic operation suppresses it by 2–7 orders of magnitude; surface treatments (ion milling, plasma cleaning) help at room temperature [40][41][42]. Quantinuum's spatially separated gate zones with localized beams produce crosstalk consistent with zero [5]; measurement crosstalk on H2 is ≤3×10⁻⁶ [7]. In micro-Penning traps, record-low electric-field noise (3.4×10⁻¹⁶ V²m⁻²Hz⁻¹) has been measured [13].

### 3.4 Connectivity and Routing

Trapped ions provide all-to-all connectivity within a crystal; QCCD extends this across zones via transport, with logical SWAPs effectively free through qubit relabeling (in software) on H-series systems [7]. Junction-based 2D arrays provide the best all-to-all connectivity of any monolithic architecture [18]. This connectivity is a strategic advantage for QEC: all-to-all systems can run high-rate codes (Skinny Logic, iceberg) that require long-range stabilizer measurements, which planar nearest-neighbor architectures cannot implement without routing overhead [3].

### 3.5 Optical and Control Complexity

Typical trapped-ion systems require 5–10 precision lasers per species; individual addressing uses AOMs, micro-mirrors, or integrated photonics [1][3]. Control electronics are substantial (198 electrodes in H1; 302 in Enchilada; 24 AWG waveform cards in the Georgia Tech exchange-cooling rig) [5][24][26]. The mitigation paths are: (a) grid cowiring (fixed analog count + one digital input per site) [19]; (b) microwave/electronic control (eQC, Sussex blueprint: control fields independent of ion number) [22][30]; (c) integrated photonics with on-chip waveguides, grating couplers, and single-photon detectors [44][45]. The Sussex blueprint projects entire DAC/control stacks wafer-stacked under the trap chip [22].

### 3.6 Summary Comparison

| Criterion | QCCD (linear/racetrack) | Photonic modular | 2D/Penning arrays | Junction arrays | Grid-based QCCD | Matter-link modular |
|---|---|---|---|---|---|---|
| Maturity | **Highest** (commercial) | Medium (lab demos) | Low–Medium | Medium–High | Medium–High | Medium |
| Demonstrated gate fidelity | 99.92–99.99% | 86% teleported CZ; 96.9% remote ent. | Single-ion only (Penning) | 99.9%+ (system) | 99.9%+ (H2/Helios) | 99.9%+ locally |
| Transport/shuttling burden | High (cooling ~68% runtime) | None (photonic) | None (static) | Moderate (junction heating) | Moderate (grid exchange sub-quanta) | High (inter-module shuttling) |
| Connectivity | All-to-all (via transport) | Reconfigurable, arbitrary | All-to-all within crystal | Best all-to-all (per NIST) | All-to-all | All-to-all across modules |
| Control complexity | High (198+ electrodes) | High (photonics + local control) | High (addressing in dense arrays) | Very high (fabrication) | **Reduced** (cowiring) | High (per-module control) |
| Primary scaling limit | Transport/cooling time; control I/O | Link rate & fidelity | Addressing; mode density; maturity | Fabrication yield; power dissipation | Laser/optical access per site | Module alignment; control integration |

---

## 4. Physical and Engineering Limits

### 4.1 Maximum Practical Ions per Trap Region

- **Linear chains (gates):** ~20–50 ions before mode crowding degrades gates [2][3].
- **Linear chains (controlled, no arbitrary gates):** ~100 ions in RF traps; 24-qubit entanglement records at Innsbruck [1][58].
- **2D Penning crystals (simulation):** 100–400 ions, up to ~300 used for spin squeezing/Dicke model studies [1].
- **2D RF crystals:** ~250 ions, set by micromotion resolvability (~4/q²) [15].
- **Micro-Penning arrays and grids:** in principle unbounded by mode crowding per site; MIT Lincoln estimated collision-limited loading of arrays above 10,000 ions [13][14][48].
- **Tsinghua's 2D Wigner crystal:** 512 ions trapped, 300 used as qubits for Ising simulation—the largest trapped-ion quantum simulator to date [57].

### 4.2 Control Electronics and Power

RF power dissipation in surface traps grows steeply with trap length (approximately n³ for ohmic losses plus n for dielectric losses in a fixed-length RF rail), motivating the Enchilada's raised-RF-electrode and perforated-dielectric design, which cut power from 101.6 mW to 38.7 mW and reduced capacitance from 11.9 pF to 3.7 pF [26]. Static-field Penning traps eliminate this scaling class entirely [14]. Control-electronics channel counts (198–302 electrodes today) are addressed by cowiring (75 signals in Enchilada; fixed count in Delaney grids) and by wafer-stacked/ASIC DACs proposed in the Sussex blueprint and pursued by Universal Quantum [22][26][54]. Cryogenic control electronics (DACs operating near 10 K) are identified by Infineon as essential for higher qubit counts [46].

### 4.3 Laser and Optical Systems

Per-ion addressing optics and laser power are the principal non-electronic scaling limits [1]. Integrated photonics routes light through on-chip waveguides and grating couplers, with MIT Lincoln's 2020 demonstration—control of a trapped strontium ion entirely through integrated waveguides, including a fiber block surviving 4 K cooldown—being the landmark [44]. Sandia has integrated single-photon avalanche detectors (SPADs) and waveguides into surface traps, detecting 369 nm ytterbium fluorescence at room temperature [45]. Microwave-based schemes (eQC; Sussex blueprint; Universal Quantum; eleQtron) decouple gate control from optical complexity, requiring global laser fields only for cooling, state prep, and readout [22][30][54].

### 4.4 Parallelism

QCCD systems are limited by the number of gate zones (two in H1) and by serial transport/cooling duty cycles [5][23][24]. The Helios architecture improves this by parallelizing cooling and gating in separate zones (zones are 750 μm apart; up to 16 qubits processed across eight operation zones) [3]. Optical segmentation proposes parallel gates across all cells [20]. Photonic modular architectures support N_ELU/2 parallel remote entanglements via OXC switches [9].

---

## 5. Current State of the Art: Key Players, Milestones, and Roadmaps

### 5.1 Quantinuum (QCCD, Racetrack → Grid)

- **H1 (2020–2022):** First complete QCCD; quantum volume advanced to 2²⁰; first real-time repeated QEC with a color code (2021) [5][7].
- **H2 (2023–2025):** 56 fully connected qubits in a racetrack geometry; QV 2²⁵; >99.99% single-qubit and >99.9% two-qubit fidelity; 100× improvement over Google's 2019 random-circuit-sampling results; first "three 9s" two-qubit fidelity across all pairs in a production device [6][7][8][62].
- **Helios (launched November 2025):** 98 physical qubits (¹³⁷Ba⁺), 99.921% average two-qubit fidelity, 99.9975% single-qubit fidelity, four-way X-junction routing, and **48 fully error-corrected logical qubits from 98 physical qubits at a 2:1 encoding ratio**; expanded to 94 logical qubits in error-detected mode (March 2026); near five-nines logical fidelity demonstrated with a novel QEC code family (Q2 2026) [3][35][50]. Helios draws ~60 kW versus 16–39 MW for leading supercomputers [62].
- **QEC milestones:** 4 logical qubits with 800× error suppression and 14,000 error-free trials (April 2024, with Microsoft) [34][56]; 12 logical qubits with 22× error reduction and five rounds of repeated error correction (September 2024) [33]; 50 entangled logical qubits (December 2024); first magic-state distillation on a commercial system (June 2025) [3][35].
- **Roadmap:** Sol (~192 qubits, 2D grid, 2027) → Apollo (thousands of physical qubits, hundreds of logical qubits, millions of gates, universal FTQC, 2029–2030) → Lumos (utility-scale, 2033) [32][50][51].

### 5.2 IonQ (Laser-Controlled Chains + EQC + Photonic Networking)

- **Systems:** Aria (25 qubits, #AQ 25) [52]; Forte/Forte Enterprise (36 qubits, #AQ 36, rack-mounted) [51]; Tempo (64+ qubits, first barium system, #AQ 64, September 2025) [49][50].
- **Fidelity records:** 99.99% two-qubit gate fidelity (October 2025)—the first crossing of the "four nines" threshold—achieved **without ground-state cooling** using eQC technology from the Oxford Ionics acquisition; single-qubit error levels of 10⁻⁷ demonstrated by Oxford (2025) [23][30][49].
- **Photonic networking:** first interconnection of two commercial trapped-ion systems via photonic entanglement (April 2026, with AFRL); DARPA HARQ selection for quantum-memory work based on Lightsynq diamond technology [55].
- **Roadmap:** 256+ qubits at 99.99% fidelity and 12 logical qubits (2026); 10,000 physical qubits / 800 logical qubits (2027); 20,000 qubits (2028); 200,000 qubits + photonic interconnect (2029); **2 million physical qubits / 80,000 logical qubits (2030)** [31]. Enablers: Oxford Ionics 2D ion-trap technology (up to 300× qubit density), Lightsynq photonic memories (up to 50× entanglement-rate improvement), and the pending $1.8B SkyWater semiconductor foundry acquisition for vertical integration [31][50][51].
- **Cautionary context:** IonQ's earlier SPAC-era roadmap (which predicted ~4,000 qubits by 2026) was missed, and the 2030 targets are widely considered extremely aggressive [31][50].

### 5.3 Oxford Ionics (now IonQ)

World-record fidelities on three axes: 99.97% two-qubit, 99.9992% single-qubit, and 99.9993% SPAM (2024); 32-qubit processor at these levels; QUARTET full-stack system installed at the UK National Quantum Computing Centre (2025); €35M German defense contract; DARPA Quantum Benchmarking Initiative selection (fault tolerance by 2033) [30][50]. Roadmap: Foundation (16–64 qubits) → Enterprise-grade (256+ qubits, >16 logical qubits at 10⁻⁸ error) → Value at Scale (10,000+ qubits via WISE multiplexing) [30].

### 5.4 Universal Quantum (Electric-Field Links + Microwave Control)

Deterministic matter links at 2,424 connections/sec with 99.999993% transfer success (the strongest interconnect demonstration of any modular approach) [21][53]; iQPU modular architecture with proprietary silicon traps, custom ASIC control, and global microwave fields eliminating per-ion lasers; operation at ~70 K; €67M DLR contract to build single-chip and multi-chip (≥100 qubit) machines; million-qubit machine projected to fit in a small meeting room [53][54].

### 5.5 Academic Research Groups

- **NIST:** Origin of QCCD [4]; X-junction transport with <1 quantum excitation [17]; 2D trap-array reordering with 1.1–1.7 quanta [18]; Penning-trap quantum simulation with hundreds of ions [1]; deep characterization of surface electric-field noise mechanisms [25][42].
- **Oxford (Lucas group):** High-rate remote entanglement (94% fidelity, 182 s⁻¹) [29]; distributed quantum computing across an optical link (2025) [11]; record single-qubit gate accuracy (1 error in 6.7 million operations, 2025); fast gates at 99.8% in 1.6 μs; microwave-driven gates in cryogenic traps at 0.5–1% error [28].
- **ETH Zurich (Home group):** Micro-Penning trap with record-low heating and junction-free 2D transport [13][14][43]; long ion chains for QEC; bosonic GKP-style logical encoding [28][43].
- **Duke/Monroe group:** Fastest photonic interconnects (250 Hz, >97% fidelity); three-node GHZ entanglement with detection loophole closed (2026); fault-tolerant Bacon-Shor logical qubit demonstration (2021) [36][61].
- **Innsbruck (Blatt/Monz; AQT):** First trapped-ion quantum repeater over 50 km [12]; fault-tolerant universal gate operations with the Steane code (2022) [36]; 24-qubit entanglement; commercial 12–20 qubit rack-mounted systems (IBEX/PINE/LYNX) and Europe's first ion-trap pilot line (CHAMP-ION) [58].
- **Tsinghua (Duan group):** 512-ion 2D Wigner crystal with 300-ion quantum simulations—the largest trapped-ion simulator to date [57].
- **MIT Lincoln Laboratory:** Cryogenic heating-rate suppression studies [40][41]; fully integrated photonic ion-trap chip (Nature 2020) [44]; scalable loading of 2D arrays (estimated >10,000 sites feasible) [1].
- **Sandia:** Foundry for the field's standard traps (HOA, Phoenix, Peregrine) [59]; Enchilada 200-ion junction trap [26][27]; integrated photonics with SPADs [45].

---

## 6. Practical Implementation Challenges

### 6.1 Cryogenic vs. Room-Temperature Operation

The dominant physics driver for cryogenic operation is **anomalous motional heating** from electric-field noise near electrode surfaces, which scales steeply with reduced ion–electrode distance and can destroy gate fidelity in small traps [25]. The experimental facts:

- MIT Lincoln measured heating-rate suppression of **seven orders of magnitude** when cooling a surface-electrode trap from room temperature to 6 K—two orders of magnitude below all previously published data for comparably sized traps [40].
- Chiaverini & Sage (2014) measured a >100× reduction in heating rates from 295 K to ~4 K in both gold and niobium traps, concluding the anomalous heating process is dominated by **non-material-specific surface contaminants** [41].
- In situ plasma cleaning improved room-temperature heating rates ~4× but showed **no improvement at cryogenic temperatures**, consistent with thermally activated surface contaminants "freezing out" at low temperature [41].
- Ex situ ion milling reduces room-temperature heating ~10× and changes the temperature scaling from power-law to Arrhenius behavior with material-dependent activation temperatures (41 K for gold, 63 K for niobium); notably, milling is **counterproductive for gold traps at cryogenic temperatures** [42].

Industry practice reflects a division: Quantinuum, IonQ (non-EQC), and AQT operate nominally at room temperature and achieve the world's best fidelities, while cryogenic operation is used where it pays off most—micro-fabricated traps with tiny ion–electrode distances (e.g., MIT Lincoln), RF-free Penning traps requiring superconducting magnets (ETH, 6.5 K) [13][43], and integrated-photonics platforms whose fiber blocks survive 4 K [44]. Universal Quantum takes a middle path at ~70 K [54]. Infineon identifies cryogenic control electronics (DACs at ~10 K) as necessary for high qubit counts [46]. Room-temperature systems avoid cryogenic capital and maintenance costs but face higher heating rates, motivating larger ion–electrode distances (which weaken confinement) or surface treatments [41][42]. No single answer fits all architectures; the tradeoff is between heating suppression vs. cryogenic engineering complexity.

### 6.2 Chip Fabrication Constraints

Trapped-ion scaling is increasingly a semiconductor manufacturing problem. Sandia's MESA foundry, with 20+ years of trap fabrication, produced the Enchilada trap with six metal layers, a raised RF electrode, perforated dielectric, and on-chip trench capacitors—302 electrodes cowired to 75 signals to fit a 100-pin package [26][27]. Infineon's production line (including Gen 3 traps with 3D electrodes via anodic wafer bonding) supports Oxford Ionics' eQC chips, eleQtron's MAGIC traps, and ZuriQ's Penning arrays, with the CHAMP-ION EU pilot line establishing "Europe's first advanced ion trap quantum chip manufacturing line" integrating electronics and photonics on a single chip [46][47][48]. IonQ's proposed SkyWater acquisition would make it the only vertically integrated US quantum platform with its own foundry [51]. The strategic framing is explicit in the Quantinuum–Infineon partnership: "QCCD is fundamentally a semiconductor technology," with integrated photonics (waveguides, grating couplers) bringing laser control onto the chip [46]. Key remaining fabrication constraints: yield and uniformity at scale, RF loss in dielectrics (addressed by the Enchilada's oxide removal), on-chip photonics at UV wavelengths (405–370 nm), and cryogenic-compatible packaging [26][44][45][46].

### 6.3 Integration with Quantum Error Correction Codes

Ion traps hold the current world records in QEC efficiency. Quantinuum's Helios runs 48 logical qubits from 98 physical qubits (2:1 ratio) using iceberg-concatenated codes—an order of magnitude better than superconducting systems' ratios [3][35]. Academic demonstrations include: the first fault-tolerant logical qubit with Bacon-Shor encoding on 15 ions at Maryland/Duke (2021), with logical SPAM error (0.6%) below the error of any physical entangling gate [36]; fault-tolerant universal gate operations with the Steane code at Innsbruck [36]; and a single-ion qudit spin-cat code at ETH/MIT that achieved beyond-break-even error correction (coherence improvement factor 1.53(7)) without mid-circuit measurement [39].

Crucially, the QEC-code design space for trapped ions differs from superconducting planar hardware. Ye and Delfosse's ion-chain model ("Chain(n,p,τm)") captures all-to-all gates, sequential unitaries, and slow (~30× ) measurements, yielding surface-code thresholds of ~0.32% per gate and demonstrating that **quantum LDPC codes are well suited to long ion chains**—their [[48,4,7]] BB5 code matches the logical error rate of a distance-7 surface code using 4× fewer physical qubits per logical qubit [37]. IonQ's CliNR partial-error-correction scheme achieves ~3:1 qubit overhead and 2:1 gate overhead, correcting all Clifford gates including native XX/ZZ gates [38]. The all-to-all connectivity of ion traps enables high-rate codes (Skinny Logic, iceberg) that planar architectures cannot implement without routing overhead [3]. The main integration challenge is measurement speed and mid-circuit measurement fidelity, which determine syndrome-extraction latency [37].

### 6.4 High-Fidelity Gate Requirements

Fault tolerance under realistic trapped-ion code models requires two-qubit gate errors below ~0.3–1% (surface-code threshold ~0.32% in the ion-chain model; up to ~1% for some high-threshold codes) [1][37]. The field is far beyond these thresholds at the unit level:

- IonQ: >99.99% two-qubit (without ground-state cooling), 99.9923% reported [23][49].
- Oxford Ionics: 99.97% two-qubit, 99.9992% single-qubit, 99.9993% SPAM [30].
- Quantinuum Helios: 99.921% average two-qubit across all pairs; 99.9975% single-qubit [3].
- Single-qubit records: 99.9999% (up to 1 error in 6.7 million operations at Oxford, 2025) [28][30].

The strategic consequence is overhead reduction: high-fidelity trapped-ion systems achieve ~13:1 physical-to-logical ratios (IonQ/Oxford Ionics estimates) versus 500:1–1,000:1 for typical superconducting estimates [30][31]. Quantinuum's 2:1 ratio with iceberg codes goes even further, though iceberg codes are not fully fault-tolerant [35]. Gate *speed* remains a disadvantage—two-qubit gates take 10–400 μs vs. tens of ns for superconducting—but the QEC overhead advantage (roughly 225× fewer physical qubits per logical qubit) more than compensates in system-level throughput comparisons [3].

### 6.5 Projected Timelines to Fault Tolerance

- **Quantinuum:** Sol (~192 qubits, 2D grid) in 2027; Apollo (thousands of qubits, hundreds of logical qubits, millions of gates) in 2029–2030; Lumos (utility-scale, DARPA QBI target) in 2033 [32][50].
- **IonQ:** 256+ qubits and 12 logical qubits (2026); 10,000 physical / 800 logical qubits (2027); 2 million physical / 80,000 logical qubits (2030) [31]. With ~1,400 logical qubits sufficient to factor RSA-2048 (per Gidney et al. 2025 estimates), IonQ's 2028 goal of ~1,600 logical qubits would, if met, cross the cryptography-relevant threshold [31].
- **Universal Quantum:** ≥100-qubit networked DLR systems within the current contract window; million-qubit machines as the long-term target [54].
- **Industry-wide assessments:** first practical quantum advantage expected around 2027; early fault-tolerant systems 2028–2033; full fault tolerance (10,000+ logical qubits) 2033–2040+; RSA-2048 breaking estimated 2033–2040+ [50]. Microsoft/Quantinuum estimate that ~100 reliable logical qubits suffice for scientific quantum advantage [33]. Monroe's assessment: scaling to 800–8,000 (or even 8 million) qubits "is dominated by engineering" [2].

---

## 7. Comparative Evaluation and Recommendation

### 7.1 Comparative Assessment

| Strategy | Fidelity demonstrated | Scalability ceiling (near-term) | Control complexity | Key risk | Overall promise |
|---|---|---|---|---|---|
| QCCD (linear/racetrack) | 99.9–99.99% | ~100–1,000 qubits [2] | High (electrodes, lasers, transport) | Transport/cooling serialization; control I/O | **Highest maturity; near-certain near-term winner** |
| QCCD + grid cowiring | 99.9%+ | ~1,000+ qubits | Reduced analog I/O [19] | Optical access per site; fabrication yield | **Most promising monolithic path to 1,000+** |
| Junction arrays (2D routing) | 99.9%+ (system) | ~200–2,000 qubits [26] | Very high (fabrication) | Junction heating; yield | Essential enabler for grids |
| Electronic control (eQC/microwave) | 99.97–99.99% | Thousands (projected) | Much reduced (no per-ion lasers) | Fidelity at scale unproven | **Highest-fidelity path; semiconductor-compatible** |
| Photonic modular | 96.9% remote ent.; 86% teleported gate | Thousands–millions (networked) | High (optics, detectors, switches) | Link rate/fidelity; distillation overhead | Complementary; necessary for distributed QC |
| Matter-link modular | 99.999993% link success | Thousands–millions (multi-chip) | High (module alignment, control) | Pre-commercial execution | **Strongest deterministic interconnect** |
| Micro-Penning arrays | Single-ion control | Thousands–millions (quadratic density) | Moderate (magnets, cryo) | Multi-ion gates unproven | Highest long-term architectural ceiling |
| Optical-potential segmentation | Proposal stage | Long chains with parallel gates | High (tweezers, crosstalk compensation) | Unproven at scale | Potential to revive monolithic chains |

### 7.2 Evaluation Against the Research Brief's Criteria

**Technical feasibility** is highest for QCCD and junction-based systems, which have demonstrated every required primitive at or near fault-tolerant quality: 99.9%+ gates, sub-quanta transport, zero-measured crosstalk, and real-time QEC [3][5][18][19]. Photonic modular systems have demonstrated distributed algorithms end-to-end, but the 86% teleported-gate fidelity and ~100 Hz link rate are still ~3 orders of magnitude from fault-tolerant distributed computing requirements [11][2].

**Physical/engineering limits** favor architectures that decouple qubit count from control resources: grid cowiring (fixed analog count per site) [19], electronic control (fixed radiation fields) [22][30], and static-field Penning traps (no RF power scaling) [14]. The RF power scaling of conventional Paul traps (approximately n³) is a real, quantified constraint at the 200+ ion scale, addressed by the Enchilada's raised-RF/perforated-dielectric design [26].

**Current technological advancement** strongly favors Quantinuum's QCCD lineage (commercial, 98 qubits, 48 logical qubits at 2:1, QV 2²⁵, 2029–2030 fault-tolerance roadmap) and IonQ/Oxford Ionics' eQC lineage (highest raw fidelities on any platform, semiconductor fab compatibility, 2026–2027 scaling milestones) [3][23][30][31][32]. Universal Quantum's deterministic matter links are the most impressive modular interconnect results published to date [21]. The micro-Penning platform is the youngest but has already set the heating-rate record and produced the largest 2D array of its kind (9 ions in a 3×3 grid) within 18 months of founding [13][48].

**Practical implementation** challenges—cryogenic vs. room-temperature tradeoffs, fabrication yield, QEC integration, gate fidelity, and timelines—are all tractable with current trajectories. The nearest-term proof points are: IonQ's 256-qubit eQC system (2026) maintaining 99.99% two-qubit fidelity; Quantinuum's Sol 2D grid (2027); Universal Quantum's DLR multi-module machines; and ZuriQ's 40-ion Penning processor [31][32][48][50][54].

### 7.3 Recommendation

The most likely successful path to fault-tolerant, real-world-scale trapped-ion computing is:

1. **QCCD-style modular processors as the foundation**—small ion crystals with shuttling, split/combine, and junction routing—because this is the only architecture that has demonstrated all required primitives at commercial scale (Quantinuum H1→H2→Helios) [5][6][3].
2. **Electronic (microwave/voltage-based) qubit control to eliminate the laser bottleneck**—Oxford Ionics' eQC has the highest demonstrated fidelities and converts trapped-ion hardware from a precision-optics discipline into a semiconductor one [30][23][3].
3. **Grid-based cowiring and 2D junction arrays for the 100–1,000+ qubit intermediate scale**—the Delaney cowiring scheme and Enchilada-class traps make the control-electronics scaling tractable [19][26][32].
4. **Modular interconnects (electric-field matter links first, photonic links for wide-area networking) for the thousand-to-million-qubit scale**—Universal Quantum's deterministic links are orders of magnitude faster and more reliable than current photonic links, while photonic interconnects provide reconfigurability and are the only path to distributed multi-node systems [21][11][55][9].
5. **Micro-Penning arrays as the long-term architectural hedge**—static fields, record-low heating, junction-free 2D transport, and CMOS-compatible fabrication make this the most elegant path to very large 2D arrays, pending multi-ion gate demonstrations [13][14][48].

Adopting a single pure strategy is unnecessary and would be a mistake; the field's leaders are already converging on hybrids. The two trajectories to track most closely are **Quantinuum (Sol in 2027, Apollo in 2029)** and **IonQ (256 qubits in 2026, 10,000 in 2027)**, with Universal Quantum's DLR deliverable and ZuriQ's 40-ion Penning processor as the most informative independent data points [31][32][48][54]. If IonQ's 256-qubit system retains 99.99% two-qubit fidelity and Quantinuum's Sol ships on schedule, fault-tolerant trapped-ion systems at the 100+ logical qubit scale—sufficient for scientific quantum advantage—are plausible by 2029–2030, with full fault tolerance following in the 2030s [31][32][50].

---

## 8. Conclusion

Ion trap quantum computing's scaling problem is not a qubit-quality problem—it is an architecture and engineering problem. The platform already possesses the highest-fidelity qubits, the longest coherence times, the best QEC efficiency, and the most favorable physical-to-logical qubit ratios of any modality. The strategies reviewed here—QCCD shuttling, photonic modular networking, monolithic 2D/Penning arrays, junction-based routing, grid multiplexing, and hybrid electronic-control/matter-link systems—each solve part of the scaling puzzle. The strongest near-term path combines QCCD architectures with electronic qubit control and grid-based multiplexing on semiconductor foundry processes, extended at the thousand-qubit scale by deterministic electric-field module links and, ultimately, photonic networks. The timeline to fault-tolerant utility is measured in years, not decades: 100+ logical qubit systems are targeted for 2029–2030, and the first error-corrected applications are expected around 2027 [31][32][50]. The next two to three years—marked by IonQ's 256-qubit eQC system, Quantinuum's Sol 2D grid, Universal Quantum's DLR machines, and ZuriQ's 40-ion Penning processor—will determine which combinations of these strategies become the foundation of the fault-tolerant era.

---

### Sources

[1] Trapped-Ion Quantum Computing: Progress and Challenges (Bruzewicz, Chiaverini, McConnell & Sage, Applied Physics Reviews 2019): https://ar5iv.labs.arxiv.org/html/1904.04178

[2] Co-designing a scalable quantum computer with trapped atomic ions (Brown, Kim & Monroe, npj Quantum Information 2016): https://www.nature.com/articles/npjqi201634

[3] Quantum Computing Modalities: Trapped-Ion QC (PostQuantum, updated 2026): https://postquantum.com/quantum-modalities/trapped-ion-qubits

[4] Architecture for a large-scale ion-trap quantum computer (Kielpinski, Monroe & Wineland, Nature 2002): https://www.nist.gov/document/wineland-nature-417pdf

[5] Demonstration of the trapped-ion quantum CCD computer architecture (Pino et al., Nature 2021): https://ar5iv.labs.arxiv.org/html/2003.01293

[6] A Race Track Trapped-Ion Quantum Processor (Moses et al., Phys. Rev. X 2023): https://arxiv.org/abs/2305.03828

[7] Quantinuum H2 Trapped-Ion Quantum Processor (EmergentMind): https://www.emergentmind.com/topics/quantinuum-h2-trapped-ion-device

[8] Quantinuum System Model H2 product page: https://www.quantinuum.com/products-solutions/quantinuum-systems/system-model-h2

[9] Fault tolerant scalable modular quantum computer architecture (Monroe, Kim & Raussendorf, US Patent US9858531B1): https://patents.google.com/patent/US9858531B1/en

[10] Modular entanglement of atomic qubits using photons and phonons (Hucul et al., Nature Physics 2015): https://www.nature.com/articles/nphys3150

[11] Distributed quantum computing across an optical network link (Main et al., Nature 2025): https://www.nature.com/articles/s41586-024-08404-x

[12] Quantum Repeater Goes the Distance (Hajdušek, APS Physics 2023, on Krutyanskiy et al., PRL 130, 213601): https://link.aps.org/doi/10.1103/Physics.16.84

[13] Penning micro-trap for quantum computing (Jain et al., Nature 2024): https://www.nature.com/articles/s41586-024-07111-x

[14] Scalable Arrays of Micro-Penning Traps for Quantum Computing and Simulation (Jain, Alonso, Grau & Home, Phys. Rev. X 2020): https://link.aps.org/doi/10.1103/PhysRevX.10.031027

[15] Two-dimensional ion crystals in radio-frequency traps for quantum simulation (Richerme, Phys. Rev. A 2016): https://iontrap.physics.indiana.edu/papers/richerme2016.pdf

[16] T-junction ion trap array for two-dimensional ion shuttling, storage, and manipulation (Hensinger et al., Applied Physics Letters 2006): https://iontrap.duke.edu/files/2025/03/034101_1_online.pdf

[17] High-fidelity transport of trapped-ion qubits through an X-junction trap array (Blakestad et al., PRL 2009): https://www.semanticscholar.org/paper/High-fidelity-transport-of-trapped-ion-qubits-an-Blakestad-Vandevender/cad81d43ceebc9f865ae69baa5eba4da55ee0e04

[18] Ion Transport and Reordering in a 2D Trap Array (NIST, Advanced Quantum Technologies 2020): https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=929736

[19] Scalable Multispecies Ion Transport in a Grid-Based Surface-Electrode Trap (Delaney et al., Phys. Rev. X 2024): https://link.aps.org/doi/10.1103/PhysRevX.14.041028

[20] Scalable Architecture for Trapped-Ion Quantum Computing Using rf Traps and Dynamic Optical Potentials (Schwerdt et al., Phys. Rev. X 2024): https://link.aps.org/doi/10.1103/PhysRevX.14.041017

[21] A high-fidelity quantum matter-link between ion-trap microchip modules (Akhtar et al., Nature Communications 2023): https://www.nature.com/articles/s41467-022-35285-3

[22] Blueprint for a microwave trapped ion quantum computer (Lekitsch et al., Science Advances 2017): https://pmc.ncbi.nlm.nih.gov/articles/PMC5287699

[23] Accelerating Towards Fault Tolerance: Unlocking 99.99% Two-Qubit Gate Fidelities (IonQ/Oxford Ionics, 2025): https://www.ionq.com/blog/accelerating-towards-fault-tolerance-unlocking-99-99-two-qubit-gate

[24] Rapid exchange cooling with trapped ions (Fallek et al., Nature Communications 2024): https://pmc.ncbi.nlm.nih.gov/articles/PMC11258264

[25] Ion-trap measurements of electric-field noise near surfaces (Brownnutt et al., Reviews of Modern Physics 2015): https://link.aps.org/doi/10.1103/RevModPhys.87.1419

[26] Multi-junction surface ion trap for quantum computing — "Enchilada" trap (Sandia, arXiv:2403.00208): https://arxiv.org/html/2403.00208v1

[27] Bigger and better quantum computers possible with new ion trap, dubbed the Enchilada (Sandia National Laboratories news release): https://newsreleases.sandia.gov/enchilada_trap

[28] Doctoral Theses — Oxford Ion Trap Quantum Computing Group: https://www.physics.ox.ac.uk/research/group/ion-trap-quantum-computing/publications/doctoral-theses

[29] High-Rate, High-Fidelity Entanglement of Qubits Across an Elementary Quantum Network (Stephenson et al., PRL 2020): https://arxiv.org/abs/1911.10841

[30] Oxford Ionics company profile (PostQuantum): https://postquantum.com/quantum-computing-companies/oxford-ionics

[31] IonQ Roadmap: https://www.ionq.com/roadmap

[32] Quantinuum Unveils Accelerated Roadmap to Achieve Universal Fault-Tolerant Quantum Computing by 2030 (Quantinuum press release, Sept 2024): https://www.quantinuum.com/press-releases/quantinuum-unveils-accelerated-roadmap-to-achieve-universal-fault-tolerant-quantum-computing-by-2030

[33] Microsoft and Quantinuum create 12 logical qubits (Microsoft Azure Quantum Blog, Sept 2024): https://azure.microsoft.com/en-us/blog/quantum/2024/09/10/microsoft-and-quantinuum-create-12-logical-qubits-and-demonstrate-a-hybrid-end-to-end-chemistry-simulation

[34] Microsoft Announces Record Breaking Logical Qubit Results (PostQuantum, April 2024): https://postquantum.com/industry-news/logical-qubit-microsoft

[35] Quantinuum Researchers Demonstrate Quantum Computations With Dozens of Protected Logical Qubits (The Quantum Insider, 2026): https://thequantuminsider.com/2026/03/10/quantinuum-researchers-demonstrates-quantum-computations-with-dozens-of-protected-logical-qubits

[36] Fault-Tolerant Operation of a Quantum Error-Correction Code (Egan et al., Nature 2021; Duke announcement): https://iontrap.duke.edu/2021/10/19/fault-tolerant-operation-of-a-quantum-error-correction-code

[37] Quantum error correction for long chains of trapped ions (Ye & Delfosse, Quantum 2025): https://quantum-journal.org/papers/q-2025-11-27-1920

[38] IonQ's Novel, Efficient Approach to Quantum Error Correction (CliNR, 2024): https://www.ionq.com/blog/our-novel-efficient-approach-to-quantum-error-correction

[39] Error correction of a logical qubit encoded in a single atomic ion (arXiv:2503.13908): https://arxiv.org/html/2503.13908v1

[40] Suppression of heating rates in cryogenic surface-electrode ion traps (Labaziewicz et al., PRL 2008): https://pubmed.ncbi.nlm.nih.gov/18232755

[41] Reduction of trapped-ion anomalous heating by in situ surface plasma cleaning (McConnell et al., PRA 2015; MIT Lincoln Laboratory): https://www.ll.mit.edu/r-d/publications/reduction-trapped-ion-anomalous-heating-situ-surface-plasma-cleaning

[42] Evidence for multiple mechanisms underlying surface electric-field noise in ion traps (NIST, PRA 2018): https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=926567

[43] A new ion trap for larger quantum computers (ETH Zurich news, 2024): https://ethz.ch/en/news-and-events/eth-news/news/2024/03/a-new-ion-trap-for-larger-quantum-computers.html

[44] MIT Lincoln Laboratory Creates The First Trapped-Ion Quantum Chip With Fully Integrated Photonics (Forbes, 2020): https://www.forbes.com/sites/moorinsights/2020/10/26/mit-lincoln-laboratory-creates-the-first-trapped-ion-quantum-chip-with-fully-integrated-photonics

[45] Trapped Ion Clock with photonic Technologies On Chip (TICTOC, Sandia National Laboratories): https://www.sandia.gov/quantum/quantum-information-sciences/projects/tictoc

[46] Trapped ion quantum computing (Infineon Technologies): https://www.infineon.com/technology/trapped-ions

[47] Quantum chips: Infineon contributes industrialization (Infineon press release, April 2026; CHAMP-ION pilot line): https://www.infineon.com/press-release/2026/infpss202604-080

[48] ZuriQ Secures $25.5M Seed Round and Advances 2D Trapped-Ion Fabrication with Infineon (Quantum Computing Report, July 2026): https://quantumcomputingreport.com/zuriq-secures-25-5m-seed-round-and-advances-2d-trapped-ion-fabrication-with-infineon

[49] Top Trapped Ion Quantum Computing Companies: Complete 2026 Guide (Quantum Zeitgeist): https://quantumzeitgeist.com/top-trapped-ion-quantum-computing-companies

[50] Quantum Computing Roadmap 2026: IonQ, IBM, Google... (Quantum Market Cap): https://quantummarketcap.com/roadmap

[51] IonQ Forte Enterprise product page: https://www.ionq.com/quantum-systems/forte-enterprise

[52] IonQ Aria product page: https://www.ionq.com/quantum-systems/aria

[53] Record-breaking discovery solves major quantum puzzle — by fitting computers together 'like a jigsaw' (Universal Quantum, 2023): https://universalquantum.com/knowledge-hub/record-breaking-discovery-solves-major-quantum-puzzle

[54] Engineering Notes from the Quantum Frontier — Vol. 1: Rethinking Scale (Universal Quantum, 2025): https://universalquantum.com/knowledge-hub/engineering-notes-from-the-quantum-frontier-vol-1

[55] IonQ Achieves Key Photonic Interconnect Milestone Demonstrating Networked Quantum Systems (IonQ press release, 2026): https://www.ionq.com/news/ionq-achieves-key-photonic-interconnect-milestone-demonstrating-networked-quantum-systems

[56] Quantinuum Partners with Microsoft in New Phase of Quantum Computing (Quantinuum press release, April 2024): https://www.quantinuum.com/press-releases/quantinuum-and-microsoft-announce-new-era-in-quantum-computing-with-breakthrough-demonstration-of-reliable-qubits

[57] A Site-Resolved 2D Quantum Simulator with Hundreds of Trapped Ions (Guo et al., Tsinghua; Nature 2024 / arXiv:2311.17163): https://arxiv.org/abs/2311.17163

[58] AQT press releases (Alpine Quantum Technologies): https://www.aqt.eu/press

[59] High Optical Access Trap 2.0 (Sandia National Laboratories): https://www.sandia.gov/research/publications/details/high-optical-access-trap-2-0-2016-01-26

[60] Cryogenic Ion Trap Package (Infleqtion): https://infleqtion.com/quantum-cores/cryogenic-ion-trap-package

[61] Fast and Hi-Fi Photonic Interconnections between Pristine Quantum Memories (Duke/Monroe group, 2025): https://iontrap.duke.edu/2025/03/22/fast-and-hi-fi-photonic-interconnections-of-pristine-quantum-memories

[62] Quantinuum Launches Industry-First, Trapped-Ion 56-Qubit Quantum Computer (Quantinuum press release, June 2024): https://www.prnewswire.com/news-releases/quantinuum-launches-industry-first-trapped-ion-56-qubit-quantum-computer-breaking-key-benchmark-record-302164906.html
