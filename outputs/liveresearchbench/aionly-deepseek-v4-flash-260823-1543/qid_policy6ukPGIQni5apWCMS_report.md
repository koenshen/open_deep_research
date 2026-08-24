# Comprehensive Analysis of U.S. State Biometric Privacy Laws: Illinois BIPA, Texas CUBI, and Washington RCW 19.375

**Prepared for:** Privacy Compliance Manager – Multi-State Biometric Data Operations  
**Date:** August 23, 2026  
**Scope:** Illinois Biometric Information Privacy Act (740 ILCS 14/1-99), Texas Capture or Use of Biometric Identifier Act (Tex. Bus. & Com. Code § 503.001), Washington Biometric Privacy Law (RCW 19.375 / HB 1493)

---

## 1. Introduction

The United States lacks a comprehensive federal biometric privacy law, leaving states to regulate the collection, use, and retention of biometric identifiers such as fingerprints, facial scans, voiceprints, and iris images. As of August 2026, only three states—Illinois, Texas, and Washington—have enacted standalone biometric privacy statutes. Each law imposes distinct consent mechanisms, penalty structures, enforcement pathways, and technology restrictions. This report provides a detailed comparison of the most current enforceable versions of these laws, including all recent amendments through the 2026 legislative sessions, and offers strategic guidance for enterprises operating across multiple jurisdictions.

The analysis draws on primary legal sources (codified statutes, official legislative histories, state attorney general guidance) and reputable secondary sources (law firm client alerts, court dockets, and legal advocacy analyses). All citations are provided in the **Sources** section with URLs where available.

---

## 2. Short Descriptions of Each Law

### 2.1 Illinois Biometric Information Privacy Act (BIPA)

**Enactment:** October 3, 2008 (P.A. 95-994), effective immediately.  
**Codification:** 740 ILCS 14/1-99.  
**Most Recent Amendment:** August 2, 2024 (SB 2979 / P.A. 103-769).  

BIPA is the oldest and most stringent U.S. biometric privacy law. It requires private entities to obtain informed written consent (including electronic signatures) before collecting biometric data, maintain a publicly available written retention and destruction policy, and store biometric data using reasonable security standards. The law prohibits selling, leasing, or trading biometric identifiers. BIPA provides a private right of action for "any person aggrieved," with statutory damages of $1,000 per negligent violation and $5,000 per intentional or reckless violation. The 2024 amendment limits damages for repeated collection of the same biometric identifier from the same person using the same method to a single recovery, and the 2026 Seventh Circuit ruling in *Clay v. Union Pacific Railroad Co.* confirmed this amendment applies retroactively to pending cases. BIPA has generated over 1,500 lawsuits and billions in settlements, making it the dominant biometric privacy litigation risk in the United States.

### 2.2 Texas Capture or Use of Biometric Identifier Act (CUBI)

**Enactment:** Originally enacted in 2001, recodified in 2009 (Tex. Bus. & Com. Code § 503.001).  
**Most Recent Amendment:** The Texas Responsible Artificial Intelligence Governance Act (TRAIGA), HB 149, signed June 22, 2025, effective January 1, 2026.  

CUBI prohibits capturing a biometric identifier for a commercial purpose without first informing the individual and receiving consent. Unlike BIPA, CUBI does not require written consent—only notice and consent. It is enforced exclusively by the Texas Attorney General, with civil penalties of up to $25,000 per violation. The TRAIGA amendments added exemptions for AI model training and security/fraud prevention, and clarified that publicly available content does not constitute consent. The Texas AG has secured two landmark settlements: $1.4 billion from Meta (2024) and $1.375 billion from Google (2025) for alleged CUBI violations. There is no private right of action under CUBI, and no class action litigation has arisen from the statute.

### 2.3 Washington Biometric Privacy Law (HB 1493 / RCW 19.375)

**Enactment:** May 16, 2017, effective July 23, 2017.  
**Codification:** RCW 19.375.010–19.375.900.  
**Amendments:** None as of August 2026.  

