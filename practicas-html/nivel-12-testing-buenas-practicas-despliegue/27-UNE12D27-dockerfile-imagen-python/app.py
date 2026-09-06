import os
import sys

PRACTICA = "UNE12D27"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D27"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from flask import Flask, jsonify

PRODUCTOS = [
    {"id": 1, "nombre": "Teclado", "stock": 8},
    {"id": 2, "nombre": "Mouse", "stock": 12},
    {"id": 3, "nombre": "Monitor", "stock": 4},
]


def create_app():
    application = Flask(__name__)

    @application.get("/")
    def index():
        return jsonify(servicio="inventario", productos=len(PRODUCTOS))

    @application.get("/productos")
    def productos():
        return jsonify(datos=PRODUCTOS, total=len(PRODUCTOS))

    @application.get("/productos/<int:producto_id>")
    def producto(producto_id):
        encontrado = next(
            (item for item in PRODUCTOS if item["id"] == producto_id),
            None,
        )
        if encontrado is None:
            return jsonify(error="Producto no encontrado"), 404
        return jsonify(encontrado)

    @application.get("/health")
    def health():
        return jsonify(status="healthy")

    return application


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8000")),
        debug=False,
    )
