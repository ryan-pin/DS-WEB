from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

app_name = "acervo"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('item/<int:pk>/', views.ItemView.as_view(), name='item'),
    path('list', views.lista_livros, name='lista'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
