# GDPR High-Value Enforcement Analysis: Fines Exceeding €10 Million (August 2023 – August 2026)

## 1. Executive Summary

Between roughly August 2023 and August 2026, European data protection authorities (DPAs) imposed at least 15–17 fines exceeding €10 million across a broad range of member states, including Ireland, the Netherlands, France, Italy, Germany, and Spain. The aggregate value of these fines exceeds €1.5 billion, with the Irish Data Protection Commission (DPC) accounting for the majority by value. Cumulative GDPR fines across all cases since May 2018 now stand at approximately €6.11–€7.1 billion depending on the dataset used, with roughly €1.2 billion issued in both 2024 and 2025 alone [1][2][3].

The enforcement landscape is characterized by several structural features:

- **Concentration in Ireland:** The Irish DPC has issued approximately €4.04 billion in cumulative fines (~57% of all fine value), driven by its role as lead supervisory authority for major US-based technology platforms under the one-stop-shop mechanism [2][3].
- **Cross-border transfers are the highest-risk category:** Three of the five largest fines in the window (TikTok €530M, Uber €290M, and the record Meta €1.2B in May 2023) involved transfers of personal data outside the EU [4][5].
- **Legal basis failures drive the most frequent high-value fines:** Invalid consent, unlawful reliance on legitimate interests, and improper contractual necessity produced fines ranging from €30.5 million to €310 million [6].
- **Security failures have the broadest DPA distribution:** Article 32 violations produced high-value fines across Ireland (Meta €91M), Italy (Enel €79.1M, Intesa Sanpaolo €31.8M), and Germany (Vodafone €30M component) [7].
- **Regulators are increasingly targeting design choices:** "Dark patterns," public-by-default child accounts, and authentication flaws that enable unauthorized access are now central to enforcement theories, not peripheral aggravating factors [8].
- **Procedural annulments remain a risk:** The €746 million Amazon fine (Luxembourg, 2021) was annulled on procedural grounds in March 2026, and Italy's €15 million OpenAI fine was annulled by the Court of Rome on 18 March 2026, underscoring that procedural rigor in fining methodology matters [9][10].

This report provides: (1) a catalog of all qualifying high-value cases, (2) the top 10 most frequent GDPR violation types with observed penalty ranges, and (3) concrete compliance gaps enterprises should proactively address, supported by official DPA decisions, the GDPR Enforcement Tracker, and legal analyses.

---

## 2. Qualifying Cases: Fines Exceeding €10 Million (August 2023 – August 2026)

The following cases meet the €10 million threshold and fall within the August 2023 – August 2026 window. They span six member states and multiple enforcement theories.

### 2.1 Ireland — Data Protection Commission (DPC)

| Case | Fine | Date | Core Violations |
|------|------|------|-----------------|
| TikTok Technology Limited | €530M | 2 May 2025 | Art. 46(1) (transfers to China) €485M; Art. 13(1)(f) (transparency) €45M |
| LinkedIn Ireland | €310M | 24 Oct 2024 | Art. 6(1)(a), (b), (f); Art. 5(1)(a); Arts. 13/14(1)(c) |
| Meta Platforms Ireland | €251M | 17 Dec 2024 | Arts. 25(1) €130M, 25(2) €110M; Arts. 33(3) €8M, 33(5) €3M |
| Meta Platforms Ireland | €91M | 27 Sept 2024 | Arts. 33(1), 33(5), 5(1)(f), 32(1) — plaintext passwords |
| TikTok Technology Limited | €345M | 1 Sept 2023 | Arts. 5(1)(a), (c), (f); 12(1); 13(1)(e); 24(1); 25(1), (2) — children's data |

**TikTok €530 million (2 May 2025):** The DPC fined TikTok €485 million for violating Article 46(1) GDPR by failing to verify, guarantee, and demonstrate that supplementary measures and Standard Contractual Clauses (SCCs) were effective to ensure essentially equivalent protection for EEA user data remotely accessed by staff in China. The DPC found that TikTok's own assessment of Chinese law (Anti-Terrorism Law, Counter-Espionage Law, Cybersecurity Law, National Intelligence Law) identified aspects precluding a finding of essential equivalence. The transfer risk assessment (TRA) was high-level only and failed to consider specific circumstances of remote access. An additional €45 million was imposed for the Article 13(1)(f) transparency infringement — the October 2021 EEA Privacy Policy failed to name third countries (including China) to which data was transferred. Notably, TikTok initially claimed it did not store EEA user data on servers in China, but disclosed in April 2025 that limited EEA data had in fact been stored there — prompting the DPC to consider further action. This is the first international transfer enforcement relating to China and the first concerning remote access rather than data storage [11][12][13].

**LinkedIn €310 million (24 October 2024):** The DPC found LinkedIn's processing of member data for behavioral analysis and targeted advertising lacked a valid lawful basis. Consent for third-party data was not freely given, sufficiently informed, specific, or unambiguous; legitimate interests for first-party data were overridden by members' rights and freedoms; and contractual necessity (Article 6(1)(b)) was rejected since behavioral analysis and advertising were not essential to the core service. LinkedIn also breached Articles 13(1)(c) and 14(1)(c) (transparency regarding legal bases) and Article 5(1)(a) (fairness). The inquiry originated from an August 2018 complaint by La Quadrature Du Net transferred from the French DPA [6][14][15].

**Meta €251 million (17 December 2024):** The fine related to a 2018 data breach affecting 29 million Facebook accounts worldwide (3 million in the EU/EEA) via exploitation of user tokens in the "View As" feature. The DPC found Meta failed to include all required information in its breach notification (Art. 33(3), €8M), failed to adequately document breaches (Art. 33(5), €3M), failed to embed data protection principles into the design of the feature (Art. 25(1), €130M), and failed to ensure only necessary personal data was processed by default (Art. 25(2), €110M). Affected data included names, emails, phone numbers, locations, dates of birth, religion, gender, and children's data [8][16][17].

**Meta €91 million (27 September 2024):** Meta inadvertently stored certain social media user passwords in plaintext on internal systems, discovered in a routine security review in January 2019. The DPC found violations of Article 33(1) (failure to notify the breach), Article 33(5) (failure to document breaches), Article 5(1)(f) (failure to ensure security of passwords), and Article 32(1) (failure to implement appropriate security measures). Deputy Commissioner Graham Doyle: "It is widely accepted that user passwords should not be stored in plaintext, considering the risks of abuse that arise from persons accessing such data" [7][18][19].

**TikTok €345 million (1 September 2023):** The DPC's investigation covered TikTok's processing of children's data between 31 July and 31 December 2020. Six findings: (1) child user profiles (ages 13–16) were public-by-default, violating data minimization and design/default requirements (€100M); (2) "Family Pairing" allowed unverified non-child users to pair with child accounts and send direct messages, posing severe risks to children (€65M); (3) the DPIA failed to identify risks of under-13s accessing the platform; (4) TikTok failed to provide adequate, clear information to child users (€180M); and (5) TikTok used "dark patterns" to nudge children into privacy-intrusive settings, infringing the fairness principle — a finding added at the direction of the EDPB under Article 65 following an objection by the Berlin DPA [20][21][22].

### 2.2 Netherlands — Autoriteit Persoonsgegevens (AP)

| Case | Fine | Date | Core Violations |
|------|------|------|-----------------|
| Uber Technologies / Uber B.V. | €290M | 22 July 2024 | Art. 44 / Chapter V — transfers to US without safeguards |
| Clearview AI | €30.5M | 3 Sept 2024 | Arts. 5(1)(a)/6(1); 9(1); 12/14; 12(3)/15; 27(1) |

