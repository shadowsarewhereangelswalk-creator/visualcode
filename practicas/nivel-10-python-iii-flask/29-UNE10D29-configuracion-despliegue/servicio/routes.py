import os
from datetime import datetime, timezone

from flask import Blueprint, current_app


principal = Blueprint("principal", __name__)


@principal.get("/")
def inicio():
    return {
        "servicio": "Flask desplegable",
        "entorno": current_app.config.get("ENV", "production"),
        "version": os.environ.get("APP_VERSION", "1.0.0"),
    }


@principal.get("/salud")
def salud():
    return {"estado": "ok", "hora": datetime.now(timezone.utc).isoformat()}


@principal.get("/preparado")
def preparado():
    return {"estado": "ready"}
