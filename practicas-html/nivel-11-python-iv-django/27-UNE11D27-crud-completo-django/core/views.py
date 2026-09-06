from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .forms import ProductoForm
from .models import Producto


class ProductoLista(ListView):
    model = Producto
    template_name = "core/lista.html"
    context_object_name = "productos"
    ordering = ["nombre"]


class ProductoCrear(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "core/formulario.html"
    success_url = reverse_lazy("lista")


class ProductoEditar(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "core/formulario.html"
    success_url = reverse_lazy("lista")


class ProductoEliminar(DeleteView):
    model = Producto
    template_name = "core/eliminar.html"
    success_url = reverse_lazy("lista")

