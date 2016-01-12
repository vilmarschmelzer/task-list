from rest_framework import serializers
from taskapp.models import Task


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task