# Design Document: A Highly Available, Horizontally Scalable Chat Application

## Introduction

This document provides a comprehensive, introductory-level design for a chat application capable of supporting millions of concurrent users. The system must deliver messages with exactly-once semantics, support typing indicators, message history, media sharing, one-to-one and group chats, and ideally end-to-end encryption. The target audience is junior developers, so explanations focus on foundational concepts, practical trade-offs, and real-world examples from proven systems like WhatsApp, Slack, and Discord.

Designing a chat system at this scale is fundamentally a distributed systems problem. The challenges are not just about writing code—they are about managing state across many machines, ensuring data is never lost, and delivering messages in milliseconds even when servers fail. The following sections break down each aspect of the architecture, from database selection to security, with clear explanations of why certain choices are made.

---

## 1. Database Selection: Comparing Relational, NoSQL, and Distributed Databases

### 1.1 The Core Trade-off: ACID vs. BASE

The fundamental choice in database technology is between ACID (Atomicity, Consistency, Isolation, Durability) and BASE (Basically Available, Soft state, Eventual consistency) models.

**ACID** databases (like PostgreSQL and MySQL) provide strong consistency. Every transaction is atomic, isolated, and durable. This is essential for financial data, user accounts, and any system where accuracy is critical. However, strong consistency comes at a cost: it requires coordination between nodes, which increases latency and limits horizontal write scalability [1][2].

**BASE** databases (like Cassandra, DynamoDB, and MongoDB) prioritize availability and partition tolerance. They allow temporary inconsistencies—different nodes may return different values for the same data for a brief period—but eventually converge to a consistent state. This trade-off enables linear horizontal scaling and high write throughput [3][4].

For a chat application, the right approach is **polyglot persistence**: using different databases for different parts of the system. Messages are a high-volume, write-heavy workload that benefits from NoSQL. User profiles and account data require strong consistency and benefit from SQL. Session management and presence data are best served by an in-memory store like Redis [5][6].

### 1.2 Database-by-Database Comparison

**PostgreSQL** is a powerful open-source relational database with full ACID compliance, complex query support, and JSONB flexibility for semi-structured data. It is excellent for user profiles, groups, and any data that needs strong consistency. However, horizontal write scaling is complex and requires extensions like CitusDB. PostgreSQL is used by companies like OpenAI, Shopify, and Notion [7][8].

**MySQL** is another pillar of relational databases. It offers excellent vertical scaling and read replication. For horizontal scaling, tools like **Vitess** (originally developed at YouTube) enable sharding. Slack migrated to Vitess and now serves 2.3 million queries per second at peak, with median latency of 2ms and p99 latency of 11ms. Slack's data is partitioned by workspace ID [9][10][11].

**MongoDB** is a document-oriented NoSQL database designed for horizontal scaling via sharding. It offers a flexible data model and tunable consistency. However, it uses document-level locking, and documents are limited to 16MB. MongoDB is a good fit for user profiles, content management, and prototyping, but it is not ideal for the high-volume, append-only message workloads that chat systems require [8][12].

**Cassandra** is a distributed NoSQL database with a peer-to-peer architecture—no master node, so there is no single point of failure. It provides linear horizontal scalability, high write throughput, and tunable consistency. Cassandra was designed for exactly this kind of workload: write-heavy, high-volume, and requiring low-latency access. However, it has known weaknesses: slow reads, compaction overhead, and JVM garbage collection pauses at scale [13][14].

**Discord's experience with Cassandra** is a cautionary tale. By 2022, Discord's Cassandra cluster had grown to 177 nodes storing trillions of messages. They faced severe problems: hot partitions, unpredictable latency (p99 read latency of 40–125ms), expensive compaction operations, and frequent JVM garbage collection pauses. These issues required increasing effort to maintain and improve [15][16].

**ScyllaDB** is a Cassandra-compatible database written in C++ instead of Java. It eliminates garbage collection pauses and uses a shared-nothing asynchronous architecture that scales linearly. Discord migrated from Cassandra to ScyllaDB and achieved dramatic improvements: p99 read latency dropped from 40–125ms to 15ms, write latency from 5–70ms to a steady 5ms. The cluster size decreased from 177 nodes to 72. This migration was completed in nine days [15][17].

**DynamoDB** is a fully managed NoSQL database from AWS. It offers automatic scaling, single-digit millisecond latency, and seamless integration with the AWS ecosystem. However, it is expensive (often 7x more than comparable alternatives), requires a fundamentally different design approach (single-table, access-pattern-driven schema), and has a maximum item size of 400KB. It is best for serverless applications where access patterns are known upfront [8][18].

### 1.3 Recommended Database Strategy for a Chat System

The recommended approach is polyglot persistence:

- **Message History**: Use a distributed NoSQL database optimized for high write throughput and low latency. ScyllaDB is the strongest choice based on proven production results at Discord. Cassandra and DynamoDB are also viable options. The data model is an append-only log with a partition key like `(channel_id, bucket)` where `bucket` represents a time window (e.g., 10 days) to prevent hot partitions [15][19].

- **User Profiles and Groups**: Use a relational database like PostgreSQL or MySQL. This data needs ACID transactions, strong consistency, and support for complex queries (e.g., finding all groups a user belongs to). These databases are also ideal for structured data like user settings and group metadata [5][7].

- **Session Management and Presence**: Use an in-memory database like Redis. Presence data (online/offline status) generates enormous traffic—WhatsApp's presence system generates 33 million requests per second, 20x the messaging load. The solution is a Redis cluster sharded by UserID with a TTL (e.g., 45 seconds) to store online status, avoiding disk writes entirely [20][21].

