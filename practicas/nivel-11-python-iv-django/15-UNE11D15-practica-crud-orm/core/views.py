from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactoForm
from .models import Contacto


def lista(request):
    busqueda = request.GET.get("q", "").strip()
    contactos = Contacto.objects.order_by("nombre")
    if busqueda:
        contactos = contactos.filter(nombre__icontains=busqueda)
    return render(request, "core/lista.html", {"contactos": contactos, "busqueda": busqueda})


def crear(request):
    formulario = ContactoForm(request.POST or None)
    if request.method == "POST" and formulario.is_valid():
        formulario.save()
        return redirect("lista")
    return render(request, "core/formulario.html", {"formulario": formulario, "titulo": "Crear contacto"})


def editar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    formulario = ContactoForm(request.POST or None, instance=contacto)
    if request.method == "POST" and formulario.is_valid():
        formulario.save()
        return redirect("lista")
    return render(request, "core/formulario.html", {"formulario": formulario, "titulo": "Editar contacto"})


def eliminar(request, pk):
    contacto = get_object_or_404(Contacto, pk=pk)
    if request.method == "POST":
        contacto.delete()
        return redirect("lista")
    return render(request, "core/eliminar.html", {"contacto": contacto})

