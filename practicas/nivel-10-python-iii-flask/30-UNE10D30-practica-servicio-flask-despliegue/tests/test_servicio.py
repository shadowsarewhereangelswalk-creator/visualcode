import pytest

from servicio import create_app, db


@pytest.fixture()
def app():
    aplicacion = create_app("testing")
    with aplicacion.app_context():
        db.create_all()
        yield aplicacion
        db.drop_all()


@pytest.fixture()
def cliente(app):
    return app.test_client()


def datos_solicitud():
    return {"nombre": "Ada Lovelace", "correo": "ada@example.com", "servicio": "ia", "mensaje": "Necesito automatizar un proceso interno."}


def test_formulario_crea_solicitud(cliente):
    respuesta = cliente.post("/", data=datos_solicitud(), follow_redirects=True)
    assert respuesta.status_code == 200
    assert "Solicitud enviada correctamente" in respuesta.text
    panel = cliente.get("/solicitudes")
    assert "Ada Lovelace" in panel.text


def test_formulario_valida_campos(cliente):
    respuesta = cliente.post("/", data={})
    assert respuesta.status_code == 200
    assert "Selecciona un servicio" in respuesta.text


def test_ciclo_api(cliente):
    creada = cliente.post("/api/solicitudes", json=datos_solicitud())
    assert creada.status_code == 201
    solicitud_id = creada.get_json()["id"]
    actualizada = cliente.patch(f"/api/solicitudes/{solicitud_id}", json={"estado": "contactada"})
    assert actualizada.get_json()["estado"] == "contactada"
    listado = cliente.get("/api/solicitudes?estado=contactada").get_json()
    assert listado["total"] == 1
    assert cliente.delete(f"/api/solicitudes/{solicitud_id}").status_code == 204


def test_salud(cliente):
    assert cliente.get("/salud").get_json()["estado"] == "ok"
