import numpy as np
#a
arr_zeros = np.zeros(10)
arr_zeros[5]=1
print(arr_zeros)
#b 
arr_h = np.arange(10,24)
print(arr_h[::-1])
#c
arr_k = np.array([1,2,0,8,2,0,1,3,0,5,0])
arr_l = arr_k[arr_k!=0]
print(arr_l)
#d
arr_l_new = np.append(arr_l,[10,20])
print(arr_l_new)
#e
vu = np.insert(arr_l_new,5,100)
print(vu)
#f
oanh = np.delete(vu,[0,1,2])
print(oanh)