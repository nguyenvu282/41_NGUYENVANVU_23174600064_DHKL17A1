import sqlite3
conn = sqlite3.connect("example.db")

# Tạo bảng
with conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT UNIQUE
        );
    """)
with conn:
    conn.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?);", ("vu", 30, "vu@example.com"))
    conn.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?);", ("oanh", 25, "oanh@example.com"))
    conn.execute("INSERT INTO users (name, age, email) VALUES (?, ?, ?);", ("hoang", 35, "hoang@example.com"))
    print("Chèn bản ghi thành công.")
cursor = conn.execute("SELECT * FROM users;")
records = cursor.fetchall()
for row in records:
    print(row)

# Đóng kết nối
conn.close()
