from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from reservas.forms import CadastroForms
from reservas.models import Reserva
from stand.models import Stand
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class IndexView(generic.TemplateView):
    template_name = 'core/index.html'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_active:
            return redirect('erro') 
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_reserva"] = Reserva.objects.count()
        context["total_stands"] = Stand.objects.count()
        return context

class ReservaListView(generic.ListView):
    model = Reserva
    template_name = 'core/reserva_list.html'
    context_object_name = 'reservas_list'

    paginate_by = 10  

    # def get_queryset(self):
    #     return Reserva.objects.all().order_by('pk')
    
class DetalheReservaView(generic.DetailView):
    model = Reserva
    template_name = 'core/reserva_detail.html'

class AdminRequiredMixin:
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect('erro') 
        return super().dispatch(request, *args, **kwargs)

class CadastroView(AdminRequiredMixin, generic.CreateView):
    model = Reserva
    form_class = CadastroForms
    success_url = reverse_lazy('lista_reserva')
    template_name = 'core/cadastro.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(stands=Stand.objects.all())
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Reserva Criada Com Sucesso!')
        return super().form_valid(form)
    
class EditarCadastroView(AdminRequiredMixin, generic.UpdateView):
    model = Reserva
    form_class = CadastroForms
    success_url = reverse_lazy('lista_reserva')
    template_name = 'core/cadastro.html'

    def form_valid(self, form):
        messages.success(self.request, 'Alterações Concluidas!')
        return super().form_valid(form)

class ExcluirCadastroView(AdminRequiredMixin,generic.DeleteView):
    model = Reserva
    template_name = 'core/reserva_confirm_delete.html'
    success_url = reverse_lazy('lista_reserva')

    def form_valid(self, form):
        messages.success(self.request, 'A Reserva Foi Excluída Com Sucesso!')
        return super().form_valid(form)
    
class ErroView(generic.TemplateView):
    template_name = 'core/erro.html'