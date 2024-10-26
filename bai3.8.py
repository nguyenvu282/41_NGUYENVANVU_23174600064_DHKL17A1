import numpy as np

# Đọc dữ liệu từ tập tin và lưu vào các danh sách heights và positions
heights = []
positions = []

with open('heights.txt', 'r') as file:
    for line in file:
        heights.append(float(line.strip()))

with open('positions.txt', 'r') as file:
    for line in file:
        positions.append(line.strip())

# 1. a) Tạo numpy array np_positions từ list positions
np_positions = np.array(positions)
print("Kiểu dữ liệu của np_positions:", np_positions.dtype)

# 1. b) Tạo numpy array np_heights từ list heights
np_heights = np.array(heights)
print("Kiểu dữ liệu của np_heights:", np_heights.dtype)

# 2. Tính chiều cao trung bình của các GK
gk_heights = np_heights[np_positions == 'GK']
average_gk_height = np.mean(gk_heights)
print("\nChiều cao trung bình của các GK:", average_gk_height, "inches")

# 3. Tính chiều cao trung bình của những vị trí khác (Không phải là GK)
other_heights = np_heights[np_positions != 'GK']
average_other_height = np.mean(other_heights)
print("Chiều cao trung bình của các vị trí khác (không phải GK):", average_other_height, "inches")

# 4. Tạo mảng dữ liệu có cấu trúc tự định nghĩa players
player_dtype = np.dtype([('position', 'U5'), ('height', 'float')])
players = np.array(list(zip(np_positions, np_heights)), dtype=player_dtype)

# 5. Sắp mảng players theo height, tìm vị trí có chiều cao cao nhất và thấp nhất
players_sorted = np.sort(players, order='height')
tallest_player = players_sorted[-1]
shortest_player = players_sorted[0]

print("\nVị trí có chiều cao cao nhất:", tallest_player['position'], "với chiều cao:", tallest_player['height'], "inches")
print("Vị trí có chiều cao thấp nhất:", shortest_player['position'], "với chiều cao:", shortest_player['height'], "inches")
