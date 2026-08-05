# Comprehensive Analysis of Liability Allocation in Accidents Involving Vehicles with Advanced Driver-Assistance Systems (ADAS)

## Executive Summary

The allocation of liability in accidents involving vehicles with advanced driver-assistance systems (ADAS) operating in a shared human-machine driving context represents one of the most complex and rapidly evolving areas of law and technology. This analysis integrates technical principles of ADAS, existing legal frameworks, and relevant case law to systematically examine the boundaries of responsibility between human drivers and automated systems. The research reveals that liability allocation is fundamentally determined by the SAE level of automation, but is significantly complicated by factors including system design limitations, driver monitoring adequacy, marketing representations, and the fragmented nature of regulatory frameworks across jurisdictions. Landmark cases such as *Benavides v. Tesla* (2025) and the Uber ATG fatality in Tempe, Arizona (2018) have established critical precedents, while legislative developments in the UK, Germany, and the European Union are reshaping the legal landscape. This report concludes with concrete regulatory recommendations for policymakers, insurers, and manufacturers.

---

## 1. Technical Principles of ADAS Relevant to Liability Allocation

### 1.1 SAE J3016 Levels of Driving Automation and Division of Responsibility

The SAE J3016 standard (jointly developed with ISO) defines six levels of driving automation from Level 0 (No Driving Automation) through Level 5 (Full Driving Automation), based on the sustained performance of the Dynamic Driving Task (DDT). This taxonomy is the foundational reference for understanding responsibility allocation, as it identifies three primary actors: the human user, the driving automation system, and other vehicle systems. [1]

**Levels 0-2:** The human driver performs all or part of the DDT and must supervise the system at all times. At Level 2 (Partial Driving Automation), the vehicle controls both steering and acceleration/deceleration simultaneously, but the driver must remain fully engaged, monitor the environment, and be responsible for Object and Event Detection and Response (OEDR). As noted by SAE J3016, "Liability almost always falls on the driver for failing to properly monitor the vehicle and its environment." [1] Current Level 2 systems include Tesla Autopilot/FSD, GM Super Cruise, and Ford BlueCruise. The standard explicitly prohibits fractional designations such as "Level 2+" or "Level 2.5." [2]

**Level 3 (Conditional Driving Automation):** The Automated Driving System (ADS) performs the entire DDT within its Operational Design Domain (ODD). The driver does not need to monitor the environment but must be "fallback-ready" and respond to a takeover request (transition demand) within a specified time—typically "at least several seconds" per SAE J3016. [2] If the driver does not respond, the system must perform a Minimum Risk Maneuver (MRM). This is where liability begins to shift from the driver to the manufacturer. Examples include Mercedes-Benz Drive Pilot (certified in Germany, California, and Nevada) and Honda Traffic Jam Pilot (Japan). [3]

**Levels 4-5:** The ADS performs the entire DDT and DDT fallback within its ODD (Level 4) or under all conditions (Level 5). No human intervention is expected. The OEM or ADS provider is likely at fault for crashes occurring within the ODD. Waymo robotaxis operate at Level 4 in geofenced areas. No Level 5 vehicles exist for consumer purchase as of 2026. [1]

### 1.2 Sensor Fusion Architecture and Limitations

ADAS sensor fusion combines data from multiple sensors—cameras, radar, LiDAR, and ultrasonic sensors—to create a comprehensive perception model of the vehicle's environment. However, each sensor type has inherent limitations that directly affect system reliability and, consequently, liability allocation. [4]

**Cameras:** High resolution, excellent object classification, and color recognition, but poor distance estimation (monocular), degraded performance in low light, snow, rain, fog, and glare. Common failure modes include camera blur, condensation, occlusion, and dirt/road grime.

**Radar:** Works well in bad weather and provides long-range detection (up to 300m), but has poor object classification and cannot distinguish shape or color. Susceptible to interference and false positives.

**LiDAR:** High 3D accuracy and excellent depth perception, but expensive, degraded by fog, rain, snow, and dust, and affected by mirror-like objects.

The NHTSA report "Safety Implications of Potential Advanced Driver Assistance Systems Sensor Degradation" (DOT HS 813 740, December 2025) found that occlusions reduced sensor response, and road grime or improper repairs significantly decreased range and point returns. System-level behavior varied: depending on sensor fusion and processing, features either shut down, degraded, or were unaffected. [5]

### 1.3 Operational Design Domain (ODD)

Per SAE J3016, the ODD is defined as "Operating conditions under which a given driving automation system or feature thereof is specifically designed to function, including, but not limited to, environmental, geographical, and time-of-day restrictions, and/or the requisite presence or absence of certain traffic or roadway characteristics." [1]

The NHTSA report "A Framework for Automated Driving System Testable Cases and Scenarios" (DOT HS 812 623, September 2018) proposes a hierarchical ODD taxonomy with six categories: Physical Infrastructure, Operational Constraints, Objects, Connectivity, Environmental Conditions, and Zones. [6]

