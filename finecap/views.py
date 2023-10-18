from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
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
    context_object_name = 'reserva'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Reserva, id=id)

def CadastroView(request):
    if request.method == 'POST':
        form = CadastroForms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CadastroForms()
    else:
        form = CadastroForms()
    return render(request, 'core/cadastro.html', {'form': form})

def EditarCadastroView(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = CadastroForms(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CadastroForms(instance=reserva)

    return render(request, 'core/cadastro.html', {'form': form})


def ExcluirCadastroView(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('index')
