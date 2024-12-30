import pandas as pd
stocks1 = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks1.csv')
stocks2 = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks2.csv')
companies = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\companies.csv')
stocks = pd.concat([stocks1, stocks2], ignore_index=True)

# Giả sử DataFrame stocks đã được nạp vào từ file dữ liệu của bạn

# 1. Tạo MultiIndex cho DataFrame stocks với cột date và symbol
stocks_multiindex = stocks.set_index(['date', 'symbol'])

# 2. Sử dụng GroupBy để tính giá trung bình (open, high, low, close) và volume trung bình
stocks_grouped = stocks_multiindex.groupby(['date', 'symbol']).mean()

# 3. Sắp xếp dữ liệu theo ngày và mã chứng khoán
stocks_sorted = stocks_grouped.sort_index(level=['date', 'symbol'])

# 4. Hiển thị kết quả cho 5 ngày đầu tiên
print("Kết quả sau khi sắp xếp và tính trung bình:")
print(stocks_sorted.head())
