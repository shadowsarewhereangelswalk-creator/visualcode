from django.urls import path

from .views import crear, inicio


urlpatterns = [path("", inicio, name="inicio"), path("crear/", crear, name="crear")]

