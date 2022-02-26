from .logic.logic_venta import get_all_ventas
from django.http import HttpResponse
from django.core import serializers

def get_ventas(request):
    venta = get_all_ventas()
    ventas_list = serializers.serialize('json',venta)
    return HttpResponse(ventas_list, content_type ='application/json')
