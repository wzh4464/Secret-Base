# tick-level 市场数据处理系统的低延迟 C++ 架构设计

## 目标

构建一个可用于高频交易（HFT）的 超低延迟市场数据处理系统，涵盖以下功能：
1. Tick-level 数据接收（ingestion）
2. 订单簿构建（Order Book Construction）
3. 策略触发（Strategy Triggering）

## 系统架构总览

```
+-------------------+     +----------------+     +------------------+     +-------------------+
| NIC + Kernel Bypass| -->| Market Feed     | -->| Order Book Engine| --> | Strategy Executor |
| (e.g. Solarflare) |     | Handler (C++)   |     | (Lock-free C++)  |     | (Real-time)       |
+-------------------+     +----------------+     +------------------+     +-------------------+
         |                         |                      |                         |
     FPGA (optional)        Multicast/UDP           Depth-1/Full Book        Order placement queue
```

## 技术选型（核心模块）

### 模块与延迟控制策略

| 模块 | 技术选型 | 延迟控制策略 |
|------|----------|--------------|
| 网络接收（Ingestion） | DPDK / Solarflare Onload | Kernel bypass, Poll Mode Driver |
| 数据解析 | C++20 + constexpr优化 | Zero-copy, memory-aligned buffers |
| 内存管理 | Arena Allocator / custom pool | 避免 malloc/free 抖动 |
| 订单簿引擎 | Lock-free ring buffer + SoA | False sharing 避免，预取优化 |
| 策略触发器 | L1 cache-local + batching | 批量触发，避免 cache miss |
| 系统调度 | Thread Affinity + Isolation | CPU core pinning，NUMA-aware allocation |
| 通信（下单） | Shared memory + UNIX domain | 比 TCP 快数十倍 |

## 核心设计详解：Tick-level 数据处理与订单簿构建

### 1. Tick Ingestion (UDP Multicast)
- 使用 DPDK / Solarflare Onload 来绕过内核栈，提供子微秒级延迟。
- Packet Handler 使用单独线程绑定 CPU core，轮询接收，避免中断造成 jitter。

```cpp
while (true) {
    auto* pkt = dpdk_recv();
    if (likely(pkt)) {
        feedHandler.parse(pkt);  // constexpr-based parser
    }
}
```

### 2. Market Feed Parsing (C++)
- 使用 固定大小内存池 + memcpy + bit-field struct 对 feed 数据进行零拷贝解析。
- 示例（假设为 ITCH 格式）：

```cpp
struct alignas(64) AddOrderMsg {
    char msgType;
    uint64_t orderID;
    uint32_t price;
    uint32_t size;
    char side;
};
```

- 使用 constexpr 解码表，避免运行时判断。

### 3. Order Book Construction
- 采用 Price Level HashMap + sorted deque（或 skip list）组织每一档报价。
- 为避免锁带来的延迟，使用单线程 + lock-free 数据结构。

```cpp
class OrderBook {
public:
    void onAddOrder(...);
    void onDeleteOrder(...);
    BestBidAsk getTopOfBook() const;
private:
    alignas(64) std::unordered_map<uint64_t, Order> orders;
    std::map<uint32_t, PriceLevel> bidLevels;
    std::map<uint32_t, PriceLevel> askLevels;
};
```

- 对于策略只需要 top-of-book 的情况，可缓存 bid/ask。

### 4. Strategy Triggering
- 策略模块应尽可能运行在 L1-cache local 数据结构上。
- 使用 ring buffer 或 lock-free queue 连接订单簿和策略模块。
- 采用 batching 技术，避免频繁触发。

```cpp
void StrategyEngine::onTopOfBookUpdate(const TopOfBook& tob) {
    if (tob.spread < threshold) {
        placeOrder(...);
    }
}
```

## 延迟控制手段总结（系统级）

### 优化层面与手段

| 优化层面 | 手段 |
|----------|------|
| 网络 | kernel bypass (DPDK, Onload), NIC tuning |
| 内存 | HugePages, NUMA binding, memory pools |
| CPU | Core pinning, cache prefetch, HT off |
| 编译器 | -O3, -march=native, PGO/LTO |
| 架构 | Avoid locks, reduce branching, zero-copy |
| 异常处理 | 无异常路径，全部 use return-code |

## 性能指标（目标）

### 模块延迟目标

| 模块 | 延迟目标 |
|------|----------|
| 数据接收 (tick ingest) | < 2 µs |
| 订单簿构建 | < 5 µs |
| 策略触发 | < 3 µs |
| 全链路（tick-to-action） | < 10 µs (99.9%) |

## 可选高级优化
- ✅ FPGA 预解析 feed，减少 CPU 开销
- ✅ RDMA 通信到下单模块，降低系统间延迟
- ✅ SIMD 批量处理更新指令（e.g., AVX512）
