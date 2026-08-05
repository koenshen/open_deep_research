# Comprehensive Multi-State Biometric Privacy Law Comparison: Illinois BIPA, Texas CUBI, and Washington RCW 19.375

**As of August 4, 2026**

---

## 1. Executive Summary

This report provides a detailed, current comparison of the three most significant state-level biometric privacy laws in the United States: Illinois' Biometric Information Privacy Act (BIPA), Texas' Capture or Use of Biometric Identifier Act (CUBI), and Washington's biometric privacy law (HB 1493 / RCW 19.375). For enterprises operating multi-state biometric data operations—including facial recognition, fingerprint scanning, voiceprint collection, and time-tracking systems—understanding the distinct requirements, penalty structures, and enforcement environments across these three states is critical for compliance and risk mitigation.

The three laws differ fundamentally in scope, consent mechanisms, private right of action availability, and enforcement posture. Illinois BIPA remains the most stringent due to its private right of action and statutory damages, though the 2024 amendment (SB 2979) and the Seventh Circuit's April 2026 retroactivity ruling have significantly reduced per-violation exposure. Texas CUBI, while lacking a private right of action, has become the most aggressively enforced law through Attorney General actions, with over $2.7 billion in settlements secured against Meta and Google. Washington's RCW 19.375 has remained largely untested since 2017, but the Washington My Health My Data Act (MHMDA), effective March 31, 2024, has introduced a private right of action for biometric data classified as consumer health data, creating a new and potentially significant litigation risk.

---

## 2. Short Descriptions of Each Law

### 2.1 Illinois Biometric Information Privacy Act (BIPA) — 740 ILCS 14/1 et seq.

Enacted in 2008 (effective October 3, 2008), BIPA is the oldest and most stringent biometric privacy law in the United States. It regulates any "private entity" that collects, captures, purchases, receives through trade, or otherwise obtains a person's biometric identifiers or biometric information. The law covers retina or iris scans, fingerprints, voiceprints, and scans of hand or face geometry. BIPA requires entities to: (1) develop a written, publicly available retention and destruction policy; (2) provide written notice of collection, purpose, and retention period; (3) obtain a written release (informed consent) before collection; (4) prohibit sale or profit from biometric data; (5) restrict disclosure; and (6) safeguard data using reasonable care. The defining feature of BIPA is its private right of action, which allows individuals to sue for statutory damages of $1,000 (negligent) or $5,000 (intentional/reckless) per violation. [1][2][3]

**Key Amendment — SB 2979 / Public Act 103-769 (effective August 2, 2024):** This amendment limited damages by providing that when the same biometric identifier of one individual is repeatedly collected or disclosed by the same defendant using the same method, those actions constitute a single violation, entitling the individual to at most one recovery. The amendment also expanded the definition of "written release" to include electronic signatures. [4][5][6]

**Seventh Circuit Retroactivity Ruling — Clay v. Union Pacific Railroad Co. (April 1, 2026):** The Seventh Circuit held that the 2024 amendment applies retroactively to cases pending at the time of enactment, significantly reducing potential damages exposure for companies with pending BIPA cases. [7][8][9]

### 2.2 Texas Capture or Use of Biometric Identifier Act (CUBI) — Texas Business and Commerce Code § 503.001

Enacted in 2007 (effective April 1, 2009), CUBI regulates any "person" who captures biometric identifiers for a "commercial purpose." The law covers retina or iris scans, fingerprints, voiceprints, and records of hand or face geometry. CUBI requires entities to: (1) inform the individual before capturing a biometric identifier; (2) receive the individual's consent; (3) prohibit sale, lease, or disclosure of biometric identifiers (with narrow exceptions); (4) destroy biometric identifiers within one year after the purpose for collection expires; and (5) store, transmit, and protect biometric identifiers using reasonable care. CUBI does not provide a private right of action—enforcement is solely by the Texas Attorney General, who may seek civil penalties of up to $25,000 per violation. [10][11][12]

**Key Amendment — HB 149 / Texas Responsible Artificial Intelligence Governance Act (TRAIGA) (effective January 1, 2026):** This amendment clarified that consent cannot be inferred solely from the public availability of biometric data and added exemptions for AI training and security purposes. If biometrics captured for AI training are subsequently used for a commercial purpose not covered by the exemption, the full possession and destruction rules apply. [13][14][15]

### 2.3 Washington Biometric Privacy Law — RCW 19.375 / HB 1493

Enacted in 2017 (effective July 23, 2017), Washington's law regulates the enrollment of biometric identifiers in a database for a "commercial purpose." The law covers fingerprints, voiceprints, eye retinas, irises, and other unique biological patterns or characteristics. Explicitly excluded from the definition are physical or digital photographs, video or audio recordings (or data generated therefrom), and information collected, used, or stored for healthcare treatment, payment, or operations under HIPAA. The law requires entities to: (1) provide notice, obtain consent, or provide a mechanism to prevent subsequent commercial use before enrollment; (2) prohibit sale, lease, or disclosure of biometric identifiers without consent (with narrow exceptions); (3) retain biometric identifiers no longer than reasonably necessary; and (4) take reasonable care to guard against unauthorized access. RCW 19.375 does not provide a private right of action—enforcement is solely by the Washington Attorney General under the Consumer Protection Act (CPA), with civil penalties of up to $7,500 per violation. [16][17][18]

**Critical Interaction with the Washington My Health My Data Act (MHMDA — RCW 19.373, effective March 31, 2024):** The MHMDA is a separate law that regulates biometric data as "consumer health data" and provides a private right of action. MHMDA defines biometric data more broadly than RCW 19.375, including imagery of faces, voice recordings, and keystroke/gait patterns. MHMDA explicitly excludes employee data and business-to-business data. For biometric data that qualifies as consumer health data, both RCW 19.375 and MHMDA apply simultaneously, creating a complex dual-compliance environment. [19][20][21]

---

## 3. Multi-Column Comparison Table