When a vehicle operates outside its ODD, the system should detect this and issue a takeover request. For Level 3 systems, the vehicle must recognize ODD boundaries and provide sufficient warning time. Mercedes-Benz Drive Pilot operates only on pre-mapped freeways with clear lane markings, speeds under 40 MPH, daytime lighting, clear weather, and no construction zones. GM Super Cruise operates on over 600,000 miles of LiDAR-mapped divided highways. [3]

Tesla's Autopilot and FSD have been criticized for having a less clearly defined ODD. A study found that drivers used Autopilot outside its intended ODD, leading to complacency and safety-critical behaviors. This lack of clear ODD definition has been a central issue in product liability litigation. [7]

### 1.4 Human-Machine Interface (HMI) and Driver Monitoring Systems

ADAS systems communicate status, limitations, and failures through multimodal interfaces—visual, auditory, and haptic channels. The NHTSA document "Human Factors Design Guidance for Level 2 and Level 3 Automated Driving Systems" (DOT HS 812 555, August 2018) recommends multimodal messages, continuous system status, anticipatory information, and alert intensity cascades. [8]

**Driver Monitoring Systems (DMS):** These are critical for liability allocation because they determine whether the system adequately ensures driver attention.

- **Camera-based systems** (GM Super Cruise, Ford BlueCruise): Use infrared cameras to track eye gaze direction, head position, eyelid closure, and body posture. They work in all lighting conditions using IR illumination.
- **Steering wheel torque sensing** (Tesla): Detects whether the driver's hands are on the steering wheel. This is simpler but "very simple and easy to fool e.g. by jamming objects that act as a counter-weight into the steering wheel." [9]

NHTSA's investigation of Tesla found that its "weak driver engagement system was not appropriate for Autopilot's permissive operating capabilities," resulting in a "critical safety gap" between drivers' expectations of Autopilot's capabilities and the system's true capabilities. [10]

Regulatory requirements are evolving: The EU General Safety Regulation mandates Driver Drowsiness and Attention Warning (DDAW) and Advanced Driver Distraction Warning (ADDW). UNECE Regulation R157 requires a driver availability recognition system for Level 3 ALKS with detection every 30 seconds. [11]

### 1.5 Override Logic and Handover Procedures

**Override Logic:** Driver steering input typically overrides the ADAS system. Tesla's Autopilot resists manual steering inputs and deactivates Autosteer, while competitors suspend lane centering and reactivate automatically. Driver braking input typically disengages adaptive cruise control. Driver acceleration input overrides speed control—this has been a factor in crashes, including the Benavides case where the driver pressed the accelerator to 100%. [12]

**Handover (Transition of Control):** SAE J3114 defines handover as including preparation, perception of the handover signal, suspension of in-vehicle tasks, and the actual process of taking control. UNECE R157 specifies a 10-second response window before the Minimum Risk Manoeuvre (MRM) is initiated, with a 4-second warning cascade. Mercedes-Benz Drive Pilot provides a 10-second takeover window; if the driver does not respond, the vehicle executes an emergency stop with hazard lights, parking brake engagement, and emergency call. [11]

---

## 2. Legal Frameworks

### 2.1 Tort Law Principles

**Negligence:** Under traditional negligence principles, a plaintiff must prove duty, breach, causation, and damages. The standard of care in motor vehicle operation requires the driver to exercise "reasonable care." When a driver relies on ADAS, the question becomes whether reliance on automation changes this standard of care.

Under the German Road Traffic Act (StVG), as amended in 2017, the driver remains legally in control of the vehicle even when Level 3 or Level 4 automated functionality is engaged. The driver may turn away from driving when the automated system is engaged, provided they remain alert enough to resume control when prompted. For Level 3 vehicle users, the driver's liability is presumed fault liability pursuant to §18(1)(1) of the Road Traffic Act, meaning the burden of proof is on the driver. [13]

**Product Liability:** Strict liability holds a manufacturer or seller responsible for any defective product, regardless of whether they were negligent. Under the Restatement (2d) of Torts §402A, "One who sells any product in a defective condition unreasonably dangerous to the user or consumer or to his property is subject to liability." [14]

Three types of product defects are relevant to ADAS:

1. **Design Defect:** A product is inherently dangerous due to a flaw in its design. For ADAS, design defect claims can center on the system's ODD, arguing that a system permitting activation in conditions it was not designed for failed ordinary consumer expectations. In the *Benavides v. Tesla* case, the court allowed design defect claims on two grounds: (1) Autopilot could be activated on roads it was not designed to handle, and (2) the driver-monitoring system was insufficient to ensure attention. [15]

2. **Manufacturing Defect:** Occurs when a product deviates from its intended design during manufacturing. The malfunction theory allows a plaintiff to establish a manufacturing defect through circumstantial evidence.

