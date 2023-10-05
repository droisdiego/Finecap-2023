from django import forms
from .models import Reserva

class CadastroForms(forms.ModelForm):
    
    class Meta:   
        model = Reserva
        fields = '__all__'

    widgets = {
        'nome': forms.TextInput(attrs={'class':'form-control'})
    }