Washington’s law is the most narrowly tailored of the three. It regulates only the "enrollment" of biometric identifiers (conversion into a reference template stored in a database) for a "commercial purpose" (defined as sale or disclosure to third parties for marketing unrelated to the initial transaction). It requires notice and consent before enrollment, but excludes photographs, video, and audio recordings from the definition of biometric identifiers, significantly limiting its application to facial recognition. Enforcement is solely by the Washington Attorney General under the Consumer Protection Act (CPA), with no private right of action. However, the separate Washington My Health My Data Act (MHMDA, effective 2024) provides a private right of action for biometric data classified as consumer health data, creating a new litigation avenue. No RCW 19.375-specific enforcement actions or class actions have been brought as of August 2026.

---

## 3. Multi-Column Comparison Table

| Dimension | Illinois BIPA (740 ILCS 14/1-99) | Texas CUBI (Tex. Bus. & Com. Code § 503.001) | Washington RCW 19.375 |
|-----------|----------------------------------|-----------------------------------------------|------------------------|
| **Enactment Year** | 2008 | 2001 (recodified 2009) | 2017 |
| **Most Recent Amendment** | August 2, 2024 (SB 2979) – limits per-scan damages, allows electronic signatures | January 1, 2026 (TRAIGA, HB 149) – AI training exemption, clarifies public availability ≠ consent | None |
| **Consent Mechanism** | Opt-in: informed written notice (specific purpose + retention term) + signed release (written or electronic signature) before collection | Opt-in: inform individual before capture + receive consent (no written requirement) | Opt-in for enrollment: notice + consent or mechanism to prevent subsequent use; security purpose exempted |
| **Notice Requirements** | Written notice of collection, purpose, retention term; public written retention/destruction policy | Notice before capture (no written form required); no statutory policy requirement | Notice reasonably designed to be readily available; no written policy mandate |
| **Opt-In vs. Opt-Out** | Opt-in (affirmative written consent) | Opt-in (affirmative consent, no written form) | Opt-in for enrollment; opt-out mechanism for subsequent commercial use permitted |
| **Private Right of Action** | Yes – any aggrieved person in state or federal court (supplemental claim) | No – only Texas Attorney General | No – only Washington AG under CPA; but MHMDA provides private right of action for biometric health data |
| **Who Can Enforce** | Private individuals (class actions) + state courts | Texas Attorney General only | Washington Attorney General only |
| **Statutory Damages** | $1,000 negligent; $5,000 intentional/reckless per violation; actual damages if greater; attorneys' fees | Up to $25,000 per violation (no minimum, no cap); AG can aggregate | None (CPA penalties: up to $7,500 per violation; treble damages up to $25,000 in private CPA actions, but RCW 19.375 limits enforcement to AG) |
| **Per-Scan / Per-Collection Calculation** | Prior to 2024 amendment: each scan = separate claim (Cothron v. White Castle). 2024 amendment: single violation for same person, same method. Retroactive per Clay v. Union Pacific (7th Cir. 2026) | Not explicitly defined; AG has argued collection + storage = two violations ($50,000 potential per instance) | Not applicable – applies only to enrollment, not each scan |
| **Damage Caps** | No cap on total damages, but single recovery per person per method per identifier | No cap; AG can aggregate across millions of individuals | CPA penalties capped at $7,500 per violation; treble damages up to $25,000 in private actions (but not available under RCW 19.375) |
| **Biometric Identifiers Covered** | Fingerprint, retina/iris scan, voiceprint, hand/face geometry | Biometric identifier (not defined in statute; interpreted broadly to include fingerprints, face scans, etc.) | Fingerprint, voiceprint, eye retinas/irises, "other unique biological patterns or characteristics" used to identify specific individual |
| **Excluded Data Types** | Writing samples, photographs, X-rays, medical images, health info under HIPAA | None explicitly excluded; AI model training and security purposes exempted | Photographs, video/audio recordings, data generated therefrom; HIPAA-related data; unenrolled identifiers |
| **Facial Recognition Coverage** | Yes – face geometry is explicitly included | Yes – AG enforcement against Meta (facial recognition) | No – photographs and video recordings excluded; separate SB 6280 regulates government use |
| **Data Retention Requirement** | Destroy when purpose satisfied or within 3 years of last interaction, whichever first | No explicit retention period; TRAIGA requires possession/destruction if later used for commercial purpose | Retain no longer than reasonably necessary for the purpose |
| **Security Requirement** | Reasonable standard of care | Not explicitly stated in statute | Reasonable care to guard against unauthorized access |
| **Sale/Profit Prohibition** | Yes – cannot sell, lease, trade, or profit from biometric data | Not explicitly prohibited (but AG has used DTPA claims) | Cannot sell, lease, or disclose for commercial purpose without consent (exceptions apply) |
| **Preemption/Exemptions** | Financial institutions (GLBA), HIPAA, government contractors, law enforcement | Financial institutions (GLBA), HIPAA, law enforcement; AI training (TRAIGA) | Financial institutions (GLBA), HIPAA, law enforcement; security purposes |
| **Statute of Limitations** | 5 years (Tims v. Black Horse Carriers, 2023 IL 127801) | Likely 2 years (trespass to personal rights) | Not specified; likely 4 years under CPA |

