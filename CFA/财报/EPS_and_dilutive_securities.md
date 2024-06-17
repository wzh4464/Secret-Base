---
toc: true
documentclass: "ctexart"
classoption: "UTF8"
---
# EPS and dilutive securities
LOS 18.g: Describe how earnings per share is calculated and calculate and interpret a company’s earnings per share (both basic and diluted earnings per share) for both simple and complex capital structures.
描述如何计算每股收益，计算和解释公司的每股收益（基本和稀释每股收益）。
LOS 18.h: Contrast dilutive and antidilutive securities and describe the implications of each for the earnings per share calculation.
对比稀释性和非稀释性证券，并描述每种证券对每股收益计算的影响。
## EPS 每股收益
EPS is reported only for shares of common stock:
EPS只针对普通股部分，计算的是普通股股东每股的收益。
资产结构：
- simple capital structure: 只有普通股，没有潜在的稀释性证券，没有可转换债券或优先股
- complex capital structure: 有潜在的稀释性证券，有可转换债券或优先股
## Basic EPS 基本每股收益
不考虑潜在的稀释性证券，只考虑普通股
$$
\text{Basic EPS} = \frac{NI - D}{WS}
$$
- NI: net income 净收益
- D: preferred dividends 优先股股息
- WS: weighted average number of shares outstanding 加权平均流通股数
本年度的优先股股息从净收入中减去，因为每股收益是指普通股股东可获得的每股收益。净收入减去优先股股息是普通股股东可获得的收入。普通股股息不会从净收入中扣除，因为它们是普通股股东可获得的净收入的一部分。普通股的加权平均数是当年流通股的数量，按当年流通的部分加权。
### Weighted average number of shares outstanding 加权平均流通股数
$$
\text{WS} = \sum_{i=1}^{n} \frac{S_i  t_i}{\sum_{i=1}^{n} t_i}
$$
注意：Remember, the payment of a cash dividend on common shares is not considered in the calculation of EPS. 现金股息不会在EPS计算中考虑。
## Diluted EPS 稀释每股收益
考虑潜在的稀释性证券，如可转换债券或优先股
- Dilutive securities: 会降低每股收益的股票期权、可转换债券、可转换优先股，如果exercised or converted到普通股
- Antidilutive securities: 会提高每股收益的股票期权、可转换债券、可转换优先股，如果exercised or converted到普通股
### Adjusted net income numerator
$$
\text{Adjusted net income} = NI - PD + CPSD + (1 - t) CDI
$$
NI: net income 净收益
PD: preferred dividends 优先股股息
CPSD: convertible preferred stock dividends 可转换优先股股息
t: tax rate 税率
CDI: convertible debt interest 可转换债券利息
### Adjusted weighted average number of shares outstanding
$$
\text{Adjusted WS} = WS + \text{shares from conversion of convertible preferred shares} + \text{shares from conversion of convertible debt} + \text{shares issuable from stock options}
$$
在财务报告中，通常需要同时体现基础每股收益（EPS）和稀释每股收益（Diluted EPS）两项内容。这两个指标为投资者和分析师提供了衡量公司盈利能力的重要视角，帮助他们评估每股普通股的盈利表现。
- 基础每股收益（EPS）：计算基础EPS时，分子是给普通股股东的可用净收益（即净收入减去优先股股息），分母是加权平均已发行普通股份数。基础EPS反映了每股普通股在会计期间内的盈利情况，不考虑任何可能的股份稀释效果。
- 稀释每股收益（Diluted EPS）：稀释EPS的计算考虑了所有可能的股份稀释情况，如可转换债券、可转换优先股和股票期权等转换成普通股后的影响。分子可能需要调整以反映这些潜在转换的影响（例如，加回可转换优先股的股息），分母则包括调整后的加权平均股份数，以反映所有潜在的稀释效果。
根据国际财务报告准则（IFRS）和美国通用会计准则（US GAAP），上市公司在其财务报告中呈现EPS时必须同时报告基础EPS和稀释EPS。这样做的目的是提供透明度，使投资者能够看到在没有任何稀释效果和考虑所有可能稀释效果两种情况下，每股普通股的盈利能力。
通过比较基础EPS和稀释EPS，投资者可以评估潜在的稀释效果对公司每股收益的影响程度，这对投资决策非常重要。如果两者之间的差异较大，这可能表明公司有大量的潜在稀释证券，可能在未来对普通股股东的盈利份额产生显著影响。
没有稀释性的那部分股份，就不在稀释EPS的分母中。因为这部分股份不会对每股收益产生负面影响，所以不在稀释EPS的分母中。
通过使用库存股方法，可以在不直接影响净利润的情况下，考虑期权和其他潜在证券的稀释效应。
<!-- red color -->
<span style="color:red">
- 分红按整年计算
- 回购股票按平均股价计算
</span>
