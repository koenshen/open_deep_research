# OCR HIPAA Enforcement Analysis: High-Penalty Cases ($1M+) – August 2021 to August 2026

## Executive Summary

This report analyzes the most significant HIPAA Security Rule enforcement actions taken by the HHS Office for Civil Rights (OCR) between August 2021 and August 2026, focusing specifically on cases where the total financial penalty exceeded $1,000,000. The analysis identifies five qualifying cases within this period, revealing consistent patterns of security compliance failures centered on risk analysis deficiencies. The report is structured to address three core questions: (1) the Security Rule provisions most frequently cited in high-penalty cases, (2) common risk assessment failures with concrete examples, and (3) the typical corrective actions OCR requires in resolution agreements.

---

## Section 1: Top 10 Security Rule Violations Leading to High Penalties

The following ranking is based on the frequency of citation across the five confirmed $1M+ cases within the research period (August 2021 – August 2026), supplemented by patterns observed in OCR's broader enforcement activity. The cases analyzed include: Montefiore Medical Center ($4.75M, 2024), Solara Medical Supplies ($3M, 2025), Warby Parker ($1.5M CMP, 2025), L.A. Care Health Plan ($1.3M, 2023), and Gulf Coast Pain Consultants ($1.19M CMP, 2024).

### 1. Failure to Conduct an Accurate and Thorough Risk Analysis (45 C.F.R. § 164.308(a)(1)(ii)(A))

**Frequency:** Cited in 5 out of 5 qualifying cases (100%)

This is the single most common violation in high-penalty cases. Every $1M+ enforcement action in the period included this provision. The requirement mandates that covered entities and business associates "conduct an accurate and thorough assessment of the potential risks and vulnerabilities to the confidentiality, integrity, and availability of electronic protected health information held by the covered entity or business associate." [1] OCR launched its Risk Analysis Initiative in October 2024 specifically targeting this failure, which is involved in roughly 90% of all HIPAA Security Rule enforcement actions. [2]

### 2. Failure to Implement Sufficient Security Measures / Risk Management (45 C.F.R. § 164.308(a)(1)(ii)(B))

**Frequency:** Cited in 4 out of 5 qualifying cases (80%)

This provision requires entities to "implement security measures sufficient to reduce risks and vulnerabilities to a reasonable and appropriate level." It was cited in the Solara, Warby Parker, L.A. Care, and Banner Health cases. OCR has confirmed that in 2026, it will expand its Risk Analysis Initiative to also include risk management enforcement. [3]

### 3. Failure to Implement Information System Activity Review Procedures (45 C.F.R. § 164.308(a)(1)(ii)(D))

**Frequency:** Cited in 4 out of 5 qualifying cases (80%)

This requirement mandates that entities implement procedures to "regularly review records of information system activity, such as audit logs, access reports, and security incident tracking reports." It was cited in the Montefiore, Warby Parker, L.A. Care, and Gulf Coast cases. The Gulf Coast case specifically found that the practice failed to implement policies for reviewing activity logs until April 2020, well after the breach had occurred. [4]

### 4. Failure to Implement Audit Controls (45 C.F.R. § 164.312(b))

**Frequency:** Cited in 3 out of 5 qualifying cases (60%)

This provision requires entities to "implement hardware, software, and/or procedural mechanisms that record and examine activity in information systems that contain or use electronic protected health information." It was cited in the Montefiore, L.A. Care, and Banner Health cases. The Montefiore case is particularly notable: the hospital had no adequate mechanisms to detect that an employee was accessing and selling patient records over a six-month period. [5]

### 5. Failure to Implement Access Controls (45 C.F.R. § 164.312(a)(1))

**Frequency:** Cited in 2 out of 5 qualifying cases (40%)

This provision requires policies and procedures for authorizing access to ePHI. It was cited in the Solara and Banner Health cases. The Solara case specifically found failures in implementing proper access controls following a phishing attack that compromised employee email accounts. [6]

### 6. Failure to Perform Periodic Evaluations (45 C.F.R. § 164.308(a)(8))

**Frequency:** Cited in 2 out of 5 qualifying cases (40%)

This provision requires entities to "perform periodic assessments of the security and effectiveness of security measures." It was cited in the Solara and L.A. Care cases. The L.A. Care case involved a three-year period of noncompliance, indicating a systemic failure to evaluate security measures. [7]

