# Comprehensive Evaluation of Cloud Migration Strategies for Enterprise Finance Applications

## Executive Summary

This report provides a detailed comparison of AWS, Microsoft Azure, and Google Cloud across three primary migration approaches—lift-and-shift (rehost), re-platforming, and full re-architecture—for large-scale enterprise application migrations in regulated financial services environments. The evaluation spans five critical dimensions: tooling and services, cost modeling, downtime and business continuity risks, performance and scalability, and security and compliance. Each provider-approach combination is assessed for its suitability to meet the stringent requirements of financial institutions including PCI DSS, SOC 2, GDPR, and regional financial regulations.

---

## Comparison Tables: Cloud Providers × Migration Approaches × Evaluation Dimensions

### 1. Tooling & Services

| Dimension | Approach | AWS | Azure | Google Cloud |
|-----------|----------|-----|-------|--------------|
| **Primary Migration Tools** | Lift-and-Shift | **AWS Application Migration Service (MGN)** – automated rehosting via continuous block-level replication; free for 90 days per source server [1] | **Azure Migrate** + **Azure Site Recovery** – comprehensive discovery, assessment, and agent-based/agentless migration; 31-day free ASR trial [2] | **Migrate to Virtual Machines** – free service for VM migration from vSphere, Hyper-V, AWS, Azure; uses continuous disk replication [3] |
| | Re-platforming | **AWS DMS**, **Schema Conversion Tool**, **App2Container**; Migration Hub Orchestrator for workflow automation [4] | **Azure Database Migration Service** – standard tier free, premium tier 6 months free; **Azure App Service** and **AKS** for containerization [5] | **Migrate to Containers** – free tool for VM-to-container conversion targeting GKE/Cloud Run; **Database Migration Service** free for homogeneous migrations [6] |
| | Re-architecture | AWS Lambda, ECS/EKS, Step Functions, DynamoDB, Aurora Serverless | Azure Functions, AKS, Cosmos DB, Azure SQL Database serverless | Cloud Run, GKE Autopilot, Cloud Spanner, BigQuery, AlloyDB |
| **Discovery & Assessment** | All | **AWS Application Discovery Service**, **Migration Evaluator** (TSO Logic), **AWS Migration Hub** (no longer open to new customers as of Nov 2025) [7] | **Azure Migrate** – agentless discovery, dependency mapping, software inventory, web app assessment; built-in RBAC roles [8] | **Google Cloud Migration Center** – unified platform with StratoZone technology; agentless discovery, TCO estimation, Gemini-powered Quick TCO Estimator [9] |
| **Automation Frameworks** | All | **Migration Hub Orchestrator** – predefined workflow templates for SAP, SQL Server, EC2; **Cloud Migration Factory** for large-scale deployments [10] | **Azure Migrate Wave Planning** – structured large-scale migrations with sequencing, visualization, tracking; **Azure Copilot** for conversational planning [11] | **Cloud Foundation Toolkit (CFT)** – Terraform-based landing zones; **Fabric FAST** – production-ready bootstrapping toolkit [12] |
| **Database Migration** | All | **AWS DMS** – homogeneous and heterogeneous, CDC support; 1.5M+ databases migrated [13] | **Azure DMS** – standard tier free, premium tier with online migrations; **SQL Server to Azure SQL MI** support [14] | **Database Migration Service** – free homogeneous migrations, CDC-based continuous replication; Gemini-powered schema conversion for heterogeneous [15] |

### 2. Cost Modeling

