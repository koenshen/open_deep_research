# Third-Party Vendor Risk 2025–2026: Lessons from Major Breaches in Finance, Healthcare, and Technology

## Executive Summary

The 2025–2026 period marks a structural turning point in third-party risk. Verizon's 2025 Data Breach Investigations Report found third-party involvement in 30% of all breaches — double the prior year's 15%, the largest single-year shift in the report's history — and its 2026 edition shows supply chain involvement rising another 60% year-over-year to appear in 48% of breaches [2][16]. IBM's 2025 Cost of a Data Breach Report puts the average supply chain-originated breach at $4.91 million with a 267-day lifecycle, the longest of any vector tracked [2].

The breaches detailed in this report share a common geometry: attackers are no longer breaking into the headline organization. They are compromising a statement-printing vendor used by two banks (Citizens, Frost), a business-process outsourcer touching one in five Americans' health data (Conduent), a procurement firm serving Swiss banking giants (Chain IQ), an abandoned four-year-old integration credential (Klue), an outsourced contact-centre agent (Qantas), and an open-source security scanner trusted by the European Commission (Trivy). The data, the liability, and the reputational damage flow upstream to the client organization regardless of where the intrusion physically occurred.

Three cross-cutting lessons emerge for risk managers:

1. **Identity is the new perimeter.** Compromised third-party credentials — often lacking MFA, or consisting of OAuth tokens and "ghost" service accounts that were never revoked — were the entry point in a majority of the major breaches analyzed. Unit 42 found identity weaknesses played a material role in nearly 90% of its 750+ incident response investigations in 2025 [3].

2. **Concentration risk is now the defining systemic vulnerability.** One vendor serving hundreds of clients creates a single point of failure: Conduent (62.2 million people affected across dozens of health plans), Salesloft/Drift (700+ organizations), and CEVA Logistics (Valve, ING, Bol, De Bijenkorf simultaneously) demonstrate the cascading scale.

3. **Point-in-time due diligence is obsolete.** The vendor that passed its initial security review months earlier was breached in nearly every major case. Regulators in the EU (DORA), the US (SEC Regulation S-P, NYDFS), and Asia-Pacific (Singapore PDPC, Australia OAIC) are now demanding continuous monitoring, contractual risk allocation, and board-level accountability.

---

## 1. The 2025–2026 Third-Party Risk Landscape

### 1.1 Aggregated statistics

- **Verizon 2025 DBIR:** 30% of all breaches involved third-party suppliers (up from 15%); the average cost to remediate a third-party-originated breach is nearly $4.8 million [1][2].
- **Verizon 2026 DBIR:** vulnerability exploitation overtook stolen credentials as the leading breach entry point (31%); ransomware appears in 48% of breaches; supply chain involvement rose 60% year-over-year to feature in 48% of breaches [2][16].
- **IBM 2025 Cost of a Data Breach Report:** supply chain breach average $4.91 million; 267-day mean lifecycle; 44% of zero-day attacks target managed file transfer systems [2].
- **Palo Alto Networks Unit 42 (2026 IR Report):** analysis of 750+ engagements found identity weaknesses in ~90% of investigations; 65% of initial access is identity-driven; SaaS data was relevant to 23% of cases in 2025, up from 6% in 2022. In over 90% of breaches, preventable gaps (limited visibility, inconsistently applied controls, excessive identity trust) materially enabled the intrusion [3].
- **Kaspersky global study (March 2026):** 31% of enterprise businesses were impacted by a supply chain attack in the past year — more than any other threat type, yet only 9% ranked it their top concern [5].
- **ENISA Threat Landscape 2025:** 10.6% of EU cyber incidents map to supply chain risk; 66% of compromised suppliers either didn't know or failed to report they were breached [2][42].
- **Group-IB High-Tech Crime Trends 2026:** compromised OAuth tokens from Drift, Salesloft, and Salesforce cascaded into 700+ organizations; a ransomware attack on fintech firm Marquis exposed data from 70 financial institutions; the Shai-Hulud worm tore through ~800 npm packages [4].
- **Healthcare:** 772 large breaches were reported to the HHS OCR in 2025, exposing the PHI of 139.7 million individuals — the worst year ever by volume. Between 2009 and 2025, over one billion Americans' records were exposed across 7,418 large healthcare breaches [6][7]. The average healthcare breach cost $7.42 million, the highest of any industry, with a 279-day lifecycle [8][6].
- **Financial services:** the average financial-sector breach cost $5.56 million in 2025, ~25% above the global average; median ransomware demands against financial institutions reached a record $3 million in 2026 [16].
- **Asia-Pacific:** ThreatBook recorded 15,205 security incidents across APAC from June 2025 to June 2026, with data breaches at 39.9% of incidents; China, India, Australia, Japan and South Korea absorb 61.78% of all incidents [77]. HKCERT recorded a record 15,877 incidents in Hong Kong in 2025, up 27% [79].

### 1.2 Why third-party risk became systemic

Supply chain attacks have become "the go-to model for scalable cybercrime and state-aligned operations" [4]. The drivers: (1) an exploded attack surface — dozens of SaaS platforms, hundreds of open-source packages, multiple MSPs per enterprise; (2) industrialized access brokering — Group-IB identified 263 instances of corporate access from Asia-Pacific sold on dark web forums in 2025 alone [78]; (3) identity abuse replacing malware — OAuth tokens, API keys, and service accounts let attackers bypass MFA entirely; and (4) open-source ecosystems becoming prime targets — 454,600+ new malicious open-source packages were identified in 2025, a 75% year-over-year jump [2]. Unit 42 found the fastest 25% of intrusions reached data exfiltration in 72 minutes, down from 285 minutes the prior year, with AI compressing attack timelines from weeks to hours [3].

---

## 2. Americas: Documented Breaches

### 2.1 Conduent Business Services — 62.2 million individuals (Healthcare)

**Vendor:** Conduent, a New Jersey-based business process outsourcing company (~56,000 employees; $3.4 billion annual revenue) handling printing, mailing, document processing, payment integrity, and back-office services for health plans, government agencies, and large employers. It supports roughly 100 million residents across 46 states and processes about $85 billion in annual disbursements [9][10].

**Timeline:**
- **October 21, 2024:** SafePay ransomware group first accessed Conduent's network.
- **January 13, 2025:** intrusion detected — 84 days later — after several states reported service outages (notably Wisconsin child-support payments).
- **February 2025:** SafePay claimed responsibility, alleging theft of multiple terabytes.
- **October 2025:** notifications began, nearly one year after initial access; initial count 10.5 million.
- **February 2026:** victim count surpassed 25 million; Texas AG Ken Paxton opened an investigation.
- **June 4, 2026:** updated HHS filing confirmed at least 62,224,658 individuals affected — the third-largest healthcare breach of all time, behind only Change Healthcare (192.7 million) and Anthem (78.8 million) [9][10].

**Scale:** roughly one in five Americans. Affected clients include Humana, Premera Blue Cross, Blue Cross Blue Shield of Texas, Montana, Illinois, and New Mexico, Volvo Group North America, Gold Coast Health Plan, Wisconsin Department of Children and Families, and Oklahoma Human Services. Data exposed: names, Social Security numbers, dates of birth, addresses, treatment information, medical records, and health insurance policy numbers [9][10].

**Root cause:** network intrusion by SafePay ransomware with approximately three months of undetected access — a business-process-outsourcing supply chain compromise. The ballooning victim count "proves the intricacy of determining breach scope when a single vendor serves hundreds of covered entity clients simultaneously" [9].

**Impacts:** direct breach costs of ~$9 million through September 2025, with another $16 million anticipated by Q1 2026 (partly covered by cyber insurance); more than 10 consolidated federal class actions in New Jersey; a Texas AG investigation; and sharp criticism from Missouri regulators over perceived non-cooperation. Conduent faced severe backlash for waiting nearly nine months before notifying affected individuals [9][10][8].

### 2.2 NYC Health + Hospitals — 1.8 million+ (Healthcare)

**Vendor/sector:** NYC Health + Hospitals, the largest US public health system, disclosed a major breach attributed to an "unnamed third-party vendor with access to NYC H+H systems" [11].

