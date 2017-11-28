from app import app
from flask import request
from models import User
from flask_login import login_user, logout_user, login_required, fresh_login_required


# @app.route('/')
# def index():
#     user = User.query.filter_by(username=username).first()
#     if user:
#         login_user(user, remember=True)
#     return 'You are now logged in!'


#Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'You are now logged out'


@app.route('/fresh')
@fresh_login_required
def fresh():
    return '<h3>you have a fresh login!<h3>'
