from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=100)])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Length(min=6, max=40)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=100),
                                                     EqualTo('confirm_password', message='Passwords must match.')])
    confirm_password = PasswordField('Confirm Password')
    accept_tos = BooleanField('I Accept the TOS', validators=DataRequired())


