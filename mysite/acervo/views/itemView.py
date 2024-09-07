from django.shortcuts import render, get_object_or_404
from django.views import View
from models import Item_pessoal


class ItemView(View):
    def get(self, request, *args, **kwargs):
        id_item = kwargs['pk']
        item = get_object_or_404(Item_pessoal, pk=id_item)
        return render(request, "acervo/item.html", {"item":item})