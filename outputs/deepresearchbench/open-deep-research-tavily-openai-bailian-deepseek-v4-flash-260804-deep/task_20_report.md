# Anthropic Streamable HTTP：工程实现深度分析报告

## 1. 概述：什么是Streamable HTTP？

**Streamable HTTP 是模型上下文协议（Model Context Protocol, MCP）的一种传输层机制**，而非 Anthropic Messages API（Claude 聊天 API）的功能。MCP 是 Anthropic 于 2024 年 11 月推出的开放标准，用于连接 AI 应用程序与外部工具、数据源和服务 [1]。

Streamable HTTP 在 **2025 年 3 月 26 日发布的 MCP 规范版本 2025-03-26** 中正式引入，取代了旧版的 HTTP+SSE（Server-Sent Events）传输方式 [2]。它允许 MCP 客户端和服务器通过 HTTP 进行通信，并可选地使用 SSE 实现服务器到客户端的流式传输 [3]。

**关键区分**：需要明确区分两个概念：
- **MCP Streamable HTTP 传输层**：用于 MCP 客户端与服务器之间工具调用的协议
- **Anthropic Messages API 流式传输**：用于从 Claude 模型获取流式生成内容的 API（`POST /v1/messages` 配合 `stream: true` 参数）

这两个概念在不同层级工作，但可以互相配合：MCP Streamable HTTP 传输层可以将 Messages API 的流式响应转发给客户端 [4]。

---

## 2. 底层架构与协议设计

### 2.1 协议栈

Streamable HTTP 的完整协议栈如下：

```
HTTP/HTTPS (传输层)
  └─ SSE (Server-Sent Events，可选流式层)
       └─ JSON-RPC 2.0 (消息格式)
            └─ MCP 语义层 (工具、资源、提示词)
```

核心消息格式是 **JSON-RPC 2.0**，所有消息必须使用 UTF-8 编码 [5]。服务器暴露一个**单一 HTTP 端点**（通常为 `/mcp` 或 `/message`），同时支持 POST 和 GET 方法 [6]。

### 2.2 传输层详细设计

**HTTP/1.1 与 HTTP/2 的微妙关系**：

Streamable HTTP 规范本身并未明确要求 HTTP/2 或 HTTP/3。然而，存在一个关键的技术限制：**HTTP/1.1 无法支持全双工流式传输**（仅支持服务器到客户端的单向流）。当使用 Python 的 fastmcp 和官方 MCP SDK 时，如果在 Hypercorn 上配合 `--h2` 标志运行（使用 HTTP/2），流式传输正常工作；如果在 Uvicorn 上运行（仅支持 HTTP/1.1），则会退化为同步请求/响应模式 [7]。

规范描述的是"单一端点上的双向 JSON-RPC"，但 HTTP/1.1 的 SSE 只能实现服务器到客户端的单向流，客户端到服务器的流式传输需要借助 HTTP/2 的服务器推送或多路复用能力 [7]。

**为何不选择 WebSocket**：

MCP 团队明确拒绝了 WebSocket 作为传输方案，原因如下 [8]：
1. 在类 RPC 场景中使用 WebSocket 会引入不必要的开销
2. 浏览器环境中无法附加自定义 HTTP 头部到 WebSocket 连接
3. 只有 GET 请求可以被透明地升级为 WebSocket 连接
4. WebSocket 无法传输 HTTP 头部信息，使认证流程复杂化

### 2.3 消息格式

**请求格式**：标准 JSON-RPC 2.0 请求对象，包含 `jsonrpc`、`method`、`params` 和 `id` 字段。

**响应格式**：标准 JSON-RPC 2.0 响应对象，包含 `jsonrpc`、`result`（或 `error`）和 `id` 字段。

**通知格式**：JSON-RPC 2.0 通知（无 `id` 字段），服务器以 HTTP 202 Accepted 响应 [5]。

### 2.4 会话管理演进

Streamable HTTP 的会话管理经历了显著的架构演进：

**2025-03-26 至 2025-11-25（有状态模式）** [6]：
- 服务器在初始化阶段可选择性地分配会话 ID，通过 `Mcp-Session-Id` 头部返回
- 客户端必须在后续所有请求中包含 `Mcp-Session-Id` 头部
- 服务器可以终止会话，客户端应发送 HTTP DELETE 来结束会话
- 支持通过 SSE 事件 ID 和 `Last-Event-ID` 头部实现流恢复

