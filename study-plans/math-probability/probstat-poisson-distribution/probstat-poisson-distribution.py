from math import exp, factorial

def poisson_distribution(lam: float, max_k: int) -> list:
    pmf = [lam ** k * exp(-lam) / factorial(k) for k in range(max_k + 1)]
    return [
        [round(float(value), 4) for value in pmf],
        round(float(sum(pmf)), 4),
        round(float(pmf[0]), 4),
    ]
