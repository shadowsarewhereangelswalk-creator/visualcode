import sys


def calcular(operacion, a, b):
    if operacion == "sumar":
        return a + b
    if operacion == "restar":
        return a - b
    if operacion == "multiplicar":
        return a * b
    if operacion == "dividir" and b != 0:
        return a / b
    raise ValueError("Operación no válida")


if "--check" in sys.argv:
    assert calcular("sumar", 4, 5) == 9
    assert calcular("dividir", 8, 2) == 4
    print("UNE10D25 OK")
    raise SystemExit(0)


from flask import Flask, request


def create_app(configuracion=None):
    aplicacion = Flask(__name__)
    aplicacion.config.from_mapping(TESTING=False, API_KEY="clave-desarrollo")
    if configuracion:
        aplicacion.config.update(configuracion)

    @aplicacion.get("/salud")
    def salud():
        return {"estado": "ok"}

    @aplicacion.post("/api/calcular")
    def api_calcular():
        if request.headers.get("X-API-Key") != aplicacion.config["API_KEY"]:
            return {"error": "No autorizado"}, 401
        datos = request.get_json(silent=True) or {}
        operacion = datos.get("operacion")
        a = datos.get("a")
        b = datos.get("b")
        if not isinstance(a, (int, float)) or isinstance(a, bool) or not isinstance(b, (int, float)) or isinstance(b, bool):
            return {"error": "a y b deben ser números"}, 422
        try:
            resultado = calcular(operacion, a, b)
        except ValueError as error:
            return {"error": str(error)}, 422
        return {"operacion": operacion, "a": a, "b": b, "resultado": resultado}

    return aplicacion


app = create_app()


if __name__ == "__main__":
    app.run()
