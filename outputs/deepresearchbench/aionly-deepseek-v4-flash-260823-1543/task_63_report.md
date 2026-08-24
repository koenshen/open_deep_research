# Mitigating Plasma-Etch-Induced Damage in Lithium Niobate Photonic Devices

## 1. Introduction: Nature and Sources of Plasma-Etch Damage in Lithium Niobate

Lithium niobate (LN, LiNbO₃) is a trigonal ferroelectric crystal (3m point group, R3c space group) with a transparency window spanning ~350 nm to 5.5 µm, a large Pockels coefficient (r₃₃ ≈ 30.8–31 pm/V), and second-order nonlinear coefficients d₃₃ = 25.2 pm/V and d₃₁ = 4.6 pm/V at 1064 nm [1][2]. Its combination of electro-optic, nonlinear, and acoustic properties has made thin-film LN (TFLN) the platform of choice for next-generation integrated photonics. However, plasma etching — the standard method for pattern transfer — introduces multiple damage mechanisms that degrade device performance:

- **Surface and sidewall roughness** — the dominant scattering-loss mechanism, typically produced by mask line-edge roughness transfer, redeposition of etch products, and micro-masking effects [3][4].
- **Stoichiometric changes and defect formation** — fluorine-based plasmas create non-volatile LiF (melting point >800°C) that redeposits on sidewalls, while the preferential removal of Li and O can leave Li-deficient, Nb-rich surfaces [5][6]. Electron-beam lithography itself (particularly at >100 keV) has also been shown to introduce lattice damage via radiolysis, knock-on displacement, and electrostatic charging [7].
- **Lattice/amorphization damage** — ion bombardment (plasma ions, FIB Ga⁺, ion implantation) creates amorphous layers and point-defect complexes. FIB damage layers scale roughly linearly with beam energy: ~23 nm at 30 kV, ~6.5 nm at 5 kV, ~1.6 nm at 1 kV argon [8].
- **Redeposition/fencing** — sputtered LN and mask material redeposits on sidewalls, forming "fences" and micro-masking that increases roughness and reduces sidewall verticality [3][9].
- **Reduced nonlinearity/electro-optic performance** — lattice damage, Li out-diffusion, and residual stress degrade the material's nonlinear susceptibility and increase absorption; photorefractive defects (Nb antisites, Li vacancies) are also aggravated by etch-induced disorder [10][11].

The following sections synthesize published, quantitative evidence on mitigation strategies, organized into (a) ex-situ treatments, (b) in-situ process optimization, (c) alternative etch routes, and (d) device-level demonstrations of recovered performance.

---

## 2. Ex-Situ Treatments for Damage Repair

### 2.1 Post-Etch Thermal Annealing

Thermal annealing is the single most effective and most widely reported ex-situ repair step for plasma-etch and ion-implantation damage in LN. The key variables are temperature, ambient (O₂, air, Ar, vacuum, or Li-rich/VTE), heating rate, and duration.

**Oxygen annealing at 520°C — the state-of-the-art reference process.** The Harvard group's record-setting 29.32-million intrinsic-Q TFLN microresonators (Photonics Research, 2024) explicitly attribute part of their success to a post-etch treatment sequence of **chemical cleaning (hot KOH, hot SC-1, diluted HF, piranha) followed by annealing at 520°C in oxygen** after a two-run optimized argon ICP-RIE etch. This produced an ultra-low propagation loss of **1.3 dB/m** — a ~2.4× improvement over the previous dry-etched TFLN record of 12 million Q [12][13]. The same 520°C/2 h O₂ annealing recipe was used in a wafer-scale LNOI fabrication study from Friedrich Schiller University Jena/Fraunhofer IOF, which combined O₂ annealing with PECVD SiO₂ cladding and achieved loaded Q of (1.34 ± 0.24) × 10⁶ and straight-waveguide propagation loss of ~2 dB/m (0.02 dB/cm) [14].

**High-temperature annealing after chemo-mechanical etching (PLACE).** Li et al. (Optics Express, 2023) fabricated ultra-high-Q LN microrings via photolithography-assisted chemo-mechanical etching (PLACE) and performed **high-temperature annealing at 450°C for 2 h in air** to restore lattice damage caused by ion implantation during the ion-slicing step. This improved loaded Q factors by **4–5×**, yielding a loaded Q of 4.29 × 10⁶ and an intrinsic Q of 4.04 × 10⁷ — corresponding to a propagation loss below **1 dB/m (0.0091 dB/cm)** [15]. The improvement was attributed to repair of implantation-induced lattice damage rather than roughness reduction, since the CMP-based process already produced ultra-smooth surfaces.

**Slow-heating annealing to repair EBL damage.** Shi et al. (Optical Materials, 2024) designed a slow-heating post-process annealing method specifically to repair damage from high-energy electron-beam lithography (EBL), which had been identified as a hidden contributor to material absorption loss in TFLN. The treatment reduced waveguide loss by approximately **50%** and roughly **doubled the intrinsic Q-factor** of micro-ring resonators, reaching Q_int = 3.93 × 10⁶ (≈0.1 dB/cm) in X-cut TFLN devices. The authors note that congruent LN (Li content ~48.6%) contains intrinsic lattice defects that make it particularly sensitive to fabrication-induced damage [7].

**Rapid thermal annealing (RTA) for lattice recrystallization.** For deep lattice damage (e.g., from ion implantation or high-energy ion bombardment), RTA is dramatically more effective than slow furnace annealing. Fleuster et al. (Applied Physics Letters, 1994) showed that **RTA of Er-implanted LiNbO₃ at 1060°C for just 1 minute in dry O₂** (heating rate ~100°C/s) produces **perfect epitaxial recrystallization**, with RBS/channeling minimum yield of (2.3 ± 0.2)% — identical to virgin crystal. In contrast, slow heating (~10°C/s) required 8-hour anneals and left columnar grain boundaries [16]. For TFLN ion-sliced films, annealing ~6 h at ≥400°C restores material properties slightly altered from bulk [17]. The US6540827B1 patent on crystal ion-slicing also discloses RTA (e.g., 40 s at 700°C in forming gas) to repair residual lattice damage and reduce surface roughening [17].

**Ambient effects.** Oxygen ambients are preferred when Li₂O out-diffusion and reduction must be countered; O₂ annealing at 520–600°C is the most common recipe in the TFLN literature [12][14]. Historically, Ti-in-diffused waveguides are fabricated in dry O₂ at >1000°C for >10 h to achieve <1 dB/cm loss [18]. For deeper stoichiometry repair, **vapor transport equilibration (VTE)** in Li-rich atmospheres can restore Li₂O content: VTE of congruent LN follows Arrhenius behavior with activation energy 0.76 ± 0.05 eV (X-cut) and 0.53 ± 0.03 eV (Z-cut) for surface Li₂O-content alteration [19]. VTE-converted near-stoichiometric LiTaO₃ (a close analog) exhibited 100-fold reduced saturated space-charge fields and ~100× higher photorefraction-limited useful lengths [20]. An early patent (WO2002075444A1) demonstrates the broader principle: amorphous LN films deposited by CVD can be crystallized into single-crystal epitaxial quality by annealing at 900–1100°C for 0.5–6 h in a Li-rich environment [21].

**Reported quantitative annealing outcomes:**

