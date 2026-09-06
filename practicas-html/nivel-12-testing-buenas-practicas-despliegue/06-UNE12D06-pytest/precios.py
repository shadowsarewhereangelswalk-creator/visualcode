from decimal import ROUND_HALF_UP, Decimal


def precio_final(precio, impuesto=Decimal("0.16")):
    precio = Decimal(str(precio))
    impuesto = Decimal(str(impuesto))
    if precio < 0 or impuesto < 0:
        raise ValueError("Los valores no pueden ser negativos")
    return (precio * (Decimal("1") + impuesto)).quantize(
        Decimal("0.01"), rounding=ROUND_HALF_UP
    )
