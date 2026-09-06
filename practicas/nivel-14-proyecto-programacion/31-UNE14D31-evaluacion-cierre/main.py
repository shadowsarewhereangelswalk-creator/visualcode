import importlib.util
import json
import os
import tempfile
from pathlib import Path

archivo_temporal = tempfile.NamedTemporaryFile(delete=False)
archivo_temporal.close()
os.environ["DB_PATH"] = archivo_temporal.name

ruta = Path(__file__).resolve().parents[1] / "30-UNE14D30-practica-p5-proyecto-final" / "main.py"
especificacion = importlib.util.spec_from_file_location("proyecto_final", ruta)
proyecto_final = importlib.util.module_from_spec(especificacion)
especificacion.loader.exec_module(proyecto_final)
proyecto_final.inicializar()

pruebas = []

assert proyecto_final.validar_correo("Ana@Ejemplo.com") == "ana@ejemplo.com"
pruebas.append("validación de correo")

assert proyecto_final.clasificar_local("Tengo un error en mi cuenta") == "soporte"
pruebas.append("clasificación de soporte")

assert proyecto_final.clasificar_local("Quiero una cotización") == "ventas"
pruebas.append("clasificación de ventas")

assert proyecto_final.clasificar_local("Hola, necesito información") == "general"
pruebas.append("clasificación general")

cliente = proyecto_final.app.test_client()
respuesta = cliente.post(
    "/api/solicitudes",
    json={"nombre": "Karen", "correo": "karen@ejemplo.com", "mensaje": "Necesito precio del servicio"},
)
assert respuesta.status_code == 201
pruebas.append("creación por API")

listado = cliente.get("/api/solicitudes")
assert listado.status_code == 200
assert len(listado.get_json()) == 1
pruebas.append("persistencia y listado")

salud = cliente.get("/salud")
assert salud.status_code == 200
assert salud.get_json()["estado"] == "ok"
pruebas.append("endpoint de salud")

print(json.dumps({"nivel": 14, "evaluacion_tecnica": "superada", "pruebas": pruebas}, ensure_ascii=False, indent=2))

os.unlink(archivo_temporal.name)
