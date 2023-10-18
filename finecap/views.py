from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import generic
from finecap.forms import CadastroForms
from finecap.models import Reserva

class Indexview(generic.ListView):
    model = Reserva
    template_name = 'core/index.html'
    context_object_name = 'reservas_list'
    
class DetalheReservaView(generic.DetailView):
    model = Reserva
    template_name = 'core/reserva.html'

class CadastroView(generic.CreateView):
    model = Reserva
    form_class = CadastroForms
    success_url = reverse_lazy('index')
    template_name = 'core/cadastro.html'
    
class EditarCadastroView(generic.UpdateView):
    model = Reserva
    form_class = CadastroForms
    success_url = reverse_lazy('index')
    template_name = 'core/cadastro.html'

class ExcluirCadastroView(generic.DeleteView):
    model = Reserva
    template_name = 'core/reserva_confirm_delete.html'
    success_url = reverse_lazy('index')
    