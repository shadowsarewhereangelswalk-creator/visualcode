from decimal import Decimal


def calcular_total(items, descuento=Decimal("0")):
    subtotal = sum(
        (Decimal(str(item["precio"])) * int(item["cantidad"]) for item in items),
        Decimal("0"),
    )
    if not Decimal("0") <= descuento <= Decimal("1"):
        raise ValueError("El descuento debe estar entre 0 y 1")
    return (subtotal * (Decimal("1") - descuento)).quantize(Decimal("0.01"))
