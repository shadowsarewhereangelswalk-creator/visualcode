from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ContactoForm


def contacto(request):
    formulario = ContactoForm(request.POST or None)
    if request.method == "POST" and formulario.is_valid():
        messages.success(request, f"Gracias, {formulario.cleaned_data['nombre']}. Tu mensaje fue validado.")
        return redirect("contacto")
    return render(request, "core/contacto.html", {"formulario": formulario})

