import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns mean, median, and mode as Python floats in a dictionary.
    """
    X = np.array(x)

    values, counts = np.unique(X, return_counts=True)
    mode = values[np.argmax(counts)]

    return {"mean":float(np.mean(X)),"median":float(np.median(X)),"mode":float(mode)}
    pass