# Comprehensive Comparison of Cloud Migration Strategies for Finance: AWS, GCP, and Azure

## Executive Summary

Financial institutions migrating from on-premises data centers to the cloud face a critical decision: which migration approach and which cloud provider best serves their regulatory, performance, and cost requirements. This report provides a detailed, dimension-by-dimension comparison of three migration strategies—**Lift-and-Shift (Rehost)**, **Re-platforming**, and **Full Re-architecture**—across **Amazon Web Services (AWS)**, **Google Cloud Platform (GCP)**, and **Microsoft Azure**, specifically tailored to large-scale enterprise applications in the finance industry.

The analysis covers five dimensions: (1) Tooling & Services, (2) Cost Modeling (TCO, migration costs, operational expenses), (3) Downtime & Business Continuity Risks, (4) Performance & Scalability Post-Migration, and (5) Security & Compliance (PCI-DSS, data residency, regulatory adherence). Each approach and provider combination is evaluated for its suitability in regulated financial environments where PCI-DSS v4.0, data residency laws, SOC 2, and other financial regulations (FINRA, FFIEC, GLBA, GDPR) apply.

The key finding is that **no single approach or provider is universally optimal**—the choice depends on workload characteristics, regulatory posture, timeline, and risk tolerance. Lift-and-Shift offers the fastest path to cloud with the lowest migration cost but highest ongoing operational expense. Re-platforming provides the best balance of cost savings and operational efficiency for most financial workloads. Full Re-architecture delivers the greatest long-term benefits but requires the highest upfront investment and is best suited for strategic modernization of core financial systems.

---

## Section 1: Lift-and-Shift (Rehost)

### 1.1 Overview

Lift-and-shift migrates workloads from on-premises to cloud infrastructure with minimal modifications. This approach preserves existing application architecture, operating systems, and database configurations. It is the fastest path to cloud for financial institutions needing to exit data centers under regulatory deadlines, merger-driven consolidation timelines, or capacity constraints.

### 1.2 Tooling & Services

**AWS:**

- **AWS Application Migration Service (MGN)** — The primary tool for lift-and-shift migrations. MGN provides continuous replication of entire servers with minimal downtime cutover. It replaced CloudEndure Migration and is fully integrated with AWS Migration Hub for tracking progress. MGN supports Windows, Linux, and most major enterprise databases.
- **AWS Database Migration Service (DMS)** — Supports homogeneous database migrations (Oracle to Oracle, SQL Server to SQL Server on EC2/RDS) with near-real-time replication.
- **AWS Migration Hub** — Central dashboard for tracking migration progress across multiple tools and accounts.
- **AWS Migration Evaluator** — Free tool for building a business case, analyzing on-premises infrastructure usage, and providing cost estimates.
- **AWS Application Discovery Service** — Agentless and agent-based discovery for server utilization, dependencies, and network connections.
- **AWS CloudFormation / Terraform** — Infrastructure as Code for provisioning target environments.
- **AWS Control Tower** — Multi-account governance with PCI-DSS enforcement guardrails.
- **Partner Solutions**: CloudHealth (cost management), Flexera (license compliance), Turbonomic (resource optimization).

**GCP:**

- **Google Cloud Migration Center** — Unified hub for all migration activities, portfolio view, wave planning, and progress tracking.
- **Google Cloud StratoZone** — Automated discovery of on-premises server inventory, dependencies, utilization metrics, and licensing. Generates detailed migration plans with right-sizing recommendations.
- **Migrate to Virtual Machines (formerly Velostrata)** — Agentless replication of on-premises VMs (VMware, Hyper-V, AWS, Azure) to GCP Compute Engine. Supports cutover replication, wave-based migrations, and test clones.
- **Database Migration Service (DMS)** — Supports heterogeneous and homogeneous migrations (Oracle, SQL Server, MySQL, PostgreSQL → Cloud SQL).
- **Transfer Appliance** — Physical data shipping appliance (10TB–200TB) for initial petabyte-scale data migration, encrypted at rest with tamper-evident chain-of-custody.
- **CloudSimple (Google Cloud VMware Engine)** — Native VMware SDDC on GCP for zero-modification lift-and-shift of VMware workloads.
- **Cloud Deployment Manager / Terraform** — IaC for resource provisioning.
- **Partner Solutions**: Carbonite Migrate, NetApp Cloud Volumes ONTAP, Google Cloud Professional Services.

**Azure:**

- **Azure Migrate** — Central hub for discovery, assessment, and migration. **Azure Migrate: Discovery and Assessment** discovers on-premises servers via appliance-based or agentless discovery.
- **Azure Migrate: Server Migration** — Agentless VM migration (VMware, Hyper-V, physical servers) with replication to Azure Managed Disks.
- **Azure Site Recovery (ASR)** — Orchestrates replication for migration and ongoing DR. Supports multi-VM consistency groups for financial application tiers.
- **Azure Database Migration Service (DMS)** — Offline mode for SQL Server → Azure SQL VM or SQL Managed Instance.
- **Azure Data Box family** — Offline data transfer (Data Box Disk, Data Box, Data Box Heavy) for large financial datasets.
- **Azure Blueprints** — Pre-defined compliance blueprints (PCI-DSS v4.0, ISO 27001) to govern the migrated environment.
- **Azure Policy** — Enforce tags, region restrictions (data residency), SKU sizes, and encryption at deploy time.
- **Partner Solutions**: Cloudamize (cost assessment), Turbonomic (right-sizing), Carbonite (agentless migration), Movere (discovery).

### 1.3 Cost Modeling

| Cost Element | AWS | GCP | Azure |
|---|---|---|---|
| **TCO Calculator** | AWS TCO Calculator, Migration Evaluator | GCP TCO Calculator | Azure TCO Calculator |
| **Migration Cost** | Low (MGN is free, DMS pay-per-use) | Low (Migrate to VMs included in Migration Center) | Low (Azure Migrate is free, ASR pay-per-use) |
| **Compute Pricing** | Per-second billing (Linux), per-hour (Windows) | Per-second billing (all OS, min 1 minute) | Per-minute billing (Linux), per-hour (Windows) |
| **Discount Programs** | Reserved Instances (up to 72%), Savings Plans (up to 66%), Spot (60-90%) | Committed Use Discounts (1yr: 57%, 3yr: 70%+), Sustained Use (20-30%), Spot (60-91%) | Reserved Instances (1yr: 40%, 3yr: 60%), Savings Plan (20-50%), Spot (60-90%) |
| **License Portability** | BYOL for Windows, SQL Server, Oracle; License Mobility for SQL Server; AWS License Manager | BYOL for Windows, SQL Server, SAP; License Mobility for SQL Server; CloudSimple for VMware | Azure Hybrid Benefit (up to 55% on SQL Server, 40% on Windows Server); Extended Security Updates for legacy OS |
| **Data Transfer** | Ingress free, egress $0.09/GB (first 10TB), Direct Connect reduces costs | Ingress free, egress $0.12/GB (first 100GB free), Cloud Interconnect reduces costs | Ingress free, egress varies, ExpressRoute reduces costs |
| **Ongoing OpEx** | Highest (self-managed VMs, OS patching, DBA overhead) | Highest (same as AWS) | Highest (same as AWS) |
| **Typical 3-Year TCO** | Baseline (100%) | Baseline (100%) | Baseline (100%) |

**Key Insight for Finance:** Lift-and-shift preserves existing licensing models, so financial institutions with significant investments in Microsoft SQL Server or Windows Server benefit most from Azure Hybrid Benefit. AWS offers strong Oracle BYOL support via Dedicated Hosts. GCP's per-second billing and custom machine types provide the most granular cost optimization for variable financial workloads.

### 1.4 Downtime & Business Continuity

