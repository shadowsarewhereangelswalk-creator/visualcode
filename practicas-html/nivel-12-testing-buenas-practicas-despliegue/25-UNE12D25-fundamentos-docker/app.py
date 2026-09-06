import os
import sys

PRACTICA = "UNE12D25"


if "--check" in sys.argv:
    assert PRACTICA == "UNE12D25"
    print(f"{PRACTICA} OK")
    raise SystemExit(0)


from flask import Flask, jsonify


def create_app():
    application = Flask(__name__)

    @application.get("/")
    def index():
        return jsonify(
            servicio="fundamentos-docker",
            estado="activo",
            entorno=os.environ.get("APP_ENV", "development"),
        )

    @application.get("/health")
    def health():
        return jsonify(status="ok")

    return application


app = create_app()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", "8000")),
        debug=False,
    )