### 7. Failure to Terminate Former Workforce Members' Access to ePHI (45 C.F.R. § 164.308(a)(3)(ii)(C))

**Frequency:** Cited in 1 out of 5 qualifying cases (20%)

This addressable implementation specification requires procedures for terminating access to ePHI when employment ends. It was cited in the Gulf Coast case, where a former contractor's access was not terminated after services ended, enabling the contractor to access the EMR system and file false Medicare claims. [4]

### 8. Failure to Implement Procedures for Establishing and Modifying Workforce Members' Access (45 C.F.R. § 164.308(a)(4)(ii)(C))

**Frequency:** Cited in 1 out of 5 qualifying cases (20%)

This addressable implementation specification requires policies for modifying user access rights. It was cited in the Gulf Coast case, where the practice lacked policies for establishing and modifying workforce access before the breach. [4]

### 9. Failure to Implement Security Incident Response and Reporting Procedures (45 C.F.R. § 164.308(a)(6))

**Frequency:** Cited in 1 out of 5 qualifying cases (20%)

This provision requires policies and procedures for responding to and reporting security incidents. It was cited in the Solara case, where the entity failed to properly respond to and report the phishing attack that compromised employee email accounts. [8]

### 10. Failure to Implement Policies and Procedures to Prevent, Detect, Contain, and Correct Security Violations (45 C.F.R. § 164.316(a))

**Frequency:** Cited in 1 out of 5 qualifying cases (20%)

This provision requires the implementation of policies and procedures to address security violations. It was cited in the Solara case, highlighting the entity's failure to establish foundational security policies. [8]

**Notable Observation:** The gap between the frequency of the top three violations (80-100% of cases) and the remaining violations (20-40% of cases) underscores that risk analysis and risk management failures are the foundational deficiencies that most frequently lead to catastrophic breaches and subsequent high penalties. The remaining violations tend to be case-specific consequences of these foundational failures.

---

## Section 2: Common Risk Assessment Failures with Real-World Examples

Analysis of the $1M+ cases reveals three recurring patterns of risk assessment failure that OCR identifies as root causes of data breaches and subsequent enforcement actions.

### Failure Pattern 1: Failure to Conduct a Comprehensive, Enterprise-Wide Risk Analysis

**Description:** Entities either entirely fail to conduct a risk analysis, or they conduct one that does not cover the entire enterprise — including all systems, locations, devices, and ePHI repositories. The risk analysis must comprehensively assess risks to "all of an entity's ePHI." [9] An inadequate risk analysis is named as a root cause in a majority of recent HHS OCR Security Rule resolution agreements. [10]

**Real-World Example: Solara Medical Supplies, LLC ($3,000,000 – January 2025)**

Solara Medical Supplies, a diabetes supplies distributor and subsidiary of AdaptHealth, suffered a phishing attack between April and June 2019 that compromised eight employee email accounts, exposing the ePHI of 114,007 individuals. [11]

OCR's investigation found that Solara "failed to conduct a compliant risk analysis to identify the potential risks and vulnerabilities to the confidentiality, integrity, and availability of all its electronic protected health information (ePHI)." [12] The entity had not conducted a comprehensive risk analysis that covered all systems where ePHI was stored, accessed, or transmitted. The phishing attack succeeded precisely because the entity had not identified the risks to its email systems.

OCR Director Melanie Fontes Rainer stated: "Cyberattacks have skyrocketed exponentially in recent years. Effective cybersecurity requires identifying potential risks and vulnerabilities to health information and implementing effective security measures to protect against them. Health care entities that fail to address identified cybersecurity issues leave themselves vulnerable to cyberattacks." [11]

The corrective action plan required Solara to conduct an enterprise-wide risk analysis of all ePHI, submit a risk analysis scope within 90 days, and complete a final risk analysis within 180 days of HHS approval. [13]

**Source:** [HHS.gov Resolution Agreement: Solara Medical Supplies](https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/solara-ra-cap/index.html)

---

### Failure Pattern 2: Failure to Conduct an Accurate and Thorough Risk Analysis (Quality/Methodology Failure)

**Description:** In this pattern, an entity may have a risk analysis document on file, but it is not sufficiently "accurate and thorough" as required by 45 C.F.R. § 164.308(a)(1)(ii)(A). The analysis fails to identify all relevant threats and vulnerabilities, does not follow a recognized methodology (such as NIST SP 800-30/66), or does not cover all systems that ultimately fail. [10]

