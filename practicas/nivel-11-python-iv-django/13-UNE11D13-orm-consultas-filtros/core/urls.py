from django.urls import path

from .views import ofertas


urlpatterns = [path("", ofertas, name="ofertas")]