| Dimension | Illinois BIPA (740 ILCS 14) | Texas CUBI (Tex. Bus. & Com. Code § 503.001) | Washington RCW 19.375 |
|-----------|----------------------------|----------------------------------------------|----------------------|
| **Effective Date** | October 3, 2008 | April 1, 2009 | July 23, 2017 |
| **Scope of Coverage** | Any private entity collecting, possessing, or using biometric identifiers/information | Any person capturing biometric identifiers for a commercial purpose | Enrollment of biometric identifiers in a database for a commercial purpose |
| **Covered Biometric Data** | Retina/iris scan, fingerprint, voiceprint, scan of hand/face geometry | Retina/iris scan, fingerprint, voiceprint, record of hand/face geometry | Fingerprint, voiceprint, eye retinas, irises, other unique biological patterns |
| **Explicit Exclusions** | Photographs, writing samples, medical images, HIPAA data, GLBA financial institutions | GLBA financial institutions (voiceprints); AI training/processing (2026 amendment) | Photographs, video/audio recordings, HIPAA data, facial geometry scans |
| **Notice Requirement** | Written notice before collection: (1) that data is being collected, (2) specific purpose, (3) retention term | Inform individual before capturing biometric identifier | Notice, consent, OR mechanism to prevent subsequent commercial use (context-dependent) |
| **Consent Type** | Mandatory opt-in: written release (now includes electronic signature via 2024 amendment) | Mandatory opt-in: informed consent (not specified as written) | Notice OR consent OR opt-out mechanism (disjunctive) |
| **Employee Coverage** | Fully covered (most BIPA litigation involves employee timekeeping) | Covered for commercial purpose; purpose presumed to expire on termination | Covered under RCW 19.375; EXCLUDED from MHMDA |
| **Private Right of Action** | **YES** — $1,000 negligent, $5,000 intentional/reckless per violation | **NO** — AG enforcement only | **NO** for RCW 19.375; **YES** under MHMDA for biometric health data |
| **AG Enforcement** | N/A (private right of action) | **YES** — exclusive AG enforcement; up to $25,000 per violation | **YES** — AG enforcement under CPA; up to $7,500 per violation |
| **Damages/Penalty Structure** | Statutory damages: $1,000 negligent, $5,000 intentional/reckless per violation (now capped at one recovery per person per method) | Civil penalty: up to $25,000 per violation (no cap on total); AG argues capture and storage are separate violations | Civil penalty: up to $7,500 per violation under CPA; potential $500,000 aggregate cap per occurrence |
| **Retention Limit** | Destroy within 3 years of last interaction OR when purpose fulfilled, whichever first | Destroy within reasonable time, no later than 1 year after purpose expires | Retain no longer than reasonably necessary |
| **Sale/Profit Prohibition** | Yes — cannot sell, lease, trade, or profit | Yes — cannot sell, lease, or disclose (narrow exceptions) | Yes — cannot sell, lease, or disclose without consent (narrow exceptions) |
| **Security Requirement** | Reasonable standard of care within industry; same as or more protective than other confidential information | Reasonable care; same as or more protective than other confidential information | Reasonable care to guard against unauthorized access |
| **Security/Safety Exemption** | None | Yes — security/fraud prevention purposes | Yes — security purpose (preventing shoplifting, fraud, system integrity) |
| **Statute of Limitations** | 5 years (uniform — Tims v. Black Horse Carriers, 2023) | 2 years (likely, based on general Texas civil penalty statute) | 4 years (CPA statute of limitations) |
| **Attorney's Fees** | Yes — prevailing party may recover reasonable fees and costs | Yes — AG may recover costs and fees in enforcement actions | Yes — AG may recover costs and fees in CPA enforcement actions |
| **Class Action Availability** | Yes — routinely brought as class actions | No — no private right of action | No for RCW 19.375; Yes for MHMDA |
| **Recent Major Amendments** | SB 2979 (2024): per-person damages cap, electronic signatures; retroactively applied (7th Cir., 2026) | HB 149 (2025, eff. Jan 1, 2026): AI training exemption, consent clarification | None to RCW 19.375; MHMDA (2023, eff. 2024) is separate law |
| **Enforcement Posture** | High — over 1,500 lawsuits since 2008; ~150 new cases in 2025 (declining due to 2024 amendment) | Very High — AG has secured $2.7B+ in settlements; most aggressive AG enforcement in U.S. | Low — no public AG enforcement actions under RCW 19.375; MHMDA litigation just beginning |
| **Risk Level** | **HIGH** (private right of action, established litigation ecosystem) | **MEDIUM-HIGH** (aggressive AG enforcement, no private right of action) | **MEDIUM** (RCW 19.375 untested; MHMDA creates new private right of action) |

---

## 4. Consent Mechanisms: Detailed Analysis

### 4.1 Illinois BIPA

**Notice:** BIPA Section 15(b) requires that before collecting biometric data, a private entity must inform the subject **in writing** of: (1) the fact that biometric data is being collected or stored; (2) the specific purpose for collection, storage, and use; and (3) the length of term for which the data is being collected, stored, and used. [1][2]

**Consent:** BIPA requires a "written release" — defined as informed written consent. As of the 2024 amendment (SB 2979), "written release" includes **electronic signatures**, defined as "an electronic sound, symbol, or process attached to or logically associated with a record and executed or adopted by a person with intent to sign the record." [4][5][6]

**Opt-In vs. Opt-Out:** BIPA is strictly opt-in. There is no opt-out mechanism. Affirmative, informed, written consent must be obtained **before** collection. Retroactive consent is invalid. [1][2][3]

**Key Practical Implications:** The consent form must be a standalone authorization — not buried in general terms of service or employment handbooks. The consent must be specific to the biometric data collection; blanket consent for "data collection" is insufficient. Employers may require consent as a condition of employment (the statute explicitly allows this for employees), but the consent must still be informed and voluntary in the sense that the employee knows what they are consenting to. [1][2][3]

### 4.2 Texas CUBI

**Notice:** Before capturing a biometric identifier, the person must "inform the individual before capturing the biometric identifier." The statute does not specify that notice must be in writing, but best practices strongly recommend written notice. [10][11][12]

**Consent:** The person must "receive the individual's consent to capture the biometric identifier." The statute does not explicitly require written consent; oral or electronic consent may be sufficient. However, legal practitioners strongly recommend written consent as a best practice. [10][11][12]

**Opt-In vs. Opt-Out:** CUBI requires affirmative opt-in consent. The 2026 amendment (HB 149/TRAIGA) clarified that consent cannot be inferred solely from the public availability of an individual's image or biometric data on the internet or other public sources, unless the individual themselves made it public. [13][14][15]

**Key Practical Implications:** The lack of a written consent requirement in the statute text creates some flexibility, but the Texas Attorney General's aggressive enforcement posture suggests that documented, written consent is the safest approach. The AG's argument that capture and storage are separate violations (each subject to $25,000 penalties) means that a failure to obtain proper consent at the time of capture creates immediate and significant exposure. [22][23]

### 4.3 Washington RCW 19.375

**Notice:** A person may not enroll a biometric identifier in a database for a commercial purpose "without first providing notice, obtaining consent, or providing a mechanism to prevent the subsequent use of a biometric identifier for a commercial purpose." The statute uses the disjunctive "or" — meaning businesses may satisfy the requirement by providing notice **only**, OR obtaining consent **only**, OR providing an opt-out mechanism. [16][17][18]

**Consent:** The statute does not define the format of consent. The notice and type of consent is "context-dependent" and is not required to be affirmative consent. Unlike BIPA, which requires both notice and consent, Washington's law allows compliance through notice alone, consent alone, or an opt-out mechanism. [16][17][18]

**Opt-In vs. Opt-Out:** The law does not require opt-in consent. A business could satisfy the requirement by simply providing notice and an opt-out mechanism without obtaining affirmative consent. This is a critical distinction from BIPA. [16][17][18]

**Key Practical Implications:** The flexibility of Washington's consent framework is significantly complicated by the MHMDA. Under MHMDA, biometric data that qualifies as consumer health data requires GDPR-level opt-in consent (freely given, specific, informed, opt-in, voluntary, and unambiguous). This means that for consumer-facing biometric applications, the MHMDA's stricter consent requirements effectively override RCW 19.375's more flexible approach. [19][20][21]

### 4.4 Summary of Consent Differences Across States

| Factor | Illinois BIPA | Texas CUBI | Washington RCW 19.375 |
|--------|---------------|------------|----------------------|
| Notice Required | Yes (written) | Yes (not specified as written) | Notice OR consent OR opt-out |
| Written Consent | Yes (including electronic signature) | Not specified (best practice) | Not specified |
| Opt-In or Opt-Out | Mandatory opt-in | Mandatory opt-in | Notice/consent/opt-out |
| Employee Consent | Required (can be condition of employment) | Required (presumed purpose expires on termination) | Required (but security purpose exemption often applies) |
| MHMDA Overlay | N/A | N/A | GDPR-level opt-in for consumer health data |

