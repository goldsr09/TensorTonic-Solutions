import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns sample variance and standard deviation as Python floats.
    """

    X = np.array(x)
    mean = np.mean(X)

    sos = [(num-mean)**2 for num in X]
    var = sum(sos)/(len(X)-1)
    return {"variance":float(var), "std_dev": float(np.sqrt(var))}
    pass