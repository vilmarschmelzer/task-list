from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .views import IndexView


app = Flask(__name__, instance_relative_config=True)

app.add_url_rule('/', view_func=IndexView.as_view('index'))

# Load the default configuration
app.config.from_object('config.default')

db = SQLAlchemy(app)

# Load the configuration from the instance folder
#app.config.from_pyfile('config.py')

# Load the file specified by the APP_CONFIG_FILE environment variable
# Variables defined here will override those in the default configuration
#app.config.from_envvar('APP_CONFIG_FILE')
