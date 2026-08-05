# Prometheus 高指标流失（High Metric Churn）的影响、系统解决方案与云厂商托管方案

## 1. 概述

Prometheus 的高指标流失（High Metric Churn）指的是**高基数**（High Cardinality，即大量唯一的标签组合）或**标签值快速变化**（如 Pod 重启、容器 ID 变更、请求路径动态变化）导致大量新时间序列被频繁创建和废弃的现象。这是 Prometheus 生产环境中**最常见、最具破坏性的性能问题**，直接导致内存溢出（OOM）、查询超时、存储成本飙升和系统不稳定。

本报告从三个维度进行全面分析：
1. 高指标流失对 Prometheus 的具体影响（内存、CPU、磁盘 I/O、查询性能、存储成本）
2. 系统性的解决方案（基数限制、聚合、重新标记、远程写入过滤、替代后端等）
3. 各大云厂商的托管方案及其高流失处理能力（AWS、Google Cloud、Azure 等）

---

## 2. 高指标流失的影响

### 2.1 内存影响

#### 2.1.1 Head Block 内存膨胀

Prometheus TSDB 将所有最近接收的时间序列保存在**Head Block**（内存中，默认约 2 小时窗口）。**高流失率的直接后果是 Head Block 中积累了大量已经不再活跃的时间序列，但它们仍然占用内存**。这与许多人的误解相反——非活跃序列并不会立即被清除，而是在整个 Head Block 窗口期内保留[1][2]。

**每序列内存消耗**：
- 每个活跃序列约消耗 **2-3 KB 的内存**[3]
- 更精确的估算：约 **3-4 KB 每序列**[4]
- 包含缓冲后约 **7.5 KB 每序列**[5]

**实际场景估算**：
- 100 万活跃序列 → 约 **4-6 GB RAM** 仅用于 Head Block[4]
- 500 万活跃序列 → 约 **15-20 GB RAM**[3]
- 1200 万序列（2 小时内，每秒创建 100 Pod，每 Pod 1000 指标）→ 即使当前 scrape 只有少量指标，内存仍会持续膨胀[2]

#### 2.1.2 内存映射块（mmap）的局限性

Prometheus v2.19.0 引入了 Head Block 完整块的内存映射，可将内存使用降低 **20-40%** [6]。然而，在高流失场景下，**每个序列往往无法填满一个完整的块（默认 120 样本）**，导致内存映射的收益大打折扣[6]。更严重的是，查询时 mmap 的块会被加载到内存，可能导致**即使分配了 60GB 内存仍然发生 OOM**[7]。

#### 2.1.3 索引内存

每个磁盘块（Block）都有一个索引读取器缓存标签、发布列表和符号表。高流失意味着更多唯一标签组合，**反向索引（Postings Index）的大小呈线性增长**，直接增加内存消耗[8]。

#### 2.1.4 真实案例

- **Coveo**：删除一个高基数 `id` 标签后，样本率下降 75%，Pod 内存从 **30GB+ 降至 8GB**（375% 改善）[9]。
- **Palark**：优化后指标从 1000 万降至 87.7 万，内存从 **64GB 降至 5GB 以下**（92% 减少）[10]。
- **Kubernetes OOM 案例**：一个 24GB 内存的 Pod 反复 OOM，增加到 48GB、64GB 仍无效，最终发现是 Oracle 数据库事务 ID 导致的高基数，删除后恢复[11]。

### 2.2 CPU 影响

- **序列创建开销大**：写入新序列比追加到已有序列昂贵得多。高流失意味着大量新序列创建，CPU 使用率显著上升[12]。
- **压缩开销**：压缩操作未被节流，导致每 2-3 小时出现**磁盘 I/O 和 CPU 峰值**，可能造成 `/metrics` 端点无响应和数据缺口[13]。
- **Gorilla 编码效率下降**：短命序列的 XOR 编码压缩效率低，进一步增加 CPU 负担[4]。
- **查询密集型**：宽范围聚合需要扫描大量序列和解码大量块，查询 CPU 消耗急剧上升[14]。

### 2.3 磁盘 I/O 影响

- **WAL 写入**：每个样本都先写入 Write-Ahead Log（WAL），每 10 秒刷新一次。高流失导致 WAL 写入量巨大[13]。
- **块刷新**：未填满的块频繁刷新到磁盘，产生大量小文件 I/O[6]。
- **压缩 I/O 峰值**：压缩操作会“冲刷”操作系统的页面缓存，降低后续查询性能[13]。
- **VictoriaMetrics 实验**：写入 10,000 个高流失指标时，产生 15 个目录和 53 个文件；稳定标签值仅产生 6 个目录和 8 个文件，数据大小分别为 764KB 和 56KB[15]。

### 2.4 查询性能影响

