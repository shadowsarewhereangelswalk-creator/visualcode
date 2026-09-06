from django.urls import path

from .views import campos


urlpatterns = [path("", campos, name="campos")]

