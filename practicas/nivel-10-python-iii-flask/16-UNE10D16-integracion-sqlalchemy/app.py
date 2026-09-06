import os
import sys


def normalizar_etiqueta(valor):
    return valor.strip().lower()[:30]


if "--check" in sys.argv:
    assert normalizar_etiqueta("  Flask  ") == "flask"
    assert normalizar_etiqueta("x" * 50) == "x" * 30
    print("UNE10D16 OK")
    raise SystemExit(0)


from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Nota(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    texto: Mapped[str] = mapped_column(String(240))
    etiqueta: Mapped[str] = mapped_column(String(30), index=True)

    def to_dict(self):
        return {"id": self.id, "texto": self.texto, "etiqueta": self.etiqueta}


def create_app(configuracion=None):
    aplicacion = Flask(__name__)
    aplicacion.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", "sqlite:///notas.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    if configuracion:
        aplicacion.config.update(configuracion)
    db.init_app(aplicacion)

    @aplicacion.cli.command("crear-db")
    def crear_db():
        db.create_all()
        print("Base de datos creada")

    @aplicacion.get("/")
    def inicio():
        return {"servicio": "Notas", "rutas": ["GET /notas", "POST /notas"]}

    @aplicacion.get("/notas")
    def listar_notas():
        etiqueta = normalizar_etiqueta(request.args.get("etiqueta", ""))
        consulta = db.select(Nota).order_by(Nota.id.desc())
        if etiqueta:
            consulta = consulta.where(Nota.etiqueta == etiqueta)
        notas = db.session.execute(consulta).scalars().all()
        return jsonify([nota.to_dict() for nota in notas])

    @aplicacion.post("/notas")
    def crear_nota():
        datos = request.get_json(silent=True) or {}
        texto = str(datos.get("texto", "")).strip()
        etiqueta = normalizar_etiqueta(str(datos.get("etiqueta", "general"))) or "general"
        if not 3 <= len(texto) <= 240:
            return {"error": "El texto debe tener entre 3 y 240 caracteres"}, 422
        nota = Nota(texto=texto, etiqueta=etiqueta)
        db.session.add(nota)
        db.session.commit()
        return nota.to_dict(), 201

    return aplicacion


app = create_app()


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
