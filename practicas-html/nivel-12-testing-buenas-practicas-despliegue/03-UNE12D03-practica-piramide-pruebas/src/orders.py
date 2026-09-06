class Inventario:
    def __init__(self, existencias):
        self.existencias = dict(existencias)

    def reservar(self, producto, cantidad):
        disponible = self.existencias.get(producto, 0)
        if cantidad <= 0 or cantidad > disponible:
            raise ValueError("Cantidad no disponible")
        self.existencias[producto] = disponible - cantidad
        return self.existencias[producto]


class Pago:
    def cobrar(self, monto):
        return {"aprobado": monto > 0, "referencia": f"P-{monto:.2f}"}


def crear_pedido(producto, cantidad, precio, inventario, pago):
    restante = inventario.reservar(producto, cantidad)
    transaccion = pago.cobrar(cantidad * precio)
    if not transaccion["aprobado"]:
        raise RuntimeError("Pago rechazado")
    return {
        "producto": producto,
        "cantidad": cantidad,
        "total": round(cantidad * precio, 2),
        "restante": restante,
        "pago": transaccion["referencia"],
    }
