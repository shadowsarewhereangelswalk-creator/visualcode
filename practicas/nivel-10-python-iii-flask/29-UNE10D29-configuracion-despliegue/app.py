import sys
from pathlib import Path


ARCHIVOS_DESPLIEGUE = ("wsgi.py", "Procfile", "gunicorn.conf.py", "Dockerfile")


if "--check" in sys.argv:
    raiz = Path(__file__).parent
    assert all((raiz / nombre).is_file() for nombre in ARCHIVOS_DESPLIEGUE)
    print("UNE10D29 OK")
    raise SystemExit(0)


from servicio import create_app


app = create_app("development")


if __name__ == "__main__":
    app.run()
