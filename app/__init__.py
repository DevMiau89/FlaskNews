from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flaskext.csrf import csrf

app = Flask(__name__)
app.config.from_object('config')

#Initialize essential objects
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = '/'
login_manager.login_message = 'You need to login'
login_manager.refresh_view = '/'
login_manager.needs_refresh_message = 'You need to re-login to access this page'

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

csrf(app)

from app import views, models
