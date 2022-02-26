from django.db import models
from bodega.models import Bodega

# Create your models here.
class Zona(models.Model):
    bodega = models.ForeignKey(Bodega,on_delete=models.CASCADE)
    tipoProducto = models.CharField(max_length=60)
    especialidad = models.CharField(max_length=60)
    capacidad = models.IntegerField()

    def __str__(self): return '{}'.format(self.capacidad,self.especialidad,self.tipoProducto,self.bodega)
