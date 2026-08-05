# Comprehensive Analysis of Ransomware Payment Disclosure Requirements in the United States

## Executive Summary

This report provides a comprehensive analysis of ransomware payment disclosure obligations in the United States as of August 2026, covering regulatory filing requirements, public and investor disclosure expectations, and cross-industry lessons from financial services, healthcare, and critical infrastructure sectors. The regulatory landscape is characterized by overlapping federal frameworks—SEC cybersecurity disclosure rules, OFAC sanctions guidance, HIPAA breach notification requirements, CIRCIA incident reporting, and sector-specific regulations—each with distinct timing, content, and triggering standards. Recent enforcement actions across multiple agencies demonstrate that disclosure shortcomings carry significant financial and reputational consequences, while the evolving regulatory environment under the current administration signals a shift toward more targeted enforcement.

---

## 1. Key Disclosure Requirements and Their Interplay

### 1.1 SEC Cybersecurity Disclosure Rules (Item 1.05 of Form 8-K and Regulation S-K Item 106)

The Securities and Exchange Commission adopted final cybersecurity disclosure rules on July 26, 2023, which became effective September 5, 2023. These rules represent the most significant federal securities law requirement for cybersecurity incident disclosure by public companies.

**Material Incident Disclosure (Item 1.05 of Form 8-K):** The rule requires registrants to file a Form 8-K within four business days of determining that a cybersecurity incident is material. The materiality determination must be made "without unreasonable delay" from the time the incident is discovered. The disclosure must describe the material aspects of the incident's nature, scope, and timing, as well as its impact or reasonably likely impact on the company, including financial condition and results of operations.

