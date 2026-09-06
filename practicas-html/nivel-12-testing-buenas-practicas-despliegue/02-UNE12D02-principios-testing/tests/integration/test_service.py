from decimal import Decimal

from src.service import RepositorioPedidos, procesar_compra


def test_servicio_guarda_pedido():
    repositorio = RepositorioPedidos()
    pedido = procesar_compra([{"precio": "10", "cantidad": 3}], repositorio)
    assert pedido["total"] == Decimal("30.00")
    assert repositorio.pedidos == [pedido]
