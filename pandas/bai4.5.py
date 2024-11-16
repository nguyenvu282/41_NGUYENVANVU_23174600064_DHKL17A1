import pandas as pd
import numpy as np

# Tạo Series với 25 giá trị ngẫu nhiên từ phân phối chuẩn có trung bình 10 và độ lệch chuẩn 5
ser = pd.Series(np.random.normal(10, 5, 25))
# 1. Giá trị tối thiểu của ser
min_value = ser.min()
print("Giá trị tối thiể:", min_value)
# 2. Phần trăm thứ 25 của ser
percentile_25 = ser.quantile(0.25)
print("Phần trăm thứ 25 :", percentile_25)
# 3. Trung vị của ser
median_value = ser.median()
print("Trung vị :", median_value)
# 4. Phần trăm thứ 75 của ser
percentile_75 = ser.quantile(0.75)
print("Phần trăm thứ 75 :", percentile_75)
# 5. Giá trị tối đa của ser
max_value = ser.max()
print("Giá trị tối đa:", max_value)