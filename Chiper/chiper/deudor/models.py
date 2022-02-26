from django.db import models
from tienda.models import Tienda
# Create your models here.
class Deudor(models.Model):
    tienda = models.OneToOneField(Tienda, on_delete=models.CASCADE, primary_key=True, default=None )
    nombre = models.CharField(max_length = 50)
    cedula = models.IntegerField()
    valor = models.FloatField()

    def __str__(self):
        return str(self.nombre)+'\n'+str(self.cedula)+'\n'+str(self.valor)