from collections import Counter
from decimal import Decimal


def crear_reporte(ventas):
    total = sum((Decimal(str(venta["total"])) for venta in ventas), Decimal("0"))
    categorias = Counter(venta["categoria"] for venta in ventas)
    principal = categorias.most_common(1)[0][0] if categorias else None
    return {
        "cantidad": len(ventas),
        "total": total.quantize(Decimal("0.01")),
        "categoria_principal": principal,
    }