- **Media Storage**: Use object storage like AWS S3, with a CDN for fast global delivery. Media files are uploaded via pre-signed URLs and served through the CDN. Thumbnails are generated asynchronously, and virus scanning is performed before files are made available for download [22][23].

- **Search Indexing**: Use a full-text search engine like Elasticsearch to enable searching through message history. This is a separate service that indexes messages asynchronously from the message queue [24].

---

## 2. Core Architecture Components

### 2.1 High-Level Architecture Overview

The system consists of several layers that work together to provide reliable, low-latency messaging:

```
[Client Apps] → [Load Balancer] → [API Gateway] → [Chat Servers] → [Message Queue] → [Storage Layer]
                                              ↓
                                        [Redis Pub/Sub]
                                              ↓
                                        [Presence Service]
                                              ↓
                                        [Notification Service]
```

- **Client Apps**: Mobile and web applications that connect to the server using WebSockets for real-time communication and HTTP for REST API calls [25].
- **Load Balancer**: Distributes incoming traffic across multiple chat server instances. For WebSocket connections, sticky sessions ensure clients consistently connect to the same server [26].
- **API Gateway**: Handles authentication (JWT/OAuth 2.0), rate limiting, and request routing. It also terminates TLS connections [27].
- **Chat Servers**: Stateless application servers that handle message routing, WebSocket connection management, and business logic. They are horizontally scalable—add more servers to handle more users [25].
- **Message Queue**: Decouples message ingestion from storage. Apache Kafka is the preferred choice for its durability, ordering guarantees, and high throughput. The chat server publishes messages to Kafka, and a separate consumer service persists them to the database [28][29].
- **Redis Pub/Sub**: Enables cross-server communication for real-time events like typing indicators and presence updates. When a chat server needs to send an event to a user connected to a different server, it publishes to Redis, and the target server's subscriber delivers it [30].
- **Presence Service**: Tracks user online/offline status. Uses Redis with TTL to avoid disk writes. Updates are pushed to relevant users via WebSocket [20].
- **Notification Service**: Sends push notifications (via FCM or APNS) to offline users when they receive messages [26].

### 2.2 Real-Time Event Handling: WebSockets

WebSockets are the foundation of real-time messaging. Unlike HTTP, which requires the client to poll for updates, a WebSocket maintains a persistent, bidirectional connection between the client and server. Both parties can send messages at any time, with very low latency [31].

Scaling WebSockets is challenging because they are stateful connections. Once a connection is established, all messages for that client must go through the same server. This requires two key mechanisms:

1. **Sticky Sessions**: The load balancer ensures that a client always connects to the same server. This is achieved using IP hash or cookie-based affinity [32].
2. **Pub/Sub Backplane**: When a message needs to reach a client connected to a different server, the system uses a pub/sub system (Redis Pub/Sub or Kafka) to forward the message to the correct server [30].

A production system must also handle backpressure. If a slow consumer accumulates a large buffer, it can cause memory exhaustion. The solution is non-blocking writes: if a client's buffer is full, the message is dropped and the connection is closed. Real-time data has an expiration date—a client that is significantly behind is consuming resources for stale data [33].

### 2.3 Messaging Layer: Message Queues and Pub/Sub

**Apache Kafka** is the recommended message queue for the durable message layer. Kafka is a distributed event streaming platform that can process millions of messages per second. It provides durability (messages are persisted to disk), ordering guarantees within a partition, and the ability to replay messages. The chat server publishes messages to a Kafka topic, and consumers read from the topic to persist messages to the database and to fan out to recipients [28][29].

**Redis Pub/Sub** is used for ephemeral, real-time events like typing indicators and presence updates. These events do not need to be persisted—if they are lost, the system simply waits for the next update. Redis Pub/Sub is extremely fast and lightweight, making it ideal for high-frequency events that do not require durability [30].

The key insight is that **durable messages and ephemeral events should use different paths**. Sending typing indicators through Kafka would be wasteful and would add unnecessary load. Using Redis Pub/Sub for ephemeral events and Kafka for durable messages is the correct separation of concerns [34].

### 2.4 Exactly-Once Message Delivery

True exactly-once delivery is theoretically impossible in a distributed system due to the Two Generals Problem. What we implement is **effectively exactly-once**: combining at-least-once delivery with idempotent processing [35][36].

The practical approach is:

1. **At-Least-Once Delivery**: The system guarantees that a message will be delivered, but it may be delivered more than once. This is achieved through acknowledgments and retries. Kafka's at-least-once semantics, combined with consumer acknowledgments, ensure messages are not lost [37].

2. **Idempotent Consumers**: Each message has a unique ID (e.g., a client-generated `message_id`). The consumer checks if this ID has already been processed before applying the message. This is done using a database unique constraint or a Redis SET NX operation [38].

3. **Deduplication at the Client**: The client also deduplicates received messages using the message ID. This provides an additional safety layer [39].

The implementation checklist includes: idempotency key assignment, durable key store, atomic write-with-check (using database unique constraints), sequence number tracking, and dead letter handling for failed messages [36].

---

## 3. Scalability Mechanisms

### 3.1 Horizontal Scaling vs. Vertical Scaling

**Vertical scaling** (adding more CPU, RAM, or storage to a single server) is simple but has hard limits. You cannot buy a machine larger than the largest available. It also creates a single point of failure [40].

**Horizontal scaling** (adding more servers) is the approach for supporting millions of users. It provides virtually unlimited growth, better fault tolerance, and seamless scaling. The key requirement is that the application must be **stateless**—any server should be able to handle any request. Session state is moved to an external store like Redis [41][42].

In practice, most systems use a hybrid approach: scale vertically for simple headroom, then scale horizontally when capacity or failure handling demands it. The transition from vertical to horizontal scaling often exposes architecture assumptions, especially around session state and caching [43].

