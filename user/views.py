from django.shortcuts import render
from django.views import generic

# Create your views here.

class AdminHomeView(generic.TemplateView):
    template_name = 'core3/home.html'

class AdminLoginview(generic.TemplateView):
    template_name = 'account/login.html'