| Treatment | Reported effect | Source |
|---|---|---|
| 520°C O₂ + chemical cleaning | Q_int = 29.32 × 10⁶; loss 1.3 dB/m | Harvard, Photonics Research 2024 [12] |
| 520°C O₂ 2 h + SiO₂ cladding | Loaded Q = 1.34 × 10⁶; loss ~2 dB/m | Jena/Fraunhofer, arXiv 2024 [14] |
| 450°C air 2 h | Q_int = 4.04 × 10⁷; loss <1 dB/m | PLACE, Opt. Express 2023 [15] |
| Slow-heating post-etch anneal | Loss −50%; Q_int up to 3.93 × 10⁶ | Shi, Opt. Mater. 2024 [7] |
| RTA 1060°C 1 min dry O₂ | Perfect recrystallization (χ_min = 2.3%) | Fleuster, APL 1994 [16] |
| 500°C air 2 h | Q improved 5.2 × 10⁴ → 1.6 × 10⁵ | Lin, Sci. Rep. 2015 [22] |

### 2.2 Wet Chemical Cleaning and Etching

Wet chemistries serve three distinct roles: (1) removing redeposited etch byproducts (LiF, sputtered mask material, polymer residues), (2) etching away the damaged surface layer itself, and (3) smoothing rough sidewalls.

**Redeposition removal — RCA-1a/SC-1.** The most detailed quantitative study comes from the NIST group (AIP Advances, 2024), which optimized LNOI waveguide fabrication with Ar-based ICP-RIE. They found that **RCA-1a solution (NH₄OH:H₂O₂:H₂O = 2:2:1) heated to 85°C was superior to piranha and RCA-1b** for removing redeposited material. The optimized clean was **15 minutes each at 0° and 90° boat orientations (30 min total)**. Prolonged cleaning (beyond 30 min) caused chipping and peeling of waveguides; a 24-h clean attacked the LN itself (film thickness reduced from 700 nm to ~630 nm and sidewall angles became asymmetric). Properly cleaned samples had equal sidewall angles of ~70° [3]. The same SC-1-type clean (NH₄OH:H₂O₂:H₂O = 1:1:5, 5 min at 80°C) is used to remove LiF byproducts after SF₆/Ar ICP-RIE in FIB+ICP metasurface fabrication [23]. Hu, Ricken, and Sohler (ECIO 2008) used an iterative process of C4F8/He ICP etching followed by 1-min SC-1 cleans (70% H₂O, 20% H₂O₂, 10% NH₄OH) to remove LiF deposition between etch cycles, enabling 5.8-µm-high ridges with nearly vertical walls [24].

**Acid treatments — HF, HF/HNO₃.** Dilute HF is a standard component of the Harvard cleaning sequence (hot KOH → hot SC-1 → diluted HF → piranha) before the 520°C O₂ anneal [12]. In the crystal ion-slicing process, 5% HF at room temperature selectively etches the ion-damaged sacrificial layer with selectivity exceeding 10³ relative to the pristine top surface [17]. For deep wet etching of bulk LN, a 1:2 HF:HNO₃ mixture at 90°C achieves ~50 µm/h on the −Z face but only ~250 nm/h on the +Z face — a dramatic crystallographic anisotropy that can be exploited but also complicates etching of arbitrary orientations [25]. More recently, Yu et al. (Optics Letters, 2024) demonstrated **poling-assisted HF wet etching** of Z-cut TFLN: high-fidelity ferroelectric domain poling defines the pattern, and HF selectively etches the −Z domains to reveal microdisk resonators — entirely avoiding plasma damage [26].

**Base solutions — KOH, NaOH, TMAH.** Hot KOH is part of the Harvard record-Q cleaning sequence [12]. The most comprehensive study of base-assisted etching for LN nanodevices (Shen et al., Nanomaterials, 2023) examined ten X-cut Mg-doped LNO samples with different masks and process combinations. Key results include:
- **Sample 4** (SiO₂ mask, high-temperature reduction at 400°C in 10% H₂+Ar, then SC-1 wet etch): ~49 nm depth with asymmetric sidewalls (44° in +Z, 85° in −Z).
- **Sample 7** (Cr mask, RIE + Al film + annealing + wet etch): ~115 nm depth with **perfect 90° sidewall angles**, described as damage-free and preserving ferroelectric properties — the optimized hybrid dry+wet process [6].

KOH-based CMP slurries can also produce sub-nanometer surfaces: a Dalian University of Technology patent reports a pH 10.2–10.6 slurry (ceria/silica + KOH + H₂O₂) achieving material removal rate 420–460 nm/min and surface roughness Ra = 0.35–0.5 nm [27].

**Sidewall smoothing via atomic layer etching (ALE).** A major advance is the demonstration that **plasma-based atomic layer etching can smooth already-etched LN surfaces**. Caltech/Oxford Instruments/JPL reported a directional ALE process using sequential HBr/BCl₃/Ar and Ar plasma exposures: **50 cycles reduced surface roughness of a TFLN waveguide from Rq = 2.07 nm to Rq = 0.34 nm (an 84% reduction)** with minimal lateral etching, and 120 cycles at 200°C produced no roughening (Rq = 0.28 nm) [28]. An earlier isotropic ALE process (H₂ and SF₆/Ar half-cycles) reduced sidewall roughness of Ar⁺-milled TFLN waveguides by 30% (Rq from 0.82 ± 0.25 to 0.55 ± 0.13 nm) after 50 cycles without any wet processing [29]. These results establish ALE as a powerful post-etch smoothing/passivation step that also removes the damaged surface monolayer by monolayer.

**Proton-exchange-enhanced wet etching.** Li et al. (Optical Materials, 2021) showed that proton exchange (PE) in pure benzoic acid improves the LN wet-etch rate by nearly **100×** (optimized 13.5 nm/min), enabling ridge waveguides in TFLN with propagation loss of 4.3 dB/cm at 850 nm. The sidewalls were protected with beeswax during wet etching [30]. This route is relevant for repairing/avoiding plasma damage because it replaces plasma pattern transfer entirely, though PE itself degrades ferroelectric properties and typically requires reverse proton exchange to restore them [5][6].

### 2.3 Surface Passivation and Cladding

Cladding layers serve two damage-mitigation functions: (1) they fill and optically "hide" residual sidewall roughness by index matching, and (2) they protect the etched surface from further oxidation/contamination and provide mechanical stability.

**Index-matched SiN/SiON coating.** A Chinese patent (CN115951449A) specifically addresses plasma-etch damage by depositing a **coating layer with refractive index equal to that of the LN waveguide (2.15–2.25, preferably 2.2)** — using silicon nitride or silicon oxynitride — to fill and repair surface/sidewall undulations without damaging the LN lattice. The coating thickness is 10–100 nm (kept below 10% influence on optical field energy), followed by **thermal annealing at 300–800°C for 5–10 min** and a 1–5 µm SiO₂ upper cladding. COMSOL simulations confirmed that the SiN cladding substantially reduces sidewall scattering loss without significantly affecting transmission [31].

**SiO₂ cladding.** The Jena wafer-scale process uses PECVD SiO₂ cladding after O₂ annealing at 520°C, with measured racetrack resonator losses of ~5 dB/m (TE) and straight-waveguide loss ~2 dB/m [14]. The refractive index contrast between LN (n ≈ 2.1) and SiO₂ (n ≈ 1.4) is ~0.7, providing strong confinement while the cladding smooths the effective index profile seen by the mode [2].

