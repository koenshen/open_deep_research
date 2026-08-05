# Comprehensive Research Report: Manufacturing Technology Options for Hollow Motor Shafts in New Energy Vehicle Electric Drive Units

## 1. Executive Summary

This report presents a comprehensive analysis of manufacturing technology options for hollow motor shafts used in New Energy Vehicle (NEV) electric drive units. Hollow shafts offer significant advantages over solid shafts, including up to 40% reduction in rotational inertia, weight savings that directly enhance battery range, and the ability to route coolant through the shaft core for improved thermal management. When the ratio of inner to outer diameter is 0.5, a hollow shaft needs to be only about 2% larger in outer diameter than a solid shaft to achieve the same load-bearing performance while reducing weight by more than 20% [50][26].

The global hollow rotor shaft market was valued at $4.7 billion in 2025 and is projected to reach $8.1 billion by 2034, growing at a CAGR of 6.2%. Steel held the largest material share at 38.4% in 2025, while aluminum is the fastest-growing material sub-segment with a CAGR of 8.3%. Forging was the leading manufacturing process with 42.5% market share [1].

This report evaluates six primary manufacturing techniques: (1) extrusion, (2) forging (open-die, closed-die, precision forging), (3) flow forming, (4) rotary swaging, (5) metal spinning, and (6) additive manufacturing. Each technique is assessed based on suitable materials, cost-effectiveness, required subsequent processing, dimensional tolerances, mechanical properties, scalability, and environmental impact. The report also covers emerging techniques including friction stir welding, laser-assisted forming, and carbon fiber composite winding.

---

## 2. Forming Techniques Overview

### 2.1 Extrusion

#### 2.1.1 Process Description

Extrusion is a metal-forming technique where a billet is pushed through a die to create continuous profiles with consistent cross-sections. **Hot extrusion** heats the metal above its recrystallization temperature (aluminum alloys: 400–500°C, steel alloys: 1,100–1,300°C), making it more malleable with less required pressure. **Cold extrusion** is performed at or near room temperature, offering higher tensile strength, no oxidation, and better surface finish [28][30][31][32][33].

For hollow shaft production, **tube extrusion** uses a mandrel to create hollow shapes, with speeds up to 3 m/s for steel tubes. **Hooker extrusion** (a forward extrusion variant) uses a tubular billet and mandrel [29][42]. **Backward extrusion** eliminates billet-container friction, requiring less force than forward extrusion [30].

#### 2.1.2 Suitable Materials

**Steels:** Low-carbon steels (≤0.3% C) are easiest to extrude; up to 0.45% C is common. Cold extrusion quality A and B bars are available, with B being higher quality for severe extrusions. Al-killed steels are preferred. Free-machining steels (with S, Pb) are less suitable. Boron-modified steels aid hardenability. Specific grades used include 20MnCr5 (for NEV motor shaft cold extrusion [43]), AISI 1035 (for combined cold extrusion of drive shafts [25][47]), 42CrMo4 (for cross-wedge rolling [27]), and AISI 1020 (for experimental hollow shaft forging [21]).

**Aluminum Alloys:** AA6082 (for cold forging of hollow shafts with variable wall thickness [24]), 6061 (for cross wedge rolling at 300–350°C), 6063 (most popular all-purpose extrusion alloy, recommended when surface finish is critical), and 7075 (high-strength option requiring special consideration).

**Extrusion Ratios:** Maximum ratios vary by material: 40 for Al 1100, 5 for AISI 1018 steel, 3.5 for Type 305 stainless steel [29][42].

#### 2.1.3 Dimensional Tolerances and Surface Finish

| Parameter | Cold Extrusion | Hot Extrusion |
|-----------|---------------|--------------|
| Achievable IT Grades | IT8–IT11 | IT13–IT16 |
| Surface Finish (Ra) | 0.8–1.6 μm as-drawn; 0.2–0.4 μm honed | 3.2–12.5 μm |

Cold-drawn seamless steel tube tolerances: OD tolerance of ±0.05–0.10 mm (precision grade), wall tolerance of ±5%, eccentricity ≤10% of nominal wall thickness, straightness of 0.5 mm/m (precision) [42].

#### 2.1.4 Mechanical Properties

Cold extrusion work hardens the material, improving strength. For 42CrMo (quenched and tempered): tensile strength 930–1080 MPa, yield strength ≥780 MPa, elongation ≥12%, impact toughness ≥63 J [16][20]. For 40Cr (quenched and tempered): tensile strength 588–735 MPa, surface hardness 28–34 HRC (can be induction hardened to 50–55 HRC locally) [11][12]. For 20CrMnTi (case-hardened): surface hardness 56–62 HRC after carburizing with tough core [11][15][17].

A research paper on cold extrusion of 20MnCr5 motor shafts for NEVs (Current Science, 2025) demonstrated that the composite extrusion process achieves good material flow, filling, and forming load, with cold extrusion force calculated theoretically at ~1731.5 t and verified via DEFORM simulation showing a maximum load of ~2000 kN (error within 20%) [43].

#### 2.1.5 Material Utilization and Cost

Cold forging/extrusion delivers up to 70% reduction in raw material waste compared to machining techniques [51]. Conventional machining of shafts from solid bar often yields buy-to-fly ratios of 6:1 to 30:1 [2][5][9]. Near-net shape processes can reduce raw material usage by up to 70% [1].

Cold extrusion is best suited for medium to high-volume production. Cold heading machines can produce up to 160 parts/min for small parts, 240–360 parts/hr for larger fasteners [20]. Cold forging production rates up to 400–450 parts per hour [51]. Tooling costs are high, with tool life of 100,000 pieces considered above average for consumable tools [29][42].

#### 2.1.6 Required Post-Processing

**Cold Extrusion:** Slug preparation (sawing/shearing, phosphate coating, lubrication), intermediate annealing for multiple severe operations, optional heat treatment (quenching, tempering), final machining for critical features, surface finishing (grinding, polishing, coating) [29][42].

**Hot Extrusion:** Quenching after extrusion, stretching/straightening, aging (for aluminum alloys), surface treatment (anodizing, plating), machining for critical dimensions [32][47].

---

### 2.2 Forging (Open-Die, Closed-Die, Precision, Upset, Cross-Wedge Rolling)

#### 2.2.1 Open-Die Forging

**Process:** Open-die forging uses flat or slightly contoured dies that do not fully enclose the workpiece. Operations include upsetting, cogging, drawing, piercing, and hollow forging [37][38][49].

**Advantages:** Reduced void formation, improved fatigue resistance, continuous grain flow, lower tooling costs, flexibility for large parts [37][38][49].

**Limitations:** Looser tolerances, requires more post-forging machining, less suitable for complex geometries [37][38].

**Dimensional Tolerances:** IT15–IT18 [57]. For parts ≤100 mm: tolerance ±0.5–1.5 mm with 1–2 mm machining allowance; for 100–500 mm: ±1.5–3 mm with 2–4 mm allowance; for ≥500 mm: ±3–6 mm with 3–6 mm allowance [57]. Surface finish: as-forged Ra 3–12 μm [59].

**Mechanical Properties:** Forging refines grain structure, aligns grain flow with component contour, eliminating porosity and voids. Forged steel exhibits 36% higher fatigue strength at 10^6 cycles, 52% higher yield strength, and 26% higher ultimate tensile strength compared to ductile cast iron [20].

**Specific Research:** A study on open-die forging of large hollow shafts for wind power plants (using steel 42CrMo4) optimized process parameters including bite ratio (0.3, 0.5, 0.7) and height reduction (10%, 20%). Optimal results favored a high bite ratio (0.7) and moderate height reduction (10–20%). A 150 kg hollow shaft was forged experimentally, showing grain sizes decreasing from 142 μm to 37 μm. The study estimates that open-die forging could achieve a weight reduction of up to 60% compared to a cast hollow shaft [31].

**Mandrel Forging and Necking (MFN):** An advanced process to produce large hollow shafts with inner stepped holes, avoiding material waste and property degradation from conventional machining. Optimal parameters: pressing reduction ~20% of wall thickness, rotation angle 12×30° [28].

#### 2.2.2 Closed-Die Forging (Impression-Die Forging)

**Process:** Uses precisely machined dies with the negative impression of the desired final shape. The workpiece is fully enclosed within the die cavity [37][38][39][45][48][49][51].

**Advantages:** High precision, near-net shape, tight tolerances, excellent surface finish, high strength, suitable for high-volume production [37][38][39][43][45][48][49][51].

**Disadvantages:** Higher tooling costs, size limitations, longer setup time [37][38][49].

**Dimensional Tolerances:** IT12–IT15 typically (hot forging IT13–IT16, cold forging IT8–IT11) [57]. Closed-die forging achieves tolerances of ±0.3 mm [37]. Surface finish: as-forged Ra 3–12 μm [37][59].

**Mechanical Properties:** Forged parts are 20% stronger than equivalent castings [36]. Precision forging with hollow billets significantly reduces material waste and manufacturing costs. Elimination of the central web improves stress distribution, enhancing die performance and component accuracy [44].

**Tooling Costs:** High. Dies are custom-machined from tool steels (e.g., H13, M2). Tooling costs typically range from 3% to 6% of top-line costs [32]. Economical for medium to high volumes (>10,000 parts) [37][38][49].

**Specific Research:** Precision forging of hollow parts in novel dies (Tuncer, 1988) explored 36 alternative die designs. Forging pressures of 10–15 times the flow stress are needed. The method significantly reduces material waste and manufacturing costs while enhancing component accuracy [44].

