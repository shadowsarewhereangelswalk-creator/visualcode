from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class LineaPedido:
    producto: str
    precio: Decimal
    cantidad: int

    @property
    def subtotal(self):
        return self.precio * self.cantidad


def total_pedido(lineas):
    if not lineas:
        raise ValueError("El pedido no puede estar vacío")
    if any(linea.cantidad <= 0 for linea in lineas):
        raise ValueError("Las cantidades deben ser positivas")
    return sum((linea.subtotal for linea in lineas), Decimal("0"))
