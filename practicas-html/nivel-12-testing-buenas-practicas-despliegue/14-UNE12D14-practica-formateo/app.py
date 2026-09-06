import json
import sys
from decimal import Decimal

PRACTICA = "UNE12D14"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D14"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from src.catalog import Producto, serializar_catalogo

productos = [
    Producto("Monitor", Decimal("199.99")),
    Producto("Cable", Decimal("12.50")),
    Producto("Descontinuado", Decimal("2"), False),
]
print(json.dumps(serializar_catalogo(productos), ensure_ascii=False, indent=2))
