from django.db import models

# Create your models here.
class Camion(models.Model):
    placa = models.CharField(max_length=60)
    capacidad = models.IntegerField()

    def __str__(self): return '{}'.format(self.placa,self.capacidad)



