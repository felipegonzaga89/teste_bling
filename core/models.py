from django.db import models

# Create your models here.


class RequisicoesRecebidas(models.Model):
    
    body = models.TextField(
        verbose_name='Body',
    )
    
    data = models.JSONField(
        verbose_name='Data',
        blank=True, null=True,
    )