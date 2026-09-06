import pytest


@pytest.fixture
def usuario_activo():
    return {"correo": "estudiante@example.com", "activo": True}
