
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .logic.logic_productos import get_all_products, get_products_referencia,create_producto
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .form import ProductoForm


def get_productos(request):
    productos = get_all_products()
    context = {
        'productos': productos
    }
    return render(request, 'Producto/productoDetail.html', context)


def get_cantidad_referencia(request, referencia):
    productos = get_products_referencia(referencia)
    context = {
        'productos': productos
    }
    return render(request, 'Producto/productoDetail.html', context)

# Create your views here.


def producto_create(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            create_producto(form)
            messages.add_message(request, messages.SUCCESS, 'Producto satisfactoriamente creado')
            return HttpResponseRedirect(reverse('productoCreate'))
        else:
            print(form.errors)
    else:
        form = ProductoForm()

    context = {
        'form': form,
    }
    return render(request, 'Producto/productoCreate.html', context)

def buscar(request):
    nombre = request.GET.get('nombre','')
    if nombre == '' or nombre == '/':
        return render(request, 'Producto/buscarProducto.html')
    return HttpResponseRedirect('/productos/buscar/'+nombre)