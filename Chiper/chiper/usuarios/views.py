from django.shortcuts import render
from .logic.logic_usuarios import get_all_encargadosOperacion
from .logic.logic_usuarios import get_all_cto
from .logic.logic_usuarios import get_all_usuarios
from .logic.logic_usuarios import get_all_encargadosLogistica
from .logic.logic_usuarios import get_all_ceo
from .logic.logic_usuarios import get_all_conductores
from .logic.logic_usuarios import get_all_tenderos
from .logic.logic_usuarios import get_all_dueños
from .logic.logic_usuarios import get_all_cajeros
from .logic.logic_usuarios import get_all_administradores
from django.http import HttpResponse
from django.core import serializers
# Create your views here.
def get_usuarios():
    usuarios = get_all_usuarios()
    usuarios_list = serializers.serialize('json',usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')

def get_cto():
    usuarios = get_all_cto()
    usuarios_list = serializers.serialize('json',usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')

def get_ceo():
    usuarios = get_all_ceo()
    usuarios_list = serializers.serialize('json', usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')

def get_tenderos():
    usuarios = get_all_tenderos()
    usuarios_list = serializers.serialize('json', usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')


def tenderos_list(request):
    measurements = get_all_tenderos()
    context = {
        'tenderos_list': measurements
    }
    return render(request, 'tenderosList.html', context)


def get_dueños():
    usuarios = get_all_dueños()
    usuarios_list = serializers.serialize('json', usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')

def get_cajeros():
    usuarios = get_all_cajeros()
    usuarios_list = serializers.serialize('json', usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')

def get_administradores():
    usuarios = get_all_administradores()
    usuarios_list = serializers.serialize('json', usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')

def get_usuarios():
    usuarios = get_all_encargadosLogistica()
    usuarios_list = serializers.serialize('json', usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')

def get_conductores():
    usuarios = get_all_conductores()
    usuarios_list = serializers.serialize('json', usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')

def get_encargadosOperacion():
    usuarios = get_all_encargadosOperacion()
    usuarios_list = serializers.serialize('json',usuarios)
    return HttpResponse(usuarios_list, content_type ='application/json')

