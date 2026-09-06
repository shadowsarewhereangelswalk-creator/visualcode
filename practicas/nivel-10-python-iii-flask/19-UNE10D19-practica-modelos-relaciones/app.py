import os
import sys


ESTADOS = {"planeado", "activo", "entregado"}


def validar_proyecto(nombre, presupuesto, estado):
    return 3 <= len(nombre.strip()) <= 100 and isinstance(presupuesto, int) and presupuesto >= 0 and estado in ESTADOS


if "--check" in sys.argv:
    assert validar_proyecto("Portal web", 1200, "activo")
    assert not validar_proyecto("x", -1, "otro")
    print("UNE10D19 OK")
    raise SystemExit(0)


from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Cliente(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80))
    correo: Mapped[str] = mapped_column(String(120), unique=True)
    proyectos: Mapped[list["Proyecto"]] = relationship(back_populates="cliente", cascade="all, delete-orphan")

    @property
    def presupuesto_total(self):
        return sum(proyecto.presupuesto for proyecto in self.proyectos)


class Proyecto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100))
    presupuesto: Mapped[int] = mapped_column(Integer)
    estado: Mapped[str] = mapped_column(String(20), default="planeado")
    cliente_id: Mapped[int] = mapped_column(ForeignKey("cliente.id"), index=True)
    cliente: Mapped[Cliente] = relationship(back_populates="proyectos")


app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY=os.environ.get("SECRET_KEY", "relaciones-local"),
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", "sqlite:///clientes.db"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)


@app.get("/")
def inicio():
    clientes = db.session.execute(db.select(Cliente).order_by(Cliente.nombre)).scalars().all()
    return render_template("clientes.html", clientes=clientes, estados=ESTADOS)


@app.post("/clientes")
def crear_cliente():
    nombre = request.form.get("nombre", "").strip()
    correo = request.form.get("correo", "").strip().lower()
    if len(nombre) < 2 or "@" not in correo:
        flash("El nombre o el correo no son válidos.", "error")
    elif db.session.scalar(db.select(Cliente).where(Cliente.correo == correo)):
        flash("Ya existe un cliente con ese correo.", "error")
    else:
        db.session.add(Cliente(nombre=nombre, correo=correo))
        db.session.commit()
        flash("Cliente creado.", "exito")
    return redirect(url_for("inicio"))


@app.post("/clientes/<int:cliente_id>/proyectos")
def crear_proyecto(cliente_id):
    cliente = db.get_or_404(Cliente, cliente_id)
    nombre = request.form.get("nombre", "").strip()
    presupuesto = request.form.get("presupuesto", type=int)
    estado = request.form.get("estado", "")
    if not validar_proyecto(nombre, presupuesto, estado):
        flash("Revisa los datos del proyecto.", "error")
    else:
        db.session.add(Proyecto(nombre=nombre, presupuesto=presupuesto, estado=estado, cliente=cliente))
        db.session.commit()
        flash("Proyecto agregado.", "exito")
    return redirect(url_for("inicio"))


@app.post("/proyectos/<int:proyecto_id>/estado")
def cambiar_estado(proyecto_id):
    proyecto = db.get_or_404(Proyecto, proyecto_id)
    estado = request.form.get("estado", "")
    if estado in ESTADOS:
        proyecto.estado = estado
        db.session.commit()
    return redirect(url_for("inicio"))


@app.post("/clientes/<int:cliente_id>/eliminar")
def eliminar_cliente(cliente_id):
    cliente = db.get_or_404(Cliente, cliente_id)
    db.session.delete(cliente)
    db.session.commit()
    flash("Cliente y sus proyectos fueron eliminados.", "exito")
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
