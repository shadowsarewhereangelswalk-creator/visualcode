import json
import sys

from src.inventory import consolidar_movimientos, productos_disponibles

PRACTICA = "UNE12D12"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D12"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


inventario = consolidar_movimientos(
    [
        {"producto": "Laptop", "cantidad": 5},
        {"producto": "Laptop", "cantidad": -2},
        {"producto": "Mouse", "cantidad": 4},
    ]
)
print(
    json.dumps(
        {"inventario": inventario, "disponibles": productos_disponibles(inventario)},
        ensure_ascii=False,
        indent=2,
    )
)