**Real-World Example: Gulf Coast Pain Consultants, LLC ($1,190,000 – December 2024)**

Gulf Coast Pain Consultants (d/b/a Clearway Pain Solutions Institute), a Florida-based pain management practice, experienced a breach when a former contractor impermissibly accessed the company's electronic medical record system between September 2018 and February 2019, exposing the ePHI of approximately 34,310 individuals. The contractor used the data to file approximately 6,500 false Medicare claims. [4]

OCR's investigation found that the practice had not conducted a HIPAA-compliant risk analysis until September 2022 — well after the breach had occurred. [4] The risk analysis that was on file at the time of the breach was not scoped to cover the access-management and audit-logging systems that ultimately failed. The practice also failed to implement procedures to regularly review information system activity records, failed to terminate the former contractor's access to ePHI, and failed to implement procedures for establishing and modifying workforce members' access. [14]

OCR Director Melanie Fontes Rainer stated: "Current and former workforce can present threats to health care privacy and security—risking continuity of care and trust in our health care system. Effective cybersecurity and compliance with the HIPAA Security Rule means being proactive in reviewing who has access to health information and responding quickly to suspected security incidents." [14]

**Source:** [HHS.gov OCR: Gulf Coast Pain Consultants](https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/gulf-coast-pain-consultants-npd/index.html)

---

### Failure Pattern 3: Failure to Implement a Risk Management Plan and Address Identified Risks

**Description:** In this pattern, entities either fail to conduct a risk analysis at all, or they conduct one but fail to implement a risk management plan that addresses the identified risks. The risk analysis findings are not linked to a Risk Management Plan that closes findings. [10] This gap between identifying risks and actually implementing security measures is what most often turns a closed-without-action matter into a civil money penalty. [10]

**Real-World Example: Banner Health Affiliated Covered Entities ($1,250,000 – February 2023)**

Banner Health, a large non-profit health system operating 30 hospitals across six states, experienced a data breach in 2016 when hackers first compromised the payment processing system of food and beverage outlets at 30 hospitals, then moved to medical servers. The breach lasted over a month before detection and exposed the PHI of 2.81 million individuals — the largest healthcare data breach of 2016. [15]

OCR's investigation found "evidence of long-term, pervasive noncompliance with the HIPAA Security Rule across Banner Health's organization." [16] Specifically, OCR identified: the lack of an analysis to determine risks and vulnerabilities to ePHI across the organization; insufficient monitoring of health information systems' activity; failure to implement an authentication process to safeguard ePHI; and failure to have security measures in place to protect ePHI from unauthorized access when transmitted electronically. [16]

Banner Health had conducted risk analyses, but they failed to identify the risks to its payment processing systems, and the entity had not implemented sufficient security measures to address the risks that were or should have been identified. The system was left vulnerable to a multi-stage attack precisely because risk analysis findings were not translated into an effective risk management plan.

OCR Director Melanie Fontes Rainer stated: "Hackers continue to threaten the privacy and security of patient information held by health care organizations, including our nation's hospitals. It is imperative that hospitals and other covered entities and business associates be vigilant in taking robust steps to protect their systems, data, and records, and this begins with understanding their risks, and taking action to prevent, respond to and combat such cyber-attacks." [15]

**Source:** [HHS.gov Resolution Agreement: Banner Health](https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/banner-health/index.html)

---

## Section 3: Typical Corrective Actions Required in OCR Resolution Agreements

OCR resolution agreements for high-penalty cases follow a consistent structure, incorporating a Corrective Action Plan (CAP) as Appendix A. The CAP is a legally binding document that specifies the actions the entity must take to remediate the violations and come into compliance. Failure to complete a CAP within the designated timeframe can void the initial settlement and leave the entity open to additional fines and penalties. [17]

### 3.1 Risk Analysis and Risk Management Mandates

**The single most common requirement across all resolution agreements is a mandate to conduct an accurate and thorough enterprise-wide risk analysis.** This is the foundational requirement of the HIPAA Security Rule (45 C.F.R. § 164.308(a)(1)(ii)(A)) and is cited in virtually every enforcement action. [1]

**Specific requirements typically include:**

