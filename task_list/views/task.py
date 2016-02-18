from flask_restful import Resource, reqparse
from task_list import db
from task_list.models import Task
from flask.ext.sqlalchemy import SQLAlchemy
from flask import jsonify
import json

parser = reqparse.RequestParser()
parser.add_argument('id')
parser.add_argument('task')


class TaskRestView(Resource):

    def delete(self, task_id):
        Task.query.filter(Task.id == task_id).delete()
        db.session.commit()
        return 'Sucesso', 204

    def post(self, task_id=None):
        args = parser.parse_args()

        if 'id' in args:
            task = Task.query.filter(Task.id == args['id']).first()
            if task is None:
                return 'Tarefa não encontrada', 404
            task.task = args['task']
        else:
            task = Task(task=args['task'])
            db.session.add(task)

        db.session.commit()

        return 'Sucesso', 201

    def get(self, task_id=None):
        tasks = Task.query.all()
        serialized = json.dumps([c.json_dump() for c in tasks])
        return serialized


class GetTaskRestView(Resource):

    def get(self, task_id):
        task = Task.query.filter(Task.id == task_id).first()

        if task is None:
            return 'Tarefa não encontrada', 404

        return json.dumps(task.json_dump())
