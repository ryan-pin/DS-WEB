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