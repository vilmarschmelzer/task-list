# coding: utf-8
from django.shortcuts import render
from django.views.generic.base import View
import logging


class IndexView(View):

    template = 'index.html'

    logger = logging.getLogger(__name__)

    def get(self, request):
        self.logger.debug("Pagina index acessada")
        return render(request, self.template)
