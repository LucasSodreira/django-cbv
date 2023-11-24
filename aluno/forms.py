from django.forms import ModelForm
from django import forms
from .models import Cliente, Hospedagem, Quarto, Consumo

class ClienteForm(ModelForm):

    class Meta:
        model = Cliente
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }), 
            'email' : forms.EmailInput(attrs={'class': 'form-control' }),
            'telefone' : forms.TextInput(attrs={'class': 'form-control' }),
            'endereco' : forms.TextInput(attrs={'class': 'form-control' })
        }
        
class HospedagemForm(ModelForm):
    
    class Meta:
        model = Hospedagem
        fields = '__all__'
        widgets = {
            'data_entrada' : forms.DateInput(attrs={'class': 'form-control' }),
            'data_saida' : forms.DateInput(attrs={'class': 'form-control' }),
            'valor' : forms.NumberInput(attrs={'class': 'form-control' }), 
            'cliente' : forms.Select(attrs={'class': 'form-control' }),
            'quarto' : forms.Select(attrs={'class': 'form-control' })
        }
        
class QuartoForm(ModelForm):
    
    class Meta:
        model= Quarto
        fields = '__all__'
        widgets = {
            'apartamento' : forms.NumberInput(attrs={'class': 'form-control' }),
            'valor' : forms.NumberInput(attrs={'class': 'form-control' })
        }
        
class ConsumoForm(ModelForm):
    
    class Meta:
        model = Consumo
        fields = '__all__'
        widget = {
            'nome' : forms.TextInput(attrs={'class': 'form-control' }),
            'data' : forms.DateInput(attrs={'class': 'form-control' }),
            'valor' : forms.NumberInput(attrs={'class': 'form-control' }),
            'hospedagem' : forms.Select(attrs={'class': 'form-control' })
        }