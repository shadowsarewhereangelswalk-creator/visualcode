import json
import sys
from tempfile import TemporaryDirectory

PRACTICA = "UNE12D21"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D21"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from repository import crear_flujo

with TemporaryDirectory() as directorio:
    print(json.dumps(crear_flujo(directorio), ensure_ascii=False, indent=2))
