from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Pergunta

def index(request):
    ultima_pergunta_lista = Pergunta.objects.order_by("-data_pub")
    contexto = {"ultima_pergunta_lista": ultima_pergunta_lista,} #httpresponde(template.render(contexto, request) abaixo
    return render(request, "enquetes/index.html", contexto)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "enquetes/detalhes.html", {"enquete":pergunta})

def resultado(request, pergunta_id):
    resultado = "Resultado da enquete de numero %s"
    return HttpResponse(resultado %pergunta_id)


def votacao(request, pergunta_id):
    resultado = "Votação da enquete de numero %s"
    return HttpResponse(resultado %pergunta_id)


###

'''
versao antiga detalhes -
def detalhes(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except Pergunta.DoesNotExist:
        raise Http404("Pergunta não existe")
    return render(request, "enquetes/detalhes.html", {"enquete":pergunta})
'''