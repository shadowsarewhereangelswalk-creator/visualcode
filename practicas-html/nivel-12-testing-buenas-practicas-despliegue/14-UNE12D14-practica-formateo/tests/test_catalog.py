from decimal import Decimal

from src.catalog import Producto, serializar_catalogo


def test_serializar_catalogo():
    productos = [
        Producto("Zeta", Decimal("9.50")),
        Producto("Alfa", Decimal("4.25")),
        Producto("Oculto", Decimal("1"), False),
    ]
    assert serializar_catalogo(productos) == [
        {"nombre": "Alfa", "precio": "4.25", "activo": True},
        {"nombre": "Zeta", "precio": "9.50", "activo": True},
    ]
