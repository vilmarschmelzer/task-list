import os
import logging


class DefaultConfig(object):
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR+'/../', 'task-list.sqlite')

    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'task-list.log'
    LOGGING_LEVEL = logging.DEBUG
