from django import forms
from .models import Stand

class StandForms(forms.ModelForm):
    
    valor = forms.CharField(widget=forms.TextInput(attrs={"class": "money","placeholder": "Valor do stand",}))
    def clean_valor(self):
        valor = self.cleaned_data["valor"]
        return valor.replace(",", ".")

    class Meta:   
        model = Stand
        fields = '__all__'

    widgets = {
        'localizacao': forms.TextInput(attrs={'class': 'form-control'}),
    }
