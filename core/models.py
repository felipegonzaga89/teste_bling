from django.db import models

# Create your models here.


class RequisicoesRecebidas(models.Model):
    
    body = models.TextField(
        verbose_name='Body',
    )