3. **Failure to Warn / Marketing Defect:** Occurs when a product does not contain sufficient warning labels or instructions for safe use. In the ADAS context, this is particularly relevant to whether manufacturers adequately warned about system limitations. The *Benavides* case allowed punitive damages claims citing Tesla's marketing as evidence of conscious disregard for safety. U.S. Transportation Secretary Pete Buttigieg criticized the "Autopilot" name as misleading, stating: "I don't think that something should be called, for example, an Autopilot, when the fine print says you need to have your hands on the wheel and eyes on the road at all times." [16]

### 2.2 Vienna Convention on Road Traffic (1968)

The Vienna Convention is an international treaty that aims to facilitate international road traffic and standardize traffic rules. As of 2026, it has 36 signatories and 91 parties. Non-signatory countries include the United States, Canada, China, Ireland, and Malaysia. [17]

**Article 8(1):** "Every moving vehicle or combination of vehicles shall have a driver." A combined reading of Articles 8, 13, and 41 leads to the consideration that the driver is a natural person (human being). [17]

**2016 Amendment (Article 8, paragraph 5bis):** Entered into force on March 23, 2016, deeming vehicle systems compliant with driver control requirements if they meet ECE Regulations or can be overridden/switched off. This amendment allows drivers to pursue other activities (non-driving tasks) while the automated system is engaged. [18]

**2021/2022 Amendment (Article 34 bis):** Entered into force in July 2022, allowing automated driving systems to satisfy the requirement for a driver, provided domestic regulations are met. The amendment states: "The requirement that every moving vehicle or combination of vehicles shall have a driver is deemed to be satisfied while the vehicle is using an automated driving system which complies with domestic technical regulations and legislation." [17]

### 2.3 UN Regulation No. 157 (UN R157) on Automated Lane Keeping Systems (ALKS)

UN R157, adopted by UNECE WP.29, is the first internationally binding regulation for Level 3 ALKS and the first binding international regulation on autonomous driving systems. It was first adopted in June 2020 and came into effect on January 22, 2021. [11]

**Key requirements:**
- System controls lateral and longitudinal movement without continuous driver command
- Driver availability monitoring system required (detection every 30 seconds)
- Clear Transition Demand protocols with a 10-second response window
- Minimum Risk Manoeuvre (MRM) if driver does not respond
- Mandatory Data Storage System for Automated Driving (DSSAD)—essentially a "black box" that records crucial data points
- Collision avoidance: the activated system shall not cause any collisions that are reasonably foreseeable and preventable

**Liability implications:** As soon as the ALKS functionality is enabled, liability shifts from the driver to the manufacturer. 54 states have signed the regulation. [11]

### 2.4 National Legislative Frameworks

**Germany:** The 2017 amendment to the Road Traffic Act (StVG) allowed Level 3 and Level 4 vehicles. The 2021 Autonomous Driving Act established a comprehensive legal framework for Level 4 vehicles, defining "motor vehicle with autonomous driving functions," "determined operational area," "technical oversight," and "minimal risk condition." The liability regime remains based on strict liability for the vehicle keeper and a rebuttable presumption of fault for the driver. The maximum liability for highly and fully automated driving functions was doubled to €10 million for personal injury and €2 million for property damage. [13]

**United Kingdom:** The Automated and Electric Vehicles Act 2018 (AEVA) establishes a direct right of action for innocent victims against the insurer of an AV that causes an accident while "driving itself" on a road or other public place. The Act provides for the defence of contributory negligence and makes clear that the insurer or owner will not be liable where the accident "wholly" results from the negligence of the person in charge of the automated vehicle. The Automated Vehicles Act 2024 introduced the concept of an Authorised Self Driving Entity (ASDE)—typically the manufacturer or AV software developer—responsible for ensuring that its authorised vehicles continue to satisfy the self-driving test over time. [19]

**European Union:** The new Product Liability Directive (EU) 2024/2853, which Member States must transpose by December 9, 2026, brings software—including embedded, stand-alone, and cloud-based applications—within the definition of a "product." It covers harm caused by the autonomous or adaptive behavior of AI systems, including post-sale changes resulting from machine learning or OTA updates. Cybersecurity vulnerabilities and failure to provide software updates are explicit defect triggers. The standard liability period is 10 years, but for latent injuries, the period is extended to 25 years. [20]

**United States:** No federal AV-specific liability law exists. Over 38 states have enacted AV-related laws. NHTSA has issued voluntary guidance (Safety 2.0) and the Standing General Order on crash reporting (SGO-2021-01), requiring manufacturers to report crashes involving Level 2 ADAS or ADS (Levels 3-5) when engaged within 30 seconds of the crash. As of November 2025, there have been 5,202 autonomous vehicle accidents reported, with 65 fatalities. [21]

---

## 3. Case Law

### 3.1 Benavides v. Tesla, Inc. (No. 1:21-cv-21940, S.D. Fla.) — The Landmark Verdict