| Dimension | Approach | AWS | Azure | Google Cloud |
|-----------|----------|-----|-------|--------------|
| **TCO Analysis Tools** | All | **AWS Pricing Calculator**, **Migration Evaluator**, **Cost Explorer**; CloudZero for real-time monitoring [16] | **Azure TCO Calculator**, **Azure Migrate business case** tool; **Azure Hybrid Benefit** savings calculator [17] | **Migration Center Quick TCO Estimator** (Gemini-powered); **Pricing Calculator** with custom machine type support [18] |
| **Upfront Migration Costs** | Lift-and-Shift | **MGN** – free for 90 days, then $0.042/hour per server; storage and compute costs apply during migration [19] | **Azure Migrate** – free portal; **ASR** – $25/instance/month after 31-day free trial; **DMS standard** – free [20] | **Migrate to Virtual Machines** – free; **Storage Transfer Service** – $0.0125/GB for agent-based transfers; **Transfer Appliance** – per-use fee [21] |
| | Re-platforming | DMS replication instances billed hourly; Schema Conversion Tool free; partner labor costs dominate | DMS premium tier ~$0.37/vCore-hour; 6-month free period; Azure App Service migration costs vary | DMS homogeneous migrations free; heterogeneous billed per GB of data processed; Migrate to Containers free |
| | Re-architecture | 5-20× cost of lift-and-shift; typically $200K-$600K+ for large enterprise apps [22] | Similar range; Azure DevOps and CI/CD tooling costs additional | Refactoring costs 5-20× lift-and-shift; $150K-$750K per line-of-business app [23] |
| **Ongoing Operational Costs** | All | Pay-as-you-go, Reserved Instances (up to 72% savings), Savings Plans; **egress**: $0.09/GB first 10TB, tiered discounts [24] | Pay-as-you-go, Reserved Instances (up to 72%), Azure Savings Plan (up to 65%); **Azure Hybrid Benefit** up to 76% savings on Windows/SQL workloads [25] | Per-second billing, Sustained Use Discounts (up to 30% automatic), CUDs (up to 70%); **egress**: $0.12/GB first 1TB; custom machine types save 20-30% [26] |
| **Licensing Implications** | Finance | **SQL Server**: BYOL (requires Software Assurance) or License Included; $1,353/month for c5.xlarge with Windows+SQL Enterprise; Oracle 2:1 vCPU rule on EC2 [27] | **Azure Hybrid Benefit**: up to 76% savings; **free ESUs** on Azure for Windows Server 2012/R2, SQL Server 2012/2014; SQL Server on VM most cost-effective for compliance [28] | **SQL Server**: License Manager on VMware Engine (Preview); Cloud SQL includes licensing with 4-core minimum; BYOL with License Mobility requires Software Assurance [29] |
| **Data Transfer/Egress** | All | $0.09/GB first 10TB; 100GB free/month; free for migration off AWS (60-day exit, full account removal); cross-AZ $0.01/GB [30] | $0.087-0.09/GB; free data transfer between primary and geo-secondary for Azure SQL DB; free intra-region traffic [31] | $0.12/GB first 1TB (Premium Tier); free exit program for customers leaving GCP; cross-zone $0.01/GB; 200GB free outbound/month [32] |

### 3. Downtime & Business Continuity Risks

| Dimension | Approach | AWS | Azure | Google Cloud |
|-----------|----------|-----|-------|--------------|
| **Failover Options** | All | **Multi-AZ**: RDS 99.95% SLA, automatic failover; **Multi-Region**: active-passive (Pilot Light, Warm Standby) or active-active; **Elastic Disaster Recovery** (sub-second RPO, 5-20 min RTO) [33] | **Availability Zones**: 99.99% VM uptime SLA, <2ms latency between zones; **Paired Regions**: automatic GRS replication; **Azure Site Recovery** (15 min RTO, 15-30 min RPO) [34] | **Live Migration**: transparent VM maintenance; **Multi-Zone**: 99.99% SLA; **Multi-Region**: 43 regions, 130 zones; **Backup & DR** service with cross-region vaults [35] |
| **Cutover Complexity** | Lift-and-Shift | MGN: non-disruptive test launches, quick cutover in minutes; rollback with full backups; DNS/Route 53 TTL management [36] | ASR: test failover isolation, 4-6 week implementation; Azure Migrate Wave Planning for structured sequencing [37] | Migrate to Virtual Machines: built-in testing, periodic data replication, fast cutover; no client-side agents required [38] |
| | Re-platforming | DMS CDC: ongoing replication, minimal downtime; test cutover recommended one week prior | DMS: continuous migration with CDC, minimal downtime; AppCAT identifies mandatory code changes before migration | DMS: continuous CDC-based replication, minimal downtime; Gemini-powered schema conversion reduces cutover risk |
| | Re-architecture | Step Functions orchestration; gradual traffic shifting; Lambda blue/green deployments | Azure DevOps CI/CD pipelines; deployment slots for App Service; AKS rolling updates | GKE automated rollouts; Cloud Run traffic splitting; gradual canary deployments |
| **Rollback Strategies** | All | MGN: source servers remain untouched until cutover confirmed; DMS: bidirectional replication possible; full backups before migration [39] | ASR: test failover cleanup procedures; Azure Migrate: pause/resume replication; full backups recommended [40] | Migration Center: snapshots/backups before migration; automated rollback triggers; DMS: source remains operational during CDC [41] |
| **Finance-Specific Risks** | All | Major US-East-1 outage (2025, ~15 hours) – treat Region as failure domain; 99.95% Multi-AZ SLA not sufficient for mission-critical; need multi-region DR [42] | NAB quote: "Trust and resilience critical for financial services" – APRA requirements; hardware outages (high likelihood) vs. region outages (low likelihood) [43] | June 2025 global outage (3 hours) – teams with tested cross-region DR could failover; financial/trading workloads: $1K-$8.5K/month egress costs [44] |

### 4. Performance & Scalability Post-Migration

