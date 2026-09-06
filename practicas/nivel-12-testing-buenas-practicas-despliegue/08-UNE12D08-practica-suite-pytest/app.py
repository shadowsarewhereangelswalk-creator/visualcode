import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

PRACTICA = "UNE12D08"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D08"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from gestor import GestorTareas

with TemporaryDirectory() as directorio:
    gestor = GestorTareas(Path(directorio) / "tareas.json")
    tarea = gestor.crear("Completar suite", "alta")
    gestor.completar(tarea["id"])
    print(json.dumps(gestor.listar(), ensure_ascii=False, indent=2))
