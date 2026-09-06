from django.db.models import Sum
from django.http import JsonResponse

from .models import Cliente


def datos(request):
    clientes = Cliente.objects.annotate(total_comprado=Sum("pedidos__total")).values("nombre", "correo", "total_comprado")
    return JsonResponse({"comando": "python manage.py cargar_demo", "clientes": list(clientes)})