**The Crash:** On May 8, 2019, in Key Largo, Florida, a 2019 Tesla Model S driven by George McGee using Enhanced Autopilot ran a stop sign at over 60 mph and struck a parked Chevy Tahoe, killing 22-year-old Naibel Benavides Leon and severely injuring Dillon Angulo. McGee dropped his phone and believed the system would brake. [22]

**Pre-Trial Rulings:** In a 70-page summary judgment opinion (July 2025), Judge Beth Bloom denied Tesla's motion for summary judgment, allowing claims that Autopilot was defectively designed in two ways: (1) Autopilot could be activated on roads it was not designed to handle (outside its ODD), and (2) Autopilot's driver-monitoring system (relying on steering wheel torque) was insufficient to ensure attention. The court also allowed punitive damages, citing evidence of Tesla's callous attitude, including Elon Musk's misleading statements and a staged 2016 commercial. The court held that "a reasonable jury could conclude" Autopilot was defectively designed. [15]

**The Verdict (August 1, 2025):** After a three-week trial, a Miami federal jury returned a $329 million verdict (later reduced to $243 million). The jury assigned 33% responsibility to Tesla and 67% to the driver. The jury awarded $200 million in punitive damages, $59 million in compensatory damages to Benavides' family, and $70 million to Angulo. Tesla was ordered to pay $42.5 million of compensatory damages plus the full $200 million in punitive damages. The court dismissed manufacturing defect and negligent misrepresentation claims pre-trial but allowed design defect and failure-to-warn claims under Florida's consumer-expectations and risk-utility tests. [22]

**Key Legal Significance:**
- First U.S. wrongful death verdict holding Tesla liable for Autopilot operation
- Established that design-defect theories grounded in ODD and driver monitoring will be framed as "foreseeable misuse" rather than pure operator error
- Tesla's marketing was used to support punitive damages, setting a precedent for marketing-based liability
- The verdict was upheld on February 20, 2026, with Judge Beth Bloom ruling the evidence "more than supported" the verdict

Carnegie Mellon professor Philip Koopman stated: "The only way the jury could have possibly ruled against Tesla was by finding a defect with the Autopilot software." [22]

### 3.2 Banner v. Tesla, Inc. (Florida Fourth District Court of Appeal, February 26, 2025)

This case involved a fatal 2019 crash where driver Jeremy Banner died after his Model 3 drove under a semi-trailer. A 2023 Florida judge ruled there was "reasonable evidence" that Tesla and Elon Musk knew of the defect. The appellate court (represented by Quinn Emanuel) secured a unanimous appellate victory reversing the trial court decision that had allowed punitive damages claims based on aspirational statements about Autopilot's future capabilities. The ruling eliminated the risk of punitive damages in this case and established a precedent for other courts. [23]

### 3.3 Hsu v. Tesla (Los Angeles, California, April 21, 2023)

A California state court jury handed Tesla a sweeping win in what appears to be the first trial related to a crash involving Autopilot. Plaintiff Justine Hsu alleged her Tesla Model S swerved into a curb while on Autopilot and that the airbag deployed violently, fracturing her jaw. The jury awarded zero damages, found the airbag did not fail to perform safely, and that Tesla did not intentionally fail to disclose facts. Jurors told Reuters they believed Tesla clearly warned that Autopilot was not self-piloting and that driver distraction was to blame. [24]

### 3.4 Uber ATG Case (Tempe, Arizona, March 18, 2018)

**The Crash:** A 2017 Volvo XC90 equipped with Uber's developmental automated driving system struck and fatally injured pedestrian Elaine Herzberg as she crossed midblock outside a crosswalk, pushing a bicycle. This was the first recorded pedestrian fatality caused by a self-driving car. [25]

**NTSB Findings (November 19, 2019):** The NTSB determined the probable cause was the failure of the vehicle operator, Rafaela Vasquez, to monitor the driving environment because she was visually distracted throughout the trip by her personal cell phone, streaming the TV show "The Voice" on Hulu. The ADS detected the pedestrian 5.6 seconds before impact but never correctly classified her or predicted her path (misclassifying her as a vehicle, bike, or unknown object). The system design precluded emergency braking, relying on the operator to intervene. Uber had disabled the vehicle's factory-installed collision avoidance system to "avoid erratic vehicle behavior." [25]

**Key NTSB Findings:**
- Uber ATG did not adequately manage the anticipated safety risk of its automated driving system's functional limitations
- Had the vehicle operator been attentive, she would likely have had sufficient time to detect and react to avoid the crash
- Uber ATG did not have a standalone operational safety division or safety manager, a formal safety plan, or a standardized operations procedure
- The car's self-driving system did not have the capability to classify an object as a pedestrian unless they were near a crosswalk
- A system called "action suppression" suppressed any planned braking for a full second while handing control back to the safety driver
- The safety driver spent 34% of the time looking at her cell phone

