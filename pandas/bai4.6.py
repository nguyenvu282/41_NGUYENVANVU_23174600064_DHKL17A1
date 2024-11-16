import pandas as pd
import numpy as np
ser = pd. Series (np. take(list ('abcdefgh'), np. random. randint(8, size=30)))

#np.take(list('abcdefgh'), np.random.randint(8, size=30)): 
# np.take lấy các giá trị trong danh sách ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'] ,
# tại các vị trí được chỉ định bởi mảng ngẫu nhiên gồm 30 số nguyên từ 0 đến 7,
#  tạo ra một danh sách 30 ký tự ngẫu nhiên từ 'a' đến 'h'
# Tính số lần xuất hiện của mỗi giá trị duy nhất trong ser
value_counts = ser.value_counts()
print("Số lần xuất hiện của mỗi giá trị duy nhất trong ser:")
print(value_counts)