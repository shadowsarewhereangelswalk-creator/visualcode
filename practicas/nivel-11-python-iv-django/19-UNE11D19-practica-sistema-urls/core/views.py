from django.http import JsonResponse
from django.urls import reverse


PRODUCTOS = [
    {"slug": "curso-django", "nombre": "Curso Django"},
    {"slug": "mentoria-python", "nombre": "Mentoría Python"},
]


def inicio(request):
    return JsonResponse({"tienda": reverse("core:tienda:lista"), "perfil": reverse("core:perfil", args=["karen"])})


def productos(request):
    return JsonResponse({"productos": [{**producto, "url": reverse("core:tienda:detalle", args=[producto["slug"]])} for producto in PRODUCTOS]})


def detalle_producto(request, slug):
    producto = next((item for item in PRODUCTOS if item["slug"] == slug), None)
    return JsonResponse(producto or {"error": "No encontrado"}, status=200 if producto else 404)


def perfil(request, usuario):
    return JsonResponse({"usuario": usuario, "ruta": request.path})

