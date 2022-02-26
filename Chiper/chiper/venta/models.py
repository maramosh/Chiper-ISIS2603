from django.db import models
from productos.models import Producto

# Create your models here.
class Venta(models.Model):
    productos = models.ForeignKey(Producto, on_delete=models.CASCADE, default=None)
    cantidad = models.IntegerField()
    valor = models.FloatField()
    fechaVenta = models.DateField(auto_now=False, auto_now_add=False)
    tipoPago = models.CharField(max_length = 60)

    def __str__(self):
        return str(self.cantidad)+'\n'+str(self.valor)+'\n'+str(self.fechaVenta) +'\n'+str(self.tipoPago)