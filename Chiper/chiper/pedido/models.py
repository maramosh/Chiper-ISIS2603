from django.db import models
from camion.models import Camion
from facturabodega.models import FacturaBodega

# Create your models here.
class Pedido(models.Model):
    camion = models.ForeignKey(Camion, on_delete=models.CASCADE)
    Factura = models.ManyToManyField(FacturaBodega)
    tipoPago = models.CharField(max_length=60)
    estado = models.CharField(max_length=60)
    valor = models.FloatField()
    cantidadProducto = models.IntegerField()

    def __str__(self): return '{}'.format(self.estado,self.cantidadProducto,self.tipoPago,self.valor,self.camion,self.Factura)
