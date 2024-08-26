from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View
from .models import Livro, Item_pessoal

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        return render(request, "acervo/index.html", {'livros': livros})

class ItemView(View):
    def get(self, request, *args, **kwargs):
        id_item = kwargs['pk']
        item = get_object_or_404(Item_pessoal, pk=id_item)
        return render(request, "acervo/item.html", {"item":item})

def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'acervo/listar_livros.html', {'livros': livros})
