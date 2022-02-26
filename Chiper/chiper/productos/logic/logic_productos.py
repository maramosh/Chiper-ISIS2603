from ..models import Producto
from django.core.exceptions import ObjectDoesNotExist

def get_all_products():
    productos = Producto.objects.all()
    return productos
def get_products_referencia(referencia):
    producto = Producto.objects.all().filter(referencia = referencia).only()
    return producto
def get_product_id(id):
    producto = Producto.objects.get(pk = id)
    return producto

def create_producto(form):
    producto = form.save()
    producto.save()
    return ()

def getId(producto):
    try:
        Producto.objects.get(nombre=producto)
    except ObjectDoesNotExist:
        return 0
    return Producto.objects.get(nombre=producto).id