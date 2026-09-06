import math
import sys
from datetime import date


EVENTOS = (
    {"id": 1, "nombre": "Python Meetup", "categoria": "tecnologia", "fecha": "2027-04-09", "cupos": 80},
    {"id": 2, "nombre": "Taller de portafolio", "categoria": "carrera", "fecha": "2027-04-12", "cupos": 24},
    {"id": 3, "nombre": "Datos para negocios", "categoria": "datos", "fecha": "2027-04-18", "cupos": 45},
    {"id": 4, "nombre": "Flask en producción", "categoria": "tecnologia", "fecha": "2027-04-23", "cupos": 60},
    {"id": 5, "nombre": "Simulación de entrevista", "categoria": "carrera", "fecha": "2027-04-27", "cupos": 16},
)


def paginar(elementos, pagina, por_pagina):
    inicio = (pagina - 1) * por_pagina
    return elementos[inicio:inicio + por_pagina], math.ceil(len(elementos) / por_pagina)


if "--check" in sys.argv:
    elementos, paginas = paginar(EVENTOS, 2, 2)
    assert [evento["id"] for evento in elementos] == [3, 4]
    assert paginas == 3
    print("UNE10D23 OK")
    raise SystemExit(0)


from flask import Flask, jsonify, request, url_for


app = Flask(__name__)


@app.get("/")
def inicio():
    return {"servicio": "Agenda de eventos", "documentacion": url_for("especificacion", _external=True)}


@app.get("/api/eventos")
def listar_eventos():
    pagina = request.args.get("pagina", 1, type=int)
    por_pagina = request.args.get("por_pagina", 3, type=int)
    if pagina < 1 or not 1 <= por_pagina <= 20:
        return {"error": {"codigo": "paginacion_invalida", "mensaje": "Usa página positiva y entre 1 y 20 resultados"}}, 400
    categoria = request.args.get("categoria", "").strip().lower()
    busqueda = request.args.get("q", "").strip().lower()
    orden = request.args.get("orden", "fecha")
    if orden not in {"fecha", "nombre", "cupos"}:
        return {"error": {"codigo": "orden_invalido", "mensaje": "El orden debe ser fecha, nombre o cupos"}}, 400
    resultados = list(EVENTOS)
    if categoria:
        resultados = [evento for evento in resultados if evento["categoria"] == categoria]
    if busqueda:
        resultados = [evento for evento in resultados if busqueda in evento["nombre"].lower()]
    resultados.sort(key=lambda evento: evento[orden])
    datos, total_paginas = paginar(resultados, pagina, por_pagina)
    return {
        "datos": datos,
        "meta": {"pagina": pagina, "por_pagina": por_pagina, "total": len(resultados), "total_paginas": total_paginas},
        "enlaces": {
            "actual": url_for("listar_eventos", pagina=pagina, por_pagina=por_pagina, categoria=categoria or None, q=busqueda or None, orden=orden, _external=True),
            "siguiente": url_for("listar_eventos", pagina=pagina + 1, por_pagina=por_pagina, categoria=categoria or None, q=busqueda or None, orden=orden, _external=True) if pagina < total_paginas else None,
        },
    }


@app.get("/api/eventos/<int:evento_id>")
def obtener_evento(evento_id):
    evento = next((item for item in EVENTOS if item["id"] == evento_id), None)
    if evento is None:
        return {"error": {"codigo": "evento_no_encontrado", "mensaje": "El evento no existe"}}, 404
    return evento


@app.post("/api/eventos/<int:evento_id>/inscripciones")
def inscribir(evento_id):
    evento = next((item for item in EVENTOS if item["id"] == evento_id), None)
    if evento is None:
        return {"error": {"codigo": "evento_no_encontrado", "mensaje": "El evento no existe"}}, 404
    if not request.is_json:
        return {"error": {"codigo": "tipo_no_admitido", "mensaje": "El cuerpo debe usar application/json"}}, 415
    datos = request.get_json(silent=True) or {}
    nombre = str(datos.get("nombre", "")).strip()
    correo = str(datos.get("correo", "")).strip().lower()
    if len(nombre) < 2 or "@" not in correo:
        return {"error": {"codigo": "datos_invalidos", "mensaje": "Nombre y correo son obligatorios"}}, 422
    inscripcion = {"id": f"{evento_id}-{date.today().isoformat()}-{correo}", "evento_id": evento_id, "nombre": nombre, "correo": correo}
    respuesta = jsonify(inscripcion)
    respuesta.status_code = 201
    respuesta.headers["Location"] = url_for("obtener_evento", evento_id=evento_id, _external=True)
    return respuesta


@app.get("/openapi.yaml")
def especificacion():
    return app.send_static_file("openapi.yaml")


@app.errorhandler(405)
def metodo_no_permitido(error):
    return {"error": {"codigo": "metodo_no_permitido", "mensaje": "El método HTTP no está habilitado"}}, 405


if __name__ == "__main__":
    app.run()
