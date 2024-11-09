import pandas as pd
import numpy as np
truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)
sxbp = ((truth - pred) ** 2).mean()

print("Sai số bình phương trung bình (MSE):", sxbp)