import sqlite3
import sqlite3

def create_db():
    conn = sqlite3.connect("expenses.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        category TEXT,
        amount REAL,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()
