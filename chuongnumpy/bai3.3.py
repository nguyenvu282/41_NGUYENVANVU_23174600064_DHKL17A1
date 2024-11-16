import numpy as np
arr_a = [1,2,3,2,3,4,3,4,5,6]
arr_b = [7,2,10,2,7,4,9,4,9,8]
#a
arr_c  = []
for i in arr_a:
    if i in arr_b and i not in arr_c:
        arr_c.append(i)
print(arr_c)    
#b
arr_d = []
for i in arr_a:
    if i not in arr_b and i not in arr_d:
        arr_d.append(i)
print(arr_d)        
#c
arr_e = np.array([2,6,1,9,10,3,27,8,6,25,16])
arr_f = arr_e[(arr_e>5)&(arr_e<=10)]
print(arr_f)