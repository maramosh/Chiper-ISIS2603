
from django import forms
from .models import Tienda

class TiendaForm(forms.ModelForm):
    class Meta:
        model = Tienda
        fields = [
            'name',
        ]
        labels = {
            'name': 'Name',
        }