| Factor | AWS | GCP | Azure |
|---|---|---|---|
| **Replication Tool** | AWS MGN (continuous replication, RPO seconds) | Migrate to VMs (continuous replication, RPO 30 seconds) | Azure Site Recovery (continuous replication, RPO 30 seconds) |
| **Typical Cutover Downtime** | 5–30 minutes per application | 1–4 hours per application wave | 15 minutes–4 hours |
| **Multi-AZ HA** | Auto Scaling groups across AZs, RDS Multi-AZ (60-120s failover) | Managed Instance Groups across zones, Cloud SQL HA (<60s failover) | Availability Sets/Zones, Azure SQL HA (60-120s failover) |
| **Multi-Region DR** | AWS DRS, Route 53, Global Accelerator; RPO seconds, RTO minutes | Migrate to VMs DR, Cloud Load Balancing, Cloud Interconnect; RPO 30s, RTO minutes | Azure Site Recovery (Azure-to-Azure), Traffic Manager, Front Door; RPO 30s, RTO minutes |
| **Live Migration** | Not available (host maintenance requires stop/start) | **GCP Live Migration** — VMs continue running during host maintenance, no downtime | Not available (host maintenance requires reboot) |
| **Connectivity** | AWS Direct Connect (dedicated, 99.95% SLA), VPN | Cloud Interconnect (dedicated, 99.99% SLA), Cloud VPN, Private Google Access | ExpressRoute (dedicated, 99.95% SLA), VPN Gateway |
| **DR Options** | Pilot Light, Warm Standby, Multi-Site via AWS DRS | Pilot Light, Warm Standby via Migrate to VMs DR | Pilot Light, Warm Standby via Azure Site Recovery |
| **Zero-Downtime Migration** | Blue/Green with Route 53 weighted routing, MGN test launches | Blue/Green with Cloud Load Balancing, test clones | Blue/Green with Traffic Manager, Azure Front Door |

**Key Insight for Finance:** GCP's Live Migration is a unique differentiator—financial VMs remain online during host maintenance, security patching, and hardware updates. This is critical for trading systems and payment processing where even planned downtime is costly. AWS and Azure require stop/start or migration to new hosts during maintenance.

### 1.5 Performance & Scalability

| Aspect | AWS | GCP | Azure |
|---|---|---|---|
| **Compute Families** | M5/M6i (memory), C5/C6i (compute), R5/R6i (memory-optimized), Graviton (ARM, 40% better price-performance) | C4/C3 (compute), M3 (memory, 4TB RAM), N4/N2 (general), Z3 (GPU), H3 (SAP HANA) | E-series (memory, up to 672GB), M-series (memory, up to 5.7TB), L-series (storage) |
| **Storage Performance** | Premium SSD v2 (80K IOPS, 1,200 MB/s), Ultra Disk (160K IOPS, 2,000 MB/s) | Hyperdisk (3.2M IOPS, 120K IOPS/vCPU, sub-ms latency), Persistent Disk SSD (30K IOPS) | Premium SSD v2 (80K IOPS, 1,200 MB/s), Ultra Disk (160K IOPS, 2,000 MB/s), Azure NetApp Files (4.5 GB/s) |
| **Network Performance** | Enhanced Networking (up to 100 Gbps), Global Accelerator | Jupiter networking (1,000 Gbps per VM), Premium Tier (private backbone), 200+ PoPs | Accelerated Networking (up to 30 Gbps), Azure Front Door |
| **Auto Scaling** | Auto Scaling groups, EC2 Auto Scaling, target tracking policies | Managed Instance Groups, regional/zonal, auto-healing, autoscaling based on CPU/memory/custom metrics | VM Scale Sets, autoscale based on metrics, Azure Autoscale |
| **Database Performance** | RDS (up to 32 vCPUs, 244GB RAM), Aurora (5x MySQL, 3x PostgreSQL) | Cloud SQL (up to 96 vCPUs, 624GB RAM, 30K IOPS), AlloyDB (4x PostgreSQL) | Azure SQL Hyperscale (100TB, 100K IOPS), SQL Managed Instance (128 vCores, 120K IOPS) |

**Key Insight for Finance:** GCP's Hyperdisk delivers up to 3.2M IOPS with sub-millisecond latency, which is critical for high-frequency trading databases and real-time payment processing. AWS Graviton processors offer 40% better price-performance for ARM-compatible workloads. Azure's M-series VMs with up to 5.7TB RAM are ideal for large SAP HANA and in-memory database deployments.

### 1.6 Security & Compliance

| Factor | AWS | GCP | Azure |
|---|---|---|---|
| **PCI-DSS Certification** | PCI-DSS v4.0 Level 1 (all regions) | PCI-DSS v4.0 compliant (all regions) | PCI-DSS v4.0 Level 1 (all regions) |
| **Data Residency Controls** | AWS Control Tower, Service Control Policies, region restrictions | Assured Workloads (data residency enforcement, CMEK, Access Transparency, Access Approval) | Azure Policy (Allowed Locations), Azure Blueprints, Azure Sovereign Clouds (Government, China 21Vianet) |
| **Encryption** | AWS KMS (CMK, HMAC), CloudHSM (FIPS 140-2 Level 3), DynamoDB/Aurora encryption at rest | Cloud KMS, Cloud HSM (FIPS 140-2/3 Level 3), Confidential VMs (AMD SEV-SNP, Intel TDX) | Azure Key Vault, Managed HSM (FIPS 140-2 Level 3), Dedicated HSM (FIPS 140-2 Level 3), Confidential Computing (Intel SGX, AMD SEV-SNP, Intel TDX) |
| **Confidential Computing** | AWS Nitro Enclaves (isolated compute environments), no full VM memory encryption | Confidential VMs (AMD SEV-SNP, memory encrypted at runtime), Confidential GKE Nodes (Intel TDX), Confidential Space | Confidential VMs (AMD SEV-SNP, Intel TDX), Confidential Containers (AKS + Intel SGX), Confidential Databases (SQL Always Encrypted with secure enclaves) |
| **Network Security** | AWS WAF, Shield Advanced (DDoS), Network Firewall, Security Groups, NACLs | Cloud Armor (WAF, DDoS, rate limiting), Cloud Firewall (next-gen, L7 inspection), VPC Service Controls | Azure WAF, DDoS Protection Standard, Azure Firewall Premium (IDPS, TLS inspection), NSGs, Virtual Network Manager |
| **Governance** | AWS Control Tower, Organizations, Service Control Policies, CloudTrail, Config | Organization Policies, IAM Conditions, Access Transparency, Access Approval, Security Command Center, Chronicle SIEM | Azure Blueprints, Azure Policy, Microsoft Defender for Cloud, Microsoft Sentinel, Purview Compliance Manager |
| **Compliance Scope (Customer Responsibility)** | **Broadest** — OS, DB, application, patching, vulnerability scanning, access controls | **Broadest** — same as on-premises, but GCP adds infrastructure-layer security | **Broadest** — same as on-premises, with Azure Policy enforcement |

**Key Insight for Finance:** GCP's Assured Workloads with Access Transparency and Access Approval provide unique capabilities for financial institutions that need to audit and approve Google staff access to their data. AWS Nitro Enclaves offer isolated compute environments for sensitive workloads but do not provide full VM memory encryption like GCP's Confidential VMs. Azure's Dedicated HSM is FIPS 140-2 Level 3 validated for payment HSM workloads (PIN processing, card personalization).

### 1.7 Pros and Cons for Regulated Finance Environments

**AWS Lift-and-Shift:**

| Pros | Cons |
|---|---|
| Fastest time-to-cloud for data center exits | Highest ongoing operational cost (self-managed VMs, OS patching) |
| MGN provides near-zero downtime migration with RPO of seconds | No live migration — VMs must be stopped/started during host maintenance |
| Strong licensing support for Oracle BYOL via Dedicated Hosts | No full VM memory encryption (Nitro Enclaves are isolated, not full VM) |
| Mature partner ecosystem (CloudHealth, Flexera, Turbonomic) | Compliance scope is identical to on-premises — no reduction in PCI-DSS controls |
| AWS Control Tower provides strong multi-account governance with PCI-DSS guardrails | Data residency requires manual enforcement via Service Control Policies |

**GCP Lift-and-Shift:**

