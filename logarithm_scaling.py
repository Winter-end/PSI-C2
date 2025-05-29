import numpy as np

def logarithm_scaling(values: np.ndarray) -> np.ndarray:
    log_values = np.log2(values)
    b = np.max(log_values)

    return b + 0.1 - log_values