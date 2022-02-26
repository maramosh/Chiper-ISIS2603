from .logic.logic_pedido import get_all_pedidos
from .logic.logic_pedido import update_one_pedido
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render,redirect
from .forms import PedidoForm
from .models import Pedido
from django.shortcuts import render

def get_pedidos(request):
    pedido = get_all_pedidos()
    pedido_list = serializers.serialize('json',pedido)
    return HttpResponse(pedido_list, content_type ='application/json')

def measurement_list(request):
    measurements = get_all_pedidos()()
    context = {
        'pedidos_list': measurements
    }
    return render(request, 'asr2.html', context)

def PedidoCreate(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_variable(data_json) == True:
            pedido = Pedido()
            pedido.camion = data_json['camion']
            pedido.cantidadProducto = data_json['cantidadProducto']
            pedido.estado = data_json['estado']
            pedido.Factura = data_json['factura']
            pedido.tipoPago = data_json['tipoPago']
            pedido.valor = data_json['valor']
            pedido.save()
            return HttpResponse("Pedido creado satisfactoriamente.")
        else:
            return HttpResponse("El pedido no ha sido creado satisfactoriamente.")

def update_pedido(request,id):
    pedido= Pedido.objects.get(pk=id)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
          form.save()
          return redirect('pedidoList')
    return render(request, 'pedido_form.html',{'form':form, 'pedido': pedido})

def asr2in(request):
    measurements = get_all_pedidos()
    context = {
        'pedidos_list': measurements
    }
    return render(request, 'asr2.html', context)