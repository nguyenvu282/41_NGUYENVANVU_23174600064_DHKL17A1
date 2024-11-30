import sqlite3

# Kết nối tới cơ sở dữ liệu SQLite
conn = sqlite3.connect("example.db")
print("Kết nối cơ sở dữ liệu thành công.")

# Đếm số bản ghi trong bảng
table_name = "users"
record_count = conn.execute(f"SELECT COUNT(*) FROM {table_name};").fetchone()[0]

print(f"Số bản ghi trong bảng '{table_name}': {record_count}")

# Đóng kết nối
conn.close()
