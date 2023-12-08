# CFA The Time Value of Money in Finance

## Outcome

- Bond Pricing 债券定价
- Value of a Stock 股票定价
- Stock Valuation Models 股票估值模型
  - no growth model
  - constant growth model
  - non-constant growth model
- Implied Return of a Bond 债券隐含收益率
- Implied Return of a Stock 股票隐含收益率
- Stock;s Required Return 股票的要求收益率
- Cash Flow Additivity 现金流可加性
- Application of Cash Flow Additivity 现金流可加性的应用
- Real-World Applications of Cash Flow Additivity 现金流可加性的现实应用 (no-arbitrage) 无套利

## TIME VALUE OF MONEY IN FIXED INCOME AND EQUITY 固定收益和股权的时间价值

### Fixed-Income Instruments and the Time Value of Money 固定收益工具和时间价值

Cash flows from fixed-income instruments:

- Discount(折现): 一次性支付, zero-coupon bond (零息债券), coupon bond (票息债券)
- Perioidic payments(定期支付): 一段时间内的多次支付
- Level payments(定额支付): 每期支付相同金额

#### Example 1: Discount Instruments

$$
\begin{aligned}
\text{PV} &= \frac{\text{FV}}{(1+r)^t}
\end{aligned}
$$

#### Example 2: Coupon Instruments

$$
\begin{aligned}
\text{PV} &= \frac{\text{C}}{(1+r)^1} + \frac{\text{C}}{(1+r)^2} + \cdots + \frac{\text{C}+\text{FV}}{(1+r)^t} \\
&= \text{C} \times \frac{1-\frac{1}{(1+r)^t}}{r} + \frac{\text{FV}}{(1+r)^t}
\end{aligned}
$$

#### Example 3: Annuity Instruments (定额支付)

$$
\begin{aligned}
A = \frac{r(PV)}{1-(1+r)^{-t}}
\end{aligned}
$$
where $A$ is the annuity payment, $r$ is the interest rate, $PV$ is the present value, and $t$ is the number of periods.