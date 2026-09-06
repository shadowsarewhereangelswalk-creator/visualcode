import json
import sys

PRACTICA = "UNE12D19"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D19"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from src.diagnostic import diagnosticar

print(json.dumps(diagnosticar(["pytest"]), ensure_ascii=False, indent=2))
