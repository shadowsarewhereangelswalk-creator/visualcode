from decimal import Decimal, InvalidOperation, ROUND_HALF_UP


def convertir_numero(valor):
    try:
        numero = Decimal(str(valor))
    except InvalidOperation as error:
        raise ValueError("El valor debe ser numérico") from error
    if not numero.is_finite():
        raise ValueError("El valor debe ser finito")
    return numero


def convertir_moneda(monto, tasa):
    monto = convertir_numero(monto)
    tasa = convertir_numero(tasa)
    if monto < 0 or tasa <= 0:
        raise ValueError("El monto no puede ser negativo y la tasa debe ser positiva")
    return (monto * tasa).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def convertir_altura(centimetros):
    centimetros = convertir_numero(centimetros)
    if centimetros <= 0:
        raise ValueError("La altura debe ser positiva")
    pulgadas = centimetros / Decimal("2.54")
    pies = int(pulgadas // 12)
    pulgadas_restantes = (pulgadas % 12).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return pies, pulgadas_restantes


def main():
    total = convertir_moneda("125.50", "36.42")
    pies, pulgadas = convertir_altura(168)
    print(f"Conversión monetaria: {total}")
    print(f"Altura: {pies} pies y {pulgadas} pulgadas")


if __name__ == "__main__":
    main()