**2026-07-28（无状态模式）** [9]：
- 移除协议级别的会话和 `Mcp-Session-Id` 头部
- 移除 `initialize`/`notifications/initialized` 握手
- 每个请求都是自描述的，包含协议版本、客户端信息和能力信息
- 任何服务器实例都可以处理任何请求，支持简单的轮询负载均衡
- 无需粘性会话或共享会话存储

---

## 3. 流式传输机制

### 3.1 SSE 在 Streamable HTTP 中的使用方式

Streamable HTTP 的流式传输基于 **Server-Sent Events (SSE)**，但做了一些关键改进 [10]：

1. **动态升级**：服务器可以动态决定是返回标准 JSON 响应还是升级到 SSE 流，而不是像旧版 HTTP+SSE 那样必须使用两个独立的端点
2. **单一端点**：所有通信通过同一个端点进行，使用不同的 HTTP 方法来区分方向
3. **可选性**：SSE 不再是强制性的，支持仅使用 JSON 响应的模式

### 3.2 HTTP 头部设计

**请求头（客户端 → 服务器）** [6][11]：

| 头部 | 说明 | 必需性 |
|------|------|--------|
| `Accept` | 必须包含 `application/json` 和/或 `text/event-stream` | 必需 |
| `MCP-Protocol-Version` | 协议版本（如 `2026-07-28`） | 2025-06-18 起必需 |
| `Mcp-Session-Id` | 会话标识符 | 可选（2025-03-26 至 2025-11-25） |
| `Mcp-Method` | JSON-RPC 方法名（如 `tools/list`） | 2026-07-28 起支持 |
| `Mcp-Name` | 工具/资源名称 | 2026-07-28 起支持 |
| `Mcp-Param-{Name}` | 工具参数自定义头部 | 2026-07-28 起支持 |
| `Authorization` | 标准 HTTP Bearer 令牌 | 推荐 |
| `Origin` | 用于 DNS 重新绑定攻击防护 | 服务器必须验证 |
| `Content-Type` | `application/json` | 必需 |
| `Last-Event-ID` | SSE 流恢复 | 可选（2025-03-26 至 2025-11-25） |

**响应头（服务器 → 客户端）** [6][11]：

| 头部 | 说明 |
|------|------|
| `Content-Type` | `application/json` 或 `text/event-stream` |
| `Mcp-Session-Id` | 会话标识符（2025-03-26 至 2025-11-25） |
| 状态码 | `200 OK`（成功）、`202 Accepted`（通知/流式响应）、`400 Bad Request`（错误）等 |

### 3.3 SSE 事件格式

**MCP 流式传输的 SSE 帧格式**：

每个 SSE 事件包含：
```
event: message\n
data: <JSON-RPC payload>\n\n
```

事件之间用双换行符（`\r\n\r\n`）分隔 [12]。

**Messages API 流式传输的 SSE 事件类型**（与 MCP 不同，但可被 MCP 传输层转发）[13]：

| 事件类型 | 说明 | 出现次数 |
|----------|------|----------|
| `message_start` | 包含初始消息对象（ID、角色、模型、使用量） | 1 次 |
| `content_block_start` | 新内容块开始（文本、工具使用、思考） | 每个块 1 次 |
| `content_block_delta` | 内容块增量更新 | 多次 |
| `content_block_stop` | 内容块结束 | 每个块 1 次 |
| `message_delta` | 累积使用量和停止原因 | 1 次 |
| `message_stop` | 消息流结束 | 1 次 |
| `ping` | 保活信号（约每 15-30 秒） | 可选 |
| `error` | 错误事件 | 可选 |

**增量类型** [14]：
- `text_delta`：文本标记
- `input_json_delta`：工具使用的部分 JSON 字符串
- `thinking_delta`：扩展思考模式下的思考标记
- `signature_delta`：思考块的伴随签名

### 3.4 客户端-服务器交互生命周期

Streamable HTTP 的生命周期包括五个阶段 [15]：

