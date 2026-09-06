import json
import sys

PRACTICA = "UNE12D16"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D16"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from descuentos import calcular_descuento

resultado = calcular_descuento("120", "vip", "EXTRA5")
print(
    json.dumps(
        {clave: str(valor) for clave, valor in resultado.items()},
        ensure_ascii=False,
        indent=2,
    )
)