| Pros | Cons |
|---|---|
| **Live Migration** — VMs stay online during host maintenance, critical for trading systems | Smaller partner ecosystem for financial services compared to AWS/Azure |
| Per-second billing with custom machine types (no instance size lock-in) | Less mature VMware migration tools (CloudSimple, not native VMware on GCP) |
| Assured Workloads provides data residency enforcement, CMEK, and Access Transparency | Fewer PCI-DSS-specific compliance blueprints compared to Azure |
| Hyperdisk delivers up to 3.2M IOPS with sub-millisecond latency for trading databases | Smaller global region footprint (40+ regions vs. AWS 30+ and Azure 60+) |
| Jupiter networking provides 1,000 Gbps per VM with 2x bisection bandwidth | Limited support for legacy Windows/SQL Server workloads (no Extended Security Updates) |

**Azure Lift-and-Shift:**

| Pros | Cons |
|---|---|
| **Azure Hybrid Benefit** — up to 55% savings on SQL Server, 40% on Windows Server with existing SA licenses | No live migration — VMs must be rebooted for host maintenance |
| Extended Security Updates for Windows Server 2012 and SQL Server 2012 (3 years post-EOL) | Per-hour billing for Windows VMs (vs. per-second for Linux) |
| Azure Site Recovery provides multi-VM consistency groups for application-consistent DR | Higher egress costs for data transfer between regions |
| Azure Blueprints with PCI-DSS v4.0 template provides one-click compliance deployment | Compliance scope is identical to on-premises |
| M-series VMs with up to 5.7TB RAM for large SAP HANA and in-memory databases | Requires careful license management for SQL Server (License Mobility) |

---

## Section 2: Re-platforming

### 2.1 Overview

Re-platforming involves moving workloads to cloud-managed services with moderate application modifications—typically migrating databases to managed services (RDS, Cloud SQL, Azure SQL), containerizing applications, or moving to PaaS web hosting. Application code remains largely unchanged, but infrastructure is modernized. This is the "sweet spot" for most financial workloads, offering significant cost savings and operational efficiency without the complexity of full re-architecture.

### 2.2 Tooling & Services

**AWS:**

- **AWS DMS + Schema Conversion Tool (SCT)** — Heterogeneous database migrations (Oracle → Aurora, SQL Server → RDS for PostgreSQL, MySQL → Aurora). SCT automates schema and code transformation.
- **AWS MGN** — Can modify target EC2 instance type, AMI, or configuration during replication (e.g., Windows Server 2012 → 2022, Linux → Amazon Linux).
- **Amazon RDS / Aurora** — Managed databases with automated backups, patching, Multi-AZ, and read replicas. RDS Custom for Oracle/SQL Server when more control is needed.
- **Amazon ECS / EKS** — Managed container services for re-platforming containerized applications.
- **AWS Elastic Beanstalk** — PaaS for web applications, abstracting infrastructure management.
- **AWS CloudFormation / Terraform** — IaC for re-platforming with managed services.

**GCP:**

- **Database Migration Service (DMS) + Datastream** — Heterogeneous migrations (Oracle → AlloyDB, SQL Server → Cloud SQL, MySQL/PostgreSQL → Cloud SQL). Datastream provides real-time CDC for near-zero downtime.
- **Migrate to Containers** — Analyzes VMs, generates container images, Kubernetes manifests, and deployment configurations. Supports VM-to-container conversion without re-architecting.
- **Cloud SQL / AlloyDB / Spanner** — Managed databases. AlloyDB is 4x faster than standard PostgreSQL with built-in columnar engine and adaptive indexing.
- **BigQuery Data Transfer Service** — Automated data ingestion from on-premises databases into BigQuery for analytics.
- **Cloud Composer (Airflow)** — Workflow orchestration for ETL/ELT pipelines.
- **Cloud Pub/Sub** — Async messaging for event-driven workflows.

**Azure:**

- **Azure Migrate: App Containerization** — Packages applications into containers (ASP.NET, Java) with minimal code changes.
- **Azure Database Migration Service (DMS)** — Online mode (continuous sync) for SQL Server → Azure SQL Managed Instance or Azure SQL Database. Uses DMA for compatibility assessment.
- **Azure SQL Database / SQL Managed Instance** — PaaS databases with Hyperscale tier (100TB, 100K IOPS) and Serverless tier for dev/test.
- **Azure App Service / AKS** — Managed web hosting and container orchestration.
- **Azure Logic Apps** — Replace legacy BizTalk, SSIS, or custom integration workflows.
- **Azure DevOps + GitHub Actions** — CI/CD pipelines for re-platformed applications.
- **Azure Hybrid Benefit** — Apply existing SQL Server/Windows Server licenses to PaaS services.

### 2.3 Cost Modeling

| Cost Element | AWS | GCP | Azure |
|---|---|---|---|
| **Migration Cost** | Medium (DMS, SCT, testing, app changes) | Medium (DMS, Datastream, containerization) | Medium (DMS, App Containerization, testing) |
| **Compute Savings** | RDS: 20-40% vs. self-managed; Aurora: 5x performance vs. MySQL | Cloud SQL: 30-50% vs. self-managed; AlloyDB: 4x performance vs. PostgreSQL | Azure SQL: 30-50% vs. SQL Server on VM; AHB: up to 55% on SQL Server |
| **Database Pricing** | RDS: $0.015-0.05/vCPU-hour + storage; Aurora: $0.03-0.10/vCPU-hour | Cloud SQL: $0.015-0.05/vCPU-hour; AlloyDB: $0.03-0.08/vCPU-hour; Spanner: $0.90-9.00/node-hour | Azure SQL: $0.02-0.08/vCore-hour; SQL MI: $0.03-0.12/vCore-hour |
| **Container Pricing** | ECS: no additional cost; EKS: $0.10/hour per cluster | GKE: $0.10/hour per cluster (Autopilot: no cost); Cloud Run: pay-per-use | AKS: $0.10/hour per cluster (free for first 10 clusters per subscription) |
| **Discount Programs** | RDS RIs (up to 60%), Aurora RIs (up to 60%) | Cloud SQL CUDs (1yr: 40%, 3yr: 55%); AlloyDB CUDs (1yr: 40%, 3yr: 55%) | Azure SQL RIs (up to 60%), AHB + RIs combined (up to 80%) |
| **Ongoing OpEx** | Medium (managed DB reduces DBA overhead, but still some manual management) | Medium (managed DB, but GKE requires cluster management) | Medium (managed DB, App Service reduces web tier management) |
| **Typical 3-Year TCO** | 60-75% of lift-and-shift baseline | 60-75% of lift-and-shift baseline | 60-75% of lift-and-shift baseline |

**Key Insight for Finance:** All three providers offer similar cost savings for re-platforming (40-60% vs. on-premises). Azure's combination of Azure Hybrid Benefit and Reserved Instances can deliver up to 80% savings on SQL Server workloads, making it the most cost-effective option for financial institutions with existing Microsoft licenses. GCP's AlloyDB offers 4x performance improvement over standard PostgreSQL, which can reduce database costs by consolidating workloads. AWS Aurora provides 5x performance over standard MySQL and 3x over standard PostgreSQL.

### 2.4 Downtime & Business Continuity

| Factor | AWS | GCP | Azure |
|---|---|---|---|
| **Database Migration Downtime** | Near-zero with DMS ongoing replication; cutover in seconds | Near-zero with Datastream CDC; cutover in seconds | Near-zero with DMS online mode; cutover in 1-2 minutes |
| **Application Cutover** | Blue/Green with Route 53 or Global Accelerator | Blue/Green with Cloud Load Balancing | Blue/Green with Azure Front Door or Traffic Manager |
| **Multi-AZ HA** | RDS Multi-AZ (60-120s failover), Aurora Multi-AZ (<30s failover) | Cloud SQL HA (<60s failover), AlloyDB HA (automatic), Spanner (built-in multi-region) | Azure SQL HA (60-120s failover), SQL MI (99.99% with zone-redundant) |
| **Multi-Region DR** | Aurora Global Database (RPO <1s, failover <1min), RDS cross-region read replicas | AlloyDB cross-region replicas, Spanner multi-region (99.999% SLA), Cloud SQL cross-region | Azure SQL active geo-replication (RPO 0s, failover groups), SQL MI geo-replication |
| **RTO/RPO** | RPO: 0-5s, RTO: 1-5 minutes | RPO: 0-5s, RTO: 1-5 minutes | RPO: 0-5s, RTO: 1-5 minutes |
| **Zero-Downtime Deployment** | RDS blue/green deployments, ECS blue/green with CodeDeploy | Cloud SQL blue/green, GKE rolling updates, Cloud Run traffic splitting | Azure SQL blue/green, App Service deployment slots, AKS rolling updates |

