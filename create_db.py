from flask_sqlalchemy import SQLAlchemy
from task_list import app, db

from task_list.models import *

db.create_all()