**Uber €290 million:** The largest fine ever imposed by the Dutch DPA, against Uber Technologies Inc. and Uber B.V. as joint controllers. Between 6 August 2021 and 27 November 2023, Uber transferred EEA drivers' personal data to the US without appropriate safeguards after removing SCCs from its joint controllership agreement. Data transferred included account details, taxi licenses, location data, photos, payment details, identity documents, and in some cases criminal and medical data. The AP rejected Uber's defenses that Chapter V is complementary to Article 3 (not mutually exclusive), that drivers were the exporters, and that Article 49 derogations applied (transfers were systematic, repetitive, and continuous; less intrusive alternatives such as EU-based servers existed, per C-252/21 Meta Platforms). The complaint originated from Ligue des droits de l'Homme on behalf of 172 French Uber drivers [23][24][25].

**Clearview AI €30.5 million:** The AP fined Clearview for scraping over 30 billion facial images from the internet without consent to create a biometric database. The AP held that the biometric "vectors" qualify as special category data under Article 9 GDPR; the GDPR applies extraterritorially under Article 3(2)(b); Clearview is the controller; and the legitimate interest basis fails all three cumulative conditions. Clearview also failed to respond to access requests (Arts. 12(3)/15) and failed to designate an EU representative (Art. 27(1)). The AP is investigating whether Clearview's directors can be held personally liable [26][27][28].

### 2.3 France — CNIL

| Case | Fine | Date | Legal Basis |
|------|------|------|-------------|
| Google LLC / Google Ireland | €325M | 1 Sept 2025 | Art. 82 French Data Protection Act (ePrivacy); Art. L. 34-5 CPCE |
| SHEIN (Infinite Styles Services) | €150M | 1 Sept 2025 | Art. 82 French Data Protection Act (ePrivacy) |
| Orange | €50M | 14 Nov 2024 | Art. L. 34-5 CPCE (ePrivacy) |
| Free Mobile | €27M | 13 Jan 2026 | Arts. 32, 34, 5(1)(e) GDPR |

**Note on French cases:** Fines under the cookie/ePrivacy rules are issued under Article 82 of the French Data Protection Act (transposing the ePrivacy Directive) and/or Article L. 34-5 of the French Postal and Electronic Communications Code, NOT under the GDPR itself. The CNIL has asserted that the GDPR one-stop-shop cooperation mechanism does not apply to these operations. They are included here because of their size and direct relevance to privacy risk assessment, but flagged as non-GDPR legal bases [29][30].

**Google €325 million (1 September 2025):** The CNIL imposed €200 million against Google LLC and €125 million against Google Ireland Limited for two breaches: (1) displaying advertisements in the form of emails inserted between private emails in Gmail's "Promotions" and "Social" tabs without user consent — affecting 53 million French users; and (2) obtaining invalid consent for advertising cookies during Google account creation — consent was not free (harder to refuse than accept — dark patterns) and not informed (users were not told cookie placement was a condition of accessing Google's services). The cookie breach affected more than 74 million accounts. Google's prior fines (€100M in 2020 and €150M in 2021) were treated as aggravating factors. An injunction requires Google to stop displaying ads between emails without consent and to obtain valid consent within six months, with €100,000 daily penalties for non-compliance [31][32][33].

**SHEIN €150 million (1 September 2025):** The CNIL found SHEIN placed advertising cookies before obtaining consent, failed to respect user choices (85 cookies remained active after users refused; new third-party cookies were placed even after withdrawal), and used confusing dual consent mechanisms. The scale was massive — an average of 12 million French residents visit shein.com monthly. The fine represented roughly 2% of SHEIN's European revenue in 2023. SHEIN argued the GDPR one-stop-shop applied, but the CNIL dismissed this, citing CJEU reasoning from Google Spain and Weltimmo [29][34][35].

### 2.4 Italy — Garante

| Case | Fine | Date | Core Violations |
|------|------|------|-----------------|
| Enel Energia | €79.1M | 8 Feb 2024 | Arts. 5(1)(f), 5(2), 24(1), 25, 28, 32 |
| Intesa Sanpaolo | €31.8M | 26 Mar 2026 | Arts. 5(1)(f), 5(2), 24, 32, 33, 34 |
| Intesa Sanpaolo (Isybank transfer) | €17.6M | 12 Mar 2026 | Arts. 5, 6, 12 — unlawful profiling during corporate reorganization |
| OpenAI (ChatGPT) | €15M | Dec 2024 (ANNULLED 18 Mar 2026) | Arts. 5, 6, 12–15, 33 |

**Enel Energia €79.1 million (8 February 2024):** The highest fine ever issued by the Garante at the time. The case stemmed from a Guardia di Finanza investigation that fined four companies €1.8 million and seized their databases. Enel acquired 978 contracts from these companies outside its sales network. Serious security shortcomings in Enel's customer management systems allowed unauthorized agents to conduct nuisance calls and sign contracts with no tangible benefit to customers — at least 9,300 contracts were activated. Violations included Articles 5(1)(f), 5(2), 24(1), 25, 28, and 32 GDPR. Mitigating factors included Enel's introduction of an authentication system preventing credential sharing [36][37][38].

**Intesa Sanpaolo €31.8 million (26 March 2026):** A single employee at the Agribusiness branch in Barletta accessed the private financial records of 3,573 customers without justification over more than two years — 6,637 queries across 460 working days. Affected individuals included 34 national politicians, 43 prominent figures, and 73 Intesa employees. The Garante found the bank's alert systems failed to detect the activity for over 19 months, the circular-access model permitted any Agribusiness manager to query the entire customer base without pre-authorization, and the initial breach notification reported only 9 affected customers (marked "complete") while the bank internally knew of 3,572. The bank also improperly downgraded the risk classification and initially declined to notify affected customers until ordered to do so. Aggravating factors included three prior enforcement actions against the bank. The bank may settle for half the amount (€15.9 million) under Article 166(8) of Italy's data protection code [39][40][41].

**Intesa Sanpaolo (Isybank) €17.6 million (12 March 2026):** The Garante fined Intesa for unlawfully processing data of approximately 2.4 million customers when it unilaterally transferred their accounts to its wholly-owned digital bank subsidiary, Isybank. Customers were selected based on criteria including age (under 65), digital channel familiarity, absence of investment products, and low balances. Customers were not properly informed — the notice was placed in the app's archive section without push notifications or text messages. The Garante found the profiling was unlawful because customers could not have reasonably anticipated the activity given the circumstances and information provided [42][43][44].

**OpenAI €15 million (December 2024; annulled 18 March 2026):** The Garante found OpenAI trained ChatGPT without an adequate legal basis prior to its public launch, failed transparency obligations, lacked sufficient age verification, and failed to notify a March 2023 data breach affecting 440 Italian users. The fine was €9 million for unlawful data processing, €320,000 for the breach notification failure, and €5.68 million for failing to comply with corrective measures imposed in 2023. The Court of Rome annulled the fine on jurisdictional grounds — OpenAI's February 2024 establishment of OpenAI Ireland Limited made the Irish DPC the lead authority under the one-stop-shop mechanism. The court did not rule on the merits [10][45][46].

### 2.5 Germany — BfDI

