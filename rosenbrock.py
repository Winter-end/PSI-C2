import numpy as np

def rosenbrock(x1: float, x2: float) -> float:
    return 1/(100*(x2 - x1**2)**2 + (1 - x1)**2 + np.finfo(np.float64).eps)
