## 2x2 Contingency Table

Prospective Randomized study 


|   | 사례 발생 | 사례 미발생   | Total |
|---|---|-----|-------|
| 시험약 | $$n_{11} = 235$$ | $$n_{12} = 8400$$ | $$8635$$ |
| 대조약 | $$n_{21} = 139$$ | $$n_{22} = 9300$$ | $$9439$$ |

#### Sample Odds Ratio 

$$\hat{\Theta} = \frac{n_{11}n_{22}}{n_{12}n_{21}} = \frac{(235)(9300)}{(139)(8400)} = 1.87$$

**Interpretation**

The estimated odds of 사례발생 for 시험약 is 1.87 times more likely than 사례발생 for 대조약.


#### Hypothesis Testing: Likelihood Ratio Test

If $\hat{\Theta} \gg 1$ or $\hat{\Theta} \ll 1$ , then perform hypothesis test for statistical significance. 

Fix significance level $\alpha = 0.05$ and find the p-value `p`,

* If `p` < $0.05$, conclude that 시험약 and 사례발생 are **not** independent (reject $H_{0}$)
* If `p` ≥ $0.05$, conclude that 시험약 and 사례발생 are independent (fail to reject $H_{0}$)

#### Confidence Interval

Note: Standard Error is from [Categorical Data Theory](https://stats.stackexchange.com/questions/266098/how-do-i-calculate-the-standard-deviation-of-the-log-odds).

Fix significance level $\alpha = 0.05$ and find the confidence interval $(\text{LB}, \text{UB})$,

* If $1 \notin (\text{LB}, \text{UB})$, conclude that 시험약 and 사례발생 are **not** independent (reject $H_{0}$)
* If $1 \in (\text{LB}, \text{UB})$, conclude that 시험약 and 사례발생 are independent (fail to reject $H_{0}$)


<div style="page-break-after: always;"></div>

**INSTRUCTIONS**

1. [https://mybinder.org/v2/gh/medisafepv/OddsRatio/master](https://mybinder.org/v2/gh/medisafepv/OddsRatio/master)

2.  왼쪽 파일 탐색기 패널에서 `exposure_statistics.ipynb` 더블클릭
