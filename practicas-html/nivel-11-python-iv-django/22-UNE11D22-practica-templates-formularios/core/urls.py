from django.urls import path

from .views import inicio, reservas


urlpatterns = [path("", inicio, name="inicio"), path("reservas/", reservas, name="reservas")]

