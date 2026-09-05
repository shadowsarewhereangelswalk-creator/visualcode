import sys


CURSOS = (
    {"slug": "html", "nombre": "HTML", "nivel": "Inicial", "horas": 12},
    {"slug": "python", "nombre": "Python", "nivel": "Intermedio", "horas": 20},
    {"slug": "flask", "nombre": "Flask", "nivel": "Intermedio", "horas": 16},
)


if "--check" in sys.argv:
    assert len(CURSOS) == 3
    assert sum(curso["horas"] for curso in CURSOS) == 48
    print("UNE10D06 OK")
    raise SystemExit(0)


from flask import Flask, abort, render_template


app = Flask(__name__)


@app.get("/")
def inicio():
    return render_template("inicio.html", cursos=CURSOS)


@app.get("/curso/<slug>")
def detalle(slug):
    curso = next((item for item in CURSOS if item["slug"] == slug), None)
    if curso is None:
        abort(404)
    return render_template("detalle.html", curso=curso)


@app.errorhandler(404)
def no_encontrado(error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run()