**Key Insight for Finance:** All three providers can achieve near-zero downtime for database re-platforming using CDC (DMS, Datastream, Azure DMS online mode). AWS Aurora Global Database provides the fastest multi-region failover (<1 minute) with RPO under 1 second. GCP Cloud Spanner offers 99.999% SLA with built-in multi-region HA, making it ideal for core banking and trading systems requiring global strong consistency. Azure SQL failover groups enable automated failover with 0 RPO for critical financial databases.

### 2.5 Performance & Scalability

| Aspect | AWS | GCP | Azure |
|---|---|---|---|
| **Database Performance** | Aurora: 5x MySQL, 3x PostgreSQL; RDS: up to 32 vCPUs, 244GB RAM | AlloyDB: 4x PostgreSQL, 100x analytical queries; Spanner: 2M+ reads/s, 200K+ writes/s; Cloud SQL: up to 96 vCPUs, 624GB RAM | Azure SQL Hyperscale: 100TB, 100K IOPS, 100 MB/s log rate; SQL MI: 128 vCores, 120K IOPS |
| **Container Performance** | EKS: 3,000+ node clusters; ECS: 1,000+ tasks per service | GKE: 15,000+ node clusters; Cloud Run: auto-scales from 0 to thousands | AKS: 1,000+ nodes per cluster; Azure Container Instances: burst capacity |
| **Auto Scaling** | Aurora Auto Scaling, RDS Auto Scaling, ECS/EKS HPA, VPA | Spanner auto-scaling, AlloyDB auto-scaling, GKE cluster autoscaler, KEDA | Azure SQL Hyperscale auto-scaling, AKS cluster autoscaler, HPA, KEDA |
| **Latency** | Aurora: sub-ms latency within region; Global Accelerator: anycast routing | Spanner: sub-10ms latency at P99 globally; Premium Tier: 40% lower latency via private backbone | Azure SQL: sub-ms latency; Front Door: global anycast routing |

**Key Insight for Finance:** GCP Cloud Spanner is the only globally distributed, strongly consistent database across all three providers, making it uniquely suited for financial applications requiring ACID transactions across multiple regions. AWS Aurora provides the best performance for MySQL/PostgreSQL-compatible workloads. Azure SQL Hyperscale is ideal for very large databases (up to 100TB) with auto-scaling storage and compute.

### 2.6 Security & Compliance

| Factor | AWS | GCP | Azure |
|---|---|---|---|
| **PCI-DSS Scope Reduction** | Moderate: RDS/Aurora reduce OS and DB patching scope, but still manage application security | Moderate: Cloud SQL/AlloyDB reduce OS and DB scope; VPC Service Controls for data exfiltration prevention | High: Azure SQL reduces OS and SQL Server patching scope; Microsoft manages anti-malware, patching |
| **Managed Service Security** | RDS: encryption at rest (AES-256), TLS 1.3, IAM auth, Audit Logs; Aurora: same plus global database encryption | Cloud SQL/AlloyDB: CMEK, CSEK, IAM, VPC Service Controls, column-level encryption (AlloyDB) | Azure SQL: TDE (transparent data encryption), Always Encrypted, dynamic data masking, row-level security, audit logging |
| **Container Security** | ECR image scanning, Amazon Inspector, EKS security groups, IAM for pods | Artifact Registry scanning, Binary Authorization, GKE Sandbox, Workload Identity, Shielded Nodes | ACR scanning, Microsoft Defender for Containers, Azure Policy for AKS, Workload Identity |
| **Governance** | AWS Config, CloudTrail, GuardDuty, Security Hub | Security Command Center, Security Health Analytics, Event Threat Detection, Chronicle SIEM | Microsoft Defender for Cloud, Microsoft Sentinel, Microsoft Purview Compliance Manager |
| **Data Residency** | Service Control Policies, region restrictions, AWS Artifact for compliance reports | Assured Workloads (data residency, CMEK, Access Transparency, Access Approval) | Azure Policy (Allowed Locations), Azure Blueprints, Azure Sovereign Clouds |

**Key Insight for Finance:** Azure SQL provides the most comprehensive built-in security features for financial databases, including Always Encrypted with secure enclaves, dynamic data masking, and row-level security—all critical for PCI-DSS compliance. GCP's Assured Workloads extends to managed services, providing data residency enforcement and Access Transparency for Cloud SQL, AlloyDB, and Spanner. AWS Aurora supports encryption at rest and in transit with IAM database authentication for fine-grained access control.

### 2.7 Pros and Cons for Regulated Finance Environments

**AWS Re-platforming:**

| Pros | Cons |
|---|---|
| Aurora provides 5x MySQL performance with full MySQL/PostgreSQL compatibility | DMS + SCT requires significant testing for schema conversion (Oracle → Aurora) |
| RDS blue/green deployments enable zero-downtime database migrations | EKS management overhead (control plane, node groups, upgrades) |
| Strong support for Oracle and SQL Server migrations via DMS and SCT | Limited global database options (Aurora Global Database supports only 5 secondary regions) |
| AWS Migration Hub provides centralized tracking across all re-platforming activities | Rightsizing requires careful instance selection (RDS instance types are fixed) |
| Well-Architected Framework provides structured guidance for re-platforming | Less automated compliance enforcement for managed services vs. Azure Policy |

**GCP Re-platforming:**

| Pros | Cons |
|---|---|
| **AlloyDB** delivers 4x PostgreSQL performance with columnar engine and adaptive indexing | Smaller ecosystem of financial services partners for database migrations |
| **Cloud Spanner** provides global strong consistency with 99.999% SLA—ideal for core banking | Spanner pricing is higher than Cloud SQL ($0.90-9.00/node-hour) |
| **Datastream** enables real-time CDC for near-zero downtime database migrations | GKE Autopilot is still maturing for complex financial workloads |
| **Assured Workloads** extends to managed services for data residency and CMEK enforcement | Less mature CI/CD tooling for financial compliance (Cloud Build, Cloud Deploy) |
| **Migrate to Containers** automates VM-to-container conversion without re-architecting | Limited support for legacy Windows workloads (fewer Windows container images) |

**Azure Re-platforming:**

| Pros | Cons |
|---|---|
| **Azure Hybrid Benefit** + RIs can deliver up to 80% savings on SQL Server workloads | Vendor lock-in via Azure Hybrid Benefit (licenses only apply to Azure) |
| **Azure SQL Hyperscale** supports databases up to 100TB with auto-scaling storage | Less mature container migration tooling (App Containerization is newer than GKE Migrate) |
| **Azure SQL Managed Instance** provides near-100% SQL Server compatibility | DMS online mode requires careful monitoring for long-running migrations |
| **Azure Policy** provides granular enforcement of security and compliance at scale | Global database options (Azure SQL geo-replication) are SQL Server-specific |
| **Microsoft Defender for Cloud** provides unified compliance dashboard across all Azure services | Fewer database options for PostgreSQL/MySQL workloads compared to AWS and GCP |

---

## Section 3: Full Re-architecture

### 3.1 Overview

Full re-architecture involves redesigning applications to leverage cloud-native services—serverless, microservices, managed databases, event-driven architectures, and AI/ML capabilities. This approach delivers the greatest long-term benefits (lowest operational cost, highest scalability, best resilience) but requires the highest upfront investment in development, testing, and compliance re-certification. It is best suited for strategic modernization of core financial systems such as trading platforms, payment processing, fraud detection, and core banking.

### 3.2 Tooling & Services

**AWS:**

