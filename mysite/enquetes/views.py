from django.shortcuts import render
from django.http import HttpResponse

from .models import Pergunta

def index(request):
    ultima_pergunta_lista = Pergunta.objects.order_by("-data_pub")
    contexto = {"ultima_pergunta_lista": ultima_pergunta_lista,} #httpresponde(template.render(contexto, request) abaixo
    return render(request, "enquetes/index.html", contexto)

def detalhes(request, pergunta_id):
    resultado = "Detalhes da enquete de numero %s"
    return HttpResponse(resultado %pergunta_id)

def resultado(request, pergunta_id):
    resultado = "Resultado da enquete de numero %s"
    return HttpResponse(resultado %pergunta_id)


def votacao(request, pergunta_id):
    resultado = "Votação da enquete de numero %s"
    return HttpResponse(resultado %pergunta_id)
