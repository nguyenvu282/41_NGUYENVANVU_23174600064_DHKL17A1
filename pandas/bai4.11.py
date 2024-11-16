import pandas as pd
oanh = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
sop = [0, 4, 8, 14, 20]

# Trích xuất các mục tại các vị trí trong danh sách pos
result = oanh.iloc[sop]
print("Các mục tại các vị trí trong pos:", result.values)
