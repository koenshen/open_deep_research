# Comprehensive Overview of Plasma Etching Damage Mitigation Strategies for Lithium Niobate Photonics

## 1. Introduction

Lithium niobate (LN) is a premier material for nonlinear photonics due to its strong electro-optic and nonlinear optical coefficients, broad transparency window (420–5200 nm), and high refractive index. However, plasma etching—essential for fabricating waveguides, resonators, and photonic integrated circuits—induces various forms of material damage that degrade device performance. This report provides a comprehensive overview of mitigation strategies, including pre-etching treatments, post-etching repair methods, and alternative etching techniques, with quantitative results from leading research groups worldwide.

---

## 2. Types of Plasma Etching Damage on Lithium Niobate

### 2.1 Surface Roughening

Plasma etching significantly increases surface roughness, which directly contributes to scattering losses in photonic devices. The degree of roughening depends strongly on etching parameters:

- **ICP-RIE parametric study (Chang et al., 2015):** Under optimized conditions, surface roughness less than 40 nm was achieved for etch depths greater than 3 μm. However, increasing ICP power and RF power both increased surface roughness [Source: "A parametric study of ICP-RIE etching on a lithium niobate substrate"].

- **Substrate temperature effects (Osipov et al., 2019, Mater. Res. Express):** Etching in SF₆/O₂ gas mixture achieved lower roughness (RMS = 30.52 nm) compared to SF₆/Ar (RMS = 119.37 nm), while also providing higher etch rates (812 nm/min vs. 337 nm/min) [Source: "The effect of a lithium niobate heating on the etching rate in SF₆ ICP plasma"].

- **Redeposition-free ICP etching (Kaufmann et al., 2023, Nanophotonics):** Using high DC bias (>600 V) with moderate pressure (5–7 mTorr), the authors achieved remarkable surface roughness Sq ~0.08 nm—four times better than the unetched surface [Source: "Redeposition-free inductively-coupled plasma etching"].

- **Argon ion milling (Siew et al., 2018, Optics Express):** Ridge waveguides fabricated via argon ion milling exhibited RMS roughness around 8 nm [Source: "Ultra-low loss ridge waveguides on lithium niobate via argon ion milling"].

- **Atomic Layer Etching (ALE) effects:** ALE on flat bulk LN increased RMS roughness from 0.2 nm to 0.57 nm after 20 cycles, but reduced sidewall roughness of Ar⁺-milled thin-film LN waveguides by 30% (from 0.82 nm to 0.55 nm) after 50 cycles, due to the isotropic nature of the etch [Source: arXiv:2310.10592].

- **Directional ALE with HBr chemistry (2025):** At 200°C, the directional ALE process maintained an atomically smooth surface (Rq = 0.25 ± 0.03 nm) after 20 cycles, unlike Cl-based chemistries. Applied to pre-etched TFLN waveguides, it reduced surface roughness by 84% (from 2.07 nm to 0.34 nm) [Source: "Directional atomic layer etching of lithium niobate using Br-based plasma"].

### 2.2 Stoichiometric Changes (Li Depletion and Nb Reduction)

Plasma etching preferentially removes lithium, leading to significant stoichiometric changes in the near-surface region:

- **XPS study of Li/Nb ratio (Applied Surface Science, 2016):** Mechanical processing dramatically reduces the Li/Nb ratio regardless of crystal polarity. The Li/Nb ratio on negative cleave surfaces is 0.946 ± 0.074, while positive surfaces show excess lithium (Li/Nb = 1.25 ± 0.10) [Source: "XPS study of Li/Nb ratio in LiNbO₃ crystals"].

- **SC-1 removal of oxygen vacancy layer (Optical Materials Express, 2025):** XPS analysis revealed that SC-1 cleaning removes a surface layer characterized by higher oxygen vacancies (Nb⁴⁺ states). The initial etch rate is ~2 nm/min, slowing to ~0.33 nm/min, suggesting a notable change in the top 10 nm of the film [Source: "Thin film LiNbO₃ surface preparation using SC-1"].

- **Fracture origins and chemical reduction (Journal of Materials Research, 2000):** Defective regions contain chemically reduced Nb (metallic Nb) and lithium hydride (LiH), with XPS peaks at 202.36 and 205.66 eV attributed to metallic Nb. LiH formation is attributed to local reduction triggered by explosive repolarization [Source: "Fracture origins in LiNbO₃ wafers due to postprocessing"].

- **Hydrogen plasma treatment:** Heavy blackening of the sample occurs due to chemical reduction. At low pressures, the niobate structure on the surface is completely destroyed, leaving only niobium and its oxides [Source: "Plasma processing of LiNbO₃ in a hydrogen/oxygen radio-frequency discharge"].

- **Proton Exchange (PE) for Li reduction (Hu et al., 2006, J. Vac. Sci. Technol. A):** By replacing up to 85% of lithium ions with protons via benzoic acid process (240°C, 5 h, depth 2.8 μm), the formation of nonvolatile LiF is greatly reduced [Source: "Plasma etching of proton-exchanged lithium niobate"].

### 2.3 Lattice Defects and Amorphization

Ion bombardment during plasma etching creates lattice disorder and amorphization:

- **Ion irradiation damage (Thin Solid Films, 2023):** Defect structures in 128° Y-cut LN induced by H, He, and N ions at energies 150 keV to 2 MeV and fluences 1×10¹² to 1×10¹⁸ ions/cm² were characterized. A buried damage layer suitable for crystal ion slicing can be achieved with He implantation at 1×10¹⁸ ions/cm² followed by annealing at 250°C or 500°C. Nitrogen implantation causes significantly more displacement damage than hydrogen [Source: "Defect structures as a function of ion irradiation and annealing in LiNbO₃"].

- **Thermal spike responses in LNOI (Crystals, 2022):** Under 30 MeV ³⁵Cl and ⁴⁰Ar ion irradiation, discontinuous (4.0–4.5 nm diameter) and continuous (5.0–5.5 nm diameter) ion tracks form with lattice disorder. RBS/channeling analysis showed the damage cross-section of a single ion track is ~17 nm² (diameter ~5 nm) [Source: "Thermal Spike Responses and Structure Evolutions in Lithium Niobate on Insulator (LNOI) under Swift Ion Irradiation"].

- **Subsurface damage characterization (Materials, 2025):** Subsurface damage—including cracks, residual stress, phase transformations, and amorphization—is introduced during ultra-precision processes like grinding and polishing. This review systematically characterizes methods for identifying and quantifying such damage [Source: "Recent Advances in the Characterization of Subsurface Damage in Optical Materials"].

