from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import View

# Create your views here.

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "acervo/index.html",)