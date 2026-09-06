import json
import sys

PRACTICA = "UNE12D04"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D04"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from calculadora import dividir, promedio, sumar

print(
    json.dumps(
        {"suma": sumar(8, 4), "division": dividir(8, 4), "promedio": promedio([4, 8])},
        indent=2,
    )
)
