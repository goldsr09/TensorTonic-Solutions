from math import comb

def binomial_distribution(n: int, p: float, threshold: int) -> dict:
    """
    Returns the PMF, mean, variance, and probability at least threshold.
    """
    PMF = []
    for i in range(n+1):
        _dist = comb(n,i)*(p**i) * (1-p)**(n-i)
        PMF.append(_dist)
    
        
    
    return {"mean":n*p, 
            "pmf":[round(num,4) for num in PMF],
            "prob_at_least": round(float(sum(PMF[threshold:])), 4),
            "variance": round(float(n * p * (1.0 - p)), 4),
           }
    
    pass
