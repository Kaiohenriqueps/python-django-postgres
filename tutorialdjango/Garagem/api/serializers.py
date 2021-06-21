from rest_framework import serializers
from Garagem import models


class GaragemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Garagem
        fields = "__all__"
