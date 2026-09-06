from decimal import Decimal

import pytest

from src.orders import LineaPedido, total_pedido


def test_total_pedido():
    lineas = [LineaPedido("Monitor", Decimal("120"), 2)]
    assert total_pedido(lineas) == Decimal("240")


def test_pedido_vacio():
    with pytest.raises(ValueError):
        total_pedido([])
