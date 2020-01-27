from login import app
from flask import render_template, redirect, url_for, Blueprint
from login.forms import RegistrationForm, LoginForm

@app.route('/')
def home():
    return render_template('home.html')

