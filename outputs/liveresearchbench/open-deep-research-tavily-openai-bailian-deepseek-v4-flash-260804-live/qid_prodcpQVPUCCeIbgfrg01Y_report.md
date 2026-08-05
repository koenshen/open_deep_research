# Comprehensive Cloud Provider Comparison: AWS, GCP, Azure, and Oracle Cloud Infrastructure (OCI) — August 2026

## Executive Summary

This report provides a detailed comparison of the four major cloud providers—Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure, and Oracle Cloud Infrastructure (OCI)—across five critical dimensions: pricing (US compute and storage), machine learning and AI capabilities, enterprise support, infrastructure and availability, and security and compliance. Each provider demonstrates distinct strengths: AWS leads in breadth of services and global infrastructure; GCP excels in AI/ML innovation and network performance; Azure offers unmatched enterprise integration and hybrid cloud capabilities; and OCI differentiates on pricing transparency, egress costs, and database performance. The following analysis provides specific, cited data for informed decision-making.

---

## 1. Pricing in the US (Compute and Storage)

### 1.1 Virtual Machines (On-Demand, Linux, US East)

**AWS EC2:**

| Instance Type | Specs | On-Demand Price | Spot Price |
|---|---|---|---|
| t3.medium | 2 vCPU, 4 GiB, burstable | $0.0416/hr ($30.37/mo) | $0.0180/hr |
| m5.large | 2 vCPU, 8 GiB, general purpose | $0.096/hr ($70.08/mo) | ~$0.058/hr |
| c5.xlarge | 4 vCPU, 8 GiB, compute optimized | $0.17/hr ($124.10/mo) | $0.073/hr |

AWS offers Savings Plans (up to 72% discount), Reserved Instances (up to 75%), and Spot Instances (up to 90% discount). Per-second billing applies with a 60-second minimum. Graviton (ARM) instances are 10-20% cheaper than equivalent x86 instances. [1][2][3]

**GCP Compute Engine:**

| Instance Type | Specs | On-Demand Price | Spot Price (approx.) |
|---|---|---|---|
| e2-standard-2 | 2 vCPU, 8 GiB | ~$0.067/hr ($48.55/mo) | ~$0.020/hr |
| n1-standard-2 | 2 vCPU, 7.5 GiB | $0.095/hr ($69.35/mo) | $0.0191/hr |
| c2-standard-4 | 4 vCPU, 16 GiB, compute optimized | $0.2088/hr ($152.42/mo) | ~$0.063/hr |

GCP charges per second with a 1-minute minimum. Sustained Use Discounts (SUDs) automatically apply up to 30% for usage exceeding 25% of a month. Committed Use Discounts (CUDs) offer up to 55% for 1-year and up to 70% for 3-year commitments. Spot VMs offer up to 91% discount. [4][5][6]

**Azure Virtual Machines:**

| Instance Type | Specs | On-Demand Price (approx.) | Spot Price (approx.) |
|---|---|---|---|
| B2s | 2 vCPU, 4 GiB, burstable | ~$0.0416/hr ($30.37/mo) | ~$0.0125/hr |
| D2s v3 | 2 vCPU, 8 GiB, general purpose | $0.096/hr ($70.08/mo) | ~$0.029/hr |
| F2s v2 | 2 vCPU, 4 GiB, compute optimized | $0.085/hr ($62.05/mo) | ~$0.026/hr |

Azure offers Reserved Instances (up to 72% savings), Spot VMs (up to 90% discount), Azure Savings Plan (up to 65%), and Azure Hybrid Benefit (up to 85% savings on Windows Server/SQL Server). [7][8][9]

**OCI Compute:**

| Instance Type | Specs | On-Demand Price | Notes |
|---|---|---|---|
| VM.Standard.E4.Flex (1 OCPU) | 1 OCPU (2 vCPU), 6 GB | ~$0.048/OCPU/hr | Flexible shape, per-second billing |
| VM.Standard.E4.Flex (2 OCPU) | 2 OCPU (4 vCPU), 16 GB | ~$0.096/hr | Confidential computing at no extra cost |
| VM.Standard.A1.Flex (Ampere) | Up to 76 OCPUs, Arm-based | ~$0.0255/OCPU/hr | 2 OCPUs/12 GB free tier |

OCI uses OCPU (1 OCPU = 1 physical core = 2 vCPUs). Flexible shapes allow scaling by single CPU and 1 GB increments. Preemptible instances at 50% discount. OCI claims up to 57% lower compute costs compared to AWS. [10][11][12]

**Key Pricing Insight:** For a comparable 4-vCPU, 16 GB VM, OCI is approximately $0.074/hr, compared to AWS (~$0.166/hr), GCP (~$0.194/hr), and Azure (~$0.192/hr), making OCI the most cost-effective for baseline compute. [13]

### 1.2 Serverless Computing

**AWS Lambda:**
- Requests: $0.20 per 1 million
- Duration (x86): $0.0000166667 per GB-second
- Duration (ARM/Graviton2): $0.0000133334 per GB-second (20% discount)
- Free Tier: 1 million requests + 400,000 GB-seconds per month (permanent)
- Memory range: 128 MB to 10,240 MB; max timeout: 900 seconds [14][15]

