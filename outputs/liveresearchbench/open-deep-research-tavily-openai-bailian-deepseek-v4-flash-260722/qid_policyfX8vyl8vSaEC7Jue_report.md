# Comprehensive Analysis of U.S. Regulatory Requirements and Best Practices for Disclosing Ransomware Payments

## Executive Overview

The landscape of ransomware payment disclosure in the United States has undergone a fundamental transformation between 2022 and 2026, driven by the SEC's landmark cybersecurity disclosure rules, OFAC's evolving sanctions framework, and sector-specific mandates from CISA, HHS, and financial regulators. Organizations now face a complex, multi-jurisdictional disclosure environment where the decision to pay a ransom—or even the occurrence of a ransomware attack—triggers overlapping obligations across federal securities law, sanctions regulations, critical infrastructure reporting mandates, and state breach notification requirements. This report synthesizes the current regulatory requirements, enforcement actions, and actionable best practices for enterprises navigating ransomware payment disclosure.

---

## 1. SEC Cybersecurity Disclosure Rules: The Core Public Company Framework

### 1.1 The Final Rule (Release No. 33-11216)

On July 26, 2023, the SEC adopted **Release No. 33-11216** ("Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure"), which added new mandates for public companies regarding cybersecurity incidents. The rules became effective September 5, 2023, with compliance dates phased through December 2024. The rule codified **Item 1.05 of Form 8-K** and adopted **Regulation S-K Item 106** (17 CFR 229.106).

### 1.2 Form 8-K Item 1.05: The Incident Disclosure Trigger

**Item 1.05** requires a registrant to disclose information about a cybersecurity incident that the registrant determines to be **"material."** This includes ransomware attacks, data breaches, and other cybersecurity events. The key provision states:

> *"A registrant shall disclose any cybersecurity incident that the registrant determines to be material, and describe the material aspects of the incident's nature, scope, timing, and impact, or reasonably likely impact, on the registrant."*

### 1.3 The 4-Business-Day Filing Deadline

Under Item 1.05(a), once a registrant **determines** that a cybersecurity incident is material, the registrant must file Form 8-K **within four (4) business days** of that determination. Critically, the 4-business-day clock starts on the date of *materiality determination*, not the date of *incident discovery*. This distinction was deliberate and is central to the SEC's enforcement strategy.

### 1.4 The "Without Unreasonable Delay" Standard

The SEC adopted a **"without unreasonable delay"** standard tied to the materiality determination process. The rule states that the registrant must make its materiality determination **"without unreasonable delay"** after discovery of the incident. This standard was designed to prevent companies from using the materiality assessment process as a delaying tactic. The SEC's adopting release explains that:

- The materiality determination must be commenced promptly upon discovery.
- Companies cannot use the materiality assessment process as a way to avoid or postpone disclosure obligations.
- The "without unreasonable delay" requirement ensures that the determination itself cannot be unreasonably delayed.

### 1.5 What Must Be Disclosed

Under Item 1.05(a)(1), the registrant must disclose:

1. **Nature** of the incident (e.g., ransomware attack, data exfiltration, system compromise)
2. **Scope** (which systems, data, or operations were affected)
3. **Timing** (when the incident occurred, was discovered, and when the materiality determination was made)
4. **Impact** (or reasonably likely impact) on the registrant, including financial condition, results of operations, business operations, reputational effects, and legal/regulatory consequences

### 1.6 The Materiality Standard for Ransomware

The SEC did not create a new materiality standard. It incorporated the long-standing Supreme Court standard from *TSC Industries, Inc. v. Northway, Inc.* (1976) and *Basic Inc. v. Levinson* (1988): a fact is material if there is **"a substantial likelihood that a reasonable investor would consider it important"** in making an investment or voting decision.

For ransomware attacks specifically, companies should consider:

- **Ransom Amount**: The size of the ransom demand relative to the company's financial resources; whether the ransom was paid or negotiations are ongoing; the financial impact of payment
- **Operational Disruption**: Duration of system downtime, impact on revenue-generating operations, critical infrastructure impacts, recovery costs
- **Data Compromise**: Whether sensitive customer data, PII, PHI, intellectual property, or trade secrets were exfiltrated
- **Reputational Harm**: Customer trust erosion, contractual consequences, stock price impact
- **Legal and Regulatory Consequences**: Class action litigation risk, regulatory investigations, compliance with other disclosure obligations
- **Ransomware-Specific Considerations**: Whether the company paid the ransom, OFAC/sanctions implications, whether law enforcement was contacted, the existence of decryption keys, whether the attacker has threatened to release stolen data

### 1.7 Delayed Disclosure Exception

The SEC included a limited exception for delayed disclosure if the **Attorney General of the United States** determines that immediate disclosure would pose a **substantial risk to national security or public safety**. The delay is initially up to **30 days** (with a possible additional **30-day extension** — total 60 days). This exception is narrow and requires written notification to the SEC.

### 1.8 Compliance Timeline

| Date | Milestone |
|------|-----------|
| July 26, 2023 | SEC adopts final rules |
| September 5, 2023 | Rules effective |
| December 18, 2023 | Item 1.05 compliance date for all registrants (except smaller reporting companies) |
| June 15, 2024 | Item 106(b)-(c) risk management/governance compliance date (large accelerated filers) |
| December 15, 2024 | Item 106(b)-(c) compliance date (all other registrants) |

