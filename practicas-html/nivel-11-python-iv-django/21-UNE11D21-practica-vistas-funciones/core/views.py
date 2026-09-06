from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import TareaForm
from .models import Tarea


def lista(request):
    return render(request, "core/tareas.html", {"tareas": Tarea.objects.order_by("completada", "-id"), "formulario": TareaForm()})


@require_POST
def crear(request):
    formulario = TareaForm(request.POST)
    if formulario.is_valid():
        formulario.save()
    return redirect("lista")


@require_POST
def alternar(request, pk):
    tarea = get_object_or_404(Tarea, pk=pk)
    tarea.completada = not tarea.completada
    tarea.save(update_fields=["completada"])
    return redirect("lista")


@require_POST
def eliminar(request, pk):
    get_object_or_404(Tarea, pk=pk).delete()
    return redirect("lista")

