import numpy as np
#a
arr=np.full((3,3),True)
print(arr)
#b
arr_1d = np.array([0,1,2,3,4,5,6,7,8])
arr_2d = np.reshape(arr_1d,(3,3))
arr_2d[:,[2,0]]=arr_2d[:,[0,2]]
print(arr_2d)
#c
arr_2d[[0,1],:]=arr_2d[[1,0],:]
print(arr_2d)
#d
vu = arr_2d[::-1,:]
print(vu)
#e
hmm = arr_2d[:,::-1]
#print(hmm)
#f
arr_2d_null = np.array([[1,2,3],[np.NaN,5,6],[7,np.NaN,9],[4,5,6]])
print('trong mảng có giá trị NaN :',np.isnan(arr_2d_null))
#g
vu = np.nan_to_num(arr_2d_null,nan=0)
print(vu)
