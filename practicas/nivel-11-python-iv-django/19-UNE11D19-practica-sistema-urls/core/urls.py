from django.urls import include, path

from . import views


producto_patterns = [
    path("", views.productos, name="lista"),
    path("<slug:slug>/", views.detalle_producto, name="detalle"),
]

app_name = "core"
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("tienda/", include((producto_patterns, "tienda"), namespace="tienda")),
    path("perfil/<str:usuario>/", views.perfil, name="perfil"),
]