**GCP Cloud Functions (1st gen) / Cloud Run functions (2nd gen):**
- Invocations: $0.40 per million
- Compute time (GB-seconds): $0.0000025/GB-second
- Free Tier: 2 million invocations + 400,000 GB-seconds per month
- Memory: 128 MB to 8 GB for Cloud Run [16][17]

**Azure Functions:**
- Consumption Plan: $0.20 per million executions, $0.000016 per GB-second
- Free Tier: 1 million executions + 400,000 GB-seconds per month
- Flex Consumption Plan (newer): $0.000026/GB-second, $0.40 per million executions
- Memory: 512 MB to 4 GB (Flex Consumption); 1.5 GB fixed (Consumption) [18][19]

**OCI Functions:**
- Invocations: $0.0000002 per invocation (effectively $0.20 per million)
- Execution: $0.00001417 per GB-second
- Free Tier: 2 million invocations + 400,000 GB-seconds per month
- Memory: 128 MB to 2048 MB; max timeout: 5 minutes [20]

**Key Insight:** AWS Lambda and OCI Functions offer the lowest invocation costs ($0.20/M), while GCP Cloud Functions offers the lowest compute duration cost ($0.0000025/GB-second). Azure Functions is most expensive on compute duration.

### 1.3 Object Storage

**AWS S3 Standard:**
- $0.023/GB/month (first 50 TB, US East)
- 11 nines durability, sub-millisecond latency
- Glacier Deep Archive: $0.00099/GB/month (180-day minimum)
- Free Tier: 5 GB (changed to $200 credits for 6 months as of July 2025) [21][22]

**GCP Cloud Storage Standard:**
- $0.020/GB/month (regional, us-central1)
- Multi-region: $0.026/GB/month
- Archive: $0.0012/GB/month (365-day minimum)
- Free Tier: 5 GB-months Standard storage [23][24]

**Azure Blob Storage Hot:**
- $0.018/GB/month (LRS, first 50 TB)
- 22% cheaper than AWS S3 Standard
- Premium: $0.18/GB; Cool: $0.01/GB; Archive: $0.00099/GB
- Free Tier: $200 credit for 30 days [25][26]

**OCI Object Storage Standard:**
- $0.0255/GB/month (single-region)
- Infrequent Access: $0.015/GB; Archive: $0.0026/GB
- Free Tier: 20 GB total across all tiers
- Includes 10 TB/month free egress [27][28]

**Key Insight:** Azure offers the lowest hot-tier object storage at $0.018/GB/month. However, OCI's 10 TB/month free egress significantly changes total cost of ownership for data-intensive workloads. AWS S3 Standard is the most expensive headline rate at $0.023/GB.

### 1.4 Block Storage

**AWS EBS:**
- gp3: $0.08/GB/month (3,000 IOPS + 125 MB/s included)
- gp2: $0.10/GB/month
- io2: $0.125/GB/month (provisioned IOPS)
- Snapshots: $0.05/GB-month [29][30]

**GCP Persistent Disk:**
- pd-standard (HDD): $0.04/GB/month
- pd-balanced: $0.11/GB/month
- pd-ssd: $0.17/GB/month
- Snapshots: $0.05/GiB-month [31][32]

**Azure Managed Disks:**
- Standard SSD (E10, 128 GB): ~$7.95/month base + $0.0015/10K transactions
- Premium SSD (P10, 128 GB): ~$17.94/month (no transaction billing)
- Standard HDD (S10, 128 GB): ~$5.89/month
- Snapshots: $0.05/GB/month [33][34]

**OCI Block Volume:**
- Standard: $0.0255/GB/month (~$26/TB/month)
- Up to 1.3 million IO/s and 12 GB/s throughput
- Snapshots: included in pricing
- Free Tier: 200 GB total block/boot volume [35][36]

**Key Insight:** OCI offers the lowest block storage pricing at $0.0255/GB/month, which is 68% cheaper than AWS gp3 ($0.08/GB) and 85% cheaper than GCP pd-ssd ($0.17/GB).

### 1.5 File Storage

**AWS EFS:**
- Standard: $0.30/GB/month (Multi-AZ, SSD)
- Standard (One Zone): $0.16/GB/month
- EFS IA: $0.016/GB/month
- Archive: $0.008/GB/month (90-day minimum) [37]

**GCP Filestore:**
- Basic HDD: $0.16/GB/month (1 TB minimum)
- Basic SSD: $0.30/GB/month (2.5 TB minimum)
- Zonal: ~$0.26/GB/month
- Regional: ~$0.36/GB/month [38][39]

**Azure Files:**
- Standard (Transaction Optimized): ~$0.0600/GiB/month
- Standard (Hot): ~$0.0255/GiB/month
- Standard (Cool): ~$0.0150/GiB/month
- Provisioned v2 (HDD): $0.0073-$0.0183/GiB/month [40][41]

**OCI File Storage:**
- Pricing not explicitly found in research, but follows the general OCI cost structure with POSIX compliance
- Positioned as higher cost than Block Volume, lower than premium file storage [42]

**Key Insight:** Azure Files offers the lowest cost file storage options, particularly with the Provisioned v2 model at $0.0073/GiB/month. AWS EFS Standard is the most expensive at $0.30/GB/month.

---

## 2. Machine Learning and AI Services

### 2.1 Managed ML Platforms

