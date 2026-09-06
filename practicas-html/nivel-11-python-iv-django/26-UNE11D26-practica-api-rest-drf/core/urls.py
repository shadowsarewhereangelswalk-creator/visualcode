from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import TareaViewSet


router = DefaultRouter()
router.register("tareas", TareaViewSet, basename="tarea")

urlpatterns = [path("", include(router.urls))]

