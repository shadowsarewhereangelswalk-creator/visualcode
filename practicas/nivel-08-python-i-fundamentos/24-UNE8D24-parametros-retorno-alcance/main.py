from decimal import Decimal


def crear_generador_codigos(prefijo):
    consecutivo = 0

    def generar():
        nonlocal consecutivo
        consecutivo += 1
        return f"{prefijo.upper()}-{consecutivo:04d}"

    return generar


def calcular_linea(nombre, precio, cantidad=1, descuento=0):
    precio = Decimal(str(precio))
    cantidad = Decimal(str(cantidad))
    descuento = Decimal(str(descuento))
    subtotal = precio * cantidad
    total = subtotal * (Decimal("1") - descuento)
    return {
        "nombre": nombre.strip().title(),
        "cantidad": int(cantidad),
        "subtotal": subtotal,
        "total": total,
    }


def generar_reporte(*lineas, titulo="Cotización", moneda="USD", **datos_cliente):
    total = sum((linea["total"] for linea in lineas), Decimal("0"))
    salida = [titulo, f'Cliente: {datos_cliente.get("nombre", "Sin nombre")}']
    salida.extend(
        f'{linea["nombre"]} x {linea["cantidad"]}: {moneda} {linea["total"]:.2f}'
        for linea in lineas
    )
    salida.append(f"Total: {moneda} {total:.2f}")
    return "\n".join(salida), total


def main():
    siguiente_codigo = crear_generador_codigos("cot")
    linea_web = calcular_linea("landing page", 450)
    linea_ia = calcular_linea("asistente virtual", 320, cantidad=3, descuento=0.1)
    reporte, total = generar_reporte(
        linea_web,
        linea_ia,
        titulo=siguiente_codigo(),
        moneda="USD",
        nombre="Karen Ramírez",
    )
    print(reporte)
    print(f"Siguiente código disponible: {siguiente_codigo()}")
    print(f"Valor retornado: {total:.2f}")


if __name__ == "__main__":
    main()
