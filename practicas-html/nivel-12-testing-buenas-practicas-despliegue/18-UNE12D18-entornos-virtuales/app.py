import json
import sys

PRACTICA = "UNE12D18"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D18"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from environment import informacion_entorno, validar_version

validar_version()
print(json.dumps(informacion_entorno(), ensure_ascii=False, indent=2))
