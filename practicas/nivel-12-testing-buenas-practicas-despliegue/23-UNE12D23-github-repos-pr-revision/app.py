import json
import sys

PRACTICA = "UNE12D23"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D23"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from review import validar_pull_request

resultado = validar_pull_request(
    {
        "titulo": "Agrega validación de usuarios",
        "descripcion": "Implementa validaciones y pruebas para el registro.",
        "pruebas_aprobadas": True,
        "revisor": "equipo-calidad",
        "autor": "estudiante",
        "rama_base": "main",
    }
)
print(json.dumps(resultado, ensure_ascii=False, indent=2))
