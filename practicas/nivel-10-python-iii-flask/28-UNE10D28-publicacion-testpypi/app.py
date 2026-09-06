import sys
from pathlib import Path


RUTA_SRC = Path(__file__).parent / "src"
sys.path.insert(0, str(RUTA_SRC))

from ai_career_slug import crear_slug


if "--check" in sys.argv:
    assert crear_slug("Python III: Flask") == "python-iii-flask"
    assert (Path(__file__).parent / "pyproject.toml").is_file()
    print("UNE10D28 OK")
    raise SystemExit(0)


from flask import Flask, request


app = Flask(__name__)


@app.get("/")
def inicio():
    texto = request.args.get("texto", "Python III: Flask")
    return {"texto": texto, "slug": crear_slug(texto), "paquete": "ai-career-slug-demo"}


if __name__ == "__main__":
    app.run()
