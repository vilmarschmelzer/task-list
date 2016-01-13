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
        tasks = Task.objects.all()
        tasks = TaskSerializer(tasks, many=True)
        return JSONResponse(tasks.data)

    def post(self, request):
        if 'id' in request.data and request.data['id'] is not None:
            task = TaskSerializer(data=request.data, instance=Task.objects.get(pk=request.data['id']))
        else:
            task = TaskSerializer(data=request.data)

        if task.is_valid():
            task.save()

        return JSONResponse(task.data)


class GetTaskRestView(APIView):

    def get(self, request,id):

        task = Task.objects.filter(id=int(id)).first()

        if task:
            task = TaskSerializer(task)
            return JSONResponse(task.data)

        return Response(status=status.HTTP_404_NOT_FOUND)


class DoneTaskRestView(APIView):

    def get(self, request,id):

        Task.objects.done(id)

        return Response(status=status.HTTP_204_NO_CONTENT)