---

## 4. Real-World Enforcement Cases and Class Action Examples

### 4.1 Illinois BIPA

#### 4.1.1 Retail Context

**a. Target (March 2024)**  
A class action was filed in Cook County Circuit Court alleging Target violated BIPA by using surveillance systems with facial recognition technology as part of anti-theft efforts, surreptitiously collecting biometric data from customers without knowledge or written consent. Target operates 14 investigation centers and two forensic labs to analyze video and fingerprints. The suit seeks $5,000 per intentional violation [1].

**b. Macy’s – *Carmine v. Macy’s Retail Holdings, Inc.* (No. 1:20-cv-04589, N.D. Ill.)**  
Filed August 2020, alleging Macy’s used Clearview AI’s facial recognition database to identify and track shoppers in Illinois. Macy’s ran identities of over 6,000 customers through Clearview’s database of billions of scraped photos. The suit claims Macy’s failed to inform individuals, provide a retention policy, or obtain written releases. The proposed class includes all Illinois residents whose biometric data is in Clearview’s database and was provided to Macy’s [2].

**c. Home Depot (September 2019)**  
A proposed class action alleged Home Depot’s facial recognition security cameras at all 76 Illinois stores surreptitiously collect and store shoppers’ faceprints without informed consent. The system tracks customers from entry through checkout. Plaintiffs seek up to $5,000 per violation [3]. Home Depot has also been accused of selling shoppers’ personal data (Belleville News-Democrat, August 2026) [4].

**d. Walmart (January 2021)**  
Walmart reached a $10 million settlement with employees in a BIPA class action alleging the company forced employees to use a palm scanner at cash registers without written consent. The class covers up to 21,677 employees who used scanners between January 28, 2014, and the end dates of use (Walmart: Feb 28, 2018; Sam’s Club: Apr 24, 2019). Each employee received approximately $461.32 [5].

#### 4.1.2 Healthcare Context

**e. *McDonald v. Symphony Bronzeville Park, LLC* (2022 IL 126511)**  
The Illinois Supreme Court unanimously held that the Workers’ Compensation Act’s exclusivity provisions do not bar BIPA claims when an employer is alleged to have violated statutory privacy rights. The case involved a nursing home employee who used a biometric timekeeping system. The court found BIPA violations are fundamentally different from physical workplace injuries [6].

**f. *Mosby v. Ingall Memorial Hospital***  
Clarified that BIPA’s healthcare exemptions apply to employees as well as patients, limiting the scope of BIPA in certain healthcare settings [7].

#### 4.1.3 Workplace Context