**Criminal Proceedings:** The safety driver was indicted for negligent homicide in September 2020. In July 2023, she pleaded guilty to endangerment and was sentenced to three years of supervised probation, avoiding prison time. [25]

### 3.5 Ford BlueCruise Investigations

Two fatal crashes in 2024 involving Ford Mustang Mach-E vehicles with BlueCruise active have led to NHTSA investigations. The first occurred on February 24, 2024, in San Antonio, Texas, where a Mustang collided with a stationary Honda CR-V, killing the Honda driver. The second occurred on March 3, 2024, in Philadelphia, Pennsylvania, where a Mustang struck two stationary vehicles, killing two young men; the driver was charged with DUI homicide. NHTSA is investigating these incidents, which could lead to a recall of approximately 130,000 vehicles. [26]

### 3.6 Phantom Braking and Unintended Acceleration Litigation

**Santiago et al. v. Tesla (N.D. Illinois, November 22, 2024):** U.S. District Judge Georgia Alexakis ruled that Tesla must face part of a proposed class-action lawsuit alleging it failed to warn buyers about a "phantom braking" defect. The court allowed a claim that Tesla concealed the defect from would-be purchasers, noting the lawsuit "successfully connects the dots" between Tesla's alleged omission of safety information on its website and buyers' reliance on the website to make purchase decisions. [27]

**Australian Class Action (2025):** A class action in Australia's Federal Court is seeking compensation for Tesla owners who experienced phantom braking. About 10,000 Tesla drivers have registered interest. The case claims Tesla misled consumers over phantom braking, battery range, and self-driving capability. [28]

### 3.7 Legal Scholarship on Liability Allocation

**Consumer Perception Research:** A Harvard Business School working paper (23-036) found that consumers hold AV manufacturers more liable than manufacturers of human-driven vehicles or human drivers for damages, even when the AV was not the cause of the accident. The underlying mechanism is counterfactual reasoning: because AVs are perceived as abnormal and unfamiliar, consumers are more likely to imagine alternative scenarios where the AV could have acted differently to avoid the accident (optimality bias). [29]

**The "Reasonable Computer Driver" Standard:** Koopman and Widen (2023) propose holding AVs to the same negligence standard as a hypothetical "reasonable human driver" on a case-by-case basis. If an AV fails to avoid harm that a reasonable driver would have avoided, the manufacturer is liable for negligence—not requiring proof of a product defect. This shifts many complex product liability cases into simpler negligence claims. [30]

**Multi-Tier Liability Regimes:** A 2026 article in the World Electric Vehicle Journal identifies four main liability regimes: (1) Driver Liability Regime (Level 2 and below), (2) System Liability Regime (Level 3+, e.g., UK), (3) Manufacturer or Operator Liability Regime (Level 3+, e.g., Germany, France, South Korea), and (4) Composite Liability Regime (transitional for Level 2-3, e.g., US, Australia, Canada). [31]

---

## 4. Regulatory Recommendations

### 4.1 Recommendations for Policymakers

**1. Adopt a Tiered Liability Framework Based on SAE Automation Levels**

Policymakers should establish clear statutory frameworks that define liability allocation according to the SAE level of automation at the time of the accident:

- **Levels 0-2:** Driver bears primary liability, with a rebuttable presumption of driver fault
- **Level 3:** Shared liability between driver and manufacturer, with the manufacturer bearing liability when the ADS is engaged and operating within its ODD, and the driver failing to respond to a valid takeover request within the specified time window
- **Levels 4-5:** Manufacturer or ADS provider bears primary liability for accidents occurring within the ODD, with a narrow exception for intentional interference or unauthorized modifications by the user

The UK's "User-in-Charge" (UIC) concept from the Law Commission's 2022 Joint Report provides a useful model. The UIC is a person in the vehicle who is not responsible for dynamic driving but must be qualified and fit to drive, and must respond to transition demands. UICs are immune from criminal offences and civil penalties while the vehicle is driving itself, unless they deliberately cause a malfunction or alter the system. [32]

**2. Mandate Data Storage Systems for Automated Driving (DSSAD)**

Following the UN R157 model, policymakers should mandate tamper-proof DSSAD that records:
- Whether the ADS was engaged at the time of the crash
- The ODD conditions at the time of the crash
- Driver monitoring data (eye gaze, hands on wheel, head position)
- Takeover request status and driver response time
- System fault or degradation events
- Sensor data and fusion outputs

The UK Law Commission recommends data retention for 39 months, in line with the standard limitation period for bringing a claim. [32] Germany's §63a StVG legally prescribes DSSAD for vehicles with automation ≥ SAE Level 3. [13]

**3. Establish Clear ODD Definition and Communication Requirements**

