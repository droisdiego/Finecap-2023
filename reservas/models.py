from django.db import models
from stand.models import Stand

class Reserva(models.Model):
    cnpj = models.CharField(max_length=50)
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=100)
    quitado = models.BooleanField()
    stand_key = models.ForeignKey(Stand, on_delete=models.CASCADE)
    
    objects = models.Manager()

    def __str__(self):
        return self.nome_empresa
    
# class Stand(models.Model):
#     localizacao = models.CharField(max_length=150)
#     valor = models.DecimalField(max_digits=10, decimal_places=2)
#     def __str__(self):
#         return self.localizacao