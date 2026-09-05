def crear_inventario():
    return [
        {"codigo": "IA-101", "nombre": "Asistente virtual", "precio": 950.0, "stock": 3, "etiquetas": ("ia", "ventas")},
        {"codigo": "WEB-204", "nombre": "Landing page", "precio": 420.0, "stock": 5, "etiquetas": ("web", "marketing")},
        {"codigo": "AUT-310", "nombre": "Automatización", "precio": 780.0, "stock": 2, "etiquetas": ("python", "procesos")},
    ]


def agregar_producto(inventario, codigo, nombre, precio, stock, etiquetas):
    if any(producto["codigo"] == codigo for producto in inventario):
        raise ValueError("El código ya existe")
    inventario.append(
        {
            "codigo": codigo,
            "nombre": nombre,
            "precio": float(precio),
            "stock": int(stock),
            "etiquetas": tuple(etiquetas),
        }
    )


def buscar_producto(inventario, codigo):
    return next((producto for producto in inventario if producto["codigo"] == codigo), None)


def vender(inventario, codigo, cantidad):
    producto = buscar_producto(inventario, codigo)
    if producto is None:
        raise LookupError("Producto no encontrado")
    if cantidad <= 0 or producto["stock"] < cantidad:
        raise ValueError("Cantidad inválida o stock insuficiente")
    producto["stock"] -= cantidad
    return producto["precio"] * cantidad


def resumir(inventario):
    valor_total = sum(producto["precio"] * producto["stock"] for producto in inventario)
    agotados = tuple(producto["codigo"] for producto in inventario if producto["stock"] == 0)
    return {
        "productos": len(inventario),
        "unidades": sum(producto["stock"] for producto in inventario),
        "valor": valor_total,
        "agotados": agotados,
    }


def main():
    inventario = crear_inventario()
    agregar_producto(inventario, "DAT-415", "Tablero de datos", 640, 4, ("datos", "reportes"))
    total_venta = vender(inventario, "IA-101", 2)
    resumen = resumir(inventario)

    print(f"Venta procesada: {total_venta:.2f}")
    for producto in inventario:
        print(f'{producto["codigo"]} · {producto["nombre"]} · stock {producto["stock"]}')
    print(f'Resumen: {resumen["productos"]} productos, {resumen["unidades"]} unidades, valor {resumen["valor"]:.2f}')


if __name__ == "__main__":
    main()
