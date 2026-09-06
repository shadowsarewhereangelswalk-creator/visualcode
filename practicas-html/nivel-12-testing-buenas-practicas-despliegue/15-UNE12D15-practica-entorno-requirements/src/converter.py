from decimal import ROUND_HALF_UP, Decimal

TASAS = {
    ("USD", "EUR"): Decimal("0.92"),
    ("EUR", "USD"): Decimal("1.09"),
    ("USD", "VES"): Decimal("40.00"),
}


def convertir(monto, origen, destino):
    monto = Decimal(str(monto))
    origen = origen.upper()
    destino = destino.upper()
    if monto < 0:
        raise ValueError("El monto no puede ser negativo")
    if origen == destino:
        return monto.quantize(Decimal("0.01"))
    try:
        tasa = TASAS[(origen, destino)]
    except KeyError as error:
        raise ValueError("Conversión no disponible") from error
    return (monto * tasa).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