**g. *Rogers v. BNSF Railway Co.* (No. 1:19-cv-03083, N.D. Ill.)**  
The first BIPA case to go to trial. In October 2022, a jury found BNSF intentionally violated BIPA by scanning fingerprints of 45,600 truck drivers without consent at four Illinois railyards. The jury awarded $228 million ($5,000 per violation). In June 2023, Judge Kennelly vacated the award, ruling damages are discretionary. The parties ultimately settled for $75 million in 2024, with final approval in June 2024 and payments mailed in February 2025 [8].

**h. *Cothron v. White Castle System, Inc.* (2023 IL 128004)**  
The Illinois Supreme Court held that a separate claim accrues under BIPA each time a private entity scans or transmits biometric data. White Castle faced potential class-wide damages exceeding $17 billion for 9,500 employees. The 2024 amendment (SB 2979) retroactively limited damages to a single recovery per person per method, as confirmed by the Seventh Circuit in *Clay v. Union Pacific* (April 2026) [9].

**i. Facebook (Meta) – *In re Facebook Biometric Information Privacy Litigation* (No. 3:15-cv-03747-JD, N.D. Cal.)**  
Facebook settled for $650 million in 2020 over its "Tag Suggestion" facial recognition feature, which allegedly extracted biometric data from up to six million Illinois users without consent. Final approval was granted in February 2021, with class members receiving approximately $397 per person. Facebook discontinued its facial recognition feature in November 2021 [10].

**j. Clearview AI Settlements**  
Two major settlements: (1) A $51.75 million settlement approved March 2025 gave class members a 23% equity stake in Clearview AI, with no cash payout and no requirement to stop collecting biometric data. (2) A separate $50 million settlement approved May 2025. Both were opposed by 22 state attorneys general. An earlier ACLU settlement compelled Clearview to comply with BIPA and banned its database access for most businesses [11].

**k. Amazon – *Svoboda v. Amazon.com Inc.* (No. 25-1361, 7th Cir., Dec. 17, 2025)**  
The Seventh Circuit affirmed certification of a BIPA class against Amazon for its "virtual try-on" (VTO) technology, which uses augmented reality to overlay makeup and eyewear on user images, allegedly capturing facial geometry without consent. The class includes over 100,000 individuals [12].

**l. Motorola Solutions / Vigilant Solutions – *Simmons v. Motorola Solutions* (Loevy + Loevy)**  
A $47.5 million settlement was reached over the "FaceSearch" facial recognition technology, which used police booking photos without BIPA compliance. Final approval was granted September 15, 2025, with class members receiving $200–$550 each [13].

**m. Other Notable Settlements**  
- TikTok: $92 million (2021)  
- Google: $100 million (2022)  
- ADP: $25 million settlement ($8.75 million in attorneys’ fees)  
- Pret A Manger: $677,000 (workplace fingerprint time clock)  
- Accu-Time Systems: $1.5 million settlement (final approval April 2026)  
- WorkEasy Software: $1.69 million settlement (final approval April 2026, appeal pending)

### 4.2 Texas CUBI

#### 4.2.1 Enforcement Actions by Texas Attorney General

**a. Texas v. Meta Platforms, Inc. (2024)**  
The Texas Attorney General secured a $1.4 billion settlement with Meta for alleged violations of CUBI and the Texas Deceptive Trade Practices Act (DTPA). The lawsuit alleged Meta captured and used biometric data from millions of Texans without consent through its facial recognition technology (Tag Suggestions). This was the first lawsuit and settlement under CUBI [14].

**b. Texas v. Google LLC (2025)**  
Texas entered into a $1.375 billion settlement with Google for alleged violations of CUBI and the DTPA. The settlement addressed claims that Google collected biometric data (including voiceprints and face scans) through its products without proper notice and consent. This was the second major CUBI settlement [15].

**c. No Private Class Actions**  
Because CUBI lacks a private right of action, no class action lawsuits have been filed under the statute. All enforcement is conducted exclusively by the Texas Attorney General.

#### 4.2.2 Common Law Privacy Torts as Alternative Avenues

