from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from finecap.models import Reserva

def index(request):
     reserva = Reserva.objects.all()
     context = {'reserva':reserva}
     return render (request, 'core/index.html',context)

def detalhe_reserva(request, id):
     reserva = get_object_or_404(Reserva, id=id)
     context = {'reserva':reserva}
     return render(request, 'core/reserva.html', context)

def quitadoresult(request):
     HttpResponse("oi")

# def cadastrar(request):


