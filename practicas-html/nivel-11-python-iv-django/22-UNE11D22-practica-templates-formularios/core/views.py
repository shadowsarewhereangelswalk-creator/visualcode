from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ReservaForm
from .models import Reserva


def inicio(request):
    formulario = ReservaForm(request.POST or None)
    if request.method == "POST" and formulario.is_valid():
        formulario.save()
        messages.success(request, "Reserva creada correctamente.")
        return redirect("inicio")
    return render(request, "core/inicio.html", {"formulario": formulario})


def reservas(request):
    return render(request, "core/reservas.html", {"reservas": Reserva.objects.order_by("fecha")})

