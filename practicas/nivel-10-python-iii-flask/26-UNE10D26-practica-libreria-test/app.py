import sys
from pathlib import Path


RUTA_SRC = Path(__file__).parent / "src"


if "--check" in sys.argv:
    assert (RUTA_SRC / "career_flask_tools" / "__init__.py").is_file()
    assert (Path(__file__).parent / "pyproject.toml").is_file()
    print("UNE10D26 OK")
    raise SystemExit(0)


sys.path.insert(0, str(RUTA_SRC))

from flask import Flask

from career_flask_tools import crear_blueprint_salud


app = Flask(__name__)
app.register_blueprint(crear_blueprint_salud(nombre_servicio="demostracion-libreria", version="1.0.0"))


@app.get("/")
def inicio():
    return {"libreria": "career-flask-tools", "salud": "/salud"}


if __name__ == "__main__":
    app.run()