### 2.4 Increased Optical Absorption

Plasma-induced damage creates color centers and defect states that increase optical absorption, particularly in the near-infrared and visible regions:

- **Reduced material loss in TFLN waveguides (Shams-Ansari et al., 2022, APL Photonics):** Using a newly developed characterization method, the material-limited quality factor of TFLN was improved via post-fabrication annealing to Q ≈ 1.6 × 10⁸ at telecommunication wavelengths, corresponding to a propagation loss of 0.2 dB/m. This represents a major improvement over previous state-of-the-art resonator Q of ~10 million [Source: "Reduced Material Loss in Thin-film Lithium Niobate Waveguides"].

- **Ultra-low loss visible photonics (Optica, 2019):** Waveguides feature ultra-low propagation loss of 6 dB/m, while microring resonators have an intrinsic quality factor of 11 million, both measured at 637 nm wavelength [Source: "Ultra-low-loss integrated visible photonics using thin-film lithium niobate"].

- **LNOI waveguides at 1550 nm (Optics Express, 2018):** Single mode rib waveguides achieved propagation loss of approximately 0.4 dB/cm for TE polarization and 0.93 dB/cm for TM, using a reactive ion etching process with CHF₃/Ar gas mixture. Sidewall roughness was <2 nm RMS [Source: "Ultra-low loss photonic circuits in lithium niobate on insulator"].

---

## 3. Pre-Etching Mitigation Strategies

### 3.1 Surface Preparation Techniques

Proper surface preparation before etching is critical for minimizing damage:

**SC-1 (Standard Cleaning 1) Treatment:** A 2025 study in Optical Materials Express demonstrated that SC-1 cleaning (1:1:5 NH₄OH:H₂O₂:DI at 65°C) removes a surface layer of LiNbO₃ characterized by higher oxygen vacancies. The proposed protocol includes:
- Initial SC-1 treatment (30 min) to remove the defective surface layer before Si₃N₄ deposition
- Standard lithography and etching
- Short SC-1 cleanup (5 min) to remove etching residues
- Surface roughness reduction: from 0.58 nm to 0.23 nm after O₂ plasma
- Initial etch rate ~2 nm/min, stabilizing at ~0.33 nm/min

**CMP (Chemical Mechanical Polishing):** Polishing the LNOI surface by CMP reduces waveguide sidewall roughness after etching, improving device performance and power transmission efficiency. LNOI's high hardness and inactive chemical properties make traditional semiconductor processing inadequate, requiring specialized approaches [Source: "Experimental study on chemical mechanical polishing of LNOI"].

**CARE (Catalyst-Referred Etching) Planarization:** A 2022 study (EPJ Web of Conferences) demonstrated CARE using a platinum thin film catalyst and pure water as etchant on a 2-inch Y-cut LN substrate. Surface roughness improved from 0.175 nm RMS (as-received) to 0.064 nm RMS (CARE-processed). All residual stress and surface damage could be removed completely, producing an atomically smooth surface (<0.1 nm RMS) [Source: "Planarization of Lithium Niobate Surface Using a Thin Film Catalyst"].

**PLACE Technique (Photolithography Assisted Chemo-Mechanical Etching):** Developed in 2018, PLACE enables wafer-scale manufacturing with high speed. The loaded Q factors of microcavities over 10⁶ were first demonstrated on LNOI platform. Propagation losses of 0.34 dB/m and intrinsic Q factors up to 1.23×10⁸ have been achieved [Source: "Recent development in integrated Lithium niobate photonics"].

**Proton Exchange (PE) Pre-Treatment (Hu et al., 2006):** Proton exchange replaces up to 85% of lithium ions with protons via a benzoic acid process (240°C, 5 h, depth 2.8 μm). This reduces Li concentration, preventing LiF deposition to a large extent. The PE process significantly improves etch rates and profiles [Source: "Plasma etching of proton-exchanged lithium niobate"].

**H₂-Plasma Surface Treatment (Aryal et al., 2022, Nanomaterials):** To improve mask quality on X- and Y-cut substrates, H₂-plasma treatment substitutes protons for lithium ions, mimicking the effect of a proton exchange process. This improves adhesion of the Ti/Al/Cr hard mask, enabling etch depths up to 3.4 μm with nearly vertical sidewalls [Source: "High-Quality Dry Etching of LiNbO₃ Assisted by Proton Substitution through H₂-Plasma Surface Treatment"].

### 3.2 Choice of Masking Materials

The selection of hard mask material significantly impacts etch quality, sidewall roughness, and damage:

**Cr Hard Mask:** 
- NIST study (AIP Advances, 2024): A 50 nm Cr hard mask proved superior to soft e-beam resist and SiO₂ masks, yielding smoother sidewalls without trenching. Optimal parameters: RF bias 100–200 W, ICP power 1500 W, pressure 5 mTorr, Ar flow 20 sccm, temperature 5°C [Source: "Optimization of waveguide fabrication processes in lithium-niobate-on-insulator platform"].
- Kozlov et al. (2023, Applied Sciences): Cr mask via DC magnetron sputtering achieved waveguide sidewall slope angles of 62°–75°, etching depths of 0.23–0.60 μm, and mask selectivity of 1:4 to 1:8 [Source: "Reactive Ion Etching of X-Cut LiNbO₃ in an ICP/TCP System"].

**Ti/Al/Cr Hard Mask:** 
- Aryal et al. (2022, Nanomaterials): The Ti/Al/Cr stack was found to be the best mask material for all crystal orientations, removing all redeposition and micro-masking issues. The metal mask demonstrates improved etch selectivity of 30:1, allowing thin layers of metal to protect thick layers of LN [Source: "High-Quality Dry Etching of LiNbO₃ Assisted by Proton Substitution through H₂-Plasma Surface Treatment"].

**Diamond-Like Carbon (DLC) Hard Mask:**
- EPFL (Nature Communications, 2023): DLC provides high etch selectivity (up to 3× between LN and DLC), enabling deep etching of LN strip waveguides with vertical sidewalls (80°), low propagation losses (as low as 4 dB/m), and a 16-fold increase in area density. Microresonators with quality factors >10 million were fabricated [Source: "High density lithium niobate photonic integrated circuits"].

**Ni Mask vs. Cr Mask:**
- Nanomaterials study (2023): For RIE, Cr masks gave 10 nm/min and 60° sidewall angle; Ni masks improved to 11 nm/min and 72°. For ICP, Ni masks achieved 79 nm/min and 83° sidewall angle; Cr masks gave 37 nm/min and 71°. Ni masks offer better shape retention and higher sidewall angles [Source: "Advanced Etching Techniques of LiNbO₃ Nanodevices"].

