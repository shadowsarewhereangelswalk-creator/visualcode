from django.http import JsonResponse
from django.shortcuts import redirect, render

from .forms import IncidenciaForm
from .models import Incidencia


def inicio(request):
    formulario = IncidenciaForm(request.POST or None)
    if request.method == "POST" and formulario.is_valid():
        formulario.save()
        return redirect("inicio")
    return render(request, "core/inicio.html", {"formulario": formulario, "incidencias": Incidencia.objects.order_by("resuelta", "-id")})


def api(request):
    prioridad = request.GET.get("prioridad")
    consulta = Incidencia.objects.all()
    if prioridad in {"baja", "media", "alta"}:
        consulta = consulta.filter(prioridad=prioridad)
    return JsonResponse({"datos": list(consulta.values("id", "titulo", "prioridad", "resuelta")), "total": consulta.count()})

