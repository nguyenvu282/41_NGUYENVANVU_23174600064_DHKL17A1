import numpy as np
GK = "Goalkeeper"
M = "Midfield"
A = "Attack"
D = "Defend"
height = [1,2,3,4,56,7,88,9]
position = [GK,M,A,D,M,D,M,M,M,A,M,M,A,A,]
arr_hei = np.array(height)
arr_posi = np.array(position)
vu = arr_hei[arr_posi[arr_posi==GK]]
print(vu)