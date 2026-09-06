from django.shortcuts import redirect, render

from .forms import ClienteForm, ProyectoForm
from .models import Cliente


def inicio(request):
    if request.method == "POST":
        formulario = ClienteForm(request.POST) if request.POST.get("tipo") == "cliente" else ProyectoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    contexto = {
        "clientes": Cliente.objects.prefetch_related("proyectos__etiquetas"),
        "cliente_form": ClienteForm(),
        "proyecto_form": ProyectoForm(),
    }
    return render(request, "core/relaciones.html", contexto)

