from django.db import models

# Create your models here.
class Garagem(models.Model):
    veiculo = models.CharField(max_length=255)
    cor = models.CharField(max_length=255)

    def __str__(self):
        return self.veiculo
