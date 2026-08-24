# Top 5 Architectural Strategies for Real-Time, Horizontally Scalable Chat Applications

## Introduction

Building a chat application for millions of concurrent users — the class of system exemplified by Slack — means engineering for extraordinary scale. Slack serves over five million simultaneous WebSocket sessions, processes more than 25 billion messages per day, and delivers messages worldwide with a p99 latency under 500 ms [1]. Discord scaled an Elixir/BEAM backend to five million concurrent users and now stores trillions of messages [2]. Twitter's timeline systems absorb roughly 300,000 read requests per second against only ~6,000 writes per second [3]. Any architecture that claims to support this scale must answer four questions simultaneously:

1. **Cloud-native vs. platform-agnostic deployment** — managed services or self-run infrastructure, and what each choice costs in operations, lock-in, and portability.
2. **Consistency model** — where strong consistency is non-negotiable (message ordering, read receipts) and where eventual consistency is acceptable (presence, typing indicators).
3. **Scalability mechanisms** — partitioning, sharding, message fan-out strategy, and storage optimization.
4. **Fault tolerance & latency** — surviving node, partition, and region failures while preserving real-time delivery.

This report analyzes the five architectural strategies that dominate the 2026 state of the art, grounded in the production systems at Slack, Discord, Twitter/X, and Uber, alongside official documentation for Kafka, Redis, Cassandra/ScyllaDB, DynamoDB, and the major cloud WebSocket services. For each strategy, the four dimensions are evaluated and exactly three pros and three cons are given.

---

## Strategy 1: The Fully Managed Cloud-Native Stack

### Overview

The fully managed strategy delegates nearly every hard distributed-systems problem to a cloud provider. The canonical AWS reference implementation pairs **Amazon API Gateway WebSockets** (managed connection handling) with **AWS Lambda** (serverless compute for connect/send/disconnect routes), **Amazon DynamoDB** (connection registry and message history), **Amazon MSK or Kinesis** (message streaming), **ElastiCache for Redis** (presence and pub/sub), and **S3** (archival) [4]. The equivalent stacks are **Azure Web PubSub + Azure Functions + Cosmos DB + Azure Cache for Redis** and **GCP Cloud Run (WebSockets) + Memorystore for Redis + Cloud Pub/Sub + Firestore**.

In the AWS reference pattern, the `$connect` route stores the connection ID in DynamoDB, the `sendmessage` Lambda function collects recipient connection IDs from DynamoDB and pushes to each via the API Gateway Management API, and `$disconnect` removes the connection record [4]. Because the gateway owns the connection, "you do not need to maintain the connection in the Lambda function. The connection is handled by API Gateway" [76]. This pattern is also used to offload WebSocket connection state from Kubernetes pods entirely, making backend services stateless and freely autoscalable [28].

### Cloud-Native vs. Platform-Agnostic Deployment

**Operational burden is near zero by design.** API Gateway invokes Lambda only on connect/disconnect/message events — not during idle periods — and DynamoDB is recommended as the connection store "due to scalability, low latency, serverless nature, and pay-per-request pricing" [77]. Azure Web PubSub is "a fully-managed service that allows developers to focus on building real-time web experiences without worrying about capacity provisioning, reliable connections, scaling, encryption or authentication" [6]. MSK Express brokers make critical Kafka configuration read-only and fully managed, with storage that scales automatically and "90% faster recovery when broker nodes fail" [9]. Kinesis is "fully managed… AWS handles everything else" [11].

**The cost is vendor lock-in.** Kinesis "cannot be self-hosted (no on-prem option), making it only viable for AWS users" [11]. DynamoDB, the API Gateway Management API, and platform-specific IAM/monitoring tooling are all proprietary. Data egress fees "can represent 10%–15% of total cloud costs and make migration financially unattractive" [22], and "each integration becomes a migration barrier, potentially turning migration into full application rewrites" [22]. Migrating from Kinesis to Kafka, for example, "requires producer/consumer code changes" and parallel running of both systems; data cannot be directly migrated [25].

**Cost behavior at massive concurrency is the central economic risk.** AWS API Gateway WebSockets bills **$1.00 per million messages** plus **$0.25 per million connection-minutes**, and connection minutes accrue **even when idle** [23][24]. At list price, one million continuously connected clients generate roughly 43.8 billion connection-minutes per month — about **$11,000/month before a single message is sent** [23]. Worse, API Gateway has **no native broadcast**: "sending the same message to multiple clients requires individual 1:1 API calls" [19]. A message to 1,000 online members therefore costs 1,000 billable Management API calls — the managed-service mirror of the O(N) fan-out problem Slack and Discord solved with custom infrastructure. Azure Web PubSub meters outbound traffic in 2-KB increments, so a 100-KB broadcast to 1,000 connections counts as ~50,000 billed messages [20]. GCP Cloud Run can serve 250,000 chat clients, but at roughly **$87/hour (~$62.6K/month)** for 1,000 instances — "up to 50x cheaper" on GCE/GKE virtual machines for predictable loads [8].

### Consistency Model Trade-offs

The managed stack is **naturally strong where it matters most**:

- **Message ordering**: Kafka/MSK provides strict per-partition ordering via the partition key; routing on `channel_id` yields per-channel order [25]. MSK defaults to `replication.factor: 3` and `min.insync.replicas: 2` for 3-AZ clusters [10], so `acks=all` producers get strong durability. DynamoDB gives ordered per-channel history with a `(channel_id, server_seq)` key and **strongly consistent reads on the main table at 2× RCU cost** [12].
- **DynamoDB Global Tables** default to multi-Region eventual consistency (MREC) with last-writer-wins and ~1-second replication; a new **Multi-Region Strong Consistency (MRSC)** mode (GA January 2025) provides zero RPO but requires exactly three Regions and disables TTL, transactions, and LSIs [15][16].

The stack is **naturally eventual where users tolerate it**:

- **Global Secondary Indexes (GSIs) are always eventually consistent** — any read pattern served from a GSI cannot be strong [12]. Empirical testing by Alex DeBrie found GSIs consistent ~96.5% immediately after a write, rising to 99.7% at 100 ms [13].
- **Redis Pub/Sub is at-most-once**: "if the subscriber is unable to handle the message… the message is forever lost" [14]. This is acceptable for presence (the next heartbeat corrects state) and typing indicators, but never for messages.
- **Read receipts** are the canonical breakage case: reading from a lagging replica makes a receipt "flicker." Per-message receipts should be read strongly; aggregate counters ("12 read") tolerate lag.

### Scalability Mechanisms

- **Partitioning**: Kafka topics partitioned by `channel_id` preserve order but pin hot channels to a single partition. MSK Serverless supports up to **2,400 partitions** per cluster with **250 GB per partition** of retention [27]; Kinesis scales in shards (1 MB/s write each) with MD5-hash routing and **no auto-scaling** [11][25].
- **Fan-out**: API Gateway requires N separate 1:1 Management API calls for broadcast [19]; Redis pub/sub fans out in O(subscribers) with sub-millisecond latency [14]; DynamoDB Streams enable event-driven fan-out (write → stream → Lambda → SQS/SNS/EventBridge) that decouples downstream work [17].
- **WebSocket layer**: API Gateway has **no direct concurrent-connection cap** but defaults to 500 new connections/sec (increasable), bounding sustained concurrency to ~3.6 million; connections die after **2 hours**, and idle connections time out after **10 minutes** [5]. Azure Web PubSub scales to **1 million concurrent connections per resource** [6]. GCP Cloud Run caps at 250 concurrent connections per instance × 1,000 instances = 250K clients, with a **60-minute request cap** requiring reconnect logic [8].
- **Storage**: DynamoDB `TTL + Streams + Kinesis Firehose → S3` provides a canonical hot/cold pipeline — TTL deletions are free and save storage cost; the full archival pipeline runs ~$0.34/month per 10 GB [17][18]. Standard-IA storage at $0.10/GB-month yields 74% cost reduction on aging data [18].

