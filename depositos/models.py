from django.db import models

# Create your models here.
class Consulta(models.Model):
    
    deposito = models.CharField(
        verbose_name='Depósito',
        max_length=150,
        blank=True, null=True,
    )
    
    sku = models.CharField(
        verbose_name='SKU',
        max_length=200,
        blank=True, null=True,
    )
    
    descricao = models.CharField(
        verbose_name='Descrição',
        max_length=200,
        blank=True, null=True,
    )
    
    saldo = models.CharField(
        verbose_name='Saldo',
        max_length=200,
        blank=True,
    )
    
    