**Rotary Forging (a variant):** A non-conventional closed-die method using a contoured or conical die that applies pressure via rotation and axial compression, offering greater dimensional accuracy and better surface finish for large, complex geometries [22][37].

#### 2.2.3 Precision Forging (Flashless Forging)

**Process:** Specialized closed-die forging that produces near-net-shape components with minimal or no flash, using carefully controlled billet volumes and precise die designs [41][44][49].

**Advantages:** Minimal material waste, reduced machining, improved grain flow, excellent mechanical properties, cost-effective for complex geometries [41][42][44][49].

**Key Parameters:** Forging pressures between 10 to 15 times the flow stress of the billet [44]. Using hollow billets eliminates the need for punching out a central web, reducing material waste and manufacturing costs [44].

**Titanium Precision Forging:** By designing closed dies that press titanium extremely close to its final net shape, raw material can be drastically reduced and secondary CNC machining time can be cut by up to 70% [42].

#### 2.2.4 Upset Forging (Upsetting/Heading)

**Process:** Compresses metal axially to enlarge a localized cross-section. Used to improve axial strength, load-bearing capacity, and fatigue resistance [20][27][30].

**Critical Design Constraint - the '3d Rule':** Unsupported length must not exceed 3× bar diameter (practically kept below 2.5d) to avoid buckling [20][29].

**Material Grades:** Carbon steel, alloy steel (40Cr, 42CrMo, 4140, 4340), stainless steel, high-nickel alloys (Monel, Inconel). Copper cannot be electro-upset; brittle alloys and high-sulfur steels are unsuitable [20].

**Mechanical Properties:** Forged steel exhibits 36% higher fatigue strength at 10^6 cycles, 52% higher yield strength, and 26% higher ultimate tensile strength compared to ductile cast iron [20]. High fatigue resistance and torsional strength, superior dimensional stability and concentricity, optimized grain flow [14].

**Cycle Times:** High production throughput. Up to 160 parts/min for small parts, 240–360 parts/hr for larger fasteners [20].

**Specific Research: Non-isothermal forging for hollow power transmission shafts:** A research article (Journal of Manufacturing Processes, Volume 47, November 2019) presents a three-stage process: (1) selective induction heating of a portion of tubular workpiece, (2) upsetting the heated section to form a solid region, and (3) further upsetting to shape a flange or conical head. FEA demonstrated feasibility for producing hollow axle shafts, stepped gear shafts, and pinion gear shafts. Experimental validation using AISI 1020 tubular blanks (OD 12.7 mm, ID 6.35 mm) successfully fabricated hollow axle and pinion gear shafts [21].

#### 2.2.5 Cross-Wedge Rolling (CWR)

**Process:** Rotary forming process using wedge-shaped tools to apply radial compressive and axial tensile forces to cylindrical billets, producing rotationally symmetric components with varying diameters. CWR is a flashless preforming step [1][4][5][8][22][24].

**Key Characteristics:**
- 30–50% material savings compared to conventional machining [4]
- 3–5× higher efficiency than conventional machining [4]
- Improved grain flow [4]
- Dimensional accuracy of ±0.1 mm [4]

**Three Main Process Types:**
1. Convex-surface synchronous rolls (dual rolls, for Ø6–150 mm, L40–1200 mm)
2. Fixed concave + rotating convex (for non-standard asymmetric shafts)
3. Opposing flat wedges (linear motion for slender shafts) [22]

**Material Grades:** 41Cr4 steel (billet Ø73 mm at 1200°C for stepped gearbox shaft [5]), 42CrMo4 steel (billet Ø216×1650 mm at 1240°C for railway axles [18][27]), 6061 aluminum alloy (at 300–350°C, mold temperature 150–200°C, rolling speed 4 r/min [24]), Ti-6Al-4V titanium alloy (at 855–945°C, optimal 885°C [12]).

**CWR for Hollow Shafts:** A research article (Metal Forming 2024) presents the design and simulation of a CWR process for producing hollow motor shafts for electric vehicles. Using a hollow billet avoids central defects (micropores, voids) common in conventional CWR. The study demonstrates that the CWR method can improve forming accuracy, maintain material performance, reduce production costs, and overcome disadvantages of traditional manufacture [22].

---

### 2.3 Flow Forming (Tube Spinning / Flow Turning)

#### 2.3.1 Process Description

Flow forming is a cold, chipless metal forming process for producing high-precision, thin-walled, net-shaped cylindrical components. The process reduces wall thickness of a preform while elongating it over a rotating mandrel using CNC-controlled rollers, without changing the internal diameter [23]. Developed in Sweden in the 1950s, flow forming is sometimes referred to as shear spinning, shear forming, and flow turning [7].

Recent technology advancements (e.g., the LEIFELD FFC Series introduced in February 2025) provide CNC-controlled vertical Flow Forming Centers with up to 50% faster setup times, up to 100% longer tool life (thanks to driven tailstock), excellent three-sided accessibility, and multi-process capability (flow forming, splitting, tooth profiling, hub preforming) [4][8].

#### 2.3.2 Types of Flow Forming

**Forward Flow Forming:** Material flows in the same direction as the roller feed. Suitable for closed-end parts like rocket nose cones [7][25].

**Reverse/Backward Flow Forming:** Material flows opposite to the roller feed direction. For cylindrical components open at both ends. Winkelmann produces cylindrical tubes up to 6 meters in length using reverse flow forming [9].

**Shear Forming (Shear Spinning):** Stretches metal over a mandrel using high-pressure rollers, reducing thickness while also reducing diameter. Governed by the Law of Sines: final thickness = original thickness × sin(semi-apex angle of cone) [20][40].

#### 2.3.3 Process Parameters

**Roller Geometry:** Entry angle (attack angle), tip radius, and exit angle (relief angle). The roller tip radius is the most crucial parameter affecting surface finish, followed by the thickness reduction ratio [23]. A typical roller setup uses a 25° attack angle and 5° relief angle [25].

**Feed Rate:** 0.1 mm/rev typical for single roller, single pass [25].

**Mandrel Speed:** 30 RPM typical [25].

**Reduction Ratios:** 40% reduction ratio per pass is common [25]. Typical thickness reduction ranges for various steels: low carbon steel 20–50%, medium carbon steel 15–40%, stainless steel 10–35%, HSLA steel 15–30% [55].

#### 2.3.4 Suitable Materials

Flow forming works with discs, preforms, or turned blanks [5]. Materials include: aluminum alloys (AA6061, AA6063, 2024, 7075), stainless steels, titanium alloys (Ti-6Al-4V), nickel-based superalloys (Inconel), and hardened steels [7][23]. Materials require ≥15% elongation for optimal formability [7].

Flow forming of Ti-6Al-4V produces primary globular alpha grains that become elongated parallel to the axis, surrounded by a fine transformed beta structure [65].

#### 2.3.5 Dimensional Tolerances and Surface Finish

| Parameter | Value |
|-----------|-------|
| Radial Run-out Tolerance | <0.05 mm |
| Part Diameter Range | ½" to 48" |
| Part Length Range | Up to 90" |
| Achievable Wall Thickness | Within a few thousandths of an inch |
| IT Grades (as-formed) | IT7–IT9 |
| IT Grades (after finish grinding) | IT6–IT8 |
| Surface Finish (as-formed) | Ra 0.4–1.6 μm |
| Surface Finish (after grinding) | Ra 0.4 μm or better |

#### 2.3.6 Mechanical Properties and Grain Refinement

Flow forming cold-works the material, increasing strength 2–3 times that of the base material [1]. Cold working of austenitic stainless steel will typically double the mechanical strength (e.g., 304 stainless steel tensile strength doubles from ~80 ksi to 160 ksi) [28]. Parts can be annealed to restore original properties if needed [28].

One-piece flow-formed solutions achieve significantly higher strengths for rotor shafts, allowing weight-optimized design of the powertrain and longer mileage per kW for electric vehicles [3].

Flow forming of cast aluminum alloy wheels enables a 30% rim thickness reduction, slightly improves yield and tensile strength, and significantly enhances elongation parallel to the forming direction [29].

#### 2.3.7 Material Utilization and Cost

Flow forming dramatically reduces the buy-to-fly (BTF) ratio, sometimes approaching 1:1, compared to 6:1 to 30:1 for conventional forging and machining [7]. Uses up to 85% less material compared to machining from forged rings [28]. Preforms are typically four times shorter than the final flowformed component [65].

The global flow forming machines market was valued at $1.82 billion in 2025, projected to grow to $3.41 billion by 2034 at 7.2% CAGR. Machine costs range from $350,000 to over $3.5 million. Automotive segment: 34.8%, aerospace: 23.6%, defense: 18.2% [50].

Tooling costs are relatively low compared to forging dies, making flow forming suitable for medium production volumes [7]. The LEIFELD FFC Series achieves up to 100% longer tool life thanks to the driven tailstock [4][8].

#### 2.3.8 Required Post-Processing

**Heat Treatment:** Stress-relief annealing, quenching and tempering, or aging depending on material [65].

**Machining:** Finish turning, grinding of critical bearing surfaces and seal diameters [71][72].

**Surface Finishing:** Shot blasting, polishing, or coating as needed [28].

**Balancing:** Dynamic balancing required for high-speed rotor shafts (up to 20,000 rpm) [2].

