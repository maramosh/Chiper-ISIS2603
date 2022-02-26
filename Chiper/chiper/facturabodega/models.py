from django.db import models

# Create your models here.
class FacturaBodega(models.Model):
    plazoDeGarantia = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self): return '{}'.format(self.plazoDeGarantia)