### Fault Tolerance & Latency

- **DynamoDB replicates across three Availability Zones** with synchronous majority quorum [12]; MSK's RF=3/minISR=2 configuration tolerates one broker loss while preserving consistency [10]; Azure Web PubSub Premium is zone-redundant, and on zone failure "active connections are dropped but reconnect typically takes only a few seconds" [7].
- **The managed edge is the weak point.** API Gateway "doesn't guarantee message ordering or delivery during disconnections," has no fallback transport for blocked WebSockets, and its 99.95% SLA allows ~4.5 hours of downtime per year [19]. Cloud Run's 60-minute cap [8] and Web PubSub's potential message loss when a client disconnects over a minute and reconnects with the same connection ID [7] mean the application must implement its own recovery logic.
- **The universal corrective pattern** is "persist before deliver": write durably and assign a per-conversation `server_seq` before acknowledging the sender; track per-device `last_delivered_seq` cursors; on reconnect, pull all messages with `seq > cursor`. "Server push is an optimization for latency, not correctness" [72][73]. Slack, for contrast, built exactly this correctness layer in-house, with Kafka as the durable ledger and Redis for in-flight fast access [53].

### Pros and Cons

**Pros**

1. **Minimal operational burden** — the provider operates the hard distributed systems: MSK manages Kafka brokers, patching, and storage scaling [9]; API Gateway owns connection lifecycle [4]; DynamoDB replicates across 3 AZs with free TTL deletions [12][18]; Azure Web PubSub is fully managed with a 99.95% Premium SLA [6][7].
2. **Elastic pay-as-you-go capacity aligned with bursty chat traffic** — Lambda/DynamoDB on-demand, MSK Serverless, and Web PubSub autoscaling absorb spikes (Slack's traffic spikes "at the top of the hour due to reminders, scheduled messages, and calendar events" [29]) without capacity planning.
3. **Native resilience and durability primitives** — 3-AZ data replication [10][12], managed failover via Global Tables [15], built-in replay (Kinesis 365-day retention, Kafka tiered storage, DynamoDB PITR/Streams) [11][17], and an integrated TTL-to-S3 archival pipeline [17][18].

**Cons**

1. **Significant vendor lock-in** — proprietary APIs (Kinesis, DynamoDB, Management API), egress fees of 10–15% of cloud costs [22], and migrations that amount to "full application rewrites" [21]. Kinesis is a one-way door: "only viable for AWS users" [11].
2. **Cost and throughput ceilings at massive concurrency** — idle connection-minutes are billable [23]; fan-out to N clients requires N billable API calls [19]; 2-KB-increment billing amplifies Azure broadcast costs [20]; Cloud Run costs 50× more than VMs for sustained loads [8]; account-level throttles (10K RPS) require support tickets to raise [5][19].
3. **Weak delivery guarantees at the managed edge** — no ordering or delivery guarantees during disconnects [19], 2-hour connection caps [5], at-most-once Redis pub/sub [14], eventually consistent GSIs and Global Tables [12][15], and per-query strong-read surcharges. The "zero-ops" promise holds for infrastructure, not for chat semantics — the application must still build the Slack-style correctness layer [72][73].

---

## Strategy 2: Self-Managed, Platform-Agnostic Open-Source Stack

### Overview

This strategy runs portable, open-source components — typically on Kubernetes — deployable identically on any cloud or on-premises. The reference stack: **self-hosted Apache Kafka or Redpanda** for the message bus, **self-managed Redis or KeyDB** for presence and pub/sub, **NATS JetStream or RabbitMQ** for real-time delivery, **Cassandra or ScyllaDB** for message history, and a **custom WebSocket gateway tier** (or the open-source Centrifugo gateway) [48][49][50]. The design principle is "deliver fast, store reliably, and design for scale": real-time delivery through Redis/NATS, durable storage through Kafka → consumer → database [42].

### Cloud-Native vs. Platform-Agnostic Deployment

**Portability is the defining advantage.** Self-hosted Kafka "wins on portability (any cloud/on-prem), full broker config control, and low vendor lock-in" [49]. Redpanda "deploys anywhere (cloud, private cloud, bare metal, edge)" [51]. Every component is open-source and free (Apache License 2.0) [50], and there are no per-connection or per-message fees — a critical factor at millions of WebSocket connections.

**The operational burden is severe.** Mark Smith, Director of Engineering at Discord, who previously helped scale Kafka at Dropbox to 15M messages/sec across 100 brokers, summarized the industry consensus: "It turns out Kafka is actually kind of hard… It's very easy to download and start them. It's a lot harder to run them at scale" — citing Kafka's **150+ broker tunables** [31]. Confluent's comparison claims self-managed Kafka averages **2+ years to reach production at scale** and $3–5M in platform development and operations costs [35]. Discord's experience on Cassandra required manual "gossip dances" — taking nodes out of rotation to compact without taking traffic — and JVM garbage-collection pauses so bad that operators had to manually reboot nodes [32][33][81].

**Cost at scale is dramatically lower.** The AxonOps 2026 cost model compares identical clusters across providers: 3 brokers (~45 MB/s ingress) costs ~$571/month self-hosted vs ~$1,045/month MSK vs ~$1,216/month Confluent; 30 brokers (~1.9 GB/s ingress) costs ~$8,820/month self-hosted vs ~$37,257/month MSK vs ~$42,000–$53,800/month Confluent [34]. Redpanda claims C++ thread-per-core architecture consumes "1/3rd the compute resources of Apache Kafka" with "up to 6x lower TCO" [51]. These savings are the compensation for the engineering time spent running the systems.

### Consistency Model Trade-offs

**The stack is naturally strong where you configure it to be.**

- **Kafka** guarantees that "a committed message will not be lost, as long as there is at least one in-sync replica alive at all times" [36]. With `acks=all` and `min.insync.replicas=2` (the production recommendation; `min.insync.replicas` defaults to 1, which silently makes `acks=all` behave like `acks=1`), per-partition ordering and durability are strong [37]. Kafka's ISR model tolerates f failures with f+1 replicas — more efficient than majority quorum [36].
- **Cassandra/ScyllaDB** provide tunable consistency: with `R + W > RF`, quorum reads guarantee intersection with writes, "providing strong consistency while maintaining distributed resilience" [38][39]. `LOCAL_QUORUM` is "generally recommended for most production environments" [39]. Cassandra 5.0's blocking read repair provides monotonic quorum reads [36].

**The stack is naturally eventual where you don't.**

- **Redis replication is asynchronous by default**; the `WAIT` command "does not create a CP system with strong consistency" [40]. Sentinel "does not guarantee that acknowledged writes are retained during failures" [41].
- **Redis Pub/Sub is at-most-once** [14]; **Core NATS is at-most-once** (JetStream adds at-least-once) [42].
- **Cassandra conflicts resolve by last-write-wins timestamp**, which can silently lose updates [36].

For the target system, per-channel ordering uses Kafka partitions keyed by `channel_id`; presence uses Redis TTL heartbeats (eventual is fine); read receipts should use QUORUM-level reads to avoid flicker; message history reads via `LOCAL_QUORUM` [39]. The team must understand that consistency is **per-query and per-component**, not global.

### Scalability Mechanisms

- **Kafka partitioning**: partitions are the horizontal-scaling lever; each partition is an ordered, immutable sequence served by one leader broker [37]. KRaft (Kafka 4.0+) replaces ZooKeeper, removing its ~200,000-partition scaling ceiling [37].
- **Cassandra/ScyllaDB sharding**: consistent-hash token ring with vnodes; Discord's schema keys messages by `(channel_id, bucket, message_id)` with Snowflake IDs for chronological clustering [33]. The **hot partition problem** — a popular channel concentrating reads on one node — caused cascading latency across Discord's cluster; the fixes were architectural, not just a faster database: a Rust data-services layer with **request coalescing** (concurrent identical requests share one DB query) and consistent-hash routing by `channel_id` [33][81].
- **Fan-out**: Redis pub/sub is the pragmatic broker for gateway interconnect at moderate scale; the Centrifugo author's benchmarks found RabbitMQ needed ~70 CPU cores to handle 100K online connections where Redis used 0.3 cores, and Kafka/Pulsar dislike dynamic ephemeral topics. His recommendation: Redis pub/sub for low-latency fan-out **plus** a sliding-window in-memory stream per channel so reconnecting clients recover messages within the at-least-once window [46].
- **WebSocket gateways**: one tuned node can hold hundreds of thousands of connections — memory is ~2–10 KB per idle connection, so 500K+ idle connections fit in 16 GB RAM with tuned OS file-descriptor limits [47]. Scaling is horizontal: shard gateways, use consistent hashing for affinity, and store session state in Redis rather than relying on fragile sticky sessions [47][48].
- **Storage optimizations**: append-only LSM trees favor writes over reads [81]; **Time-Window Compaction Strategy (TWCS)** is "the recommended compaction strategy for time-series and expiring TTL workloads" — it compacts only within a time window, so entire SSTables expire at once via TTL [44][45]. Kafka tiered storage (KIP-405) offloads old segments to S3/HDFS/GCS [61].

### Fault Tolerance & Latency

- **Kafka** isolates failures via ISR: a follower is removed after 30 seconds of lag; consumers never read past the high watermark, so they never see potentially lost records [36]. With RF=3/minISR=2, one broker loss is tolerated [37].
- **Cassandra** uses phi-accrual failure detection, hinted handoff, read repair, and Merkle-tree anti-entropy repair [36][38]. Discord's ScyllaDB migration cut p99 read latency from 40–125 ms to a stable 15 ms, p99 write latency from 5–70 ms to 5 ms, and shrank the cluster from 177 to 72 nodes [32][33].
- **Redis** requires at least three Sentinels; failover never starts without majority, and the quorum is only for failure detection [41]. Discord's own architecture demonstrates the endgame: Slack's 2021 Availability-Zone gray failure drove an 18-month migration to **cellular architecture** where services communicate only within their AZ and unhealthy AZs are drained in under 5 minutes [29].
- **Latency profile**: self-hosted Kafka often outperforms managed for real-time workloads [48]; NATS JetStream offers single-digit-millisecond publish-to-consume [71]; Redis pub/sub delivers sub-millisecond in-region fan-out [14].

### Pros and Cons

**Pros**

1. **Full portability and zero vendor lock-in** — the same open-source stack runs on any cloud, on-premises, or hybrid environment [49][50][51]; no proprietary APIs and no per-connection fees.
2. **Predictable, dramatically lower infrastructure cost at scale** — the AxonOps model shows self-hosted Kafka at roughly half to one-fifth the cost of managed alternatives as clusters grow [34]; Redpanda claims up to 6× lower TCO [51].
3. **Deep control and performance tuning** — full broker/database configuration control, per-query consistency levels, and compaction-strategy selection. The payoff is documented: Discord's ScyllaDB migration delivered 3–8× better p99 latency while using 60% fewer nodes [32][33].

**Cons**

1. **Significant operational burden and required SRE expertise** — "Kafka is actually kind of hard" [31]; 150+ tunables, JMX metric firehoses, manual patching and upgrades, 3AM pages, and multi-year productionization timelines [35][47][48].
2. **Loss of managed-service conveniences** — no 99.99% SLA from the platform (Confluent contrasts its SLA of max 0.876 hours/year downtime vs MSK's 99.9%) [35]; automatic scaling, upgrades, and monitoring are all manual; community support "can be slow and inconsistent" [50].
3. **Eventual consistency drift across components** — async Redis replication [40], at-most-once pub/sub [14][42], LWW conflict resolution [36], and per-component consistency settings create a system where enforcing strong consistency for read receipts and ordered history is a continuous engineering effort, and windowed inconsistencies (flicker, flapping presence, out-of-order messages) surface precisely at scale.

---

## Strategy 3: Fan-Out-on-Write with Per-User Inboxes and Sharded WebSocket Gateways

### Overview

This is the architecture of Slack, Twitter/X, and Discord — the three canonical large-scale messaging systems. When a user sends a message to a channel, the system writes it once to the channel log, then **fans it out on write** to per-user inboxes and/or directly to the sharded WebSocket gateway tier holding each connected user's connection, using a pub/sub bus (Redis pub/sub, Kafka, NATS) to route events to the right gateway node [3][29][53].

Slack's production implementation consists of four core Java services: **Channel Servers (CS)** — stateful, in-memory servers holding channel history, mapped to channel subsets via consistent hashing, serving ~16 million channels per host at peak; **Gateway Servers (GS)** — stateful, in-memory servers holding user info and WebSocket subscriptions, deployed multi-region with a draining mechanism for region failover; **Admin Servers (AS)** — stateless interfaces between the webapp and CS; and **Presence Servers (PS)** — in-memory, powering the green presence dots, with users hashed to individual PSs [1][29]. Consistent Hash Ring Managers (CHARMs) replace unhealthy CSs in under 20 seconds, and CSs register in Consul [1].

The message path: client → Webapp API → AS → CS (via consistent hashing) → every subscribed GS worldwide → connected clients. Slack serves "tens of millions of channels per host, tens of millions of connected clients," and delivers messages worldwide within 500 ms [1][30]. Twitter's variant maintains a **per-user home timeline** — a Redis list of tweet IDs capped at ~800 entries, replicated 3× across machines — updated at write time by a fan-out service that queries the social graph (Flock) and appends the tweet ID to every follower's list [3][55]. Discord's variant shards the gateway into thousands of slices, each handling a small fraction of users, with sessions resumable after disconnect [56][67].

### Cloud-Native vs. Platform-Agnostic Deployment

This pattern is **deployment-agnostic in principle**: every component has both managed and self-managed options. Kafka runs on bare metal, VMs, or containers, managed or self-managed [37]; Redis and NATS have cloud offerings; the gateway tier can be built on Node.js, Go, Elixir/BEAM, or Netty, or outsourced to managed WebSocket services. Slack, Twitter, and Uber all built the stateful tiers in-house because no managed service met their requirements — Slack's home-grown CHARMs, Consul, and multi-region draining are the direct consequence [1][29][30].

**The operational burden is the truth of this strategy.** The gateway tier is stateful, and "state is the enemy of scalability" [68]. Postman's Sync service, built on this pattern, "disconnected all clients" on every deployment, causing "6–8 hour recovery surges when a million sockets reconnected" — until they engineered a custom two-part gateway (Fastify + ElastiCache Redis) with externalized session state [62]. Kernel tuning is mandatory: file-descriptor limits, conntrack tables, ephemeral port exhaustion, and ~50 KB RAM per idle connection with TLS (~100 GB for 1M connections) [47][63]. L4 load balancers are recommended over L7 because L7 proxies "enforce idle timeouts, silently dropping idle WebSocket connections — creating a self-inflicted connection storm" [47].

**Cost favors self-managed at scale.** One million concurrent connections on AWS API Gateway would cost ~$11,000/month in idle connection-minutes alone [23], while a tuned EC2 fleet can hold 500K connections per node [63]; the Hacker News consensus after published 600K-connection benchmarks: "AWS API Gateway websockets are much more expensive than EC2 at sustained load" [63]. The trade-off is that the EC2 fleet must be built, monitored, and repaired by the team.

### Consistency Model Trade-offs

The pattern targets **strong per-channel ordering with loose cross-channel ordering** — the accepted industry standard [29][72]. Slack uses client-generated message IDs and salts for idempotency, and "durable-before-ack ordering": the message persists before the sender is acknowledged or delivery begins [53]. Slack's delivery contract is **at-least-once with client-side idempotency** to prevent duplicate message display [54]. Twitter's timelines use Snowflake IDs (timestamp + worker ID + sequence) for globally time-sortable ordering [55].

**Where eventual consistency is accepted**: presence. Presence is "computed, not stored" — Discord handles presence as ephemeral high-volume state via an in-memory distributed cache with partial fan-out, and Slack reduces presence events by a factor of 5 via pub/sub and viewport-scoped delivery [1][52][67]. A momentarily stale green dot is acceptable UX; a lost message is not.

**Where eventual consistency breaks**: the celebrity problem. Twitter observed "race conditions where replies appear before original tweets" when high-fan-out users' tweets were delayed in fan-out [3]. Redis Pub/Sub is at-most-once — acceptable for transient events, never for messages [14]; Kafka guarantees ordering only within a partition, so a channel's messages must map to a single partition to preserve order [37][64].

### Scalability Mechanisms

- **Fan-out on write vs. read**: pure write fan-out gives O(1) reads — Twitter's timeline service median request is 5 ms, p99 ~100 ms [3] — but produces massive write amplification: "a hot group example: 50,000 members with fan-out-on-write creates 50,000 writes per message" [63]. At Slack's scale, 75K messages/sec × ~20 members/channel ≈ 1.5M WebSocket pushes/sec [29]. The production solution is **hybrid**: users/channels below a threshold (~10K–20K followers on Twitter) use fan-out on write; celebrities/large guilds skip fan-out and are merged at read time [55][56]. Discord's /r/Overwatch guild with 30,000 concurrent users showed why: publishing an event took 900 ms to 2.1 s in the naive design [2].
- **Per-user inboxes**: Twitter's inbox is a Redis list per user, capped at ~800–1,000 IDs with FIFO eviction; active users stay entirely in RAM; each tweet ID is replicated across 3 machines [3][55]. The inbox is a **derived cache**, not the source of truth — the authoritative tweet store (T-bird) hydrates the IDs [3]. For chat, the equivalent is: channel log = source of truth; per-user inbox or per-device `last_delivered_seq` cursor = materialized view [72][73].
- **Sharded WebSocket gateways**: Discord shards by `shard_id = (guild_id >> 22) % num_shards`, with each shard supporting up to 2,500 guilds [57]. One Elixir process per guild (a GenServer) provides fault isolation — one busy server's crash never impacts others [2]. Discord's **Manifold** library fixes the O(N) fan-out problem: by grouping PIDs by remote node and consistent hashing across cores, each sending process calls `send/2` only once per involved remote node, reducing network traffic by 90%+ in large servers [2]. **FastGlobal** cut ring lookups from 7 μs to 0.3 μs using a read-only shared heap; the **Semaphore** library protected the guild registry from 5M session processes stampeding it [2].
- **Storage optimizations**: messages are append-only in the channel log; Discord's ScyllaDB schema `(channel_id, bucket, message_id)` clusters by time [33]; Snowflake IDs "cluster well for storage" unlike random UUIDs [81]. Hot history lives in CS memory (Slack) or ScyllaDB (Discord); cold data tiers to object storage; search is a separate index (Slack uses Elasticsearch) [29][55].

### Fault Tolerance & Latency

- **Gateway node failure** drops thousands of connections, but Discord's design limits blast radius: "if one [shard] crashes, only a small portion of users are affected" [67]. Discord's protocol supports **Session Resumption** — `Resume` (opcode 6) with a `session_id` and `resume_gateway_url` — so clients resubscribe without re-identifying; sessions stay resumable for minutes after non-clean disconnects [57]. Slack's GS draining switches users to the nearest good region; its Flannel edge cache absorbs reconnect thundering herds [1][29][52].
- **Reconnection storms** are the classic failure: Postman's 6–8 hour recovery surges after each deploy [62]. Mitigations: jittered exponential backoff (Slack uses 1 s base, 30 s max, 0–50% jitter) [29], rate limiting, and startup-payload reduction — Slack's Flannel cuts bootstrap payloads 44× for 32K-user teams [52].
- **Kafka/Redis failure**: Twitter's MirrorMaker caused weekly outages with 5–10 minute rebalancing pauses; Uber replaced it with uReplicator using static partition assignment [61]. Redis Cluster provides automatic failover but with asynchronous replication and split-brain prevention requiring odd node counts [68]. Uber's RAMEN push platform achieved **99.99% server-side reliability, 1.5M+ concurrent connections, and 250K messages/sec** using sequence numbers for resumability — clients reconnect with the largest sequence number seen, and the server resends missed messages [59]. Uber's chat platform cut undelivered-event errors from 46% to 0.45% using bidirectional ping-pong heartbeats, backed-off reconnects with contact re-fetching, and 10K sockets per machine with 20× horizontal scaling [60].
- **Latency baselines**: Slack delivers worldwide in 500 ms [1]; Discord targets sub-100 ms delivery [67]; Twitter's timeline reads are tens of milliseconds normally [3].

### Pros and Cons

**Pros**

1. **Extremely fast reads** — per-user inboxes are precomputed at write time, giving O(1) timeline reads: Twitter's timeline service median is 5 ms [3]; Slack scales linearly to tens of millions of connected clients [1].
2. **Proven at planetary scale** — this is the architecture of Twitter, Slack, Discord, and Uber's push platform; every component has survived real production incidents, from Slack's gray-failure-driven cellular migration [29] to Discord's 5M-user Elixir scaling [2].
3. **Deployment flexibility** — the pattern runs on open-source components (Kafka, Redis, NATS) or managed equivalents (MSK, ElastiCache, Ably), and the gateway tier is portable across clouds if session state is externalized to Redis [37][47][68].

**Cons**

1. **Severe write amplification and hot-key problems** — one message to 1,000 members = 1,000 pushes [53]; a 31M-follower celebrity tweet = 31M timeline updates [3]; Discord's early design failed at 30,000 concurrent users in one guild [2]. The hybrid push/pull threshold exists precisely because pure fan-out "collapses for celebrities" [55][56].
2. **Consistency and duplication complexity** — at-least-once delivery requires idempotent consumers and client-side dedup [54]; Redis pub/sub is at-most-once [14]; Kafka ordering holds only within a partition [37]; the celebrity race condition (replies before originals) is a documented failure mode [3]; per-user inbox state must reconcile with the authoritative channel log after every failure [72][73].
3. **High operational burden** — the stateful gateway tier demands kernel tuning, L4 load balancing, session resumption buffers, and reconnect-storm management [47][62][63]; Slack runs four stateful Java services plus CHARMs, Consul, and Flannel [1]; Postman's team spent years engineering around deployment-induced disconnects [62]; fully-managed alternatives eliminate this burden but reintroduce per-connection costs [19][63].

---

## Strategy 4: Log-Centric Event Sourcing with Append-Only Channel Logs and Materialized Views

### Overview

This strategy treats **the append-only log as the system of record**. Every chat message is an event appended to a durable, ordered channel log (Kafka, Kinesis, NATS JetStream, or DynamoDB Streams). All other state — per-user inboxes, unread counts, read receipts, search indexes, analytics — is a **materialized view** (CQRS projection) built by consuming the log. Slack's production architecture embodies this principle: Kafka serves as the durable event log — "the system's ledger" — while Redis holds in-flight fast-access job data [53]. Kafka itself is "a distributed commit log: an ordered, replicated, append-only record store" [37]. Twitter's home timelines are literally materialized views of the tweet log: they store only tweet IDs, capped at 800, hydrated against the authoritative tweet store at read time [3]. NATS JetStream goes further, treating consumers as server-side views of a stream — "JetStream behaves more like a NoSQL data store" [69][75].

The core distinction from Strategy 3 is architectural emphasis: Strategy 3 optimizes the fan-out path; Strategy 4 makes **replayability and derivation** the organizing principles. Any view can be rebuilt at any time by replaying the log from an offset, timestamp, or snapshot.

### Cloud-Native vs. Platform-Agnostic Deployment

The log abstraction is fully portable across deployment models:

- **Self-hosted Kafka** (Strategy 2's operations) or **MSK/Confluent** (Strategy 1's delegation) — both expose the same commit-log semantics [35][37].
- **Kinesis** is AWS-only and not self-hostable [11].
- **NATS JetStream** ships as a single small binary with Raft-based persistence, ideal for edge or constrained environments [69].
- **Redpanda** is Kafka-API-compatible and deploys anywhere [51].

The strategic choice is therefore **which log tier to bind to**, and the managed/self-managed trade-offs are exactly those analyzed in Strategies 1 and 2: MSK Express offloads broker operations [9]; self-hosted Kafka wins on cost and control [34]; Kinesis maximizes lock-in [11]. The pattern itself is implementation-agnostic — which is its principal portability strength.

### Consistency Model Trade-offs

The log provides **strong per-partition ordering and durability**. With `acks=all` and `min.insync.replicas=2`, a committed message is never lost while one ISR replica lives [36]. Kafka's transactional API (idempotent producers + transactions + `read_committed` consumers) enables exactly-once processing, but at a cost: roughly 2–5 ms added latency and 10–20% throughput reduction [66]. Uber's production exactly-once ad pipeline combines Flink transactional producers, Kafka `read_committed` isolation, two-minute checkpoints, per-record UUIDs, and sink-side deduplication — demonstrating that end-to-end exactly-once is "a coordinated strategy across producers, consumers, and sinks, not a single feature" [61][70].

**Materialized views are eventually consistent by construction.** A view builder consuming the log lags the write path by definition. For message history this is fine: the log itself provides strong read-your-writes ("did my message land?") via a synchronous log read or strong store read [12][72]. For read receipts and unread counts, the system must either (a) update the view transactionally with the event write (e.g., DynamoDB transactions), (b) accept bounded staleness with monotonic cursors, or (c) route the affected user's reads to the log. Presence should **not** be in the log at all — ephemeral state belongs in Redis heartbeats, not an immutable ledger [14][72]. The event-sourcing literature consistently recommends: "strong per-channel ordering with loose cross-channel ordering" [29], causal consistency for reply threads [71], and "read-your-own-writes" as the pragmatic contract for chat [74].

### Scalability Mechanisms

- **Partitioning**: partition by `channel_id` gives per-channel ordering and parallelizes across brokers; the cost is hot channels pinned to one partition — Discord's hot-partition problem [33][81]. MSK Serverless supports 2,400 partitions with 250 GB/partition of retention, enabling long replay windows [27].
- **Fan-out**: the log decouples producers from consumers — **any number of consumer groups** can read the same log at their own pace (fan-out on read from the log), while materialized-view builders (inbox writer, search indexer, analytics pipeline) perform fan-out on write to their own stores. This is strictly more flexible than the single-path fan-out of Strategy 3, at the cost of operating more moving parts.
- **Storage optimizations**: append-only logs are sequential-write-optimized [37][81]; **Kafka tiered storage (KIP-405)** offloads old segments to S3/HDFS/GCS/Azure, "decoupling retention from broker capacity" — Uber runs this in production [61]. **Log compaction** keeps the latest value per key for stateful streams [37]. For time-bucketed message history in Cassandra/ScyllaDB, **TWCS** is the recommended compaction strategy for TTL expiring time-series data [44][45]. Hot history stays in row-oriented stores (ScyllaDB/DynamoDB); cold analytics move to columnar stores (S3 + Athena/Redshift) via Firehose [17][18].
- **Materialized views in practice**: Twitter's per-user timelines (Redis lists of IDs) [3], Discord's ScyllaDB `(channel_id, bucket, message_id)` table [33], and search indexes are all projections of the same event stream. Kafka Streams' KTables and Flink stateful operators are the standard view-building engines [37][61].

### Fault Tolerance & Latency

- **Replay is the superpower.** A corrupted or lost view is rebuilt by replaying the log: Kinesis supports `AT_SEQUENCE_NUMBER`, `AT_TIMESTAMP`, `TRIM_HORIZON`, and `LATEST` iterators [11]; Kafka consumers track offsets in `__consumer_offsets` with rebalance-aware assignment [37]; MSK Serverless's 250 GB/partition retention enables "reconstructing application state after failures by replaying data from the earliest timestamps" [27].
- **Log replication** (ISR, RF=3/minISR=2) provides the durability base [36][37]. Multi-region replication uses MirrorMaker 2 or Uber's uReplicator (which eliminated 5–10 minute rebalance pauses) [61]. Uber's architecture of **Regional Clusters + Aggregate Clusters** with cross-region replication is the production reference [61].
- **Change Data Capture** extends the pattern to other systems: Uber's StorageTapper reads MySQL binlogs into Kafka, making the log the integration backbone [61].
- **Latency**: Kafka achieves p99 15–25 ms; NATS JetStream delivers single-digit-millisecond publish-to-consume [71]. The critical latency insight is that strong consistency requires waiting for the slowest replica, so read-your-writes via the log adds a quorum round-trip — the standard trade-off of "as slow as the slowest network path" [36][74].
- **Backfill logic**: offline clients catch up from per-device `last_seq` cursors — either from the log, from a Redis sliding-window stream, or from the history store [46][72][73]. This is the same correctness pattern as every other strategy, but the log gives it a unified implementation.

### Pros and Cons

**Pros**

1. **The log is an immutable, replayable source of truth** — auditability, time travel, view rebuilds, and disaster recovery for free. Kinesis timestamps, Kafka offsets, and 250 GB/partition retention make "reconstruct application state by replaying data from the earliest timestamps" a practical operational procedure [27][61][69].
2. **Full decoupling of write path from read path (CQRS)** — ingestion and projections scale independently; any number of consumers (inboxes, search, analytics, ML) read the same log at their own pace [37][69]; new consumers are added without touching producers.
3. **Naturally supports multi-consumer fan-out and Change Data Capture** — Uber's production Kafka runs 12M messages/sec across 200K partitions, feeding matching, fraud, analytics, and search simultaneously [61].

**Cons**

1. **Materialized views are eventually consistent** — strong read-your-writes requires synchronous log reads or transactional view updates, adding latency and complexity; flickering unread counts and read receipts are the classic bugs [12][72][74].
2. **Operating a log platform at scale is heavy** — Kafka's 150+ tunables [31], consumer-group rebalancing failures [61], ZooKeeper→KRaft migrations [35], and event-schema evolution (a log is forever; events must be versioned) are real operational tax. The log is a single logical system of record, so its failure modes are existential until ISR quorum returns [36].
3. **Hot partitions bound per-channel throughput** — ordering is per partition, so a very large channel is pinned to one partition leader; Discord's hot-partition cascades show the consequence [33][81]. Mitigations (splitting hot channels across sub-partitions) sacrifice strict global ordering.

---

## Strategy 5: Serverless Event-Driven Architecture and Realtime BaaS

### Overview

The fully serverless strategy pushes delegation to its logical extreme: compute is **functions-as-a-service** (AWS Lambda, Azure Functions, Cloud Run), state is a **managed NoSQL/streaming service** (DynamoDB, Cosmos DB, Kinesis, Pub/Sub), and realtime connectivity is either a **managed WebSocket gateway** (API Gateway WebSockets, Azure Web PubSub) or a **realtime Backend-as-a-Service** (Ably, PubNub, Pusher, Firebase Realtime Database). The canonical AWS tutorial implements the entire chat backend as three Lambda functions (`$connect`, `sendmessage`, `$disconnect`) plus a DynamoDB connection registry [4]. GCP's reference implementation runs stateless Cloud Run containers with WebSockets, synchronizing instances via Memorystore Redis pub/sub [8][78]. The BaaS variant outsources connections, presence, and pub/sub entirely: Ably reports handling 30+ billion connections monthly with a 99.999% uptime SLA, 99.999999% message survivability, 6.5 ms global delivery, and automatic connection resumption [68].

### Cloud-Native vs. Platform-Agnostic Deployment

**Operational burden approaches zero.** There are no servers, no connection pools to tune, no TLS terminations to manage. "The connection is handled by API Gateway" — Lambda runs only on connection events [76]. Azure Web PubSub is fully managed, encrypts, authenticates, and autoscales connections with a Premium SLA of 99.95% [6][79]. Cloud Run autoscales stateless instances to 250K concurrent chat clients [8][78].

**Lock-in is maximal.** The API Gateway Management API is a proprietary callback interface; Kinesis is not self-hostable [11]; BaaS platforms are proprietary by definition — migrating off Ably/Pusher means rewriting the realtime layer. Data egress fees and proprietary IAM tooling compound the trap [21][22]. The EKS + API Gateway pattern (offload connections to the managed gateway, keep business logic in Kubernetes) is a deliberate de-risking hybrid: it "enables easy scaling up and down" of stateless pods while avoiding the cost of managing connections in the cluster [28].

**Cost explodes at sustained concurrency.** As computed in Strategy 1, one million continuously connected clients on API Gateway cost ~$11,000/month in idle connection-minutes alone [23]. Every broadcast to N recipients is N billable Management API calls [19]. Azure Web PubSub bills outbound in 2-KB increments [20]. Cloud Run's 250K-client reference costs ~$87/hour [8]. Ably's pricing is per connection and per message — the BaaS vendor is profitable precisely because the per-connection economics are priced for delegation. The consensus of published analyses: managed WebSockets "may suit small to medium-sized projects," but "for large-scale realtime applications with high-frequency updates, the request limits become a major limitation" [80].

### Consistency Model Trade-offs

The serverless platform provides **strong consistency where you pay for it**: DynamoDB strongly consistent reads (2× RCU, main table only, not GSIs) [12], DynamoDB transactions (2× WCU) [12], and MREC/MRSC Global Tables for multi-region [15]. **Eventual consistency is the platform default everywhere else**: GSIs are always eventual [12][13]; Global Tables default to LWW eventual [15]; Redis pub/su b is at-most-once [14]. Lambda event-source mappings redeliver entire failed batches, so consumers see duplicates — at-least-once is the operating contract [11].

The serverless answer to the chat consistency problem is the same as every other strategy's: **persist before deliver**, per-channel `server_seq` ordering, per-device `last_delivered_seq` cursors, and idempotent message IDs [72][73]. The difference is that the platform does not help with ordering guarantees — "no guarantees on message delivery or ordering" from the AWS gateway [19] — so all ordering correctness lives in the application layer. For presence, the platform's managed channels (or Redis pub/sub) are naturally eventual and self-healing [14]. For read receipts, DynamoDB strong reads on the main table provide the required monotonicity [12].

### Scalability Mechanisms

- **Connection scaling is delegated**: API Gateway has no direct concurrent-connection cap (bounded by the 500/sec connection rate and 2-hour duration) [5]; Azure Web PubSub scales to 1M connections per resource [6]; Cloud Run reaches 250K clients [8]. The practical ceiling is the account-level API throttle (10K RPS default), which requires support tickets to raise [5][19].
- **Fan-out**: the AWS pattern requires iterating the connection registry and calling the Management API once per recipient — O(N) billable calls per broadcast [4][19]. Azure Web PubSub has native group broadcast, billed as outbound messages in 2-KB increments [20]. The BaaS platforms (Ably, Pusher) provide native channel publish/subscribe with automatic connection resumption [68].
- **Compute scaling**: Lambda concurrency and Cloud Run instance limits bound the fan-out logic; Kinesis→Lambda consumers scale by shard count with no auto-scaling [11]. The EKS+API Gateway hybrid pattern uses KEDA to scale pods on connection count and message rate [28].
- **Storage**: DynamoDB on-demand scales to any throughput; TTL + Streams + Firehose archives old messages to S3 at ~$0.34/month per 10 GB [17][18]. Hot data lives in DynamoDB (row-oriented, point-read optimized); cold data in S3 (columnar analytics via Athena) [17].

### Fault Tolerance & Latency

- **Platform-managed failover**: Azure Web PubSub Premium is zone-redundant; on zone failure "active connections are dropped but reconnect typically takes only a few seconds" [7]. DynamoDB Global Tables provide 99.999% multi-region availability [15]. The provider owns patching, capacity, and control-plane failover [6][7].
- **The managed edge degrades gracefully but loses data**: API Gateway "doesn't guarantee message ordering or delivery during disconnections" [19]; Cloud Run's 60-minute cap forces reconnects [8]; Web PubSub may lose messages if a client disconnects over a minute [7]; Redis pub/sub is at-most-once [14]. The platform is reliable for connections; **the application must be reliable for messages** — via the cursor/backfill pattern [72][73].
- **Retry and backfill**: Kinesis provides `AT_TIMESTAMP` replay [11]; Lambda DLQs and DynamoDB Streams provide event-driven retry [17]; the client reconnects and pulls `seq > last_seen` from DynamoDB. Ably's BaaS claim of 99.999999% message survivability with automatic resumption is the vendor-grade version of the same guarantee [68].
- **Latency**: in-region DynamoDB strong reads add ~1× read cost with single-digit-millisecond latency [12]; Kinesis Enhanced Fan-Out delivers ~70 ms consumer latency vs ~200 ms standard [11]; the gateway adds one network hop. The dominant latency risk at scale is the N-call Management API fan-out, which makes broadcast latency O(N) [19].

### Pros and Cons

**Pros**

1. **No infrastructure to manage** — the platform owns connections, scaling, failover, patching, and encryption: "focus on building real-time web experiences without worrying about capacity provisioning, reliable connections, scaling, encryption or authentication" [6]; Lambda runs only on connection events [76].
2. **True pay-per-use elasticity** — capacity scales to zero; no idle server cost; DynamoDB on-demand and Lambda absorb traffic spikes without capacity planning; Cloud Run autoscales to 250K clients without infrastructure work [8][78].
3. **Fastest time-to-market** — a working chat backend is a tutorial's worth of code [4]; BaaS platforms add managed presence, pub/sub channels, and connection resumption out of the box [68][80]; the EKS+API Gateway hybrid preserves Kubernetes portability for business logic [28].

**Cons**

1. **Cost explosion at high sustained concurrency** — idle connection-minutes are billable [23]; fan-out is N billable API calls [19]; Azure bills outbound in 2-KB increments [20]; Cloud Run costs ~$87/hour for 250K clients [8]; BaaS per-connection pricing makes millions of concurrent users a seven-figure annual line item [80].
2. **Hard platform ceilings and maximal lock-in** — 500 connections/sec and 10K RPS account throttles (increasable only via tickets) [5][19]; 2-hour connection caps [5]; no native broadcast on AWS [19]; proprietary Management APIs and Kinesis-style one-way doors [11]; BaaS is proprietary by definition [68].
3. **Weak delivery guarantees at the edge** — no ordering or delivery guarantees during disconnects [19]; at-most-once pub/sub [14]; eventually consistent GSIs/Global Tables [12][15]; Lambda batch redelivery produces duplicates [11]; "no guarantees" means the application must implement the full cursor/backfill correctness layer — the "zero-ops" promise excludes chat semantics [72][73].

---

## Comparative Summary

| Strategy | Operational burden | Cost at extreme scale | Vendor lock-in | Consistency control | Message ordering | Best fit |
|---|---|---|---|---|---|---|
| 1. Managed cloud-native | Very low | High (per-connection/message billing) | High | Strong via DynamoDB strong reads/Kafka partitions; eventual elsewhere | Per-partition | Teams without infra depth; bursty workloads; MVP to medium scale |
| 2. Self-managed OSS | High (SRE required) | Low (infrastructure only) | Low | Tunable per query (QUORUM/ISR); multi-component drift | Per-partition | Cost-sensitive teams with strong ops; long-term scale horizons |
| 3. Fan-out-on-write gateways | High (stateful tier) | Low–medium (EC2 + OSS) | Low–medium | At-least-once + idempotency; eventual presence | Per-channel via sequencer | The proven Slack/Discord/Twitter/Uber pattern |
| 4. Log-centric event sourcing | Medium–high (log platform) | Medium | Medium (log choice dependent) | Strong per-partition log; eventual views | Per-partition log | Audit-heavy multi-consumer systems; replay/backfill needs |
| 5. Serverless/BaaS | Very low | Very high at sustained concurrency | Very high (BaaS) | Platform-dependent; generally weaker edges | Not guaranteed | Prototypes, spiky loads, small teams; not Slack-scale economics |

---

## Conclusion

The five strategies are not mutually exclusive — production systems compose them. Slack runs the fan-out-on-write pattern (Strategy 3) on self-managed infrastructure (Strategy 2), with Kafka as the ledger (Strategy 4) [1][53]. Discord runs the same composition on Elixir/BEAM and ScyllaDB [2][32]. Uber combines Kafka log-centric infrastructure with its own push platform [59][61]. The managed strategies (1 and 5) are the fastest on-ramps; the self-managed and log-centric strategies (2 and 4) are where the economics and correctness controls converge at scale; and the fan-out-on-write gateway pattern (3) is the proven endgame that every large system has reached.

Across all five strategies, the same engineering truths recur:

1. **The durable channel log is the backbone.** Persist before you deliver; the log (Kafka, Kinesis, DynamoDB, ScyllaDB) is the source of truth, and every fast path is a cache or projection of it [53][72].
2. **Fan-out is the core scaling problem.** Write-side fan-out optimizes reads at the cost of write amplification; hybrid push/pull thresholds manage celebrities and megaguilds [3][55][56].
3. **Presence is ephemeral.** Keep its high-volume churn out of the durable path; eventual consistency is correct here [14][67].
4. **Strong consistency is a per-query decision, not a global one.** Message ordering and sender-visible read receipts demand strong guarantees; presence, typing indicators, and aggregate counters tolerate seconds of staleness [12][72][74].
5. **At-least-once plus idempotency is the practical delivery contract.** Exactly-once exists only as a coordinated producer/consumer/sink strategy, and its cost (latency + throughput) is rarely justified for chat [66][70].
6. **Operational burden is the hidden axis.** The managed strategies price operations in dollars; the self-managed strategies price them in engineering time. The right choice depends on the team and the lifecycle stage [19][31][35].

For a student designing this system from first principles, the recommended synthesis is: start with a managed stack (Strategy 1/5) to reach working code quickly; adopt the log-centric discipline (Strategy 4) from day one — durable logs, per-channel sequence numbers, cursor-based sync; and evolve toward the fan-out-on-write gateway architecture (Strategy 3) with self-managed components (Strategy 2) as concurrency crosses into the millions, where per-connection billing and platform ceilings change the economic equation decisively [19][23][34].

---

## Sources

[1] Slack Engineering — Real-time Messaging: https://slack.engineering/real-time-messaging
[2] Discord Blog — How Discord Scaled Elixir to 5,000,000 Concurrent Users: https://discord.com/blog/how-discord-scaled-elixir-to-5-000-000-concurrent-users
[3] HighScalability — The Architecture Twitter Uses to Deal with 150M Active Users: https://highscalability.com/the-architecture-twitter-uses-to-deal-with-150m-active-users
[4] AWS Docs — Tutorial: Create a WebSocket chat app with a WebSocket API: https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-chat-app.html
[5] AWS Docs — Quotas for configuring and running a WebSocket in API Gateway: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-execution-service-websocket-limits-table.html
[6] Microsoft Learn — Scale an instance of Azure Web PubSub Service: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/howto-scale-manual-scale
[7] Microsoft Learn — Reliability in Azure Web PubSub Service: https://learn.microsoft.com/en-us/azure/reliability/reliability-web-pubsub
[8] Ahmet Alp Balkan — Building a high-scale chat server on Cloud Run: https://ahmet.im/blog/cloud-run-chat-server
[9] AWS Big Data Blog — Simplifying Kafka operations with Amazon MSK Express brokers: https://aws.amazon.com/blogs/big-data/simplifying-kafka-operations-with-amazon-msk-express-brokers
[10] AWS Docs — Default Amazon MSK configuration: https://docs.aws.amazon.com/msk/latest/developerguide/msk-default-configuration.html
[11] Kadeck — An in-depth look at Amazon Kinesis and a comparison to Apache Kafka: https://www.kadeck.com/blog/an-in-depth-look-at-amazon-kinesis-and-a-comparison-to-apache-kafka
[12] AWS Docs — DynamoDB read consistency: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html
[13] Alex DeBrie — Understanding Eventual Consistency in DynamoDB: https://alexdebrie.com/posts/dynamodb-eventual-consistency
[14] Redis Docs — Redis Pub/Sub: https://redis.io/docs/latest/develop/pubsub
[15] OneUptime — How to Handle Redis Pub/Sub Message Delivery Guarantees: https://oneuptime.com/blog/post/2026-03-31-redis-pubsub-message-delivery-guarantees/view
[16] AWS Docs — Global tables — multi-active, multi-Region replication (DynamoDB): https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GlobalTables.html
[17] AWS Database Blog — Archive to cold storage with Amazon DynamoDB: https://aws.amazon.com/blogs/database/archive-to-cold-storage-with-amazon-dynamodb
[18] Usage.ai — DynamoDB TTL: Free Deletions That Save You Real Money: https://www.usage.ai/blogs/aws/reserved-instances/dynamodb/ttl-cost-savings
[19] Ably — Scaling AWS API Gateway WebSocket APIs: https://ably.com/topic/scaling-aws-api-gateway-websocket-apis
[20] Microsoft Learn — Billing model of Azure Web PubSub service: https://learn.microsoft.com/en-us/azure/azure-web-pubsub/concept-billing-model
[21] Amnic — What Is Vendor Lock-In and How Can You Avoid It?: https://amnic.com/blogs/vendor-lock-in
[22] Qovery — How to Avoid Vendor Lock-In When Adopting Cloud PaaS: https://www.qovery.com/blog/the-high-cost-of-vendor-lock-in-in-cloud-computing
[23] CostGoat — AWS API Gateway Pricing Calculator & Complete Cost Guide: https://costgoat.com/pricing/amazon-api-gateway
[24] CloudZero — AWS API Gateway Pricing Simplified: 2026 Guide For Cost Savings: https://www.cloudzero.com/blog/aws-api-gateway-pricing
[25] OneUptime — How to Compare Kinesis vs Kafka (MSK): https://oneuptime.com/blog/post/2026-02-12-compare-kinesis-vs-kafka-msk/view
[26] DEV Community — Amazon Kinesis vs Amazon MSK: The Complete Guide for Stream Processing on AWS: https://dev.to/datatechbridge/amazon-kinesis-vs-amazon-msk-the-complete-guide-for-stream-processing-on-aws-3e35
[27] AWS Big Data Blog — Create more partitions and retain data longer in your MSK Serverless clusters: https://aws.amazon.com/blogs/big-data/create-more-partitions-and-retain-data-for-longer-in-your-msk-serverless-clusters
[28] AWS Containers Blog — Optimize WebSocket applications scaling with API Gateway on Amazon EKS: https://aws.amazon.com/blogs/containers/optimize-websocket-applications-scaling-with-api-gateway-on-amazon-eks
[29] Snowan GitBook — System Design: Slack — Enterprise Real-Time Messaging: https://snowan.gitbook.io/study-notes/ai-blogs/design-slack-messaging-system
[30] InfoQ — Real-Time Messaging Architecture at Slack: https://www.infoq.com/news/2023/04/real-time-messaging-slack
[31] ScyllaDB — Discord, on the Joy of Opinionated Systems: https://www.scylladb.com/2019/03/20/discord-on-the-joy-of-opinionated-systems
[32] ByteByteGo — How Discord Stores Trillions of Messages with High Performance: https://blog.bytebytego.com/p/how-discord-stores-trillions-of-messages
[33] HelloInterview — How Discord Moved Trillions of Messages to ScyllaDB: https://www.hellointerview.com/learn/system-design/in-the-wild/discord-messages-scylladb
[34] AxonOps — Kafka Cost Comparison 2026: Self-Hosted vs Amazon MSK vs Confluent Cloud: https://axonops.com/blog/kafka-cost-comparison-2026-self-hosted-vs-amazon-msk-vs-confluent-cloud
[35] Confluent — Confluent Cloud vs. Amazon MSK: Cost, Support & Features: 2026 Comparison: https://www.confluent.io/compare/confluent-cloud-vs-amazon-msk
[36] Confluent — Kafka Replication (official design docs): https://docs.confluent.io/kafka/design/replication.html
[37] Factor House — Apache Kafka architecture: a complete guide: https://factorhouse.io/articles/kafka-architecture
[38] Apache Cassandra Documentation — Dynamo: https://cassandra.apache.org/doc/stable/cassandra/architecture/dynamo.html
[39] Pythian — Cassandra Consistency Level Guide: https://www.pythian.com/blog/cassandra-consistency-level-guide
[40] Redis Docs — Redis replication: https://redis.io/docs/latest/operate/oss_and_stack/management/replication
[41] Redis Docs — High availability with Redis Sentinel: https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel
[42] NATS Documentation — JetStream: https://docs.nats.io/concepts/jetstream
[43] OneUptime — How to Implement a Pub/Sub with Persistence using Redis Streams: https://oneuptime.com/blog/post/2026-03-31-redis-pubsub-with-persistence/view
[44] Apache Cassandra Documentation — Time Window Compaction Strategy (TWCS): https://cassandra.apache.org/doc/latest/cassandra/managing/operating/compaction/twcs.html
[45] ScyllaDB Docs — Choose a Compaction Strategy: https://docs.scylladb.com/manual/stable/architecture/compaction/compaction-strategies.html
[46] Centrifugal Blog — Scaling WebSocket in Go and beyond: https://centrifugal.dev/blog/2020/11/12/scaling-websocket
[47] Centrifugo Documentation — Load balancing and proxying: https://centrifugal.dev/docs/server/load_balancing
[48] WebSocket.org — WebSockets at Scale: Architecture for Millions of Connections: https://websocket.org/guides/websockets-at-scale
[49] AutoMQ — Self-Hosted Kafka vs. Fully Managed Kafka: Pros & Cons: https://www.automq.com/blog/self-hosted-kafka-vs-fully-managed-kafka-pros-amp-cons
[50] Instaclustr — Kafka vs Confluent: 6 differences, pros/cons, and how to choose: https://www.instaclustr.com/education/apache-kafka/kafka-vs-confluent-6-differences-pros-cons-and-how-to-choose
[51] Redpanda — Data Streaming Features & Capabilities: https://www.redpanda.com/data-streaming/platform-capabilities
[52] Slack Engineering — Flannel: An Application-Level Edge Cache to Make Slack Scale: https://slack.engineering/flannel-an-application-level-edge-cache-to-make-slack-scale
[53] ByteByteGo — How Slack Supports Billions of Daily Messages: https://blog.bytebytego.com/p/how-slack-supports-billions-of-daily
[54] scalewithchintan — Slack Message Fanout Architecture Explained: https://scalewithchintan.com/blog/slack-message-fanout-architecture
[55] System Design Handbook — Design Twitter System Design: A Complete Guide: https://www.systemdesignhandbook.com/guides/design-twitter-system-design
[56] Kartikeya Sharma — Timeline Architecture | Fanout on Read vs Fanout on Write (YouTube): https://www.youtube.com/watch?v=SeeKlGMxyBQ
[57] Discord Documentation — Gateway API: https://docs.discord.com/developers/events/gateway
[58] Level Up Coding — System Design Twitter | Scaling Timeline Writes for Fast Reads: https://levelup.gitconnected.com/system-design-twitter-scaling-timeline-writes-for-fast-reads-19f755abaded
[59] Uber Engineering — Uber's Real-Time Push Platform (RAMEN): https://www.uber.com/us/en/blog/real-time-push-platform
[60] ByteByteGo — How Uber Built Real-Time Chat to Handle 3 Million Tickets Per Week: https://blog.bytebytego.com/p/how-uber-built-real-time-chat-to
[61] Factor House — How Uber uses Apache Kafka in production: https://factorhouse.io/articles/uber-kafka-architecture
[62] Postman Blog — Websocket Gateway: How Postman Handles Million Concurrent Connections: https://blog.postman.com/postman-engineering-million-concurrent-connections
[63] Hacker News — 600k concurrent websocket connections on AWS using Node.js (2015): https://news.ycombinator.com/item?id=21222913
[64] Confluent — Message Delivery Guarantees for Apache Kafka: https://docs.confluent.io/kafka/design/delivery-semantics.html
[65] Conduktor — Kafka Exactly-Once: Producers + Transactions: https://www.conduktor.io/glossary/exactly-once-semantics-in-kafka
[66] TechAhead — How Discord Architecture Supports 19 Million Active Communities: https://www.techaheadcorp.com/blog/discord-architecture-social-media-app-development
[67] Ably — How to scale WebSockets for high-concurrency systems: https://ably.com/topic/the-challenge-of-scaling-websockets
[68] Tim Derzhavets — NATS JetStream vs Kafka: Choosing the Right Persistent Messaging Layer for Cloud-Native Systems: https://timderzhavets.com/blog/nats-jetstream-vs-kafka-choosing-the-right-persistent
[69] Confluent — Exactly-Once Semantics Are Possible: Here's How Apache Kafka Does It: https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it
[70] Sanj.dev — NATS vs Apache Kafka vs RabbitMQ: Messaging Showdown: https://sanj.dev/post/nats-kafka-rabbitmq-messaging-comparison
[71] System Design School — Chat / Messenger System Design: https://systemdesignschool.io/problems/chatapp/solution
[72] Educative — Chat System Design: https://www.educative.io/blog/chat-system-design
[73] System Design Handbook — How to Design a Chat System: A Complete Guide: https://www.systemdesignhandbook.com/guides/design-a-chat-system
[74] Synadia — NATS & Kafka Compared: Part 1 (YouTube): https://www.youtube.com/watch?v=C4BnJ5QLeTY
[75] AWS re:Post — In a serverless event driven architecture, is it better to use EC2 or Lambda for a Chat service?: https://repost.aws/questions/QUuuE73vW4QkCk3c7m8WLOmQ/in-a-serverless-event-driven-architecture-i-wish-to-add-a-chat-service-is-it-better-to-use-and-ec2-or-lambda
[76] CloudThat — Scalable Real Time Communication Using AWS WebSocket APIs and AWS Lambda: https://www.cloudthat.com/resources/blog/scalable-real-time-communication-using-aws-websocket-apis-and-aws-lambda
[77] Google Cloud Docs — Building a WebSocket Chat service for Cloud Run: https://docs.cloud.google.com/run/docs/tutorials/websockets
[78] Azure Pricing — Azure Web PubSub Service: https://azure.microsoft.com/en-us/pricing/details/web-pubsub
[79] Ably — Amazon API Gateway pricing: What you need to know: https://ably.com/topic/amazon-api-gateway-pricing
[80] Hussein Nasser — How Discord Stores Trillions of Messages (YouTube): https://www.youtube.com/watch?v=xynXjChKkJc
