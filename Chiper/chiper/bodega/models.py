from django.db import models

# Create your models here.
class Bodega(models.Model):
    direccion = models.CharField(max_length=60)
    capacidadRestante = models.IntegerField()
    numeroDeZonas = models.IntegerField()

    def __str__(self): return '{}'.format(self.direccion,self.capacidadRestante,self.numeroDeZonas)
