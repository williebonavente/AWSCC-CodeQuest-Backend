from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'new_books.db')
db = SQLAlchemy(app)

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(120), nullable=False)  # Removed unique=True
    published_year = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}-{self.author}>'

with app.app_context():
    db.create_all()

    new_book = Books(title="To Kill a Mockingbird", author="Harper Lee", published_year=1960)
    db.session.add(new_book)
    db.session.commit()   

if __name__ == '__main__':
    app.run()