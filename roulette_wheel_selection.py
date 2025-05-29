import numpy as np
import pandas as pd

def roulette_wheel_selection(df: pd.DataFrame, eval_name: str):
    sum_values = np.sum(df[eval_name])
    res = np.zeros((df.shape[0], 2))
    for _ in range(df.shape[0]):
        random_number = np.random.uniform(0, sum_values)
        
        top = 0.0
        for i in range(df.shape[0]):
            top += df.loc[i, eval_name]
            if random_number <= top:
                res[_] = (df.loc[i, 'x1'], df.loc[i, 'x2'])
                break

    return res
