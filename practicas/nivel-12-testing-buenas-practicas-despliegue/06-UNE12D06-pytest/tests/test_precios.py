from decimal import Decimal

import pytest
from precios import precio_final


def test_precio_final():
    assert precio_final("100") == Decimal("116.00")


def test_redondeo():
    assert precio_final("9.99") == Decimal("11.59")


def test_valor_negativo():
    with pytest.raises(ValueError, match="negativos"):
        precio_final("-1")
