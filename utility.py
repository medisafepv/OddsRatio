import pandas as pd
from scipy.stats import fisher_exact
import scipy.stats
import math

def input_data_param(alph, r1, r2, n11, n12, n21, n22):
    d = {"사례 발생" : [n11, n21], "사례 미발생" : [n12, n22]}
    return pd.DataFrame(d, index=[r1, r2])
    
def compute_sample_odds_ratio(r1, r2, n11, n12, n21, n22):
    odds = (n11 * n22) / (n12 * n21)
    print("The estimated odds of 사례발생 for {} is {:.2f} times more likely than 사례발생 for {}".format(r1, odds, r2))
    # return odds

def conduct_likelihood_ratio_test(data, alph, r1, alternative='two-sided'):
    oddsr, p = fisher_exact(data, alternative='two-sided')

    if p < alph:
        print("Since {:.3f} < {}, {} and 이상사례 are not independent (reject the H0)".format(p, alph, r1))
    else:
        print("Since {:.3f} ≥ {}, {} and 이상사례 are independent (fail to reject the H0)".format(p, alph, r1))

def find_confidence_interval(alph, r1, r2, n11, n12, n21, n22):
    # Find Z critical value
    Z = scipy.stats.norm.ppf(1 - alph / 2)
    
    # Standard Error of Log Odds Ratio from Categorical Data Theory
    se = pow((1 / n11) + (1 / n12) + (1 / n21) + (1 / n22), 0.5)
    
    log_odds = math.log((n11 * n22) / (n12 * n21))
    
    LB = pow(math.e, log_odds - Z * se)
    UB = pow(math.e, log_odds + Z * se)
    print("{:.0f}% Confidence Interval for the Log Odds Ratio of 이상사례 and {}:".format((1 - alph) * 100, r1))
    print("    ({:.2f}, {:.2f})".format(LB, UB))
    
    if 1 >= LB and 1 <= UB:
        print("Since 1 is in ({:.2f}, {:.2f}), we conclude that {} and 이상사례 are independent (fail to reject the H0)".format(LB, UB, r1))
    else:
        print("Since 1 is not in ({:.2f}, {:.2f}), we conclude that {} and 이상사례 are not independent (reject the H0)".format(LB, UB, r1))