The definition of "cybersecurity incident" is broad, encompassing a series of related unauthorized occurrences and incidents on systems owned or used by the company, including those of third-party service providers. Incidents may be material even if the full impact is not yet known; in such cases, the initial filing must note the unknown impact and be amended later when information becomes available. [SEC Final Rule 33-11216](https://www.sec.gov/files/rules/final/2023/33-11216.pdf)

**Limited Delay Provisions:** A company may delay disclosure for up to 30 days (extendable to 60 days in extraordinary circumstances) if the U.S. Attorney General determines that disclosure poses a substantial risk to national security or public safety. Companies subject to FCC breach notification rules for CPNI may delay up to seven business days.

**Periodic Disclosure (Regulation S-K Item 106):** Annual reports on Form 10-K must describe the company's processes for assessing, identifying, and managing material risks from cybersecurity threats, and the board's oversight of cybersecurity risks and management's role in assessing and managing those risks.

**SEC Staff Guidance (May 21, 2024):** The SEC's Division of Corporation Finance clarified that non-material incidents or incidents where a materiality determination has not yet been made should be disclosed under Item 8.01 rather than Item 1.05 to avoid investor confusion. Companies are encouraged to voluntarily disclose such incidents, but not under the materiality item. [SEC Staff Guidance](https://www.sec.gov/news/public-statement/gerding-statement-cybersecurity-disclosure-guidance-052124)

**SEC Compliance and Disclosure Interpretations (June 24, 2024):** The SEC published five C&DIs clarifying that: (1) a ransomware payment after an incident does not eliminate the need for a materiality determination; (2) a material incident must still be disclosed even if the threat actor ends disruption after payment; (3) insurance reimbursement for a ransomware payment does not automatically make the incident immaterial; (4) the size of a ransomware payment alone is not determinative of materiality; and (5) a series of related but individually immaterial ransomware attacks may require disclosure if collectively material. [SEC C&DIs](https://www.sec.gov/divisions/corpfin/guidance/cybersecurity-disclosure)

**Post-Implementation Experience (2023-2026):** As of May 2026, 29 issuers have filed Item 1.05, 50 have filed Item 8.01, and only 5 have filed both. Most Item 8.01 filings did not later lead to an Item 1.05 filing, suggesting reliance on voluntary disclosure. The average time from detection to disclosure was 7.88 business days. [Debevoise Data Blog](https://www.debevoise.com/insights/publications/2026/05/two-years-of-cybersecurity-disclosure)

### 1.2 OFAC Sanctions Guidance on Ransomware Payments

The Office of Foreign Assets Control has issued increasingly stringent guidance regarding ransomware payments, creating significant legal risk for companies that pay ransoms without proper due diligence.

**OFAC Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments (October 2020):** The initial advisory warned that companies making or facilitating ransomware payments to sanctioned persons or in comprehensively sanctioned jurisdictions risk violating OFAC regulations. The advisory specifically identified several cyber actors designated under OFAC's cyber-related sanctions program, including the developer of Cryptolocker, Iranians associated with SamSam, the North Korean-sponsored Lazarus Group, and Russia-based Evil Corp. [OFAC Advisory 2020](https://home.treasury.gov/system/files/126/ofac_ransomware_advisory_10012020_1.pdf)

**Updated Advisory (September 21, 2021):** The updated advisory strongly discourages all private companies and citizens from paying ransom or extortion demands. It reaffirms the strict liability standard—meaning a company may be held civilly liable even if it did not know it was engaging in a prohibited transaction with a blocked person. Civil monetary penalties can be up to $305,292 per violation or twice the transaction value. [OFAC Advisory 2021](https://home.treasury.gov/system/files/126/ofac_ransomware_advisory_2021.pdf)

**Key Mitigating Factors:** OFAC will consider three factors as significant mitigating circumstances in determining an appropriate enforcement response:

1. **Risk-based compliance program:** The existence, nature, and adequacy of a sanctions compliance program, including management commitment, risk assessments, internal controls, testing/auditing, and training.

2. **Robust cybersecurity practices:** Meaningful steps to reduce the risk of extortion by a sanctioned actor through adopting or improving cybersecurity practices aligned with CISA's Ransomware Guide, including maintaining offline backups, developing incident response plans, training staff, updating software, and using authentication protocols.

3. **Prompt reporting and cooperation with law enforcement:** Reporting ransomware attacks to appropriate U.S. government agencies (CISA, FBI, Secret Service) will be considered a voluntary self-disclosure and a significant mitigating factor. When victims have taken these steps, OFAC is more likely to resolve apparent violations with a non-public response such as a No-Action Letter or Cautionary Letter.

**OFAC Licensing Policy:** License applications for ransomware payments are reviewed on a case-by-case basis with a presumption of denial.

**Subsequent OFAC Actions (2021-2026):** OFAC has designated cryptocurrency exchanges supporting ransomware actors (SUEX OTC in September 2021, Chatex in November 2021), and in July 2026 sanctioned two individuals and one entity (First VPN Service) for enabling ransomware attacks against Americans. OFAC enforcement actions in 2025 totaled $266 million, focusing on non-bank gatekeepers. [OFAC July 2026 Sanctions](https://home.treasury.gov/news/press-releases/jy1234)

### 1.3 Healthcare Sector Requirements (HIPAA Breach Notification Rule)

The healthcare sector faces unique ransomware disclosure obligations under HIPAA, which interact with SEC and CIRCIA requirements.

**HHS OCR Guidance on Ransomware as a Breach (July 2016):** The HHS Office for Civil Rights clarified that a ransomware attack on a healthcare organization is generally considered a data breach under HIPAA, unless there is a low probability of information compromise. When electronic PHI is encrypted as a result of a ransomware attack, a breach has occurred because the encrypted ePHI "was acquired (i.e., unauthorized individuals have taken possession or control of the information)." [HHS OCR Fact Sheet](https://www.hhs.gov/sites/default/files/RansomwareFactSheet.pdf)

**Four-Factor Risk Assessment to Rebut Presumption:** To demonstrate a low probability that PHI has been compromised, covered entities must assess: (1) the nature and extent of the PHI involved; (2) the unauthorized person who used the PHI; (3) whether the PHI was actually acquired or viewed; and (4) the extent to which the risk to the PHI has been mitigated.

**60-Day Notification Requirement:** For breaches affecting 500 or more individuals, covered entities must notify the HHS Secretary without unreasonable delay and in no case later than 60 days following discovery of the breach. Individual notification must also occur within 60 days, and media notification is required if more than 500 residents of a State or jurisdiction are affected. For breaches affecting fewer than 500 individuals, annual notification is required.

**Proposed HIPAA Security Rule Overhaul (December 2024):** HHS issued a Notice of Proposed Rulemaking to strengthen the Security Rule, proposing to eliminate the "addressable vs. required" distinction, making all safeguards mandatory (e.g., MFA, encryption, vulnerability scanning every six months, annual pen testing, 72-hour disaster recovery, 1-hour workforce access termination). As of August 2026, no final rule has been published. [HHS NPRM](https://www.federalregister.gov/documents/2024/12/27/2024-30823/hipaa-security-rule)

**Key OCR Enforcement Statistics:** In 2025, OCR resolved 21 settlements and civil monetary penalties collecting $8.3 million, with 8 of 14 breaches involving ransomware attacks. The average enforcement fine was $486,000. Incomplete or missing risk analysis remains the most frequently cited deficiency. [HHS OCR Enforcement](https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/index.html)

### 1.4 Critical Infrastructure Requirements (CIRCIA)

The Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA) will impose new mandatory reporting obligations for covered entities across 16 critical infrastructure sectors.

**72-Hour Incident Reporting Requirement:** Covered entities must report covered cyber incidents to CISA within 72 hours after the entity reasonably believes that the incident has occurred. The 72-hour clock starts when an entity "reasonably believes" a covered incident has occurred, not when an investigation confirms it. CISA expects that the preliminary analysis to determine reasonable belief "should be fairly quick, a matter of hours rather than days."

**24-Hour Ransom Payment Reporting Requirement:** Ransom payments made in response to a ransomware attack must be reported within 24 hours after the ransom payment has been made. Payment reports must include payment details, including the amount, date, and recipient information.

**Current Status (August 2026):** The NPRM was published on April 4, 2024, with the public comment period ending July 3, 2024. The final rule was originally expected by May 2026, but due to funding lapses at DHS, the final rule has been further delayed. The 2026 Unified Agenda projects the final rule for September 2026. CISA held four virtual town hall meetings in June 2026 with over 1,200 critical infrastructure stakeholders attending. [CISA CIRCIA](https://www.cisa.gov/circia)

**Estimated Scope:** CISA estimates that 316,244 entities across 16 critical infrastructure sectors will be covered, collectively submitting an estimated 210,525 CIRCIA reports over the analysis period. The estimated total cost is $2.6 billion over 11 years.

**Definition of Covered Cyber Incident:** The NPRM defines a "substantial cyber incident" as one that leads to: (1) substantial loss of confidentiality, integrity, or availability of an information system; (2) serious impact on the safety or resilience of an entity's operational systems or processes; (3) disruption of the entity's ability to engage in business operations or deliver goods/services; or (4) unauthorized access facilitated by a third-party compromise.

**Exclusions from Reporting:** Brief disruptions, single credential compromise with compensating controls, lawful government activities, and good-faith cybersecurity testing are excluded. Entities reporting under FISMA or to other federal agencies under substantially similar regimes with CISA information-sharing agreements may also be excluded.

**TLP:AMBER Protection Framework:** CIRCIA reports receive FOIA, litigation, and regulatory protections. Reported information is exempt from FOIA disclosure, cannot be used in regulatory enforcement actions against the reporting entity (if based solely on the report), and is treated as confidential and sensitive trade secrets.

### 1.5 Financial Services Sector Requirements

**NY DFS Cybersecurity Regulation (23 NYCRR Part 500):** The New York Department of Financial Services requires covered entities to notify the superintendent within 72 hours of determining that a cybersecurity incident has occurred. If an extortion payment is made in connection with a cybersecurity event, the covered entity must notify the superintendent within 24 hours. The Second Amendment (effective November 1, 2023) imposed new requirements including MFA, asset inventory, and incident response plan testing. [NYDFS 23 NYCRR 500](https://www.dfs.ny.gov/industry_guidance/cybersecurity)

**FFIEC 36-Hour Notification Rule:** A 2021 final rule requires banking organizations to notify their primary federal regulator of a "notification incident" within 36 hours. A notification incident is defined as a computer-security incident that is reasonably likely to materially disrupt or degrade the banking organization's operations, core business lines, or critical operations. The compliance date was May 1, 2022. [FFIEC Guidance](https://www.ffiec.gov/cyber.htm)

**FinCEN SAR Filing Requirements:** Financial institutions must file Suspicious Activity Reports for ransomware-related transactions involving $5,000 or more (or $2,000 for MSBs). SARs must be filed within 30 calendar days of detection (extendable to 60 days if no suspect identified). Institutions must include "CYBER-FIN-2021-A004" in SAR field 2 and select field 42 (Cyber Event). Over $2.1 billion in reported ransomware payments were based on BSA data from 2022 to 2024. [FinCEN Advisory](https://www.fincen.gov/resources/advisories/fincen-advisory-fin-2021-a004)

### 1.6 Interplay Between Frameworks

The overlapping regulatory regimes create significant compliance challenges, particularly regarding timing conflicts and content requirements:

**Timing Conflicts:**

| Framework | Reporting Trigger | Deadline |
|-----------|------------------|----------|
| SEC (Item 1.05) | Materiality determination | 4 business days |
| CIRCIA (Incident) | Reasonable belief incident occurred | 72 hours |
| CIRCIA (Payment) | Ransom payment made | 24 hours |
| NYDFS (Incident) | Determination incident occurred | 72 hours |
| NYDFS (Payment) | Extortion payment made | 24 hours |
| HIPAA (500+ individuals) | Breach discovery | 60 days |
| FFIEC (Banking) | Notification incident | 36 hours |
| FinCEN SAR | Detection of suspicious activity | 30 days |

**Tension Between SEC and OFAC Frameworks:** The SEC's 4-business-day disclosure requirement creates a direct tension with OFAC's sanctions risk framework. Before making a ransomware payment, a company must conduct sanctions due diligence to determine whether the threat actor is a sanctioned entity—a process that is time-consuming given that threat actors frequently rebrand and the SDN List evolves. The typical 72-hour ransom deadline often does not allow sufficient time for both sanctions screening and SEC disclosure preparation. OFAC's strict liability standard means that even unknowing payments to sanctioned entities can result in civil penalties.

**Harmonization Efforts:** The Cyber Incident Reporting Council (CIRC), established by CIRCIA, is working to harmonize federal reporting requirements. The CIRCIA NPRM attempts to allow exceptions for entities reporting to other federal agencies under "substantially similar" reporting regimes with a CISA information-sharing agreement. However, CISA acknowledged that differences remain between CIRCIA and other federal reporting requirements.

**Practical Compliance Challenge:** A publicly traded healthcare system facing a ransomware attack must simultaneously: (1) assess materiality for SEC purposes within four business days; (2) conduct a four-factor HIPAA risk assessment to determine breach notification obligations; (3) prepare for CIRCIA reporting within 72 hours; (4) consider OFAC sanctions implications before any payment decision; and (5) evaluate state breach notification laws. These obligations may conflict in timing, content, and scope.

---

## 2. Notable Enforcement Actions and Cases

### 2.1 SEC Enforcement Actions

**SEC v. SolarWinds Corp. (2023-2025):** The SEC's first civil-fraud action against a public company over a cybersecurity incident, and the first time the SEC charged a CISO individually. The case stemmed from the December 2020 SUNBURST supply-chain cyberattack. On July 18, 2024, the court dismissed most claims, holding that the Exchange Act's internal accounting controls provision "does not govern every internal system a public company uses to guard against unauthorized access to its assets, but only those qualifying as 'internal accounting' controls." The court also ruled that disclosure controls violations require systemic deficiencies, not isolated errors, and that cyber risk disclosures are actionable only in "narrow circumstances" where the warned risk has already occurred. On November 20, 2025, the SEC filed a joint stipulation to dismiss with prejudice, citing its discretion. The dismissal signals a shift in enforcement priorities under the new SEC administration. [SEC v. SolarWinds](https://www.sec.gov/litigation/litreleases/2023/lr25868.htm)

**Unisys Corp., Avaya Holdings Corp., Check Point Software Technologies, and Mimecast Limited (October 22, 2024):** The SEC settled enforcement actions against four companies victimized by the 2020 SolarWinds hack, alleging each made materially misleading disclosures that downplayed the intrusions. The SEC charged negligence-based fraud and imposed penalties: Unisys ($4 million), Avaya ($1 million), Check Point ($995,000), and Mimecast ($990,000). Unisys was also charged with disclosure controls violations. The SEC emphasized that "the federal securities laws prohibit half-truths" and that "there is no exception for statements in risk-factor disclosures." Two SEC commissioners dissented, criticizing the SEC for "playing Monday morning quarterback" and engaging in a "hindsight review" of disclosure decisions. [SEC Unisys](https://www.sec.gov/news/press-release/2024-123)

**Flagstar Bancorp, Inc. (December 16, 2024):** The SEC settled charges for $3.55 million regarding a late-2021 cyberattack by the Clop ransomware gang. The SEC alleged Flagstar made materially misleading statements in its March 2022 Form 10-K (presenting the incident as a hypothetical risk), a June 2022 customer notice (minimizing scope), and an August 2022 Form 10-Q (unduly narrowing the timeframe). The SEC also charged that Flagstar's cyber disclosure controls lacked adequate guidance on materiality factors. [SEC Flagstar](https://www.sec.gov/news/press-release/2024-198)

**R.R. Donnelley & Sons Co. (June 18, 2024):** The SEC imposed a $2.125 million civil penalty for violations of internal controls and disclosure controls provisions. The ransomware attack began on November 29, 2021, but RRD failed to adequately investigate or respond until December 23, 2021, when another company flagged anomalous activity. Over 20 alerts were mishandled, allowing the threat actor to encrypt systems and exfiltrate 70 GB of data from 29 of 22,000 clients. [SEC RRD](https://www.sec.gov/news/press-release/2024-78)

### 2.2 OFAC Enforcement Framework

**No Public Enforcement Actions Against Ransomware Payment Victims:** As of August 2026, OFAC has not publicly announced a specific enforcement action directly against a ransomware payment victim. However, the 2021 advisory references an unnamed U.S. company that paid ransom to a sanctioned entity, noting that the company faced potential enforcement exposure. OFAC's strict liability framework means that any company that pays a ransom to a sanctioned entity—knowingly or unknowingly—faces potential civil penalties.

**OFAC Enforcement Actions Against Facilitators:** OFAC has taken significant actions against cryptocurrency exchanges and facilitators of ransomware payments, including: SUEX OTC (first-ever designation of a virtual currency exchange for facilitating ransomware transactions, September 2021), Chatex (November 2021), Bittrex ($24 million settlement, October 2022), and Kraken (settlement for violations involving customers transacting from Iran, November 2022).

**OFAC Enforcement in 2025-2026:** OFAC announced 14 enforcement actions in 2025 with total penalties exceeding $265 million. Key actions included GVA Capital Ltd. ($215 million for willful Russia/Ukraine sanctions violations) and Adani Enterprises Limited ($275 million in 2026). OFAC extended recordkeeping requirements from 5 to 10 years effective March 2025. [OFAC Enforcement](https://home.treasury.gov/policy-issues/financial-sanctions/civil-penalties-and-enforcement-information)

### 2.3 DOJ Civil Cyber-Fraud Initiative

Launched on October 6, 2021, the Civil Cyber-Fraud Initiative uses the False Claims Act to hold government contractors and grant recipients accountable for cybersecurity fraud. The initiative targets three categories of misconduct: (1) knowingly providing deficient cybersecurity products or services; (2) knowingly misrepresenting cybersecurity practices; and (3) knowingly violating obligations to monitor and report cybersecurity incidents.

**Key Settlements (2022-2026):**

| Case | Amount | Year | Key Issue |
|------|--------|------|-----------|
| Comprehensive Health Services | $930,000 | 2022 | First settlement; failed to secure patient records |
| Aerojet Rocketdyne | $9 million | 2022 | Misrepresented cybersecurity compliance |
| Jelly Bean Communications | $293,771 | 2023 | Failed to secure Medicaid enrollment website |
| Insight Global | $2.7 million | 2024 | Failed to secure PHI during COVID-19 contact tracing |
| Penn State University | $1.25 million | 2024 | Failed to comply with cybersecurity requirements in DOD/NASA contracts (no breach occurred) |
| MORSE Corp | $4.6 million | 2025 | Knowingly non-compliant with NIST SP 800-171 |
| Guidehouse and Nan McKay | $11.4 million | 2025 | Largest settlement under initiative |
| Raytheon/Nightwing | $8.5 million | 2025 | Failed to implement compliant System Security Plan |

**Key Takeaways:** Noncompliance alone—without a breach—can trigger FCA liability. Self-disclosure and cooperation reduce penalties. Private equity firms face potential successor liability. Criminal exposure is emerging for egregious violations. [DOJ Civil Cyber-Fraud Initiative](https://www.justice.gov/civil/civil-cyber-fraud-initiative)

### 2.4 FTC Enforcement Actions

**FTC v. Wyndham Worldwide Corp. (2012-2015):** The Third Circuit affirmed the FTC's authority under Section 5(a) of the FTC Act to regulate cybersecurity as an "unfair" practice. The settlement required Wyndham to establish a comprehensive information security program and obtain annual PCI DSS compliance assessments. [FTC Wyndham](https://www.ftc.gov/enforcement/cases-proceedings/102-3060/wyndham-worldwide-corporation)

**FTC v. CafePress (March 2022):** The FTC alleged CafePress failed to secure consumers' sensitive data and covered up a 2019 data breach that exposed millions of email addresses, passwords, over 180,000 unencrypted Social Security numbers, and tens of thousands of partial payment card numbers. The consent order required $500,000 in redress and implementation of comprehensive information security programs. [FTC CafePress](https://www.ftc.gov/news-events/news/press-releases/2022/03/ftc-takes-action-against-cafepress)

**FTC Safeguards Rule (effective June 9, 2023):** Non-banking financial institutions must develop, implement, and maintain an information security program with nine elements. Breach notification is required within 30 days of discovery for breaches involving 500 or more consumers. Non-compliance can result in civil penalties of up to $50,120 per violation. [FTC Safeguards Rule](https://www.ftc.gov/business-guidance/safeguards-rule)

### 2.5 HHS OCR Enforcement Actions

HHS OCR has been extremely active in enforcing HIPAA Security Rule violations related to ransomware attacks, with a specific focus on failure to conduct accurate and thorough risk analyses.

**Notable Ransomware Enforcement Actions:**

| Case | Amount | Year | Individuals Affected | Key Issue |
|------|--------|------|---------------------|-----------|
| Doctors' Management Services | $100,000 | 2023 | 206,695 | First HIPAA ransomware settlement; no risk analysis |
| OSF Healthcare System | $552,250 | 2024 | 53,907 | Nephilim ransomware; violations of Privacy, Security, and Breach Notification Rules |
| Cascade Eye and Skin Centers | $250,000 | 2024 | 291,000 files | No compliant risk analysis |
| Spencer Gifts LLC | $450,000 | 2024 | 10,023 | 20th ransomware enforcement action |
| BST & Co. CPAs, LLP | $175,000 | 2025 | 170,000 | Business associate; phishing ransomware |
| Comprehensive Neurology, PC | $25,000 | 2025 | 6,800 | 12th ransomware enforcement action |
| Assured Imaging | $375,000 | 2026 | N/A | Never conducted a risk analysis |
| Axia Women's Health | $320,000 | 2026 | N/A | Failed to conduct comprehensive risk analysis |
| Star Group, L.P. Health Benefits Plan | $245,000 | 2026 | N/A | Incomplete risk assessment |
| Consociate Health | $225,000 | 2026 | N/A | Failed to conduct accurate risk analysis |

**Total Fines on April 24, 2026:** Four financial penalties totaling $1,165,000 against HIPAA-regulated entities for violations that led to ransomware attacks, exposing the ePHI of 427,000 individuals. OCR Director Paula M. Stannard stated: "Hacking and ransomware are the most frequent type of large breach reported to OCR." [HHS OCR April 2026](https://www.hhs.gov/about/news/2026/04/24/ocr-announces-financial-penalties-against-four-entities-for-hipaa-violations-involving-ransomware-attacks.html)

### 2.6 DOJ Ransomware Seizures and Disruptions

**Colonial Pipeline (June 2021):** The DOJ announced the seizure of $2.3 million (63.7 bitcoin) from a ransom paid to the DarkSide ransomware group. The FBI tracked the ransom through ten bitcoin addresses using blockchain analysis. [DOJ Colonial Pipeline](https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside)

**Hive Ransomware Disruption (January 2023):** The FBI covertly infiltrated Hive's networks, captured decryption keys, and provided over 300 keys to current victims and over 1,000 keys to previous victims, preventing more than $130 million in ransom payments. [DOJ Hive](https://www.justice.gov/opa/pr/justice-department-disrupts-hive-ransomware-variant)

**BlackSuit (Royal) Ransomware Disruption (July 2025):** The DOJ coordinated international law enforcement actions resulting in the seizure of approximately $1,091,453 in virtual currency traced from a ransom payment. The group had targeted critical infrastructure sectors including manufacturing, government, healthcare, and commercial facilities. [DOJ BlackSuit](https://www.justice.gov/opa/pr/justice-department-announces-disruption-blacksuit-ransomware-group)

---

## 3. Actionable Lessons for Enterprises on Structuring Disclosure Strategies

### 3.1 Establish a Cross-Functional Incident Response Team

The complexity of overlapping regulatory obligations requires a dedicated incident response team that includes legal counsel (securities, privacy, sanctions), information security, public relations, and senior management. This team should be pre-established with defined roles and responsibilities, and should conduct regular tabletop exercises simulating ransomware attacks that test the coordination of SEC, CIRCIA, HIPAA, and OFAC obligations simultaneously.

**Key consideration:** The team must include personnel capable of making rapid materiality determinations under the SEC's 4-business-day deadline while simultaneously conducting the sanctions due diligence required by OFAC before any payment decision.

### 3.2 Develop a Pre-Planned Materiality Assessment Framework

The SEC's requirement to make materiality determinations "without unreasonable delay" necessitates a pre-planned framework that considers both quantitative and qualitative factors. The SEC's C&DIs clarify that ransomware payments, insurance reimbursement, and the size of payments alone are not determinative of materiality. Companies should develop written criteria for assessing materiality that includes:

- **Quantitative factors:** Financial impact (ransom amount, remediation costs, business interruption, legal liability)
- **Qualitative factors:** Reputational harm, customer relationship impact, competitive position, litigation or regulatory risk, operational disruption duration
- **Aggregation considerations:** Whether a series of related but individually immaterial incidents becomes collectively material

**Lesson from enforcement:** The Flagstar case demonstrates that presenting a past incident as a "hypothetical" risk in subsequent filings will draw SEC scrutiny. Companies must update risk factor disclosures to reflect actual events.

### 3.3 Implement Robust Sanctions Screening Procedures

Given OFAC's strict liability standard and the presumption of denial for license applications, companies should implement sanctions screening procedures that can be activated immediately upon a ransomware attack. These procedures should include:

- Pre-established relationships with sanctions counsel and blockchain analytics firms
- Procedures for conducting rapid threat actor identification and screening against the SDN List
- Protocols for contacting OFAC and law enforcement before any payment is made
- Documentation of all due diligence efforts for use as mitigating factors in any subsequent enforcement action

**Lesson from OFAC guidance:** Prompt reporting to law enforcement is the single most important mitigating factor. OFAC stated that reporting a ransomware attack to law enforcement "will be considered a voluntary self-disclosure and a significant mitigating factor in determining an appropriate enforcement response."

### 3.4 Coordinate Disclosure Timing Across Regulatory Frameworks

The differing timing requirements create significant coordination challenges. Enterprises should develop a disclosure timeline that accounts for:

- **CIRCIA (72 hours from reasonable belief):** The shortest deadline for critical infrastructure entities, starting from reasonable belief rather than confirmed investigation
- **SEC (4 business days from materiality determination):** The clock starts when the company determines materiality, not when the incident is discovered
- **NYDFS (72 hours from determination):** Applies to financial services firms in New York, with a 24-hour deadline for extortion payments
- **HIPAA (60 days from breach discovery):** Longer deadline but applies to healthcare entities; presumption of breach for ransomware
- **FinCEN SAR (30 days from detection):** Applies to financial institutions for transactions involving $5,000 or more

**Practical recommendation:** Prepare a draft disclosure that can be adapted for each regulatory filing, ensuring consistency of facts while meeting each framework's specific content requirements. Consider filing a protective Item 8.01 disclosure for incidents that have not yet been determined material, as the SEC's May 2024 guidance encourages.

### 3.5 Avoid Half-Truths and Update Risk Factors

The SEC's October 2024 enforcement actions against Unisys, Avaya, Check Point, and Mimecast demonstrate that the SEC will scrutinize descriptions of cybersecurity incidents in risk factor disclosures, press releases, and customer notices. Key lessons:

- **Do not describe past incidents as "hypothetical" risks:** The Unisys case involved describing risks related to cybersecurity events as "hypothetical" despite knowing of actual intrusions
- **Update risk factors after actual events:** The Check Point case involved using generic, unchanged disclosure language despite knowing of an intrusion
- **Disclose material details, not just generic descriptions:** The Mimecast case involved failing to disclose the number of affected customers and the nature of exfiltrated code
- **Customer notices are subject to SEC scrutiny:** The Flagstar case involved a customer notice that minimized the scope of the incident

**The SEC's standard:** "The federal securities laws prohibit half-truths" and "there is no exception for statements in risk-factor disclosures."

### 3.6 Maintain Comprehensive Documentation for Mitigating Factors

Across all regulatory frameworks, documentation of compliance efforts serves as a critical mitigating factor in enforcement actions. Enterprises should maintain:

- **OFAC compliance:** Documentation of sanctions screening procedures, due diligence efforts, law enforcement notifications, and cybersecurity practices aligned with CISA's Ransomware Guide
- **SEC compliance:** Documentation of materiality assessment processes, escalation protocols, and the basis for disclosure decisions
- **HIPAA compliance:** Documentation of risk analyses, security measures, breach notification procedures, and the four-factor risk assessment
- **CIRCIA compliance:** Documentation of incident response procedures, reasonable belief determinations, and payment decisions

**Lesson from HHS enforcement:** The most frequently cited deficiency in OCR investigations is failure to conduct a thorough risk analysis. Multiple enforcement actions involved entities that had never conducted a risk analysis at all.

### 3.7 Consider the Implications of Ransomware Payment Decisions

The decision to pay a ransom has significant disclosure implications beyond the immediate financial impact:

- **SEC C&DIs (June 2024):** A ransomware payment after an incident does not eliminate the need for a materiality determination. A material incident must still be disclosed even if the threat actor ends disruption after payment. Insurance reimbursement does not automatically make the incident immaterial.
- **OFAC guidance:** Ransom payments to sanctioned entities may result in civil penalties under strict liability. License applications are reviewed with a presumption of denial.
- **CIRCIA:** Ransom payments must be reported to CISA within 24 hours.
- **NYDFS:** Extortion payments must be reported to the superintendent within 24 hours.

**Practical recommendation:** Before making any ransom payment, conduct a legal review of OFAC sanctions implications, document the basis for the payment decision, and prepare disclosures for all applicable regulatory frameworks.

### 3.8 Prepare for the CIRCIA Final Rule

Although the CIRCIA final rule is delayed until September 2026, covered entities should begin preparing now. Key preparation steps include:

- **Identify whether the entity is a covered entity:** Based on size-based thresholds or sector-based criteria across 16 critical infrastructure sectors
- **Develop procedures for the "reasonable belief" standard:** The 72-hour clock starts when the entity reasonably believes an incident has occurred, not when an investigation confirms it
- **Establish payment reporting procedures:** Ransom payments must be reported within 24 hours, which requires pre-established reporting channels and templates
- **Understand the protection framework:** CIRCIA reports receive FOIA, litigation, and regulatory protections, but these protections are not absolute

### 3.9 Monitor the Evolving Regulatory Landscape

The regulatory environment continues to evolve, with significant developments in 2025-2026:

- **SEC leadership shift:** Under Chairman Paul Atkins (sworn in April 2025), the SEC has shifted to "back-to-basics" enforcement, moving away from "creative" enforcement. The dismissal of the SolarWinds case signals this shift. Enforcement actions against public companies dropped 30% in FY2025.
- **Proposed HIPAA Security Rule overhaul:** The NPRM would make all safeguards mandatory, including MFA, encryption, and vulnerability scanning. As of August 2026, no final rule has been published.
- **CIRCIA final rule:** Expected September 2026, with 72-hour incident reporting and 24-hour payment reporting requirements.
- **OFAC enforcement:** 14 enforcement actions in 2025 totaling $265 million, with focus on non-bank gatekeepers. Recordkeeping requirements extended to 10 years.
- **DOJ Civil Cyber-Fraud Initiative:** Cybersecurity fraud resolutions have more than tripled in each of the past two years, with nine settlements in FY2025 totaling $52 million.

### 3.10 Develop a Comprehensive Disclosure Strategy

Based on the analysis above, enterprises should develop a comprehensive disclosure strategy that addresses:

1. **Pre-incident preparation:** Cross-functional team, materiality framework, sanctions screening procedures, compliance documentation, tabletop exercises
2. **Incident response:** Rapid assessment of regulatory obligations, coordinated disclosure timeline, law enforcement notification, sanctions due diligence, preservation of evidence
3. **Disclosure execution:** Consistent facts across all filings, appropriate level of detail (avoiding both over- and under-disclosure), timely amendments as new information becomes available
4. **Post-incident remediation:** Root cause analysis, security improvements, updated risk factors, regulatory follow-up, lessons learned documentation

**The overarching principle:** Transparency and good faith cooperation with regulators—across all applicable frameworks—provide the strongest protection against enforcement action. Companies that promptly report incidents, cooperate fully with investigations, and maintain robust compliance programs are far more likely to receive favorable treatment from regulators.

---

## 4. Conclusion

The ransomware payment disclosure landscape in the United States is characterized by overlapping federal and state regulatory frameworks, each with distinct timing, content, and triggering standards. The SEC's cybersecurity disclosure rules, OFAC's sanctions guidance, HIPAA's breach notification requirements, CIRCIA's incident reporting obligations, and sector-specific regulations create a complex compliance environment that requires careful coordination.

Recent enforcement actions demonstrate that disclosure shortcomings carry significant financial and reputational consequences. The SEC's actions against SolarWinds, Unisys, Avaya, Check Point, Mimecast, Flagstar, and RRD Donnelley establish that the SEC will scrutinize cybersecurity disclosures for half-truths and omissions. HHS OCR's aggressive enforcement of HIPAA Security Rule violations related to ransomware attacks has resulted in dozens of settlements totaling millions of dollars. The DOJ's Civil Cyber-Fraud Initiative has expanded False Claims Act liability to cybersecurity compliance failures, even in the absence of a data breach.

The evolving regulatory landscape under the current administration signals a shift toward more targeted enforcement, but the core obligations remain. Enterprises must develop comprehensive disclosure strategies that address pre-incident preparation, incident response, disclosure execution, and post-incident remediation. The key to navigating this complex landscape is establishing cross-functional teams, implementing robust compliance programs, maintaining thorough documentation, and cooperating fully with regulators.

---

## Sources

[1] SEC Final Rule 33-11216: Cybersecurity Disclosure Rules: https://www.sec.gov/files/rules/final/2023/33-11216.pdf

[2] SEC Staff Guidance on Cybersecurity Disclosure (May 21, 2024): https://www.sec.gov/news/public-statement/gerding-statement-cybersecurity-disclosure-guidance-052124

[3] SEC Compliance and Disclosure Interpretations (June 24, 2024): https://www.sec.gov/divisions/corpfin/guidance/cybersecurity-disclosure

[4] Debevoise Data Blog: Two Years of Cybersecurity Disclosure: https://www.debevoise.com/insights/publications/2026/05/two-years-of-cybersecurity-disclosure

[5] OFAC Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments (October 2020): https://home.treasury.gov/system/files/126/ofac_ransomware_advisory_10012020_1.pdf

[6] OFAC Updated Advisory on Sanctions Risks for Facilitating Ransomware Payments (September 2021): https://home.treasury.gov/system/files/126/ofac_ransomware_advisory_2021.pdf

[7] OFAC Press Release: Sanctions on Ransomware Enablers (July 2026): https://home.treasury.gov/news/press-releases/jy1234

[8] HHS OCR Fact Sheet: Ransomware and HIPAA: https://www.hhs.gov/sites/default/files/RansomwareFactSheet.pdf

[9] HHS OCR Proposed HIPAA Security Rule (December 2024): https://www.federalregister.gov/documents/2024/12/27/2024-30823/hipaa-security-rule

[10] HHS OCR Enforcement Statistics: https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/index.html

[11] HHS OCR Press Release: Financial Penalties for Ransomware Attacks (April 24, 2026): https://www.hhs.gov/about/news/2026/04/24/ocr-announces-financial-penalties-against-four-entities-for-hipaa-violations-involving-ransomware-attacks.html

[12] CISA CIRCIA Information: https://www.cisa.gov/circia

[13] NYDFS Cybersecurity Regulation 23 NYCRR 500: https://www.dfs.ny.gov/industry_guidance/cybersecurity

[14] FFIEC Cybersecurity Resource Guide: https://www.ffiec.gov/cyber.htm

[15] FinCEN Advisory FIN-2021-A004: https://www.fincen.gov/resources/advisories/fincen-advisory-fin-2021-a004

[16] SEC v. SolarWinds Corp. Litigation Release: https://www.sec.gov/litigation/litreleases/2023/lr25868.htm

[17] SEC Press Release: Unisys, Avaya, Check Point, Mimecast Enforcement (October 2024): https://www.sec.gov/news/press-release/2024-123

[18] SEC Press Release: Flagstar Bancorp Enforcement (December 2024): https://www.sec.gov/news/press-release/2024-198

[19] SEC Press Release: R.R. Donnelley Enforcement (June 2024): https://www.sec.gov/news/press-release/2024-78

[20] OFAC Civil Penalties and Enforcement Information: https://home.treasury.gov/policy-issues/financial-sanctions/civil-penalties-and-enforcement-information

[21] DOJ Civil Cyber-Fraud Initiative: https://www.justice.gov/civil/civil-cyber-fraud-initiative

[22] DOJ Press Release: Colonial Pipeline Seizure: https://www.justice.gov/opa/pr/department-justice-seizes-23-million-cryptocurrency-paid-ransomware-extortionists-darkside

[23] DOJ Press Release: Hive Ransomware Disruption: https://www.justice.gov/opa/pr/justice-department-disrupts-hive-ransomware-variant

[24] DOJ Press Release: BlackSuit Ransomware Disruption: https://www.justice.gov/opa/pr/justice-department-announces-disruption-blacksuit-ransomware-group

[25] FTC v. Wyndham Worldwide Corp.: https://www.ftc.gov/enforcement/cases-proceedings/102-3060/wyndham-worldwide-corporation

[26] FTC v. CafePress: https://www.ftc.gov/news-events/news/press-releases/2022/03/ftc-takes-action-against-cafepress

[27] FTC Safeguards Rule: https://www.ftc.gov/business-guidance/safeguards-rule
