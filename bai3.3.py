import numpy as np

# Khởi tạo các array
arr_a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
arr_b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

# Yêu cầu 1: Tạo array arr_c chỉ lấy các phần tử xuất hiện ở cả arr_a và arr_b
arr_c = np.intersect1d(arr_a, arr_b)
print("Array arr_c (phần tử xuất hiện ở cả arr_a và arr_b):", arr_c)

# Yêu cầu 2: Tạo array arr_d chứa các phần tử chỉ xuất hiện ở arr_a
arr_d = np.setdiff1d(arr_a, arr_b)
print("Array arr_d (phần tử chỉ xuất hiện ở arr_a):", arr_d)

# Khởi tạo array arr_e
arr_e = np.array([2, 6, 1, 9, 10, 3, 27, 8, 6, 25, 16])

# Yêu cầu 3: Tạo array arr_f chỉ chứa các phần tử từ 5 đến 10 của arr_e
arr_f = arr_e[(arr_e >= 5) & (arr_e <= 10)]
print("Array arr_f (phần tử từ 5 đến 10 trong arr_e):", arr_f)
