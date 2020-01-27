
import os
from flask import Flask, request, flash
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
db = SQLAlchemy(app)
from flask import render_template, redirect, url_for
from login.forms import LoginForm, RegistrationForm
from login.db_helper import insert_user


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['POST'])
def login():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for('home'))
    return render_template('login.html', form=form)

@app.route('/register', methods=['POST'])
def register():
    form = RegistrationForm(request.form)
    print('NOT VALIDATED YET')
    if form.validate_on_submit():
        flash('Thanks for registering')
        print('VALIDATED OH')
        insert_user(form.username.data, form.email.data, form.password.data)
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


