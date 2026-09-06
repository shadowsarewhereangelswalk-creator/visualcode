from django.urls import path

from . import views


app_name = "core"
urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("articulos/<int:articulo_id>/", views.articulo, name="articulo"),
    path("categorias/<slug:slug>/", views.categoria, name="categoria"),
    path("recursos/<uuid:identificador>/", views.recurso, name="recurso"),
]

