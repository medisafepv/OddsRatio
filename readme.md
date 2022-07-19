## 2x2 Contingency Table

Prospective Randomized study 

![table1.png](table1.png)

#### Sample Odds Ratio 

$$\hat{\Theta} = \frac{n_{11}n_{22}}{n_{12}n_{21}} = \frac{(1)(379)}{(377)(1)} = 1.00531$$

##### Interpretation

The estimated odds of AE occuring (사례발생) for someone taking 시험약 is 1.00531 times more likely of AE occuring for someone taking 대조약. Since $\hat{\Theta} \approx 1$, there is no association between exposure group (drug) vs. outcome (AE occuring).

<div style="page-break-after: always;"></div>

#### Hypothesis Testing: Likelihood Ratio Test

If $\hat{\Theta} \gg 1$, then perform hypothesis test for statistical significance. 

데이터 및 변수 입력 cell:


```python
import pandas as pd

n_11 = 1
n_12 = 377
n_21 = 1
n_22 = 379

d = {"사례 발생" : [n_11, n_21], "사례 미발생" : [n_12, n_22]}
data = pd.DataFrame(d, index=["시험약", "대조약"])

data
```

Liklihood ratio test cell:


```python
from scipy.stats import fisher_exact

oddsr, p = fisher_exact(data, alternative='two-sided')
p
```




    1.0



Using significance level $\alpha = 0.05$

* If `p` < $0.05$, conclude that exposure (drug) and outcome (AE occuring) is **not** independent (reject $H_{0}$)
* If `p` ≥ $0.05$, conclude that exposure (drug) and outcome (AE occuring) is independent (fail to reject $H_{0}$)

Example:
$p = 1 > 0.05 \implies$ exposure (drug) and outcome (AE occuring) is independent (i.e., no association)

<div style="page-break-after: always;"></div>

**INSTRUCTIONS**

1. [https://mybinder.org/v2/gh/medisafepv/OddsRatio/master](https://mybinder.org/v2/gh/medisafepv/OddsRatio/master)

2.  왼쪽 파일 탐색기 패널에서 `exposure_statistics.ipynb` 더블클릭
