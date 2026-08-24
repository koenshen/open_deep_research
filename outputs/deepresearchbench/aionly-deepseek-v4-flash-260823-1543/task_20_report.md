# Anthropic Streamable HTTP 功能工程实现方案深度解析

## 概述

在深入探讨之前，需要明确一个重要概念区分：在 Anthropic 生态系统中，"Streamable HTTP" 是 **Model Context Protocol (MCP)** 的传输层协议名称，而非 Claude API 的流式功能名称。Claude API 的流式响应功能（通过 `/v1/messages` 端点）官方称为 **"Streaming messages"** 或 **"SSE streaming"**，通过设置 `"stream": true` 参数启用。这两个概念在架构上密切相关但属于不同层面，本报告将分别详细阐述，并揭示它们之间的技术联系。

---

## 1. Streamable HTTP 协议的定义与核心特性

### 1.1 什么是 Streamable HTTP

Streamable HTTP 是 **Model Context Protocol (MCP)** 的当前标准传输协议，取代了最初在 MCP 规范中引入的旧版 HTTP+SSE（Server-Sent Events）传输。根据 MCP 规范（2026-07-28 版本）的定义，Streamable HTTP 使 MCP 客户端和服务器能够通过标准 HTTP 进行通信，服务器作为独立进程运行，能够处理多个客户端连接，使用 HTTP POST 和 GET 请求，并可选择性地使用 Server-Sent Events (SSE) 进行流式传输 [Streamable HTTP - MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)。

### 1.2 与标准 HTTP 流式传输的区别

Streamable HTTP 与传统的 HTTP 流式传输方法有本质区别。传统的 HTTP+SSE 方法需要两个独立的连接：一个用于客户端到服务器通信的标准 HTTP POST 端点，以及一个用于服务器到客户端流式传输的专用 SSE 端点。这种双通道方法在企业级应用中造成了严重的复杂性问题和可扩展性阻碍 [Understanding MCP Recent Change Around HTTP+SSE](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse)。

旧版 HTTP+SSE 传输存在五项结构性缺陷：

