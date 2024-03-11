from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("<h1>Aplicação de enquetes - DSWEB 2024.1</h1> <br> <h2>20231014040013</h2> <br> <h3>Ryan Pinheiro</h3>")