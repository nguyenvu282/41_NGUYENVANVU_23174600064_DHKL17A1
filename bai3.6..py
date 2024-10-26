import numpy as np

# 1. Tạo array arr có kích thước 3x3 với các giá trị True
arr = np.full((3, 3), True)
print("Array arr (3x3 với giá trị True):")
print(arr)

# 2. Tạo array 2 chiều từ arr_ID và đổi cột
arr_ID = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])
arr_2D = arr_ID.reshape((3, 3))
arr_2D[:, [0, 2]] = arr_2D[:, [2, 0]]  # Đổi cột 1 và cột 3
print("\nArray arr_2D sau khi đổi cột 1 và cột 3:")
print(arr_2D)

# 3. Đổi dòng 1 và dòng 2
arr_2D[[0, 1],] = arr_2D[[1, 0], ]
print("\nArray arr_2D sau khi đổi dòng 1 và dòng 2:")
print(arr_2D)

# 4. Đảo ngược các dòng
arr_2D = arr_2D[::-1]
print("\nArray arr_2D sau khi đảo ngược các dòng:")
print(arr_2D)

# 5. Đảo ngược các cột
arr_2D = arr_2D[:, ::-1]
print("\nArray arr_2D sau khi đảo ngược các cột:")
print(arr_2D)

# 6. Kiểm tra giá trị rỗng trong arr_2D_null
arr_2D_null = np.array([[1, 2, 3], [np.NaN, 5, 6], [7, np.NaN, 9], [4, 5, 6]])
has_nan = np.isnan(arr_2D_null).any()
print("\nCó giá trị rỗng trong arr_2D_null không?", has_nan)

# 7. Thay thế giá trị null bằng 0
arr_2D_null[np.isnan(arr_2D_null)] = 0
print("\nArray arr_2D_null sau khi thay thế giá trị null bằng 0:")
print(arr_2D_null)
