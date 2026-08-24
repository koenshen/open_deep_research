# Ransomware Payment Disclosure Requirements in the United States: A Comprehensive Regulatory and Strategic Analysis (August 2026)

## 1. Introduction

Ransomware payment disclosures now sit at the intersection of multiple overlapping U.S. federal and state regulatory regimes. A single incident can trigger: an SEC Form 8-K filing within four business days of a materiality determination; a CISA report within 72 hours (once CIRCIA's final rule takes effect); a ransom payment report within 24 hours under NYDFS and CIRCIA; a 36-hour notification to federal banking regulators; and state breach notification obligations with deadlines as short as 30 days. Compounding this complexity, the Office of Foreign Assets Control (OFAC) imposes strict-liability sanctions risk on any payment made to a blocked or sanctioned actor, and the Department of Justice (DOJ) has built a voluntary self-disclosure architecture that can reward — or penalize — how enterprises sequence their notifications.

This report provides a comprehensive analysis of the ransomware payment disclosure landscape as of August 2026, covering: (1) the key federal and sector-specific disclosure requirements; (2) enforcement actions that highlight where companies went wrong; and (3) practical lessons for enterprises building disclosure procedures, including the pay-vs-not-pay decision, internal governance, and pitfalls to avoid.

---

## 2. Key Disclosure Requirements

### 2.1 SEC Cybersecurity Disclosure Rules

#### 2.1.1 The Final Rule: Form 8-K Item 1.05 and Regulation S-K Item 106

The SEC adopted its final cybersecurity disclosure rules on July 26, 2023, published at 88 FR 51896 (Release Nos. 33-11216; 34-97989), effective September 5, 2023. The rule has two principal components [1][2][4]:

- **Form 8-K Item 1.05 (current incident reporting):** Registrants must disclose any material cybersecurity incident within **four business days of determining materiality**, describing the material aspects of the incident's nature, scope, timing, and impact (or reasonably likely impact), including on financial condition and results of operations. If new material information emerges, an amended 8-K must be filed within four business days of learning that information. The rule became effective December 18, 2023 for most registrants and June 15, 2024 for smaller reporting companies [1][3][4].
- **Regulation S-K Item 106 (periodic disclosure):** Registrants must describe in their annual reports their processes for assessing, identifying, and managing material cybersecurity risks (Item 106(b)), and the board's oversight and management's role regarding cybersecurity risks (Item 106(c)). The proposed requirement to disclose board members' cybersecurity expertise was dropped from the final rule [1][4][5].

The rule defines a cybersecurity incident as "an unauthorized occurrence, or a series of related unauthorized occurrences, on or conducted through a registrant's information systems that jeopardizes the confidentiality, integrity, or availability of a registrant's information systems or any information residing therein." The inclusion of "a series of related unauthorized occurrences" is significant: it means continuous small attacks by the same threat actor can be aggregated for materiality purposes [1][89].

#### 2.1.2 The Materiality Standard and the Four-Business-Day Clock

The SEC retained the Supreme Court's traditional materiality standard: information is material if "there is a substantial likelihood that a reasonable shareholder would consider it important" or if disclosure "would have been viewed by the reasonable investor as having significantly altered the 'total mix' of information made available" [1][4][5].

Three operational points are critical:

1. **The four-business-day clock starts on materiality determination, not on discovery of the incident.** Registrants must make materiality determinations "as soon as reasonably practicable after discovery" — but the SEC's Division of Corporation Finance Director, Erik Gerding, has confirmed that the determination date may differ from the incident date, the date the company discussed the incident with peers, or the date it reported to law enforcement [3][4][12].
2. **Materiality is not a numbers test.** The SEC did not adopt a quantifiable threshold (e.g., a dollar amount of ransom paid or revenue affected). The June 24, 2024 Compliance & Disclosure Interpretations (C&DIs) confirm that the size of a ransomware payment, by itself, is not determinative of materiality, and that insurance reimbursement does not automatically render an incident immaterial — registrants must weigh qualitative factors such as reputational harm, customer relationships, litigation risk, and future insurance availability or cost [3][6][7].
3. **Paying a ransom does not extinguish the disclosure obligation.** C&DI 104B.05 and 104B.06 make clear that a registrant must assess materiality and, if material, disclose the incident even if a ransom is paid and the incident ends or data is returned before the 8-K filing deadline [3][6][7].

#### 2.1.3 SEC Staff Guidance: Item 8.01 vs. Item 1.05

Gerding's May 21, 2024 statement clarified that Item 1.05 is reserved exclusively for incidents determined to be material. Companies that have not yet made a materiality determination — or that have determined an incident is immaterial — may voluntarily disclose under **Item 8.01** (Other Events). If an incident disclosed under Item 8.01 is later determined to be material, the company must file an Item 1.05 8-K within four business days of that later determination. The staff's view is that this distinction gives investors better signal clarity [6][8][9][10][82].

A separate June 24, 2024 statement addressed Regulation FD: the cybersecurity rules do not preclude companies from sharing incident information with commercial counterparties (vendors, customers) for remediation purposes, but Regulation FD still applies to any additional information shared beyond the 8-K [6][9][82].

#### 2.1.4 National Security and Public Safety Delay

Disclosure may be delayed only if the U.S. Attorney General determines that disclosure poses a substantial risk to national security or public safety. The FBI is the intake point for delay requests and "will not process requests unless they are received immediately upon a company's determination that a cybersecurity incident is material." Delays are capped at 30 days initially, extendable in 30-day increments, with up to 60 additional days in extraordinary circumstances — and any further delay requires an SEC exemptive order. Critically, neither the request nor the government's consideration time tolls the four-business-day filing clock; if the DOJ does not respond in time, the registrant must still file [3][79][80][81]. In practice, the national security delay has been invoked only rarely — both known instances in the first two years of the rule were by AT&T in 2024 [11].

#### 2.1.5 SolarWinds Litigation and Its Aftermath

The SEC's lawsuit against SolarWinds Corp. and its CISO Timothy Brown — the first enforcement action alleging fraud based on pre-breach cybersecurity misrepresentations, and the first naming a CISO as an individual defendant — has shaped the enforcement environment [17][18]. In July 2024, the U.S. District Court for the Southern District of New York dismissed most of the SEC's claims, including the novel theory that cybersecurity controls fall within Section 13(b)(2)(B) internal accounting controls, and found the company's Form 8-K "captured the big picture" of the SUNBURST attack [16][17]. On November 20, 2025, the SEC dismissed the remaining charges with prejudice, without admission of wrongdoing [17][18][19].

The dismissal signals a recalibration of SEC cyber enforcement — particularly toward treating cyberattack victims as victims rather than defendants. However, the core disclosure rules remain fully in effect, and the five-year statute of limitations means a future administration could revive aggressive theories. Private securities class actions and derivative suits following cyber incidents also remain active [17][18][19].

### 2.2 OFAC Sanctions Framework for Ransomware Payments

#### 2.2.1 The October 2020 and September 2021 Advisories

OFAC issued its first ransomware advisory on October 1, 2020, and a superseding **Updated Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments** on September 21, 2021 [23][24][25]. The updated advisory applies not only to ransomware victims but also to financial institutions, cyber insurance firms, and digital forensics and incident response (DFIR) companies that facilitate payments on victims' behalf [23][26].

Key points:

- OFAC "strongly discourages all private companies and citizens from paying ransom or extortion demands." The 2021 advisory shifted the language from "does not encourage" to "strongly discourages" [23][26].
- **Payments to sanctioned parties are prohibited under a strict liability standard.** If the ransom recipient is a Specially Designated National (SDN), an entity owned 50% or more by SDNs (the "50 Percent Rule"), or located in a comprehensively embargoed jurisdiction, the payer can face civil penalties even without knowledge of the sanctions nexus [23][28][29].
- **OFAC license applications for ransomware payments are reviewed with a presumption of denial** [23][26].
- **Two "significant mitigating factors"** reduce enforcement exposure: (1) strong cybersecurity practices (e.g., CISA's Ransomware Guide best practices), and (2) prompt reporting of the attack to law enforcement, CISA, Treasury's Office of Cybersecurity and Critical Infrastructure Protection (OCCIP), or other agencies, with ongoing cooperation — including providing technical details, ransom demands, and payment instructions. Timely self-disclosure can qualify as a voluntary self-disclosure for mitigation purposes [23][26].

#### 2.2.2 Designations and Enforcement Context

On September 21, 2021, OFAC designated **SUEX OTC, S.R.O.** — a Russian cryptocurrency exchange — marking the first-ever sanctions designation of a crypto exchange. OFAC alleged that over 40% of SUEX's known transaction history was associated with illicit actors, including at least eight ransomware variants. The designation included specific digital currency addresses (Bitcoin, Ethereum, Tether) on the SDN List [25][27][29]. On November 8, 2021, OFAC designated **Chatex** and its infrastructure providers, as well as REvil/Sodinokibi actors Yevgeniy Polyanin and Yaroslav Vasinskyi [29].

OFAC has also brought civil penalty settlements against virtual currency platforms for sanctions violations — including Binance ($706 million), Bittrex (over $263 million), Poloniex ($15.3 million), CoinList Markets ($1.25 million), and Uphold HQ ($180,575) — with a recurring theme of failures to use IP address, KYC, and geolocation data for sanctions screening [29]. The Cyber-Related Sanctions Regulations (31 CFR Part 578), implementing Executive Orders 13694, 13757, 14144, and 14306, provide the regulatory foundation [29].

#### 2.2.3 OFAC's Virtual Currency Compliance Expectations

OFAC's "Sanctions Compliance Guidance for the Virtual Currency Industry" requires a risk-based compliance program with five essential components: (1) management commitment; (2) risk assessment; (3) internal controls — including sanctions screening, geolocation tools/IP blocking, KYC procedures, transaction monitoring, and blockchain analytics; (4) testing and auditing; and (5) training. Blocked virtual currency must be reported to OFAC within 10 business days. Voluntary self-disclosure can reduce proposed civil penalties by 50% [28].

### 2.3 CISA and CIRCIA

#### 2.3.1 CIRCIA Statutory Requirements

The Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA), signed March 15, 2022, requires covered critical infrastructure entities to report: (1) **covered cyber incidents to CISA within 72 hours** after reasonably believing the incident occurred, and (2) **ransom payments within 24 hours of payment**. Supplemental reports are required when substantial new information emerges [33][36][39].

CIRCIA reports are exempt from FOIA, not admissible as evidence in civil litigation, and reporting entities receive liability protection for submitting reports. However, CISA may issue requests for information and subpoenas for non-compliance, refer matters to DOJ (false statements carry up to five years' imprisonment, up to eight if involving terrorism), and refer non-compliant federal contractors to DHS's Suspension and Debarment Official [36][38][39].

#### 2.3.2 Rulemaking Status (as of August 2026)

CIRCIA's final rule has been significantly delayed. CISA published its Notice of Proposed Rulemaking in April 2024, missed the statutory October 2025 deadline, set an internal May 2026 target, and — following a DHS appropriations lapse that disrupted stakeholder engagement — is now **targeting September 2026** for the final rule, per the Unified Agenda [33][34][35][37].

The proposed rule would apply to entities in the 16 critical infrastructure sectors using a two-track coverage test (size-based: exceeding SBA small business size standards; sector-based: 16 sectors covered regardless of size). CISA estimates **316,244 affected entities**. The 72-hour clock starts when an entity "reasonably believes" a covered incident occurred — not when investigation confirms it. The rule proposes a two-year data preservation requirement and four report types: Covered Cyber Incident Reports (72 hours), Ransom Payment Reports (24 hours), Joint Reports, and Supplemental Reports [33][35][36][37].

Industry groups — including the American Hospital Association and the Bank Policy Institute — have raised concerns about vague definitions, overlapping federal reporting duties, and potentially severe penalties [36]. CIRCIA does **not** replace existing obligations (SEC, HIPAA, TSA, state laws); it adds to them [37].

#### 2.3.3 Related CISA Programs

- **Ransomware Vulnerability Warning Pilot (RVWP):** Established under CIRCIA, launched January 30, 2023. CISA proactively identifies vulnerable systems (e.g., via Cyber Hygiene scanning and administrative subpoena authority) and notifies owners. Receiving a notification does not indicate compromise, but indicates immediate risk [40].
- **StopRansomware.gov:** The official U.S. government ransomware resource hub, providing the Ransomware Response Checklist, prevention guidance, and reporting channels. CISA's guidance states: "Every ransomware incident should be reported to the U.S. government" — a victim only needs to report once to the FBI, CISA, or Secret Service [41][42][43].
- **Joint CISA/FBI advisory AA21-243A** strongly discourages payment: "Payment does not guarantee files will be recovered, nor does it ensure protection from future breaches" [44].

### 2.4 Sector-Specific Disclosure Requirements

#### 2.4.1 Financial Services

**NYDFS 23 NYCRR Part 500 (Second Amendment, effective November 1, 2023):** Covered entities must notify NYDFS within **72 hours of determining a cybersecurity incident occurred** (Section 500.17(a)). Critically, **any extortion payment must be reported within 24 hours**, with a written description within 30 days (Section 500.17(c)). Ransomware deployments affecting a material part of information systems trigger reporting. The June 2023 proposal would have **prohibited ransom payments without superintendent approval** — this provision was dropped from the final rule, but the 24-hour payment notification requirement was retained [45][46][48][49]. Annual certifications are due April 15, signed by the highest-ranking executive and CISO [45][85]. Enforcement penalties under Financial Services Law §408 include civil monetary fines, license revocation, and cease-and-desist orders [46][85].

**Federal banking agencies (OCC/Fed/FDIC) — Computer-Security Incident Notification Rule:** Banking organizations must notify their primary federal regulator of any "notification incident" — a computer-security incident that materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, banking operations, customer service delivery, business lines, or U.S. financial stability — **as soon as possible and no later than 36 hours** after determining the incident occurred. Bank service providers must notify affected banking organization customers when covered services are disrupted for **four or more hours**. The rule became effective April 1, 2022, with compliance required by May 1, 2022 [49][50][51][53].

**FTC GLBA Safeguards Rule (amended October 2023, effective May 13, 2024):** Non-banking financial institutions under FTC jurisdiction must notify the FTC within **30 days of discovery** of the unauthorized acquisition of unencrypted customer information involving at least 500 consumers. The notification is filed electronically and entered into a publicly available database. This applies to ANY nonpublic personal information — not just "sensitive" data — and there are no exceptions for events that don't cause consumer harm [54][55].

**FinCEN SAR requirements:** Financial institutions must file Suspicious Activity Reports (SARs) for ransomware-related transactions using key term "RANSOMWARE" / "CYBER-FIN-2021-A004." FinCEN's October 2020 advisory warned that DFIR firms and cyber insurers facilitating ransom payments may be deemed **money transmitters**, requiring MSB registration and BSA compliance. FinCEN's Financial Trend Analysis reported $590 million in suspected ransomware payments in SARs filed January–June 2021 (exceeding all of 2020's $416 million), and over **$2.1 billion in ransomware payments across 2022–2024**, with 2023 reaching an all-time high of $1.1 billion across 1,512 incidents [30][31][32].

#### 2.4.2 Healthcare

**HIPAA Breach Notification Rule (45 CFR §§ 164.400-414):** Covered entities and business associates must notify affected individuals, HHS OCR, and (for breaches affecting 500+ residents of a state) media outlets **within 60 days of breach discovery** — "without unreasonable delay" and no later than 60 days. Breaches affecting fewer than 500 individuals may be logged and reported annually, due within 60 days after year-end. Ransomware that encrypts ePHI is **presumed a breach** unless a documented four-factor risk assessment demonstrates a low probability of compromise. The 60-day clock starts at discovery, not when the investigation concludes — waiting until day 60 can itself constitute a violation [56][57][58].

**HIPAA Security Rule NPRM (December 27, 2024):** HHS OCR proposed the first major Security Rule update since 2013, including mandatory annual risk assessments, mandatory encryption of ePHI at rest and in transit, mandatory MFA, vulnerability scanning every six months, annual penetration testing, incident response plan testing, and a 72-hour data restoration requirement. The comment period closed March 7, 2025; **as of August 2026 the rule is not final**, with OMB's Unified Agenda targeting July 2027 for final action. OCR continues to enforce the current Security Rule, under which risk analysis remains the most-frequently-cited deficiency [59][60].

#### 2.4.3 Critical Infrastructure

**TSA Pipeline Security Directives:** Security Directive Pipeline-2021-01 (effective May 28, 2021) requires owners/operators of critical pipelines and LNG facilities to **report cybersecurity incidents to CISA within 12 hours of identification**, designate a 24/7 Cybersecurity Coordinator, and conduct gap assessments against NIST and API standards. The directives have been renewed and updated through SD Pipeline-2021-02F (effective May 3, 2025) and SD Pipeline-2021-01G (effective January 16, 2026), with civil penalties up to approximately $15,000 per day per violation [61][62][63].

**CFATS (Chemical Facility Anti-Terrorism Standards):** The CFATS program's statutory authorization **expired on July 27, 2023**, and as of August 2026 it remains lapsed. CISA cannot enforce compliance, conduct inspections, or require reporting. The program's ~3,200 previously covered facilities are encouraged to maintain security voluntarily through CISA's ChemLock program [64][65].

**EPA Water Sector:** EPA serves as the Sector Risk Management Agency for water. A March 2024 enforcement alert found 70% of inspected water systems in violation of SDWA Section 1433 cybersecurity standards. A coordinated series of cyberattacks against U.S. water utilities began in late July 2026, affecting at least 30 systems across 12 states, prompting new legislative proposals including the Water Cyber Shield Act of 2026 [66][67][68][69].

#### 2.4.4 State Breach Notification Laws

All 50 states, plus D.C. and territories, have breach notification laws. Roughly 20 states impose numeric deadlines: **30 days** (California, Colorado, Florida, Maine, New Jersey, New York, Washington), **45 days** (Alabama, Arizona, Indiana, Maryland, Ohio, Oregon, Rhode Island, Tennessee, Vermont, Wisconsin), and **60 days** (Connecticut, Delaware, Louisiana, South Dakota, Texas); the remainder require notice "without unreasonable delay" [70].

Notable recent developments: **California's SB 446** (effective January 1, 2026) imposes a strict 30-calendar-day notification deadline for affected residents and requires AG notification within 15 days of consumer notification for breaches affecting 500+ residents [72]. **New York's SHIELD Act** covers "access" to computerized data (broader than "acquisition"), includes biometric data and email credentials in the definition of private information, and imposes penalties up to $250,000 for notification failures [71]. Multi-state breaches are governed by the strictest applicable clock, and 24 states provide a private right of action [70].

---

## 3. Enforcement Examples

### 3.1 SEC Enforcement Actions

#### 3.1.1 SolarWinds (dismissed November 2025)

The SEC's case against SolarWinds and CISO Timothy Brown alleged material misrepresentations in a public Security Statement, boilerplate risk disclosures that failed to convey known vulnerabilities, an inadequate Form 8-K, and deficient disclosure/internal accounting controls. The district court dismissed most claims in July 2024, holding that: cybersecurity controls are outside the scope of Section 13(b)(2)(B); two misclassified incidents do not establish deficient disclosure controls; risk disclosures are actionable only where "the warned risk has already occurred"; and the Form 8-K "captured the big picture." The SEC dismissed the remaining claim with prejudice on November 20, 2025 [16][17][18][19]. **Lesson:** the SEC's aggressive theories faced significant judicial pushback, but the case's shadow persists — companies should still expect scrutiny of pre-breach security statements and post-breach 8-K completeness.

#### 3.1.2 Blackbaud ($3 million, March 2023)

Blackbaud suffered a ransomware attack on May 14, 2020, paid the ransom, and disclosed on July 16, 2020 that the attacker "did not access bank account information, or social security numbers." By late July 2020, Blackbaud's cyber team learned the attacker **had** accessed bank account information and SSNs in unencrypted form — but this was not escalated to senior management. An August 4, 2020 Form 10-Q described the exfiltration risk as "hypothetical" when it had already occurred. The SEC charged violations of non-scienter anti-fraud provisions and failure to maintain adequate disclosure controls [21]. **Lesson:** disclosure controls must escalate evolving breach-scope information promptly, and companies must avoid characterizing realized events as hypothetical risks.

#### 3.1.3 The October 2024 SolarWinds-Compromise Sweep

The SEC settled charges against **Unisys ($4 million)**, **Avaya ($1 million)**, **Check Point Software Technologies ($995,000)**, and **Mimecast ($990,000)** for misleading disclosures related to intrusions via the SolarWinds Orion compromise. The orders found that these companies learned threat actors had accessed their systems but negligently minimized the incidents — some continuing to frame intrusions as hypothetical risks in SEC filings after they had occurred. Unisys also faced a disclosure controls violation. Acting Enforcement Director Sanjay Wadhwa: "while public companies may become targets of cyberattacks, it is incumbent upon them to not further victimize their shareholders... by providing misleading disclosures" [22]. **Lesson:** post-incident, risk-factor language must be updated to reflect actual intrusions — boilerplate can become an enforcement hook.

#### 3.1.4 Other Notable SEC Actions

- **Flagstar Bancorp ($3.5 million):** Falsely stated in SEC filings that no unauthorized access to customer data occurred after a 2021 cyberattack, when file-transfer data had in fact been accessed [10].
- **ICE (May 2024, Regulation SCI):** ICE failed to report a "zero-day" VPN vulnerability exploitation "immediately," waiting four days to conclude no unauthorized access occurred. SEC Enforcement Director Gurbir Grewal: "When it comes to cybersecurity, especially events at critical market intermediaries, every second counts and four days can be an eternity" [22].

### 3.2 OFAC and Financial Crimes Enforcement

While OFAC has not publicly announced a civil penalty specifically for a ransomware payment to an SDN (as of August 2026), the agency has built a clear enforcement architecture around ransomware-enabled sanctions violations:

- **SUEX OTC designation (September 21, 2021):** First-ever designation of a cryptocurrency exchange for facilitating ransomware payments, including specific digital currency addresses [25][27].
- **Chatex designation (November 8, 2021):** Second exchange designation, with over half of its known transaction history associated with illicit actors [29].
- **Virtual currency platform settlements** (Binance, Bittrex, Poloniex, CoinList, Uphold) demonstrate OFAC's strict-liability approach and its expectation that companies use IP address, KYC, and geolocation data for screening [29].

FinCEN has also made clear that ransomware-related SARs are "situations involving violations that require immediate attention," and that DFIR firms accounted for 63% of ransomware-related SARs filed in 2021 — reflecting the government's visibility into payment facilitation [30][32].

### 3.3 Healthcare Enforcement

- **Presence Health ($475,000, 2017):** First OCR settlement solely for Breach Notification Rule violations — the entity exceeded the 60-day notification deadline [57].
- **BST & Co. CPAs ($175,000):** Ransomware breach exposed 100,000+ individuals' PHI [57].
- **Deer Oaks ($225,000):** Failure to conduct a risk analysis before a breach [57].
- **Comstar ($75,000):** Ransomware attack affecting 585,621 individuals [57].
- **2024–2025 OCR enforcement** exceeded $9.4 million in settlements and penalties, with inadequate risk analysis the most common violation (13 of 20 cases) [57].

### 3.4 Financial Services Enforcement

- **NYDFS Healthplex (2025):** $2 million civil penalty for Part 500 violations, demonstrating NYDFS's active enforcement posture [84].
- **Block Inc. ($40 million, 2025):** Board-reviewed third-party cybersecurity policy and business continuity control failures [46].
- **Gemini Trust Co. ($37 million + $1.1 billion restitution, 2024):** Failure to assess and oversee a third-party lending partner [46].
- **PayPal ($2 million):** No MFA for users and undocumented access controls [46].
- **State AGs:** Massachusetts AG fined an entity $795,000 for delayed notifications; California AG fined a software company $6.75 million for misleading the public about a breach [10].

---

## 4. Lessons for Enterprises on Disclosure Strategy

### 4.1 When and How to Disclose: Timing, Materiality, and Coordination

**Build the materiality determination workflow before an incident occurs.** The four-business-day SEC clock is unforgiving. Real-world data from the first two years of the rule shows an average detection-to-disclosure time of 7.88 business days and a median of 4.5 business days — with 50% of filers needing to amend their 8-Ks as scope information evolved [10][11]. The fastest materiality determination on record was Halliburton at 2 days; UnitedHealth took 1 day; AT&T took 84 days (with a national security delay) [11].

A disciplined workflow should include [12][13][14]:

- **Pre-drafted templates** for Item 1.05 and Item 8.01 disclosures, including placeholder language for incident nature, scope, timing, and impact [15].
- **A designated cross-functional materiality team:** CISO/CIO, CFO, General Counsel, and business leaders must be convened immediately upon incident discovery [12][13].
- **Contemporaneous documentation** of the materiality assessment process — who was involved, what facts were considered, and conclusions reached — because the SEC may request it [12].
- **A decision tree:** If material → file Item 1.05 within four business days. If immaterial or undetermined → consider voluntary Item 8.01 disclosure. If later determined material → file Item 1.05 within four business days of that determination [6][8][9].

**Coordinate the 8-K timeline with other regulatory clocks.** The 8-K deadline does not harmonize with other regimes. Enterprises should build a **notification sequencing matrix** that maps, for each incident type, the following deadlines [49][45][36][61][56]:

| Deadline | Regime | Trigger |
|---|---|---|
| 12 hours | TSA (pipelines/LNG) | Cybersecurity incident identification |
| 24 hours | NYDFS §500.17(c) | Extortion payment made |
| 24 hours | CIRCIA (when final) | Ransom payment made |
| 36 hours | Federal banking regulators | Notification incident determined |
| 72 hours | NYDFS §500.17(a) | Cybersecurity incident determined |
| 72 hours | CIRCIA (when final) | Reasonable belief of covered incident |
| 4 business days | SEC 8-K Item 1.05 | Materiality determination |
| 30 days | NYDFS §500.17(c) | Written description of extortion payment |
| 30 days | FTC Safeguards Rule | Unauthorized acquisition of 500+ consumers' unencrypted data |
| 30–45 days | State breach laws | Breach discovery/confirmation |
| 60 days | HIPAA | Breach discovery (individuals, OCR, media) |

**Practical tip:** The fastest clocks (TSA 12-hour, NYDFS/CIRCIA 24-hour ransom payment, banking 36-hour) are typically triggered earlier than the SEC's materiality clock. Companies should treat the SEC filing as the *public* disclosure anchor but ensure the earlier regulator-specific notices are prepared and sent in parallel, without premature public statements that could undermine law enforcement or investor communications [10][15][36].

### 4.2 Navigating the Tension Between SEC Materiality and Sector-Specific Deadlines

The SEC's materiality threshold (with its SolarWinds-era "lessons learned") operates on a different axis than sector-specific notification rules:

- **Sector rules use objective, incident-based triggers** — e.g., "notification incident" (banking), "cybersecurity incident" (NYDFS), "covered cyber incident" (CIRCIA), "breach of unsecured PHI" (HIPAA). These do not require a materiality judgment.
- **The SEC rule uses a subjective investor-focused test** — materiality must be determined "as soon as reasonably practicable," but the determination itself is a judgment call that courts review with hindsight.

**Key tension:** a company may be required to notify NYDFS or its banking regulator within 24–72 hours of an incident that it has not yet determined to be material for SEC purposes. The resolution is procedural, not substantive: **sector notifications do not themselves make an incident material, and consulting with regulators does not trigger the SEC clock** [3][82]. But the information gathered for those notifications (impact assessments, forensic findings, operational impact analyses) will feed directly into the materiality determination. Companies should therefore treat the sector notification process as the first phase of the SEC materiality assessment, not as a separate track [10][15].

The SEC's "series of related unauthorized occurrences" definition also requires companies to aggregate individually immaterial ransomware attacks over time — e.g., repeated small attacks by the same threat actor exploiting the same vulnerability — and assess whether the series is collectively material [3][6][7][89]. This aggregation analysis should be built into quarterly disclosure controls, not just incident response [12][14].

### 4.3 The Pay-vs-Not-Pay Decision: OFAC Compliance and Its Interaction with Disclosure

**The OFAC screening obligation is non-negotiable and precedes any payment decision.** Before making any ransomware payment, enterprises must [23][28][29]:

1. **Screen the payment recipient** against the SDN List — including digital currency addresses (searchable via the "ID #" field in OFAC's Sanctions List Search tool), legal entity names, and aliases [28].
2. **Check IP addresses and wallet addresses** using blockchain analytics tools; collect and document KYC information on the purported recipient [28][29].
3. **Assess jurisdictional exposure:** Is the threat actor or payment intermediary located in or affiliated with a comprehensively embargoed jurisdiction (e.g., North Korea, Iran, Syria, Cuba, Crimea)? [23].
4. **Consider whether the actor is a designated group** — e.g., Evil Corp, REvil/Sodinokibi actors, or other SDN-listed ransomware operators [23][29].
5. **Document all due diligence contemporaneously**, including the decision rationale, in case OFAC or another regulator inquires [28].

**The government's position on payment.** OFAC "strongly discourages" payment; the FBI and CISA warn that payment does not guarantee recovery and funds criminal enterprises [23][44]. There is **no federal statute that categorically criminalizes ransom payments**, but payments to SDNs, embargoed jurisdictions, or designated foreign terrorist organizations can trigger civil or criminal liability [26][32].

**Interaction with disclosure obligations.** The SEC's C&DIs are explicit: the size of a ransom payment is not determinative of materiality; insurance reimbursement does not make an incident immaterial; and the incident must be disclosed even if the payment resolves it before the 8-K deadline [3][6][7]. In practice, no company disclosed paying a ransom in the first year of Item 1.05 filings — but that does not mean payments did not occur; it may reflect that those incidents were not material or that companies chose not to volunteer the information [10].

**DOJ voluntary self-disclosure incentives.** The DOJ's Corporate Enforcement and Voluntary Self-Disclosure Policy (CEP) — made department-wide on March 10, 2026 — provides a three-tier system: Tier 1 (declination for full self-disclosure, cooperation, and remediation absent aggravating circumstances), Tier 2 ("near miss": NPAs under three years, no monitor, 50–75% fine reductions), and Tier 3 (up to 50% reductions for cooperation). The March 30, 2026 NSD guidance confirms that national-security-related voluntary self-disclosures (including IEEPA/OFAC-adjacent violations) should be sent to **NSD.VSD@usdoj.gov**, and that a disclosure made solely to OFAC or BIS will **not** qualify for criminal VSD credit under the CEP [73][74][75][77][78]. For ransomware payments, this means: if a payment may have involved a sanctions nexus, companies should consider whether to make a coordinated voluntary self-disclosure to OFAC (civil) and DOJ (criminal) to secure maximum mitigation.

**FinCEN SAR filing.** Ransomware-related suspicious activity must be reported via SAR with key term "RANSOMWARE" — whether the financial institution is the victim or merely processes the payment. DFIR firms facilitating payments may themselves be money transmitters requiring MSB registration [30][32].

### 4.4 Internal Governance, Board Communication, and Cross-Functional Coordination

Effective disclosure procedures require a pre-existing governance architecture [12][13][15]:

- **Board oversight:** Under Item 106(c), the board's role in overseeing cybersecurity risks must be disclosed — including which committee is responsible and the processes by which the board is informed. NYDFS §500.4 requires the CISO to report annually in writing to the senior governing body [1][45].
- **Management roles:** Item 106(c) requires disclosure of which management positions are responsible for cybersecurity risk management, their relevant expertise, and their incident-reporting processes. The SEC staff has signaled that "mere statements that a process exists" are insufficient — the disclosure must describe the process and expertise concretely [4][5].
- **CFO/Treasury integration:** The CFO's office typically executes the wire transfer for any ransom payment and must be part of the materiality team — and is central to the 24-hour NYDFS/CIRCIA ransom payment reporting triggers [12][13].
- **Communications/IR:** Legal, CISO, and communications teams must coordinate disclosure protocols. Regulation FD applies to any information shared beyond the 8-K, so investor calls, customer communications, and media statements must be consistent with SEC filings [6][9][82].
- **Tabletop exercises:** PwC and others recommend diagnostic assessments and tabletop exercises simulating ransomware incidents, including the materiality determination and notification sequencing — noting that clients often discover they are less ready than expected [13].

### 4.5 Avoiding Common Pitfalls That Led to Prior Enforcement Actions

**Pitfall 1: Delayed disclosure pending internal investigation.** The SEC's position is that companies must assess materiality as soon as reasonably practicable; they cannot wait for a full forensic investigation. If materiality is determined but scope is unknown, file under Item 1.05 and amend later [2][3][10]. The ICE case shows regulators' intolerance for delay even when the ultimate conclusion is "no unauthorized access" [22].

**Pitfall 2: Incomplete or inaccurate statements of incident scope.** Blackbaud's initial disclosure omitted that SSNs and bank account numbers were accessed; the subsequent 10-Q characterized realized exfiltration as "hypothetical." The enforcement outcome was a $3 million penalty and a disclosure controls finding [21]. **Lesson:** as investigation findings evolve, escalate them promptly to the disclosure team and amend filings within four business days.

**Pitfall 3: Continuing to use boilerplate risk-factor language post-incident.** The Unisys/Avaya/Check Point/Mimecast sweep penalized companies that framed intrusions as hypothetical risks after they had occurred [22]. **Lesson:** conduct a post-incident review of all periodic-report risk factors and update language to reflect actual events.

**Pitfall 4: Failure to aggregate related immaterial incidents.** The "series of related unauthorized occurrences" definition requires collective materiality assessment [3][6][7][89]. **Lesson:** maintain a running log of all security incidents (including low-severity ransomware attempts) and review the aggregate quarterly.

**Pitfall 5: Unvetted payment decisions.** Paying a ransom to an SDN or embargoed jurisdiction without screening creates strict-liability OFAC exposure [23][28]. **Lesson:** no payment should be made without documented SDN screening, IP/wallet analysis, and a sanctions nexus assessment — and the payment decision itself should be documented in the incident file, because it will be relevant to both the SEC materiality assessment and any regulator inquiry [28][29].

**Pitfall 6: Inconsistent statements across stakeholders.** The SEC's June 2024 Reg FD guidance makes clear that additional information shared with customers, vendors, or analysts beyond the 8-K is subject to Regulation FD [6][9][82]. **Lesson:** centralize external communications about incidents through a single coordinated process; use confidentiality agreements where counterparty sharing is necessary for remediation.

**Pitfall 7: Premature or unnecessary Item 1.05 filings.** Filing under Item 1.05 before a materiality determination can confuse investors and trigger follow-up questions from SEC staff. The Gerding guidance is explicit that Item 1.05 is not a voluntary disclosure vehicle [6][8][9]. **Lesson:** use Item 8.01 for voluntary early disclosure; reserve Item 1.05 for material incidents.

---

## 5. Conclusion

The ransomware payment disclosure landscape as of August 2026 is characterized by **converging but unharmonized regulatory regimes**. The SEC's four-business-day materiality clock operates alongside 24-hour ransom payment reporting (NYDFS; CIRCIA when final), 36-hour banking notifications, 72-hour incident reporting, 12-hour pipeline reporting, and 30–60-day breach notification laws. OFAC's strict-liability sanctions framework makes pre-payment screening a mandatory step in any payment decision, and DOJ's new department-wide Corporate Enforcement Policy creates powerful incentives for coordinated voluntary self-disclosure.

For enterprises, the strategic imperatives are clear: build the cross-functional materiality and notification workflow before an incident occurs; pre-draft disclosure templates; maintain a notification sequencing matrix; document all materiality assessments and OFAC screening contemporaneously; update boilerplate risk factors immediately after any incident; and treat the pay-vs-not-pay decision as a multi-regulatory event requiring coordination among legal, finance, cybersecurity, and communications — not a unilateral operational choice. The enforcement record — from Blackbaud's $3 million penalty for incomplete scope disclosure to the SolarWinds dismissal's cautionary tale about overreach — demonstrates that the greatest risk lies not in any single filing deadline, but in inconsistent, incomplete, or delayed communication to the market, regulators, and law enforcement.

---

## Sources

[1] Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure (SEC Final Rule, 88 FR 51896): https://www.federalregister.gov/documents/2023/08/04/2023-16194/cybersecurity-risk-management-strategy-governance-and-incident-disclosure

[2] SEC Small Entity Compliance Guide — Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure: https://www.sec.gov/resources-small-businesses/small-business-compliance-guides/cybersecurity-risk-management-strategy-governance-incident-disclosure

[3] SEC Exchange Act Form 8-K Compliance & Disclosure Interpretations (last updated June 24, 2024): https://www.sec.gov/rules-regulations/staff-guidance/compliance-disclosure-interpretations/exchange-act-form-8-k

[4] Deloitte — SEC Issues New Requirements for Cybersecurity Disclosures: https://dart.deloitte.com/USDART/home/publications/deloitte/heads-up/2023/sec-rule-cyber-disclosures

[5] Harvard Law School Forum on Corporate Governance — SEC Adopts Final Rules on Cybersecurity Disclosure: https://corpgov.law.harvard.edu/2023/08/09/sec-adopts-final-rules-on-cybersecurity-disclosure

[6] Mintz — SEC Issues Updated Guidance on Cybersecurity Incident Disclosure Under Item 1.05 of Form 8-K: https://www.mintz.com/insights-center/viewpoints/2901/2024-07-11-sec-issues-updated-guidance-cybersecurity-incident

[7] Akin Gump — SEC Publishes Five C&DIs Covering Cybersecurity Incident Disclosures Pursuant to Item 1.05 of Form 8-K: https://www.akingump.com/en/insights/blogs/ag-deal-diary/sec-publishes-five-canddis-covering-cybersecurity-incident-disclosures-pursuant-to-item-105-of-form-8-k

[8] Hunton — SEC Staff Provides Guidance on Cyber Form 8-K Reporting: https://www.hunton.com/privacy-and-cybersecurity-law-blog/sec-staff-provides-guidance-on-cyber-form-8-k-reporting

[9] Morrison & Foerster — U.S. SEC Issues Updated Guidance on Cybersecurity Disclosure: https://www.mofo.com/resources/insights/240625-u-s-sec-issues-updated-guidance-on-cybersecurity-disclosure

[10] NYU Compliance & Enforcement — One Year of Form 8-K Material Cybersecurity Incident Reporting: https://wp.nyu.edu/compliance_enforcement/2025/03/25/lessons-learned-one-year-of-form-8-k-material-cybersecurity-incident-reporting

[11] Cherry Hill Advisory — SEC Cybersecurity Disclosure Rule: Two Years of 8-K Filings (2026): https://www.cherryhilladvisory.com/sec-cybersecurity-disclosure-rule-two-year-review

[12] PwC — Making Materiality Judgments in Cybersecurity Incident Reporting: https://www.pwc.com/us/en/services/consulting/cybersecurity-data-tech-risk/library/sec-final-cybersecurity-disclosure-rules/materiality-sec-cybersecurity-compliance.html

[13] PwC — SEC's Cyber Disclosure Rule: https://www.pwc.com/us/en/services/consulting/cybersecurity-data-tech-risk/library/sec-final-cybersecurity-disclosure-rules.html

[14] VComply — SEC Cybersecurity Disclosure Rules in 2026: https://www.v-comply.com/sec-cybersecurity-disclosure-rules-in-2026

[15] NetDiligence — SEC Cyber Incident Reporting: https://netdiligence.com/blog/2025/08/new-sec-cyber-disclosure-rule

[16] Holland & Knight — Court in SolarWinds Case Blows Down SEC's Cyber Enforcement Authority: https://www.hklaw.com/en/insights/publications/2024/07/court-in-solarwinds-case-blows-down-secs-cyber-enforcement-authority

[17] McDermott — SEC Dismisses SolarWinds Lawsuit: What CISOs Need to Know: https://www.mcdermottlaw.com/insights/sec-dismisses-solarwinds-lawsuit

[18] Harvard Law School Forum — SolarWinds Dismissed: What the SEC's U-Turn Signals for Cyber Enforcement: https://corpgov.law.harvard.edu/2025/12/07/solarwinds-dismissed-what-the-secs-u-turn-signals-for-cyber-enforcement

[19] Hunton — SEC Dismisses Remainder of SolarWinds Case: https://www.hunton.com/privacy-and-cybersecurity-law-blog/sec-dismisses-remainder-of-solarwinds-case

[20] WSHB — Important Development in Landmark Cybersecurity Case as SEC and SolarWinds Reach Preliminary Settlement: https://www.wshblaw.com/experience-important-development-in-landmark-cybersecurity-case-as-sec-and-solarwinds-reach-preliminary-settlement

[21] Haynes Boone — SEC Enforcement Action Against Blackbaud, Inc.: https://www.haynesboone.com/news/alerts/sec-enforcement-action-against-blackbaud-inc

[22] Cooley — SEC Remains Focused on Disclosure of Cybersecurity Incidents: https://sle.cooley.com/2024/06/06/sec-remains-focused-on-disclosure-of-cybersecurity-incidents

[23] OFAC — Updated Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments (September 21, 2021): https://ofac.treasury.gov/media/912981/download?inline=

[24] OFAC — Ransomware Advisory (October 1, 2020): https://ofac.treasury.gov/recent-actions/20201001

[25] OFAC — Publication of Updated Ransomware Advisory; Cyber-Related Designation (September 21, 2021): https://ofac.treasury.gov/recent-actions/20210921

[26] Covington & Burling — OFAC Issues Updated Guidance on Ransomware Payments: https://www.insideprivacy.com/cybersecurity-2/ofac-issues-updated-guidance-on-ransomware-payments

[27] Cleary — OFAC Updates Ransomware Advisory and Sanctions Virtual Currency Exchange: https://www.clearytradewatch.com/2021/09/ofac-updates-ransomware-advisory-and-sanctions-virtual-currency-exchange

[28] OFAC — Sanctions Compliance Guidance for the Virtual Currency Industry: https://ofac.treasury.gov/media/913571/download?inline=

[29] Global Investigations Review — Practical Issues in Cyber-Related Sanctions: https://globalinvestigationsreview.com/guide/the-guide-sanctions/seventh-edition/article/practical-issues-in-cyber-related-sanctions-ofac-designations-highlight-renewed-focus-digital-currency

[30] Money Laundering Watch — FinCEN Reports Spiraling SARs Relating to Ransomware: https://www.moneylaunderingnews.com/2021/10/fincen-reports-spiraling-sars-relating-to-ransomware

[31] FinCEN — Financial Trend Analysis on Ransomware (2022–2024 data): https://www.fincen.gov/news/news-releases/fincen-issues-financial-trend-analysis-ransomware

[32] WilmerHale — Ransomware Attacks: Financial Crimes Compliance Requirements: https://www.wilmerhale.com/en/insights/client-alerts/20201008-ransomware-attacks-financial-crimes-compliance-requirements

[33] Exterro — CISA Sets September 2026 Target for Final Cyber Incident Reporting Rules: https://www.exterro.com/resources/cisa-sets-september-2026-target-for-final-cyber-incident-reporting-rules

[34] Hunton — CISA Plans to Finalize Cyber Incident Reporting Regulations in September 2026: https://www.hunton.com/privacy-and-cybersecurity-law-blog/cisa-plans-to-finalize-cyber-incident-reporting-regulations-in-september-2026

[35] Bright Defense — CISA Advances CIRCIA Reporting Rule Toward 2026 Deadline: https://www.brightdefense.com/news/cisa-advances-circia-reporting-rule-toward-2026-deadline

[36] Fisher Phillips — FAQs for Businesses About CIRCIA Regulations: https://www.fisherphillips.com/en/insights/insights/new-federal-cybersecurity-reporting-rules-are-on-their-way

[37] Elisity — CIRCIA Reporting Requirements: Healthcare Guide 2026: https://www.elisity.com/blog/circia-healthcare-compliance-guide-new-regulations-critical-controls-for-2026

[38] Alation — CIRCIA Compliance Guide 2026: https://www.alation.com/blog/circia-compliance-guide-2026

[39] Morrison & Foerster — U.S. Congress Passes Cyber Incident and Ransom Payment Reporting Requirement: https://www.mofo.com/resources/insights/220311-cyber-incident-ransom-payment-reporting

[40] CISA — Ransomware Vulnerability Warning Pilot (RVWP): https://www.cisa.gov/stopransomware/Ransomware-Vulnerability-Warning-Pilot

[41] CISA — Stop Ransomware: https://www.cisa.gov/stopransomware

[42] CISA — Report Ransomware: https://www.cisa.gov/stopransomware/report-ransomware

[43] CISA — StopRansomware Guide: https://www.cisa.gov/stopransomware/ransomware-guide

[44] CISA/FBI — Ransomware Awareness for Holidays and Weekends (AA21-243A): https://www.cisa.gov/news-events/cybersecurity-advisories/aa21-243a

[45] NYDFS — Cybersecurity Regulation 23 NYCRR Part 500 (Second Amendment): https://www.dfs.ny.gov/cybersecurity/23-NYCRR-Part-500

[46] WilmerHale — NYDFS Finalizes Amendments to Cybersecurity Regulations: https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20231128-nydfs-finalizes-amendments-to-cybersecurity-regulations

[47] Koley Jessen — New York Department of Financial Services Strengthens Cybersecurity Regulation: https://www.koleyjessen.com/insights/publications/new-york-department-of-financial-services-strengthens-cybersecurity-regulation-through-recent-amendment

[48] Debevoise — A Summary of the Final Amendments to the NYDFS Cyber Rules: https://www.debevoisedatablog.com/2023/11/14/a-summary-of-the-final-amendments-to-the-nydfs-cyber-rules

[49] Federal Register — Computer-Security Incident Notification Requirements for Banking Organizations and Their Bank Service Providers (86 FR 66424): https://www.federalregister.gov/documents/2021/11/23/2021-25510/computer-security-incident-notification-requirements-for-banking-organizations-and-their-bank

[50] Federal Reserve — Agencies Approve Final Rule Requiring Computer-Security Incident Notification: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20211118a.htm

[51] Morrison & Foerster — Federal Banking Agencies Issue Long-Awaited Computer Security Incident Notice Rules: https://www.mofo.com/resources/insights/211122-computer-security-incident-notice-rules

[52] Ncontracts — New Cyber Incident Notification Rule & 4 Steps to Update Response Plan: https://www.ncontracts.com/nsight-blog/4-steps-to-update-your-institutions-incident-response-plan

[53] OCC Bulletin 2022-8 — Information Technology: OCC Points of Contact for Banks' Computer-Security Incident Notifications: https://www.occ.gov/news-issuances/bulletins/2022/bulletin-2022-8.html

[54] FTC — Safeguards Rule: What Your Business Needs to Know: https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know

[55] Covington & Burling — FTC Finalizes New Notification Requirement for GLBA Safeguards Rule: https://www.cov.com/en/news-and-insights/insights/2023/11/ftc-finalizes-new-notification-requirement-for-glba-safeguards-rule

[56] HHS — Breach Notification Rule: https://www.hhs.gov/hipaa/for-professionals/breach-notification/index.html

[57] HIPAA Journal — What Are the HIPAA Breach Notification Requirements?: https://www.hipaajournal.com/hipaa-breach-notification-requirements

[58] Censinet — How to Meet 60-Day Breach Notification Requirements: https://censinet.com/perspectives/meet-60-day-breach-notification-requirements

[59] HHS — HIPAA Security Rule NPRM: https://www.hhs.gov/hipaa/for-professionals/security/hipaa-security-rule-nprm/index.html

[60] Paul Hastings — HHS OCR Releases Proposed Updates to HIPAA Security Rule: https://www.paulhastings.com/insights/ph-privacy/hhs-ocr-releases-proposed-updates-to-hipaa-security-rule

[61] TSA — TSA Updates, Renews Cybersecurity Requirements for Pipeline Owners (July 26, 2023): https://www.tsa.gov/news/press/releases/2023/07/26/tsa-updates-renews-cybersecurity-requirements-pipeline-owners

[62] Davis Wright Tremaine — TSA Security Directive Requires 30-Day Cybersecurity Assessments, Rapid Incident Notification for "Critical" Pipeline and LNG Facilities: https://www.dwt.com/blogs/privacy--security-law-blog/2021/06/tsa-pipeline-lng-cybersecurity-rules

[63] Federal Register — Ratification of Security Directives (January 17, 2025): https://www.federalregister.gov/documents/2025/01/17/2025-01243/ratification-of-security-directives

[64] CISA — Chemical Facility Anti-Terrorism Standards (CFATS): https://www.cisa.gov/resources-tools/programs/chemical-facility-anti-terrorism-standards-cfats

[65] SOCMA — Chemical Facility Anti-Terrorism Standards (CFATS): https://www.socma.org/policy/chemical-facility-anti-terrorism-standards-cfats

[66] Nossaman — Water Utilities: Congress Temporarily Extends Cyber Laws, EPA Releases New Guidance: https://www.nossaman.com/newsroom-insights-water-utilities-congress-temporarily-extends-cyber-laws-epa-releases-new-guidance

[67] GAO — Critical Infrastructure Protection: EPA Urgently Needs a Strategy to Address Cybersecurity Risks to Water and Wastewater Systems (GAO-24-106744): https://www.gao.gov/products/gao-24-106744

[68] E&E News — 'Frightening' Cyberattacks on Water Utilities Renew Calls for Regulations: https://www.eenews.net/articles/frightening-cyberattacks-on-water-utilities-renew-calls-for-regulations

[69] FBI — Malicious Cyber Actors Targeting Water and Wastewater Sector (PSA 2026): https://www.fbi.gov/investigate/cyber/alerts/2026/malicious-cyber-actors-targeting-water-and-wastewater-sector-internet--facing-programmable-logic-controllers-causing-operational-disruptions

[70] Privacy Rights Clearinghouse — Data Breach Notification Laws: A 50-State Survey (2026 Edition): https://privacyrights.org/resources-tools/reports/data-breach-notification-laws-50-state-survey-2026-edition

[71] New York Attorney General — SHIELD Act: https://ag.ny.gov/resources/organizations/data-breach-reporting/shield-act

[72] Data Protection Report — California Tightens Data Breach Notification Timelines, Imposes 30-Day Notice Requirement: https://www.dataprotectionreport.com/2025/11/california-tightens-data-breach-notification-timelines-imposes-30-day-notice-requirement

[73] DOJ Criminal Division — Corporate Enforcement: https://www.justice.gov/criminal/criminal-division-corporate-enforcement

[74] Gibson Dunn — Key Takeaways from DOJ's First-Ever Department-Wide Corporate Enforcement and Voluntary Self-Disclosure Policy: https://www.gibsondunn.com/key-takeaways-from-doj-first-ever-department-wide-corporate-enforcement-and-voluntary-self-disclosure-policy

[75] Cooley — DOJ Announces New Corporate Enforcement and Voluntary Self-Disclosure Policy: https://investigations.cooley.com/2026/03/18/doj-announces-new-corporate-enforcement-and-voluntary-self-disclosure-policy

[76] Miller & Chevalier — DOJ Criminal Division Issues Updated Corporate Enforcement and Voluntary Self-Disclosure Policy: https://www.millerchevalier.com/publication/doj-criminal-division-issues-updated-corporate-enforcement-and-voluntary-self

[77] DOJ Office of Public Affairs — Reporting Voluntary Self-Disclosures of Violations of National Security Laws Under the Department-Wide Corporate Enforcement Policy: https://www.justice.gov/opa/pr/reporting-voluntary-self-disclosures-violations-national-security-laws-under-department-wide

[78] Baker McKenzie — DOJ National Security Division Issues Guidance on Voluntary Self-Disclosures: https://sanctionsnews.bakermckenzie.com/doj-national-security-division-issues-guidance-on-voluntary-self-disclosures-under-the-new-department-wide-corporate-enforcement-policy

[79] FBI — Guidance to Victims of Cyber Incidents on SEC Reporting Requirements: FBI Policy Notice Summary: https://www.fbi.gov/investigate/cyber/fbi-guidance-to-victims-of-cyber-incidents-on-sec-reporting-requirements-fbi-policy-notice-summary

[80] Skadden — FBI, DOJ and SEC Publish Guidance on Requesting Delayed Reporting of Material Cyber Incidents on Form 8-K: https://www.skadden.com/insights/publications/2023/12/fbi-doj-and-sec-publish-guidance

[81] Paul Hastings — FBI, DOJ, and SEC Publish Guidance on Requesting Delayed Reporting of Item 1.05 Material Cybersecurity Incidents on Form 8-K: https://www.paulhastings.com/insights/ph-privacy/fbi-doj-and-sec-publish-guidance-on-requesting-delayed-reporting-of-item-1

[82] Loeb & Loeb — SEC Issues Guidance on Material Cybersecurity Incidents: https://www.loeb.com/en/insights/publications/2024/07/sec-issues-guidance-on-material-cybersecurity-incidents

[83] Bitsight — SEC Regulations: What Is a Material Cybersecurity Incident?: https://www.bitsight.com/blog/sec-regulations-what-material-cybersecurity-incident

[84] Steptoe — Final NYDFS Cybersecurity Rules Take Effect: What Financial Services Companies Must Do Now: https://www.steptoe.com/en/news-publications/final-nydfs-cybersecurity-rules-take-effect-what-financial-services-companies-must-do-now.html

[85] SaltyCloud — What Is 23 NYCRR Part 500? NYDFS Cybersecurity: https://www.saltycloud.com/blog/what-is-23-nycrr-500

[86] Aon — Ransomware Payment Prohibitions — Do They Work, and Will More States Adopt Them?: https://www.aon.com/risk-services/professional-services/ransomware-payment-prohibitions-do-they-work-and-will-more-states-adopt-them

[87] Freeman Mathis & Gary — Congress Ready to Implement New Cyber Incident and Ransomware Payment Reporting Legislation: https://www.fmglaw.com/cyber-privacy-security/congress-ready-to-implement-new-cyber-incident-and-ransomware-payment-reporting-legislation

[88] White House — Expanding Capabilities to Combat Transnational Cyber-Enabled Crime (August 2026): https://www.whitehouse.gov/presidential-actions/2026/08/expanding-capabilities-to-combat-transnational-cyber-enabled-crime

[89] BDO — SEC Cybersecurity Rules: A Snapshot: https://arch.bdo.com/sec-cybersecurity-rules-a-snapshot