While CUBI does not provide a private right of action, Texas recognizes common law torts of **intrusion upon seclusion** and **misappropriation of name or likeness**, which could potentially be used by individuals alleging biometric privacy violations. The statute of limitations for these torts is two years. However, no significant biometric privacy class actions have been brought under these theories in Texas.

### 4.3 Washington RCW 19.375

#### 4.3.1 No RCW 19.375-Specific Enforcement Actions

As of August 2026, no enforcement actions have been filed by the Washington Attorney General specifically under RCW 19.375. The law has not generated significant litigation due to its narrow scope and lack of private right of action.

#### 4.3.2 My Health My Data Act (MHMDA) – First Lawsuit

**a. *Maxwell v. Amazon.com, Inc.* (Filed Feb 10, 2025)**  
The first class action complaint under the Washington My Health My Data Act (MHMDA) alleged Amazon collected consumer health data—including biometric data and precise location—through its SDKs in mobile apps without proper consent. The MHMDA provides a private right of action for biometric data classified as consumer health data, with treble damages up to $25,000. This case is pending [16].

#### 4.3.3 Clearview AI Multidistrict Litigation (Involving Washington)

The $51.75 million Clearview AI settlement (discussed under Illinois) resolved claims from multiple states, including Washington. The settlement provided an equity stake rather than cash, and was approved in March 2025. This is not a Washington-specific enforcement action.

---

## 5. Strategic Implications for Multi-State Biometric Data Operations

### 5.1 Compliance Conflicts and Gaps

Enterprises operating across Illinois, Texas, and Washington face a patchwork of requirements that create significant compliance challenges:

1. **Consent Form Divergence:** Illinois requires a **written release** (now including electronic signatures) with specific disclosures about purpose and retention. Texas requires only **notice and consent**, with no written form mandated. Washington requires only **notice and consent upon enrollment** for commercial purposes, with a security exemption. A single biometric time-tracking system deployed across all three states must be configured to meet the highest standard (Illinois) while ensuring lower standards do not create gaps (e.g., failing to provide notice in Texas or Washington where no written release is required).

2. **Enrollment vs. Collection:** Washington only regulates **enrollment** (conversion to a reference template), not mere collection or capture. Illinois and Texas regulate **collection** broadly. This means a facial recognition system that captures but does not enroll a biometric identifier (e.g., real-time analysis without storing a template) may be outside Washington’s scope but still subject to BIPA and CUBI.

3. **Private Right of Action Risk:** The most significant operational risk is in Illinois, where BIPA provides a private right of action and has produced over 1,500 lawsuits. Texas and Washington (under RCW 19.375) lack private rights of action, but the Washington MHMDA now provides a private right of action for biometric health data. Enterprises must assess whether their biometric data qualifies as "consumer health data" under MHMDA, which could create Washington class action exposure comparable to BIPA.

4. **Penalty Exposure:** Illinois’ per-violation damages ($1,000/$5,000) are capped by the 2024 amendment to a single recovery per person per method, but the absence of a total cap means class action exposure can still reach hundreds of millions. Texas’ $25,000 per violation penalty, while higher per violation, is only enforceable by the AG, reducing aggregate risk absent AG action. Washington has no statutory damages under RCW 19.375, but the CPA provides up to $7,500 per violation in AG enforcement, and MHMDA provides treble damages up to $25,000 in private actions.

### 5.2 Risk Management Strategies

1. **Adopt a Single Highest Standard Across All States:** Implement BIPA-level compliance nationwide—written notice with specific purpose and retention term, written consent (electronic signature acceptable), publicly available retention/destruction policy, and reasonable security standards. This minimizes the risk of a multi-state rollout inadvertently violating Illinois law while easily satisfying Texas and Washington requirements.

2. **Vendor Management:** Under BIPA, businesses remain liable for third-party biometric technology providers (e.g., time clock vendors). Ensure contracts require vendors to comply with BIPA, CUBI, and Washington law, and include indemnification and audit rights. The *BNSF Railway* case illustrates that companies cannot delegate BIPA compliance to contractors.

