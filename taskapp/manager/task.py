from django.db import models


class TaskManager(models.Manager):

    def delete(self, id):

        task = self.filter(id=id).first()

        if task:
            task.delete()