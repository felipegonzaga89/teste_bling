from rest_framework import viewsets
from core.models import *
from .serializers import RequisicoesRecebidasSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RequisicoesRecebidasViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    
    queryset = RequisicoesRecebidas.objects.all()
    serializer_class = RequisicoesRecebidasSerializer

    def get_permissions(self):
        if self.action == 'list':  # Para o método GET (listar)
            return [IsAuthenticated()]  # Exige autenticação
        return super().get_permissions()  # Permite POST sem autenticação