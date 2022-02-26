from ..models import Usuario
from ..models import EncargadoOperacion
from ..models import EncargadoLogistico
from ..models import CTO
from ..models import CEO
from ..models import Dueño
from ..models import Cajero
from ..models import Conductor
from ..models import Tendero
from ..models import Administrador

def get_all_usuarios():
    usuarios = Usuario.objects.all()
    return usuarios

def get_all_encargadosOperacion():
    encargadosOperacion = EncargadoOperacion.objects.all()
    return encargadosOperacion

def get_all_encargadosLogistica():
    encargadosLogistica = EncargadoLogistico.objects.all()
    return encargadosLogistica

def get_all_cto():
    cto = CTO.objects.all()
    return cto

def get_all_ceo():
    ceo = CEO.objects.all()
    return ceo

def get_all_conductores():
    conductores = Conductor.objects.all()
    return conductores

def get_all_tenderos():
    tenderos = Tendero.objects.all()
    return tenderos

def get_all_dueños():
    dueños = Dueño.objects.all()
    return dueños

def get_all_cajeros():
    cajeros = Cajero.objects.all()
    return cajeros

def get_all_administradores():
    administradores = Administrador.objects.all()
    return administradores