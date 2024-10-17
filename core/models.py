from django.db import models

# Create your models here.


class RequisicoesRecebidas(models.Model):
    
    retorno = models.TextField(
        verbose_name='retorno',
        blank=True, null=True,
    )
    
    data = models.JSONField(
        verbose_name='Data',
        blank=True, null=True,
    )