from django.http import JsonResponse
from django.urls import reverse


def inicio(request):
    return JsonResponse({"articulo_ejemplo": reverse("core:articulo", args=[7]), "categoria_ejemplo": reverse("core:categoria", args=["django"])})


def articulo(request, articulo_id):
    return JsonResponse({"tipo": "articulo", "id": articulo_id})


def categoria(request, slug):
    return JsonResponse({"tipo": "categoria", "slug": slug})


def recurso(request, identificador):
    return JsonResponse({"tipo": "recurso", "uuid": str(identificador)})

