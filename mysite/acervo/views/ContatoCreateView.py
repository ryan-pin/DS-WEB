from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from models import ContatoPessoal
from forms import ContatoPessoalForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class ContatoCreateView(CreateView):
    model = ContatoPessoal
    form_class = ContatoPessoalForm
    template_name = 'cadastracontato.html'
    success_url = reverse_lazy('acervo:index')