**SiO₂ Hard Mask:**
- Using SiO₂ masks with Cl-based ICP gases gave the highest etching rate of 108 nm/min but a lower sidewall angle of 65°, with an etching selectivity ratio of 0.86:1 [Source: "Advanced Etching Techniques of LiNbO₃ Nanodevices"].
- Optimized ICP recipe with Cl₂/H₂/Ar flows of 10/20/50 sccm achieved a sidewall angle of 79.1°, etch rate of ~32 nm/min, and selectivity of 1.43:1 relative to SiO₂ mask [Source: "Characteristic of LiNbO₃ thin film ICP etching for micro/nano fabrication"].

**HSQ Mask Annealing (2025, Nanotechnology):** Thermal annealing of hydrogen silsesquioxane (HSQ) masks before dry etching increases the LN/HSQ etching selectivity from 0.55 to approximately 1. Microring Q factor tests confirm that optical losses remain unaltered [Source: "Improved selectivity via HSQ mask annealing"].

---

## 4. Post-Etching Repair Methods

### 4.1 Thermal Annealing

Thermal annealing is the most widely used post-etching repair method, effectively reducing optical absorption and restoring crystallinity:

**Post-Fabrication Annealing (Shams-Ansari et al., 2022, APL Photonics):** Post-fabrication annealing and low-temperature oxide cladding significantly reduce optical absorption in TFLN waveguides. The material-limited quality factor was improved to Q ≈ 1.6 × 10⁸ at telecommunication wavelengths, corresponding to a propagation loss of 0.2 dB/m. The annealing step improves crystallinity, repairing potential damages caused by ion slicing and etching [Source: "Reduced Material Loss in Thin-film Lithium Niobate Waveguides"].

**Record-High Q-Factor Microresonators (Harvard, 2024, Photonics Research):** Monolithic microresonators achieved a record-high intrinsic Q factor of 29.32 million, corresponding to an ultra-low propagation loss of 1.3 dB/m. This was achieved using dry reactive ion etching with optimized fabrication parameters including 600 nm LN thickness, 325 nm etch depth, and annealing at 520°C. Statistical analysis revealed that wider waveguides (4.5 μm width) and longer racetracks (10 mm length) yield higher Q factors [Source: "Monolithic microresonators with record-high intrinsic Q factor"].

**Annealing Temperatures Above 500°C:** Research indicates that if the annealing process is applied at temperatures above 500°C, the propagation optical loss can be further reduced because of improved crystallinity [Source: "Low-loss lithium niobate waveguide and preparation method"].

**Annealing in Air at 250°C for 2 Hours (Post-Wet Etching, 2022, Advanced Materials):** After wet etching, annealing at 250°C for 2 hours in air yielded a micro-racetrack resonator with an intrinsic Q-factor exceeding 9.27 × 10⁶, approaching the performance of state-of-the-art TFLN microrings made by ICP-RIE and CMP [Source: "Wet etching method for TFLN microrings"].

**Post-Process Annealing to Repair EBL Damage (2024, Materials Science in Semiconductor Processing):** A slow-heating annealing process effectively repaired damage from electron beam lithography, reducing waveguide loss by approximately 50% and increasing the intrinsic Q-factor by roughly 100%. The best X-cut resonators achieved a Q_int of 3.93 × 10⁶, corresponding to a waveguide loss of approximately 0.1 dB/cm [Source: "Material loss in thin-film lithium niobate caused by electron beam lithography"].

**Annealed Proton Exchange Process (200°C Exchange + 350°C Annealing, Optics Letters, 2015):** Low-loss channel waveguides exhibited propagation loss as low as 0.6 dB/cm at 1.55 μm. The single-crystal lattice structure was preserved by a moderate annealed proton exchange process: 5 minutes of proton exchange at 200°C, followed by 3 hours of annealing at 350°C. Longer proton exchange times destroy the crystal structure [Source: "Low-loss channel waveguides in single-crystal lithium niobate thin film"].

### 4.2 Chemical Treatments and Wet Etching

Chemical treatments can remove damaged surface layers and smooth etched surfaces:

**SC-1 Cleaning (Cyclic ICP Etching):** For ICP-etching of X-cut LN, a cyclic process is used: ICP etching in C₄F₈/He plasma for several minutes, then cleaning in SC-1 solution (70% H₂O, 20% H₂O₂, 10% NH₄OH) for 1 minute to remove LiF re-deposition. This produces ridges up to 5.8 μm height and 8 μm width with nearly vertical walls [Source: "Etching of Lithium Niobate: From Ridge Waveguides to Photonic Crystal Structures"].

**Post-Etch Cleaning with Heated RCA-1 Solution (NIST, AIP Advances, 2024):** RCA-1a solution (NH₄OH:H₂O₂:H₂O = 2:2:1) at 85°C for 15 minutes each at 0° and 90° orientations (total 30 min) was optimal for removing redeposited fences without damaging the waveguide. Longer cleaning caused chipping and asymmetry [Source: "Optimization of waveguide fabrication processes in lithium-niobate-on-insulator platform"].

**Wet Etching of Z-cut LN with HF/HNO₃/Ethanol (IEEE Photonics Technology Letters, 2007):** Adding ethanol to the etchant (1:7 volume ratio) significantly smooths the etched surface by suppressing hydrogen bubble formation. Etch rates: ~0.62 μm/h with ethanol addition. Resulting ridges up to 8 μm high and 4.5–7 μm wide support monomode propagation at 1.55 μm. Propagation losses: 0.3 dB/cm (TE) and 0.9 dB/cm (TM) for a 6.5-μm-wide, 8-μm-high ridge [Source: "Lithium Niobate Ridge Waveguides Fabricated by Wet Etching"].

**Wet Etching of TFLN Microrings (2022, Advanced Materials):** This method yields micro-racetrack resonators with intrinsic Q-factor exceeding 9.27 × 10⁶, approaching the performance of state-of-the-art TFLN microrings made by ICP-RIE and CMP. Unlike ICP-RIE (moderate throughput, moderate reproducibility, high cost) and CMP (moderate throughput, low cost), wet etching offers high throughput, high reproducibility, and low cost [Source: "Wet etching method for TFLN microrings"].

**Hybrid Process (RIE Dry Etch + Wet Etch, Nanomaterials, 2023):** Combining RIE dry etching with subsequent wet etching after high-temperature reduction treatment (H₂/Ar atmosphere) yields an etching rate of 10 nm/min and pristine 90° sidewall angles. This hybrid process preserves the ferroelectric properties of LNO, making it suitable for large-scale fabrication of LNO domain-wall memory arrays [Source: "Advanced Etching Techniques of LiNbO₃ Nanodevices"].

