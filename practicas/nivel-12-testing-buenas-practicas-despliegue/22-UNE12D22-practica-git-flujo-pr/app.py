import json
import sys
from tempfile import TemporaryDirectory

PRACTICA = "UNE12D22"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D22"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from workflow import aprobar_y_fusionar, preparar_repositorio, revisar_cambios

with TemporaryDirectory() as directorio:
    repositorio = preparar_repositorio(directorio)
    resultado = revisar_cambios(repositorio)
    resultado["merge"] = aprobar_y_fusionar(repositorio)
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
