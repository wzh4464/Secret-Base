---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# Positions and short selling

- Long position: 多头头寸
- Short position: 空头头寸
- Leverage position: 杠杆头寸

## Short position

- 两笔
  - Borrowing cost: 借款成本
  - Interest from the short sale proceeds: 空头卖出所得利息
- All dividends and interest on the shorted stock are paid to the lender of the stock.
- Short rebate rate: 空头回购利率
  - The rate at which the short seller can invest the proceeds from the short sale.

## Leveraged position

- Buy on margin: 保证金交易
  - The investor buy securities by borrowing some of the purchase price from a brokerage firm.
  - The borrowed money is the margin loan. Buyer's equity is the portion of the purchase price that is not borrowed.
- Call money rate: 购买保证金交易的利率
  - The interest rate charged on the margin loan.
- Financing leverage ratio: 融资杠杆比率
  - The ratio of the amount of the margin loan to the investor's equity in the transaction.
- Initial margin requirement: 初始保证金要求
  - The minimum percentage of the purchase price that the investor must be buyer's equity.
- Maintenance margin requirement: 维持保证金要求
  - The minimum amount of equity that the investors must maintain in the margin account.
- Margin call: 保证金追缴
  - A demand by the brokerage firm for the investor to deposit additional funds or securities to bring the margin account up to the minimum maintenance margin requirement.

### Price triggering the margin call

$$
P_c = P_0 \frac{1 - IM}{1 - MM}
$$
假设：先亏自己的钱，再亏借来的钱。
Margin call 条件: 自有资金占比小于$MM$.
-$P_c$: Price triggering the margin call
-$P_0$: Initial price of the stock
-$IM$: Initial margin requirement
-$MM$: Maintenance margin requirement
