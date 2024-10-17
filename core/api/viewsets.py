from rest_framework import viewsets, status
from core.models import *
from .serializers import RequisicoesRecebidasSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response


class RequisicoesRecebidasViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    
    queryset = RequisicoesRecebidas.objects.all()
    serializer_class = RequisicoesRecebidasSerializer
    
    # def get_permissions(self):
    #     if self.action == 'list':  # Para o método GET (listar)
    #      return [IsAuthenticated()]  # Exige autenticação
    #     return super().get_permissions()  # Permite POST sem autenticação
    
    def create(self, request, *args, **kwargs):
        # Cria uma nova instância do serializer com os dados da requisição
        # serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True)  # Valida os dados
        
        RequisicoesRecebidas.objects.create(retorno=request.data)
        

        # Salva a nova instância no banco de dados
        # self.perform_create(serializer)

        # Retorna a resposta com os dados criados
        return Response(status=status.HTTP_201_CREATED)    




   