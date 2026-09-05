import pytest

from app import create_app, db


@pytest.fixture()
def app():
    aplicacion = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite://"})
    with aplicacion.app_context():
        db.create_all()
        yield aplicacion
        db.drop_all()


@pytest.fixture()
def cliente(app):
    return app.test_client()


def test_crear_y_obtener_tarea(cliente):
    creada = cliente.post("/api/tareas", json={"titulo": "Probar servicio"})
    assert creada.status_code == 201
    tarea_id = creada.get_json()["id"]
    obtenida = cliente.get(f"/api/tareas/{tarea_id}")
    assert obtenida.status_code == 200
    assert obtenida.get_json()["titulo"] == "Probar servicio"


def test_actualizar_y_filtrar(cliente):
    tarea_id = cliente.post("/api/tareas", json={"titulo": "Documentar API"}).get_json()["id"]
    actualizada = cliente.patch(f"/api/tareas/{tarea_id}", json={"completada": True})
    assert actualizada.status_code == 200
    respuesta = cliente.get("/api/tareas?completada=true").get_json()
    assert respuesta["total"] == 1


def test_validacion_y_eliminacion(cliente):
    assert cliente.post("/api/tareas", json={"titulo": "x"}).status_code == 422
    tarea_id = cliente.post("/api/tareas", json={"titulo": "Eliminar registro"}).get_json()["id"]
    assert cliente.delete(f"/api/tareas/{tarea_id}").status_code == 204
    assert cliente.get(f"/api/tareas/{tarea_id}").status_code == 404
