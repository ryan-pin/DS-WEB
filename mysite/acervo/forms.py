from django import forms
from .models import Livro, ContatoPessoal

class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['nome', 'autor', 'ano', 'foto_capa']

class ContatoPessoalForm(forms.ModelForm):
    class Meta:
        model = ContatoPessoal
        fields = ['email', 'telefone']