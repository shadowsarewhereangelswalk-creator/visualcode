import json
import sys

from src.converter import convertir

PRACTICA = "UNE12D15"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D15"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


print(json.dumps({"resultado": str(convertir("100", "USD", "EUR"))}, indent=2))