- **AWS Lambda** — Serverless compute for microservices. Supports PCI-DSS compliant workloads when configured with VPC, encryption, and logging.
- **Amazon API Gateway** — RESTful APIs for frontend microservices. Integrates with AWS WAF, Cognito, and Lambda.
- **Amazon DynamoDB** — Fully managed NoSQL database. PCI-DSS compliant, encryption at rest, VPC endpoints, point-in-time recovery. For high-throughput transaction processing and ledger systems.
- **Amazon Aurora** — Relational database with serverless capabilities (Aurora Serverless v2). Multi-Master for high-availability write workloads.
- **Amazon SQS / SNS / EventBridge** — Event-driven architecture components for decoupling microservices.
- **Amazon ECS / EKS (Fargate)** — Serverless containers. Fargate eliminates EC2 management, reducing PCI-DSS compliance scope.
- **AWS Step Functions** — Workflow orchestration for financial business processes (trade settlement, loan processing, fraud detection).
- **Amazon Kinesis / MSK** — Streaming data services for real-time financial data processing.
- **AWS Well-Architected Framework Tool** — Evaluates re-architected workloads against six pillars.
- **AWS Application Composer** — Visual tool for designing serverless applications.

**GCP:**

- **Cloud Run** — Fully managed serverless containers. 1ms billing granularity, auto-scales to zero. Supports HTTP/2, gRPC, WebSockets.
- **GKE Autopilot** — Serverless Kubernetes. GKE manages nodes, scaling, security. **GKE Enterprise** for multi-cluster, multi-cloud management.
- **Cloud Functions (2nd gen)** — Event-driven functions for fraud detection, transaction processing, notifications.
- **BigQuery** — Serverless data warehouse with petabyte-scale analytics. **BigQuery ML** for ML model training in SQL.
- **Cloud Spanner** — Global, strongly consistent, horizontally scalable database. For core banking, trading systems, payment processing.
- **Firestore** — Serverless NoSQL document database for customer profiles, session data, real-time updates.
- **Cloud Pub/Sub / Eventarc** — Async messaging and event routing for event-driven microservices.
- **Workflows** — Serverless workflow orchestration for financial transaction processing.
- **Vertex AI** — Unified ML platform for fraud detection, credit scoring, algorithmic trading.
- **Dataflow (Apache Beam)** — Unified stream/batch processing for real-time financial analytics.
- **Cloud Deploy** — Managed delivery pipelines for GKE and Cloud Run.

**Azure:**

- **Azure Functions** — Serverless compute for event-driven financial processing (payment validation, fraud detection, trade settlement).
- **Azure API Management** — API gateway with OAuth2, OpenID Connect, throttling, mTLS.
- **Azure Kubernetes Service (AKS)** — Managed Kubernetes with **Azure Container Instances** for burst capacity.
- **Azure Service Bus / Event Grid / Event Hubs** — Event-driven architecture for transaction processing, audit trails, and real-time analytics.
- **Azure Cosmos DB** — Globally distributed, multi-model database. Multi-region writes (0 RPO), 99.999% read availability, autoscale up to 1M RU/s per container.
- **Azure SQL Database (Hyperscale)** — For relational workloads requiring ACID compliance (general ledger, settlements).
- **Azure Logic Apps (Standard)** — Stateful workflows for complex financial processes (KYC, AML, trade lifecycle).
- **Azure Chaos Studio** — Deliberate fault injection to validate resilience of re-architected financial applications.
- **Microsoft Defender for DevOps** — Scans IaC templates, container images, and code for compliance violations pre-deployment.
- **Azure DevOps / GitHub Actions** — Full CI/CD with policy-as-code, container scanning, and deployment gates.

### 3.3 Cost Modeling

| Cost Element | AWS | GCP | Azure |
|---|---|---|---|
| **Migration Cost** | Highest (full application redesign, testing, compliance re-certification, staff training) | Highest (same as AWS) | Highest (same as AWS) |
| **Compute Pricing** | Lambda: $0.0000167/GB-second, $0.20/1M requests; Fargate: $0.000024/vCPU-second | Cloud Run: $0.000024/vCPU-second, $0.0000025/GB-second; Cloud Functions: $0.0000004/invocation | Azure Functions: $0.000016/GB-second, $0.20/1M executions; AKS: $0.10/hour (control plane) |
| **Database Pricing** | DynamoDB: $0.00065/hour per WCU/RCU (provisioned), $1.25/1M requests (on-demand); Aurora Serverless: $0.06-0.12/ACU-hour | Cloud Spanner: $0.90-9.00/node-hour; Firestore: $0.036/100K reads, $0.108/100K writes; BigQuery: $5/TB processed | Cosmos DB: $0.008-0.12/hour per RU/s (provisioned), $0.30/1M RU (serverless); Azure SQL Hyperscale: $0.02-0.08/vCore-hour |
| **Storage Pricing** | DynamoDB: $0.25/GB-month; S3: $0.023/GB-month (Standard) | Firestore: $0.108/GB-month; Cloud Storage: $0.020/GB-month (Standard) | Cosmos DB: $0.25/GB-month; Blob Storage: $0.018/GB-month (Hot) |
| **Discount Programs** | Compute Savings Plans (apply to Lambda, Fargate); DynamoDB Reserved Capacity (up to 50%) | No CUDs for serverless; Spanner CUDs (1yr: 30%, 3yr: 40%) | Azure Savings Plan (apply to Functions, AKS); Cosmos DB Reserved Capacity (up to 65%) |
| **Ongoing OpEx** | **Lowest** — no servers to manage, auto-scaling, no idle costs | **Lowest** — same as AWS, auto-scales to zero | **Lowest** — same as AWS, auto-scales to zero |
| **Typical 3-Year TCO** | 40-60% of lift-and-shift baseline | 40-60% of lift-and-shift baseline | 40-60% of lift-and-shift baseline |

**Key Insight for Finance:** All three providers offer similar serverless pricing models. AWS Lambda and DynamoDB are the most mature serverless services with the largest ecosystem. GCP Cloud Run and Cloud Spanner offer unique advantages for containerized serverless and globally consistent databases. Azure Cosmos DB provides multi-region writes with 0 RPO and 99.999% read availability, making it ideal for active-active financial architectures. The cost savings from re-architecture (50-70% vs. on-premises) come primarily from eliminating idle capacity, reducing operational staff, and leveraging pay-per-use pricing.

### 3.4 Downtime & Business Continuity

| Factor | AWS | GCP | Azure |
|---|---|---|---|
| **Architecture Pattern** | Strangler Fig (incremental microservices migration), blue/green, canary | Strangler Fig, blue/green, traffic splitting, canary | Strangler Fig, blue/green, deployment slots, canary |
| **Multi-AZ Availability** | Lambda/DynamoDB/API Gateway are inherently multi-AZ | Cloud Run/Cloud Functions/Spanner are inherently multi-AZ | Azure Functions/Cosmos DB/AKS are inherently multi-AZ |
| **Multi-Region Active-Active** | DynamoDB Global Tables (multi-master, eventual consistency); Aurora Global Database (1 primary, 5 secondary) | Spanner (multi-region, strong consistency, 99.999% SLA); Firestore (multi-region, strong consistency) | Cosmos DB (multi-region writes, 0 RPO, 99.999% read availability); Azure SQL (active geo-replication) |
| **RTO/RPO** | RPO: 0s (DynamoDB Global Tables), RTO: <1min (automatic) | RPO: 0s (Spanner), RTO: <1min (automatic) | RPO: 0s (Cosmos DB multi-region writes), RTO: <1min (automatic) |
| **Chaos Engineering** | AWS Fault Injection Simulator (FIS) | Cloud Chaos Studio (via third-party tools) | Azure Chaos Studio (native fault injection) |
| **Zero-Downtime Deployment** | Lambda versions + aliases, API Gateway canary deployments, CodeDeploy | Cloud Run traffic splitting, GKE canary with Cloud Deploy, Workflows | Azure Functions deployment slots, AKS canary, Logic Apps versioning |

**Key Insight for Finance:** GCP Cloud Spanner is the only globally distributed database with strong consistency across all three providers, making it uniquely suitable for financial applications requiring ACID transactions across multiple regions (e.g., global payment systems, multi-currency trading platforms). AWS DynamoDB Global Tables provide multi-master writes with eventual consistency, which is suitable for many financial use cases but not for applications requiring strong consistency. Azure Cosmos DB offers multi-region writes with 0 RPO and 99.999% read availability, with configurable consistency levels (strong, bounded staleness, session, consistent prefix, eventual).

