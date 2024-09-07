
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from models import Livro
from forms import LivroForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

@method_decorator(login_required, name='dispatch')
class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'cadastralivro.html'
    success_url = reverse_lazy('acervo:index')