from django.db import models

# Create your models here.

class Stand(models.Model):
    localizacao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return self.localizacao