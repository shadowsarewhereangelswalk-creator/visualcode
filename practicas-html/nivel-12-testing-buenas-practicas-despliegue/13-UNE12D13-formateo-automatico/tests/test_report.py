from decimal import Decimal

from src.report import crear_reporte


def test_crear_reporte():
    reporte = crear_reporte(
        [
            {"categoria": "A", "total": "10.25"},
            {"categoria": "A", "total": "4.75"},
            {"categoria": "B", "total": "2"},
        ]
    )
    assert reporte == {
        "cantidad": 3,
        "total": Decimal("17.00"),
        "categoria_principal": "A",
    }


def test_reporte_vacio():
    assert crear_reporte([])["categoria_principal"] is None
