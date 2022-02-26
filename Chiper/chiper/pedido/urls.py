from django.urls import path
from . import views

urlpatterns = [
        path('list/',views.get_pedidos, name = 'pedidoList'),
        path('update/<int:id>/', views.update_pedido, name = 'pedidoUpdate'),
        path('opciones/', views.asr2in)
]