**ALD Al₂O₃/HfO₂.** While not yet demonstrated specifically as an LN etch-damage passivation layer, ALD-grown HfO₂/Al₂O₃ films have been characterized for high laser-induced damage thresholds (LIDT), with inorganic precursors (HfCl₄, AlCl₃) yielding LIDTs of 22 J/cm² and 14 J/cm² respectively — relevant for nonlinear devices where surface quality and damage resistance are coupled [32]. ALD's conformal coverage makes it a natural candidate for sidewall passivation of etched LN structures.

---

## 3. In-Situ Process Optimization

### 3.1 Plasma Gas Chemistry

**Fluorine-based chemistries (SF₆, CHF₃, CF₄, C4F8).** F-based plasmas are the workhorse for LN etching but suffer from the well-documented LiF redeposition problem: LiF has a melting point above 800°C, so it does not volatilize at typical process temperatures, accumulating on sidewalls, lowering etch rates, and producing non-vertical profiles with sidewall angles limited to 60–75° [5][33][34]. Hu et al. (JVST A, 2006) systematically characterized this behavior:
- CF₄ at 500 mTorr: PE-LN etch rate 480 nm/h (pure LN only 157 nm/h), with surface cracks.
- SF₆ at 500 mTorr: PE-LN 1.53 µm/h, selectivity 46:1, but highly isotropic with severe undercut.
- **CHF₃/Ar ICP-RIE at 6 mTorr, 130 V dc bias, without He-backside cooling: 5.76 µm/h, selectivity 32:1, nearly vertical 82° walls with negligible undercut** — the optimal F-based recipe [5].

The dramatic rate increase without backside cooling is explained by the volatility of NbF₅ (boiling point ~234°C), which requires elevated substrate temperature to desorb [5]. This temperature effect was confirmed and quantified by Osipov et al. (Materials Research Express, 2019), who found a three-regime dependence of SF₆ ICP etch rate on substrate temperature: modest increase from 373–423 K, near-linear growth to 711 nm/min at 523 K, then saturation/roll-off above 523 K due to non-volatile LiF formation. **SF₆/O₂ mixtures significantly outperformed SF₆/Ar at 598 K: 812 nm/min versus 337 nm/min, with RMS roughness 30.5 nm versus 119.4 nm** [35]. In deep etching (>80 µm), an optimal process with ≈110° wall inclination, ~20:1 Cr selectivity, and ~300 nm/min rate was developed using SF₆/O₂ with periodic HF treatments to remove LiF [36].

The Sumitomo Osaka Cement work on ECR plasma (CHF₃ and CF₄) for 40 Gb/s LN modulators found that CF₄ caused notch lines growing along ridge waveguide feet (catastrophic breakage) plus F and C contamination that weakened SiO₂ buffer adhesion; **switching from CF₄ to CHF₃ eliminated the notches**, and residual F/C contamination was removed by either dilute HNO₃ wet etching or **O₂ annealing at 600°C for 1 h** [37].

**Chlorine-based chemistries (Cl₂, BCl₃, Cl₂/H₂/Ar).** Cl-based plasmas form LiCl, which is easily removed (volatile), avoiding the LiF problem, but generally produce lower etch rates. Huang et al. (J. Micromech. Microeng., 2026) optimized a Cl₂/H₂/Ar ICP recipe: **ICP 600 W, RF bias 120 W, pressure 10 mTorr, Cl₂/H₂/Ar = 10/20/50 sccm**, achieving a steep sidewall angle of 79.1°, etch rate ~32 nm/min, and 1.43:1 selectivity to SiO₂. Their five-step model highlights the synergy of chemical chlorination, hydrogen-assisted oxygen removal, and argon-ion anisotropic sputtering [38]. Earlier work by Bahadori et al. achieved 83° sidewalls with Ar/Cl₂/BCl₃ (1.45:1 selectivity) [6][38].

**Argon-based (physical) etching.** Ar-only sputtering avoids LiF formation entirely and has produced the best optical-quality devices in the literature. Ulliac et al. (Optical Materials, 2016) used Ar plasma at 2 mTorr with an S1828 photoresist mask and achieved single-mode waveguides with **5 dB/cm overall loss** at 1550 nm — better than previous Ar-etched photonic wires (7.5–9.9 dB/cm) [39]. The ETH Zurich group (Kaufmann et al., Nanophotonics, 2023) established that Ar ICP etching is "the most established process for high-quality photonic integrated circuits" in LN, with reported propagation losses as low as 2.7 dB/m in multimode structures; they developed a redeposition-free regime by balancing DC bias and pressure, achieving Q-factor variation below 2% across four samples and calculated propagation loss of **1.55 dB/cm** in 600-nm-wide racetrack resonators [9]. The Harvard record-Q devices also use Ar ICP-RIE (~0.6 nm/s etch rate, split into two runs) [12]. The main Ar-etch drawbacks are near-unity mask selectivity (so masks must be thick) and redeposition of sputtered LN, which can be managed via bias/pressure optimization (see §3.2) [9][3].

**H₂-plasma pre-treatment (proton substitution).** Aryal et al. (Nanomaterials, 2022) developed a novel **H₂-plasma treatment (30 sccm H₂, 15 mTorr, RF 150 W, ICP 300 W, DC bias 53 V)** applied before lithography/metallization. It substitutes protons for Li ions at the surface — a dry, cleanroom-compatible analog of wet proton exchange — which relieves surface tension and dramatically improves Ti/Al/Cr mask adhesion on X- and Y-cut LN. Using CHF₃/Ar etching with periodic cooling/cleaning cycles, they achieved etch depths up to **3.4 µm with smooth sidewalls and near-perfect verticality (~3° offset)** across multiple crystallographic orientations [40].

### 3.2 Bias Power, Pressure, and Temperature Windows

The most systematic parametric data come from the ETH Zurich study (Kaufmann et al., 2023), which swept DC bias, pressure, etch depth, and aspect ratio for Ar ICP etching:

- **DC bias sweep (100–800 V, 1 mTorr, 20°C):** total redeposition decreased almost **fourfold** from 100 V to 800 V, trending toward redeposition-free above ~1 kV. Trench depth increased 5× with bias. Sidewall angle remained 60–63° on both +Z and −Z faces. **Surface roughness (Sq) was ~0.08 nm for biases above 200 V — four times better than the un-etched surface (0.31 nm)**, demonstrating the "polishing character" of the Ar process. Sample bow was minimized at 300 V (20 nm over 8×8 mm²) and 600 V (<5 nm).
- **Pressure sweep:** redeposition vanished completely above ~7 mTorr at 600 V (and ~11 mTorr at 400 V), but with significant structural damage. The **redeposition-free window is 5–7 mTorr at 600 V**; etch rates dropped to minima (27 nm/min at 400 V; 12 nm/min at 600 V) in this window. Surface roughness degraded with pressure (Sq = 0.10, 0.12, 0.15 nm at 3, 5, 7 mTorr).
- **Etch rate scaling:** 0.09 nm/min per watt of ICP power and 0.10 nm/min per volt of DC bias — enabling precise process transfer.
- **Aspect-ratio effects:** redeposition decreases with decreasing gap size (1 µm → 100 nm) because ions bouncing between sidewalls aid removal; dense structures are redeposition-free down to 1 µm gaps [9].

The NIST study independently confirmed the bias window for Ar ICP-RIE: **RF power 100–200 W is optimal** (at ICP 1500 W, 5 mTorr, 5°C). At 50 W, sidewalls are fully enveloped by redeposit; at 300 W, redeposit is eliminated, but above 300 W, line-edge roughness transfers to the waveguide causing striations and damage [3].

