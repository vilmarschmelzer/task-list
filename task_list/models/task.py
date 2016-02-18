from task_list import db


class Task(db.Model):

    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.Text)

    def __init__(self, task=None):
        self.task = task

    def json_dump(self):
        return dict(id=self.id, task=self.task)
