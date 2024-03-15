import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Pergunta(models.Model):
    texto_perg = models.CharField(max_length = 200)
    data_pub = models.DateTimeField("Data de Publicação")
    def __str__(self): #overwrite
        return "{} ({})".format(self.texto_perg, self.id)
    def publicada_recentemente(self):
        agora = timezone.now()
        return self.data_pub >= agora - datetime.timedelta(hours = 24)

class Alternativa(models.Model):
    texto_alt = models.CharField(max_length = 200)
    qtd_votos = models.IntegerField("Quantidade de votos", default = 0)
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    def __str__(self): #overwrite
        return "{} ({})".format(self.texto_alt, self.id)

