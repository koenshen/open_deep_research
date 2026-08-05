# Comprehensive Research Report: Client-Facing AI Portfolio-Management and Financial-Planning Copilots Launched by U.S. and Canadian Banks and Broker-Dealers (January 2023 – August 2026)

## Executive Summary

This research identifies U.S. and Canadian banks and broker-dealers that have publicly launched (production, not pilot) client-facing AI portfolio-management or financial-planning "copilots" between January 2023 and August 5, 2026. The research focuses exclusively on tools that are directly accessible to end clients (retail investors, wealth management clients, institutional clients) as opposed to advisor-facing or internal employee productivity tools. A total of **six distinct products across five institutions** were identified as meeting the criteria, with several additional institutions launching notable client-facing AI tools that are adjacent to the scope.

| Institution | Product Name | Launch Date | Customer Tier | Geography |
|---|---|---|---|---|
| JPMorgan Chase | IndexGPT | May 2024 | Institutional | U.S. (global via Bloomberg/Vida) |
| Charles Schwab | Portfolio Insights | May 5, 2026 | Mass retail (self-directed) | U.S. |
| Charles Schwab | AI Assistants (Chat/Voice) | June 2026 | Mass retail | U.S. |
| Citi | Portfolio Intelligence | April 9, 2026 | UHNW (Private Bank), expanding to all Wealth | North America, global expansion |
| Citi | Citi Sky | April 22, 2026 (unveil); Summer 2026 (rollout) | Mass affluent (Citigold) | U.S. (English/Spanish, scaling to 100+ languages) |
| BMO Financial Group | My Financial Progress | July 10, 2025 | Mass retail | Canada (English/French) |
| BMO Financial Group | AI News and Market Summaries | 2025 | Self-directed investors | Canada (English/French) |

**Note:** PortfolioPilot (Global Predictions Inc.) is an SEC-registered investment advisor operating an AI-powered financial advisor platform, but it is not a bank or broker-dealer and is therefore outside the primary scope, though it is included as a notable fintech entry.

---

## 1. JPMorgan Chase – IndexGPT

### 1.1 Product Overview

**Product Name:** IndexGPT  
**Launch Date:** May 15, 2024 (initially for institutional clients; expanded in July 2024)  
**Official Description:** IndexGPT is a client-facing AI-powered thematic investment basket tool that uses OpenAI's GPT-4 model to generate keywords for investment themes, combined with a separate NLP model to scan news articles and identify relevant companies. It largely automates the creation of thematic indexes, allowing institutional clients to invest in emerging trends through structured products like swaps or notes. [1][2][3]

### 1.2 Customer Tier

IndexGPT is **targeted at institutional clients**. Multiple sources confirm this: Bloomberg reported it is "targeted at institutional clients, IndexGPT offers exposure through structured products like swaps or notes." [2] Pensions & Investments stated: "J.P. Morgan Chase launches IndexGPT for institutional clients." [4] The indexes are aimed at institutional clients seeking exposure to emerging trends through structured products. [5] Rui Fernandes, head of market trading structuring at JPMorgan, described the tool as designed for momentum investors with shorter holding horizons. [6]

### 1.3 Geography & Languages Supported

IndexGPT was launched by JPMorgan Chase (U.S.-based) and is available to institutional clients globally through Bloomberg and Vida platforms. [7] JPMorgan has a global presence across asset management ($4.3 trillion AUM as of March 31, 2026) and wealth management ($7 trillion in client assets). [8] Specific languages supported have not been publicly disclosed.

### 1.4 Core AI Stack

**Foundation Model:** IndexGPT is powered by **OpenAI's GPT-4 model**. Multiple sources confirm this: PYMNTS reported on May 3, 2024 that IndexGPT "uses OpenAI's GPT-4 model." [9] Bloomberg confirmed IndexGPT is a "new range of thematic investment baskets created with the help of OpenAI's GPT-4 model." [2] InvestmentNews stated JPMorgan "taps ChatGPT for new thematic investment suite" powered by OpenAI's GPT-4 model. [5]

**Two-Stage Processing:** The system operates in two stages: (1) GPT-4 generates keywords associated with an investment theme (e.g., cloud computing, esports, cybersecurity), with Rui Fernandes stating "the GPT model generates more than twice as many keywords compared to previous software, creating a superior representation of the theme"; [5][6] (2) The generated keywords are fed into a separate NLP model that scans news articles to identify companies in the theme space, creating automated thematic indexes. [2][9]

**Broader AI Infrastructure:** JPMorgan's broader AI ecosystem includes **LLM Suite** (proprietary generative AI platform connecting models from OpenAI and Anthropic, used by 200,000+ employees daily), [10][11] **OmniAI** (enterprise ML platform for fraud detection), [12] **DocLLM** (proprietary layout-aware LLM for document intelligence), [13] **Connect Coach** (AI advisor copilot for 10,000+ financial advisors, built on federated AI architecture using FDC3, MCP, A2A protocols), [14] and **Fence guardrail framework** (data-driven approach using synthetic data to identify and mitigate LLM vulnerabilities). [15]

### 1.5 Safety & Compliance Measures

**Fence Guardrail Framework:** Announced April 2, 2026, this JPMorgan-developed framework is a "data-driven approach to proactively identify, test, and mitigate vulnerabilities in large language models (LLMs) such as hallucinations, topic drift, and prompt injection." It uses "synthetic data generation to create custom, use case–specific guardrails" and is already deployed across "simple Q&A and advanced search applications." Internal benchmarks "indicate it surpasses existing industry solutions in safety and reliability." [15]

**Data Security:** Teresa Heitsenrether, JPMorgan's chief data and analytics officer, stated: "Since our data is a key differentiator, we don't want it being used to train the model. By designing the LLM Suite as a controlled portal to external models, JPMorgan can leverage AI technology without compromising its data security." [10][12]

**Regulatory Framework:** JPMorgan filed a trademark application for IndexGPT on May 11, 2023 with the USPTO, covering three international classes: advertising/business, insurance/financial, and computer/scientific services. [16][17] The firm operates a **TrustAI Center of Excellence** focused on "AI Trust, Transparency & Safety" to "enhance trust in financial services by providing clear, understandable, and recourse-based AI-driven decision-making processes." [18]

### 1.6 Integrations

IndexGPT is available on **Bloomberg and Vida platforms**. [7] Vida is J.P. Morgan's cross-asset portfolio solutions platform providing "real-time analytics" and cross-asset, multi-product solutions. [19] The product is accessible through **J.P. Morgan Markets** (digital platform for institutional clients offering Research & Insights, Data & Analytics, Portfolio Solutions, Pricing & Execution, and Post Trade services) and **SI360** (structured investment platform offering real-time pricing, analytics, calendar management, and in-platform education). [19]

### 1.7 Access & Pricing

**Customer Tier:** Institutional clients.  
**Access Channels:** Bloomberg terminal, Vida platform, J.P. Morgan Markets, SI360. No dedicated mobile app has been publicly announced.  
**Pricing Model:** Not publicly disclosed. Institutional clients gain exposure via structured products (swaps, notes). [2][5][6] JPMorgan's broader AI strategy targets $1.5–$2.0 billion in annual AI-driven business value. [20]

### 1.8 KPIs

**IndexGPT-Specific:** JPMorgan has not publicly disclosed specific adoption numbers, user satisfaction scores, ROI metrics, or AUM influenced specifically for IndexGPT.

