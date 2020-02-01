from login import db
from login.models import User
from werkzeug.security import generate_password_hash, check_password_hash


def insert_user(username, email, password):
    user = User(username=username, email=email,
                password=generate_password_hash(password, method='sha256'))
    db.session.add(user)
    db.session.commit()


def check_exists(username):
    return User.query.filter_by(username=username).first()


def check_password(username, password):
    user = User.query.filter_by(username=username).first()
    return check_password_hash(user.password, password)
