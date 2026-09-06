from repository import crear_flujo


def test_flujo_git_completo(tmp_path):
    resultado = crear_flujo(tmp_path / "repositorio")
    assert resultado["rama"] == "main"
    assert resultado["historial"][0] == "Integra estado"
    assert resultado["contenido"] == ["versión inicial", "estado validado"]