3. **Data Retention and Destruction:** Implement a uniform policy to destroy biometric data within three years of the individual’s last interaction (Illinois’ strictest requirement) or as soon as the purpose is satisfied, whichever is sooner. This ensures compliance with Illinois and Washington’s “reasonably necessary” standard.

4. **Insurance Coverage Audit:** Review general liability and cyber insurance policies for biometric privacy exclusions. Following *West Bend Mutual Ins. Co. v. Krishna Schaumburg Tan, Inc.* (2021 IL 125978), BIPA claims may be covered under "publication" provisions, but insurers are increasingly adding explicit biometric data exclusions. The 2026 *Clay v. Union Pacific* ruling may also affect insurer-insured litigation over prior settlements.

5. **Monitor for Private Right of Action Expansion:** Texas and Washington may amend their laws to add private rights of action. The failed Texas HB 4705 (2023) would have added a private right of action under CUBI. Washington’s People’s Privacy Act (HB 1671, proposed 2025) would add a private right of action for biometrics under the CPA. Compliance teams should track legislative developments and prepare for potential litigation.

### 5.3 Operational Recommendations

1. **Conduct a Biometric Data Inventory:** Identify all systems that collect, capture, store, or transmit biometric identifiers (fingerprint time clocks, facial recognition cameras, voiceprint authentication, iris scanners, etc.). Categorize by purpose (workplace time tracking, security, customer analytics, marketing) and jurisdiction.

2. **Implement a Consent Management Platform:** For consumer-facing systems (e.g., facial recognition at retail stores), deploy a digital consent workflow that captures electronic signatures meeting Illinois’ requirements. For employee-facing systems, integrate consent into onboarding and HRIS workflows.

3. **Update Privacy Policies:** Illinois requires a publicly available written policy on biometric data retention and destruction. Ensure this policy is posted on company websites and at physical locations where biometric data is collected.

4. **Train Employees on BIPA Requirements:** The most common source of BIPA litigation is employer-employee disputes over time clocks. Train HR and operations staff on the need for written consent before the first scan, proper disclosure of purpose and retention, and data security obligations.

5. **Engage Legal Counsel for Multi-State Strategy:** Given the complexity and evolving nature of these laws, retain privacy counsel with expertise in all three jurisdictions. Consider a single compliance framework that satisfies the most stringent requirements (Illinois) to create a safe harbor across all states.

6. **Prepare for MHMDA Litigation in Washington:** With the first MHMDA class action filed in 2025, Washington is emerging as a second frontier for biometric privacy litigation. Enterprised that use biometric data in consumer health contexts (e.g., fitness apps, wellness programs, healthcare facilities) should treat MHMDA compliance as a priority equal to BIPA.

---

## 6. Conclusion

The biometric privacy landscape in the United States is dominated by Illinois’ BIPA, which continues to generate the most litigation and highest settlements. Texas’ CUBI, while carrying a higher per-violation penalty ($25,000), is enforced only by the Attorney General and has not produced private class actions. Washington’s RCW 19.375 is the most narrowly tailored, but the separate My Health My Data Act now provides a private right of action for biometric health data, creating a new wave of litigation risk.

For enterprises with multi-state biometric data operations, the pragmatic approach is to adopt BIPA-level compliance as a baseline, invest in vendor management and insurance, and monitor legislative developments in Texas and Washington for potential private right of action expansions. The 2024 BIPA amendment and the 2026 *Clay v. Union Pacific* ruling provide some relief from annihilative per-scan damages, but the overall risk environment remains challenging, particularly for workplace biometric time-tracking systems.

---

## Sources

[1] Target class-action lawsuit claims retailer violated Illinois' privacy law – NBC Chicago: https://www.nbcchicago.com/news/local/target-hit-with-class-action-lawsuit-claiming-it-violated-illinois-biometric-privacy-law/3410850

[2] Class Action Claims Macy's Used Clearview AI Database to Identify, Track Illinois Shoppers – ClassAction.org: https://www.classaction.org/news/class-action-claims-macys-used-clearview-ai-database-to-identify-track-illinois-shoppers

