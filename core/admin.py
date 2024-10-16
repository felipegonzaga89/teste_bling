from django.contrib import admin
from core.models import RequisicoesRecebidas
# Register your models here.

@admin.register(RequisicoesRecebidas)
class RequisicoesRecebidasAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'retorno']
    
    readonly_fields = ['data_criacao']