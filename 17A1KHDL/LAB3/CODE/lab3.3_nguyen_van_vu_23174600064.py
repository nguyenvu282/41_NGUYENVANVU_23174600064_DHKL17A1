import pandas as pd
stocks1 = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks1.csv')
stocks2 = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks2.csv')
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
stocks['average'] = stocks[['open', 'high', 'low', 'close']].mean(axis=1)
print(stocks.head(5))
