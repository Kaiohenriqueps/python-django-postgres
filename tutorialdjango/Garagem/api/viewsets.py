from rest_framework import viewsets
from Garagem.api import serializers
from Garagem import models


class GaragemViewsets(viewsets.ModelViewSet):
    serializer_class = serializers.GaragemSerializer
    queryset = models.Garagem.objects.all()
