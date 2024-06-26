from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path     # <-- add this

DB_NAME = "new_books.db"
db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

 # Connect to the database:
    from .model import Book
    if not path.exists("../instance/" + DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created Database!")

        return app