from flask_restful import Resource, reqparse
from task_list import db
from task_list.models import Task
from flask.ext.sqlalchemy import SQLAlchemy


parser = reqparse.RequestParser()
parser.add_argument('task')


class TaskRestView(Resource):

    def delete(self, id):
        pass

    def post(self):
        args = parser.parse_args()
        print(args)

        task = Task(task=args['task'])
        db.session.add(task)
        db.session.commit()

        return 'Sucesso', 201
