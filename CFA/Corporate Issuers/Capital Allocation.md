# Capital Allocation

## Capital Allocation Process

- Idea Generation
- Investment Analysis
- Capital Allocation Planning
- Monitoring and Post-audit

## Types of Capital Allocation

- Replacement Projects 体量不变
- Expansion Projects 体量增加
- New Products or Services 体量增加
- Regulatory, Safety and Environmental Projects 体量不变
- Others
  - Management pet projects
  - High-risk projects

<!-- red color -->
## <span style="color:red"> Capital Budgeting Process</span>

- Decisions are based on cash flows
- Decisions are not based on accounting net income or operating income
- Cash flows are based on opportunity costs
- Cash flows are analyzed on an after-tax basis
- Timing of cash flows is crucial
- Financing costs are ignored (在折现率中已经考虑了)
- Sunk costs are ignored

### Capital Allocation Assumptions

- Opportunity cost
- Incremental cash flows
- Cannibalization 负效应，比如产品之间的互相影响

## Investment Decision Criteria 定量分析

### NPV (Net Present Value)

$$
NPV = \sum_{t=0}^{n} \frac{CF_t}{(1+r)^t} - Outlay
$$

- NPV > 0, accept
- 都折现到$0$时刻
- 减去 outlay
- 可以用计算器计算

#### 优点

- 具体化了投资的价值
- 正值的NPV意味着投资的回报率高于折现率
- 考虑了时间价值

#### 缺点

- 需要预测未来的现金流
- 体量没有被考虑

### IRR (Internal Rate of Return) 回报率

$$
\sum_{t=0}^{n} \frac{CF_t}{(1+IRR)^t} - Outlay = 0
$$

#### 优点

- 体量被考虑

#### 缺点

- 再投资的假设
- 多个 IRR 解
- 和NPV不一致的时候，NPV优先

### ROIC Return on Invested Capital

$$
\text{ROIC} = \frac{\text{NOPAT (Net Operating Profit After Tax)}}{\text{Average book value of invested capital}}
$$

<span style="color:red">注意是账面价值</span>

#### 投资标准

- ROIC > Cost of Capital

## Real Options

- Timing option 在之后再投资
- Size option
  - Abandonment option 允许放弃如果财务结果不好
  - Growth option 允许扩大规模
- Flexibility option
  - Price-setting option
  - Product-flexibility option
- Fundamental Options
  - Options are embedded in a project that can raise its value
  - The payoffs are contingent on an underlying asset, just like a financial option
