from src.service import RepositorioPedidos, procesar_compra


def test_compra_completa():
    pedido = procesar_compra(
        [{"precio": "9.99", "cantidad": 1}, {"precio": "5", "cantidad": 2}],
        RepositorioPedidos(),
    )
    assert pedido["id"] == 1
    assert str(pedido["total"]) == "19.99"
