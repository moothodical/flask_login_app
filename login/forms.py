from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=50)], description="enter your username")
    password = PasswordField('Password', validators=[DataRequired(), Length(max=100)], description="enter your password")
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)], description="enter a username")
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=100)], description="enter your email")
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=100),
                                                     EqualTo('confirm_password', message='Passwords must match.')], description="enter a password")
    confirm_password = PasswordField('Confirm Password', description="confirm password")
    submit = SubmitField('Create Account')

