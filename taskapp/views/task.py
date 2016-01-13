# coding: utf-8
from rest_framework.views import APIView
from taskapp.serializer import TaskSerializer
from json_response import JSONResponse
from taskapp.models import Task
from rest_framework.response import Response
from rest_framework import status
import logging


class TaskRestView(APIView):

    logger = logging.getLogger(__name__)

    def delete(self, request, id=None):

        if Task.objects.delete(id):

            self.logger.debug('Task removida com sucesso')
            return Response('Tarefa removida com sucesso', status=status.HTTP_204_NO_CONTENT)

        self.logger.debug('Task nº %s não encontrada para remover' % (id))
        return Response('Tarefa não encontrada', status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        tasks = Task.objects.all()
        tasks = TaskSerializer(tasks, many=True)

        self.logger.debug('Buscando Tasks')
        return JSONResponse(tasks.data)

    def post(self, request):

        '''
        O post salva o objeto Task (INSERT | UPDATE), caso a Task tiver id será buscado o objeto altual no banco de dados executar Update,
        Não é identificado que é um novo objeto a ser inserido no banco de dados
        '''

        if 'id' in request.data and request.data['id'] is not None:

            task = Task.objects.filter(id=request.data['id']).first()

            if task is None:
                self.logger.debug('Task não encontrada para atualizar')
                return Response('Tarefa não encontrada para atualizar', status=status.HTTP_404_NOT_FOUND)

            task = TaskSerializer(data=request.data, instance=Task.objects.get(pk=request.data['id']))
            self.logger.debug('Alterando Task')
        else:
            task = TaskSerializer(data=request.data)
            self.logger.debug('Nova Task')

        if task.is_valid():
            task.save()
            self.logger.debug('Task salva como sucesso')
            return JSONResponse(task.data)

        self.logger.debug('Task requisição mal formada')

        return Response('Tarefa inválida, falta informação na tarefa', status=status.HTTP_400_BAD_REQUEST)


class GetTaskRestView(APIView):

    logger = logging.getLogger(__name__)

    def get(self, request,id):

        task = Task.objects.filter(id=int(id)).first()

        self.logger.debug('Buscando Task nº: %s' % (id))

        if task:
            task = TaskSerializer(task)
            self.logger.debug('Task encontrada')
            return JSONResponse(task.data)
        self.logger.debug('Task não encontrada')

        return Response('Tarefa não encontrada', status=status.HTTP_404_NOT_FOUND)


class DoneTaskRestView(APIView):

    logger = logging.getLogger(__name__)

    def get(self, request,id):
        if Task.objects.done(id):
            self.logger.debug('Task nº %s finalizada com sucesso' % (id))
            return Response('Tarefa finalizada com sucesso', status=status.HTTP_204_NO_CONTENT)

        self.logger.debug('Task nº %s não encontrada para finalizar' % (id))
        return Response('Tarefa não encontrada', status=status.HTTP_404_NOT_FOUND)