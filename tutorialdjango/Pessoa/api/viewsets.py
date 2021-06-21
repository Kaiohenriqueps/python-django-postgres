from rest_framework import viewsets
from Pessoa.api import serializers
from Pessoa import models


class PessoaViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.PessoaSerializer
    queryset = models.Pessoa.objects.all()
