from django.http import JsonResponse

from .models import Inventario


def inventario(request):
    productos = list(Inventario.objects.filter(activo=True).values("id", "nombre", "precio", "stock"))
    return JsonResponse({"migracion": "0002", "productos": productos})

