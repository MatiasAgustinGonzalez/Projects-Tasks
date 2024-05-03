from django import forms
from .models import Tarjeta
from django.contrib.auth.models import User

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

class TarjetaSearchForm(forms.Form):
    titulo = forms.CharField(max_length=20, required=True, label="Ingresar nombre Proyecto")
    estado = forms.ChoiceField(choices=Tarjeta.Tipo.choices, required=False, label="Seleccionar estado")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']