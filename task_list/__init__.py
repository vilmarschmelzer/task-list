from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])

db = SQLAlchemy(app)

# URLS
from .views import IndexView, TaskRestView, GetTaskRestView
app.add_url_rule('/', view_func=IndexView.as_view('index'))
app.add_url_rule('/task/<task_id>/', view_func=TaskRestView.as_view('task'))
app.add_url_rule('/task/', defaults={'task_id': None}, view_func=TaskRestView.as_view('task_'))
app.add_url_rule('/get-task/<task_id>/', view_func=GetTaskRestView.as_view('get-task'))
