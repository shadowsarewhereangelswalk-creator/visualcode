from django.shortcuts import redirect, render

from .forms import AutorForm, LibroForm
from .models import Autor


def inicio(request):
    if request.method == "POST":
        formulario = AutorForm(request.POST) if request.POST.get("tipo") == "autor" else LibroForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("inicio")
    contexto = {"autores": Autor.objects.prefetch_related("libros"), "autor_form": AutorForm(), "libro_form": LibroForm()}
    return render(request, "core/biblioteca.html", contexto)

