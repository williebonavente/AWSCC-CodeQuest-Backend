import os
import sqlite3

database_path = os.path.join(os.path.dirname(__file__), "test.db")

connection = sqlite3.connect(database_path)

# print(connection.total_changes)

cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS example (id  INTEGER, name TEXT , age INTEGER)")


cursor.execute("INSERT INTO example VALUES (1, 'alice', 20)")
cursor.execute("INSERT INTO example VALUES (2, 'bob', 30)")
cursor.execute("INSERT INTO example VALUES (3, 'eve', 40)")

connection.commit()


cursor.execute("SELECT * FROM example")
rows = cursor.fetchall()

for row in rows:
    print(row)
    
cursor.execute("DELETE FROM example WHERE id = 1")
cursor.execute("UPDATE example SET age = 31 WHERE id = 2")

# Direct SQL requests
cursor.execute("UPDATE example SET age = 31 WHERE id = 2")
# SQL requests with place holders
age_var = 31
id_var = 2
cursor.execute("UPDATE example SET age = ? WHERE id = ?", (age_var, id_var))


connection.close()