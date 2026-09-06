import json
import sys

PRACTICA = "UNE12D10"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D10"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from clima import obtener_recomendacion


class ClienteDemo:
    def consultar(self, ciudad):
        return {"temperatura": 30}


print(
    json.dumps(
        obtener_recomendacion("Caracas", ClienteDemo()),
        ensure_ascii=False,
        indent=2,
    )
)