**阶段 1 — 初始化**：
1. 客户端向 MCP 端点发送 POST 请求，包含 `initialize` 请求（JSON-RPC）
2. 服务器响应 `InitializeResult`，可选地包含 `Mcp-Session-Id` 头部
3. 客户端发送 `initialized` 通知
4. 服务器确认（HTTP 202 Accepted）

*（注：在 2026-07-28 无状态规范中，此握手被移除，改为每个请求携带协议版本和能力信息，服务器实现 `server/discover` RPC）* [9]

**阶段 2 — 客户端请求**：
1. 客户端发送 POST 请求，包含 JSON-RPC 请求（如 `tools/list`、`tools/call`）
2. 服务器可以响应：
   - 单一 JSON 响应（简单操作）
   - SSE 流（长时间运行或流式响应）
   - HTTP 202 Accepted（通知）

**阶段 3 — 客户端通知/响应**：
1. 客户端通过 POST 发送通知
2. 服务器接受（HTTP 202）或拒绝（HTTP 400）

**阶段 4 — 客户端监听服务器消息**：
1. 客户端发送 HTTP GET 请求打开 SSE 流
2. 服务器推送消息、通知和进度更新

**阶段 5 — 会话终止**：
1. 客户端发送 HTTP DELETE 请求
2. 服务器响应 HTTP 204 No Content

---

## 4. SDK 实现细节

### 4.1 TypeScript SDK

**仓库**：`https://github.com/modelcontextprotocol/typescript-sdk` [16]

**关键类**：

- **`StreamableHTTPClientTransport`**：客户端实现，处理 HTTP POST 请求发送 JSON-RPC 消息、接收 SSE 流式响应、通过 `Mcp-Session-Id` 头部管理会话（2026-07-28 前版本）[17]
- **`StreamableHTTPServerTransport`**：服务器端实现，处理双向通信，包括 SSE 通知 [18]
- **`WebStandardStreamableHTTPServerTransport`**：使用 Web 标准 `Request`/`Response` API 的底层实现，而非 Node.js HTTP API [19]

**版本历史**：
- v1.9.0：Streamable HTTP 代码存在于源码但未包含在编译分发中 [20]
- v1.10.0：首次正确导出 Streamable HTTP 支持 [20]
- v2.0.0（当前稳定版）：支持 2026-07-28 规范，拆分为 `@modelcontextprotocol/server` 和 `@modelcontextprotocol/client` [16]

**已知问题**：
- Issue #861：`StreamableHTTPClientTransport` 未正确实现 `Transport` 接口，导致 TypeScript 编译错误 [17]
- Issue #484：通过 HTTP 代理使用时，Node.js 的 `fetch` 尝试创建 HTTPS CONNECT 隧道，导致 `Unexpected content type: null` 错误 [21]
- Issue #1658：无公共 API 可从外部持久化会话数据重建会话感知的传输实例 [22]

### 4.2 Python SDK

**仓库**：`https://github.com/modelcontextprotocol/python-sdk` [23]

**关键类**：

- **`StreamableHTTPSessionManager`**（`src/mcp/server/streamable_http_manager.py`，441 行）：服务器端会话管理器，支持有状态模式（会话跟踪、事件存储、空闲超时）和无状态模式（每次请求创建新传输实例）[24]

**配置参数** [24]：
- `app`：MCP 服务器实例
- `event_store`：事件存储（用于流恢复）
- `json_response`：是否仅返回 JSON 响应
- `stateless`：是否启用无状态模式
- `security_settings`：安全设置
- `session_idle_timeout`：空闲超时（推荐 1800 秒）
- `max_request_body_size`：最大请求体大小（默认 4 MiB）

**客户端实现**：
- `streamable_http_client` 传输函数/模块，使用 `read_stream` 和 `write_stream` 进行异步通信 [25]

**版本历史**：
- v1.8.0（2025年5月8日）：首次支持 Streamable HTTP 传输 [26]
- v2.0.0（2026年7月28日）：支持 2026-07-28 规范，FastMCP 更名为 MCPServer [27]

**已知问题**：
- Issue #1190：v1.12.0+ 中 HTTP Streamable 模式下的 `ClosedResourceError` 错误 [28]
- Issue #1941：连接到仅支持 POST 的 MCP 服务器时客户端无限挂起 [29]
- Issue #1053：Google Cloud Run 上的连接兼容性问题 [30]

### 4.3 Go SDK