**AWS SageMaker AI:**
- Fully managed end-to-end ML platform for building, training, and deploying custom models
- Unified Studio for data, analytics, and AI (2025-2026 update)
- Features: Autopilot, Feature Store, Data Wrangler, Pipelines, Clarify, Model Monitor, Debugger, Ground Truth, Neo, JumpStart, Canvas
- Flexible Training Plans for inference endpoints with GPU capacity reservation
- Serverless model customization with pay-per-token model
- Supports Amazon Nova, Llama, Qwen, and other models [43][44]

**GCP Vertex AI (now Gemini Enterprise Agent Platform):**
- Rebranded at Google Cloud Next 2026 as Gemini Enterprise Agent Platform
- Four core functions: Agent Studio (low-code), Agent Development Kit (ADK 1.0), Agent Runtime (long-running agents up to 7 days), governance tools
- Model Garden with 200+ models including Gemini 3.5, Claude Opus 4.7, DeepSeek-V3.2
- AutoML integrated into the platform
- Vector Search 2.0 GA with collections, auto-embeddings, hybrid search [45][46][47]

**Azure Machine Learning:**
- Full ML lifecycle management with Python SDK, Azure CLI, REST APIs, and studio
- Model catalog with hundreds of models from Azure OpenAI, Mistral, Meta, Cohere, NVIDIA, Hugging Face
- Automated ML, MLOps, Responsible AI capabilities
- No additional charge for Azure ML—only pay for underlying compute resources
- 2,107 verified companies use Azure ML as of 2026 [48][49]

**OCI Data Science:**
- Fully managed platform with JupyterLab-based environment
- Supports NVIDIA GPUs and distributed training
- AI Quick Actions for no-code deployment, fine-tuning, and evaluation of foundation models
- AutoML for feature engineering, model selection, hyperparameter tuning, model evaluation
- Integrates with Hugging Face, supports OpenAI open-weight models [50][51]

### 2.2 Foundation Model Access and APIs

**AWS Bedrock:**
- Over 100 foundation models from 18+ providers via single API
- Models include: Amazon Nova, Anthropic Claude (Opus 4.8, Sonnet 5), OpenAI GPT-5.x, Meta Llama 4, DeepSeek, Google Gemma, Mistral, Cohere, Stability AI
- Key features: Bedrock AgentCore, Knowledge Bases (RAG), Guardrails, Flows, Model Evaluation, Prompt caching (up to 90% savings), Batch inference (50% discount)
- Pricing: $0.035/MTok (Nova Micro) to $75/MTok output (Claude Opus 4.6) [52][53][54]

**GCP Gemini Enterprise Agent Platform:**
- Gemini 3.5, 3.1 Pro, 2.5 Flash models
- Agent2Agent (A2A) Protocol v1.0 in production at 150 organizations
- Google Antigravity for orchestrating multi-agent workflows
- Speach-to-Text: 125+ languages
- Translation AI: 100+ languages
- Imagen 3/4 for image generation [55][56]

**Azure OpenAI Service:**
- Enterprise-grade access to OpenAI GPT models (GPT-4, GPT-4o, GPT-5, etc.)
- LLM API Pricing (per 1M tokens, July 2026): GPT-5: $1.75 input, $14.00 output; GPT-4o: $2.50 input, $10.00 output
- Azure AI Foundry (formerly AI Studio): code-first platform with Agent Service, Knowledge, Control Plane
- Foundry Agent Service GA: managed PaaS for agent definitions, tools, and runtime
- Agent 365 governance layer with Entra ID for agents ($15/user/month) [57][58][59]

**OCI Generative AI Service:**
- Supported models: Cohere Command A, Rerank 4, Embed 4; Meta Llama 4 Scout/Maverick; NVIDIA Nemotron 3 Ultra; GLM 5.2
- OCI Generative AI Agents: combines LLMs and RAG with enterprise data
- First-class LangChain integration
- Regions: US Midwest, Brazil East, Japan Central, UK South, India South, UAE Central, Germany Central [60][61]

### 2.3 Custom AI Hardware and Training Infrastructure

**AWS:**
- **Trainium3** (December 2025): 3nm chip, 2.52 petaflops FP8, 144 GB HBM3e, 4.4x more compute than Trainium2
- **Trainium2:** Powers Trn2 instances ($44.70/hr for trn2.48xlarge); 30-50% cost savings vs H100
- **Inferentia2:** 4x higher throughput, 40% better price-performance for inference
- **Project Rainier:** Nearly 500,000 Trainium2 chips for Anthropic's Claude training [62][63]

**GCP:**
- **Ironwood (TPUv7):** 4.6 petaFLOPS per chip, scaling to 42.5 exaFLOPS superpods (announced April 2026)
- **GPU instances:** A3 High (8x H100 at ~$10.98/hr per GPU), A4 (8x NVIDIA B200 Blackwell)
- TPUv5p for scaling billion-parameter models [64][65]

**Azure:**
- **ND H100 v5:** 8x NVIDIA H100 80GB, ~$88.49-$98.32/hr
- **ND H200 v5:** Generally available, pre-integrated into Azure Batch, AKS, Azure OpenAI
- **ND GB200 V6:** 2x AI supercomputing performance over previous GPU generations
- **GPU pricing:** H100 $10.60/hr per GPU, A100 $3.67/hr, Tesla T4 $0.343/hr [66][67]

