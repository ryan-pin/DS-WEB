from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from .models import Livro, Item_pessoal, ContatoPessoal
from .forms import LivroForm, ContatoPessoalForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import EmprestimoLivroForm


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


class EmprestimoLivroView(UpdateView):
    model = Livro
    form_class = EmprestimoLivroForm
    template_name = 'emprestarlivro.html'
    success_url = reverse_lazy('lista')  # Redirecionar para a lista de livros ou outro lugar

    def form_valid(self, form):
        livro = form.save(commit=False)
        livro.disponivel = False  # Marca o livro como indisponível
        livro.save()
        messages.success(self.request, f'O livro "{livro.nome}" foi emprestado com sucesso!')
        return super().form_valid(form)

## FORMS ##

@method_decorator(login_required, name='dispatch')
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'cadastralivro.html'
    success_url = reverse_lazy('acervo:index')

@method_decorator(login_required, name='dispatch')
class ContatoCreateView(CreateView):
    model = ContatoPessoal
    form_class = ContatoPessoalForm
    template_name = 'cadastracontato.html'
    success_url = reverse_lazy('acervo:index')