**仓库**：`https://github.com/modelcontextprotocol/go-sdk` [31]

**关键结构**：
- **`StreamableHTTPHandler`**（`mcp/streamable.go`）：包装 MCP 服务器的 HTTP 处理器 [32]
- **`StreamableServerTransport`**：服务器端传输类型 [33]
- **`StreamableClientTransport`**：客户端传输类型 [33]

**设计特点** [34]：
- 使用单一 `mcp` 包包含所有 MCP API（类似 `net/http`）
- 基于双向 JSON-RPC 流的低级 `Transport` 接口
- 支持有状态和无状态模式，通过 `Stateless` 标志控制
- 使用 `getServer` 工厂模式支持每个会话的服务器定制

**版本历史**：
- v1.7.0（2026年7月28日）：完全支持 2026-07-28 规范，无线协议重写为无状态模型 [35]

### 4.4 Spring AI Java SDK

**文档**：`https://docs.spring.io/spring-ai/reference/api/mcp/mcp-streamable-http-server-boot-starter-docs.html` [36]

**配置**：
- `spring.ai.mcp.server.protocol=STREAMABLE` 启用 Streamable HTTP
- `spring.ai.mcp.server.streamable-http` 自定义 MCP 端点路径（默认为 `/mcp`）
- 支持 WebMVC（同步）和 WebFlux（响应式、非阻塞）两种模式

---

## 5. 错误处理机制

### 5.1 HTTP 层面的错误处理

**HTTP 状态码** [37]：

| 状态码 | 错误类型 | 说明 |
|--------|----------|------|
| 400 | `invalid_request_error` | 请求错误，不应重试 |
| 401 | `authentication_error` | 认证失败，不应重试 |
| 402 | `billing_error` | 计费问题 |
| 403 | `permission_error` | 权限拒绝 |
| 404 | `not_found_error` | 资源未找到（会话不存在或未知） |
| 405 | `method_not_allowed` | DELETE 操作不支持 |
| 413 | `request_too_large` | 请求超出大小限制 |
| 429 | `rate_limit_error` | 速率限制，应使用指数退避重试 |
| 500 | `api_error` | 服务器错误，应使用退避重试 |
| 504 | `timeout_error` | 超时 |
| 529 | `overloaded_error` | API 过载，应使用退避重试 |

### 5.2 MCP 协议级错误

**标准 JSON-RPC 错误代码** [38]：
- `-32700`：解析错误（无效的 JSON）
- `-32600`：无效的请求
- `-32601`：方法未找到
- `-32602`：无效的参数
- `-32603`：内部错误

**MCP 特定错误代码** [6]：
- `-32020`：`HeaderMismatch` — 自定义头部与请求体不匹配

### 5.3 流式错误处理

**流中断恢复策略** [39]：

针对 Messages API 流式传输（可被 MCP 转发）：

| 模型版本 | 恢复策略 |
|----------|----------|
| Claude 4.5 及更早 | 将部分响应放入助手消息并继续 |
| Claude 4.6 及更新 | 发送用户消息指示模型从断点继续 |

**恢复限制**：可以从最近的文本块恢复，但工具使用和思考块**无法部分恢复** [39]。

**重试策略** [40]：
- 使用**完全抖动**的指数退避，基础延迟 500ms，上限 30 秒
- 最多 **5 次**重试尝试
- 断路器：当过去 20 个请求中失败率超过 50% 时停止重试
- 超时设置：交互式聊天 30 秒，代理步骤 60-90 秒

**保活机制**：
- Messages API 每约 **15-30 秒**发送 `ping` 事件 [41]
- TypeScript SDK 默认静默丢弃 `ping` 事件 `if (sse.event === 'ping') continue` [41]
- 提议改进：将 ping 转发给客户端，添加语义状态字段，使服务器能在 ping 载荷中声明 `nextPingWithinMs` [41]

**已知流错误**：
- 流空闲超时：SSE 流可能在中途停滞，既不发送 `message_stop` 也不发送错误事件。大多数停滞在约 50-70 秒后恢复（表明服务器端 60 秒超时/重试边界），但有些永远不会恢复 [42]
- 原始 JSON 解析错误：SSE 流中含有未转义的控制字符（C0 范围 U+0000–U+001F）或 U+2028 行分隔符时可能出错 [43]

