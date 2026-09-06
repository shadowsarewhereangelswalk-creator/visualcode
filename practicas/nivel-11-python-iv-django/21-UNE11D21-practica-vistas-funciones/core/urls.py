from django.urls import path

from . import views


urlpatterns = [
    path("", views.lista, name="lista"),
    path("crear/", views.crear, name="crear"),
    path("<int:pk>/alternar/", views.alternar, name="alternar"),
    path("<int:pk>/eliminar/", views.eliminar, name="eliminar"),
]

