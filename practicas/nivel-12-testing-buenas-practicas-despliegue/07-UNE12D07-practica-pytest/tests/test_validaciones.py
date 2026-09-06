import pytest
from validaciones import calcular_progreso, validar_usuario


@pytest.mark.parametrize(
    ("nombre", "correo", "edad"),
    [
        ("Karen", "karen@example.com", 30),
        ("Luis", "luis@example.org", 18),
        ("María", "maria@example.net", 120),
    ],
)
def test_usuarios_validos(nombre, correo, edad):
    assert validar_usuario(nombre, correo, edad)["valido"] is True


def test_usuario_invalido():
    resultado = validar_usuario("A", "correo", 15)
    assert resultado["errores"] == ["nombre", "correo", "edad"]


def test_progreso_aproximado():
    assert calcular_progreso(1, 3) == pytest.approx(33.333333)


@pytest.mark.parametrize(("completadas", "total"), [(1, 0), (-1, 5), (6, 5)])
def test_progreso_invalido(completadas, total):
    with pytest.raises(ValueError):
        calcular_progreso(completadas, total)
