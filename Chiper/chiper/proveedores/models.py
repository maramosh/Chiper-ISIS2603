from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=60)
    cantProductos = models.IntegerField()

    def __str__(self): return '{}'.format(self.nombre,self.cantProductos)

