# CFA

## INTEREST RATES, PRESENT VALUE, AND FUTURE VALUE

1. interpret interest rates as required rates of return, discount rates, or opportunity costs
解释利率为所需的回报率，折现率或机会成本
1. interest rate = real risk-free rate + premium
利率=实际无风险利率+溢价
1. calculate and interpret the future value (FV) and present value (PV) of a single sum of money, an ordinary annuity, an annuity due, a perpetuity (PV only), and a series of unequal cash flows
计算和解释单笔资金，普通年金，年金，永续年金（仅PV）和不等现金流的未来价值（FV）和现值（PV）
1. time line
1. different frequency of compounding
不同的复利频率
1. calculate and interpret the effective annual rate (EAR) and annual interest rate (APR)
计算和解释有效年利率（EAR）和年利率（APR）

## Note

### Interest Rates

- Real Risk-free rate: the time preferences of individuals for current versus future real consumption.
不考虑通货膨胀的情况下的无风险利率, 通常是美国国债利率。代表个人对现在和未来消费的偏好
- Inflation premium: The inflation premium compensates investors for the expected erosion of purchasing power of a bond’s future cash flows due to inflation.
通货膨胀溢价补偿投资者对债券未来现金流由于通货膨胀而购买力的预期侵蚀。
- Nominal risk-free rate = real risk-free rate + inflation premium
名义无风险利率 = 实际无风险利率 + 通货膨胀溢价
governmental short-term debt (T-bills) is often used as a proxy for the nominal risk-free rate
政府短期债务（T票）通常用作名义无风险利率的替代品
- Default risk premium: the difference between the interest rate on a U.S. Treasury bond and a corporate bond of equal maturity and marketability
违约风险溢价：美国国债利率与同等期限和市场性的公司债券利率之间的差异
- Liquidity premium:
小公司债券的流动性溢价高于大公司债券
小公司债券不易买卖，因此需要更高的利率来补偿，在出售头寸(position)时，可能会损失更多
美国T票的流动性溢价为零
- Maturity risk premium: The maturity premium compensates investors for the increased sensitivity of the market value of debt to a change in market interest rates as maturity is extended, in general (holding all else equal). The difference between the interest rate on longer-maturity, liquid Treasury debt and that on short-term Treasury debt reflects a positive maturity premium for the longer-term debt (and possibly different inflation premiums as well).
到期风险溢价：到期风险溢价补偿投资者对债务市场价值对市场利率变化的敏感性，因为到期日延长，一般来说（其他条件不变）。较长期限的流动性美国国债利率与短期美国国债利率之间的差异反映了较长期债务的正到期溢价（以及可能的不同通货膨胀溢价）。

### FUTURE VALUE OF A SINGLE CASH FLOW

- Future value (FV)
- Present value (PV)
- Number of periods (n)
- Stated annual interest rate 是年利率，不是实际利率

lump sum (一次性支付): 仍然是 $FV = PV(1+r)^n$
Pension fund: 养老金

$$
FV = PV(1+r)^n
$$

### NON-ANNUAL COMPOUNDING (FUTURE VALUE)

LO: calculate the solution for time value of money problems with different frequencies of compounding

### Annuity (年金)

- Ordinary annuity (普通年金): payments occur at the end of each period
- Annuity due (年金): payments occur at the beginning of each period
- Perpetuity (永续年金): an annuity with an infinite life

### Mortgage (抵押贷款)

- Down payment (首付)
- We use the equation from annuity to calculate the monthly payment

<!-- TODO: Need Review -->

<div style="border: 1px solid red; padding: 10px;">

e.g. 30-year mortgage, 8% interest rate, \$100,000 loan, monthly payment = \$733.76
$$
\begin{align*}
FV &= 100,000 * (1+0.08/12)^{30*12} \\
&=  1.903 * 10^6 \\
A &= FV / \left(\frac{(1+0.08/12)^{30*12}-1}{0.08/12}\right) \\
&= 733.7646
\end{align*}
$$
</div>

## Return

### Geometric Mean Return

$$
\begin{align*}
\text{Geometric Mean Return} &= \left(\prod_{i=1}^n (1+R_i)\right)^{1/n} - 1
\end{align*}
$$
