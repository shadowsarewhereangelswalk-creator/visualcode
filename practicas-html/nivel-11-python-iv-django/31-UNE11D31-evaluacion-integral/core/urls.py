from django.urls import path

from .views import api, inicio


urlpatterns = [path("", inicio, name="inicio"), path("api/incidencias/", api, name="api")]