[3] Class Action Claims Home Depot Facial Recognition Security Cameras Violate Illinois Privacy Law – ClassAction.org: https://www.classaction.org/news/class-action-claims-home-depot-facial-recognition-security-cameras-violate-illinois-privacy-law

[4] Home Depot accused of selling shoppers' personal data – Belleville News-Democrat: https://www.facebook.com/BellevilleND/posts/home-depot-accused-of-selling-shoppers-personal-data-to-boost-profit/1625719939561529

[5] Walmart Reaches $10M Settlement with Employees in Class Action BIPA Lawsuit – ID Tech Wire: https://idtechwire.com/walmart-reaches-10-million-settlement-employees-class-action-bipa-lawsuit-011907

[6] McDonald v. Symphony Bronzeville Park, LLC (2022 IL 126511) – Justia: https://law.justia.com/cases/illinois/supreme-court/2022/126511.html

[7] BIPA Update: Illinois Limits Liability and Clarifies Electronic Consent – Greenberg Traurig: https://www.gtlaw.com/en/insights/2024/8/bipa-update-illinois-limits-liability-and-clarifies-electronic-consent-for-biometric-data-collection

[8] Rogers v. BNSF Railway Company Settlement Website: https://bnsfbipaclassaction.com

[9] Cothron v. White Castle System, Inc. (2023 IL 128004) – Justia: https://law.justia.com/cases/illinois/supreme-court/2023/128004.html

[10] In re Facebook Biometric Info. Privacy Litig. (No. 3:15-cv-03747-JD, N.D. Cal.) – Robbins Geller: https://www.rgrdlaw.com/cases-in-re-facebook-biometric-info-privacy-litig.html

[11] Clearview AI USD 51.75 Million Class Action Settlement Approved – ICLG: https://iclg.com/news/22418-clearview-ai-usd-51-75-million-class-action-settlement-approved

[12] Seventh Circuit Affirms Certification of BIPA Class Comprised of Customers Who Used Amazon's "Virtual Try-On" Tool – Duane Morris: https://blogs.duanemorris.com/classactiondefense/2025/12/30/seventh-circuit-affirms-certification-of-bipa-class-comprised-of-customers-who-used-amazons-virtual-try-on-tool

[13] Motorola Class Action – Loevy + Loevy: https://www.loevy.com/class-actions/privacy-bipa/motorola-class-action

[14] Texas Attorney General Secures $1.4 Billion Settlement with Meta – Texas Attorney General: https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-14-billion-settlement-meta-over-its-unauthorized-capture

[15] Texas Attorney General Secures $1.375 Billion Settlement with Google – Texas Attorney General (press release, 2025): https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-1375-billion-settlement-google

[16] First Lawsuit Filed Under Washington's My Health My Data Act – Orrick: https://www.orrick.com/en/Insights/2025/02/First-Lawsuit-Filed-Under-Washingtons-My-Health-My-Data-Act

[17] 2025 Illinois Compiled Statutes – 740 ILCS 14/ Biometric Information Privacy Act – Justia: https://law.justia.com/codes/illinois/chapter-740/act-740-ilcs-14

[18] Texas Business & Commerce Code § 503.001 – FindLaw (current as of 2026): https://codes.findlaw.com/tx/business-and-commerce-code/tex-bus-and-com-code-sect-503-001/

[19] Washington State Legislature – Chapter 19.375 RCW: https://app.leg.wa.gov/RCW/default.aspx?cite=19.375

[20] Clay v. Union Pacific Railroad Co. (No. 25-2185, 7th Cir. Apr. 1, 2026) – Discussion via Davis Wright Tremaine: https://www.dwt.com/blogs/privacy--security-law-blog/2024/08/illinois-bipa-biometrics-law-amended-for-damages

[21] BIPA Amendment Bill Signed into Law – Byte Back Law: https://www.bytebacklaw.com/2024/08/bipa-amendment-bill-signed-into-law

