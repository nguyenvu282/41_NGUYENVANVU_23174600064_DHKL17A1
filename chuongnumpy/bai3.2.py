# a
import numpy as np
arr = np.arange(0,10)
#print(arr,'kiểu dữ liệu là:',arr.dtype,'---','với kích thước là',arr.size)
#b
arr_odd = arr[arr%2==1]
print(" số lẻ: ",arr_odd)
arr_even = arr[arr%2==0]
print('mảng chẵn là:',arr_even)
#c
arr[arr%2==1]=100
arr_update_1 = arr
print('thay thế lẻ =100:', arr_update_1)