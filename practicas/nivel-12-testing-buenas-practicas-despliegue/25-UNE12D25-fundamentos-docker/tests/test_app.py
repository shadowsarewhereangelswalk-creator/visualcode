from app import create_app


def test_inicio():
    cliente = create_app().test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert respuesta.get_json()["estado"] == "activo"


def test_health():
    respuesta = create_app().test_client().get("/health")
    assert respuesta.get_json() == {"status": "ok"}