**OCI:**
- **OCI Supercluster:** Scales to 131,072 NVIDIA B200 GPUs, custom RDMA RoCE v2 (2.5-9.1 microseconds latency)
- **GPU pricing:** Flat $10/hr for H100, $10-12/hr for H200, $14-16/hr for B200
- Claims up to 220% better pricing on GPU VMs compared to competitors
- First 10 TB egress free [68][69]

---

## 3. Enterprise Support

### 3.1 Support Plans and Pricing

**AWS Support Plans:**

| Plan | Price | Key Features | Critical Response Time |
|---|---|---|---|
| Basic | Free | Documentation, re:Post, Health Dashboard | N/A |
| Business+ | $29/mo + 9% of first $10K | 24/7 support, unlimited cases, 500+ Trusted Advisor checks | <30 min |
| Enterprise | $5,000/mo + 10% first $150K | TAM, 75% DevOps Agent credits, Security Incident Response | <15 min |
| Unified Operations | $50,000/mo + 10% first $150K | TAM + DSE + Billing Specialist, Incident Detection, Proactive Monitoring | <5 min |

AWS announced a restructuring at re:Invent 2025: Developer, Business, and Enterprise On-Ramp plans will be discontinued January 1, 2027. [70][71]

**GCP Support Plans:**

| Plan | Price | Key Features | P1 Response Time |
|---|---|---|---|
| Basic | Free | Documentation, community forums, Active Assist | N/A |
| Standard | $29/mo or 3% of charges | Unlimited case users, Recommender tool | 4 hours (business hours) |
| Enhanced | $100/mo + 10% first $10K | 24/7 support, Third-Party Technology Support | 1 hour |
| Premium | $15,000/mo + 10% first $150K | Named TAM, Customer Aware Support, Event Management, 6,250 training credits | 15 minutes |

Enterprise negotiation available for $5M+ annual spend, reducing Premium Support from $12.5K list to $8K-$10K/month. [72][73]

**Azure Support Plans:**

| Plan | Price | Key Features | Sev A Response Time |
|---|---|---|---|
| Basic | Free | Self-help, Advisor, Service Health | N/A |
| Developer | $29/mo | Business hours access, third-party software support | N/A (Sev C: 8 business hours) |
| Standard | $100/mo | 24/7 support, unlimited cases | <1 hour |
| Professional Direct | $1,000/mo | ProDirect delivery managers, architecture support, webinars | <1 hour |
| Unified Enterprise | Custom | Covers all Microsoft products, Customer Success Delivery Reviews, Flex allowance | <15 minutes (Azure) |

As of July 1, 2024, Microsoft ended free Azure Standard Support for Enterprise Agreement customers. [74][75]

**OCI Support:**
- Enterprise-level support is included in base service fees for OCI services—no extra 3-10% charge like AWS/Azure
- Oracle Support Rewards: earn $0.25-$0.33 per $1 spent on OCI to reduce on-premises technical support bills
- For on-premises Oracle software: Premier Support at 22% of net license fee per year, with 4-8% annual escalator
- OCI Support: Severity 1 response within 1 hour; 24/7 phone, chat, web support [76][77]

### 3.2 Service Level Agreements (SLAs)

**AWS SLAs:**
- EC2 (Multi-AZ): 99.99% monthly uptime
- EC2 (Single Instance): 99.5%
- S3 Standard: 99.9%
- RDS (Multi-AZ): 99.95%
- Credits: <99.99% but ≥99.0% → 10%; <95.0% → 100% [78]

**GCP SLAs:**
- Compute Engine (Premium Tier, Multi-zone): ≥99.99%
- Cloud Storage (Standard multi-region): ≥99.95%
- Cloud SQL (Enterprise Plus with HA): ≥99.95%
- Cloud Spanner (multi-region): ≥99.999%
- Credits: 10% to 50% of monthly bill depending on performance [79][80]

**Azure SLAs:**
- VMs (2+ instances in Availability Zones): 99.99%
- VMs (2+ instances in Availability Set): 99.95%
- VMs (Single Instance with Premium SSD): 99.9%
- Blob Storage: ≥99.9% (99.99% for RA-GRS reads)
- SQL Database (Business Critical with zone redundancy): 99.995%
- Functions: 99.95% [81][82]

**OCI SLAs:**
- Autonomous Database: 99.995% (with Autonomous Data Guard)
- Compute: 99.995%
- Object Storage: covered under comprehensive SLA framework
- End-to-end SLAs covering availability, manageability, and performance
- Credits: <99.9% → 10%; <95% → 100% [83][84]

---

## 4. Infrastructure and Availability

### 4.1 Data Center Regions and Availability Zones

| Provider | Regions | Availability Zones | Edge Locations | Countries Served |
|---|---|---|---|---|
| **AWS** | 39 (launched), 2 planned | 123 (7 planned) | 750+ CloudFront POPs, 1,140+ embedded POPs | 245 |
| **GCP** | 43 (official), 42 (third-party) | 130 (official), 127 (third-party) | 202+ Cloud CDN PoPs | 200+ |
| **Azure** | 70+ announced, 46 GA | 35 regions support AZs | 192+ edge sites, 109 metro cities | 140 |
| **OCI** | 50+ public, 48 operational | 58 ADs (63 planned) | Global edge locations | 28+ countries |

