from webapp import create_app


def test_inicio():
    app = create_app({"TESTING": True, "APP_ENV": "testing"})
    respuesta = app.test_client().get("/")
    assert respuesta.status_code == 200
    assert b"Aplicaci" in respuesta.data


def test_health():
    app = create_app({"TESTING": True, "APP_ENV": "testing", "APP_VERSION": "2.0.0"})
    datos = app.test_client().get("/health").get_json()
    assert datos == {
        "status": "ok",
        "environment": "testing",
        "version": "2.0.0",
    }
