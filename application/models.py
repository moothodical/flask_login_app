from application import login_manager
from application import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

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

    def __repr__(self):
        return f"User: {self.user_id}, {self.username}, {self.email}"

    def get_id(self):
        return self.user_id

    @login_manager.user_loader
    def load_user(user_id):  # used to load user, flask_login knows nothing about DB
        return User.query.get(int(user_id))
