from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/home')
def home():
    return "Home page"

@app.route('/about')
def about():
    return "This is the about page."

@app.route('/contact')
def contact():
    return "You can contact us at contact@example.com"

if __name__ == "__main__":
    app.run()