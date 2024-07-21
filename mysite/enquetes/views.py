from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

from .models import Pergunta, Alternativa

class IndexView(View):
    def get(self, request, *args, **kwargs):
        ultima_pergunta_lista = Pergunta.objects.order_by("-data_pub")
        contexto = {"ultima_pergunta_lista": ultima_pergunta_lista,}
        return render(request, "enquetes/index.html", contexto)

class DetalhesView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id=kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
        return render(request, "enquetes/detalhes.html", {"enquete":pergunta})
    def post(self, request, *args, **kwargs):
        pergunta_id=kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
        try:
            id_votado = request.POST['escolha']
            alt_selec = pergunta.alternativa_set.get(pk=id_votado)
        except (KeyError, Alternativa.DoesNotExist):
            contexto = {
                'enquete': pergunta,
                'error': '!!! Você precisa selecionar uma alternativa para votar!!!'
            }
            return render(request, 'enquetes/detalhes.html', contexto)
        else:
            alt_selec.qtd_votos += 1
            alt_selec.save()
            return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta_id, )))

class ResultadoView(View):
    def get(self, request, *args, **kwargs):
        pergunta_id=kwargs['pk']
        pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
        return render(request, "enquetes/resultado.html", {"enquete":pergunta})


###

'''
def index(request):
    ultima_pergunta_lista = Pergunta.objects.order_by("-data_pub")
    contexto = {"ultima_pergunta_lista": ultima_pergunta_lista,} #httpresponde(template.render(contexto, request) abaixo
    return render(request, "enquetes/index.html", contexto)

def detalhes(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "enquetes/detalhes.html", {"enquete":pergunta})

def resultado(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    return render(request, "enquetes/resultado.html", {"enquete":pergunta})


VOTAÇÂO
def votacao(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id)
    try:
        alt = pergunta.alternativa_set.get(pk=request.POST['escolha'])
    except (KeyError, Alternativa.DoesNotExist):
        contexto = {
            'enquete': pergunta,
            'error': '!!! Você precisa selecionar uma alternativa para votar!!!'
            }
        return render(request, 'enquetes/detalhes.html', contexto)
    else:
        alt.qtd_votos += 1
        alt.save()
        return HttpResponseRedirect(reverse('enquetes:resultado', args=(pergunta_id, )))



versao antiga detalhes -
def detalhes(request, pergunta_id):
    try:
        pergunta = Pergunta.objects.get(pk=pergunta_id)
    except Pergunta.DoesNotExist:
        raise Http404("Pergunta não existe")
    return render(request, "enquetes/detalhes.html", {"enquete":pergunta})
'''