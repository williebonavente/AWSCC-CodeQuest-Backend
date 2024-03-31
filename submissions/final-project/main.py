from flask import Flask, request, render_template, session, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from itsdangerous import URLSafeTimedSerializer
from flask_mail import Mail, Message
import os

# Initialize Flask-Mail
app = Flask(__name__)
mail = Mail(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(os.getcwd(), 'test.db')
app.config['SECRET_KEY'] = 'developers'  # Needed for sessions
# Add this line
app.config['SECURITY_PASSWORD_SALT'] = '123'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

serializer = URLSafeTimedSerializer('123')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), index=True, unique=True)
    email_verified = db.Column(db.Boolean, default=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        # self.password_hash = generate_password_hash(password)
        self.password = password

    def check_password(self, password):
        # return check_password_hash(self.password_hash, password)
        return self.password == password


class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def set_password(self, password):
        # self.password_hash = generate_password_hash(password)
        self.password = password

    def check_password(self, password):
        # return check_password_hash(self.password_hash, password)
        return self.password == password


@app.route('/')
def home():
    return render_template('home.html')

@app.before_request
def create_tables():
    db.create_all()

# Generate a confirmation token


def generate_confirmation_token(email):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return serializer.dumps(email, salt=app.config['SECURITY_PASSWORD_SALT'])

# Confirm a token
def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = serializer.loads(
            token,
            salt=app.config['SECURITY_PASSWORD_SALT'],
            max_age=expiration
        )
    except:
        return False
    return email

# Send an email
def send_email(to, subject, template):
    msg = Message(
        subject,
        recipients=[to],
        html=template,
        sender=app.config['MAIL_DEFAULT_SENDER']
    )
    mail.send(msg)


def send_confirmation_email(user_email):
    token = generate_confirmation_token(user_email)
    confirm_url = url_for('confirm_email', token=token, _external=True)
    html = render_template('email/activate.html', confirm_url=confirm_url)
    subject = "Please confirm your email"
    msg = Message(subject, sender=app.config['SECURITY_EMAIL_SENDER'], recipients=[user_email])
    msg.html = html
    mail.send(msg)

@app.route('/register', methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        user_by_email = User.query.filter_by(email=email).first()
        user_by_username = User.query.filter_by(username=username).first()
        if user_by_username is not None:
            message = 'Username already in use'
        elif user_by_email is not None:
            message = 'Email already in use'
        else:
            user = User(username=username, email=email, password=password)
            db.session.add(user)
            db.session.commit()
            token = serializer.dumps(user.id, salt='email-verification-salt')
            return redirect(url_for('verify', token=token))
    return render_template('register.html', message=message)

@app.route('/register_success')
def register_success():
    return 'Your account has been created successfully. Please <a href="{}">login</a>.'.format(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            return 'Invalid email or password'
        if not user.email_verified:
            return redirect(url_for('verify'))
            
        session['user_id'] = user.id  # Store the user id in the session
        # Redirect to the passwords page
        return redirect(url_for('handle_passwords'))
    return render_template('login.html')

@app.route('/verify<token>', methods=['GET', 'POST'])
def verify(token):
    try:
        # Check the token
        user_id = serializer.loads(token, salt='email-verification-salt', max_age=3600)
    except:
        return 'The verification link is invalid or has expired.'

    user = User.query.get(user_id)
    if user is None:
        return 'User not found'

    user.email_verified = True
    db.session.add(user)
    db.session.commit()
    return render_template('verified.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove the user_id from the session
    return redirect(url_for('home'))  # Redirect to the home page


def get_current_user():
    if 'user_id' not in session:
        return None
    return User.query.get(session['user_id'])

@app.route('/user/<id>/delete_name', methods=['DELETE'])
def delete_name(id):
    user = User.query.get(id)
    if user is None:
        return 'User not found', 404
    user.username = None
    db.session.commit()
    return render_template('passwords.html', user=user)

@app.route('/user/<id>/update_name', methods=['PUT'])
def update_name(id):
    user = User.query.get(id)
    if user is None:
        return 'User not found', 404
    new_name = request.json.get('username')
    if new_name is None or new_name == '':
        return 'Invalid name', 400
    user.username = new_name
    db.session.commit()
    return render_template('passwords.html', user=user)

@app.route('/passwords', methods=['GET', 'POST'])
def handle_passwords():
    user = get_current_user()
    if not user:  # If the user is not logged in
        return redirect(url_for('login'))  # Redirect to the login page

    if request.method == 'POST':
        # Handle adding a new password
        name = request.form['name']
        password = request.form['password']
        # Add the user ID to the password
        new_password = Password(name=name, password=password, user_id=user.id)
        db.session.add(new_password)
        db.session.commit()

    # Handle viewing all passwords
    # Filter the passwords by the user ID
    passwords = Password.query.filter_by(user_id=user.id).all()
    password_data = []
    for password in passwords:
        password_data.append({
            'id': password.id,
            'name': password.name,
            'password': password.password,
            'username': user.username  # get the user's name
        })
    return render_template('passwords.html', passwords=passwords, user=user)

@app.route('/passwords/<id>', methods=['DELETE'])
def delete_password(id):
    password = Password.query.get(id)
    if password is None:
        return 'Password not found', 404
    db.session.delete(password)
    db.session.commit()
    return 'Password deleted successfully!'


@app.route('/passwords/<id>', methods=['PUT'])
def update_password(id):
    password = Password.query.get(id)
    if password is None:
        return 'Password not found', 404
    new_password = request.json.get('password')
    password.password = new_password
    db.session.commit()
    return 'Password updated successfully!'

# Generate a password reset token


def get_reset_token(email, expires_sec=1800):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    return s.dumps(email, salt='password-reset-salt')

# Verify a password reset token


def verify_reset_token(token):
    s = URLSafeTimedSerializer(app.config['SECRET_KEY'])
    try:
        email = s.loads(token, salt='password-reset-salt', max_age=1800)
    except:
        return None
    return email


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            token = get_reset_token(email)
            # Send an email with the token here...
        return 'An email has been sent with instructions to reset your password.'
    return render_template('reset_password_request.html')


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    email = verify_reset_token(token)
    if not email:
        return 'The reset link is invalid or has expired.'
    user = User.query.filter_by(email=email).first()
    if request.method == 'POST':
        password = request.form['password']
        user.set_password(password)
        db.session.commit()
        return 'Your password has been updated!'
    return render_template('reset_password.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