| Dimension | Approach | AWS | Azure | Google Cloud |
|-----------|----------|-----|-------|--------------|
| **Performance Characteristics** | Lift-and-Shift | ~30% cost savings without optimizations (GE Oil & Gas); preserves app performance; rightsizing required post-migration [45] | Immediate cost savings via Azure Hybrid Benefit; performance preserved; follow-on modernization to PaaS services [46] | Minimal modification preserves performance; usage-driven analytics for rightsizing; no over-provisioning [47] |
| | Re-platforming | SQL Server to RDS: managed backups, patching, read replicas; Graviton processors for better price-performance | SQL Server to Azure SQL MI: built-in read-only replica (Business Critical), In-Memory OLTP; 1-2ms storage IO latency [48] | On-prem SQL to Cloud SQL: managed service, automatic failover, 99.99% SLA; up to 96 CPUs, 624GB memory [49] |
| | Re-architecture | Cloud-native: Lambda, ECS/EKS, Aurora; RenaissanceRe: 3,000 parallel containers, 45TB data processed per run [50] | Azure Functions, AKS, Cosmos DB; Hyperscale SQL DB up to 100TB; serverless compute with per-second billing [51] | GKE Autopilot, Cloud Run, Cloud Spanner; BigQuery for analytics; Axion-based VMs: 2× better price-performance [52] |
| **Scalability Capabilities** | All | **Auto Scaling**: predictive scaling, scheduled scaling; **Lambda**: automatic function scaling; **Aurora**: up to 15 read replicas [53] | **Azure SQL serverless**: auto-scales compute; **AKS**: horizontal/vertical pod autoscaling; **Elastic pools**: shared resource pools [54] | **GKE Autoscaler**: cluster/pod/vertical autoscaling; **Cloud SQL**: committed use discounts up to 52%; **Custom machine types**: exact vCPU/RAM configuration [55] |
| **Latency Considerations** | Finance | **Local Zones**: ~50μs within AZ, ~400μs across AZs; **Outposts**: 40% better performance; placement decisions 20,000× more impact than app tuning [56] | **Availability Zones**: <2ms between zones; **ExpressRoute**: dedicated private connections; **Business Critical**: 1-2ms storage IO latency [57] | **Within-region**: cheaper and faster than cross-region; **Edge locations**: sub-millisecond response; **Live migration**: transparent maintenance [58] |

### 5. Security & Compliance

| Dimension | Approach | AWS | Azure | Google Cloud |
|-----------|----------|-----|-------|--------------|
| **Compliance Certifications** | All | **143 standards**: PCI DSS Level 1, SOC 1/2/3, HIPAA, FedRAMP, GDPR, FIPS 140-3, NIST 800-171; **AWS Artifact**: 2,600+ security controls [59] | **100+ offerings**: PCI DSS 4.0 Level 1, SOC 1/2/3, HIPAA, FedRAMP, GDPR, FIPS 140-3; broadest portfolio in industry [60] | **PCI DSS, SOC 2, HIPAA, FedRAMP, GDPR**; **Assured Workloads**: automatic compliance controls for FedRAMP, IL5, CJIS, ITAR, EU Sovereign Controls [61] |
| **Security Tooling** | All | **Security Hub** (8 standards), **GuardDuty**, **Inspector**, **Config**, **Control Tower**, **Audit Manager**, **KMS** (FIPS 140-2) [62] | **Defender for Cloud**, **Azure Policy**, **Purview**, **Azure Blueprints**, **Dedicated HSM** (FIPS 140-3 Level 3), **Managed HSM** [63] | **Security Command Center**, **Cloud Armor** (WAF/DDoS), **Cloud KMS** (FIPS 140-3 Level 3), **Shielded VMs**, **Confidential VMs** [64] |
| **Encryption** | All | **KMS**: CMEK, CSEK; **EBS encryption** at rest; **TLS 1.2** in transit; **FIPS 140-3** validated modules [65] | **Key Vault**: Managed HSM (FIPS 140-3 Level 3); **Azure Dedicated HSM**; **CMEK**; **BYOK**; **Azure Confidential Computing** [66] | **Cloud KMS**: CMEK, CSEK, Cloud EKM, Cloud HSM; **FIPS 140-3 Level 3**; **Autokey** for automated key provisioning; **Confidential VMs** [67] |
| **Data Residency** | Finance | **European Sovereign Cloud** (GA Jan 2026): independent EU cloud, own SOC 2; **Canada Regions**: Montreal, Calgary; **Outposts**: on-premises data residency [68] | **60+ regions**: data residency enforced via Azure Policy; **Azure Cloud HSM**: data never leaves deployment region; **Service Trust Portal** for compliance documentation [69] | **43 regions, 130 zones**: SLA-backed data residency; **Assured Workloads**: region-restricted deployments; **Transfer Appliance**: EU data never leaves EU boundaries [70] |
| **Financial Services Regulation** | All | **OSFI** (Canada B-10, B-13, E-21), **PCI DSS**, **SOC 2**, **GDPR**; **AWS User Guide for Federally Regulated Financial Institutions in Canada** [71] | **23 NYCRR 500**, **FFIEC**, **GLBA**, **SOX**, **SEC 17a-4**, **APRA**, **MAS**, **OSFI**, **PCI DSS 4.0**; dedicated Financial Services section in Service Trust Portal [72] | **Assured Workloads** for FedRAMP, IL5; **PCI DSS**; **SOC 2**; **Data Boundary** for EU sovereign control; **Cloud4C**: PCI-DSS, NESA, SAMA, RBI, OJK, MAS [73] |

