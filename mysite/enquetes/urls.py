from . import views
from django.urls import path

urlpatterns = [ #URL /enquetes/ -> lista geral das enquetes
    path("", views.index, name="index"),
    path("<int:pergunta_id>/", views.detalhes, name="detalhes"),
    path("<int:pergunta_id>/resultado", views.resultado, name="resultado"),
    path("<int:pergunta_id>/votacao", views.votacao, name= "votacao"),
]