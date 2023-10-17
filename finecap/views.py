from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import generic
from finecap.models import Reserva

# def index(request):
#      reserva = Reserva.objects.all()
#      context = {'reserva':reserva}
#      return render (request, 'core/index.html',context)
class Indexview(generic.TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = {'reserva': Reserva.objects.all()}
        return context

class DetalheReservaView(generic.DetailView):
    model = Reserva
    template_name = 'core/reserva.html'
    context_object_name = 'reserva'

    def get_object(self, queryset=None):
        id = self.kwargs.get('id')
        return get_object_or_404(Reserva, id=id)
