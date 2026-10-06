import numpy as np

def discrete_moments(values: list, probabilities: list) -> list:
    """
    Returns the first moment, second moment, variance, and standard deviation.
    """
    mean = 0
    second_mom = 0
    for val, prob in zip(values,probabilities):
        mean += val*prob
        second_mom += val**2*prob

    var = second_mom - mean**2
    s_d = np.sqrt(var)
        
    
    
    
    return [mean,second_mom,var,s_d]

    
    pass
