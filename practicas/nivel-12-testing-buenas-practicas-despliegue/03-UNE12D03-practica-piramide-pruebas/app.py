import json
import sys

PRACTICA = "UNE12D03"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D03"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from src.orders import Inventario, Pago, crear_pedido

resultado = crear_pedido("teclado", 2, 25.5, Inventario({"teclado": 6}), Pago())
print(json.dumps(resultado, ensure_ascii=False, indent=2))
