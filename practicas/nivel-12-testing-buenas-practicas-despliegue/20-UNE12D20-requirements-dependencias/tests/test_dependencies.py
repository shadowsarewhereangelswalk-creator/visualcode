from dependencies import crear_informe, leer_dependencias


def test_leer_dependencias(tmp_path):
    ruta = tmp_path / "requirements.txt"
    ruta.write_text("Flask>=3.1,<4\npytest>=8.4,<10\n", encoding="utf-8")
    informe = crear_informe(leer_dependencias(ruta))
    assert [item["nombre"] for item in informe] == ["Flask", "pytest"]
    assert informe[0]["version"] == "<4,>=3.1"


def test_ignorar_referencia(tmp_path):
    ruta = tmp_path / "requirements.txt"
    ruta.write_text("-r base.txt\npackaging>=24\n", encoding="utf-8")
    assert crear_informe(leer_dependencias(ruta))[0]["nombre"] == "packaging"
