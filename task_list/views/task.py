from flask_restful import Resource, reqparse
from task_list import db, auth, app
from task_list.models import Task
from memory_profiler import profile
import json


parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('task')
parser.add_argument('done', type=bool)


class TaskRestView(Resource):

    decorators = [auth.login_required]

    def delete(self, task_id):
        Task.query.filter(Task.id == task_id).delete()
        db.session.commit()
        return 'Sucesso', 204

    def post(self, task_id=None):
        args = parser.parse_args()
        task = Task(task=args['task'], done=args['done'])
        db.session.add(task)

        db.session.commit()

        return 'Sucesso', 201

    def put(self, task_id):
        args = parser.parse_args()

        task = Task.query.getTask(task_id)
        if task is None:
            return 'Tarefa não encontrada', 404

        task.task = args['task']
        task.done = args['done']
        db.session.commit()

        return 'Sucesso', 201

    def get(self, task_id=None):
        if task_id is None:
            tasks = Task.query.all()
            serialized = json.dumps([c.json_dump() for c in tasks])
        else:
            task = Task.query.getTask(task_id)
            serialized = json.dumps(task.json_dump())

        return serialized
