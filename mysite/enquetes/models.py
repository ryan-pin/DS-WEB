from django.db import models

# Create your models here.
class Pergunta(models.Model):
    texto_perg = models.CharField(max_length = 200)
    data_pub = models.DateTimeField("Data de Publicação")

class Alternativa(models.Model):
    texto_alt = models.CharField(max_length = 200)
    qtd_votos = models.IntegerField(default = 0)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
