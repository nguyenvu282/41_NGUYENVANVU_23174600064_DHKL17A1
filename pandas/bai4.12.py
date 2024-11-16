import pandas as pd
pdd1 = pd.Series(range(5))
pdd2 = pd.Series(list('abcde'))
# Xếp chồng ser1 và ser2 theo chiều dọc
doc = pd.concat([pdd1, pdd2], axis=0)
# Xếp chồng ser1 và ser2 theo chiều ngang
nhgang = pd.concat([pdd1, pdd2], axis=1)
nhgang.columns = ['pdd1', 'pdd2']  # Đặt tên cột cho dễ đọc
print(doc)
print(nhgang)
