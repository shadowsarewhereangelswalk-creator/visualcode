import os
import sys


def texto_valido(valor, minimo=2, maximo=120):
    return minimo <= len(str(valor).strip()) <= maximo


if "--check" in sys.argv:
    assert texto_valido("Flask")
    assert not texto_valido("")
    assert not texto_valido("x" * 121)
    print("UNE10D18 OK")
    raise SystemExit(0)


from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class Autor(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(80), unique=True)
    articulos: Mapped[list["Articulo"]] = relationship(back_populates="autor", cascade="all, delete-orphan")

    def to_dict(self, incluir_articulos=False):
        datos = {"id": self.id, "nombre": self.nombre, "total_articulos": len(self.articulos)}
        if incluir_articulos:
            datos["articulos"] = [articulo.to_dict() for articulo in self.articulos]
        return datos


class Articulo(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(120))
    contenido: Mapped[str] = mapped_column(Text)
    autor_id: Mapped[int] = mapped_column(ForeignKey("autor.id"), index=True)
    autor: Mapped[Autor] = relationship(back_populates="articulos")

    def to_dict(self):
        return {"id": self.id, "titulo": self.titulo, "contenido": self.contenido, "autor_id": self.autor_id}


app = Flask(__name__)
app.config.from_mapping(
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", "sqlite:///blog.db"),
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)
db.init_app(app)


@app.get("/")
def inicio():
    return {"proyecto": "Blog relacional", "relacion": "Autor 1:N Articulo"}


@app.get("/autores")
def listar_autores():
    autores = db.session.execute(db.select(Autor).order_by(Autor.nombre)).scalars().all()
    return {"autores": [autor.to_dict(incluir_articulos=True) for autor in autores]}


@app.post("/autores")
def crear_autor():
    datos = request.get_json(silent=True) or {}
    nombre = str(datos.get("nombre", "")).strip()
    if not texto_valido(nombre, 2, 80):
        return {"error": "El nombre debe tener entre 2 y 80 caracteres"}, 422
    if db.session.scalar(db.select(Autor).where(Autor.nombre == nombre)):
        return {"error": "El autor ya existe"}, 409
    autor = Autor(nombre=nombre)
    db.session.add(autor)
    db.session.commit()
    return autor.to_dict(), 201


@app.post("/autores/<int:autor_id>/articulos")
def crear_articulo(autor_id):
    autor = db.get_or_404(Autor, autor_id)
    datos = request.get_json(silent=True) or {}
    titulo = str(datos.get("titulo", "")).strip()
    contenido = str(datos.get("contenido", "")).strip()
    if not texto_valido(titulo, 3, 120) or not texto_valido(contenido, 10, 5000):
        return {"error": "El título o el contenido no son válidos"}, 422
    articulo = Articulo(titulo=titulo, contenido=contenido, autor=autor)
    db.session.add(articulo)
    db.session.commit()
    return articulo.to_dict(), 201


@app.delete("/autores/<int:autor_id>")
def eliminar_autor(autor_id):
    autor = db.get_or_404(Autor, autor_id)
    db.session.delete(autor)
    db.session.commit()
    return "", 204


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