**Sources:** [85][86][87][88]

### 4.2 Geographic Coverage and Unique Features

**AWS:** Largest global infrastructure with 39 regions and 123 availability zones. Each region has a minimum of 3 AZs physically separated by up to 60 miles. CloudFront has 750+ POPs across 100+ cities. Local Zones (45) and Wavelength Zones (33) for edge computing. Nearly 20 million kilometers of fiber optic cabling. [85]

**GCP:** 43 regions with 130 zones. Each region has 3+ zones (except us-central1 with 4). Google's global private fiber network spans 10 million kilometers. All regions connected via Google's network, using agentic AI and digital twins to reduce outage durations by up to 93%. GCP holds 13% of worldwide cloud infrastructure market (Q3 2025). [86][89]

**Azure:** Over 70 announced regions globally—more than any other cloud provider. Over 400 datacenters worldwide. 370,000+ miles of terrestrial and subsea fiber. 35 regions support availability zones, each with typically 3 AZs. Target of less than 2 ms round-trip latency between zones. Available in 140 countries. [87][90]

**OCI:** 50+ public cloud regions across 28 countries. Over 100 cloud regions when including all deployment types (public, government, sovereign, dedicated, multicloud, Alloy). Oracle's strategy is to offer at least two cloud regions in virtually every country for business continuity and data sovereignty. Oracle Interconnect for Azure (12 regions, zero data transfer charges) and Google Cloud (11 regions). OCI plans to build 100 new cloud data centers. [88][91]

### 4.3 Network Performance

- **AWS:** Fully redundant backbone with multiple 400GbE fibers. Peers with thousands of Tier 1/2/3 telecom carriers globally.
- **GCP:** 10 million km of fiber, BBR congestion control, QUIC protocol. Cheapest region: us-central1 (Iowa).
- **Azure:** 370,000+ miles of fiber. Over 190 edge sites. Four Azure US Government cloud regions.
- **OCI:** Custom RDMA over Converged Ethernet (RoCE v2) with 2.5-9.1 microseconds latency. Up to 3,200 Gb/sec cluster network bandwidth. Consistent global pricing across all regions.

---

## 5. Security and Compliance

### 5.1 Compliance Certifications

| Provider | Total Certifications | Key Standards |
|---|---|---|
| **AWS** | 143 security standards | SOC 1/2/3, ISO 27001/27017/27018/27701/20000/22301, PCI DSS Level 1, HIPAA, FedRAMP (Moderate/High), GDPR, FIPS 140-3 (Level 3), NIST 800-53/800-171, CSA STAR, C5, IRAP |
| **GCP** | 150+ global standards | SOC 1/2/3, ISO 27001/27017/27018/27701/9001/22301, PCI DSS v4.0, FedRAMP (Moderate/High), HIPAA, HITRUST, FIPS 140-3, GDPR, CCPA, C5, IRAP, ENS, TISAX, ISMAP, K-ISMS, MTCS |
| **Azure** | 100+ compliance offerings | SOC 1/2/3, ISO 27001/27017/27018/27701/9001/20000/22301, PCI DSS Level 1, FedRAMP (Moderate/High), HIPAA, HITRUST, FIPS 140-2, GDPR, C5, IRAP, ENS, TISAX, ISMAP, K-ISMS, MTCS |
| **OCI** | Comprehensive global attestations | SOC 1/2/3, ISO 27001/27017/27018/9001/42001, PCI DSS, FedRAMP (Moderate/High), DoD DISA SRG IL5, FIPS 140-2 Level 3, HIPAA, HITRUST, TX-RAMP, C5, UK Cyber Essentials, HDS, IRAP, ISMAP, ISMS, MTCS, MeitY |

**Sources:** [92][93][94][95]

### 5.2 Encryption Features

**AWS Key Management Service (KMS):**
- FIPS 140-3 Security Level 3 validated HSMs
- Key types: Symmetric, HMAC, asymmetric (RSA, ECC, SM2), post-quantum ML-DSA signing keys
- Multi-Region keys, automatic and on-demand rotation
- Custom key stores (CloudHSM-backed or External Key Store)
- Post-quantum cryptography: ML-KEM for TLS, ML-DSA for digital signatures (2025) [96][97]

**GCP Cloud KMS:**
- Default encryption at rest using AES-256 (transparent, no action needed)
- CMEK (Customer-Managed Encryption Keys)
- CSEK (Customer-Supplied Encryption Keys)
- Cloud HSM: FIPS 140-2 Level 3 certified
- External Key Manager (EKM) for keys outside Google Cloud
- Confidential VMs with AMD SEV-ES for encrypted in-use memory [98][99]

**Azure Key Vault and Microsoft Entra ID:**
- Azure Key Vault for secrets, keys, and certificates management
- FIPS 140-2 Level 2 (Standard) and Level 3 (Premium) HSMs
- Azure Disk Encryption with SSE (Server-Side Encryption)
- Microsoft Entra ID (formerly Azure AD) for identity and access management
- Azure Confidential Computing with Intel SGX and AMD SEV-SNP [100][101]