---

## Detailed Pros and Cons: Provider-Approach Combinations for Regulated Financial Environments

### AWS

#### Lift-and-Shift (Rehost)

**Pros:**
- **AWS MGN** is the most mature lift-and-shift tool, evolved from CloudEndure with continuous block-level replication and 90-day free period [1]
- **No application changes required** – critical for legacy financial systems where source code may be unavailable
- **30% cost savings** even without optimization (GE Oil & Gas benchmark) [45]
- **Elastic Disaster Recovery** provides sub-second RPO and 5-20 minute RTO – suitable for financial services BC/DR requirements [33]
- **143 compliance certifications** including PCI DSS Level 1, SOC 2, and regional financial regulations [59]
- **AWS Artifact** provides on-demand access to 2,600+ security controls for auditor review [59]

**Cons:**
- **Does not address technical debt** – legacy security gaps, excessive permissions, and poor configurations persist
- **Oracle licensing penalty**: 2:1 vCPU conversion rule on EC2 effectively doubles license costs vs. on-premises [27]
- **SQL Server licensing complexity**: BYOL requires Software Assurance; License Included can be more expensive than on-premises for sustained workloads
- **Egress costs**: $0.09/GB first 10TB can accumulate significantly for data-intensive financial workloads ($1,000-$8,500/month typical for finance/trading) [24]
- **Migration Hub deprecated**: New customers cannot use Migration Hub as of November 2025; must use AWS Transform instead [7]

#### Re-platforming

**Pros:**
- **AWS DMS**: 1.5M+ databases migrated, supports CDC for minimal downtime, heterogeneous migrations via Schema Conversion Tool [13]
- **App2Container**: automates containerization of legacy apps without source code changes
- **RDS for SQL Server**: managed backups, patching, Multi-AZ failover, read replicas – reduces operational overhead
- **AWS Graviton processors**: up to 40% better price-performance for ARM-compatible workloads
- **End-of-Support Migration Program (EMP)**: migrated legacy Windows apps to newer OS versions without code changes (now EOL April 2025) [74]

**Cons:**
- **Oracle on RDS**: License Included only for SE2; Enterprise Edition requires BYOL with 2:1 penalty on RDS as well
- **Database migration costs**: $60K-$300K per database for Oracle to Aurora migration; 10-30% of PL/SQL may require manual conversion [13]
- **EMP end-of-life**: Legacy Windows migration support no longer available; Cloudhouse Alchemy is successor but requires separate licensing [74]
- **Limited heterogeneous database support**: Schema Conversion Tool automates 70-90% of conversion but remaining 10-30% requires manual effort

#### Full Re-architecture (Refactor)

**Pros:**
- **Serverless architecture**: Lambda, Step Functions, Fargate, Aurora Serverless – automatic scaling, pay-per-use, reduced operational burden
- **RenaissanceRe case study**: 3,000 parallel containers processing 45TB of financial risk models in production [50]
- **Microservices on ECS/EKS**: full CI/CD pipelines, service mesh, observability
- **Aurora Global Database**: <1 minute failover across regions, up to 99.99% availability
- **DynamoDB Global Tables**: multi-region active-active with last-writer-wins reconciliation

**Cons:**
- **5-20× cost of lift-and-shift**: typical $200K-$600K+ for large enterprise applications [22]
- **6-24 months timeline**: not suitable for data center lease expiry or urgent compliance deadlines
- **Requires new skills**: serverless, containerization, CI/CD – significant training investment
- **AWS Prescriptive Guidance**: "Refactor is not recommended for large migrations because it involves modernizing the application during the migration" [75]
- **Financial services risk**: automated failover "not recommended" for critical applications; manual approval processes preferred

---

### Azure

#### Lift-and-Shift (Rehost)

**Pros:**
- **Azure Hybrid Benefit**: up to 76% savings on Windows Server and SQL Server licenses – Microsoft's strongest advantage for Microsoft-centric financial institutions [25]
- **Free Extended Security Updates (ESUs)**: Windows Server 2012/R2 ESUs free on Azure through October 2026; SQL Server 2012/2014 ESUs also free [76]
- **Azure Migrate**: comprehensive discovery, assessment, dependency mapping – all free; built-in RBAC roles for least-privilege access [8]
- **Azure Site Recovery**: 31-day free trial per instance, then $25/instance/month; 15-minute RTO, 15-30 minute RPO [20]
- **Broadest compliance portfolio**: 100+ offerings including PCI DSS 4.0, SOC 2, FFIEC, GLBA, SOX, APRA, MAS, OSFI [60]

