# coding: utf-8
from rest_framework.views import APIView
from taskapp.serializer import TaskSerializer
from json_response import JSONResponse
from taskapp.models import Task
from rest_framework.response import Response
from rest_framework import status


class TaskRestView(APIView):

    def delete(self, request, id=None):
        Task.objects.delete(id)

        return Response(status=status.HTTP_204_NO_CONTENT)

    def get(self, request):

        if id is None:

            tasks = Task.objects.all()
            tasks = TaskSerializer(tasks, many=True)
            return JSONResponse(tasks.data)

    def post(self, request):

        task = TaskSerializer(data=request.data)

        if task.is_valid():
            task.save()

        return JSONResponse(task.data)