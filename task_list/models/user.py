from task_list import db
from passlib.apps import custom_app_context as pwd_context


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username

        self.hash_password(password)

    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)

    def json_dump(self):
        return dict(id=self.id, username=self.username)
