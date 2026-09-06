import json

import pytest
from gestor import GestorTareas


@pytest.fixture
def gestor(tmp_path):
    return GestorTareas(tmp_path / "tareas.json")


def test_lista_inicial_vacia(gestor):
    assert gestor.listar() == []


@pytest.mark.parametrize("prioridad", ["baja", "media", "alta"])
def test_crear_por_prioridad(gestor, prioridad):
    tarea = gestor.crear("Aprender pytest", prioridad)
    assert tarea["prioridad"] == prioridad
    assert tarea["id"] == 1


def test_ids_consecutivos(gestor):
    gestor.crear("Primera tarea")
    segunda = gestor.crear("Segunda tarea")
    assert segunda["id"] == 2


def test_persistencia_json(gestor):
    gestor.crear("Guardar archivo")
    datos = json.loads(gestor.ruta.read_text(encoding="utf-8"))
    assert datos[0]["titulo"] == "Guardar archivo"


def test_completar(gestor):
    tarea = gestor.crear("Completar tarea")
    assert gestor.completar(tarea["id"])["completada"] is True


def test_eliminar(gestor):
    tarea = gestor.crear("Eliminar tarea")
    gestor.eliminar(tarea["id"])
    assert gestor.listar() == []


@pytest.mark.parametrize(
    ("titulo", "prioridad"), [("x", "alta"), ("Válida", "urgente")]
)
def test_rechazar_tarea_invalida(gestor, titulo, prioridad):
    with pytest.raises(ValueError):
        gestor.crear(titulo, prioridad)


def test_tarea_inexistente(gestor):
    with pytest.raises(LookupError):
        gestor.completar(99)