[22] An Analysis of Cases Brought Under Illinois' State Biometrics Law – Chamber of Progress: https://progresschamber.org/wp-content/uploads/2023/03/Who-Benefits-from-BIPA-Analysis-of-Cases-Under-IL-Biometrics-Law.pdf

[23] Update: Seventh Circuit Holds That BIPA Amendment Limiting Damages Applies Retroactively – Davis Wright Tremaine: https://www.dwt.com/blogs/privacy--security-law-blog/2024/08/illinois-bipa-biometrics-law-amended-for-damages

[24] BIPA Cases: 7th Circuit Rules Change to Illinois Law's Damages Provision Retroactively Limits Defendant Exposure – Jackson Lewis: https://www.jacksonlewis.com/insights/bipa-cases-7th-circuit-rules-change-illinois-laws-damages-provision-retroactively-limits-defendant-exposure

[25] Texas Responsible Artificial Intelligence Governance Act (TRAIGA), HB 149 – Texas Legislature: https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=HB149

[26] Washington My Health My Data Act – RCW 19.373: https://app.leg.wa.gov/RCW/default.aspx?cite=19.373

[27] Biometric Information Privacy – Statutes, Claims and Litigation [Update] – Gen Re: https://www.genre.com/us/knowledge/publications/2024/january/biometric-information-privacy-statutes-claims-and-litigation-update-en

[28] Biometric Backlash: The Rising Wave of Litigation Under BIPA and Beyond – Epstein Becker Green: https://www.ebglaw.com/commercial-litigation-update/biometric-backlash-the-rising-wave-of-litigation-under-bipa-and-beyond

[29] 2025 Year-In-Review: Biometric Privacy Litigation – Squire Patton Boggs: https://www.privacyworld.blog/2025/12/2025-year-in-review-biometric-privacy-litigation

[30] West Bend Mutual Ins. Co. v. Krishna Schaumburg Tan, Inc. (2021 IL 125978) – Justia: https://law.justia.com/cases/illinois/supreme-court/2021/125978.html

[31] A BAD MATCH: ILLINOIS AND THE BIOMETRIC INFORMATION PRIVACY ACT – Institute for Legal Reform: https://instituteforlegalreform.com/wp-content/uploads/2021/10/ILR-BIPA-Briefly-FINAL.pdf

[32] U.S. biometric laws & pending legislation tracker – BCLP: https://www.bclplaw.com/en-US/events-insights-news/us-biometric-laws-and-pending-legislation-tracker.html

[33] EPIC Testimony on Washington People's Privacy Act (HB 1671) – EPIC: https://epic.org/documents/testimony-on-washington-peoples-privacy-act-hb-1671

[34] Biometric Data, Privacy Rules, Washington State – CaseGuard: https://caseguard.com/articles/washington-revised-code-ann-19375020

[35] Washington's New Biometric Privacy Law: What Businesses Need to Know – Davis Wright Tremaine: https://www.dwt.com/insights/2017/07/washingtons-new-biometric-privacy-law-what-busines

[36] Diving into the Washington My Health My Data Act: Part 7 – Quarles: https://www.quarles.com/newsroom/publications/diving-into-the-washington-my-health-my-data-act-7

[37] $1.5M Accu-Time Settlement Ends Litigation Over Alleged Biometric Data Collection – ClassAction.org: https://www.classaction.org/news/1.5m-accu-time-settlement-ends-litigation-over-alleged-biometric-data-collection

[38] Illinois Fingerprint Time Clock $1.69M Settlement (WorkEasy) – ClaimDepot: https://www.claimdepot.com/settlements/easyworkforce-bipa-lawsuit

[39] BIPA Compliance for Schaumburg Employers: Fingerprint Timeclocks and Facial Recognition – M&A Law Firm, P.C.: https://malawillinois.com/bipa-compliance-for-schaumburg-employers-fingerprint-timeclocks-and-facial-recognition

[40] Seventh Circuit Confirms BIPA Amendment Has Retroactive Application – Paul Hastings: https://www.paulhastings.com/insights/ph-privacy/7th-circuit-confirms-bipa-amendment-has-retroactive-application
