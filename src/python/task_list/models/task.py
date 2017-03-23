from task_list import db
from task_list.query import TaskQuery


class Task(db.Model):

    __tablename__ = 'task'
    query_class = TaskQuery

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.Text)
    done = db.Column(db.Boolean, default=False)

    def __init__(self, task=None, done=None):
        self.task = task
        self.done = done

    def json_dump(self):
        return dict(id=self.id, task=self.task, done=self.done)
