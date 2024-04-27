from django import forms
from .models import Tarjeta

class TarjetaCreateForm(forms.ModelForm):
    class Meta:
        model = Tarjeta
        fields = ['lider', 'sponsor', 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin','estado']
        labels = {
            'lider': 'Seleccionar el lider',
            'sponsor': 'Seleccionar el sponsor',
            'titulo': 'Seleccionar el titulo',
            'descripcion': 'Seleccionar el descripcion',
            'fecha_inicio': 'Seleccionar el fecha_inicio',
            'fecha_fin': 'Seleccionar el fecha_fin',
            'estado': 'Seleccionar el estado',
        }