**OCI Vault:**
- FIPS 140-2 Level 3 certified HSMs
- Four vault options: Virtual Vault, Virtual Private Vault, Dedicated KMS, External KMS
- Always-on encryption at rest (AES-256) and in transit (TLS 1.2+)
- MACsec for inter-region traffic
- Security Advisor workflows enforce 4096-bit master encryption keys in Maximum Security Zones
- Oracle Data Safe for assessment, auditing, and masking [102][103]

### 5.3 Identity and Access Management (IAM)

- **AWS IAM:** Fine-grained access control with policies, roles, groups, and users. Supports identity federation, multi-factor authentication, and AWS Organizations for multi-account management.
- **GCP Cloud IAM:** Resource hierarchy (Organization → Folder → Project → Resource). Predefined and custom roles, service accounts, and identity federation.
- **Azure Microsoft Entra ID:** Enterprise-grade identity management with Conditional Access, Privileged Identity Management (PIM), and Azure RBAC. Supports hybrid identity with Active Directory.
- **OCI IAM:** Compartment-based resource hierarchy, policy-based access control, federation with identity providers, and dynamic groups for automated policy enforcement.

---

## 6. Summary Comparison Table

| Dimension | AWS | GCP | Azure | OCI |
|---|---|---|---|---|
| **Compute Pricing (4 vCPU, 16 GB, On-Demand, Linux, US East)** | ~$0.166/hr (c5.xlarge) | ~$0.194/hr (c2-standard-4) | ~$0.192/hr (D4s v5) | ~$0.074/hr (VM.Standard.E4.Flex) |
| **Object Storage (Hot Tier, per GB)** | $0.023/GB (S3 Standard) | $0.020/GB (Regional) | $0.018/GB (Blob Hot LRS) | $0.0255/GB (Standard) |
| **Block Storage (per GB)** | $0.08/GB (gp3) | $0.04/GB (pd-standard HDD) | ~$0.062/GB (Standard SSD) | $0.0255/GB (Standard) |
| **Serverless (per GB-second)** | $0.0000166667 | $0.0000025 | $0.000016 (Consumption) | $0.00001417 |
| **Free Tier (Compute)** | 750 hrs/month (12 months) | 2 million invocations, 400K GB-s (permanent) | $200 credit (30 days) + 750 hrs B-series (12 months) | 2 AMD VMs + 2 OCPU/12 GB Ampere (permanent) |
| **Free Egress** | 100 GB/month | 5 GB/month (Cloud Functions) | 100 GB/month | 10 TB/month |
| **ML Models (Foundation Models)** | 100+ (18 providers) | 200+ (Model Garden) | 100+ (Azure OpenAI + Model Catalog) | 10+ (Cohere, Meta, NVIDIA, GLM) |
| **Custom AI Chips** | Trainium3, Inferentia2 | Ironwood (TPUv7), TPUv5p | ND H100, H200, GB200 V6 | OCI Supercluster (B200, H100) |
| **Support Plan (Entry-Level Paid)** | Business+: $29/mo + 9% | Standard: $29/mo or 3% | Developer: $29/mo | Included in base fees |
| **Critical Response Time** | 15 min (Enterprise), 5 min (Unified) | 15 min (Premium) | 15 min (Unified Enterprise) | 1 hour (Severity 1) |
| **Compute SLA (Multi-AZ)** | 99.99% | 99.99% | 99.99% | 99.995% |
| **Database SLA** | 99.95% (RDS Multi-AZ) | 99.999% (Spanner) | 99.995% (SQL DB Business Critical) | 99.995% (Autonomous DB with ADG) |
| **Regions** | 39 (launched) | 43 (official) | 70+ (announced, 46 GA) | 50+ (public) |
| **Availability Zones** | 123 | 130 | 35 regions with AZs | 58 ADs |
| **Edge Locations** | 750+ POPs + 1,140+ embedded | 202+ PoPs | 192+ edge sites | Global edge network |
| **Compliance Certifications** | 143 | 150+ | 100+ | Comprehensive global attestations |
| **Encryption (HSM Level)** | FIPS 140-3 Level 3 | FIPS 140-2 Level 3 | FIPS 140-2 Level 3 (Premium) | FIPS 140-2 Level 3 |
| **Unique Differentiator** | Breadth of services, global reach | AI/ML innovation, network performance | Enterprise integration, hybrid cloud | Pricing transparency, egress costs, database performance |

---

## 7. Key Takeaways

**Pricing:** OCI offers the most aggressive pricing for compute (up to 57% lower than AWS) and block storage (68% cheaper than AWS gp3). Azure offers the lowest hot-tier object storage. GCP provides the most cost-effective serverless compute (GB-second pricing). AWS offers the most flexible discounting models (Savings Plans, Reserved, Spot).

**Machine Learning and AI:** AWS leads with the broadest model selection (100+ models from 18 providers) and custom AI hardware (Trainium3, Inferentia2). GCP's Gemini Enterprise Agent Platform represents the most advanced agentic AI platform. Azure offers the deepest enterprise AI integration with OpenAI models and Microsoft 365 ecosystem. OCI focuses on specialized AI workloads with Cohere models and competitive GPU pricing.

**Enterprise Support:** AWS and Azure offer the most comprehensive support plans, with AWS reducing minimums and response times in 2025-2026. GCP's Premium Support provides 15-minute response times with a named TAM. OCI differentiates by including enterprise-level support in base service fees, eliminating the 3-10% surcharge typical of competitors.