- **索引选择性崩溃**：高基数导致反向索引中的发布列表过长，查询时需要扫描大量序列 ID，然后循环查找相关块[16]。
- **更多块需要扫描**：长时间范围的查询需要扫描更多磁盘块，每个块的处理开销累积[16]。
- **块解码开销**：宽范围聚合需要加载并解码大量序列的块，**查询超时或返回错误“query processing would load too many samples into memory”** 是常见现象[14]。
- **最坏情况**：如果添加 `user_id` 标签，会有数十万个不同时间序列，每个只有 1 个数据点——这是**最坏场景**[17]。

### 2.5 存储成本

- Prometheus 平均仅存储 1-2 字节/样本，但**高流失导致 Gorilla 压缩效率下降**，实际存储量增加[18]。
- 压缩操作的内存需求过高：一个 365 天保留期的服务器，正常使用 ~20GB RSS，进行一次 2% 的压缩需要额外 6GB 内存；10% 的压缩可能直接导致 OOM[19]。
- 公式估算：`所需磁盘空间 = 保留时间(秒) × 每秒摄入样本数 × 字节/样本`，但高流失下索引和标签开销会显著增加实际用量[18]。

### 2.6 WAL 增长与崩溃恢复

- **WAL 重放极慢**：高流失后重启，WAL 重放需要大量内存和时间。每秒 100 万样本的恢复时间约 25 分钟，且内存密集[13]。
- **崩溃恢复失败**：崩溃时可能无法成功恢复——能处理正常负载的服务器，恢复时可能因内存不足而永远无法启动[13]。
- **WAL 目录填满**：内存上升时 WAL 目录快速膨胀[12]。

### 2.7 为何高流失是 Prometheus 不稳定性的首要原因

- “高基数 Prometheus 内存使用的第一大原因”[20]。
- “高基数是导致大多数用户离开 Prometheus 的失败点”[21]。
- “OOM 不一定意味着内存不足——可能是内存泄漏或高基数问题。盲目增加内存只是治标不治本”[11]。
- “短命时间序列成本高昂，即使只抓取一次，也会在内存中保留 1-3 小时”[22]。

---

## 3. 系统解决方案

### 3.1 基数限制与强制执行

#### 3.1.1 抓取级别限制

```yaml
scrape_configs:
  - job_name: 'my-app'
    # 每次抓取的最大样本数
    sample_limit: 5000
    # 每个指标的最大标签数
    label_limit: 30
    # 标签名最大长度
    label_name_length_limit: 200
    # 标签值最大长度
    label_value_length_limit: 200
```

`sample_limit` 是最后的安全网——如果目标超过限制，整个抓取被标记为失败，超出的数据会被丢弃[23]。

#### 3.1.2 序列数随时间变化限制（提案中）

Prometheus 目前只有每次抓取的样本数限制，但**无法限制工作负载随时间引入的新序列数**。GitHub issue #17109 提出了 `series_added_limit`（基于每次抓取）和 `series_added_over_time_limit`（基于滚动时间窗口）两种方案[24]。

#### 3.1.3 保留期限制

```bash
--storage.tsdb.retention.time=15d   # 默认 15 天
--storage.tsdb.retention.size=500GB # 最大磁盘空间
```

将保留期设为最小值（2 小时）可以强制数据快速循环，适合仅作为转发代理的场景[25]。

### 3.2 聚合与记录规则

记录规则是 **Prometheus 工具箱中最被低估的工具**[26]。它预计算频繁使用的 PromQL 查询，将结果存储为新的、低基数的时间序列。

```yaml
groups:
  - name: cardinality_reduction
    interval: 30s
    rules:
      # 聚合高基数标签（如 pod、instance、user_id）
      - record: job:http_requests_total:rate5m
        expr: |
          sum by (job, status, method) (
            rate(http_requests_total[5m])
          )
```

**工作原理**：原始 `http_requests_total` 可能包含 `pod`、`instance`、`user_id` 等标签，记录规则通过 `sum by` 聚合掉这些高基数标签，生成只有 3 个标签的新指标，大幅降低内存消耗[27]。

**局限性**：
- 记录规则**不降低摄入成本**，只降低查询成本[28]
- 新规则不会自动回填历史数据
- 规则数量膨胀会增加 TSDB 开销
- 记录规则与 Prometheus 共享 TSDB，无法独立扩展[28]

### 3.3 重新标记策略

**重新标记（Relabeling）是控制基数最有效的方法**，在抓取时、写入存储前执行。

#### 3.3.1 删除整个标签（`labeldrop`）

```yaml
metric_relabel_configs:
  # 删除高基数标签
  - action: labeldrop
    regex: 'container_id|pod_uid|uid|instance'
```

**注意**：如果有多个序列仅通过被删除的标签区分，删除后它们会冲突并合并（任意保留一个值）[29]。

#### 3.3.2 删除整个指标（`drop`）

