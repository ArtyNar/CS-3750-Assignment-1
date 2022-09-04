import sqlite3

# Open a file with a database
try:
    con = sqlite3.connect("src/databases/data.db")
    print("Connected successfully")
except sqlite3.Error:
    print("Error open db.\n")

cur = con.cursor()

# Create users table
cur.execute("""
CREATE TABLE IF NOT EXISTS users (
    id integer PRIMARY KEY,
    username text NOT NULL,
    password text NOT NULL
); """)

cur.execute("DELETE FROM users")
con.commit()
con.close()