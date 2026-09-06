from decimal import Decimal, ROUND_HALF_UP


def calcular_servicio(precio_hora, horas, impuesto, descuento=0):
    precio_hora = Decimal(str(precio_hora))
    horas = Decimal(str(horas))
    impuesto = Decimal(str(impuesto))
    descuento = Decimal(str(descuento))

    subtotal = precio_hora * horas
    monto_descuento = subtotal * descuento
    base_imponible = subtotal - monto_descuento
    monto_impuesto = base_imponible * impuesto
    total = base_imponible + monto_impuesto

    return {
        "subtotal": subtotal.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "descuento": monto_descuento.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "impuesto": monto_impuesto.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "total": total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP),
        "horas_completas": int(horas // 1),
        "tiene_fraccion": horas % 1 != 0,
    }


def mostrar_cotizacion(detalle):
    print("Cotización de servicio")
    print(f'Subtotal: ${detalle["subtotal"]}')
    print(f'Descuento: ${detalle["descuento"]}')
    print(f'Impuesto: ${detalle["impuesto"]}')
    print(f'Total: ${detalle["total"]}')
    print(f'Horas completas: {detalle["horas_completas"]}')
    print(f'Incluye fracción de hora: {detalle["tiene_fraccion"]}')


if __name__ == "__main__":
    mostrar_cotizacion(calcular_servicio(37.5, 12.5, 0.16, 0.08))
