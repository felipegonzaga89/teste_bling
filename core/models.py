from django.db import models

# Create your models here.


class RequisicoesRecebidas(models.Model):
    
    retorno = models.JSONField(
        verbose_name='Retorno',
        blank=True, null=True,
    )
    
    data_criacao = models.DateTimeField(
        verbose_name='Data de Criação',
        auto_now_add=True,
        blank=True,
        null=True,
    )

   