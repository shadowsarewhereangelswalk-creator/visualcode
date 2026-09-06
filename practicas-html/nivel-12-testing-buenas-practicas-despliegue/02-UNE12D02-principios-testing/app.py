import json
import sys

PRACTICA = "UNE12D02"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D02"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from src.service import RepositorioPedidos, procesar_compra

pedido = procesar_compra([{"precio": "12.50", "cantidad": 2}], RepositorioPedidos())
pedido["total"] = str(pedido["total"])
print(json.dumps(pedido, ensure_ascii=False, indent=2))
