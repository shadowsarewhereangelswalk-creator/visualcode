from flask import Blueprint, jsonify


principal = Blueprint("principal", __name__)


@principal.get("/")
def inicio():
    return {
        "aplicacion": "Servicio Flask",
        "estado": "activo",
        "estructura": "application factory y blueprint",
    }


@principal.get("/salud")
def salud():
    return jsonify(estado="ok")
