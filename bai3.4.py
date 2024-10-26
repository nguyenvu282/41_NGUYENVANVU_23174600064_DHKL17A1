import numpy as np

# Yêu cầu 1: Tạo arr_zeros có 10 phần tử 0, cập nhật phần tử ở vị trí thứ 5 là 1.
arr_zeros = np.zeros(10, dtype=int)
arr_zeros[5] = 1
print("Array arr_zeros sau khi cập nhật:", arr_zeros)

# Yêu cầu 2: Tạo arr_h có giá trị từ 10 đến 24. In danh sách các phần tử theo thứ tự đảo ngược của arr_h.
arr_h = np.arange(10, 25)
arr_h_reversed = arr_h[::-1]
print("Array arr_h theo thứ tự đảo ngược:", arr_h_reversed)

# Yêu cầu 3: Tạo arr_l từ arr_k với các phần tử khác 0.
arr_k = np.array([1, 2, 0, 8, 2, 0, 1, 3, 0, 5, 0])
arr_l = arr_k[arr_k != 0]
print("Array arr_l (phần tử khác 0 từ arr_k):", arr_l)

# Yêu cầu 4: Thêm 2 phần tử có giá trị là 10 và 20 vào cuối array arr_l.
arr_l = np.append(arr_l, [10, 20])
print("Array arr_l sau khi thêm 10 và 20:", arr_l)

# Yêu cầu 5: Thêm phần tử có giá trị 100 vào vị trí có index = 5 trong arr_l.
arr_l = np.insert(arr_l, 5, 100)
print("Array arr_l sau khi thêm 100 ở index 5:", arr_l)

# Yêu cầu 6: Xóa các phần tử tại vị trí có index = 0, 1, 2 trong arr_l.
arr_l = np.delete(arr_l, [0, 1, 2])
print("Array arr_l sau khi xóa các phần tử tại index 0, 1, 2:", arr_l)
