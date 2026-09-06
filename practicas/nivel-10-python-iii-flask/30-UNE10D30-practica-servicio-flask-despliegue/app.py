import sys
from pathlib import Path


ARCHIVOS_CLAVE = ("wsgi.py", "Dockerfile", "Procfile", "alembic.ini", "requirements.txt")


if "--check" in sys.argv:
    raiz = Path(__file__).parent
    assert all((raiz / archivo).is_file() for archivo in ARCHIVOS_CLAVE)
    assert (raiz / "servicio" / "models.py").is_file()
    assert (raiz / "tests" / "test_servicio.py").is_file()
    print("UNE10D30 OK")
    raise SystemExit(0)


from servicio import create_app, db


app = create_app("development")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()
