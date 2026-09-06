import json
import sys
from decimal import Decimal

from src.orders import LineaPedido, total_pedido

PRACTICA = "UNE12D11"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D11"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


lineas = [
    LineaPedido("Teclado", Decimal("35.50"), 1),
    LineaPedido("Mouse", Decimal("18.25"), 2),
]
print(json.dumps({"total": str(total_pedido(lineas))}, indent=2))
