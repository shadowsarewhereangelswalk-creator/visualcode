import os
import sys


def validar_titulo(valor):
    titulo = str(valor).strip()
    return titulo if 3 <= len(titulo) <= 120 else ""


def convertir_booleano(valor):
    return valor if isinstance(valor, bool) else None


if "--check" in sys.argv:
    assert validar_titulo("Crear API") == "Crear API"
    assert not validar_titulo("x")
    assert convertir_booleano(False) is False
    assert convertir_booleano("false") is None
    print("UNE10D22 OK")
    raise SystemExit(0)


from flask import Flask, jsonify, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Tarea(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(120))
    completada: Mapped[bool] = mapped_column(Boolean, default=False)

    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "completada": self.completada}


def create_app(configuracion=None):
    aplicacion = Flask(__name__)
    aplicacion.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", "sqlite:///api_tareas.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if configuracion:
        aplicacion.config.update(configuracion)
    db.init_app(aplicacion)

    @aplicacion.get("/api/tareas")
    def listar_tareas():
        consulta = db.select(Tarea).order_by(Tarea.id)
        completada = request.args.get("completada", "")
        if completada in {"true", "false"}:
            consulta = consulta.where(Tarea.completada.is_(completada == "true"))
        tareas = db.session.execute(consulta).scalars().all()
        return {"datos": [tarea.to_dict() for tarea in tareas], "total": len(tareas)}

    @aplicacion.post("/api/tareas")
    def crear_tarea():
        datos = request.get_json(silent=True) or {}
        titulo = validar_titulo(datos.get("titulo", ""))
        if not titulo:
            return {"error": {"codigo": "datos_invalidos", "mensaje": "El título debe tener entre 3 y 120 caracteres"}}, 422
        tarea = Tarea(titulo=titulo)
        db.session.add(tarea)
        db.session.commit()
        respuesta = jsonify(tarea.to_dict())
        respuesta.status_code = 201
        respuesta.headers["Location"] = url_for("obtener_tarea", tarea_id=tarea.id, _external=True)
        return respuesta

    @aplicacion.get("/api/tareas/<int:tarea_id>")
    def obtener_tarea(tarea_id):
        return db.get_or_404(Tarea, tarea_id).to_dict()

    @aplicacion.patch("/api/tareas/<int:tarea_id>")
    def actualizar_tarea(tarea_id):
        tarea = db.get_or_404(Tarea, tarea_id)
        datos = request.get_json(silent=True) or {}
        if not datos or not set(datos).issubset({"titulo", "completada"}):
            return {"error": {"codigo": "campos_invalidos", "mensaje": "Envía título o completada"}}, 422
        if "titulo" in datos:
            titulo = validar_titulo(datos["titulo"])
            if not titulo:
                return {"error": {"codigo": "titulo_invalido", "mensaje": "El título no es válido"}}, 422
            tarea.titulo = titulo
        if "completada" in datos:
            completada = convertir_booleano(datos["completada"])
            if completada is None:
                return {"error": {"codigo": "tipo_invalido", "mensaje": "completada debe ser booleano"}}, 422
            tarea.completada = completada
        db.session.commit()
        return tarea.to_dict()

    @aplicacion.delete("/api/tareas/<int:tarea_id>")
    def eliminar_tarea(tarea_id):
        tarea = db.get_or_404(Tarea, tarea_id)
        db.session.delete(tarea)
        db.session.commit()
        return "", 204

    @aplicacion.errorhandler(404)
    def no_encontrado(error):
        return {"error": {"codigo": "no_encontrado", "mensaje": "Recurso no encontrado"}}, 404

    @aplicacion.errorhandler(405)
    def metodo_no_permitido(error):
        return {"error": {"codigo": "metodo_no_permitido", "mensaje": "Método no permitido"}}, 405

    return aplicacion


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