```yaml
metric_relabel_configs:
  # 删除 debug 级别指标
  - source_labels: [__name__]
    regex: 'debug_.*'
    action: drop
  # 仅保留特定的 histogram bucket
  - source_labels: [__name__, le]
    regex: 'http_request_duration_seconds_bucket;(0\.005|0\.01|0\.05|0\.1|0\.5|1)'
    action: keep
```

#### 3.3.3 白名单方法（`labelkeep`）

```yaml
metric_relabel_configs:
  # 只保留以下标签
  - action: labelkeep
    regex: '__name__|job|namespace|pod|status|method'
```

#### 3.3.4 规范化动态标签值

```yaml
metric_relabel_configs:
  # 将 /api/users/12345 映射为 /api/users/:id
  - source_labels: [path]
    regex: '/api/users/[0-9]+'
    replacement: '/api/users/:id'
    target_label: path
    action: replace
  # 将状态码归为类别
  - source_labels: [status_code]
    regex: '2[0-9][0-9]'
    replacement: '2xx'
    target_label: status_class
    action: replace
```

**实际效果**：Coveo 通过删除一个 `id` 标签，内存从 30GB+ 降至 8GB[9]。Palark 通过优化将指标从 1000 万降至 87.7 万，内存从 64GB 降至 5GB[10]。

### 3.4 远程写入过滤

`write_relabel_configs` 在抓取后、远程写入前应用，**数据被丢弃后永远不会离开实例**，这是控制网络带宽和远程存储成本最有效的方法[30]。

```yaml
remote_write:
  - url: "https://mimir.example.com/api/v1/push"
    write_relabel_configs:
      # 丢弃不需要的指标
      - source_labels: [__name__]
        regex: 'go_gc_.*|debug_.*'
        action: drop
      # 仅保留特定 job 的指标
      - source_labels: [job]
        regex: 'kubernetes-nodes|kube-state-metrics'
        action: keep
      # 删除高基数标签
      - action: labeldrop
        regex: 'container_id|uid|pod_uid'
```

**选择性路由**：可以将高优先级指标发送到高性能端点，其他指标发送到廉价端点[31]。

### 3.5 Prometheus Agent 模式

Agent 模式（从 v2.32.0 开始实验性，后续版本稳定）优化了 Prometheus 二进制程序，专门用于抓取和远程写入，禁用查询、告警和本地存储，仅保留自定义的 WAL[32]。

```bash
prometheus --enable-feature=agent --config.file=prometheus.yml
```

**资源节省（基准测试，5000 主机，1% 流失率，12 小时运行）**：

| 指标 | Prometheus Agent | Grafana Agent | vmagent |
|------|-----------------|---------------|---------|
| 最大内存 | 19 GB | 25.3 GB | **2.2 GB** |
| 平均 CPU | 3.69 核 | 4.16 核 | **2.69 核** |
| 网络使用 | 15.2 MB/s | 17.3 MB/s | **4.78 MB/s** |
| 磁盘 I/O | 7.61 MB/s | 4.38 MB/s | **0 MB/s** |

**Kubernetes Operator 支持**：Prometheus Operator v0.64.0+ 提供了 `PrometheusAgent` CRD（v1alpha1），简化了配置[33]。

### 3.6 使用替代后端

当 Prometheus 实例承受高流失压力时，需要立即可靠的缓解措施，然后才能实施架构变更。

#### 3.6.1 VictoriaMetrics

**VictoriaMetrics 是处理高流失的最佳选择之一**，专为高基数和流失设计，内存和磁盘使用量远低于 Prometheus。

- 单节点可处理 **1 亿+ 活跃序列**[34]
- 内存使用：**每百万活跃序列约 1 GB**，而 Prometheus 需要 3-7 GB[35]
- 5G 电信测试：Prometheus 内存波动 17-20 GB 且指数增长，VictoriaMetrics 仅用 **1 GB**[36]
- 磁盘使用：约 **10 倍压缩**，平均 1 字节/数据点[37]
- **vmagent**：Prometheus Agent 的替代品，内存使用减少 4 倍，网络带宽减少 4 倍[34]

**部署方式**：
```yaml
remote_write:
  - url: "http://victoria-metrics:8428/api/v1/write"
```

#### 3.6.2 Thanos

Thanos 通过 Sidecar 模式扩展 Prometheus，提供全局查询和长期存储，**最小化对现有部署的干扰**。

- 数据存储在对象存储（S3、GCS）中，Prometheus 本地保留期可设为最短 2 小时
- 支持压缩、降采样和高效查询历史数据[38]
- **适合已有 Prometheus 部署、需要全局视图的场景**[39]

#### 3.6.3 Grafana Mimir

Mimir 是 Cortex 的继任者，专为**大规模多租户部署**设计。

