import pandas as pd
data = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\companies.csv')
df = pd.DataFrame(data)

stocks1 = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks1.csv')
stocks2 = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks2.csv')
companies = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\companies.csv')
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
merged_data = pd.merge(stocks, companies, on='symbol')
average_close_per_company = merged_data.groupby("name")["close"].mean().reset_index()

# Hiển thị 5 công ty đầu tiên trong kết quả
print('5 dòng đầu của file',df.head())
print("\nGiá đóng cửa trung bình cho mỗi công ty:")
print(average_close_per_company.head())