---

## 6. 独特优化与权衡

### 6.1 Streamable HTTP vs. HTTP+SSE（旧版）

**为何 MCP 用 Streamable HTTP 取代 HTTP+SSE** [10][44][45]：

| 特性 | 旧版 HTTP+SSE | Streamable HTTP |
|------|---------------|-----------------|
| 端点 | 两个端点（`/sse` + `/messages`） | 单一统一端点 |
| 连接 | 需要两个持久连接 | 单连接，可动态升级 |
| 状态管理 | 必须有状态 | 支持完全无状态 |
| 基础设施兼容性 | 差（CDN、API 网关、负载均衡器不兼容） | 好（与标准 HTTP 基础设施兼容） |
| 安全性 | 令牌需在 URL 查询字符串中传递 | 标准 `Authorization: Bearer` 头部 |
| 流恢复 | 不支持 | 支持（通过 SSE 事件 ID） |
| 双向通信 | 单向（SSE 仅服务器到客户端） | 双向（GET/POST） |
| 水平扩展 | 困难（需要粘性会话） | 容易（无状态、轮询负载均衡） |

**性能对比** [46]：

| 指标 | HTTP+SSE | Streamable HTTP |
|------|----------|-----------------|
| 1000 并发用户下的平均响应时间 | 0.0018s → 1.5112s（退化） | 0.0075s（稳定） |
| TCP 连接数 | 数千 | 数十 |
| 成功率（高并发） | 低 | 100% |

### 6.2 Streamable HTTP vs. STDIO

**适用场景对比** [47]：

| 特性 | STDIO | Streamable HTTP |
|------|-------|-----------------|
| 部署场景 | 本地、单客户端 | 云端、多用户 |
| 通信方式 | 子进程 stdin/stdout | HTTP/HTTPS |
| 消息格式 | 换行符分隔的 JSON-RPC | JSON-RPC over HTTP |
| 安全性 | 无需认证 | 需要认证和安全措施 |
| 扩展性 | 单用户 | 水平扩展 |
| 延迟 | 低 | 略高（网络开销） |
| 适用场景 | IDE 集成、CLI 工具、本地开发 | Web 应用、SaaS 平台、企业部署 |

### 6.3 从有状态到无状态的演进

**2026-07-28 规范的重大变化** [9][48]：

1. **无状态核心**：MCP 从双向有状态协议转变为请求/响应无状态协议
2. **`server/discover` RPC**：服务器必须实现此 RPC 来通告支持的协议版本、能力和身份
3. **多轮往返请求（MRTR）**：引入 `InputRequiredResult` 模式，替代服务器发起的调用（如 `roots/list`、`sampling`）
4. **`subscriptions/listen`**：单一长期存在的 POST 响应流，替代单个变更通知
5. **标准化 HTTP 头部**：`Mcp-Method`、`Mcp-Name`、`Mcp-Param-*` 使流量可路由和缓存
6. **可缓存结果**：`ttlMs` 和 `cacheScope` 字段支持客户端缓存
7. **W3C Trace Context 传播**：标准化分布式追踪

**此演进带来的好处**：
- 任何服务器实例可以处理任何请求（真正水平扩展）
- 无需粘性会话或共享会话存储
- 可与普通 HTTP 基础设施（CDN、API 网关、负载均衡器）无缝协作
- 支持无服务器部署（Vercel、AWS Lambda、Cloudflare Workers）

**此演进的代价**：
- 失去 SSE 流恢复能力
- 需要更复杂的客户端逻辑（每个请求携带完整上下文）
- 增加每个请求的元数据开销

### 6.4 行业采纳情况

多家公司和平台已宣布弃用 HTTP+SSE 以支持 Streamable HTTP [49][50][51][52][53]：
- **Atlassian**：2026 年 3 月弃用 HTTP+SSE，2026 年 6 月 30 日硬截止
- **Keboola**：2026 年 4 月 1 日弃用 SSE，迁移到无状态 Streamable HTTP
- **RapidMCP**：移除 SSE 支持，过渡到新的流式端点
- **Gradio**：提交 Issue 替换弃用的 SSE 传输（Issue #11458，通过 PR #11622 解决）
- **n8n**：v1.99.0 开始支持 Streamable HTTP
- **Zed 编辑器**：PR #39021 添加对最新 MCP 规范（包括 Streamable HTTP）的支持

