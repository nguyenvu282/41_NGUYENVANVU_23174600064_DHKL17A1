import numpy as np
import pandas as pd

# Khởi tạo RandomState và tạo Series
np.random.seed(100)
ser = pd.Series(np.random.randint(1, 5, [12]))

# Tìm hai phần tử có tần suất cao nhất
top2 = ser.value_counts().nlargest(2).index

# Thay thế tất cả các phần tử khác bằng 'Other'
ser = ser.apply(lambda x: x if x in top2 else 'Other')

print("Series sau khi thay thế các phần tử còn lại bằng 'Other':")
print(ser)