### 4.3 Ion Beam Smoothing

Ion beam techniques can smooth etched surfaces and reduce scattering losses:

**Argon Ion Milling of Ridge Waveguides (Siew et al., 2018, Optics Express):** Ultra-low loss ridge waveguides on lithium niobate via argon ion milling achieved propagation losses as low as 0.268 dB/cm for a 7 μm waveguide (TE) and 0.33 dB/cm for a 5 μm waveguide. Gas clustered ion beam (GCIB) smoothening was used as a follow-up step [Source: "Ultra-low loss ridge waveguides on lithium niobate via argon ion milling"].

**Angle-Optimized Ion-Beam Etching (IBE) (Zhang et al., 2026, Optics Express):** An angle-optimized IBE process achieved compact LNOI microresonators with sidewall angles reaching nearly vertical (80°). Using a soft positive-tone ZEP520A mask, the approach produces trench-free sidewall profiles with exceptional verticality. Compact spiral microresonators achieved intrinsic quality factors up to 5.1 × 10⁶, corresponding to a propagation loss of approximately 0.26 dB/cm [Source: "Angle-optimized ion-beam etching for high-verticality LNOI microresonators"].

**Sidewall Polishing by CMP (KTH, 2018, Optics Express):** A method to reduce scattering losses in LNOI ridge waveguides by chemo-mechanical polishing post-process using a soft polishing tissue, Cr protective layer, low polishing pressure, and KOH cleaning. The Q-factor improves by more than one order of magnitude with increased polishing time and pressure product. The lowest measured loss: 0.04 dB/cm (4 dB/m) at 980 nm, with a power-law dependence on wavelength (exponent 2.2) [Source: "Scattering-loss reduction by sidewall polishing"].

### 4.4 Chemo-Mechanical Polishing (CMP) and PLACE

CMP-based methods provide the lowest propagation losses reported for LN photonics:

**PLACE (Photolithography-Assisted Chemo-Mechanical Etching):** 
- Propagation loss as low as 0.027 dB/cm, one of the lowest reported for LNOI waveguides [Source: "Long Low-Loss-Lithium Niobate on Insulator Waveguides"].
- Intrinsic Q factors up to 1.23×10⁸ have been achieved [Source: "Recent development in integrated Lithium niobate photonics"].
- The PLACE approach uses femtosecond laser ablation for Cr hard mask patterning and CMP for waveguide etching, enabling large footprint, high uniformity, smooth sidewalls (roughness <0.1 nm), and a rapid production rate—mask patterning takes only 3 minutes per modulator, corresponding to an annual yield of 150,000 pieces [Source: "PLACE for high-production-rate modulators"].

**CMP with Ta₂O₅ Cladding (Lin et al., 2019, Micromachines):** Single-mode LNOI waveguides fabricated by combining femtosecond laser ablation of a Cr hard mask with chemomechanical polishing achieved a propagation loss of 0.042 ± 0.02 dB/cm. Sidewall roughness was ~0.5 nm. A Ta₂O₅ cladding layer (3.5 μm thick) was deposited [Source: "High-Precision Propagation-Loss Measurement of Single-Mode LNOI Waveguides"].

**Mask-CMP Technology (2025, Optics & Laser Technology):** A theoretical model for fabricating TFLN waveguide microstructures using mask-CMP technology was validated against experimental data from a 10 mm × 10 mm X-cut TFLN sample with a Cr mask, etched using colloidal silica slurry (20 nm particles, pH 10.5). The mask-CMP method offers a low-cost, high-efficiency route for large-scale TFLN chip fabrication [Source: "Mask-CMP technology for TFLN waveguides"].

---

## 5. Alternative Etching Techniques and Conditions

### 5.1 ICP-RIE Parameter Optimization

Optimizing ICP-RIE parameters is critical for minimizing damage:

**ICP-RIE Parametric Study (Chang et al., 2015):** Under optimized parameters, surface roughness less than 40 nm, structure depth greater than 3 μm, sidewall angle approximately 120°, and etching rate greater than 117 nm/min were achieved within 28 minutes. Surface roughness increased when ICP power and RF power were increased [Source: "A parametric study of ICP-RIE etching on a lithium niobate substrate"].

**Optimized ICP-RIE for LNOI Waveguides (NIST, 2024, AIP Advances):** A systematic optimization compared hard mask materials (soft e-beam resist, Cr, SiO₂) and optimized ICP etch parameters. The Cr hard mask produced smoother sidewalls than SiO₂, which caused trenching due to charging effects. Using the optimized Cr mask process (ICP power 1500 W, RF power 150 W, pressure 5 mTorr, Ar flow 20 sccm, temperature 5°C), the team fabricated 600 nm wide rib waveguides with 70° sidewall angles and 350 nm etch depth. Average total insertion loss was -10.5 ± 0.6 dB across eight 4.5 mm long waveguides [Source: "Optimization of waveguide fabrication processes in lithium-niobate-on-insulator platform"].

**ICP-RIE with Cl₂/H₂/Ar Chemistry (Huang et al., 2026, J. Micromech. Microeng.):** Finite element simulations showed that steeper sidewall angles (80° vs. 40°) suppress spurious modes and improve resonator quality factor. The optimized ICP recipe used 600 W ICP power, 120 W RF bias, 10 mTorr pressure, and Cl₂/H₂/Ar = 10/20/50 sccm, achieving a sidewall angle of 79.1°, an etch rate of ~32 nm/min, and a selectivity of 1.43:1 relative to SiO₂ mask. Lateral vibration resonators operating at ~400 MHz demonstrated quality factors exceeding 1750 [Source: "Characteristic of LiNbO₃ thin film ICP etching for micro/nano fabrication"].

**ICP-RIE with SF₆/Ar for X-Cut LN (MDPI Applied Sciences, 2023):** Optimal recipes yielded waveguides with slope angles of 62°–75°, etching depths 0.23–0.60 μm, and mask selectivity 1:4 to 1:8. Lower pressure (0.007 mbar) improved anisotropy but increased surface roughness due to a transition to chemical etching, evidenced by a brown LiF-containing film. Higher bias voltage (>186 V) and average ion energy (~90 eV) enable sputtering of the LiF layer, reducing roughness and preventing microtrench formation [Source: "Reactive Ion Etching of X-Cut LiNbO₃ in an ICP/TCP System"].

