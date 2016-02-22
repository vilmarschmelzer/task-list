from sqlalchemy.orm import Query


class TaskQuery(Query):

    def getTask(self, task_id):
        from task_list.models import Task
        return self.filter(Task.id == task_id).first()
