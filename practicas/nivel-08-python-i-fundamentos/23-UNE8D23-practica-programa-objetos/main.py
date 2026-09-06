from dataclasses import dataclass, field
from decimal import Decimal, ROUND_HALF_UP


@dataclass(frozen=True)
class Servicio:
    codigo: str
    nombre: str
    precio: Decimal

    def __post_init__(self):
        if self.precio <= 0:
            raise ValueError("El precio debe ser positivo")


@dataclass
class Cliente:
    codigo: str
    nombre: str
    correo: str

    def resumen(self):
        return f"{self.codigo} · {self.nombre} · {self.correo}"


@dataclass
class ItemCotizacion:
    servicio: Servicio
    cantidad: int = 1

    @property
    def subtotal(self):
        return self.servicio.precio * self.cantidad


@dataclass
class Cotizacion:
    numero: str
    cliente: Cliente
    items: list[ItemCotizacion] = field(default_factory=list)
    impuesto: Decimal = Decimal("0.16")

    def agregar(self, servicio, cantidad=1):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.items.append(ItemCotizacion(servicio, cantidad))

    @property
    def subtotal(self):
        return sum((item.subtotal for item in self.items), Decimal("0"))

    @property
    def total(self):
        return self.subtotal * (Decimal("1") + self.impuesto)

    def resumen(self):
        moneda = Decimal("0.01")
        lineas = [f"Cotización {self.numero}", self.cliente.resumen()]
        for item in self.items:
            lineas.append(
                f"{item.servicio.nombre} x {item.cantidad}: {item.subtotal.quantize(moneda, rounding=ROUND_HALF_UP):.2f}"
            )
        lineas.append(f"Subtotal: {self.subtotal.quantize(moneda, rounding=ROUND_HALF_UP):.2f}")
        lineas.append(f"Total: {self.total.quantize(moneda, rounding=ROUND_HALF_UP):.2f}")
        return "\n".join(lineas)


def main():
    cliente = Cliente("CLI-001", "Ana Torres", "ana@ejemplo.com")
    landing = Servicio("WEB-01", "Landing page", Decimal("450"))
    automatizacion = Servicio("AUT-02", "Automatización", Decimal("320"))
    cotizacion = Cotizacion("COT-2027-001", cliente)
    cotizacion.agregar(landing)
    cotizacion.agregar(automatizacion, 3)
    print(cotizacion.resumen())


if __name__ == "__main__":
    main()
