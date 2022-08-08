from flask import Flask
from flask_socketio import SocketIO, send
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# app instance
app = Flask(__name__)

# app configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rps.db'
app.config['SECRET_KEY'] = '5ecret555hhhh'

# enable sockets
# socketio = SocketIO(app)

# connect app to database
db = SQLAlchemy(app)

# enable password encryption for app
bcrypt = Bcrypt(app)

# enable login and establish message parameters
login_manager = LoginManager(app)
login_manager.login_view = 'index'
login_manager.login_message = 'Please sign in or flascreate an account'
login_manager.login_message_category = 'info'

from rps import routes
