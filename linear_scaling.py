import numpy as np

def linear_scaling(values: np.ndarray) -> np.ndarray:
    C_ZWIEL = 1.5
    epsilon =  1e-6
    
    values_mean = np.mean(values)
    values_min = np.min(values)
    values_max = np.max(values)

    def condition() -> bool:
        return values_min > ((C_ZWIEL * values_mean - values_max) / (C_ZWIEL - 1))
    
    if condition():
        a = (C_ZWIEL - 1) * values_mean / (values_max - values_mean + epsilon)
        b = values_mean * (values_max - C_ZWIEL * values_mean) / (values_max - values_mean + epsilon)
    else:
        a = values_mean / (values_mean - values_min + epsilon)
        b = - values_min * values_mean / (values_mean - values_min + epsilon)

    return a * values + b