---

## 2. OFAC Guidance on Ransomware Payments: Sanctions Risk Framework

### 2.1 The September 2021 Advisory

On September 21, 2021, OFAC published a landmark **Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments**. This was the first explicit guidance addressing the intersection of ransomware payments and U.S. sanctions law.

**Key Provisions:**

- **Policy Statement**: Paying a ransom to a person or entity on the SDN List (or otherwise subject to U.S. sanctions) could constitute a sanctions violation, even if the victim did not know the recipient was sanctioned.
- **"Facilitation" Expansion**: U.S. persons could be held liable not only for direct payments but also for "facilitating" ransomware payments by third parties (e.g., incident response firms, cyber insurance companies, digital forensics firms, payment negotiators, financial institutions processing transactions).
- **Risk-Based Compliance Expectations**: Organizations were expected to implement risk-based compliance programs that account for sanctions risks related to ransomware attacks.
- **"Willful Blindness" Warning**: OFAC explicitly warned that it would hold companies accountable if they deliberately ignored red flags suggesting a ransomware payment would go to a sanctioned party.

### 2.2 The November 2021 Virtual Currency Guidance

On November 15, 2021, OFAC issued **"Sanctions Guidance for the Virtual Currency Industry"** specifically targeting cryptocurrency exchanges, virtual asset service providers (VASPs), and other blockchain-related entities. Key provisions include:

- **Virtual Currency is Not Anonymous**: Blockchain analytics can trace transactions.
- **GeoIP and Sanctions Screening**: Mandated screening of IP addresses, blockchain addresses, and wallet transactions against the SDN List.
- **Heightened KYC/AML Standards**: Including transaction monitoring for ransomware-related flows.
- **Reporting Obligations**: Immediate reporting to OFAC (within 10 days of a blocked transaction) and voluntary self-disclosure for potential violations.
- **Blocking Requirements**: If a ransomware payment involves a sanctioned entity or jurisdiction, the transaction must be blocked, and OFAC must be notified.

### 2.3 The OFAC Compliance Framework: Six Pillars

#### (1) Risk Assessment Requirements for Ransom Payments

Organizations must conduct a **risk-based assessment** before making any ransom payment, including:

