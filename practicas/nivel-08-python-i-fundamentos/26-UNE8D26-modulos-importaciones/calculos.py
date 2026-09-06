from decimal import Decimal, ROUND_HALF_UP


def convertir_decimal(valor):
    return Decimal(str(valor))


def calcular_total(precio, cantidad=1, descuento=0, impuesto=0.16):
    precio = convertir_decimal(precio)
    cantidad = convertir_decimal(cantidad)
    descuento = convertir_decimal(descuento)
    impuesto = convertir_decimal(impuesto)
    subtotal = precio * cantidad
    base = subtotal * (Decimal("1") - descuento)
    total = base * (Decimal("1") + impuesto)
    return total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