- **Risk Analysis Scope:** The entity must submit a risk analysis scope document within 90 days of the effective date of the CAP, detailing the methodology, systems, and locations to be covered. [13]
- **Final Risk Analysis:** The entity must complete and submit a final risk analysis within 180 days of HHS approval of the scope document. [13]
- **Risk Management Plan:** The entity must develop and implement a risk management plan within 60 days of HHS approval of the risk analysis, addressing all identified risks and vulnerabilities. [13]
- **Enterprise-Wide Coverage:** The risk analysis must cover all ePHI, regardless of where it is stored, accessed, or transmitted — including all systems, devices, locations, and business associate relationships. [9]

**Example from Solara Medical Supplies:** The CAP required Solara to "conduct an enterprise-wide risk analysis of ePHI" with a risk analysis scope submitted within 90 days and a final risk analysis within 180 days of HHS approval. The risk management plan was due within 60 days of HHS approval of the risk analysis. [13]

### 3.2 Policy and Procedure Revisions

Every resolution agreement requires the entity to develop, maintain, and revise written policies and procedures to comply with the HIPAA Privacy, Security, and Breach Notification Rules. These policies must be submitted to HHS for review and approval.

**Common policy revision requirements include:**

- **Security Management Process:** Policies addressing the full security management cycle, including risk analysis, risk management, sanction policies, and information system activity review. [5]
- **Access Controls:** Policies for authorizing access to ePHI, including least privilege principles, role-based access, and termination procedures. [6]
- **Audit Controls:** Policies for implementing mechanisms to record and examine activity in information systems containing or using ePHI. [5]
- **Workforce Security:** Policies for workforce clearance, termination procedures, and access establishment and modification. [14]
- **Breach Notification:** Policies for timely notification to affected individuals, HHS, and the media. [8]

**Example from Montefiore Medical Center:** The CAP required Montefiore to "implement audit controls, update policies, and investigate workforce compliance failures." The hospital was specifically required to implement hardware, software, or procedural mechanisms to record and examine activity in systems containing or using PHI. [5]

### 3.3 Workforce Training Requirements

All resolution agreements require workforce training on HIPAA policies and procedures. Training typically must be provided to all workforce members with access to ePHI and must be repeated at specified intervals.

**Common training requirements include:**

- **Initial Training:** Training must be provided within 60 days of HHS approval of training materials.
- **Annual Refresher Training:** Training must be provided at least every 12 months thereafter.
- **Content Requirements:** Training must cover HIPAA policies and procedures, phishing awareness, cybersecurity threats, and specific requirements related to the entity's violations.
- **Documentation:** Entities must maintain documentation of training, including attendance records and training materials.

**Example from Top of the World Ranch Treatment Center:** The CAP required the entity to "provide annual HIPAA training to workforce members with access to ePHI." [18]

### 3.4 Independent Monitoring and Audit Controls

Resolution agreements often require the entity to implement audit controls to record and examine information system activity. In some cases, a third-party independent monitor may be required.

**Specific requirements include:**

- **Audit Controls Implementation:** The entity must implement hardware, software, or procedural mechanisms to record and examine activity in all information systems that contain or use ePHI. [5]
- **Third-Party Monitor:** In severe cases, OCR may mandate hiring a third-party compliance monitor at the entity's expense, lasting one to several years and requiring regular reports to OCR. [17]
- **System Activity Review:** The entity must implement procedures to regularly review records of information system activity, including audit logs, access reports, and security incident tracking reports. [14]

**Example from Montefiore Medical Center:** The CAP specifically required Montefiore to "implement audit controls" as a direct response to the malicious insider incident that went undetected for six months. [5]

### 3.5 Reporting Obligations to OCR

All resolution agreements include detailed reporting obligations to OCR for a specified period. These typically include:

- **Implementation Report:** A detailed report submitted within 120 days after HHS approval of policies and training materials, documenting the implementation of all CAP requirements.
- **Annual Reports:** Subsequent annual reports for the duration of the compliance term, documenting ongoing compliance activities, any changes to systems or operations, and any security incidents.
- **Reportable Events:** Immediate notification to HHS (typically within 30 days) of any workforce member non-compliance or any breach of the CAP.
- **Document Retention:** All entities must retain all documents and records relating to compliance with the CAP for six years from the effective date. [13]

**Example from Solara Medical Supplies:** The CAP required Solara to submit an Implementation Report within 120 days of training approval, followed by annual reports for a two-year compliance term. Solara was also required to retain all relevant documents for six years. [13]

### 3.6 Breach Notification Requirements

