import json
import sys

PRACTICA = "UNE12D05"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D05"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from banco import Cuenta

cuenta = Cuenta("Karen", 100)
cuenta.depositar(25)
cuenta.retirar(40)
print(json.dumps({"titular": cuenta.titular, "saldo": str(cuenta.saldo)}, indent=2))
