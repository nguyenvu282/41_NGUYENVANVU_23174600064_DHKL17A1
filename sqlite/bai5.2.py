import sqlite3
conn = sqlite3.connect(":memory:")
version = conn.execute("SELECT sqlite_version();").fetchone()[0]
print(f"Phiên bản SQLite: {version}")
conn.close()