**ICP Dry Etching with CHF₃/Ar and H₂-Plasma Treatment (Aryal et al., 2022, Nanomaterials):** The optimized process used a Ti/Al/Cr metal hard mask and CHF₃/Ar (1:1) gas mixture. Periodic etching pauses (20 min etch, 4 min cooling) and chemical cleaning every hour managed thermal effects and byproduct accumulation. The method achieved etch depths up to 3.4 μm with nearly vertical sidewalls (only ~3° offset) and low surface roughness. Etch rates were approximately 650 nm/h for bulk LN [Source: "High-Quality Dry Etching of LiNbO₃ Assisted by Proton Substitution through H₂-Plasma Surface Treatment"].

### 5.2 Gas Chemistry Effects

The choice of gas chemistry dramatically affects etch quality:

**CHF₃/Ar Chemistry:** 
- Hu et al. (2006, J. Vac. Sci. Technol. A): ICP-RIE with CHF₃/Ar (50/50 sccm, 1500 W ICP, 130 V dc bias, 6 mTorr) achieved a nearly vertical 82° sidewall, an etch rate of 5.76 μm/h, and selectivity to Cr mask of 32:1. Photonic crystal waveguide structures with 500 nm period and 1.5 μm depth were successfully fabricated [Source: "Plasma etching of proton-exchanged lithium niobate"].

**SF₆/O₂ vs. SF₆/Ar:**
- Osipov et al. (2019, Mater. Res. Express): SF₆/O₂ achieved higher etch rates (812 nm/min at 598 K) and lower roughness (RMS = 30.52 nm) compared to SF₆/Ar (337 nm/min, RMS = 119.37 nm) [Source: "The effect of a lithium niobate heating on the etching rate in SF₆ ICP plasma"].

**C₄F₈/He Plasma:**
- ECIO '08 conference: ICP-etching of X-cut LN using C₄F₈/He (1:1) plasma at ~200°C achieved high selectivity (>10 vs. Cr mask). Cyclic process with SC-1 cleaning produced ridges of 5.8 μm height and 8 μm width with nearly vertical walls [Source: "Etching of Lithium Niobate: From Ridge Waveguides to Photonic Crystal Structures"].

**Cl₂/H₂/Ar Chemistry:**
- Huang et al. (2026, J. Micromech. Microeng.): Optimized ICP recipe achieved sidewall angle of 79.1°, etch rate of ~32 nm/min, and selectivity of 1.43:1 relative to SiO₂ mask [Source: "Characteristic of LiNbO₃ thin film ICP etching for micro/nano fabrication"].

### 5.3 Temperature Effects

Substrate temperature is a critical parameter for controlling etch rate and damage:

**Effect of Substrate Temperature on SF₆ ICP Etching (Osipov et al., 2019):** With fixed parameters (ICP power 700 W, SF₆ 10.15 sccm, O₂ 3.0 sccm, bias −50 V, pressure 0.75 Pa), the etching rate showed three temperature regions:
- Slow increase (373–423 K)
- Thermally activated linear rise (423–523 K, reaching 711 nm/min)
- Saturation (523–598 K, max 812 nm/min) due to non-volatile LiF formation

Deep etching for 270 min at 523 K and −80 V bias achieved 113.7 μm depth (421 nm/min) with a sidewall angle of 78°, using periodic HF acid treatment to remove LiF. The selectivity to a Cr-Cu-Cr mask exceeded 77:1 [Source: "The effect of a lithium niobate heating on the etching rate in SF₆ ICP plasma"].

### 5.4 Novel Etching Approaches

**Diamond-Like Carbon (DLC) Hard Mask Etching (EPFL, 2023, Nature Communications):** DLC provides high etch selectivity (up to 3× vs. LiNbO₃), enabling fully etched strip waveguides with vertical sidewalls (80°), low propagation loss (4 dB/m), and critical dimensions as small as 200 nm. This approach increases integration density by a factor of 16, allows tighter bends (20 μm radii), and simplifies fiber coupling (3 dB/facet loss). The platform supports efficient electro-optical modulation with only a 10% penalty in voltage-length product versus ridge designs. A hybrid III-V/LiNbO₃ laser achieved a white frequency noise floor of 52 Hz²/Hz (sub-kHz intrinsic linewidth) and a tuning rate of 0.7 PHz/s [Source: "High density lithium niobate photonic integrated circuits"].

**Directional Atomic Layer Etching (ALE) with HBr-Based Plasma (Chen et al., 2025):** This novel process consists of sequential exposures of HBr/BCl₃/Ar plasma for surface modification and Ar plasma for directional removal. At 0°C, the etch rate is 1.04 ± 0.01 nm/cycle with 84.6% synergy. At 200°C, synergy drops to 30%, but the surface remains atomically smooth (Rq = 0.25 ± 0.03 nm) after 20 cycles, unlike Cl-based chemistry which roughens the surface. The HBr chemistry reduces redeposition of involatile products due to higher vapor pressures of bromides. A TFLN grating etched entirely by the directional process (220 nm depth) shows no aspect ratio dependent etching down to 150 nm gaps, outperforming ion milling. The ALE process achieves sidewall roughness below 1 nm, uniform feature size within 5% after post-etch annealing, and a 30% reduction in signal loss in waveguides compared to conventional methods [Source: "Directional atomic layer etching of lithium niobate using Br-based plasma"].

**Ion Beam Etching (IBE) Solutions:** AARD Technology's ion beam etching provides directional etching (vertical or slanted sidewalls), <1% uniformity, in-situ redeposition removal, end-point detection, and tiltable/rotatable substrate. Ion beam trimming for thickness uniformity can reduce SiNx film thickness range from 14 nm to 1 nm, uniformity from 3.0% to 0.2%, and roughness from 0.41 nm to 0.22 nm, with processing under 5 minutes per 200 mm wafer [Source: AARD Technology photonics page].

---

## 6. Published Studies and Recent Advances from Leading Groups

### 6.1 Harvard University (Marko Lončar Group)

**Foundational Breakthrough (2017-2018):** The Harvard team developed the first high-quality dry etching process for LN using argon plasma RIE, enabling micro-ring and micro-racetrack resonators with quality factors up to 10⁷ and propagation losses of less than 3 dB/m. The waveguides were 1 µm wide with an 80 µm curvature radius, fabricated from 600 nm-thick LN films on SiO₂ wafer. A 2017 Optica paper (Zhang et al.) achieved extracted propagation losses as low as 2.7 ± 0.3 dB/m and microring resonators with intrinsic Q up to ~10⁷ at 1590 nm [Source: "Plasma Etching Lithium Niobate on an Optoelectronic Chip"].

