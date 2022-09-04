import sqlite3
import django

# Open a file with a database
try:
    con = sqlite3.connect("src/databases/data.db")
    print("Connected successfully")
except sqlite3.Error:
    print("Error open db.\n")

cur = con.cursor()

# # Insert into users table
# cur.execute("""
# INSERT INTO users (username, password)
# VALUES('artemkoval', 'qwerty');
# """)

cur.execute("SELECT * FROM users")

# Print query outputs
rows = cur.fetchall()
for row in rows:
    print(row)

# Print query outputs
rows = cur.fetchall()
for row in rows:
    print(row)

con.commit()
con.close()