Policymakers should require manufacturers to:
- Clearly define the ODD for each ADAS feature in standardized, consumer-friendly language
- Implement geofencing or other technical measures to prevent activation outside the ODD
- Provide clear, multimodal warnings when the vehicle approaches ODD boundaries
- Include ODD parameters in the DSSAD for accident investigation purposes

The NHTSA ODD Framework (DOT HS 812 623) provides a hierarchical taxonomy for this purpose. [6]

**4. Regulate Driver Monitoring System Standards**

Policymakers should establish minimum standards for DMS, including:
- Requirement for camera-based eye gaze tracking (not merely steering wheel torque sensing) for Level 2 and above
- Real-time detection of driver distraction, drowsiness, and hands-off-wheel
- Cascading alert intensity with increasing urgency
- Inability to disable or bypass the DMS by the driver
- Continuous monitoring even when the system is engaged

The EU General Safety Regulation and UNECE R157 provide models for these requirements. [11] NHTSA should issue a proposed rulemaking to mandate DMS standards for Level 2 ADAS, addressing the "critical safety gap" identified in its Tesla investigation. [10]

**5. Prohibit Misleading Marketing of ADAS Features**

Policymakers should:
- Prohibit marketing terms that imply greater automation capability than the system actually possesses (e.g., "Autopilot," "Full Self-Driving" for Level 2 systems)
- Require clear, standardized labeling of ADAS features by SAE level
- Establish civil and criminal penalties for misleading marketing, as proposed by the UK Law Commission [32]
- Require manufacturers to disclose system limitations in all marketing materials

The UK government's consultation outcome on protecting marketing terms (July 2026) notes that "Research evidence consistently shows that the distinction between driver assistance systems and self-driving technology is not well understood by the public." [33]

**6. Harmonize International Regulatory Frameworks**

Policymakers should work toward international harmonization of:
- Liability allocation rules for cross-border AV operations
- Data sharing standards for accident investigation
- Type-approval requirements for ADAS and ADS
- Insurance requirements for automated vehicles

The UNECE WP.29 framework, including UN R157, R155, and R156, provides a foundation for such harmonization. [11]

### 4.2 Recommendations for Insurers

**1. Develop Usage-Based Insurance Models for ADAS-Equipped Vehicles**

Insurers should leverage connected car data to develop usage-based insurance (UBI) models that:
- Price premiums based on actual ADAS engagement and driving behavior
- Differentiate between manual driving, Level 2 assistance, and higher automation levels
- Offer discounts for vehicles with robust DMS and clearly defined ODD
- Adjust premiums based on DSSAD data showing responsible system use

Research shows that ADAS-equipped vehicles have 23% less bodily injury costs, 14% less property damage, and 8% less collision claims costs. [34]

**2. Implement No-Fault Compensation Schemes**

Following the UK's Automated and Electric Vehicles Act 2018 model, insurers should support no-fault compensation schemes that:
- Provide direct compensation to victims without proving fault
- Allow insurers to recover costs from manufacturers under product liability law
- Reduce litigation costs and provide faster compensation
- Cover all victims regardless of fault attribution

The European Added Value Assessment (EPRS, 2018) found that 74% of stakeholders were concerned about liability issues, and 87% saw autonomous vehicles as the most urgent regulatory area. A new EU legislation with a no-fault insurance framework was deemed preferable. [35]

**3. Establish Data Access Protocols**

Insurers should:
- Advocate for statutory rights to access DSSAD data for claims processing
- Develop standardized data formats for accident reconstruction
- Partner with manufacturers to create data exchanges that reduce complexity and cost
- Ensure consumer consent and data privacy protections

The UK Law Commission recommends that "specific legal provision should be made requiring those who control data from such vehicles (typically the ASDE) to make it available to insurers in order to determine liability for a claim." [32]

**4. Create Hybrid Insurance Products**

Insurers should develop hybrid policies that cover:
- Driver liability for manual driving and Level 2 operation
- Manufacturer/operator liability for Level 3+ operation
- Cyber liability for technology errors and hacking
- Product liability for software defects and OTA updates

Partnerships such as Munich Re/Mobileye and Swiss Re/Baidu demonstrate the feasibility of AV-tailored insurance based on data from aftermarket systems and autonomous driving behavior. [36]

### 4.3 Recommendations for Manufacturers

**1. Design Systems with Clear ODD and Robust Driver Monitoring**

Manufacturers should:
- Implement geofencing or other technical measures to prevent ADAS activation outside the ODD
- Use camera-based DMS that tracks eye gaze, not just steering wheel torque
- Design cascading alert systems with multimodal warnings (visual, auditory, haptic)
- Ensure that the DMS cannot be disabled or bypassed by the driver
- Implement fail-operational techniques that allow the ADS to continue functioning at a reduced capacity when system limits are reached

The NHTSA investigation of Tesla found that "Tesla's weak driver engagement system was not appropriate for Autopilot's permissive operating capabilities," resulting in a "critical safety gap" that "led to foreseeable misuse and avoidable crashes." [10]

