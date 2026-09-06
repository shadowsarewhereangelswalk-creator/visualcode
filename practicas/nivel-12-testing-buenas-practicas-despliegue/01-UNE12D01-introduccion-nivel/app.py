import json
import sys

PRACTICA = "UNE12D01"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D01"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from src.quality import evaluar_pipeline

resultado = evaluar_pipeline(
    {"tests": True, "lint": True, "format": True, "coverage": True, "build": True}
)
print(json.dumps(resultado, ensure_ascii=False, indent=2))
