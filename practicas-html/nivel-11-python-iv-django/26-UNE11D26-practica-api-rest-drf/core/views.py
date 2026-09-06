from rest_framework import viewsets

from .models import Tarea
from .serializers import TareaSerializer


class TareaViewSet(viewsets.ModelViewSet):
    serializer_class = TareaSerializer

    def get_queryset(self):
        consulta = Tarea.objects.order_by("-creada_en")
        completada = self.request.query_params.get("completada")
        if completada in {"true", "false"}:
            consulta = consulta.filter(completada=completada == "true")
        return consulta