- **Sanctions Exposure Analysis**: Determining whether the ransomware actor or their intermediaries is a sanctioned person, entity, or jurisdiction (e.g., North Korea's Lazarus Group, Russia-linked ransomware groups like Conti).
- **Geographic Risk**: Assessing whether the ransom demand originates from a comprehensively sanctioned jurisdiction (Iran, North Korea, Syria, Cuba, or the Crimea/Donetsk/Luhansk regions of Ukraine).
- **Blockchain Tracing**: Using blockchain analytics tools (e.g., Chainalysis, TRM Labs, Elliptic) to trace the wallet addresses and identify potential sanctions exposure.
- **Documentation**: Maintaining a written record of the risk assessment, including investigative steps, tools used, and conclusions reached.
- **Ongoing Monitoring**: Recognizing that sanctions designations change frequently.

#### (2) Sanctions Screening Obligations

Before remitting any ransom payment, organizations must screen all known identifiers against the SDN List, SSI List, CAPTA List, and NS-MBS List. Screening must cover:

- The ransomware group's name, aliases, wallet addresses, associated IP addresses, email addresses, and any other identifiers.
- Any payment facilitators, negotiators, insurance carriers, or third-party services involved in the transaction.
- If a match is found, the transaction must be blocked, and a report must be filed with OFAC within 10 business days.

#### (3) The "FAC" Indicator Framework

The "FAC" framework is a three-part due diligence structure:

| Component | Description |
|-----------|-------------|
| **Financial Due Diligence** | Tracing the flow of funds; understanding the source and destination of payments; using blockchain analytics to identify wallet addresses; evaluating whether the receiving entity is a known threat actor or sanctioned entity. |
| **Administrative Due Diligence** | Maintaining internal policies, procedures, and controls; documenting the decision-making process; keeping records of all communications with threat actors; preserving evidence of the ransomware attack. |
| **Compliance Due Diligence** | Verifying that the organization's compliance program is up-to-date; conducting sanctions screening; ensuring that personnel involved in the payment decision are trained on sanctions risks; performing post-payment reviews. |

#### (4) Reporting Requirements

OFAC mandates two distinct reporting obligations:

- **Blocked Transaction Reports**: Within **10 business days** of blocking a transaction, using Form TD F 90-22.50 or OFAC's online reporting portal.
- **Voluntary Self-Disclosures (VSDs)**: Strongly encouraged if a ransom payment was made and the organization later discovers sanctions exposure. Prompt filing (within 30 days of discovery is considered timely) is critical.

Organizations are also expected to report ransomware incidents to:
- **FBI** (local field office or IC3)
- **CISA**
- **U.S. Secret Service** (for financial crimes)
- **FinCEN** (Suspicious Activity Reports)

#### (5) Mitigating Factors

OFAC's **Economic Sanctions Enforcement Guidelines** outline specific **mitigating factors** that can reduce penalty exposure:

| Mitigating Factor | Description |
|-------------------|-------------|
| **Timely Self-Disclosure (VSD)** | The single most impactful factor; can reduce the base penalty by up to 50–80% |
| **Full Cooperation** | Providing OFAC with all relevant documents, transaction records, communications with threat actors, blockchain analytics reports, and making personnel available for interviews |
| **Remedial Measures** | Implementing new sanctions compliance controls; hiring dedicated compliance personnel; adopting blockchain analytics tools; enhancing employee training; revising incident response plans |
| **No Prior History of Violations** | A clean enforcement record over the preceding five years |
| **Minor or Technical Violation** | The violation was inadvertent, not part of a pattern, and the dollar amount was small |
| **Corrective Action Post-Violation** | Promptly ceasing the violative conduct, securing the network, and improving cybersecurity posture |

#### (6) The "Willful Blindness" Standard

OFAC's willful blindness standard holds that a person or organization cannot avoid liability by deliberately ignoring red flags or consciously avoiding knowledge of facts that would indicate a sanctions violation. Evidence of willful blindness includes:

- Failure to implement compliance controls despite known risks
- Deliberately structuring payments to avoid triggering screening
- Choosing not to use available blockchain analytics tools
- Not checking the SDN List before making payments
- Contractual provisions that intentionally limit knowledge of the recipient

### 2.4 OFAC Enforcement Actions

| Case | Year | Penalty | Key Lesson |
|------|------|---------|------------|
| **BitGo Settlement** | 2021 | $98,830 | Companies must screen transactions against the SDN List even if they are not the direct beneficiary |
| **Payward, Inc. (Kraken)** | 2022 | $362,159 | GeoIP controls and sanctions screening are mandatory for VASPs |
| **Bittrex Settlement** | 2022 | $29,280,000 | Largest virtual currency sanctions enforcement action; failure to implement screening controls over many years |
| **CoinList Settlement** | 2023 | $1.2 million | Failure to implement effective IP blocking and sanctions screening controls |

### 2.5 Subsequent Updates (2022-2026)

- **March 2022**: Updated guidance following Russia's invasion of Ukraine, emphasizing ransomware payments to Russia-linked groups carry heightened sanctions risk.
- **September 2022**: OFAC designated **Tornado Cash** to the SDN List, warning that using such mixers to launder ransomware proceeds could result in sanctions exposure.
- **September 2023**: OFAC published a **"Ransomware and Sanctions" fact sheet** with a simplified compliance checklist for small and medium-sized businesses.
- **January 2024**: OFAC updated its Enforcement Guidelines, increasing the maximum civil penalty for IEEPA violations to $394,167 per violation.
- **June 2024**: OFAC Supplemental Advisory clarified that the "facilitation" standard applies to **cyber insurance companies** that have the ability to influence or control the payment decision.

---

## 3. Other Federal Frameworks: Sector-Specific Requirements

### 3.1 CISA — CIRCIA (Cyber Incident Reporting for Critical Infrastructure Act of 2022)

**Statutory Citation**: Cyber Incident Reporting for Critical Infrastructure Act of 2022, Pub. L. No. 117-103, Div. Y (enacted March 15, 2022), codified at 6 U.S.C. §§ 681–681g.

**Who Must Report**: Entities operating in one or more of the **16 critical infrastructure sectors** as defined in Presidential Policy Directive 21 (PPD-21).

**Reporting Timelines**:

| Type | Deadline |
|------|----------|
| Covered cyber incident report | Within 72 hours from when the entity reasonably believes the incident occurred |
| Ransom payment report | Within 24 hours from the time of any ransom payment |

**Ransomware Provisions**: Under the proposed rule, a "ransomware attack" is a presumptive covered cyber incident. The 24-hour ransom payment notification is separate from and in addition to the 72-hour incident report. The ransom payment report must include the date of payment, amount and form of payment (including cryptocurrency type and wallet addresses), ransom demand details, threat actor information, and the entity's response status.

**Enforcement**: CISA can issue subpoenas for non-compliance. Civil penalties are authorized at a maximum of 0.5% of the entity's gross revenue from the preceding fiscal year, subject to a maximum of $5 million per violation.

### 3.2 HHS — HIPAA Breach Notification Rule

**Regulatory Citation**: 45 C.F.R. §§ 164.400–164.414

**Who Must Notify**: "Covered entities" (health plans, healthcare clearinghouses, health care providers who conduct standard electronic transactions) and their "business associates."

**The October 2023 HHS Bulletin on Ransomware**: This bulletin clarified that a ransomware attack that results in the encryption of ePHI is **presumed to be a breach** under the HIPAA Breach Notification Rule unless the covered entity or business associate can demonstrate that there is a low probability that the ePHI was compromised. The burden is on the entity to prove that the ePHI was not compromised.

**Notification Timelines**:

| Notification Type | Deadline | Recipient |
|-------------------|----------|-----------|
| Individual notification | Without unreasonable delay, no later than 60 calendar days | Affected individuals |
| HHS notification | Same 60-day window | HHS Secretary |
| Media notification | Same 60-day window | Prominent media outlets (if 500+ residents affected) |
| Business associate notification | Promptly | Covered entity |

**Penalties**: HIPAA civil monetary penalties range from $100 to $50,000 per violation, with a maximum of $1.5 million per calendar year for identical violations.

### 3.3 Financial Services Sector

#### OCC/FDIC/Federal Reserve — Computer-Security Incident Notification Rule

**Regulatory Citation**: 12 C.F.R. Part 53 (OCC); 12 C.F.R. Part 304 (FDIC); 12 C.F.R. Part 225 (Federal Reserve Board)

**Effective Date**: May 1, 2022

**Who Must Notify**: All banking organizations supervised by the OCC, FDIC, or Federal Reserve Board.

**Notification Trigger**: A "computer-security incident" that results in actual harm to the confidentiality, integrity, or availability of an information system. Notification is required when the banking organization notifies a customer of a security breach involving PII or reasonably believes that a notification to any customer, counterparty, or other third party is required.

**Timeline**: "As soon as possible, but no later than **36 hours** after determining that a computer-security incident has occurred."

#### FinCEN — SAR Filing Requirements

**Regulatory Citation**: FinCEN Advisory FIN-2021-A006 (October 1, 2021)

**SAR Filing Trigger**: Financial institutions must file a Suspicious Activity Report (SAR) when they receive a ransom payment from a victim, process a ransom payment on behalf of a client, or suspect that a transaction involves ransomware proceeds.

**Timeline**: 30 days from the date of initial detection of the suspicious transaction (extensions available up to 60 days).

**Specific Instructions**: Select "Ransomware" in the SAR Filing Instructions and include the keyword "**CYBER RANSOMWARE**" in the narrative text.

### 3.4 FTC Requirements

#### FTC Safeguards Rule (GLBA)

**Regulatory Citation**: 16 C.F.R. Part 314

The amended Safeguards Rule (effective 2023) requires non-bank financial institutions to maintain a written information security program, designate a qualified individual (CISO), conduct written risk assessments, and maintain a written incident response plan addressing ransomware and other security events.

#### FTC Act Section 5

The FTC has brought enforcement actions against companies for failing to protect data from ransomware under the theory that:
- **Deceptive**: Company's privacy policy or security representations were false or misleading.
- **Unfair**: Failure to maintain reasonable security causes substantial injury to consumers.

### 3.5 State Breach Notification Laws

All 50 states have enacted data breach notification laws. The most common timeline is **30 days** from discovery of the breach. Key states include:

| State | Statute | Timeline | Key Provision |
|-------|---------|----------|---------------|
| California | Cal. Civ. Code §§ 1798.29, 1798.82 | Most expedient, no later than 30 days | Encryption alone may not be sufficient to avoid notification |
| New York | N.Y. Gen. Bus. Law § 899-aa | No later than 30 days | 72 hours for DFS-regulated entities (23 NYCRR 500) |
| Texas | Tex. Bus. & Com. Code § 521.053 | No later than 60 days | Must notify Texas Attorney General if 250+ residents affected |
| Florida | Fla. Stat. § 501.171 | No later than 30 days | Must notify Florida Department of Legal Affairs |

### 3.6 DHS/TSA Requirements

| Sector | Directive | Reporting Timeline |
|--------|-----------|-------------------|
| Pipeline | TSA Security Directives (SD-1 through SD-4) | 12 hours to CISA |
| Rail | TSA Security Directives | 24 hours to CISA |
| Aviation | TSA Security Directives | 24 hours to CISA |

### 3.7 NERC CIP Requirements (Electric Sector)

**Standard**: CIP-008-6 (Cyber Security — Incident Reporting and Response Planning)

**Reporting Timeline**: Report to the Electricity Information Sharing and Analysis Center (E-ISAC) and NERC within **1 hour** of confirming a "reportable cyber security incident."

**Penalties**: NERC can impose penalties of up to $1 million per day per violation; FERC can impose additional penalties of up to $1,340,694 per day per violation.

---

## 4. Enforcement Actions Highlighting Disclosure Shortcomings

### 4.1 SEC v. SolarWinds Corp. and Timothy G. Brown (filed October 2023)

**The Allegations**: The SEC alleged that SolarWinds and its CISO defrauded investors by making materially false and misleading statements about the company's cybersecurity practices and risks. The SEC claimed that while SolarWinds publicly described its cybersecurity posture in glowing terms—including "highly evolved" security practices and "Security by Design" philosophy—internal communications showed that the company's security posture was "not mature" and that the company had "no visibility" into its own network.

**Key Lessons**:
- Vague aspirational language can be dangerous if it contradicts internal reality.
- Personal liability for CISOs is a real risk.
- Internal communications (Slack messages, emails, presentations) are a primary source of evidence for enforcement.
- Known risks must be disclosed, even if a breach has not occurred.

### 4.2 SEC Charges Against Blackbaud (March 2024)

**The Allegations**: The SEC alleged that Blackbaud misled investors about the scope of a ransomware attack that occurred in May 2020. Blackbaud characterized the incident as a "business email compromise" rather than a ransomware attack, stated that no sensitive personal information was accessed, and implied that the ransom payment had successfully prevented any data from being released.

**What the SEC Alleged Should Have Been Disclosed**: The attacker had accessed a broader range of data, including sensitive donor information, social security numbers, and bank account information. The company had no guarantee that the attacker had deleted the data.

**Penalty**: $3 million civil penalty.

**Key Lessons**:
- Precision matters in describing the type of attack.
- Data exfiltration must be disclosed clearly.
- Ransom payment disclosures should not imply certainty about data deletion.
- Relying on an incomplete investigation is risky.

### 4.3 SEC Charges Against First American Financial Corporation (2021)

**The Allegations**: The SEC alleged that First American had a known vulnerability—a design flaw in its EaglePro document management system that exposed millions of sensitive customer records—but failed to disclose this risk to investors. The company disclosed generic "cybersecurity risks" and "data breaches" language but did not disclose the specific, material vulnerability.

**Penalty**: $487,616 penalty.

**Key Lessons**: Known vulnerabilities must be disclosed. Hiding behind generic "cybersecurity risk" language is not sufficient if a specific, material risk is known.

### 4.4 SEC Charges Against RR Donnelley (2022)

**The Allegations**: The SEC alleged that RR Donnelley delayed disclosing a ransomware attack and minimized the impact when it did disclose. Internal communications showed that management knew the attack was more severe than what was publicly stated.

**Penalty**: $2.1 million penalty.

**Key Lessons**: Timeliness of disclosure is critical. Do not minimize the impact of an attack.

### 4.5 DOJ Civil Cyber-Fraud Initiative (Launched October 2021)

**Overview**: The DOJ uses the False Claims Act (FCA) to pursue government contractors and grant recipients that knowingly provide deficient cybersecurity products or services, misrepresent their cybersecurity practices, or fail to report cybersecurity incidents.

**Key Cases**:

| Case | Year | Penalty | Key Issue |
|------|------|---------|-----------|
| Comprehensive Health Services | 2022 | $930,000 | False certification of compliance with cybersecurity requirements |
| Aerojet Rocketdyne | 2023 | $9 million | False certification of NIST SP 800-171 compliance |
| Guidehouse, Inc. | 2023 | $3.86 million | Failure to provide adequate cybersecurity monitoring |
| Virginia Tech | 2023 | $12.75 million | Failure to comply with cybersecurity requirements in research contracts |

### 4.6 FTC Enforcement Actions

| Case | Year | Penalty | Key Issue |
|------|------|---------|-----------|
| FTC v. Wyndham Worldwide | 2015 | 20-year audit requirement | Inadequate security practices leading to data breaches |
| FTC v. D-Link | 2019 | $2.5M settlement | Failure to secure IoT products; deceptive marketing claims |
| FTC v. Zoom | 2020 | $85M settlement | Deceptive claims about encryption |
| FTC v. CafePress | 2022 | $500,000 settlement | Failure to secure consumer data |
| FTC v. Chegg | 2022 | Administrative order | Security failures exposing student data |

### 4.7 Shareholder Derivative Litigation

| Case | Outcome | Key Lesson |
|------|---------|------------|
| In re Equifax Shareholder Derivative Litigation | Dismissed (2018) | Board engagement matters; the Caremark standard is high |
| In re Facebook Shareholder Derivative Litigation | Settlement (2023) | Boards must demonstrate active oversight of privacy and data security risks |
| In re SolarWinds Shareholder Derivative Litigation | Pending | Derivative litigation is a growing risk following cybersecurity incidents |

---

## 5. Cross-Industry Lessons and Best Practices

### 5.1 Pre-Incident Planning

**Disclosure Playbooks**: A ransomware disclosure playbook should be a living document, updated quarterly, that operationalizes the SEC's three-pronged disclosure mandate. It should include:

- **Trigger Events**: Define objective criteria for playbook activation (e.g., ransomware encryption detected, exfiltration confirmed, ransom demand received, law enforcement notified).
- **Decision Trees**: Pre-mapped workflows for different ransomware scenarios (encryption-only, encryption + exfiltration, double extortion with threat of public release, triple extortion).
- **Holding Statements**: Pre-approved, jurisdiction-specific templates that acknowledge an "incident" without prejudicing ongoing investigations, waiving privilege, or violating OFAC sanctions screening obligations.

**Cross-Functional Incident Response Team (IRT)** : The IRT must include standing members with defined alternates:

| Role | Function |
|------|----------|
| CISO / IT Security Lead | Technical forensics, containment, eradication, threat actor communication |
| General Counsel / Deputy GC | Legal hold, privilege, regulatory notifications, OFAC sanctions screening |
| CFO / Treasurer | Ransom amount assessment, insurance activation, liquidity, accounting treatment |
| Chief Communications Officer | Internal/external messaging, investor relations, media strategy |
| Chief Compliance Officer | Regulatory mapping, cross-border obligations, sanctions compliance |
| Head of Risk / Audit | Materiality assessment, board reporting, risk register impact |

**Tabletop Exercises**: Conduct at least **semi-annual** cross-functional tabletops that simulate the full disclosure timeline from Day 0 through Day 30.

### 5.2 The Materiality Determination Process

**Quantitative Factors**:

| Factor | Assessment Methodology |
|--------|----------------------|
| Ransom Amount / Revenue | Ransom demand ÷ most recent annual revenue |
| Ransom Amount / Market Cap | Ransom demand ÷ market capitalization |
| Operational Downtime Costs | Days of downtime × daily revenue; plus recovery costs |
| Recovery Costs | Forensic investigation, legal, PR, system restoration, credit monitoring |
| Stock Price Impact | Pre-incident vs. post-disclosure trading volume/price change |
| Insurance Recovery | Net ransom exposure after insurance |

**Qualitative Factors**:

| Factor | Key Questions |
|--------|--------------|
| Data Exfiltration | Was PII, PHI, financial data, IP, or trade secrets exfiltrated? |
| Reputational Harm | Will the incident affect customer trust, partner relationships, brand equity? |
| Regulatory Risk | How many regulatory regimes are triggered? What are the potential fines? |
| Litigation Risk | Shareholder derivative suits, securities class actions, contractual claims |
| Operational Resilience | Is the company's ability to operate, fulfill orders, or meet compliance obligations impaired? |
| Threat Actor Profile | Is the threat actor state-sponsored, known for aggressive data publication? |

### 5.3 The "Without Unreasonable Delay" Standard: Operationalization

**Operationalization Framework**:

1. **Incident Classification** (within 4 hours of discovery): Classify as ransomware using objective indicators.
2. **Initial Materiality Assessment** (within 24 hours): Preliminary quantitative/qualitative analysis.
3. **Full Due Diligence** (Days 1–4): Forensic investigation, legal analysis, OFAC sanctions screening, regulatory mapping.
4. **Materiality Determination** (by Day 4): Formal Disclosure Committee vote with documented rationale.
5. **Form 8-K Filing** (within 4 business days of materiality determination): If material, file Item 1.05.

### 5.4 Coordination Between Legal, Communications, IT Security, and Executive Teams

**Decision Rights Matrix**:

| Decision | Legal | IT Security | Communications | CFO | CEO | Board |
|----------|-------|-------------|----------------|-----|-----|-------|
| Incident classification | Advise | **Own** | Input | — | — | — |
| Materiality determination | **Own** | Input | Input | Input | Input | — |
| Disclosure timing | **Own** | Input | Input | Input | Input | Inform |
| Disclosure content | **Own** | Input | **Own** | Input | Approve | Informed |
| Ransom payment decision | **Own** | Advise | — | **Own** | Approve | **Approve** |
| Law enforcement notification | **Own** | **Own** | — | — | Inform | Inform |

**The Golden Rule of Ransomware Communications**: Never say "we have no evidence of data exfiltration" until you are certain. The single most common correction/amendment in ransomware 8-K filings involves the discovery of exfiltration after initial statements that none occurred.

### 5.5 Board Oversight

Under SEC Release No. 33-11216, registrants must disclose:
- Board's oversight of cybersecurity risks (Item 106(b)(1))
- Whether cybersecurity expertise exists on the board (Item 406(b)(4))
- Management's role in assessing and managing cybersecurity risk

**Best Practices**:
- At minimum, delegate cybersecurity oversight to the Audit Committee with a dedicated cybersecurity charter.
- At least one board member with cybersecurity experience.
- Standing quarterly cybersecurity briefing from CISO.
- Board-level tabletop exercise on a material ransomware scenario at least annually.
- Confirm D&O insurance covers securities class actions arising from cybersecurity incidents.

### 5.6 International Considerations

**GDPR Breach Notification (72 Hours)** : Under GDPR Article 33, data controllers must notify the relevant supervisory authority of a personal data breach within **72 hours** of becoming aware of the breach. The 72-hour GDPR clock starts from awareness of the breach, not materiality determination, meaning SEC disclosure may be informed by or follow GDPR notification.

**Other Major International Regimes**:

| Jurisdiction | Requirement | Timeline |
|-------------|-------------|----------|
| UK | UK DPA 2018 / ICO | 72 hours |
| EU NIS2 | Network and Information Security Directive 2 | 24 hours (early warning), 72 hours (notification) |
| EU DORA | Digital Operational Resilience Act | 4 hours (initial), 24 hours (full) |
| Australia | SOCI Act | 12 hours (cyber incident), 24 hours (ransomware payment) |
| Singapore | CCA / MAS | 2 hours (critical systems) |
| India | CERT-In Directions | 6 hours of detection |
| China | PIPL / CSL / DSL | "Immediately" (CSL), 48 hours (MLPS) |

**Recommended Multinational Notification Approach**:

1. **Hour 0–6**: Identify all affected jurisdictions; map regulatory obligations.
2. **Hour 6–24**: Notify in jurisdictions with shortest timelines (India CERT-In, Singapore MAS, UK early warning, NIS2 early warning).
3. **Hour 24–72**: Notify in GDPR jurisdictions, CISA CIRCIA, financial regulators.
4. **Day 4**: File SEC Form 8-K (if material).
5. **Day 4–60**: Complete remaining notifications (HIPAA, state AGs, contractual counterparties, data subjects).

### 5.7 Accounting Treatment

Under **U.S. GAAP**:

| Scenario | Treatment | Standard |
|----------|-----------|----------|
| Ransom payment to regain access to data/systems | Loss from cyber incident (operating expense) | ASC 450 (Contingencies) |
| Ransom payment to prevent data publication | Loss from cyber incident (operating expense) | ASC 450 |
| Insurance recovery | Separate presentation (not netted) | ASC 450-20 |

### 5.8 The "FAC" Framework for Ransom Payment Decisions

**Financial Due Diligence**:
- What is the ransom amount?
- What is the net cost of not paying?
- What is the net cost of paying?
- Is insurance coverage available?

**Administrative Due Diligence**:
- Who is the threat actor? Check OFAC SDN List.
- What is the threat actor's reputation for decrypting data?
- What is the law enforcement position?
- What is the board's position?

**Compliance Due Diligence**:
- OFAC sanctions screening of the threat actor, ransom demand, and Bitcoin wallet.
- RPC (Russia/Ukraine-related sanctions) screening.
- Anti-Money Laundering (AML) obligations (FinCEN SAR filing).
- Data privacy and contractual notification obligations.

**Decision Matrix**:

| FAC Score | Assessment | Recommended Action |
|-----------|------------|-------------------|
| Green (Low risk) | No sanctions nexus; reliable threat actor; insurance coverage; law enforcement neutral | Pay ransom with board approval; file SAR; notify regulators |
| Yellow (Moderate risk) | Some sanctions nexus; uncertain decryption reliability; partial insurance coverage | Enhanced due diligence; consult OFAC for specific license |
| Red (High risk) | Direct sanctions nexus; known non-payment group; no insurance coverage; law enforcement recommends against payment | DO NOT PAY; pursue alternative recovery; coordinate with law enforcement |

---

## 6. Summary Comparison Table: Ransomware Reporting Timelines by Framework

| Framework | Incident Notification Deadline | Ransom Payment Deadline | Affected Entities |
|-----------|-------------------------------|------------------------|-------------------|
| **SEC Form 8-K Item 1.05** | 4 business days from materiality determination | N/A (included in incident disclosure) | Public companies |
| **CISA CIRCIA** | 72 hours (proposed) | 24 hours (proposed) | 16 critical infrastructure sectors |
| **HIPAA Breach Notification** | 60 calendar days | N/A (not separately required) | Covered entities and business associates |
| **OCC/FDIC/Fed** | 36 hours | N/A (separate requirement) | Banking organizations |
| **FinCEN SAR** | 30 days (standard SAR) | Included in SAR | Financial institutions under BSA |
| **TSA Pipeline** | 12 hours | N/A (included in incident report) | TSA-covered pipeline operators |
| **TSA Rail** | 24 hours | N/A | TSA-covered rail operators |
| **TSA Aviation** | 24 hours | N/A | TSA-covered airport/aircraft operators |
| **NERC CIP** | 1 hour | N/A | BES registered entities |
| **State Breach Notification** | 30 days (most common) | N/A | Any entity with PII of state residents |

---

## 7. Actionable Lessons for Enterprises on Disclosure Strategy

### 7.1 Establish a Cross-Functional Incident Response Team

The IRT must be pre-designated with defined roles, alternates, and 24/7 availability. The team should convene within 2 hours of any confirmed ransomware incident and include representatives from legal, IT security, communications, finance, compliance, and executive leadership.

### 7.2 Create a Disclosure Committee for Materiality Determinations

This standing committee should have a charter that includes:
- Pre-defined meeting protocols (24/7 availability, 2-hour convening requirement).
- Voting thresholds (e.g., unanimous consent for materiality finding).
- Documentation requirements (minutes of all materiality determinations, preserved under privilege).
- Escalation (automatic escalation to Audit Committee chair if ransom exceeds a defined threshold).

### 7.3 Develop Pre-Approved Templates

Develop three tiers of templates:

| Tier | Audience | Content Scope |
|------|----------|--------------|
| Tier 1 | Internal (employees, board) | Acknowledge incident; no details on ransom, exfiltration, or threat actor |
| Tier 2 | Regulators (SEC, CISA, State AGs) | Facts known, remediation steps, investor notification plans |
| Tier 3 | External (customers, partners, media, shareholders) | Narrowest scope; privilege-preserving; compliance-focused |

### 7.4 Conduct Pre-Payment OFAC Screening

Before any ransom payment, conduct mandatory sanctions screening of all wallet addresses, threat actor identifiers, and associated jurisdictions. Contract with a blockchain analytics firm (Chainalysis, TRM Labs, Elliptic) to trace the ransom demand. Embed OFAC compliance into the incident response plan.

### 7.5 Document the Materiality Determination Process

Meticulously document the materiality determination process and timing. The SEC's enforcement actions demonstrate that the gap between internal knowledge and public disclosure is a primary source of liability. Maintain a detailed record of all due diligence steps, screening results, and the decision-making process.

### 7.6 Coordinate with Law Enforcement

Report ransomware incidents to CISA and the FBI, independent of sanctions reporting. Document all law enforcement coordination. If law enforcement requests delayed disclosure, obtain written documentation of the request and coordinate with SEC counsel if the incident is material.

### 7.7 File Voluntary Self-Disclosures Promptly

If a ransom payment is made and sanctions exposure is later identified, file a Voluntary Self-Disclosure with OFAC within 30 days. Timely self-disclosure is the single most impactful mitigating factor in OFAC enforcement.

### 7.8 Review Cyber Insurance Policies

Ensure that cyber insurance policies do not mandate or incentivize payments without sanctions due diligence. Confirm pre-approval requirements, reimbursement limits, and coverage for ransom payments, legal costs, and regulatory fines.

### 7.9 Train Incident Response Teams

Train incident response teams, legal counsel, and finance personnel on the OFAC ransomware framework, SEC disclosure rules, and sector-specific reporting obligations. Conduct annual training updates to reflect regulatory changes.

### 7.10 Maintain Consistent Internal and External Communications

The SEC and other regulators will compare internal communications (emails, Slack messages, presentations) with public disclosures. Companies should ensure that internal communications are consistent with external disclosures and that employees are trained on the importance of accurate internal documentation.

---

### Sources

[1] SEC Release No. 33-11216, "Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure" (July 26, 2023): https://www.sec.gov/rules/2023/07/cybersecurity-risk-management-strategy-governance-and-incident-disclosure

[2] 17 CFR 229.106 — Regulation S-K Item 106 (Cybersecurity): https://www.ecfr.gov/current/title-17/chapter-II/part-229/subpart-229.100/section-229.106

[3] SEC Form 8-K Item 1.05 — Cybersecurity Incident Disclosure: https://www.sec.gov/files/form8-k.pdf

[4] OFAC, "Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments" (September 21, 2021): https://ofac.treasury.gov/media/9131/download?inline

[5] OFAC, "Sanctions Guidance for the Virtual Currency Industry" (November 15, 2021): https://ofac.treasury.gov/media/9136/download?inline

[6] OFAC, "Economic Sanctions Enforcement Guidelines" (31 CFR Part 501, Appendix A): https://www.ecfr.gov/current/title-31/subtitle-B/chapter-V/part-501/appendix-Appendix%20A%20to%20Part%20501

[7] OFAC Enforcement Actions: https://ofac.treasury.gov/civil-penalties-and-enforcement-information

[8] Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA), Pub. L. No. 117-103, Div. Y: https://www.congress.gov/bill/117th-congress/house-bill/2471

