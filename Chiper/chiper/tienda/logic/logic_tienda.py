from ..models import Tienda
from  productos.models import Producto


def get_all_tiendas():
    tiendas = Tienda.objects.all()
    return tiendas

def get_inventario():
    pTienda = Tienda.objects.get(pk=1)
    inventario = Producto.objects.filter(tienda__name__icontains = pTienda.name)
    return inventario

def get_prodcutos():
    productos = Producto.objects.all()
    return productos

def comp_listas():
    lista1 = get_inventario()
    lista2 =get_prodcutos()
    comparacion = []

    for item in lista1:
        if item not in lista2:
            comparacion.append(item)

    if len(comparacion) > 0:
        print('A la tienda le faltan los productos : ')
        for item in comparacion: print('%s' % item)
    else:
        print('A la tienda no le faltan prodcutos')

    return comparacion




