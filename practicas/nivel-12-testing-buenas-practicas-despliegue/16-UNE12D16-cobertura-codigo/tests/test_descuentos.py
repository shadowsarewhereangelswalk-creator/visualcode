from decimal import Decimal

import pytest
from descuentos import calcular_descuento


@pytest.mark.parametrize(
    ("tipo", "tasa"),
    [("regular", "0"), ("frecuente", "0.10"), ("vip", "0.20")],
)
def test_tasas(tipo, tasa):
    assert calcular_descuento(100, tipo)["tasa"] == Decimal(tasa)


def test_cupon_extra():
    resultado = calcular_descuento(100, "vip", "EXTRA5")
    assert resultado["descuento"] == Decimal("25.00")
    assert resultado["total"] == Decimal("75.00")


@pytest.mark.parametrize(("subtotal", "tipo"), [(-1, "regular"), (10, "desconocido")])
def test_datos_invalidos(subtotal, tipo):
    with pytest.raises(ValueError):
        calcular_descuento(subtotal, tipo)
