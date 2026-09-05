from flask import Blueprint


def crear_blueprint_salud(nombre_servicio, version="1.0.0", url_prefix=""):
    blueprint = Blueprint("career_health", __name__, url_prefix=url_prefix)

    @blueprint.get("/salud")
    def salud():
        return {"estado": "ok", "servicio": nombre_servicio, "version": version}

    return blueprint
