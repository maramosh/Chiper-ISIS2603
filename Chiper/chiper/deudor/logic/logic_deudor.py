from ..models import Deudor

def get_all_deudores():
    deudores = Deudor.objects.all()
    return deudores