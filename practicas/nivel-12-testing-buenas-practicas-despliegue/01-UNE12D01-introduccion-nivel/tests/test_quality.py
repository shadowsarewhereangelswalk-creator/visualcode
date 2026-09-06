from src.quality import evaluar_pipeline


def test_pipeline_aprobado():
    resultado = evaluar_pipeline(
        {"tests": True, "lint": True, "format": True, "coverage": True, "build": True}
    )
    assert resultado["listo_para_desplegar"] is True
    assert resultado["aprobadas"] == 5


def test_pipeline_incompleto():
    resultado = evaluar_pipeline({"tests": True, "lint": False})
    assert resultado["listo_para_desplegar"] is False
    assert "lint" in resultado["faltantes"]
