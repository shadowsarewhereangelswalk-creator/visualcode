from django.db.models import Q
from django.http import JsonResponse

from .models import Oferta


def ofertas(request):
    consulta = Oferta.objects.filter(activa=True)
    busqueda = request.GET.get("q", "").strip()
    modalidad = request.GET.get("modalidad", "").strip()
    salario_minimo = request.GET.get("salario_minimo")
    if busqueda:
        consulta = consulta.filter(Q(cargo__icontains=busqueda) | Q(empresa__icontains=busqueda))
    if modalidad:
        consulta = consulta.filter(modalidad=modalidad)
    if salario_minimo and salario_minimo.isdigit():
        consulta = consulta.filter(salario__gte=int(salario_minimo))
    datos = list(consulta.order_by("-salario").values("id", "cargo", "empresa", "modalidad", "salario"))
    return JsonResponse({"total": len(datos), "ofertas": datos})

