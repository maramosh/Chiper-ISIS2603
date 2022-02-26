from django.db import models
from tienda.models import Tienda

class Producto(models.Model):
    tienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, default=None)
    nombre = models.CharField(max_length = 60)
    marca = models.CharField(max_length = 60)
    precioChiper = models.FloatField()
    precioTienda = models.FloatField()
    codigo = models.IntegerField()
    catidad = models.IntegerField()
    fechaDeVencimiento = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return '{}'.format(self.nombre,self.marca,self.precioChiper,self.precioTienda,self.codigo,self.catidad,self.fechaDeVencimiento)