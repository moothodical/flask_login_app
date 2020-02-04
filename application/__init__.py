import os
from flask import Flask, request, flash, session
from flask_session import Session
from flask_login import current_user, login_user, logout_user, login_required, LoginManager
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
from flask import render_template, redirect, url_for
from application.forms import LoginForm, RegistrationForm
from application.models import User


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
SESSION_TYPE = 'redis'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)


@app.route('/')
@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()

    if form.validate_on_submit():
        user = User.check_exists(form.username.data)
        if user is None:  # if user does not exist
            flash('That user does not exist', 'danger')
            return redirect(url_for('login'))
        else:  # user does exist
            if not User.check_password(form.username.data, form.password.data):
                flash('Invalid password', 'danger')
                return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        if not next_page:
            next_page = url_for('home')
        flash('Logged in successfully!')
        return redirect(url_for('home'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    print('NOT VALIDATED YET')
    if form.validate_on_submit():
        if check_exists(form.username.data):
            flash(
                f'There is already a user created with the username {form.username.data}', 'danger')
            return redirect(url_for('register'))
        else:
            insert_user(form.username.data,
                        form.email.data, form.password.data)
            flash(
                f'Account created with username {form.username.data}', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', form=form)
