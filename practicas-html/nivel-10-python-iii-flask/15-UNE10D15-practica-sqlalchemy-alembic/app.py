import os
import sys


ESTADOS = {"pendiente", "en_progreso", "completada"}


def validar_titulo(titulo):
    titulo = titulo.strip()
    return titulo if 3 <= len(titulo) <= 120 else ""


if "--check" in sys.argv:
    assert validar_titulo("Crear migración") == "Crear migración"
    assert not validar_titulo("x")
    assert len(ESTADOS) == 3
    print("UNE10D15 OK")
    raise SystemExit(0)


from flask import Flask, flash, redirect, render_template, request, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()


class Tarea(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(120))
    estado: Mapped[str] = mapped_column(String(20), default="pendiente")


def create_app():
    aplicacion = Flask(__name__)
    aplicacion.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "desarrollo-cambiar")
    aplicacion.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL", "sqlite:///tareas.db")
    aplicacion.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(aplicacion)
    migrate.init_app(aplicacion, db)

    @aplicacion.get("/")
    def inicio():
        estado = request.args.get("estado", "")
        consulta = db.select(Tarea).order_by(Tarea.id.desc())
        if estado in ESTADOS:
            consulta = consulta.where(Tarea.estado == estado)
        tareas = db.session.execute(consulta).scalars().all()
        return render_template("tareas.html", tareas=tareas, estados=ESTADOS, filtro=estado)

    @aplicacion.post("/tareas")
    def crear_tarea():
        titulo = validar_titulo(request.form.get("titulo", ""))
        if not titulo:
            flash("El título debe tener entre 3 y 120 caracteres.", "error")
            return redirect(url_for("inicio"))
        db.session.add(Tarea(titulo=titulo))
        db.session.commit()
        flash("Tarea creada.", "exito")
        return redirect(url_for("inicio"))

    @aplicacion.post("/tareas/<int:tarea_id>/estado")
    def cambiar_estado(tarea_id):
        tarea = db.get_or_404(Tarea, tarea_id)
        estado = request.form.get("estado", "")
        if estado not in ESTADOS:
            flash("Estado no válido.", "error")
            return redirect(url_for("inicio"))
        tarea.estado = estado
        db.session.commit()
        flash("Estado actualizado.", "exito")
        return redirect(url_for("inicio"))

    @aplicacion.post("/tareas/<int:tarea_id>/eliminar")
    def eliminar_tarea(tarea_id):
        tarea = db.get_or_404(Tarea, tarea_id)
        db.session.delete(tarea)
        db.session.commit()
        flash("Tarea eliminada.", "exito")
        return redirect(url_for("inicio"))

    return aplicacion


app = create_app()


if __name__ == "__main__":
    app.run()
