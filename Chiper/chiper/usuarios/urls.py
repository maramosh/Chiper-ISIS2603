from django.urls import path
from . import views

urlpatterns = [
        path('list/',views.tenderos_list, name = 'tenderosList'),

]