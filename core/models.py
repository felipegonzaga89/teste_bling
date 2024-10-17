from django.db import models

# Create your models here.


class RequisicoesRecebidas(models.Model):
    
    retorno = models.JSONField(
        verbose_name='Retorno',
        blank=True, null=True,
    )
    
   