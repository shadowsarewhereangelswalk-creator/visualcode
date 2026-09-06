from django.urls import path

from . import views


urlpatterns = [
    path("", views.lista, name="lista"),
    path("buscar/", views.buscar, name="buscar"),
    path("<int:noticia_id>/", views.detalle, name="detalle"),
]

