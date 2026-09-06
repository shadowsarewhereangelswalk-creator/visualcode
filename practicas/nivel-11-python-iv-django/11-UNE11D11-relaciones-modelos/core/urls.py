from django.urls import path

from .views import relaciones


urlpatterns = [path("", relaciones, name="relaciones")]

