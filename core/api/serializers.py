from rest_framework import serializers
from core.models import *

class RequisicoesRecebidasSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequisicoesRecebidas
        fields = ['id', 'retorno']  # Inclua o campo `id` se você quiser retorná-lo também
