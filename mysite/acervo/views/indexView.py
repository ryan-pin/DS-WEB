from django.shortcuts import render
from django.views import View
from models import Livro


class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, "acervo/index.html", {'livros': livros})