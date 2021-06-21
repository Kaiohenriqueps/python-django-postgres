from django.db import models

# Create your models here.
class Garagem(models.Model):
    veiculo = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)
    ano_fabricacao = models.CharField(max_length=4, default="1990")
    telefone = models.CharField(max_length=20, default="")
    email = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.veiculo