**Infrastructure:** AWS has the largest global footprint at 39 regions with the most edge locations. Azure has the most announced regions (70+). GCP leads in network performance with 10 million km of fiber and advanced congestion control. OCI emphasizes a "dual region per country" strategy for data sovereignty and offers unique multicloud interconnects.

**Security and Compliance:** GCP leads with 150+ compliance certifications. AWS offers 143 security standards. All four providers maintain SOC 1/2/3, ISO 27001, PCI DSS, HIPAA, and FedRAMP certifications. OCI stands out with DoD DISA SRG IL5 authorization and EU sovereign cloud regions.

---

### Sources

[1] AWS EC2 Pricing: https://aws.amazon.com/ec2/pricing/  
[2] AWS EC2 Instance Types: https://aws.amazon.com/ec2/instance-types/  
[3] AWS Savings Plans: https://aws.amazon.com/savingsplans/  
[4] GCP Compute Engine Pricing: https://cloud.google.com/compute/pricing  
[5] GCP Sustained Use Discounts: https://cloud.google.com/compute/docs/sustained-use-discounts  
[6] GCP Committed Use Discounts: https://cloud.google.com/compute/docs/committed-use-discounts  
[7] Azure Virtual Machines Pricing: https://azure.microsoft.com/en-us/pricing/details/virtual-machines/  
[8] Azure Reserved Instances: https://azure.microsoft.com/en-us/pricing/reserved-vm-instances/  
[9] Azure Spot VMs: https://azure.microsoft.com/en-us/pricing/spot/  
[10] OCI Compute Pricing: https://www.oracle.com/cloud/compute/pricing/  
[11] OCI Flexible Shapes: https://docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm  
[12] OCI Always Free Tier: https://www.oracle.com/cloud/free/  
[13] OCI vs AWS Pricing Comparison: https://www.oracle.com/cloud/price-comparison/  
[14] AWS Lambda Pricing: https://aws.amazon.com/lambda/pricing/  
[15] AWS Lambda Documentation: https://docs.aws.amazon.com/lambda/  
[16] GCP Cloud Functions Pricing: https://cloud.google.com/functions/pricing  
[17] GCP Cloud Run Pricing: https://cloud.google.com/run/pricing  
[18] Azure Functions Pricing: https://azure.microsoft.com/en-us/pricing/details/functions/  
[19] Azure Functions Documentation: https://docs.microsoft.com/en-us/azure/azure-functions/  
[20] OCI Functions Pricing: https://www.oracle.com/cloud/cloud-native/functions/pricing/  
[21] AWS S3 Pricing: https://aws.amazon.com/s3/pricing/  
[22] AWS S3 Documentation: https://docs.aws.amazon.com/s3/  
[23] GCP Cloud Storage Pricing: https://cloud.google.com/storage/pricing  
[24] GCP Cloud Storage Documentation: https://cloud.google.com/storage/docs  
[25] Azure Blob Storage Pricing: https://azure.microsoft.com/en-us/pricing/details/storage/blobs/  
[26] Azure Blob Storage Documentation: https://docs.microsoft.com/en-us/azure/storage/blobs/  
[27] OCI Object Storage Pricing: https://www.oracle.com/cloud/storage/object-storage/pricing/  
[28] OCI Object Storage Documentation: https://docs.oracle.com/en-us/iaas/Content/Object/Concepts/objectstorageoverview.htm  
[29] AWS EBS Pricing: https://aws.amazon.com/ebs/pricing/  
[30] AWS EBS Volume Types: https://aws.amazon.com/ebs/volume-types/  
[31] GCP Persistent Disk Pricing: https://cloud.google.com/compute/disks-image-pricing  
[32] GCP Persistent Disk Documentation: https://cloud.google.com/compute/docs/disks  
[33] Azure Managed Disks Pricing: https://azure.microsoft.com/en-us/pricing/details/managed-disks/  
[34] Azure Managed Disks Documentation: https://docs.microsoft.com/en-us/azure/virtual-machines/managed-disks-overview  
[35] OCI Block Volume Pricing: https://www.oracle.com/cloud/storage/block-volume/pricing/  
[36] OCI Block Volume Documentation: https://docs.oracle.com/en-us/iaas/Content/Block/Concepts/overview.htm  
[37] AWS EFS Pricing: https://aws.amazon.com/efs/pricing/  
[38] GCP Filestore Pricing: https://cloud.google.com/filestore/pricing  
[39] GCP Filestore Documentation: https://cloud.google.com/filestore/docs  
[40] Azure Files Pricing: https://azure.microsoft.com/en-us/pricing/details/storage/files/  
[41] Azure Files Documentation: https://docs.microsoft.com/en-us/azure/storage/files/  
[42] OCI File Storage Documentation: https://docs.oracle.com/en-us/iaas/Content/File/Concepts/filestorageoverview.htm  
[43] AWS SageMaker Documentation: https://docs.aws.amazon.com/sagemaker/  
[44] AWS SageMaker AI Features: https://aws.amazon.com/sagemaker/features/  
[45] GCP Gemini Enterprise Agent Platform: https://cloud.google.com/vertex-ai  
[46] GCP Model Garden: https://cloud.google.com/model-garden  
[47] GCP Agent Development Kit: https://cloud.google.com/agent-development-kit  
[48] Azure Machine Learning: https://azure.microsoft.com/en-us/services/machine-learning/  
[49] Azure Machine Learning Documentation: https://docs.microsoft.com/en-us/azure/machine-learning/  
[50] OCI Data Science: https://www.oracle.com/cloud/data-science/  
[51] OCI Data Science Documentation: https://docs.oracle.com/en-us/iaas/Content/data-science/overview.htm  
[52] AWS Bedrock: https://aws.amazon.com/bedrock/  
[53] AWS Bedrock Pricing: https://aws.amazon.com/bedrock/pricing/  
[54] AWS Bedrock Documentation: https://docs.aws.amazon.com/bedrock/  
[55] GCP Gemini Models: https://cloud.google.com/gemini  
[56] GCP AI Services: https://cloud.google.com/products/ai  
[57] Azure OpenAI Service: https://azure.microsoft.com/en-us/services/cognitive-services/openai-service/  
[58] Azure AI Foundry: https://azure.microsoft.com/en-us/products/ai-foundry  
[59] Azure OpenAI Pricing: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service/  
[60] OCI Generative AI: https://www.oracle.com/cloud/ai/generative-ai/  
[61] OCI Generative AI Documentation: https://docs.oracle.com/en-us/iaas/Content/generative-ai/overview.htm  
[62] AWS Trainium: https://aws.amazon.com/ai/machine-learning/trainium/  
[63] AWS Inferentia: https://aws.amazon.com/ai/machine-learning/inferentia/  
[64] GCP TPU Pricing: https://cloud.google.com/tpu/pricing  
[65] GCP GPU Instances: https://cloud.google.com/compute/docs/gpus  
[66] Azure GPU VMs: https://azure.microsoft.com/en-us/pricing/details/virtual-machines/linux/  
[67] Azure ND-series: https://docs.microsoft.com/en-us/azure/virtual-machines/nd-series  
[68] OCI Supercluster: https://www.oracle.com/cloud/ai/supercluster/  
[69] OCI GPU Pricing: https://www.oracle.com/cloud/compute/gpu/pricing/  
[70] AWS Support Plans: https://aws.amazon.com/premiumsupport/plans/  
[71] AWS Support SLA: https://aws.amazon.com/premiumsupport/sla/  
[72] GCP Support Plans: https://cloud.google.com/support  
[73] GCP Premium Support: https://cloud.google.com/support/premium  
[74] Azure Support Plans: https://azure.microsoft.com/en-us/support/plans/  
[75] Azure Unified Support: https://azure.microsoft.com/en-us/support/plans/unified/  
[76] OCI Support: https://www.oracle.com/cloud/support/  
[77] Oracle Support Rewards: https://www.oracle.com/cloud/support-rewards/  
[78] AWS SLA Documentation: https://aws.amazon.com/sla/  
[79] GCP Compute Engine SLA: https://cloud.google.com/compute/sla  
[80] GCP Cloud Storage SLA: https://cloud.google.com/storage/sla  
[81] Azure SLA for VMs: https://azure.microsoft.com/en-us/support/legal/sla/virtual-machines/  
[82] Azure SLA for SQL Database: https://azure.microsoft.com/en-us/support/legal/sla/sql-database/  
[83] OCI SLA Overview: https://www.oracle.com/cloud/sla/  
[84] OCI Autonomous Database SLA: https://www.oracle.com/database/autonomous-database/sla/  
[85] AWS Global Infrastructure: https://aws.amazon.com/about-aws/global-infrastructure/  
[86] GCP Cloud Locations: https://cloud.google.com/about/locations  
[87] Azure Global Infrastructure: https://azure.microsoft.com/en-us/global-infrastructure/  
[88] OCI Global Infrastructure: https://www.oracle.com/cloud/data-center-locations/  
[89] GCP Network: https://cloud.google.com/network  
[90] Azure Regions: https://azure.microsoft.com/en-us/global-infrastructure/regions/  
[91] OCI Regions: https://docs.oracle.com/en-us/iaas/Content/General/Concepts/regions.htm  
[92] AWS Compliance: https://aws.amazon.com/compliance/  
[93] GCP Compliance: https://cloud.google.com/security/compliance  
[94] Azure Compliance: https://azure.microsoft.com/en-us/overview/trusted-cloud/compliance/  
[95] OCI Compliance: https://www.oracle.com/cloud/security/compliance/  
[96] AWS KMS Features: https://aws.amazon.com/kms/features/  
[97] AWS KMS Documentation: https://docs.aws.amazon.com/kms/  
[98] GCP Cloud KMS: https://cloud.google.com/kms  
[99] GCP Encryption at Rest: https://cloud.google.com/security/encryption-at-rest  
[100] Azure Key Vault: https://azure.microsoft.com/en-us/services/key-vault/  
[101] Azure Encryption: https://docs.microsoft.com/en-us/azure/security/fundamentals/encryption-overview  
[102] OCI Vault: https://www.oracle.com/cloud/security/vault/  
[103] OCI Encryption: https://docs.oracle.com/en-us/iaas/Content/KeyManagement/Concepts/keymanagementoverview.htm