Kozlov et al. (Applied Sciences, 2023) provided a mechanistic explanation for the bias dependence in SF₆/Ar RIE of X-cut LN. At bias 186 V (0.03 mbar, Ar⁺ energy ~90 eV), surfaces were smooth with microtrenches at the waveguide base; at bias 141 V (0.007 mbar, Ar⁺ ~30 eV), surfaces were rough with a brown LiFₓ layer. They proposed that **ion energies near 90 eV create vacancies in the LiF layer, enhancing diffusion of reaction products and surface sputtering**, while below a 30–90 eV transition, chemical etching dominates, leaving LiF that blocks product out-diffusion and causes swelling and roughness [33]. This transition point explains why "soft landing" final steps must still maintain sufficient ion energy to clear LiF.

**Temperature effects** are equally critical. Hu et al. doubled the CHF₃/Ar etch rate (2.88 → 5.76 µm/h) simply by removing He backside cooling, exploiting NbF₅ volatility [5]. Osipov's data (above) show that modest substrate heating (250°C) can increase SF₆/O₂ etch rates from ~127–282 nm/min to **711–812 nm/min** [35][36]. Conversely, for Ar-based processes, the NIST group etched at 5°C in 1-minute segments with 5-minute cooldown periods to prevent thermal damage, and Aryal et al. used 20-min etch/4-min cool cycles with hourly chemical cleaning to manage the low thermal conductivity of LN [3][40].

### 3.3 Etch Mask Selection

Mask choice directly determines sidewall roughness, profile, and redeposition behavior:

- **Chromium (Cr) masks** are the most common hard mask. They provide high selectivity (up to 48:1 with CHF₃/Ar on PE-LN [5]) and resistance to high bias power, but the polycrystalline grain size (~55 nm) transfers granular features to sidewalls, and the mask line-edge roughness (20–30 nm for sputtered Cr) is inherited by the etched structure [3][33]. The NIST study selected Cr over SiO₂ and soft resist after showing that soft (resist) masks produce persistent striated sidewall defects, while SiO₂ masks produce striations and base "trenching" from charge buildup [3].
- **Nickel (Ni) masks** outperform Cr in both RIE and ICP: Ni-mask ICP etching achieved **79 nm/min with ~83° sidewall angles** (vs. 37 nm/min and ~71° for Cr under the same ICP conditions) due to Ni's higher hardness and shape retention [6]. Electroplated Ni masks (350 nm thick, near-90° profile) have enabled sub-micron holey arrays in LN with ~6:1 selectivity [41].
- **Titanium/Aluminum stacks** work on all LN cuts when protected by a Cr cap, since unprotected Al produces redeposited AlF₃ "pyramids"; CrF₄ byproducts are more volatile. Ti/Al masks are removed with dilute HF [40].
- **Dielectric masks (SiO₂, SiN, HSQ)** enable CMOS-compatible processing but generally have lower selectivity (0.86:1–1.43:1 [6][38]) and can charge-buffer ions, causing sidewall striations and trenching [3]. Importantly, **thermal annealing of HSQ masks before dry etching increases the LN/HSQ selectivity from 0.55 to ~1** without changing optical losses, as measured by microring Q-factors [42].
- **Photoresist masks** (e.g., S1828 with soft post-bake) suffice for Ar-based etching where selectivity is inherently near 1 [39], but produce striated defects in higher-bias RIE [3].

**Trapezoidal mask profiles** are a powerful redeposition-mitigation trick: ETH Zurich's IBE simulations showed that increasing the mask sidewall angle from 85° to 50° progressively reduces redeposition, and they recommend trapezoidal masks (via PECVD SiO₂ or SiNₓ/a-Si) as one of three routes to redeposition-free etching [9].

### 3.4 Process Sequencing and Multi-Step Recipes

Several published strategies use interrupted etching or multi-step sequences to manage damage:

- **Iterative etch + wet clean cycles:** Hu et al. (ECIO 2008) used C4F8/He ICP etching with SC-1 cleaning between cycles to remove LiF, achieving 5.8-µm-high ridges with near-vertical walls [24]. Osipov's deep-etch process uses 30-s HF treatments every 90 minutes to strip non-volatile LiF, enabling 113.7-µm-deep profiles [35].
- **Two-step argon milling + GCIB smoothing:** Siew et al. (Optics Express, 2018) used initial high-power Ar ion milling at 7° off-normal, followed by a low-power 3-min step at 60° off-normal, then **gas cluster ion beam (GCIB) smoothing**, achieving propagation losses of **0.268 dB/cm (TE, 7 µm) and 0.33 dB/cm (TE, 5 µm)** in 700-nm-deep etched ridge waveguides — at the time the lowest reported for etched LN [43].
- **Low-bias final steps ("soft landing"):** The Kozlov data imply that a final low-bias step must stay above the ~90 eV ion-energy threshold to avoid LiF accumulation; below this, roughness increases sharply [33].
- **Periodic cooling/cleaning:** For deep etches in low-thermal-conductivity LN, 20-min etch/4-min cool cycles with hourly solvent cleaning (Aryal et al.) and 1-min etch/5-min cool cycles (NIST) prevent thermal damage and byproduct accumulation [3][40].
- **Chamber conditioning:** In shared cleanrooms, dedicated chambers for F- vs Cl-chemistries, extensive O₂ plasma cleans, and dummy-wafer conditioning are essential for reproducibility; CHF₃ specifically was found to contaminate chambers and harm reproducibility in the ETH study, which restricted gases to Cl₂, SF₆, O₂, and Ar [9][44].

---

## 4. Alternative Etch Processes and Damage-Avoidance Routes

### 4.1 Ion Beam Etching and Argon Ion Milling

Ion beam etching (IBE) and argon ion milling are purely physical sputtering processes (typically Ar⁺, 300–1000 eV). They etch any material, offer highly anisotropic profiles (collimated beam, tunable 0°–70°+ via tiltable stage), but have low rates (10–100 nm/min), poor selectivity (~1:1 to 3:1), and redeposition risk [45]. For LN specifically, Ar ion milling is used when the highest optical quality is required, since it avoids chemical damage from reactive gases. The record Q-factors in dry-etched TFLN (Harvard, 29.32 M) use Ar ICP-RIE, not IBE, but the two-step Ar milling + GCIB work (0.27–0.33 dB/cm) demonstrates the viability of the physical route [12][43]. **Angle-optimized IBE** (Zhang et al., Optics Express, 2026) used incidence angles from 0° to 30° with a soft positive-tone resist mask, achieving sidewall verticality approaching 80° (vs. typical <70°), etch depth ~400 nm, RMS roughness 0.65 nm on the unetched region, and **intrinsic Q up to 5.1 × 10⁶ (0.08 dB/cm)** in compact spiral microresonators [46]. Damage from ion milling can be mitigated by reducing beam energy (e.g., 300–500 eV) and post-etch annealing — an example from GaN HEMTs showed that reducing beam energy from 800 to 400 eV recovered channel mobility to >95% of pristine value [45]. Redeposition in ion milling is reduced by sample rotation and oblique incidence (45° Ar⁺ with rotation reduced MRAM MTJ short-circuit defects by ~80%) [45].

