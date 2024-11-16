import numpy as np
import pandas as pd

# Khởi tạo dữ liệu
mylist = list('abcedfghijkImnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)

# Chuyển đổi Series thành DataFrame mà không dùng reset_index()
df = pd.DataFrame({'Character': ser.index, 'Value': ser.values})

# Kết quả
print(df)