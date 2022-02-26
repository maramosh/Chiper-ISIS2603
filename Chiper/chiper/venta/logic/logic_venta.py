from ..models import Venta

def get_all_ventas():
    ventas = Venta.objects.all()
    return ventas