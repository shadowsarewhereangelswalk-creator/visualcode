from flask import Blueprint, render_template


web = Blueprint("web", __name__)


@web.get("/")
def inicio():
    servicios = (
        {"nombre": "Aplicaciones web", "estado": "Disponible"},
        {"nombre": "Automatizaciones", "estado": "Disponible"},
        {"nombre": "APIs", "estado": "En preparación"},
    )
    return render_template("index.html", servicios=servicios)