- 处理 **10 亿+ 活跃序列**（1,500 个副本，~7,000 CPU 核，30 TiB RAM）[40]
- 运行时配置支持动态更新，无需重启组件
- 原生多租户、摄入去重、自适应限制
- 查询分片实现**高基数 CPU 密集型查询的 10 倍执行时间减少**[40]
- **适合新建中央可扩展指标平台的场景**[39]

#### 3.6.4 后端对比

| 后端 | 最大序列数 | 流失处理能力 | 运维复杂度 | 存储效率 |
|------|-----------|-------------|-----------|---------|
| Prometheus（原生） | 2-500 万/实例 | 差 | 低 | 1-2 字节/样本 |
| VictoriaMetrics | 1 亿+（单节点）/ 数十亿（集群） | **优秀** | 低-中 | ~1 字节/样本 |
| Thanos | 数十亿（通过对象存储） | 良好 | 中-高 | 1-2 字节/样本 |
| Grafana Mimir | 数十亿（多租户） | **优秀** | 高 | ~1-2 字节/样本 |
| ClickHouse | 无限（查询时定义） | **优秀** | 高 | 高度可压缩 |

**扩展路径建议**：
- 低于 100 万序列 → 单 Prometheus 优化
- 100-500 万 → 分片或 VictoriaMetrics 单节点
- 超过 500 万 → 分布式架构（Thanos 增量迁移、Mimir 多租户治理、VictoriaMetrics 集群）[39]

### 3.7 服务端率限制

使用 Mimir/Cortex 时，可以配置摄入率限制：

```yaml
# Mimir 运行时配置
overrides:
  my-team:
    max_global_series_per_user: 500000
    max_global_series_per_metric: 50000
    max_samples_per_second: 10000
    ingestion_rate: 10000
    ingestion_burst_size: 20000
```

### 3.8 分层架构（Federation）

对于多集群场景，可以使用**两层 Prometheus 架构**：
- **收集层**：短保留期（2 小时），抓取高基数指标，应用记录规则聚合掉 `pod_name` 等高基数标签
- **主控层**：长保留期，通过 federation 抓取预聚合指标

一个实际案例：Istio 的 telemetry v2 为每个指标添加 `pod_name` 标签，通过两层架构将指标从 337,635 降至 **10,143**（减少 97%）[41]。

---

## 4. 云厂商托管方案

### 4.1 Amazon Managed Service for Prometheus (AMP)

#### 架构与后端
AMP 基于 **Cortex** 构建，AWS 与 Grafana Labs 合作进行了大规模优化：修复了 O(n²) S3 上传问题、Ingester 内存泄漏、Store Gateway 响应慢等问题，实现了 Shuffle Sharding 以增强租户隔离[42][43]。

#### 扩展能力
- **默认活跃序列限制**：5000 万/工作区（2025 年 7 月提升）[44]
- **最大支持**：**15 亿活跃序列/工作区**（需申请），以及 20 万条记录/告警规则（2026 年 7 月宣布）[45]
- 自动扩展摄入和存储

#### 高流失处理能力
- **基于标签的活跃序列限制**：2025 年 9 月发布，允许为不同标签集设置配额，防止噪声邻居影响整个工作区[46]
- 4 个新的 CloudWatch 指标：`ActiveSeriesPerLabelSet`、`ActiveSeriesLimitPerLabelSet`、`IngestionRatePerLabelSet`、`DiscardedSamplesPerLabelSet`[46][47]
- 支持记录规则和重新标记来控制基数[48]
- **推荐实践**：增加抓取间隔（如从 30s 到 60s 可减半成本）、使用重新标记过滤指标、使用原生 AMP 告警[49]

#### 定价
- **摄入**：分层定价，$0.90/千万样本（前 20 亿），之后更低
- **存储**：$0.03/GB/月
- **查询**：$0.10/十亿处理样本
- **200k 样本/秒工作负载**：约 **$13,323/月**；降低到 1 分钟分辨率约 **$1,600/月**[50]
- **100 万样本/秒**：约 **$47,000/月**[50]

#### 限制
- 仅指标，无日志/追踪
- 跨区域出口费 $0.09/GB
- 保留期默认 150 天（最长 1095 天，数据粒度随年龄变化：<15 天 1 分钟，15-63 天 5 分钟，>63 天 1 小时）[51]
- 自托管 Prometheus 在重度指标摄入场景下成本远低于 AMP（130 万指标/15 秒：自托管 $500/月 vs AMP $45k/月）[52]

### 4.2 Google Cloud Managed Service for Prometheus (GMP)

#### 架构与后端
GMP 基于 **Monarch**——Google 全球分布式内存时间序列数据库，服务于 Google 内部所有应用监控。**Monarch 不是 Cortex/Thanos/Mimir 的衍生品，而是 Google 自研的后端**[53][54]。

- 收集 **2 万亿+ 活跃时间序列**，存储 **65 千万亿数据点**[53]
- 服务全球查询，每秒处理数百万查询
- 存储近一 PB 压缩时间序列在内存中[54]

