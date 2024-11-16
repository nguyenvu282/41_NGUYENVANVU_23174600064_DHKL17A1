import pandas as pd
import numpy as np

# Tạo dữ liệu ngẫu nhiên
ser = pd.Series(np.random.randint(1, 10, 7))

# Tìm vị trí của các số là bội của 3
positions = np.where(ser % 3 == 0)[0]


print("Vị trí của các số là bội của 3:", positions)