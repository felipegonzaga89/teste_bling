# Generated by Django 5.1.2 on 2024-10-17 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposito', models.CharField(blank=True, max_length=150, null=True, verbose_name='Depósito')),
                ('sku', models.CharField(blank=True, max_length=200, null=True, verbose_name='SKU')),
                ('descricao', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição')),
                ('saldo', models.CharField(blank=True, max_length=200, verbose_name='Saldo')),
            ],
        ),
    ]
