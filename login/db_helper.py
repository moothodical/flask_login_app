from login import db
from login.models import User
from login import security


def insert_user(username, email, password):
    encrypted_password = security.encrypt_password(password)
    user = User(username, email, encrypted_password)
    db.session.add(user)
    db.session.commit()


def check_exists(username):
    return User.query.filter_by(username=username).first()
