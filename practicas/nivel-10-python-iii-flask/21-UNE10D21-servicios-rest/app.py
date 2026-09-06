import sys


LIBROS = {
    1: {"id": 1, "titulo": "Python práctico", "autor": "Ana Torres", "disponible": True},
    2: {"id": 2, "titulo": "Flask desde cero", "autor": "Luis Vega", "disponible": True},
}


def siguiente_id():
    return max(LIBROS, default=0) + 1


def validar_libro(datos):
    titulo = str(datos.get("titulo", "")).strip()
    autor = str(datos.get("autor", "")).strip()
    return (titulo, autor) if len(titulo) >= 2 and len(autor) >= 2 else None


if "--check" in sys.argv:
    assert siguiente_id() == 3
    assert validar_libro({"titulo": "Clean Code", "autor": "Robert Martin"})
    assert validar_libro({}) is None
    print("UNE10D21 OK")
    raise SystemExit(0)


from flask import Flask, jsonify, request, url_for


app = Flask(__name__)


@app.get("/")
def inicio():
    return {
        "servicio": "Biblioteca REST",
        "coleccion": url_for("listar_libros", _external=True),
    }


@app.get("/api/libros")
def listar_libros():
    disponible = request.args.get("disponible")
    libros = list(LIBROS.values())
    if disponible in {"true", "false"}:
        valor = disponible == "true"
        libros = [libro for libro in libros if libro["disponible"] is valor]
    return jsonify(datos=libros, total=len(libros))


@app.post("/api/libros")
def crear_libro():
    datos = request.get_json(silent=True) or {}
    campos = validar_libro(datos)
    if campos is None:
        return {"error": "Se requieren título y autor"}, 422
    libro_id = siguiente_id()
    LIBROS[libro_id] = {"id": libro_id, "titulo": campos[0], "autor": campos[1], "disponible": True}
    respuesta = jsonify(LIBROS[libro_id])
    respuesta.status_code = 201
    respuesta.headers["Location"] = url_for("obtener_libro", libro_id=libro_id, _external=True)
    return respuesta


@app.get("/api/libros/<int:libro_id>")
def obtener_libro(libro_id):
    libro = LIBROS.get(libro_id)
    if libro is None:
        return {"error": "Libro no encontrado"}, 404
    return libro


@app.patch("/api/libros/<int:libro_id>")
def actualizar_libro(libro_id):
    libro = LIBROS.get(libro_id)
    if libro is None:
        return {"error": "Libro no encontrado"}, 404
    datos = request.get_json(silent=True) or {}
    if "disponible" not in datos or not isinstance(datos["disponible"], bool):
        return {"error": "El campo disponible debe ser booleano"}, 422
    libro["disponible"] = datos["disponible"]
    return libro


@app.delete("/api/libros/<int:libro_id>")
def eliminar_libro(libro_id):
    if libro_id not in LIBROS:
        return {"error": "Libro no encontrado"}, 404
    del LIBROS[libro_id]
    return "", 204


@app.errorhandler(405)
def metodo_no_permitido(error):
    return {"error": "Método no permitido"}, 405


if __name__ == "__main__":
    app.run()
