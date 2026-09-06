from django.urls import path

from .views import datos


urlpatterns = [path("", datos, name="datos")]

