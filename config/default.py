import os

# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


DEBUG = True
SQLALCHEMY_ECHO = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR+'/../', 'task-list.sqlite')