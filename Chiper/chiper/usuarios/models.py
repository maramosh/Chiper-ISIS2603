from django.db import models


# Create your models here.
class Usuario(models.Model):
    nombre = models.CharField(max_length=60)
    contrasena = models.CharField(max_length=60)
    identificacion = models.IntegerField()
    numeroCelular = models.IntegerField()
    email = models.CharField(max_length=60)


def __str__(self):
    return '{}'.format(self.nombre, self.contrasena, self.identificacion, self.numeroCelular, self.email)


class EncargadoOperacion(Usuario):
    cargo = models.CharField(max_length=60)
    nivel = models.CharField(max_length=60)


def __str__(self):
    return '{}'.format(self.cargo, self.nivel)

class EncargadoLogistico(Usuario):
    experiencia = models.CharField(max_length=60)



def __str__(self):
    return '{}'.format(self.cargo, self.nivel)

class Administrador(Usuario):

    def __str__(self):
        return '{}'.format(self.area)


class CEO(Administrador):



    def __str__(self):
        return '{}'.format()


class CTO(Administrador):


    def __str__(self):
        return '{}'.format()




class Tendero(Usuario):

    RUT = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.RUT)

class Dueño(Tendero):
 
    def __str__(self):
        return '{}'.format()

class Cajero(Tendero):


    def __str__(self):
        return '{}'.format(self)

class Conductor(Usuario):

    licencia = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.licencia)
