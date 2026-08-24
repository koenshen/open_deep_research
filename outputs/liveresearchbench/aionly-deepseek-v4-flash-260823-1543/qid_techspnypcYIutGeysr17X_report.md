# Designing a Highly Available, Horizontally Scalable Chat Application

## Introduction

This report provides a beginner-friendly, comprehensive design for a chat application that supports millions of concurrent users. The design addresses message delivery guarantees, typing indicators, message history, media sharing, 1:1 and group chats, and end-to-end encryption. The audience is junior developers, so each concept is explained with clear language and real-world trade-offs before diving into technical depth.

The design is built around four major pillars:

1. **Core Architecture Components** — messaging layer, storage layer, and real-time event handling
2. **Scalability Mechanisms** — sharding, partitioning, load balancing, horizontal scaling
3. **High Availability & Fault Tolerance** — redundancy, replication, failover, disaster recovery, and the exactly-once delivery question
4. **Security & Encryption Design** — TLS, encryption at rest, and end-to-end encryption architecture

The report concludes with a database selection comparison (relational vs. NoSQL vs. distributed databases) evaluated across scalability, latency, and consistency, with recommendations for which database types fit which parts of the system.

---

## 1. Core Architecture Components

A chat system at scale can be decomposed into several layers, each with a distinct responsibility. The key insight for beginners is this: **separate the things that are stateless (easy to scale) from the things that are stateful (harder to scale)**.

### 1.1 The Stateless Chat/API Gateway Layer

The chat/API gateway is the **entry point** for all clients. It handles authentication, REST/HTTP operations (fetching history, uploading media, profile updates), and routes messages into the system.

This layer should be **stateless** — meaning each instance stores no per-user data in local memory. Every request carries everything the server needs (auth token, message content). Because gateway instances are stateless, you can run any number of them behind a load balancer and freely add/remove instances. The AWS Elastic Load Balancing documentation explains the model: "Elastic Load Balancing automatically distributes your incoming traffic across multiple targets... It monitors the health of its registered targets, and routes traffic only to the healthy targets" [1].

For real-time communication, this layer also handles WebSocket connections. AWS describes WebSocket APIs as "bidirectional. A client can send messages to a service, and services can independently send messages to clients. WebSocket APIs are often used in real-time applications such as chat applications, collaboration platforms, multiplayer games, and financial trading platforms" [2]. The backend "can send callback messages to connected clients" [3].

### 1.2 The Real-Time Event Handling Layer (WebSocket Connection Servers)

This layer consists of servers that maintain persistent, long-lived WebSocket connections with clients and fan out real-time events (new messages, typing indicators, presence updates) to them.

This is a **stateful service** — each server holds an open TCP socket plus in-memory connection state (user ID, connection ID, subscriptions). The core difficulty: if a client's request lands on a different server than the one holding its socket, that server cannot deliver the event. Two standard solutions exist:

- **Sticky sessions (session persistence):** The load balancer remembers which backend server handled the client's first connection and routes all subsequent requests from that client to the same server. NGINX supports this with `ip_hash` or the `hash` directive [4].
- **Application-controlled routing (consistent hashing):** The gateway computes which connection server should own a given user (e.g., `hash(user_id)`) and routes that user's WebSocket connection to that specific server. This is covered in detail in Section 2.3.

When a connection server fails, all its sockets die; clients must reconnect. Consistent hashing minimizes how many users are remapped when a server fails or is added.

### 1.3 The Publish-Subscribe / Message Broker Layer

The broker layer decouples message producers (the gateway) from message consumers (the connection servers). It is the "nervous system" of the chat application.

**Apache Kafka** is the most proven option for durable, ordered message streaming. Kafka is "a distributed streaming platform" with three key capabilities: "(1) publish and subscribe to streams of records, (2) store streams of records in a fault-tolerant way, (3) process streams of records as they occur" [5]. Kafka runs as a cluster, stores records in topics, and provides four core APIs: Producer, Consumer, Streams, and Connect [6].

The key concept for chat is the **partition**. "Each topic is a partitioned log where each partition is an ordered, immutable, continually-appended sequence of records. Each record gets an offset" [5]. "Kafka only provides a total order over records within a partition, not between different partitions in a topic" [5]. This maps perfectly to chat: using `conversation_id` as the message key ensures all messages of one conversation go to the same partition, so the broker preserves per-conversation ordering. "Events with the same key go to the same partition, guaranteeing order" [7].

**Consumer groups** enable parallel consumption while preserving order. "Kafka balances partitions among members so each partition is assigned to exactly one consumer per group" [8]. To scale consumption, add more consumers — but "there cannot be more consumer instances than partitions" [9]. This means you must design your partition count with your maximum parallelism in mind.

**Redis Pub/Sub** is a lightweight alternative for the fan-out layer, but it has a critical caveat: "Redis' Pub/Sub exhibits at-most-once message delivery semantics... If the subscriber is unable to handle the message (for example, due to an error or a network disconnect) the message is forever lost" [10]. For stronger guarantees, Redis Streams is recommended, as it "supports both at-most-once and at-least-once delivery" [10].

### 1.4 The Storage Layer

The storage layer holds message history, user presence metadata, media metadata, and user profiles. Different data types have different requirements, so a chat system typically uses multiple storage engines:

- **Message history:** A distributed database (Cassandra or DynamoDB) partitioned by conversation ID with a time-based sort key. This enables the classic "fetch last N messages for a conversation" range query on a single partition.
- **User presence/online status:** An in-memory store (Redis) with TTL-based keys that expire automatically when a user's heartbeat times out.
- **Media blobs:** Object storage (S3) with a database index holding metadata (object key, uploader, timestamp, content type).
- **User profiles and social graph:** A relational database (PostgreSQL) for joins, referential integrity, and transactions.

Section 5 provides a full database comparison with per-component recommendations.

### 1.5 How the Pieces Fit Together: A Message's Journey

1. Alice sends a message via WebSocket to a connection server.
2. The connection server validates Alice's auth token and publishes the message to Kafka with key = `conversation_id`.
3. A message processor consumer reads from Kafka, assigns a sequence number, writes the message to the message-history database (DynamoDB/Cassandra), and publishes a "new message" event to the pub/sub layer (or a per-conversation Kafka topic).
4. Connection servers subscribed to that conversation receive the event and push it to all connected members' WebSockets.
5. If Bob is offline, the message is already durably stored in the history database; Bob fetches it on reconnect.

This design keeps the hot path (real-time delivery) separate from the durable path (history), which is the key to scale.

---

## 2. Scalability Mechanisms

### 2.1 Stateless vs. Stateful Scaling

- **Stateless services** (chat/API gateway, REST endpoints, consumers after the broker) scale freely by adding instances behind a load balancer. NGINX, a common Layer 7 load balancer, "was first created to solve the C10K problem (serving 10,000 simultaneous connections on a single web server)" and defaults to round-robin load balancing [4][11].
- **Stateful services** (WebSocket connection servers, Kafka partitions, Redis slots) each own specific state. Scaling requires either sticky sessions/consistent hashing at the edge, or explicit partitioning with rebalancing.

