from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ContatoPessoal(models.Model):
    email = models.CharField(max_length=100, unique=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)
    usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    def __str__(self): #overwrite
        return "{} ".format(self.email)

class Livro(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 50)
    ano = models.IntegerField("Data de Publicação")
    foto_capa = models.ImageField(upload_to = 'uploads/')
    disponivel = models.BooleanField(default=True)
    contato_pessoal = models.ForeignKey(ContatoPessoal, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self): #overwrite
        return "{} - {} - {} ({})".format(self.nome, self.autor, self.ano, self.id)

class Item_pessoal(models.Model):
    nome = models.CharField(max_length = 100)
    autor = models.CharField(max_length = 50)
    ano = models.IntegerField("Data de Publicação")
    foto_capa = models.ImageField(upload_to = 'uploads/')
    disponivel = models.BooleanField(default=True)

    def __str__(self): #overwrite
        return "{} - {} - {} ({})".format(self.nome, self.autor, self.ano, self.id)

