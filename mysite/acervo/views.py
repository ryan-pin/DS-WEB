from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.views import View
from .models import Livro, Item_pessoal, ContatoPessoal
from .forms import LivroForm, ContatoPessoalForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import EmprestimoLivroForm, RegistroUsuarioForm
from django.contrib.auth import login, authenticate


# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.filter(disponivel=True)
        return render(request, "acervo/index.html", {'livros': livros})

class ItemView(View):
    def get(self, request, *args, **kwargs):
        id_item = kwargs['pk']
        item = get_object_or_404(Item_pessoal, pk=id_item)
        return render(request, "acervo/item.html", {"item":item})


class Listarlivros(View):
    def get(self, request, *args, **kwargs):
        livros = Livro.objects.all()
        livros_disp = Livro.objects.filter(disponivel=True)
        livros_indisp = Livro.objects.filter(disponivel=False)

        context = {
            'livros': livros,
            'livros_disp': livros_disp,
            'livros_indisp': livros_indisp,
            }
        return render(request, "acervo/listar_livros.html", context)

@method_decorator(login_required, name='dispatch')
class EmprestimoLivroView(UpdateView):
    model = Livro
    form_class = EmprestimoLivroForm
    template_name = 'emprestarlivro.html'
    success_url = reverse_lazy('acervo:index')

    def form_valid(self, form):
        livro = form.save(commit=False)
        livro.disponivel = False
        livro.save()
        messages.success(self.request, f'O livro "{livro.nome}" foi emprestado com sucesso!')
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class DevolverLivroView(View):
    def post(self, request, *args, **kwargs):
        livro_id = kwargs['pk']
        livro = get_object_or_404(Livro, pk = livro_id)
        livro.disponivel = True
        livro.contato_pessoal = None
        livro.save()
        return redirect("acervo:index")


## FORMS ##

class RegistroUsuarioView(CreateView):
    model = User
    form_class = RegistroUsuarioForm
    template_name = 'registrar.html'
    success_url = reverse_lazy('acervo:index')

    def form_valid(self, form):
        response = super().form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
        return response


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

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

