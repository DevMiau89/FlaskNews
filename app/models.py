from app import db
from app import login_manager
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=True)
    last_name = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(255), unique=True)
    salt = db.Column(db.String(72))
    password = db.Column(db.String(20), unique=True)

    @staticmethod
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymus(self):
        return False

    def get_id(self):
        return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % self.username


