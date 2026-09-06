from pathlib import Path
for ruta in ["app/templates","app/static/css","app/static/js","tests","data"]:
    Path(ruta).mkdir(parents=True,exist_ok=True)
for archivo in ["app/__init__.py","app/routes.py","tests/test_app.py"]:
    Path(archivo).touch()
print("Arquitectura creada")
