import sqlite3

# Kết nối tới cơ sở dữ liệu SQLite
conn = sqlite3.connect("example.db")
print("Kết nối cơ sở dữ liệu thành công.")

# Tên bảng và cột cần cập nhật
table_name = "users"
column_name = "age"
new_value = 40
with conn:
    conn.execute(f"UPDATE {table_name} SET {column_name} = ?;", (new_value,))
    print(f"Tất cả các giá trị trong cột '{column_name}' đã được cập nhật thành {new_value}.")
cursor = conn.execute(f"SELECT * FROM {table_name};")
records = cursor.fetchall()

print("Các bản ghi sau khi cập nhật:")
for row in records:
    print(row)

# Đóng kết nối
conn.close()