from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ServicioViewSet, SolicitudViewSet, estado, inicio, panel


router = DefaultRouter()
router.register("servicios", ServicioViewSet)
router.register("solicitudes", SolicitudViewSet)

urlpatterns = [
    path("", inicio, name="inicio"),
    path("panel/", panel, name="panel"),
    path("panel/<int:pk>/estado/", estado, name="estado"),
    path("api/", include(router.urls)),
]