### 2.2 Sharding/Partitioning Chat Data

There are two primary sharding strategies for chat data:

**By conversation/group ID:** All messages of a group live in one shard/partition. This enables per-conversation ordering and efficient group history reads. In DynamoDB, use `conversation_id` as partition key and `message_timestamp` as sort key — "all items with the same partition key value are stored together in sorted order by sort key value" [12]. In Kafka, use `conversation_id` as the message key so "events with the same key go to the same partition, guaranteeing order" [7].

**By user ID:** Each user's messages, presence, and subscriptions live in one shard/partition. This is useful for per-user mailboxes or event feeds (e.g., a "feed" of all conversations the user participates in).

**Write sharding for hot keys:** A very popular conversation can exceed a single partition's write budget. DynamoDB's official guidance recommends "write sharding" — appending a random number or a calculated suffix to the partition key to spread writes across partitions [13]. The trade-off: you must query all suffixes and merge results to read all items. The calculated-suffix approach (e.g., `hash(order_id) % 200`) allows you to compute the exact key on read, avoiding the merge cost [13].

### 2.3 Load Balancing and Consistent Hashing

- **Round robin** distributes requests evenly but is "unaware of which server holds a given user's WebSocket; a client may be routed to a different server on each request" — which breaks long-lived connections.
- **Consistent hashing** maps keys to positions on a hash ring, and each server owns an arc of the ring. A key always maps to the same server as long as the server set is unchanged. When a server fails or is added, only the keys in the affected arcs move.

The canonical primary source for consistent hashing is the original Amazon Dynamo paper, which describes "consistent hashing with 'virtual nodes' (multiple tokens per node) to distribute load, handle heterogeneity, and disperse load evenly during failures" [14]. Virtual nodes mean each physical server pretends to be several positions on the hash ring, so load is spread more evenly and failures disperse keys among many successors.

**Why this matters for WebSockets:** Without consistent hashing, `hash(user_id) % N` remaps almost all users to different servers when one fails, causing a thundering herd of reconnects. With consistent hashing, only the failed server's users remap.

Redis Cluster uses a fixed 16384-slot ring, which is consistent hashing with a fixed granularity. The `CLUSTER KEYSLOT` command "returns an integer identifying the hash slot the specified key hashes to" [15]. You can use hash tags to force related keys into the same slot (e.g., `conversation:{conversation_id}:messages` and `conversation:{conversation_id}:presence`), ensuring all related data lives on one node [16].

### 2.4 Fan-Out Approaches for Group Chats

**Option A: Write-amplification fan-out (per-recipient queues)** — for small groups (e.g., ≤ 50 members). The message is written once to the source-of-truth conversation history, then the system writes one copy (or one event) into each recipient's feed/queue. Trade-off: N writes per message, but each recipient reads only their own queue. This matches Kafka's consumer-group model: "each message is delivered to one consumer instance per subscribing group" [5].

**Option B: Read-amplification on-demand fetching (for large groups)** — for groups with thousands of members. The message is written once to the conversation topic/table. Members' clients fetch history on demand (pagination via range query on the sort key), and the connection servers use pub/sub or a lightweight per-room topic for the "new message" notification. Trade-off: many members re-read the same storage, but the read is cheap because it is a fetch by partition key + sort key range (locality).

**Hybrid:** use pub/sub notification (at-most-once) for liveness + durable history for replay. Redis's official production guidance recommends: "write the durable record... to its primary store, then PUBLISH a notification so live consumers can pick it up immediately" [17].

### 2.5 Why This Architecture Scales Horizontally

1. The stateless chat/API gateway scales freely behind a Layer-7 load balancer.
2. The WebSocket connection servers scale via consistent hashing (pinning `hash(user_id)` to a server), minimizing reconnect storms.
3. The pub/sub broker decouples producers from consumers: Kafka consumers in a group scale up to the partition count with per-partition ordering preserved [8]; Redis Streams consumer groups scale within a group with PEL-based at-least-once delivery [18].
4. The storage layer shards by user/conversation ID, with write sharding for hot keys [13].
5. Media scales out of the hot path entirely via S3 presigned URLs: "if you receive a presigned URL to upload an object, you can upload an object only if the creator of the URL has the necessary permissions" [19], meaning clients upload directly to S3 without the gateway proxying bytes.

---

## 3. High Availability & Fault Tolerance

### 3.1 The Exactly-Once Delivery Question

The requirement for "exactly-once delivery" must be addressed carefully. As the Confluent documentation on Kafka delivery semantics explains, there are three delivery semantics:

- **At-most-once:** messages are delivered once but may be lost in a system failure
- **At-least-once:** messages are never lost but may be delivered more than once
- **Exactly-once:** each message is delivered once and only once, never lost or read twice [20]

**Why true exactly-once is challenging:** A producer cannot distinguish "request lost" from "response lost." If it retries, it risks duplication; if it doesn't retry, it risks loss. Three failure scenarios must be handled: broker failure, producer-to-broker RPC failure (which can cause duplicate writes), and client failure [21]. The Confluent engineering blog states it clearly: exactly-once "requires a cooperation between the messaging system itself and the application producing and consuming the messages" [21].

**The practical engineering answer: at-least-once + idempotency + deduplication.** This is the industry-standard approach, and it is explicitly documented by AWS for SQS: "Applications must be designed to be idempotent (capable of processing the same message more than once without adverse effects)" [22].

The mitigation pattern has four parts:

1. **Client-generated idempotency keys:** the sender generates a unique message ID (e.g., UUID) and attaches it to every message.
2. **Server-side deduplication tables:** a dedupe table keyed by message ID with an atomic conditional insert (e.g., `attribute_not_exists` in DynamoDB, or a unique constraint in PostgreSQL) so concurrent duplicates can't both pass; the second arrival is a no-op [23].
3. **Storing message status as an idempotent operation:** "mark message X as delivered" executed twice has the same effect as once.
4. **Client and server ACK/NACK with retries:** the receiver ACKs only after durable processing; on failure it NACKs and the sender retries (with backoff); a crash between processing and ACK causes redelivery, which is precisely why dedup tables must be consulted before re-executing business logic [22].

**How Kafka implements exactly-once (for reference):** Kafka provides three mechanisms: (1) **Idempotent producers** (`enable.idempotence=true`, default since Kafka 3.0) — each producer gets a unique Producer ID and per-partition sequence numbers; the broker deduplicates retries by tracking (PID, sequence number) pairs, "similar to TCP" [21][24]. (2) **Transactions** (Kafka 0.11+) — atomic writes across multiple partitions via the transactions API, with a persistent `transactional.id` that fences zombie producers across restarts [21]. (3) **Exactly-once stream processing** — via Kafka Streams with `processing.guarantee=exactly_once`, which coordinates offsets, state snapshots, and outputs in a single transaction [21].

**Critical limitations:** Kafka's exactly-once guarantees "apply only within Kafka Streams' internal processing; external RPC calls or custom client operations aren't covered" [21]. And "The sink must be either idempotent (safely handling duplicate writes like Cassandra or key-value stores) or transactional (participating in two-phase commit like PostgreSQL or MySQL)" [25]. Even with Kafka transactions, the application must be idempotent at the boundary.