**2. Implement Transparent and Accurate Marketing**

Manufacturers should:
- Use SAE level designations in all marketing materials
- Clearly disclose system limitations and ODD boundaries
- Avoid marketing terms that imply full automation for Level 2 systems
- Provide consumer education programs on proper ADAS use
- Ensure that in-vehicle HMI clearly communicates the current automation level and driver responsibilities

The *Benavides* case established that misleading marketing can be used to support punitive damages claims. [22]

**3. Ensure Robust Data Recording and Sharing**

Manufacturers should:
- Implement DSSAD that meets or exceeds UN R157 requirements
- Store data for at least 39 months as recommended by the UK Law Commission
- Make data available to insurers and accident investigators
- Ensure data integrity and tamper-proofing
- Comply with privacy regulations while enabling safety data sharing

**4. Adopt Safety-Critical Design Principles**

Manufacturers should:
- Follow ISO 26262 (functional safety) and ISO 21448 (SOTIF) standards
- Conduct thorough Hazard Analysis and Risk Assessment (HARA)
- Implement fail-safe and fail-operational techniques as appropriate
- Develop comprehensive safety cases for ADS features
- Establish safety management systems as proposed by Germany and the UK for UN R157 compliance

**5. Prepare for Product Liability Under the New EU PLD**

Manufacturers operating in the EU should:
- Ensure compliance with the EU Product Liability Directive 2024/2853, which covers software, AI systems, and OTA updates
- Implement post-market monitoring for software defects
- Document all software updates and modifications
- Maintain cybersecurity protections under UN R155
- Budget for the extended 25-year liability period for latent injuries

**6. Accept Liability When ADS Is Engaged**

Following Mercedes-Benz's example, manufacturers should:
- Clearly state their acceptance of liability when the ADS is engaged and used as designed
- Ensure that this acceptance covers both product defect liability and tort liability
- Communicate this policy clearly to consumers and regulators
- Develop insurance products that cover this liability exposure

However, as CMU autonomy expert Phil Koopman notes, "Anyone turning on Drive Pilot should presume they will be blamed for any crash, no matter what Mercedes-Benz says," because the distinction between product defect liability and driver negligence remains legally ambiguous. [37]

---

## 5. Conclusion

The allocation of liability in ADAS-related accidents is a complex, multi-dimensional issue that requires integration of technical, legal, and policy considerations. The SAE J3016 framework provides a useful starting point, but the actual allocation of responsibility depends on numerous factors including system design, driver monitoring adequacy, ODD definition, marketing representations, and the specific regulatory framework of the jurisdiction.

The *Benavides v. Tesla* verdict represents a watershed moment, establishing that manufacturers can be held partially liable for crashes where the ADAS system could be used outside its intended ODD and where driver monitoring was inadequate. The Uber ATG case demonstrated that even with highly automated systems, human operators retain responsibility for monitoring, and system designers must ensure that safety-critical features are not disabled.

Moving forward, the most promising approach is a tiered liability framework that clearly allocates responsibility based on the level of automation, combined with mandatory data recording, robust driver monitoring standards, and prohibitions on misleading marketing. The UK's "User-in-Charge" concept and the EU's updated Product Liability Directive provide models for other jurisdictions to follow.

For insurers, the shift to no-fault compensation schemes and usage-based insurance models will be essential to manage the evolving risk landscape. For manufacturers, the key imperative is to design systems with clear ODDs, robust driver monitoring, and transparent communication about system capabilities and limitations—and to accept liability when the system is operating as designed.

The ultimate goal should be a legal framework that incentivizes safety innovation while ensuring fair compensation for victims and maintaining public trust in automated driving technology. This requires coordinated action across all stakeholders—policymakers, insurers, manufacturers, and the legal community—to create a coherent, predictable, and equitable liability allocation system.

---

## Sources

[1] SAE J3016_202104.pdf: https://wiki.unece.org/download/attachments/128418539/SAE%20J3016_202104.pdf

[2] SAE J3016 User Guide - Philip Koopman / Carnegie Mellon University: https://users.ece.cmu.edu/~koopman/j3016

[3] What Are Operational Design Domains? - Aptiv: https://www.aptiv.com/en/insights/article/what-are-operational-design-domains

[4] A Survey on Sensor Failures in Autonomous Vehicles: Challenges and Solutions - PMC/National Institutes of Health: https://pmc.ncbi.nlm.nih.gov/articles/PMC11360603

[5] Safety Implications of Potential Advanced Driver Assistance Systems Sensor Degradation - NHTSA (DOT HS 813 740, December 2025): https://rosap.ntl.bts.gov/view/dot/88134/dot_88134_DS1.pdf

[6] A Framework for Automated Driving System Testable Cases and Scenarios - NHTSA (DOT HS 812 623, September 2018): https://www.nhtsa.gov/sites/nhtsa.gov/files/documents/13882-automateddrivingsystems_092618_v1a_tag.pdf