**Focused ion beam (FIB) milling** is the most damage-prone etch route: Ga⁺ at 30 kV creates ~20–23 nm amorphous layers, ~6 nm at 5 kV, and ~3 nm at 2 kV; the damage layer correlates nearly 1:1 with beam energy [8][47]. Raman studies confirm that FIB-induced lattice defects significantly degrade LN optical performance [48]. When FIB is used, a combination approach is recommended: FIB to define the pattern, then ICP-RIE with SF₆/Ar using the FIB-patterned Cr as a hard mask, then SC-1 cleaning to remove LiF — the process used by Jin et al. for LN metasurfaces with sidewall angles >80° [23].

**Reactive ion beam etching (RIBE)** combines RIE's chemical selectivity with IBE's directional control (rates 100–500 nm/min, aspect ratios ≤5:1); adding F- and Cl-gases to Ar beams is commercially offered for LN waveguide fabrication [45][1]. Early RIBE studies on LN (Ren et al., 1987) examined etch-rate dependence on beam energy, current density, and gas flow for CF₄/CHF₃, noting surface-roughening mechanisms and changes in dark conductivity of etched surfaces [49].

### 4.2 Atomic Layer Etching (ALE)

ALE is the most exciting recent addition to the LN etch toolbox. Two processes have been demonstrated:

- **Isotropic ALE (H₂ + SF₆/Ar):** etch per cycle (EPC) of 1.59 ± 0.02 nm/cycle with 96.9% synergy; the SF₆/O₂ variant achieves 2.24 nm/cycle with 99.5% synergy. The process is self-limiting and reduces sidewall roughness of Ar⁺-milled waveguides by 30% [29].
- **Directional ALE (HBr/BCl₃/Ar + Ar):** EPC 1.04 nm/cycle with 84.6% synergy at 0°C; at 200°C, EPC rises to 1.25 nm/cycle with surface remaining atomically smooth (Rq = 0.25 nm after 20 cycles). HBr chemistry reduces redeposition vs. F- and Cl-based plasmas because Br-based etch products have higher vapor pressures. **ALE-etched gratings showed no aspect-ratio-dependent etching down to 150 nm gaps**, in contrast to ion milling where ARDE appears below 300 nm. As a post-treatment, 50 cycles reduced waveguide roughness from Rq = 2.07 nm to 0.34 nm (84% reduction) with minimal lateral etching [28].

ALE thus serves both as an alternative etch (for shallow, damage-minimal pattern transfer) and as an ex-situ smoothing/repair step after conventional plasma etching.

### 4.3 Femtosecond Laser Ablation and Chemo-Mechanical Etching

**Femtosecond laser ablation** offers a "cold" machining route with minimal heat-affected zones (no observable HAZ vs. ~40 µm for nanosecond pulses [50]), but LN processing still produces structural defects that require post-annealing. Lin et al. (Scientific Reports, 2015) combined femtosecond laser micromachining with FIB milling to fabricate LN whispering-gallery microresonators; **thermal annealing at 500°C for 2 h in air improved the Q from 5.2 × 10⁴ to 1.6 × 10⁵**, directly demonstrating annealing-induced recovery after laser/FIB processing [22]. Crack-free femtosecond processing of LN is an active research topic, with defect management being the key challenge [51]. Femtosecond laser modification + selective etching (FLICE) is well established in glass (etch selectivity up to 1000:1 between modified and unmodified regions [52]) and has been applied to LN for depressed-cladding waveguides [53].

**Photolithography-assisted chemo-mechanical etching (PLACE)** completely bypasses plasma etching: a Cr mask is patterned by femtosecond laser direct writing, and CMP transfers the pattern chemo-mechanically, producing ultra-smooth surfaces (<0.5 nm RMS) with no plasma damage. Combined with 450°C annealing to repair ion-slicing damage, PLACE achieved the highest Q factors reported on TFLN (Q_int = 4.04 × 10⁷, <1 dB/m) [15]. PLACE-fabricated phase modulators achieved half-wave voltage ~3 V with only 2.8 dB insertion loss [54]. Similarly, the Chinese Optics Letters 2022 report of Q > 10⁸ used "chemo-mechanical etching" to thin bulk LN into pristine films, explicitly "avoiding ion slicing and ion etching processes" [55].

---

## 5. Device-Level Demonstrations of Recovered/Preserved Performance

### 5.1 Micro-Ring Resonators and Q-Factors

The Q-factor is the most sensitive single metric for etch damage. Reported milestones:

| Device/Process | Q-factor | Loss | Key post-etch steps | Source |
|---|---|---|---|---|
| Monolithic TFLN microring, Ar ICP-RIE (Harvard) | **Q_int = 29.32 × 10⁶** | **1.3 dB/m** | Hot KOH, SC-1, dilute HF, piranha; 520°C O₂ anneal; wide (3–5 µm) racetrack waveguides | Photonics Research 2024 [12] |
| PLACE microring, Z-cut TFLN | **Q_int = 4.04 × 10⁷** | **<1 dB/m (0.0091 dB/cm)** | 450°C air 2 h anneal (repairs ion-slicing damage) | Opt. Express 2023 [15] |
| Chemo-mechanically etched microring (no ion etch) | **Q > 10⁸** | ~0.0034 dB/cm | None (no plasma/ion exposure) | Chin. Opt. Lett. 2022 [55] |
| Angle-optimized IBE spiral microresonators | Q_int = 5.1 × 10⁶ | 0.08 dB/cm | 0–30° incidence angles; RMS 0.65 nm | Opt. Express 2026 [46] |
| Slow-heating anneal of EBL-damaged rings | Q_int = 3.93 × 10⁶ | ~0.1 dB/cm | Slow-heating post-process anneal | Opt. Mater. 2024 [7] |
| Ar ICP-RIE racetracks (ETH Zurich) | Q variation <2% | 1.55 dB/cm | Redeposition-free bias/pressure window | Nanophotonics 2023 [9] |
| Ar ICP-RIE rib waveguides (NIST) | — | ≤2 dB/cm | RCA-1a 85°C, 30 min; Cr mask; RF 150 W | AIP Advances 2024 [3] |
| Ar milling + GCIB smoothing | — | **0.268 dB/cm** (7 µm TE) | GCIB sidewall smoothing | Opt. Express 2018 [43] |
| Ar plasma ICP-RIE (FEMTO-ST) | — | 5 dB/cm | S1828 resist mask; wet clean | Opt. Mater. 2016 [39] |

The Harvard result is particularly instructive: the **combination of wide waveguides (3–5 µm) to reduce sidewall-overlap, optimized two-run Ar ICP-RIE, aggressive wet chemical cleaning, and 520°C O₂ annealing** pushed dry-etched TFLN within one order of magnitude of the theoretical material limit (Q ≈ 163 M) [12]. A complementary roughness study (Optica, 2025) showed that Q factors up to 27 × 10⁶ in wide waveguides (3.5 µm) are limited by interface roughness, while narrower waveguides (1.2 µm) are limited by sidewall roughness — and that **Z+ surfaces are significantly rougher (σ = 1.4–2.45 nm) than Z− surfaces (σ = 0.4–0.5 nm)**, causing >30% Q degradation in narrow PPLN devices vs. <7% in wide ones [10].

### 5.2 Waveguide Propagation Loss

Propagation loss directly quantifies the combined effect of surface roughness, stoichiometry, and defect absorption. Across the literature:

