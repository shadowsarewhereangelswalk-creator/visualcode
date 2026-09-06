from app import create_app


def test_catalogo():
    cliente = create_app().test_client()
    respuesta = cliente.get("/productos")
    assert respuesta.status_code == 200
    assert respuesta.get_json()["total"] == 3


def test_producto():
    cliente = create_app().test_client()
    assert cliente.get("/productos/1").get_json()["nombre"] == "Teclado"
    assert cliente.get("/productos/99").status_code == 404
