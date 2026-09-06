from unittest.mock import Mock

from src.orders import Inventario, crear_pedido


def test_pedido_integra_inventario_y_pago():
    pago = Mock()
    pago.cobrar.return_value = {"aprobado": True, "referencia": "P-001"}
    pedido = crear_pedido("mouse", 2, 15, Inventario({"mouse": 5}), pago)
    assert pedido["total"] == 30
    assert pedido["restante"] == 3
    pago.cobrar.assert_called_once_with(30)
