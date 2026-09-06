def clasificar_cliente(cliente):
    if not cliente["activo"]:
        return "inactivo"
    if cliente["compras"] >= 5000 and cliente["antiguedad"] >= 3:
        return "premium"
    if cliente["compras"] >= 2000 or cliente["antiguedad"] >= 2:
        return "frecuente"
    return "nuevo"


def descuento_por_categoria(categoria):
    if categoria == "premium":
        return 0.15
    if categoria == "frecuente":
        return 0.08
    return 0.0


def crear_plan_pagos(total, monto_maximo):
    if total <= 0 or monto_maximo <= 0:
        raise ValueError("Los montos deben ser positivos")
    cuotas = []
    saldo = round(total, 2)
    numero = 1
    while saldo > 0:
        monto = min(monto_maximo, saldo)
        cuotas.append({"numero": numero, "monto": round(monto, 2)})
        saldo = round(saldo - monto, 2)
        numero += 1
    return cuotas


def procesar_clientes(clientes, precio):
    resultados = []
    for cliente in clientes:
        categoria = clasificar_cliente(cliente)
        if categoria == "inactivo":
            continue
        descuento = descuento_por_categoria(categoria)
        total = round(precio * (1 - descuento), 2)
        resultados.append(
            {
                "nombre": cliente["nombre"],
                "categoria": categoria,
                "descuento": descuento,
                "total": total,
                "cuotas": crear_plan_pagos(total, 400),
            }
        )
    return resultados


def main():
    clientes = [
        {"nombre": "Ana", "edad": 34, "compras": 6800, "antiguedad": 4, "activo": True},
        {"nombre": "Luis", "edad": 27, "compras": 2400, "antiguedad": 1, "activo": True},
        {"nombre": "Marta", "edad": 41, "compras": 900, "antiguedad": 1, "activo": False},
        {"nombre": "Diego", "edad": 22, "compras": 350, "antiguedad": 0, "activo": True},
    ]
    for resultado in procesar_clientes(clientes, 1200):
        montos = ", ".join(f'{cuota["monto"]:.2f}' for cuota in resultado["cuotas"])
        print(f'{resultado["nombre"]}: {resultado["categoria"]} · total {resultado["total"]:.2f} · cuotas {montos}')


if __name__ == "__main__":
    main()
