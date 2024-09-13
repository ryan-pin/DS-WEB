class EmprestimoLivroForm(forms.ModelForm):
    contato_pessoal = forms.ModelChoiceField(queryset=ContatoPessoal.objects.all(), required=True, label="Contato Pessoal")

    class Meta:
        model = Livro
        fields = ['contato_pessoal']  # Apenas o contato pessoal para vincular o livro