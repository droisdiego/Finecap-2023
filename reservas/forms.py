from django import forms
from .models import Reserva

class CadastroForms(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        # Passe a lista de stands como argumento para o formulário
        stands = kwargs.pop('stands', None)
        super().__init__(*args, **kwargs)

        if stands:
            self.fields['stand_key'].queryset = stands


    
    class Meta:   
        model = Reserva
        fields = '__all__'

    widgets = {
        'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
        'nome_empresa' : forms.TextInput(attrs={'class':'form-control'}),
        'categoria_empresa' : forms.TextInput(attrs={'class':'form-control'}),
        'stand_key' : forms.Select(attrs={'class':'form-control'}),
    }
