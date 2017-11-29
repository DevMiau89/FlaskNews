from app import app
from flask import request, render_template, session, abort
from models import User
from flask_login import login_user, logout_user, login_required, fresh_login_required


@app.route('/', methods=['GET', 'POST'])
def index():
    # user = User.query.filter_by(username=username).first()
    # if user:
    #     login_user(user, remember=True)
    return render_template('index.html')


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


@app.route('/register')
def register():
    return render_template('register.html')


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = some_random_string()
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token
