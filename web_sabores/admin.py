from django.contrib import admin
from .models import Consulta

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'email', 'asunto', 'categoria', 'fecha']
    list_filter  = ['categoria']
    search_fields = ['nombre', 'email', 'mensaje']
    readonly_fields = ['categoria', 'fecha']