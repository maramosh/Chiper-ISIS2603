from .logic.logic_deudor import get_all_deudores
from django.http import HttpResponse
from django.core import serializers

def get_deudores(request):
    deudor = get_all_deudores()
    deudor_list = serializers.serialize('json',deudor)
    return HttpResponse(deudor_list, content_type ='application/json')
