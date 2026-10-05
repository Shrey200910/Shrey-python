import numpy as np


def fit_line(x: np.ndarray, y: np.ndarray) -> tuple[float, float]:
    """
    Simple linear regression by the covariance/variance closed form.

    x, y: shape (n,).

    w = sum((x-mean_x)*(y-mean_y)) / sum((x-mean_x)^2)
    b = mean_y - w * mean_x

    If every x_i is identical, the denominator is 0: return (0.0, mean_y)
    instead of dividing.
    """
    # TODO: compute mean_x, mean_y first, then the two sums in a second pass.
    mean_x = np.mean(x)
    mean_y = np.mean(y)
    
    denominator = np.sum((x - mean_x) ** 2)
    
    if denominator == 0.0:
        return 0.0, float(mean_y)
        
    w = np.sum((x - mean_x) * (y - mean_y)) / denominator
    b = mean_y - w * mean_x
    
    return float(w), float(b)
