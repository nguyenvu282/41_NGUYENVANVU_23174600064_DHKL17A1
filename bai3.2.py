import numpy as np
arr = np.arange(0,10)
# a)
print(arr)
print("kiểu dữ liệu của mảng là")
print(arr.dtype)
print("kích thước của mảng là")
print(arr.shape)
#b)
ar_odd = arr[arr%2==1]
ar_even= arr[arr%2==0]
print(ar_odd)
print(ar_even)
#c)
arr_up = arr.copy()
arr_up[arr_up % 2 == 1] = 100
print(arr_up)
