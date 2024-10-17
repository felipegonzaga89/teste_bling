from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import RequisicoesRecebidas  # Substitua pelo seu modelo
from depositos.models import Consulta
import json


@receiver(post_save, sender=RequisicoesRecebidas)  # Substitua MyModel pelo seu modelo
def requisicoes_post_save(sender, instance, created, **kwargs):
    if created:
        dados = json.loads(instance.retorno['data'])
        
        deposito = dados['retorno']['estoques'][0]['estoque']['depositos'][0]['deposito']['nome']
        sku = dados['retorno']['estoques'][0]['estoque']['codigo']
        descricao = dados['retorno']['estoques'][0]['estoque']['nome']
        saldo = dados['retorno']['estoques'][0]['estoque']['estoqueAtual']
        
        Consulta.objects.create(
            deposito=deposito,
            sku=sku,
            descricao=descricao,
            saldo=saldo,
        )
        
        print(f'Novo objeto criado: {instance}')
    