**Cons:**
- **SQL Server on VM still most expensive option**: Red9 analysis shows VM costs $1,890/month vs. Managed Instance $2,534/month for comparable configuration [77]
- **Oracle licensing**: Azure also subject to Oracle's 2:1 vCPU rule; no License Included options for Oracle EE
- **Egress costs**: $0.087-0.09/GB starting rate; can be significant for data-intensive workloads [31]
- **Azure Cloud HSM is IaaS-only**: does not integrate with PaaS/SaaS services; requires Azure Key Vault Managed HSM for PaaS [78]

#### Re-platforming

**Pros:**
- **Azure SQL Managed Instance**: best of both worlds – SQL Server compatibility with PaaS benefits; Business Critical tier offers 1-2ms storage IO latency, In-Memory OLTP, built-in read-only replica [48]
- **Azure DMS**: standard tier free for offline migrations; premium tier 6 months free; CDC-based continuous replication for minimal downtime [14]
- **Azure App Service**: easy migration of ASP.NET apps; Azure Migrate AppCAT analyzes code for mandatory changes before migration [79]
- **Azure Kubernetes Service (AKS)**: free control plane; Migrate to Containers tooling; AKS Automatic now manages system nodes (cost included) [80]
- **Wave Planning**: structured large-scale migrations with sequencing, visualization, tracking, and monitoring [11]

**Cons:**
- **SQL Managed Instance expensive**: often the most expensive option for comparable configurations; General Purpose tier has 5-10ms storage IO latency [48]
- **AppCAT limitations**: currently only supports ASP.NET and ASP.NET Core; Java version exists but limited
- **Azure Spring Apps retiring**: March 31, 2028 – all Spring Boot workloads must migrate to Container Apps or AKS [81]
- **Compliance requirements often favor VM**: financial services, healthcare, government often require OS-level control, preferring SQL Server on VM over PaaS [77]

#### Full Re-architecture (Refactor)

**Pros:**
- **Azure Functions**: serverless compute with automatic scaling, pay-per-execution
- **Azure Cosmos DB**: multi-region active-active, 99.999% availability SLA, turnkey global distribution
- **Azure SQL Database Hyperscale**: up to 100TB storage, rapid auto-scaling, serverless compute option
- **Azure Kubernetes Service**: managed Kubernetes with automated updates, scaling, security; community call with financial services case study [80]
- **Azure DevOps**: integrated CI/CD pipelines, artifact feeds, test plans for enterprise development

**Cons:**
- **5-20× cost of lift-and-shift**: $200K-$600K+ for large enterprise applications [22]
- **High complexity**: requires significant architectural changes, new skills, and extensive testing
- **Microsoft recommends deferring modernization**: "modernize during migration only when the team has the skills and time, otherwise defer" [82]
- **Cost management challenges**: Flexera 2025 data shows organizations waste ~27% of cloud spend on average

---

### Google Cloud

#### Lift-and-Shift (Rehost)

**Pros:**
- **Migrate to Virtual Machines**: free service – no cost for the migration tool itself; only pay for consumed resources [3]
- **Per-second billing**: minimum 1 minute, then per-second increments – ideal for variable workloads [26]
- **Sustained Use Discounts**: up to 30% automatic discount with no commitment – best for unpredictable workloads [24]
- **Custom machine types**: configure exact vCPU and RAM, saving 20-30% compared to fixed instance sizes [26]
- **Free egress program**: customers leaving GCP can migrate data out at no cost (60-day migration period) [32]
- **Live migration**: transparent VM maintenance with no downtime – unique among cloud providers [35]

**Cons:**
- **Smaller market share (~13%)**: fewer financial services case studies and partner ecosystem compared to AWS and Azure
- **SQL Server licensing**: BYOL requires License Mobility with Software Assurance; Cloud SQL includes licensing with 4-core minimum, no BYOL option [29]
- **Limited legacy OS support**: no equivalent to AWS EMP or Azure ESUs for end-of-life Windows/SQL Server versions
- **Egress costs**: $0.12/GB starting rate – higher than AWS ($0.09) and Azure ($0.087) for initial tier [32]
- **Fewer compliance certifications**: still comprehensive but narrower breadth than Azure's 100+ offerings

#### Re-platforming

**Pros:**
- **Database Migration Service**: free for homogeneous migrations; CDC-based continuous replication; Gemini-powered schema conversion for heterogeneous [15]
- **Migrate to Containers**: free tool for VM-to-container conversion targeting GKE or Cloud Run – no source code required [6]
- **Cloud SQL**: fully managed, automatic failover, 99.99% SLA; supports SQL Server, PostgreSQL, MySQL; up to 96 CPUs, 624GB memory [49]
- **AlloyDB**: PostgreSQL-compatible with 4× faster transaction processing, 99.99% availability SLA
- **Migration Center**: unified platform with StratoZone technology, Gemini-powered TCO estimation, database discovery and assessment [9]

**Cons:**
- **Cloud SQL SQL Server**: 4-core minimum licensing; no BYOL option; HA incurs only one license for active resource [29]
- **Heterogeneous migration costs**: billed per GB of data processed; 3TB CDC migration approximately $6,659 [15]
- **Oracle migration**: supported via Bare Metal Solution (physical machines) or Oracle-to-PostgreSQL via DMS; no native Oracle managed service
- **Limited SQL Server version support**: Cloud SQL supports SQL Server 2017, 2019, 2022 – no 2014 or earlier

