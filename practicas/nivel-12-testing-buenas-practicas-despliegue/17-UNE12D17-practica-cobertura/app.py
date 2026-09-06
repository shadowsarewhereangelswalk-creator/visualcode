import json
import sys

PRACTICA = "UNE12D17"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D17"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from orders import crear_pedido

pedido = crear_pedido("Karen", 65)
pedido.confirmar()
print(json.dumps(pedido.serializar(), ensure_ascii=False, indent=2))