- **Dry-etched TFLN:** best values are 1.3 dB/m (multimode, Harvard [12]), ~2 dB/m (Jena wafer-scale [14]), 1.55 dB/cm (ETH Zurich single-mode racetracks [9]), ~2 dB/cm (NIST rib waveguides [3]), 5 dB/cm (Ulliac Ar plasma [39]).
- **Hybrid dry + smoothing:** 0.27–0.33 dB/cm with GCIB smoothing [43]; 0.08 dB/cm with angle-optimized IBE spirals [46].
- **Wet/CMP routes (no plasma):** 0.027 dB/cm with CMP (Wu et al., Nanomaterials 2018 — Rq = 0.452 nm, intrinsic Q = 1.14 × 10⁷) [56]; <1 dB/m with PLACE [15]; 0.0034 dB/cm with chemo-mechanical etching [55].
- **Modeling:** Hammer et al. (Optics Express, 2024) modeled sidewall roughness as thin lossy layers (thickness 20 nm) and found measured losses of 3.8–9.4 dB/cm across rib/strip waveguides, with a fitted lossy-layer permittivity ε″ = 0.0194; loss decreases with increasing waveguide top width due to reduced field strength at sidewalls [57].

### 5.3 Electro-Optic Modulators

Etch damage affects modulator performance through both optical loss (insertion loss, Q) and the electro-optic coefficient (r₃₃), which is sensitive to lattice damage and stoichiometry. Published device results include:

- **Tsinghua (Chinese Optics Letters, 2021):** LN-silica hybrid waveguide modulator with **VπL = 1.7 V·cm**, half-wave voltage 3.4 V over 5 mm, extinction ratio >17 dB, and only 1.3 dB roll-off at 67 GHz (6 dB bandwidth >110 GHz). The 100-nm SiO₂ buffer layer reduced optical loss by more than two orders of magnitude (below 0.1 dB/cm); waveguides were defined by HSQ EBL and argon-based RIE (300 nm partial etch) [58].
- **PLACE phase modulator (Optics Letters, 2024):** dual-arm TFLN phase modulator with Vπ ≈ 3 V, insertion loss 2.8 dB, and 29-sideband frequency-comb generation at 2 W microwave power — demonstrating that damage-free (non-plasma) fabrication preserves the electro-optic response [54].
- **Review context (Nanomaterials, 2024):** commercial TFLN modulators routinely exceed 100 GHz bandwidth (up to 110–170 GHz in the lab); low-loss LN waveguides of 0.1 dB/cm have been demonstrated; hybrid Si₃N₄/LN modulators reach VπL = 2.2–4 V·cm with >70 GHz bandwidth and <2.5 dB insertion loss [1]. For comparison, Ansys simulations based on published TFLN phase modulators give constant VπL of 3.18 V·cm [59].
- **Resonant modulators** reach VπL = 0.67 V·cm using Bragg gratings on X-cut LNOI, but rely on high-Q resonators that are extremely sensitive to etch-induced scattering loss [1].

### 5.4 Nonlinear Performance (PPLN and SHG)

The second-order nonlinearity (d₃₃ ≈ 27 pm/V) is the key figure of merit for frequency conversion. Etch damage manifests as reduced conversion efficiency and increased green/IR-induced photorefraction:

- **Shallow-etched TFLN waveguides** (Zhao et al., Optics Express, 2020) achieved **SHG conversion efficiency of 939 %W⁻¹** (length-normalized 3757 %W⁻¹·cm⁻²) [60].
- **Adapted-width PPLN waveguides** (Micromachines, 2024) reached **peak SHG power conversion efficiency of 2.1 × 10⁴ %W⁻¹** by compensating TFLN thickness inhomogeneity (±15 nm for a 600-nm film) with width adaptation along the 21-mm waveguide. The authors note that prior work by Chen et al. used adapted poling designs to achieve ~10⁴ %W⁻¹ — both demonstrations relied on etched waveguides (h = 300 nm etch depth, 75° sidewall angle) [61].
- **PPLN waveguide for 2-µm pumping** (UCSB, IEEE 2016) used a low-loss TFLN platform (<1 dB/cm for TE) with SiN strip loading and surface poling, demonstrating the feasibility of etch-based PPLN for mid-IR [62].
- **Watt-level SHG in PPLT** (EPFL, arXiv 2025) achieved 1.065 W on-chip at 775 nm from 4.5 W pump using Ar ion beam etching + **KOH wet etching for smooth sidewalls** — explicitly combining physical etching with a wet smoothing step [63].
- **Annealing restores nonlinearity:** In Ti:PPLN waveguides, "optical cleaning" with an auxiliary 532 nm laser restored phase-matching after photorefractive damage (generated power increased from 0.25 to 1.87 µW after 12 min), though recovery was only partial [11]. For plasma-damaged devices, the 520°C O₂ annealing step in the Harvard record-Q process is the strongest published evidence that annealing preserves (and recovers) the material quality needed for nonlinear operation [12].

---

## 6. Synthesis and Practical Recommendations

Based on the accumulated literature, a comprehensive damage-mitigation strategy for LN photonic devices should combine several layers of defense:

**1. Choose the etch chemistry deliberately.**
- For best optical quality with standard dry etching: **Ar-based ICP-RIE**, operated in the redeposition-free window (5–7 mTorr at ~600 V DC bias), with Cr or Ni hard masks [9][12].
- For high-rate deep etching: **SF₆/O₂ at elevated substrate temperature (250–325°C)**, with periodic HF/SC-1 cleans to strip LiF [35][36].
- For moderate rate with vertical walls: **CHF₃/Ar at 6 mTorr, ~130 V bias, without backside cooling** (82° walls, 5.76 µm/h) [5].
- Avoid CF₄ (notch formation) [37]; avoid CHF₃ in shared chambers if reproducibility is a concern [9].

**2. Optimize bias, pressure, and temperature to the "sweet spots" identified in parametric studies.**
- Maintain Ar⁺/ion energies above ~90 eV to avoid LiF-blocked rough surfaces [33].
- For Ar ICP-RIE: RF power 100–200 W (NIST), DC bias 400–600 V with 5–7 mTorr (ETH) [3][9].
- Use substrate heating (150–325°C) for F-based chemistries to volatilize NbF₅; use cooling cycles for Ar-based processes to prevent thermal damage [35][5][3].

**3. Select masks that minimize roughness transfer.**
- Ni > Cr > SiO₂ > soft resist for profile fidelity and selectivity [6][3]; anneal HSQ masks to improve selectivity [42]; use trapezoidal mask profiles to suppress redeposition [9].

**4. Always plan a post-etch treatment sequence.**
- **Wet clean:** SC-1/RCA-1a (2:2:1, 85°C, 15 min per orientation) to remove redeposited material; optionally dilute HF and hot KOH as in the Harvard sequence [3][12].
- **Thermal anneal:** 450–520°C in O₂ for 1–2 h is the most validated repair step for dry-etched TFLN [12][14]; consider slow-heating ramps to repair EBL damage [7]; for severe implantation/lattice damage, RTA at 1000–1060°C for 1 min in dry O₂ provides perfect recrystallization [16].
- **Cladding:** SiO₂ PECVD, or index-matched SiN/SiON (n ≈ 2.2, 10–100 nm) to fill residual roughness [31][14].

**5. Consider damage-avoidance alternatives where Q and nonlinearity are paramount.**
- PLACE/chemo-mechanical etching (Q_int > 10⁷, <1 dB/m) [15]; Ar milling + GCIB smoothing (0.27 dB/cm) [43]; ALE smoothing (84% roughness reduction) [28]; proton-exchange + wet etch for shallow structures [30].