### 3.5 Performance & Scalability

| Aspect | AWS | GCP | Azure |
|---|---|---|---|
| **Serverless Compute** | Lambda: 1,000 concurrent executions (default, can increase to 10,000s); 15-minute timeout; 10GB memory | Cloud Run: 1,000 concurrent requests per container (default); 60-minute timeout; 16GB memory | Azure Functions: 1,000 concurrent executions (default); 10-minute timeout (default); 14GB memory |
| **NoSQL Database** | DynamoDB: 1M+ requests/second, sub-10ms latency at P99, autoscale | Firestore: 1M+ writes/second, sub-10ms latency, multi-region strong consistency | Cosmos DB: 1M+ requests/second, sub-10ms latency at P99, 5 consistency levels |
| **Relational Database** | Aurora Serverless v2: up to 256 ACUs, sub-ms latency, auto-scaling | Spanner: 2M+ reads/second, 200K+ writes/second, auto-scaling, global strong consistency | Azure SQL Hyperscale: 100TB, 100K IOPS, auto-scaling storage and compute |
| **Streaming Data** | Kinesis: 1MB/s per shard, 1,000 records/s per shard; MSK: unlimited throughput | Pub/Sub: 10M+ messages/second, exactly-once delivery; Dataflow: auto-scaling | Event Hubs: 1MB/s per partition, millions of events/second; Premium/Dedicated tier |
| **Global Network** | Global Accelerator: anycast IP, 90+ PoPs; CloudFront: 400+ PoPs | Premium Tier: 200+ PoPs, 40+ regions, private backbone with 40% lower latency | Azure Front Door: 100+ PoPs, global anycast; Azure CDN: 130+ PoPs |
| **AI/ML** | SageMaker: managed ML platform, built-in algorithms, distributed training | Vertex AI: unified ML platform, Model Garden, AutoML, 200+ custom models | Azure Machine Learning: managed ML platform, AutoML, responsible AI dashboard |

**Key Insight for Finance:** GCP Cloud Spanner with strong consistency and global distribution is uniquely suited for financial applications that require ACID transactions across multiple regions. AWS DynamoDB provides the highest throughput for NoSQL workloads (1M+ requests/second) with sub-10ms latency. Azure Cosmos DB offers the most flexibility with 5 consistency levels, allowing financial applications to choose the right trade-off between consistency and performance. For streaming financial data, GCP Pub/Sub with exactly-once delivery and Dataflow with auto-scaling provide the most robust event-driven architecture.

### 3.6 Security & Compliance

| Factor | AWS | GCP | Azure |
|---|---|---|---|
| **PCI-DSS Scope Reduction** | **Maximum** — Lambda, DynamoDB, API Gateway are fully managed; no servers to secure | **Maximum** — Cloud Run, Cloud Functions, Spanner, Firestore are fully managed | **Maximum** — Azure Functions, Cosmos DB, API Management are fully managed |
| **Serverless Security** | Lambda: VPC config, IAM roles, KMS encryption, CloudWatch logs, X-Ray tracing | Cloud Run: IAM, VPC ingress/egress, mTLS, Cloud Audit Logs, Secret Manager | Azure Functions: IAM, VNet integration, Key Vault, Application Insights, Defender for Cloud |
| **Database Security** | DynamoDB: encryption at rest (KMS), VPC endpoints, fine-grained access control, point-in-time recovery | Firestore: encryption at rest (CMEK), IAM, VPC Service Controls, audit logging | Cosmos DB: encryption at rest (CMEK), RBAC, firewall, VNet service endpoints, private endpoints |
| **Confidential Computing** | Nitro Enclaves (isolated compute for sensitive workloads) | Confidential VMs (AMD SEV-SNP, full VM memory encryption); Confidential Space (multi-party TEE) | Confidential VMs (AMD SEV-SNP, Intel TDX); Confidential Containers (AKS + Intel SGX) |
| **Governance & Compliance** | AWS Control Tower, Service Control Policies, CloudTrail, Config, GuardDuty, Security Hub | Organization Policies, IAM Conditions, Access Transparency, Access Approval, Security Command Center, Chronicle SIEM | Azure Blueprints, Azure Policy, Microsoft Defender for Cloud, Microsoft Sentinel, Purview Compliance Manager, Azure Policy as Code |
| **Data Residency** | SCPs, region restrictions, CloudFront geo-restriction | Assured Workloads (data residency, CMEK, Access Transparency, Access Approval) | Azure Policy (Allowed Locations), Azure Blueprints, Azure Sovereign Clouds |

**Key Insight for Finance:** All three providers offer maximum PCI-DSS scope reduction for re-architected workloads, as serverless services eliminate the need to manage OS, runtime, database platform, and patching. GCP's Confidential VMs with AMD SEV-SNP provide full VM memory encryption, which is critical for financial applications processing sensitive data in memory (trading algorithms, PII, IP). AWS Nitro Enclaves provide isolated compute environments but do not encrypt the full VM memory. Azure's Confidential Computing portfolio includes Confidential VMs, Confidential Containers, and Confidential Databases, providing the broadest range of confidential computing options for financial workloads.

### 3.7 Pros and Cons for Regulated Finance Environments

**AWS Re-architecture:**

| Pros | Cons |
|---|---|
| Most mature serverless ecosystem (Lambda, DynamoDB, API Gateway, Step Functions) | No global database with strong consistency (DynamoDB Global Tables are eventually consistent) |
| DynamoDB provides 1M+ requests/second with sub-10ms latency for high-throughput trading | No full VM memory encryption (Nitro Enclaves are isolated, not full VM) |
| Step Functions provides robust workflow orchestration for financial business processes | Lambda has 15-minute timeout limit (limited for long-running financial batch jobs) |
| AWS Well-Architected Framework provides structured guidance for re-architecture | API Gateway costs can be significant for high-volume financial APIs |
| Strong partner ecosystem for financial services (Accenture, Deloitte, Cognizant, Infosys, TCS) | Re-architecture requires significant investment in staff training (Lambda, DynamoDB, CDK) |

**GCP Re-architecture:**

| Pros | Cons |
|---|---|
| **Cloud Spanner** provides global strong consistency with 99.999% SLA—unique for core banking | Spanner pricing is higher than DynamoDB/Cosmos DB for smaller workloads |
| **Confidential VMs** with AMD SEV-SNP provide full VM memory encryption for sensitive financial data | Smaller serverless function ecosystem (Cloud Functions 2nd gen is newer than Lambda) |
| **Cloud Run** provides serverless containers with 60-minute timeout (vs. Lambda's 15 minutes) | Cloud Run has lower concurrent request limits (1,000 vs. Lambda's 10,000s) |
| **BigQuery** provides petabyte-scale analytics with built-in ML (BigQuery ML) for fraud detection | Smaller partner ecosystem for financial services re-architecture |
| **Assured Workloads** with Access Transparency and Access Approval for regulated financial data | GKE Autopilot is still maturing for complex financial workloads |

**Azure Re-architecture:**

| Pros | Cons |
|---|---|
| **Cosmos DB** provides multi-region writes with 0 RPO and 5 consistency levels | Cosmos DB pricing is complex (RU/s, storage, throughput, consistency level) |
| **Azure Chaos Studio** provides native fault injection for validating financial application resilience | Azure Functions has 10-minute default timeout (can be extended to 60 minutes with Premium plan) |
| **Azure API Management** provides comprehensive API gateway with OAuth2, mTLS, rate limiting | AKS management overhead for complex financial microservices |
| **Microsoft Defender for DevOps** scans IaC and containers for compliance violations pre-deployment | Smaller serverless container ecosystem (Azure Container Apps is newer than Cloud Run) |
| **Azure Policy as Code** enables compliance enforcement via CI/CD pipelines | Vendor lock-in risk with Cosmos DB (proprietary API, though supports MongoDB/Cassandra compatibility) |