---

## 7. 总结

Anthropic 的 Streamable HTTP 是 MCP 协议的一次重大架构演进，从两个关键方面改变了 AI 工具通信的方式：

**第一，传输层简化**。通过将旧的 HTTP+SSE 双端点模型替换为单一统一端点，Streamable HTTP 消除了持久连接的需求，使服务器可以完全无状态运行。这带来了显著的可扩展性优势——任何服务器实例可以处理任何请求，支持简单的轮询负载均衡，并与标准 HTTP 基础设施无缝集成。

**第二，流式传输的灵活性**。Streamable HTTP 允许服务器动态决定是返回标准 JSON 响应还是升级到 SSE 流，而不是强制使用 SSE。这种灵活性使协议既适用于简单请求-响应场景，也适用于需要实时流式传输的复杂场景。

**2026-07-28 的无状态演进**是这一架构思想的自然延伸——移除协议级别的会话和初始化握手，使每个请求自描述，进一步简化了部署和扩展。

**工程实现层面**，官方的 TypeScript、Python、Go 和 Java（Spring AI）SDK 都提供了完整的 Streamable HTTP 支持，包括：
- 客户端传输实现（处理 HTTP POST/GET、SSE 流解析、会话管理）
- 服务器端传输实现（处理请求路由、SSE 流创建、安全验证）
- 无状态和有状态两种模式支持
- 与旧版 HTTP+SSE 的后向兼容机制

**关键权衡**在于：Streamable HTTP 在简化架构、提高可扩展性和基础设施兼容性的同时，增加了每个请求的元数据开销，并移除了某些流恢复能力。但总体而言，这些权衡在大多数生产场景中是有利的，这从行业的广泛采纳中可以得到印证。

---

### 资料来源

[1] Introducing the Model Context Protocol: https://www.anthropic.com/news/model-context-protocol

[2] MCP 2025-03-26 Changelog: https://modelcontextprotocol.io/specification/2025-03-26/changelog

[3] MCP 2025-03-26 Transports: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports

[4] MCP Streamable HTTP Examples: https://github.com/invariantlabs-ai/mcp-streamable-http

[5] MCP Specification Basic Transports: https://modelcontextprotocol.io/specification/2025-06-18/basic/transports

[6] MCP 2026-07-28 Streamable HTTP Transport: https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http

[7] MCP Discussion #598 - Streamable HTTP Confusion: https://github.com/orgs/modelcontextprotocol/discussions/598

[8] Reddit r/mcp - SSE vs. Streamable HTTP: https://www.reddit.com/r/mcp/comments/1kdyse2/sse_vs_streamable_http_which_will_be_the_standard

[9] MCP Blog - The 2026-07-28 Specification: https://blog.modelcontextprotocol.io/posts/2026-07-28

[10] Bright Data - SSE vs Streamable HTTP: https://brightdata.com/blog/ai/sse-vs-streamable-http

[11] Christian Posta - Understanding MCP Recent Change Around HTTP+SSE: https://blog.christianposta.com/understanding-mcp-recent-change-around-http-sse

[12] Go SDK streamable.go: https://github.com/modelcontextprotocol/go-sdk

[13] Anthropic Platform Docs - Streaming Messages: https://platform.claude.com/docs/en/build-with-claude/streaming

[14] Anthropic Platform Docs - Fine-grained Tool Streaming: https://platform.claude.com/docs/en/agents-and-tools/tool-use/fine-grained-tool-streaming

[15] The New Stack - How MCP Uses Streamable HTTP: https://thenewstack.io/how-mcp-uses-streamable-http-for-real-time-ai-tool-interaction

[16] TypeScript SDK Repository: https://github.com/modelcontextprotocol/typescript-sdk

[17] TypeScript SDK Issue #861 - StreamableHTTPClientTransport: https://github.com/modelcontextprotocol/typescript-sdk/issues/861

[18] TypeScript SDK Issue #1658 - Session-aware transport: https://github.com/modelcontextprotocol/typescript-sdk/issues/1658

[19] TypeScript SDK Issue #260 - WebStandardStreamableHTTPServerTransport: https://github.com/modelcontextprotocol/typescript-sdk/issues/260

