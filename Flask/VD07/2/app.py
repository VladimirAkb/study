from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user, UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo, Email, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

DATABASE = 'users.db'

# --- Работа с БД ---

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

# --- Модель пользователя для Flask-Login ---

class User(UserMixin):
    def __init__(self, id_, username, email, password_hash):
        self.id = id_
        self.username = username
        self.email = email
        self.password_hash = password_hash

    @staticmethod
    def get(user_id):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE id = ?', (user_id,)).fetchone()
        conn.close()
        if not user:
            return None
        return User(user['id'], user['username'], user['email'], user['password'])

    @staticmethod
    def get_by_username(username):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        if not user:
            return None
        return User(user['id'], user['username'], user['email'], user['password'])

    @staticmethod
    def get_by_email(email):
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE email = ?', (email,)).fetchone()
        conn.close()
        if not user:
            return None
        return User(user['id'], user['username'], user['email'], user['password'])

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# --- Формы регистрации, логина, изменения профиля ---

class RegisterForm(FlaskForm):
    username = StringField('Логин', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Пароль', validators=[InputRequired(), Length(min=6, max=80)])
    confirm_password = PasswordField('Подтвердите пароль', validators=[InputRequired(), EqualTo('password', message='Пароли должны совпадать')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        if User.get_by_username(username.data):
            raise ValidationError('Логин уже занят')

    def validate_email(self, email):
        if User.get_by_email(email.data):
            raise ValidationError('Email уже зарегистрирован')

class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[InputRequired()])
    password = PasswordField('Пароль', validators=[InputRequired()])
    submit = SubmitField('Войти')

class ProfileForm(FlaskForm):
    username = StringField('Логин', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email()])
    password = PasswordField('Новый пароль (оставьте пустым, чтобы не менять)', validators=[])
    confirm_password = PasswordField('Подтвердите пароль', validators=[EqualTo('password', message='Пароли должны совпадать')])
    submit = SubmitField('Обновить')

    def validate_username(self, username):
        user = User.get_by_username(username.data)
        if user and user.id != current_user.id:
            raise ValidationError('Логин уже занят')

    def validate_email(self, email):
        user = User.get_by_email(email.data)
        if user and user.id != current_user.id:
            raise ValidationError('Email уже зарегистрирован')

# --- Роуты ---

@app.route('/')
@login_required
def home():
    return render_template('home.html', username=current_user.username)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                         (form.username.data, form.email.data, hashed_password))
            conn.commit()
            flash('Регистрация прошла успешно! Войдите, пожалуйста.', 'success')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Пользователь с таким логином или почтой уже существует.', 'danger')
        finally:
            conn.close()
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_username(form.username.data)
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            flash('Вы вошли в систему.', 'success')
            return redirect(url_for('home'))
        else:
            flash('Неверный логин или пароль.', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Вы вышли из системы.', 'info')
    return redirect(url_for('login'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data

        conn = get_db_connection()
        try:
            if password:
                hashed_password = generate_password_hash(password, method='sha256')
                conn.execute('UPDATE users SET username = ?, email = ?, password = ? WHERE id = ?',
                             (username, email, hashed_password, current_user.id))
            else:
                conn.execute('UPDATE users SET username = ?, email = ? WHERE id = ?',
                             (username, email, current_user.id))
            conn.commit()
            flash('Данные профиля обновлены.', 'success')
        except sqlite3.IntegrityError:
            flash('Логин или почта уже заняты другим пользователем.', 'danger')
        finally:
            conn.close()

        # Обновим текущего пользователя для flask-login (перезагрузим)
        user = User.get(current_user.id)
        login_user(user)

        return redirect(url_for('profile'))

    return render_template('profile.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
