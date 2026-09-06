import sys
from pathlib import Path


RUTA_SRC = Path(__file__).parent / "src"
sys.path.insert(0, str(RUTA_SRC))

from career_service_kit import crear_respuesta, pagina_valida


if "--check" in sys.argv:
    assert crear_respuesta([1, 2], total=2)["meta"]["total"] == 2
    assert pagina_valida(1, 20)
    assert not pagina_valida(0, 20)
    print("UNE10D27 OK")
    raise SystemExit(0)


from flask import Flask, request


app = Flask(__name__)
ELEMENTOS = [{"id": numero, "nombre": f"Recurso {numero}"} for numero in range(1, 26)]


@app.get("/")
def inicio():
    pagina = request.args.get("pagina", 1, type=int)
    por_pagina = request.args.get("por_pagina", 5, type=int)
    if not pagina_valida(pagina, por_pagina):
        return {"error": "Paginación no válida"}, 400
    inicio = (pagina - 1) * por_pagina
    datos = ELEMENTOS[inicio:inicio + por_pagina]
    return crear_respuesta(datos, total=len(ELEMENTOS), pagina=pagina, por_pagina=por_pagina)


if __name__ == "__main__":
    app.run()