### 3.2 Sharding Strategies

Sharding is the process of splitting a large database into smaller, independent pieces (shards) spread across multiple servers. The choice of shard key is the most critical design decision [44].

For a chat system, the primary sharding strategies are:

- **Sharding by Conversation ID**: All messages for a given conversation are stored on the same shard. This is the recommended approach for chat because it simplifies message ordering (ordering is guaranteed within a partition) and allows efficient retrieval of a conversation's history. The shard key is the conversation ID, and consistent hashing is used to map conversations to shards [45][46].

- **Sharding by User ID**: A secondary database sharded by user ID is used to efficiently retrieve a user's list of conversations, sorted by recency. This is necessary for the inbox view that shows all a user's conversations [47].

- **Sharding by Geographic Region**: Shards are placed in different physical locations, close to the users they serve. This reduces latency and is useful for global deployments. For example, Shard A serves North America, Shard B serves Europe, and Shard C serves Asia [48].

**Consistent hashing** is the technique used to map keys to shards while minimizing rebalancing when servers are added or removed. Both keys and servers are hashed onto a circular space. A key is assigned to the next server found by moving clockwise from the key's position. When a server is added or removed, only a fraction of keys (roughly 1/n) need to be remapped, compared to nearly all keys with simple modulo hashing [49][50].

Virtual nodes are an extension of consistent hashing. Each physical server is represented by many (100–200) virtual nodes on the ring, which provides a more balanced distribution of keys and better resilience to uneven data distributions [50].

### 3.3 Load Balancing Techniques

Load balancing distributes incoming traffic across multiple servers. The choice of algorithm depends on the workload:

- **Round Robin**: Distributes requests sequentially. Simple and effective for stateless services with identical servers [51].
- **Least Connections**: Routes requests to the server with the fewest active connections. Best for WebSocket servers where connections have varying lifetimes [51].
- **IP Hash**: Uses the client's IP address to determine which server receives the request. This provides implicit sticky sessions, which are essential for WebSocket connections [52].
- **Application-Level (Layer 7)**: Load balancers like NGINX and HAProxy can make routing decisions based on HTTP headers, cookies, and URL paths. This is used for API gateways and content-based routing [53].

For global deployments, **Global Server Load Balancing (GSLB)** uses DNS to steer traffic to the nearest data center, reducing latency and providing disaster recovery [54].

---

## 4. High Availability and Fault Tolerance

### 4.1 High Availability Patterns

**Active-Passive Failover**: One active server handles all traffic while passive servers remain on standby. A heartbeat mechanism detects failure and triggers automatic failover. This is simpler to configure but results in resource underutilization (standby servers sit idle) and longer recovery times during failover [55].

**Active-Active Clusters**: Multiple servers actively process traffic concurrently, with a load balancer distributing requests. If one server fails, the others continue serving traffic. This provides better resource utilization and near-instantaneous failover, but adds complexity for data synchronization [55].

**Multi-Region Deployment**: For true high availability, the system is deployed across multiple geographic regions. There are two approaches:

- **Active-Passive Multi-Region**: One primary region handles all read-write traffic. A secondary region maintains a continuously replicated copy via asynchronous replication. Failover promotes the secondary region to primary. This provides clear operational model with bounded data loss (replication lag) [56].

- **Active-Active Multi-Region**: Multiple regions are all writable. This requires Conflict-Free Replicated Data Types (CRDTs) or other conflict resolution mechanisms. It provides the highest availability but is the most complex to implement [57].

### 4.2 Replication and Data Durability

Within a single region, data is replicated across multiple servers (nodes) to handle failures. The recommended approach is a quorum-based system like Raft, which provides strong consistency and automatic failover [56].

- **Synchronous Replication**: Within a region, the primary waits for acknowledgment from a majority of replicas before acknowledging the write. This ensures no data loss but increases latency [58].
- **Asynchronous Replication**: Across regions, the primary does not wait for the remote region. This keeps write latency low but risks losing data if the primary fails before replication completes [56].

For the database layer, every shard is actually a replication group. **Sharding handles capacity, replication handles availability**. In a production system, every shard should have multiple replicas across different availability zones [59].

### 4.3 Fault Tolerance Patterns

**Circuit Breaker Pattern**: Prevents an application from repeatedly trying an operation that is likely to fail. The circuit breaker has three states: closed (normal), open (failures exceeded threshold, requests fail immediately), and half-open (limited trial requests to test recovery). This prevents cascading failures and allows the system to recover gracefully [60][61].

**Retry with Exponential Backoff**: When a transient failure occurs, retry with increasing delays: 1 second, then 2, then 4, then 8... The formula is `delay = base_delay * 2^(attempt_count)`. Adding **jitter** (randomization) prevents the thundering herd problem where all clients retry at the same time [62][63].

**Graceful Degradation**: The system should preserve core functionality even under degraded conditions. For example, if the message database is slow, the system can still deliver messages from cache and queue writes for later. If the search service is down, the system can still send and receive messages without search functionality [64].

**Rate Limiting**: Controls the rate at which an application processes requests. Common algorithms include:

- **Token Bucket**: Allows controlled bursts. Tokens are added at a fixed rate, and each request consumes a token. Bursts are allowed up to the bucket size [65].
- **Sliding Window Counter**: A good compromise between accuracy and memory usage. It tracks request counts in a sliding time window [65].
- **Fixed Window Counter**: Simple but allows boundary bursts (e.g., 100 requests in the first second of the window, then 0 for the rest) [65].

Redis is the standard choice for storing rate limit counters due to its atomic operations and low latency [65].

---

## 5. One-to-One and Group Chat Design

