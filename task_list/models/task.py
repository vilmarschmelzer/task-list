from task_list import db


class Task(db.Model):

    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    task = db.Column(db.Text)