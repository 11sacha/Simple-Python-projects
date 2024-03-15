import sqlite3

try:
    with (sqlite3.connect("expenses.db")) as conn:
        cur = conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS expenses
                    (id INTEGER PRIMARY KEY,
                    Date DATE,
                    description TEXT,
                    category TEXT,
                    price REAL)""")
                    
        conn.commit()

except sqlite3.Error as e:
    print(f"Error: {e}")

