# Comprehensive Cloud Provider Comparison: AWS, GCP, Azure, and OCI (2026)

## Executive Summary

This report provides a detailed comparison of four major cloud providers—Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure, and Oracle Cloud Infrastructure (OCI)—across five critical dimensions as of August 2026. The analysis focuses on the US market and incorporates the most recent pricing changes, service updates, and strategic shifts announced by each provider.

The cloud market in 2026 is characterized by intensifying competition, with AI workloads driving the majority of new infrastructure spending. AWS maintains the largest market share at approximately 30%, followed by Azure at 25%, GCP at 13%, and OCI at roughly 3%. Multi-cloud adoption has reached 89% among enterprises, reflecting a strategic shift away from single-vendor lock-in.

Key findings include: OCI offers the most aggressive raw compute pricing and has eliminated outbound data transfer charges entirely; GCP leads in AI/ML platform innovation with its rebranded Gemini Enterprise Agent Platform; AWS provides the deepest enterprise support ecosystem with the most extensive global infrastructure; Azure offers the strongest compliance portfolio and the most attractive pricing for Microsoft-centric enterprises; and all four providers are racing to deliver enterprise-grade generative AI capabilities with agent-first architectures.

---

## 1. Pricing in the US

### 1.1 Compute Pricing

#### On-Demand Virtual Machines

All pricing reflects Linux instances in US East regions (us-east-1 for AWS, us-central1 for GCP, East US for Azure, and US East Ashburn for OCI). Prices are per hour unless otherwise noted.

**2 vCPU / 8 GB RAM Configuration:**

| Provider | Instance Type | On-Demand Hourly | Monthly (730 hrs) |
|---|---|---|---|
| AWS | m7i.large (Intel) | $0.1008 | ~$73.58 |
| AWS | t4g.large (ARM Graviton2) | $0.0672 | ~$49.06 |
| Azure | D2s v3 (Intel) | $0.096 | ~$70.08 |
| GCP | n2-standard-2 (Intel) | $0.0971 | ~$70.90 |
| GCP | e2-standard-2 (AMD) | $0.067 | ~$48.91 |
| OCI | VM.Standard.E6 (2 OCPU = 4 vCPU, 8 GB) | $0.0450 | ~$32.85 |

