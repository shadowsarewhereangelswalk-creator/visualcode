from django.db.models import Avg, Count, Sum
from django.http import JsonResponse

from .models import Venta


def reporte(request):
    consulta = Venta.objects.all()
    categoria = request.GET.get("categoria", "").strip()
    if categoria:
        consulta = consulta.filter(categoria__iexact=categoria)
    resumen = consulta.aggregate(ventas=Count("id"), total_ingresos=Sum("total"), promedio_venta=Avg("total"))
    categorias = list(consulta.values("categoria").annotate(ventas=Count("id"), total_ingresos=Sum("total")).order_by("-total_ingresos"))
    return JsonResponse({"resumen": resumen, "categorias": categorias})
