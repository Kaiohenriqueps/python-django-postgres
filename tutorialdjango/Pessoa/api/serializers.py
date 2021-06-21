from rest_framework import serializers
from Pessoa import models


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pessoa
        fields = "__all__"
