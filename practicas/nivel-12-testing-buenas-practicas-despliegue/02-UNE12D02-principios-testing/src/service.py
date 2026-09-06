from .cart import calcular_total


class RepositorioPedidos:
    def __init__(self):
        self.pedidos = []

    def guardar(self, pedido):
        pedido = {"id": len(self.pedidos) + 1, **pedido}
        self.pedidos.append(pedido)
        return pedido


def procesar_compra(items, repositorio):
    total = calcular_total(items)
    return repositorio.guardar({"items": items, "total": total})
