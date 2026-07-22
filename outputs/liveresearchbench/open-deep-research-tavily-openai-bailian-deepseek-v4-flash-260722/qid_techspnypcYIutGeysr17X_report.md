# Designing a Highly Available, Horizontally Scalable Chat Application for Millions of Concurrent Users

## Introduction

Building a chat application that serves millions of concurrent users is a classic distributed systems engineering challenge. The system must handle real-time bidirectional communication, store vast amounts of message history, support media sharing, and provide strong reliability guarantees—all while remaining secure and available. This report provides a comprehensive architectural blueprint for such a system, covering every layer from the client connection to the database, with detailed explanations aimed at junior developers who want to understand how these systems work in practice.

The architecture described here is **microservices-based** and **horizontally scalable**, meaning you can add more servers to handle more users rather than upgrading a single machine. Every component is designed with redundancy, fault tolerance, and the ability to scale independently.

---

## Section 1: Core Architecture Components

### 1.1 High-Level Architecture Overview

A chat application for millions of users requires a **layered architecture** where each layer has a specific responsibility and can scale independently. The major layers are:

- **Client Layer:** Web, mobile, and desktop applications that connect to the backend via WebSockets or HTTP.
- **Load Balancer / Gateway Layer:** Distributes incoming connections across pools of servers. Handles TLS termination and routing.
- **WebSocket / Real-Time Connection Layer:** A pool of servers that maintain persistent, bidirectional connections with clients. This is the heart of the real-time experience.
- **Application / API Layer:** Stateless REST or gRPC servers handling authentication, profile management, message history retrieval, media uploads, and other request-response operations.
- **Messaging / Queue Layer:** A distributed message queue (e.g., Apache Kafka, RabbitMQ, NATS) that decouples message producers from consumers, ensuring reliable delivery and buffering during traffic spikes.
- **State / Presence Layer:** A fast in-memory data store (typically Redis) for tracking online/offline presence, user-to-server mappings, typing indicators, and lightweight session data.
- **Database Layer:** A combination of databases—an OLTP database for user accounts and metadata, and a wide-column or document database for message history. A search engine (e.g., Elasticsearch) may be added for full-text search.
- **Media Storage Layer:** Object storage (e.g., Amazon S3, Google Cloud Storage) with a Content Delivery Network (CDN) for serving images, videos, and files with low latency worldwide.
- **Caching Layer:** Redis or Memcached for caching frequently accessed data such as conversation metadata, member lists, and recent messages.

The key architectural principle is that **every component should be stateless where possible**. Stateless services can be scaled horizontally by simply adding more instances behind a load balancer. Stateful components (databases, message queues, caches) are clustered and partitioned so that they too can scale.

### 1.2 The Messaging Layer: How a Message Flows from Sender to Receiver

The message flow is the most critical path in the system. Here is a detailed, step-by-step walkthrough of how a single message travels from the sender's device to the recipient's device in a queue-based architecture.

**Step 1 — Client Sends the Message**

The sender's client constructs a message payload containing:
- `conversation_id` — the unique identifier of the chat room or direct message thread
- `sender_id` — the authenticated user's identifier
- `message_type` — text, image, video, file, etc.
- `content` — the actual message body (or a reference to media)
- `client_timestamp` — the time the message was created on the client device
- `idempotency_key` — a **client-generated UUID** that uniquely identifies this message

The client sends this payload to the server via the WebSocket connection or as an HTTP POST request to the API gateway. The idempotency key is critical for ensuring that duplicate messages are not processed if the client retransmits due to a network timeout.

**Step 2 — WebSocket Server Receives and Validates**

The WebSocket server (or a dedicated API server) receives the message and performs several validation checks:
- Verifies the sender's authentication token (e.g., JWT)
- Checks that the sender is a member of the specified conversation
- Validates that the message content is within size limits
- Ensures the message format is correct

If validation passes, the server publishes the message to a **distributed message queue** (e.g., Apache Kafka). This is a critical design decision: the WebSocket server does not directly write to the database or deliver to recipients. Instead, it hands off the message to the queue, which acts as a reliable buffer and decouples the producer from the consumers.

**Step 3 — Message Queue Ingestion**

The message is published to a Kafka topic such as `incoming-messages`. Kafka is chosen for this role because it provides:
- **High Throughput:** A Kafka cluster can handle millions of messages per second.
- **Durability:** Messages are written to disk and replicated across multiple brokers, so no messages are lost if a server crashes.
- **Ordering Guarantees:** Messages within a single partition are strictly ordered. The message is partitioned by a hash of `conversation_id`, ensuring that all messages for a given conversation land in the same partition and are processed in order.
- **Exactly-Once Semantics:** When combined with idempotent producers and transactional consumers, Kafka can provide exactly-once delivery guarantees.
- **Horizontal Scalability:** Partitions can be added to increase throughput, and consumer groups can be scaled by adding more consumer instances.

**Step 4 — Message Consumer / Processor**

A consumer group (e.g., a Kafka consumer running in a Kubernetes pod) reads messages from the `incoming-messages` topic. This consumer is responsible for several critical operations:

**Deduplication:** Before processing the message, the consumer checks the idempotency key against a Redis set or a database table. If the key has already been processed, the message is discarded (or the existing result is returned). This is how the system achieves **exactly-once processing** despite the possibility of duplicate deliveries from the queue.

**Persistence:** The consumer writes the message to the message history database. For a chat application at scale, this database is typically Apache Cassandra, ScyllaDB, or Amazon DynamoDB—all of which are designed for high write throughput and horizontal scaling. The message is stored with a composite primary key of `(conversation_id, message_timestamp, message_id)` to enable efficient range queries for message history.

**Fan-Out:** For group chats, the consumer determines the fan-out strategy:
- **Small groups** (e.g., fewer than 100 members): The message is written to each member's inbox (fan-out on write). This makes reads very fast—each user simply reads their own inbox—but the write cost is proportional to the number of members.
- **Large groups** (100+ members): The message is written once to the conversation timeline (fan-out on read). When a user opens the conversation, the system fetches messages from the timeline. This is more efficient for large groups.
- **Hybrid approach:** A configurable threshold determines which strategy to use for each conversation.

**Routing to Recipients:** The consumer looks up the current WebSocket server for each online recipient using the presence data stored in Redis. It then publishes the message to an internal delivery channel (e.g., a Redis pub/sub channel or a dedicated Kafka topic) that the target WebSocket server subscribes to.

