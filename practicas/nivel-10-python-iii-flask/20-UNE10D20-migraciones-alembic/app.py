import os
import sys
from decimal import Decimal, InvalidOperation


def convertir_precio(valor):
    try:
        precio = Decimal(str(valor)).quantize(Decimal("0.01"))
    except (InvalidOperation, ValueError):
        return None
    return precio if precio >= 0 else None


if "--check" in sys.argv:
    assert convertir_precio("19.9") == Decimal("19.90")
    assert convertir_precio("incorrecto") is None
    assert convertir_precio(-1) is None
    print("UNE10D20 OK")
    raise SystemExit(0)


from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, Numeric, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)
migrate = Migrate()


class Producto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), unique=True)
    precio: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    stock: Mapped[int] = mapped_column(Integer, default=0)

    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "precio": str(self.precio), "stock": self.stock}


def create_app():
    aplicacion = Flask(__name__)
    aplicacion.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL", "sqlite:///inventario.db"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )
    db.init_app(aplicacion)
    migrate.init_app(aplicacion, db)

    @aplicacion.get("/")
    def inicio():
        return {"servicio": "Inventario", "migracion_actual": "20270420_02"}

    @aplicacion.get("/productos")
    def listar_productos():
        productos = db.session.execute(db.select(Producto).order_by(Producto.nombre)).scalars().all()
        return {"productos": [producto.to_dict() for producto in productos]}

    @aplicacion.post("/productos")
    def crear_producto():
        datos = request.get_json(silent=True) or {}
        nombre = str(datos.get("nombre", "")).strip()
        precio = convertir_precio(datos.get("precio"))
        stock = datos.get("stock", 0)
        if not 2 <= len(nombre) <= 100 or precio is None or not isinstance(stock, int) or stock < 0:
            return {"error": "Los datos del producto no son válidos"}, 422
        if db.session.scalar(db.select(Producto).where(Producto.nombre == nombre)):
            return {"error": "El producto ya existe"}, 409
        producto = Producto(nombre=nombre, precio=precio, stock=stock)
        db.session.add(producto)
        db.session.commit()
        return producto.to_dict(), 201

    return aplicacion


app = create_app()


if __name__ == "__main__":
    app.run()
