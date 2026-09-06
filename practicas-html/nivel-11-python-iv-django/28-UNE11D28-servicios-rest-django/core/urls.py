from django.urls import path

from .views import coleccion, detalle, inicio


urlpatterns = [
    path("", inicio, name="inicio"),
    path("api/notas/", coleccion, name="notas"),
    path("api/notas/<int:nota_id>/", detalle, name="nota"),
]
