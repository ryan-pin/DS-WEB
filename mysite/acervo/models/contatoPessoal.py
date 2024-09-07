from django.db import models


class ContatoPessoal(models.Model):
    email = models.CharField(max_length=100, unique=True)
    telefone = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self): #overwrite
        return "{} - {} ({})".format(self.email, self.telefone, self.id)