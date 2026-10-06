from scipy.stats import norm

def normal_distribution(mu: float, sigma: float, x: float) -> dict:
    """
    Returns the z-score, CDF, PDF, and one-standard-deviation probability.
    """

    return {"cdf":norm.cdf(x, loc=mu, scale=sigma),"pdf":norm.pdf(x, loc=mu, scale=sigma),
            "prob_within_1_std":0.6827,"z_score":(x-mu)/sigma}
    pass
