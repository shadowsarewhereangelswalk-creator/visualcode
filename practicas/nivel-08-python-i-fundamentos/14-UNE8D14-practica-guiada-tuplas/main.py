ventas = (
    ("COT-001", "Landing page", 450.0, 2),
    ("COT-002", "Automatización", 780.0, 1),
    ("COT-003", "Asistente virtual", 950.0, 3),
    ("COT-004", "Landing page", 450.0, 1),
)


def totalizar(registros):
    totales = []
    for codigo, servicio, precio, cantidad in registros:
        subtotal = precio * cantidad
        totales.append((codigo, servicio, cantidad, subtotal))
    return tuple(totales)


def encontrar_mayor(registros):
    return max(registros, key=lambda registro: registro[3])


def resumir_servicios(registros):
    resumen = {}
    for _, servicio, cantidad, subtotal in registros:
        unidades, total = resumen.get(servicio, (0, 0.0))
        resumen[servicio] = unidades + cantidad, total + subtotal
    return tuple((servicio, *valores) for servicio, valores in sorted(resumen.items()))


def main():
    registros = totalizar(ventas)
    codigo, servicio, cantidad, subtotal = encontrar_mayor(registros)
    print(f"Mayor venta: {codigo} · {servicio} · {cantidad} · {subtotal:.2f}")
    print("Resumen:")
    for nombre, unidades, total in resumir_servicios(registros):
        print(f"{nombre}: {unidades} unidades · {total:.2f}")


if __name__ == "__main__":
    main()
