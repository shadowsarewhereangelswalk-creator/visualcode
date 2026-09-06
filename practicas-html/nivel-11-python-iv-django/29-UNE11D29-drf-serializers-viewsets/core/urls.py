from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework.routers import DefaultRouter

from .views import ClienteViewSet, ProyectoViewSet


router = DefaultRouter()
router.register("clientes", ClienteViewSet)
router.register("proyectos", ProyectoViewSet, basename="proyecto")

urlpatterns = [
    path("", RedirectView.as_view(url="/api/", permanent=False), name="inicio"),
    path("api/", include(router.urls)),
]
