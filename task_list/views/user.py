from flask_restful import Resource, reqparse
from task_list import db, auth
from task_list.models import User
import json

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)
parser.add_argument('username')
parser.add_argument('password')


class UserRestView(Resource):

    def delete(self, user_id):
        User.query.filter(User.id == user_id).delete()
        db.session.commit()
        return 'Sucesso', 204

    def post(self, user_id=None):
        args = parser.parse_args()
        user = User(username=args['username'], password=args['password'])
        db.session.add(user)

        db.session.commit()

        return 'Sucesso', 201

    def put(self, user_id):
        args = parser.parse_args()

        user = User.query.get(user_id)
        if user is None:
            return 'Usuário não encontrado', 404

        user.username = args['username']
        user.hash_password(args['password'])

        db.session.commit()

        return 'Sucesso', 201

    def get(self, user_id=None):
        if user_id is None:
            users = User.query.all()
            serialized = json.dumps([c.json_dump() for c in users])
        else:
            user = User.query.get(user_id)
            serialized = json.dumps(user.json_dump())

        return serialized
