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

class EmprestimoLivroForm(forms.ModelForm):
    contato_pessoal = forms.ModelChoiceField(queryset=ContatoPessoal.objects.all(), required=True, label="Contato Pessoal")

    class Meta:
        model = Livro
        fields = ['contato_pessoal']  # Apenas o contato pessoal para vincular o livro