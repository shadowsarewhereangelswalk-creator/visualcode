from decimal import ROUND_HALF_UP, Decimal


def calcular_descuento(subtotal, tipo_cliente, cupon=None):
    subtotal = Decimal(str(subtotal))
    if subtotal < 0:
        raise ValueError("Subtotal no válido")
    tasas = {
        "regular": Decimal("0"),
        "frecuente": Decimal("0.10"),
        "vip": Decimal("0.20"),
    }
    if tipo_cliente not in tasas:
        raise ValueError("Tipo de cliente no válido")
    tasa = tasas[tipo_cliente]
    if cupon == "EXTRA5":
        tasa += Decimal("0.05")
    tasa = min(tasa, Decimal("0.25"))
    descuento = (subtotal * tasa).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return {
        "subtotal": subtotal,
        "tasa": tasa,
        "descuento": descuento,
        "total": subtotal - descuento,
    }