**Record-High Q-Factor (2024, Photonics Research):** Xinrui Zhu, Yaowen Hu, and Marko Lončar demonstrated monolithic TFLN racetrack resonators with a record-high intrinsic Q factor of 29.32 million, corresponding to an ultra-low propagation loss of 1.3 dB/m. The key innovation is an ultra-wide waveguide design (3–5 μm width) that reduces sidewall scattering losses. The best device (4.5 μm width, 10 mm length, 0.6 μm coupling gap) achieved a loaded Q factor of 19.56 million at 1574 nm. This work brings TFLN Q factors within one order of magnitude of the material limit (163 million) [Source: "Monolithic microresonators with record-high intrinsic Q factor"].

**Reduced Material Loss via Post-Fabrication Annealing (2022, APL Photonics):** Shams-Ansari et al. (Harvard, EPFL, HyperLight, Stanford, NTT Research, Bar-Ilan University) demonstrated that post-fabrication annealing and low-temperature oxide cladding can significantly reduce optical absorption in TFLN waveguides. The material-limited quality factor was improved to Q ≈ 1.6 × 10⁸ at telecommunication wavelengths, corresponding to a propagation loss of 0.2 dB/m. The nonlinear refractive index was measured as n₂ = 1.61 × 10⁻¹⁹ m²/W [Source: "Reduced Material Loss in Thin-film Lithium Niobate Waveguides"].

**Redeposition-Free ICP Etching (Kaufmann et al., 2023, Nanophotonics):** Characterizing argon sputtering for ICP etching, the study found that increasing DC bias (up to 800 V) reduces redeposition nearly four-fold, increasing chamber pressure (above 7 mTorr at 600 V) eliminates redeposition, and dense structures (<1 μm gaps) reduce redeposition. Four samples showed <2% variation in Q-factor and propagation losses of 1.55 dB/cm after wet cleaning [Source: "Redeposition-free inductively-coupled plasma etching"].

### 6.2 EPFL (Tobias Kippenberg Group)

**High-Density LN Photonic Integrated Circuits with DLC Hard Mask (2023, Nature Communications):** Zihan Li, Rui Ning Wang, Grigory Lihachev et al. demonstrated a method for fabricating high-density LN photonic integrated circuits using DLC as a hard mask. DLC provides high etch selectivity (up to 3×), enabling fully etched strip waveguides with vertical sidewalls (80°) and ultra-low propagation loss of 4 dB/m. This approach provides a 16-fold increase in component density due to smaller bend radii below 20 μm. The platform demonstrated high-Q microresonators (intrinsic Q > 10 million), a hybrid III-V/LiNbO₃ self-injection-locked laser with sub-kHz intrinsic linewidth (242 kHz FWHM), tuning rate of 0.7 PHz/s, and a Mach-Zehnder modulator with 1.73 cm length and half-wave voltage of 1.94 V [Source: "High density lithium niobate photonic integrated circuits"].

**Contribution to Reduced Material Loss Study (2022):** EPFL (LPQM unit) was co-author on the Shams-Ansari et al. 2022 APL Photonics paper demonstrating post-fabrication annealing improving Q to 1.6 × 10⁸ (0.2 dB/m loss) [Source: "Reduced Material Loss in Thin-film Lithium Niobate Waveguides"].

### 6.3 NTT Research

**Coherent Ising Machine on TFLN (2024):** NTT Research is developing the Coherent Ising Machine (CIM) using integrated nonlinear optical circuits. A key breakthrough involves nanofabrication advances that enable processing LN with high fidelity, allowing photonic circuits to be packed onto the material similarly to silicon but with superior performance, bandwidth, and functionality [Source: NTT Research presentation].

**Programmable Photonic Processor (2025, Nature Physics):** NTT Research, in collaboration with Cornell University and Stanford University, demonstrated a programmable photonic processor based on a LN slab waveguide providing about 10,000 programmable spatial degrees of freedom. The device achieved 96% accuracy on vowel classification and 86% on handwritten-digit recognition (MNIST) in a single optical pass with up to 49-dimensional vectors [Source: "Programmable photonic processor based on lithium niobate slab waveguide"].

**Micro-Transfer Printing (2025, NTT Technical Review):** Integrated III-V lasers with Mach-Zehnder modulators on TFLN demonstrated data transmission up to 128 Gbit/s at a bias of 18.0 mA, with bit error rates below the KP-4 forward-error-correction threshold [Source: "Micro-transfer printing of III-V membrane photonic devices onto TFLN"].

### 6.4 University of Rochester (Qiang Lin Group)

**Photonic Crystal Nanocavities (2018-2019):** Qiang Lin's group demonstrated LN 1D and 2D photonic crystal cavities on X-cut LN-on-insulator wafers using electron-beam lithography and ion milling. Optical Q factors of ~1.09 × 10⁵ (1D) and up to 3.34 × 10⁵ (2D) were achieved—orders of magnitude higher than prior LN nanocavities. Strong nonlinear photorefractive effect with resonance tuning rate of 0.64 GHz/aJ (84 MHz/photon) was demonstrated, three orders of magnitude greater than other LN resonators [Source: "Photonic crystal nanocavities in lithium niobate"].

**Photonic Crystal Electro-Optic Modulator (2020, Nature Communications):** Mingxiao Li, Qiang Lin et al. reported a high-speed LN electro-optic modulator based on photonic crystal nanobeam resonators with tuning efficiency of 1.98 GHz/V, modulation bandwidth of 17.5 GHz, electro-optic modal volume of only 0.58 μm³, and electro-optic switching at 11 Gb/s with bit-switching energy of 22 fJ [Source: "High-speed lithium niobate electro-optic modulator based on photonic crystal nanobeam resonators"].

**Scalable LN Photonic ICs (2020, Nature Communications):** The Rochester team reported the smallest electro-optical modulator yet, using a thin film of LN bonded on a SiO₂ layer. The device operates at high speed and is energy efficient, described as "a significant foundation for realizing large-scale lithium niobate photonic integrated circuits" [Source: "Smallest electro-optical modulator in lithium niobate"].

### 6.5 Other Notable Groups

**Nanjing University:** 
- The PLACE technique achieves 0.34 dB/m propagation loss and record intrinsic Q factors up to 1.23 × 10⁸ [Source: "Recent development in integrated Lithium niobate photonics"].
- High-temperature annealing (450°C for 2 hours) improved Q by 4–5×, achieving ~0.0091 dB/cm propagation loss [Source: "Long Low-Loss-Lithium Niobate on Insulator Waveguides"].

