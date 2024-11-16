import pandas as pd
import numpy as np

# Tạo dữ liệu ngẫu nhiên
vu = pd.Series(np.random.random(20))

# Tạo danh sách nhãn cho các phân vị
nhan = []
for i in range(10):
    nhan.append(f'lei {i+1}')

# Chia chuỗi thành 10 phân vị bằng nhau và thay thế bằng tên phân vị
hmm = pd.qcut(vu, q=10, labels=nhan)

print(vu)