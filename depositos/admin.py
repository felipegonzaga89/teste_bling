from django.contrib import admin
from depositos.models import Consulta
from django_object_actions import DjangoObjectActions, action
from django.http import HttpResponseRedirect
from django.shortcuts import render
import csv
import io
from django.urls import reverse



# Register your models here.

@admin.register(Consulta)
class ConsultaAdmin(DjangoObjectActions, admin.ModelAdmin):
    
    list_display = [field.name for field in Consulta._meta.fields]
    
    search_fields = [
        'deposito',
        'sku',
        'descricao',
    ]

    changelist_actions = ('importar_dados', )
    
    def importar_dados(self, request, queryset):
        if request.method == 'POST' and request.FILES['csv_file']:
            csv_file = request.FILES['csv_file']
            if not csv_file.name.endswith('.csv'):
                self.message_user(request, "Apenas arquivos CSV são suportados.")
                return HttpResponseRedirect(request.path_info)

            # Lê o arquivo CSV
            decoded_file = csv_file.read().decode('utf-8')
            io_string = io.StringIO(decoded_file)
            reader = csv.reader(io_string, delimiter=';')
            next(reader)  # Pula o cabeçalho, se houver

            deposito = request.POST['deposito']
            for row in reader:
                sku = row[0]
                descricao = row[1]
                saldo = float(row[2]) 
                
                consulta, created = Consulta.objects.get_or_create(
                    deposito=deposito,
                    sku=sku,
                    descricao=descricao,
                    defaults={'saldo': saldo}
                )

                if not created:  # Se a consulta já existia, atualiza o saldo
                    consulta.saldo = saldo
                    consulta.save()
            self.message_user(request, "Dados importados com sucesso.")
            return HttpResponseRedirect(reverse('admin:depositos_consulta_changelist'))
        
        
        
        depositos = Consulta.objects.values('deposito').distinct()  # Filtra depósitos únicos

    

        return render(request, 'admin/depositos/consulta/import_csv.html', {'depositos': depositos})