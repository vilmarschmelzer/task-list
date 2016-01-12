# coding: utf-8
from django.shortcuts import render
from django.views.generic.base import View


class IndexView(View):

    template = 'index.html'

    def get(self, request):
        return render(request, self.template)
