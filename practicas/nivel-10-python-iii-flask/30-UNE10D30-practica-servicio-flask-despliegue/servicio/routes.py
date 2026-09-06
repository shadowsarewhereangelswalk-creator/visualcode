from flask import Blueprint, flash, jsonify, redirect, render_template, request, url_for
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from . import db
from .models import Solicitud


SERVICIOS = {
    "desarrollo-web": "Desarrollo web",
    "automatizacion": "Automatización",
    "datos": "Análisis de datos",
    "ia": "Solución con IA",
}
ESTADOS = {"nueva", "contactada", "en_progreso", "cerrada"}
principal = Blueprint("principal", __name__)
api = Blueprint("api", __name__)


def validar_solicitud(datos):
    limpio = {
        "nombre": str(datos.get("nombre", "")).strip(),
        "correo": str(datos.get("correo", "")).strip().lower(),
        "servicio": str(datos.get("servicio", "")).strip(),
        "mensaje": str(datos.get("mensaje", "")).strip(),
    }
    errores = {}
    if not 2 <= len(limpio["nombre"]) <= 80:
        errores["nombre"] = "El nombre debe tener entre 2 y 80 caracteres."
    if "@" not in limpio["correo"] or len(limpio["correo"]) > 120:
        errores["correo"] = "El correo no es válido."
    if limpio["servicio"] not in SERVICIOS:
        errores["servicio"] = "Selecciona un servicio."
    if not 10 <= len(limpio["mensaje"]) <= 2000:
        errores["mensaje"] = "El mensaje debe tener entre 10 y 2000 caracteres."
    return limpio, errores


@principal.route("/", methods=["GET", "POST"])
def inicio():
    datos = request.form.to_dict() if request.method == "POST" else {}
    errores = {}
    if request.method == "POST":
        limpio, errores = validar_solicitud(datos)
        if not errores:
            db.session.add(Solicitud(**limpio))
            db.session.commit()
            flash("Solicitud enviada correctamente.", "exito")
            return redirect(url_for("principal.inicio"))
    return render_template("inicio.html", datos=datos, errores=errores, servicios=SERVICIOS)


@principal.get("/solicitudes")
def solicitudes():
    estado = request.args.get("estado", "")
    consulta = db.select(Solicitud).order_by(Solicitud.id.desc())
    if estado in ESTADOS:
        consulta = consulta.where(Solicitud.estado == estado)
    registros = db.session.execute(consulta).scalars().all()
    return render_template("solicitudes.html", solicitudes=registros, estados=ESTADOS, filtro=estado)


@principal.post("/solicitudes/<int:solicitud_id>/estado")
def cambiar_estado(solicitud_id):
    solicitud = db.get_or_404(Solicitud, solicitud_id)
    estado = request.form.get("estado", "")
    if estado in ESTADOS:
        solicitud.estado = estado
        db.session.commit()
        flash("Estado actualizado.", "exito")
    else:
        flash("El estado no es válido.", "error")
    return redirect(url_for("principal.solicitudes"))


@principal.get("/salud")
def salud():
    try:
        db.session.execute(text("SELECT 1"))
    except SQLAlchemyError:
        return {"estado": "error", "base_datos": "no disponible"}, 503
    return {"estado": "ok", "base_datos": "disponible"}


@api.get("/solicitudes")
def api_listar():
    estado = request.args.get("estado", "")
    limite = request.args.get("limite", 20, type=int)
    if not 1 <= limite <= 100:
        return {"error": "limite debe estar entre 1 y 100"}, 400
    consulta = db.select(Solicitud).order_by(Solicitud.id.desc()).limit(limite)
    if estado in ESTADOS:
        consulta = consulta.where(Solicitud.estado == estado)
    registros = db.session.execute(consulta).scalars().all()
    return {"datos": [solicitud.to_dict() for solicitud in registros], "total": len(registros)}


@api.post("/solicitudes")
def api_crear():
    datos = request.get_json(silent=True) or {}
    limpio, errores = validar_solicitud(datos)
    if errores:
        return {"error": {"codigo": "datos_invalidos", "campos": errores}}, 422
    solicitud = Solicitud(**limpio)
    db.session.add(solicitud)
    db.session.commit()
    respuesta = jsonify(solicitud.to_dict())
    respuesta.status_code = 201
    respuesta.headers["Location"] = url_for("api.api_obtener", solicitud_id=solicitud.id, _external=True)
    return respuesta


@api.get("/solicitudes/<int:solicitud_id>")
def api_obtener(solicitud_id):
    return db.get_or_404(Solicitud, solicitud_id).to_dict()


@api.patch("/solicitudes/<int:solicitud_id>")
def api_actualizar(solicitud_id):
    solicitud = db.get_or_404(Solicitud, solicitud_id)
    datos = request.get_json(silent=True) or {}
    if set(datos) != {"estado"} or datos["estado"] not in ESTADOS:
        return {"error": {"codigo": "estado_invalido", "mensaje": "Envía un estado permitido"}}, 422
    solicitud.estado = datos["estado"]
    db.session.commit()
    return solicitud.to_dict()


@api.delete("/solicitudes/<int:solicitud_id>")
def api_eliminar(solicitud_id):
    solicitud = db.get_or_404(Solicitud, solicitud_id)
    db.session.delete(solicitud)
    db.session.commit()
    return "", 204
