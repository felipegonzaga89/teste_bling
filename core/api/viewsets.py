from rest_framework import viewsets
from core.models import *
from .serializers import RequisicoesRecebidasSerializer

class RequisicoesRecebidasViewSet(viewsets.ModelViewSet):
    queryset = RequisicoesRecebidas.objects.all()
    serializer_class = RequisicoesRecebidasSerializer
