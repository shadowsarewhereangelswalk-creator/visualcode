from django.http import JsonResponse

from .services import mapa_aplicacion


def inicio(request):
    return JsonResponse(mapa_aplicacion())