### 5.1 One-to-One Chat Flow

When User A sends a message to User B:

1. The message is sent from the client to a load balancer, which routes it to a chat server.
2. The chat server validates the message, assigns a unique message ID (e.g., Snowflake ID), and publishes it to Kafka.
3. A consumer reads from Kafka and persists the message to the message database (e.g., ScyllaDB).
4. The server checks if User B is online by querying the presence service (Redis). If online, the message is pushed to User B's WebSocket connection. If offline, a push notification is sent via FCM/APNS [26][66].

### 5.2 Group Chat and Fan-Out Strategies

Group chat is where the architecture gets genuinely hard. When a user sends a message to a group of 100 people, the system must deliver the message to all 100 members. This is called **fan-out** [67].

There are three fan-out strategies:

**Fan-out on Write (Push Model)**: The message is immediately pushed to all recipients. This provides fast reads (the data is already there when the recipient checks) but has high write overhead. For a group with 1000 members, writing one message requires 1000 database writes. This does not scale for very large groups [68][69].

**Fan-out on Read (Pull Model)**: The message is stored once, and recipients fetch it when they read their inbox. This has low write overhead but higher read latency, as each recipient must query the database to find new messages. This is suitable for very large groups where fan-out on write would be impractical [68][69].

**Hybrid Approach**: Use fan-out on write for small groups (up to ~100 members) and fan-out on read for large groups. This is the approach used by Twitter for timelines: normal users get fan-out on write, celebrities with millions of followers get fan-out on read [70].

For a chat system, the recommended approach is:

- **Small groups (<100 members)**: Fan-out on write. Each recipient gets a copy of the message in their personal inbox. This provides fast reads and simple delivery tracking [71].
- **Large groups (100–500 members)**: Direct server-to-server delivery combined with Kafka-based fan-out. The message is published to Kafka, and a fan-out service determines recipients and pushes to their WebSocket connections [71].
- **Very large groups (>500 members)**: Fan-out on read. The message is stored once, and recipients fetch it when they read the channel. This is the approach used by Discord for large servers [72].

### 5.3 Group Membership Management

The Group Service manages all group-related data: member lists, roles, permissions, and group metadata. This data is stored in a relational database (PostgreSQL or MySQL) for ACID compliance. Redis is used as a cache for fast access [73].

When a user joins or leaves a group, the fan-out list must be updated dynamically. For large groups, membership changes need to be propagated efficiently without disrupting ongoing message delivery. The system updates the cache and database, and the next message delivery uses the updated list [74].

### 5.4 Media Sharing

Media sharing involves several components:

- **Upload Flow**: The client uploads the file to blob storage (S3) using a pre-signed URL. The URL is generated by the media service and includes an expiration time [22].
- **Thumbnail Generation**: A background worker monitors the upload bucket, generates thumbnails at multiple sizes (e.g., 100px, 300px, 800px), and stores them in the CDN [75].
- **Virus Scanning**: Files are scanned before they are made available for download. The system uses a quarantine bucket: files are uploaded to a private quarantine bucket, scanned, and only moved to the public bucket if they pass. The scan result acts as a gate—nothing becomes downloadable until the gate says so [23].
- **CDN Distribution**: Frequently accessed media is cached on CDN edge servers for fast delivery to users worldwide. CDN URLs are signed and expire after a configurable period (e.g., 14 days) [22].

### 5.5 Message History and Pagination

For retrieving message history, **cursor-based pagination** is strongly recommended over offset-based pagination. Cursor-based pagination uses a pointer (the cursor) to the last message the user has seen. The client requests the next page by sending this cursor. This approach:

- Avoids the performance degradation of offset pagination (which requires the database to count all previous rows)
- Provides consistent results even when new messages are arriving (no phantom rows or duplicates)
- Scales to any depth with constant performance [76][77]

The cursor is typically a message ID or timestamp. For example, the request might be: "Give me the 20 messages before message ID 12345." The database uses an index to find the starting position and returns the next 20 messages [78].

### 5.6 Read Receipts and Delivery Status

Read receipts track whether a message has been delivered to and read by the recipient. The standard pattern is:

- **Single tick**: Message sent (arrived at the server)
- **Double tick**: Message delivered (arrived at the recipient's device)
- **Blue tick**: Message read (recipient opened the message)

At scale, tracking individual read receipts for every message in a large group is expensive. The solution is to use **batch read receipts**: the client sends a single "read up to message ID X" event, rather than individual events for each message. This reduces the number of database writes from O(N) to O(1) per user [79][80].

Discord uses a hybrid approach: for one-to-one chats, read receipts are updated instantly. For group chats, receipts are aggregated in Redis and flushed to the database every 10 seconds [81].

---

## 6. Real-World Case Studies

### 6.1 Discord: From MongoDB to Cassandra to ScyllaDB

Discord's database evolution illustrates the challenges of scaling a chat system:

- **Phase 1 (MongoDB, 2015)**: Discord launched with a single MongoDB replica set. By November 2015, 100 million messages caused data and indexes to exceed RAM, leading to unpredictable latency [15].

- **Phase 2 (Cassandra, 2015–2022)**: Discord migrated to Cassandra with a composite primary key of `((channel_id, bucket), message_id)` where `bucket` represents a 10-day window. This kept partitions under 100MB. By 2022, the cluster had grown to 177 nodes storing trillions of messages, but they faced severe problems: hot partitions, unpredictable latency (p99 read latency of 40–125ms), expensive compaction operations, and frequent JVM garbage collection pauses [15][16].

- **Phase 3 (ScyllaDB, 2022–present)**: Discord migrated to ScyllaDB, a C++ Cassandra-compatible database that eliminates GC pauses. They built a Rust-based data service layer with request coalescing (multiple requests for the same row combined into a single query) and consistent hash routing. Results: p99 read latency dropped to 15ms, write latency to 5ms, and the cluster size decreased from 177 nodes to 72. The migration was completed in nine days [15][17].

### 6.2 Slack: MySQL with Vitess

Slack's architecture is built on a LAMP stack (Linux, Apache, MySQL, PHP) with MySQL configured for eventual consistency and sharded via Vitess using workspace ID as the partition key. Key numbers: 2.3 million queries per second at peak (2 million reads, 300,000 writes), median query latency of 2ms, p99 of 11ms [9][10][11].

Slack uses two API types: a web API (HTTP) for user sessions and a real-time API (WebSockets) for chat, typing indicators, and presence. The chat server is a PHP monolith that performs CRUD operations on the database. A stateful gateway server pushes messages to clients over WebSockets, with consistent hashing mapping channels to gateways. Non-critical tasks are deferred via a custom job queue [82].

The hardest part of Slack's design is not message delivery—it is **blast radius management**. A 2021 incident forced a complete migration to a cellular architecture where failures in one cell do not cascade to the entire platform [83].

### 6.3 WhatsApp: Erlang, Mnesia, and Simplicity

WhatsApp's architecture is legendary for its efficiency: 900 million users served by only 50 engineers. The key design decisions:

- **Erlang/OTP**: Each user gets a dedicated Erlang process (lightweight actor-model processes, ~2 KB each, handling 2+ million concurrent connections per server). This makes concurrency a natural property of the system [84][85].
- **Mnesia**: An in-memory distributed database for sub-millisecond session lookups. Messages are relayed through the server but not stored permanently—the source of truth remains on the device [86].
- **Presence System**: The presence system generates 33 million requests per second, 20x the messaging load. The solution is a Redis cluster sharded by UserID with a TTL (45 seconds) to store online status, avoiding disk writes. WhatsApp uses **lazy presence**—no green dot in the chat list, only querying connection state when a conversation is opened [20].

The key lesson from WhatsApp: "System design isn't just about what you add to a diagram; it's about what you have the courage to leave out. Every new feature is a tax on the architecture's simplicity" [87].

---

## 7. Security and Encryption

### 7.1 Encryption in Transit and at Rest

**Encryption in Transit** protects data while it moves over the network. TLS (Transport Layer Security) is the standard protocol. It provides authentication (via digital certificates), confidentiality (via encryption), and integrity (via message authentication codes). All communication between clients and servers, and between servers, must use TLS 1.2 or TLS 1.3 [88][89].

**Encryption at Rest** protects stored data. This includes:

- **Database Encryption**: The database files are encrypted using AES-256. Most modern databases support transparent data encryption (TDE) [90].
- **File-Level Encryption**: Media files stored in S3 are encrypted at rest using server-side encryption (SSE-S3 or SSE-KMS) [91].
- **Backup Encryption**: Backups are encrypted before being stored.

Both forms of encryption are non-negotiable baselines. The global average cost of a data breach reached $4.44 million in 2025, making encryption of both data states essential [92].

### 7.2 End-to-End Encryption (E2EE)

E2EE ensures that messages are encrypted on the sender's device and can only be decrypted by the recipient's device. The server never has access to the plaintext. This is the most secure form of encryption for messaging [93].

**The Signal Protocol** is the gold standard for E2EE and is used by Signal, WhatsApp, and Facebook Messenger. It consists of two main components:

1. **X3DH (Extended Triple Diffie-Hellman)**: Establishes a shared secret key between two users who have never communicated before. It uses multiple key pairs (identity key, signed pre-key, one-time pre-key, ephemeral key) and combines them using Diffie-Hellman operations to produce a root key [94][95].

2. **Double Ratchet Algorithm**: After the initial key exchange, the Double Ratchet continuously updates the encryption keys after each message. It combines two ratchets:

   - **DH Ratchet (periodic key updates)**: Each time a new Diffie-Hellman public value is received, the root key is updated using a DH computation. This provides **forward secrecy** (compromise of current keys does not compromise past messages) and **break-in recovery** (compromise of current keys does not compromise future messages) [96][97].
   - **Symmetric-key Ratchet (per-message keys)**: Between DH ratchet steps, the sending and receiving chain keys are derived using a key derivation function (KDF). Each message uses a unique message key, so compromising one message key does not compromise other messages [96].

The Double Ratchet provides:
- **Confidentiality**: Messages are encrypted with AES-256-GCM
- **Integrity**: HMAC-SHA256 ensures messages have not been tampered with
- **Authentication**: The identity keys authenticate the participants
- **Forward Secrecy**: Past messages remain secure even if long-term keys are compromised
- **Post-Compromise Security**: Future messages become secure again after a compromise, as the DH ratchet introduces new randomness [96][97]

**Post-Quantum Security**: In October 2025, Signal announced the Sparse Post Quantum Ratchet (SPQR), which adds a quantum-safe ratchet (using ML-KEM) to the Double Ratchet, forming the Triple Ratchet. An attacker must break both elliptic-curve and ML-KEM to compromise the system [98].

### 7.3 Key Management and Verification

**Key Registration**: When a user installs the app, their device generates a set of key pairs (identity key, signed pre-key, one-time pre-keys). The public keys are uploaded to the server's key directory. Other users can look up these keys to initiate encrypted conversations [99].

**Key Verification (Safety Numbers)**: To prevent man-in-the-middle attacks, users must verify each other's identity keys. This is typically done by comparing a fingerprint (a hash of the public keys) displayed as a QR code or a numeric string. In-person verification is the most secure method. Key transparency (as used by WhatsApp) partially automates this by checking keys against a publicly auditable record [100][101].

**Key Loss**: If a user loses their private key (e.g., by changing devices), they cannot read their old messages. This is a fundamental trade-off of E2EE: strong security means no backdoor recovery mechanism. Solutions include:

- **Recovery Key/Seed Phrase**: Some apps provide a recovery key (e.g., a 24-word mnemonic phrase) that can restore access to encrypted data [102].
- **Cloud Backups**: Signal and WhatsApp provide encrypted cloud backups. Signal requires its own recovery key; WhatsApp uses iCloud/Google Drive, optionally with an extra encryption key [103].
- **Session Resumption**: If the user has other verified devices, they can use them to authorize a new device [103].

### 7.4 Trade-offs of E2EE

E2EE provides strong security but comes with trade-offs:

- **No Server-Side Search**: The server cannot see the contents of encrypted messages, so it cannot index them for search. Search must be performed client-side, which is limited to messages stored on the device [104].
- **No Server-Side Deduplication**: The server cannot perform content-based deduplication on encrypted messages [104].
- **No Moderation**: The service cannot scan for illegal content or spam. This is a significant concern for regulatory compliance [104].
- **Complex Key Management**: Users are responsible for their keys. If they lose their keys (or their device), they lose access to their messages [103].

For these reasons, some systems use a hybrid approach: encrypt only the most sensitive data with E2EE, while less sensitive data remains accessible for server-side processing [104].

### 7.5 Authentication and Authorization

**JWT (JSON Web Tokens)**: JWTs are used for stateless authentication. The client receives a signed token containing the user's identity and permissions. The token is sent with each request (typically in an HTTP header or cookie). Best practices include:

- Use short-lived access tokens (15 minutes) with refresh tokens stored in HTTP-only cookies [105].
- Verify signatures using strong algorithms (e.g., RS256 or ES256) [106].
- Store tokens securely (HTTP-only cookies for browser apps, secure storage for mobile apps) [105].

**OAuth 2.0**: For delegated authorization, OAuth 2.0 allows users to grant third-party applications limited access to their resources without sharing their credentials. The authorization code flow is the recommended approach, with the `state` parameter for CSRF protection [107].

**Rate Limiting**: Protects against brute-force attacks and DDoS. Implemented at the API gateway using Redis counters. The token bucket algorithm is a good choice for allowing controlled bursts while maintaining overall fairness [65].

**Input Sanitization**: Prevent XSS and injection attacks by sanitizing all user input. Front-end frameworks like React and Vue have built-in XSS protection. For SQL injection, use parameterized queries or ORMs [108].

---

## 8. Typing Indicators

Typing indicators are lightweight, ephemeral events that signal when a user is composing a message. They are not stored and do not need to be durable [109].

**Architecture**:

1. **Client-Side Debouncing**: The client does not send a typing event on every keystroke. Instead, it sends a "typing" event once every 3 seconds and a "stopped typing" event 5 seconds after the last keystroke [110].

2. **Server-Side Handling**: The chat server receives the typing event and publishes it to Redis Pub/Sub. The event contains the conversation ID, the user ID, and the status (typing/stopped). The server does not store this event or queue it for retry—if it fails, the next event will correct it [109][110].

3. **Cross-Server Delivery**: Redis Pub/Sub broadcasts the event to all chat servers. Only the server that has the recipient's WebSocket connection delivers the event to the client. The recipient's client displays the typing indicator [109].

4. **Server-Side TTL**: The server enforces a timeout (e.g., 10 seconds). If no new typing event is received within the timeout, the indicator is cleared. This handles the case where the "stopped typing" event is lost [110].

**Performance**: This approach is extremely efficient. The data sent is minimal (a few bytes), and Redis Pub/Sub can handle millions of events per second. End-to-end latency is typically 10–15ms [109].

**Best Practices**: Allow users to disable typing indicators. The feature adds no significant load to the system since the data is not persisted, but it can be a privacy concern for some users [110].

---

## 9. Conclusion

Designing a chat application for millions of concurrent users requires careful consideration of trade-offs at every layer. The key principles are:

1. **Polyglot Persistence**: Use the right database for each workload. ScyllaDB for message history, PostgreSQL for user profiles, Redis for presence and caching, S3 for media, and Elasticsearch for search.

2. **Separation of Concerns**: Use different paths for durable messages (Kafka + database) and ephemeral events (Redis Pub/Sub). This prevents the system from being overwhelmed by high-frequency, low-value events.

3. **Horizontal Scalability**: Design for statelessness from day one. Use consistent hashing for sharding, sticky sessions for WebSocket connections, and a pub/sub backplane for cross-server communication.

4. **Fault Tolerance**: Implement circuit breakers, retry with exponential backoff, and graceful degradation. Assume that every component will fail and design accordingly.

5. **Security**: Encrypt data in transit (TLS) and at rest (AES-256). Implement E2EE using the Signal Protocol for maximum privacy. Use JWT or OAuth 2.0 for authentication, and rate limiting for protection.

6. **Learn from Real-World Systems**: Discord's migration from Cassandra to ScyllaDB, Slack's use of Vitess for MySQL sharding, and WhatsApp's elegant Erlang architecture all provide valuable lessons. The most important lesson is from WhatsApp: "System design isn't just about what you add to a diagram; it's about what you have the courage to leave out."

The architecture described in this document is not a blueprint to be followed blindly, but a framework for thinking about the trade-offs. Start simple, monitor carefully, and evolve the architecture in response to real constraints rather than hypothetical scenarios.

---

### Sources

[1] ACID vs BASE Consistency Models: A Comparative Study: https://www.studocu.com/in/document/nirmala-college/database-technology-and-nosql/acid-vs-base-consistency-models/53627016

[2] ACID vs BASE: Understanding Database Consistency Models: https://bmf-tech.com/posts/acid-vs-base

[3] ACID vs. BASE: A Deep Dive into Database Consistency Models: https://medium.com/@lucasmedja1/acid-vs-base-a-deep-dive-into-database-consistency-models-8d0a798f7a72

[4] ACID and BASE consistency models: https://karanpratapsingh.com/courses/system-design/acid-and-base-consistency-models

[5] Chat App System Design: Messaging Architecture: https://trueconf.com/blog/reviews-comparisons/chat-app-system-design

[6] Designing a Real-time Chat App (WhatsApp, Slack): https://codefarm0.medium.com/designing-a-real-time-chat-app-whatsapp-slack-bf17912356d7

[7] When to Use PostgreSQL vs MongoDB vs DynamoDB (2026 Guide): https://singhajit.com/postgresql-vs-mongodb-vs-dynamodb

[8] Database Scalability Comparison: Postgres, MySQL, MongoDB, DynamoDB, Cassandra, Couchbase: https://scalewithchintan.com/blog/database-scalability-postgres-mysql-mongodb-dynamodb-cassandra-couchbase

[9] Database Management Systems Comparison: https://www.altexsoft.com/blog/comparing-database-management-systems-mysql-postgresql-mssql-server-mongodb-elasticsearch-and-others

[10] Messaging Architecture: https://newsletter.systemdesign.one/p/messaging-architecture

[11] Slack's Vitess deployment: https://www.cncf.io/case-studies/slack/

[12] Cassandra vs MongoDB: https://aws.amazon.com/compare/the-difference-between-cassandra-and-mongodb

[13] NoSQL Database Comparison: https://www.dnsstuff.com/nosql-database-comparison/amp

[14] How Discord Stores Trillions of Messages: https://discord.com/blog/how-discord-stores-trillions-of-messages

[15] How Discord Stores Trillions of Messages (2022 update): https://discord.com/blog/how-discord-stores-trillions-of-messages

[16] Discord's Cassandra to ScyllaDB Migration: https://www.scylladb.com/2022/06/08/how-discord-migrated-from-cassandra-to-scylladb/

[17] DynamoDB Comparison: https://www.scylladb.com/learn/dynamodb/introduction-to-dynamodb/comparison

[18] Designing WhatsApp's Presence System: https://www.linkedin.com/posts/arslanahmad_systemdesign-whatsapp-scalability-activity-7402941303627558912-

[19] How to Design a Real-Time Chat Application: https://www.designgurus.io/blog/design-chat-application

[20] Design a Chat System: https://bytebytego.com/courses/system-design-interview/design-a-chat-system

[21] Media Sharing Architecture: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[22] Virus Scanning for File Uploads: https://stackoverflow.com/questions/73326665/architecture-of-a-simple-chat-web-app-at-scale

[23] Best Database for Chat Applications: https://quickblox.com/blog/beginners-guide-to-chat-app-architecture

[24] Scalable chat app architecture: https://ably.com/blog/chat-app-architecture

[25] Engineering a scalable backend for a messaging app: https://www.rst.software/blog/engineering-a-scalable-backend-for-a-messaging-app-like-whatsapp-4-key-principles

[26] Authentication and Authorization: https://www.ionos.com/digitalguide/server/know-how/mongodb-vs-dynamodb

[27] Apache Kafka: https://kafka.apache.org/documentation/

[28] RabbitMQ vs Kafka: https://www.baeldung.com/cs/eventual-consistency-vs-strong-eventual-consistency-vs-strong-consistency

[29] Redis Pub/Sub: https://redis.io/docs/latest/develop/interact/pubsub/

[30] WebSockets: https://developer.mozilla.org/en-US/docs/Web/API/WebSocket

[31] WebSocket Scaling Strategies: https://ably.com/blog/chat-app-architecture

[32] WebSocket Backpressure: https://www.rst.software/blog/chat-app-architecture

[33] Separating Ephemeral from Durable Events: https://codefarm0.medium.com/designing-a-real-time-chat-app-whatsapp-slack-bf17912356d7

[34] Exactly-Once Delivery: https://www.developers.dev/tech-talk/the-pragmatic-guide-to-data-consistency-in-microservices-strong-vs-eventual-for-enterprise-scale.html

[35] Idempotency Keys: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[36] At-Least-Once Delivery: https://bytebytego.com/courses/system-design-interview/design-a-chat-system

[37] Deduplication: https://designgurus.substack.com/p/postgresql-vs-dynamodb-vs-cassandra

[38] Client-Side Deduplication: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[39] Horizontal vs Vertical Scaling: https://scalewithchintan.com/blog/database-scalability-postgres-mysql-mongodb-dynamodb-cassandra-couchbase

[40] Stateless Architecture: https://karanpratapsingh.com/courses/system-design/acid-and-base-consistency-models

[41] Stage-by-Stage Scaling Roadmap: https://www.rst.software/blog/engineering-a-scalable-backend-for-a-messaging-app-like-whatsapp-4-key-principles

[42] Hybrid Scaling: https://singhajit.com/postgresql-vs-mongodb-vs-dynamodb

[43] Sharding Strategies: https://www.designgurus.io/blog/design-chat-application

[44] Sharding by Conversation ID: https://bytebytego.com/courses/system-design-interview/design-a-chat-system

[45] Two-Shard Write Problem: https://codefarm0.medium.com/designing-a-real-time-chat-app-whatsapp-slack-bf17912356d7

[46] Sharding by User ID: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[47] Geographic Sharding: https://scalewithchintan.com/blog/database-scalability-postgres-mysql-mongodb-dynamodb-cassandra-couchbase

[48] Consistent Hashing: https://karanpratapsingh.com/courses/system-design/acid-and-base-consistency-models

[49] Virtual Nodes: https://www.scylladb.com/learn/dynamodb/introduction-to-dynamodb/comparison

[50] Load Balancing Algorithms: https://www.nginx.com/resources/glossary/load-balancing/

[51] Sticky Sessions: https://ably.com/blog/chat-app-architecture

[52] Application Load Balancing: https://aws.amazon.com/elasticloadbalancing/application-load-balancer/

[53] Global Server Load Balancing: https://www.cloudflare.com/learning/performance/global-load-balancer/

[54] Active-Passive vs Active-Active: https://www.designgurus.io/blog/design-chat-application

[55] Multi-Region Active-Passive: https://www.scylladb.com/learn/dynamodb/introduction-to-dynamodb/comparison

[56] Active-Active with CRDTs: https://karanpratapsingh.com/courses/system-design/acid-and-base-consistency-models

[57] Raft Consensus Algorithm: https://raft.github.io/

[58] Sharding vs Replication: https://bytebytego.com/courses/system-design-interview/design-a-chat-system

[59] Circuit Breaker Pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker

[60] Circuit Breaker + Exponential Backoff: https://www.developers.dev/tech-talk/the-pragmatic-guide-to-data-consistency-in-microservices-strong-vs-eventual-for-enterprise-scale.html

[61] Exponential Backoff with Jitter: https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/

[62] Retry Policies: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[63] Graceful Degradation: https://www.rst.software/blog/engineering-a-scalable-backend-for-a-messaging-app-like-whatsapp-4-key-principles

[64] Rate Limiting Algorithms: https://www.nginx.com/blog/rate-limiting-nginx/

[65] One-to-One Chat Flow: https://bytebytego.com/courses/system-design-interview/design-a-chat-system

[66] Group Chat Complexity: https://www.designgurus.io/blog/design-chat-application

[67] Fan-out on Write: https://codefarm0.medium.com/designing-a-real-time-chat-app-whatsapp-slack-bf17912356d7

[68] Fan-out on Read: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[69] Hybrid Fan-out: https://newsletter.systemdesign.one/p/messaging-architecture

[70] Fan-out Strategy for Group Chat: https://www.designgurus.io/blog/design-chat-application

[71] Discord's Group Chat: https://discord.com/blog/how-discord-stores-trillions-of-messages

[72] Group Service: https://bytebytego.com/courses/system-design-interview/design-a-chat-system

[73] Group Membership Management: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[74] Thumbnail Generation: https://stackoverflow.com/questions/73326665/architecture-of-a-simple-chat-web-app-at-scale

[75] Cursor-based Pagination: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[76] Offset vs Cursor: https://bytebytego.com/courses/system-design-interview/design-a-chat-system

[77] Slack's Cursor Pagination: https://newsletter.systemdesign.one/p/messaging-architecture

[78] Batch Read Receipts: https://www.designgurus.io/blog/design-chat-application

[79] Read Receipts: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[80] Discord's Read Receipts: https://discord.com/blog/how-discord-stores-trillions-of-messages

[81] Slack's Architecture: https://newsletter.systemdesign.one/p/messaging-architecture

[82] Slack's Cellular Architecture: https://www.cncf.io/case-studies/slack/

[83] WhatsApp's Erlang Architecture: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[84] WhatsApp's 50 Engineers: https://newsletter.systemdesign.one/p/messaging-architecture

[85] Mnesia Database: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[86] WhatsApp's Design Philosophy: https://www.designgurus.io/blog/design-chat-application

[87] TLS Protocol: https://www.cloudflare.com/learning/ssl/transport-layer-security-tls/

[88] Encryption in Transit: https://aws.amazon.com/security/encryption-in-transit/

[89] Encryption at Rest: https://aws.amazon.com/security/encryption-at-rest/

[90] Data Breach Costs: https://www.ibm.com/reports/data-breach

[91] End-to-End Encryption: https://signal.org/docs/

[92] X3DH Protocol: https://signal.org/docs/specifications/x3dh/

[93] Double Ratchet Algorithm: https://signal.org/docs/specifications/doubleratchet/

[94] Double Ratchet Explained: https://sentientrant.com/cybersecurity/signal-protocol-whatsapp-encryption

[95] SPQR Post-Quantum Ratchet: https://signal.org/blog/spqr/

[96] Key Registration: https://signal.org/docs/specifications/x3dh/

[97] Safety Numbers: https://signal.org/blog/safety-number-updates/

[98] Key Transparency: https://signal.org/blog/key-transparency/

[99] Key Recovery: https://signal.org/blog/secure-value-recovery/

[100] Cloud Backups: https://signal.org/blog/secure-value-recovery/

[101] E2EE Trade-offs: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[102] JWT Best Practices: https://auth0.com/blog/refresh-tokens-what-are-they-and-when-to-use-them/

[103] JWT Security: https://www.ionos.com/digitalguide/server/know-how/mongodb-vs-dynamodb

[104] OAuth 2.0: https://oauth.net/2/

[105] XSS Prevention: https://owasp.org/www-community/attacks/xss/

[106] Typing Indicators: https://ably.com/blog/chat-app-architecture

[107] Typing Indicator Debouncing: https://codefarm0.medium.com/designing-a-real-time-chat-app-whatsapp-slack-bf17912356d7

[108] Redis Pub/Sub for Typing: https://www.rst.software/blog/chat-app-architecture

[109] Typing Indicator Best Practices: https://www.hellointerview.com/learn/system-design/problem-breakdowns/whatsapp

[110] Typing Indicator Performance: https://bytebytego.com/courses/system-design-interview/design-a-chat-system