#### 扩展能力
- **无活跃序列数限制**[55]
- 服务可以支持任何业务产生的指标量[53]

#### 高流失处理能力
- **按样本定价**，无前期基数费用[55]
- 可定制的采样周期和过滤器用于成本控制[55]
- 基于标签的成本控制
- 动态多项目监控（Metrics Scopes）[56]
- 本地直方图存储（Monarch 原生支持，无需查询时从计数器构建）[57]

#### 数据保留
- **24 个月（2 年）** 免费保留[55]
- 客户案例：集群存储从 1TB 降至 50GB，保留期从 7 天延长至 2 年[58]

#### 定价
- **$0.060/百万样本**（前 500 亿），之后分层折扣
- **200k 样本/秒工作负载**：约 **$75,072/月**（仅摄入，含稀疏指标折扣约 $45,000/月）[50]
- **100 万样本/秒**：约 **$327,000/月**[50]
- 被评价为“成本天文数字”，某些情况下比第三方方案贵 30 倍[59]

#### 限制
- 工具碎片化，需要手动数据过滤[60]
- Grafana 不支持 OAuth2 认证，需要使用 Prometheus UI 作为代理[61]
- 缺乏基数控制、流式聚合、多租户和 SLA[59]
- 某些操作大小写不敏感（与开源 Prometheus 不同）[62]

### 4.3 Azure Monitor Managed Service for Prometheus

#### 架构与后端
Azure 的托管 Prometheus 服务基于 **Microsoft 自研基础设施**，是 Azure Monitor Metrics 的一部分，数据存储在 Azure Monitor 工作区中[63]。

#### 扩展能力
- **默认处理 100 万活跃序列**，可申请扩展至 **2500 万+**[64]
- 默认摄入限制：100 万事件/分钟/工作区[65]
- 自动扩展和高可用性，数据复制到配对区域[64]

#### 高流失处理能力
- 最小抓取间隔：1 秒[62]
- 记录规则和告警规则通过规则组管理（最多 20 条/组，500 组/工作区）[63][64]
- 通过 ConfigMap 进行指标过滤和成本控制[66]
- **大小写不敏感系统**：与开源 Prometheus 不同，仅大小写不同的时间序列被视为相同[62]
- 重复时间序列会导致 422 错误[62]
- 标签名 ≤511 字符，标签值 ≤1023 字符，≤63 标签/时间序列[62]

#### 数据保留
- **18 个月**免费保留[64]

#### 定价
- 预览期：$0.16/千万样本摄入
- 查询：$0.10/十亿样本处理
- 无需存储费（保留期内）[63][64]

#### 限制
- Sidecar 容器最多处理 150,000 个唯一时间序列[65]
- 节点更新期间可能出现 1-2 分钟数据缺口[62]
- Windows 节点未自动启用指标收集[62]
- 内容长度限制曾为 1 MB（已修复）[67]

### 4.4 其他云厂商

#### Alibaba Cloud
提供 **Managed Service for Prometheus**，特点包括：
- 数据收集性能比开源 Prometheus 高 **20 倍**
- 运维成本降低 **90%**
- 每副本 600 万数据点（vs 自托管 100 万）
- 查询 6 亿数据点仅需 8-10 秒（vs 自托管 180 秒）[68]

#### DigitalOcean、Oracle Cloud、IBM Cloud
**不提供原生托管 Prometheus 服务**，但可以通过社区方案或第三方集成实现：
- DigitalOcean：提供 1-Click App 自安装，或通过 Managed Databases 的 Prometheus 端点消费指标[69][70]
- Oracle Cloud：社区项目 `oci-prometheus-sd-proxy` 实现 OCI 服务发现，需通过 Management Agent 收集[71]
- IBM Cloud：Monitoring 服务（基于 Sysdig）支持 Prometheus 远程写入，提供预定义指标和仪表盘[72]

#### 第三方托管服务
- **Grafana Cloud**：基于 Mimir，SaaS 形式，按活跃序列计费，95 百分位突发保护[73]
- **VictoriaMetrics Cloud**：200k 样本/秒约 **$328.50/月**（比 AWS 便宜 40 倍，比 GCP 便宜 228 倍）[50]
- **Logz.io**：统一指标、日志和追踪，提供 Data Optimization Hub 过滤噪声指标[74]
- **Sysdig**：完全托管，自动服务发现，支持 PromQL[75]

### 4.5 云厂商方案对比

