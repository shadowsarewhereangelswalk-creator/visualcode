import os
import sys


PRIORIDADES = {"baja", "media", "alta"}


def datos_validos(titulo, prioridad):
    return 3 <= len(titulo.strip()) <= 100 and prioridad in PRIORIDADES


if "--check" in sys.argv:
    assert datos_validos("Estudiar Flask", "alta")
    assert not datos_validos("x", "urgente")
    print("UNE10D17 OK")
    raise SystemExit(0)


from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Pendiente(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(100))
    prioridad: Mapped[str] = mapped_column(String(10), default="media")
    completado: Mapped[bool] = mapped_column(Boolean, default=False)


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get("SECRET_KEY", "practica-local"),
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", "sqlite:///pendientes.db"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)


@app.get("/")
def inicio():
    consulta = db.select(Pendiente).order_by(Pendiente.completado, Pendiente.id.desc())
    pendientes = db.session.execute(consulta).scalars().all()
    return render_template("index.html", pendientes=pendientes, prioridades=PRIORIDADES)


@app.post("/pendientes")
def crear():
    titulo = request.form.get("titulo", "").strip()
    prioridad = request.form.get("prioridad", "")
    if not datos_validos(titulo, prioridad):
        flash("Revisa el título y la prioridad.", "error")
        return redirect(url_for("inicio"))
    db.session.add(Pendiente(titulo=titulo, prioridad=prioridad))
    db.session.commit()
    flash("Pendiente creado.", "exito")
    return redirect(url_for("inicio"))


@app.post("/pendientes/<int:pendiente_id>/alternar")
def alternar(pendiente_id):
    pendiente = db.get_or_404(Pendiente, pendiente_id)
    pendiente.completado = not pendiente.completado
    db.session.commit()
    return redirect(url_for("inicio"))


@app.post("/pendientes/<int:pendiente_id>/editar")
def editar(pendiente_id):
    pendiente = db.get_or_404(Pendiente, pendiente_id)
    titulo = request.form.get("titulo", "").strip()
    prioridad = request.form.get("prioridad", "")
    if not datos_validos(titulo, prioridad):
        flash("No se pudo actualizar el pendiente.", "error")
        return redirect(url_for("inicio"))
    pendiente.titulo = titulo
    pendiente.prioridad = prioridad
    db.session.commit()
    flash("Pendiente actualizado.", "exito")
    return redirect(url_for("inicio"))


@app.post("/pendientes/<int:pendiente_id>/eliminar")
def eliminar(pendiente_id):
    pendiente = db.get_or_404(Pendiente, pendiente_id)
    db.session.delete(pendiente)
    db.session.commit()
    flash("Pendiente eliminado.", "exito")
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