---

## Section 4: Cross-Provider Comparison Tables

### 4.1 Lift-and-Shift: AWS vs. GCP vs. Azure

| Dimension | AWS | GCP | Azure |
|---|---|---|---|
| **Tooling Maturity** | ★★★★★ (MGN, DMS, Migration Hub, Migration Evaluator) | ★★★★☆ (Migration Center, StratoZone, Migrate to VMs, DMS) | ★★★★★ (Azure Migrate, ASR, DMS, Data Box) |
| **Migration Cost** | Low (MGN free, DMS pay-per-use) | Low (Migrate to VMs included in Migration Center) | Low (Azure Migrate free, ASR pay-per-use) |
| **Ongoing OpEx** | High (self-managed VMs) | High (self-managed VMs) | High (self-managed VMs) |
| **License Cost Savings** | Moderate (AWS License Manager, BYOL for Oracle) | Low (BYOL for Windows/SQL Server, CloudSimple for VMware) | **High** (Azure Hybrid Benefit: up to 55% SQL Server, 40% Windows Server) |
| **Downtime** | 5–30 minutes (MGN) | 1–4 hours (Migrate to VMs) | 15 minutes–4 hours (ASR) |
| **Live Migration** | No | **Yes** (GCP-exclusive) | No |
| **Compute Performance** | Graviton (40% better price-performance), Ultra Disk (160K IOPS) | Hyperdisk (3.2M IOPS, sub-ms latency), Jupiter network (1,000 Gbps) | M-series (5.7TB RAM), Azure NetApp Files (4.5 GB/s) |
| **PCI-DSS Scope** | Broadest (customer manages OS, DB, application) | Broadest (customer manages OS, DB, application) | Broadest (customer manages OS, DB, application) |
| **Data Residency** | Service Control Policies, region restrictions | Assured Workloads (data residency, CMEK, Access Transparency) | Azure Policy (Allowed Locations), Azure Sovereign Clouds |
| **Best for Finance** | Oracle-heavy workloads, fast data center exits, Graviton-compatible apps | VMware workloads, latency-sensitive trading, data residency-focused institutions | Microsoft-centric environments (SQL Server, Windows Server, SAP) |

### 4.2 Re-platforming: AWS vs. GCP vs. Azure

| Dimension | AWS | GCP | Azure |
|---|---|---|---|
| **Database Migration** | ★★★★★ (DMS + SCT, Aurora, RDS) | ★★★★★ (DMS + Datastream, AlloyDB, Spanner) | ★★★★★ (DMS, SQL MI, Azure SQL Hyperscale) |
| **Container Migration** | ★★★★☆ (ECS, EKS, App2Container) | ★★★★★ (Migrate to Containers, GKE Autopilot, Cloud Run) | ★★★★☆ (App Containerization, AKS, Azure Container Instances) |
| **Migration Cost** | Medium | Medium | Medium |
| **Ongoing OpEx** | Medium (managed DB, but still some manual management) | Medium (managed DB, GKE cluster management) | Medium (managed DB, App Service reduces web tier ops) |
| **3-Year TCO vs. Lift-and-Shift** | 60–75% | 60–75% | 60–75% |
| **Database Downtime** | Near-zero (DMS ongoing replication) | Near-zero (Datastream CDC) | Near-zero (DMS online mode) |
| **Multi-Region DR** | Aurora Global Database (RPO <1s, failover <1min) | Spanner (99.999% SLA, multi-region strong consistency) | Azure SQL failover groups (RPO 0s, automated failover) |
| **Database Performance** | Aurora: 5x MySQL, 3x PostgreSQL | AlloyDB: 4x PostgreSQL, 100x analytical queries | Azure SQL Hyperscale: 100TB, 100K IOPS |
| **PCI-DSS Scope Reduction** | Moderate (RDS/Aurora reduce OS/DB patching scope) | Moderate (Cloud SQL/AlloyDB reduce OS/DB scope) | High (Azure SQL reduces OS/SQL Server patching, Microsoft manages anti-malware) |
| **Best for Finance** | Oracle/SQL Server migrations to Aurora or RDS | PostgreSQL migrations to AlloyDB, global databases with Spanner | SQL Server migrations to Azure SQL, Microsoft-centric environments |

### 4.3 Re-architecture: AWS vs. GCP vs. Azure

| Dimension | AWS | GCP | Azure |
|---|---|---|---|
| **Serverless Compute** | ★★★★★ (Lambda, Fargate, Step Functions) | ★★★★★ (Cloud Run, Cloud Functions, Workflows) | ★★★★☆ (Azure Functions, AKS, Logic Apps) |
| **NoSQL Database** | ★★★★★ (DynamoDB: 1M+ requests/s, sub-10ms latency) | ★★★★☆ (Firestore: 1M+ writes/s, multi-region strong consistency) | ★★★★★ (Cosmos DB: multi-region writes, 0 RPO, 5 consistency levels) |
| **Relational Database** | ★★★★☆ (Aurora Serverless v2, up to 256 ACUs) | ★★★★★ (Spanner: global strong consistency, 99.999% SLA) | ★★★★☆ (Azure SQL Hyperscale: 100TB, auto-scaling) |
| **Event-Driven Architecture** | ★★★★★ (SQS, SNS, EventBridge, Kinesis, MSK) | ★★★★★ (Pub/Sub, Eventarc, Dataflow, Workflows) | ★★★★★ (Service Bus, Event Grid, Event Hubs, Logic Apps) |
| **Global Consistency** | Eventually consistent (DynamoDB Global Tables) | **Strongly consistent** (Spanner) | Configurable (Cosmos DB: 5 consistency levels) |
| **Confidential Computing** | ★★★★☆ (Nitro Enclaves, not full VM encryption) | ★★★★★ (Confidential VMs: AMD SEV-SNP, full memory encryption) | ★★★★★ (Confidential VMs, Confidential Containers, Confidential Databases) |
| **PCI-DSS Scope** | Minimum (fully managed serverless services) | Minimum (fully managed serverless services) | Minimum (fully managed serverless services) |
| **Migration Cost** | Highest | Highest | Highest |
| **Ongoing OpEx** | Lowest | Lowest | Lowest |
| **3-Year TCO vs. On-Premises** | 40–60% | 40–60% | 40–60% |
| **Best for Finance** | High-throughput trading, event-driven microservices, fraud detection | Global core banking, strong consistency requirements, confidential computing | Multi-region active-active, Microsoft-centric microservices, responsible AI |

---

## Section 5: Conclusion and Recommendations

### 5.1 Key Findings

1. **No single provider or approach is universally optimal for financial services.** The choice depends on workload characteristics, existing licensing, regulatory posture, timeline, and risk tolerance.

2. **Lift-and-Shift is the fastest path to cloud** but has the highest ongoing operational cost and broadest compliance scope. It is best suited for data center exits, merger-driven consolidation, and temporary colocation exit. GCP's Live Migration provides a unique advantage for financial workloads that cannot tolerate downtime during host maintenance.

3. **Re-platforming offers the best balance of cost savings, operational efficiency, and compliance scope reduction** for most financial workloads. All three providers offer strong capabilities for database and container migration. Azure's Hybrid Benefit provides the strongest cost advantage for Microsoft-centric environments. GCP's AlloyDB and Spanner provide unique performance and consistency advantages. AWS Aurora provides the best performance for MySQL/PostgreSQL workloads.

4. **Full Re-architecture delivers the greatest long-term benefits** (lowest operational cost, highest scalability, best resilience, minimum compliance scope) but requires the highest upfront investment. It is best suited for strategic modernization of core financial systems. GCP Cloud Spanner is uniquely suited for global core banking with strong consistency. AWS DynamoDB provides the highest throughput for NoSQL workloads. Azure Cosmos DB provides the most flexible consistency model.

