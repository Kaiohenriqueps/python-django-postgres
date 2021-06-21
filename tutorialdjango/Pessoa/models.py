from django.db import models

# from django.contrib.auth.models import User

# Create your models here.
class Pessoa(models.Model):
    # id = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    telefone = models.CharField(max_length=20)
    email = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
