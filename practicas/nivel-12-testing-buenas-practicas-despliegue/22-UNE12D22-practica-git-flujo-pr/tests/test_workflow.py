from workflow import aprobar_y_fusionar, preparar_repositorio, revisar_cambios


def test_flujo_de_rama_y_revision(tmp_path):
    repositorio = preparar_repositorio(tmp_path / "proyecto")
    revision = revisar_cambios(repositorio)
    assert revision["archivos"] == ["test_status.py"]
    assert revision["commits"] == ["Agrega pruebas del servicio"]
    assert aprobar_y_fusionar(repositorio) == "Integra pruebas de estado"
