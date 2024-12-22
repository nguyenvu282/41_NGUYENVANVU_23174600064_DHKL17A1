import numpy as np
vu = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])


def qdoi_diem(diem):
    if 8.5<=diem<=10:
        return 'A'
    elif 8.0<=diem<=8.4:
        return 'B+'
    elif 7.0<=diem<8:
        return 'B'
    else:
        return'F'

x = [[qdoi_diem(j) for j in i] for i in vu]
