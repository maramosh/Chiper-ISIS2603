from .logic.logic_facturas import get_all_facturas
from django.http import HttpResponse
from django.core import serializers

def get_facturas(request):
    factura = get_all_facturas()
    facturas_list = serializers.serialize('json',factura)
    return HttpResponse(facturas_list, content_type ='application/json')
