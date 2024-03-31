from flask import Flask, render_template
import sqlite3
import os

app = Flask(__name__)
app.config["DB_NAME"] = os.path.join(os.path.dirname(__file__), "books.db")


def get_db():
    db = sqlite3.connect(app.config["DB_NAME"])
    db.row_factory = sqlite3.Row
    return db
@app.route("/")
def index():
    connection = get_db()
    books = connection.execute("SELECT * FROM books").fetchall()
    connection.close()
    return render_template("index.html", books=books)



if __name__ == "__main__":
    app.run()