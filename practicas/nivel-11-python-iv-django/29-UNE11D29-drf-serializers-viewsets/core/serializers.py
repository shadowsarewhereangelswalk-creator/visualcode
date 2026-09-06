from rest_framework import serializers

from .models import Cliente, Proyecto


class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = ["id", "cliente", "nombre", "estado", "presupuesto"]


class ClienteSerializer(serializers.ModelSerializer):
    proyectos = ProyectoSerializer(many=True, read_only=True)
    total_proyectos = serializers.IntegerField(source="proyectos.count", read_only=True)

    class Meta:
        model = Cliente
        fields = ["id", "nombre", "correo", "total_proyectos", "proyectos"]

