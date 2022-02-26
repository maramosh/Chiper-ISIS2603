from django.db import models

# Create your models here.
class Tienda(models.Model):
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 50)
    priority = models.IntegerField()

    def __str__(self):
        return str(self.name)+'\n'+str(self.address)+'\n'+str(self.priority)