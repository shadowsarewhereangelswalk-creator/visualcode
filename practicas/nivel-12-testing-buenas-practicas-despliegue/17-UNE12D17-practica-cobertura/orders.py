from dataclasses import asdict, dataclass
from decimal import Decimal


@dataclass
class Pedido:
    cliente: str
    subtotal: Decimal
    envio: Decimal
    estado: str = "nuevo"

    def confirmar(self):
        if self.estado != "nuevo":
            raise ValueError("El pedido ya fue procesado")
        self.estado = "confirmado"
        return self.estado

    def cancelar(self):
        if self.estado == "enviado":
            raise ValueError("No se puede cancelar un pedido enviado")
        self.estado = "cancelado"
        return self.estado

    def serializar(self):
        datos = asdict(self)
        datos["subtotal"] = str(self.subtotal)
        datos["envio"] = str(self.envio)
        datos["total"] = str(self.subtotal + self.envio)
        return datos


def crear_pedido(cliente, subtotal):
    cliente = cliente.strip()
    subtotal = Decimal(str(subtotal))
    if len(cliente) < 3 or subtotal <= 0:
        raise ValueError("Datos de pedido no válidos")
    envio = Decimal("0") if subtotal >= 50 else Decimal("5")
    return Pedido(cliente, subtotal, envio)
