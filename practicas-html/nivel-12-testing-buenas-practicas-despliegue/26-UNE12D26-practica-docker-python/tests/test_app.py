import pytest
from app import create_app


@pytest.fixture
def cliente():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_crud_tareas(cliente):
    creada = cliente.post("/tareas", json={"titulo": "Construir imagen"})
    assert creada.status_code == 201
    tarea_id = creada.get_json()["id"]
    actualizada = cliente.patch(f"/tareas/{tarea_id}", json={"completada": True})
    assert actualizada.get_json()["completada"] is True
    listado = cliente.get("/tareas").get_json()
    assert listado["total"] == 1


def test_validacion(cliente):
    respuesta = cliente.post("/tareas", json={"titulo": "x"})
    assert respuesta.status_code == 422


def test_health(cliente):
    assert cliente.get("/health").status_code == 200
