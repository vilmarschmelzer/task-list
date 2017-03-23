from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
import json
import os
from flask_restful import request
from flask import redirect
import logging


app = Flask(__name__)

if 'APP_SETTINGS' in os.environ:
    app.config.from_object(os.environ['APP_SETTINGS'])
else:
    app.config.from_object('config.DefaultConfig')

db = SQLAlchemy(app)
auth = HTTPBasicAuth()

handler = logging.FileHandler(app.config['LOGGING_LOCATION'])
handler.setLevel(app.config['LOGGING_LEVEL'])
formatter = logging.Formatter(app.config['LOGGING_FORMAT'])
handler.setFormatter(formatter)
app.logger.addHandler(handler)


from .models import User


@auth.verify_password
def verify_password(username, password):
    user = User.query.filter_by(username=username).first()
    if not user or not user.verify_password(password):
        return False
    return True


@app.route('/api/users', methods=['POST'])
def new_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username is None or password is None:
        return 400 # missing arguments
    if User.query.filter_by(username=username).first() is not None:
        return 400 # existing user
    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()
    return user.username, 201


'''@app.route("/logout")
@auth.login_required
def logout():

    return redirect('/')'''

# URLS
from .views import IndexView, TaskRestView, UserRestView
app.add_url_rule('/', view_func=IndexView.as_view('index'))

# Task
app.add_url_rule('/task/', defaults={'task_id': None}, view_func=TaskRestView.as_view('task_'))
app.add_url_rule('/task/<int:task_id>/', view_func=TaskRestView.as_view('task'))

# User
app.add_url_rule('/user/', defaults={'user_id': None}, view_func=UserRestView.as_view('user_'))
app.add_url_rule('/user/<int:user_id>/', view_func=UserRestView.as_view('user'))
