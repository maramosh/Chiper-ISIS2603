from django.urls import path
from . import views

urlpatterns = [
        path('list/',views.get_tiendas, name = 'tiendaList'),
        path('faltan/<int:id>/',views.get_prodcutosFaltan, name = 'pFaltan'),
        path('lista/',views.get_prodcutos, name = 'pList')
]