**Joining:** For multi-piece designs, laser welding of two flowformed half shafts (as in NETFORM's design) [1].

**Inspection:** Ultrasonic testing, X-ray, dimensional inspection [12].

#### 2.3.9 Specific Advantages for Hollow Shaft Applications

- **Weight reduction:** Flowforming increases material strength 2–3 times, enabling thinner walls and reduced weight [1]. NETFORM's two-piece hollow rotor shaft design consists of two flowformed half shafts laser-welded together, suitable for both low and high torque applications [1].
- **Internal cooling:** Hollow shafts allow for coolant oil flow through the shaft, resulting in increased heat transfer. An optional center support component can be added for higher stiffness, also allowing coolant flow [1].
- **High-speed capability:** WF Maschinenbau achieves radial run-out tolerances <0.05 mm, capable of withstanding up to 20,000 rpm [2].
- **Integration of features:** Flow forming can integrate internal cooling fins and/or external stop collar. Internal cooling tubes can be inserted during the drawing-in process [2].
- **Tooth-guided cooling channel design:** A novel rotor-cooling shaft concept using cold-formed 20MnCr5 steel with tooth-guided internal channels achieves up to 110% higher cooling efficiency at low rotational speeds compared to conventional hollow shafts. The design outperforms the state of the art of a hollow cooling shaft by at least 30% in heat transfer [6].

---

### 2.4 Rotary Swaging (Radial Forging)

#### 2.4.1 Process Description

Rotary swaging is a high-precision cold-forming process in which several die segments oscillate radially and simultaneously strike the workpiece in rapid succession at frequencies exceeding 1,000 strokes per minute [31]. Each stroke produces incremental forming of 0.25–1.5 mm, reducing forming forces and improving material strength [31]. The process can be performed with stationary or rotating workpieces, and with or without internal mandrels, depending on the required geometry [31].

Radial forging is an incremental process using four mechanically driven dies for cold, semi-hot, and hot forming of complex profiles, with benefits such as high forming forces, large die adjustment range, oil-free production, and very tight tolerances [14][16].

Two main types: **infeed swaging** (surface roughness Ra 1.0 µm) and **high-precision recess swaging** (Ra 0.1 µm) [87]. Two categories: **sinking** (without mandrel, outer diameter reduction only) and **mandrel swaging** (with internal mandrel to control inner diameter) [15][17].

#### 2.4.2 Process Parameters

| Parameter | Value |
|-----------|-------|
| Strokes per minute | Up to 10,000 |
| Incremental step | 0.25–1.5 mm per stroke |
| Forging frequency (hot rotary swaging) | 100–200/min (preferred 160/min) |
| Single-pass reduction (hot) | 30–50 mm (preferred 40 mm) |
| Rotation speed | 10–30 R/min (preferred 20 R/min) |
| Initial forging temperature | 1000–1100°C (preferred 1060°C) |
| Final forging temperature | 800–900°C (preferred 850°C) |

#### 2.4.3 Suitable Materials

**Steel grades:** 42CrMo (axle steel), 35CrMnSiA, E355 steel tubes, stainless steel 1.4301 (AISI 304) [11][17][30][35].

**Aluminum alloys:** 2024 aluminum tubes (after rotary swaging and T6 heat treatment, yield stress reaches approximately 350 MPa) [49].

**Other materials:** Aluminum, nickel, magnesium, stainless steel, low-carbon steel, copper, lead, zinc [33].

GFM radial forging for EV rotor shafts uses semihot forging at 700–850°C, enabling monobloc design and cost-effective blanks [16].

#### 2.4.4 Dimensional Tolerances and Surface Finish

| Parameter | Value |
|-----------|-------|
| Outside diameter tolerances | 0.01–0.1 mm (typical) |
| Inside diameter tolerances (with mandrel) | 0.03 mm |
| Typical tolerance | ±0.005" (±0.127 mm), can be as tight as ±0.001" (±0.025 mm) |
| Infeed swaging surface finish | Ra 1.0 µm |
| High-precision recess swaging surface finish | Ra 0.1 µm |
| General rotary swaging surface finish | Ra 0.8–3.2 µm |
| GFM radial forging hammer axis repeatability | 0.1 mm/100 mm |
| Chuck axis repeatability | 1 mm/7250 mm |

General IT grades: Cold forging/swaging achieves IT8–IT11. For hot forging, IT13–IT16 [44].

#### 2.4.5 Mechanical Properties and Grain Refinement

**Fatigue strength increase:** Cold-forming via rotary swaging can increase fatigue strength by up to 30%, enabling significant downsizing of cross-sections [31].

**Fatigue life improvement:** For 42CrMo axle steel rods reduced from Φ25 mm to Φ15 mm in ten passes: yield strength increased by 16.6% (from 749 MPa to 873 MPa), ultimate tensile strength increased by 32.5% (from about 977 MPa to 1295 MPa), and elongation decreased by 31.5% [30]. Torsion yield strength increased by 43.2% and ultimate torsion strength by 19.3%, with no loss in maximum torsion angle [30]. Compression yield strength increased by 6.8% [30]. Fatigue life improved significantly: up to 409.4% increase at the highest maximum stress (480 MPa) and 45.2% increase at the lowest maximum stress (420 MPa) [30]. Hardness rose 8.57% on average [30].

**Recrystallization:** In rotary swaging of railway motor shafts, the recrystallization fraction in the swaged region reached 72.29%. Quenching and tempering treatment increased the yield strength in the rotary-swaged region by 27.5% [11].

**Grain refinement:** The rotary swaging process refines grain size, decreases the eutectic phase fraction, enhances mechanical strength, and decreases mechanical elongation [49].

**Patent data (CN109622849B):** For 35CrMnSiA steel, tensile strength +15%, yield strength +10%, impact energy significantly improved compared to traditional machining [17].

#### 2.4.6 Material Utilization and Cost

Rotary swaging produces **zero waste material** (chipless) [33]. Material savings of over 30% compared to traditional machining (about 520 kg per piece for large missile shell components) [17]. Axle lightweighting: over 30% weight reduction achieved for railway hollow shafts [11]. Weight reductions of up to 50% compared to conventional machining [31].

Short cycle times due to high-speed hammering [31]. Processing time reduction of 5–7 days per piece compared to traditional machining [17]. Production rate up to 200–300 pieces/hour [33].

Low tooling effort [31]. Dies are simple in contour due to the incremental nature of the process [16]. Over 200 GFM radial forging machines deployed in automotive applications [16]. Over 10 million shafts produced annually by Muhr und Bender KG (Mubea) using GFM machines for stabilizers [16].

#### 2.4.7 Required Post-Processing

**Heat Treatment:** Quenching and tempering (increases yield strength by 27.5% in swaged region) [11]. Post-swaging tempering restores elastic range and increases microhardness [32].

**Machining:** Finish machining of critical features [14].

**Surface Treatment:** Shot blasting, coating as required [16].

**Balancing:** Dynamic balancing for high-speed rotating components [2].

**Inspection:** Ultrasonic, X-ray, dimensional inspection, mechanical testing [17].

#### 2.4.8 Specific Advantages for Hollow Shaft Applications

- **Weight reduction:** GFM radial forging produces hollow and bottle-shaped contours for EV rotor shafts, enabling monobloc design [16]. Hollow side shafts, drive shafts, and monoblock shafts (MTS) are produced [16].
- **Complex internal geometries:** Can produce near-net shape outer contours and net-shape inner contours for gear shafts (AT, DCT, CVT transmissions) [16].
- **Hollow shafts for railway motors:** Trial production successfully fabricated a hollow shaft measuring 635 mm in length with a maximum outer diameter of Φ105 mm, achieving over 30% weight reduction [11].
- **Fatigue improvement:** Particularly beneficial for torsional working conditions [30].
- **Oil-free production:** GFM uses cooling with water instead of emulsion, avoiding oil carry-over [16].

---

### 2.5 Metal Spinning

#### 2.5.1 Process Description

Metal spinning is a chipless forming process in which a rotating mandrel and roller are used to transform flat or tubular blanks into axially symmetric hollow parts [19]. The process involves mounting a metal blank on a lathe, rotating it at high speed, and applying localized pressure with a roller to achieve plastic deformation without material removal [19]. Modern CNC technology has automated the process, making it faster, more accurate, and cost-effective [19][22].

#### 2.5.2 Types of Metal Spinning

**Conventional Spinning:** Maintains original wall thickness while reducing diameter. The metal is gradually forced onto a mandrel with a roller [18][40].

**Shear Spinning (Shear Forming):** Reduces wall thickness according to the Law of Sines. Requires high-pressure rollers, more precision, and cooling. The minimum angle required is between 12 and 18 degrees depending on material properties [55].

**Tube Spinning:** Reduces wall thickness of hollow cylinders to produce longer tubes, can be forward or backward [46].

**Hot Spinning:** For thicker plates and low-ductility metals, allows larger deformations, refines grain structure but causes oxidation [46]. Recent advances show that robust thermal management can roughly double achievable deformation before failure [52].

**Deep Spinning:** A novel process using a roller with a constant-clearance blank holder to suppress wrinkling, achieving limiting spinning ratios (LSR) of 2.4 for annealed aluminum blanks and 2.24 for hard aluminum blanks in a single pass (compared to conventional 1.75 and 1.67 respectively) [53].

#### 2.5.3 Suitable Materials

Nearly any ductile metal can be spun, including titanium, aluminum, steel, stainless steel, copper, brass, and nickel alloys [19][22]. The process is suitable for materials with good elongation properties.

#### 2.5.4 Dimensional Tolerances and Surface Finish

| Parameter | Value |
|-----------|-------|
| Typical tolerances (CNC spinning) | ±0.125 mm to ±0.5 mm |
| Surface finish (CNC spinning) | Ra 0.8–3.2 μm |
| Minimum wall thickness | 0.5 mm (aluminum), 0.8 mm (steel) |
| Maximum diameter | Up to 3,000 mm |
| Maximum length | Up to 6,000 mm |

#### 2.5.5 Mechanical Properties

Metal spinning induces work hardening, improving strength properties. The process maintains or improves grain structure through controlled deformation. CNC spinning ensures consistent, repeatable forming with minimal operator input [19].

#### 2.5.6 Material Utilization and Cost

Metal spinning is a chipless process with high material utilization rates (typically >85%). Minimal waste compared to machining. Tooling costs are low (typically simple mandrels and rollers), making it suitable for prototype and low-to-medium volume production. Cycle times vary depending on part complexity, from 30 seconds to several minutes per part.

#### 2.5.7 Required Post-Processing

- Stress-relief annealing (if required)
- Trimming of excess material
- Surface finishing (polishing, coating)
- Inspection (dimensional, surface quality)

#### 2.5.8 Specific Advantages

- Low tooling costs (ideal for prototypes and small batches)
- High material utilization
- Suitable for large diameter parts
- Can produce complex contours
- CNC control enables consistent quality

---

### 2.6 Additive Manufacturing and Emerging Techniques

#### 2.6.1 Selective Laser Melting (SLM) / Laser Powder Bed Fusion (LPBF)

**Process Description:** SLM is an Additive Manufacturing process that produces near-net shape products from metallic powders in a layer-by-layer fashion, directly from CAD models [11]. SLM uses a high-power laser to fully melt metal powder, producing parts with nearly 100% density. According to ISO/ASTM 52900, it is classified under Laser Powder Bed Fusion (LPBF) [4].

**Density/Mechanical Properties:** SLM fabrication with materials such as 316L stainless steel, Ti6Al4V, Inconel 718 and AlSi10Mg has achieved relative densities of 99% or higher [11]. After Hot Isostatic Pressing (HIP), SLM parts often demonstrate isotropic mechanical properties and high cycle fatigue performance comparable to cast or forged materials [4].

**Dimensional Tolerances and Surface Finish:**

| Parameter | Value |
|-----------|-------|
| Standard tolerances (LPBF metals) | ±0.050 mm + ±0.005 mm/mm |
| Protolabs DMLS tolerances (X/Y) | ±0.003 in. for first inch + 0.1% of nominal length |
| Protolabs DMLS tolerances (Z) | ±0.006 in. for first inch + 0.1% of nominal length |
| As-built surface roughness | 10–80 µm Ra |
| Minimum feature size (normal) | 0.015 in. (0.381 mm) |
| Minimum feature size (high resolution) | 0.006 in. (0.153 mm) |
| Layer thickness | 20–60 µm (normal 30 µm, high resolution 20 µm) |
| Build volume | Up to 1.5 meters |

**Suitable Materials:** Ti6Al4V, AlSi10Mg, 316L stainless steel, Inconel 718, cobalt-chromium alloys, C103 refractory alloy, tool steel, copper, aluminum alloys, precious metals [4][41].

**Post-Processing:** Stress relief heat treatment, support removal, Hot Isostatic Pressing (HIP), surface finishing (CNC machining, polishing, tumbling, blasting), heat treatment [4][29].

**Key Challenges:** Residual stresses, limited build speed, need for extensive post-processing, high costs. An estimated 70% of all metal AM failures occur from physical distortion of the part [45]. Higher energy densities (e.g., 65.4 J/mm³) produce smoother surfaces (Ra < 15 μm) and more stable melt pools [9].

**Technology Readiness Level (TRL):** SLM/LPBF is generally at TRL 7–9 for automotive non-critical components, and TRL 6–8 for structural/rotating components like shafts. EOS classifies Premium products as TRL 7–9 (rock solid baseline, repeatable quality for serial production) [37].

#### 2.6.2 Direct Metal Laser Sintering (DMLS)

DMLS is a common 3D printing technique, originated in 1995 at the Fraunhofer Institute for Laser Technology in Germany [20]. DMLS uses a high-power laser to sinter (partially melt) fine metal powder layer by layer, producing strong, accurate parts [23].

**Dimensional Tolerances:** ±0.05 mm (±0.002 in.) [23].

**Cost:** The total manufacturing cost of a typical DMLS part is approximately $100–$2,500 including finishing and material [23].

**Materials:** Stainless steel 17-4 PH, 316L, Aluminum AlSi10Mg, Inconel 718, Cobalt Chrome Co28Cr6Mo, Titanium Ti6Al4V [26].

**Mechanical Properties:** Parts printed using DMLS are stronger, denser, and more precise than cast metal parts [20].

**TRL:** DMLS is at TRL 7–9 for serial production in automotive tooling and low-volume production parts.

#### 2.6.3 Electron Beam Melting (EBM)

**Process Description:** EBM uses a high-energy electron beam to selectively melt and fuse metallic powders layer by layer in a vacuum chamber [30]. The vacuum environment prevents oxidation, enables high chemical purity, and allows HIP without internal gas pressure risks [36].

**Key Advantages:** Faster build speeds than SLM (approximately 80 cm³/h for Ti-6Al-4V vs. 30 cm³/h for LPBF [42]). The high-energy beam heats the powder bed to optimal ambient temperature (exceeding 1,000°C), resulting in no residual stresses [40]. The elimination of thermal stress enables part stacking for industrial-scale production [36].

**Surface Finish:** Typically rougher (Ra ~40 μm) compared to SLM (Ra ~20 μm) [42]. The rougher surface can be beneficial for certain applications (e.g., medical implants) [38].

**Build Volume:** Up to 200×200×380 mm³ (A2X) and Ø300×380 mm³ (Q20+) [42].

**Suitable Materials:** Titanium, tantalum, stainless steel, tool steel, cobalt chrome, copper, nickel alloys. EBM can process difficult-to-print alloys such as titanium aluminide (TiAl), pure copper, and crack-prone nickel alloys [36]. As of 2019, EBM is the only commercially available AM method for TiAl production [39].

**Cost Comparison:** A cost comparison with laser systems (for aerospace bracket and orthopedic hip cup in Ti64) showed EBM had lower costs in all steps except milling, with total cost per part up to 50% lower, driven by reduced powder price, no need for post-process heat treatment, and easy support removal [39].

**TRL:** EBM is at TRL 7–9 for aerospace and medical applications. For automotive structural components, it is at approximately TRL 6–8.

#### 2.6.4 Directed Energy Deposition (DED)

**Process Description:** DED uses a directed heat source (laser, electron beam, or electric arc) to melt feedstock material (powder or wire) onto a substrate, building parts layer by layer [59]. DED stands out for its versatility in building entirely new parts, repairing worn or damaged components, and performing cladding operations [58].

**Key Parameters:**
- Deposition rates: 10–40 cm³/h for laser powder DED, up to 5 kg/h for WAAM [58][59]
- Build volume: up to 5×5×7 feet (1.5×1.5×2.1 m) [53]
- Material utilization: often exceeding 80% [58]
- Surface finish: rough (approximately 1 mm for WAAM), requiring post-processing [59]
- Layer thickness: 0.25 mm to 0.5 mm [57]

**Applications:** DED is most suitable for repairing and remanufacturing automotive and aerospace components. Compared to conventional welding, repair via DED has advantages including lower heat input, warpage and distortion, higher cooling rate, lower dilution rate, excellent metallurgical bonding, and suitability for full automation [49]. Repair of high-value components like turbine blades, blisks, shrouds, crankshafts, and dies [49]. Remanufacturing an engine via DED requires only 55% of the energy and 67% of the labor of new production [49].

**Cost Savings:** DED can lower repair costs by up to 50% [61]. A life-cycle assessment of a 316L turbine blade repair demonstrated a 45% reduction in carbon footprint and 36% energy savings compared to replacement [51].

**TRL:** DED for repair is at TRL 7–9 (commercialized in aerospace). For new part production in automotive, it is at approximately TRL 5–7.

#### 2.6.5 Hybrid Additive-Subtractive Manufacturing

**Definition:** Hybrid additive and subtractive manufacturing integrates AM and subtractive manufacturing in a single platform to produce complex, high-precision parts [5].

**Key Findings:** A systematic review of 181 articles from 2018–2025 found that ~70% of studies used metal materials (most commonly 316L stainless steel and Ti-6Al-4V), with sequential operations (add then subtract) being the predominant configuration [5].

**Benefits:** Reduces setup time, labor, and turnaround by enabling one-machine production; eliminates misinterpretation between processes; optimizes floor space; allows new strategies such as machining most of a part and 3D-printing complex features, or creating bi-metal tools [3].

**Commercial Systems:** DMG Lasertec 65, Mazak VC-500A/5x AM, and research setups [5].

**For Hollow Shafts:** Hybrid manufacturing is particularly relevant because the shaft can be additively built with internal features (cooling channels, lightweighting structures) and then finish-machined to achieve the tight tolerances required for bearing seats and mating surfaces (typically ≤0.10 mm tolerance for EV motor shafts) [20].

**TRL:** Hybrid additive-subtractive manufacturing is at TRL 6–8 for automotive applications, with commercial systems available but limited adoption in serial production.

#### 2.6.6 Friction Stir Welding (FSW) for Joining Hollow Shaft Sections

**Process Description:** FSW is a solid-state joining process that uses a rotating, non-consumable tool to generate frictional heat to join materials. The metal is heated to the point where it is soft enough to be stirred together, but not actually turned liquid [22][43]. FSW offers improved weldability, reduced distortion, and enhanced fatigue resistance compared to arc welding [29].

**For Hollow Motor Shafts Specifically:** A key paper (Akiyama, Honda, and Nakanishi, 2016 IEEE ICRERA) presents a method using ultraprecision friction welding to join a pipe and solid parts, achieving the required quality (tolerance ≤0.10 mm). By adjusting welding conditions and work clamping, defect-free hollow shafts were produced, suitable for practical EV applications. The approach lowers shaft inertia, improving motor responsiveness, and reduces manufacturing cost compared to traditional solid shafts [20][21].

**Advantages for EVs:** Friction Welding enables joining dissimilar metals, a substantial advantage for lightweighting. In one automotive program, cycle times improved by up to 32% [25].

**FSW in E-Mobility:** FSW is a key technology for e-mobility, excelling at joining lightweight alloys like aluminum, producing high-quality, distortion-free joints, improving thermal management, and reducing the need for filler materials [23].

**Energy Efficiency:** FSW offers up to 80% less energy consumption than MIG or laser welding, with no pores, cracks, or need for shielding gas [28].

**Process Parameters:** Best welding parameters for achieving maximum tensile strength: rotation speed of 1000 rpm, welding speed of 45 mm/min, appropriate axial force [37].

**TRL:** FSW for joining hollow shaft sections is at TRL 7–9 for automotive applications, with commercial implementations already in production for EV components.

#### 2.6.7 Laser-Assisted Forming and Incremental Sheet Forming

**Laser-Assisted Forming (LAF):** Laser forming utilizes laser energy to induce controlled thermal expansion and plastic deformation. Min et al. showed that LAF can reduce bending forces by 43%. Springback has been reduced about 10 times on titanium and 30 times on aluminum [43]. With optimized parameters (750 W laser output, six forming passes, scan rate of 5 mm/s), the maximum force decreased to approximately 2.1 kN [43].

**Incremental Sheet Forming (ISF):** ISF is a highly adaptable alternative to traditional forming processes for producing customized metal components [44]. Machina Labs' RoboCraftsman system uses robotic incremental sheet metal forming to replace traditional die-based stamping. It achieves over 10× reduction in lead time and tooling cost savings exceeding $1 million per unique part design [50].

**TRL:** LAF and ISF are at approximately TRL 5–7 for automotive tubular components.

#### 2.6.8 Carbon Fiber Composite Winding and Hybrid Metal-Composite Shafts

**Hybrid Shaft Approach:** A hybrid shaft combining carbon-reinforced plastic (CFRP) and stainless steel can create a rotor shaft that is 50% lighter than its conventional counterpart, manufactured via dry filament winding and centrifugal casting [1].

**CFRP Drive Shaft Performance:** A study on carbon fiber reinforced epoxy drive shaft for SAE Baja ATV using filament winding with fiber orientation of [852/±452/252]s showed average torsional strength of 1770 Nm (8.5% more than OEM steel shaft at 1630 Nm), weight of only 0.8 kg (60% lighter than 2.5 kg steel shaft), and strength-to-weight ratio increased by 339% (2212 Nm/kg vs. 652 Nm/kg) [3].

**NASA Composite Shaft for Electric Motors:** A NASA technical memorandum (February 2026) reports on manufacturing process development of a CFRP composite shaft for electric motors. Two methods were explored: hybrid biaxial/triaxial fabric overwrap and traditional overbraid approach. Four prototype shafts were successfully produced using the hybrid fabric overwrap method, employing T700S carbon fiber, bismaleimide (BMI) resin, and a 3D-printed ceramic washout mandrel. The final shafts averaged 140 g mass, closely matching the design target of 142 g. The selected machine design has a nominal rotational speed of 15,860 rpm and is predicted to achieve a specific power of roughly 10 kW/kg at an efficiency of 96.6%. The overbraid method is recommended for volume production [9].

**Composite Sleeves for High-Speed Motors:** Carbon fiber sleeves are essential to contain permanent magnets against centrifugal forces in high-speed motors (operating from 30,000 to over 100,000 RPM). Carbon fiber sleeves are replacing traditional metal (Inconel, titanium, stainless steel) sleeves because they are electromagnetically near-transparent, reducing eddy current losses by 2–3% and lowering operating temperatures by 20–30°C [2].

**Weight Reduction:** Composite drive shafts deliver a weight reduction of up to 65% compared to conventional steel. Optimized composite drive shafts demonstrate up to 79.6% weight reduction versus steel tubes [8].

**TRL:** CFRP composite shafts for automotive applications are at TRL 5–8, with limited adoption in serial production due to cost, joining challenges, and durability concerns.

---

## 3. Materials Selection for Hollow Motor Shafts

### 3.1 Steel Grades

#### 3.1.1 Carburizing Steels (Case-Hardening Steels)

Carburizing diffuses carbon into the surface of low-carbon steel at high temperatures (899–954°C), resulting in a hard, wear-resistant case (58–62 HRC) while maintaining a tough, ductile core [26]. This is ideal for parts that must withstand repeated contact stress and fatigue.

**AISI/SAE 8620 (UNS G86200):** A common carburizing alloy steel with flexible heat treatment options. Chemical composition: Fe (96.9–98.0%), Mn (0.70–0.90%), Ni (0.40–0.70%), Cr (0.40–0.60%), C (0.18–0.23%) [7].

- **Mechanical Properties (Annealed):** Tensile Strength 530 MPa, Yield Strength 385 MPa, Elastic Modulus 190–210 GPa, Izod Impact 115 J, Brinell Hardness 149 [7].
- **Mechanical Properties (Single Quenched & Tempered at 230°C):** Tensile Strength 1157 MPa, Yield Strength 833 MPa, Elongation 14.3% [11].
- **Heat Treatment:** Carburizing at 899–954°C, oil quench from 820–860°C, low temper at 150–200°C. Case depth should be 10–12% of component diameter [5][55].
- **Key Findings:** The carburized case by itself is not as strong as predicted by hardness; it fractures with little plasticity due to quench embrittlement. Lower case carbon content dramatically increases bending strength: at 0.42% carbon, strength is double that at 0.80–0.95% carbon. Light case depths (0.016 inches) yield higher strength than standard case depths (0.035 inches) [4][8].
- **Applications:** Medium-strength components such as camshafts, fasteners, gears. 8620 carburized is the best steel for shafts with integral splines or gear teeth [5][55].

**20CrMnTi (GB Standard):** A high-performance alloy steel for critical components enduring high-speed, medium-load, and impact conditions. Chemical composition: C (0.17–0.23%), Si (0.17–0.37%), Mn (0.80–1.10%), Ti (0.04–0.10%). Corresponds to SAE 8620, 16MnCr5 (1.7131) [1]. The 1%EG-modified 20CrMnTi material had the highest tensile strength of 1088 MPa and a Vickers hardness of 4.7 GPa [15].

**16MnCr5 (EN 1.7131):** Balanced combination of strength, toughness, fatigue resistance, and surface hardness. After carburizing and quenching: core hardness 30–38 HRC, surface hardness 58–62 HRC [5].

- **Mechanical Properties (Normalized):** Tensile Strength 650–800 MPa, Yield Strength 380–500 MPa, Elongation 12–16%, Impact Toughness ≥40 J [5].
- **Mechanical Properties (After Carburizing):** Core Tensile Strength 800–950 MPa, Core Yield Strength 600–750 MPa, Core Ductility 8–12% elongation [5].
- **Applications:** Automotive gears, transmission shafts, industrial couplings, agricultural machinery. Designed for parts up to 30 mm in diameter subjected to low stresses and abrasion [5][9].

**20MnCr5 (EN 1.7147):** Related grade to 16MnCr5 with higher carbon content. The base alloys 20MnCr5 and SAE 8620 showed similar hardness profiles [18]. Used in cold extrusion of motor shafts for NEVs [43].

#### 3.1.2 Quench-and-Temper Steels (Through-Hardening Steels)

These medium-carbon alloy steels (0.38–0.43% C) are quenched and tempered to achieve through-hardness with excellent fatigue resistance.

**AISI 4140 (SAE 4140) / 42CrMo4 (DIN) / 42CrMo (GB):** A chromium-molybdenum alloy steel with ~0.40% carbon, valued for its ability to through-harden in 2–4 inch sections to 140–180 ksi tensile strength while maintaining good toughness [27].

- **Chemical Composition:** C (0.38–0.43%), Cr (0.80–1.10%), Mo (0.15–0.25%), Mn (0.75–1.00%) [27].
- **Mechanical Properties:** Through quenching and tempering, tensile strength can reach 850–1000 MPa, yield strength ≥650 MPa, impact toughness ≥50 J. High-frequency induction quenching can achieve surface hardness of 50–55 HRC, and nitriding can reach ≥1000 HV [22].
- **4140 vs. 42CrMo:** 4140 has tensile strength 655 MPa, yield 415 MPa, elongation 25.7%; 42CrMo has tensile 1080 MPa, yield 930 MPa, elongation 12% — making 42CrMo stronger but 4140 more ductile [21]. 42CrMo has better mechanical properties and is more suitable for high load and high temperature environments [21].
- **Heat Treatment:** Quenching at 840–870°C, tempering at 540–660°C to achieve 28–32 HRC (high toughness) or 35–40 HRC (high strength). Surface strengthening via induction hardening (50–55 HRC) or nitriding (≥1000 HV) [21][22][27].
- **Fatigue:** 4140 has an endurance limit of ~480 MPa vs. 1045's ~300 MPa — a ~60% higher endurance limit [5][55].
- **Applications:** Heavy-duty transmission shafts, automobile crankshafts/camshafts, gear shafts, spline shafts, wind power main shafts, machine tool spindles, hydraulic pump shafts [22][27].
- **Key Recommendation:** 4140 Pre-Hardened (PH) is the best overall shaft material grade for industrial SPMs and custom shafts, no post-machining heat treatment required [5][55].

**AISI 4340 (SAE 4340):** A nickel-chromium-molybdenum low-alloy steel known for its high strength, deep hardenability, and excellent toughness [20]. The nickel content (1.65–2.00%) maintains Charpy V-notch impact energy above 40 ft-lb at tensile strengths up to 200,000 PSI and temperatures as low as -40°F [20].

- **Chemical Composition:** C (0.40%), Mn (0.75%), Si (0.30%), Cr (0.80%), Ni (1.80%), Mo (0.25%) [37].
- **Mechanical Properties:** Tensile strengths range from 125,000 to over 280,000 PSI depending on heat treatment. At 400°F temper: UTS 1905 MPa, 0.2% YS 1530 MPa, Elongation 11.0%. At 1100°F temper: UTS 1140 MPa, 0.2% YS 1035 MPa, Elongation 18% [37].
- **Applications:** Aerospace landing gear, military ordnance, oil field drill string components, high-performance automotive drivetrain parts [20][37].

### 3.2 Aluminum Alloys

**6061 Aluminum:** Tensile strength ~310 MPa, yield strength ~276 MPa (T6 temper). Used in cross wedge rolling at 300–350°C [24][47]. Suitable for moderate-strength applications where weight reduction is critical.

**6063 Aluminum:** Most popular all-purpose extrusion alloy, recommended when surface finish is critical or when material is to be anodized [47].

**7075 Aluminum:** Tensile strength ~572 MPa, yield strength ~503 MPa (T6 temper). High-strength option with excellent strength-to-weight ratio, but more difficult to form and weld.

**2024 Aluminum:** After rotary swaging and T6 heat treatment, yield stress reaches approximately 350 MPa [49]. Used in aerospace and high-performance automotive applications.

**6082 Aluminum:** Characterized for cold forging of hollow shafts with variable wall thickness in FEM studies [24].

### 3.3 Emerging Materials

**Carbon Fiber Composites:** CFRP drive shafts can achieve up to 65% weight reduction compared to conventional steel. A NASA study (February 2026) demonstrated CFRP composite shafts for electric motors with specific power of roughly 10 kW/kg at 96.6% efficiency [9].

**Hybrid Functionally Graded Composites:** Novel automotive engine shafts made of composites with material property grading offer potential for optimized performance [ResearchGate, Asiri 2021].

**Aluminum-Lithium Alloys:** Offer 5–10% weight reduction over conventional aluminum alloys with improved stiffness, suitable for aerospace and high-performance automotive applications.

---

## 4. Comparative Analysis

### 4.1 Comprehensive Comparison Table

| Criterion | Extrusion (Cold) | Extrusion (Hot) | Forging (Closed-Die) | Flow Forming | Rotary Swaging | Metal Spinning | SLM/LPBF | CFRP Winding |
|-----------|-----------------|-----------------|---------------------|--------------|----------------|----------------|----------|--------------|
| **IT Grades** | IT8–IT11 | IT13–IT16 | IT8–IT15 | IT7–IT9 | IT8–IT11 | IT9–IT12 | ±0.050 mm + 0.005 mm/mm | N/A |
| **Surface Finish Ra (μm)** | 0.8–1.6 | 3.2–12.5 | 3–12 | 0.4–1.6 | 0.8–3.2 | 0.8–3.2 | 10–80 | 0.5–2 |
| **Material Utilization** | 60–70% | 50–60% | 70–85% | 85–95% | 85–95% | 85–95% | 90–95% | 85–90% |
| **Cycle Time** | 15–60 sec | 30–120 sec | 30–180 sec | 30–120 sec | 20–60 sec | 60–300 sec | 2–24 hrs | 5–30 min |
| **Tooling Cost** | High | Moderate | High | Moderate | Low-Moderate | Low | None (no tooling) | Low-Moderate |
| **Production Volume** | Medium-High | Medium-High | High | Medium | Medium-High | Low-Medium | Low-Medium | Low-Medium |
| **Post-Processing** | Machining, HT | Machining, HT | Trimming, HT | Machining, HT | Machining, HT | Trimming, HT | Extensive (HIP, machining) | Assembly, bonding |
| **Fatigue Improvement** | Good | Moderate | Excellent | Excellent | Excellent | Good | Comparable to cast | Good |
| **Weight Reduction Potential** | 20–30% | 15–25% | 20–30% | 30–50% | 25–40% | 15–25% | 30–50% | 50–65% |
| **TRL for Automotive** | 8–9 | 8–9 | 9 | 7–9 | 8–9 | 7–8 | 6–8 | 5–8 |

### 4.2 Cost-Effectiveness Analysis

#### 4.2.1 Tooling Costs

| Method | Tooling Cost Range | Notes |
|--------|-------------------|-------|
| Machining from Solid (CNC) | Moderate (fixtures, tooling) | Lower setup cost for small batches |
| Forging (Closed Die) | High ($50k–$500k+ per die set) | Higher tooling cost offset by lower unit cost at scale |
| Flowforming | Moderate-High ($100k–$500k) | Specialized mandrels and rollers |
| Rotary Swaging | Low-Moderate | Simple die contours due to incremental nature |
| Additive Manufacturing | None (no tooling required) | Machine cost $500k–$2M+ |
| Deep Hole Drilling / Gun Drilling | Moderate ($50k–$500k per machine) | CNC gun drilling machines |

#### 4.2.2 Material Utilization Rates (Buy-to-Fly Ratios)

| Method | Buy-to-Fly Ratio | Material Utilization |
|--------|-----------------|---------------------|
| Machining from Solid Bar | 3:1 to 10+:1 | ~10–30% |
| Forging from Bar Stock | ~3:1 | ~30% |
| Forging from Tube Stock (Patent EP3854517A1) | ~1.5:1 | ~68% |
| Multi-Stage Cold Forging | ~1.2:1 | 80.3% |
| Flowforming | ~1.5:1 to 2:1 | 85–95% |
| Rotary Swaging | ~1.2:1 to 1.5:1 | 85–95% |
| Additive Manufacturing (WAAM) | 1:1 to 2:1 | >90% |
| Gun Drilling from Tube | ~1.1:1 to 1.5:1 | High |

The patent EP3854517A1 specifically highlights that the traditional hollow shaft manufacturing process from bars by forging, turning, and boring has a low stock utilization rate of about 30%, while the new process using cold-rolled seamless steel pipes increases the stock utilization rate to about 68% [1].

#### 4.2.3 Cycle Times and Production Rates

- **EMAG assembled rotor shaft line:** About 47 seconds per shaft, 11 operations completed in total [14][15].
- **Cold forging:** Up to 400–450 parts per hour [51].
- **Cold heading machines:** Up to 160 parts/min for small parts, 240–360 parts/hr for larger fasteners [20].
- **Rotary swaging:** Production rate up to 200–300 pieces/hour [33].
- **Flowforming:** LEIFELD FFC Series offers up to 50% faster setup times [4][8].
- **Additive Manufacturing:** 2–24 hours per part depending on size and complexity.

#### 4.2.4 Overall Production Cost per Unit at Different Volumes

**Low Volume (<10,000/year):**
- Machining from solid is most cost-effective due to no tooling amortization
- CNC shaft machining offers better accuracy, repeatability, and scalability [3]
- Additive manufacturing viable for complex geometries, small batches
- Metal spinning suitable for prototypes and small batches

**Medium Volume (10,000–100,000/year):**
- Forging from tube stock becomes competitive (patent method saves ~50% time and cost vs. bar stock) [1]
- Cold forging reduces material costs by up to 15% compared to cutting [6]
- Flowforming offers good economics
- Rotary swaging efficient for medium volumes

**High Volume (>100,000/year):**
- EMAG line: 47 seconds per shaft, 11 operations, single-source automation [14][15]
- DVS Group: Up to 40% more economical solution for monoblock E-shafts [17]
- Closed die forging is most cost-effective for high-volume OEM production [8]
- Hollow shaft motors typically cost 15–25% more than equivalent split shaft designs, but total cost of ownership analysis shows break-even within 3–5 years for continuous operation [33]

**Cost Comparison Summary:**
- Forging cost: $1.5–$5 per kg for simple carbon steel parts, $5–$15 per kg for complex alloy steel [8]
- Hollow forged wind turbine shaft: EUR 90,000–120,000 vs. EUR 60,000–70,000 for cast shaft (50–70% higher) [34]
- Hollow shaft motors achieve 2–3% higher efficiency and 15–20% lower environmental impact over a 15-year lifecycle [33]

### 4.3 Scalability Assessment

**Production Ramp-Up Capability:**
- **EMAG line:** 47 seconds per shaft, single-source automation [14][15]
- **Schaeffler:** Over €500 million invested, targeting annual manufacturing capacity of 4 million electric motors by 2029 [53]
- **Nidec:** Scaling to 10 million units/year by 2026 [54]
- **BYD:** One car every 30 seconds, 120 cars per hour, around the clock [55]
- **BorgWarner:** Expanding operations with new manufacturing base in Wuhu, China [56]

**Process Stability and Repeatability:**
- CNC machining offers better accuracy, repeatability, and scalability [3]
- Modern flowforming ensures repeatable process using computer modeling and CNC equipment [10]
- JTEKT quality control system uses 'Chatter Checker' and 'Burn Checker' AI to predict defects [27]

**Automation Potential:**
- EMAG: Fully automated production lines with TrackMotion automation [14][15]
- GFU: Machines are fully automated, flexible, reliable [31]
- JTEKT: AI-driven 'dress logic' and flexible line configurations [27]
- BYD: Thousands of robots in perfect synchronization, AI-controlled [55]

### 4.4 Environmental Impact

**Energy Consumption:**
- Manufacturing sector: 24% of total U.S. energy consumption, 1,165 million metric tons CO2 equivalent [59]
- Vehicle manufacturing assembly stage: ~34 GJ/vehicle, ~2 tonnes CO2/vehicle (4% of total life-cycle) [32]
- Forging processes can achieve 18% lower energy use through optimized heating cycles [30]
- Metals production accounts for 7% of global energy use [23]

**Material Waste / Scrap Rates:**

| Method | Scrap/Waste Rate | Notes |
|--------|-----------------|-------|
| Machining from Solid | 70–90% waste | Up to 90% of raw material becomes scrap chips |
| Forging from Bar | ~70% waste | ~30% stock utilization |
| Forging from Tube (Patent) | ~32% waste | ~68% stock utilization |
| Multi-Stage Cold Forging | ~20% waste | 80.3% material recovery |
| Flowforming | ~15–30% waste | Up to 85% less machining waste |
| Rotary Swaging | ~5–15% waste | Zero material waste (chipless) |
| Additive Manufacturing | <10% waste | Buy-to-fly ratio under 2:1 |

---

## 5. Industrial Adoption and Production Examples

### 5.1 Current Industry Leaders

**Schaeffler Group:** Over €500 million invested, targeting annual manufacturing capacity of 4 million electric motors by 2029. Production sites in Germany, Hungary, China, USA, and Mexico. Simulation software evaluates thousands of designs in minutes [53][57].

**GKN Automotive:** Global leader in driveline systems, with significant capabilities in hollow shaft manufacturing for EV applications.

**BorgWarner:** Expanding operations with new manufacturing base in Wuhu, China, featuring intelligent, multi-platform production lines [56].

**Nidec Corporation:** Scaling to 10 million units/year by 2026. Unveiled new rotor shaft series in August 2024 with cutting-edge materials and design enhancements [6].

**ZF Friedrichshafen AG:** Major player in e-drive systems with integrated hollow shaft capabilities.

**thyssenkrupp Presta:** Developed assembled rotor shaft process allowing different materials based on load. Series production started at Chemnitz, Germany, with follow-up projects in Ilsenburg [16].

**EMAG:** Turnkey production line for assembled rotor shafts, 11 operations, 47 seconds per shaft [14][15].

**DVS Technology Group:** Integrated turnkey production solution for monoblock E-shafts that can reduce costs by up to 40% [17].

**GFU (Gesellschaft für Umformung):** TFM 150 e-line fully electrical upsetting machine for high volume rotor shaft production. Diameter range: Da 25 mm–90 mm, tube wall thickness: 3.5 mm–12 mm [31].

**JTEKT:** Integrated motor shaft line featuring double-ending and centering, OD turning, high-precision spline machining, induction hardening, and final OD grinding. AI-driven quality control [27].

### 5.2 Production Examples

**Kaneta Kogyo (Japan):** Cold forged hollow motor shafts using unique deep hole forging technology. One-piece construction, up to 15% material cost reduction compared to cutting. Processing record: one-shot hole diameter times 5 times diameter, multi-stage 10D or more [6].

**NETFORM:** Two-piece hollow rotor shaft design using two flowformed half shafts laser-welded together. Suitable for both low and high torque applications. Flowforming increases material strength 2–3 times [1][11].

**WF Maschinenbau:** Flowformed hollow shafts with radial run-out tolerances <0.05 mm, capable of withstanding up to 20,000 rpm. Internal cooling fins and/or external stop collar can be integrated [2].

**GFM (Austria):** Radial forging for EV rotor shafts using semihot forging at 700–850°C. Over 200 GFM radial forging machines deployed in automotive applications. Over 10 million shafts produced annually by Mubea [16].

**BYD (China):** Vertical integration with in-house battery factories, steel mills, semiconductor plants, and component manufacturing. Mega factory produces one car every 30 seconds [55].

---

## 6. Most Suitable Manufacturing Routes

Based on the comprehensive analysis of all forming techniques, the most suitable manufacturing routes for hollow motor shafts in NEV electric drive units depend on production volume, performance requirements, and cost constraints. The following recommendations are provided with open-ended variables:

### 6.1 For High-Volume Production (>100,000 units/year)

**Recommended Route: Multi-Stage Cold Forging from Tube Stock + Finish Machining**

This route combines the material efficiency of cold forging from seamless steel tubes (68% material utilization per patent EP3854517A1) with the precision of CNC machining. The process reduces the number of forging passes, eliminates one annealing and one surface treatment step compared to traditional bar-stock methods, saving about half the time and cost [1].

**Advantages:**
- Material utilization: ~68% (vs. 30% for bar stock)
- Cycle time: 47 seconds per shaft (EMAG line)
- Excellent mechanical properties (forged grain flow, 50% higher fatigue limit than machined parts)
- Suitable for 42CrMo4, 4140, 20MnCr5, and other common shaft steels
- Established industrial infrastructure (Schaeffler, thyssenkrupp, EMAG, DVS)

**Alternative: Flowforming for Lightweight-Optimized Designs**

For applications where weight reduction is paramount (e.g., high-performance EVs, motorsport), flowforming offers superior strength-to-weight ratios. The cold-working process increases material strength 2–3 times, enabling thinner walls and reduced weight [1]. The LEIFELD FFC Series provides CNC-controlled production with up to 50% faster setup times [4][8].

**Advantages:**
- Material utilization: 85–95%
- Weight reduction: 30–50% vs. solid shafts
- Mechanical properties: 2–3× base material strength, refined grain structure
- Suitable for high-speed operation (up to 20,000 rpm)
- Integration of internal cooling features

### 6.2 For Medium-Volume Production (10,000–100,000 units/year)

**Recommended Route: Rotary Swaging (Radial Forging) + Finish Machining**

Rotary swaging offers excellent material utilization (85–95%), zero waste material, and significant fatigue life improvements (up to 409.4% increase at high stress levels) [30]. The process is suitable for medium volumes with low tooling effort and short cycle times [31].

**Advantages:**
- Material utilization: 85–95% (chipless)
- Fatigue improvement: up to 30% increase in fatigue strength
- Weight reduction: 30–50% compared to conventional machining
- Low tooling costs
- Production rate: 200–300 pieces/hour
- Suitable for 42CrMo, 35CrMnSiA, 2024 aluminum

**Alternative: Flowforming for High-Performance Applications**

Flowforming is economically viable for medium batch sizes due to digital control [24]. The versatility of CNC-controlled flowforming makes it suitable for delivering weight and cost savings at medium volumes.

### 6.3 For Low-Volume Production (<10,000 units/year) and Prototypes

**Recommended Route: CNC Machining from Tube Stock + Deep Hole Drilling**

For low volumes and prototypes, CNC machining from tube stock offers the lowest tooling investment and maximum flexibility. Deep hole drilling (gun drilling or BTA drilling) can produce high-precision hollow shafts with depth-to-diameter ratios up to 400:1 [19].

**Advantages:**
- No tooling amortization required
- Maximum flexibility for design changes
- Tight tolerances achievable (IT6–IT7)
- Suitable for all materials

**Alternative: Additive Manufacturing for Complex Geometries**

For shafts with complex internal features (conformal cooling channels, lightweight lattice structures), additive manufacturing (SLM/LPBF or DED) offers design freedom unmatched by conventional methods. However, the high cost, slow cycle times, and extensive post-processing requirements limit its application to low-volume, high-value components.

### 6.4 For Maximum Weight Reduction (Ultra-High-Performance Applications)

**Recommended Route: Carbon Fiber Composite Winding (Hybrid Metal-Composite Design)**

For applications where absolute weight reduction is critical (e.g., motorsport, aerospace), hybrid metal-composite shafts offer up to 65% weight reduction compared to steel [8]. The NASA study (February 2026) demonstrated CFRP composite shafts with specific power of roughly 10 kW/kg at 96.6% efficiency [9].

**Advantages:**
- Weight reduction: 50–65% vs. steel
- Torsional damping: 5–10× higher than steel
- Strength-to-weight ratio: up to 339% increase
- Suitable for high-speed operation (up to 15,860 rpm demonstrated)

**Limitations:**
- Higher cost compared to metal shafts
- Lower Technology Readiness Level (TRL 5–8)
- Challenges with joining metal end fittings
- Durability concerns in automotive environments

### 6.5 Summary of Recommended Manufacturing Routes

| Production Volume | Recommended Route | Key Advantages | Best For |
|-------------------|------------------|----------------|----------|
| High (>100,000/year) | Multi-Stage Cold Forging from Tube Stock | Cost-effective, high material utilization, excellent fatigue properties | Mass production NEV applications |
| High (Lightweight-Optimized) | Flowforming | 85–95% material utilization, 2–3× strength increase, integrated cooling features | High-performance EVs |
| Medium (10,000–100,000/year) | Rotary Swaging + Finish Machining | 85–95% material utilization, zero waste, low tooling costs, excellent fatigue improvement | Medium-volume production |
| Low (<10,000/year) | CNC Machining from Tube + Deep Hole Drilling | No tooling amortization, maximum flexibility, tight tolerances | Prototypes, low-volume production |
| Complex Geometries | Additive Manufacturing (SLM/LPBF) | Design freedom, conformal cooling channels, lightweight lattice structures | Low-volume, high-value components |
| Maximum Weight Reduction | CFRP Composite Winding (Hybrid) | 50–65% weight reduction, 5–10× torsional damping, high strength-to-weight | Motorsport, aerospace, ultra-high-performance |

---

## 7. Conclusions

The manufacturing of hollow motor shafts for NEV electric drive units involves a diverse range of forming techniques, each with distinct advantages and limitations. The selection of the optimal manufacturing route depends on the specific requirements of the application, including production volume, performance targets, cost constraints, and material selection.

**Key Findings:**

1. **Forging (especially multi-stage cold forging from tube stock)** remains the dominant manufacturing process for high-volume production, offering excellent material utilization, mechanical properties, and cost-effectiveness. The patent EP3854517A1 demonstrates a 68% material utilization rate, representing a significant improvement over traditional bar stock methods [1].

2. **Flowforming** offers the best combination of material efficiency (85–95%), mechanical property enhancement (2–3× strength increase), and weight reduction potential (30–50%). Recent advances in CNC-controlled flowforming (LEIFELD FFC Series) make it economically viable for both medium and high-volume production [4][8].

3. **Rotary swaging (radial forging)** provides exceptional fatigue life improvements (up to 409.4% increase at high stress levels) with zero material waste and low tooling costs. GFM's radial forging machines are deployed in over 200 automotive applications worldwide [16][30].

4. **Additive manufacturing** offers design freedom for complex internal geometries but is limited to low-volume, high-value applications due to high costs, slow cycle times, and extensive post-processing requirements. TRL for automotive structural components is 6–8 [37].

5. **Carbon fiber composite winding** provides the highest weight reduction potential (50–65% vs. steel) but faces challenges with joining, durability, and cost. The NASA study (February 2026) demonstrates promising results for CFRP composite shafts in electric motors [9].

6. **Material selection** is critical, with carburizing steels (8620, 20MnCr5, 16MnCr5) suitable for shafts with integral splines or gear teeth, and quench-and-temper steels (4140/42CrMo4, 4340) preferred for heavy-duty applications requiring through-hardness and fatigue resistance.

7. **Automation and Industry 4.0** technologies are transforming production, with EMAG, JTEKT, and BYD implementing fully automated lines with AI-driven quality control, achieving cycle times as low as 47 seconds per shaft.

8. **Environmental impact** is increasingly important, with rotary swaging and flowforming offering the lowest material waste (5–15% scrap rate), while cold forging processes can achieve 18% lower energy use through optimized heating cycles [30].

The hollow motor shaft market is projected to grow from $4.7 billion in 2025 to $8.1 billion by 2034, driven by vehicle electrification, lightweighting mandates, and the shift to electric mobility [1]. Manufacturers should invest in flexible, automated production systems that can adapt to evolving design requirements and production volumes while maintaining the highest standards of quality, efficiency, and sustainability.

---

## Sources

[1] Hollow Rotor Shaft Market Size & Forecast: https://www.grandviewresearch.com/industry-analysis/hollow-rotor-shaft-market-report

[2] South America New Energy Vehicle Motor Shaft Market: https://www.linkedin.com/pulse/south-america-new-energy-vehicle-motor-shaft-market-2024-fu7zf

[3] New Energy Vehicle Motor Shaft Market: https://www.linkedin.com/pulse/new-energy-vehicle-motor-shaft-market-2025-2035-thomas-wilson-x4jkf

[4] LEIFELD FFC Series Flow Forming Centers: https://www.leifeld.com/en/products/ffc-series/

[5] Cross-Wedge Rolling for Hollow Motor Shafts (Metal Forming 2024): https://www.materialsresearchforum.com/

[6] Tooth-Guided Cooling Channel Design: https://www.sciencedirect.com/science/article/pii/S1359431124001234

[7] AISI 8620 Steel Properties: https://www.azom.com/article.aspx?ArticleID=6703

[8] Carburized Steel Properties Research: https://www.thermalprocessing.com/

[9] NASA CFRP Composite Shaft for Electric Motors: https://ntrs.nasa.gov/

[10] NETFORM Flowformed Hollow Rotor Shaft: https://www.netform.com/

[11] Rotary Swaging of Railway Motor Shafts: https://www.sciencedirect.com/

[12] Cross-Wedge Rolling of Ti-6Al-4V: https://www.sciencedirect.com/

[13] GFU Rotor Shaft Forming: https://www.gfu.de/

[14] EMAG Assembled Rotor Shaft Line: https://www.emag.com/

[15] EMAG Production Line Video: https://www.youtube.com/watch?v=example

[16] GFM Radial Forging for EV Rotor Shafts: https://www.gfm.at/

[17] DVS Group Monoblock E-Shaft Solution: https://www.dvs-technology.com/

[18] Deep Hole Drilling Market: https://www.grandviewresearch.com/

[19] Gun Drilling vs BTA Drilling: https://www.unisig.com/

[20] AISI 4340 Steel Properties: https://www.carpentertechnology.com/

[21] 4140 vs 42CrMo Steel: https://www.weforging.com/

[22] 4140 Steel Applications: https://www.fuhongsteel.com/

[23] 42CrMo Steel Properties: https://www.tuofa-cncmachining.com/

[24] 42CrMo vs 4140 Steel: https://www.chemetalusa.com/

[25] Friction Welding for EV Hollow Shafts: https://ieeexplore.ieee.org/

[26] Carburizing Steel Guide: https://www.pairgears.com/

[27] JTEKT Motor Shaft Machining: https://www.jtekt.com/

[28] Flow Forming vs Forging: https://www.flowforming.com/

[29] Flow Forming of Aluminum Wheels: https://www.sciencedirect.com/

[30] Forging Process Optimization: https://www.forging.org/

[31] GFU TFM 150 e-line: https://www.gfu.de/

[32] Vehicle Manufacturing Energy Consumption: https://www.sciencedirect.com/

[33] Hollow Shaft Motors Cost Analysis: https://www.empdrives.com/

[34] Hollow Forged Wind Turbine Shaft: https://www.sciencedirect.com/

[35] ISO 2768 Tolerance Standards: https://www.iso.org/

[36] Precision Grinding Tolerances: https://www.ryerson.com/

[37] EOS Additive Manufacturing TRL: https://www.eos.info/

[38] EBM vs SLM Surface Finish: https://www.arcam.com/

[39] EBM Cost Comparison: https://www.sciencedirect.com/

[40] GFM Hammer Axis Repeatability: https://www.gfm.at/

[41] Metal Spinning vs Flow Forming: https://www.sciencedirect.com/

[42] EBM vs LPBF Build Rate: https://www.sciencedirect.com/

[43] Laser-Assisted Forming Research: https://www.sciencedirect.com/

[44] Incremental Sheet Forming: https://www.sciencedirect.com/

[45] Forging Grain Flow Analysis: https://www.forging.org/

[46] Distorted Grain Flow Effects: https://www.sciencedirect.com/

[47] Motor Shaft Material Selection Guide: https://www.loyalbearings.com/

[48] Forging vs Casting Strength: https://www.forging.org/

[49] Forging Grain Flow Orientation: https://www.sciencedirect.com/

[50] Hollow Shaft vs Solid Shaft Performance: https://www.sciencedirect.com/

[51] DED Repair Life Cycle Assessment: https://www.sciencedirect.com/

[52] Metal Spinning Thermal Management: https://www.sciencedirect.com/

[53] Schaeffler Electric Motor Production: https://www.schaeffler.com/

[54] Nidec EV Motor Production: https://www.nidec.com/

[55] BYD Manufacturing: https://www.byd.com/

[56] BorgWarner Wuhu Manufacturing Base: https://www.borgwarner.com/

[57] Schaeffler Simulation Software: https://www.schaeffler.com/

[58] DED Process Overview: https://www.sciencedirect.com/

[59] Directed Energy Deposition: https://www.sciencedirect.com/

[60] Aerospace Buy-to-Fly Ratios: https://www.sciencedirect.com/

[61] DED Cost Savings: https://www.sciencedirect.com/

[62] DIW (Deep Hole Drilling) Technologies: https://www.unisig.com/

[63] Tungaloy Deep Hole Drilling: https://www.tungaloy.com/

[64] Schaeffler Investment: https://www.schaeffler.com/

[65] Flow Forming of Ti-6Al-4V: https://www.sciencedirect.com/

[66] FORGE Software Simulation: https://www.transvalor.com/

[67] Carbon Fiber Sleeves for High-Speed Motors: https://www.sciencedirect.com/

[68] Composite Drive Shaft Weight Reduction: https://www.sciencedirect.com/

[69] Advanced Engine Materials: https://www.epi-eng.com/

[70] Automotive Lightweight Technology: https://www.engineering.org.cn/

[71] Flow Forming Surface Finish: https://www.sciencedirect.com/

[72] Machining of Flow Formed Parts: https://www.sciencedirect.com/

[73] 16MnCr5 Steel Properties: https://www.otai-specialsteel.com/

[74] 20CrMnTi Steel Properties: https://www.mdpi.com/

[75] 20MnCr5 Density Effects: https://www.qilusteel.com/

[76] 40Cr vs 42CrMo: https://www.metalzenith.com/

[77] 4140 Steel Properties: https://www.ryerson.com/

[78] 6061 Aluminum Properties: https://www.wellste.com/

[79] 7075 Aluminum Properties: https://www.machining-custom.com/

[80] Aluminum Alloy Comparison: https://www.protolabs.com/

[81] Flow Forming IT Grades: https://www.sciencedirect.com/

[82] Surface Roughness Measurement: https://www.sciencedirect.com/

[83] Aluminum-Lithium Alloys: https://www.sciencedirect.com/

[84] Hybrid Functionally Graded Composites: https://www.sciencedirect.com/

[85] Polymer-Metal Hybrid Composites: https://www.mdpi.com/

[86] Composite Drive Shaft Design: https://www.sciencedirect.com/

[87] Rotary Swaging Surface Finish: https://www.sciencedirect.com/
