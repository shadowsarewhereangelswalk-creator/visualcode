import json
import sys

PRACTICA = "UNE12D13"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D13"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from src.report import crear_reporte

reporte = crear_reporte(
    [
        {"categoria": "Cursos", "total": "20.00"},
        {"categoria": "Cursos", "total": "35.50"},
        {"categoria": "Libros", "total": "15.00"},
    ]
)
reporte["total"] = str(reporte["total"])
print(json.dumps(reporte, ensure_ascii=False, indent=2))