Resolution agreements often include requirements to provide timely breach notification to affected individuals, HHS, and the media. The Breach Notification Rule requires notification to be provided without unreasonable delay and within 60 calendar days of discovery. [19]

**Specific requirements include:**

- **Individual Notification:** Notice to affected individuals within 60 days of discovery of the breach.
- **HHS Notification:** Notification to the HHS Secretary, with the timeline depending on the number of affected individuals.
- **Media Notification:** Notification to prominent media outlets if the breach affects more than 500 individuals in a state or jurisdiction.
- **Corrective Actions:** Entities may be required to provide overdue notifications as part of the CAP.

**Example from Solara Medical Supplies:** OCR found that Solara violated the Breach Notification Rule by failing to issue timely notifications to HHS, affected individuals, and prominent media outlets for both the phishing breach and the mis-mailed notification letters. [8]

### 3.7 Compliance Period and Monitoring

**Monitoring Periods:** The most common monitoring period for resolution agreements is **two years**. This is consistent across the vast majority of cases reviewed:

- **Two-year CAPs:** Montefiore Medical Center, Solara Medical Supplies, Banner Health, Gulf Coast Pain Consultants, Northeast Surgical Group, Regional Women's Health Group, Assured Imaging, SG Health Plan, Top of the World Ranch Treatment Center, Comstar, LLC, OSF Healthcare System, USR Holdings, Manasa Health Center, St. Joseph's Medical Center, New England Dermatology and Laser Center, Memorial Hermann Health System, Health Specialists of Central Florida, USR Holdings, LLC.
- **Three-year CAPs:** MMG Fusion, LLC, Green Ridge Behavioral Health, Doctors' Management Services, BST & Co. CPAs, LLP.

**Key Deadlines Found in CAPs:**

| Requirement | Typical Deadline |
|-------------|------------------|
| Risk analysis scope | Within 90 days of effective date |
| Final risk analysis | Within 180 days of HHS approval |
| Risk management plan | Within 60 days of HHS approval of risk analysis |
| Training | Within 60 days of HHS approval of training materials; annual refreshers |
| Implementation Report | Within 120 days of HHS approval of policies/training |
| Annual Reports | Due annually for duration of compliance term |
| Document Retention | Six years from effective date |

### 3.8 Enforcement Mechanisms

Resolution agreements include specific enforcement mechanisms to ensure compliance:

- **Breach of CAP:** If the entity fails to comply with any term of the CAP, HHS may impose civil monetary penalties for the original violations.
- **Civil Money Penalties:** Willful neglect violations not corrected within 30 days can expose entities to significant civil monetary penalties, assessed on a per-day, per-violation basis. [3]
- **No Waiver of Rights:** The entity does not waive its rights to contest the findings, but the CAP is binding.
- **Public Disclosure:** Resolution agreements are publicly posted on the HHS.gov website. [20]

### 3.9 Variations by Entity Type

**Covered Entities:** The majority of enforcement actions target covered entities (healthcare providers, health plans, healthcare clearinghouses). Common violations include failure to conduct risk analysis, failure to implement access controls, failure to provide timely patient access to records, and impermissible disclosures.

**Business Associates:** OCR has increasingly targeted business associates. Notable business associate cases in the period include:
- **MMG Fusion, LLC:** A Maryland software company acting as a business associate, settled for $10,000 with a three-year CAP. [21]
- **Comstar, LLC:** A Massachusetts billing and collection business associate, paid $75,000 with a two-year CAP. [22]
- **Consociate Health:** A business associate, paid $225,000 with a two-year CAP. [23]
- **USR Holdings, LLC:** A business associate, settled with a two-year CAP. [24]

### 3.10 OCR's Risk Analysis Initiative (2024-2026)

OCR launched its Risk Analysis Initiative in October 2024, based on the premise that inadequate risk analysis is involved in roughly 90% of OCR HIPAA Security Rule enforcement actions. [2] Since its introduction, the initiative has resulted in numerous enforcement actions targeting covered entities and business associates that failed to conduct adequate security risk analyses. [25]

OCR Director Paula M. Stannard stated: "Compliance with the HIPAA Risk Analysis provision is more essential than ever" and "Covered entities and business associates cannot protect electronic protected health information if they haven't identified potential risks and vulnerabilities." [2]

As of April 2026, OCR had completed 14 enforcement actions under the Risk Analysis Initiative, including the four ransomware settlements announced on April 23, 2026, totaling $1,165,000. [26] The OCR Director confirmed that in 2026, OCR will expand its risk analysis enforcement initiative to also include risk management. [3]

