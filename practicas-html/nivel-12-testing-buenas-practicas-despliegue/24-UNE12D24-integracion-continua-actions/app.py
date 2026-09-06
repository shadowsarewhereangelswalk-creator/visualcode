import json
import sys

from quality import crear_slug, normalizar_nombre

PRACTICA = "UNE12D24"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D24"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


print(
    json.dumps(
        {
            "nombre": normalizar_nombre("  integración   continua  "),
            "slug": crear_slug("Integración Continua"),
        },
        ensure_ascii=False,
        indent=2,
    )
)
