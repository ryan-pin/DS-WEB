from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = "acervo"
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('item/<int:pk>/', views.ItemView.as_view(), name='item'),
    path('lista', views.Listarlivros.as_view(), name='lista'),
    path('cad-livro/', views.LivroCreateView.as_view(), name='cadastrar-livro'),
    path('cad-contato/', views.ContatoCreateView.as_view(), name='cadastrar-contato'),
    path('livro/<int:pk>/emprestar/', views.EmprestimoLivroView.as_view(), name='emprestar-livro'),
    path('registrar/', views.RegistroUsuarioView.as_view(), name='registrar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
