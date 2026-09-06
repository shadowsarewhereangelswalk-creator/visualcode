from django.urls import path

from .views import ProductoCrear, ProductoEditar, ProductoEliminar, ProductoLista


urlpatterns = [
    path("", ProductoLista.as_view(), name="lista"),
    path("crear/", ProductoCrear.as_view(), name="crear"),
    path("<int:pk>/editar/", ProductoEditar.as_view(), name="editar"),
    path("<int:pk>/eliminar/", ProductoEliminar.as_view(), name="eliminar"),
]

