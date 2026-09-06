from rest_framework import serializers

from .models import Servicio, Solicitud


class ServicioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servicio
        fields = ["id", "nombre", "slug", "descripcion", "precio_desde"]


class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = ["id", "servicio", "nombre", "correo", "mensaje", "estado", "creada_en"]
        read_only_fields = ["id", "creada_en"]