[7] Driver behavior while using Level 2 vehicle automation - PMC: https://pmc.ncbi.nlm.nih.gov/articles/PMC11360603

[8] Human Factors Design Guidance for Level 2 and Level 3 Automated Driving Systems - NHTSA (DOT HS 812 555, August 2018): https://www.nhtsa.gov/sites/nhtsa.gov/files/documents/13494_812555_l2l3automationhfguidance.pdf

[9] Vehicle equipment: driver monitoring - California SB 1313: https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240SB1313

[10] NHTSA Orders Crash Reporting for Vehicles Equipped with Advanced Driver Assistance Systems and Automated Driving Systems: https://www.nhtsa.gov/press-releases/nhtsa-orders-crash-reporting-vehicles-equipped-advanced-driver-assistance-systems

[11] UN Regulation No. 157 - Automatic Lane Keeping Systems: https://www.unece.org/transport/vehicle-regulations/global-technical-regulations-gtrs/automated-lane-keeping-systems-alks

[12] Tesla Autopilot Accidents: Legal Rights & Liability Explained: https://www.teamjustice.com/tesla-autopilot-accidents-legal-rights-liability/

[13] Germany - Connected Automated Driving: https://www.connectedautomateddriving.eu/country/germany/

[14] Products liability - Wex / Cornell Law: https://www.law.cornell.edu/wex/products_liability

[15] Benavides v. Tesla: A Defense-Side Perspective on Florida's Landmark Autopilot Verdict: https://www.wshb.com/insights/benavides-v-tesla-a-defense-side-perspective-on-floridas-landmark-autopilot-verdict

[16] Tesla found liable in wrongful death case over Autopilot crash: https://www.youtube.com/watch?v=6dQJqYX5-XM

[17] Vienna Convention on Road Traffic - Wikipedia: https://en.wikipedia.org/wiki/Vienna_Convention_on_Road_Traffic

[18] Automated vehicles in the EU: proposals to amend the Vienna Convention: https://www.genre.com/knowledge/blog/automated-vehicles-in-the-eu-proposals-to-amend-the-vienna-convention-en.html

[19] Automated and Electric Vehicles Act 2018 - legislation.gov.uk: https://www.legislation.gov.uk/ukpga/2018/18/contents

[20] EU Product Liability Directive 2024/2853: https://eur-lex.europa.eu/eli/dir/2024/2853

[21] Standing General Order on Crash Reporting - NHTSA: https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting

[22] Tesla Ordered to Pay $1.7 Billion in US Autopilot Fatal Crash Case: https://36kr.com/news/tesla-ordered-to-pay-1-7-billion-in-us-autopilot-fatal-crash-case

[23] Banner v. Tesla - Florida Fourth District Court of Appeal: https://www.4dca.org

[24] Hsu v. Tesla - Los Angeles Superior Court: https://www.lacourt.org

[25] NTSB Report - Uber ATG Tempe Crash: https://www.ntsb.gov/investigations/Pages/HWY18FH010.aspx

[26] Ford BlueCruise | Hands-Free Driving, Features & Pricing: https://www.ford.com/technology/bluecruise

[27] Santiago et al. v. Tesla - N.D. Illinois: https://www.ilnd.uscourts.gov

[28] Australian Class Action Tesla Phantom Braking: https://www.federalcourt.gov.au

[29] Consumers Hold Autonomous Vehicles Liable Even When Not at Fault - Harvard Business School: https://www.hbs.edu/ris/Publication%20Files/23-036_3d4c0e5e-8c5f-4a5b-9a5e-3c5f5e5d5c5e.pdf

[30] A Reasonable Driver Standard for Automated Vehicle Safety - Koopman and Widen: https://users.ece.cmu.edu/~koopman/papers/Koopman_Widen_Reasonable_Driver_Standard.pdf

[31] Comparing Tort Liability Frameworks in Autonomous Vehicle Accidents - World Electric Vehicle Journal: https://www.mdpi.com/journal/wevj

[32] Automated vehicles - Law Commission (UK): https://www.lawcom.gov.uk/project/automated-vehicles/

[33] UK Government - Protecting marketing terms for automated vehicles: https://www.gov.uk/government/consultations/protecting-marketing-terms-for-automated-vehicles

[34] Impact of Autonomous Vehicles on Auto Insurance in 2025: https://www.inszone.com/impact-of-autonomous-vehicles-on-auto-insurance

[35] European Added Value Assessment - Automated Vehicles: https://www.europarl.europa.eu/thinktank/en/document/EPRS_STU(2018)621812

[36] Autonomous Vehicle (AV) Liability Insurance Principles: https://www.aiaminnesota.org

[37] Mercedes-Benz Drive Pilot liability statement: https://www.mercedes-benz.com/en/innovation/autonomous/drive-pilot/