1. **双连接需要会话 ID 关联**：使用 GET /sse 端点进行服务器到客户端的流式传输，以及 POST /messages 端点进行客户端到服务器通信，两者之间需要状态性的会话关联
2. **强制粘性会话阻碍水平扩展**：持久的 SSE 连接意味着负载均衡器必须使用粘性会话，使得水平扩展变得困难
3. **对无服务器架构不友好**：持久连接在 Cloud Run、Lambda、Azure Functions 等无服务器平台上会不可预测地断开 [MCP Streamable HTTP Transport](https://apigene.ai/blog/mcp-streamable-http)
4. **防火墙/代理干扰**：代理和防火墙经常终止长生命周期的 SSE 连接
5. **单向流式传输限制**：SSE 是单向的（仅服务器到客户端），且协议不支持可恢复流

此外，旧版 HTTP+SSE 还存在安全弱点：它要求持久开放连接，造成安全盲点，安全层仅在初始连接时检查身份，开发者被迫在 URL 查询字符串中传递访问令牌（`?token=xyz`），将凭证暴露在服务器日志和浏览器历史中 [Why MCP's Move Away from Server Sent Events Simplifies Security](https://auth0.com/blog/mcp-streamable-http)。

### 1.3 Streamable HTTP 解决的问题

Streamable HTTP 通过以下设计解决了所有这些问题：

- **单一端点设计**：使用标准 HTTP POST 和 GET 方法，支持 JSON 和 SSE 响应模式
- **可选会话管理**：会话 ID 为可选，支持无状态服务器部署
- **可恢复性**：支持通过 `Last-Event-ID` 头部恢复断开的连接
- **动态升级**：服务器可以根据特定交互的需求动态决定是否升级到 SSE 流 [A Visual Guide to MCP's Streamable HTTP Transport](https://medium.com/the-ai-language/a-visual-guide-to-mcps-streamable-http-transport-6dc18fe751ad)

### 1.4 发布历程

- **2024 年 11 月**：MCP 初始发布，HTTP+SSE 作为传输选项之一（与 stdio 并列）
- **2025 年 3 月（规范版本 2025-03-26）**：Streamable HTTP 传输正式引入，取代 HTTP+SSE 传输
- **2025 年 6 月 22 日**：Anthropic 宣布 Claude Code 支持通过 Streamable HTTP 连接远程 MCP 服务器 [Claude Code Gains Support for Remote MCP Servers](https://www.infoq.com/news/2025/06/anthropic-claude-remote-mcp)
- **2026 年 5 月 21 日**：2026-07-28 发布候选版本宣布，是自发布以来最大的修订
- **2026 年 7 月 28 日**：2026-07-28 规范正式发布，MCP 在协议层面完全变为无状态 [The 2026-07-28 MCP Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate)

---

## 2. 网络架构与传输机制

### 2.1 Streamable HTTP 传输架构

Streamable HTTP 定义了一个单一端点（通常为 `/mcp` 或 `/message`），同时处理客户端到服务器和服务器到客户端的通信。客户端通过 HTTP POST 向此单一端点发送 JSON-RPC 消息。服务器根据交互需求，返回单个 JSON 响应（针对简单调用）或打开 SSE 流（针对进度更新、流式结果）[Streamable HTTP - MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http)。

**核心架构要求**：

- 每个 JSON-RPC 消息必须是一个新的 HTTP POST 请求，`Accept` 头部必须同时列出 `application/json` 和 `text/event-stream`
- 客户端可以发出 HTTP GET 请求以打开 SSE 流，接收服务器发起的消息
- 服务器必须返回 `Content-Type: text/event-stream` 或 HTTP 405
- 客户端可以同时保持多个 SSE 流连接；服务器不得跨多个流广播相同消息

### 2.2 会话管理演变

**2025-03-26 至 2025-11-25 版本**：使用 `Mcp-Session-Id` 头部进行会话管理。服务器在初始化期间分配会话 ID，客户端在后续请求中包含此头部。会话 ID "应该是全局唯一的且加密安全的（例如，安全生成的 UUID、JWT 或加密哈希）"。

**2026-07-28 版本**：MCP 在协议层完全变为无状态，移除了 `initialize`/`initialized` 握手和 `Mcp-Session-Id` 头部。每个请求现在在其 `_meta` 字段中内联携带自己的协议版本和客户端能力。规范明确规定："一个 2026-07-28 服务器如果收到来自旧版客户端的 `Mcp-Session-Id` 头部，需要忽略它，而不是生成或回显会话 ID" [Understanding MCP Recent Change Around HTTP+SSE](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse)。

### 2.3 Claude API 流式传输的传输机制

Claude API 的流式传输使用 **Server-Sent Events (SSE)** 通过 HTTP/HTTPS 传输。`stream()` 调用通过服务器发送的事件保持 HTTP 连接活跃 [Streaming messages - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/streaming)。

**连接建立与生命周期**：
- 客户端发送标准 HTTP POST 请求至 `https://api.anthropic.com/v1/messages`
- 请求体中包含 `"stream": true`
- 标准头部包括 `x-api-key`（认证）和 `anthropic-version`（例如 `2023-06-01`）
- 服务器响应 HTTP 200 并开始流式传输 SSE 事件
- 连接保持打开，直到流完成（发送 `message_stop` 事件）或发生错误
- 所有通信使用 TLS (HTTPS)，SDK 自动处理 TLS

### 2.4 性能基准测试

在持续负载测试下，Streamable HTTP 的性能表现显著优于旧版 SSE 传输：
- **Streamable HTTP**：在 100% 成功率下维持 290-300 RPS，每次调用延迟约 10ms
- **SSE 传输**：吞吐量下降至 7-30 RPS，延迟升至数百毫秒 [MCP Transport Comparison](https://gingerlabs.ai/blog/mcp-transport-comparison)

在 1000 并发用户测试场景中，Streamable HTTP 的 TCP 连接数明显低于 HTTP+SSE，后者需要长期维护单独的连接。Streamable HTTP 的总执行时间仅为 SSE 服务器的四分之一 [Comparison of data before and after using Streamable HTTP](https://medium.com/@higress_ai/comparison-of-data-before-and-after-using-streamable-http-b094db8b414e)。

---

## 3. HTTP 层面的流式处理

### 3.1 Claude API 的 SSE 线格式

Claude API 的流式传输 **不使用** 分块传输编码（`TE: chunked`）作为其主要流式传输机制，而是使用 **Server-Sent Events (SSE)**。返回的 `Content-Type` 头部为 `text/event-stream` [Streaming messages - Claude Platform Docs](https://docs.anthropic.com/en/api/messages-streaming)。

每个 SSE 事件遵循标准格式：
```
event: {event_type}
data: {JSON_data}\n\n
```

### 3.2 事件类型与序列

流遵循特定的事件流程：

1. **`message_start`** — 包含一个空的 Message 对象（`content: []`），包括消息 ID、模型、角色和初始用法令牌计数
2. **内容块** — 每个内容块有一系列事件：
   - **`content_block_start`** — 内容块开始，包括块类型（text、tool_use、thinking）、索引和初始内容
   - **`content_block_delta`**（一个或多个）— 增量更新，delta 类型根据内容块类型而变化
   - **`content_block_stop`** — 内容块结束
3. **`message_delta`** — 最终 Message 的顶级变化，包括 `stop_reason`、`stop_sequence` 和累积的 `usage` 令牌计数
4. **`message_stop`** — 最终事件，表示流完成
5. **`ping` 事件** — 可能在任何时间出现的保活事件，应忽略
6. **`error` 事件** — 可能在任何时间出现，如 `overloaded_error`

### 3.3 内容块 Delta 类型

四种 delta 类型已被文档化：

1. **Text delta** (`text_delta`)：增量文本内容，字段为 `delta.text`，包含字符串片段
2. **Input JSON delta** (`input_json_delta`)：用于 `tool_use` 内容块的局部 JSON 字符串，字段为 `delta.partial_json`。需要在 `content_block_stop` 时累积和解析 JSON
3. **Thinking delta** (`thinking_delta`)：使用扩展思维时的思考内容，字段为 `delta.thinking`
4. **Signature delta** (`signature_delta`)：在 `thinking` 块的 `content_block_stop` 之前发送，用于验证完整性，字段为 `delta.signature`

### 3.4 细粒度工具流式传输

除了标准流式传输外，Anthropic 还提供 **细粒度工具流式传输**，在 Claude 生成工具输入时将其直接传送给客户端，无需服务器端缓冲或 JSON 验证 [Fine-grained tool streaming](https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming)。

**启用方式**：在任何用户定义的工具定义上将 `eager_input_streaming` 设置为 `true`，并在请求上启用流式传输。

**工作原理**：初始的 `content_block_start` 事件包含 `input: {}`（空对象占位符）。实际输入作为一系列 `input_json_delta` 事件到达，每个事件携带 `partial_json` 字符串片段。客户端拼接这些片段，并在块关闭时解析结果。

**重要警告**："由于 API 在流式传输前不会缓冲或验证工具输入，您可能会收到部分或无效的 JSON。"当累积的输入是无效/不完整的 JSON 时，应通过返回带有 `is_error: true` 的 `tool_result` 内容块来报告失败。

### 3.5 关键 HTTP 头部和 Nginx 配置

将 SSE 放在 Nginx 后面时，需要 `proxy_buffering off` 配置。关键头部包括：
- `Cache-Control: no-cache`
- `X-Accel-Buffering: no`（禁用 Nginx 缓冲）

"省略 `proxy_buffering off` 意味着 Nginx 收集整个流到其缓冲区中，然后一次性发送出去。那不是流式传输。那只是一个慢速响应。几乎所有人在第一次将 SSE 放在 Nginx 后面时都会犯这个错误" [FastAPI + Claude API: Production Streaming Guide](https://jangwook.net/en/blog/en/fastapi-claude-api-streaming-production-guide-2026)。

---

## 4. 后端实现细节

### 4.1 服务器基础设施架构

**Anthropic 在 Google Kubernetes Engine (GKE) 上运行 Claude 推理，使用 TPU**。在 Google Cloud Next 2024 的演讲中，Anthropic 工程师详细介绍了 Claude（Claude 3 家族）的部署架构 [How Anthropic uses Google Kubernetes Engine to run inference for Claude](https://www.youtube.com/watch?v=b87I1plPeMg)：

- **GKE 与 StatefulSets**：Anthropic 使用 GKE stateful set 管理推理工作负载，支持客户触发的维护，实现接近 100% 的可用性
- **Leader Worker Set 模式**：用于处理不同类型资源的工作负载（如负载均衡器 + 昂贵的 TPU/GPU）
- **TPU 使用**：每个 TPU 芯片每秒计算 393 万亿次操作，256 个芯片在高速网格中协同工作。TPU v5e 每美元推理性能比 TPU v4 高出 2.7 倍
- **容器预加载**：使用辅助引导磁盘，对 16GB 容器镜像实现 29 倍的容器启动时间改进
- **Cloud Storage Fuse**：Pod 启动时间改进约 40%

### 4.2 流式连接管理

**服务器端连接管理**：Anthropic 使用 SSE 保持 HTTP 连接在生成期间保持活跃。服务器必须维护连接状态、生成状态（模型的 KV 缓存）和 SSE 事件流缓冲区。

**Bigtable 存储**：Anthropic 构建了基于 Google Cloud Bigtable 的 PB 级审计和访问控制系统。每个 Claude 提示、完成和对话都以加密安全方式存储在 Bigtable 中，并带有保留控制。内容使用 zstandard 压缩，并使用每个项目唯一的密钥加密。超过 4MB 的 blob 被分割成 4MB 块存储在单独的表中 [Scaling intelligence: How Anthropic secures Claude with Bigtable](https://www.youtube.com/watch?v=UaI1ABXQ4-M)。

### 4.3 背压处理

**客户端侧背压问题**：一个关键的 GitHub Issue (#842) 报告了流式响应在传输过程中持续中断，且在未收到 `message_stop` 事件的情况下发生的现象。该问题特别在使用 `tool_use` 且包含大 JSON 负载时出现 [GitHub Issue #842](https://github.com/anthropics/anthropic-sdk-typescript/issues/842)。

**关键发现**："放慢消费速度可以修复问题这一事实表明 SDK 或底层连接没有正确处理背压信号。"用户无法确定根本原因是背压/流控制、时序问题、大小限制（约 270-280KB 阈值）、网络中介（Cloudflare 代理）还是其他原因。

**Anthropic API 速率限制作为背压机制**：Anthropic 使用基于层级的速率限制系统，作为主要的背压机制。限制在三个维度上定义：每分钟请求数 (RPM)、每分钟输入令牌数 (ITPM) 和每分钟输出令牌数 (OTPM) [How to Handle Anthropic 429 / 529 Errors in Production](https://www.respan.ai/articles/anthropic-api-rate-limits)。

**构建层级系统（基于累积信用购买）**：
- 层级 1：$5 购买
- 层级 2：$40 购买
- 层级 3：$200 购买
- 层级 4：$400 购买

**Claude Opus 4 的速率限制示例**：
- 层级 1：30K ITPM, 8K OTPM
- 层级 2：450K ITPM, 90K OTPM
- 层级 3：800K ITPM, 160K OTPM
- 层级 4：2M ITPM, 400K OTPM

**背压信令机制**：
- HTTP 头部：`Retry-After`、`X-RateLimit-*` 头部使得带抖动的指数退避成为可能
- 最持久的架构"将令牌桶速率限制与租户入口点配对（以执行公平配额），与泄漏桶或基于队列的背压配对（以平滑对下游 LLM 提供商的流量），以及在外部 API 边界使用断路器（以在提供商降级期间保护服务健康）" [Rate Limiting and Backpressure Patterns for AI Agent APIs](https://zylos.ai/research/2026-02-25-rate-limiting-backpressure-ai-agent-apis)

### 4.4 请求取消

**客户端侧取消机制（Claude Code）**：Claude Code 通过 **AbortController 的推送模型** 实现取消功能 [Chapter 2: Cancellation & Abort Propagation](https://kenhuangus.substack.com/p/chapter-2-cancellation-and-abort)：

- 每个 `QueryEngine` 拥有一个 `AbortController`（可选由调用者传入用于嵌入）
- 暴露一个单一的 `interrupt()` 方法，调用 `abortController.abort()`
- 使用辅助函数设置最大监听器（默认 50），以避免来自许多订阅者的警告
- `createChildAbortController` 为子代理和每个工具隔离创建子作用域，使用 `WeakRef` 防止内存泄漏

**核心设计原则**："当用户按下 Ctrl-C，当上游超时触发，或当审核系统标记生成时，必须端到端停止：对模型的正在进行的 HTTP 流必须关闭，生成子进程必须终止，待处理的权限对话框必须释放，审计日志必须记录停止的内容。"

**静默流中止错误**：一个关键 GitHub Issue (#38905) 描述了 Claude Code 在 Anthropic API SSE 流中断时静默停止工作的 bug [GitHub Issue #38905](https://github.com/anthropics/claude-code/issues/38905)。根本原因是 Anthropic SDK 的 SSE 流迭代器静默吞掉了 `AbortError` 和 `FetchRequestCanceledException`，导致 `for await` 循环正常完成。

### 4.5 错误处理

**错误码和错误格式**：

| 状态码 | 错误类型 | 描述 | 可重试？ |
|--------|----------|------|---------|
| 400 | `invalid_request_error` | 格式错误的请求 | 否 |
| 401 | `authentication_error` | API 密钥问题 | 否 |
| 402 | `billing_error` | 支付/计费问题 | 否 |
| 403 | `permission_error` | 密钥缺少权限 | 否 |
| 404 | `not_found_error` | 错误的模型 ID 或端点 | 否 |
| 413 | `request_too_large` | 请求超过大小限制 | 否 |
| 429 | `rate_limit_error` | 达到 RPM、ITPM 或 OTPM 限制 | 是 |
| 500 | `api_error` | 内部服务器错误 | 是 |
| 504 | `timeout_error` | 请求超时 | 是 |
| 529 | `overloaded_error` | API 过载 | 是 |

**流式传输中的错误处理**：错误可以在 SSE 流式传输期间在 200 响应后以 `error` 事件到达。相同的事件循环中需要相同的错误处理逻辑。

**中断流的错误恢复**：
- **Claude 4.5 及更早版本**：捕获部分响应，构造包含部分助手响应作为新助手消息开头的延续请求
- **Claude 4.6 及更高版本**：相同的捕获策略，但添加一条用户消息，指示模型从停止的地方继续

**限制**："工具使用和扩展思维块无法部分恢复。您可以从最近的文本块恢复流式传输。"

---

## 5. 客户端实现注意事项

### 5.1 连接与消费

**Python SDK**：`client.messages.stream()` 方法返回一个 `MessageStreamManager`，生成一个 `MessageStream` 用于迭代流式文本和事件。可以使用 `async for event in stream:` 迭代流，事件通过 `.type` 进行类型化（例如 `"text"`、`"input_json"`、`"message_stop"`、`"content_block_stop"`）[anthropic-sdk-python/helpers.md](https://github.com/anthropics/anthropic-sdk-python/blob/main/helpers.md)。

**TypeScript SDK**：`.stream()` 方法返回一个流对象。可以使用 `.on('contentBlock', ...)` 和 `.on('message', ...)` 事件处理器消费，或使用 `for await (const event of stream)` 迭代 [anthropic-sdk-typescript](https://github.com/anthropics/anthropic-sdk-typescript)。

**基本代码示例（Python）**：
```python
async with client.messages.stream(
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say hello there!"}],
    model="claude-sonnet-5"
) as stream:
    async for event in stream:
        if event.type == "text":
            print(event.text, end="", flush=True)
    accumulated = await stream.get_final_message()
```

**基本代码示例（TypeScript）**：
```typescript
const stream = client.messages
  .stream({
    messages: [{ role: 'user', content: 'How do you recursively list all files in a directory in Rust?' }],
    model: 'claude-sonnet-5',
    max_tokens: 1024,
  })
  .on('contentBlock', (content) => console.log('contentBlock', content))
  .on('message', (message) => console.log('message', message));

const message = await stream.finalMessage();
```

### 5.2 状态管理

**累积完整响应**：SDK 提供辅助方法从流中累积完整的 `Message` 对象。
- Python：`accumulated = await stream.get_final_message()`
- TypeScript：`const message = await stream.finalMessage()`

返回的对象"与通过 `client.messages.create()` 得到的 Message 完全相同——相同的 `content[0].text`、相同的 `stop_reason`、相同的 `usage`" [Claude Messages API: Streaming](https://medium.com/@gurpartap.sandhu3/claude-messages-api-streaming-4bd16a39b085)。

**重要注意事项**：
- 新事件类型可能会在未来添加，代码应优雅地处理未知事件类型
- `message_delta` 中的 `usage` 计数是累积的，不是每个块的数值
- Ping 事件（保活）可以出现在任何地方，应忽略

### 5.3 重连与弹性

**连接断开处理**：Streamable HTTP 规范支持可恢复性："服务器可以在 SSE 事件上附加全局唯一 ID，以支持使用 `Last-Event-ID` 头部恢复断开的连接"。

**超时设置**：
- 默认超时：10 分钟
- 对于大量 `max_tokens` 的请求，SDK 实际上在底层需要流式传输，以避免 HTTP 连接在 Claude 工作时超时

**重试逻辑**：
- 默认重试次数：2 次，带短指数退避
- 触发重试的错误类型：连接错误、408、409、429、500+
- 不应重试的错误类型：AuthenticationError/BadRequestError

### 5.4 生产环境最佳实践

**Flow control**：使用 `AsyncAnthropic`（而非同步客户端）以避免阻塞事件循环。SSE 格式要求 `data:` 前缀 + JSON + 两个换行符（`\n\n`）。

**UI 渲染**：
- "不要在中途渲染 markdown"——等待直到有一个完整的 "块"（段落中断或两个换行），然后渲染完成的块
- 显示打字指示器——从请求到第一个令牌大约有 300-500ms 的延迟
- 支持用户操作中止——允许用户取消流式传输的中间生成

**监控**：对于流式 API，生产监控推荐三个指标：TTFT（首次令牌时间）、TPS（每秒令牌数）和流式错误率。

### 5.5 已知的 Ping 感知流式传输监视器问题

一个关键的 GitHub Issue (#998) 讨论了需要 Ping 感知的流式传输监视器。核心问题是 Anthropic API 的 SSE 流每约 15-30 秒发出 `ping` 事件作为存活信号，但 TypeScript SDK 静默丢弃它们。这阻止了下游消费者区分"服务器正在积极思考"和"流已静默停滞"两种情况 [GitHub Issue #998](https://github.com/anthropics/anthropic-sdk-typescript/issues/998)。

提出的 4 步修复方案包括：
1. 转发 ping——停止丢弃，生成为 `{ type: 'ping', timestamp }`
2. 语义化 ping——添加 `status` 字段（'queued', 'thinking', 'tool_executing', 'generating', 'rate_limited'）
3. 自适应客户端阈值——每个状态使用不同的超时，而不是一个全局魔法数字
4. 服务器驱动的阈值——服务器告诉客户端 `nextPingWithinMs`，客户端只需遵守

---

## 6. 性能特征与可扩展性

### 6.1 首次令牌时间 (TTFT) 延迟

**Anthropic API TTFT 基准测试**（来自独立来源）：

| 模型 | 场景 | TTFT |
|------|------|------|
| Claude Sonnet 4 | 500 令牌输入，200 令牌输出，p50，美国东部 | 800ms |
| Claude Opus 4.8 | 短答案 Q&A，128 令牌输出 | 0.75s |
| Claude Haiku 4.5 | 短答案 Q&A | 0.96s |
| Claude Opus 4.7 | 通过 Anthropic API | 2s |

**行业背景**："Groq 在首次令牌时间 (TTFT) 方面领先，大多数模型低于 200ms，得益于定制 LPU 硬件。TTFT 低于 500ms 感觉瞬间完成。超过 2 秒感觉有问题。"

### 6.2 每秒令牌数 (TPS) 吞吐量

**输出速度基准测试**（p50，在 10,000 输入令牌下测量）：

| 模型 | 提供商 | 令牌/秒 |
|------|--------|---------|
| Claude Sonnet 4.6（最大努力） | Azure | 60.2 t/s |
| Claude Sonnet 4.6（最大努力） | Amazon | 59.1 t/s |
| Claude Sonnet 4.6（最大努力） | Google | 55.1 t/s |
| Claude Sonnet 4.6（最大努力） | Anthropic | 54.2 t/s |
| Claude 3 Haiku | Amazon | 79.0 t/s |
| Claude Sonnet 4 | Anthropic | 80 t/s |

### 6.3 延迟优化技术

- **使用流式传输（`stream: true`）** 以获得感知速度
- **保持提示简洁**
- **使用提示缓存**——缓存提示减少 90% 的时间
- **选择正确的区域**以最小化网络延迟
- **细粒度工具流式传输**跳过缓冲步骤，减少大参数（如文档或代码块）的第一个片段的时间

### 6.4 可扩展性模式

**基础设施扩展**：Anthropic 使用事件驱动、异步基础设施模式，包括 GKE stateful set、Pod 中断预算和优雅终止。

**Streamable HTTP 可扩展性**：Streamable HTTP 是唯一支持认证、水平扩展、无状态服务器部署和可恢复流的 MCP 传输。MCP 服务器使用 Streamable HTTP 可以完全无状态，实现直接的水平扩展。

**多提供商策略**：Anthropic API 可通过多个提供商使用：
- 第一方 Anthropic API (`api.anthropic.com`)
- Amazon Bedrock
- Google Cloud Vertex AI
- Microsoft Foundry

**网关模式**：企业级 Claude 应用网关是自托管服务，位于本地 Claude Code 客户端和 Google Cloud 的 Vertex AI / Agent Platform 之间，处理身份、策略、遥测、支出限制和路由。

---

## 7. 开源参考实现、SDK 和代码示例

### 7.1 官方 Anthropic SDK

**Python SDK**（`anthropic` 0.50+）：
- 提供 `client.messages.stream()` 方法，返回 `MessageStreamManager`
- 支持同步和异步（`AsyncAnthropic`）客户端
- `.text_stream` 属性允许直接迭代文本 delta
- MCP 助手：`async_mcp_tool`/`mcp_tool`、`mcp_message`、`mcp_resource_to_content`、`mcp_resource_to_file`

**TypeScript SDK**（`@anthropic-ai/sdk` 0.60+）：
- 提供 `client.messages.stream()` 方法
- 支持事件处理器：`.on('contentBlock', ...)`、`.on('message', ...)`
- 支持 `for await...of` 迭代
- `.finalMessage()` 累积事件为完整 Message 对象
- 支持的运行时：Node.js 20 LTS+、Deno v1.28.0+、Bun 1.0+、Cloudflare Workers、Vercel Edge Runtime、Jest 28+、Nitro v2.6+

**Java SDK**（`com.anthropic:anthropic-java:2.53.0`）：
- 需要 Java 8+
- 使用构建器模式创建请求
- 支持同步和异步操作
- 流式传输：同步 `StreamResponse` 和异步 `AsyncStreamResponse`，支持 `MessageAccumulator`

**其他 SDK**：PHP、Go、C#（非官方）、Ruby 均有官方或社区支持。

### 7.2 MCP Streamable HTTP 参考实现

**invariantlabs-ai/mcp-streamable-http** GitHub 仓库提供了 Python 和 TypeScript 的 MCP Streamable HTTP 客户端和服务器示例实现 [invariantlabs-ai/mcp-streamable-http](https://github.com/invariantlabs-ai/mcp-streamable-http)：
- 130 星，37 分支，2 关注者
- 演示跨语言兼容性（Python 客户端 ↔ TypeScript 服务器，反之亦然）
- 使用以天气为焦点的 MCP 服务器，将请求转发给 Anthropic 的 Claude 语言模型

### 7.3 生产环境代码示例

**FastAPI + Claude API 流式传输代理**：
```python
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from anthropic import AsyncAnthropic

client = AsyncAnthropic()

async def generate_stream():
    async with client.messages.stream(
        max_tokens=1024,
        messages=[{"role": "user", "content": "Tell me a story"}],
        model="claude-sonnet-5"
    ) as stream:
        async for event in stream:
            if event.type == "text":
                yield f"data: {event.text}\n\n"

@app.get("/chat/stream")
async def chat_stream():
    return StreamingResponse(generate_stream(), media_type="text/event-stream")
```

**Deno 浏览器 SSE 代理**：将每个文本 delta 转发为一个 SSE 消息，使用 `JSON.stringify` 防止换行符破坏 `data:` 框架 [Stream a Claude response to the browser](https://docs.deno.com/examples/anthropic_sse)。

---

## 8. 与替代方案的比较

### 8.1 Streamable HTTP vs. HTTP+SSE

| 维度 | HTTP+SSE（旧版） | Streamable HTTP |
|------|------------------|-----------------|
| 连接数 | 2 个（GET /sse + POST /messages） | 1 个单一端点 |
| 状态管理 | 需要会话 ID 关联 | 可选，支持完全无状态 |
| 水平扩展 | 需要粘性会话 | 支持无状态水平扩展 |
| 无服务器兼容性 | 不友好 | 友好 |
| 可恢复性 | 不支持 | 支持（Last-Event-ID） |
| 延迟（负载下） | 数百毫秒 | 约 10ms |
| 吞吐量（负载下） | 7-30 RPS | 290-300 RPS |

### 8.2 Streamable HTTP vs. WebSocket

| 维度 | WebSocket | Streamable HTTP |
|------|-----------|-----------------|
| 协议 | ws:// 或 wss:// | 标准 HTTP |
| 通信模式 | 全双工双向 | 请求-响应，可选升级到 SSE |
| 帧开销 | 2-6 字节 | 完整 HTTP 头部 |
| 基础设施兼容性 | 需要 WebSocket 兼容客户端 | 与标准 HTTP 中间件完全兼容 |
| 适用场景 | 会话式 AI、代理工作流、实时协作 | 状态查询、批处理、简单集成 |

**决策框架**：
- **使用 HTTP（Streamable HTTP/SSE）** 用于：无状态查询、可缓存响应、批处理、简单集成、REST API 端点
- **使用 WebSocket** 用于：会话式 AI、代理工作流、实时指导、多设备 AI、人类参与工作流

### 8.3 Streamable HTTP vs. 长轮询

长轮询未被直接比较，但 MCP 决策框架明确表明，Streamable HTTP 是远程/网络通信的首选方法，因为它避免了维护持久连接的开销和复杂性（如 SSE 所需），同时提供比基于轮询的方法更好的可扩展性。

### 8.4 MCP 传输决策框架

- **本地**：使用 stdio。约 0ms 网络开销。每个进程一个客户端。无需认证、网络或多租户。最适合本地工具、CLI 代理和桌面 AI 客户端（Claude Desktop、Cursor）
- **远程/网络/云/多用户**：毫无例外地使用 Streamable HTTP。它是唯一支持认证、水平扩展、无状态服务器部署和可恢复流的 MCP 传输
- **SSE**：仅用于向后兼容
- **迁移成本低**：在大多数 MCP SDK 中，将 stdio 转换为 Streamable HTTP 只是一个参数更改

### 8.5 Anthropic 选择 Streamable HTTP 的原因

从 HTTP+SSE 到 Streamable HTTP 的转变是由 SSE 的三个主要结构性问题驱动的：

1. **无法同时从客户端向服务器发送数据**
2. **资源密集型的长期连接**
3. **与负载均衡器和代理的兼容性差**

新的 Streamable HTTP "简化了协议，使用单一连接点，允许服务器在何时使用流式传输与一次性响应之间更加灵活，在适当时支持完全无状态的服务器实现，并且更紧密地遵循标准 HTTP 模式，使其更易于实现和部署" [Understanding MCP Recent Change Around HTTP+SSE](https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse)。

---

## 9. 结论

Anthropic 的 Streamable HTTP 功能代表了一种从传统持久连接模式向更灵活、可扩展的 HTTP 标准模式的重大架构转变。在 MCP 传输层，它通过单一端点设计、可选会话管理和动态流升级，解决了旧版 HTTP+SSE 的五项根本性缺陷。在 Claude API 层面，SSE 流式传输通过细粒度事件类型、部分 JSON 流式传输和复杂的错误恢复策略，提供了生产级的能力。

这两个概念虽然不同，但在技术上紧密相连：MCP 服务器可以使用 Claude API 生成响应，而 MCP Streamable HTTP 传输可以携带这些响应作为 SSE 流。MCP 连接器功能允许通过 Claude Messages API 直接连接到远程 MCP 服务器 [MCP connector](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)。

对于开发者而言，理解这两个层面及其技术细节，对于构建可靠、可扩展的 AI 应用至关重要。关键要点包括：使用适当的 SDK 和流式传输模式、实现正确的背压和错误处理、采用 Ping 感知的监视器，以及根据部署场景选择正确的传输协议。

---

### 来源

[1] Streamable HTTP - MCP Specification: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http

[2] Streaming messages - Claude Platform Docs: https://platform.claude.com/docs/en/build-with-claude/streaming

[3] Understanding MCP Recent Change Around HTTP+SSE: https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse

[4] Why MCP's Move Away from Server Sent Events Simplifies Security: https://auth0.com/blog/mcp-streamable-http

[5] MCP Streamable HTTP Transport: From SSE Migration to Production: https://apigene.ai/blog/mcp-streamable-http

[6] A Visual Guide to MCP's Streamable HTTP Transport: https://medium.com/the-ai-language/a-visual-guide-to-mcps-streamable-http-transport-6dc18fe751ad

[7] Claude Code Gains Support for Remote MCP Servers over Streamable HTTP: https://www.infoq.com/news/2025/06/anthropic-claude-remote-mcp

[8] The 2026-07-28 MCP Specification Release Candidate: https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate

[9] Streaming messages - Claude Platform Docs (debug): https://docs.anthropic.com/en/api/messages-streaming

[10] Fine-grained tool streaming: https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming

[11] How Anthropic uses Google Kubernetes Engine to run inference for Claude: https://www.youtube.com/watch?v=b87I1plPeMg

[12] Scaling intelligence: How Anthropic secures Claude with Bigtable: https://www.youtube.com/watch?v=UaI1ABXQ4-M

[13] GitHub Issue #842 - Streaming responses consistently interrupted: https://github.com/anthropics/anthropic-sdk-typescript/issues/842

[14] How to Handle Anthropic 429 / 529 Errors in Production: https://www.respan.ai/articles/anthropic-api-rate-limits

[15] Rate Limiting and Backpressure Patterns for AI Agent APIs: https://zylos.ai/research/2026-02-25-rate-limiting-backpressure-ai-agent-apis

[16] GitHub Issue #38905 - Silent stream abort: https://github.com/anthropics/claude-code/issues/38905

[17] Chapter 2: Cancellation & Abort Propagation: https://kenhuangus.substack.com/p/chapter-2-cancellation-and-abort

[18] anthropic-sdk-python/helpers.md: https://github.com/anthropics/anthropic-sdk-python/blob/main/helpers.md

[19] anthropic-sdk-typescript: https://github.com/anthropics/anthropic-sdk-typescript

[20] Claude Messages API: Streaming: https://medium.com/@gurpartap.sandhu3/claude-messages-api-streaming-4bd16a39b085

[21] GitHub Issue #998 - Ping-aware streaming watchdog: https://github.com/anthropics/anthropic-sdk-typescript/issues/998

[22] FastAPI + Claude API: Production Streaming Guide: https://jangwook.net/en/blog/en/fastapi-claude-api-streaming-production-guide-2026

[23] Stream a Claude response to the browser: https://docs.deno.com/examples/anthropic_sse

[24] MCP Transport Comparison: https://gingerlabs.ai/blog/mcp-transport-comparison

[25] Comparison of data before and after using Streamable HTTP: https://medium.com/@higress_ai/comparison-of-data-before-and-after-using-streamable-http-b094db8b414e

[26] invariantlabs-ai/mcp-streamable-http: https://github.com/invariantlabs-ai/mcp-streamable-http

[27] MCP connector: https://platform.claude.com/docs/en/agents-and-tools/mcp-connector

[28] SSE vs Streamable HTTP: Why MCP Switched Transport Protocols: https://brightdata.com/blog/ai/sse-vs-streamable-http

[29] Transports - MCP Specification (2025-03-26): https://modelcontextprotocol.io/specification/2025-03-26/basic/transports

[30] Anthropic Claude API Errors Reference: https://hidekazu-konishi.com/entry/anthropic_claude_api_errors_reference.html