**Bottom line for the design:** True exactly-once end-to-end (from client A to client B's screen) is unachievable in a distributed system. The correct target is: at-least-once delivery from the broker, plus idempotency keys and a server-side dedupe table so that duplicates are harmless and the user-visible effect is exactly-once.

### 3.2 Replication and Quorum Concepts

**Kafka replication:** "For a topic with replication factor N, up to N-1 server failures are tolerated without losing committed records" [5]. The common production setting is a replication factor of 3 [7]. Each partition has one leader (all reads and writes) and zero or more followers that replicate. A node is "alive" if it maintains its session with the controller and, if a follower, doesn't fall too far behind — these are the **in-sync replicas (ISR)**. "Kafka guarantees that a committed message will not be lost, as long as there is at least one in-sync replica alive at all times" [26].

The availability matrix for `acks=all` with RF=3: with `min.insync.replicas=1`, you tolerate 2 broker failures (default; low durability); with `min.insync.replicas=2`, you tolerate 1 broker failure (recommended for production); with `min.insync.replicas=3`, you tolerate 0 failures (maximum durability, no fault tolerance) [27]. General formula: with `replication.factor=N` and `min.insync.replicas=M`, tolerate `N-M` broker failures [27].

**Cassandra replication:** "The total number of replicas for a keyspace across a Cassandra cluster is referred to as the keyspace's replication factor" [28]. Production default RF=3. "All replicas are equally important — no primary/master" [28]. Consistency levels are tunable per query: "Cassandra offers consistency levels including ONE, TWO, THREE, QUORUM (majority n/2+1), ALL, LOCAL_QUORUM, EACH_QUORUM, LOCAL_ONE, and ANY" [29]. The strong-consistency formula is **W + R > RF** — e.g., QUORUM writes + QUORUM reads with RF=3 guarantees at least one replica participates in both, so writes are visible to reads [29][30].

**PostgreSQL replication:** PostgreSQL uses leader-based replication. In synchronous replication, "the primary will wait for any or all replicas (based on synchronous replication mode) to confirm that they received and wrote the data" before acknowledging the commit [31]. Levels of `synchronous_commit` range from `off` (no wait) to `remote_apply` (waits for the transaction to be applied on the replica) [31]. Risk: "With a single synchronous replica that is unavailable, the primary will hang indefinitely. To avoid this, use at least two replicas with FIRST or ANY options" [31].

### 3.3 Failover and Leader Election

**Raft consensus** is the most understandable consensus algorithm and is the foundation for etcd, Kubernetes, and Kafka's KRaft mode. Raft works by electing a distinguished leader responsible for managing the replicated log [32]. Key mechanics:

- Server states: **leader, follower, or candidate**; time divided into **terms**, each beginning with an election [32].
- Followers become candidates after an election timeout (randomized 150–300 ms), increment the term, vote for themselves, request votes; a candidate wins with a **majority** of votes [32][33].
- "A log entry is committed once replicated on a majority of servers" [32].
- Raft guarantees: at most one leader per term, leader append-only, log matching, leader completeness, state machine safety [32].

**ZooKeeper and etcd patterns:** ZooKeeper uses ephemeral sequential znodes (lowest number is leader; ephemeral nodes auto-delete on crash) [34]. etcd with Raft uses a **lease** (time-limited lock) with compare-and-swap; a crash causes lease expiration (~10 s) and re-election [34]. The golden rule: "at any point in time, at most one node believes it is the leader. Violating this — called 'split brain' — leads to duplicate processing, data corruption, or worse" [34].

**Kafka leader election:** "On leader crash, controller elects a new leader from current ISR to maintain consistency" [35]. With `unclean.leader.election.enable=false` (the default since 0.11.0.0), Kafka waits for an ISR replica to return rather than electing an out-of-sync replica — favoring consistency over availability [26].

**WebSocket connection server failover:** When a connection server dies, all its sockets die; clients reconnect. The shared-state pattern stores connection and session state externally (Redis, a database): "Instead of relying on clients always reaching the same server, store connection and session state externally (Redis, a database, or another shared store). This way, any server can handle any reconnecting client and restore its state from the shared store" [36]. The pub/sub backplane ensures any server can deliver to any client: "With Redis, a WebSocket server instance receives a message from a client, instead of only broadcasting it to its local clients, it also publishes this message to a specific Redis channel. All other WebSocket server instances, subscribed to the same Redis channel, will receive this message and then broadcast it to their respective connected clients" [37].

**Load balancer health checks:** "Each load balancer node routes requests only to the healthy targets in the enabled Availability Zones" [38]. If all targets fail health checks, the load balancer **fails open** and routes to all targets regardless of health status [38][39]. ALB health check settings: interval (default 30 s), timeout (default 5 s), healthy threshold (default 5), unhealthy threshold (default 2), success codes (default 200) [38]. NLB health checks use a "consensus mechanism to determine target health" [39].

### 3.4 Disaster Recovery: RPO and RTO

**RPO (Recovery Point Objective)** = data loss tolerance (time); **RTO (Recovery Time Objective)** = downtime tolerance (time). "If RPO = 5 minutes and RTO = 2 hours: You have backups every 5 minutes → at most, you lose 5 minutes of data. Your system must be restored within 2 hours → downtime cannot exceed 2 hours" [40].

**PostgreSQL point-in-time recovery (PITR):** "At all times, PostgreSQL maintains a write ahead log (WAL) in the `pg_wal/` subdirectory of the cluster's data directory. The log records every change made to the database's data files" [41]. Continuous archiving combines a file-system-level backup with backup of WAL files, enabling recovery to any point in time. "Each archive recovery creates a new timeline to distinguish WAL records" [41]. The formula: **Base Backup + Continuous WAL Archiving = PITR** [42].

**DynamoDB backups:** "Amazon DynamoDB point-in-time recovery (PITR) provides automatic continuous backups of your DynamoDB table data... up to 35 days of recovery points at a per second granularity" [43]. "Restores can be made to any point in time from five minutes before the current time up to the configured recovery period" [43]. PITR always restores to a new table [44]. On-demand backups provide full snapshots for long-term retention [45].

**Cross-region replication (DynamoDB global tables):** Multi-Region eventual consistency (MREC) is the default, "replicating changes typically within a second"; Multi-Region strong consistency (MRSC) "synchronously replicates changes to another Region before the write returns, and strongly consistent read operations on any replica always return the latest version of an item" [46]. MREC supports RPO/RTO measured in seconds; MRSC supports RPO of zero with higher latency [46].

The AWS disaster recovery whitepaper defines four strategy tiers: Backup and Restore (simplest, lowest cost), Pilot Light (data replicated, core infra always on), Warm Standby (scaled-down fully functional copy), and Multi-site Active/Active (workload runs simultaneously in multiple Regions) [47].

### 3.5 Consistency Approaches for Chat

The CAP theorem states that a distributed data store can provide at most two of three guarantees: consistency, availability, and partition tolerance [48]. The formal proof (Gilbert & Lynch, 2002) shows it is "impossible in the asynchronous network model to implement a read/write data object that guarantees availability, atomic consistency, in all fair executions (including those in which messages are lost)" [49]. Brewer's 2012 clarification: "designers only need to sacrifice consistency or availability in the presence of partitions, and partition management/recovery techniques exist" [50].

**Why chat systems choose availability:** Partitions are unavoidable. During a partition, a chat system should keep accepting messages (availability) and reconcile via per-conversation ordering when the partition heals, rather than erroring out. "Cassandra is by default an AP (Available Partition-tolerant) database, hence it is 'always on'. But you can indeed configure the consistency on a per-query basis" [51].

**Per-conversation ordering** is preserved via Kafka partitions (key = `conversation_id`) or database sequence numbers. Each message carries a monotonically increasing sequence number within the conversation; readers sort by it, and reconnecting clients do catch-up ("give me everything after seq N") — the same mechanism that powers WebSocket resume after failover [36]. This sacrifices cross-conversation global ordering (irrelevant for chat) while keeping per-conversation order strong.

---

## 4. Security & Encryption Design

### 4.1 Protecting Messages in Transit: TLS 1.3

**TLS (Transport Layer Security)** is "a cryptographic protocol designed to provide communications security over a computer network," providing privacy (confidentiality), integrity, and authenticity [52]. TLS 1.3 (RFC 8446) is the current version, published by the IETF in August 2018 [53][54].

Key security improvements in TLS 1.3:

- Removed RSA key exchange (which lacked forward secrecy and was vulnerable to Bleichenbacher's attack); TLS 1.3 uses only ephemeral Diffie-Hellman [54].
- Only allows AEAD (authenticated encryption with associated data) ciphers, which combine encryption and integrity in one operation [54].
- The server signs the entire handshake transcript, preventing downgrade attacks (FREAK, LogJam, CurveSwap) [54].
- Mandates perfect forward secrecy via ephemeral keys [52].
- Reduces handshake latency from 2 round-trips to 1 (1-RTT), with optional 0-RTT resumption for clients that have connected before [54][55].

For chat, TLS secures both HTTPS API traffic and WebSocket traffic. **WebSocket Secure (wss://)** is the WebSocket protocol running over TLS. All traffic between clients and servers should use TLS 1.3. NIST SP 800-52 specifies how TLS is to be used in government applications [56].

### 4.2 Protecting Messages at Rest: Encryption and Envelope Encryption

**Amazon S3 server-side encryption (SSE):** "All Amazon S3 buckets have encryption configured by default, and all new objects that are uploaded to an S3 bucket are automatically encrypted at rest" [57]. Since January 5, 2023, all new object uploads are automatically encrypted at no additional cost [58]. S3 uses "256-bit Advanced Encryption Standard Galois/Counter Mode (AES-GCM)" and encrypts "each object with a unique key, and additionally encrypts the key itself with a key that is rotated regularly" [58]. Note: "Server-side encryption encrypts only the object data, not the object metadata" [58].

**Envelope encryption** is the pattern used by AWS KMS: "the practice of encrypting plaintext data with a data key, then encrypting that data key under another key, with the top-level key (root key) remaining in plaintext" [59]. The workflow:

1. Client/S3 requests a plaintext data key and an encrypted copy.
2. AWS KMS generates and encrypts the data key.
3. Data is encrypted with the plaintext data key; the plaintext key is removed from memory.
4. The encrypted data key is stored alongside the encrypted data [60].

**Why envelope encryption matters for chat:** If you need to encrypt message content in a database or media in S3, you can use a KMS key to generate data keys; the data keys encrypt the data. The KMS key never leaves FIPS 140-3 validated hardware security modules — "Your plaintext KMS keys never leave the HSMs, are never written to disk, and are only ever used in the volatile memory of the HSMs" [61]. This gives you central key management, rotation, and auditing (via CloudTrail).

### 4.3 End-to-End Encryption (E2EE) Architecture

End-to-end encryption ensures that messages are readable only by the communicating endpoints, "not by any servers involved in delivering messages" [62]. The Signal Protocol is "the gold standard for end-to-end encrypted messaging, powering applications like WhatsApp, Signal, and Facebook Messenger" [63].

#### The Signal Protocol (Conceptual Level)

The Signal Protocol provides: confidentiality, integrity, authentication, forward secrecy (compromised past keys don't expose past messages), post-compromise security (compromised keys don't expose future messages), and asynchronicity (works even when the recipient is offline) [64]. The two core building blocks are:

**X3DH (Extended Triple Diffie-Hellman) Key Agreement:** "X3DH establishes a shared secret key between two parties who mutually authenticate each other based on public keys. X3DH provides forward secrecy and cryptographic deniability" [65]. It is designed for asynchronous settings where Bob is offline but has published information to a server.

The protocol uses five public keys: Alice's identity key (IKA), Alice's ephemeral key (EKA), Bob's identity key (IKB), Bob's signed prekey (SPKB), and Bob's one-time prekey (OPKB) [65]. The DH calculations: SK = KDF(DH1 || DH2 || DH3), where DH1 = DH(IKA, SPKB) and DH2 = DH(EKA, IKB) provide mutual authentication, while DH3 = DH(EKA, SPKB) provides forward secrecy. With a one-time prekey, DH4 = DH(EKA, OPKB) is added [65].

The process: (1) Bob publishes his identity key and prekeys to a server; (2) Alice fetches a prekey bundle, verifies the prekey signature, and sends an initial message; (3) Bob receives and processes the initial message, deleting used one-time prekey private keys for forward secrecy [65]. A malicious server "can only refuse delivery or withhold one-time prekeys" — it cannot learn the session key or message content [65].

**The Double Ratchet Algorithm:** After the initial key agreement, the Double Ratchet derives new keys for every message. "The parties derive new keys for every Double Ratchet message so that earlier keys cannot be calculated from later ones, and parties send DH public values mixed into derived keys so later keys can't be calculated from earlier ones — offering protection in case of key compromise" [66].

It combines two ratchets: a **symmetric-key ratchet** (KDF chains) providing forward secrecy (each message gets a unique message key derived from a chain key; old chain keys are deleted), and a **Diffie-Hellman ratchet** providing break-in recovery (parties generate new DH key pairs and mix the DH outputs into the root chain, so if a chain key is compromised at time n, an attacker cannot produce future keys) [66][67]. Out-of-order messages are handled via headers containing message numbers (N and PN), with skipped message keys stored for later-arriving messages [67].

**Prekeys:** Prekeys are one-time ephemeral public keys uploaded in advance to a central server. "Bob publishes a set of one-time prekeys (plus identity key and signed prekey) to the server; Alice fetches a prekey bundle to initiate a session; Bob deletes used one-time prekey private keys for forward secrecy" [63][65].

#### Group Chats: Sender Keys vs. MLS

**Sender Keys (Signal's approach for groups):** Each user owns a sender key (public signature key + symmetric chain key) shared with all group members via pairwise Double Ratchet sessions. Each sender's messages are encrypted with their own sender key. This supports concurrency and message reordering but has a scaling problem: "Each user has their own symmetric key, meaning O(n) secret material is maintained at all times" [68]. For a group of 100,000 members, a key update requires ~100,000 encryption operations [69].

**Messaging Layer Security (MLS, RFC 9420):** MLS is the IETF-standardized alternative, designed for "efficient asynchronous group key establishment with forward secrecy (FS) and post-compromise security (PCS) for groups in size ranging from two to thousands" [70]. It uses a **binary ratchet tree** where participants know private key material for all nodes from their leaf up to the root, enabling O(log n) operations instead of O(n) [69]. "If you have a group with 100,000 members you have 100,000 encryption operations and ciphertext uploads each time you want to update your key material. If you use something like MLS... it scales logarithmically and so you end up with just 17 operations" [69].

MLS also provides **group integrity**: "all members cryptographically agree on group state/membership, making it impossible for a third party to add members without existing members being aware" [71]. MLS was officially published as RFC 9420 on July 19, 2023, and is deployed by Cisco Webex, RingCentral, Google Messages, and Apple Messages [72][73].

#### How E2EE Affects Server Design

- **Server stores only ciphertext:** The central server's role is storing/distributing pre-key bundles, relaying messages, and enabling asynchronous messaging — it cannot decrypt or read message content [63][65].
- **Metadata remains visible:** "The protocol does not prevent retention of metadata about when and with whom users communicate; Signal's servers keep only recipient identifiers as long as needed to transmit messages" [64]. The "sealed sender" feature conceals the sender's identifier from servers [74].
- **Search and moderation become harder:** Because the server cannot read messages, it cannot offer server-side content search, cannot scan for spam/abuse content, and cannot moderate message content [65].
- **Key backup is a challenge:** "New devices are new clients without history access; history restoration outside MLS may reduce FS/PCS guarantees" [75]. Signal's Secure Backups use "a 64-character recovery key generated on the user's device. This key is never shared with Signal's servers and is the only way to unlock a backup. Losing it means losing access to your backup permanently" [76].

#### Recommendation for this design

For a chat application that treats E2EE as a "desirable feature," the pragmatic approach:

1. **Always use TLS 1.3** for all traffic in transit and SSE-KMS/envelope encryption for data at rest — this protects against network and infrastructure attackers.
2. **For E2EE, integrate the Signal Protocol** for 1:1 chats (using libsignal) — it is battle-tested with proven forward secrecy and post-compromise security.
3. **For group chats, use MLS (RFC 9420)** — the O(log n) scaling makes it the only practical choice for large groups, and it is now an IETF standard with multiple production implementations (OpenMLS, mls-rs, MLS++).
4. **Acknowledge the trade-offs:** E2EE means no server-side search or moderation, metadata is still visible to the server, and key backup/device management requires careful UX design (recovery keys, secure backup).

---

## 5. Database Selection Comparison

This section compares three database categories — relational databases, NoSQL key-value/document stores, and distributed databases — across three axes: **scalability, latency, and consistency**. It then recommends which database types are appropriate for which parts of the chat system.

### 5.1 Comparison Across Three Axes

| Axis | Relational (PostgreSQL) | NoSQL KV/Document (Redis) | Distributed (Cassandra/DynamoDB) |
|---|---|---|---|
| **Scalability** | Vertical scale + read replicas via streaming/log-shipping replication; single-writer primary; declarative table partitioning for large tables [77][78] | In-memory key-value; horizontal scaling via clustering/sharding (Redis Cluster shards by key-slot algorithm); TTL-based ephemeral keys [10][79] | Linear horizontal scale-out on commodity hardware (Cassandra token ring consistent hashing, vnodes; DynamoDB partitions at 3000 RCU/1000 WCU per partition); multi-master replication [29][80] |
| **Latency** | Disk-backed, transactional; MVCC avoids read/write blocking; benefits from external cache tier (e.g., Redis) for hot data [81] | Sub-millisecond in-memory; Pub/Sub ~1ms; TTL-based ephemeral keys [10][82] | Single-partition fast latency at any scale (Cassandra); DAX write-through cache reduces DynamoDB read latency; DAX+DynamoDB consistent within 10–100ms under normal conditions [29][83][84] |
| **Consistency** | Full ACID; MVCC snapshots; Serializable Snapshot Isolation; strong consistency on primary; replicas eventually consistent; synchronous replication optional [81][85] | At-most-once Pub/Sub delivery; no strong cross-region guarantees; TTL eviction [10] | Tunable: eventual (ONE, ANY), quorum (QUORUM, LOCAL_QUORUM, EACH_QUORUM), strong (ALL, SERIAL); W+R>RF; DynamoDB: eventually consistent (default, half cost) vs strongly consistent (ConsistentRead=true, tables+LSI only); ACID transactions available [29][86][87] |

### 5.2 Detailed Analysis

#### Relational Databases (PostgreSQL)

**Scalability:** PostgreSQL's official documentation describes streaming replication (primary/standby), synchronous replication, logical replication, and declarative table partitioning [77][78]. Hot standby servers accept read-only queries, enabling read scaling [85]. However, PostgreSQL is not a natively sharded/distributed database — horizontal scaling requires extensions or middleware, and writes are concentrated on a single primary.

**Latency:** Single-node reads are fast for indexed point queries (MVCC snapshot reads with no reader-writer blocking) [81]. Partition pruning reduces I/O for very large tables [78]. There is no built-in distributed cache layer — a chat system typically adds Redis in front.

**Consistency:** PostgreSQL provides full ACID transactions. MVCC means "reading never blocks writing and writing never blocks reading" [81]. The strictest isolation level is Serializable Snapshot Isolation [81]. Synchronous replication offers 2-safe replication where each commit waits for confirmation the commit was written to WAL on disk of both primary and standby [77].

#### NoSQL Key-Value/Document Stores (Redis, MongoDB)

**Redis scalability:** Redis is an in-memory data store. Clustering (Redis Cluster) shards keys across nodes with hash slots; sharded Pub/Sub (Redis 7.0+) "assigns shard channels to slots using the same key-slot algorithm... limiting message propagation to within a shard, enabling horizontal scaling in cluster mode" [10].

**Redis latency:** In-memory operations are O(1), giving sub-millisecond latency — "latencies of 1 millisecond with appropriate message size, network conditions, and subscriber processing time" [82].

**Redis consistency:** "Redis' Pub/Sub exhibits at-most-once message delivery semantics... Once the message is sent by the Redis server, there's no chance of it being sent again" [10]. For stronger guarantees, Redis Streams is recommended [10].

**MongoDB** (as an alternative document store): MongoDB supports sharding via shard keys with hashed or ranged strategies, chunk-based balancing, and live resharding (MongoDB 5.0+) [88]. Consistency is tunable via read concern (`local`, `available`, `majority`, `linearizable`, `snapshot`) and write concern (`w:0`, `w:1`, `w:"majority"`) [89][90]. Multi-document ACID transactions are supported on sharded clusters [88]. MongoDB is classified as CP (single-master) [48].

#### Distributed Databases (Cassandra, DynamoDB)

**Cassandra scalability:** Cassandra "relies on Dynamo style: Dataset partitioning using consistent hashing, Multi-master replication using versioned data and tunable consistency, Distributed cluster membership and failure detection via a gossip protocol, Incremental scale-out on commodity hardware" [29]. Consistent hashing with a token ring means "unlike naive modulo hashing (where adding a node invalidates almost all mappings), consistent hashing only moves a small fraction of keys when nodes change" [29]. Vnodes (multiple tokens per physical node) provide balanced distribution and even query load [29].

**Cassandra latency:** "Fast single-partition latency at any scale" [29]. Reads/writes touch only the replicas that own the partition.

**Cassandra consistency:** Tunable per query. "Writes are always sent to all replicas; consistency level controls how many responses the coordinator waits for. Reads only target enough replicas to satisfy the consistency level. For overlapping replica sets, W + R > RF guarantees writes are visible to reads" [29]. QUORUM = (RF/2) + 1. LOCAL_QUORUM is "generally recommended for most production environments" [30][91].

**DynamoDB scalability:** Fully managed; "no limits on data size or request throughput per table" [92]. Every partition is designed to deliver "a maximum capacity of 3,000 read units per second and 1,000 write units per second" [80]. Applications should be designed for "uniform activity across all partition keys" [80].

**DynamoDB latency:** Single-digit millisecond latency at any scale [93]. **DAX (DynamoDB Accelerator)** is a write-through caching service that provides microsecond-to-millisecond reads [83]. Under normal working conditions, "both DynamoDB and DAX will be consistent within a 10-100ms" [84].

**DynamoDB consistency:** Two read options for tables and LSIs: eventually consistent (default; half cost) and strongly consistent (via `ConsistentRead=true`). "When your application writes data to a DynamoDB table and receives an HTTP 200 response (OK), that means the write completed successfully and has been durably persisted" [86]. All reads from GSIs and streams are eventually consistent [86]. DynamoDB supports ACID transactions across multiple items and tables [93].

### 5.3 Per-Component Recommendations

#### (1) Message History Storage — Cassandra or DynamoDB

**Why:** Message history is a write-heavy, append-only workload partitioned by conversation ID with a time-based clustering/sort key. Both Cassandra and DynamoDB are designed for this: a partition per conversation (partition key = `conversation_id`), with a time-based clustering key (Cassandra) or sort key (DynamoDB) so messages are stored in order and retrievable as a contiguous range.

- Cassandra: "fast single-partition latency at any scale" [29]; TimeWindowCompactionStrategy (TWCS) suits time-ordered appends and automatically compacts/drops old SSTables for TTL-based message retention [94].
- DynamoDB: composite primary key (partition key + sort key) maps directly; "all items with the same partition key value are stored together in sorted order by sort key value" [12]; TTL for message retention; DAX for hot-history caching [83].

**Trade-offs:** Both sacrifice ad-hoc queries and cross-partition joins — you must model access patterns up front. Eventual consistency is the default; strong reads cost 2× in DynamoDB; QUORUM in Cassandra requires coordinating a majority [29][86]. DynamoDB is fully managed (no ops) but vendor-locked; Cassandra requires cluster operations expertise but offers multi-datacenter replication and no vendor lock-in [29].

**Hot conversation concern:** A very popular conversation can exceed a single partition's write budget (DynamoDB: 1,000 write units/s per partition). Mitigate with write sharding [13] or design for uniform activity [80].

#### (2) User Presence and Online Status Metadata — Redis

**Why:** Presence/status is ephemeral, high-frequency, low-value-if-lost data. Redis TTL-based keys ("A key with an associated timeout is often said to be *volatile* in Redis terminology") [95] give automatic expiration of stale presence. O(1) reads/writes provide sub-millisecond updates [82]. Redis Pub/Sub provides the broadcast mechanism for presence events [10].

**Trade-offs:** In-memory — data lost on restart unless persistence configured; memory capacity bounds the number of tracked users; at-most-once Pub/Sub delivery means a missed presence event is corrected by the next heartbeat [10]. For "last seen" that must survive restarts, write through to a durable store.

#### (3) Media Metadata and Blobs — Object Storage (S3) + Database Index

**Why:** Media blobs (images, videos, voice messages) are binary content best stored in object storage. S3 encrypts all new objects at rest by default (SSE-S3 AES-GCM, unique-per-object keys) [57][58]. A database (DynamoDB or PostgreSQL) holds the metadata index (object key, uploader, timestamp, content type, dimensions, duration) — S3 server-side encryption "encrypts only the object data, not the object metadata" [58], so sensitive metadata should live in the database index.

**Presigned URLs for uploads/downloads:** "By default, all Amazon S3 objects are private... However, the object owner may share objects with others by creating a presigned URL" that "grants time-limited permission to download objects using the security credentials of the AWS user who generated the URL" [96]. This keeps media out of the chat gateway hot path — clients upload directly to S3.

**Trade-offs:** Two systems to manage (object store + index) with consistency between them (write S3 first, then index; handle failures/retries/orphan cleanup); SSE-KMS adds KMS API costs but gives key control/auditing [60]; CDN (CloudFront) adds cache invalidation considerations.

#### (4) User Profiles, Friend and Contact Relationships — PostgreSQL

**Why:** Profile data and social graph need **joins** ("my friends' profiles"), **referential integrity** (no orphaned friendship rows), and **transactions** (adding a friend + creating the reverse edge atomically). PostgreSQL provides full ACID transactions, MVCC ("reading never blocks writing and writing never blocks reading") [81], and Serializable Snapshot Isolation [81]. This data is low-write, read-mostly, easily cached, and fits relational modeling.

**Trade-offs:** Single-writer primary (standbys are read-only) [77][85]; for very large write loads, scale reads with replicas and consider partitioning [78]. For a typical chat app, profile/contact data is low-volume and high-value, so strong consistency and joins matter more than horizontal write scaling.

#### (5) Ordering/Deduplication Tables

- **Per-conversation ordering:** Use Cassandra's clustering key / DynamoDB's sort key within a partition (e.g., a time-based or monotonic sort key per conversation) [29][12]. This is the chat norm — you only need per-conversation ordering, not global ordering.
- **Deduplication/idempotency:** Use a primary-key-based natural dedup in the history store (idempotent PUTs in DynamoDB/Cassandra), plus a short-TTL Redis dedup window for retry storms. DynamoDB conditional writes (`attribute_not_exists`) [23] and Cassandra lightweight transactions (`IF NOT EXISTS`, SERIAL/LOCAL_SERIAL consistency) [29][91] provide atomic compare-and-set semantics. PostgreSQL unique indexes give immediate, transactional dedup (`INSERT ... ON CONFLICT DO NOTHING`).

---

## 6. Conclusion

This design provides a complete blueprint for a highly available, horizontally scalable chat application. The key takeaways:

1. **Separate stateless from stateful layers.** The chat/API gateway is stateless and scales freely; WebSocket connection servers are stateful and scale via consistent hashing; the storage layer shards by user/conversation ID.

2. **Exactly-once delivery is a distributed-systems myth in its purest form.** The practical approach is at-least-once delivery from the broker plus idempotency keys and a server-side dedupe table so that duplicates are harmless and the user-visible effect is exactly-once. Kafka provides strong internal exactly-once mechanisms (idempotent producers, transactions), but the application boundary still requires idempotent design.

3. **Replication is the foundation of availability.** Kafka with RF=3 and `min.insync.replicas=2` tolerates one broker failure without data loss; Cassandra with RF=3 and QUORUM consistency tolerates one node failure; PostgreSQL with synchronous replication provides 2-safe commits at the cost of latency. Raft consensus (via etcd or KRaft) provides leader election and split-brain prevention.

4. **Chat systems choose availability over consistency during partitions** (CAP theorem), preserving per-conversation ordering via partition keys and sequence numbers, and reconciling with eventual consistency when the partition heals.

5. **Security is layered.** TLS 1.3 protects all traffic in transit; SSE-KMS/envelope encryption protects data at rest; and end-to-end encryption via the Signal Protocol (1:1) and MLS (groups) protects content from the server itself. E2EE has real trade-offs — no server-side search or moderation, visible metadata, and complex key backup — which must be accepted consciously.

6. **The database comparison shows no single winner.** Use a distributed database (Cassandra/DynamoDB) for message history, Redis for presence, S3 + database index for media, and PostgreSQL for profiles/social graph. Each tool is chosen for what it does best: horizontal write scaling, sub-millisecond ephemeral state, cheap blob storage, and relational integrity.

---

## Sources

[1] Elastic Load Balancing – Application Load Balancers: https://docs.aws.amazon.com/pdfs/elasticloadbalancing/latest/application/elb-ag.pdf

[2] API Gateway WebSocket APIs: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api.html

[3] Overview of WebSocket APIs in API Gateway: https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html

[4] Load Balancing Node.js Application Servers with NGINX: https://docs.nginx.com/nginx/deployment-guides/load-balance-third-party/node-js

[5] Introduction | Apache Kafka (0.10.2): https://kafka.apache.org/0102/getting-started/introduction

[6] Introduction | Apache Kafka (current): https://kafka.apache.org/documentation

[7] Introduction | Apache Kafka: https://kafka.apache.org/documentation

[8] KafkaConsumer javadoc (kafka 2.5.0 API): https://kafka.apache.org/25/javadoc/org/apache/kafka/clients/consumer/KafkaConsumer.html

[9] Introduction | Apache Kafka (0.8.1): https://kafka.apache.org/081/getting-started/introduction

[10] Redis Pub/sub | Docs: https://redis.io/docs/latest/develop/pubsub

[11] Load Balancing Apache Tomcat Servers with NGINX: https://docs.nginx.com/nginx/deployment-guides/load-balance-third-party/apache-tomcat

[12] Core components of Amazon DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.CoreComponents.html

[13] Using write sharding to distribute workloads evenly in DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-sharding.html

[14] Dynamo: Amazon's Highly Available Key-value Store (SOSP 2007): https://www.allthingsdistributed.com/files/amazon-dynamo-sosp2007.pdf

[15] CLUSTER KEYSLOT | Redis Docs: https://redis.io/docs/latest/commands/cluster-keyslot

[16] Database clustering | Redis Docs: https://redis.io/docs/latest/operate/rs/databases/durability-ha/clustering

[17] Redis pub/sub with Lettuce | Docs: https://redis.io/docs/latest/develop/use-cases/pub-sub/java-lettuce

[18] Redis streaming | Docs: https://redis.io/docs/latest/develop/use-cases/streaming

[19] Uploading objects with presigned URLs: https://docs.aws.amazon.com/AmazonS3/latest/userguide/PresignedUrlUploadObject.html

[20] Confluent Docs – Message Delivery Guarantees for Apache Kafka: https://docs.confluent.io/kafka/design/delivery-semantics.html

[21] Confluent Blog – Exactly-Once Semantics Are Possible: Here's How Apache Kafka Does It: https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it

[22] AWS SQS Developer Guide – Amazon SQS at-least-once delivery: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/standard-queues-at-least-once-delivery.html

[23] AWS SQS Developer Guide – Exactly-once processing in Amazon SQS: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues-exactly-once-processing.html

[24] Conduktor – Exactly-Once Semantics in Kafka: https://www.conduktor.io/glossary/exactly-once-semantics-in-kafka

[25] ActiveWizards – Kafka Exactly-Once Semantics: Idempotence and Transactions Guide: https://activewizards.com/blog/kafka-exactly-once-semantics-guide

[26] Confluent Docs – Kafka Replication and Committed Messages: https://docs.confluent.io/kafka/design/replication.html

[27] Conduktor – Kafka min.insync.replicas Explained: https://www.conduktor.io/kafka/kafka-topic-configuration-min-insync-replicas

[28] Apigee Docs – About Cassandra replication factor and consistency level: https://docs.apigee.com/private-cloud/v4.53.01/about-cassandra-replication-factor-and-consistency-level

[29] Apache Cassandra Documentation – Dynamo (architecture): https://cassandra.apache.org/doc/stable/cassandra/architecture/dynamo.html

[30] DataStax Documentation – How is the consistency level configured?: https://docs.datastax.com/en/cassandra-oss/3.0/cassandra/dml/dmlConfigConsistency.html

[31] Crunchy Data Blog – Synchronous Replication in PostgreSQL: https://www.crunchydata.com/blog/synchronous-replication-in-postgresql

[32] Raft Paper (Ongaro & Ousterhout): https://raft.github.io/raft.pdf

[33] Wikipedia – Raft (algorithm): https://en.wikipedia.org/wiki/Raft_(algorithm)

[34] System Design Sandbox – Leader Election: https://www.systemdesignsandbox.com/learn/leader-election

[35] Medium – Kafka Topics, Partitions, Replication, ISR, Leader Election, Acks — Deep Dive: https://medium.com/@anil.goyal0057/kafka-topics-partitions-replication-isr-leader-election-acks-deep-dive-a744def1d413

[36] websocket.org – WebSockets at Scale: Architecture for Millions of Connections: https://websocket.org/guides/websockets-at-scale

[37] OneUptime – How to Use Redis with WebSockets for Pub/Sub: https://oneuptime.com/blog/post/2026-02-02-redis-websockets-pubsub/view

[38] AWS ELB Docs – Health checks for Application Load Balancer target groups: https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html

[39] AWS ELB Docs – Health checks for Network Load Balancer target groups: https://docs.aws.amazon.com/elasticloadbalancing/latest/network/target-group-health-checks.html

[40] Veeam Blog – RTO vs RPO: What They Mean and How To Set Targets: https://www.veeam.com/blog/recovery-time-recovery-point-objectives.html

[41] PostgreSQL Docs – Continuous Archiving and Point-in-Time Recovery (PITR): https://www.postgresql.org/docs/current/continuous-archiving.html

[42] DEV Community – PostgreSQL Backups and Point-in-Time Recovery with pgBackRest: https://dev.to/mohhddhassan/postgresql-backups-and-point-in-time-recovery-with-pgbackrest-13gp

[43] AWS DynamoDB Developer Guide – Point-in-time backups for DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Point-in-time-recovery.html

[44] AWS DynamoDB Developer Guide – Enable point-in-time recovery in DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery_Howitworks.html

[45] AWS Database Blog – Backup strategies for Amazon DynamoDB: https://aws.amazon.com/blogs/database/backup-strategies-for-amazon-dynamodb

[46] AWS DynamoDB Developer Guide – DynamoDB read consistency: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html

[47] AWS Whitepaper – Disaster recovery options in the cloud: https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html

[48] Wikipedia – CAP theorem: https://en.wikipedia.org/wiki/CAP_theorem

[49] Mosharaf Chowdhury – Brewer's Conjecture and the Feasibility of Consistent, Available, Partition-Tolerant Web Services: https://mosharaf.com/blog/2011/09/19/brewers-conjecture-and-the-feasibility-of-consistent-available-partition-tolerant-web-services

[50] Devopedia – CAP Theorem: https://devopedia.org/cap-theorem

[51] Pythian Blog – Cassandra Consistency Level Guide: https://www.pythian.com/blog/cassandra-consistency-level-guide

[52] Wikipedia – Transport Layer Security: https://en.wikipedia.org/wiki/Transport_Layer_Security

[53] IETF Datatracker – RFC 8446: https://datatracker.ietf.org/doc/html/rfc8446

[54] Cloudflare Blog – A Detailed Look at RFC 8446 (a.k.a. TLS 1.3): https://blog.cloudflare.com/rfc-8446-aka-tls-1-3

[55] Internet Society – Deploying TLS 1.3: https://www.internetsociety.org/blog/2018/08/deploying-tls-1-3

[56] NIST CSRC Glossary – Transport Layer Security (TLS): https://csrc.nist.gov/glossary/term/transport_layer_security

[57] AWS Docs – Protecting data with server-side encryption (S3): https://docs.aws.amazon.com/AmazonS3/latest/userguide/serv-side-encryption.html

[58] AWS Docs – Using server-side encryption with Amazon S3 managed keys (SSE-S3): https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingServerSideEncryption.html

[59] AWS Docs – AWS KMS cryptography essentials: https://docs.aws.amazon.com/kms/latest/developerguide/kms-cryptography.html

[60] AWS Docs – Using server-side encryption with AWS KMS keys (SSE-KMS): https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingKMSEncryption.html

[61] AWS Key Management Service (KMS) FAQs: https://aws.amazon.com/kms/faqs

[62] RFC Editor – RFC 9420: https://www.rfc-editor.org/info/rfc9420

[63] Wikipedia – Signal Protocol: https://en.wikipedia.org/wiki/Signal_Protocol

[64] Signal Official Documentation: https://signal.org/docs

[65] Signal Specification – The X3DH Key Agreement Protocol: https://signal.org/docs/specifications/x3dh

[66] Signal Specification – The Double Ratchet Algorithm: https://signal.org/docs/specifications/doubleratchet

[67] positive-intentions.com – Adapting the Signal Protocol for P2P Messaging: https://positive-intentions.com/blog/p2p-signal-protocol

[68] arXiv 2301.07045 – Analysis and Improvements of the Sender Keys Protocol: https://arxiv.org/pdf/2301.07045

[69] The Stack – RFC 9420 – A Messaging Layer Security Overview: https://www.thestack.technology/rfc9420-ietf-mls-standard

[70] IETF Datatracker – RFC 9420 The Messaging Layer Security (MLS) Protocol: https://datatracker.ietf.org/doc/html/rfc9420

[71] Phoenix R&D Blog – RFC 9420 aka Messaging Layer Security (MLS): https://blog.phnx.im/rfc-9420-mls

[72] Wikipedia – Messaging Layer Security: https://en.wikipedia.org/wiki/Messaging_Layer_Security

[73] RFC Editor – RFC 9750 The Messaging Layer Security (MLS) Architecture: https://www.rfc-editor.org/info/rfc9750

[74] Signal Blog – Technology preview: Sealed sender for Signal: https://signal.org/blog/sealed-sender

[75] RFC 9750 – The Messaging Layer Security (MLS) Architecture: https://www.rfc-editor.org/info/rfc9750

[76] Signal Blog – Introducing Signal Secure Backups: https://signal.org/blog/introducing-secure-backups

[77] PostgreSQL Docs – Log-Shipping Standby Servers: https://www.postgresql.org/docs/current/warm-standby.html

[78] PostgreSQL Docs – Table Partitioning: https://www.postgresql.org/docs/current/ddl-partitioning.html

[79] Google Cloud Docs – Supported Redis configurations (Memorystore for Redis): https://docs.cloud.google.com/memorystore/docs/redis/supported-redis-configurations

[80] AWS Docs – Best practices for designing and using partition keys effectively in DynamoDB: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html

[81] PostgreSQL Docs – 13.1. Introduction (Concurrency Control / MVCC): https://www.postgresql.org/docs/current/mvcc-intro.html

[82] Redis Glossary – Understanding pub/sub in distributed systems: https://redis.io/glossary/pub-sub

[83] AWS Docs – DAX and DynamoDB consistency models: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DAX.consistency.html

[84] AWS re:Post – DynamoDB DAX Consistency SLA: https://repost.aws/questions/QU_lAeFu-_TCGBaongbHdpeQ/dynamodb-dax-consistency-sla

[85] PostgreSQL Docs – Hot Standby: https://www.postgresql.org/docs/current/hot-standby.html

[86] AWS DynamoDB Developer Guide – DynamoDB read consistency: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadConsistency.html

[87] AWS DynamoDB Developer Guide – DynamoDB read and write operations: https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/read-write-operations.html

[88] MongoDB Manual – Sharding: https://www.mongodb.com/docs/manual/sharding

[89] MongoDB Manual – Read Concern: https://www.mongodb.com/docs/manual/reference/read-concern

[90] MongoDB Manual – Write Concern: https://www.mongodb.com/docs/manual/reference/write-concern

[91] Pythian Blog – Cassandra Consistency Level Guide: https://www.pythian.com/blog/cassandra-consistency-level-guide

[92] All Things Distributed – Amazon DynamoDB – a Fast and Scalable NoSQL Database Service: https://www.allthingsdistributed.com/2012/01/amazon-dynamodb.html

[93] AWS Whitepaper – Comparing the Use of Amazon DynamoDB and Apache HBase for NoSQL: https://docs.aws.amazon.com/pdfs/whitepapers/latest/comparing-dynamodb-and-hbase-for-nosql/comparing-dynamodb-and-hbase-for-nosql.pdf

[94] Apache Cassandra Glossary: https://cassandra.apache.org/_/glossary.html

[95] Redis Docs – EXPIRE command: https://redis.io/docs/latest/commands/expire

[96] AWS Docs – Sharing objects with presigned URLs: https://docs.aws.amazon.com/AmazonS3/latest/userguide/ShareObjectPreSignedURL.html