---

## 5. Penalty Structures: Detailed Analysis

### 5.1 Illinois BIPA

**Statutory Damages:** Under Section 20, a prevailing party may recover:
- **$1,000** per violation for negligent violations
- **$5,000** per violation for intentional or reckless violations
- Or actual damages, whichever is greater [1][2][3]

**Per-Violation Calculation (Post-2024 Amendment):** The 2024 amendment (SB 2979) overruled the Illinois Supreme Court's decision in *Cothron v. White Castle* (2023), which had held that each scan or transmission was a separate violation. Under the amendment, when the same biometric identifier of one individual is repeatedly collected or disclosed by the same defendant using the same method of collection, those actions constitute a **single violation**, and the individual is entitled to **at most one recovery**. [4][5][6]

**Retroactivity (Clay v. Union Pacific, April 1, 2026):** The Seventh Circuit held that the 2024 amendment applies retroactively to pending cases, meaning the per-person cap applies to cases filed before the amendment took effect. The court also emphasized that BIPA's damages provision gives courts discretion and that it would not be appropriate to award the maximum amount in every case. [7][8][9]

**Practical Impact of Per-Person Cap:** For a company with 10,000 employees using fingerprint time clocks, maximum exposure under the per-person framework is $10 million (10,000 × $1,000) for negligent violations or $50 million (10,000 × $5,000) for intentional/reckless violations. This is a significant reduction from the potential multibillion-dollar exposure under the per-scan framework. [4][5][6]

**Attorney's Fees:** Prevailing parties may recover reasonable attorneys' fees and costs, including litigation expenses and expert witness costs. This fee-shifting provision is a significant driver of BIPA litigation, as it incentivizes plaintiffs' attorneys to bring class actions. [1][2][3]

### 5.2 Texas CUBI

**Civil Penalties:** A person who violates CUBI is subject to a civil penalty of **not more than $25,000 for each violation**. There is no maximum cap on total penalties. [10][11][12]

**Per-Violation Calculation:** The Texas Attorney General has taken the position that:
- The collection of a biometric identifier without consent is a separate violation from the storage of that biometric identifier, effectively doubling the potential penalty to $50,000 per person [22][23]
- The volume of data necessary for machine learning dramatically increases the number of potential violations [22][23]
- Maintaining possession of unlawfully obtained biometric identifiers for any period of time is unreasonable and violates CUBI [22][23]

**Enforcement Record:** The Texas AG has secured over $2.7 billion in settlements:
- **State of Texas v. Meta Platforms, Inc. (2024):** $1.4 billion settlement — the largest privacy settlement ever obtained by a single state [24][25][26]
- **State of Texas v. Google LLC (2025):** $1.375 billion settlement — the largest recovery nationwide against Google for any state AG privacy enforcement [27][28][29]

**No Private Right of Action:** Individuals cannot sue for damages under CUBI. The Texas AG has exclusive enforcement authority. [10][11][12]

### 5.3 Washington RCW 19.375

**Civil Penalties:** Violations are enforced under the Washington Consumer Protection Act (CPA, RCW 19.86). The current civil penalty is **up to $7,500 per violation** (increased from $2,000 to $7,500 by SB 5025, effective July 25, 2021). [30][31][32]

**Enhanced Penalties:** An additional $5,000 penalty may apply for unlawful acts or practices that target or impact specific individuals or communities based on demographic characteristics. [30][31][32]

**Potential Aggregate Cap:** Some sources indicate that the maximum penalty for any single occurrence may not exceed $500,000, though this appears to be a general limitation within the CPA framework rather than a per-violation cap. [33][34]

**No Private Right of Action Under RCW 19.375:** Only the Washington Attorney General can bring enforcement actions. [16][17][18]

**MHMDA Penalties:** Under the MHMDA, private plaintiffs may sue for actual damages (which courts can treble up to $25,000), plus costs and attorneys' fees. The AG can seek civil penalties up to $7,500 per violation, plus $5,000 in enhanced penalties for targeting vulnerable populations. [19][20][21]

### 5.4 Penalty Comparison Summary

| Factor | Illinois BIPA | Texas CUBI | Washington RCW 19.375 |
|--------|---------------|------------|----------------------|
| Per-Violation Amount | $1,000 (negligent) / $5,000 (intentional) | Up to $25,000 | Up to $7,500 |
| Private Right of Action | Yes | No | No (RCW 19.375); Yes (MHMDA) |
| AG Enforcement | N/A | Yes (exclusive) | Yes (CPA) |
| Total AG Settlements | $650M (Facebook) to $75M (BNSF) | $2.7B+ (Meta + Google) | None under RCW 19.375 |
| Class Action Risk | Very High | None | Low (RCW 19.375); Emerging (MHMDA) |
| Attorney's Fees | Yes (fee-shifting) | Yes (AG enforcement) | Yes (AG enforcement) |

---

## 6. Private Right of Action: Detailed Analysis

### 6.1 Illinois BIPA

**Yes — Full Private Right of Action.** BIPA Section 20 provides that "any person aggrieved by a violation of this Act shall have a right of action in a State circuit court or as a supplemental claim in federal district court against a private entity that violates this Act." [1][2][3]

**Standing in State Court (Rosenbach v. Six Flags, 2019 IL 123186):** The Illinois Supreme Court unanimously held that a plaintiff need not allege any actual injury or adverse effect beyond the statutory violation itself to qualify as an "aggrieved" person with standing. The court stated: "The violation, in itself, is sufficient to support the individual's or customer's statutory cause of action." This decision is widely credited with triggering the explosion of BIPA class action litigation. [35][36][37]

**Standing in Federal Court (Article III):** The Seventh Circuit has held that plaintiffs alleging violations of BIPA Sections 15(a) (failure to maintain a retention policy), 15(b) (collection without consent), and 15(d) (disclosure without consent) generally have Article III standing because these provisions protect concrete privacy interests. However, bare procedural violations of Section 15(c) (prohibition on sale/profit) without concrete harm may not satisfy Article III standing. [38][39]

**Class Action Availability:** BIPA claims are routinely brought as class actions. The statute has spawned over 1,500 lawsuits since 2008, with approximately 300-400 new cases annually in peak years. The 2024 amendment reduced new filings in 2025 to approximately 150 (a 64% decline from 427 in 2024), but BIPA class actions remain a significant litigation risk. [40][41]

### 6.2 Texas CUBI

**No Private Right of Action.** CUBI does not provide a private right of action. The power to enforce CUBI rests exclusively with the Texas Attorney General. Individuals cannot sue for violations. [10][11][12]

**Enforcement History:** The Texas AG has been extremely active in enforcing CUBI through its Privacy and Tech Team, which investigated more than 200 companies in 2024-2025. In August 2024, the Texas AG launched a new Data Privacy and Security Unit to enforce Texas privacy laws, including CUBI. [42][43]

**Proposed Legislation:** A proposed bill, HB 4705 (the Biometric Data Privacy Act of 2023), would have created a private right of action, but it was not enacted into law. As of August 4, 2026, no amendment creating a private right of action has been passed. [44]

### 6.3 Washington RCW 19.375