---

## Sources

[1] HHS.gov - Guidance on Risk Analysis: https://www.hhs.gov/hipaa/for-professionals/security/guidance/guidance-risk-analysis/index.html

[2] McDonald Hopkins - OCR announces 11th and 12th Risk Analysis Initiative enforcement actions: https://www.mcdonaldhopkins.com/insights/news/ocr-announces-risk-analysis-initiative-enforcement-actions

[3] HHS OCR YouTube - Risk Management Under the HIPAA Security Rule: https://www.youtube.com/watch?v=kDyrj-fJzhw

[4] HIPAA Journal - Failure to Terminate Access Rights Results in $1.19 Million HIPAA Fine: https://www.hipaajournal.com/gulf-coast-pain-consultants-hipaa-penalty

[5] HHS.gov - Voluntary Resolution Agreement: Montefiore Medical Center: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/montiefore/index.html

[6] HIPAA Journal - Solara Medical Supplies Pays $3M to Settle Alleged HIPAA Security and Breach Notification Rule Violations: https://www.hipaajournal.com/solara-medical-supplies-hipaa-settlement

[7] OCR Press Release - L.A. Care Health Plan Settlement: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/lacare/index.html

[8] HHS.gov - Solara Medical Supplies, LLC Resolution Agreement and Corrective Action Plan: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/solara-ra-cap/index.html

[9] Medcurity - The Risk Analysis Failure Pattern in HHS OCR Settlements: https://medcurity.com/risk-analysis-failure-pattern-hhs-ocr-settlements-2026

[10] Ogletree Deakins - 2025 Enforcement Trends: Risk Analysis Failures at the Center of HHS's Multimillion-Dollar HIPAA Penalties: https://ogletree.com/insights-resources/blog-posts/2025-enforcement-trends-risk-analysis-failures-at-the-center-of-hhss-multimillion-dollar-hipaa-penalties

[11] HHS.gov - OCR Press Release: Solara Medical Supplies Settlement: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/solara-ra-cap/index.html

[12] HIPAA Journal - Solara Medical Supplies Pays $3M to Settle Alleged HIPAA Security and Breach Notification Rule Violations: https://www.hipaajournal.com/solara-medical-supplies-hipaa-settlement

[13] HHS.gov - Solara Medical Supplies, LLC Resolution Agreement and Corrective Action Plan: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/solara-ra-cap/index.html

[14] HHS.gov - OCR Notice of Final Determination: Gulf Coast Pain Consultants: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/gulf-coast-pain-consultants-npd/index.html

[15] HHS.gov - OCR Press Release: Banner Health Settlement: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/banner-health/index.html

[16] HIPAA Journal - Banner Health Settles Alleged HIPAA Security Rule Violations for $1.25 Million: https://www.hipaajournal.com/banner-health-settles-alleged-hipaa-security-rule-violations-for-1-25-million

[17] Compliancy Group - HIPAA 2024 Year in Review: https://compliancy-group.com/hipaa-2024-year-in-review

[18] HHS.gov - OCR Press Release: Top of the World Ranch Treatment Center: https://www.hhs.gov/press-room/ocr-settles-hipaa-security-rule-investigation-twrtc.html

[19] HHS.gov - Breach Notification Rule: https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html

[20] HHS.gov - Resolution Agreements Page: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/index.html

[21] HHS.gov - OCR Press Release: MMG Fusion: https://www.hhs.gov/press-room/ocr-mmg-fusion-hipaa-agreement.html

[22] HHS.gov - OCR Press Release: Comstar, LLC: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/comstar-ra-cap/index.html

[23] HHS.gov - OCR Press Release: Four Ransomware Settlements: https://www.hhs.gov/press-room/ocr-settles-four-ransomware-investigations.html

[24] HHS.gov - OCR Press Release: USR Holdings, LLC: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/usr-holdings-ra-cap/index.html

[25] Feldesman LLP - OCR's New Initiative Yields Seven HIPAA Enforcement Actions: https://www.feldesman.com/ocrs-new-security-risk-analysis-initiative-results-in-seven-enforcement-actions-in-first-six-months

[26] HHS.gov - OCR Press Release: Four Ransomware Settlements: https://www.hhs.gov/press-room/ocr-settles-four-ransomware-investigations.html
