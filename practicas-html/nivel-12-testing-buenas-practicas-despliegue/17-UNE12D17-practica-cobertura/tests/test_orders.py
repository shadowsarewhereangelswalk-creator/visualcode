from decimal import Decimal

import pytest
from orders import crear_pedido


def test_pedido_con_envio_gratis():
    pedido = crear_pedido("Karen", 50)
    assert pedido.envio == Decimal("0")
    assert pedido.confirmar() == "confirmado"
    assert pedido.serializar()["total"] == "50"


def test_pedido_con_costo_envio():
    pedido = crear_pedido("María", 20)
    assert pedido.envio == Decimal("5")
    assert pedido.cancelar() == "cancelado"


def test_confirmacion_repetida():
    pedido = crear_pedido("Pedro", 60)
    pedido.confirmar()
    with pytest.raises(ValueError, match="procesado"):
        pedido.confirmar()


def test_cancelacion_enviado():
    pedido = crear_pedido("Lucía", 70)
    pedido.estado = "enviado"
    with pytest.raises(ValueError, match="enviado"):
        pedido.cancelar()


@pytest.mark.parametrize(("cliente", "subtotal"), [("A", 10), ("Cliente", 0)])
def test_datos_invalidos(cliente, subtotal):
    with pytest.raises(ValueError):
        crear_pedido(cliente, subtotal)