5. **Security and compliance are table stakes for all three providers.** All maintain PCI-DSS v4.0 Level 1 certification, SOC 2 Type II reports, ISO 27001 certification, and support for data residency controls. The key differentiators are:
   - **GCP**: Assured Workloads with Access Transparency and Access Approval for auditing Google staff access; Confidential VMs with full memory encryption; Assured Workloads for Sovereign Controls.
   - **AWS**: Nitro Enclaves for isolated compute environments; AWS License Manager for Oracle BYOL compliance; AWS Control Tower for multi-account governance.
   - **Azure**: Azure Hybrid Benefit for license cost savings; Azure Dedicated HSM for payment HSM workloads; Azure Policy for granular compliance enforcement; Azure Sovereign Clouds for government and regulated industries.

### 5.2 Recommendations by Financial Workload Type

| Workload Type | Recommended Approach | Recommended Provider | Rationale |
|---|---|---|---|
| **Core Banking / Ledger Systems** | Re-architecture | GCP (Spanner) | Global strong consistency, 99.999% SLA, ACID transactions across regions |
| **Payment Processing** | Re-architecture | AWS (Lambda, DynamoDB, Step Functions) | Highest throughput, most mature serverless ecosystem, PCI-DSS compliant |
| **Trading Systems (latency-sensitive)** | Re-platforming or Lift-and-Shift | GCP (Hyperdisk, Live Migration, Jupiter network) | Sub-ms latency, zero-downtime host maintenance, 1,000 Gbps networking |
| **SQL Server / SAP Workloads** | Re-platforming | Azure (Azure SQL, Azure Hybrid Benefit) | Up to 80% cost savings with AHB + RIs, near-100% SQL Server compatibility |
| **Oracle Database Workloads** | Re-platforming | AWS (Aurora via DMS + SCT) or GCP (AlloyDB) | Strong migration tooling, PostgreSQL compatibility with enhanced performance |
| **Fraud Detection / ML** | Re-architecture | GCP (Vertex AI, BigQuery, Dataflow) or AWS (SageMaker, Kinesis) | Unified ML platform, real-time streaming analytics, petabyte-scale data processing |
| **Data Center Exit (Urgent)** | Lift-and-Shift | GCP (Live Migration, per-second billing) | Minimal downtime, no application changes, fastest time-to-cloud |
| **Multi-Region Active-Active** | Re-architecture | Azure (Cosmos DB) or GCP (Spanner) | Cosmos DB: 0 RPO multi-region writes, 5 consistency levels; Spanner: strong consistency |
| **Confidential / Regulated Data** | Re-architecture | GCP (Confidential VMs, Assured Workloads) | Full memory encryption, data residency enforcement, Access Transparency |
| **VMware-Heavy Environments** | Lift-and-Shift | GCP (CloudSimple) or AWS (VMware Cloud on AWS) | Native VMware SDDC, zero-modification migration, HCX support |

### 5.3 Strategic Considerations for Financial Institutions

1. **Start with a pilot migration using Lift-and-Shift** to establish cloud governance, security controls, and operational processes. Use this experience to build a cloud center of excellence (CoE) with regulatory compliance expertise.

2. **Prioritize re-platforming for the majority of financial workloads.** The 40-60% cost savings, operational efficiency gains, and compliance scope reduction make this the most attractive approach for most applications. Reserve re-architecture for strategic systems that will benefit from cloud-native capabilities.

3. **Invest in compliance automation early.** Use Azure Policy, AWS Control Tower, or GCP Assured Workloads to enforce data residency, encryption, and security controls from day one. This reduces the compliance burden during migration and ensures ongoing regulatory adherence.

4. **Plan for multi-cloud or hybrid strategies** where appropriate. Financial institutions may use different providers for different workloads (e.g., Azure for SQL Server, GCP for Spanner, AWS for serverless). Ensure that data residency, encryption, and security controls are consistent across providers.

5. **Engage cloud provider financial services teams and compliance programs.** AWS MAP, Azure Migration and Modernization Program, and GCP Migration Center provide funding, tools, and expertise for regulated migrations. Cloud provider financial services teams (AWS Financial Services, GCP Financial Services, Azure Financial Services) can provide regulatory guidance and compliance documentation.

6. **Conduct thorough dependency mapping and risk assessment** before migration. Financial applications have complex interdependencies (trading systems, payment rails, settlement systems) that must be mapped and migrated together. Use provider discovery tools (StratoZone, AWS Application Discovery Service, Azure Migrate) to build a complete dependency map.

7. **Implement continuous compliance monitoring** post-migration. Use AWS Security Hub, GCP Security Command Center, or Azure Microsoft Defender for Cloud to monitor for compliance drift, misconfigurations, and security threats. Integrate with existing SIEM (Splunk, Chronicle, Sentinel) for unified security operations.

---

## Sources

[1] AWS Application Migration Service (MGN) Documentation: https://docs.aws.amazon.com/mgn/latest/ug/what-is-application-migration-service.html

[2] AWS Database Migration Service (DMS) Documentation: https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html

[3] AWS Migration Hub Documentation: https://docs.aws.amazon.com/migrationhub/latest/ug/whatishub.html

[4] AWS Well-Architected Framework: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html

[5] AWS PCI-DSS Compliance: https://aws.amazon.com/compliance/pci-dss-level-1/

[6] AWS Control Tower Documentation: https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html

[7] AWS Migration Acceleration Program (MAP): https://aws.amazon.com/migration-acceleration-program/

[8] Google Cloud Migration Center Documentation: https://cloud.google.com/migration-center/docs

[9] Google Cloud StratoZone Documentation: https://cloud.google.com/stratozone/docs

[10] Google Cloud Migrate to Virtual Machines Documentation: https://cloud.google.com/migrate/compute-engine/docs

[11] Google Cloud Database Migration Service Documentation: https://cloud.google.com/database-migration/docs

[12] Google Cloud Assured Workloads Documentation: https://cloud.google.com/assured-workloads/docs

[13] Google Cloud Confidential Computing Documentation: https://cloud.google.com/confidential-computing

[14] Google Cloud PCI-DSS Compliance: https://cloud.google.com/security/compliance/pci-dss

[15] Google Cloud AlloyDB Documentation: https://cloud.google.com/alloydb/docs

[16] Google Cloud Spanner Documentation: https://cloud.google.com/spanner/docs

[17] Azure Migrate Documentation: https://docs.microsoft.com/en-us/azure/migrate/migrate-services-overview

[18] Azure Site Recovery Documentation: https://docs.microsoft.com/en-us/azure/site-recovery/site-recovery-overview

[19] Azure Database Migration Service Documentation: https://docs.microsoft.com/en-us/azure/dms/dms-overview

[20] Azure Hybrid Benefit Documentation: https://docs.microsoft.com/en-us/azure/azure-sql/azure-hybrid-benefit

[21] Azure PCI-DSS Compliance: https://docs.microsoft.com/en-us/azure/compliance/pci-dss-level-1

[22] Azure Policy Documentation: https://docs.microsoft.com/en-us/azure/governance/policy/overview

[23] Azure Blueprints Documentation: https://docs.microsoft.com/en-us/azure/governance/blueprints/overview

[24] Azure Confidential Computing Documentation: https://docs.microsoft.com/en-us/azure/confidential-computing/

[25] Azure Cosmos DB Documentation: https://docs.microsoft.com/en-us/azure/cosmos-db/introduction

[26] Azure SQL Database Hyperscale Documentation: https://docs.microsoft.com/en-us/azure/azure-sql/database/service-tier-hyperscale

[27] Microsoft Purview Compliance Manager: https://docs.microsoft.com/en-us/microsoft-365/compliance/compliance-manager

[28] Microsoft Service Trust Portal: https://servicetrust.microsoft.com/

[29] AWS Financial Services Competency Partners: https://aws.amazon.com/financial-services/partner-solutions/

[30] Google Cloud Financial Services Solutions: https://cloud.google.com/solutions/financial-services

[31] Azure Financial Services Compliance: https://azure.microsoft.com/en-us/industries/financial-services/

[32] PCI Security Standards Council: https://www.pcisecuritystandards.org/

[33] FINRA Cloud Guidance: https://www.finra.org/rules-guidance/guidance/cloud-computing

[34] FFIEC IT Examination Handbook: https://www.ffiec.gov/it-examination.htm

[35] GDPR Compliance Guidance: https://gdpr.eu/compliance/
