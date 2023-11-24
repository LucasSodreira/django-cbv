from django.views.generic import TemplateView,UpdateView,CreateView,DeleteView,ListView
from django.shortcuts import render,get_object_or_404,redirect
from .models import Cliente, Hospedagem, Consumo, Quarto
from .forms import HospedagemForm
from django.urls import reverse_lazy


class Hospedagem_Criar(CreateView):
    template_name = 'form/form_hospedagem.html'
    form_class = HospedagemForm
    success_url = reverse_lazy('hospedagem_listar')
    
class Hospedagem_Editar(UpdateView):
    model = Hospedagem
    form_class = HospedagemForm
    template_name = 'form/form_hospedagem.html'
    pk_url_kwarg = 'id'
    
    def get_success_url(self):
        return reverse_lazy('hospedagem_listar')
    
class Hospedagem_Remover(DeleteView):
    model = Hospedagem
    success_url = reverse_lazy('hospedagem_listar')
    pk_url_kwarg = 'id'
    
    def get(self,*args,**kwargs):
        return self.delete(*args,**kwargs)
    
class Hospedagem_Listar(ListView):
    model = Hospedagem
    template_name = 'cliente/hospedagem.html'
    context_object_name = 'hospedagems'

class Index(TemplateView):
    template_name = 'cliente/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_clientes'] = Cliente.objects.count()
        context['total_hospedagem'] = Hospedagem.objects.count()
        context['total_quarto'] = Quarto.objects.count()
        return context