**6. Design for damage tolerance.**
- Wide waveguides (3–5 µm) reduce sidewall-overlap and scattering [12][10]; racetrack geometries with large bend radii; adapted-width designs to compensate thickness inhomogeneity in nonlinear devices [61].

In summary, the field has converged on a clear best-practice recipe for high-performance dry-etched TFLN devices: **Ar-based ICP-RIE in a redeposition-free parameter window → aggressive wet chemical cleaning (hot KOH, SC-1, dilute HF, piranha) → annealing at 520°C in oxygen → SiO₂ or index-matched cladding**. This sequence has reproducibly yielded Q-factors above 10⁷ and propagation losses in the dB/m range, and it forms the baseline against which all other mitigation strategies — from ALE smoothing to PLACE — should be compared.

---

### Sources

[1] High-Speed Electro-Optic Modulators Based on Thin-Film Lithium Niobate (Nanomaterials 2024): https://www.mdpi.com/2079-4991/14/10/867

[2] Microstructure and domain engineering of lithium niobate crystal films for integrated photonic applications (Light: Science & Applications 2020): https://www.nature.com/articles/s41377-020-00434-0

[3] Optimization of waveguide fabrication processes in lithium-niobate-on-insulator platform (Kumar, Klimov, Kuo — AIP Advances/NIST): https://pmc.ncbi.nlm.nih.gov/articles/PMC11194688

[4] Estimation of losses caused by sidewall roughness in thin-film lithium niobate rib and strip waveguides (Hammer et al., Optics Express 2024): https://ris.uni-paderborn.de/download/54668/54669/2024-06%20Hammer%20-%20Optics%20Express%20-%20Estimation%20of%20losses%20caused%20by%20sidewall%20roughness%20in%20thin-film%20lithium%20niobate%20rib%20and%20strip%20waveguides.pdf

[5] Plasma etching of proton-exchanged lithium niobate (Hu et al., J. Vac. Sci. Technol. A 2006): http://www-old.mpi-halle.mpg.de/mpi/publi/pdf/6717_06.pdf

