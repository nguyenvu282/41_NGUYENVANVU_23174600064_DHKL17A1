import pandas as pd
dfstock = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks1.csv')
#print('kiểm tra xem có dữ liệu null ko',dfstock.isnull())
dfstock['high'] = dfstock['high'].fillna(dfstock['high'].mean()) 
#print(dfstock['high'])
dfstock['low'] = dfstock['low'].fillna(dfstock['low'].mean()) 
#print(dfstock['low'])
print('hiển thị tt ko còn dũ liệu null',dfstock.info())