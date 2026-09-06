from decimal import Decimal

import pytest
from src.cart import calcular_total


def test_calcular_total_unitario():
    assert calcular_total([{"precio": "8.50", "cantidad": 2}]) == Decimal("17.00")


def test_descuento_invalido():
    with pytest.raises(ValueError):
        calcular_total([], Decimal("1.1"))
