import pandas as pd

dfstock = pd.read_csv('D:\\17A1KHDL\\LAB3\\DATA\\stocks1.csv')
print('5 dòng đầu',dfstock.head()) # muôn hiển thị nhiều hơn thêm 6 vào ô tronngs
print('kiểu dữ liệu mỗi cột trong dòng',dfstock.dtypes)
print('tt tổng quan',dfstock.info()) 



