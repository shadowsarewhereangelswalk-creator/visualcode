from django import forms

from .models import Cliente, Proyecto


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nombre", "correo"]


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ["cliente", "nombre", "estado", "etiquetas"]

