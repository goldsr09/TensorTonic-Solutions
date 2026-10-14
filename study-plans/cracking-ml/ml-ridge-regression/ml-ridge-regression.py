import numpy as np

def ridge_regression(X: list, y: list, alpha: float, lr: float, epochs: int) -> tuple:
    """
    Returns the fitted weight list and bias.
    """
    X_mat = np.array(X)
    Y_mat = np.array(y)
    
    n,m = X_mat.shape

    w = np.zeros(m)
    b = 0.0

    for epoch in range(epochs):
        y_pred = np.dot(X_mat,w) + b

        error = y_pred - Y_mat


        db = (2 / n) * np.sum(error)
        dw = (2 / n) * np.dot(X_mat.T, error) + (2 * alpha * w)
        
        # Step C: The Update Function!
        w = w - lr * dw
        b = b - lr * db

    return ([round(num,4) for num in w],round(b,4))
        
    pass
