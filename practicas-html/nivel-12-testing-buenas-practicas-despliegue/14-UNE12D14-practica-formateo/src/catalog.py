from dataclasses import asdict, dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Producto:
    nombre: str
    precio: Decimal
    activo: bool = True


def serializar_catalogo(productos):
    activos = sorted(
        (producto for producto in productos if producto.activo),
        key=lambda producto: producto.nombre.casefold(),
    )
    return [
        {**asdict(producto), "precio": str(producto.precio)} for producto in activos
    ]