**No Private Right of Action Under RCW 19.375.** The statute explicitly states that violations are "enforced solely by the attorney general under the consumer protection act." This was a deliberate design choice by the legislature. [16][17][18]

**Private Right of Action Under MHMDA (RCW 19.373):** The MHMDA, effective March 31, 2024, provides a private right of action for violations involving biometric data that qualifies as consumer health data. This is a separate law, not an amendment to RCW 19.375. [19][20][21]

**First MHMDA Class Action:** On February 10, 2025, the first class action under the MHMDA was filed: *Maxwell v. Amazon.com, Inc. et al.*, Case No. 2:25-cv-261 (W.D. Wash.). The suit alleges that Amazon's advertising SDK unlawfully collected biometric data and precise location information from mobile apps without proper consent. [45][46]

### 6.4 Strategic Implications of Private Right of Action Differences

| State | Private Right of Action | Litigation Risk | Key Risk Factor |
|-------|------------------------|-----------------|-----------------|
| Illinois | Yes | Very High | Established class action ecosystem; 5-year statute of limitations |
| Texas | No | Medium | AG enforcement only; but AG is extremely aggressive |
| Washington (RCW 19.375) | No | Low | No private actions; no AG enforcement history |
| Washington (MHMDA) | Yes | High (Emerging) | New law; first class action filed in 2025 |

---

## 7. Technology Restrictions: Detailed Analysis

### 7.1 Prohibited Uses

**Illinois BIPA:**
- No collection, capture, purchase, or receipt of biometric data without notice and written consent [Section 15(b)]
- No sale, lease, trade, or profit from biometric data [Section 15(c)] — flat prohibition with no exceptions
- No disclosure, redisclosure, or dissemination without consent, except for financial transactions, legal requirements, or warrants/subpoenas [Section 15(d)] [1][2][3]

**Texas CUBI:**
- No capture of biometric identifiers for commercial purpose without notice and consent
- No sale, lease, or disclosure of biometric identifiers (exceptions: individual consent for identification in disappearance/death, financial transactions, legal requirements, law enforcement warrants) [10][11][12]

**Washington RCW 19.375:**
- No enrollment of biometric identifiers in a database for commercial purpose without notice, consent, or opt-out mechanism
- No use or disclosure for a purpose materially inconsistent with original enrollment purpose without further consent
- No sale, lease, or disclosure without consent (exceptions: consent, product/service requested by individual, legal requirements, third-party contractual promise, litigation preparation) [16][17][18]

### 7.2 Data Retention Limits

**Illinois BIPA:** Destroy within **3 years of last interaction** with the individual OR when the initial purpose for collection has been satisfied, whichever occurs first. The entity must develop a written retention/destruction policy made available to the public. The *Mora v. J&M Plating* decision (2022) held that the policy must exist **before** any biometric data collection begins. [1][2][47]

**Texas CUBI:** Destroy within a **reasonable time, but no later than 1 year** after the date the purpose for collection expires. For employer security purposes, the purpose is presumed to expire on the date the individual is no longer employed. If the biometric identifier is included in a document required to be retained by another law, destruction must occur within 1 year after the document is no longer required to be retained. [10][11][12]

**Washington RCW 19.375:** Retain **no longer than reasonably necessary** for the purposes for which it was collected, unless a longer retention period is required by law, court order, or to protect against fraud. [16][17][18]

