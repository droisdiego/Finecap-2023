from django.contrib import admin
from .models import * 

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('nome_empresa','quitado')

@admin.register(Stand)
class StandAdmin(admin.ModelAdmin):
    list_display = ('localizacao','valor',)
