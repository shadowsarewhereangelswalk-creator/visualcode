from src.orders import Inventario, Pago, crear_pedido


def test_flujo_completo():
    pedido = crear_pedido("cámara", 1, 80, Inventario({"cámara": 2}), Pago())
    assert pedido == {
        "producto": "cámara",
        "cantidad": 1,
        "total": 80,
        "restante": 1,
        "pago": "P-80.00",
    }
