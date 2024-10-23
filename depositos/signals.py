from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import RequisicoesRecebidas  # Substitua pelo seu modelo
from depositos.models import Consulta
import json


@receiver(post_save, sender=RequisicoesRecebidas)  # Substitua MyModel pelo seu modelo
def requisicoes_post_save(sender, instance, created, **kwargs):
    if created:
        try:
            dados = json.loads(instance.retorno['data'])
            
            deposito = dados['retorno']['estoques'][0]['estoque']['depositos'][0]['deposito']['nome']
            sku = dados['retorno']['estoques'][0]['estoque']['codigo']
            descricao = dados['retorno']['estoques'][0]['estoque']['nome']
            saldo = dados['retorno']['estoques'][0]['estoque']['estoqueAtual']
            print(f'saldo é {saldo}')
            
            print('completou try')
        except:
            dados = instance.retorno
            
            deposito = dados['retorno']['estoques'][0]['estoque']['depositos'][0]['deposito']['nome']
            sku = dados['retorno']['estoques'][0]['estoque']['codigo']
            descricao = dados['retorno']['estoques'][0]['estoque']['nome']
            saldo = dados['retorno']['estoques'][0]['estoque']['estoqueAtual']
            print('completou except')
            
        try:
            consulta = Consulta.objects.get(
                deposito=deposito,
                descricao=descricao,
            )
            consulta.saldo = saldo
            consulta.save()
            print('criou no try de update')
            
        except:
            Consulta.objects.create(
                deposito=deposito,
                sku=sku,
                descricao=descricao,
                saldo=saldo,
            )
            print('criou no except de criacao')
            
        # consulta, created = Consulta.objects.get_or_create(
        #     deposito=deposito,
        #     sku=sku,
        #     defaults={'descricao': descricao, 'saldo': saldo}
        # )
        
        # if not created:
        #     print(f'Atualizando saldo para: {saldo}')
        #     consulta.saldo = saldo
        #     consulta.save()
        #     print(f'id da consulta é {consulta.id}')
        # else:
        #     print(f'Criando nova consulta com saldo: {saldo}')


        
        print(f'Novo objeto criado: {instance}')
    