| 特性 | AWS AMP | GCP GMP | Azure Managed Prometheus |
|------|---------|---------|--------------------------|
| **后端** | Cortex | Monarch（Google 自研） | Microsoft 自研 |
| **最大活跃序列** | 15 亿/工作区（需申请） | 无限制（2 万亿+） | 2500 万+（需申请） |
| **数据保留** | 150 天（最长 1095 天） | 24 个月 | 18 个月 |
| **定价模型** | 按样本摄入、存储、查询 | 按样本摄入（分层） | 按样本摄入、查询 |
| **200k 样本/秒成本** | ~$13,323/月 | ~$75,072/月 | ~$0.16/千万样本 |
| **基数控制** | 标签级限制、记录规则、重新标记 | 按样本定价、采样周期、过滤器 | 记录规则、ConfigMap 过滤 |
| **多云支持** | 是（远程写入任意环境） | 是（多云、跨项目） | AKS 和 Azure Arc 集群 |
| **Grafana 集成** | Amazon Managed Grafana + 插件 | 通过 Prometheus UI 代理 | Azure Managed Grafana + 专用插件 |

---

## 5. 诊断与监控

### 5.1 关键指标

| 指标 | 含义 | 来源 |
|------|------|------|
| `prometheus_tsdb_head_series` | 当前 Head Block 中的活跃序列数 | [1][6][9] |
| `rate(prometheus_tsdb_head_series_created_total[15m])` | 序列创建速率（流失率） | [1] |
| `prometheus_tsdb_head_stale_series` | Head Block 中废弃序列数（v3.6.0+） | [76] |
| `scrape_series_added` | 每次抓取新增的序列数 | [9] |
| `process_resident_memory_bytes` | Prometheus 进程内存使用 | [77] |
| `prometheus_tsdb_compactions_total` | 压缩活动 | [78] |

### 5.2 诊断 PromQL

```promql
// 总序列数
prometheus_tsdb_head_series

// 按指标名统计序列数（Top 10）
topk(10, count by (__name__)({__name__=~".+"}))

// 按 job 统计基数
topk(10, count by (job)({job=~".+"}))

// 废弃序列比例（v3.6.0+）
prometheus_tsdb_head_stale_series{} / prometheus_tsdb_head_series{}
```

### 5.3 阈值

- **高基数起点**：**几百万时间序列**[79]
- **安全范围**：16GB RAM 约 **200-300 万序列**[4]
- **每序列内存**：约 **2-3 KB**[3]
- **废弃序列比例**：<0.3 忽略，0.3-0.5 密切关注，>0.5 需要干预[76]
- **标签设计原则**：如果标签可能有 **10,000+ 唯一值**，属于追踪 span 而非指标标签[17]

### 5.4 工具

- **TSDB Status API**：`/api/v1/status/tsdb?limit=50`[9]
- **promtool**：`./tsdb analyze`[10]
- **mimirtool**：查找未使用的指标[80]

---

## 6. 最佳实践总结

1. **预防胜于治疗**：在添加标签前问自己——这个标签是否可能有超过 10,000 个唯一值？如果是，应该放在追踪中而非指标中[17]。

2. **分层防御**：
   - 第一层：**重新标记**在抓取时删除高基数标签
   - 第二层：**记录规则**预聚合降低维度
   - 第三层：**基数限制**（`sample_limit`、`label_limit`）
   - 第四层：**远程写入过滤**控制离站数据
   - 第五层：**替代后端**（VictoriaMetrics、Mimir）处理高流失

3. **监控与告警**：持续监控 `prometheus_tsdb_head_series` 和 `scrape_series_added`，设置合理的告警阈值。

4. **容量规划**：估算公式 `内存 = (活跃序列 × 3 KB) + (摄入速率 × 2 小时 × 样本大小)`[3]。

5. **选择正确的后端**：根据规模选择——小规模用 Prometheus 优化，中等规模用 VictoriaMetrics 单节点，大规模用 Mimir 或 VictoriaMetrics 集群。

6. **成本优化**：增加抓取间隔、过滤无用指标、使用原生告警系统、利用分层定价和折扣。

---

## 7. 结论

高指标流失是 Prometheus 生产环境中最具破坏性的问题，直接导致内存溢出、查询超时、存储成本飙升和系统不稳定。其根本原因在于 Prometheus 的**内存优先架构**——所有活跃序列必须完全适配内存，无法溢出到磁盘。

解决方案呈现**分层防御**的特征：从最基础的重新标记和基数限制，到记录规则聚合，再到远程写入过滤和替代后端。没有银弹，最佳实践是组合使用多种方法。

在云厂商选择上，**AWS AMP** 提供最灵活的标签级基数控制和大规模扩展能力（15 亿序列），**GCP GMP** 基于 Monarch 实现无限扩展但成本较高，**Azure 方案**更适合 AKS 原生场景。对于成本敏感或需要极致性能的场景，**VictoriaMetrics Cloud** 和 **Grafana Cloud** 提供了显著的性价比优势。

最终，**预防成本远低于修复成本**——在指标设计阶段就遵循基数原则，比在崩溃后排查要有效得多。

---

### 来源

