from django.apps import AppConfig


class DepositosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'depositos'

    def ready(self):
        import depositos.signals  # Substitua pelo caminho correto