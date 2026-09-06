import json
import sys

PRACTICA = "UNE12D20"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D20"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from dependencies import crear_informe, leer_dependencias

print(
    json.dumps(
        crear_informe(leer_dependencias("requirements.txt")),
        ensure_ascii=False,
        indent=2,
    )
)
