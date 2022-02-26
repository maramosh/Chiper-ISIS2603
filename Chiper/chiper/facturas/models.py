from django.db import models


# Create your models here.
class Factura(models.Model):
    valor = models.FloatField()
    fecha = models.DateField(auto_now=False, auto_now_add=False)
    codigo = models.IntegerField()
    direccion = models.CharField(max_length = 50)
    nombreEmisor = models.CharField(max_length = 60)

    def __str__(self):
        return str(self.valor)+'\n'+str(self.fecha)+'\n'+str(self.codigo) +'\n'+str(self.direccion) +'\n'+str(self.nombreEmisor)