[9] HHS Bulletin, "Ransomware and HIPAA" (October 2023): https://www.hhs.gov/hipaa/for-professionals/security/guidance/ransomware/index.html

[10] HIPAA Breach Notification Rule, 45 C.F.R. §§ 164.400–164.414: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D

[11] OCC Computer-Security Incident Notification Rule, 12 C.F.R. Part 53: https://www.ecfr.gov/current/title-12/chapter-I/part-53

[12] FinCEN Advisory FIN-2021-A006, "Advisory on Ransomware and the Use of the Financial System to Facilitate Ransom Payments" (October 1, 2021): https://www.fincen.gov/resources/advisories/fincen-advisory-fin-2021-a006

[13] FTC Safeguards Rule, 16 C.F.R. Part 314: https://www.ecfr.gov/current/title-16/chapter-I/subchapter-C/part-314

[14] SEC v. SolarWinds Corp. and Timothy G. Brown, SEC Release No. 2023-198 (October 30, 2023): https://www.sec.gov/news/press-release/2023-198

[15] SEC Charges Blackbaud, Inc., SEC Release No. 2024-28 (March 2024): https://www.sec.gov/news/press-release/2024-28

[16] SEC Charges First American Financial Corporation, SEC Release No. 2021-93 (May 2021): https://www.sec.gov/news/press-release/2021-93

