from django.urls import path

from .views import lista


app_name = "servicios"
urlpatterns = [path("", lista, name="lista")]

