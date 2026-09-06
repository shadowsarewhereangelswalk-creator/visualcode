import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Nota


def inicio(request):
    return JsonResponse({"servicio": "API de notas", "coleccion": "/api/notas/"})


def validar(datos):
    titulo = str(datos.get("titulo", "")).strip()
    contenido = str(datos.get("contenido", "")).strip()
    return (titulo, contenido) if 3 <= len(titulo) <= 120 and len(contenido) >= 5 else None


@csrf_exempt
@require_http_methods(["GET", "POST"])
def coleccion(request):
    if request.method == "GET":
        notas = [nota.to_dict() for nota in Nota.objects.order_by("-id")]
        return JsonResponse({"datos": notas, "total": len(notas)})
    try:
        datos = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON no válido"}, status=400)
    campos = validar(datos)
    if campos is None:
        return JsonResponse({"error": "Datos no válidos"}, status=422)
    nota = Nota.objects.create(titulo=campos[0], contenido=campos[1])
    return JsonResponse(nota.to_dict(), status=201)


@csrf_exempt
@require_http_methods(["GET", "PATCH", "DELETE"])
def detalle(request, nota_id):
    try:
        nota = Nota.objects.get(pk=nota_id)
    except Nota.DoesNotExist:
        return JsonResponse({"error": "Nota no encontrada"}, status=404)
    if request.method == "GET":
        return JsonResponse(nota.to_dict())
    if request.method == "DELETE":
        nota.delete()
        return JsonResponse({}, status=204)
    try:
        datos = json.loads(request.body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "JSON no válido"}, status=400)
    campos = validar({"titulo": datos.get("titulo", nota.titulo), "contenido": datos.get("contenido", nota.contenido)})
    if campos is None:
        return JsonResponse({"error": "Datos no válidos"}, status=422)
    nota.titulo, nota.contenido = campos
    nota.save()
    return JsonResponse(nota.to_dict())