[17] SEC Charges RR Donnelley & Sons Company, SEC Release No. 2022-167 (September 2022): https://www.sec.gov/news/press-release/2022-167

[18] DOJ Civil Cyber-Fraud Initiative (October 6, 2021): https://www.justice.gov/opa/pr/deputy-attorney-general-announces-civil-cyber-fraud-initiative

[19] DOJ, Comprehensive Health Services Settlement (2022): https://www.justice.gov/opa/pr/justice-department-announces-civil-cyber-fraud-initiative-settlement

[20] DOJ, Aerojet Rocketdyne Settlement (February 2023): https://www.justice.gov/opa/pr/aerojet-rocketdyne-agrees-pay-9-million-resolve-allegations-false-claims-act

[21] DOJ, Virginia Tech Settlement (2023): https://www.justice.gov/opa/pr/virginia-tech-pay-1275-million-resolve-false-claims-act-allegations-relating-cybersecurity

[22] FTC v. Wyndham Worldwide Corporation, Third Circuit Decision (2015): https://www.ftc.gov/legal-library/browse/cases-proceedings/112-3174-wyndham-worldwide-corporation

[23] FTC v. D-Link Corporation (2019): https://www.ftc.gov/news-events/news/press-releases/2019/07/ftc-sends-case-against-d-link-court

[24] FTC v. Zoom Video Communications (2020): https://www.ftc.gov/news-events/news/press-releases/2020/11/ftc-reaches-settlement-zoom-over-allegations-misleading-consumers-about-security

[25] FTC v. CafePress (2022): https://www.ftc.gov/news-events/news/press-releases/2022/03/ftc-takes-action-against-cafepress-data-breach

[26] TSA Security Directives — Pipeline: https://www.tsa.gov/news/press/releases/2022/07/25/tsa-announces-extension-pipeline-cybersecurity-requirements

[27] NERC Standard CIP-008-6, "Cyber Security — Incident Reporting and Response Planning": https://www.nerc.com/pa/Stand/Reliability%20Standards/CIP-008-6.pdf

[28] California Breach Notification Law, Cal. Civ. Code §§ 1798.29, 1798.82: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.29

[29] New York Breach Notification Law, N.Y. Gen. Bus. Law § 899-aa: https://www.nysenate.gov/legislation/laws/GBS/899-AA

[30] SEC Small Entity Compliance Guide, "Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure" (December 2023): https://www.sec.gov/corpfin/sec-cybersecurity-small-entity-compliance-guide
