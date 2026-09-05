import sys


SERVICIOS = {
    1: {"nombre": "Landing page", "precio": 450},
    2: {"nombre": "Automatización", "precio": 780},
    3: {"nombre": "Asistente virtual", "precio": 950},
}


if "--check" in sys.argv:
    assert SERVICIOS[2]["precio"] == 780
    print("UNE10D04 OK")
    raise SystemExit(0)


from flask import Flask, abort, jsonify, request
from markupsafe import escape


app = Flask(__name__)


@app.get("/")
def inicio():
    return {
        "mensaje": "Rutas y vistas en Flask",
        "rutas": ["/saludo/<nombre>", "/servicios", "/servicios/<id>", "/cotizacion"],
    }


@app.get("/saludo/<nombre>")
def saludo(nombre):
    return f"<h1>Hola, {escape(nombre)}</h1>"


@app.get("/servicios")
def servicios():
    limite = request.args.get("limite", type=int)
    datos = [{"id": identificador, **servicio} for identificador, servicio in SERVICIOS.items()]
    return jsonify(datos[:limite] if limite else datos)


@app.get("/servicios/<int:identificador>")
def servicio(identificador):
    encontrado = SERVICIOS.get(identificador)
    if encontrado is None:
        abort(404)
    return {"id": identificador, **encontrado}


@app.post("/cotizacion")
def cotizacion():
    datos = request.get_json(silent=True) or {}
    identificador = datos.get("servicio_id")
    cantidad = datos.get("cantidad", 1)
    if identificador not in SERVICIOS or not isinstance(cantidad, int) or cantidad <= 0:
        return {"error": "Datos inválidos"}, 400
    seleccionado = SERVICIOS[identificador]
    return {
        "servicio": seleccionado["nombre"],
        "cantidad": cantidad,
        "total": seleccionado["precio"] * cantidad,
    }, 201


@app.errorhandler(404)
def no_encontrado(error):
    return {"error": "Recurso no encontrado"}, 404


if __name__ == "__main__":
    app.run()
