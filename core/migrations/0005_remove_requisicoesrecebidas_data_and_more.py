# Generated by Django 5.1.2 on 2024-10-17 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_requisicoesrecebidas_body_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requisicoesrecebidas',
            name='data',
        ),
        migrations.AlterField(
            model_name='requisicoesrecebidas',
            name='retorno',
            field=models.JSONField(blank=True, null=True, verbose_name='Retorno'),
        ),
    ]