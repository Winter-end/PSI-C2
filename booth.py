import numpy as np

def booth(x1: float, x2: float) -> float:
    return 1/((x1 + 2*x2 - 7)**2 + (2*x1 + x2 - 5)**2 + np.finfo(np.float64).eps)