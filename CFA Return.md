# CFA Return

## Holding Period Return (HPR)

$$
R = \frac{P_1 - P_0 + I_1}{P_0}
$$

- $P_0$ is the initial price
- $P_1$ is the final price
- $I_1$ is the income received during the period

## Arithmetic or Mean Return

$$
\bar{R_i} = \frac{1}{n} \sum_{t=1}^n R_{it}
$$

## Geometric Mean Return

$$
\bar{R_i} = \sqrt[n]{\prod_{t=1}^n (1 + R_{it})} - 1
$$

A geometric mean return provides a more accurate representation of the growth in portfolio value over a given time period than the arithmetic mean return.

## The Harmomic Mean

Used in cost averaging (The periodic investment of a fixed amount of money.)

## Trimmed Mean

A trimmed mean is the mean calculated after removing a certain percentage of the highest and lowest values.

## Winsorized Mean

A winsorized mean is the mean calculated after replacing a certain percentage of the highest and lowest values with the highest and lowest values.

## Money-Weighted and Time-Weighted Rate of Return

### Money-Weighted Rate of Return

$$
\sum_{t=1}^n \frac{CF_t}{(1 + r)^t} = 0
$$

> Steps:
>
> 1. Suppose the return $r$ (see it as interest rate) is unknown.
> 2. Calculate the present value of all cash flows using the unknown return $r$.
> 3. Solve for $r$.

### Time-Weighted Rate of Return

$$
\prod_{t=1}^n (1 + r_t) = \frac{P_n}{P_0}
$$

> Steps:
>
> 1. Everytime there is a cash flow, normalize the portfolio value to the previous period.
> 2. Calculate the geometric mean return. (Compound return)

### Money-Weighted vs. Time-Weighted

<span style="color:red;">Money-weighted rate reveals the ability of the investor. Time-weighted rate reveals the market performance.</span>