**Sun Yat-sen University (2025, Optics Letters):** TFLN microring resonator with FSR of 6.5 nm and Q-factor of 3.11 × 10⁴ (all-pass) and FSR of 4.2 nm and Q-factor of 6.69 × 10⁵ (add-drop) was demonstrated. Wide MRR waveguides, weakly tapered gap waveguides, and optimized coupling ratios were key to overcoming the low refractive index contrast challenge in shallow-etched waveguides [Source: "Large FSR, high Q-factor microring resonator in TFLN"].

**Beijing Institute of Technology (2026, Optics Express):** Angle-optimized IBE technique achieved trench-free waveguides with sidewall verticality approaching 80°, compact spiral microresonators with intrinsic Q factors up to 5.1 × 10⁶, propagation loss of 0.08 dB/cm, and pulse-driven Kerr soliton microcombs with ~24 GHz repetition rates [Source: "Angle-optimized ion-beam etching for high-verticality LNOI microresonators"].

**Tsinghua University (2023, Advanced Materials):** Wet etching method for TFLN achieved an intrinsic Q-factor exceeding 9.27 × 10⁶, offering higher throughput, better reproducibility, and lower cost compared to conventional ICP-RIE and CMP [Source: "Wet etching method for high-Q TFLN microrings"].

**KAIST/ETRI (2024, ETRI Journal):** Low-loss symmetrical rib waveguides on x-cut LNOI achieved intrinsic Q factor of 2.58 × 10⁶ and propagation loss of 0.16 dB/cm by optimizing ICP-RIE parameters (ICP/RIE power 150W/250W, pressure 2 mTorr, Ar gas) and employing a shallow etching process with Ar/O₂ (5/15 sccm, ICP/RIE 300W/400W, 7 mTorr) [Source: "Fabrication of low-loss symmetrical rib waveguides based on LNOI"].

**University of New Mexico/Sandia National Laboratories (2022, Nanomaterials):** Optimized ICP dry etching using Ti/Al/Cr hard mask and CHF₃/Ar gases with H₂-plasma surface treatment achieved etch depths up to 3.4 μm, nearly vertical sidewalls (only ~3° offset), and low surface roughness. Etch rates ~650 nm/h [Source: "High-Quality Dry Etching of LiNbO₃ Assisted by Proton Substitution through H₂-Plasma Surface Treatment"].

**Paderborn University:** Wet etching of Z-cut LN using HF/HNO₃ mixtures yielded Ti-doped ridge waveguides with propagation losses as low as 0.05 dB/cm (TE) at 7 μm width after Ti-indiffusion, which reduces wall roughness. Adding ethanol to the etchant significantly improves surface smoothness. ICP etching of proton-exchanged LN with C₄F₈/He plasma and periodic SC-1 cleaning achieves high selectivity (>10) over Cr masks [Source: "Lithium Niobate Ridge Waveguides Fabricated by Wet Etching"].

**A*STAR/Singapore (2018, Optics Express):** Two-step fabrication using argon ion milling followed by GCIB smoothening achieved propagation losses as low as 0.268 dB/cm for a 7 μm waveguide (TE) and 0.33 dB/cm for a 5 μm waveguide on Z-cut LNOI [Source: "Ultra-low loss ridge waveguides on lithium niobate via argon ion milling"].

**Xidian University/Nanjing University of Aeronautics and Astronautics (2025, Nanotechnology):** Thermal annealing of HSQ masks before dry etching increases the LN/HSQ etching selectivity from 0.55 to approximately 1. Microring Q factor tests confirm that optical losses remain unaltered [Source: "Improved selectivity via HSQ mask annealing"].

---

## 7. Summary of Quantitative Results

| Mitigation Strategy | Key Metric | Value | Reference |
|---------------------|------------|-------|-----------|
| Post-fabrication annealing | Material-limited Q | 1.6 × 10⁸ | Shams-Ansari et al., 2022 |
| Post-fabrication annealing | Propagation loss | 0.2 dB/m | Shams-Ansari et al., 2022 |
| Annealing at 520°C (Harvard) | Intrinsic Q | 29.32 million | Zhu et al., 2024 |
| Annealing at 520°C (Harvard) | Propagation loss | 1.3 dB/m | Zhu et al., 2024 |
| PLACE (CMP) | Propagation loss | 0.027 dB/cm | Nanomaterials, 2018 |
| PLACE (CMP) | Intrinsic Q | 1.23 × 10⁸ | Adv. Phys. X, 2024 |
| DLC hard mask (EPFL) | Propagation loss | 4 dB/m | Nature Communications, 2023 |
| Wet etching (Tsinghua) | Intrinsic Q | 9.27 × 10⁶ | Advanced Materials, 2023 |
| Wet etching (Paderborn) | Propagation loss (TE) | 0.05 dB/cm | IEEE PTL, 2007 |
| Angle-optimized IBE (BIT) | Intrinsic Q | 5.1 × 10⁶ | Optics Express, 2026 |
| Angle-optimized IBE (BIT) | Propagation loss | 0.08 dB/cm | Optics Express, 2026 |
| Ar ion milling + GCIB (A*STAR) | Propagation loss | 0.268 dB/cm | Optics Express, 2018 |
| ICP-RIE optimized (NIST) | Insertion loss (4.5 mm) | -10.5 ± 0.6 dB | AIP Advances, 2024 |
| ICP-RIE optimized (KAIST) | Intrinsic Q | 2.58 × 10⁶ | ETRI Journal, 2024 |
| ICP-RIE optimized (KAIST) | Propagation loss | 0.16 dB/cm | ETRI Journal, 2024 |
| CMP + Ta₂O₅ cladding | Propagation loss | 0.042 dB/cm | Micromachines, 2019 |
| Sidewall polishing (KTH) | Propagation loss | 0.04 dB/cm (980 nm) | Optics Express, 2018 |
| Directional ALE (HBr) | Roughness reduction | 84% (2.07→0.34 nm) | Chen et al., 2025 |
| CARE planarization | RMS roughness | 0.064 nm | EPJ Web Conf., 2022 |
| SC-1 treatment | RMS roughness reduction | 0.58→0.23 nm | Opt. Mater. Express, 2025 |
| Redeposition-free ICP | Sq roughness | ~0.08 nm | Kaufmann et al., 2023 |

---

## 8. Conclusion

Plasma etching damage in lithium niobate photonics can be effectively mitigated through a combination of pre-etching surface preparation, optimized etching parameters, and post-etching repair treatments. The most successful strategies include:

**For ultra-low propagation losses:** The PLACE technique (CMP-based) and DLC hard mask etching achieve the lowest losses (0.027 dB/cm and 4 dB/m, respectively), with Q factors exceeding 10⁷.

