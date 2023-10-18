from django.urls import reverse_lazy
from django.views import generic
from finecap.forms import CadastroForms
from finecap.models import Reserva
from django.contrib import messages

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

    def form_valid(self, form):
        messages.success(self.request, 'Reserva Criada Com Sucesso!')
        return super().form_valid(form)
    
class EditarCadastroView(generic.UpdateView):
    model = Reserva
    form_class = CadastroForms
    success_url = reverse_lazy('index')
    template_name = 'core/cadastro.html'

    def form_valid(self, form):
        messages.success(self.request, 'Alterações Concluidas!')
        return super().form_valid(form)

class ExcluirCadastroView(generic.DeleteView):
    model = Reserva
    template_name = 'core/reserva_confirm_delete.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        messages.success(self.request, 'A Reserva Foi Excluída Com Sucesso!')
        return super().form_valid(form)
    