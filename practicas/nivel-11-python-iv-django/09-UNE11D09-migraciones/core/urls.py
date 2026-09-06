from django.urls import path

from .views import estado


urlpatterns = [path("", estado, name="estado")]