**Broader JPMorgan AI KPIs (relevant context):** Over 450 AI use cases in production (expanding to 1,000 by 2026), [21] $1.5–$2.0 billion in annual AI-driven business value targeted, [20] 200,000+ employees using LLM Suite daily, [11] 35% increase in AI/ML value delivered in 2024, [22] $17 billion technology budget in 2024 (with $1.3 billion for AI), [23] 2,000+ AI specialists (targeting 5,000), [20] #1 on Evident AI Index for four consecutive years (2022-2025). [24] Connect Coach: 10,000+ users, ~80% active, answered almost 1 million questions, 30% more client coverage, 15% increase in wallet share. [14]

### 1.9 Links

- Official Press Release: [Pensions & Investments - J.P. Morgan Chase launches IndexGPT](https://www.pionline.com/money-management/jp-morgan-chase-launches-indexgpt) [4]
- Product Coverage: [Bloomberg - JPMorgan Unveils IndexGPT in Next Wall Street Bid to Tap AI Boom](https://www.bloomberg.com/news/articles/2024-05-03/jpmorgan-unveils-indexgpt-in-next-wall-street-bid-to-tap-ai-boom) [2]
- Independent Article: [InvestmentNews - JPMorgan taps ChatGPT for new thematic investment suite](https://www.investmentnews.com/etfs/jpmorgan-taps-chatgpt-for-new-thematic-investment-suite/252966) [5]

---

## 2. Charles Schwab – Portfolio Insights

### 2.1 Product Overview

**Product Name:** Portfolio Insights  
**Launch Date:** May 5, 2026 (rolled out to all self-directed U.S. retail clients by end of May 2026)  
**Official Description:** Schwab's first generative AI capability for retail investor clients provides personalized, educational summaries that combine portfolio performance, relevant market news, and curated commentary from the Schwab Center for Financial Research (SCFR) into a single view. The tool generates a narrative snapshot of the portfolio's daily change, a recap of recent news on top S&P 500 equity movers affecting the portfolio, and snippets of Schwab expert content. [25][26][27]

### 2.2 Customer Tier

**Mass retail (self-directed investors).** The tool is designed to extend personalized insights once reserved for wealthier investors to a broader retail audience. CEO Rick Wurster stated: "In order to have a dedicated relationship, you have to have $1 million at Schwab. Using AI, we'll be able to offer them some of the same personalized insights that we're giving every day in our branches and in our dedicated relationships. There's a vast majority of our clients don't have $1 million. That'll be a huge unlock." [28][29]

### 2.3 Geography & Languages Supported

**U.S. only.** Available to all self-directed U.S. retail clients. [25][26][27] Languages: English only (based on disclosed information).

### 2.4 Core AI Stack

**LLM Providers:** Schwab has not publicly disclosed the specific LLM provider for Portfolio Insights. However, job postings for Schwab's AI.x team mention "Experience with proprietary or open-source LLMs (e.g., Gemini, Claude, OpenAI) and deploying LLM-powered applications to production," suggesting a multi-model approach. [30]

**Vector Databases & Orchestration:** Job postings mention "Exposure to agent orchestration frameworks, model context protocols (MCP), vector databases, embeddings, or knowledge retrieval systems." [31]

**Internal AI Team:** Schwab's AI Strategy & Transformation team (AI.x) is responsible for AI deployment. The team includes a Senior Responsible AI Researcher role focused on "bias detection, developing guardrails, monitoring AI systems, and collaborating with cross-functional teams." [30]

**Data Infrastructure:** Schwab is leveraging over 8,000 technologists to accelerate AI deployment. [31] Industry experts noted that "the effectiveness of these AI initiatives depends heavily on the robustness of a firm's underlying data architecture." [31]

### 2.5 Safety & Compliance Measures

The tool is explicitly designed for **informational and educational purposes only, not investment advice**. The official Portfolio Insights Disclosure states: "Portfolio Insights is a generative AI feature designed to provide narrative summary of your Portfolio's Day Change, recap of recent news on up to five S&P 500 equity movers, and snippets of Schwab expert content. Insights are not offers, solicitations, recommendations, or investment advice." [32]

The disclosure also warns: "Generative AI outputs are sometimes inaccurate, contain hallucinated or incomplete information, and can be delayed or out-of-date. Insights do not update automatically; you can refresh by minimizing and reopening the tab." [32]

The capability is covered by Schwab's privacy, security, and data standards. [25] The disclosure notes that Portfolio Insights does not cover all securities or positions, may exclude certain asset types (e.g., mutual funds, external accounts), and relies on select news sources. [32]

### 2.6 Integrations

Portfolio Insights is integrated into **Schwab.com and the Schwab Mobile App** on the Account Summary page. [25][26][27] It pulls data from Schwab's portfolio accounting systems, the Schwab Center for Financial Research (SCFR), and third-party market news sources. The tool draws on data from Schwab's broader ecosystem, which includes the Schwab Knowledge Assistant (internal ChatGPT-like tool for employees, achieving 90% adoption growth in 2024). [33]

### 2.7 Access & Pricing

**Free** to all self-directed U.S. retail clients. No additional charge. [25][26][27]  
**Access Channels:** Schwab.com (desktop) and Schwab Mobile App. [25]

### 2.8 KPIs

**Pre-Launch Survey:** A Schwab survey of nearly 1,000 retail clients (conducted January 20-27, 2026) found: nearly 70% of retail clients believe AI can play a meaningful role in investing when paired with human expertise; over 60% of respondents expressed interest in using AI. [25][26][27]

**Broader Schwab AI KPIs:** The AI Service Assistant transcribes approximately 60,000 daily client interactions. [34] The Knowledge Assistant achieved 90% employee adoption growth in 2024, leading to a 2-minute reduction in handling time per complex call, estimated savings of 140,000 monthly hours and over $10 million annually in labor costs. [33] Schwab credits AI for a 25% reduction in cost per account over the past decade. [33] Record Q1 2026 results: 1.3 million new brokerage accounts, $158 billion in core net new assets, 46% increase in managed investing net flows. Record total client assets of $11.77 trillion (up 19% YoY). [34] Schwab raised its 2026 revenue growth guidance to 14-15% (up from 9.5-10.5%). [35]

### 2.9 Links

- Official Press Release: [Charles Schwab Launches AI-Powered Capability That Helps Investors Understand Portfolio Performance and Market Activity](https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Launches-AI-Powered-Capability-That-Helps-Investors-Understand-Portfolio-Performance-and-Market-Activity/default.aspx) [25]
- Product Page: [Schwab Portfolio Insights Disclosure](https://www.schwab.com/legal/portfolio-insights-disclosure) [32]
- Independent Article: [ThinkAdvisor - Schwab Unveils AI Portfolio Insight Tool for Retail Clients](https://www.thinkadvisor.com/2026/05/05/schwab-unveils-ai-portfolio-insight-tool-for-retail-clients) [26]

---

## 3. Charles Schwab – AI Assistants (Chat/Voice)

### 3.1 Product Overview

**Product Name:** AI Assistants (chat and voice)  
**Launch Date:** June 2026 (first investor AI agent); announced during Q1 2026 earnings call on April 16, 2026 [36][37]  
**Official Description:** Series of AI assistants enabling clients to interact with chat and voice for service and support. Initial capabilities include answering general questions and performing actions like setting beneficiaries. CEO Rick Wurster stated: "Starting over the summer, we will introduce the first of several AI assistants that will enable our clients to interact with chat and voice." [36][37]

### 3.2 Customer Tier

**Mass retail.** Designed to help serve clients who cannot currently be served at scale by human advisors. Wurster noted: "AI can help us create personalized and deeper relationships with the clients we can't currently serve at scale." [36]

### 3.3 Geography & Languages Supported

**U.S. only** (based on disclosed information). Languages: English initially.

### 3.4 Core AI Stack

**Technology Partner:** Schwab is working with a "leading AI agent firm" on the build-out. Wurster stated: "We are working with a leading AI agent firm on this build-out and look forward to sharing more details soon." [36] The specific partner has not been publicly named.

**Guardrails:** Schwab emphasized that the AI assistants will have guardrails and human handoffs. Wurster stated: "We are ensuring handoffs to human agents and strict guardrails." [37]

### 3.5 Safety & Compliance Measures

Schwab's approach to AI safety is summarized in a June 5, 2026 letter from CEO Rick Wurster titled "Committed to Connection": "AI will help supercharge the way we serve you... For clients who prefer to interact directly with AI-powered capabilities, those experiences will be intuitive and tailored to you. For clients who want the combination of people and technology, we will continue to bring both to you." [38]

The AI assistants are designed with "handoffs to human agents and strict guardrails." [37] Wurster noted that 77% of U.S. investors currently use AI, but over 90% still prefer human involvement alongside AI. [36]

### 3.6 Integrations

The AI assistants integrate with Schwab's existing service and support infrastructure. They are part of a broader AI ecosystem at Schwab that includes: Schwab Knowledge Assistant (internal employee tool), AI Service Assistant (transcribing 60,000 daily client interactions), and planned AI assistants for advisors. [33][34][37]

### 3.7 Access & Pricing

**Pricing Model:** CEO Rick Wurster indicated that the firm would charge for agentic AI options for clients. "If someone is going to move cash with an advisor, we would charge, and we would charge for an agentic AI option." He also noted that "half of clients are willing to pay for AI financial tools." [37]  
**Access Channels:** Chat and voice (mobile app and web). [36]

### 3.8 KPIs

**Pre-Launch Data:** 77% of U.S. investors use AI today, though more than 90% still prefer human involvement in addition to AI. [36] Half of clients are willing to pay for AI financial tools. [37] Schwab's cost to serve an account has come down 21% over the past five years (41% inflation-adjusted). [39] Schwab's expense on client assets stood at 12 basis points over the past 12 months, compared with 38 basis points for wirehouse competitors. [35]

### 3.9 Links

- Official Announcement: [MLQ.ai - Schwab launches AI assistants to enhance client interactions](https://mlq.ai/earnings/highlight/SCHW-schwab-launches-ai-assistants-to-enhance-4b7ffe) [36]
- Independent Article: [WealthManagement.com - Schwab AI Push To Include Client-Facing AI Agents in June](https://www.wealthmanagement.com/ria-news/schwab-makes-ai-push-with-client-facing-agents-to-roll-out-in-june) [37]
- CEO Letter: [Schwab CEO's Note: Committed to Connection](https://www.schwab.com/learn/story/ceos-note) [38]

---

## 4. Citi – Portfolio Intelligence

### 4.1 Product Overview

**Product Name:** Portfolio Intelligence  
**Launch Date:** April 9, 2026 (available to Citi Private Bank clients in North America; global expansion planned for Q2 2026; all Wealth clients by year-end 2026) [40][41]  
**Official Description:** A client-facing platform that provides Citi Wealth clients with holistic portfolio insights. It consolidates positions, performance, and market insights from Citi Wealth's Chief Investment Office into a single interface at the click of a button. Andy Sieg, Head of Wealth, stated: "Citi Wealth aims to set the industry standard for client advice and service. Our objective is to create an ecosystem of AI-powered tools that scale the identification of investment opportunities, spot risks and provide guidance for next steps." [40][41]

### 4.2 Customer Tier

**Initial Launch:** Citi Private Bank clients (ultra-high-net-worth / UHNW segment).  
**Expansion Plan:** Will expand to Citi Private Bank clients globally in Q2 2026, and to all Wealth clients by year-end 2026. [40][41]

### 4.3 Geography & Languages Supported

**Initial Geography:** Available to Citi Private Bank clients in North America as of April 9, 2026.  
**Expansion:** Global expansion to Citi Private Bank clients in Q2 2026, all Wealth clients by year-end 2026. [40][41] Languages not explicitly specified for Portfolio Intelligence.

### 4.4 Core AI Stack

**Infrastructure Partners:** Citi has a multi-year strategic agreement with Google Cloud (announced October 28, 2024) to modernize its technology infrastructure, using Google Cloud's Vertex AI platform for generative AI capabilities. [42] Citi is also working with Palantir on account opening simplification. [40]

**Data Foundation:** Portfolio Intelligence is built on a unified "One Wealth" data foundation that connects transactions, holdings, behaviors, and external signals. [43] Citi Wealth's "Wealth Intelligence" initiative is built on this unified data foundation. [43]

**AI Model Evolution:** The AskWealth platform (a precursor/complementary tool) was originally powered by Meta's Llama large language model suite but was transitioning to Google's Gemini, indicating the broader AI infrastructure is shifting toward Google's Gemini models. [44]

**Developer Tools:** Citi has deployed AI coding tools to 30,000 developers. The bank's internal agentic AI platform, **Citi Stylus Workspaces** (launched September 2025), lets employees compress multistep tasks across systems into a single prompt. [45]

### 4.5 Safety & Compliance Measures

**Enterprise-Wide AI Governance:** Citi has a comprehensive risk and control framework for Generative AI. The bank created fast-track approval processes that cut sign-off from six months to under six weeks for AI products. [46]

**Human-in-the-Loop Oversight:** Citi emphasizes human-in-the-loop oversight, treating regulatory compliance as a feature, and measuring tangible economic value ("capacity created") rather than vanity metrics. [47]

**Responsible AI:** Citi's approach to responsible AI includes transparency, human oversight, and a culture driven by measurable outcomes. Joe Bonanno stated: "Responsible AI enables scale... Trust is what allows AI to scale in Wealth Management." [43]

**Governance Structure:** Citi has a dedicated "Head of Generative AI Risk and Control - Citi Wealth" role designed to "design and implement a comprehensive risk and control framework for Generative AI use cases across global wealth management," "lead risk assessments, identify potential vulnerabilities, and recommend mitigation strategies for Gen AI initiatives," and "ensure all Gen AI initiatives comply with local, regional, and global regulatory requirements, including data privacy laws and AI ethics standards." [48]

**Important Note:** Citi has not released an open-ended LLM bot to consumers, citing hallucination risk and data-privacy concerns. [47]

### 4.6 Integrations

Portfolio Intelligence integrates positions, performance metrics, and market insights from **Citi Wealth's Chief Investment Office** into a single digital experience. [40][41] It is part of a broader ecosystem of AI-powered tools that includes advisor-facing tools: **AskWealth CIO** (chat-based access to CIO research for advisors), **Client 360** (unified internal client data platform consolidating holdings, positions, call logs, and client interests), and **CitiScribe** (AI note-taking for advisors, deployed to all North American Wealth advisors in Q1 2026, saving advisors up to four hours per client meeting). [40][41]

**Technology Stack:** Citi's technology stack includes MuleSoft (integration platform), Informatica (data integration), Splunk Enterprise (analytics), and Google Cloud infrastructure. [49]

### 4.7 Access & Pricing

**Pricing:** Portfolio Intelligence is a **free tool included for eligible Citi Wealth clients**. It is not a separately priced product. [40][41]  
**Access Channels:** Digital interface – likely accessible via Citi's online banking platform and/or mobile app (described as "at the click of a button" and "easy-to-use interface"). [40] No API access has been publicly announced.

### 4.8 KPIs

**Specific to Portfolio Intelligence:** Launched on April 9, 2026, so no specific adoption metrics or KPIs have been publicly reported as of August 5, 2026.

**Broader Citi AI KPIs (relevant context):** 52% containment rate in call-center IVA (saving $6.6M/year); 30–40% reduction in false positive AML alerts; 35–50% developer productivity gains; 15–20% execution cost reduction in FX trading; 60% reduction in tax document processing time; 34% eligible staff adoption of Citi Assist in two weeks; 100,000 developer hours saved per week via automated code reviews. [47][45] CitiScribe saves advisors up to four hours per client meeting. [40] Citi Wealth revenue grew 11% to $3.1 billion in Q1 2026. [50] Citi manages approximately $1 trillion in assets. [50]

### 4.9 Links

- Official Press Release: [Citi Wealth Deploys AI-Powered Technology to Enhance Client Experience](https://www.citigroup.com/global/news/press-release/2026/citi-wealth-deploys-ai-powered-technology-to-enhance-client-experience) [40]
- Independent Article: [PYMNTS - Citi Arms Wealth Advisors With 4 AI Tools to Cut Busywork](https://www.pymnts.com/news/artificial-intelligence/2026/citi-arms-wealth-advisors-with-4-ai-tools-to-cut-busywork) [41]
- Independent Article: [Banking Dive - Citi adds AI-powered adviser in wealth unit](https://www.bankingdive.com/news/citi-sky-ai-wealth-adviser-google-banking/819087) [51]

---

## 5. Citi – Citi Sky

### 5.1 Product Overview

**Product Name:** Citi Sky  
**Launch Date:** Unveiled April 22, 2026 (at Google Cloud Next 2026 conference in Las Vegas); rolling out to Citigold clients starting summer 2026 in a phased U.S. rollout [52][53]  
**Official Description:** Citi Sky is an "always-on, AI-powered member of the Citi Wealth team" built using Google Cloud and Google DeepMind technologies. It is an agentic AI tool with a human-like avatar that can converse with clients like a human adviser. Andy Sieg, Head of Wealth at Citi, stated: "We believe Citi Sky will change the model of wealth management... With Citi Sky, you simply ask – and act. This is the shift from interface to intelligence, from transactions to outcomes." [52][53]

### 5.2 Customer Tier

**Mass affluent (Citigold clients).** Citi plans to extend Sky to credit card and other lines of business by 2027. Joe Bonanno, Head of Wealth Intelligence at Citi, noted: "This is opening up new segments. It's also making our advisers smarter, because it's building up this corpus of knowledge on people's goals and objectives and interests." [52]

### 5.3 Geography & Languages Supported

**Initial Geography:** United States (phased rollout to Citigold clients starting summer 2026).  
**Languages:** English and Spanish initially, with plans to scale to 100+ languages. [52][53]

### 5.4 Core AI Stack

**Technology Platform:** Built on the **Gemini Enterprise Agent Platform** and leverages **Google DeepMind's real-time avatar technology** and **Gemini's live audio/video models**. [52][53] Thomas Kurian, CEO of Google Cloud, stated: "The future of financial services lies in the ability to turn vast amounts of data into conversational, actionable intelligence for investors." [52]

**Key Capabilities:** Financial guidance (e.g., CD maturity alerts, market insights from Citi's Chief Investment Office), natural conversational interaction via voice and video, multilingual support, and the ability to interpret client reactions. [52][53]

**Infrastructure:** Citi Sky operates within Citi's secure environment to address security and hallucination concerns. It was built using Google Cloud's secure infrastructure with a defense-in-depth approach, incorporating multiple layers of security such as data encryption at rest, in transit, and in use with Confidential Computing. [42]

### 5.5 Safety & Compliance Measures

Citi Sky operates within **Citi's secure environment** to address security and hallucination concerns. [52] The tool is designed to work alongside human advisors, not replace them. [52] Citi's enterprise-wide AI governance framework applies, including the fast-track approval processes and human-in-the-loop oversight described in Section 4.5. [46][47]

### 5.6 Integrations

Citi Sky integrates with Citi's wealth management systems, including the Chief Investment Office's market insights and research. It is designed to be an always-on intelligent assistant that works alongside human advisors. [52] Citi plans to extend Sky to credit card and other lines of business by 2027. [52]

### 5.7 Access & Pricing

**Access Channels:** Voice and video (conversational interface). Available via mobile app. [52][53]  
**Pricing Model:** Not explicitly disclosed. Available to Citigold clients as part of their banking relationship.

### 5.8 KPIs

**Specific to Citi Sky:** Rolling out starting summer 2026, so no specific adoption metrics have been publicly reported as of August 5, 2026.

### 5.9 Links

- Official Press Release: [Citi Wealth Unveils "Citi Sky" – An AI-Powered Member of the Citi Wealth Team](https://www.prnewswire.com/news-releases/citi-wealth-unveils-citi-sky--an-ai-powered-member-of-the-citi-wealth-team-built-using-google-cloud-and-google-deepmind-technologies-302749822.html) [52]
- Independent Article: [Forbes - Transforming Wealth Management Using AI At Citi](https://www.forbes.com/sites/randybean/2026/05/18/transforming-wealth-management-using-ai-at-citi) [53]
- Independent Article: [Business Insider - AI Agents Could Supercharge Wealth Advisors, but Memory Issue Remains](https://www.businessinsider.com/citi-ai-wealth-management-agents-2026-4) [54]

---

## 6. BMO Financial Group – My Financial Progress

### 6.1 Product Overview

**Product Name:** My Financial Progress  
**Launch Date:** July 10, 2025 [55][56]  
**Official Description:** An innovative digital goal planning platform available to all BMO clients via BMO's Mobile Banking app and Online Banking. The tool helps Canadians create personalized, adaptive long-term financial plans, gain comprehensive insights into their finances, and access real-time strategies to reach their goals. It adjusts goals and strategies as circumstances change, allowing clients to monitor progress anytime, anywhere. The platform is based on Conquest Planning software. [55][56]

### 6.2 Customer Tier

**Mass retail audience.** "Similar available tools are typically complex and geared towards professional advisors, but My Financial Progress simplifies the interface and reimagines the experience for a mass retail audience." [56][57] BMO is the seventh largest bank in North America by assets ($1.4 trillion as of April 30, 2025), serving 13 million customers. [55]

### 6.3 Geography & Languages Supported

**Canada only.** Available in English and French (BMO serves Canadian clients). [55][56]

### 6.4 Core AI Stack

**Underlying Technology:** Conquest Planning's proprietary AI expert system called **Strategic Advice Manager (SAM)**. [58][59]

**Nature of SAM:** SAM is a **deterministic calculation engine** – it produces auditable, repeatable results based on codified financial planning best practices. It is NOT a generative AI or large language model. It is an AI expert system that analyzes each client's complete financial picture and surfaces personalized, compliant strategies for every client in seconds. [58][59]

**Architecture:** Built using a **"Blackboard System" architecture**, where each strategy is tested and ranked against the client's situation, goals, best practices, and preferences. [58]

**Key Characteristics:** "If you can't trace it, you can't defend it. Because SAM is deterministic, every strategy can be inspected, re-run, and validated." [58] SAM supports regulatory frameworks such as CRM2/CRM3 (Canada), Best Interest/DOL Fiduciary (U.S.), and FCA Targeted Support (UK). [58] The engine is not hallucinatory because it is deterministic: any error is systematic and discoverable. [58]

**Additional AI Capabilities from Conquest (April 2026):** SAM Guide (agentic natural language assistant within the advisor application), SAM Bytes (micro-journeys bundling multiple strategies), LLM Data Migration (AI-powered data ingestion from unstructured data), and MCP server (Model Context Protocol server allowing external AI agents to access Conquest data via APIs, reducing hallucination risk). [60][61]

**Conquest Planning Scale:** Over 2 million financial plans created on the platform. Trusted by 6 of the top 10 banks in North America and major enterprises. Supports over 60,000 advisors at 1,000+ financial institutions. Over 70% of the Canadian financial market; 80% of Canadian advisor market. [59][62]

### 6.5 Safety & Compliance Measures

**Conquest / SAM Level:** Deterministic engine produces auditable, repeatable results; every calculation can be traced, re-run, and validated. [58] "Compliance-first AI" approach: "SAM Guide is built for speed and security. It's not bolted onto a general-purpose LLM. It's purpose-built, plan-aware, and grounded in a proprietary calculation engine that compliance teams can trust." – Ken Lotocki, CPO. [60][61]

**BMO Level:** BMO has a comprehensive AI governance framework. The **BMO Institute for Applied Artificial Intelligence & Quantum** was established April 6, 2026 as an enterprise-wide Centre of Excellence. [63] **Responsible AI Principles** include accountability, bias mitigation, transparency, explainability, privacy, monitoring, security, and sustainability. [64] **Human-in-the-loop philosophy** is a central tenet. [65] BMO has a formal AI governance committee overseeing all AI deployments. [66] BMO Chief AI Officer Kristin Milchanowski stated: "Generative AI is limited and doesn't scale well in corporate... We're really focused right now on the AI agents, because in banking… everything we do needs to be governed." [66]

### 6.6 Integrations

**Custodian/Portfolio Systems:** Conquest's open two-way API integrates with existing financial systems, CRM, and portfolio management systems. [58][59]  
**BMO Account Integration:** Users can sync their BMO accounts for real-time updates. [56]  
**Integration with Existing BMO Digital Tools:** BMO SmartProgress, BMO Insights (CashTrack, Spend Categorization), BMO Savings Amplifier Account, BMO CreditView, BMO PaySmart. [55]  
**Conquest Clients Include:** BNY Pershing, RBC, Fidelity Clearing Canada, Wealthsimple, Morgan Stanley Wealth Management Canada, Raymond James, SunLife. [58]

### 6.7 Access & Pricing

**Free to BMO clients.** Available to all clients via BMO Mobile Banking app and Online Banking. [55][56]  
**Mobile App:** BMO Mobile Banking app. [55]  
**Web:** BMO Online Banking. [55]  
**API:** Conquest has an open two-way API (enterprise integration). [59]

### 6.8 KPIs

**Conquest-Level KPIs:** Over 2 million financial plans created on the Conquest platform. [59] 14 percentage points growth in new client onboards with $1M+ investible assets. [59] 4x more plans per advisor. [59] 30% increase in financial plans at Scotiabank directly attributed to Conquest. [61] A large retirement planner saw engagement rise from 4% to 90% on day one. [61] 40% conversion rate to digitally fulfilled plans or direct advisor relationships. [61] Over 1.5 million households served across three countries (as of 2025). [61] Plans created in 15 minutes vs. industry average of 10 hours. [59]

**BMO-Level AI KPIs:** BMO ranked joint #1 globally in AI Talent Development in the 2025 Evident AI Index. [67] BMO ranked #19 globally in AI maturity in banking (Evident AI Index), climbing five spots. [67] BMO ranked #1 in EMARKETER's 2026 Canada Mobile Banking Emerging Features Benchmark. [68] BMO's Lumi (GenAI assistant) reduced help desk calls by 60%. [64] BMO's call center AI solution: 70% reduction in average hold time, 10% increase in first-call resolution, CAD $6.5 million annual benefit. [65] BMO's Q2'26 adjusted net income rose 34% Y/Y to $2.7 billion. [69]

### 6.9 Links

- Official Press Release: [BMO Newsroom - BMO's My Financial Progress Digital Platform Empowers Canadians](https://newsroom.bmo.com/2025-07-10-BMOs-My-Financial-Progress-Digital-Platform-Empowers-Canadians-with-Personalized-Goal-Planning-Experience) [55]
- BMO Blog: [My Financial Progress: the digital goal-planning tool putting control in clients' hands](https://www.bmo.com/en-ca/main/about-bmo/news-insights/blog/my-financial-progress) [56]
- Independent Article: [Investment Executive - Tech roundup: BMO clients can build their own financial plan in Conquest Planning](https://www.investmentexecutive.com/industry-news/tech-roundup-bmo-clients-can-build-their-own-financial-plan-in-conquest-planning) [57]

---

## 7. BMO Financial Group – AI News and Market Summaries (BMO InvestorLine)

### 7.1 Product Overview

**Product Name:** AI News and Market Summaries  
**Launch Date:** 2025 (exact date not specified in available sources) [70][71]  
**Official Description:** An AI-powered feature providing continuously refreshed summaries of Canadian and U.S. market information, including stock-specific updates. Available to all adviceDirect and self-directed InvestorLine clients. Silvio Stroescu, President, BMO InvestorLine and Head, Wealth Digital First, stated: "Most days, the firehose of market news creates more noise than insight. Investors don't need more headlines – they need clarity on what's actually moving the markets and the names in their portfolios. AI News and Market Summaries delivers that clarity and enables investors to spend less time scrolling and more time building expertise with greater clarity, choice, and confidence." [70][71]

### 7.2 Customer Tier

**Self-directed investors and adviceDirect clients** (mass retail to mass affluent). [70][71]

### 7.3 Geography & Languages Supported

**Canada only.** Bilingual (English and French). [70][71]

### 7.4 Core AI Stack

**Specific LLM provider, models, and technology stack details are not publicly disclosed.** The tool is described as "AI-powered" with **sentiment analysis** capabilities. [72] BMO's broader AI infrastructure includes: Lumi (GenAI assistant), Rovr AI (insurance advisor assistant), Nexa (knowledge assistant for private wealth), and the BMO Institute for Applied AI & Quantum. [63][64] BMO's overall AI stack includes "observability stacks and machine learning ops to LLM orchestration, vector databases, and advanced enterprise search." [73] BMO has partnerships with Microsoft (Azure OpenAI Service for insurance AI), Vector Institute, IBM Quantum Network, Dataiku, Dynatrace, and Google Cloud. [74]

### 7.5 Safety & Compliance Measures

The tool is embedded within BMO's existing regulated digital investing platform (BMO InvestorLine), subject to regulatory oversight. BMO's broader Responsible AI framework applies, including human-in-the-loop philosophy, AI governance committee oversight, and formal Responsible AI and Data Ethics Forum. [64][65][66] BMO InvestorLine FAQ includes standard disclaimers: "All market data is provided by a third-party vendor and is delayed by at least 20 minutes unless otherwise noted. The third-party information does not represent BMO InvestorLine's views, and is not intended to provide investment, tax, accounting or legal advice." [72]

### 7.6 Integrations

Available on the **BMO Invest app** (mobile) and **BMO InvestorLine 2.0 website** (desktop). [72] Research tools integrated alongside: Trading Central (Value Analyzer, Technical Insights), CFRA, and Morningstar. [72] Account alerts and corporate calendar are also available. [72]

### 7.7 Access & Pricing

**Free** to all BMO InvestorLine adviceDirect and self-directed clients. [70][71]  
**Access Channels:** BMO Invest app (mobile) and BMO InvestorLine 2.0 website (desktop). [72]

### 7.8 KPIs

**Specific KPIs for this tool are not publicly available.** BMO's broader digital engagement metrics include: #1 in EMARKETER's 2026 Canada Mobile Banking Emerging Features Benchmark, [68] ranked joint #1 globally in AI Talent Development (2025 Evident AI Index), [67] and 37% of Americans using AI to manage finances (2024 BMO survey, with Gen Z leading at 61%). [75]

### 7.9 Links

- Official BMO Blog: [BMO InvestorLine introduces AI News and Market Summaries in Canada](https://www.bmo.com/en-ca/main/about-bmo/news-insights/blog/bmo-investorline-introduces-ai-news-and-market-summaries-in-canada) [70]
- Product Page: [BMO InvestorLine FAQ](https://www.secure.bmoinvestorline.com/wealth/journeys/content/micro/education-hub/faq.html) [72]
- BMO Learning Centre: [How to use AI for Investing](https://www.bmo.com/en-ca/main/personal/investments/learning-centre/ai-for-investing) [71]

---

## 8. Additional Notable Client-Facing AI Tools (Pre-2023 or Adjacent Scope)

The following client-facing AI tools were launched prior to the January 2023 cutoff but remain relevant as established production systems active during the research period:

### 8.1 Bank of America – Erica
- **Launch Date:** June 2018
- **Current Status:** As of August 2025, Erica had surpassed 3 billion client interactions, serving nearly 50 million users. [76] As of Q2 2026, active users increased 23% YoY to 24.6 million. [77]
- **Description:** Uses natural language processing and machine learning (not generative AI) to answer questions, manage accounts, and provide proactive insights. Erica does not provide investment advice but handles banking tasks and connects clients to Merrill for investing. [76]

### 8.2 Wells Fargo – Fargo
- **Launch Date:** October 2022
- **Current Status:** Built on Google Cloud's Dialogflow conversational AI platform. Fargo serves Wells Fargo's 27 million mobile customers with features including instant card freezing, transaction searches, and budgeting tips. [78] As of 2024, Fargo had 242.4 million interactions. [79]

### 8.3 RBC – NOMI Suite
- **Launch Date:** 2017 (NOMI Insights and Find & Save); April 2019 (NOMI Budgets); September 2021 (NOMI Forecast) [80][81]
- **Current Status:** As of 2024, NOMI had 1.5 million active users, with 53% calling it a game-changer for their finances. NOMI Forecast won Best Use of AI for Customer Experience at The Digital Banker Awards 2023. [81] NOMI includes Insights (personalized spending alerts), Find & Save (automated savings, with over $3.6 billion saved), Budgets (personalized budgets), and Forecast (7-day cashflow prediction). [82]

### 8.4 Truist – Truist Assist
- **Launch Date:** September 15, 2022
- **Current Status:** As of 2025, Truist Assist had 5.5 million conversations with 80%+ resolution rate. [83] AI-enhanced digital virtual assistant for personal banking clients, using NLP/NLU to answer over 100 common inquiries. [84]

### 8.5 US Bank – Smart Assistant
- **Launch Date:** July 23, 2020
- **Description:** Voice-first banking feature integrated into the mobile app, using NLP for voice and text commands including Zelle payments, transfers, bill inquiries, and card management. [85]

## 9. Notable Fintech: PortfolioPilot by Global Predictions Inc.

While not a bank or broker-dealer, PortfolioPilot is an SEC-registered investment advisor operating an AI-powered financial advisor platform for self-directed investors that fits the product description.

**Product Name:** PortfolioPilot  
**Launch Date:** Operating as of May 2026 (specific launch date not provided)  
**Description:** AI-powered financial advisor platform providing hedge fund-inspired technology including net worth tracking, personalized investment advice, continuous tax optimization, estate planning tools, retirement planning, and scenario modeling. Claims over 50,000 users and $40 billion in assets under analysis (as of May 2026). [86]

**Pricing:** Free tier (net worth tracking, planning, portfolio assessment); Gold ($20/month, includes investment recommendations, fee detection, tax optimization, limited AI assistant); Platinum ($49/month, adds fee optimization, tax-efficient distribution advice, unlimited AI, equity research, custom simulations); Pro ($99/month, adds quarterly expert calls, private equity modeling, multi-user). [86]

**Availability:** United States and Canada. [86]

---

## 10. Notable Advisor-Facing AI Tools (Outside Scope)

The following major AI tools were identified but are **advisor-facing or internal employee tools**, not client-facing, and therefore fall outside the primary scope of this report. They are listed for context:

- **Morgan Stanley – AI @ Morgan Stanley Assistant:** Launched September 2023. Advisor-facing chatbot for accessing research. 98% adoption among advisor teams. [87]
- **Morgan Stanley – AI @ Morgan Stanley Debrief:** Launched June 26, 2024. Advisor-facing meeting summary tool powered by OpenAI's GPT-4 and Whisper. [88]
- **Goldman Sachs – GS AI Assistant:** Launched firmwide mid-2025 (pilot January 2025). Internal employee tool. [89]
- **Bank of America – ask MERRILL and ask PRIVATE BANK:** Advisor-facing tools. 23 million interactions in 2024. [90]
- **Wells Fargo – AI Teammate:** Launched July 17, 2026. Advisor-facing conversational tool for information retrieval. [91]
- **UBS – Red (AI Assistant):** Advisor-facing. Deployed to 52,000+ employees as of 2025. [92]
- **Raymond James – Raimond (formerly Rai):** Advisor-facing operations AI agent. Piloted by 600 advisors as of May 2026. [93]
- **HSBC – Wealth Intelligence:** Launched September 2025. For wealth management staff (not clients). [94]
- **BNY Mellon – Eliza:** Internal enterprise AI platform. 20,000 employees building AI agents. 125+ live use cases. [95]

## 11. Institutions with No Confirmed Client-Facing AI Portfolio/Wealth Management Copilot (Jan 2023 – Aug 2026)

- **Goldman Sachs:** GS AI Assistant is internal. AlphaAI (launched July 2026) is an investment platform for identifying AI-related investment opportunities, not a client-facing copilot. [96]
- **Fidelity:** Fidelity Go is a robo-advisor (pre-2023). No new client-facing AI portfolio management copilot launched within the window. [97]
- **UBS:** No client-facing AI copilot identified. Red and STAAT are advisor-facing. [92]
- **HSBC US:** Wealth Intelligence is staff-facing. [94]
- **PNC Financial Services:** No client-facing AI wealth management copilot identified. [98]
- **US Bank:** Smart Assistant is a general banking assistant (launched 2020, pre-window). [85]
- **Truist:** Truist Assist is a general banking assistant (launched September 2022, pre-window). [84]
- **Scotiabank:** Digital assistant launched June 2022 (pre-window). AI agents used for payment operations (internal). [99]
- **National Bank of Canada:** No client-facing AI wealth management copilot identified. [100]
- **Northern Trust:** AI tools are internal (document digitization, reconciliation, fraud detection). [101]
- **BNY Mellon:** Eliza platform is internal. Wove and Pershing X embed AI but are advisor-facing platforms. [95]

---

## Sources

[1] Pensions & Investments - J.P. Morgan Chase launches IndexGPT: https://www.pionline.com/money-management/jp-morgan-chase-launches-indexgpt

[2] Bloomberg - JPMorgan Unveils IndexGPT in Next Wall Street Bid to Tap AI Boom: https://www.bloomberg.com/news/articles/2024-05-03/jpmorgan-unveils-indexgpt-in-next-wall-street-bid-to-tap-ai-boom

[3] Yahoo Finance - JPMorgan Unveils IndexGPT in Next Wall Street Bid to Tap AI Boom: https://finance.yahoo.com/news/jpmorgan-unveils-indexgpt-next-wall-110001888.html

[4] Pensions & Investments - J.P. Morgan Chase launches IndexGPT: https://www.pionline.com/money-management/jp-morgan-chase-launches-indexgpt

[5] InvestmentNews - JPMorgan taps ChatGPT for new thematic investment suite: https://www.investmentnews.com/etfs/jpmorgan-taps-chatgpt-for-new-thematic-investment-suite/252966

[6] WealthManagement.com - JPMorgan Unveils IndexGPT in Next Wall Street Bid to Tap AI Boom: https://www.wealthmanagement.com/equities/jpmorgan-unveils-indexgpt-in-next-wall-street-bid-to-tap-ai-boom

[7] AI Street / Klover - JPMorgan Uses AI Agents: 10 Ways to Use AI: https://www.klover.ai/jpmorgan-uses-ai-agents-10-ways-to-use-ai-in-depth-analysis-2025

[8] JPMorganChase - Asset & Wealth Management Letter 2025: https://www.jpmorganchase.com/content/dam/jpmc/jpmorgan-chase-and-co/investor-relations/documents/asset-and-wealth-management-letter-2025.pdf

[9] PYMNTS - JPMorgan Chase Unveils AI-Powered Tool for Thematic Investing: https://www.pymnts.com/news/artificial-intelligence/2024/jpmorgan-chase-unveils-ai-powered-tool-thematic-investing

[10] CTO Magazine - AI in Banking: JP Morgan Leads the AI Sphere: https://ctomagazine.com/jp-morgan-chase-accelerates-ai-adoption

[11] Emerj - Artificial Intelligence at JPMorgan Chase: https://emerj.com/artificial-intelligence-at-jpmorgan-chase

[12] CTO Magazine - AI in Banking: JP Morgan Leads the AI Sphere: https://ctomagazine.com/jp-morgan-chase-accelerates-ai-adoption

[13] JPMorganChase - Artificial Intelligence Research: https://www.jpmorganchase.com/about/technology/research/ai

[14] YouTube / OSFF - How JPMorgan Built an AI Ecosystem That's Helping 10,000+ Financial Advisors Close 30% More Deals: https://www.youtube.com/watch?v=xgTb0XnQD74

[15] JPMorganChase - Strengthening LLM guardrails with synthetic data generation (Fence framework): https://www.jpmorganchase.com/about/technology/blog/fence-framework

[16] CNBC - JPMorgan developing ChatGPT-like A.I. investment advisor (May 2023): https://www.cnbc.com/2023/05/25/jpmorgan-develops-ai-investment-advisor.html

[17] Fortune - Meet 'IndexGPT,' JPMorgan's A.I. stock picker: https://fortune.com/2023/05/26/jpmorgan-indexgpt-a-i-stock-picker

[18] JPMorganChase - Artificial Intelligence Research: https://www.jpmorganchase.com/about/technology/research/ai

[19] J.P. Morgan Markets - SI360 Structured Investments: https://markets.jpmorgan.com/pricing-and-execution/si360

[20] Klover - JPMorgan's AI Strategy: Chasing AI Dominance: https://www.klover.ai/jpmorgan-ai-strategy-chasing-ai-dominance

[21] Emerj - Artificial Intelligence at JPMorgan Chase: https://emerj.com/artificial-intelligence-at-jpmorgan-chase

[22] AI News - JPMorgan Chase AI strategy: US$18B bet paying off: https://www.artificialintelligence-news.com/news/jpmorgan-chase-ai-strategy-2025

[23] CTO Magazine - AI in Banking: JP Morgan Leads the AI Sphere: https://ctomagazine.com/jp-morgan-chase-accelerates-ai-adoption

[24] JPMorganChase - JPMorganChase continues to lead the world's top banks in AI maturity: https://www.jpmorganchase.com/about/technology/blog/jpmc-evident-25

[25] Charles Schwab Pressroom - Charles Schwab Launches AI-Powered Capability That Helps Investors Understand Portfolio Performance and Market Activity: https://pressroom.aboutschwab.com/press-releases/press-release/2026/Charles-Schwab-Launches-AI-Powered-Capability-That-Helps-Investors-Understand-Portfolio-Performance-and-Market-Activity/default.aspx

[26] ThinkAdvisor - Schwab Unveils AI Portfolio Insight Tool for Retail Clients: https://www.thinkadvisor.com/2026/05/05/schwab-unveils-ai-portfolio-insight-tool-for-retail-clients

[27] Investing.com - Schwab launches AI-powered portfolio insights for retail clients: https://www.investing.com/news/company-news/schwab-launches-aipowered-portfolio-insights-for-retail-clients-93CH-4659319

[28] Bloomberg - Schwab Plans to Use AI to Reach, Serve Less-Affluent Customers: https://www.bloomberg.com/news/articles/2026-05-13/schwab-plans-to-use-ai-to-reach-serve-less-affluent-customers

[29] Citywire Pro Buyer - Schwab debuts client-facing AI tool: https://citywire.com/pro-buyer/news/schwab-debuts-client-facing-ai-tool/a2489265

[30] Schwab Careers - Senior Responsible AI Researcher: https://www.schwabjobs.com/job/san-francisco/senior-responsible-ai-researcher-ai-x/33727/98242190080

[31] WealthTech Strategy - Anthropic Launches Financial AI Agents & Schwab's AI Initiative Responds: https://www.wealthtechstrategy.com/post/anthropic-launches-financial-ai-agents-schwab-s-ai-initiative-responds

[32] Charles Schwab - Portfolio Insights Disclosure: https://www.schwab.com/legal/portfolio-insights-disclosure

[33] Emerj - Artificial Intelligence at Charles Schwab - Two Use Cases: https://emerj.com/artificial-intelligence-at-charles-schwab-two-use-cases

[34] Yahoo Finance - The Charles Schwab Corporation Q1 2026 Earnings Call Summary: https://finance.yahoo.com/markets/stocks/articles/charles-schwab-corporation-q1-2026-164723922.html

[35] InvestmentNews - Schwab touts AI as its biggest growth lever at investor day: https://www.investmentnews.com/fintech/schwab-touts-ai-as-its-biggest-growth-lever-at-investor-day/266613

[36] MLQ.ai - Schwab launches AI assistants to enhance client interactions: https://mlq.ai/earnings/highlight/SCHW-schwab-launches-ai-assistants-to-enhance-4b7ffe

[37] WealthManagement.com - Schwab AI Push To Include Client-Facing AI Agents in June: https://www.wealthmanagement.com/ria-news/schwab-makes-ai-push-with-client-facing-agents-to-roll-out-in-june

[38] Schwab.com - CEO's Note: Committed to Connection: https://www.schwab.com/learn/story/ceos-note

[39] Bloomberg YouTube - AI Will Help Wealth Managers, Not Hurt Them, Schwab CEO Says: https://www.youtube.com/watch?v=8N2_xgex_fg

[40] Citi Group - Citi Wealth Deploys AI-Powered Technology to Enhance Client Experience: https://www.citigroup.com/global/news/press-release/2026/citi-wealth-deploys-ai-powered-technology-to-enhance-client-experience

[41] PYMNTS - Citi Arms Wealth Advisors With 4 AI Tools to Cut Busywork: https://www.pymnts.com/news/artificial-intelligence/2026/citi-arms-wealth-advisors-with-4-ai-tools-to-cut-busywork

[42] Citi Group - Google Cloud Strategic Agreement: https://www.citigroup.com/global/news/press-release/2024/citi-and-google-cloud-announce-expanded-strategic-agreement

[43] Citi Group - Wealth Intelligence: https://www.citigroup.com/global/wealth

[44] Citi Group - AI Innovation: https://www.citigroup.com/global/technology/ai

[45] Citi Group - Technology: https://www.citigroup.com/global/technology

[46] Citi Group - AI Governance: https://www.citigroup.com/global/technology/ai-governance

[47] Business Insider - AI Agents Could Supercharge Wealth Advisors, but Memory Issue Remains: https://www.businessinsider.com/citi-ai-wealth-management-agents-2026-4

[48] Citi Group - Careers - Head of Generative AI Risk and Control: https://www.citigroup.com/global/careers

[49] Citi Group - Technology Stack: https://www.citigroup.com/global/technology/stack

[50] Citi Group - Q1 2026 Earnings: https://www.citigroup.com/global/investors/q1-2026-earnings

[51] Banking Dive - Citi adds AI-powered adviser in wealth unit: https://www.bankingdive.com/news/citi-sky-ai-wealth-adviser-google-banking/819087

[52] PRNewswire - Citi Wealth Unveils "Citi Sky" – An AI-Powered Member of the Citi Wealth Team: https://www.prnewswire.com/news-releases/citi-wealth-unveils-citi-sky--an-ai-powered-member-of-the-citi-wealth-team-built-using-google-cloud-and-google-deepmind-technologies-302749822.html

[53] Forbes - Transforming Wealth Management Using AI At Citi: https://www.forbes.com/sites/randybean/2026/05/18/transforming-wealth-management-using-ai-at-citi

[54] Business Insider - AI Agents Could Supercharge Wealth Advisors, but Memory Issue Remains: https://www.businessinsider.com/citi-ai-wealth-management-agents-2026-4

[55] BMO Newsroom - BMO's My Financial Progress Digital Platform Empowers Canadians: https://newsroom.bmo.com/2025-07-10-BMOs-My-Financial-Progress-Digital-Platform-Empowers-Canadians-with-Personalized-Goal-Planning-Experience

[56] BMO Blog - My Financial Progress: the digital goal-planning tool putting control in clients' hands: https://www.bmo.com/en-ca/main/about-bmo/news-insights/blog/my-financial-progress

[57] Investment Executive - Tech roundup: BMO clients can build their own financial plan in Conquest Planning: https://www.investmentexecutive.com/industry-news/tech-roundup-bmo-clients-can-build-their-own-financial-plan-in-conquest-planning

[58] Conquest Planning - SAM: https://conquestplanning.com/sam

[59] Conquest Planning - Media: https://conquestplanning.com/media

[60] Conquest Planning - AI Innovation: https://conquestplanning.com/media/conquest-planning-previews-next-chapter-of-compliance-first-ai-innovation

[61] Wealth Professional - Conquest Planning says its new AI tools shrink 10-hour plans to minutes: https://www.wealthprofessional.ca/news/industry-news/conquest-planning-says-its-new-ai-tools-shrink-10-hour-plans-to-minutes/391777

[62] Conquest Planning - Named among CNBC's World's Top Fintech Companies 2026: https://finance.yahoo.com/technology/ai/articles/conquest-planning-named-among-cnbcs-130000195.html

[63] BMO AI Hub: https://ai.bmo.com

[64] BMO - Responsible AI: https://ai.bmo.com/responsible-ai

[65] BMO - Return on Intelligence: https://www.bmo.com/en-us/main/about-bmo/our-impact/clients/technology-innovation/return-on-intelligence

[66] BMO - AI and the future of personalized advice: https://ai.bmo.com/our-stories/ai-and-the-future-of-personalized-advice

[67] BMO - Ranked #1 Globally in AI Talent Development: https://www.bmo.com/en-ca/main/about-bmo/news-insights/blog/bmo-ranked-1-globally-in-ai-talent-development

[68] BMO - EMARKETER 2026 Canada Mobile Banking Emerging Features Benchmark: https://www.bmo.com/en-ca/main/about-bmo/news-insights

[69] BMO - Q2 2026 Earnings: https://www.bmo.com/ir

[70] BMO Blog - BMO InvestorLine introduces AI News and Market Summaries in Canada: https://www.bmo.com/en-ca/main/about-bmo/news-insights/blog/bmo-investorline-introduces-ai-news-and-market-summaries-in-canada

[71] BMO - How to use AI for Investing: https://www.bmo.com/en-ca/main/personal/investments/learning-centre/ai-for-investing

[72] BMO InvestorLine FAQ: https://www.secure.bmoinvestorline.com/wealth/journeys/content/micro/education-hub/faq.html

[73] BMO - Technology and Innovation: https://www.bmo.com/en-us/main/about-bmo/our-impact/clients/technology-innovation

[74] BMO - Innovation with Impact (AI & Quantum Institute): https://www.bmo.com/en-us/main/about-bmo/news-insights/blog/innovation-with-impact

[75] BMO - 37% of Americans use AI to manage finances: https://www.bmo.com/en-ca/main/about-bmo/news-insights

[76] Bank of America Newsroom - Erica: https://newsroom.bankofamerica.com/erica

[77] Yahoo Finance - BofA Erica active users: https://finance.yahoo.com/news/bank-america-erica-ai-assistant-2026

[78] Fintech Futures - Wells Fargo Fargo: https://www.fintechfutures.com/2022/10/wells-fargo-launches-fargo-ai-assistant

[79] Training The Street - Wells Fargo Fargo interactions: https://www.trainingthestreet.com/wells-fargo-fargo-ai

[80] Newswire.ca - RBC NOMI Budgets: https://www.newswire.ca/news/rbc-nomi-budgets

[81] RBC Newsroom - NOMI Forecast: https://www.rbc.com/newsroom/nomi-forecast

[82] RBC - NOMI Suite: https://www.rbc.com/nomi

[83] Truist Annual Report 2025: https://www.truist.com/investor-relations/annual-report-2025

[84] PRNewswire - Truist Assist: https://www.prnewswire.com/news-releases/truist-launches-truist-assist-2022

[85] US Bank Blog - Smart Assistant: https://www.usbank.com/blog/smart-assistant

[86] PortfolioPilot: https://www.portfoliopilot.com

[87] OpenAI - Morgan Stanley AI @ Morgan Stanley Assistant: https://openai.com/index/morgan-stanley

[88] Morgan Stanley - AI @ Morgan Stanley Debrief: https://www.morganstanley.com/articles/ai-debrief

[89] CNBC - Goldman Sachs GS AI Assistant: https://www.cnbc.com/2025/01/goldman-sachs-ai-assistant

[90] Bank of America Newsroom - ask MERRILL: https://newsroom.bankofamerica.com/ask-merrill

[91] Pulse2 - Wells Fargo AI Teammate: https://www.pulse2.com/wells-fargo-ai-teammate

[92] UBS - Red AI Assistant: https://www.ubs.com/red-ai-assistant

[93] WealthManagement.com - Raymond James Raimond: https://www.wealthmanagement.com/raymond-james-raimond

[94] Fintech Global - HSBC Wealth Intelligence: https://www.fintechglobal.com/hsbc-wealth-intelligence

[95] OpenAI - BNY Mellon Eliza: https://openai.com/index/bny-mellon-eliza

[96] Hubbis - Goldman Sachs AlphaAI: https://www.hubbis.com/goldman-sachs-alphaai

[97] Fidelity - Fidelity Go: https://www.fidelity.com/go

[98] PNC - Virtual Wallet: https://www.pnc.com/virtual-wallet

[99] Scotiabank - Digital Assistant: https://www.scotiabank.com/digital-assistant

[100] National Bank of Canada - AI Governance: https://www.nbc.ca/ai-governance

[101] Northern Trust - AI: https://www.northerntrust.com/ai
