from career_flask_tools import correo_valido, crear_blueprint_salud, texto_requerido
from flask import Flask


def test_validadores():
    assert correo_valido("ada@example.com")
    assert not correo_valido("correo-invalido")
    assert texto_requerido("  Flask  ") == "Flask"
    assert not texto_requerido("x", minimo=2)


def test_blueprint_salud():
    app = Flask(__name__)
    app.register_blueprint(crear_blueprint_salud("servicio-prueba", "2.0.0"))
    respuesta = app.test_client().get("/salud")
    assert respuesta.status_code == 200
    assert respuesta.get_json() == {"estado": "ok", "servicio": "servicio-prueba", "version": "2.0.0"}
