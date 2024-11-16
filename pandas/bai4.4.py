import pandas as pd

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

# Yêu cầu 1: Từ ser1 hãy xóa các mục có mặt trong ser2
ser1_unique = ser1[~ser1.isin(ser2)]
print("Các mục trong ser1 mà không có trong ser2:")
print(ser1_unique)

# Yêu cầu 2: Lấy tất cả các mục của ser1 và ser2 nhưng không nằm chung trong cả hai
unique_values = pd.concat([ser1, ser2]).drop_duplicates(keep=False)
print("Các mục không nằm chung trong cả hai series:")
print(unique_values)