import sys

PRACTICA = "UNE12D28"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D28"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from config import cargar_configuracion
from flask import Flask, jsonify


def create_app():
    application = Flask(__name__)

    @application.get("/")
    def index():
        return jsonify(cargar_configuracion())

    @application.get("/health")
    def health():
        return jsonify(status="ok")

    return application


app = create_app()


if __name__ == "__main__":
    configuracion = cargar_configuracion()
    app.run(
        host="0.0.0.0",
        port=configuracion["puerto"],
        debug=False,
    )
