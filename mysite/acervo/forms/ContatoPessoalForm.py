from django import forms
from models import ContatoPessoal

class ContatoPessoalForm(forms.ModelForm):
    class Meta:
        model = ContatoPessoal
        fields = ['email', 'telefone']