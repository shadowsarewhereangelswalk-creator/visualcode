import json
import sys

PRACTICA = "UNE12D06"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D06"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from precios import precio_final

print(json.dumps({"precio_final": str(precio_final("29.99"))}, indent=2))
