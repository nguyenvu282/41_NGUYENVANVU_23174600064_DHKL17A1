import pandas as pd
chuoi_1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
chuoi_2 = pd.Series([1, 3, 10, 13])

vi_tri = []
for gia_tri in chuoi_2:
    if gia_tri in chuoi_1.values:
        vi_tri.append(chuoi_1[chuoi_1 == gia_tri].index[0])

print("Vị trí của các mục của chuoi_2 trong chuoi_1:", vi_tri)