*Note: 1 OCPU = 2 vCPUs for x86-based compute on OCI. OCI uses flexible shapes where CPU and memory are configured separately. Pricing is $0.0255/OCPU hour + $0.0015/GB memory hour for standard x86 VMs [Source: CloudZero OCI](https://www.cloudzero.com/blog/oracle-cloud-pricing).*

**4 vCPU / 16 GB RAM Configuration:**

| Provider | Instance Type | On-Demand Hourly | Monthly (730 hrs) |
|---|---|---|---|
| AWS | m7i.xlarge (Intel) | $0.2016 | ~$147.17 |
| AWS | m7g.xlarge (ARM Graviton4) | $0.1632 | ~$119.14 |
| Azure | D4s v3 (Intel) | $0.192 | ~$140.16 |
| GCP | n2-standard-4 (Intel) | $0.1942 | ~$141.77 |
| GCP | e2-standard-4 (AMD) | $0.1340 | ~$97.84 |
| OCI | VM.Standard.E6 (2 OCPU = 4 vCPU, 16 GB) | $0.0750 | ~$54.75 |

OCI is consistently the cheapest for raw on-demand compute. Oracle claims a 4 vCPU, 16 GB RAM instance costs **$54/month** on OCI versus 2.1-2.3 times more on AWS, Azure, and GCP [Source: Oracle Cloud Pricing](https://www.oracle.com/cloud/pricing). For a 2 CPU, 8 GB instance, EffectiveSoft found OCI at $38.69/month compared to $70.08 on AWS and Azure [Source: EffectiveSoft](https://www.effectivesoft.com/blog/cloud-pricing-comparison.html).

Among the Big Three, GCP's e2-series (AMD) offers the lowest on-demand pricing at $0.134/hr for 4 vCPU/16 GB, while AWS and Azure are nearly identical for equivalent x86 instances [Source: shattered.io](https://shattered.io/aws-vs-azure-vs-gcp-2026).

**ARM Instance Pricing:** All three major providers offer ARM-based instances at approximately 20% lower on-demand pricing than equivalent x86 instances. AWS Graviton4, Azure Cobalt 100, and GCP Tau T2A deliver roughly 40% better price-performance than x86 across all three providers [Source: Usage.ai](https://www.usage.ai/blogs/finops/multi-cloud/cloud-pricing-comparison). OCI's Ampere A1 shapes are significantly cheaper, with the first 3,000 OCPU-hours and 18,000 GB-hours per month free.

#### Reserved Instance and Commitment Discounts

**AWS Savings Plans and Reserved Instances:**
- Compute Savings Plans (most flexible): Up to 66% off on-demand, covering EC2, Fargate, and Lambda across any instance family and region [Source: CloudZero](https://www.cloudzero.com/blog/aws-savings-plans)
- EC2 Instance Savings Plans (locked to family/region): Up to 72% off
- Standard Reserved Instances: Up to 72% discount for 1-year or 3-year terms
- Convertible RIs: Up to 66% discount, exchangeable across families
- Spot Instances: Up to 90% off on-demand, reclaimable with 2-minute warning
- Payment options: All Upfront (largest discount), Partial Upfront, or No Upfront [Source: AWS EC2 Pricing](https://aws.amazon.com/ec2/pricing/reserved-instances/pricing)

**Azure Reserved Instances and Savings Plans:**
- Reserved VM Instances: Up to 72% savings compared to pay-as-you-go (1-year or 3-year terms)
- Azure Savings Plan for Compute: Up to 65% savings, more flexible across regions, VM types, and OS
- Azure Hybrid Benefit: When combined with Reserved Instances, can reduce Windows Server or SQL Server workload costs by up to 85% [Source: CloudZero](https://www.cloudzero.com/blog/azure-reservations-vs-savings-plans)
- **Important: As of July 1, 2026**, Azure retired new purchases and renewals of Reserved VM Instances for select legacy VM series (Av2, Dv2/Dsv2, Dv3/Dsv3, Ev3/Esv3, F/Fs/Fsv2, G/Gs, Ls/Lsv2). Existing RIs are honored through their full term. Microsoft recommends transitioning to Azure Savings Plans or newer VM generations [Source: Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-machines/prepay-reserved-vm-instances).

**GCP Committed Use Discounts (CUDs) and Sustained Use Discounts (SUDs):**
- SUDs: Automatic, up to 30% off for running N1/N2/N2D/C2/M1/M2 instances more than 25% of the month. No commitment required. Not available on E2, C3, C4, N4, or accelerator-optimized families [Source: CloudZero](https://www.cloudzero.com/blog/google-cloud-compute-engine-pricing-guide)
- Resource-based CUDs: Up to 55% off for standard machine types, up to 70% for memory-optimized (3-year terms)
- Compute Flexible CUDs (spend-based): 28% (1-year), 46% (3-year) for most series
- Spot VMs: Up to 91% off on-demand, interruptible

**OCI Reserved Instances and Universal Credits:**
- Pay-as-you-go: Per-second billing for compute, per GB-month for storage
- Universal Credits: Prepaid committed spend with volume discounts. Estimated discounts: ~20% for 1-year, ~40% for 3-year commitments
- Average discount off PAYG based on 200+ enterprise contracts: 40-70% [Source: VendorBenchmark](https://vendorbenchmark.com/vendors/oracle-cloud-infrastructure-pricing)
- Preemptible Instances: 50% of regular pricing
- Unused Capacity reservations: 85% of regular instances

#### 2026 Pricing Changes

- **Google Cloud** cut compute pricing by 8% across all regions in Q1 2026 [Source: Tech Insider](https://tech-insider.org/aws-vs-azure-vs-google-cloud-2026)
- **GCP** adjusted multi-region storage pricing: Nearline multi-region increased from $0.010/GB to $0.015/GB per month; Archive multi-region in US/EU decreased from $0.004/GB to $0.0024/GB per month [Source: CloudZero](https://www.cloudzero.com/blog/gcp-storage-pricing)
- **Azure** introduced Smart Tier (GA April 2026) which automates blob movement between Hot, Cool, and Cold tiers [Source: SpendArk](https://spendark.com/blog/azure-pricing-changes-2026)
- **Azure** paused a planned 128 KiB minimum billable object size for Cool/Cold/Archive tiers on June 8, 2026, before it took effect [Source: SpendArk](https://spendark.com/blog/azure-pricing-changes-2026)
- **AWS Free Tier** changed July 15, 2025: new accounts now get up to $200 in credits for 6 months instead of 12 months of free tier instances [Source: CloudZero](https://www.cloudzero.com/blog/s3-pricing)
- **OCI** eliminated all outbound data transfer charges across its full commercial footprint as of February 2026, making egress $0 across all regions, all compute shapes [Source: Spheron](https://www.spheron.network/blog/oracle-cloud-oci-gpu-pricing-2026)

#### Serverless Compute Pricing

**AWS Lambda** (us-east-1): $0.20 per 1 million requests, $0.0000166667/GB-second for x86 (Tier 1), with ARM/Graviton2 at 20% cheaper. Free tier: 1 million requests + 400,000 GB-seconds per month (perpetual) [Source: CostGoat](https://costgoat.com/pricing/aws-lambda).

**Azure Functions** (Consumption Plan): $0.20 per million executions, $0.000016/GB-second. Free tier: 1 million requests + 400,000 GB-seconds per month. Flex Consumption Plan (recommended): $0.000026/GB-second with Always Ready features [Source: Modal](https://modal.com/blog/azure-function-pricing-guide).

**Google Cloud Functions** (1st Gen): $0.40 per million invocations, $0.0000100/GHz-second, $0.0000025/GB-second. Free tier: 2 million invocations + 200,000 GHz-seconds + 400,000 GB-seconds per month [Source: Google Cloud Pricing](https://cloud.google.com/functions/pricing-1stgen).

**Oracle Functions**: $0.20 per million invocations, $0.00001417/GB-second. Free tier: 2 million invocations + 400,000 GB-seconds per month. Based on the open source Fn Project [Source: srvrlss.io](https://www.srvrlss.io/provider/oracle-cloud-functions).

### 1.2 Storage Pricing

#### Object Storage (per GB per month, US East, single-region/LRS)

| Tier | AWS S3 | Azure Blob | GCP Cloud Storage | OCI Object Storage |
|---|---|---|---|---|
| Standard/Hot | $0.023 | $0.018 | $0.020 | $0.0255 |
| Infrequent Access/Cool | $0.0125 (S3 Standard-IA) | $0.01 | $0.01 (Nearline) | $0.015 |
| Cold | $0.004 (Glacier Instant Retrieval) | $0.0045 | $0.004 (Coldline) | N/A |
| Archive | $0.00099 (Glacier Deep Archive) | $0.00099 | $0.0012 | $0.0026 |

**Key findings:** Azure's Hot tier is the cheapest at $0.018/GB (LRS), 22% cheaper than AWS S3 Standard at $0.023/GB [Source: nOps](https://www.nops.io/blog/azure-storage-pricing). For archive storage, AWS Glacier Deep Archive and Azure Blob Archive are tied at $0.00099/GB/month—the cheapest options. OCI Object Storage is the most expensive for standard tier at $0.0255/GB but includes 10 TB free egress per month [Source: Finout](https://www.finout.io/blog/cloud-storage-pricing-comparison).

#### Block Storage (per GB per month, US East)

| Provider | Volume Type | Price/GB/month |
|---|---|---|
| AWS EBS | gp3 | $0.08 (includes 3,000 IOPS and 125 MB/s throughput) |
| Azure | Premium SSD v2 | $0.08-$0.12/GiB (decoupled pricing) |
| GCP | Persistent Disk Balanced | $0.11/GiB |
| GCP | Persistent Disk SSD | $0.17-$0.19/GiB |
| OCI | Block Volume (Balanced) | $0.0255 (all performance included, up to 60 IOPS/GB) |

OCI Block Volume is the cheapest at $0.0255/GB/month, claiming 4-5 times less than competitors [Source: CloudZero](https://www.cloudzero.com/blog/oracle-cloud-pricing). AWS EBS gp3 is the recommended default for AWS, 20% cheaper than gp2. GCP Persistent Disk SSD is the most expensive among standard SSD options at $0.17-$0.19/GB.

#### File Storage (per GB per month, US East)

| Provider | Service | Tier | Price/GB/month |
|---|---|---|---|
| AWS EFS | EFS Standard (Regional) | Standard | $0.30 |
| AWS EFS | EFS One Zone | Standard | $0.16 |
| Azure Files | Premium SSD (Provisioned v2) | Premium | $0.1001-$0.1249/GiB |
| Azure Files | Standard HDD (Pay-as-you-go) | Hot | $0.0255-$0.0593/GiB |
| Azure Files | Standard HDD (Pay-as-you-go) | Cool | $0.015-$0.0338/GiB |
| GCP Filestore | Basic HDD | HDD | ~$0.16/GiB |
| GCP Filestore | Basic SSD | SSD | ~$0.30/GiB |
| OCI File Storage | File Storage | Standard | $0.30/GB |

Azure Files (Standard HDD Cool) is the cheapest at $0.015-$0.0338/GiB. AWS EFS can be significantly reduced with lifecycle management, achieving effective costs as low as $0.0315/GB by automatically moving data to IA and Archive tiers [Source: CloudZero](https://www.cloudzero.com/blog/aws-efs-pricing).

#### Data Egress Costs

Data egress is a significant hidden cost that can exceed storage costs. The providers differ dramatically:

| Provider | First 10 TB/month | Beyond 10 TB | Free Tier |
|---|---|---|---|
| AWS | $0.09/GB | Decreasing tiers to $0.05/GB (150+ TB) | 100 GB/month free |
| Azure | $0.087/GB | Similar tiered pricing | 5-100 GB/month free |
| GCP | $0.12/GB (first 1 TB), $0.11/GB (1-10 TB) | $0.08/GB (10+ TB) | 5-100 GB/month free |
| OCI | $0.00/GB (first 10 TB/month free) | ~$0.0085/GB | 10 TB/month free |

OCI is dramatically cheaper for egress: 10 TB free per month, then $0.0085/GB—roughly 10 times cheaper than AWS/Azure and 14 times cheaper than GCP. As of February 2026, OCI eliminated all outbound data transfer charges across its full commercial footprint [Source: Spheron](https://www.spheron.network/blog/oracle-cloud-oci-gpu-pricing-2026). GCP is the most expensive for egress at $0.12/GB for the first 1 TB, 33% more than AWS ($0.09/GB) and 38% more than Azure ($0.087/GB).

---

## 2. Machine Learning and AI Services

### 2.1 Managed ML Platforms

#### Amazon SageMaker AI

SageMaker remains the heavyweight champion of custom machine learning, offering an end-to-end ecosystem for building, training, and deploying ML models. Key components include SageMaker Studio (IDE), Autopilot (AutoML), Feature Store, Data Wrangler, Pipelines (MLOps), Clarify (bias detection and explainability), Model Monitor, and JumpStart (600+ pre-trained models for one-click deployment) [Source: DEV Community](https://dev.to/aws-builders/the-aws-aiml-landscape-in-2026-simplified-17i3).

SageMaker HyperPod supports training 100B+ parameter models with automatic fault recovery and 99.9% uptime during 6-week training cycles. AWS Inferentia3 chips reduce LLM inference costs by 58%. SageMaker Serverless Inference scales to zero, providing a genuine advantage for development environments [Source: AgileSoftLabs](https://www.agilesoftlabs.com/blog/2026/06/gcp-vs-aws-for-ml-workloads-in-2026).

Pricing: Pay-as-you-go with free tier (250 notebook hours), Savings Plans up to 64% off. H100 on SageMaker runs $8.60-$10.80/hr per accelerator. AWS cut H100 prices 44% in late 2025 [Source: AgileSoftLabs](https://www.agilesoftlabs.com/blog/2026/06/gcp-vs-aws-for-ml-workloads-in-2026).

Market share: AWS holds 34% of the cloud ML market [Source: Ankur's Newsletter](https://www.ankursnewsletter.com/p/azure-ml-vs-vertex-ai-vs-sagemaker).

#### Google Vertex AI → Gemini Enterprise Agent Platform (2026 Rebrand)

In a major strategic shift for 2026, Vertex AI has been rebranded and replaced by the **Gemini Enterprise Agent Platform**. This is not just a rename—it's an evolution to include agent services (Agent Studio, Agent Gateway, Agent Identity, Agent Registry). All previous Vertex AI features (Model Garden, Custom Training, AutoML, Model Registry, Endpoints, Pipelines) are now subsumed under the "Models" menu within Agent Platform. Searching for Vertex AI in the Google Cloud Console redirects to Agent Platform, and Vertex AI documentation is no longer being updated [Source: GCP Study Hub](https://gcpstudyhub.com/blog/vertex-ai-replaced-by-gemini-enterprise-agent-platform).

The Agent Platform is structured around four pillars:
- **Build**: Agent Garden (prebuilt agents/templates), ADK (open-source agent framework), MCP Servers, RAG Engine, Vector Search 2.0
- **Scale**: Deployments, Memory Bank (cross-session long-term memory), Sessions
- **Govern**: Agent Registry, Policies, Gateways (enforcing Model Armor), Security (Agent Identity + threat scanning)
- **Optimize**: Topology (visual map of agent connections), Evaluation (testing with simulations and live monitoring)

Key deprecations include Vertex AI Extensions (shutdown after November 26, 2026), Vertex Explainable AI (deprecated March 16, 2026), and Vertex AI Feature Store (legacy deprecated February 17, 2026) [Source: Google Cloud](https://docs.cloud.google.com/vertex-ai/docs/release-notes).

Training costs: TPU v5p on GCP runs ~$4.20/hr on-demand. Vertex AI is 28% cheaper for training ($612 vs $847 for 72-hour run) and 35% cheaper for inference compared to SageMaker. However, teams should consider the "engineering tax" of JAX rewrites for TPU optimization [Source: AgileSoftLabs](https://www.agilesoftlabs.com/blog/2026/06/gcp-vs-aws-for-ml-workloads-in-2026).

Market share: GCP holds 22% of the cloud ML market [Source: Ankur's Newsletter](https://www.ankursnewsletter.com/p/azure-ml-vs-vertex-ai-vs-sagemaker).

#### Azure Machine Learning (Microsoft Foundry)

Azure Machine Learning is now part of **Microsoft Foundry** (formerly Azure AI Studio, then Azure AI Foundry). The platform offers a catalog of 11,000+ models (OpenAI, Anthropic, Meta, Google, xAI, Hugging Face, Microsoft MAI), a Foundry Agent Service for building AI agents, and Azure Machine Learning for custom models [Source: Voiceflow](https://www.voiceflow.com/blog/microsoft-azure).

Key capabilities include Automated Machine Learning (no-code training), forecasting with time series, drag-and-drop visual interface, ONNX Runtime for cross-platform deployment, and MLflow integration. Azure ML is best for regulated industries (healthcare/finance) with 93+ compliance certifications, confidential computing via Intel SGX v4, and hybrid deployments through Arc-enabled clusters supporting 150+ edge sites [Source: Ankur's Newsletter](https://www.ankursnewsletter.com/p/azure-ml-vs-vertex-ai-vs-sagemaker).

Market share: Azure holds 29% of the cloud ML market [Source: Ankur's Newsletter](https://www.ankursnewsletter.com/p/azure-ml-vs-vertex-ai-vs-sagemaker).

#### Oracle OCI Data Science

OCI Data Science is a fully managed platform for data scientists to build, train, deploy, and manage ML models using Python and open source tools. Key features include JupyterLab-based environment, NVIDIA GPU support for distributed training, and MLOps capabilities with automated pipelines and model monitoring. The platform supports large language models through Hugging Face and other frameworks [Source: Oracle](https://www.oracle.com/artificial-intelligence/data-science).

Oracle announced the **Oracle AI Data Platform** at Oracle AI World 2025, backed by over $1.5 billion in collective investment. The platform is designed to connect generative AI models with enterprise data, applications, and workflows. It was named an Overall Leader in the ISG Buyers Guide for AI and Data Platforms 2026 [Source: Oracle](https://www.oracle.com/ai-data-platform).

### 2.2 Pre-built AI Services

#### Vision Services

| Provider | Service | Key Features |
|---|---|---|
| **AWS** | Rekognition | Object detection, facial analysis, content moderation, PPE detection; 95% inappropriate content blocked at $0.001/image [Source: Codilime](https://codilime.com/blog/practical-guide-aws-ai-services) |
| **Azure** | Azure Vision (Foundry Tools) | Image Analysis, Spatial Analysis; 99.9% SLA for Standard tier; retires September 25, 2028 [Source: Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/whats-new) |
| **GCP** | Vision AI (Agent Platform) | Integrated into Gemini Enterprise Agent Platform |
| **OCI** | OCI Vision | Deep-learning image analysis, custom model training, Stored Video Analysis (GA); Free Tier available [Source: Oracle](https://www.oracle.com/artificial-intelligence/vision) |

#### Natural Language Processing

| Provider | Service | Key Features |
|---|---|---|
| **AWS** | Comprehend | Sentiment analysis, entity recognition, PII detection, custom classification; 60% faster ticket routing for customer support [Source: Codilime](https://codilime.com/blog/practical-guide-aws-ai-services) |
| **Azure** | Azure Language (Foundry Tools) | Named entity recognition, sentiment analysis, summarization, question answering; Free tier: 5,000 transactions/month |
| **GCP** | Natural Language (Agent Platform) | Integrated into Gemini Enterprise Agent Platform |
| **OCI** | OCI Language | Sentiment analysis, entity recognition, content classification (600+ categories), language detection (100+ languages), translation (30 languages), custom model training; HIPAA and FedRAMP compliant; OCI Language 3.0 GA [Source: Oracle](https://www.oracle.com/artificial-intelligence/language) |

#### Speech Services

| Provider | Service | Key Features |
|---|---|---|
| **AWS** | Transcribe & Polly | Speech-to-text with 99%+ accuracy, speaker diarization, call analytics, 60+ language TTS with neural voices |
| **Azure** | Azure Speech (Foundry Tools) | MAI-Transcribe-1, MAI-Voice-1, LLM Speech API (GA June 2026), GPT-transcribe; Free tier: 5 audio hours/month |
| **GCP** | Speech-to-Text & Text-to-Speech (Agent Platform) | Integrated into Gemini Enterprise Agent Platform |
| **OCI** | OCI Speech | Multilingual Real-Time ASR (Whisper model, 57 languages), Neural TTS (limited availability), diarization, async ASR with 50% latency reduction; Free Tier available [Source: Oracle](https://www.oracle.com/artificial-intelligence/speech) |

### 2.3 Generative AI Services

#### AWS Bedrock

Amazon Bedrock provides access to leading foundation models through a single API, including Anthropic Claude (Opus 4.7, Sonnet 4.6, Haiku 4.5), Amazon Titan, Meta Llama 4, AI21 Labs Jurassic, Cohere Command, Stability AI, DeepSeek V3.2, Mistral AI, Google Gemma, OpenAI GPT-5.6 series, NVIDIA Nemotron, xAI Grok, and more [Source: AWS](https://aws.amazon.com/bedrock/pricing).

Core features include Knowledge Bases for RAG, Autonomous Agents, Guardrails (blocks up to 88% of harmful content with 99% accuracy), Custom Model Import, Prompt Caching (up to 90% reduction on input token costs), Intelligent Prompt Routing, and Batch Inference (50% discount vs. on-demand).

Pricing examples (us-east-1, per million tokens): Claude Opus 4.7: $5 input / $25 output; Claude Sonnet 4.6: $3 input / $15 output; DeepSeek V3.2: $0.62 input / $1.85 output; Amazon Nova Micro: $0.035 input / $0.14 output (143x cheaper than Opus) [Source: CloudZero](https://www.cloudzero.com/blog/amazon-bedrock-pricing).

New services include Amazon Q family (developer and business), Kiro (agentic IDE), Amazon Nova Act (UI automation agent), and Amazon Bedrock AgentCore [Source: DEV Community](https://dev.to/aws-builders/the-aws-aiml-landscape-in-2026-simplified-17i3).

#### Google Gemini Enterprise Agent Platform (Generative AI)

The Agent Platform provides access to Google's Gemini models including Gemini 3.1 Pro Preview (1M token context window), Gemini 3.1 Flash-Lite (most cost-efficient), Gemini 3.1 Flash Image (image generation), and partner models including Claude Opus 4.7, DeepSeek-V3.2, Qwen3-Coder, Mistral Codestral 2, and OpenAI gpt-oss models [Source: Google Cloud](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/release-notes).

Key statistics from Google Cloud Next '26: Nearly 75% of Google Cloud customers use AI products, 16 billion tokens processed per minute via API, 40% QoQ growth in Gemini Enterprise paid monthly active users [Source: Google Cloud Blog](https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26).

Pricing: Gemini 2.0 Flash at $0.075/million tokens vs. Claude Sonnet at ~$3.00/million = 30-40x cost difference. Processing 10B tokens/month = $750 with Gemini vs $30,000+ with Claude [Source: AgileSoftLabs](https://www.agilesoftlabs.com/blog/2026/06/gcp-vs-aws-for-ml-workloads-in-2026).

#### Azure OpenAI Service (Microsoft Foundry)

Azure OpenAI Service provides access to OpenAI's models through Azure, including GPT-5 series (GPT-5, GPT-5-mini, GPT-5-nano), GPT-4 series (GPT-4.1, GPT-4o), reasoning models (o3, o4-mini), audio models (GPT-4o-transcribe, GPT Realtime API), image models (GPT-image-1, DALL-E), and video generation (Sora) [Source: Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/whats-new).

Pricing: GPT-5: $5 input / $20 output per 1M tokens; GPT-5-mini: $0.50 / $2.00; GPT-5-nano: $0.05 / $0.40; o3: $10.00 / $40.00 per 1M tokens. Batch API offers 50% off with 24-hr SLA. Provisioned Throughput Units (PTUs) deliver up to 70% savings for sustained workloads [Source: CloudZero](https://www.cloudzero.com/blog/azure-openai-pricing).

Azure OpenAI is authorized for all U.S. Government data classification levels (April 16, 2025) and is covered under Microsoft Online Services BAA (HIPAA), FedRAMP High in Azure Government [Source: Microsoft Learn](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/whats-new).

#### Oracle OCI Generative AI Service

OCI Generative AI provides access to leading foundation models including Cohere (Command R, Command R+, Embed, Rerank 4), Meta Llama, xAI Grok, Google Gemini, OpenAI gpt-oss-20b and gpt-oss-120b, NVIDIA Nemotron 3 Ultra, and Alibaba Qwen. The service offers two modes: On-Demand (pay-as-you-go) and Dedicated (reserved GPU capacity for production workloads).

OCI Enterprise AI (GA) provides end-to-end capabilities for building, deploying, and governing AI agents with built-in IAM, guardrails, observability, and auditability. Sovereign AI options are available for data hosting and processing [Source: Oracle](https://www.oracle.com/artificial-intelligence/enterprise-ai).

### 2.4 Enterprise-Grade AI Tools and Responsible AI

#### AWS Responsible AI

AWS defines responsible AI through eight dimensions: fairness, explainability, privacy and security, safety, controllability, veracity and robustness, governance, and transparency. Key tools include SageMaker Clarify (bias detection and model explainability—note: no longer open to new customers as of 2026), SageMaker Model Monitor (data quality and drift monitoring), Bedrock Guardrails (blocks up to 88% of harmful content with 99% accuracy), Model Evaluation, and AWS AI Service Cards for transparency [Source: AWS](https://aws.amazon.com/ai/responsible-ai).

#### Google Cloud Responsible AI

Google's AI Principles (since 2018) guide six dimensions: fairness, interpretability & transparency, security & privacy, reliability & safety, accountability & governance, and social & environmental benefits. With the deprecation of Vertex Explainable AI (March 16, 2026), the primary governance tools are now within the Agent Platform: Model Armor (content filtering through Gateways), Agent Policies, and Agent Gateway (secure connectivity). The Agent Platform includes a structured risk assessment framework using BigQuery and automated model risk detection [Source: Google Cloud](https://cloud.google.com/responsible-ai).

#### Azure Machine Learning Responsible AI

Microsoft's Responsible AI Standard encompasses six principles: fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability. The Responsible AI Dashboard integrates multiple tools: Fairlearn (fairness assessment), Error Analysis (identifying high-error subsets), InterpretML (model interpretability), DiCE (counterfactual what-if analysis), and EconML (causal inference). The Responsible AI Scorecard provides customizable PDF reports for stakeholders. Microsoft released an open-source Agent Governance Toolkit in April 2026 addressing all 10 OWASP agentic AI risks [Source: Microsoft Learn](https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai?view=azureml-api-2).

#### Oracle Responsible AI

Oracle emphasizes enterprise-grade security, privacy, and governance built into its AI services. Key features include zero data retention endpoints (customer data not used for model training), HIPAA and FedRAMP compliance, two-layer security model (OCI IAM + fine-grained access control), AI Registry for centralized agent management, and comprehensive audit logs. The OCI AI Data Platform includes an AI Data Catalog with lineage-tracked pipelines and RBAC [Source: Oracle](https://www.oracle.com/artificial-intelligence/ai-services).

---

## 3. Enterprise Support

### 3.1 Support Plan Tiers and Pricing

#### AWS Support Plans

AWS offers three current paid support plans as of August 2026: **Business Support+**, **Enterprise Support**, and **Unified Operations**. Basic Support is free for all customers. Several older plans (Developer Support, Business Support, and Enterprise On-Ramp) are being discontinued on January 1, 2027 [Source: AWS](https://aws.amazon.com/premiumsupport/pricing).

| Plan | Minimum | Pricing Structure | Key Features |
|---|---|---|---|
| **Basic** (Free) | $0 | Included | Documentation, health dashboard, limited Trusted Advisor checks |
| **Business Support+** | $29/month | 9% (up to $10K), 7% ($10K-$80K), 5% ($80K-$250K), 3% (over $250K) | 24/7 phone/web/chat, 30-min critical response, 500+ Trusted Advisor checks, support API |
| **Enterprise Support** | $5,000/month | 10% (up to $150K), 7% ($150K-$500K), 5% ($500K-$1M), 3% (over $1M) | Designated TAM, 15-min critical response, AWS Security Incident Response, strategic reviews |
| **Unified Operations** | $50,000/month | 10% (up to $1M), 6% ($1M-$5M), 5% (over $5M) | TAM + Domain Engineer + Senior Billing Specialist, 5-min critical response, AWS Countdown Premium included |

**Pricing examples:** For $20K monthly charges, Business Support+ costs $1.6K. For $750K, Enterprise Support costs $52K. For $1.5M, Unified Operations costs $130K [Source: AWS](https://aws.amazon.com/premiumsupport/pricing).

**Negotiation insight:** Enterprises that bundle support negotiations with their primary commitment renewals (EDP, EA, CUD) achieve support discounts of 25-45%, versus 5-15% when support is negotiated separately. At $10M annual spend, AWS Enterprise Support at list rate is approximately 7x more expensive than GCP Premium Support [Source: VendorBenchmark](https://vendorbenchmark.com/blog/cloud-support-plan-pricing-benchmark-comparison).

#### Azure Support Plans

Azure offers five support plans: Basic (free), Developer ($29/month), Standard ($100/month), Professional Direct ($1,000/month), and Unified Enterprise (pricing varies) [Source: Microsoft Azure](https://azure.microsoft.com/en-us/support/plans).

| Plan | Price | Key Features |
|---|---|---|
| **Basic** (Free) | $0 | Billing/subscription management, Azure Advisor, Azure Health Status |
| **Developer** | $29/month | Business hours access, Sev C response within 8 business hours |
| **Standard** | $100/month | 24/7 technical support, Sev A within 1 hour, Sev B within 4 hours, Sev C within 8 hours |
| **Professional Direct** | $1,000/month | ProDirect delivery managers, support API, Sev A within 1 hour, Sev B within 2 hours, Sev C within 4 hours |
| **Unified Enterprise** | Varies | Customer Success Account Managers, escalation management, health assessments, Mission Critical Services, Flex Allowance |

**Azure Rapid Response** (add-on to Unified Enterprise): Sev A+ within 15 minutes, Sev B within 2 hours, Sev C within 4 hours [Source: Microsoft Azure](https://azure.microsoft.com/en-us/support/plans/response).

**Important note:** As of July 1, 2024, Microsoft ended its free Azure Standard Support offer for customers using Enterprise Agreements (EA) or Microsoft Customer Agreements (MCA-E) [Source: US Cloud](https://www.uscloud.com/blog/how-much-is-microsoft-azure-enterprise-support).

#### GCP Support Plans

Google Cloud offers four support tiers: Basic (free), Standard ($29/month min), Enhanced ($100/month min), and Premium ($15,000/month min) [Source: Google Cloud](https://cloud.google.com/support/premium).

| Plan | Minimum | Pricing Structure | Key Features |
|---|---|---|---|
| **Basic** (Free) | $0 | Included | Documentation, community forums, billing support |
| **Standard** | $29/month | 3% of monthly charges (whichever is higher) | Case creation, P2 response within 4 business hours, English-only, email-based |
| **Enhanced** | $100/month | 10% (first $0-$10K), 7% ($10K-$80K), 5% ($80K-$250K), 3% (over $250K) | 24/7 response, multilingual (English, Japanese, Mandarin, Korean, French), P1 within 1 hour, optional TAA |
| **Premium** | $15,000/month | 10% (first $0-$150K), 7% ($150K-$500K), 5% ($500K-$1M), 3% (over $1M) | Dedicated TAM, 15-min P1 response, Cloud Skills Boost, Operational Health Reviews, Event Management |

**Response times by tier:** Standard: P2 within 4 hours (business hours only); Enhanced: P1 within 1 hour, P2 within 4 hours, P3/P4 within 8 hours; Premium: P1 within 15 minutes, P2 within 2 hours, P3 within 4 hours, P4 within 8 hours [Source: Google Cloud](https://cloud.google.com/support/premium).

**Key pricing insight:** At $10M annual spend, GCP Premium Support at negotiated rates ($8K-$10K/month for $5M+ EA customers) is significantly cheaper than AWS Enterprise Support [Source: VendorBenchmark](https://vendorbenchmark.com/blog/cloud-support-plan-pricing-benchmark-comparison).

#### OCI Support

Oracle Cloud Infrastructure takes a fundamentally different approach: **"The base fees for OCI services include enterprise-ready support for those services—there is no extra charge for technical support of production workloads using OCI"** [Source: Oracle](https://www.oracle.com/cloud/pricing).

Unlike competitors charging 3-10% of prior month/year for support, Oracle includes enterprise support for production workloads at no extra charge. Oracle Support Rewards allow customers to earn $0.25-$0.33 in rewards for every $1 spent on OCI, applied to reduce on-premises technical support costs, potentially to zero [Source: Oracle](https://www.oracle.com/cloud/pricing).

### 3.2 Service Level Agreements (SLAs)

#### Compute SLAs

| Configuration | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| Multi-AZ/Multi-Zone | 99.99% | 99.99% | 99.99% | 99.99% |
| Single Instance (Premium) | 99.5% | 99.9% (Premium SSD) | 99.9% (non-memory optimized) | 99.99% |
| Single Instance (Standard) | 99.5% | 99.5% (Standard SSD) | 99.5% (Standard Tier) | 99.99% |

**AWS EC2:** Region-Level SLA (deployed across two or more AZs): 99.99% monthly uptime. Instance-Level SLA: 99.5% for each individual instance. AWS will not charge for any single EC2 instance unavailable for more than six minutes of a clock hour (applied automatically) [Source: AWS](https://aws.amazon.com/compute/sla).

**Azure VMs:** Multi-instance across Availability Zones: 99.99%. Multi-instance in same Availability Set: 99.95%. Single instance with Premium SSD: 99.9%. Single instance with Standard SSD: 99.5%. Single instance with Standard HDD: 95% [Source: Microsoft Azure](https://www.azure.cn/en-us/support/sla/virtual-machines).

**GCP Compute Engine (Premium Tier):** Multiple Zones: 99.99%. Single Instance (Memory Optimized): 99.95%. Single Instance (all other families): 99.9% [Source: Google Cloud](https://cloud.google.com/compute/sla).

**OCI Compute:** OCI provides approximately 99.99% SLA for virtual machines. Oracle claims to be the first cloud vendor to offer performance SLAs, guaranteeing infrastructure performance greater than 90% of published performance, 99.9% of the time [Source: Oracle](https://www.oracle.com/cloud/sla).

#### Other Service SLAs

| Service | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| Object Storage | 99.9% (S3 Standard) | 99.9% (Blob) | 99.95% (Multi-Regional) | 99.9% |
| Database (Multi-AZ) | 99.95% (RDS) | 99.99% (SQL Database) | 99.999% (Spanner multi-region) | 99.995% (Autonomous DB) |
| Load Balancing | 99.99% | 99.99% | 99.99% | 99.99% |
| DNS | 100% | 100% | 100% | 100% |

### 3.3 Enterprise Support Experience

**AWS** offers the most comprehensive support ecosystem with AI-powered assistance, designated Technical Account Managers, and response times as fast as 5 minutes for critical issues (Unified Operations). AWS has the largest market share and the most mature support infrastructure, but also the highest support costs at scale [Source: AWS News Blog](https://aws.amazon.com/blogs/aws/new-and-enhanced-aws-support-plans-add-ai-capabilities-to-expert-guidance).

**Azure** provides strong integration with the Microsoft ecosystem, making it the best choice for organizations already using Active Directory, SQL Server, and Office 365. Unified Enterprise support covers the entire Microsoft stack (cloud, hybrid, and on-premises). Azure has 25% market share with 40% YoY growth [Source: Usage.ai](https://www.usage.ai/blogs/top-cloud-service-providers-2026).

**GCP** offers the fastest-growing platform (+63% YoY) with the most cost-effective enterprise support pricing. Premium Support includes dedicated TAMs, Operational Health Reviews, and Event Management. GCP's support is generally 5-10% cheaper than AWS/Azure for AI workloads [Source: Tech Insider](https://tech-insider.org/aws-vs-azure-vs-google-cloud-2026).

**OCI** differentiates by including enterprise support for production workloads at no extra charge—a fundamentally different pricing model from the other three hyperscalers. OCI's Support Rewards program can reduce on-premises support costs to zero. Negative reviews note that the billing model and pricing cost estimator are difficult to understand, making costs hard to predict [Source: TrustRadius](https://www.trustradius.com/products/oracle-cloud-infrastructure/pricing).

---

## 4. Infrastructure and Availability

### 4.1 Global Infrastructure Overview

| Provider | Regions | Availability Zones | Edge Locations | Countries |
|---|---|---|---|---|
| **AWS** | 33+ launched | 105+ | 600+ (Point of Presence) | 30+ |
| **Azure** | 60+ | 160+ | 300+ (PoPs) + 190+ (edge sites) | 30+ |
| **GCP** | 40+ | 121+ | 200+ | 30+ |
| **OCI** | 48+ | 60+ | 200+ | 23+ |

### 4.2 US Presence

#### AWS US Regions

AWS operates 6 US regions with 18+ availability zones:
- **US East (N. Virginia)** - us-east-1: 6 AZs
- **US East (Ohio)** - us-east-2: 3 AZs
- **US West (Oregon)** - us-west-2: 4 AZs
- **US West (N. California)** - us-west-1: 3 AZs
- **AWS GovCloud (US-East)** - us-gov-east-1: 3 AZs
- **AWS GovCloud (US-West)** - us-gov-west-1: 3 AZs

AWS has the most extensive US infrastructure with 600+ edge locations, including multiple Local Zones in major US cities (Los Angeles, Boston, Chicago, Dallas, Denver, Houston, Kansas City, Las Vegas, Miami, Minneapolis, New York City, Philadelphia, Phoenix, Portland, San Diego, Seattle, and more).

#### Azure US Regions

Azure operates 11 US regions with 30+ availability zones:
- East US (Virginia): 3 AZs
- East US 2 (Virginia): 3 AZs
- Central US (Iowa): 3 AZs
- North Central US (Illinois): 3 AZs
- South Central US (Texas): 3 AZs
- West US (California): 3 AZs
- West US 2 (Washington): 3 AZs
- West US 3 (Arizona): 3 AZs
- US Gov Virginia: 3 AZs
- US Gov Texas: 3 AZs
- US Gov Arizona: 3 AZs

Azure has 300+ global PoPs and 190+ edge sites, with extensive Azure ExpressRoute locations in major US cities.

#### GCP US Regions

GCP operates 6 US regions with 18+ availability zones:
- us-central1 (Iowa): 4 AZs
- us-east1 (South Carolina): 4 AZs
- us-east4 (Northern Virginia): 3 AZs
- us-east5 (Dallas): 3 AZs
- us-west1 (Oregon): 3 AZs
- us-west2 (Los Angeles): 3 AZs

GCP has 200+ edge locations and recently announced expansion plans for additional US regions.

#### OCI US Regions

OCI operates 8 US regions with 12+ availability zones:
- US East (Ashburn): 3 AZs
- US East (Chicago): 1 AZ
- US East (Toronto): 1 AZ
- US West (Phoenix): 3 AZs
- US West (Salt Lake City): 1 AZ
- US West (San Jose): 1 AZ
- US Gov (Ashburn): 1 AZ
- US Gov (Phoenix): 1 AZ

OCI has 200+ edge locations and offers OCI FastConnect in major US metropolitan areas.

### 4.3 Edge and Local Zone Strategy

**AWS** leads with the most extensive edge infrastructure, including 600+ Points of Presence, AWS Local Zones (for ultra-low latency applications), AWS Wavelength (for 5G edge computing), and AWS Outposts (for hybrid on-premises deployments). AWS Local Zones now cover 30+ US metropolitan areas.

**Azure** offers Azure Edge Zones, Azure Private Edge Zones, and Azure ExpressRoute with 300+ global PoPs. Azure's edge strategy includes integration with 5G networks through Azure Private MEC (Multi-access Edge Compute).

**GCP** provides Google Distributed Cloud Edge, Cloud CDN with 200+ edge locations, and Google Cloud CDN with support for Media CDN (for streaming workloads). GCP's edge infrastructure is less extensive than AWS but continues to expand.

**OCI** offers OCI FastConnect for dedicated network connectivity, OCI Edge Services for cloud-native network functions, and OCI Compute for edge locations. While OCI has fewer edge locations, its 200+ PoPs cover major US markets.

### 4.4 Network Latency and Performance

All four providers offer sub-10ms latency within US regions for most services. Key differentiators include:

- **AWS**: Global Accelerator for optimized traffic routing, AWS Direct Connect for dedicated network connections
- **Azure**: Azure Front Door for global load balancing and acceleration, ExpressRoute for private connections
- **GCP**: Premium Tier network (enters Google's network at the closest edge location), Cloud CDN for content delivery
- **OCI**: OCI FastConnect for dedicated private connectivity, Oracle Cloud Infrastructure network with consistent global pricing

---

## 5. Security and Compliance

### 5.1 Encryption

| Capability | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| **Encryption at Rest** | AES-256 (default for S3, EBS, RDS) | AES-256 (default for Blob, Disk, SQL) | AES-256 (default for Cloud Storage, Persistent Disk) | AES-256 (default for Object Storage, Block Volume) |
| **Encryption in Transit** | TLS 1.2+ (default) | TLS 1.2+ (default) | TLS 1.2+ (default) | TLS 1.2+ (default) |
| **Customer-Managed Keys (CMK)** | AWS KMS (HSM-backed) | Azure Key Vault (HSM-backed) | Cloud KMS (HSM-backed) | OCI Vault (HSM-backed) |
| **Hardware Security Module (HSM)** | AWS CloudHSM (FIPS 140-2 Level 3) | Azure Dedicated HSM (FIPS 140-2 Level 3) | Cloud HSM (FIPS 140-2 Level 3) | OCI HSM (FIPS 140-2 Level 3) |
| **Key Rotation** | Automatic (annual) | Automatic (90-180 days) | Automatic (configurable) | Automatic (configurable) |

### 5.2 Identity and Access Management (IAM)

| Capability | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| **IAM Service** | AWS IAM | Microsoft Entra ID (formerly Azure AD) | Cloud IAM | OCI IAM |
| **Multi-Factor Authentication (MFA)** | Yes (hardware, software, SMS) | Yes (conditional access) | Yes (2-Step Verification) | Yes (hardware, software, SMS) |
| **Single Sign-On (SSO)** | AWS SSO (via IAM Identity Center) | Microsoft Entra ID (native) | Cloud Identity (Google Workspace) | OCI Identity Federation |
| **Role-Based Access Control (RBAC)** | Yes (fine-grained policies) | Yes (Azure RBAC) | Yes (primitive roles) | Yes (policies with conditions) |
| **Federation** | SAML 2.0, OIDC, Web Identity | SAML 2.0, OIDC, WS-Fed | SAML 2.0, OIDC | SAML 2.0, OIDC |
| **Privileged Access Management** | IAM Access Analyzer | Privileged Identity Management (PIM) | Access Context Manager | OCI Identity Domains |

### 5.3 Network Security

| Capability | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| **Virtual Private Cloud** | Amazon VPC | Azure Virtual Network | VPC (Virtual Private Cloud) | OCI VCN |
| **Web Application Firewall (WAF)** | AWS WAF | Azure WAF (Application Gateway) | Cloud Armor | OCI WAF |
| **DDoS Protection** | AWS Shield (Standard + Advanced) | Azure DDoS Protection (Basic + Standard) | Cloud Armor (Standard + Premium) | OCI DDoS Protection |
| **Network Segmentation** | Security Groups, NACLs | NSGs, ASGs, Azure Firewall | Firewall Rules, VPC Firewall | Security Lists, Network Security Groups |
| **VPN** | AWS VPN (Site-to-Site, Client) | Azure VPN Gateway | Cloud VPN | OCI VPN (Site-to-Site, OpenVPN) |
| **Private Connectivity** | AWS Direct Connect | Azure ExpressRoute | Cloud Interconnect | OCI FastConnect |

### 5.4 Threat Detection and Monitoring

| Capability | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| **SIEM/SOAR** | Amazon Security Lake | Microsoft Sentinel | Chronicle Security Operations | OCI Security Advisor |
| **Threat Detection** | Amazon GuardDuty | Microsoft Defender for Cloud | Security Command Center (Premium) | OCI Cloud Guard |
| **Vulnerability Scanning** | Amazon Inspector | Microsoft Defender Vulnerability Management | Security Command Center (Vulnerability) | OCI Vulnerability Scanning Service |
| **Configuration Monitoring** | AWS Config | Azure Policy | Google Cloud Asset Inventory | OCI Compliance Checker |
| **Log Management** | CloudWatch Logs, Amazon OpenSearch | Azure Log Analytics, Azure Monitor | Cloud Logging, Cloud Monitoring | OCI Logging, OCI Monitoring |
| **Audit Logging** | AWS CloudTrail | Azure Audit Logs | Cloud Audit Logs | OCI Audit |

### 5.5 Compliance Certifications

All four providers have extensive compliance certifications, with Azure leading in total number of certifications.

| Certification | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| **SOC 1/2/3** | Yes | Yes | Yes | Yes |
| **ISO 27001** | Yes | Yes | Yes | Yes |
| **ISO 27017** | Yes | Yes | Yes | Yes |
| **ISO 27018** | Yes | Yes | Yes | Yes |
| **ISO 27701** | Yes | Yes | Yes | Yes |
| **FedRAMP High** | Yes | Yes | Yes | Yes |
| **FedRAMP Moderate** | Yes | Yes | Yes | Yes |
| **HIPAA** | Yes (BAA available) | Yes (BAA available) | Yes (BAA available) | Yes (BAA available) |
| **PCI DSS Level 1** | Yes | Yes | Yes | Yes |
| **GDPR** | Yes | Yes | Yes | Yes |
| **HITRUST** | Yes | Yes | Yes | Yes |
| **C5 (Germany)** | Yes | Yes | Yes | Yes |
| **IRAP (Australia)** | Yes | Yes | Yes | Yes |
| **FIPS 140-2** | Yes | Yes | Yes | Yes |
| **FIPS 140-3** | Yes | Yes | Yes | Yes |
| **Total Certifications** | 90+ | 93+ | 80+ | 70+ |

#### FedRAMP Status

All four providers maintain FedRAMP Authorizations for their cloud infrastructure:

- **AWS**: FedRAMP High and Moderate Authorizations for 100+ services, including AWS GovCloud (US-East and US-West) specifically designed for government workloads
- **Azure**: FedRAMP High Authorization for Azure Government, FedRAMP Moderate for commercial Azure; authorized for all U.S. Government data classification levels (April 16, 2025)
- **GCP**: FedRAMP High Authorization for Google Cloud Platform, FedRAMP Moderate for GCP and Google Workspace
- **OCI**: FedRAMP High Authorization for OCI Government Cloud, FedRAMP Moderate for commercial OCI

#### HIPAA Compliance

All four providers offer Business Associate Agreements (BAAs) for HIPAA compliance, enabling healthcare workloads:

- **AWS**: HIPAA-eligible services include 200+ services, with BAA available for all covered services
- **Azure**: HIPAA-compliant services include 90+ services, with BAA available for all covered services
- **GCP**: HIPAA-compliant services include 100+ services, with BAA available for all covered services
- **OCI**: HIPAA-compliant services include OCI Language, OCI Speech, OCI Vision, and core infrastructure services, with BAA available

### 5.6 Industry-Specific Compliance

| Industry | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| **Healthcare** | HIPAA, HITRUST, GxP | HIPAA, HITRUST, GxP | HIPAA, HITRUST, GxP | HIPAA, HITRUST |
| **Financial Services** | PCI DSS, SOC, FFIEC, FINRA | PCI DSS, SOC, FFIEC, FINRA | PCI DSS, SOC, FFIEC | PCI DSS, SOC, FFIEC |
| **Government** | FedRAMP, DoD IL5, ITAR | FedRAMP, DoD IL5, ITAR | FedRAMP, DoD IL5 | FedRAMP, DoD IL5 |
| **Education** | FERPA | FERPA | FERPA | FERPA |
| **Energy** | NERC CIP | NERC CIP | NERC CIP | NERC CIP |

### 5.7 Security Architecture Comparison

**AWS** provides the most mature and comprehensive security toolset with the largest ecosystem of third-party security integrations. AWS Security Hub centralizes security findings from multiple sources, and AWS Config provides detailed resource configuration tracking. AWS Shield Advanced offers 24/7 DDoS protection with access to the AWS DDoS Response Team [Source: AWS](https://aws.amazon.com/security).

**Azure** offers the strongest identity and access management through Microsoft Entra ID, with features like Conditional Access, Privileged Identity Management, and Identity Protection. Microsoft Defender for Cloud provides unified security management across hybrid cloud environments. Azure Sentinel is a cloud-native SIEM with built-in AI capabilities [Source: Microsoft Azure](https://azure.microsoft.com/en-us/products/security).

**GCP** provides Security Command Center (Premium) for threat detection, vulnerability scanning, and asset inventory. GCP's security model is built on Google's infrastructure security, which includes custom-designed hardware and software. Chronicle Security Operations provides SIEM capabilities [Source: Google Cloud](https://cloud.google.com/security).

**OCI** offers OCI Cloud Guard for threat detection, OCI Vulnerability Scanning Service, and OCI Security Advisor for centralized security management. OCI's security architecture emphasizes customer data control and zero data retention for AI services. OCI is the first cloud vendor to offer performance SLAs, which include security performance guarantees [Source: Oracle](https://www.oracle.com/security).

---

## 6. Summary Comparison Table

| Dimension | AWS | Azure | GCP | OCI |
|---|---|---|---|---|
| **Market Share (Q1 2026)** | ~30% | ~25% | ~13% | ~3% |
| **Compute (4 vCPU/16 GB, On-Demand)** | ~$147/month | ~$140/month | ~$98-$142/month | ~$55/month |
| **Compute (Max Discount)** | Up to 72% (3-year RI) | Up to 72% (RI) + 85% with Hybrid Benefit | Up to 55% (3-year CUD) + 30% SUD (automatic) | 40-70% (negotiated) |
| **Object Storage (Standard/GB)** | $0.023 | $0.018 | $0.020 | $0.0255 |
| **Block Storage (Standard SSD/GB)** | $0.08 (gp3) | $0.08-$0.12/GiB (Premium v2) | $0.11/GiB (Balanced) | $0.0255 |
| **Data Egress (First 10 TB)** | $0.09/GB | $0.087/GB | $0.12/GB | $0.00/GB (10 TB free) |
| **Serverless (Free Tier)** | 1M req + 400K GB-s | 1M req + 400K GB-s | 2M req + 400K GB-s | 2M req + 400K GB-s |
| **ML Platform** | SageMaker AI | Azure ML (Microsoft Foundry) | Gemini Enterprise Agent Platform | OCI Data Science |
| **GenAI Service** | Bedrock | Azure OpenAI Service | Gemini Enterprise Agent Platform | OCI Generative AI |
| **GenAI Models** | 30+ (Claude, Titan, Llama, DeepSeek) | 11,000+ (GPT-5, Claude, Llama, Mistral) | Gemini 3.1, Claude, DeepSeek, Qwen | Cohere, Llama, Grok, Gemini, Nemotron |
| **Enterprise Support (Min)** | $5,000/month | $100/month (Standard) | $15,000/month (Premium) | Included (at no extra charge) |
| **Critical Response Time** | 5-30 min (by plan) | 15 min-1 hr (by plan) | 15 min-1 hr (by tier) | 5-15 min (by severity) |
| **Compute SLA (Multi-AZ)** | 99.99% | 99.99% | 99.99% | 99.99% |
| **US Regions** | 6 (3 GovCloud) | 11 (3 GovCloud) | 6 | 8 (2 GovCloud) |
| **Edge Locations** | 600+ | 300+ PoPs + 190+ edge sites | 200+ | 200+ |
| **Compliance Certifications** | 90+ | 93+ | 80+ | 70+ |
| **FedRAMP** | High (GovCloud) | High (Azure Government) | High (GCP) | High (OCI GovCloud) |
| **HIPAA** | Yes (BAA) | Yes (BAA) | Yes (BAA) | Yes (BAA) |
| **Key Strength** | Breadth of services, ecosystem maturity | Microsoft ecosystem, compliance portfolio | AI/ML innovation, cost-effectiveness | Raw compute pricing, egress costs, Oracle integration |
| **Key Weakness** | High egress costs, complex pricing | Vendor lock-in concerns, legacy retirement | Smaller ecosystem, TPU engineering tax | Smaller ecosystem, limited AI services |

---

## 7. Conclusion and Selection Guidance

The choice between AWS, Azure, GCP, and OCI in 2026 depends heavily on an organization's specific workloads, existing infrastructure, compliance requirements, and strategic priorities.

**Choose AWS** if your organization values the broadest ecosystem of services, the most mature cloud infrastructure, and the deepest long-term commitment discounts. AWS is the safest choice for organizations building large-scale, multi-service architectures and those requiring the most extensive global edge infrastructure. AWS is particularly strong for organizations already using AWS-native services like S3, Redshift, and DynamoDB.

**Choose Azure** if your organization is already invested in the Microsoft ecosystem (Active Directory, SQL Server, Office 365, Dynamics 365) or operates in heavily regulated industries requiring the most comprehensive compliance portfolio. Azure offers the best value for Windows Server and SQL Server workloads (up to 85% off with Hybrid Benefit + RIs) and provides exclusive access to OpenAI's GPT-5 series through Azure OpenAI Service.

**Choose GCP** if your organization prioritizes AI/ML capabilities, cost-effectiveness, and open-source technologies. GCP leads in AI innovation with the Gemini Enterprise Agent Platform, offers the most cost-effective AI infrastructure (28% cheaper training, 35% cheaper inference than SageMaker), and provides the simplest commitment structure. GCP is ideal for organizations already using BigQuery and those building agent-first AI applications.

**Choose OCI** if your organization's primary concerns are raw compute cost, data egress charges, and Oracle ecosystem integration. OCI offers the most aggressive on-demand pricing (up to 57% lower than AWS/Azure/GCP for equivalent configurations), zero egress charges (as of February 2026), and enterprise support included at no extra cost. OCI is particularly attractive for organizations running Oracle databases, financial services workloads, and applications with high data transfer requirements.

For most organizations, a **multi-cloud strategy** remains the practical recommendation in 2026, with 89% of enterprises already adopting multi-cloud approaches. The most common pattern is AWS primary + GCP for AI/BigQuery, or Azure primary + OCI for Oracle database workloads.

---

## Sources

[1] AWS vs Azure vs Google Cloud 2026 [Compared] - Tech Insider: https://tech-insider.org/aws-vs-azure-vs-google-cloud-2026

[2] Cloud Pricing Comparison 2026: AWS, Azure, GCP, Oracle - EffectiveSoft: https://www.effectivesoft.com/blog/cloud-pricing-comparison.html

[3] AWS vs GCP vs Azure: GCP Cuts SQL Costs 30% [2026] - shattered.io: https://shattered.io/aws-vs-azure-vs-gcp-2026

[4] Cloud Pricing Comparison 2026: AWS vs Azure vs GCP+ - CloudZero: https://www.cloudzero.com/blog/cloud-pricing-comparison

[5] Cloud Pricing Comparison: AWS vs Azure vs GCP (2026) - Usage.ai: https://www.usage.ai/blogs/finops/multi-cloud/cloud-pricing-comparison

[6] AWS EC2 Pricing Guide: All Models Explained (2026) - Usage.ai: https://www.usage.ai/blogs/aws/ec2/pricing

[7] Amazon EC2 Pricing Guide 2026 - GoCloud.io: https://go-cloud.io/amazon-ec2-pricing

[8] The Ultimate Guide to Amazon EC2 Pricing in 2026 - nOps: https://www.nops.io/blog/ec2-pricing-how-much-does-aws-ec2-really-cost

[9] AWS EC2 Reserved Instance Pricing - AWS: https://aws.amazon.com/ec2/pricing/reserved-instances/pricing

[10] Google Cloud Pricing 2026: Cost Breakdown & Hidden Costs - Eon: https://www.eon.io/blog/google-cloud-pricing

[11] How to Optimize Google Compute Engine Pricing (2026 Guide) - Usage.ai: https://www.usage.ai/blogs/gcp/compute-engine

[12] Google Cloud Compute Engine Pricing Guide (Updated 2026) - CloudZero: https://www.cloudzero.com/blog/google-cloud-compute-engine-pricing-guide

[13] Google Cloud Pricing 2026: Total Cost & Competitors - CheckThat.ai: https://checkthat.ai/brands/google-cloud/pricing

[14] Azure Pricing Changes 2026: Every Update to Your Bill - SpendArk: https://spendark.com/blog/azure-pricing-changes-2026

[15] Azure Pricing Guide 2026: Costs, Discounts & Management Tools - Sedai: https://sedai.io/blog/microsoft-azure-pricing-guide

[16] Prepay for Azure virtual machines to save money - Microsoft Learn: https://learn.microsoft.com/en-us/azure/virtual-machines/prepay-reserved-vm-instances

[17] Oracle Cloud Pricing: A Guide To Oracle Cloud Costs (2026) - CloudZero: https://www.cloudzero.com/blog/oracle-cloud-pricing

[18] Oracle Cloud Pricing - Oracle: https://www.oracle.com/cloud/pricing

[19] OCI Price List - Oracle: https://www.oracle.com/cloud/price-list

[20] The Ultimate Guide to AWS S3 Pricing 2026 - Cloudchipr: https://cloudchipr.com/blog/amazon-s3-pricing-explained

[21] Amazon S3 pricing: the complete 2026 guide - CloudZero: https://www.cloudzero.com/blog/s3-pricing

[22] Azure Blob Storage Pricing: A 2026 Cost Breakdown - CloudZero: https://www.cloudzero.com/blog/azure-blob-storage-pricing

[23] Google Cloud Storage Pricing: The No BS Guide To GCP Storage Costs [2026] - CloudZero: https://www.cloudzero.com/blog/gcp-storage-pricing

[24] Cloud & AI Storage Pricing Comparison 2026: AWS, Azure, GCP, OCI - Finout: https://www.finout.io/blog/cloud-storage-pricing-comparison

[25] AWS Lambda Pricing Calculator & Cost Guide (Aug 2026) - CostGoat: https://costgoat.com/pricing/aws-lambda

[26] AWS Lambda pricing: what it actually costs in 2026 - CloudZero: https://www.cloudzero.com/blog/lambda-pricing

[27] Azure Functions pricing: Consumption vs. Flex Consumption - Modal: https://modal.com/blog/azure-function-pricing-guide

[28] Google Cloud Functions Review 2026 - srvrlss.io: https://www.srvrlss.io/provider/google-cloud-functions

[29] Oracle Cloud Functions Review 2026 - srvrlss.io: https://www.srvrlss.io/provider/oracle-cloud-functions

[30] GCP vs AWS for ML Workloads in 2026: Vertex AI vs SageMaker (Honest Comparison) - AgileSoftLabs: https://www.agilesoftlabs.com/blog/2026/06/gcp-vs-aws-for-ml-workloads-in-2026

[31] Top 8 Vertex AI Alternatives in 2026 - TrueFoundry: https://www.truefoundry.com/blog/exploring-alternatives-to-vertexai

[32] Azure ML vs Vertex AI vs SageMaker: A Comparison - Ankur's Newsletter: https://www.ankursnewsletter.com/p/azure-ml-vs-vertex-ai-vs-sagemaker

[33] SageMaker vs Azure ML vs Google AI Platform: A Comprehensive Comparison - CloudOptimo: https://www.cloudoptimo.com/blog/sagemaker-vs-azure-ml-vs-google-ai-platform-a-comprehensive-comparison

[34] The AWS AI/ML Landscape in 2026 — Simplified - DEV Community: https://dev.to/aws-builders/the-aws-aiml-landscape-in-2026-simplified-17i3

[35] A Practical Guide to AWS AI Services: Features, Use Cases & Benefits - Codilime: https://codilime.com/blog/practical-guide-aws-ai-services

[36] Introducing AWS AI Service Cards - AWS: https://aws.amazon.com/blogs/machine-learning/introducing-aws-ai-service-cards-a-new-resource-to-enhance-transparency-and-advance-responsible-ai

[37] Vertex AI release notes - Google Cloud: https://docs.cloud.google.com/vertex-ai/docs/release-notes

[38] Vertex AI Is Now Gemini Enterprise Agent Platform - GCP Study Hub: https://gcpstudyhub.com/blog/vertex-ai-replaced-by-gemini-enterprise-agent-platform

[39] Welcome to Google Cloud Next26 - Google Cloud Blog: https://cloud.google.com/blog/topics/google-cloud-next/welcome-to-google-cloud-next26

[40] What's New in Oracle AI? June 2026 Edition - Oracle Blogs: https://blogs.oracle.com/ai-and-datascience/whats-new-in-ai-june-2026

[41] Data Science Service - Oracle: https://www.oracle.com/artificial-intelligence/data-science

[42] AI Data Platform - Oracle: https://www.oracle.com/ai-data-platform

[43] OCI Enterprise AI - Oracle: https://www.oracle.com/artificial-intelligence/enterprise-ai

[44] AWS Bedrock Pricing 2026 - Bacancy Technology: https://www.bacancytechnology.com/blog/aws-bedrock-pricing

[45] Amazon Bedrock Pricing Explained 2026 - nOps: https://www.nops.io/blog/amazon-bedrock-pricing

[46] Amazon Bedrock pricing in 2026: every model and hidden costs - CloudZero: https://www.cloudzero.com/blog/amazon-bedrock-pricing

[47] Azure OpenAI Pricing 2026: Models, PTU & Hidden Costs - Amnic: https://amnic.com/blogs/understanding-the-true-cost-of-azure-openai

[48] Azure OpenAI Pricing: Models, Costs & Tracking AI Spend - CloudZero: https://www.cloudzero.com/blog/azure-openai-pricing

[49] What's new in Azure OpenAI in Microsoft Foundry Models? - Microsoft Learn: https://learn.microsoft.com/en-us/azure/foundry-classic/openai/whats-new

[50] AI Services - Oracle: https://www.oracle.com/artificial-intelligence/ai-services

[51] AI Speech to Text - Oracle: https://www.oracle.com/artificial-intelligence/speech

[52] AI Image Recognition - OCI Vision - Oracle: https://www.oracle.com/artificial-intelligence/vision

[53] AI Text Analysis at Scale - Oracle: https://www.oracle.com/artificial-intelligence/language

[54] Responsible AI - AWS: https://aws.amazon.com/ai/responsible-ai

[55] Responsible AI - Google Cloud: https://cloud.google.com/responsible-ai

[56] What is Responsible AI - Azure Machine Learning - Microsoft Learn: https://learn.microsoft.com/en-us/azure/machine-learning/concept-responsible-ai?view=azureml-api-2

[57] Cloud Support Plan Pricing Benchmarks 2026 - VendorBenchmark: https://vendorbenchmark.com/blog/cloud-support-plan-pricing-benchmark-comparison

[58] AWS Support Plans - AWS: https://docs.aws.amazon.com/awssupport/latest/user/aws-support-plans.html

[59] New and enhanced AWS Support plans add AI capabilities to expert guidance - AWS News Blog: https://aws.amazon.com/blogs/aws/new-and-enhanced-aws-support-plans-add-ai-capabilities-to-expert-guidance

[60] AWS Support Plan Pricing - AWS: https://aws.amazon.com/premiumsupport/pricing

[61] Azure Support Plans Comparison - Microsoft Azure: https://azure.microsoft.com/en-us/support/plans

[62] Support Plans—Support Scope and Responsiveness - Microsoft Azure: https://azure.microsoft.com/en-us/support/plans/response

[63] Premium Support - Google Cloud: https://cloud.google.com/support/premium

[64] Standard Support overview - Google Cloud: https://docs.cloud.google.com/support/docs/standard

[65] Amazon Compute Service Level Agreement - AWS: https://aws.amazon.com/compute/sla

[66] SLA for Virtual Machines - Azure: https://www.azure.cn/en-us/support/sla/virtual-machines

[67] Compute Engine Service Level Agreement (SLA) - Google Cloud: https://cloud.google.com/compute/sla

[68] Oracle Cloud Infrastructure Service Level Agreement - Oracle: https://www.oracle.com/cloud/sla

[69] AWS Security - AWS: https://aws.amazon.com/security

[70] Azure Security - Microsoft Azure: https://azure.microsoft.com/en-us/products/security

[71] Google Cloud Security - Google Cloud: https://cloud.google.com/security

[72] Oracle Security - Oracle: https://www.oracle.com/security

[73] Top Cloud Service Providers 2026 - Usage.ai: https://www.usage.ai/blogs/top-cloud-service-providers-2026

[74] Oracle Cloud Infrastructure Pricing 2026 - TrustRadius: https://www.trustradius.com/products/oracle-cloud-infrastructure/pricing

[75] OCI Costs Overview & How OCI Compares to AWS/Azure/GCP - Finout: https://www.finout.io/blog/oci-costs-overview
