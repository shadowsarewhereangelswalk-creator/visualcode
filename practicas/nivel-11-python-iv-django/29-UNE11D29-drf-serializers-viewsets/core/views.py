from django.db.models import Count, Sum
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Cliente, Proyecto
from .serializers import ClienteSerializer, ProyectoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.prefetch_related("proyectos").order_by("nombre")
    serializer_class = ClienteSerializer


class ProyectoViewSet(viewsets.ModelViewSet):
    serializer_class = ProyectoSerializer

    def get_queryset(self):
        consulta = Proyecto.objects.select_related("cliente").order_by("-id")
        estado = self.request.query_params.get("estado")
        return consulta.filter(estado=estado) if estado else consulta

    @action(detail=False)
    def resumen(self, request):
        datos = self.get_queryset().aggregate(proyectos=Count("id"), presupuesto=Sum("presupuesto"))
        return Response(datos)

