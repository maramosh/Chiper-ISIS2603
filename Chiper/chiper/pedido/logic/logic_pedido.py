from ..models import Pedido

def get_all_pedidos():
    pedidos = Pedido.objects.all()
    return pedidos

def update_one_pedido():
    p = Pedido.objects.get(pk=1)
    p.estado = 'preparado'
    p.save()
    return p