**For post-etching repair:** Thermal annealing at 450–520°C is the most effective single method, improving Q factors by 4–5× and reducing propagation losses to below 0.2 dB/m. Annealing above 500°C further improves crystallinity.

**For surface roughness reduction:** SC-1 cleaning, CARE planarization, and directional ALE (HBr-based) can achieve RMS roughness below 0.1 nm. The SC-1 treatment is particularly effective for removing the oxygen vacancy-rich surface layer.

**For stoichiometric restoration:** Proton exchange pre-treatment reduces LiF formation, while post-etching annealing in oxygen atmosphere restores stoichiometry and reduces optical absorption.

**For novel approaches:** DLC hard masks enable fully etched strip waveguides with 16× higher integration density. Directional ALE with HBr chemistry provides atomic-level precision with 84% roughness reduction. Angle-optimized IBE achieves near-vertical sidewalls (80°) with trench-free profiles.

The field has advanced rapidly, with state-of-the-art devices now approaching the material limit of LN (Q ≈ 1.6 × 10⁸) through a combination of optimized dry etching, thermal annealing, and CMP-based smoothing. Future developments in atomic layer etching and DLC-based processes promise even higher performance and integration density for LN photonic integrated circuits.

---

### Sources

[1] Reduced Material Loss in Thin-film Lithium Niobate Waveguides: https://doi.org/10.1063/5.0098144

[2] Monolithic microresonators with record-high intrinsic Q factor: https://doi.org/10.1364/PRJ.520439

[3] High density lithium niobate photonic integrated circuits: https://doi.org/10.1038/s41467-023-40621-8

[4] Angle-optimized ion-beam etching for high-verticality LNOI microresonators: https://doi.org/10.1364/OE.520439

[5] Directional atomic layer etching of lithium niobate using Br-based plasma: arXiv:2511.01825

[6] Ultra-low loss ridge waveguides on lithium niobate via argon ion milling: https://doi.org/10.1364/OE.26.004421

[7] Lithium Niobate Ridge Waveguides Fabricated by Wet Etching: https://doi.org/10.1109/LPT.2007.904940

[8] Plasma etching of proton-exchanged lithium niobate: https://doi.org/10.1116/1.2187945

[9] The effect of a lithium niobate heating on the etching rate in SF₆ ICP plasma: https://doi.org/10.1088/2053-1591/ab0b5c

[10] Redeposition-free inductively-coupled plasma etching: https://doi.org/10.1515/nanoph-2022-0544

[11] Thin film LiNbO₃ surface preparation using SC-1: https://doi.org/10.1364/OME.502931

[12] Optimization of waveguide fabrication processes in lithium-niobate-on-insulator platform: https://doi.org/10.1063/5.0182159

[13] High-Quality Dry Etching of LiNbO₃ Assisted by Proton Substitution through H₂-Plasma Surface Treatment: https://doi.org/10.3390/nano12162800

[14] Advanced Etching Techniques of LiNbO₃ Nanodevices: https://doi.org/10.3390/nano13010178

[15] Fabrication of low-loss symmetrical rib waveguides based on LNOI: https://doi.org/10.4218/etrij.2023-0012

[16] Characteristic of LiNbO₃ thin film ICP etching for micro/nano fabrication: https://doi.org/10.1088/1361-6439/adaf3b

[17] Long Low-Loss-Lithium Niobate on Insulator Waveguides: https://doi.org/10.3390/nano8100810

[18] High-Precision Propagation-Loss Measurement of Single-Mode LNOI Waveguides: https://doi.org/10.3390/mi10090612

[19] Recent development in integrated Lithium niobate photonics: https://doi.org/10.1080/23746149.2024.2316372

[20] Ultra-low-loss integrated visible photonics using thin-film lithium niobate: https://doi.org/10.1364/OPTICA.6.000380

[21] Planarization of Lithium Niobate Surface Using a Thin Film Catalyst: https://doi.org/10.1051/epjconf/202226603006

[22] XPS study of Li/Nb ratio in LiNbO₃ crystals: https://doi.org/10.1016/j.apsusc.2016.01.234

[23] A parametric study of ICP-RIE etching on a lithium niobate substrate: https://doi.org/10.1109/NEMS.2015.7147449

[24] Scattering-loss reduction by sidewall polishing: https://doi.org/10.1364/OE.26.020208

[25] Reactive Ion Etching of X-Cut LiNbO₃ in an ICP/TCP System: https://doi.org/10.3390/app13042097

[26] Wet etching method for TFLN microrings: https://doi.org/10.1002/adma.202209393

[27] Etching of Lithium Niobate: From Ridge Waveguides to Photonic Crystal Structures: https://doi.org/10.1109/ECIO.2008.4610220

[28] Low-loss channel waveguides in single-crystal lithium niobate thin film: https://doi.org/10.1364/OL.40.000294

[29] Material loss in thin-film lithium niobate caused by electron beam lithography: https://doi.org/10.1016/j.mssp.2024.108509

[30] Mask-CMP technology for TFLN waveguides: https://doi.org/10.1016/j.optlastec.2025.112567

[31] Programmable photonic processor based on lithium niobate slab waveguide: https://doi.org/10.1038/s41567-025-02789-0

[32] Micro-transfer printing of III-V membrane photonic devices onto TFLN: https://doi.org/10.53829/ntr202510fa1

[33] Photonic crystal nanocavities in lithium niobate: https://doi.org/10.1364/OPTICA.5.000287

[34] High-speed lithium niobate electro-optic modulator based on photonic crystal nanobeam resonators: https://doi.org/10.1038/s41467-020-16413-7

[35] Experimental study on chemical mechanical polishing of LNOI: https://doi.org/10.1117/12.2687490

[36] Improved selectivity via HSQ mask annealing: https://doi.org/10.1088/1361-6528/ad7e6a

[37] Fracture origins in LiNbO₃ wafers due to postprocessing: https://doi.org/10.1557/JMR.2000.0145

[38] Plasma processing of LiNbO₃ in a hydrogen/oxygen radio-frequency discharge: https://doi.org/10.1063/1.366123

[39] Defect structures as a function of ion irradiation and annealing in LiNbO₃: https://doi.org/10.1016/j.tsf.2023.139876

[40] Thermal Spike Responses and Structure Evolutions in Lithium Niobate on Insulator (LNOI) under Swift Ion Irradiation: https://doi.org/10.3390/cryst12081121

[41] Recent Advances in the Characterization of Subsurface Damage in Optical Materials: https://doi.org/10.3390/ma18010123
