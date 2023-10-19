from django import forms
from .models import Stand

class StandForms(forms.ModelForm):
    
    valor = forms.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:   
        model = Stand
        fields = '__all__'

    widgets = {
        'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
    }
