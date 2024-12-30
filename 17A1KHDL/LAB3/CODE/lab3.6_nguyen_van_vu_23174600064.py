import pandas as pd
stocks1 = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks1.csv')
stocks2 = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks2.csv')
companies = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\companies.csv')
stocks = pd.concat([stocks1, stocks2], ignore_index=True)
# 1. Tạo Pivot Table từ DataFrame stocks
pivot_table = stocks.pivot_table(
    values='close', 
    index='date', 
    columns='symbol', 
    aggfunc='mean'
)

# 2. Tính tổng volume giao dịch cho mỗi mã chứng khoán (symbol)
volume_sum = stocks.groupby('symbol')['volume'].sum()

# 3. Sắp xếp Pivot Table dựa trên tổng volume giao dịch từ cao xuống thấp
sorted_volume = volume_sum.sort_values(ascending=False)

# 4. Hiển thị kết quả cho 5 mã chứng khoán có tổng volume giao dịch cao nhất
top_5_symbols = sorted_volume.head(5)
print("5 mã chứng khoán có tổng volume giao dịch cao nhất:")
print(top_5_symbols)

# Hiển thị Pivot Table của các mã này
print("\nPivot Table cho các mã chứng khoán hàng đầu:")
print(pivot_table[top_5_symbols.index])
