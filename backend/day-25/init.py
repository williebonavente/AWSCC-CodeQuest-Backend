import sqlite3
import os

connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), "books.db"))
schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
with open(schema_path) as f:
    connection.executescript(f.read())

current = connection.cursor()
current.execute(
    '''
    INSERT INTO books (title, author, published_year)
    VALUES ('To Kill a Mockingbird', 'Harper Lee', 1960);
    '''
)
connection.commit()
connection.close()
