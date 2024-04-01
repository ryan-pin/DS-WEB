from . import views
from django.urls import path

app_name = "enquetes"
urlpatterns = [ #URL /enquetes/ -> lista geral das enquetes
    path("", views.index, name="index"),
    path("<int:pergunta_id>/detalhes/", views.detalhes, name="detalhes"),
    path("<int:pergunta_id>/resultado", views.resultado, name="resultado"),
    path("<int:pergunta_id>/votacao", views.votacao, name= "votacao"),
]