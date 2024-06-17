---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# Cost of Capital
1. WACC (Weighted Average Cost of Capital)
2. Cost of Different Sources of Capital
3. Estimating Beta
4. Flotation Costs
## WACC (Weighted Average Cost of Capital)
$$
WACC = \frac{E}{V} \times r_e + \frac{D}{V} \times r_d \times (1 - T_c) + \frac{P}{V} \times r_p
$$
这里每一项都是边际值
- $E$: market value of equity
- $D$: market value of debt
- $V$: total market value of equity and debt
- $r_e$: cost of equity
- $r_d$: cost of debt
- $T_c$: corporate tax rate
- $P$: market value of preferred stock
- $r_p$: cost of preferred stock
<span style="color:red">market value</span>
## Cost of Different Sources of Capital
- Debt
  - YTM (yield to maturity)
  - Debt rating 利用债券评级
- Equity
  - Preferred stock
  - Common stock
    - CAPM
    - Bond yield plus risk premium
### YTM (yield to maturity) 折现率
$$
P_0 = \frac{PMT}{1 + YTM} + \frac{PMT}{(1 + YTM)^2} + \cdots + \frac{PMT + FV}{(1 + YTM)^n}
$$
- $P_0$: current price
- $PMT$: payment
- $FV$: face value
- $n$: number of periods
### Preferred Stock
$$
r_p = \frac{D}{P}
$$
- $D$: dividend
- $P$: price <span style="color:red">market value</span>
### CAPM (Capital Asset Pricing Model)
$$
E(R_i) = R_f + \beta_i \times (E(R_m) - R_f)
$$
- $E(R_i)$: expected return
- $R_f$: risk-free rate
- $\beta_i$: the return sensitivity of stock $i$ to changes in the market return: 股票的市场敏感性
- $E(R_m)$: expected return of the market
### Bond yield plus risk premium
$$
r_e = r_d + \text{risk premium}
$$
- $r_d$: cost of debt 税前
## Estimating Beta
### Unpublished or thinly traded companies
Two components
- 财务风险
- 属性风险
找到一个相似的公司
$$
\beta_U = \beta_E \times \frac{1}{1 + (1 - t) \frac{D}{E}} \\
\beta_E = \beta_U \times (1 + (1 - t) \frac{D}{E})
$$
- $\beta_U$ : unlevered beta
- $\beta_E$ : levered beta
## Flotation Costs
- First way: incorporate the flotation costs into the cost of capital, 利用高登模型
- Second way: deduct the flotation costs from the initial cash flow, 利用调整后的现金流
