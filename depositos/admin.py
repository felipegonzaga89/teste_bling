from django.contrib import admin
from depositos.models import Consulta
# Register your models here.

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    
    list_display = [field.name for field in Consulta._meta.fields]
    
    search_fields = [
        'deposito',
        'sku',
        'descricao',
    ]
