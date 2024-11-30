import sqlite3
conn = sqlite3.connect("vu.db")
table_name = "users"
condition = "id = 2" 
with conn:
    conn.execute(f"DELETE FROM {table_name} WHERE {condition};")
    print(f"Hàng có điều kiện '{condition}' đã được xóa.")

# Hiển thị dữ liệu sau khi xóa
cursor = conn.execute(f"SELECT * FROM {table_name};")
records = cursor.fetchall()
for row in records:
    print(row)
conn.close()