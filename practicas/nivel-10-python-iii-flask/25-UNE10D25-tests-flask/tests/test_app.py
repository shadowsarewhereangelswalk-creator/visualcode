import pytest

from app import calcular, create_app


@pytest.fixture()
def app():
    return create_app({"TESTING": True, "API_KEY": "prueba-secreta"})


@pytest.fixture()
def cliente(app):
    return app.test_client()


def test_calcular_funcion():
    assert calcular("multiplicar", 6, 7) == 42
    with pytest.raises(ValueError):
        calcular("dividir", 3, 0)


def test_salud(cliente):
    respuesta = cliente.get("/salud")
    assert respuesta.status_code == 200
    assert respuesta.get_json() == {"estado": "ok"}


def test_requiere_api_key(cliente):
    respuesta = cliente.post("/api/calcular", json={"operacion": "sumar", "a": 2, "b": 3})
    assert respuesta.status_code == 401


def test_suma_autorizada(cliente):
    respuesta = cliente.post(
        "/api/calcular",
        json={"operacion": "sumar", "a": 2, "b": 3},
        headers={"X-API-Key": "prueba-secreta"},
    )
    assert respuesta.status_code == 200
    assert respuesta.get_json()["resultado"] == 5


@pytest.mark.parametrize("datos", [{}, {"operacion": "sumar", "a": "2", "b": 3}, {"operacion": "dividir", "a": 2, "b": 0}])
def test_datos_invalidos(cliente, datos):
    respuesta = cliente.post("/api/calcular", json=datos, headers={"X-API-Key": "prueba-secreta"})
    assert respuesta.status_code == 422
