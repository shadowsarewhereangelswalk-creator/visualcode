from django.http import JsonResponse

from .models import Curso


def campos(request):
    datos = [{"nombre": campo.name, "tipo": campo.get_internal_type()} for campo in Curso._meta.fields]
    return JsonResponse({"modelo": "Curso", "campos": datos})

