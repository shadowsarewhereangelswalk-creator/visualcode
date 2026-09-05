from decimal import Decimal, ROUND_HALF_UP


def convertir_decimal(valor):
    return Decimal(str(valor))


def calcular_subtotal(precio, cantidad):
    precio = convertir_decimal(precio)
    cantidad = convertir_decimal(cantidad)
    if precio <= 0 or cantidad <= 0:
        raise ValueError("El precio y la cantidad deben ser positivos")
    return precio * cantidad


def calcular_descuento(subtotal, porcentaje=0):
    porcentaje = convertir_decimal(porcentaje)
    if not Decimal("0") <= porcentaje <= Decimal("1"):
        raise ValueError("El descuento debe estar entre cero y uno")
    return subtotal * porcentaje


def calcular_impuesto(base, tasa=0.16):
    return base * convertir_decimal(tasa)


def crear_cotizacion(servicio, precio, cantidad=1, descuento=0, impuesto=0.16):
    subtotal = calcular_subtotal(precio, cantidad)
    ahorro = calcular_descuento(subtotal, descuento)
    base = subtotal - ahorro
    tributo = calcular_impuesto(base, impuesto)
    total = base + tributo
    moneda = Decimal("0.01")
    return {
        "servicio": servicio.strip().title(),
        "subtotal": subtotal.quantize(moneda, rounding=ROUND_HALF_UP),
        "descuento": ahorro.quantize(moneda, rounding=ROUND_HALF_UP),
        "impuesto": tributo.quantize(moneda, rounding=ROUND_HALF_UP),
        "total": total.quantize(moneda, rounding=ROUND_HALF_UP),
    }


def mostrar_cotizacion(cotizacion):
    print(cotizacion["servicio"])
    for concepto in ("subtotal", "descuento", "impuesto", "total"):
        print(f'{concepto.title()}: {cotizacion[concepto]:.2f}')


if __name__ == "__main__":
    mostrar_cotizacion(
        crear_cotizacion(
            servicio="integración de datos",
            precio=280,
            cantidad=4,
            descuento=0.12,
        )
    )