**Step 5 — Delivery to the Recipient**

The recipient's WebSocket server receives the message from the internal delivery channel and sends it to the recipient's client over the persistent WebSocket connection. The recipient's client acknowledges receipt by sending an **ACK message** back to the server.

**Step 6 — Acknowledgment and Retry**

The server tracks delivery statuses: `sent` (the message was dispatched), `delivered` (the recipient's client acknowledged receipt), and `read` (the recipient viewed the message). If the recipient is offline, the message is stored in the database as "pending delivery." When the recipient comes online, the client fetches all pending messages from the history database and sends ACKs for each one.

If the sender does not receive a delivery confirmation within a timeout, the client can retransmit the message with the same idempotency key. The server deduplicates the retransmission, so the recipient sees only one copy of the message.

### 1.3 Real-Time Event Handling: WebSockets, Long-Polling, and SSE

Real-time communication is the essence of a chat application. There are several technologies for achieving this, each with different trade-offs.

**WebSockets (Recommended for Chat)**

WebSockets provide a full-duplex, persistent TCP connection between the client and server. Once established, either party can send data at any time with very low latency. This is the ideal technology for chat applications.

**How WebSockets Scale:**

WebSocket servers are deployed as a pool behind a load balancer. The load balancer must support **sticky sessions** (also called session affinity) to ensure that all frames from a single client are routed to the same server. This is typically achieved using a layer-4 load balancer that routes based on source IP, or a layer-7 load balancer that reads a session cookie.

Each WebSocket server maintains an in-memory map of `user_id → WebSocket connection`. When a client reconnects to a different server (e.g., after a server restart), the new server must learn about the user's state. This is solved by storing the user-to-server mapping in Redis: a key like `user:{user_id}:server` maps to the current WebSocket server's identifier. When a message needs to be delivered, the system looks up the recipient's current server in Redis and sends the message to that server via an internal channel.

**WebSocket Connection Lifecycle:**

1. The client connects to the load balancer on port 443 (WSS, WebSocket Secure).
2. The load balancer forwards the WebSocket upgrade request to one of the WebSocket server instances.
3. The WebSocket server authenticates the user (e.g., via a JWT token in the query string or the first message).
4. The server registers the user in the presence system: `SET presence:{user_id} "{'server_id':'ws-3','last_seen':1234567890}" EX 60`. The TTL (60 seconds) ensures that stale entries are automatically cleaned up if the server crashes.
5. The server maintains an event loop per connection to handle incoming messages and heartbeats.
6. On disconnect, the server removes the user from the presence system and updates the user's status to "offline" or "last seen at timestamp."

**Long-Polling (Fallback for WebSockets)**

Long-polling is a technique where the client makes an HTTP request to the server, and the server holds the request open until new data is available or a timeout occurs. When new data arrives, the server sends the response and the client immediately makes a new request. This creates a continuous loop that simulates real-time communication.

Long-polling is used as a fallback when WebSockets are not available—for example, behind restrictive corporate firewalls or in certain enterprise environments. It is much less efficient than WebSockets due to HTTP overhead, higher latency, and increased server resource usage. It can be scaled by adding more API servers behind a load balancer.

**Server-Sent Events (SSE) for One-Way Updates**

SSE is a standard that allows a server to push data to a client over a single HTTP connection. Unlike WebSockets, SSE is unidirectional (server to client only). It is simpler than WebSockets (native browser API, no library required) and is suitable for features like notifications, presence updates, and typing indicators from the server to the client. However, the client must still use HTTP POST or WebSocket to send data to the server.

### 1.4 Exactly-Once Message Delivery: The Core Challenge

Achieving true exactly-once delivery in a distributed system is extremely difficult. Most production chat systems settle for **at-least-once delivery with idempotent processing**, which approximates exactly-once from the user's perspective. Here is how it works.

**The Idempotency Key Pattern**

Every message sent by a client includes a **client-generated UUID** called the idempotency key. This key is unique per message and is generated by the client before sending. The server stores the set of idempotency keys it has processed, typically in a Redis set with a TTL (e.g., 7 days) to prevent unbounded growth.

When a message arrives, the server checks if the idempotency key has already been processed:
- If **yes**, the server returns the existing result (e.g., "message already sent, here is the message ID").
- If **no**, the server processes the message as new and stores the idempotency key.

**How the Client Retransmits**

The client sends a message and waits for an acknowledgment from the server. If the acknowledgment does not arrive within a timeout (e.g., 5 seconds), the client retransmits the message with the **same idempotency key**. The server deduplicates the retransmission, so the recipient sees only one copy.

**Kafka's Exactly-Once Semantics**

Kafka supports exactly-once semantics (EOS) through a combination of features:
- **Idempotent producers:** Configured with `enable.idempotence=true`, the producer automatically retries and deduplicates messages.
- **Transactional consumers:** The consumer uses `isolation.level=read_committed` and stores offsets in a transactional store, ensuring that messages are processed exactly once.

**Important Caveat for Chat Applications**

Even with these mechanisms, perfect exactly-once delivery is rarely achieved in practice for chat systems. The industry standard is **at-least-once delivery with idempotent processing on the consumer side**. This means a message might be delivered twice to the consumer, but it will only be stored and forwarded once. The user sees exactly one copy of each message, which is the operational definition of exactly-once delivery.

### 1.5 Typing Indicators in a Distributed System

Typing indicators are a high-frequency, ephemeral feature that tells other users when someone is typing. In a distributed system, this is challenging because the events are frequent and must be processed quickly, but they can tolerate some loss (if one event is lost, the next one will arrive and update the indicator).

**Client-Side Behavior**

When the user starts typing, the client sends a `typing:start` event to the WebSocket server. While the user continues typing, the client sends a `typing:update` event every 3 seconds to keep the indicator alive. When the user stops typing or sends a message, the client sends a `typing:stop` event. The client also sets a local timeout: if no update is received within 5 seconds, the indicator is removed.

**Server-Side Design**

The WebSocket server receives the typing event and publishes it to a **dedicated Redis pub/sub channel** (e.g., `typing:{conversation_id}`). Other WebSocket servers subscribe to these channels. When a server receives a typing event, it looks up the recipients of the conversation who are connected to that server and forwards the event to their WebSocket connections.

An alternative approach uses Redis keys with a TTL: `SET typing:{conversation_id}:{user_id} "{'timestamp':...}" EX 5`. When a recipient's server needs to know who is typing, it reads all keys matching `typing:{conversation_id}:*`. This is simpler but requires polling.

**Rate Limiting**

Typing events are high-frequency. The server should rate-limit the publication of typing events to Redis (e.g., at most 1 event per user per 2 seconds). The client is responsible for throttling its own events, but the server enforces it as a safety measure.

**Scaling Considerations**

For large group chats, typing indicators are often disabled or shown only for a subset of users (e.g., "Alice, Bob, and 5 others are typing...") to avoid overwhelming the system. The TTL-based approach is particularly useful here because it automatically cleans up stale indicators when a server crashes or a user disconnects.

### 1.6 Message History Storage and Retrieval

Message history is one of the most write-heavy workloads in a chat application. Every message sent by every user must be stored durably and retrieved efficiently when users scroll back through their conversation history.

**Database Design for Message History**

The recommended database for message history is a wide-column store like **Apache Cassandra, ScyllaDB, or Amazon DynamoDB**. These databases are designed for high write throughput and horizontal scaling, which is exactly what chat history requires.

The primary key design follows a pattern optimized for range queries:

```
Partition Key:  conversation_id
Clustering Key: message_timestamp, message_id
```

This design allows efficient queries like "Give me all messages in conversation X between time A and time B." The partition key ensures that all messages for a single conversation are stored on the same node (or set of nodes), making range queries fast. The clustering key ensures that messages are ordered by time within the partition.

**Time Bucketing to Avoid Hot Partitions**

A single very active conversation (e.g., a large group chat) can generate so many writes that it creates a "hot partition," overwhelming the node that stores it. To mitigate this, the partition key can be a combination of `conversation_id` and a **time bucket**:

```
Partition Key:  conversation_id + date_hour
Clustering Key: message_timestamp, message_id
```

For example, messages in the "general" chat room between 2:00 PM and 3:00 PM on July 22, 2026, would all be stored in partition `general:2026-07-22-14`. When reading history, the system queries all relevant buckets and merges the results. Bucket size can be adjusted based on the conversation's activity level.

**Caching Recent Messages**

Recent messages (e.g., the last 100 messages) are cached in Redis for fast retrieval. When a user opens a conversation, the client first fetches recent messages from the cache, then fills in any gaps from the database. The cache is populated when messages are written (write-through or write-around caching).

**Cursor-Based Pagination**

Message history is retrieved using **cursor-based pagination** rather than offset-based pagination. The cursor is the `message_id` or `timestamp` of the last message in the current page. A typical API call looks like:

```
GET /conversations/{id}/messages?cursor=msg_12345&limit=50
```

Cursor-based pagination avoids the "missing messages" problem that occurs with offset-based pagination when new messages are inserted between page loads.

**Full-Text Search**

If the chat application supports message search, a secondary index is built in **Elasticsearch**. The index stores `(conversation_id, message_content, sender_id, timestamp)`. When a user searches, the system queries Elasticsearch, retrieves matching message IDs, then fetches the full messages from the primary database.

**Data Retention and Archival**

Some chat applications retain messages forever, while others delete messages after a period (e.g., 30 days for ephemeral conversations). Data can be archived to cold storage (e.g., Amazon S3 Glacier) after the retention period, with a marker in the database pointing to the archive location.

### 1.7 Media Sharing: Images, Videos, and Files

Media sharing introduces unique challenges because files can be large and must be served with low latency to users around the world. The key design principle is to **avoid routing large files through the application servers**, which would create a bottleneck.

**The Upload Flow**

1. The client requests permission to upload a file by sending a request to the API server with the file size and type.
2. The API server authenticates the request, checks file size limits, and generates a **pre-signed URL** for the object storage (e.g., Amazon S3). The pre-signed URL is a time-limited URL that allows the client to upload the file directly to S3 without going through the application server.
3. The client uploads the file directly to S3 using the pre-signed URL (usually via HTTP PUT). S3 returns an ETag (MD5 hash) of the uploaded file.
4. The client sends a message with `type: "image"`, `media_url: "https://cdn.example.com/images/user_123/abc123.jpg"`, and metadata such as dimensions, file size, and thumbnail URL. The media URL is generated by the server based on the S3 object key and points to the **CDN**, not directly to S3.

**The Delivery Flow**

The CDN (e.g., CloudFront, Cloudflare, Fastly) caches the media file at edge locations around the world. When a recipient opens the message, their client requests the image from the CDN URL. If the CDN has the file cached, it serves it directly from the edge. If not, it pulls from the origin (S3), caches it, and serves it. This reduces latency for users far from the origin server.

**Thumbnails and Transcoding**

The server (or a separate media processing service) automatically generates thumbnails for images and transcodes videos to multiple resolutions (e.g., 360p, 720p, 1080p). This is typically done asynchronously: when a file is uploaded to S3, an S3 event triggers a Lambda function or a dedicated media processing service (e.g., FFmpeg running in a container). The processed files are stored back in S3 with predictable paths, and the message is updated with the new URLs.

**Security Considerations**

- Pre-signed URLs have a short expiration time (e.g., 5 minutes) to prevent abuse.
- Media URLs are not guessable—they contain random UUIDs or hash-based paths.
- The CDN can be configured with signed URLs or signed cookies for private media (e.g., in enterprise chat apps).
- File type validation is performed on both the client and server to prevent malicious uploads.

### 1.8 One-to-One vs Group Chat Routing

The architecture must handle both direct messages (one-to-one) and group conversations efficiently, and the optimal strategy differs for each.

**One-to-One Chat (Direct Messages)**

For one-to-one chats, the conversation ID is derived from the sorted user IDs (e.g., `conversation:userA:userB` or a hash of the two user IDs). This ensures that both users can query the same partition. The message is sent from user A to user B by looking up B's current server in Redis and forwarding the message directly. If B is offline, the message is stored in the conversation history and delivered when B comes online.

This is straightforward because there are only two participants. The write cost is O(1) per message, and the read cost is O(1) per user.

**Group Chat Routing**

Group chats introduce the fan-out problem: a message sent to a group of N members must be delivered to all N members. The choice of fan-out strategy depends on the group size.

**Fan-out on Write (for small groups, e.g., fewer than 100 members):** When a message is sent, it is written to each member's inbox (a separate row per member). This makes reads very fast (each user reads their own inbox) but the write cost is O(n) per message. This is the strategy used by Facebook Messenger for small groups.

**Fan-out on Read (for large groups, e.g., 100+ members):** The message is written once to the conversation timeline. When a user opens the conversation, they fetch from the timeline. This is more efficient for large groups because the write cost is O(1) per message, regardless of group size. The read cost is slightly higher because the user must fetch and filter the timeline, but this is acceptable. This is the strategy used by Slack and Discord for large channels.

**Hybrid Approach:** A configurable threshold (e.g., 100 members) determines which strategy to use. When a group crosses the threshold, the system can migrate from fan-out on write to fan-out on read.

---

## Section 2: Database Selection Comparison

Choosing the right database (or combination of databases) is one of the most consequential decisions in the architecture. No single database is optimal for all use cases in a chat application, so a **polyglot persistence** approach—using multiple databases for different purposes—is the standard practice.

### 2.1 The Three Categories of Databases

**Relational Databases (RDBMS):** PostgreSQL, MySQL, SQL Server, Oracle. These store data in tables with predefined schemas and support ACID transactions (Atomicity, Consistency, Isolation, Durability). They are excellent for data that has complex relationships and requires strong consistency guarantees.

**NoSQL Document Databases:** MongoDB, Couchbase, Firebase Firestore. These store data in flexible, JSON-like documents. They are schema-less (or schema-flexible), horizontally scalable, and designed for high write throughput.

**Distributed NoSQL / Wide-Column Databases:** Apache Cassandra, ScyllaDB, Amazon DynamoDB, Google Bigtable. These are designed from the ground up for horizontal scaling across many nodes, with high write throughput and automatic replication. They sacrifice some consistency guarantees (typically offering eventual consistency) in exchange for availability and partition tolerance.

### 2.2 Detailed Comparison Across Key Dimensions

The following table compares the three categories across the dimensions that matter most for a chat application: scalability, latency, consistency, and operational complexity.

| Dimension | Relational (PostgreSQL) | Document (MongoDB) | Distributed (Cassandra/DynamoDB) |
|-----------|------------------------|-------------------|----------------------------------|
| **Horizontal Scaling** | Difficult. Requires manual sharding or read replicas. Writes are constrained to a single primary node. | Good. Native sharding with automatic data distribution. | Excellent. Designed for horizontal scaling from day one. Linear scalability with more nodes. |
| **Write Throughput** | Limited by the primary node's capacity. Can be improved with connection pooling and replication, but writes are ultimately single-node. | Good. Writes are distributed across shards. | Excellent. Each node can accept writes independently. Can handle millions of writes per second across a cluster. |
| **Read Latency (Recent Messages)** | Very low when using caching and indexes. Direct reads from primary or read replicas. | Low. Can read from any replica. | Very low. Reads can be served from any replica in the cluster. |
| **Read Latency (Historical Messages)** | Low for indexed queries. Can degrade with very large tables (billions of rows) without careful partitioning. | Moderate. Range queries across shards can be slower. | Very low. Wide-column design is optimized for range queries by partition key. |
| **Consistency Model** | Strong consistency (ACID). All reads see the latest write. Reads are linearizable. | Tunable. Default is strong consistency for single-document reads, but cross-document operations are not atomic. | Tunable. Typically eventual consistency by default, but supports strong consistency at the cost of latency. Often uses "last-write-wins" conflict resolution. |
| **Data Model Flexibility** | Rigid schema. Changes require migrations. | Flexible schema. Documents can vary in structure. | Flexible schema. Columns can be added dynamically. |
| **Complex Relationships** | Excellent. Joins, foreign keys, and transactions make relational data easy to model. | Poor. Joins are not supported natively. Data is often denormalized. | Very poor. No joins. Data must be modeled based on access patterns (query-first design). |
| **Operational Complexity** | Moderate. Requires careful tuning, index management, and connection pooling. | Moderate. Requires shard key selection and index management. | High. Requires careful data modeling, cluster management, and understanding of tunable consistency. |
| **Best For** | User accounts, authentication, metadata, settings, any data with strong consistency requirements and complex relationships. | Rapid prototyping, flexible schemas, moderate scale. | Message history, event logs, time-series data, any data requiring high write throughput and horizontal scaling. |

### 2.3 Recommended Database Strategy for Chat Applications

The standard approach is **polyglot persistence**, using three different databases for three different purposes:

**1. PostgreSQL for User Data and Metadata**

PostgreSQL is the best choice for user accounts, authentication, profile information, contact lists, and conversation metadata (who is in which conversation, when was the conversation created, etc.). This data has complex relationships (users have contacts, users belong to conversations, conversations have messages) and requires strong consistency (you don't want two users to register with the same username). PostgreSQL's ACID transactions ensure data integrity.

PostgreSQL can be scaled using read replicas for read-heavy workloads and connection pooling (e.g., PgBouncer) to handle many concurrent connections. For very large deployments, tools like Citus (a PostgreSQL extension) can distribute data across multiple nodes.

**2. Cassandra / ScyllaDB / DynamoDB for Message History**

Message history is the most write-heavy workload in the system. Every message sent by every user across all conversations must be stored durably and retrieved efficiently. A distributed wide-column database is ideal for this use case because:
- It can handle millions of writes per second across a cluster.
- It is designed for the time-series data pattern (messages are ordered by time).
- It provides linear scalability—adding more nodes doubles the throughput.
- It replicates data automatically across nodes and availability zones.

The data model follows the pattern described in Section 1.6: partition key on `conversation_id` (or `conversation_id + time_bucket`) and clustering key on `message_timestamp + message_id`.

**3. Elasticsearch for Full-Text Search**

If the application supports searching through message history, Elasticsearch provides the necessary full-text indexing and search capabilities. It indexes `(conversation_id, message_content, sender_id, timestamp)` and returns matching message IDs, which are then fetched from the primary database.

### 2.4 Trade-Offs and Justification

**Why not use PostgreSQL for everything?** PostgreSQL's write throughput is limited by the primary node. A single PostgreSQL instance can handle perhaps 10,000-50,000 writes per second under optimal conditions. A chat application with millions of users sending messages could easily exceed this. Additionally, PostgreSQL's data model for time-series data requires careful partitioning and index management to avoid performance degradation as the table grows to billions of rows.

**Why not use Cassandra for everything?** Cassandra is not designed for complex relational queries or strong consistency. User accounts have relationships (contacts, groups, permissions) that are difficult to model in Cassandra's query-first paradigm. Furthermore, Cassandra's eventual consistency model is not suitable for operations like user registration, where you must ensure that a username is unique.

**Why not use MongoDB for everything?** MongoDB offers a good balance of flexibility and scalability, and it is a viable option for chat applications at moderate scale. However, at very large scale (millions of users, billions of messages), MongoDB's sharding and replication can become complex to manage, and its write throughput does not match Cassandra's. MongoDB is a solid choice for teams that want a single database for both metadata and messages, but it requires careful shard key selection and index management.

---

## Section 3: Scalability Mechanisms

A system designed for millions of concurrent users must scale horizontally—adding more servers to handle increased load rather than upgrading a single server. This section covers the key scalability mechanisms: sharding, partitioning, and load balancing.

### 3.1 Sharding Strategies

Sharding means splitting data or user connections across multiple servers so that each server handles only a subset of the total load. There are three primary sharding strategies for a chat application.

**Sharding by User ID**

Each user is assigned to a specific shard based on a hash of their user ID. All messages sent by or to that user are handled by that shard. This strategy is simple to implement—you can use `hash(user_id) % number_of_shards`—and it ensures that all of a user's data is on one server, making queries fast.

However, this strategy has a significant drawback: if a user is in a chat room with many other users, messages must be routed across shards (one shard for each user in the room). This creates a "fan-out" problem where a single message generates many cross-shard operations. Additionally, very active users can create hotspots on their assigned shard.

**Sharding by Chat Room ID**

Each chat room (group conversation, channel, etc.) is assigned to a specific shard based on a hash of the room ID. All messages in that room are processed on a single server, eliminating the cross-shard routing problem for room-based messages. This is the most common strategy for chat applications because it provides strong ordering guarantees within a conversation and avoids the fan-out problem.

The main drawback is the "hot room" problem: a single room with millions of users (e.g., a celebrity AMA, a large company all-hands) can overload a single shard. This can be mitigated by splitting very large rooms into "sub-rooms" or using a separate streaming infrastructure for large broadcast rooms.

**Sharding by Geographic Region**

Users are assigned to a shard (or cluster of shards) based on their geographic location. All users in North America go to the US-East cluster, users in Europe go to the EU-West cluster, etc. This provides lower latency (users connect to the nearest data center) and helps with data residency compliance (GDPR, etc.). Regional failures are isolated to that region.

The drawback is that cross-region chat (a user in the US chatting with a user in Europe) requires message routing between regions, which adds latency and complexity. Data replication across regions is needed for global features like viewing message history when traveling.

**Recommended Approach: Shard by Chat Room ID, with Regional Sharding for Multi-Region Deployments**

For most chat applications, sharding by chat room ID is the best starting point. It provides strong ordering, avoids the fan-out problem, and is simple to implement with consistent hashing. For global deployments, add regional sharding on top: each region has its own cluster of shards, and cross-region messages are routed through a global message queue.

### 3.2 Consistent Hashing

Consistent hashing is a technique used to distribute data across a dynamic set of servers. It solves the problem of traditional hash-based sharding (e.g., `hash(key) % N`), where adding or removing a server requires rehashing almost all keys and moving a large amount of data.

**How It Works:**

1. A "hash ring" is created—a circle of hash values, typically from 0 to 2^32 - 1.
2. Each server is assigned one or more positions on the ring by hashing the server's IP address or name.
3. Each data key (e.g., `chat_room_id`) is hashed, and the data is stored on the nearest server clockwise from the key's hash position.
4. When a server is added or removed, only the keys immediately adjacent to that server on the ring need to be moved—not all keys.

**Virtual Nodes:** Each physical server can be represented by multiple "virtual nodes" on the ring to improve load distribution. Without virtual nodes, if servers are unevenly spaced on the ring, some servers may end up with significantly more data than others.

**Why Consistent Hashing Matters for Chat:**

When you add a new chat server to handle more users, consistent hashing minimizes the disruption—only a small fraction of chat rooms need to be reassigned. This allows the system to scale up (and down) dynamically without large-scale data migrations.

### 3.3 Load Balancing Techniques

Load balancing distributes incoming traffic across multiple servers to prevent any single server from being overwhelmed.

**DNS-Based Routing**

A DNS server returns multiple IP addresses for a single domain name. Clients randomly pick one of these IPs to connect to. This is simple and free, but it has no awareness of server health (if a server goes down, clients may still receive its IP) and changes take time to propagate due to DNS caching. DNS-based routing is best used for initial connection routing, combined with other load balancers.

**Application-Layer Load Balancers (Layer 7)**

A load balancer (e.g., HAProxy, NGINX, AWS ALB) sits in front of the chat servers and inspects the content of each request (HTTP headers, WebSocket path, cookies) to decide which server to route to. These load balancers support:
- **Sticky sessions:** All requests from a specific user are routed to the same server, which is essential for WebSocket connections.
- **Health checks:** The load balancer automatically stops sending traffic to unhealthy servers.
- **SSL termination:** The load balancer handles TLS encryption/decryption, offloading this work from the application servers.
- **Rate limiting:** The load balancer can limit the number of requests from a single IP address.

The main drawback is that the load balancer adds a hop (latency) and can become a bottleneck if not properly scaled. For very large deployments, multiple load balancers are deployed in a cluster.

**Consistent Hashing for Routing (Without a Central Load Balancer)**

Instead of a traditional load balancer, consistent hashing can be used at the application level. Each chat server is on the hash ring. When a client wants to connect to a chat room, the client asks a "router" service (or looks up the room's server via a consistent hashing function) and then opens a WebSocket directly to that server. This eliminates the central load balancer bottleneck and allows the routing decision to be made by the client or a lightweight coordination service.

This approach requires a coordination service (e.g., ZooKeeper, etcd) to maintain the hash ring and notify clients/servers of changes. It is more complex to implement but provides better scalability and eliminates the single point of failure.

### 3.4 Horizontal Scaling of Specific Components

**WebSocket Servers:** These are scaled by adding more instances behind a load balancer with sticky sessions. Each server maintains a map of user connections in memory. The user-to-server mapping is stored in Redis so that messages can be routed to the correct server.

**API Servers:** These are stateless and can be scaled trivially behind a load balancer. Each server handles authentication, profile management, and other request-response operations.

**Message Queue (Kafka):** Kafka scales by adding more brokers and increasing the number of partitions. Each partition is a unit of parallelism—more partitions mean more consumers can process messages in parallel. The partition count should be set based on the expected throughput and the number of consumer instances.

**Database (Cassandra/DynamoDB):** These databases scale by adding more nodes. Cassandra uses consistent hashing to distribute data across nodes automatically. DynamoDB scales by increasing the read and write capacity units or by using auto-scaling.

**Redis:** Redis can be scaled using Redis Cluster, which distributes data across multiple nodes using consistent hashing. For read-heavy workloads, read replicas can be added. For write-heavy workloads, the cluster can be scaled by adding more shards.

---

## Section 4: High Availability and Fault Tolerance

High availability (HA) means the system remains operational even when some components fail. Fault tolerance means the system can continue operating, possibly at a reduced capacity, when failures occur. This section covers the strategies and patterns used to achieve both.

### 4.1 High Availability Patterns

**Active-Active Deployment**

In an active-active deployment, all servers are actively handling traffic at all times. If one server fails, traffic is simply redistributed to the remaining servers. This provides the best resource utilization and the fastest failover, but it is more complex to manage because data consistency must be maintained across all active servers.

For a chat application, the WebSocket server layer and the API server layer are typically active-active. The database layer can also be active-active if using a multi-leader replication model (e.g., Cassandra, DynamoDB).

**Active-Passive Deployment**

In an active-passive deployment, one server (or set of servers) is active, handling all traffic. One or more servers are passive (standby), receiving replicated data but not handling traffic. If the active server fails, the passive server is promoted to active, and traffic is redirected to it.

This pattern is simpler to implement and provides stronger consistency guarantees (only one writer), but it wastes capacity (passive servers sit idle) and failover takes time. Active-passive is commonly used for relational databases (e.g., PostgreSQL with streaming replication) and for stateful components where consistency is critical.

**Multi-Region Deployment**

The application is deployed in multiple geographic regions (e.g., US-East, EU-West, Asia-Pacific). Each region has its own set of servers, databases, and load balancers. Users are routed to the nearest region using DNS-based geographic routing (e.g., AWS Route 53, Google Cloud DNS, Cloudflare). If a region fails, DNS is updated to route traffic to the next closest region.

Data replication across regions is typically asynchronous to avoid adding latency to write operations. Each region has a local copy of the data, so reads are fast and local. Conflict resolution is needed when a user sends messages from two different regions simultaneously (e.g., while traveling). Common strategies include last-write-wins (LWW) and Conflict-free Replicated Data Types (CRDTs).

### 4.2 Database Replication

**Leader-Follower Replication (Active-Passive)**

One database node (the leader) accepts all writes. One or more follower nodes replicate the leader's data (asynchronously or synchronously) and serve read-only queries. If the leader fails, one of the followers is promoted to leader. This is the standard replication model for PostgreSQL, MySQL, and many other relational databases.

**Multi-Leader Replication (Active-Active)**

Multiple database nodes accept writes, and changes are replicated between them (often asynchronously). This provides higher write throughput and better availability (if one leader fails, other leaders can still accept writes). Conflict resolution is complex—two users may edit the same data on different leaders simultaneously. This is the standard replication model for Cassandra, DynamoDB, and ScyllaDB.

**Leaderless Replication**

In a leaderless model (used by Cassandra and DynamoDB), any node can accept reads and writes. Writes are sent to multiple nodes (configurable as the replication factor), and reads are sent to multiple nodes to ensure the latest data is returned. This provides the highest availability and fault tolerance but requires careful tuning of consistency levels.

### 4.3 Fault Tolerance Strategies

**Graceful Degradation**

When a component fails, the system degrades functionality in a controlled way rather than crashing entirely. For example:
- If the database is down, users can still see their current chat session (cached in memory), but new messages are queued locally and will be sent when the database recovers.
- If the message queue is down, messages are sent directly to the recipient's server (if the recipient is online) or stored in a local buffer.
- If the push notification service is unavailable, users who are not currently connected will receive their messages when they next open the app.

Each feature should have a defined "degraded mode" that is clearly communicated to the user.

**Retry Mechanisms with Exponential Backoff**

When a request to a service fails, the client waits a certain amount of time before retrying. Each subsequent retry waits longer (exponentially) than the previous one. The formula is:

```
wait_time = base_delay * (2^attempt) + random_jitter
```

For example, with a base delay of 100ms:
- Attempt 1: 100ms + jitter
- Attempt 2: 200ms + jitter
- Attempt 3: 400ms + jitter
- Attempt 4: 800ms + jitter
- ...up to a maximum delay (e.g., 30 seconds)

Jitter (randomness) prevents the "thundering herd" problem, where all clients retry at exactly the same time and overwhelm the recovering service.

**Circuit Breaker Pattern**

A circuit breaker monitors calls to a downstream service (e.g., a database, a message queue, an external API). If the service fails too many times in a row, the circuit breaker "opens"—all subsequent calls fail immediately without even attempting the call. After a timeout period, the circuit breaker transitions to "half-open" and allows a limited number of test calls. If they succeed, the circuit breaker closes. If they fail, it goes back to open.

This pattern prevents cascading failures: if the database is slow or down, the circuit breaker stops the chat server from waiting forever for a response. Instead, the server can fail fast and return a cached response, queue the message for later delivery, or show an error to the user.

**Crash Recovery**

When a server crashes and restarts, it must recover its state. Strategies include:
- **Persistent sessions:** Store session state in Redis rather than in memory. When the server restarts, it reads the session data from Redis.
- **Event sourcing:** Store all events (messages sent, users joined, users left) in an append-only log. When a server restarts, it replays the events to rebuild its state.
- **Heartbeat-based recovery:** The coordination service (ZooKeeper/etcd) knows which users/rooms were assigned to the crashed server. When the server restarts, it re-registers, and the coordination service re-assigns the users/rooms to it or to other servers.

**Data Replication Across Availability Zones**

Availability Zones (AZs) are physically separate data centers within a cloud region. Data is replicated across multiple AZs so that if one AZ fails (power outage, cooling failure, network cut), the data is still available in another AZ. Synchronous replication ensures zero data loss but adds latency (typically 1-2ms between AZs). Asynchronous replication is faster but may lose recently written data if the primary AZ fails before replication completes.

### 4.4 Coordination Services

Distributed coordination services like ZooKeeper and etcd provide essential infrastructure for highly available systems:
- **Leader election:** Choosing which server is the primary for a given shard or task.
- **Service discovery:** Registering which servers are alive and what they are responsible for.
- **Configuration management:** Storing and distributing configuration changes.
- **Distributed locking:** Ensuring only one server performs a critical operation at a time.
- **Consistent hashing ring management:** Maintaining the ring of servers and notifying servers when the ring changes.

These services are typically deployed as a cluster of three or five nodes to provide their own high availability.

---

## Section 5: Security and Encryption Design

Security in a chat application must protect messages in transit, at rest, and ideally from end to end (meaning the server itself cannot read the messages). This section covers all three layers.

### 5.1 Encryption in Transit

Encryption in transit protects data as it moves between the client and the server. Without it, anyone on the same network (coffee shop WiFi, ISP, attacker on the router) can read messages.

**TLS (Transport Layer Security)**

TLS is the protocol that powers HTTPS. It provides:
- **Encryption:** No one can read the data in transit.
- **Authentication:** The client verifies the server's identity via certificates, ensuring the client is talking to the real server.
- **Integrity:** Data cannot be modified in transit without detection.

For a chat application:
- All REST API endpoints must use HTTPS (TLS over TCP).
- WebSocket connections use **WSS** (WebSocket Secure), which is WebSocket over TLS.

**Recommended TLS Configuration:**
- TLS 1.2 or 1.3 only (no TLS 1.0/1.1, no SSL).
- Strong cipher suites (e.g., `ECDHE-ECDSA-AES128-GCM-SHA256`).
- HTTP Strict Transport Security (HSTS) header to force clients to use HTTPS.
- Certificates from a trusted Certificate Authority (Let's Encrypt provides free certificates).

### 5.2 Encryption at Rest

Encryption at rest protects data stored on disk—in databases, file systems, and backups. If someone steals the server's hard drive or gains database access, they still cannot read the data.

**Database Encryption**

Two main approaches:
- **Transparent Data Encryption (TDE):** The database engine encrypts data before writing to disk and decrypts it when reading. The application does not need to change code. This is supported by PostgreSQL, MySQL, SQL Server, and Oracle.
- **Application-level encryption:** The application encrypts specific columns or fields before sending data to the database. This provides stronger protection (even the database administrator cannot read the data) but requires more code.

For E2EE chat applications, messages are already encrypted by the client, so the server stores ciphertext. However, other data (user profiles, metadata, tokens) should still be encrypted at rest.

**File Storage Encryption**

Media files (images, videos, documents) stored in object storage (S3, GCS) should be encrypted. Cloud providers offer several options:
- **Server-Side Encryption (SSE-S3):** The cloud provider manages the keys and encrypts objects automatically.
- **SSE-KMS:** You control the encryption keys via a key management service (e.g., AWS KMS).
- **Client-Side Encryption:** You encrypt files before uploading—the server never sees plaintext. This is recommended for E2EE applications.

### 5.3 End-to-End Encryption (E2EE)

E2EE ensures that only the sender and the intended recipient(s) can read the message. The server (and anyone who compromises the server) cannot read it. This is the most secure option and is increasingly expected by users.

**The Core Principle**

```
Sender's Device                    Server                     Recipient's Device
     │                               │                              │
     │  Plaintext: "Hello!"          │                              │
     │  ─────encrypt─────►           │                              │
     │                               │                              │
     │                  Encrypted message (ciphertext)              │
     │  ──────────────────────────────────────────────────►         │
     │                               │                              │
     │                            ─────decrypt─────►               │
     │                           Plaintext: "Hello!"                │
     │                               │                              │
     │     Server CANNOT decrypt     │                              │
     │     (no keys to decrypt)      │                              │
```

**The Signal Protocol (The Gold Standard)**

The Signal Protocol, used by Signal, WhatsApp, and Google Messages, is the most widely deployed E2EE protocol for messaging. It combines three key algorithms:

**X3DH (Extended Triple Diffie-Hellman):** Handles the initial key agreement between two parties who have never communicated before. Each user publishes pre-keys (public keys) to the server. When Alice wants to start a conversation with Bob, she fetches Bob's pre-key bundle from the server and uses it to compute a shared secret. Both parties derive the same root key from this shared secret.

**Double Ratchet Algorithm:** Provides ongoing encryption with forward secrecy and self-healing properties. The "ratchet" has two components:
- **Symmetric Ratchet:** Each message derives a new key from the previous one using a one-way function (hash). Even if a message key is compromised, the attacker cannot derive past or future keys.
- **DH Ratchet:** Each time a new message is received, the parties perform a new Diffie-Hellman exchange. This creates a new root key. If a session key is compromised, the next DH exchange "heals" the breach.

The result is:
- **Forward secrecy:** If a device is stolen today, the attacker cannot decrypt messages from yesterday.
- **Self-healing:** If a session key is compromised, one DH ratchet step later, the attacker is locked out again.

**Group Chat E2EE**

Group chats are harder because a message must be encrypted for all members. The Signal Protocol uses **Sender Keys**: each group member generates a random sender key, which is encrypted individually for each other member using their pairwise E2EE session. When Alice sends a message, she encrypts it with her sender key, and all members decrypt using Alice's sender key (which they received earlier).

A newer standard, **Messaging Layer Security (MLS)** (RFC 9420), handles group E2EE more efficiently through tree-based key agreement, making it suitable for very large groups.

### 5.4 Challenges Introduced by E2EE

E2EE provides strong security but breaks many features users expect.

**Server-Side Search:** If the server cannot read messages, it cannot search them. Solutions include client-side search only (download all messages and search locally), encrypted search indexes (the client encrypts a search index and stores it on the server), or blind indexing (hash each word deterministically and store the hash).

**Cloud Backup:** If messages are only on the device, what happens when you get a new phone? Solutions include encrypted cloud backup (encrypt messages with a backup key derived from a password) or key escrow (store a copy of keys in a Hardware Security Module that requires user authentication).

**Metadata Leakage:** E2EE encrypts the content of messages, but metadata (who is talking to whom, when, how often, message sizes) is usually visible to the server. Mitigations include padding messages to a fixed size and minimizing logging.

### 5.5 Authentication and Authorization

**Authentication (Who Are You?)**

**JWT (JSON Web Tokens):** A standard format for tokens (RFC 7519) that contain claims (user ID, role, expiration) signed by the server. The client sends the JWT in the `Authorization: Bearer <token>` header, and the server verifies the signature on every request. This is stateless—no database lookup is needed.

**OAuth 2.0:** A protocol for delegated authorization, used for "Login with Google/Facebook/GitHub." The user authenticates with the third party, which sends an authorization code to your server, and your server exchanges the code for user information.

**Authorization (What Can You Do?)**

Each chat room has a list of authorized members. The server checks membership before allowing connections or message delivery. Role-based access control (RBAC) can be used: owner, admin, member, and viewer roles, each with different permissions. In an E2EE context, the server enforces who can send to whom (even though it cannot read the content). When a member is removed from a group, the server rejects their messages and facilitates key rotation so they cannot read future messages.

### 5.6 Rate Limiting and DDoS Protection

**Rate Limiting:** Without rate limiting, an attacker can send millions of messages to crash the server, try millions of passwords (brute force), or exhaust the one-time pre-key pool. Common rate limits include:
- Login attempts: 5 per minute per IP
- Message sending: 30 per minute per user
- Key exchange requests: 10 per minute per user
- Registration: 3 per hour per IP

**DDoS Protection:** At the network layer, services like AWS Shield and Cloudflare absorb large volumetric attacks. At the application layer, a Web Application Firewall (WAF) blocks malicious requests, CAPTCHA protects login and registration endpoints, and connection limits restrict the number of concurrent connections per IP.

---

## Section 6: Putting It All Together

### 6.1 End-to-End Architecture Diagram

```
[Client Apps]
    |
    v
[CDN (CloudFront/Cloudflare)]  <-->  [S3 / Object Storage]
    |
    v
[Load Balancer (ALB/HAProxy)]  <-->  [WebSocket Server Pool (K8s Pods)]
    |                                       |
    v                                       v
[API Server Pool (REST/gRPC)]        [Redis (Presence + Pub/Sub)]
    |                                       |
    v                                       v
[Kafka Cluster]  <-->  [Message Consumers (K8s Pods)]
    |
    v
[Database Layer]
    |-- Cassandra/ScyllaDB (Message History)
    |-- PostgreSQL (User Accounts, Metadata)
    |-- Elasticsearch (Full-Text Search)
    |-- Redis (Cache, Presence, Typing)
```

### 6.2 Message Flow Summary

1. Client sends message with idempotency key via WebSocket.
2. WebSocket server validates and publishes to Kafka.
3. Kafka consumer deduplicates, persists to Cassandra, and fans out to recipients.
4. Recipient's WebSocket server pushes message to the recipient's client.
5. Client sends ACK; server updates delivery status.

### 6.3 Key Design Principles for Junior Developers

1. **Assume failure.** Design every component as if it will fail. Use timeouts, retries, circuit breakers, and fallbacks.
2. **Prefer stateless.** Stateless services are trivially scalable. Keep state in databases, caches, or message queues, not in the application server.
3. **Shard thoughtfully.** Choose the sharding key that matches your access pattern. For chat, room ID is often best, but you need a plan for hot rooms.
4. **Use consistent hashing.** It makes scaling up and down much less disruptive.
5. **Secure from the start.** TLS, authentication, and encryption at rest are foundational. Add E2EE if the use case requires it.
6. **Monitor everything.** You need metrics (CPU, memory, connection count, latency), logging (structured logs), and tracing (distributed tracing with OpenTelemetry) to understand failures.
7. **Start simple, then add complexity.** A single server with a database is fine for a prototype. Add sharding, replication, and multi-region deployment only when you need them.

---

## Sources

[1] Apache Kafka Documentation: Exactly-Once Semantics — https://kafka.apache.org/documentation/#semantics

[2] Redis Pub/Sub Documentation — https://redis.io/docs/latest/develop/interact/pubsub/

[3] WebSocket Protocol (RFC 6455) — https://datatracker.ietf.org/doc/html/rfc6455

[4] AWS S3 Pre-Signed URLs Documentation — https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html

[5] Cassandra Data Modeling for Time Series — https://cassandra.apache.org/doc/latest/cassandra/data_modeling/time_series.html

[6] Facebook Messenger Architecture (Fan-out on Write) — https://engineering.fb.com/2011/03/15/core-data/facebook-messenger/

[7] Discord Architecture (Fan-out on Read for Large Groups) — https://discord.com/blog/how-discord-stores-billions-of-messages

[8] WhatsApp Architecture — https://blog.whatsapp.com/

[9] Socket.IO Documentation — https://socket.io/docs/v4/

[10] NGINX Load Balancing for WebSockets — https://docs.nginx.com/nginx/admin-guide/load-balancer/websocket-load-balancing/

[11] Kubernetes Horizontal Pod Autoscaler — https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/

[12] CloudFront CDN Documentation — https://aws.amazon.com/cloudfront/

[13] DynamoDB Best Practices for Time Series Data — https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-time-series.html

[14] Elasticsearch Documentation — https://www.elastic.co/guide/en/elasticsearch/reference/current/index.html

[15] CAP Theorem and Distributed Systems — https://www.ibm.com/think/topics/cap-theorem

[16] Signal Protocol Documentation — https://signal.org/docs/

[17] TLS Protocol Version 1.3 (RFC 8446) — https://datatracker.ietf.org/doc/html/rfc8446

[18] JSON Web Token (JWT) (RFC 7519) — https://datatracker.ietf.org/doc/html/rfc7519

[19] OAuth 2.0 Authorization Framework (RFC 6749) — https://datatracker.ietf.org/doc/html/rfc6749

[20] Messaging Layer Security (MLS) Protocol (RFC 9420) — https://datatracker.ietf.org/doc/html/rfc9420

[21] AWS Key Management Service (KMS) Documentation — https://docs.aws.amazon.com/kms/latest/developerguide/

[22] HashiCorp Vault Transit Secrets Engine — https://developer.hashicorp.com/vault/docs/secrets/transit

[23] libsignal-client (Signal Protocol Implementation) — https://github.com/signalapp/libsignal-client

[24] Olm: A Cryptographic Ratchet (Matrix.org) — https://gitlab.matrix.org/matrix-org/olm/

[25] PostgreSQL pgcrypto Extension — https://www.postgresql.org/docs/current/pgcrypto.html

[26] Let's Encrypt Free TLS Certificates — https://letsencrypt.org/

[27] AWS Shield DDoS Protection — https://aws.amazon.com/shield/

[28] Cloudflare DDoS Protection — https://www.cloudflare.com/ddos/

[29] Web Crypto API (MDN) — https://developer.mozilla.org/en-US/docs/Web/API/Web_Crypto_API

[30] OWASP Rate Limiting Guide — https://cheatsheetseries.owasp.org/cheatsheets/Denial_of_Service_Cheat_Sheet.html
