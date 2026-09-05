def agregar_producto(inventario, nombre, precio, cantidad):
    producto = {
        "id": max((item["id"] for item in inventario), default=0) + 1,
        "nombre": nombre.strip().title(),
        "precio": float(precio),
        "cantidad": int(cantidad),
    }
    if producto["precio"] <= 0 or producto["cantidad"] < 0:
        raise ValueError("Precio o cantidad inválidos")
    inventario.append(producto)
    return producto


def actualizar_producto(inventario, producto_id, cantidad):
    for producto in inventario:
        if producto["id"] == producto_id:
            producto["cantidad"] = int(cantidad)
            return producto
    raise LookupError("Producto no encontrado")


def eliminar_producto(inventario, producto_id):
    for indice, producto in enumerate(inventario):
        if producto["id"] == producto_id:
            return inventario.pop(indice)
    raise LookupError("Producto no encontrado")


def filtrar_disponibles(inventario):
    return [producto for producto in inventario if producto["cantidad"] > 0]


def valor_inventario(inventario):
    return sum(producto["precio"] * producto["cantidad"] for producto in inventario)


def main():
    inventario = []
    agregar_producto(inventario, "teclado", 42.5, 8)
    agregar_producto(inventario, "monitor", 210, 3)
    agregar_producto(inventario, "cámara web", 76.9, 0)
    actualizar_producto(inventario, 3, 5)
    eliminado = eliminar_producto(inventario, 1)

    print(f'Eliminado: {eliminado["nombre"]}')
    for producto in filtrar_disponibles(inventario):
        print(f'{producto["id"]}: {producto["nombre"]} · {producto["cantidad"]} unidades')
    print(f"Valor del inventario: {valor_inventario(inventario):.2f}")


if __name__ == "__main__":
    main()