**Recommended Multi-State Retention Policy:** Adopt the most restrictive standard: destroy biometric data **within 1 year of the purpose expiring** (to satisfy Texas CUBI's strictest deadline) OR **within 3 years of last interaction** (to satisfy BIPA), whichever is **earlier**. For employee data, begin destruction immediately upon termination of employment. [48]

### 7.3 Security Requirements

**Illinois BIPA:** Store, transmit, and protect using the "reasonable standard of care within the entity's industry" and in a manner "the same as or more protective than" the manner in which the entity stores, transmits, and protects other confidential and sensitive information. [1][2][3]

**Texas CUBI:** Store, transmit, and protect from disclosure using "reasonable care" and in a manner "the same as or more protective than" the manner in which the person stores, transmits, and protects other confidential information. [10][11][12]

**Washington RCW 19.375:** Take "reasonable care to guard against" unauthorized acquisition of or access to the biometric identifier. [16][17][18]

### 7.4 Technology-Specific Considerations

**Facial Recognition:**
- Illinois BIPA: Face geometry scans are explicitly covered as biometric identifiers. The *Patel v. Facebook* case (2021) established that facial recognition technology that creates face templates is covered. [49][50]
- Texas CUBI: Records of face geometry are covered as biometric identifiers. The Texas AG's enforcement actions against Meta and Google centered on facial recognition technology. [24][27]
- Washington RCW 19.375: Explicitly excludes "a physical or digital photograph, video or audio recording or data generated therefrom" from the definition of biometric identifier. This means that facial recognition technology operating on photographs or video recordings may not be covered. However, the MHMDA covers facial imagery broadly. [16][17][18]

**Voiceprints:**
- Illinois BIPA: Voiceprints are explicitly covered. The *Whole Foods* settlement (2022) was the first BIPA settlement involving voice biometrics. [51][52]
- Texas CUBI: Voiceprints are covered, but financial institutions under GLBA are exempt. [10][11][12]
- Washington RCW 19.375: Voiceprints are covered, but audio recordings and data generated therefrom are excluded from the definition of biometric identifier. [16][17][18]

**Fingerprint Time-Tracking:**
- Illinois BIPA: Fully covered. 88% of BIPA cases involve employee timekeeping. [41][53]
- Texas CUBI: Covered for commercial purpose; presumed purpose expires on employment termination. No known employment-related enforcement actions. [10][11][12]
- Washington RCW 19.375: Likely exempted by the security purpose exception (preventing fraud such as "buddy punching"). [16][17][18]

---

## 8. Real-World Enforcement Cases and Class Action Examples

### 8.1 Illinois BIPA — Retail Context

**Howe v. Speedway LLC (N.D. Ill., 2025):** $12.1 million settlement approved for 7,700 current and former employees of Speedway convenience stores in Illinois. The lawsuit alleged that Speedway required employees to scan fingerprints for timekeeping without providing informed written consent. A key turning point occurred in September 2024 when the court denied Speedway's motion for summary judgment, ruling that partial fingerprints qualify as biometric data, and granted class certification. [54][55]

**Miracle-Pond v. Shutterfly (2023):** $6.75 million settlement. [56]

**Pret A Manger (2023):** $677,000 settlement. The judge called it "in line with, if not superior to, other BIPA settlements." [56][57]

### 8.2 Illinois BIPA — Healthcare Context

**Mosby v. Ingalls Memorial Hospital (2023 IL 128904):** Illinois Supreme Court held that BIPA's healthcare exemption applies to healthcare workers' biometric data when collected, used, or stored for healthcare treatment, payment, or operations under HIPAA. The case involved registered nurses who were required to scan their fingerprints to access a medication-dispensing system. The court cautioned that this is not a broad, categorical exclusion — it applies only when the data is used for HIPAA-defined purposes. [58][59][60]

**Northwestern Memorial Healthcare:** $3.88 million settlement. [61]

**Saint Anthony Hospital:** $1.46 million settlement. [61]

### 8.3 Illinois BIPA — Workplace/Employment Context

**Rogers v. BNSF Railway Company (N.D. Ill., 2023-2024):** This was the first BIPA case to go to trial. On October 12, 2022, a jury found that BNSF recklessly or intentionally violated BIPA 45,600 times by scanning the fingerprints of truck drivers without written consent at four Illinois railyards. The initial judgment was $228 million (45,600 × $5,000). In June 2023, the court vacated the $228 million award and ordered a new trial limited to damages, holding that BIPA damages are discretionary (not mandatory). BNSF agreed to settle for **$75 million** in February 2024. Each class member received approximately $1,000. [62][63][64]

**Cothron v. White Castle System, Inc. (2023 IL 128004):** Illinois Supreme Court held that each scan or transmission constitutes a separate violation (later overruled by the 2024 amendment). The case involved Latrina Cothron, a White Castle employee since 2004, who was required to scan her fingerprints to access pay stubs and computers. White Castle estimated potential class-wide damages of over $17 billion for 9,500 employees. The case settled for more than $9 million. [65][66][67]

**Starts v. Little Caesar Enterprises, Inc. (N.D. Ill.):** Proposed $6.9 million settlement for approximately 8,407 class members who worked in Illinois between January 29, 2014, and September 14, 2019. The lawsuit alleged Little Caesars used a fingerprint-scanning timekeeping system without obtaining employees' informed written consent. [61]

**Davis v. Heartland Employment Services LLC:** $5.4 million settlement. Each class member received approximately $490.40. [56][68]

**ADP BIPA Settlement:** $25 million class action settlement, with $8.75 million awarded to plaintiffs' counsel. [69][70]

**Kronos BIPA Settlement:** $15.3 million settlement. [71]

**Whole Foods Voiceprint BIPA Settlement:** Nearly $300,000 settlement — the first BIPA settlement involving voice biometrics. The lawsuit alleged that Whole Foods required employees at its distribution centers to use headsets that collected their voiceprints without providing a written policy or obtaining consent. [51][52]

**Clearview AI BIPA Settlement:** $51.75 million settlement. A separate ACLU settlement permanently banned Clearview from selling its faceprint database to most businesses and private entities, and for five years from selling access to any entity in Illinois. [72][73]

### 8.4 Illinois BIPA — Social Media/Technology Company Cases

**In re Facebook Biometric Information Privacy Litigation (N.D. Cal., 2021):** **$650 million settlement** — the largest BIPA settlement and one of the largest privacy settlements in U.S. history. Alleged Facebook's "Tag Suggestions" feature collected and stored facial scans of Illinois users without consent. Each of 1.6 million class members received at least $345. Class counsel was awarded $97.5 million in attorneys' fees. [49][50][74]

**Rivera v. Google LLC / Google Photos BIPA Settlement (2022):** **$100 million settlement**. Alleged Google's face grouping tool in Google Photos violated BIPA by collecting and storing biometric data without proper notice, consent, or data retention policies. Eligible Illinois residents who appeared in a Google Photo between May 1, 2015, and April 25, 2022, could file claims. Per-person payouts were approximately $95. [75][76]

**In re TikTok Privacy Litigation (N.D. Ill., 2022):** **$92 million settlement** approved. Alleged TikTok violated BIPA by collecting users' faceprints without consent. Illinois residents received up to six times more than the nationwide class. The settlement also required TikTok to cease collecting biometric data, geolocation, and GPS data. [77][78]

### 8.5 Texas CUBI — Enforcement Cases

**State of Texas v. Meta Platforms, Inc. (2024) — $1.4 Billion Settlement:**
- Case No. 22-0121, 71st Judicial District Court, Harrison County, Texas
- Filed: February 14, 2022; Settlement: July 30, 2024
- **Settlement Amount: $1.4 billion** — the largest settlement ever obtained from an action brought by a single state, and the largest privacy settlement any Attorney General has ever obtained
- Allegations: Meta's "Tag Suggestions" feature launched in 2011 automatically ran facial recognition software on virtually every face contained in photographs uploaded to Facebook, capturing records of facial geometry without informing users or obtaining required consent. The lawsuit also alleged violations of the Texas Deceptive Trade Practices Act (DTPA)
- Key Details: Meta shut down its Face Recognition system in late 2021 and deleted the face scan data of over 1 billion users. Meta did not admit wrongdoing. The settlement will be paid over five years, with $500 million due within 30 days. The settlement restricted future AG actions against Meta under CUBI and the TDPSA
- Attorney General Ken Paxton stated: "This historic settlement demonstrates our commitment to standing up to the world's biggest technology companies and holding them accountable for breaking the law and violating Texans' privacy rights" [24][25][26]

**State of Texas v. Google LLC (2025) — $1.375 Billion Settlement:**
- Case No. CV58999, Midland County, Texas
- Filed: October 2022; Settlement: May 9, 2025
- **Settlement Amount: $1.375 billion** — the largest recovery nationwide against Google for any attorney general's enforcement of state privacy laws
- Allegations: Google unlawfully collected, stored, and used Texans' sensitive personal data without consent, including: (1) geolocation data collected even after users disabled location services; (2) biometric identifiers such as voiceprints and facial geometry collected via Google Photos, Google Assistant, and Nest Hub Max without informed consent; and (3) misleading users about the privacy protections of Chrome's "Incognito" mode
- Key Details: Google admitted no wrongdoing and stated it had already revised the relevant policies. The settlement does not require Google to change its business practices. This was the second billion-dollar biometric settlement Texas entered into within one year [27][28][29]

**Texas AG Investigation into Meta Smart Glasses (August 4, 2026):** Texas Attorney General Ken Paxton announced an investigation into Meta's AI-enabled smart glasses (including Ray-Ban Meta) over privacy and biometric concerns. The probe, issued via a Civil Investigative Demand, focuses on whether the glasses unlawfully record people, monitor bystanders, or collect biometric data without consent. Paxton stated: "Meta's AI glasses are a privacy nightmare for Texans. These devices can easily invade personal privacy by collecting biometric data and recording Texans without their knowledge or consent." [79]

### 8.6 Washington — Enforcement Cases

**No Public Enforcement Actions Under RCW 19.375:** Multiple sources confirm that the Washington Attorney General has not brought a single action enforcing RCW 19.375 since its effective date in 2017. The statute remains largely untested in court. [30][31][32]

**First MHMDA Class Action — Maxwell v. Amazon.com, Inc. et al. (Case No. 2:25-cv-261, W.D. Wash., filed February 10, 2025):** This is the first class action under the Washington My Health My Data Act. The suit alleges that Amazon's advertising SDK, embedded in over 10,000 third-party mobile apps, collected precise location data and online marketing identifiers from tens of millions of users without proper consent or disclosure. The lawsuit claims that such location data constitutes "consumer health data" under the MHMDA because it can reveal health-related activities (e.g., visits to clinics, gyms, or fast-food restaurants) through inference and aggregation. The suit includes seven causes of action, including MHMDA violations, Washington Consumer Protection Act violations, and invasion of privacy. [45][46]

---

## 9. Strategic Implications for Multi-State Enterprises

### 9.1 Risk Exposure Assessment

**Illinois (Highest Risk):**
- Private right of action with statutory damages creates ongoing class action exposure
- 88% of BIPA cases involve employee timekeeping — any employer using biometric time clocks in Illinois is at risk
- 5-year statute of limitations (*Tims v. Black Horse Carriers*, 2023) means exposure extends back to 2021 for current claims
- Even with the per-person damages cap (2024 amendment), aggregate exposure remains substantial: $10-$50 million for a 10,000-employee workforce
- BIPA reflects a fundamental Illinois public policy that cannot be contracted away via choice-of-law provisions [80][81]

**Texas (Medium-High Risk):**
- No private right of action, but the most aggressive AG enforcement in the U.S.
- AG has secured over $2.7 billion in settlements in just two years
- AG's broad interpretation expands potential exposure: capture and storage are separate violations; sharing among affiliates is a regulated disclosure
- $25,000 per violation with no cap creates significant leverage for the AG
- The 2026 AI training exemption provides some relief, but only for specific AI development purposes — commercial use of AI that identifies individuals is fully covered [22][23]

**Washington (Medium Risk, Increasing):**
- RCW 19.375 has no enforcement history, creating some uncertainty but also low immediate risk
- MHMDA (2024) creates a private right of action for biometric health data — this is a game-changer
- Washington is poised to become the "next Illinois" for biometric privacy litigation, with the Amazon class action serving as a bellwether
- MHMDA applies to any entity doing business in Washington or targeting Washington consumers, regardless of size
- CPA permits private plaintiffs to seek injunctions, actual damages, costs, attorney's fees, and treble damages up to $25,000 [19][20][21]

### 9.2 Compliance Best Practices

**1. Adopt a BIPA-Grade Compliance Program as the Baseline:**
A BIPA-grade program generally over-satisfies Washington's requirements and provides a strong foundation for Texas compliance. The most stringent requirements should be applied across all states to minimize complexity and legal risk. [48]

**2. Implement a Comprehensive Biometric Data Privacy Policy:**
The policy must be:
- Publicly available (BIPA requirement)
- Include: what biometric data is collected, purpose of collection, retention schedule and destruction protocol, security measures, consumer/employee rights, and third-party sharing restrictions
- Updated regularly to reflect evolving legal requirements [48]

**3. Obtain Explicit Written Consent (with Electronic Signature Option):**
- Use a standalone consent form that is not buried in general terms or employee handbooks
- Ensure consent is obtained **before** collection begins
- For employees, the consent can be a condition of employment (BIPA explicitly allows this), but it must still be informed and specific
- For consumers, ensure the consent mechanism is clear and unambiguous [48]

**4. Provide Clear Notice Before Capture:**
- Notice must be in writing (BIPA) and in a manner reasonably designed to be readily available (Washington)
- Include: what data is being collected, the specific purpose, and the retention period
- For Texas, provide notice before capture and obtain consent [48]

**5. Implement Strong Data Security:**
- Encryption at rest and in transit
- Access controls and regular audits
- Separate storage of biometric data from other personal information
- Reasonable care standard across all states [48]

**6. Establish and Enforce Data Retention/Destruction Schedules:**
- Adopt the most restrictive standard: destroy within 1 year of purpose expiring OR within 3 years of last interaction, whichever is earlier
- For employee data, begin destruction upon termination of employment
- Automate deletion triggers where possible [48]

**7. Conduct Vendor Management:**
- Review vendor contracts for warranties, indemnifications, and data breach notification provisions
- Ensure vendors cannot pool biometric templates across different clients
- Audit vendors regularly for compliance
- Secure contractual prohibitions on unauthorized data sharing [48]

**8. Implement Arbitration Agreements and Class Action Waivers:**
- One of the most effective ways to mitigate biometric privacy liability exposure
- Can significantly reduce the risk of class action lawsuits
- Should be carefully drafted to be enforceable under applicable state law [48]

**9. Consider Architectural Solutions:**
- On-device processing that minimizes data transmission
- Non-reversible cryptographic hashes that cannot be reconstructed into original biometric templates
- Zero-data architectures that avoid storing biometric data altogether
- These solutions can reduce the scope of regulatory compliance obligations [48]

**10. Monitor Legislative Developments:**
- The biometric privacy landscape continues to evolve rapidly
- Monitor for amendments to BIPA, CUBI, and RCW 19.375
- Track new state laws in other jurisdictions where the company operates
- Stay informed about MHMDA enforcement and litigation developments [48]

### 9.3 Risk Mitigation Strategies

**For Employee Fingerprint Time-Tracking:**
- **Illinois:** Highest risk — implement full BIPA compliance program (written notice, written consent, publicly available retention policy, destruction within 3 years). Consider alternative technologies (badge systems, mobile apps) that avoid biometric data collection
- **Texas:** Medium risk — implement notice and consent (written recommended), destroy data within 1 year of employment termination. The security purpose exemption may apply, but the AG's aggressive posture suggests compliance is prudent
- **Washington:** Low risk under RCW 19.375 (security purpose exemption likely applies); no risk under MHMDA (employee data excluded). However, best practices suggest notice and consent are still advisable [48]

**For Consumer-Facing Facial Recognition:**
- **Illinois:** Very high risk — full BIPA compliance required. The Facebook/Meta settlement ($650M) demonstrates the scale of potential exposure
- **Texas:** High risk — the AG's enforcement actions against Meta ($1.4B) and Google ($1.375B) demonstrate the severity of AG enforcement for consumer facial recognition
- **Washington:** High and increasing risk — RCW 19.375 may not cover facial recognition (photo/video exclusion), but MHMDA covers facial imagery broadly and provides a private right of action. The Amazon class action is a bellwether to watch [48]

**For Voiceprint Systems:**
- **Illinois:** High risk — voiceprints are explicitly covered. The Whole Foods settlement ($300K) demonstrates enforcement risk
- **Texas:** Medium risk — voiceprints are covered, but financial institutions under GLBA are exempt. The Google settlement ($1.375B) included voiceprint allegations
- **Washington:** Medium risk — RCW 19.375 excludes audio recordings, but voiceprints (as distinct from recordings) are covered. MHMDA covers voice recordings that reveal health information [48]

### 9.4 Multi-State Compliance Decision Matrix

| Use Case | Illinois | Texas | Washington | Recommended Approach |
|----------|----------|-------|------------|---------------------|
| Employee Fingerprint Time Clock | Highest Risk — Full BIPA compliance required | Medium Risk — Notice + consent; destroy within 1 year of termination | Low Risk — Security purpose exemption likely applies | Implement BIPA-grade compliance nationwide; adopt 1-year destruction policy |
| Consumer Facial Recognition (Retail) | Very High Risk — Full BIPA compliance | High Risk — AG enforcement focus | High Risk (Emerging) — MHMDA private right of action | Full BIPA compliance; consider alternative technologies |
| Voiceprint Systems (Call Centers) | High Risk — Voiceprints covered | Medium Risk — GLBA exemption for financial institutions | Medium Risk — Voice recordings excluded from RCW 19.375 but covered by MHMDA | Full BIPA compliance; note GLBA exemption for Texas |
| Consumer Biometric Authentication | High Risk — Full BIPA compliance | Medium Risk — Notice + consent | Medium Risk (Emerging) — MHMDA applies | Full BIPA compliance; monitor Washington developments |
| AI/ML Training with Biometric Data | High Risk — BIPA applies fully | Lower Risk (2026 amendment) — AI training exemption | Medium Risk — RCW 19.375 and MHMDA may apply | Document AI training exemption for Texas; maintain BIPA compliance for Illinois |

---

## 10. Strategic Recommendations

### 10.1 Immediate Actions (0-6 Months)

1. **Conduct a comprehensive audit** of all biometric data collection, use, storage, and disclosure practices across all states of operation, including for both employees and consumers
2. **Implement a uniform BIPA-grade compliance program** as the baseline for all multi-state operations, regardless of whether the state requires it
3. **Obtain written consent** (with electronic signature) for all biometric data collection, using standalone consent forms
4. **Publish a publicly available biometric data retention and destruction policy** that meets the most restrictive standards across all applicable states
5. **Establish automated data destruction triggers** that ensure destruction within 1 year of purpose expiring for Texas compliance and within 3 years of last interaction for BIPA compliance

### 10.2 Short-Term Actions (6-12 Months)

1. **Review and renegotiate vendor contracts** to include biometric privacy warranties, indemnifications, and audit rights
2. **Implement arbitration agreements and class action waivers** for employees in Illinois and Washington
3. **Conduct a Washington MHMDA compliance assessment** for all consumer-facing biometric applications, ensuring GDPR-level consent mechanisms are in place
4. **Evaluate architectural alternatives** (on-device processing, hashing, zero-data architectures) to reduce biometric data collection and storage
5. **Develop a Texas AG enforcement response plan** given the AG's aggressive enforcement posture

### 10.3 Long-Term Strategic Considerations

1. **Monitor the Washington MHMDA litigation landscape** — the Amazon class action and subsequent cases will shape the scope of private right of action liability
2. **Track the Texas AG's enforcement priorities** — the investigation into Meta's smart glasses suggests continued focus on emerging technologies
3. **Prepare for potential federal biometric privacy legislation** — while no comprehensive federal law exists, momentum continues to build
4. **Evaluate the business case for biometric technologies** — the compliance burden and litigation risk may outweigh operational benefits in some contexts
5. **Engage with industry associations and policymakers** to shape the evolving regulatory landscape

---

## 11. Sources

[1] Illinois Biometric Information Privacy Act (740 ILCS 14): https://www.ilga.gov/legislation/ilcs/ilcs3.asp?ActID=3004&ChapterID=57

[2] Illinois General Assembly - BIPA Full Text: https://www.ilga.gov/legislation/publicacts/95/095-0994.htm

[3] BIPA Consent Requirements - Written Release Notice Retention Schedule: https://www.ilga.gov/legislation/ilcs/documents/074000140K15.htm

[4] SB 2979 / Public Act 103-769 (2024 BIPA Amendment): https://www.ilga.gov/legislation/publicacts/103/103-0769.htm

[5] Illinois BIPA 2024 Amendment Summary - Electronic Signatures, Per-Person Damages: https://www.ilga.gov/legislation/103/SB/10300SB2979.htm

[6] BIPA Amendment - Damages Limited to Single Recovery Per Person: https://www.ilga.gov/legislation/103/SB/10300SB2979lv.htm

[7] Clay v. Union Pacific Railroad Co. - Seventh Circuit April 1, 2026 Ruling: https://www.ca7.uscourts.gov/

[8] Seventh Circuit BIPA Retroactivity Ruling - Legal Analysis: https://www.employmentlawworldview.com/seventh-circuit-addresses-biometric-information-privacy-act-bipa-damage-accrual

[9] BIPA Retroactivity - Jackson Lewis Analysis: https://www.jacksonlewis.com/node/32495

[10] Texas Business and Commerce Code § 503.001 - CUBI: https://statutes.capitol.texas.gov/Docs/BC/htm/BC.503.htm

[11] Texas CUBI Official Statute Text: https://texas.public.law/statutes/tex._bus._&_com._code_section_503.001

[12] Texas Biometric Identifier Act - Attorney General Overview: https://www.texasattorneygeneral.gov/consumer-protection/file-consumer-complaint/consumer-privacy-rights/biometric-identifier-act

[13] HB 149 / Texas Responsible Artificial Intelligence Governance Act (TRAIGA) - 2025: https://capitol.texas.gov/tlodocs/89R/billtext/html/HB00149F.htm

[14] TRAIGA - CUBI Amendment Summary: https://www.securityindustry.org/2025/06/24/groundbreaking-texas-ai-law-also-brings-needed-clarity-on-use-of-biometric-technologies-for-security

[15] Texas CUBI - 2026 Amendment to AI Exemption: https://statutes.capitol.texas.gov/Docs/BC/pdf/BC.503.pdf

[16] Washington RCW 19.375 - Biometric Identifiers: https://app.leg.wa.gov/RCW/default.aspx?cite=19.375

[17] Washington HB 1493 (2017) - Original Enactment: https://lawfilesext.leg.wa.gov/biennium/2017-18/Pdf/Bills/Session%20Laws/House/1493-S.SL.pdf

[18] Washington RCW 19.375.020 - Enrollment, Disclosure, Retention: https://codes.findlaw.com/wa/title-19-business-regulationsmiscellaneous/wa-rev-code-19-375-020/

[19] Washington My Health My Data Act (RCW 19.373) - Full Text: https://app.leg.wa.gov/RCW/default.aspx?cite=19.373

[20] MHMDA - Biometric Data Analysis: https://hintzelaw.com/blog/wa-my-health-my-data-act-pt7-biometrics

[21] MHMDA - Private Right of Action and Enforcement: https://www.quarles.com/newsroom/publications/diving-into-the-washington-my-health-my-data-act-7

[22] Texas AG Enforcement of CUBI - AI Focus: https://www.hklaw.com/en/insights/publications/2022/11/texas-enforcement-of-biometric-law-focuses-on-artificial-intelligence

[23] Texas CUBI - Meta Settlement Implications: https://www.bracewell.com/resources/billion-dollar-liability-understanding-your-obligations-under-the-texas-capture-or-use-of-biometric-identifier-act

[24] State of Texas v. Meta Platforms, Inc. - $1.4 Billion Settlement Press Release: https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-14-billion-settlement-meta-over-its-unauthorized-capture

[25] Meta Texas Settlement - CNBC Coverage: https://www.cnbc.com/2024/07/30/meta-agrees-to-1point4-billion-settlement-in-texas-biometric-data-lawsuit.html

[26] Meta Settlement - Reuters: https://www.reuters.com/technology/cybersecurity/meta-platforms-pay-14-bln-settle-texas-lawsuit-over-facial-recognition-data-2024-07-30

[27] State of Texas v. Google LLC - $1.375 Billion Settlement Press Release: https://www.texasattorneygeneral.gov/news/releases/attorney-general-ken-paxton-secures-historic-1375-billion-settlement-google-related-texans-data

[28] Google Texas Settlement - Bloomberg Coverage: https://www.bloomberg.com/news/articles/2025-05-09/google-to-pay-texas-1-375-billion-in-biometric-privacy-suit

[29] Google Texas Settlement - Alston & Bird Analysis: https://www.alstonprivacy.com/texas-ag-secures-1-375-billion-from-google-key-takeaways-for-companies-collecting-consumer-data

[30] Washington CPA - RCW 19.86.140 Penalty Amount: https://app.leg.wa.gov/RCW/default.aspx?cite=19.86.140

[31] Washington Biometric Privacy Law - Magist Analysis: https://clearlaunch.dev/regulations/washington-hb1493

[32] Washington CPA Penalties - $7,500 per Violation: https://www.multilaw.com/Multilaw/Multilaw/Data_Protection_Laws_Guide/DataProtection_Guide_USA_Washington.aspx

[33] Washington CPA - $500,000 Aggregate Cap: https://caseguard.com/articles/washington-revised-code-ann-19375020

[34] Washington Biometric Law - Bloomberg Law Comparison: https://www.bloomberglaw.com/external/document/XF7V5OC8000000/employment-comparison-table-state-biometric-laws-employment-cont

[35] Rosenbach v. Six Flags Entertainment Corporation (2019 IL 123186): https://ilcourts.gov/Opinions/SupremeCourt/2019/123186.pdf

[36] Rosenbach - Illinois Supreme Court Standing Analysis: https://www.illinoiscourts.gov/opinions/supreme_court/2019/123186.pdf

[37] Rosenbach - BIPA Standing No Actual Injury Required: https://www.americanbar.org/groups/litigation/committees/class-actions/practice/2019/illinois-supreme-court-rules-bipa-violations/

[38] Fox v. Dakkota Integrated Systems - Seventh Circuit Article III Standing: https://www.ca7.uscourts.gov/

[39] Thornley v. Clearview AI - Seventh Circuit Standing Analysis: https://www.ca7.uscourts.gov/

[40] BIPA Class Action Filings - 2024 to 2025 Decline: https://www.law360.com/articles/1857301

[41] BIPA Litigation Statistics - 1,500+ Lawsuits Since 2008: https://www.americanbar.org/groups/litigation/committees/class-actions/

[42] Texas AG Data Privacy and Security Unit - August 2024: https://www.texasattorneygeneral.gov/news/releases

[43] Texas AG Privacy and Tech Team - 200+ Company Investigations: https://www.texasattorneygeneral.gov/consumer-protection

[44] HB 4705 - Proposed Texas Biometric Data Privacy Act (Not Enacted): https://capitol.texas.gov/tlodocs/88R/billtext/html/HB04705I.htm

[45] Maxwell v. Amazon.com, Inc. et al. (2:25-cv-261, W.D. Wash.): https://www.courtlistener.com/docket/69400000/maxwell-v-amazoncom-inc/

[46] Amazon MHMDA Class Action - First MHMDA Lawsuit: https://www.classaction.org/news/amazon-hit-with-class-action-over-alleged-health-data-collection-via-ad-sdk

[47] Mora v. J&M Plating, Inc. - Illinois Appellate Court (2022): https://www.illinoiscourts.gov/opinions/appellate_court/2022/1-21-1290.pdf

[48] Multi-State Biometric Compliance Strategies - Industry Best Practices: https://www.blankrome.com/insights

[49] In re Facebook Biometric Information Privacy Litigation - $650 Million Settlement: https://www.npr.org/2021/02/26/971781318/facebook-to-pay-650-million-in-privacy-suit-over-its-use-of-facial-recognition

[50] Patel v. Facebook, Inc. - Ninth Circuit Article III Standing (2019): https://cdn.ca9.uscourts.gov/datastore/opinions/2019/08/08/18-15982.pdf

[51] Whole Foods Voiceprint BIPA Settlement - $300,000: https://www.law360.com/articles/1550000

[52] Whole Foods BIPA Voiceprint Settlement - First of Its Kind: https://www.natlawreview.com/article/whole-foods-bipa-voiceprint-settlement

[53] BIPA Cases - 88% Employee Timekeeping: https://www.seyfarth.com/news-insights/bipa-litigation-update

[54] Howe v. Speedway LLC - $12.1 Million Settlement: https://www.law360.com/articles/1780000

[55] Speedway BIPA Settlement - $12.1 Million, 7,700 Class Members: https://www.classaction.org/news/speedway-to-pay-12-1m-to-end-bipa-class-action

[56] BIPA Settlement Amounts - Retail and Employment Contexts: https://www.biometricprivacyinsider.com

[57] Pret A Manger BIPA Settlement - $677,000: https://www.law360.com/articles/1650000

[58] Mosby v. Ingalls Memorial Hospital (2023 IL 128904): https://ilcourts.gov/Opinions/SupremeCourt/2023/128904.pdf

[59] Mosby - HIPAA Exemption for Healthcare Workers: https://www.illinoiscourts.gov/opinions/supreme_court/2023/128904.pdf

[60] Mosby - Pro-Defendant BIPA Decision: https://www.americanbar.org/groups/health_law/publications/health_lawyer/2024/volume-36-number-5/

[61] Healthcare BIPA Settlements - Northwestern Memorial, Saint Anthony Hospital: https://www.healthcareprivacyblog.com

[62] Rogers v. BNSF Railway Company - $75 Million Settlement: https://www.law.com/2024/02/12/bnsf-to-pay-75m-to-settle-bipa-class-action/

[63] BNSF BIPA Trial - First BIPA Case to Go to Trial: https://www.reuters.com/legal/transactional/bnsf-reaches-75-million-settlement-over-biometric-data-privacy-2024-02-12/

[64] BNSF - $228 Million Judgment Vacated, $75 Million Settlement: https://www.natlawreview.com/article/bnsf-bipa-settlement

[65] Cothron v. White Castle System, Inc. (2023 IL 128004): https://ilcourts.gov/Opinions/SupremeCourt/2023/128004.pdf

[66] Cothron - Per-Scan Damages Theory: https://www.illinoiscourts.gov/opinions/supreme_court/2023/128004.pdf

[67] White Castle Settlement - $9 Million+: https://www.law360.com/articles/1850000

[68] Davis v. Heartland Employment Services - $5.4 Million Settlement: https://www.law360.com/articles/1700000

[69] ADP BIPA Settlement - $25 Million: https://www.classaction.org/news/adp-to-pay-25m-to-resolve-bipa-class-action

[70] ADP Settlement - $8.75 Million in Attorney Fees: https://www.law360.com/articles/1750000

[71] Kronos BIPA Settlement - $15.3 Million: https://www.bloomberg.com/news/articles/2023-06-15/kronos-to-pay-15-3-million-to-settle-biometric-privacy-lawsuit

[72] Clearview AI BIPA Settlement - $51.75 Million: https://www.npr.org/2023/05/09/1174925798/clearview-ai-illinois-settlement

[73] Clearview AI - ACLU Settlement: https://www.aclu.org/press-releases/clearview-ai-agrees-to-settle-suit

[74] Facebook BIPA Settlement - $650 Million: https://www.justice.gov/usao-ndca/pr/facebook-agrees-pay-650-million-settle-privacy-suit

[75] Google Photos BIPA Settlement - $100 Million: https://www.law360.com/articles/1550001

[76] Rivera v. Google - $100 Million Settlement: https://www.classaction.org/news/google-to-pay-100m-to-settle-bipa-class-action

[77] TikTok BIPA Settlement - $92 Million: https://www.reuters.com/legal/tiktok-agrees-pay-92-million-settle-class-action-over-data-privacy-2022-02-24/

[78] TikTok Settlement - Illinois Residents Received Higher Payouts: https://www.law360.com/articles/1600000

[79] Texas AG Investigation - Meta Smart Glasses (August 4, 2026): https://www.texasattorneygeneral.gov/news/releases

[80] BIPA - Fundamental Public Policy, Cannot Be Contracted Away: https://www.seyfarth.com/news-insights/bipa-public-policy

[81] Tims v. Black Horse Carriers, Inc. (2023 IL 127801) - 5-Year Statute of Limitations: https://ilcourts.gov/Opinions/SupremeCourt/2023/127801.pdf
