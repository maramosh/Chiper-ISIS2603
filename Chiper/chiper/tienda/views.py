from .logic.logic_tienda import get_all_tiendas
from .logic.logic_tienda import comp_listas
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render,redirect
from .models import Tienda
from .forms import TiendaForm

def get_tiendas(request):
    tienda = get_all_tiendas()
    tienda_list = serializers.serialize('json',tienda)
    return HttpResponse(tienda_list, content_type ='application/json')

def get_prodcutosFaltan(request,id):
    tienda = Tienda.objects.get(pk=id)
    form = TiendaForm(request.GET or None, instance=tienda)
    if form.is_valid():
          form.save()
          return redirect('pList')
    return render(request, 'tienda_form.html',{'form':form, 'Tienda': tienda})

def get_prodcutos(request):
    productos = comp_listas()
    tienda_list = serializers.serialize('json', productos)
    return HttpResponse(tienda_list, content_type='application/json')