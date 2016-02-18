#from migrate.versioning import api
#from config.default import SQLALCHEMY_DATABASE_URI
#from config.default import SQLALCHEMY_MIGRATE_REPO
from task_list import db
from task_list.models import *
import os.path
db.create_all()

#db.session.add(Task('dasdada'))
#db.cummit()


#if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
#    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
#    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#else:
#    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
