from collections import defaultdict


def consolidar_movimientos(movimientos):
    existencias = defaultdict(int)
    for movimiento in movimientos:
        producto = movimiento["producto"].strip()
        cantidad = int(movimiento["cantidad"])
        if not producto or cantidad == 0:
            raise ValueError("Movimiento no válido")
        existencias[producto] += cantidad
        if existencias[producto] < 0:
            raise ValueError(f"Existencia negativa para {producto}")
    return dict(sorted(existencias.items()))


def productos_disponibles(existencias):
    return [nombre for nombre, cantidad in existencias.items() if cantidad > 0]
