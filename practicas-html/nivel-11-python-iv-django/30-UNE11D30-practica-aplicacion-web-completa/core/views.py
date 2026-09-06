from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from rest_framework import viewsets

from .forms import SolicitudForm
from .models import Servicio, Solicitud
from .serializers import ServicioSerializer, SolicitudSerializer


def inicio(request):
    formulario = SolicitudForm(request.POST or None)
    if request.method == "POST" and formulario.is_valid():
        formulario.save()
        messages.success(request, "Solicitud enviada correctamente.")
        return redirect("inicio")
    servicios = Servicio.objects.filter(activo=True).order_by("nombre")
    return render(request, "core/inicio.html", {"servicios": servicios, "formulario": formulario})


def panel(request):
    estado = request.GET.get("estado", "")
    solicitudes = Solicitud.objects.select_related("servicio").order_by("-creada_en")
    if estado in {"nueva", "contactada", "cerrada"}:
        solicitudes = solicitudes.filter(estado=estado)
    return render(request, "core/panel.html", {"solicitudes": solicitudes, "filtro": estado})


@require_POST
def estado(request, pk):
    solicitud = get_object_or_404(Solicitud, pk=pk)
    nuevo_estado = request.POST.get("estado")
    if nuevo_estado in {"nueva", "contactada", "cerrada"}:
        solicitud.estado = nuevo_estado
        solicitud.save(update_fields=["estado"])
    return redirect("panel")


class ServicioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Servicio.objects.filter(activo=True).order_by("nombre")
    serializer_class = ServicioSerializer


class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.select_related("servicio").order_by("-creada_en")
    serializer_class = SolicitudSerializer

