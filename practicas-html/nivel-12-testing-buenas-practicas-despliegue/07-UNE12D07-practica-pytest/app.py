import json
import sys

PRACTICA = "UNE12D07"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D07"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from validaciones import calcular_progreso, validar_usuario

print(
    json.dumps(
        {
            "usuario": validar_usuario("Karen", "karen@example.com", 30),
            "progreso": calcular_progreso(7, 10),
        },
        indent=2,
    )
)