[20] TypeScript SDK Issue #359 - StreamableHTTP module not found: https://github.com/modelcontextprotocol/typescript-sdk/issues/359

[21] TypeScript SDK Issue #484 - HTTP Proxy incompatibility: https://github.com/modelcontextprotocol/typescript-sdk/issues/484

[22] TypeScript SDK Issue #340 - validateSession bug: https://github.com/modelcontextprotocol/typescript-sdk/issues/340

[23] Python SDK Repository: https://github.com/modelcontextprotocol/python-sdk

[24] Python SDK streamable_http_manager.py: https://github.com/modelcontextprotocol/python-sdk/blob/main/src/mcp/server/streamable_http_manager.py

[25] Python SDK Issue #1017 - Documentation errors: https://github.com/modelcontextprotocol/python-sdk/issues/1017

[26] Python SDK v1.8.0 Release: https://github.com/modelcontextprotocol/python-sdk/releases

[27] Python SDK v2.0.0 Release: https://github.com/modelcontextprotocol/python-sdk/releases

[28] Python SDK Issue #1190 - ClosedResourceError: https://github.com/modelcontextprotocol/python-sdk/issues/1190

[29] Python SDK Issue #1941 - Client hang: https://github.com/modelcontextprotocol/python-sdk/issues/1941

[30] Python SDK Issue #1053 - Cloud Run compatibility: https://github.com/modelcontextprotocol/python-sdk/issues/1053

[31] Go SDK Repository: https://github.com/modelcontextprotocol/go-sdk

[32] Go SDK streamable.go: https://github.com/modelcontextprotocol/go-sdk/blob/main/mcp/streamable.go

[33] Go SDK Issue #10 - Streamable HTTP support: https://github.com/modelcontextprotocol/go-sdk/issues/10

[34] Go SDK Design Discussion #364: https://github.com/modelcontextprotocol/go-sdk/discussions/364

[35] Go SDK v1.7.0 Release: https://github.com/modelcontextprotocol/go-sdk/releases

[36] Spring AI MCP Streamable HTTP Starter: https://docs.spring.io/spring-ai/reference/api/mcp/mcp-streamable-http-server-boot-starter-docs.html

[37] Anthropic Platform Docs - API Overview: https://platform.claude.com/docs/en/api/overview

[38] MCP Specification - Transports: https://modelcontextprotocol.io/specification/2025-03-26/basic/transports

[39] Anthropic Platform Docs - Streaming: https://platform.claude.com/docs/en/build-with-claude/streaming

[40] Anthropic Rate Limits: https://platform.claude.com/docs/en/api/rate-limits

[41] TypeScript SDK Streaming Implementation: https://github.com/anthropics/anthropic-sdk-typescript

[42] Claude Code Streaming Watchdog Analysis: https://github.com/orgs/modelcontextprotocol/discussions

[43] MCP Stream Parsing Bug: https://github.com/modelcontextprotocol/servers/issues

[44] Auth0 - Why MCP's Move Away from SSE Simplifies Security: https://auth0.com/blog/mcp-streamable-http

[45] Medium - Understanding MCP's Streamable HTTP Revolution: https://medium.com/aimonks/understanding-mcps-streamable-http-revolution-from-dual-endpoints-to-unified-architecture-0d1396694058

[46] Higress.AI - MCP Protocol: Streamable HTTP Performance: https://ziyou.framer.website/en/blog/mcp-protocol-why-is-streamable-http-the-best-choice

[47] AWS Builder Center - MCP Transport Mechanisms: STDIO vs Streamable HTTP: https://builder.aws.com/content/35A0IphCeLvYzly9Sw40G1dVNzc/mcp-transport-mechanisms-stdio-vs-streamable-http

[48] MCP Blog - The 2026-07-28 MCP Specification Release Candidate: https://blog.modelcontextprotocol.io/posts/2026-05-21

[49] Atlassian MCP Server Deprecation: https://developer.atlassian.com/cloud/jira/platform/mcp/

[50] Keboola MCP Deprecation: https://www.keboola.com/blog/mcp

[51] RapidMCP Transition: https://rapidmcp.com/docs

[52] Gradio Issue #11458: https://github.com/gradio-app/gradio/issues/11458

[53] n8n MCP Server Node: https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-base.mcpServer/