[1] Prometheus 高基数炸弹：https://openobserve.ai/blog/prometheus-data-cardinality

[2] Prometheus 用户组关于高流失率性能影响的讨论：https://groups.google.com/g/prometheus-users/c/wRtG7zq6sZ4

[3] Prometheus 高内存使用与 OOM 修复：https://devopskit.in/blog/prometheus-high-memory-oom-fix

[4] 高基数指标：Prometheus 与 ClickHouse 的扩展性对比：https://last9.io/blog/high-cardinality-metrics-prometheus-clickhouse

[5] Prometheus 内存使用指南：https://www.groundcover.com/learn/observability/prometheus-memory-usage

[6] Prometheus v2.19.0 内存映射块减少 40% 内存：https://grafana.com/blog/new-in-prometheus-v2-19-0-memory-mapping-of-full-chunks-of-the-head-block-reduces-memory-usage-by-as-much-as-40

[7] GreptimeDB 与 Prometheus 在高基数下的对比：https://clickhouse.com/blog/clickhouse-vs-promethous-high-cardinality-p1-understanding-the-problem

[8] Prometheus TSDB 笔记：http://flaneur2020.github.io/posts/2020-07-18-prometheus-tsdb

[9] Coveo 高内存消耗调查：https://source.coveo.com/2021/03/03/prometheus-memory

[10] Palark 资源消耗优化：https://palark.com/blog/prometheus-resource-consumption-optimization

[11] 为什么 Prometheus 不适合高基数数据：https://devops.stackexchange.com/questions/8189/why-is-prometheus-not-a-good-choice-for-data-with-high-cardinality

[12] ClickHouse 与 Prometheus 高基数问题理解：https://clickhouse.com/blog/clickhouse-vs-promethous-high-cardinality-p1-understanding-the-problem

[13] Prometheus 常见问题排查：https://last9.io/blog/troubleshooting-common-prometheus-pitfalls-cardinality-resource-utilization-and-storage-challenges

[14] Prometheus 高基数问题介绍：https://victorpierre.dev/learning/metrics/prometheus/high_cardinality

[15] VictoriaMetrics 流失率与高基数：https://itnext.io/victoriametrics-churn-rate-high-cardinality-metrics-an-indexdb-004137029164

[16] Prometheus 数据索引与查询性能：https://www.youtube.com/watch?v=hSpBpVvgRxk

[17] 为什么 Prometheus 不适合高基数数据（Stack Exchange）：https://devops.stackexchange.com/questions/8189/why-is-prometheus-not-a-good-choice-for-data-with-high-cardinality

[18] Prometheus 存储：技术术语通俗解释：https://valyala.medium.com/prometheus-storage-technical-terms-for-humans-4ab4de6c3d48

[19] Prometheus TSDB 压缩与保留：https://ganeshvernekar.com/blog/prometheus-tsdb-compaction-and-retention

[20] Prometheus 高基数问题（Victor Pierre）：https://victorpierre.dev/learning/metrics/prometheus/high_cardinality

[21] Prometheus 扩展性指南（2026）：https://alexandre-vazquez.com/prometheus-scalability

[22] Cloudflare 保护 Prometheus 的三层机制：https://news.ycombinator.com/item?id=25432729

[23] Prometheus 抓取配置文档：https://prometheus.io/docs/prometheus/latest/configuration/configuration/#scrape_config

[24] GitHub Issue #17109：https://github.com/prometheus/prometheus/issues/17109

[25] Prometheus 存储文档：https://prometheus.io/docs/prometheus/latest/storage/

[26] 记录规则最佳实践：https://prometheus.io/docs/practices/rules/

[27] Prometheus 记录规则指南：https://last9.io/blog/prometheus-recording-rules/

[28] Prometheus 记录规则的局限性：https://last9.io/blog/prometheus-recording-rules-limitations/

[29] Prometheus 重新标记配置：https://prometheus.io/docs/prometheus/latest/configuration/configuration/#relabel_config

[30] Prometheus 远程写入文档：https://prometheus.io/docs/prometheus/latest/storage/#remote-storage-integrations

[31] 远程写入调优指南：https://prometheus.io/docs/practices/remote_write/

[32] Prometheus Agent 模式：https://prometheus.io/docs/prometheus/latest/feature_flags/#agent

[33] Prometheus Agent CRD：https://prometheus-operator.dev/docs/user-guides/agent/

[34] VictoriaMetrics 文档：https://docs.victoriametrics.com/

[35] VictoriaMetrics 与 Prometheus 性能对比：https://victoriametrics.com/blog/victoriametrics-vs-prometheus/

[36] 5G 电信场景 Prometheus vs VictoriaMetrics：https://itnext.io/victoriametrics-churn-rate-high-cardinality-metrics-an-indexdb-004137029164

[37] VictoriaMetrics 压缩性能：https://victoriametrics.com/blog/victoriametrics-compression/