**Timeline:** suspicious activity detected February 2, 2026; unauthorized access ran from roughly late November 2025 through February 2026; reported to HHS March 24, 2026 [11].

**Scale/impact:** at least 1.8 million people affected. Exposed data included three layers: (1) classical PII (names, SSNs, driver's license and passport numbers, taxpayer IDs, bank and card data); (2) medical and insurance data (diagnoses, medications, test results, claims) capable of enabling blackmail and fraudulent claims; and (3) biometrics — fingerprint and palm-print data that "stay with a person for life and cannot be easily erased or replaced" [11]. In July 2026, LeakNet published a preview of a claimed 11-terabyte archive linked to 12M+ people (unverified). Response included 24 months of free Kroll credit/identity monitoring [11].

### 2.3 Citizens Financial Group / Frost Bank / TSYS — single shared vendor (Finance)

**Vendor:** a single third-party vendor providing statement printing for Citizens Financial Group and tax-document fulfillment for Frost Bank. Neither bank's own network was directly breached [12][13][14].

**Timeline:** April 20, 2026, the Everest ransomware gang listed both banks on its dark-web extortion portal with a six-day ultimatum. Class actions were filed within four days; on May 2, Everest listed TSYS (a Global Payments subsidiary) on its leak site [12][13].

**Scale:** 3.65 million bank records across both institutions — ~3.4 million Citizens records (names, addresses, account numbers; reportedly no SSNs) and ~250,000 Frost records including Social Security numbers, tax IDs, mortgage rates, income, and investment data capable of enabling full identity theft [12][13][14].

**Root cause:** a shared vendor with weaker security holding high-value customer data. Everest combined data exfiltration with ransom demands and a weeks-long dwell time. Analysts identified four problematic vendor-access patterns: standing VPN credentials, network-level reach, local copies as workflow, and no session evidence [14].

**Impacts:** six class-action lawsuits were filed against the banks — not the vendor — "because liability flows upstream regardless of where the compromise occurred" [12]. Regulatory framing shifted: "Our vendor was breached, not us" describes where the intrusion occurred, but does not answer whether the bank met its GLBA/OCC oversight obligations. Regulators now hold financial institutions accountable for vendor oversight failures regardless of who technically owned the compromised systems [12][13].

### 2.4 Marquis Software — 70+ financial institutions (Finance)

**Vendor:** Marquis Software, a Texas fintech providing customer relationship tools for banks and credit unions, tracking accounts, SSNs, account numbers, addresses, balances, and employee notes [15].

**Timeline:** breach occurred August 2025; detected August 14; company notified law enforcement and hired experts; warned 74+ institutions in November 2025; regulatory filings later revealed 672,075 people affected (law firms estimate up to 1.35 million) [15].

**Root cause:** a hack of vendor systems — UpGuard describes the vector as a SonicWall vulnerability — with a reported (but unconfirmed) ransom payment [15][16]. Group-IB classifies it as a ransomware attack on a fintech firm exposing data from 70 financial institutions [4].

**Impacts:** affected banks stressed that hackers never breached their own systems — yet the breach triggered notification obligations, legal exposure, and reputational damage across the client base. At least one affected company noted its bank was impacted but not among the 74 listed institutions, suggesting broader reach [15].

### 2.5 Allianz Life and Canada Life — Salesforce CRM campaigns (Insurance/Finance)

**Allianz Life (August 2025):** hackers linked to Scattered Spider and ShinyHunters exfiltrated over 2.8 million customer and partner records from Allianz Life's Salesforce CRM via advanced vishing attacks that bypassed technical defenses. UpGuard lists 1,497,063 affected individuals. The campaign targeted 700+ organizations, including Adidas, Google, Cartier, and Louis Vuitton [16][17].

**Canada Life (April 2026):** Canada's second-largest insurer disclosed that ShinyHunters gained access through a single compromised employee account and used it to query data in the insurer's Salesforce CRM environment. Canada Life's verified count was 70,000 individuals (less than 0.5% of ~14 million customers); ShinyHunters claimed 5.5 million records — described by analysts as "extortion inflation." Exposed data included names, dates of birth, addresses, gender, and income level; no SINs or banking details were confirmed. The vulnerability was "the human account and absence of controls to detect unusual bulk exports from a single user session — not a Salesforce flaw." Experts noted many large insurers still rely on basic passwords or easily phished MFA rather than phishing-resistant MFA, device checks, and conditional access [18][19].

### 2.6 PowerSchool — 62 million students, parents, and educators (Technology/Education)

**Vendor:** PowerSchool, a Folsom, California-based education technology provider serving over 18,000 school organizations across 90 countries and supporting 60+ million students [20].

**Timeline:** earliest unauthorized activity December 19, 2024; PowerSchool aware by December 28; communicated to customers January 7, 2025; DOJ court documents (May 2025) confirmed ~62 million individuals affected and a ransom demand of ~$2.85 million in bitcoin; Ontario Information and Privacy Commissioner (IPC) released its final report November 17, 2025 [20][21][22].

**Root cause:** a threat actor exploited credentials with elevated administrative privileges belonging to a PowerSchool subcontractor outside the US. Many institutions had enabled "always on" remote maintenance. CrowdStrike's investigation confirmed access via a single compromised credential to the PowerSource support portal, with data exfiltration via an export tool. The perpetrator — Matthew D. Lane, a 19-year-old US student — pleaded guilty [20][21].

**Ontario IPC findings:** Canada's most detailed regulatory response to a third-party breach concluded the institutions involved did NOT have reasonable safeguards. Systemic weaknesses included: elevated user privileges contrary to least-privilege principles; no MFA on PowerSource; continuous remote access; short log retention; inconsistent/outdated contracts lacking confidentiality, subcontracting, security, retention, and audit provisions; and over-collection of sensitive data (health card numbers, SINs, insurance details) without legal authority. The IPC ordered compliance proof within six months, emphasizing that "accountability cannot be outsourced" [21][22].

### 2.7 Salesloft/Drift → Salesforce OAuth supply-chain breach — 700+ organizations (Technology)

**Vendor:** Salesloft's Drift AI chat agent, which connects via OAuth to customers' Salesforce CRM systems. The intrusion cluster UNC6395 stole the OAuth tokens Drift uses to connect to customer Salesforce environments [23][24][25].

**Timeline (per Cloudflare's detailed reconstruction):** August 9 reconnaissance; August 12 initial compromise via stolen credential; August 17 bulk exfiltration via Salesforce Bulk API 2.0 (case text pulled in ~3 minutes, then the Bulk job entry was deleted to cover tracks); August 20 Salesloft revoked all Drift-to-Salesforce connections; August 25 Cloudflare disabled the Drift account and rotated 104 exposed API tokens; September 2 customers notified [23].

**Scale:** 700+ organizations impacted, including Cloudflare, Google, PagerDuty, Palo Alto Networks, Proofpoint, Zscaler, Tanium, BeyondTrust, CyberArk, Tenable, Qualys, Rubrik, Elastic, Workday, Workiva, Fastly, and Nutanix. Exposed data included business contacts, support case text, account information, and — in some cases — API keys and cloud credentials found in support cases [23][25].

**Root cause:** stolen OAuth tokens enabling attackers to impersonate the trusted Drift application and bypass MFA. Persistent OAuth access (non-expiring tokens), over-permissive app permissions, limited monitoring of SaaS logs, and unsecured secrets stored in Salesforce fields were the enabling blind spots. FINRA issued a member alert to all firms, recommending disconnection of integrations, credential rotation, forensic log review, and least-privilege controls [23][24][25].

### 2.8 Klue → Salesforce OAuth supply-chain breach — ~200 organizations (Technology)

**Vendor:** Klue, a market intelligence SaaS provider whose integration infrastructure connected customers' CRMs (Salesforce, HubSpot, Gong, Google Drive, Slack) [26][27][28].

**Timeline:** June 11–24, 2026. Attackers exploited a legacy dormant test credential created in 2022 for a prototype integration that was never shipped — "a ghost credential... that should have been revoked years ago." Klue detected the intrusion June 12, disclosed June 15, and engaged CrowdStrike. The Icarus extortion group listed Klue on its leak site June 19; a second hacking group then claimed access to the same stolen data and launched a separate extortion campaign — indicating the original attackers were themselves compromised [26][27][28].

**Scale:** ~195–200 organizations affected, including LastPass, Huntress, Recorded Future, Tanium, Jamf, HackerOne, Snyk, OneTrust, Sprout Social, Gong, Insurity, 8x8, ReliaQuest, Pendo, and BeyondTrust. Attackers queried the Salesforce environments of at least 12 organizations in one 24-hour exfiltration run: "a slow initial pull to blend with normal traffic, then a surge of nearly 1,000 queries in a 15-minute window — invisible to organizations without API-layer logging." Data exposed: customer names, emails, addresses, phone numbers, support case histories, sales records, and — critically — customer OAuth tokens [26][27][28].

**Impacts:** LastPass confirmed this was the eighth time customer data had been exposed since 2011 — the 2022 incident alone was linked to cryptocurrency thefts exceeding $150 million. FINRA issued a member alert despite Klue not being a financial services company. Icarus reportedly reached an agreement with Klue not to publish data, but a second group still holds a portion — "illustrating how ransom payments don't guarantee data disappearance." Analysts noted the breach "does not discriminate by security maturity": HackerOne and Recorded Future, both security companies, were victims [26][27][28][80].

### 2.9 Latin America — MedicSolution (Brazil) and the Mexican government

**MedicSolution (September 2025):** KillSec obtained more than 34 GB of data comprising 94,818 files — medical evaluations, lab results, unredacted patient photos, and records relating to minors — from a software provider serving Brazil's healthcare sector. "Notably, the data was not taken through a complex hack but was left exposed in misconfigured AWS cloud buckets, highlighting persistent gaps in incident response and monitoring across the sector." Despite outreach, MedicSolution issued no public response. Brazil's LGPD classifies health data as sensitive and requires breach reporting within three business days; the ANPD has issued fines totaling over BRL 98 million (~$20M) since 2023 [30].

**Mexican government (January 30, 2026):** the Chronus Group posted datasets allegedly exfiltrated from at least 25 government institutions — 2.3 terabytes affecting up to 36 million citizens, including healthcare registration records (IMSS Bienestar). Root causes: legacy system exploitation (obsolete platforms not decommissioned or segmented), third-party vendor compromise (nearly 30% of government agencies exchange data with over 5,000 third parties; vendor-related breaches surged 68%), and credential abuse with unrevoked credentials. Infostealers LummaC2 and Vidar were confirmed with high confidence [31]. Regional context: 452 ransomware incidents hit Latin America in 2025, with Brazil (128), Mexico (78), Argentina (63), Colombia (51), and Peru (27) hardest hit; healthcare, finance, and government are the most-targeted sectors [32].

---

## 3. Europe: Documented Breaches

### 3.1 Synnovis / NHS — ~900,000 patients (Healthcare)

**Vendor:** Synnovis, a pathology services provider in South-East London co-owned by Guy's and St Thomas' NHS Foundation Trust, King's College Hospital NHS Foundation Trust, and SYNLAB [33].

**Timeline:** ransomware attack June 3, 2024; stolen data published June 20, 2024; notifications to affected patients began only in late 2025 because the investigation into the unstructured, fragmented stolen data took over a year [33].

**Scale/impact:** ~900,000 patients affected; 10,000+ outpatient and elective procedure appointments postponed. In June 2025, a hospital trust confirmed one patient's death was partly attributed to a delayed blood test result caused by the attack — the first publicly confirmed UK death linked to a cyber attack. Data could relate to any Synnovis service user across NHS hospitals, GP practices, and clinics in England [33][34].

### 3.2 DXS International — NHS clinical decision-support vendor (Healthcare)

**Vendor:** DXS International, a British company whose BestPathway and Next-Gen platforms serve ~2,000 GP practices and manage care for ~17 million registered patients — roughly 10% of all NHS referrals [35][36].

**Timeline:** unauthorized access detected December 14, 2025; DevMan ransomware group claimed the breach the same day, alleging theft of 300 GB; DXS disclosed in a London Stock Exchange filing December 18 and notified the ICO [35][36].

**Significance:** at ~£3.4 million annual revenue, DXS is small but strategically important given patient data exposure. UK cybersecurity regulations do not automatically cover third-party health IT suppliers like DXS — a gap the incoming Cyber Security and Resilience Bill is designed to close [35][36].

### 3.3 Miljödata — 1.5 million people (Sweden, Healthcare/Public Sector)

**Vendor:** Miljödata, a Swedish IT provider for sick-leave, rehabilitation, injury, and HR management software used by 80% of Sweden's municipalities (164+ municipalities and 4 regions affected) [81][82].

**Timeline:** attack detected August 24, 2025; DataCarry ransomware group published stolen data September 12–14, 2025; HIBP disclosed the breach September 16 [81][82].

**Scale:** personal data of 1.5 million people leaked, including Swedish personal identity numbers, medical certificates, rehabilitation plans, and work-injury reports. Affected organizations included the City of Stockholm (40,000+ employees), Scandinavian Airlines, Boliden, Volvo Group North America (16,991 current and former employees with SSNs and medical records), and multiple universities. Sweden's prosecution authority confirmed the leak; a GDPR investigation was launched [81][82].

### 3.4 Advanced Computer Software Group — ICO fine (Healthcare)

**Vendor:** Advanced Computer Software Group, a Birmingham-based NHS software supplier providing systems for NHS 111, GP records access, mental health trusts, and care organizations [37].

**Timeline:** LockBit ransomware attack in August 2022; ICO final fine £3,076,320 in March 2025 (reduced from a £6.09 million provisional fine) [37].

**Root cause:** LockBit accessed health and care systems via a customer account that lacked MFA — legitimate credentials used on a third-party account. The ICO determined Advanced "failed to keep its healthcare systems secure." The incident crippled NHS 111 services and forced staff to use pen and paper, prompting a COBR crisis meeting. Data of 79,404 people was exposed, including details of how to gain entry to the homes of 890 people receiving care at home [37][34].

### 3.5 Chain IQ Group — UBS and Pictet (Finance)

**Vendor:** Chain IQ, a Swiss-headquartered global indirect procurement service company serving more than 60 clients across 49 countries [38][39][40].

**Timeline:** attacked June 12, 2025, alongside 19 other companies; Worldleaks (formerly Hunters International) claimed the attack; Chain IQ contained it within 8 hours 45 minutes by revoking access; affected customers notified the same evening [38][39].

**Scale:** ~910 GB and more than 1.9 million files stolen, including personal data of 137,000 UBS employees (names, emails, phone numbers, job roles, and even the internal direct phone number of UBS's CEO) and 230,000 lines of Pictet internal billing data with highly detailed expenses. Other affected clients included Manor, Implenia, KPMG, Mizuho, FedEx, IBM, Swiss Life, AXA, and Swisscom. Chain IQ stated it holds no data relating to clients' core business, so no client financial data was stolen [38][39][40].

**Lesson:** "the procurement security paradox" — procurement systems contain vendor relationships, contractual details, financial transaction histories, and supply-chain dependencies, making them attractive targets; compromising a single provider unlocks access to dozens of client organizations [40].

### 3.6 CEVA Logistics — Valve, ING, Bol, De Bijenkorf, Ajax (Finance/Retail/Logistics)

**Vendor:** CEVA Logistics, a French-headquartered global logistics provider with 1,000+ warehouses, ~$18.3 billion 2025 revenue, and ~110,000 employees [44][45].

**Timeline:** attack affected CEVA's European contract logistics operation between July 29 and August 1, 2026; customers notified August 1; public reporting August 6–11 [44][46].

**Scale:** eight warehouses disrupted; air, ocean, ground, and rail operations continued. Affected organizations — none of which were themselves breached — included Valve (Steam hardware shipments in Europe), Bol, De Bijenkorf, Ajax, ING, and Ace & Tate. Exposed data: names, postal addresses, phone numbers, email addresses, order details, VAT numbers, and for Valve, the type and price of Steam hardware ordered. The Dutch Data Protection Authority received breach reports from 10 organizations and is investigating [44][45][46][47].

**Root cause:** unconfirmed, but the pattern — operational disruption plus confirmed data exfiltration — suggests ransomware or disruptive malware on public-facing applications. The incident demonstrates that "the organization suffering the original breach and the organization carrying the customer relationship are not the same. Contracts can transfer responsibilities, but they cannot transfer reputational impact." Valve warned customers to expect highly targeted fake messages referencing real order details, and Bol halted data exchange with CEVA [44][47].

### 3.7 European Commission — Trivy open-source supply-chain compromise (Technology/Government)

**Vendor:** Trivy, Aqua Security's open-source container and filesystem vulnerability scanner — among the most widely deployed security tools in modern CI/CD pipelines. Compromising Trivy was "not an attack against a single organization but against the security scanning layer of a large fraction of modern CI/CD pipelines simultaneously" [41][42][43].

**Timeline:** late February 2026, an automated bot exploited a `pull_request_target` GitHub Actions workflow, exfiltrating a PAT belonging to the aqua-bot service account; March 19, 2026, TeamPCP pushed a malicious tag (v0.69.4) and repointed 76 of 77 trivy-action tags and all 7 setup-trivy tags to malicious commits. The same day, the actor obtained a compromised AWS secret with management rights over European Commission AWS accounts. The Commission's CSOC received alerts March 24; CERT-EU was notified March 25; the Commission publicly disclosed March 27; ShinyHunters published the exfiltrated dataset March 28 [41][42][43].

**Scale:** ~91.7 GB compressed (340 GB uncompressed), relating to websites hosted for up to 71 clients of the Europa web hosting service (42 internal Commission clients and at least 29 other EU entities), including potentially the European Medicines Agency, European Banking Authority, ENISA, and Frontex. Personal data (names, usernames, email addresses) was confirmed; nearly 52,000 files of outbound email communications were included. No websites were taken offline or tampered with [41][43].

**Root cause:** a cascading supply-chain campaign by TeamPCP against open-source security infrastructure — Trivy, Checkmarx KICS, LiteLLM, and Telnyx — with a shared RSA-4096 key providing technical attribution. The payload exfiltrated CI/CD secrets, encrypted them, and used an ICP blockchain canister for C2 that "cannot be taken down via conventional means." CERT-EU recommendations: pin GitHub Actions to full SHA hashes, rotate all exposed credentials, audit CI/CD pipelines, and deploy behavioral monitoring for CI/CD environments [41][42][43].

### 3.8 Marks & Spencer and Co-op — Scattered Spider via third-party help desk (Retail)

**Vendor:** M&S and the Co-op were both breached in April–May 2025 via third-party help desks — Tata Consultancy Services (TCS) for M&S — using vishing and "MFA fatigue" social engineering [48][49][50][51].

**Timeline:** initial access believed to have begun as early as February 2025; attack launched over the Easter weekend (April 19–21) with contactless payment failures; M&S acknowledged the incident April 22; DragonForce ransomware encrypted VMware ESXi servers; online shopping suspended April 25; stolen customer data revealed May 13; M&S online orders only resumed June 10.

**Scale/impact:** M&S lost roughly £300 million in operating profit; up to £750 million wiped from market value; personal information of a portion of M&S's 9.4 million active online customers compromised. The Co-op lost £80 million operating profit, had contactless payments disabled in 200 of 2,300 stores, and exposed ~6.2–6.5 million member records. M&S reverted to paper-based tracking for fresh food and clothing. Four arrests were made by the NCA [48][49][50][51].

**Root cause:** SIM swapping to bypass MFA, then help-desk impersonation at TCS and other outsourced support providers to obtain credentials, then DragonForce ransomware deployment via Active Directory. CEO Stuart Machin called it "unlucky... through human error" [48][50].

### 3.9 Other notable European incidents

- **Kering (September 2025):** ~7.4 million customers of Gucci, Balenciaga, and Alexander McQueen had personal details and detailed spending data stolen via compromised Salesforce credentials — "one weak link = full compromise." Kering refused ransom negotiations [52].
- **France Titres / ANTS (April 2026):** 11.7 million accounts exposed via an "elementary" IDOR vulnerability on the government identity portal; a 15-year-old suspect arrested. At least the fourth significant French government identity-infrastructure breach in under 12 months [53][54].
- **Capita (ICO £14 million fine, October 2025):** the 2023 breach of the UK outsourcing giant hit councils, the NHS, and defence simultaneously through a single supplier, affecting ~6.6 million individuals — one of the largest UK security-failure fines on record [34].
- **Workday (August 2025):** vishing and malicious OAuth app approval exposed business contact data across up to 11,000 corporate customers and 70 million individual user records (unconfirmed figures); neither the core HR/payroll systems nor customer tenants were breached [16].

---

## 4. Asia-Pacific: Documented Breaches

### 4.1 Japan — Askul and KDDI

**Askul Corporation (October–December 2025):** the e-commerce and logistics provider suffered a RansomHouse ransomware attack first detected October 19, 2025, suspending order processing for business customers and partners including Muji and The Loft. Approximately 740,000 records were stolen — ~590,000 business customer records, 132,000 individual customer records, 15,000 business partner records, and 2,700 employee records. **Root cause: compromise of an outsourced partner's administrator account that lacked MFA**; attackers disabled EDR, wiped backups, and exfiltrated ~1.1 TB. No ransom was paid; CEO Akira Yoshioka pledged BCP strengthening [55][56].

**KDDI (June–July 2026):** one of Japan's largest telecom providers detected unauthorized access to its email system June 17, 2026 — 52 days after the initial exploit on May 16. The intrusion exploited a **zero-day vulnerability in unnamed third-party software** shared across six ISPs (STNet, JCOM, Chubu Telecommunications, NIFTY, BIGLOBE, and KDDI), exposing up to 14.2 million email addresses and passwords. As of early July 2026, no CVE had been issued and the vendor was still developing a patch. Japan lacks a US-style mandatory disclosure clock, which explained the slow disclosure pace. Analysts predicted phishing campaigns against the 12.2 million exposed addresses and tighter Japanese regulatory oversight of shared infrastructure [57].

### 4.2 India — Tata Electronics and the Tata ecosystem

**Tata Electronics (June 2026):** the Tata Group electronics manufacturer — a key supplier to Apple, Tesla, ASML, Intel, and Qualcomm, employing 75,000+ people — had 204,341 files totaling 630.4 GB posted by the World Leaks group on June 12, 2026. Exposed data included iPhone 18 Pro circuit-board designs marked as Apple property, Tesla vehicle-program engineering drawings marked "TRADE SECRET," passport scans of staff, cryptographic certificates and key files, and years of internal emails. Tata confirmed the incident June 22, stating it was identified "a few weeks ago" — meaning the attackers likely had access for weeks or months, mapping the file system before the damage was done [58][59].

**Root cause:** a supply-chain attack — not against Apple or Tesla directly, but against the company building their products. This was the Tata Group's second major breach within roughly ten months, following the Jaguar Land Rover attack (August–October 2025), which halted production across JLR's UK plants, cost an estimated £1.9 billion to the British economy, and affected over 5,000 supplier companies. JLR's attack was traced to social engineering by ShinyHunters weeks earlier, compounded by a prior HELLCAT compromise via Jira credentials that may have left residual access [58][59][34].

### 4.3 Australia — Qantas, Genea, MediSecure, and the Victorian education system

**Qantas (June–July 2025):** data of approximately 5.7 million customers was stolen from a third-party customer servicing platform used by a Qantas contact centre in Manila. Per the OAIC's official report, a contact-centre agent received a vishing call from an actor impersonating "Qantas IT help" and was directed to connect the CRM instance to a data extraction tool. Data compromised: names, emails, phone numbers, dates of birth, and Frequent Flyer details (no financial data). Qantas detected and contained the incident the same day, and publicly disclosed within 48 hours. In July 2026, the OAIC closed its preliminary inquiries without commencing an investigation, concluding there was nothing to suggest Qantas failed to take reasonable steps under APP 1.2, APP 8 (cross-border disclosure), or APP 11 (security) — though a representative complaint by Maurice Blackburn remains under consideration [60][61]. The OAIC's report noted the "default configuration (allowing end users to authorize third-party application connections)" was the enabling weakness, since changed by the CRM provider [60].

**Genea Fertility (February–March 2025):** one of Australia's largest IVF providers was attacked by the Termite ransomware group, which stole ~700 GB of highly sensitive patient data — names, dates of birth, Medicare numbers, medical histories, diagnoses, pathology results, and potentially passport information spanning six years. Access began around January 31, 2025; Genea detected it February 14 — over two weeks of undetected access. Data was published on the dark web despite a court injunction. Impacts: downed phone lines, inaccessible patient portal, delayed urgent treatment matters, and deep patient anxiety over exposure of private fertility data. A representative complaint was lodged with the OAIC in October 2025 [62][63].

**MediSecure (April–June 2024, reference benchmark):** Australia's electronic prescription provider confirmed 12.9 million individuals' personal and health information was stolen (6.5 TB) in a ransomware attack the company attributed to a third-party vendor. MediSecure entered voluntary administration in June 2024, and the stolen data was offered for sale on an underground forum for $50,000 [64][65]. UpGuard notes MediSecure ranks among the largest healthcare breaches globally, with the same structural lesson as Conduent: concentrated healthcare supply chains create single points of failure [66].

**Victorian Department of Education (January 2026):** a third party gained access to a department database via a school's network intrusion, exposing names, school-issued email addresses, encrypted passwords, and year levels of current and former students across all ~1,700 Victorian government schools. The Office of the Victorian Information Commissioner launched a formal investigation [66][83].

### 4.4 Singapore — PDPC enforcement against SaaS providers

Singapore's Personal Data Protection Commission (PDPC) issued a series of enforcement decisions in 2025–2026 illustrating the regulatory consequences of vendor-side failures [67]:

- **People Central Pte Ltd (January 2026):** SaaS HR provider fined SGD 17,500 after deletion and exfiltration of personal data of 95,000 individuals; lapses included lack of two-factor authentication and insufficient security testing.
- **Singapore Data Hub Pte Ltd (April 2025):** SaaS provider fined SGD 17,500 after exfiltration of 689,000 individuals' data; contributing factors included publicly accessible web servers running outdated operating systems, weak password policy, no MFA, no network segmentation, and no regular patching.
- **Air Sino-Euro Associates Travel (October 2025):** travel agency fined SGD 47,000 after exfiltration of 336,759 individuals' data; PDPC found no contractual clauses with IT vendors defining scope of responsibilities and no MFA for privileged accounts.

Singapore law is explicit: a data controller may be found in breach of the PDPA even if its vendor is not — the controller bears responsibility for exercising reasonable oversight of the vendor. Maximum fines are the greater of 10% of annual Singapore turnover or SGD 1 million [67].

---

## 5. Common Root Causes

Across the 2025–2026 incidents in all three regions, recurring root causes cluster into six categories:

### 5.1 Compromised third-party credentials lacking MFA
The single most common root cause. Askul (outsourced partner admin account without MFA), Advanced Computer Software (customer account without MFA), PowerSchool (subcontractor credential without MFA on PowerSource), Change Healthcare (stolen Citrix credentials lacking MFA, 2024 benchmark), and the US mortgage-services supply-chain breach all fit this pattern [55][37][21][12][75]. The fix is not merely "enforce MFA" — it is **phishing-resistant MFA** (FIDO2/WebAuthn), because vishing and SIM-swapping defeated traditional MFA at M&S, Co-op, Qantas, and Allianz Life [50][60][17].

### 5.2 Standing access that outlives its purpose — OAuth tokens and "ghost" credentials
The Klue breach exploited a four-year-old test credential for an integration that never shipped; the Salesloft/Drift breach weaponized persistent OAuth tokens from a trusted SaaS integration. Unit 42 reports 99% of 680,000+ cloud identities analyzed had excessive permissions [3][26][23]. "You can't steal a credential that doesn't exist. You cannot replay a token that has already expired" — zero standing privileges and short-lived tokens are the emerging standard [80].

### 5.3 Misconfigured cloud services
MedicSolution's 34 GB healthcare leak came from misconfigured AWS buckets, not a sophisticated hack [30]. The March 2026 Salesforce Experience Cloud campaign — exploiting misconfigured guest user profiles — triggered a FINRA alert [29]. The 2024 benchmark Kaiser breach (13.4 million records) leaked via third-party tracking technologies, not an intrusion [8].

### 5.4 Unpatched and legacy software
KDDI's zero-day in third-party email software; Barts Health NHS Trust's exploitation of a known, patchable Oracle E-Business Suite vulnerability; Marquis's SonicWall vulnerability; SSCL/MoD payroll's unpatched contractor systems; and the Mexican government's never-decommissioned legacy platforms [57][36][16][34][31]. Supply chain attacks increasingly target the security tools themselves — the Trivy compromise is the exemplar [41].

### 5.5 Social engineering of vendor help desks and support staff
Scattered Spider's playbook — vishing IT help desks, MFA fatigue, SIM swapping — breached M&S via TCS, the Co-op via an outsourced help desk, Qantas via a Manila contact-centre agent, Allianz Life and Canada Life via Salesforce vishing, and Workday via a malicious OAuth app approval [48][49][60][17][18]. The human in the vendor's support chain is now a primary target.

### 5.6 Concentration and fourth-party risk
Conduent served hundreds of health plans; CEVA served Valve, ING, and Bol simultaneously; the Citizens/Frost vendor served multiple banks; Chain IQ served 60+ enterprises; Drift's OAuth tokens reached 700+ organizations. Concentration risk turns one vendor's failure into an industry-wide event, and "fourth-party risk" — the vendor's vendor — is now recognized by regulators as equivalent exposure [9][44][12][40][74].

---

## 6. Business Impacts Observed Across Multiple Clients

### 6.1 Operational disruption
Ransomware at vendors caused weeks of operational paralysis with real-world consequences: Synnovis delayed 10,000+ NHS appointments and was linked to one patient's death [33]; M&S lost online trading for 46 days and reverted to paper tracking [48]; JLR halted production across UK plants [34]; Askul suspended order processing for partners like Muji [55]; CEVA disrupted eight warehouses serving major retailers [44]. Unit 42 notes 87% of intrusions now span two or more attack surfaces, making containment harder [3].

### 6.2 Direct financial losses
- Conduent: ~$25 million in breach costs, partly insured [9].
- M&S: ~£300 million lost operating profit; Co-op: £80 million [48][49].
- JLR: estimated £1.9 billion UK economic impact [34].
- IBM 2025: supply chain breach average $4.91 million, 11% above the global average [2].
- Regulatory fines: Advanced £3.08 million (2025); Capita £14 million combined (2025); Australian Clinical Labs $5.8 million — the first civil penalty under Australia's Privacy Act — for failing to take reasonable steps under APP 11, failing to assess a suspected breach promptly, and failing to notify the OAIC timely [37][34][66].

### 6.3 Legal liability and class actions
Class actions now follow vendor breaches within days, and they name the client organization, not the vendor: six class actions against Citizens and Frost within four days [12]; more than ten consolidated federal class actions against Conduent [9]; proposed class actions against EY after its third-party ITSM platform breach exposed client tax documents [76]. Standing analysis post-Spokeo means plaintiffs with SSNs and tax IDs exposed (Frost) are in materially stronger positions than those with only names and addresses (Citizens) [12].

### 6.4 Regulatory penalties and enforcement escalation
- **DORA (EU):** fully applicable since January 17, 2025; the first 19 critical third-party providers (CTPPs) were designated November 18, 2025, including AWS, Microsoft, Google Cloud, IBM, SAP, Accenture, and TCS. Fines reach 10% of annual global turnover; CTPPs face periodic penalty payments up to 1% of average daily worldwide turnover per day. 2026 enforcement is no longer a grace period — Dutch, German, and French regulators have issued formal findings and remediation orders [69][70][71].
- **SEC Regulation S-P:** 72-hour customer notification for service-provider incidents; compliance deadlines December 3, 2025 (large institutions) and June 3, 2026 (smaller entities); SEC Form 8-K requires material incident disclosure within 4 business days [73].
- **DOJ/False Claims Act:** $52 million recovered across nine cyber FCA settlements in 2025 for "misrepresentations" about cybersecurity compliance — not just data breaches [73].
- **Ontario IPC (PowerSchool):** ordered institutions to prove compliance with new safeguards within six months [21][22].
- **UK Cyber Security and Resilience Bill:** will bring IT suppliers and managed service providers into scope for mandatory incident reporting within 24 hours [36].
- **India:** CERT-In six-hour incident reporting; DPDP Act obligations [59].

### 6.5 Reputational damage and cascading effects across vendor ecosystems
The most damaging effect is often the targeted fraud that follows: exposed delivery data from CEVA enabled scams quoting real addresses and recent purchases [45]; exposed SSNs and medical data from Conduent enable identity theft, medical identity theft, and personalized phishing [9]; the Kering spending data created "serious concerns about targeted fraud attempts against high-net-worth individuals" [52]. The Canada Life case shows how even a "small" confirmed impact (70,000) coexists with an unverified claim (5.5 million) that drives media coverage and customer anxiety — and how a single compromised employee account at an insurer undermines trust in an entire sector [18][19]. Companies whose vendors are breached also inherit notification complexity: determining which engagement each record came from, which entity notifies, and which jurisdiction's clock applies [76].

---

## 7. Risk-Management Best Practices Now Being Adopted

### 7.1 Continuous monitoring replaces point-in-time assessments
"Third-party risk management must evolve from a procurement checkbox into a continuous operationalized security function" [13]. Regulators in the US (OCC/Fed/FDIC guidance), EU (DORA Article 28), and Singapore (PDPC) expect end-to-end evaluation across the full vendor lifecycle. Practical measures: continuous attack-surface monitoring (SecurityScorecard, BitSight, Recorded Future), quarterly vendor access audits, and real-time anomaly detection on vendor connections. Only 18% of TPRM programs are fully integrated with enterprise risk management; only 26% incorporate incident response into TPRM — both are now being treated as deficiencies [1][74].

### 7.2 Vendor tiering and data-aware due diligence
Vendor risk programs are being re-tiered by data sensitivity, not contract value. The EY breach shows the failure mode: due diligence evaluated the ITSM platform's security at procurement time, but nobody tracked which datasets engagement teams later loaded into it. "The firms that handle a supply-chain compromise well are not the ones with the strictest procurement gate; they are the ones who can still say, two years later, exactly which dataset went where" [76]. Similarly, the Citizens/Frost breach shows the need to assess concentration risk in specialized functions like statement printing, where a handful of vendors serve the entire industry [13].

### 7.3 Contractual risk allocation
Standard clauses being adopted: 24–36-hour breach-notification obligations (aligned with OCC's 36-hour notification-incident rule and NYDFS/Reg S-P 72-hour rules), audit rights, sub-contractor disclosure (DORA Article 30 requires full sub-outsourcing transparency for critical functions), exit assistance with data portability, right-to-terminate on breach, and retention/destruction schedules. The Ontario IPC found that even adequate contract terms were unenforced at PowerSchool — the lesson is that contracts require active verification, not signatures [22][12][69].

### 7.4 Identity and access controls
- Deploy phishing-resistant MFA (FIDO2/passkeys) for all privileged and vendor-facing accounts [18][50].
- Implement just-in-time privileged access and Zero Standing Privileges; revoke credentials when projects end; time-box pilot credentials [80].
- Audit and inventory all OAuth grants and connected apps quarterly; scope OAuth tokens to minimum access; enforce IP restrictions and short token lifetimes [25][28].
- Enable API-layer logging to detect bulk-query exfiltration patterns — the Klue breach ran 24 hours undetected without it [28].
- Help-desk identity proofing: shared "green words," call-back verification, and ticket-based verification to defeat vishing [50].

### 7.5 Incident response coordination
Incorporate vendors into incident response plans; run tabletop exercises simulating vendor breaches; maintain "break-glass" severing plans for critical integrations (Cloudflare's response to Drift — revoking credentials, rotating 104 tokens, re-onboarding integrations — is the reference model) [23]. The UK NCSC urged organizations to review help-desk password-reset processes after M&S/Co-op [50][51].

### 7.6 Cyber insurance considerations
Conduent's breach costs were partly covered by cyber insurance, but insurers are tightening requirements: coverage is increasingly conditional on demonstrated continuous monitoring, MFA, and third-party oversight. Breach costs — legal defense, notification, credit monitoring, regulatory defense, business interruption — routinely reach tens of millions, and ransomware payments (PowerSchool's ~$2.85 million; Change Healthcare's ~$22 million) do not guarantee data disappearance, as the Klue second-extortion episode demonstrated [9][21][26][2].

### 7.7 New standards and frameworks gaining traction

- **DORA (EU):** the most consequential new regime — five pillars including ICT risk management, incident reporting (4-hour initial, 72-hour intermediate), resilience testing (TLPT by January 2028), and third-party risk with mandatory contractual clauses and CTPP oversight. The ECB found 65%+ of EU financial entities use at least two of AWS/Azure/GCP for critical functions, and more than 30% of significant banks' outsourcing budgets concentrate on just 10 ICT providers [69][70][71][72].
- **SEC Regulation S-P / NYDFS Part 500 / OCC-Fed-FDIC guidance (US):** lifecycle third-party risk management with board accountability; NYDFS's October 2025 TPSP guidance requires senior governing bodies to actively engage [73].
- **CMMC (US defense supply chain):** Level 1 and 2 self-assessments began November 2025; mandatory C3PAO third-party assessment for Level 2 starts November 2026 [73].
- **SBOM momentum:** CISA's 2025 Minimum Elements for SBOM; joint international SBOM guidance (September 2025); SBOMs are moving from voluntary to expected for software supply chain transparency [2].
- **UK Cyber Security and Resilience Bill:** brings MSPs and IT suppliers into scope; 24-hour incident reporting; ransomware disclosure requirements [36].
- **Australia:** Privacy and Other Legislation Amendment Act 2024 (new APP 11.3 security measures); Cyber Security Act 2024 ransomware payment reporting (72 hours to ASD); OAIC NDB scheme with a 30-day assessment window [66][68].
- **Singapore PDPA:** 72-hour PDPC notification after determining a notifiable breach; fines up to 10% of turnover; enforcement trend shows increasing penalties and scrutiny of vendor management [67].
- **Japan APPI:** Article 25 supervision of entrusted persons; 2026 reform agenda includes risk-based regulation and new rules for biological data [31].

---

## 8. Actionable Recommendations for Risk Managers

1. **Build a risk-tiered vendor inventory** covering all third and fourth parties, classified by data sensitivity and criticality — not contract value. You cannot monitor what you have not inventoried [74][1].

2. **Move from annual assessments to continuous monitoring.** Use vendor security ratings, automated attack-surface monitoring, and real-time alerts for critical vendors. Re-assess access quarterly, not at onboarding [13][17].

3. **Enforce phishing-resistant MFA everywhere**, especially on vendor admin accounts, remote maintenance portals, and help-desk systems. The PowerSchool, Askul, and Advanced breaches all involved vendor accounts without MFA [21][55][37].

4. **Audit and clean up standing access now.** Inventory every OAuth grant, API key, service account, and test credential. Revoke anything unused. Time-box pilot credentials at creation. Implement API-layer logging for bulk query detection [28][80][25].

5. **Stress-test concentration risk.** Map where your data converges — statement printers, clearinghouses, claim processors, logistics providers, CRM integrators. A single shared vendor (Conduent, CEVA, Chain IQ) can become your single point of failure [9][44][40].

6. **Redesign contracts around incident response.** Include 24–36-hour notification obligations, audit rights, sub-contractor disclosure, data return/destruction on termination, and exit assistance. Then verify compliance — enforce the clauses you already have [12][22][69].

7. **Integrate vendors into incident response plans.** Conduct tabletop exercises with key vendors; maintain break-glass severing procedures for critical integrations; define which entity notifies which regulators and individuals in multi-party breaches [23][76].

8. **Prepare for the litigation aftermath.** Vendor breaches generate class actions within days, naming your organization. Document your oversight, preserve evidence, and coordinate legal, communications, and notification in parallel [12][9].

9. **Align with the new regulatory baseline**: DORA contractual requirements (EU), SEC Reg S-P and state rules (US), PDPC expectations (Singapore), OAIC guidance (Australia). Treat regulatory compliance as a floor, not a ceiling [69][73][67].

10. **Reassess cyber insurance** in light of vendor breaches: confirm coverage for vendor-originated incidents, understand sub-limits, and expect insurers to require continuous monitoring and MFA as conditions [9].

---

## Sources

[1] FortifyData — Third-Party Data Breaches in 2026 (Updated Monthly): https://fortifydata.com/blog/top-third-party-data-breaches-in-2025

[2] swif.ai — Supply Chain Attack Statistics for 2026: https://www.swif.ai/blog/supply-chain-attack-statistics

[3] Palo Alto Networks Unit 42 — 2026 Incident Response Report: https://www.paloaltonetworks.com/resources/research/unit-42-incident-response-report

[4] Group-IB — Six Supply Chain Attack Groups to Watch Out for in 2026: https://www.group-ib.com/blog/supply-chain-attack-groups-2026

[5] Kaspersky — Supply Chain Attacks Top List of Threats Companies Suffered (March 2026): https://www.kaspersky.com/about/press-releases/supply-chain-attacks-top-list-of-threats-companies-suffered-over-past-12-months

[6] HIPAA Journal — Healthcare Data Breach Statistics (Updated for 2026): https://www.hipaajournal.com/healthcare-data-breach-statistics

[7] HIPAA Journal — Largest Healthcare Data Breaches of 2025: https://www.hipaajournal.com/largest-healthcare-data-breaches-of-2025

[8] UpGuard — 34 Biggest Healthcare Data Breaches (Updated July 2026): https://www.upguard.com/blog/biggest-data-breaches-in-healthcare

[9] Paubox — Conduent Breach Hits 62M, Ranking Third Largest in US Healthcare History: https://www.paubox.com/blog/conduent-breach-hits-62m-ranking-third-largest-in-us-healthcare-history

[10] HIPAA Journal — Conduent Business Services Data Breach Affected More Than 62.2 Million Individuals: https://www.hipaajournal.com/conduent-business-solutions-data-breach

[11] Malwarebytes — Biometrics, Diagnoses, and Bank Details Exposed in Major Healthcare Breach: https://www.malwarebytes.com/blog/news/2026/05/biometrics-diagnoses-and-bank-details-exposed-in-major-healthcare-breach

[12] ComplianceHub.Wiki — Citizens Bank and Frost Bank: Everest Ransomware's Third-Party Breach and the GLBA Vendor Accountability Gap: https://compliancehub.wiki/citizens-frost-bank-everest-ransomware-glba-vendor-risk

[13] Fyntralink — Everest Ransomware Breaches TSYS and Two Major Banks Through a Single Vendor: https://fyntralink.com/blog/everest-ransomware-tsys-citizens-frost-third-party-vendor-breach-sama-tprm-2026

[14] Cybele Software — Citizens/Frost Breach: 3.65M Records via One Vendor: https://blog.cybelesoft.com/citizens-frost-breach-vendor-access-vdi

[15] The Record (Recorded Future News) — Bank Software Vendor Marquis Says More Than 670,000 Impacted by August Breach: https://therecord.media/marquis-bank-vendor-data-breach

[16] UpGuard — 26 Biggest Data Breaches in Finance (Updated July 2026): https://www.upguard.com/blog/biggest-data-breaches-financial-services

[17] Obsidian Security — Allianz Life Salesforce Data Breach: Scattered Spider & ShinyHunters: https://www.obsidiansecurity.com/resource/allianz-data-leaked-in-major-wave-of-salesforce-attacks

[18] Cybersecurity Canada — Canada Life Data Breach: What Canadians and Canadian Businesses Need to Know: https://cybersecuritycanada.ca/news/posts/canada-life-data-breach-what-canadians-need-to-know

[19] Insurance Business — Canada Life Breach: Threat Actor Claims 5.5 Million Records Now for Sale: https://www.insurancebusinessmag.com/ca/news/breaking-news/canada-life-breach-threat-actor-claims-5-5-million-records-now-for-sale-579646.aspx

[20] PowerSchool — SIS Incident (Official Disclosure): https://www.powerschool.com/security/sis-incident

[21] Hicks Morley — Final Report Released on PowerSchool Cyberattack: https://hicksmorley.com/2025/11/20/final-report-released-on-powerschool-cyberattack

[22] Lerners LLP — IPC Rules: Accountability Cannot Be Outsourced in PowerSchool Breach: https://lerners.ca/insights/powerschool-privacy-complaint

[23] Anomali — Reviewing the Salesforce–Salesloft Drift OAuth Supply Chain Breach: https://www.anomali.com/blog/salesloft-drift-breach-recap

[24] FINRA — Cybersecurity Alert: Salesloft Drift AI Supply Chain Attack: https://www.finra.org/rules-guidance/guidance/salesloft-drift-AI-supply-chain-attack

[25] Valence Security — Salesforce OAuth Token Breach: What Every Security Team Must Know: https://www.valencesecurity.com/resources/blogs/salesforce-oauth-token-breach-what-every-security-team-must-know

[26] Rescana — Klue Supply Chain Breach Exposes OAuth Tokens and Salesforce Data (June 2026): https://www.rescana.com/post/klue-supply-chain-breach-exposes-oauth-tokens-and-salesforce-data-in-multi-stage-cybersecurity-incident-june-2026

[27] Huntress — Cybercrime Breaches Klue: Salesforce Data Impacted for Many: https://www.huntress.com/blog/klue-breach-investigation

[28] CybelAngel — LastPass Data Breach 2026: The Klue OAuth Attack That Hit 12 Security Vendors: https://cybelangel.com/blog/lastpass-forgotten-credential

[29] FINRA — Cybersecurity Alert: Salesforce Experience Cloud Security Incident: https://www.finra.org/rules-guidance/guidance/cybersecurity-alert-salesforce-experience-cloud-security-incident

[30] Infosecurity Magazine — KillSec Ransomware Hits Brazilian Healthcare IT Vendor: https://www.infosecurity-magazine.com/news/killsec-ransomware-hits-brazilian

[31] Rescana — 2026 Mexican Government Data Breach Analysis: Chronus Group Attack Exposes 36 Million Citizens: https://www.rescana.com/post/2026-mexican-government-data-breach-analysis-chronus-group-attack-exposes-36-million-citizens-via-legacy-and-third-party

[32] Recorded Future / Insikt Group — Latin America and the Caribbean Cybercrime Landscape: https://www.recordedfuture.com/research/latin-america-and-the-caribbean-cybercrime-landscape

[33] NHS England — Synnovis Cyber Incident (Update 10 November 2025): https://www.england.nhs.uk/synnovis-cyber-incident

[34] UpGuard — Biggest Data Breaches in the UK (Updated July 2026): https://www.upguard.com/blog/biggest-data-breaches-uk

[35] The Record (Recorded Future News) — Hackers Breach Internal Servers of Tech Provider for Britain's Health Service: https://therecord.media/uk-nhs-tech-provider-dxs-discloses-hack

[36] Periculo — NHS Supply Chain Cyber Incidents: DXS and Barts Health Attack: https://www.periculo.co.uk/cyber-security-blog/nhs-supply-chain-cyber-incidents-dxs-and-barts-health-attack

[37] Silicon UK — UK ICO Fines NHS Supplier for Medical Records Breach: https://www.silicon.co.uk/security/security-management/uk-ico-fines-nhs-supplier-for-medical-records-breach-574865

[38] Chain IQ — Cyber-Attack Chain IQ Group AG (Official Notice): https://chainiq.com/news/cyber-attack-chain-iq-group-ag

[39] INCIBE-CERT — Chain IQ Data Breach Affects Major Banks and Companies in Switzerland: https://www.incibe.es/en/incibe-cert/publications/cybersecurity-highlights/chain-iq-data-breach-affects-major-banks-and-companies-switzerland

[40] SecurityWeek — Chain IQ, UBS Data Stolen in Ransomware Attack: https://www.securityweek.com/chain-iq-ubs-data-stolen-in-ransomware-attack

[41] CERT-EU — European Commission Cloud Breach: A Supply-Chain Compromise: https://cert.europa.eu/blog/european-commission-cloud-breach-trivy-supply-chain

[42] Cloud Security Alliance Labs — TeamPCP: CI/CD Kill Chain from Trivy to the EU: https://labs.cloudsecurityalliance.org/research/csa-research-note-teampcp-cicd-supply-chain-20260403-csa-sty

[43] The Next Web — Hackers Breached the European Commission by Poisoning the Security Tool It Used to Protect Itself: https://thenextweb.com/news/european-commission-breach-trivy-supply-chain

[44] Conscia — A Supply Chain Nightmare: How One Logistics Provider Exposed the Hidden Risks of Third-Party Concentration: https://conscia.com/blog/hidden-risks-of-third-party-concentratio

[45] TechCrunch — A Data Breach at Shipping Giant Ceva Logistics Is Rippling Across Banks, Retailers, Steam Gamers, and Beyond: https://techcrunch.com/2026/08/10/a-data-breach-at-shipping-giant-ceva-logistics-is-rippling-across-banks-retailers-steam-gamers-and-beyond

[46] The Register — Cyberattack on Logistics Giant CEVA Delivers Customer Data into the Wrong Hands: https://www.theregister.com/cyber-crime/2026/08/11/cyberattack-on-logistics-giant-ceva-delivers-customer-data-into-the-wrong-hands/5286229

[47] Rescana — CEVA Logistics Cyberattack Disrupts European Warehouses and Exposes Customer Data: https://www.rescana.com/post/ceva-logistics-cyberattack-disrupts-european-warehouses-and-exposes-customer-data-cybersecurity-incident-analysis

[48] BlackFog — Marks & Spencer Breach: How a Ransomware Attack Unfolded: https://www.blackfog.com/marks-and-spencer-ransomware-attack

[49] BBC News — M&S and Co-op Hacks: Scattered Spider Is Focus of Police Investigation: https://www.bbc.com/news/articles/ckgnndrgxv3o

[50] 1Kosmos — 'Spider' Strikes Britain: The Hacks at M&S, Co-Op & How to Stop Them: https://www.1kosmos.com/resources/blog/spider-strikes-britain-the-hacks-at-ms-co-op-how-to-stop-them

[51] Vorboss — Marks & Spencer Cyberattack: Scattered Spider Breach & Lessons Learned: https://vorboss.com/blog/marks-spencer-cyberattack

[52] SecurityBrief UK — Kering Data Breach Exposes 7.4M Luxury Customers' Details & Spend: https://securitybrief.co.uk/story/kering-data-breach-exposes-7-4m-luxury-customers-details-spend

[53] SafeState — French Government Agency Data Breach Hits Up to 19 Million Citizens: https://www.safestate.com/post/french-government-agency-data-breach-hits-up-to-19-million-citizens

[54] UpGuard — Biggest Data Breaches in France (Updated July 2026): https://www.upguard.com/blog/biggest-data-breaches-france

[55] Rescana — Askul Corporation Ransomware Attack: 740,000 Customer Records Stolen in RansomHouse Data Breach: https://www.rescana.com/post/askul-corporation-ransomware-attack-740-000-customer-records-stolen-in-ransomhouse-data-breach-of-b

[56] The Record (Recorded Future News) — Japanese Retailer Askul Confirms Data Leak After Cyberattack Claimed by Russia-Linked Group: https://therecord.media/askul-confirms-data-breach-ransomware-incident

[57] Rescana — KDDI Email System Breach Exposes Up to 14.2 Million Credentials Across Six Japanese ISPs: https://www.rescana.com/post/kddi-email-system-breach-exposes-up-to-14-2-million-credentials-across-six-japanese-isps

[58] TechCrunch — Tata Electronics, a Major Tech Supplier to Apple and Tesla, Confirms Data Breach: https://techcrunch.com/2026/06/22/tata-electronics-a-major-tech-supplier-to-apple-and-tesla-confirms-data-breach

[59] Skeletos — 630 GB. 200,000 Files. Apple and Tesla Trade Secrets. What the Tata Electronics Breach Means for Every Indian Manufacturer: https://skeletos.io/tata-electronics-data-breach-world-leaks-supply-chain

[60] OAIC — Report into Preliminary Inquiries of Qantas: https://www.oaic.gov.au/privacy/privacy-assessments-and-decisions/privacy-decisions/Investigation-inquiry-reports/report-into-preliminary-inquiries-of-qantas

[61] ClassActions.com.au — Qantas Data Breach — Register for Compensation: https://qantasdatabreach.com.au

[62] The Guardian — Sensitive Details of Australian IVF Patients Posted to Dark Web After Genea Data Breach: https://www.theguardian.com/society/2025/feb/26/genea-data-breach-hack-ivf-patient-details-leaked-ntwnfb

[63] Cyber Management Alliance — Genea Cyber Attack Timeline: https://www.cm-alliance.com/genea-cyber-attack-timeline

[64] SecurityWeek — MediSecure Data Breach Impacts 12.9 Million Individuals: https://www.securityweek.com/medisecure-data-breach-impacts-12-9-million-individuals

[65] Huntress — MediSecure Data Breach: What Happened, Impact, and Lessons: https://www.huntress.com/threat-library/data-breach/medisecure-data-breach

[66] UpGuard — 23 Biggest Data Breaches in Australia (Updated July 2026): https://www.upguard.com/blog/biggest-data-breaches-australia

[67] Baker McKenzie — Singapore: PDPC Fines Several Organizations (January 2026): https://www.bakermckenzie.com/en/insight/publications/2026/01/singapore-pdpc-fines-several-organizations

[68] OAIC — Latest Notifiable Data Breach Statistics for January to June 2025: https://www.oaic.gov.au/news/blog/latest-notifiable-data-breach-statistics-for-january-to-june-2025

[69] Vendorica — Critical Third-Party Providers (CTPPs): The 19 Designated Under DORA: https://vendorica.com/supervisory/critical-third-party-providers

[70] Pillsbury Law — DORA Now Fully in Effect: Financial Entities and Their Service Providers Reach Critical Milestone: https://www.pillsburylaw.com/en/news-and-insights/dora-eu-financial-entities-service-providers.html

[71] Regulation-DORA.eu — DORA Enforcement 2026: The Grace Period Is Over: https://www.regulation-dora.eu/blog/dora-enforcement-2026-end-grace-period

[72] Neotas — DORA Compliance for Third-Party Risk: Complete Guide 2026: https://www.neotas.com/dora-compliance-for-third-party-risk-management

[73] BitSight — Guide to Global Third-Party Risk Regulations in 2026: https://www.bitsight.com/blog/guide-to-global-third-party-risk-regulations-us-europe-2026

[74] Bridgeforce — Navigating Third-Party Risk Management in 2026: https://bridgeforce.com/insights/third-party-risk-management-in-2026

[75] ManageEngine — Financial Supply Chain Data Breach: Managing Vendor Risks: https://www.manageengine.com/log-management/cyber-security/financial-supply-chain-data-breach.html

[76] PKWARE — 2026 Data Breaches: Cybersecurity Incidents Explained: https://www.pkware.com/blog/2026-data-breaches

[77] ThreatBook — APAC's Cyber Threat Landscape: Inside the 2026 Mid-Year Data: https://threatbook.io/blog/apacs-cyber-threat-landscape-inside-the-2026-mid-year-data

[78] SecurityBrief Australia — AI-Fuelled Supply Chain Cyber Attacks Surge in Asia-Pacific: https://securitybrief.com.au/story/ai-fuelled-supply-chain-cyber-attacks-surge-in-asia-pacific

[79] HKCERT — Hong Kong Cybersecurity Outlook 2026: https://www.hkcert.org/press-centre/hkcert-releases-hong-kong-cybersecurity-outlook-2026-security-incidents-hit-record-high-with-27-annual-increase-ai-related-attacks-and-supply-chain-risks-emerge-as-top-concerns-nearly-30-of-enterprises-lack-dedicated-cybersecurity-personnel

[80] Akeyless — The Klue Breach and the Case for Zero Standing Privileges: https://www.akeyless.io/blog/klue-breach-standing-secrets

[81] FireCompass — Miljödata Data Breach: Data Leak Sparks GDPR Investigation: https://firecompass.com/miljodata-data-breach

[82] Have I Been Pwned — Miljödata Breach: https://haveibeenpwned.com/Breach/Miljodata

[83] NetStrategy — Victorian School Data Breach: 2026 Cybersecurity Lessons: https://netstrategy.net/data-breach-impacts-victorian-schools-key-cybersecurity-lessons-for-2026
