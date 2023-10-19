from django.urls import reverse_lazy
from django.views import generic
from stand.forms import StandForms
from stand.models import Stand
from django.contrib import messages

class StandListView(generic.ListView):
    model = Stand
    template_name = 'core2/stand_list.html'
    context_object_name = 'lista_stand'
    paginate_by = 10 
    
class DetalheStandView(generic.DetailView):
    model = Stand
    template_name = 'core2/stand_detail.html'

class CreateStandView(generic.CreateView):
    model = Stand
    form_class = StandForms
    success_url = reverse_lazy('lista_stand')
    template_name = 'core2/stand_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Stand Criado Com Sucesso!')
        return super().form_valid(form)
    
class EditarStandView(generic.UpdateView):
    model = Stand
    form_class = StandForms
    success_url = reverse_lazy('lista_stand')
    template_name = 'core2/stand_form.html'

    def form_valid(self, form):
        messages.success(self.request, 'Alterações Concluidas!')
        return super().form_valid(form)

class ExcluirStandView(generic.DeleteView):
    model = Stand
    template_name = 'core2/stand_confirm_delete.html'
    success_url = reverse_lazy('lista_stand')

    def form_valid(self, form):
        messages.success(self.request, 'O Stand Foi Excluída Com Sucesso!')
        return super().form_valid(form)
    