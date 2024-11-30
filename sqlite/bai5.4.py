import sqlite3

conn = sqlite3.connect("vu")
tables = conn.execute("""
    SELECT name 
    FROM sqlite_master 
    WHERE type='table'
    ORDER BY name;
""").fetchall()
if tables:
    print("Các bảng trong cơ sở dữ liệu:")
    for table in tables:
        print(f"- {table[0]}")
else:
    print("Không có bảng nào trong cơ sở dữ liệu.")
conn.close()
