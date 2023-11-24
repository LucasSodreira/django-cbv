from django.contrib import admin
from .models import Cliente, Hospedagem, Consumo, Quarto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nome','email','telefone','endereco')

@admin.register(Hospedagem)
class HospedagemAdmin(admin.ModelAdmin):
    list_display=('data_entrada','data_saida','valor','cliente','quarto')
    
@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display=('apartamento','valor')
    
@admin.register(Consumo)
class Consumo(admin.ModelAdmin):
    list_display=('nome','data','valor','hospedagem')