[38] Thanos 文档：https://thanos.io/

[39] 扩展路径建议：https://alexandre-vazquez.com/prometheus-scalability

[40] Mimir 扩展到 10 亿活跃序列：https://grafana.com/blog/how-we-scaled-our-new-prometheus-tsdb-grafana-mimir-to-1-billion-active-series

[41] 分层 Prometheus 减少基数：https://alexandre-vazquez.com/prometheus-scalability

[42] AWS AMP 与 Cortex：https://aws.amazon.com/prometheus/

[43] AWS 与 Grafana Labs 合作优化 Cortex：https://last9.io/blog/aws-prometheus-production-patterns

[44] AWS AMP 活跃序列限制提升至 5000 万：https://aws.amazon.com/about-aws/whats-new/2025/07/amazon-managed-service-prometheus-50M-default-activeserieslimit

[45] AWS AMP 支持 15 亿活跃序列：https://aws.amazon.com/about-aws/whats-new/2026/07/amazon-managed-service-prometheus-1500m-metrics-workspace

[46] AWS AMP 标签级限制：https://aws.amazon.com/blogs/mt/optimizing-metrics-ingestion-with-amazon-managed-service-for-prometheus

[47] AWS AMP 优化指标摄入：https://aws-news.com/article/2025-09-18-optimizing-metrics-ingestion-with-amazon-managed-service-for-prometheus

[48] AWS AMP 最佳实践：https://last9.io/blog/aws-prometheus-production-patterns

[49] AWS AMP 成本优化：https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-costs.html

[50] 托管 Prometheus 定价对比：https://victoriametrics.com/blog/managed-prometheus-pricing

[51] AWS AMP 数据保留：https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-workspace-data-retention.html

[52] 自托管 vs AMP 成本对比：https://news.ycombinator.com/item?id=25432729

[53] Google Cloud Managed Service for Prometheus 介绍：https://cloud.google.com/blog/products/operations/introducing-google-cloud-managed-service-for-prometheus

[54] Monarch 数据库论文：https://research.google/pubs/monarch/

[55] Google Cloud Managed Service for Prometheus 文档：https://cloud.google.com/managed-prometheus

[56] GMP 多项目监控：https://cloud.google.com/stackdriver/docs/managed-prometheus

[57] GMP 与 GKE 集成：https://metoro.io/blog/gke-monitoring

[58] GMP 客户案例：https://cloud.google.com/blog/products/operations/introducing-google-cloud-managed-service-for-prometheus

[59] GMP 成本问题：https://medium.com/google-cloud/google-managed-prometheus-with-opentelemetry-1a1fd1f0ae8a

[60] GMP 工具碎片化：https://engineering.sada.com/a-centralized-model-for-google-managed-prometheus-metrics-collection-4bb8a512ee52

[61] GMP Grafana 集成：https://cloud.google.com/stackdriver/docs/managed-prometheus

[62] Azure Monitor Managed Service for Prometheus 文档：https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview

[63] Azure 托管 Prometheus 介绍：https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-overview

[64] Azure 托管 Prometheus 扩展能力：https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-scaling

[65] Azure 托管 Prometheus 限制：https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-limits

[66] Azure 托管 Prometheus ConfigMap 配置：https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-configuration

[67] Azure 托管 Prometheus 常见问题：https://learn.microsoft.com/en-us/azure/azure-monitor/essentials/prometheus-metrics-faq

[68] Alibaba Cloud Managed Service for Prometheus：https://www.alibabacloud.com/product/prometheus

[69] DigitalOcean Prometheus 1-Click App：https://marketplace.digitalocean.com/apps/prometheus

[70] DigitalOcean Managed Databases Prometheus 端点：https://docs.digitalocean.com/products/databases/how-to/monitor-prometheus/

[71] OCI Prometheus 服务发现代理：https://github.com/oracle/oci-prometheus-sd-proxy

[72] IBM Cloud Monitoring 文档：https://cloud.ibm.com/docs/monitoring

[73] Grafana Cloud 定价：https://grafana.com/pricing/

[74] Logz.io 托管 Prometheus：https://logz.io/blog/comparing-prometheus-managed-services

[75] Sysdig 托管 Prometheus：https://sysdig.com/products/monitoring/

[76] SRECon 2026：高频率部署与废弃序列压缩：https://www.usenix.org/conference/srecon24americas/presentation/vernekar

[77] Prometheus 指标文档：https://prometheus.io/docs/concepts/metrics/

[78] Prometheus TSDB 压缩与保留：https://ganeshvernekar.com/blog/prometheus-tsdb-compaction-and-retention

[79] Prometheus 存储术语：https://valyala.medium.com/prometheus-storage-technical-terms-for-humans-4ab4de6c3d48

[80] mimirtool 文档：https://grafana.com/docs/mimir/latest/manage/tools/mimirtool/
