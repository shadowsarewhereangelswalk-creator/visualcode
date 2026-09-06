import sys


CATALOGO = (
    {"slug": "landing-page", "nombre": "Landing page", "categoria": "web", "precio": 450},
    {"slug": "automatizacion", "nombre": "Automatización", "categoria": "python", "precio": 780},
    {"slug": "asistente-virtual", "nombre": "Asistente virtual", "categoria": "ia", "precio": 950},
    {"slug": "auditoria-seo", "nombre": "Auditoría SEO", "categoria": "marketing", "precio": 520},
)


def buscar_servicio(slug):
    return next((servicio for servicio in CATALOGO if servicio["slug"] == slug), None)


if "--check" in sys.argv:
    assert buscar_servicio("automatizacion")["precio"] == 780
    assert buscar_servicio("inexistente") is None
    print("UNE10D05 OK")
    raise SystemExit(0)


from flask import Flask, abort, request, url_for


app = Flask(__name__)


@app.get("/")
def inicio():
    return {
        "nombre": "Catálogo de servicios",
        "enlaces": {
            servicio["nombre"]: url_for("detalle", slug=servicio["slug"])
            for servicio in CATALOGO
        },
    }


@app.get("/catalogo")
def catalogo():
    categoria = request.args.get("categoria", "").strip().lower()
    precio_maximo = request.args.get("precio_maximo", type=float)
    resultados = list(CATALOGO)
    if categoria:
        resultados = [servicio for servicio in resultados if servicio["categoria"] == categoria]
    if precio_maximo is not None:
        resultados = [servicio for servicio in resultados if servicio["precio"] <= precio_maximo]
    return {"total": len(resultados), "resultados": resultados}


@app.get("/catalogo/<slug>")
def detalle(slug):
    servicio = buscar_servicio(slug)
    if servicio is None:
        abort(404)
    return servicio


@app.post("/catalogo/<slug>/cotizar")
def cotizar(slug):
    servicio = buscar_servicio(slug)
    if servicio is None:
        abort(404)
    datos = request.get_json(silent=True) or {}
    unidades = datos.get("unidades", 1)
    if not isinstance(unidades, int) or unidades < 1:
        return {"error": "Las unidades deben ser un entero positivo"}, 422
    return {
        "servicio": servicio["nombre"],
        "unidades": unidades,
        "total": servicio["precio"] * unidades,
    }, 201


@app.errorhandler(404)
def no_encontrado(error):
    return {"error": "Servicio no encontrado"}, 404


if __name__ == "__main__":
    app.run()
