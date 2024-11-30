import sqlite3
conn = sqlite3.connect("kk.db")
print("Kết nối cơ sở dữ liệu thành công.")

with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        );
    """)
    print("Tạo bảng 'users' thành công.")
conn.close()
print("Đã đóng kết nối cơ sở dữ liệu.")