[6] Advanced Etching Techniques of LiNbO3 Nanodevices (Shen et al., Nanomaterials 2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC10609314

[7] Reduced material loss caused by Electron Beam Lithography in thin-film lithium niobate through post-process annealing (Shi et al., Optical Materials 2024): https://www.sciencedirect.com/science/article/abs/pii/S0925346724002325

[8] Amorphous Layer Formed during EM Sample Preparation using FIB (Globalsino): https://www.globalsino.com/EM/page4493.html

[9] Redeposition-free inductively-coupled plasma etching of lithium niobate for integrated photonics (Kaufmann et al., Nanophotonics 2023): https://pmc.ncbi.nlm.nih.gov/articles/PMC11501321

[10] Roughness-Limited Performance in Ultra-Low-Loss Lithium Niobate Cavities (Optica/arXiv 2505.01913): https://arxiv.org/html/2505.01913v2

[11] Photorefraction Management in Lithium Niobate Waveguides: High-Temperature vs. Cryogenic Solutions (arXiv 2601.15817): https://arxiv.org/html/2601.15817v1

[12] Twenty-nine million intrinsic Q-factor monolithic microresonators on thin film lithium niobate (Photonics Research 2024, Harvard): https://nano-optics.seas.harvard.edu/sites/g/files/omnuum6446/files/prj-12-8-a63.pdf

[13] Monolithic Ultrahigh-Q Lithium Niobate Microring Resonator (arXiv 1712.04479): https://arxiv.org/html/1712.04479v1

[14] Fabrication of low-loss lithium niobate on insulator waveguides on the wafer scale (arXiv 2407.09208, Jena/Fraunhofer): https://arxiv.org/pdf/2407.09208

[15] Ultra-high Q lithium niobate microring monolithically fabricated by photolithography assisted chemo-mechanical etching (Li et al., Optics Express 2023): https://arxiv.org/pdf/2306.10504

[16] Rapid thermal annealing of MeV erbium implanted LiNbO3 single crystals for optical doping (Fleuster et al., Applied Physics Letters 1994): http://www.erbium.nl/wp-content/uploads/2016/08/Rapid_thermal_annealing_of_MeV_implanted_LiNbO3_single_crystals_for_optical_doping_-_Appl_Phys_Lett_1994.pdf

[17] US6540827B1 — Slicing of single-crystal films using ion implantation (Columbia University): https://patents.google.com/patent/US6540827B1/en

[18] Fabrication techniques of lithium niobate waveguides (Armenise, IEE Proceedings J 1988): https://www.academia.edu/70911515/Fabrication_techniques_of_lithium_niobate_waveguides

[19] Li-Rich Vapor Transport Equilibration Temperature Dependence of Surface Composition of Initially Congruent LiNbO3 Crystal (Zhang et al., J. Am. Ceram. Soc. 2012): https://www.semanticscholar.org/paper/Li%E2%80%90Rich-Vapor-Transport-Equilibration-Temperature-Zhang-Wang/d6e2dccbe306171c1d8c33b2c8ba3d8fce39efaa

[20] Optical properties and ferroelectric engineering of vapor-transport-equilibrated near-stoichiometric lithium tantalate (Stanford, J. Appl. Phys. 2007): https://web.stanford.edu/~rlbyer/PDF_AllPubs/2007/425.pdf

[21] WO2002075444A1 — Thin film lithium niobate and electro-optic optical elements (Wisconsin Alumni Research Foundation): https://patents.google.com/patent/WO2002075444A1/en

[22] Fabrication of high-Q lithium niobate microresonators using femtosecond laser micromachining (Lin et al., Scientific Reports 2015): https://pmc.ncbi.nlm.nih.gov/articles/PMC4308694

[23] Fabrication of lithium niobate metasurfaces via a combination of FIB and ICP-RIE (Jin et al., Chinese Optics Letters 2022): https://www.researching.cn/articles/OJ8c8a1b62c7c6c8d2

[24] Etching of Lithium Niobate: From Ridge Waveguides to Photonic Crystal Structures (Hu, Ricken, Sohler — ECIO 2008): https://physik.uni-paderborn.de/fileadmin-nw/physik/Alumni/Sohler/2008/ecio08_hu.pdf

[25] Deep structures wet etched into lithium niobate using a physical mask (Randles, RIT thesis 2002): https://repository.rit.edu/theses/7344

[26] Poling-assisted hydrofluoric acid wet etching of thin-film lithium niobate (Yu et al., Optics Letters 2024): https://opg.optica.org/abstract.cfm?uri=ol-49-4-854

[27] CN103978406A — High-efficiency super-smooth chemical mechanical polishing method for lithium niobate crystal (Dalian University of Technology): https://patents.google.com/patent/CN103978406A/en

[28] Directional atomic layer etching of lithium niobate using Br-based plasma (arXiv 2511.01825): https://arxiv.org/html/2511.01825v1

[29] Isotropic atomic layer etching of MgO-doped lithium niobate using sequential exposures of H2 and SF6/Ar plasmas (arXiv 2310.10592): https://arxiv.org/pdf/2310.10592

[30] Fabrication of ridge optical waveguide in thin film lithium niobate by proton exchange and wet etching (Li et al., Optical Materials 2021): https://www.sciencedirect.com/science/article/abs/pii/S0925346721006340

[31] CN115951449A — Low-loss lithium niobate waveguide and preparation method thereof: https://patents.google.com/patent/CN115951449A/en

[32] Atomic layer deposition for fabrication of HfO2/Al2O3 thin films with high laser-induced damage thresholds (Wei et al., Nanoscale Research Letters 2015): https://pmc.ncbi.nlm.nih.gov/articles/PMC4385131

[33] Reactive Ion Etching of X-Cut LiNbO3 in an ICP/TCP System for the Fabrication of an Optical Ridge Waveguide (Kozlov et al., Applied Sciences 2023): https://www.mdpi.com/2076-3417/13/4/2097

[34] Characteristic of LiNbO3 thin film ICP etching for micro/nano fabrication (Huang et al., J. Micromech. Microeng. 2026): https://iopscience.iop.org/article/10.1088/1361-6439/ae36b6

[35] The effect of a lithium niobate heating on the etching rate in SF6 ICP plasma (Osipov et al., Materials Research Express 2019): https://iopscience.iop.org/article/10.1088/2053-1591/aafa9d

[36] Deep Etching of LiNbO3 Using Inductively Coupled Plasma in SF6-Based Gas Mixture (Osipov et al., J. Microelectromech. Syst. 2021): https://ieeexplore.ieee.org/document/9280327

[37] Analyses of LiNbO3 wafer surface etched by ECR plasma of CHF3 and CF4 (Mitsugi et al., 1998 Dry Process Symposium): https://www.soc.co.jp/sys/wp-content/themes/soc/assets/pdf/development/technology/document/2001_analysis.pdf

[38] High-Quality Dry Etching of LiNbO3 Assisted by Proton Substitution through H2-Plasma Surface Treatment (Aryal et al., Nanomaterials 2022): https://www.mdpi.com/2079-4991/12/16/2836

[39] Argon plasma inductively coupled plasma reactive ion etching study for smooth sidewall thin film lithium niobate waveguide application (Ulliac et al., Optical Materials 2016): https://www.sciencedirect.com/science/article/abs/pii/S0925346715301816

[40] High-Quality Dry Etching of LiNbO3 Assisted by Proton Substitution through H2-Plasma Surface Treatment (Aryal et al. — mask details): https://www.mdpi.com/2079-4991/12/16/2836

[41] Electroplated Ni mask for plasma etching of submicron-sized lithium niobate (FEMTO-ST, Microelectronic Engineering 2013): https://hal.science/hal-00914620/file/Electroplated_Ni_mask_for_plasma_etching_of_submicron-sized_2013_auteur.pdf

[42] Improved selectivity in dry etching of lithium niobate with thermal annealed hydrogen silsesquioxane mask (Hou et al., Nanotechnology 2025): https://eurekamag.com/research/100/222/100222930.php

[43] Ultra-low loss ridge waveguides on lithium niobate via argon ion milling and gas clustered ion beam smoothening (Siew et al., Optics Express 2018): https://pubmed.ncbi.nlm.nih.gov/29475292

[44] Navigating plasma etching of photonic chips in shared cleanrooms (Awan, J. Phys. Photonics 2025): https://iopscience.iop.org/article/10.1088/2515-7647/ae0ee5/pdf

[45] Reactive Ion Etching vs Ion Milling (IBE): Complete Comparison Guide (NineScrolls): https://ninescrolls.com/insights/reactive-ion-etching-vs-ion-milling

[46] Angle-optimized ion-beam etching for high-verticality and low-loss lithium niobate microresonators (Zhang et al., Optics Express 2026): https://opg.optica.org/oe/abstract.cfm?uri=oe-34-4-6870

[47] Avoiding Common Types of Lamella Defects Caused by the Focused Ion Beam (Covalent): https://www.youtube.com/watch?v=_pKw8SMnFiM

[48] Raman characterization of focused ion beam fabricated lithium niobate film (J. Appl. Phys. 135, 033101): https://pubs.aip.org/aip/jap/article/135/3/033101/3000637

[49] Reactive ion beam etching characteristics of LiNbO3 (Ren et al., Nucl. Instr. Meth. B 1987): https://www.sciencedirect.com/science/article/abs/pii/S0168583X87802021

[50] When Does Femtosecond Laser Ablation Outperform Nanosecond Processing? (JPT Laser): https://en.jptoe.com/about/newsroom/technical-information/nanosecond-vs-femtosecond-laser-ablation

[51] Crack-free femtosecond laser processing of lithium niobate (J. Appl. Phys. 129, 063102, 2021): https://pubs.aip.org/aip/jap/article/129/6/063102/287542

[52] Repair of Fused Silica Damage Using Selective Femtosecond Laser-Induced Etching (Fang et al., Crystals 2023): https://www.mdpi.com/2073-4352/13/2/309

[53] Femtosecond laser micromachining of lithium niobate depressed cladding waveguides (He et al., Optical Materials Express 2013): https://opg.optica.org/fulltext.cfm?uri=ome-3-9-1378

[54] Compact low-half-wave-voltage thin film lithium niobate electro-optic phase modulator fabricated by PLACE (Gao et al., Optics Letters 2024): https://pure.ecnu.edu.cn/en/publications/compact-low-half-wave-voltage-thin-film-lithium-niobate-electro-o

[55] Lithium niobate microring with ultra-high Q factor above 10^8 (Gao et al., Chinese Optics Letters 2022): https://pure.ecnu.edu.cn/en/publications/lithium-niobate-microring-with-ultra-high-q-factor-above-10sup8su

[56] Long Low-Loss-Lithium Niobate on Insulator Waveguides with Sub-Nanometer Surface Roughness (Wu et al., Nanomaterials 2018): https://www.mdpi.com/2079-4991/8/11/910

[57] Estimation of losses caused by sidewall roughness in thin-film lithium niobate rib and strip waveguides (Hammer et al., Optics Express 2024): https://ris.uni-paderborn.de/download/54668/54669/2024-06%20Hammer%20-%20Optics%20Express%20-%20Estimation%20of%20losses%20caused%20by%20sidewall%20roughness%20in%20thin-film%20lithium%20niobate%20rib%20and%20strip%20waveguides.pdf

[58] Wideband thin-film lithium niobate modulator with low half-wave-voltage length product (Liu et al., Chinese Optics Letters 2021): https://www.researching.cn/articles/OJ9d03e04e9a0ee503

[59] Thin Film Lithium Niobate Electro-Optic Phase Modulator (Ansys Optics): https://optics.ansys.com/hc/en-us/articles/19435937674387-Thin-Film-Lithium-Niobate-Electro-Optic-Phase-Modulator

[60] Shallow-etched thin-film lithium niobate waveguides for second-harmonic generation (Zhao et al., Optics Express 2020): https://opg.optica.org/oe/abstract.cfm?uri=oe-28-13-19669

[61] Efficient Second-Harmonic Generation in Adapted-Width Waveguides Based on Periodically Poled Thin-Film Lithium Niobate (He et al., Micromachines 2024): https://www.mdpi.com/2072-666X/15/9/1145

[62] A thin-film PPLN waveguide for second-harmonic generation (Chang et al., UCSB IEEE 2016): https://siliconphotonics.ece.ucsb.edu/sites/default/files/2017-06/C1007_0.pdf

[63] Watt-level second harmonic generation in periodically poled thin-film lithium tantalate (EPFL, arXiv 2512.07968): https://arxiv.org/html/2512.07968v1
