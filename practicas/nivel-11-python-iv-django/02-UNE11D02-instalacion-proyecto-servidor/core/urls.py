from django.urls import path

from .views import inicio, salud


urlpatterns = [
    path("", inicio, name="inicio"),
    path("salud/", salud, name="salud"),
]