#### Full Re-architecture (Refactor)

**Pros:**
- **Cloud Spanner**: globally distributed, strongly consistent, 99.999% availability SLA – ideal for financial ledgers and trading systems
- **BigQuery**: serverless data warehouse, automatic scaling, $6.25/TB queried; BigQuery Migration Service for Snowflake/Teradata/Databricks migrations [83]
- **GKE Autopilot**: fully managed Kubernetes, no node management, pay-per-pod
- **Cloud Run**: serverless containers, automatic scaling to zero, pay-per-request
- **Axion-based VMs**: 2× better price-performance with Google's custom ARM processors [52]
- **Assured Workloads**: automatic compliance controls for regulated industries – FedRAMP, IL5, PCI DSS, HIPAA, EU Sovereign Controls [61]

**Cons:**
- **5-20× cost of lift-and-shift**: $150K-$750K per line-of-business application [23]
- **6-24 months timeline**: significant investment in architecture redesign and development
- **Smaller container ecosystem**: fewer third-party integrations compared to Azure's .NET ecosystem or AWS's comprehensive tooling
- **Cloud Spanner complexity**: requires careful schema design for global distribution; not suitable for all workloads

---

## Strategic Recommendations for Financial Institutions

### When to Choose Each Approach

| Scenario | Recommended Approach | Primary Provider | Rationale |
|----------|---------------------|------------------|-----------|
| Data center lease expiry (6-12 months) | Lift-and-Shift | AWS or Azure | Fastest time-to-cloud, no code changes, 30% cost savings |
| Microsoft-centric workloads (SQL Server, .NET, Windows) | Lift-and-Shift or Re-platform | Azure | Azure Hybrid Benefit (up to 76% savings), free ESUs, best licensing economics |
| Oracle-heavy estate | Lift-and-Shift | AWS (RDS for Oracle BYOL) | RDS avoids 2:1 vCPU penalty; dedicated hosts for licensing optimization |
| Legacy modernization with 3-5 year horizon | Re-platform | Any, depending on existing stack | Balance of effort and value; hybrid pattern (rehost apps, replatform databases) |
| High-performance financial modeling | Re-architecture | AWS or GCP | AWS: 3,000 parallel containers (RenaissanceRe); GCP: Cloud Spanner, BigQuery |
| Low-latency trading (sub-millisecond) | Lift-and-Shift or Re-architecture | AWS (Local Zones, Outposts) | 50μs within AZ, 400μs across AZs; Direct Connect for hybrid; placement optimization |
| Strict data residency (EU, Canada, Saudi Arabia) | Any | GCP (Assured Workloads) or AWS (European Sovereign Cloud) | Region-restricted deployments, personnel access controls, independent cloud structures |
| Multi-cloud strategy | Lift-and-Shift initially | Any | Use free egress programs (GCP, AWS) and avoid lock-in; re-platform later |

### Key Financial Services Considerations

