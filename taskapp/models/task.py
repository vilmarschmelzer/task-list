from django.db import models
from taskapp.manager import TaskManager


class Task(models.Model):
    task = models.TextField()
    done = models.BooleanField(default=False)

    objects = TaskManager()