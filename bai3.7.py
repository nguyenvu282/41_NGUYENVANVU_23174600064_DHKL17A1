import numpy as np

# Đọc dữ liệu từ file 'baseball_2D.txt' và lưu vào list 'baseball'
baseball = []
with open('baseball_2D.txt', 'r') as file:
    for line in file:
        height, weight = map(float, line.strip().split())
        baseball.append([height, weight])

# 1. Tạo 2D numpy array tên np_baseball từ baseball
np_baseball = np.array(baseball)
print("Kiểu dữ liệu của np_baseball:", np_baseball.dtype)
print("Kích thước của np_baseball:", np_baseball.shape)

# 2. In các giá trị của dòng thứ 50 trong np_baseball
print("\nDòng thứ 50 trong np_baseball:", np_baseball[49])

# 3. Tạo numpy array np_weight với dữ liệu được lấy từ cột hai của np_baseball
np_weight = np_baseball[:, 1]
print("\nArray np_weight (cân nặng):", np_weight)

# 4. Cho biết chiều cao của vận động viên thứ 124
height_124 = np_baseball[123, 0]
print("\nChiều cao của vận động viên thứ 124:", height_124, "inches")

# 5. Chiều cao trung bình, cân nặng trung bình của các cầu thủ
average_height = np.mean(np_baseball[:, 0])
average_weight = np.mean(np_baseball[:, 1])
print("\nChiều cao trung bình của các cầu thủ:", average_height, "inches")
print("Cân nặng trung bình của các cầu thủ:", average_weight, "pounds")

# 6. Nhận xét về mối tương quan giữa chiều cao và cân nặng
correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]
print("\nHệ số tương quan giữa chiều cao và cân nặng của các cầu thủ:", correlation)

if correlation > 0:
    print("Nhận xét: Chiều cao và cân nặng có mối tương quan thuận.")
elif correlation < 0:
    print("Nhận xét: Chiều cao và cân nặng có mối tương quan nghịch.")
else:
    print("Nhận xét: Không có mối tương quan giữa chiều cao và cân nặng.")
