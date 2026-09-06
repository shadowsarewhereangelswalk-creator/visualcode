from rest_framework import serializers

from .models import Tarea


class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = ["id", "titulo", "descripcion", "completada", "creada_en"]
        read_only_fields = ["id", "creada_en"]

    def validate_titulo(self, valor):
        titulo = valor.strip()
        if len(titulo) < 3:
            raise serializers.ValidationError("El título debe tener al menos 3 caracteres.")
        return titulo

