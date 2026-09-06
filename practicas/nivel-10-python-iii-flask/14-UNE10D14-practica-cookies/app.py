import sys


IDIOMAS = {"es": "Español", "en": "English"}
TEMAS = {"claro": {"fondo": "#f8fafc", "texto": "#0f172a", "acento": "#0369a1"}, "oscuro": {"fondo": "#0f172a", "texto": "#f8fafc", "acento": "#38bdf8"}}
TEXTOS = {
    "es": {"titulo": "Tu espacio de aprendizaje", "mensaje": "Tus preferencias se guardan en cookies.", "guardar": "Guardar preferencias"},
    "en": {"titulo": "Your learning space", "mensaje": "Your preferences are stored in cookies.", "guardar": "Save preferences"},
}


def normalizar_preferencias(tema, idioma):
    return tema if tema in TEMAS else "claro", idioma if idioma in IDIOMAS else "es"


if "--check" in sys.argv:
    assert normalizar_preferencias("oscuro", "en") == ("oscuro", "en")
    assert normalizar_preferencias("otro", "fr") == ("claro", "es")
    print("UNE10D14 OK")
    raise SystemExit(0)


from flask import Flask, make_response, redirect, render_template, request, url_for


app = Flask(__name__)


@app.get("/")
def inicio():
    tema, idioma = normalizar_preferencias(request.cookies.get("tema", "claro"), request.cookies.get("idioma", "es"))
    return render_template("inicio.html", tema=tema, idioma=idioma, estilos=TEMAS[tema], textos=TEXTOS[idioma], idiomas=IDIOMAS, temas=TEMAS)


@app.post("/preferencias")
def preferencias():
    tema, idioma = normalizar_preferencias(request.form.get("tema", ""), request.form.get("idioma", ""))
    respuesta = make_response(redirect(url_for("inicio")))
    configuracion = {"max_age": 60 * 60 * 24 * 365, "samesite": "Lax", "httponly": True}
    respuesta.set_cookie("tema", tema, **configuracion)
    respuesta.set_cookie("idioma", idioma, **configuracion)
    return respuesta


@app.post("/preferencias/restablecer")
def restablecer():
    respuesta = make_response(redirect(url_for("inicio")))
    respuesta.delete_cookie("tema")
    respuesta.delete_cookie("idioma")
    return respuesta


if __name__ == "__main__":
    app.run()