**Vodafone GmbH — €45 million (3 June 2025):** The largest GDPR fine issued in Germany to date, split into €15 million for Article 28(1) violations (failure to sufficiently review and monitor partner agencies) and €30 million for Article 32(1) security flaws (authentication weaknesses in the "MeinVodafone" portal that allowed unauthorized third parties to retrieve customers' eSIM profiles). The first violation stemmed from fraudulent conduct by employees of third-party sales agencies who tricked customers into signing fictitious contracts. The BfDI also criticized overly broad access granted to partners into customer systems. Vodafone cooperated continuously, accepted the fines, and paid them in full; a follow-up audit will assess corrective measures. Federal Commissioner Prof. Dr. Louisa Specht-Riemenschneider: "Data protection is often mistakenly seen as an obstacle to IT investments. In fact, the opposite is true... Investing instead of incurring risks!" [47][48][49].

### 2.6 Spain — AEPD

**Aena — €10,043,002 (2025):** The largest AEPD fine ever issued, against the state-owned Spanish airport operator for deploying "high-risk" biometric facial recognition systems at eight airports without an adequate Data Protection Impact Assessment (Article 35 GDPR). The AEPD found Aena violated Article 35, Article 35(7)(b) (risk assessment), and Article 5(1)(c) (data minimization) — approximately 40,000 travelers were enrolled, and biometric data was retained up to two years. The choice of one-to-many (1:N) facial recognition architecture was highlighted as a structural compliance failure. The AEPD temporarily suspended all biometric data processing until a compliant DPIA is conducted [50][51][52].

---

## 3. Top 10 Most Frequent GDPR Violation Types in High-Value Cases

The following ranking is based on (a) the frequency with which each violation type appears in the qualifying high-value cases catalogued above, cross-referenced with (b) the CMS GDPR Enforcement Tracker's authoritative violation-type statistics covering all fines. The number of qualifying high-value cases per violation type is noted.

### Rank 1: Insufficient / Invalid Legal Basis for Data Processing (Article 6 GDPR)

- **Relevant articles:** Article 6(1) GDPR (lawfulness of processing: consent 6(1)(a), contract 6(1)(b), legitimate interests 6(1)(f)); Article 5(1)(a) (lawfulness principle); Article 7 (conditions for consent).
- **Description:** Processing personal data without a valid lawful basis, or relying on a basis that does not actually apply — e.g., "contractual necessity" for behavioral advertising, or consent that is not freely given, specific, informed, and unambiguous. This is the single most common violation type in GDPR enforcement overall, accounting for approximately 34% of all fines (669 fines, average €2.9M per CMS 2025) [1][53].
- **Qualifying cases (4):** LinkedIn €310M (Oct 2024 — invalid consent, unlawful legitimate interests and contractual necessity under Art. 6(1)(a), (b), (f)); Clearview AI €30.5M (Sept 2024 — no legal basis under Art. 6(1) read with Art. 5(1)(a)); TikTok €345M (Sept 2023 — fairness/dark patterns under Art. 5(1)(a)); Google €325M (Sept 2025 — invalid cookie consent, ePrivacy-based).
- **Observed penalty range:** €30.5M – €310M (with context cases up to €1.2B for Meta's 2023 transfer fine, which CMS categorizes under this heading).
- **Risk driver:** This violation type drove the two largest fines in the window (LinkedIn €310M; Google €325M) and the largest fine of all time (Meta €1.2B), making it the single highest-value violation category alongside international transfers [2][6].

### Rank 2: Non-Compliance with General Data Processing Principles (Article 5 GDPR)

- **Relevant articles:** Article 5(1) GDPR — lawfulness, fairness, transparency (a); purpose limitation (b); data minimization (c); accuracy (d); storage limitation (e); integrity and confidentiality (f); Article 5(2) (accountability).
- **Description:** Breaches of the overarching principles governing all processing, most commonly the fairness principle (including "dark patterns" that manipulate users toward privacy-intrusive choices), data minimization (collecting/retaining more data than necessary), and the security/integrity principle. CMS records 644 fines of this type (average €3.8M), noting this category has the highest average fine amount of any category, driven by the TikTok fines [1][53].
- **Qualifying cases (5):** TikTok €345M (fairness/dark patterns, data minimization, security); LinkedIn €310M (fairness); Uber €290M (CMS categorizes as general principles); Clearview €30.5M (Art. 5(1)(a) read with Art. 6); Enel €79.1M (Arts. 5(1)(f) and 5(2)).
- **Observed penalty range:** €30.5M – €345M.
- **Notable:** The EDPB used Article 65 dispute resolution to add the fairness/dark-patterns finding to the TikTok €345M case, signaling willingness to expand principle-based findings [20][22].

### Rank 3: Insufficient Technical and Organisational Security Measures (Article 32 GDPR)

- **Relevant articles:** Article 32(1) GDPR (security of processing); Article 5(1)(f) (integrity and confidentiality); Article 24 (controller responsibility).
- **Description:** Failure to implement appropriate security measures commensurate with risk — inadequate authentication, failure to encrypt sensitive data (e.g., plaintext passwords), poor access controls, and insufficient protection against unauthorized access or misuse. CMS records 418 fines (average €2.0M); Scrut.io lists it as the most common reason in their dataset (86 fines) [1][53].
- **Qualifying cases (4):** Meta €91M (plaintext passwords); Enel €79.1M (security shortcomings enabling unauthorized agents); Vodafone €45M (€30M component for Art. 32(1) portal/authentication flaws); Meta €251M (the underlying breach stemmed from design failures, classified as security-related).
- **Observed penalty range:** €30M – €91M.
- **Risk driver:** This category produced the broadest distribution of high-value fines across the most diverse set of DPAs (Ireland, Italy, Germany), making it the most predictable target for enterprises across all sectors [7][37][48].

### Rank 4: International Data Transfers Without Appropriate Safeguards (Chapter V, Articles 44–49 GDPR)

- **Relevant articles:** Article 44 (general principle); Article 45 (adequacy decisions); Article 46 (transfers subject to appropriate safeguards — SCCs, BCRs); Article 49 (derogations).
- **Description:** Transferring or providing remote access to personal data from the EU/EEA to a third country without an adequacy decision, valid SCCs with supplementary measures, or another Chapter V safeguard — and without a robust Transfer Impact Assessment demonstrating "essentially equivalent" protection. Remote access by third-country personnel to EU data constitutes a "transfer."
- **Qualifying cases (2):** TikTok €530M (€485M for Art. 46(1) transfers to China); Uber €290M (Art. 44/Chapter V transfers to US). Context: Meta €1.2B (May 2023), the largest GDPR fine ever.
- **Observed penalty range:** €290M – €530M — the highest individual penalties observed in the window.
- **Risk driver:** PrivacyEngine confirms "the largest penalties have stemmed from unlawful international data transfers." Three of the five largest fines ever involve transfers outside the EU. The TikTok decision establishes that transfer enforcement now applies to remote access scenarios, not just data storage [4][5][11][12].

### Rank 5: Data Protection by Design and by Default (Article 25 GDPR)

- **Relevant articles:** Article 25(1) (data protection by design); Article 25(2) (data protection by default).
- **Description:** Failure to build data protection into processing systems at the design stage, and failure to ensure default settings are the most privacy-protective (e.g., public-by-default child accounts, features designed without access-control safeguards).
- **Qualifying cases (3):** Meta €251M (€240M of €251M for Arts. 25(1) and 25(2) in the "View As" breach); TikTok €345M (Arts. 25(1)/(2) for public-by-default child accounts — €100M — and Family Pairing — €65M); Enel €79.1M (Art. 25 cited among violations).
- **Observed penalty range:** €65M – €240M (as component fines within larger packages).
- **Risk driver:** The DPC explicitly stated that "the failure to build in data protection requirements throughout the design and development cycle can expose individuals to very serious risks and harms" [8][16][17].

### Rank 6: Transparency / Information Obligations (Articles 12, 13, 14 GDPR)

- **Relevant articles:** Article 12 (transparent information, communication and modalities); Article 13 (information where data collected from data subject, including 13(1)(c) lawful basis and 13(1)(f) third-country transfers); Article 14 (information where data not obtained from data subject); Article 5(1)(a) (transparency principle).
- **Description:** Failure to provide data subjects with clear, specific, and easily understandable privacy information — including the lawful basis relied upon, categories of recipients, and third countries to which data is transferred. Vague wording ("public," "anyone," "third parties") and failure to name recipient countries are common deficiencies.
- **Qualifying cases (4):** TikTok €530M (Art. 13(1)(f) — €45M standalone); LinkedIn €310M (Arts. 13(1)(c), 14(1)(c)); TikTok €345M (Arts. 12(1), 13(1)(e) — €180M, the largest single component); Clearview €30.5M (Arts. 12(1), 14(1)-(2)).
- **Observed penalty range:** €45M – €310M (standalone or bundled).
- **Risk driver:** The EDPB's 2026 Coordinated Enforcement Framework focuses specifically on transparency and information obligations (Articles 12–14), signaling increased future enforcement [54].

### Rank 7: Processing Special Categories of Personal Data Without a Valid Exemption (Article 9 GDPR)

- **Relevant articles:** Article 9(1) (prohibition on processing sensitive data); Article 9(2) (exceptions); Article 4(14) (definition of biometric data).
- **Description:** Processing sensitive categories of personal data — including biometric data (e.g., facial recognition vectors/embeddings) and health/criminal data — without a valid Article 9(2) exception.
- **Qualifying cases (2):** Clearview AI €30.5M (Art. 9(1) biometric data violation — core finding); Uber €290M (special category and criminal data transferred, major aggravating factor).
- **Observed penalty range:** €30.5M – €290M (as standalone or aggravating factor).
- **Risk driver:** The AP's Clearview decision is the leading high-value standalone Article 9 case in the window; the Aena €10.04M fine further demonstrates that biometric processing without proper DPIA and minimization is a top regulatory priority [26][27][50].

### Rank 8: Children's Data Protection Failures (Articles 5, 12, 24, 25 GDPR; Recital 38)

- **Relevant articles:** Article 5(1)(a), (c), (f); Articles 12(1) and 13(1)(e) (transparency to children); Article 24(1) (controller responsibility); Articles 25(1) and (2) (design and default); Article 8 (child's consent).
- **Description:** Processing children's personal data without the enhanced protections required by the GDPR — public-by-default child accounts, inadequate age verification, design features exposing children to risk, and transparency information not adapted to children's comprehension.
- **Qualifying cases (1):** TikTok €345M (Sept 2023 — the entirety of the fine concerned children's data). Context: Meta/Instagram €405M (Sept 2022, outside window).
- **Observed penalty range:** €345M (qualifying window); €405M (context).
- **Risk driver:** Both of the largest children's-data fines in GDPR history exceeded €300M, demonstrating the extreme severity regulators attach to this area. The CMS tracker does not treat "children's data" as a separate violation category — these cases are classified under general principles, design/default, and transparency [20][21][22].

### Rank 9: Controller / Processor Obligations — Processor Oversight and Accountability (Articles 24, 28 GDPR)

- **Relevant articles:** Article 24(1) (controller responsibility); Article 28(1) (controllers may only engage processors providing sufficient guarantees; ongoing supervision); Article 28(3) (processor contract requirements); Article 5(2) (accountability).
- **Description:** Failure to exercise adequate oversight over processors and sub-processors (partner agencies, vendors), including failure to select/audit/monitor them, or executing processor contracts that do not reflect actual processing activities.
- **Qualifying cases (3):** Vodafone €45M (€15M for Art. 28(1) partner agency oversight); Enel €79.1M (Art. 28 contracts that did not reflect actual processing); TikTok €345M (Art. 24(1) findings for platform settings and DPIA failures).
- **Observed penalty range:** €15M – €79.1M.
- **Risk driver:** Processor-oversight failures are an emerging high-value enforcement area. The Heuking analysis emphasizes: "Art. 28 GDPR requires not just formal contracts but material, ongoing monitoring of service providers" [47][48][55].

### Rank 10: Failure to Fulfil Data Subject Rights (Articles 12, 15, 17, 20 GDPR)

- **Relevant articles:** Article 12(2) and 12(3) (facilitating and responding to requests); Article 15 (right of access); also Articles 17 (erasure), 20 (portability).
- **Description:** Failure to respond to, or properly facilitate, data subjects' requests to access their personal data (including ignoring access requests and failing to provide information about processing).
- **Qualifying cases (1):** Clearview AI €30.5M (failure to respond to two access requests and failure to facilitate the right of access — among bundled violations).
- **Observed penalty range:** €30.5M (bundled); standalone fines in this category are typically below €10M, but the EDPB's 2024 Coordinated Enforcement Framework sweep on the right of access and 2025 sweep on the right to erasure signal rising regulatory attention [26][27][56].
- **Risk driver:** While rarely the sole basis for high-value fines in the window, data subject rights failures are the fourth most common violation category overall and are a focus of coordinated EDPB enforcement.

---

## 4. Standard Penalty Ranges by Violation Type

| Violation Type | Core Articles | Observed Penalty Range (Qualifying Cases) | Notable Anchors |
|---|---|---|---|
| International transfers | 44–49 | €290M – €530M | TikTok €485M; Uber €290M; Meta €1.2B (2023 context) |
| Invalid legal basis | 6, 7 | €30.5M – €310M | LinkedIn €310M; Google €325M (ePrivacy) |
| General principles (incl. fairness) | 5 | €30.5M – €345M | TikTok €345M; Enel €79.1M |
| Data protection by design/default | 25 | €65M – €240M (components) | Meta €240M component of €251M |
| Security measures (TOMs) | 32, 5(1)(f) | €30M – €91M | Meta €91M; Vodafone €30M component |
| Transparency/information | 12, 13, 14 | €45M – €310M | TikTok €180M component; LinkedIn bundled |
| Special category data | 9 | €30.5M – €290M (aggravating) | Clearview €30.5M; Uber €290M (aggravating) |
| Children's data | 5, 12, 24, 25 | €345M | TikTok €345M; Meta/Instagram €405M (2022 context) |
| Processor oversight | 24, 28 | €15M – €79.1M | Vodafone €15M; Enel bundled |
| Data subject rights | 12, 15 | €30.5M (bundled) | Clearview bundled |
| Breach notification | 33, 34 | €3M – €8M (standalone components) | Meta €8M (Art. 33(3)); Meta €3M (Art. 33(5)) |
| DPIA failures | 35 | €10.04M | Aena €10.04M |

**Important context on penalty calculation:** Article 83 GDPR provides two tiers — Tier 1 (Art. 83(4)) up to €10 million or 2% of worldwide annual turnover for procedural violations; Tier 2 (Art. 83(5)) up to €20 million or 4% of total global turnover for serious violations including unlawful processing, invalid consent, processing special category data, violating data subject rights, and unlawful cross-border transfers. The term "undertaking" is equivalent to its meaning under Articles 101 and 102 TFEU — a whole corporate group can be treated as one undertaking, allowing total worldwide annual turnover to be used for calculating fines. Authorities weigh: gravity and nature of the infringement, intentional vs. negligent conduct, mitigation efforts, precautionary measures, recidivism, cooperation, data categories affected, and proactive breach notification [57][58][59].

---

## 5. Specific Compliance Gaps Enterprises Should Avoid

The following compliance gaps are derived directly from the enforcement actions analyzed above. Each gap includes the concrete failings that led to the fines and preventive controls.

### Gap 1: Unlawful Cross-Border Transfers Without Valid Safeguards

**Cases:** TikTok €530M; Uber €290M; Meta €1.2B (context).

**Concrete failings:**
- TikTok allowed remote access to EEA user data by personnel in China for ~1.5 years without demonstrating essentially equivalent protection; TRAs were high-level only and failed to consider specific circumstances of remote access; supplementary measures (encryption, "Project Clover") were general security measures that did not address government-access risks under Chinese law [11][12][13].
- Uber removed SCCs from its joint controllership agreement, arguing SCCs could not be used when processing falls directly under GDPR scope; the Dutch AP rejected this argument, finding Chapter V is complementary to Article 3 [23][24].
- Uber transferred data to US servers in a centralized IT infrastructure, including special category data (health, criminal records), with no EU-based alternative.

**Preventive controls:**
- Maintain a complete data-flow map identifying all third-country transfers, **including remote access by personnel located outside the EU** (which constitutes a "transfer" even if data is not stored there).
- Ensure a valid transfer mechanism is continuously maintained (adequacy decision, SCCs, BCRs); do not assume Article 3 extraterritoriality eliminates Chapter V obligations.
- Conduct substantively robust Transfer Risk Assessments that include detailed analysis of destination-country law measured against the European Essential Guarantees; merely preparing a TRA is insufficient — they must form a defensible basis for conclusions about essentially equivalent protection.
- Design supplementary measures that meaningfully address specific government-access risks (strong encryption with key separation, pseudonymisation, data minimization).
- Keep privacy policies up to date and transparently name all third-country destinations (Article 13(1)(f)).
- Revisit TRAs whenever local law changes or new enforcement guidance is issued [11][12][13][23][24][25].

### Gap 2: No Valid Lawful Basis for Advertising / Behavioural Profiling / Targeted Advertising

**Cases:** LinkedIn €310M; Google €325M (ePrivacy-adjacent); Meta €390M (context).

**Concrete failings:**
- LinkedIn relied on consent that was not freely given, sufficiently informed, specific, or unambiguous; legitimate interests were overridden by members' rights; contractual necessity was rejected for behavioral analysis and advertising [6][14][15].
- Google's cookie consent was not free (harder to refuse than accept — dark patterns) and not informed (users not told access depended on advertising cookie placement); Google also displayed Gmail ads without consent [31][32][33].
- Meta changed the legal basis from consent to contract for advertising, "forcing" users to accept terms (context case).

**Preventive controls:**
- Maintain a documented legal-basis register for every processing purpose; validate the basis is genuine before launch (consent must be freely given, specific, informed, unambiguous, and revocable; legitimate interests require a documented balancing test/LIA; contractual necessity must be truly necessary for the core service).
- Do not use "consent or pay" binary models without careful assessment (the European Commission fined Meta €200 million under the DMA in 2025 for its "Consent or Pay" model).
- Ensure no processing of third-party data for advertising occurs without a valid independent basis.
- Provide clear, transparent information about lawful bases in privacy notices (Articles 13/14).
- Conduct DPIAs for profiling activities and document necessity/proportionality analysis [6][14][15][31][32][33].

### Gap 3: Inadequate Technical and Organisational Security Measures (TOMs)

**Cases:** Meta €91M; Enel €79.1M; Vodafone €45M; Intesa Sanpaolo €31.8M; Meta €251M.

**Concrete failings:**
- Meta stored hundreds of millions of Facebook user passwords in plaintext since 2012 [7][18][19].
- Enel failed to implement measures to prevent unauthorized agents from exploiting easy access points into its information systems; at least 9,300 contracts were activated through illicit activity [36][37][38].
- Vodafone's "MeinVodafone" portal and hotline authentication processes allowed unauthorized third parties to retrieve eSIM profiles; overly broad partner access to customer systems [47][48][49].
- Intesa Sanpaolo's circular-access model permitted any Agribusiness manager to query the entire customer base without pre-authorization; alerts configured to allow repeated accesses to go undetected; no enhanced controls for high-risk clients (PEPs) [39][40][41].
- Meta's "View As" feature combined with the "Happy Birthday Composer" facility created a token vulnerability granting full access to ~29 million accounts [8][16][17].

**Preventive controls:**
- Implement encryption at rest and in transit as a baseline; never store passwords in plaintext — use salted hashing per NIST/NCSC/OWASP guidance.
- Design access controls on a need-to-know/least-privilege basis with role-based access control (RBAC), prior authorization for out-of-portfolio access, enhanced controls for high-risk individuals, automatic escalation to supervisors, and real-time anomaly detection.
- Conduct thorough due diligence of third parties/processors before engagement; implement continuous monitoring of vendor activities (not "set and forget").
- Build data protection into the design and development cycle (Article 25); test features for token/permission vulnerabilities before deployment.
- Maintain robust monitoring, logging, and alerting to detect unauthorized access [7][18][19][36][37][38][39][40][41][47][48][49].

### Gap 4: Breach Notification and Documentation Failures (Articles 33–34)

**Cases:** Meta €251M (Art. 33(3) €8M; Art. 33(5) €3M); Meta €91M (Arts. 33(1), 33(5)); Intesa Sanpaolo €31.8M; OpenAI €15M (€320K component).

**Concrete failings:**
- Meta failed to include all required information in its breach notification (nature of breach, DPO contact details, likely consequences, mitigation measures) [8][16][17].
- Meta failed to notify the DPC of the plaintext-password breach and failed to document the breaches [7][18][19].
- Intesa Sanpaolo's initial notification understated scope (9 vs. 3,573 data subjects), was incomplete as to breach perimeter, missed Article 33 deadlines, improperly downgraded the risk classification against ENISA methodology, and initially declined to notify affected customers individually until ordered to do so by the Garante [39][40][41].
- OpenAI failed to notify the Garante of a March 2023 data breach affecting 440 Italian users [10][45].

**Preventive controls:**
- Establish a breach-response plan with clear internal escalation, a 72-hour external notification capability, and pre-drafted notification templates containing all Article 33(3) elements.
- Document every breach (facts, effects, remedial actions) regardless of severity.
- Apply an objective, impact-focused risk assessment aligned with EDPB Guidelines 9/2022; do not downgrade risk based on the internal nature of the actor.
- Use the phased notification mechanism under Article 33 when scope is unclear, but do not use uncertainty to understate known facts.
- Notify data subjects under Article 34 without undue delay if any realistic possibility of high risk exists [8][16][17][39][40][41][45].

### Gap 5: Insufficient Oversight and Monitoring of Processors / Third-Party Partners (Article 28)

**Cases:** Vodafone €45M (€15M component); Enel Energia €79.1M (Art. 28 bundled); Enel €563,050 (March 2026, follow-up).

**Concrete failings:**
- Vodafone failed to adequately vet and monitor partner agencies; malicious employees in partner agencies committed fraud through fictitious contracts or contract changes; Vodafone granted overly broad access to partners into customer systems [47][48][49].
- Enel executed contracts with other entities that did not reflect actual personal data processing or include data controller obligations; failed to demonstrate effective control over telemarketing partners [36][37][38][60].

**Preventive controls:**
- Conduct thorough due diligence of third parties/processors before engagement (security posture, compliance history, fraud controls).
- Implement continuous monitoring of vendor activities; audit partner agencies on a scheduled basis; vet and periodically re-vet partner personnel with customer access.
- Establish clear contracts with binding data processing agreements (DPAs) and security expectations; enforce least-privilege access for partners.
- Incorporate third-party scenarios into incident response planning [47][48][49][55].

### Gap 6: Failure to Conduct Adequate Data Protection Impact Assessments (DPIAs) for High-Risk Processing (Article 35)

**Cases:** Aena €10.04M; OpenAI €15M (annulled).

**Concrete failings:**
- Aena deployed one-to-many (1:N) facial recognition systems at eight airports without a compliant DPIA; failed to identify or evaluate disadvantages, risks, or less invasive alternatives; stored biometric data up to two years, exceeding data minimization limits; continued processing despite negative reports from the AEPD. The AEPD imposed a temporary suspension of all biometric processing until a compliant DPIA is conducted [50][51][52].
- OpenAI produced its DPIA and LIA after the service launched; the Garante held legal basis cannot be applied retrospectively [10][45].

**Preventive controls:**
- Conduct DPIAs before launching any high-risk processing (biometrics, large-scale profiling, new technologies, AI training, systematic monitoring).
- Ensure DPIAs evaluate necessity, suitability, and proportionality, including identification of risks, disadvantages, and less invasive alternatives (e.g., traditional ID checks vs. 1:N facial recognition).
- Apply data minimization in system design; set appropriate retention limits.
- Obtain DPO sign-off on DPIAs; revisit DPIAs whenever processing changes materially or new guidance is issued (e.g., EDPB Opinion 11/2024 on facial recognition at airports) [50][51][52][45].

### Gap 7: Cookie Consent Violations and Dark Patterns (ePrivacy + GDPR Interface)

**Cases:** Google €325M; SHEIN €150M; Orange €50M (context).

**Concrete failings:**
- Google's consent was not free (harder to refuse than accept) and not informed (users not told cookie placement was a condition of accessing services) [31][32][33].
- SHEIN placed advertising cookies before obtaining consent; 85 cookies remained active after users refused; new third-party cookies were placed even after withdrawal; consent banners lacked essential information and clarity; confusing dual consent mechanisms [29][34][35].

**Preventive controls:**
- Implement a compliant Consent Management Platform (CMP) that blocks all non-essential cookies/trackers before consent is obtained.
- Design cookie banners with equally prominent "Accept" and "Reject" options; provide full purpose information before consent; ensure a genuine, one-click refusal mechanism.
- Honor user choices across all sessions/devices, including withdrawal of consent.
- Disclose all third parties that place cookies and the purposes of each; regularly audit third-party trackers.
- Treat cookie/ePrivacy compliance as a separate track from GDPR compliance given the inapplicability of the one-stop-shop [29][31][32][33][34][35].

### Gap 8: Failure to Honor Data Subject Rights and Transparency Obligations

**Cases:** LinkedIn €310M (transparency component); Clearview €30.5M (access request failures); context: Spotify €5M (Sweden, 2023); Uber €10M (Netherlands, 2024).

**Concrete failings:**
- LinkedIn failed to provide clear, transparent information about the lawful bases relied upon (Articles 13(1)(c), 14(1)(c)) [6][14][15].
- Clearview failed to respond to two access requests and failed to facilitate the right of access [26][27].

**Preventive controls:**
- Implement automated workflows for data subject requests covering access, rectification, erasure, restriction, portability, and objection, with documented SLAs (GDPR requires response within one month).
- Ensure erasure/deletion processes cover all systems, backups, and third-party processors.
- Maintain accurate, current, and complete privacy notices (Articles 13/14) that clearly identify lawful bases, purposes, third countries of transfer, retention periods, and data subject rights.
- Regularly test DSR fulfillment, including via EDPB Coordinated Enforcement Framework sweeps [56].

### Gap 9: Data Protection by Design and by Default Failures (Article 25)

**Cases:** Meta €251M (€240M); TikTok €345M (€165M combined); Meta €265M (2022 context).

**Concrete failings:**
- Meta's "View As" feature was designed without adequate safeguards against token exploitation; the design allowed unauthorized exposure of profile information, including sensitive categories [8][16][17].
- TikTok set child user profiles (ages 13–16) to public-by-default; the "Family Pairing" feature allowed unverified adults to pair with child accounts; dark patterns nudged children into privacy-intrusive settings [20][21][22].

**Preventive controls:**
- Embed privacy into system design from the outset; conduct privacy reviews at the architecture/design stage, not after launch.
- Apply privacy by default: the most privacy-friendly settings must be the default (private-by-default accounts for minors, minimal data collection, limited retention).
- Test new features for vulnerabilities before deployment; implement secure development lifecycle (SDLC) practices.
- Apply data minimization at the system level — collect and process only the personal data necessary for each purpose [8][16][17][20][21][22].

### Gap 10: Governance, Accountability, and Cooperation Failures

**Cases:** Intesa Sanpaolo €31.8M; Enel €79.1M; OpenAI €15M (€5.68M for failure to comply with corrective measures); TikTok €530M (inaccurate information provided to DPA).

**Concrete failings:**
- Intesa Sanpaolo's systemic design of access controls failed to detect suspicious insider behavior for over two years; remedial measures were only implemented after regulatory intervention; communication to affected customers only occurred after a Garante order [39][40][41].
- OpenAI failed to comply with corrective measures imposed in 2023 (the temporary ban and required corrective actions) [10][45].
- TikTok initially told the DPC it did not store EEA user data on servers in China, but disclosed in April 2025 that limited EEA data had in fact been stored there — the DPC stated it received inaccurate information and is considering further action [11][12].

**Preventive controls:**
- Establish a formal accountability framework: maintain Records of Processing Activities (RoPA), assign clear ownership (DPO, privacy office), and document compliance decisions (LIAs, DPIAs, TRA records) before incidents occur.
- Implement insider-risk and access-governance programs: role-based access control, least privilege, need-to-know policies, real-time anomaly detection.
- Cooperate fully and promptly with supervisory authorities: respond to information requests within deadlines, provide complete and accurate information, and avoid understating breach scope. The TikTok case shows that providing inaccurate information to a DPA can trigger further action.
- Treat supervisory authority corrective orders as mandatory compliance obligations; implement and evidence remediation within deadlines [39][40][41][45][11][12].

### Gap 11: Unlawful Profiling and Processing Without Legal Basis in Corporate Reorganizations

**Cases:** Intesa Sanpaolo (Isybank) €17.6M.

**Concrete failings:**
- Intesa transferred ~2.4 million customer accounts to its digital bank subsidiary based on profiling criteria (age, digital channel familiarity, absence of investment products, low balances) without an appropriate legal basis.
- Customers were not properly informed — the notice was placed in the app's archive section without push notifications or text messages.
- The transfer forced changes including new IBANs, lack of physical branches, and mandatory mobile app access.
- The Garante emphasized the processing was unlawful because customers could not have reasonably anticipated this activity given the circumstances and information provided [42][43][44].

**Preventive controls:**
- Identify and document a valid legal basis before any new processing, including consumer data transfers between affiliates/subsidiaries.
- Provide clear, action-oriented customer notices for material changes in processing (account transfers, controller changes, new data uses); do not bury notices in app archives without direct communication.
- Conduct DPIAs for large-scale profiling and segmentation of customers for migration to new services [42][43][44].

### Gap 12: AI Training and Generative AI Without Valid Legal Basis (Emerging Area)

**Cases:** OpenAI €15M (annulled on jurisdictional grounds, but the underlying theory remains instructive).

**Concrete failings:**
- OpenAI trained ChatGPT without an adequate legal basis prior to public launch; DPIA and LIA produced after launch were not decisive (legal basis cannot be applied retrospectively).
- Failure to meet transparency/information obligations toward users; inaccurate processing of personal information; absence of age verification mechanisms; failure to notify the March 2023 data breach [10][45][46].

**Preventive controls:**
- Establish and document a lawful basis for AI training before processing personal data; conduct DPIAs and LIAs before deployment, not after.
- Implement effective age verification mechanisms where services may be accessed by minors.
- Provide clear, accessible information to users about how their data is used for AI training, including rights to object, rectify, and delete.
- Monitor EDPB guidance and prepare for EU AI Act high-risk requirements (penalties up to €35 million or 7% of global turnover effective 2 August 2026) [10][45][46][61].

---

## 6. Key Enforcement Trends and Strategic Implications

### 6.1 Enforcement Concentration and Collection Realities

Ireland's DPC has issued approximately €4.04 billion in cumulative fines (~57% of all fine value), yet only ~€20 million (0.5%) has actually been collected as of the 2026 reports, as most major fines are under appeal. However, companies almost always implement corrective orders despite appealing headline amounts — Meta localised EU data infrastructure, LinkedIn rewrote consent flows within three months, and Vodafone paid its fine in full and implemented system improvements [2][3][48][62].

### 6.2 Geographic Breadth and Sector Expansion

While big tech remains the primary target (8 of the 10 largest fines were imposed on US-based companies), enforcement has expanded into financial services (Intesa Sanpaolo €49.4M across two fines), energy (Enel €79.1M), telecommunications (Vodafone €45M), and state-owned enterprises (Aena €10.04M). Spain's AEPD imposed 325 fines totaling ~€48.1 million in 2025 — the highest enforcement amount in its history, with 11 fines exceeding €1 million [50][63][64].

### 6.3 Repeat Offenders Face Escalating Penalties

Recidivism is a significant aggravating factor. Google's CNIL fines escalated from €100M (2020) to €150M (2021) to €325M (2025). Uber's Dutch AP fines escalated from €600,000 (2018) to €10M (2023) to €290M (2024). Intesa Sanpaolo's Garante fines referenced three prior enforcement actions. Enterprises should treat any prior DPA interaction as a signal that future violations will be penalized more severely [23][31][32][33][39][40][41].

### 6.4 Coordinated Enforcement and New Legal Frameworks

The EDPB's Coordinated Enforcement Framework (CEF) is conducting annual cross-EU sweeps — 2024 on the right of access, 2025 on the right to erasure, 2026 on transparency obligations (Articles 12–14). The EU AI Act's high-risk provisions become enforceable 2 August 2026 with penalties up to €35 million or 7% of global turnover — higher than the GDPR's €20 million or 4%. The Digital Omnibus (proposed 19 November 2025) represents the largest GDPR reform since 2018 [54][61][65].

### 6.5 Procedural Annulments: A Cautionary Note

Two of Europe's most high-profile GDPR fines were struck down within a single week in March 2026: the Luxembourg Administrative Court annulled Amazon's €746 million fine on procedural grounds (CNPD did not properly assess intentionality/negligence or weigh a more lenient measure; case remanded), and the Court of Rome annulled Italy's €15 million OpenAI fine on jurisdictional grounds (one-stop-shop). These annulments underscore that DPAs must follow rigorous procedural methodology — but they do not overturn the underlying substantive violations, which remain instructive for compliance [9][10][66].

---

## 7. Conclusion

The August 2023 – August 2026 enforcement period establishes several clear messages for enterprises:

1. **Cross-border transfers are the highest financial risk** in GDPR enforcement, with fines up to €530 million for failures to verify essentially equivalent protection — including for remote access scenarios.
2. **Legal basis is the most frequent enforcement theory** across all fine sizes, and behavioral advertising on the basis of "contractual necessity" or weak consent is unlawful.
3. **Security failures produce the broadest geographic distribution** of high-value fines, and regulators expect encryption, least-privilege access controls, anomaly detection, and continuous processor oversight as baseline measures.
4. **Design choices are now enforcement targets**: dark patterns, public-by-default settings for children, and authentication flaws that enable unauthorized access all attracted fines in the hundreds of millions.
5. **DPAs expect proactive, documented compliance** — DPIAs before high-risk processing, TRAs before transfers, breach documentation, and full cooperation during inquiries. Retrospective compliance documentation is not a defense.
6. **The enforcement ecosystem is expanding** beyond big tech into financial services, energy, telecommunications, and public-sector entities, with coordinated EDPB sweeps and new frameworks (EU AI Act, DMA) creating overlapping obligations.

For privacy risk assessments, the practical takeaway is that enterprises should treat the GDPR's accountability principle (Article 5(2)) as the foundational requirement: document every compliance decision before processing begins, verify that legal bases are genuine and specific, ensure security measures are proportionate to risk, and maintain the ability to demonstrate all of the above to supervisory authorities on demand.

---

## Sources

[1] CMS GDPR Enforcement Tracker Report 2025 — Executive Summary: https://cms.law/en/media/international/files/publications/publications/gdpr-enforcement-tracker-report-may-2025?v=8

[2] UniConsent — GDPR Enforcement and Fines 2026: Business Categories, Fines, Trends: https://www.uniconsent.com/blog/gdpr-enforcement-fines-2026

[3] DLA Piper GDPR Fines and Data Breach Survey: January 2026: https://www.dlapiper.com/en-us/insights/publications/2026/01/dla-piper-gdpr-fines-and-data-breach-survey-january-2026

[4] PrivacyEngine — GDPR Statistics Worldwide 2026: Fines, Breaches & Trends: https://www.privacyengine.io/gdpr-statistics-worldwide-2026

[5] Maya Data Privacy — GDPR Fines 2024–2025: The 10 Most Expensive Penalties: https://www.mayadataprivacy.com/post/gdpr-fines-2024-2025-top-10-penalties-anonymization

[6] Irish Data Protection Commission — Press Release: DPC fines LinkedIn Ireland €310 million: http://www.dataprotection.ie/en/news-media/press-releases/irish-data-protection-commission-fines-linkedin-ireland-eu310-million

[7] Irish Data Protection Commission — Press Release: DPC announces 91 million euro fine of Meta: https://www.dataprotection.ie/en/news-media/press-releases/DPC-announces-91-million-fine-of-Meta

[8] Irish Data Protection Commission — Press Release: DPC fines Meta €251 Million: http://www.dataprotection.ie/en/news-media/press-releases/irish-data-protection-commission-fines-meta-eu251-million

[9] CNPD Luxembourg — Amazon decision: https://cnpd.public.lu/en/actualites/national/2025/03/amazon-decision.html

[10] Cross-Border Data Forum — Generative AI and GDPR Enforcement in Europe: https://www.crossborderdataforum.org/generative-ai-and-gdpr-enforcement-in-europe-a-lot-of-noise-one-fine-zero-survivors

[11] Irish Data Protection Commission — Press Release: DPC fines TikTok €530 million: https://www.dataprotection.ie/en/news-media/latest-news/irish-data-protection-commission-fines-tiktok-eu530-million-and-orders-corrective-measures-following

[12] Simmons & Simmons — International data transfers: implications of the €530m fine on TikTok: https://www.simmons-simmons.com/en/publications/cmocwmjy3015eus3gv4sa4fq8/international-data-transfers-implications-of-the-530m-fine-on-tiktok

[13] Maynard Nexsen — Irish DPC Fines TikTok Over EEA Data Transfers to China: https://www.maynardnexsen.com/publication-irish-data-protection-commission-fines-tiktok-over-eea-data-transfers-to-china

[14] Hunton — Irish Regulator Fines LinkedIn 310 Million Euros for GDPR Violations: https://www.hunton.com/privacy-and-cybersecurity-law-blog/irish-regulator-fines-linkedin-310-million-euros-for-gdpr-violations

[15] Goodwin — Irish DPC Fines LinkedIn €310M for GDPR Violations: https://www.goodwinlaw.com/en/insights/publications/2024/11/insights-finance-dpc-irish-data-protection-commission-fines-linkedin

[16] GDPRhub — DPC (Ireland) - Meta "View-as" feature: https://gdprhub.eu/index.php?title=DPC_%28Ireland%29_-_Meta_%22View-as%22_feature

[17] Hunton — Irish Regulator Fines Meta 251 Million Euros Following Investigation into Data Breach: https://www.hunton.com/privacy-and-cybersecurity-law-blog/irish-regulator-fines-meta-251-million-euros-following-investigation-into-data-breach

[18] Clyde & Co — Meta fined €91 million in Ireland due to a lack of security in respect of users' passwords: https://www.clydeco.com/en/insights/2024/10/meta-fined-%E2%82%AC91-million-in-ireland-due-to-a-lack-of

[19] Keepabl — DPC 91m fine Meta plain text password: https://keepabl.com/news/dpc-91m-fine-meta-plain-text-password

[20] Matheson — DPC Fines TikTok €345m for GDPR Violations Concerning Children's Data: https://www.matheson.com/insights/dpc-fines-tiktok-345m-for-gdpr-violations-concerning-childrens-data

[21] Baker Botts — TikTok's €345 Million Fine for GDPR Violations on Child Data Protection: https://www.bakerbotts.com/thought-leadership/publications/2023/november/tiktoks-345-million-fine-for-gdpr-violations-on-child-data-protection

[22] Irish Data Protection Commission — Press Release: DPC announces €345 million fine of TikTok: http://www.dataprotection.ie/en/news-media/press-releases/DPC-announces-345-million-euro-fine-of-TikTok

[23] Autoriteit Persoonsgegevens (Dutch DPA) — Dutch DPA imposes a fine of 290 million euro on Uber: https://www.autoriteitpersoonsgegevens.nl/en/current/dutch-dpa-imposes-a-fine-of-290-million-euro-on-uber-because-of-transfers-of-drivers-data-to-the-us

[24] GDPRhub — AP (The Netherlands) - Uber: https://gdprhub.eu/index.php?title=AP_%28The_Netherlands%29_-_Uber

[25] European Law Blog — Into the Data Transfer Thicket: The Dutch Uber Decision: https://europeanlawblog.eu/1xjmngct

[26] Autoriteit Persoonsgegevens — Decision fines and orders subject to a penalty Clearview (official PDF): https://www.autoriteitpersoonsgegevens.nl/en/system/files?file=2024-09%2FDecision+fines+and+orders+subject+to+a+penalty+Clearview.pdf

[27] EDPB — Dutch Supervisory Authority imposes a fine on Clearview: https://www.edpb.europa.eu/news/dutch-supervisory-authority-imposes-a-fine-on-clearview-because-of-illegal-data-collection-for_en

[28] Hunton — Dutch Regulator Fines Clearview AI 30.5 Million Euros: https://www.hunton.com/privacy-and-cybersecurity-law-blog/dutch-regulator-fines-clearview-ai-30-5-million-euros

[29] CNIL — Cookies placed without consent: SHEIN fined 150 million euros: https://www.cnil.fr/en/cookies-placed-without-consent-shein-fined-150-million-euros-cnil

[30] CNIL — Cookie regulation: the CNIL is continuing the action plan initiated in 2019 and has imposed two fines on SHEIN and GOOGLE: https://www.cnil.fr/en/cookie-regulation-cnil-continuing-action-plan-initiated-2019-and-has-imposed-two-fines-shein-and

[31] CNIL — Cookies and advertisements inserted between emails: Google fined 325 million euros: https://www.cnil.fr/en/cookies-and-advertisements-inserted-between-emails-google-fined-325-million-euros-cnil

[32] Goodwin — CNIL Imposes Record €325 Million Fine on Google: https://www.goodwinlaw.com/en/insights/publications/2025/09/insights-practices-dpc-cnil-imposes-record-325-million-fine

[33] EDPB — GOOGLE fined 325 000 000 EUR by the CNIL: https://www.edpb.europa.eu/news/french-sa-cookies-and-advertisements-inserted-between-emails-google-fined-325-000-000-eur-by_en

[34] Reflectiz — Shein Handed €150 Million Fine Over Cookie Consent Violations: https://www.reflectiz.com/blog/shein-privacy-fine

[35] Browne Jacobson — Cookie compliance crackdown: SHEIN fined €150 million by CNIL: https://www.brownejacobson.com/insights/retail-law-roundup-september-2025/cookie-compliance-crackdown-shein-fined-%E2%82%AC150-million-by-cnil

[36] GDPR Enforcement Tracker — ETid-2306: GDPR fine against Enel Energia SpA (Italy, 2024): https://www.enforcementtracker.com/ETid-2306

[37] Orsingher — Italian DPA fines Enel Energia for telemarketing: https://orsingher.com/en/data-protection-italian-dpa-fines-enel-energia-for-telemarketing

[38] Reuters — Italy regulator fines Enel unit 79 million euros for telemarketing abuses: https://www.reuters.com/business/energy/italy-regulator-fines-enel-unit-79-million-euros-telemarketing-abuses-2024-02-29

[39] DataGuidance — Italy: Garante fines Intesa Sanpaolo €31M for unlawful data access: https://www.dataguidance.com/news/italy-garante-fines-intesa-sanpaolo-eu31m-unlawful

[40] Securiti.ai — €49.4 Million in Lessons: What Intesa Sanpaolo's Twin GDPR Fines Mean for Financial Institutions: https://securiti.ai/intesa-sanpaolo-gdpr-fines-lessons-financial-institutions

[41] DSN Group — The Italian DPA's Fine Against Intesa Sanpaolo: Lessons for Access Management and Data Breach Handling: https://www.dsn-group.com/privacy-notes/the-italian-dpas-fine-against-intesa-sanpaolo-lessons-for-access-management-and-data-breach-handling-2959622

[42] DataGuidance — Italy: Garante fines Intesa Sanpaolo €17.6M for unlawful processing of data: https://www.dataguidance.com/news/italy-garante-fines-intesa-sanpaolo-eu176m-unlawful

[43] ICLG — Italian banking giant fined over data protection lapses: https://iclg.com/news/23722-italian-banking-giant-fined-over-data-protection-lapses

[44] DSN Group — Unlawful Profiling and Poor Transparency: Key Takeaways from the Garante's Fine Against Intesa Sanpaolo: https://www.dsn-group.com/privacy-notes/unlawful-profiling-and-poor-transparency-key-takeaways-from-the-garantes-fine-against-intesa-sanpaolo-0259296

[45] Lewis Silkin — OpenAI faces €15 million fine as the Italian Garante strikes again: https://www.lewissilkin.com/en/insights/2025/01/14/openai-faces-15-million-fine-as-the-italian-garante-strikes-again-102jtqc

[46] DataGuidance — Italy: Garante fines OpenAI €15M for GDPR non-compliance: https://www.dataguidance.com/news/italy-garante-fines-openai-eu15m-gdpr-non-compliance

[47] BfDI (German DPA) — BfDI imposes fines on Vodafone (press release): https://www.bfdi.bund.de/SharedDocs/Pressemitteilungen/EN/2025/06_Geldbu%C3%9Fe-Vodafone.html

[48] Rescana — Vodafone's €45 Million GDPR Penalty: Critical Lessons in Third-Party Risk Management and IAM: https://www.rescana.com/post/vodafone-s-45-million-gdpr-penalty-critical-lessons-in-third-party-risk-management-and-iam-for-cis

[49] GDPRhub — BfDI (Germany) - Vodafone: https://gdprhub.eu/index.php?title=BfDI_%28Germany%29_-_Vodafone

[50] CMS — Data protection laws and GDPR enforcement in Spain (GDPR Enforcement Tracker Report 2026): https://cms.law/en/int/publication/GDPR-Enforcement-Tracker-Report/spain

[51] DataGuidance — Spain: AEPD fines AENA €10.04M for GDPR violations in biometric facial recognition program: https://www.dataguidance.com/news/spain-aepd-fines-aena-eu10043002-gdpr-violations

[52] GDPRhub — AEPD (Spain) - EXP202304532 (Aena): https://gdprhub.eu/index.php?title=AEPD_%28Spain%29_-_EXP202304532&mtc=today

[53] Scrut.io — Avoiding GDPR fines in 2025: Enforcement trends and tips: https://www.scrut.io/hub/gdpr/gdpr-fines-penalties-us-eu-guide

[54] CMS GDPR Enforcement Tracker Report 2026 — Numbers and Figures: https://cms.law/en/int/publication/GDPR-Enforcement-Tracker-Report/numbers-and-figures

[55] Heuking — EUR 45 million GDPR-fine against Vodafone — what are the conclusions for EU companies: https://www.heuking.de/en/news-events/newsletter-articles/detail/eur-45-million-gdpr-fine-against-vodafone-what-are-the-conclusions-for-eu-companies.html

[56] EDPB Annual Report 2024: https://www.edpb.europa.eu/system/files/2025-04/edpb-annual-report-2024_en.pdf

[57] gdpr-info.eu — Fines / Penalties: https://gdpr-info.eu/issues/fines-penalties

[58] GDPR.eu — What are the GDPR Fines?: https://gdpr.eu/fines

[59] AGPLAW — How GDPR Fines are Calculated when an EU Company is Found in Breach: https://www.agplaw.com/how-gdpr-fines-are-calculated-when-an-eu-company-is-found-in-breach

[60] DataGuidance — Italy: Garante fines Enel Energia €563,050 for unlawful telemarketing: https://www.dataguidance.com/news/italy-garante-fines-enel-energia-eu563050-unlawful

[61] Kiteworks — GDPR Enforcement Trends: €7.1 Billion in Fines and Rising: https://www.kiteworks.com/gdpr-compliance/gdpr-fines-data-privacy-enforcement-2026

[62] PrivacyTerms.io — Biggest GDPR Fines Ever: Top 50 Ranked: https://privacyterms.io/biggest-gdpr-fines-all-time

[63] Cornerstone Counsel — Record GDPR Fines in Spain in 2025: 325 Sanctions Totalling an Unprecedented €48.1 Million: https://cornerstonecounsel.es/record-gdpr-fines-in-spain-in-2025-325-sanctions-totalling-an-unprecedented-e48-1-million

[64] DLA Piper GDPR Fines and Data Breach Survey: January 2025: https://www.dlapiper.com/en-us/insights/publications/2025/01/dla-piper-gdpr-fines-and-data-breach-survey-january-2025

[65] SecurityWall — GDPR Fines Tracker 2026: https://securitywall.co/blog/gdpr-fines-tracker-2026

[66] OneTrust DataGuidance — Luxembourg Jurisdictions: https://www.dataguidance.com/jurisdictions/luxembourg
