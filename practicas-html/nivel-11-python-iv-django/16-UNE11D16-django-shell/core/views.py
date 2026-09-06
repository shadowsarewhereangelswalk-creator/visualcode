from django.http import JsonResponse

from .models import Curso


def resumen(request):
    return JsonResponse({"comando": "python manage.py demo_orm", "cursos": list(Curso.objects.values("id", "nombre", "nivel", "activo"))})