1. **Compliance is table stakes, not a differentiator**: All three providers offer PCI DSS Level 1, SOC 2, and HIPAA. The differentiator is the breadth of regional financial regulations (Azure leads with 100+ offerings) and ease of compliance management (GCP's Assured Workloads, AWS's Artifact, Azure's Policy).

2. **Licensing costs can dominate TCO**: For Microsoft-centric organizations, Azure Hybrid Benefit can reduce Windows/SQL Server costs by up to 76%. AWS and GCP can be significantly more expensive for these workloads. Oracle customers should carefully evaluate the 2:1 vCPU penalty on AWS and Azure vs. OCI or dedicated hosts.

3. **Egress costs are the hidden tax**: Financial/trading workloads typically incur $1,000-$8,500/month in egress fees (25-35% of cloud bill). All three providers have free data transfer programs, but with significant caveats (full account exit, 60-day window, approval required).

4. **Disaster recovery is non-negotiable**: The 2025 AWS US-East-1 outage (15 hours) and GCP global outage (3 hours) demonstrate that multi-region architecture is essential. Financial institutions should plan for active-passive or active-active configurations, not just availability zones.

5. **Migration strategy is workload-specific**: "There is no single correct way to move to the cloud, only a correct way to move each workload." [82] A portfolio approach (retire 10-20% of apps, rehost 50-70%, replatform 15-25%, re-architect 5-10%) is recommended for large-scale enterprise migrations.

---

## Sources

[1] AWS Application Migration Service (MGN) – Lift-and-Shift Migration: https://aws.amazon.com/application-migration-service/

[2] Azure Migrate – Comprehensive Migration Tool: https://azure.microsoft.com/en-us/products/azure-migrate

[3] Migrate to Virtual Machines – Google Cloud: https://cloud.google.com/products/cloud-migration/virtual-machines

[4] AWS Database Migration Service: https://aws.amazon.com/dms/

[5] Azure Database Migration Service Pricing: https://azure.microsoft.com/en-us/pricing/details/database-migration

[6] Migrate to Containers – Google Cloud: https://cloud.google.com/products/cloud-migration/containers

[7] AWS Migration Hub Deprecation Notice: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/what-is-migrationhub-orchestrator.html

[8] Azure Migrate Release History: https://docs.azure.cn/en-us/migrate/whats-new?view=migrate

[9] Google Cloud Migration Center Overview: https://docs.cloud.google.com/migration-center/docs/migration-center-overview

[10] AWS Migration Hub Orchestrator: https://docs.aws.amazon.com/migrationhub-orchestrator/latest/userguide/what-is-migrationhub-orchestrator.html

[11] Azure Migrate Wave Planning: https://docs.azure.cn/en-us/migrate/whats-new?view=migrate

[12] Google Cloud Foundation Fabric: https://github.com/GoogleCloudPlatform/cloud-foundation-fabric

[13] Oracle Database to AWS Migration Cost: https://migrationcost.com/oracle-to-aws-migration-cost

[14] Azure Database Migration Service (Classic) Pricing: https://azure.microsoft.com/en-us/pricing/details/database-migration

[15] Google Cloud Database Migration Service Overview: https://docs.cloud.google.com/database-migration/docs/overview

[16] AWS TCO Calculation Guide: https://www.cloudzero.com/blog/tco-aws

[17] Azure Hybrid Benefit Pricing: https://azure.microsoft.com/en-us/pricing/offers/hybrid-benefit

[18] Google Cloud Pricing Calculator: https://cloud.google.com/products/calculator

[19] AWS Transform MGN Pricing: https://aws.amazon.com/application-migration-service/pricing

[20] Azure Site Recovery Pricing: https://azure.microsoft.com/en-us/pricing/details/site-recovery

[21] Google Cloud Storage Transfer Service: https://cloud.google.com/storage-transfer-service

[22] Lift and Shift vs Re-architect Cost Comparison: https://thecompetenza.com/blog/lift-and-shift-vs-rearchitect-cloud-migration-strategy

[23] Lift and Shift vs Re-platform vs Re-architect: https://www.sequentur.com/lift-and-shift-vs-re-platform-vs-re-architect-choosing-the-right-cloud-migration-strategy

[24] AWS Egress Costs: https://www.nops.io/blog/aws-egress-costs-and-how-to-avoid

[25] Azure Hybrid Benefit Official Page: https://azure.microsoft.com/en-us/pricing/offers/hybrid-benefit

[26] Google Cloud Compute Engine Pricing: https://cloud.google.com/products/compute/pricing

[27] AWS SQL Server Licensing Guide: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/sql-server-licensing.html

[28] Azure Extended Security Updates FAQ: https://learn.microsoft.com/en-us/lifecycle/faq/extended-security-updates

[29] SQL Server Licensing on Google Cloud VMware Engine: https://docs.cloud.google.com/vmware-engine/docs/vmware-ecosystem/sql-server-licensing

[30] AWS Data Transfer Pricing: https://www.cloudflare.com/learning/cloud/what-is-aws-data-transfer-pricing

[31] Azure SQL Database Pricing: https://azure.microsoft.com/en-us/pricing/details/azure-sql-database/single

[32] Google Cloud Exit Program: https://cloud.google.com/exit-cloud

[33] AWS Elastic Disaster Recovery: https://aws.amazon.com/disaster-recovery/pricing

[34] Azure Availability Zones: https://azure.microsoft.com/en-us/explore/global-infrastructure/availability-zones

[35] Google Cloud Regions and Zones: https://docs.cloud.google.com/compute/docs/regions-zones

[36] AWS Application Migration Service: Process and Best Practices: https://faddom.com/aws-application-migration-service-process-pricing-and-best-practices

[37] Azure Site Recovery vs Traditional DR: https://www.infrassist.com/blog/azure-site-recovery-vs-traditional-disaster-recovery

[38] Migrate to Virtual Machines Documentation: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0

[39] AWS Lift and Shift Strategy Guide: https://cloudtech.com/feeds/blog/lift-shift-aws

[40] Azure Site Recovery Costs Breakdown: https://criticalcloud.ai/blog/azure/azure-site-recovery-costs-breakdown

[41] 6 Steps to Google Cloud Migration: https://faddom.com/6-steps-to-google-cloud-migration-and-critical-best-practices

[42] AWS Disaster Recovery Strategies: https://n2ws.com/blog/aws-disaster-recovery/aws-disaster-recovery

[43] Modern Azure Resilience with Mark Russinovich: https://techcommunity.microsoft.com/blog/reliability-and-resiliency-in-azure/modern-azure-resilience-with-mark-russinovich/4508967

[44] Google Cloud Disaster Recovery: https://www.firefly.ai/academy/google-cloud-disaster-recovery

[45] AWS Migration Strategies (6 Rs): https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud

[46] Lift-and-Shift to Azure: A Strategic Approach: https://www.viacode.com/lift-and-shift-to-azure-a-strategic-cloud-migration-approach

[47] Google Cloud Migration Center: Database Discovery and Assessment: https://cloud.google.com/blog/products/infrastructure-modernization/database-discovery-and-assessment-with-migration-center

[48] Azure SQL Managed Instance Resource Limits: https://learn.microsoft.com/en-us/azure/azure-sql/managed-instance/resource-limits?view=azuresql

[49] Google Cloud SQL Pricing: https://www.trustradius.com/products/google-cloud-sql/pricing

[50] AWS Serverless Architecture for Financial Modelling: https://aws.amazon.com/blogs/hpc/a-serverless-architecture-for-high-performance-financial-modelling

[51] Azure SQL Database Serverless: https://azure.microsoft.com/en-us/pricing/details/azure-sql-database/single

[52] Google Cloud Compute Engine Product Page: https://cloud.google.com/products/compute

[53] AWS Auto Scaling Predictive Scaling: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html

[54] Azure Architecture Strategies for Availability Zones: https://learn.microsoft.com/en-us/azure/well-architected/design-guides/regions-availability-zones

[55] Google Cloud Sustained Use Discounts Guide: https://costimizer.ai/blogs/sustained-use-discounts

[56] AWS Low Latency for Trading: https://aws.amazon.com/blogs/web3/optimize-tick-to-trade-latency-for-digital-assets-exchanges-and-trading-platforms-on-aws-part-2

[57] Azure Availability Zones Documentation: https://azure.microsoft.com/en-us/explore/global-infrastructure/availability-zones

[58] Google Cloud Global Locations: https://cloud.google.com/about/locations

[59] AWS Cloud Compliance: https://aws.amazon.com/compliance

[60] Azure Compliance Documentation: https://learn.microsoft.com/en-us/azure/compliance

[61] Google Cloud Assured Workloads: https://cloud.google.com/security/products/assured-workloads

[62] AWS Security Hub Standards Reference: https://docs.aws.amazon.com/securityhub/latest/userguide/standards-reference.html

[63] Azure Policy for Financial Services Compliance: https://oneuptime.com/blog/post/2026-02-16-how-to-set-up-azure-policy-for-financial-services-regulatory-compliance-auditing/view

[64] Google Cloud Security Command Center: https://cloud.google.com/security-command-center

[65] AWS Compliance: FIPS 140: https://aws.amazon.com/compliance

[66] Azure Dedicated HSM Documentation: https://learn.microsoft.com/en-us/azure/cloud-hsm/overview

[67] Google Cloud Key Management Service: https://docs.cloud.google.com/kms/docs/key-management-service

[68] AWS European Sovereign Cloud: https://aws.amazon.com/compliance/soc-faqs

[69] Azure Service Trust Portal: https://servicetrust.microsoft.com

[70] Google Cloud Transfer Appliance EU Data Residency: https://docs.cloud.google.com/transfer-appliance/docs/4.0/overview

[71] AWS User Guide for Federally Regulated Financial Institutions in Canada: https://d1.awsstatic.com/onedam/marketing-channels/website/public/Canada-FinServ-ComplianceGuide-FederallyRegulatedFinancialInstitutions.pdf

[72] Azure Compliance Offerings (PDF): https://static1.squarespace.com/static/5770fb98bebafbef665cb19a/t/6078241b5dc58301d23fdea5/1618486303562/Microsoft+Azure+Compliance+Offerings.pdf

[73] Cloud4C Google Cloud Migration Services: https://www.cloud4c.com/google-cloud-services/gcp-migration

[74] AWS EMP End of Life: https://cloudhouse.com/aws-emp-technology-end-of-life

[75] AWS Prescriptive Guidance: Migration Strategies: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-guide/migration-strategies.html

[76] Windows Server End of Support Key Dates: https://www.tenforums.com/windows-10-news/190597-windows-server-end-support-key-dates.html

[77] SQL on Azure: VM vs Managed Instance vs SQL DB: https://red9.com/blog/sql-vm-vs-azure-mi-vs-azure-sql-database

[78] Azure Cloud HSM Overview: https://learn.microsoft.com/en-us/azure/cloud-hsm/overview

[79] Azure Migrate Application and Code Assessment: https://www.codemag.com/Article/2405051/Preparing-for-Azure-with-Azure-Migrate-Application-and-Code-Assessment

[80] AKS Community Call June 2026: https://www.youtube.com/watch?v=3GQkcyVZhEY

[81] Azure Spring Apps Retirement Announcement: https://learn.microsoft.com/en-us/azure/spring-apps/basic-standard/retirement-announcement

[82] Azure Migration Strategy: The 6 Rs Explained: https://www.apps4rent.com/blog/azure-migration-strategy-6-rs

[83] Google Cloud BigQuery Migration Service: https://www.youtube.com/watch?v=vY_m9dM6WxE
