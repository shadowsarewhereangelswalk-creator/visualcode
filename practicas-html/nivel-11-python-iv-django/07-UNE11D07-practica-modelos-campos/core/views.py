from decimal import Decimal, InvalidOperation

from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from .models import Producto


def inicio(request):
    return render(request, "core/productos.html", {"productos": Producto.objects.order_by("nombre")})


@require_POST
def crear(request):
    try:
        precio = Decimal(request.POST.get("precio", ""))
        stock = int(request.POST.get("stock", "0"))
    except (InvalidOperation, ValueError):
        return redirect("inicio")
    nombre = request.POST.get("nombre", "").strip()
    categoria = request.POST.get("categoria", "").strip()
    if nombre and categoria and precio >= 0 and stock >= 0:
        Producto.objects.create(nombre=nombre, categoria=categoria, precio=precio, stock=stock)
    return redirect("inicio")

